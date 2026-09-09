#!/usr/bin/env python3
"""Detect drift in the external sources this collection depends on.

WHAT THIS DOES AND DOES NOT DO, because the boundary is the whole design.

It detects. It never judges. It does not edit a claim, move a tier, open a pull
request, or update a stored hash. Its output is a report that becomes the input
to REFRESH.md, which a human runs.

The reason is recorded as error 27 and the four errors before it: this
collection has repeatedly turned "could not reach" into "not there", and a CI
runner is a MORE network-restricted environment than a browser, not a less
restricted one. Automating the adjudication would put this project's most
repeated failure cause on a cron schedule.

So every source lands in exactly one of three states:

    unchanged     fetched, and it matches what was recorded
    changed       fetched, and it does not match. A human adjudicates.
    unreachable   NOT FETCHED. Not evidence of anything.

`unreachable` is never merged into `unchanged`. A run where half the sources
were unreachable is not a clean run, and the report says so at the top.
"""

import argparse
import hashlib
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TIMEOUT = 30
UA = "dev-conventions-source-watch/1 (+https://github.com/natanaelfejes/dev-conventions)"

UNCHANGED, CHANGED, UNREACHABLE = "unchanged", "changed", "unreachable"


def fetch(url, accept=None):
    """Return (text, None) or (None, reason). A reason is never a finding."""
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    if accept:
        req.add_header("Accept", accept)
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
            return r.read().decode("utf-8", "replace"), None
    except urllib.error.HTTPError as e:
        return None, f"HTTP {e.code}"
    except urllib.error.URLError as e:
        return None, f"unreachable: {e.reason}"
    except Exception as e:                      # noqa: BLE001 - report, never raise
        return None, f"{type(e).__name__}: {e}"


def normalise(html):
    """Text only, whitespace collapsed. Nav and boilerplate still move, which is
    why a change is reported for a human to read rather than acted on."""
    t = re.sub(r"<script.*?</script>|<style.*?</style>", " ", html, flags=re.S | re.I)
    t = re.sub(r"<[^>]+>", " ", t)
    return re.sub(r"\s+", " ", t).strip()


# --------------------------------------------------------------------------
# The four jobs. Each returns (rows, unreachable) and neither list absorbs the
# other.
# --------------------------------------------------------------------------

def job_page_drift(sources):
    rows, unreachable = [], []
    for entry in sources.get("vendor_doc", []):
        url = entry["url"]
        body, reason = fetch(url)
        if body is None:
            unreachable.append((url, reason, entry.get("claims", [])))
            continue
        digest = hashlib.sha256(normalise(body).encode()).hexdigest()
        stored = (entry.get("content_hash") or "").strip()
        if not stored:
            rows.append((CHANGED, url, "no hash recorded, run --seed", entry.get("claims", [])))
        elif digest == stored:
            rows.append((UNCHANGED, url, f"{digest[:12]}", entry.get("claims", [])))
        else:
            rows.append((CHANGED, url, f"{stored[:12]} -> {digest[:12]}", entry.get("claims", [])))
    return rows, unreachable


def job_venue_records(sources):
    """Crossref is content-negotiation friendly and works from CI. The assertion
    is that the DOI still resolves AND still returns the title this collection
    cites. A DOI that resolves to a different paper is the failure that error 20
    exists for."""
    rows, unreachable = [], []
    for entry in sources.get("venue_record", []):
        doi = entry["doi"]
        url = f"https://api.crossref.org/works/{urllib.parse.quote(doi)}"
        body, reason = fetch(url, accept="application/json")
        if body is None:
            unreachable.append((doi, reason, entry.get("claims", [])))
            continue
        try:
            titles = json.loads(body)["message"].get("title") or [""]
            title = titles[0]
        except Exception as e:                  # noqa: BLE001
            unreachable.append((doi, f"unparseable response: {e}", entry.get("claims", [])))
            continue
        want = (entry.get("title_contains") or "").strip()
        if not want:
            rows.append((UNCHANGED, doi, f"resolves: {title[:60]}", entry.get("claims", [])))
        elif want.lower() in title.lower():
            rows.append((UNCHANGED, doi, f"title matches: {title[:60]}", entry.get("claims", [])))
        else:
            rows.append((CHANGED, doi, f"expected {want!r}, got {title[:60]!r}", entry.get("claims", [])))
    return rows, unreachable


def job_gap_surveillance(sources, since_days=35):
    """The arXiv API, not the HTML site, which blocks runners. Reports candidates
    for a human to read. It does not decide whether a paper closes a gap."""
    rows, unreachable = [], []
    for entry in sources.get("gap_query", []):
        for term in entry.get("terms", []):
            q = urllib.parse.urlencode({
                "search_query": f"all:{term}",
                "sortBy": "submittedDate",
                "sortOrder": "descending",
                "max_results": "10",
            })
            body, reason = fetch(f"http://export.arxiv.org/api/query?{q}")
            if body is None:
                unreachable.append((f"gap {entry['gap']}: {term}", reason, [entry.get("label", "")]))
                continue
            hits = []
            for m in re.finditer(r"<entry>(.*?)</entry>", body, re.S):
                blk = m.group(1)
                pub = re.search(r"<published>(.*?)</published>", blk)
                ttl = re.search(r"<title>(.*?)</title>", blk, re.S)
                idm = re.search(r"<id>(.*?)</id>", blk)
                if not (pub and ttl and idm):
                    continue
                age = (datetime.now(timezone.utc)
                       - datetime.fromisoformat(pub.group(1).replace("Z", "+00:00"))).days
                if age <= since_days:
                    hits.append(f"{idm.group(1).rsplit('/', 1)[-1]}  {' '.join(ttl.group(1).split())[:80]}")
            state = CHANGED if hits else UNCHANGED
            detail = "; ".join(hits) if hits else f"no submissions in {since_days} days"
            rows.append((state, f"gap {entry['gap']}: {term}", detail, [entry.get("label", "")]))
    return rows, unreachable


def job_comparables(sources):
    """Recorded with a timestamp rather than a date. A star count moved 524 in
    hours on 2026-09-09, which is why."""
    rows, unreachable = [], []
    token = os.environ.get("GITHUB_TOKEN", "")
    for entry in sources.get("comparable", []):
        repo = entry["repo"]
        req = urllib.request.Request(
            f"https://api.github.com/repos/{repo}",
            headers={"User-Agent": UA, "Accept": "application/vnd.github+json",
                     **({"Authorization": f"Bearer {token}"} if token else {})})
        try:
            with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
                d = json.loads(r.read().decode())
        except Exception as e:                  # noqa: BLE001
            unreachable.append((repo, f"{type(e).__name__}: {e}", [entry.get("note", "")]))
            continue
        rows.append((UNCHANGED, repo,
                     f"{d.get('stargazers_count'):,} stars, pushed {d.get('pushed_at')}",
                     [entry.get("note", "")]))
    return rows, unreachable


# --------------------------------------------------------------------------

def render(results, unreachable_all, total):
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    n_unreach = len(unreachable_all)
    out = [f"# Source drift report, {now}", ""]

    if n_unreach:
        out += [f"> **{n_unreach} of {total} sources were NOT REACHED.** Their state is unknown, "
                f"not unchanged. Read the unreachable section before acting on anything below.", ""]
    else:
        out += [f"> All {total} sources were reached.", ""]

    for title, rows in results:
        changed = [r for r in rows if r[0] == CHANGED]
        out += [f"## {title}", "",
                f"{len(rows)} checked, **{len(changed)} changed**, "
                f"{len(rows) - len(changed)} unchanged.", ""]
        if changed:
            for _, what, detail, claims in changed:
                out.append(f"- **{what}**  {detail}")
                for c in claims:
                    if c:
                        out.append(f"    - at risk: {c}")
        else:
            out.append("No change detected in any source this job could reach.")
        out.append("")

    out += ["## Not reached", ""]
    if unreachable_all:
        out.append("**Not a finding. Not evidence of absence.** Open these by hand.")
        out.append("")
        for what, reason, claims in unreachable_all:
            out.append(f"- **{what}**  {reason}")
            for c in claims:
                if c:
                    out.append(f"    - claim depending on it: {c}")
    else:
        out.append("Every source was reached.")
    out += ["", "---", "",
            "This job **detects**. It does not adjudicate, edit a claim, move a tier, or open a "
            "pull request. Feed it to `REFRESH.md`. A changed page is a question, not a defect, "
            "and an unreachable one is neither."]
    return "\n".join(out)


def load_sources(path):
    import yaml
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def seed(path, data):
    """Fill empty content_hash values. A human runs this deliberately; CI never
    does, because a job that updates its own baseline can never report drift."""
    text = path.read_text(encoding="utf-8")
    for entry in data.get("vendor_doc", []):
        if (entry.get("content_hash") or "").strip():
            continue
        body, reason = fetch(entry["url"])
        if body is None:
            print(f"  SKIP  {entry['url']}  {reason}")
            continue
        digest = hashlib.sha256(normalise(body).encode()).hexdigest()
        text = text.replace(f'  - url: {entry["url"]}', f'  - url: {entry["url"]}', 1)
        # replace the first empty hash following this url
        i = text.index(entry["url"])
        j = text.index('content_hash: ""', i)
        text = text[:j] + f'content_hash: "{digest}"' + text[j + len('content_hash: ""'):]
        print(f"  seeded {entry['url']}  {digest[:12]}")
    path.write_text(text, encoding="utf-8")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--seed", action="store_true", help="fill empty content hashes, run by a human")
    ap.add_argument("--out", default="", help="write the report here as well as stdout")
    ap.add_argument("--sources", default=str(ROOT / "sources.yml"))
    args = ap.parse_args()

    path = Path(args.sources)
    data = load_sources(path)

    if args.seed:
        seed(path, data)
        return 0

    jobs = [("Page drift, vendor documentation", job_page_drift),
            ("Venue records", job_venue_records),
            ("Gap surveillance", job_gap_surveillance),
            ("Comparables", job_comparables)]
    results, unreachable_all, total = [], [], 0
    for title, fn in jobs:
        rows, unreach = fn(data)
        results.append((title, rows))
        unreachable_all += unreach
        total += len(rows) + len(unreach)

    report = render(results, unreachable_all, total)
    print(report)
    if args.out:
        Path(args.out).write_text(report, encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
