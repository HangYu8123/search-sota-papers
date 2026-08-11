# Bundled helper scripts

Optional-capability helpers for harnesses that can execute Python 3 (any CLI
harness). Both are stdlib-only, keep the polite-client rules from
`references/sources.md` automatically, and handle 429/5xx with exponential
backoff so rate limiting stays out of the agent loop. Their output is **only
candidate leads** — every paper still passes the skill's normal validation.

## `arxiv_sweep.py` — exhaustive arXiv enumeration

Walks a `search_query` × `submittedDate` window to exhaustion (paginated,
3 s between requests, resumable) and writes one JSON line per paper.

```bash
python arxiv_sweep.py --query 'cat:cs.RO AND abs:"agentic"' \
    --from 2026-03-01 --to 2026-08-11 --out sweep.jsonl
python arxiv_sweep.py --category cs.RO --category cs.AI \
    --from 2026-07-01 --to 2026-08-01 --out ro.jsonl --max-results 5000
```

| Flag | Meaning |
|---|---|
| `--query` | raw arXiv `search_query` expression |
| `--category` | arXiv category; repeatable, OR-joined; AND-combined with `--query` |
| `--from` / `--to` | submittedDate window, `YYYY-MM-DD` (or raw `YYYYMMDDHHMM`) |
| `--out` | JSONL path (default stdout); rerun to resume, `--no-resume` to ignore |
| `--page-size` | results per request, ≤ 2000 (default 100) |
| `--delay` | seconds between requests (default 3) |
| `--max-results` | stop after N records (default 0 = the whole window) |

Output fields: `id` (versionless), `version`, `title`, `authors`, `summary`,
`published`, `updated`, `primary_category`, `categories`, `abs_url`, `pdf_url`,
`doi`, `comment`, `journal_ref`.

Resume assumes the same query and window; it continues from the existing file's
line count and skips ids already written.

## `resolve_ids.py` — batch metadata / citation resolution

arXiv ids or DOIs in, one JSON line per paper out. Primary source is the
Semantic Scholar batch endpoint (≤ 500 ids per POST); `--source openalex`
resolves through OpenAlex instead (DOI-filter batches of 50; arXiv ids are
mapped to their `10.48550/arXiv.*` DOIs).

```bash
python resolve_ids.py --ids-file ids.txt --out resolved.jsonl
python resolve_ids.py --jsonl sweep.jsonl --id-field id --source openalex
```

| Flag | Meaning |
|---|---|
| `--ids-file` | one id per line: `2406.09246`, `arXiv:…`, `10.x/…`, `DOI:…`, arxiv.org/doi.org URLs, 40-hex S2 ids, `CorpusId:N` |
| `--jsonl` / `--id-field` | draw ids from a JSONL file (e.g. a sweep output) |
| `--out` | JSONL path (default stdout) |
| `--source` | `s2` (default) or `openalex` |
| `--delay` | seconds between batches (default 3) |

Output fields: `input_id`, `source`, `found`, `paper_id`, `title`, `year`,
`publication_date`, `venue`, `citation_count`, `external_ids`,
`open_access_pdf`, `authors`.

Citation counts from the two sources are **not interchangeable** — the skill's
rule of naming one primary citation source per run still applies.

## API keys

Both scripts read, in this order (environment wins):

1. `S2_API_KEY`, `OPENALEX_API_KEY`, `SOTA_MAILTO` (or `CROSSREF_MAILTO`)
   environment variables;
2. `~/.config/find-sota-papers/config.json` — written by
   `python install.py --configure-keys`; override the path with
   `FIND_SOTA_PAPERS_CONFIG`.

Keys are optional but strongly recommended: anonymous OpenAlex credit is about
ten searches a day, and anonymous Semantic Scholar traffic shares a heavily
throttled pool.
