#!/usr/bin/env python3
"""Batch-resolve paper ids to metadata + citation counts, writing JSONL.

Primary source is the Semantic Scholar batch endpoint (<= 500 ids per POST,
exponential backoff on 429). `--source openalex` resolves through OpenAlex
instead (DOI-filter batches; arXiv ids are mapped to their 10.48550 DOIs).

Input ids may be bare arXiv ids (2406.09246), ARXIV:/arXiv: prefixed, DOIs,
DOI: prefixed, arxiv.org/doi.org URLs, 40-hex S2 paper ids, or CorpusId:N.

Examples:
    python resolve_ids.py --ids-file ids.txt --out resolved.jsonl
    python resolve_ids.py --jsonl sweep.jsonl --id-field id --source openalex

Output: one JSON object per input id —
    input_id, source, found, title, year, publication_date, venue,
    citation_count, external_ids, open_access_pdf, authors

Reads S2_API_KEY / OPENALEX_API_KEY / SOTA_MAILTO from the environment or from
~/.config/find-sota-papers/config.json (see `install.py --configure-keys`).
Stdlib only.
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

S2_BATCH = "https://api.semanticscholar.org/graph/v1/paper/batch"
S2_FIELDS = "title,year,publicationDate,venue,citationCount,externalIds,openAccessPdf,authors"
OPENALEX_WORKS = "https://api.openalex.org/works"
OPENALEX_SELECT = "id,doi,display_name,publication_year,publication_date,cited_by_count,ids,primary_location,open_access,authorships"
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


def normalize(raw):
    """Return (s2_id, doi) for one input token; either element may be None."""
    token = raw.strip()
    if not token:
        return None, None
    match = re.search(r"arxiv\.org/(?:abs|pdf|html)/([0-9]{4}\.[0-9]{4,5})", token, re.I)
    if match:
        return "ARXIV:" + match.group(1), "10.48550/arXiv." + match.group(1)
    match = re.search(r"doi\.org/(10\..+)$", token, re.I)
    if match:
        return "DOI:" + match.group(1), match.group(1)
    match = re.match(r"(?:arxiv:)\s*([0-9]{4}\.[0-9]{4,5})(v[0-9]+)?$", token, re.I)
    if match:
        return "ARXIV:" + match.group(1), "10.48550/arXiv." + match.group(1)
    match = re.match(r"([0-9]{4}\.[0-9]{4,5})(v[0-9]+)?$", token)
    if match:
        return "ARXIV:" + match.group(1), "10.48550/arXiv." + match.group(1)
    match = re.match(r"(?:doi:)?\s*(10\..+)$", token, re.I)
    if match:
        return "DOI:" + match.group(1), match.group(1)
    if re.match(r"^[0-9a-f]{40}$", token, re.I):
        return token.lower(), None
    if re.match(r"^CorpusId:[0-9]+$", token, re.I):
        return token, None
    print("  skipping unrecognized id: {!r}".format(token), file=sys.stderr)
    return None, None


def http_json(url, data=None, headers=None, max_tries=6):
    delay = 5.0
    payload = json.dumps(data).encode("utf-8") if data is not None else None
    for attempt in range(1, max_tries + 1):
        try:
            request = urllib.request.Request(url, data=payload, headers=headers or {})
            if payload is not None:
                request.add_header("Content-Type", "application/json")
            with urllib.request.urlopen(request, timeout=90) as response:
                return json.loads(response.read().decode("utf-8"))
        except urllib.error.HTTPError as exc:
            if exc.code in (429, 500, 502, 503, 504) and attempt < max_tries:
                retry_after = exc.headers.get("Retry-After")
                wait = float(retry_after) if retry_after else delay
                print(
                    "  HTTP {}, retry {}/{} in {:.0f}s".format(
                        exc.code, attempt, max_tries, wait
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
                    "  network error ({}), retry {}/{} in {:.0f}s".format(
                        exc, attempt, max_tries, delay
                    ),
                    file=sys.stderr,
                )
                time.sleep(delay)
                delay *= 2
                continue
            raise
    raise RuntimeError("unreachable")


def resolve_s2(ids, config, delay):
    headers = {"User-Agent": "find-sota-papers/resolve_ids"}
    if config.get("s2_api_key"):
        headers["x-api-key"] = config["s2_api_key"]
    url = "{}?fields={}".format(S2_BATCH, S2_FIELDS)
    for offset in range(0, len(ids), 500):
        batch = ids[offset : offset + 500]
        results = http_json(url, data={"ids": [s2 for s2, _ in batch]}, headers=headers)
        for (input_id, _), paper in zip(batch, results):
            if not paper:
                yield {"input_id": input_id, "source": "s2", "found": False}
                continue
            open_access = paper.get("openAccessPdf") or {}
            yield {
                "input_id": input_id,
                "source": "s2",
                "found": True,
                "paper_id": paper.get("paperId"),
                "title": paper.get("title"),
                "year": paper.get("year"),
                "publication_date": paper.get("publicationDate"),
                "venue": paper.get("venue"),
                "citation_count": paper.get("citationCount"),
                "external_ids": paper.get("externalIds"),
                "open_access_pdf": open_access.get("url"),
                "authors": [a.get("name") for a in paper.get("authors") or []],
            }
        if offset + 500 < len(ids):
            time.sleep(delay)


def resolve_openalex(ids, config, delay):
    with_doi = [(input_id, doi) for input_id, doi in ids if doi]
    for input_id, doi in ids:
        if not doi:
            yield {
                "input_id": input_id,
                "source": "openalex",
                "found": False,
                "note": "no DOI mapping for this id form",
            }
    for offset in range(0, len(with_doi), 50):
        batch = with_doi[offset : offset + 50]
        params = {
            "filter": "doi:" + "|".join(doi for _, doi in batch),
            "per_page": len(batch),
            "select": OPENALEX_SELECT,
        }
        if config.get("openalex_api_key"):
            params["api_key"] = config["openalex_api_key"]
        if config.get("mailto"):
            params["mailto"] = config["mailto"]
        url = "{}?{}".format(OPENALEX_WORKS, urllib.parse.urlencode(params))
        response = http_json(url, headers={"User-Agent": "find-sota-papers/resolve_ids"})
        by_doi = {}
        for work in response.get("results", []):
            work_doi = (work.get("doi") or "").replace("https://doi.org/", "").lower()
            by_doi[work_doi] = work
        for input_id, doi in batch:
            work = by_doi.get(doi.lower())
            if not work:
                yield {"input_id": input_id, "source": "openalex", "found": False}
                continue
            location = work.get("primary_location") or {}
            source = location.get("source") or {}
            open_access = work.get("open_access") or {}
            yield {
                "input_id": input_id,
                "source": "openalex",
                "found": True,
                "paper_id": work.get("id"),
                "title": work.get("display_name"),
                "year": work.get("publication_year"),
                "publication_date": work.get("publication_date"),
                "venue": source.get("display_name"),
                "citation_count": work.get("cited_by_count"),
                "external_ids": work.get("ids"),
                "open_access_pdf": open_access.get("oa_url"),
                "authors": [
                    (a.get("author") or {}).get("display_name")
                    for a in work.get("authorships") or []
                ],
            }
        if offset + 50 < len(with_doi):
            time.sleep(delay)


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--ids-file", help="file with one id per line")
    parser.add_argument("--jsonl", help="JSONL file to draw ids from")
    parser.add_argument("--id-field", default="id", help="field in --jsonl (default: id)")
    parser.add_argument("--out", help="output JSONL path (default: stdout)")
    parser.add_argument(
        "--source", choices=["s2", "openalex"], default="s2", help="default: s2"
    )
    parser.add_argument(
        "--delay", type=float, default=3.0, help="seconds between batches (default 3)"
    )
    args = parser.parse_args()

    raw_ids = []
    if args.ids_file:
        with open(args.ids_file, "r", encoding="utf-8") as handle:
            raw_ids.extend(line for line in handle if line.strip())
    if args.jsonl:
        with open(args.jsonl, "r", encoding="utf-8") as handle:
            for line in handle:
                line = line.strip()
                if line:
                    value = json.loads(line).get(args.id_field)
                    if value:
                        raw_ids.append(str(value))
    if not raw_ids:
        sys.exit("error: no ids — give --ids-file and/or --jsonl")

    seen, ids = set(), []
    for raw in raw_ids:
        s2_id, doi = normalize(raw)
        if s2_id and s2_id not in seen:
            seen.add(s2_id)
            ids.append((s2_id, doi))

    config = load_config()
    resolver = resolve_s2 if args.source == "s2" else resolve_openalex
    sink = open(args.out, "w", encoding="utf-8") if args.out else sys.stdout
    found = total = 0
    try:
        for record in resolver(ids, config, args.delay):
            sink.write(json.dumps(record, ensure_ascii=False) + "\n")
            total += 1
            found += 1 if record.get("found") else 0
        sink.flush()
    finally:
        if args.out:
            sink.close()

    print(
        "done: {}/{} resolved via {} ({} unique ids in)".format(
            found, total, args.source, len(ids)
        ),
        file=sys.stderr,
    )


if __name__ == "__main__":
    main()
