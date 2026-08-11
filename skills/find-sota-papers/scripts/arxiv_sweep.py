#!/usr/bin/env python3
"""Politely walk an arXiv API query x date window to exhaustion, writing JSONL.

One invocation replaces the dozens of hand-issued page fetches an exhaustive
category sweep otherwise needs, and keeps arXiv's politeness rules (one
connection, >= 3 s between requests, exponential backoff on 429/5xx).

Examples:
    python arxiv_sweep.py --query 'cat:cs.RO AND abs:"agentic"' \
        --from 2026-03-01 --to 2026-08-11 --out sweep.jsonl
    python arxiv_sweep.py --category cs.RO --category cs.AI \
        --from 2026-07-01 --to 2026-08-01 --out ro.jsonl --max-results 5000

Output: one JSON object per line —
    id (versionless), version, title, authors, summary, published, updated,
    primary_category, categories, abs_url, pdf_url, doi, comment, journal_ref

Resume: rerunning with the same query/window and --out continues from the line
count of the existing file and skips ids already written. Stdlib only.
"""

import argparse
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

API = "https://export.arxiv.org/api/query"
ATOM = "{http://www.w3.org/2005/Atom}"
ARXIV = "{http://arxiv.org/schemas/atom}"
OPENSEARCH = "{http://a9.com/-/spec/opensearch/1.1/}"
CONFIG_PATH = os.environ.get(
    "FIND_SOTA_PAPERS_CONFIG",
    os.path.join(os.path.expanduser("~"), ".config", "find-sota-papers", "config.json"),
)


def load_config():
    """Env vars win; the dotfile written by `install.py --configure-keys` backs them."""
    config = {}
    try:
        with open(CONFIG_PATH, "r", encoding="utf-8") as handle:
            loaded = json.load(handle)
        if isinstance(loaded, dict):
            config.update(loaded)
    except (OSError, ValueError):
        pass
    for env, key in (
        ("S2_API_KEY", "s2_api_key"),
        ("OPENALEX_API_KEY", "openalex_api_key"),
        ("SOTA_MAILTO", "mailto"),
        ("CROSSREF_MAILTO", "mailto"),
    ):
        if os.environ.get(env):
            config[key] = os.environ[env]
    return config


def normalize_stamp(value, is_end):
    """Accept YYYY-MM-DD or YYYYMMDDHHMM; return arXiv's YYYYMMDDHHMM."""
    digits = re.sub(r"[^0-9]", "", value)
    if len(digits) == 8:
        return digits + ("2359" if is_end else "0000")
    if len(digits) == 12:
        return digits
    sys.exit("error: bad date {!r} — use YYYY-MM-DD or YYYYMMDDHHMM".format(value))


def build_query(args):
    parts = []
    if args.query:
        parts.append("({})".format(args.query))
    if args.category:
        cats = " OR ".join("cat:{}".format(c) for c in args.category)
        parts.append("({})".format(cats))
    if args.date_from or args.date_to:
        start = normalize_stamp(args.date_from or "1991-01-01", False)
        end = normalize_stamp(args.date_to or "2100-01-01", True)
        parts.append("submittedDate:[{} TO {}]".format(start, end))
    if not parts:
        sys.exit("error: give --query and/or --category (optionally with --from/--to)")
    return " AND ".join(parts)


def fetch_page(query, start, page_size, user_agent, max_tries=6):
    params = urllib.parse.urlencode(
        {
            "search_query": query,
            "start": start,
            "max_results": page_size,
            "sortBy": "submittedDate",
            "sortOrder": "descending",
        }
    )
    url = "{}?{}".format(API, params)
    delay = 5.0
    for attempt in range(1, max_tries + 1):
        try:
            request = urllib.request.Request(url, headers={"User-Agent": user_agent})
            with urllib.request.urlopen(request, timeout=60) as response:
                return response.read()
        except urllib.error.HTTPError as exc:
            if exc.code in (429, 500, 502, 503, 504) and attempt < max_tries:
                retry_after = exc.headers.get("Retry-After")
                wait = float(retry_after) if retry_after else delay
                print(
                    "  HTTP {} at start={}, retry {}/{} in {:.0f}s".format(
                        exc.code, start, attempt, max_tries, wait
                    ),
                    file=sys.stderr,
                )
                time.sleep(wait)
                delay *= 2
                continue
            raise
        except (urllib.error.URLError, TimeoutError) as exc:
            if attempt < max_tries:
                print(
                    "  network error at start={} ({}), retry {}/{} in {:.0f}s".format(
                        start, exc, attempt, max_tries, delay
                    ),
                    file=sys.stderr,
                )
                time.sleep(delay)
                delay *= 2
                continue
            raise
    raise RuntimeError("unreachable")


def parse_page(payload):
    """Return (total_results, [entry dicts]). Raises on non-Atom payloads."""
    root = ET.fromstring(payload)
    total_text = root.findtext(OPENSEARCH + "totalResults")
    total = int(total_text) if total_text and total_text.isdigit() else None
    entries = []
    for entry in root.findall(ATOM + "entry"):
        raw_id = entry.findtext(ATOM + "id") or ""
        match = re.search(r"abs/([^/]+?)(v(\d+))?$", raw_id)
        if not match:
            continue  # the API returns one error pseudo-entry for bad queries
        versionless = match.group(1)
        pdf_url = None
        for link in entry.findall(ATOM + "link"):
            if link.get("title") == "pdf":
                pdf_url = link.get("href")
        primary = entry.find(ARXIV + "primary_category")
        entries.append(
            {
                "id": versionless,
                "version": int(match.group(3)) if match.group(3) else None,
                "title": " ".join((entry.findtext(ATOM + "title") or "").split()),
                "authors": [
                    author.findtext(ATOM + "name")
                    for author in entry.findall(ATOM + "author")
                ],
                "summary": " ".join((entry.findtext(ATOM + "summary") or "").split()),
                "published": entry.findtext(ATOM + "published"),
                "updated": entry.findtext(ATOM + "updated"),
                "primary_category": primary.get("term") if primary is not None else None,
                "categories": [c.get("term") for c in entry.findall(ATOM + "category")],
                "abs_url": "https://arxiv.org/abs/{}".format(versionless),
                "pdf_url": pdf_url,
                "doi": entry.findtext(ARXIV + "doi"),
                "comment": entry.findtext(ARXIV + "comment"),
                "journal_ref": entry.findtext(ARXIV + "journal_ref"),
            }
        )
    return total, entries


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--query", help="raw arXiv search_query expression")
    parser.add_argument(
        "--category", action="append", help="arXiv category (repeatable, OR-joined)"
    )
    parser.add_argument("--from", dest="date_from", help="window start (YYYY-MM-DD)")
    parser.add_argument("--to", dest="date_to", help="window end (YYYY-MM-DD)")
    parser.add_argument("--out", help="output JSONL path (default: stdout)")
    parser.add_argument("--page-size", type=int, default=100, help="<= 2000; default 100")
    parser.add_argument(
        "--delay", type=float, default=3.0, help="seconds between requests (default 3)"
    )
    parser.add_argument(
        "--max-results", type=int, default=0, help="stop after N records (0 = all)"
    )
    parser.add_argument(
        "--no-resume",
        action="store_true",
        help="ignore an existing --out file instead of continuing it",
    )
    args = parser.parse_args()

    if not 1 <= args.page_size <= 2000:
        sys.exit("error: --page-size must be 1..2000")

    query = build_query(args)
    mailto = load_config().get("mailto")
    user_agent = "find-sota-papers/arxiv_sweep" + (
        " (mailto:{})".format(mailto) if mailto else ""
    )

    seen, start = set(), 0
    if args.out and os.path.exists(args.out) and not args.no_resume:
        with open(args.out, "r", encoding="utf-8") as handle:
            for line in handle:
                line = line.strip()
                if line:
                    try:
                        seen.add(json.loads(line)["id"])
                    except (ValueError, KeyError):
                        pass
        start = len(seen)
        if start:
            print(
                "resuming: {} records already in {} (same query/window assumed)".format(
                    start, args.out
                ),
                file=sys.stderr,
            )

    sink = open(args.out, "a", encoding="utf-8") if args.out else sys.stdout
    written = pages = 0
    total = None
    empty_retries = 0
    try:
        while True:
            payload = fetch_page(query, start, args.page_size, user_agent)
            page_total, entries = parse_page(payload)
            total = page_total if page_total is not None else total
            pages += 1

            if not entries:
                # arXiv sometimes returns a valid-but-empty page mid-pagination.
                if total is not None and start < total and empty_retries < 3:
                    empty_retries += 1
                    print(
                        "  empty page at start={} with totalResults={}, retry {}/3".format(
                            start, total, empty_retries
                        ),
                        file=sys.stderr,
                    )
                    time.sleep(args.delay * 2)
                    continue
                break
            empty_retries = 0

            for record in entries:
                if record["id"] in seen:
                    continue
                seen.add(record["id"])
                sink.write(json.dumps(record, ensure_ascii=False) + "\n")
                written += 1
                if args.max_results and written >= args.max_results:
                    break
            sink.flush()

            start += len(entries)
            if args.max_results and written >= args.max_results:
                break
            if total is not None and start >= total:
                break
            time.sleep(args.delay)
    finally:
        if args.out:
            sink.close()

    print(
        "done: {} new records ({} total unique) over {} pages; totalResults={}".format(
            written, len(seen), pages, total if total is not None else "unknown"
        ),
        file=sys.stderr,
    )


if __name__ == "__main__":
    main()
