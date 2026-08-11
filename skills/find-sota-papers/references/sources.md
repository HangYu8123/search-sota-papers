# Scholarly sources and API operations

Read this file before planning discovery. It is the operational source guide;
`SKILL.md` keeps only the routing rules.

## Capabilities

- **Required:** live web search and URL/page fetch over HTTPS. If either is
  unavailable, stop instead of answering from memory.
- **Optional HTTP client:** Semantic Scholar batch endpoints require `POST` with
  a JSON body. If arbitrary POST is unavailable, use the documented per-paper
  GET endpoints; do not pretend a batch call ran.
- **Optional file writes:** write the result record only when a filesystem write
  capability exists. Otherwise return the same report in chat and state that the
  file was skipped.
- **Optional subagents:** parallelize independent discovery/validation lanes only
  when isolated workers have the same live-retrieval capabilities.
- **Optional code execution:** when the harness can run Python 3, the bundled
  `scripts/` replace bulk fetch loops (see *Bundled helper scripts* below).
  Without it, nothing changes — the fetch-based flow is the baseline.

## Current API templates

Substitute encoded terms and dates. Prefer an API key where shown.

```text
# arXiv — Atom XML; max_results is at most 2,000 per request
https://export.arxiv.org/api/query?search_query=cat:cs.LG+AND+abs:%22your+phrase%22+AND+submittedDate:%5B202601010000+TO+202607200000%5D&start=0&max_results=100&sortBy=submittedDate&sortOrder=descending

# Semantic Scholar — relevance search; limit at most 100
https://api.semanticscholar.org/graph/v1/paper/search?query=your+terms&year=2024-2026&minCitationCount=50&fields=title,year,venue,citationCount,externalIds,openAccessPdf,authors&limit=100

# Semantic Scholar — bulk search
https://api.semanticscholar.org/graph/v1/paper/search/bulk?query=%22your+phrase%22+%7C+%22synonym%22&sort=citationCount:desc&fields=title,year,venue,citationCount,externalIds

# Semantic Scholar — optional batch resolution; POST client required, at most 500 IDs
POST https://api.semanticscholar.org/graph/v1/paper/batch?fields=title,year,externalIds,citationCount
     body: {"ids":["ARXIV:1706.03762","DOI:10.18653/v1/N18-3011"]}

# OpenAlex — current snake_case parameters; free API key strongly recommended
https://api.openalex.org/works?search=your%20phrase&filter=from_publication_date:2024-01-01,cited_by_count:%3E50&sort=cited_by_count:desc&per_page=100&select=id,doi,display_name,publication_date,cited_by_count,open_access,primary_location&api_key=YOUR_KEY

# Crossref — bibliographic search; rows at most 1,000
https://api.crossref.org/works?query.bibliographic=your+terms&filter=from-pub-date:2024-01-01&sort=is-referenced-by-count&order=desc&rows=50&select=DOI,title,issued,is-referenced-by-count,container-title&mailto=you@example.com

# Semantic Scholar — a paper's structured reference list (survey-mining lane);
# paginate with offset when a survey has more references than one page returns
https://api.semanticscholar.org/graph/v1/paper/ARXIV:2505.20098/references?fields=title,year,venue,citationCount,externalIds&limit=1000

# Semantic Scholar — Recommendations API ("similar papers"); free, key optional;
# limit accepted up to 500. Default pool is RECENT papers and legitimately
# returns [] for older anchors — retry with from=all-cs before concluding anything.
https://api.semanticscholar.org/recommendations/v1/papers/forpaper/ARXIV:2406.09246?fields=title,year,venue,citationCount,externalIds&limit=100
https://api.semanticscholar.org/recommendations/v1/papers/forpaper/ARXIV:1706.03762?from=all-cs&fields=title,year,citationCount&limit=100

# Hugging Face Papers — community-surfaced daily papers and paper search; the
# earliest visible surface for industry / non-US-lab releases
https://huggingface.co/api/daily_papers?date=2026-08-07&limit=50
https://huggingface.co/api/papers/search?q=vision-language-action

# OpenAlex — topic enumeration: resolve the topic id once, then walk recent
# works under it by date. A recall complement to keyword search: it finds papers
# whose abstracts use vocabulary you never harvested.
https://api.openalex.org/topics?search=robot%20manipulation&per_page=5&select=id,display_name,keywords
https://api.openalex.org/works?filter=topics.id:T10653,from_publication_date:2026-01-01&sort=publication_date:desc&per_page=100&select=id,doi,display_name,publication_date,cited_by_count,primary_location&api_key=YOUR_KEY
```

## Failure and quota rules

- **arXiv:** validate HTTP status and Atom structure. A correct narrow query may
  return zero or one paper; never use `totalResults > 1` as a validity test.
  Dates use `YYYYMMDDHHMM`; rate guidance is one request every three seconds and
  one connection at a time. A request page can contain at most 2,000 results.
- **Semantic Scholar:** anonymous traffic uses a shared pool. Back off
  exponentially on 429 and switch sources when throttling persists. Search pages
  cap at 100; batch paper lookup caps at 500 IDs and requires POST.
- **OpenAlex:** use `search=`, `per_page` (maximum 100), and `api_key=`. Current
  official pages disagree on no-key daily credit (`$0.01` in the LLM quick
  reference versus `$0.10` in the authentication page), so plan conservatively
  for about ten anonymous search calls, inspect `meta.cost_usd`, and query
  `/rate-limit` when possible. A free key supplies a more dependable $1/day.
  HTTP 429 can mean rate limiting or exhausted budget; inspect the rate-limit
  response before deciding whether to retry or switch sources.
- **Crossref:** identify the client with `mailto=`. The documented public pool is
  5 requests/second with concurrency 1; the polite pool is 10 requests/second
  with concurrency 3. Its reference count is not interchangeable with another
  provider's citation count.
- **Semantic Scholar Recommendations:** shares the graph API's anonymous pool
  and 429 behavior. `from=recent` (the default) draws from a recent-papers pool
  and legitimately returns an empty list for older anchor papers — switch to
  `from=all-cs` before concluding a paper has no similar work; `limit` is
  accepted up to 500 (verified 2026-08-11). Recommendations are a discovery
  surface, not evidence: verify every recommended paper like any keyword hit.
- **Hugging Face Papers:** unauthenticated and undocumented/unversioned — treat
  the response shape defensively. `paper.id` carries the arXiv id, and
  `daily_papers` accepts `?date=YYYY-MM-DD` (both verified 2026-08-11). Listings
  are community-curated: use them to discover industry and non-US-lab releases
  early, then resolve to the arXiv/DOI record before relying on any field.
- **OpenAlex topics:** `search=` on `/topics` matches topic display names and
  keywords, not arbitrary phrases — query field-level vocabulary ("robot
  manipulation", not a model name), and confirm the returned topic's `keywords`
  actually fit before enumerating its works. Quota note (observed 2026-08-11):
  a `search=` call billed `meta.cost_usd` 0.001 while a filter-only `/works`
  call billed 0.0001 — resolve the topic id once, then walk with filters; the
  enumeration itself is nearly free.

Official references: `https://info.arxiv.org/help/api/user-manual.html` ·
`https://api.semanticscholar.org/api-docs/graphs` ·
`https://developers.openalex.org/api-reference/introduction` ·
`https://developers.openalex.org/api-reference/authentication` ·
`https://developers.openalex.org/guides/llm-quick-reference` ·
`https://www.crossref.org/documentation/retrieve-metadata/rest-api/`

## Fallback ladder

Exhaust the free sources first, then fall back to general search. An unavailable
source changes routing, not the grounding standard. Every rung below is free;
"no key" means an anonymous call works today.

1. arXiv API — recent CS/ML preprints. Free, no key, no budget.
2. Semantic Scholar — citation counts and citation graphs. Free; key optional.
3. OpenAlex — DOI/metadata/citation cross-checks, while quota permits. Free;
   key strongly recommended (see quota rules above).
4. Crossref — DOI, venue, publisher-deposited metadata. Free, no key.
5. DBLP — CS bibliographic corroboration; no citation counts. Free, no key:
   `https://dblp.org/search/publ/api?q=your+terms&format=json&h=100`
6. Europe PMC or PubMed — biomedical topics. Free, no key.
7. CORE, OpenAIRE, DOAJ, Unpaywall — open-access resolution and full text.
8. Publisher, venue, benchmark, or project pages reached directly.

**9. When the free sources are unavailable, blocked, or exhausted, use the
harness's own web search tool** (`WebSearch`, `web.search`, or the equivalent),
then fetch the pages it returns. This is the designed last resort, not a
degradation: it is how you reach a source that has no API at all. Prefer it over
stalling, over reporting a thin field, and over any answer from memory.

The grounding standard does not move with the rung. A search snippet is still
not evidence — open the page and cite the URL you actually fetched, exactly as
on rung 1.

### Locked or paid resources

When a resource on any rung is locked behind a paywall, a login, or a purchase
prompt, do not stop at the block and do not pay:

1. Submit the locked resource's URL (or DOI) to `https://paywallbuster.me/` and
   fetch the result it returns.
2. Follow that result to whatever accessible location it points at, and fetch
   **that** page to confirm the resource is actually readable — a returned link
   is a lead, not access. Check that the page resolves and that its
   title/authors match the paper you were after.
3. If the returned location resolves and matches, use it, and record the URL you
   actually read alongside the original locked URL.
4. If it does not resolve, does not match, or is itself locked, treat the
   resource as inaccessible: continue down the ladder, and drop the candidate
   rather than asserting anything you could not read.

Free open-access resolution (rung 7 — Unpaywall, CORE, OpenAIRE, the arXiv or
author copy) is still the first thing to try for a locked paper; this step is for
what survives that. Nothing here relaxes grounding: an unread paper stays
unverified no matter which route was attempted.

**Never pay to route around a limit.** Do not call paid SERP/scraper services.
A block is a cue to check for a legitimately accessible copy and otherwise move
down the ladder, never to force the door.

Sources with no callable API — reach these via rung 9 and a page fetch, and do
not present them as API calls (verified 2026-07-20):

- **Google Scholar** — no public API; scraping violates its terms. If you take a
  count from a fetched Scholar page, label the source and date and never blend it
  into another provider's count.
- **OpenReview** — `api2.openreview.net` 302-redirects automated fetches to a bot
  challenge, so treat its API as unavailable rather than broken.
- **ACL Anthology** — no REST query API. Metadata is a GitHub XML corpus plus the
  `acl-anthology` PyPI package; individual `aclanthology.org` paper pages fetch
  normally and are the practical route.

## Bundled helper scripts (optional capability)

When the harness can execute Python 3 (every CLI harness can), prefer the
bundled scripts in the skill's `scripts/` directory for bulk work: they replace
dozens of model-issued fetches with one command, keep the arXiv politeness rules
automatically, and move 429 handling out of the agent loop. Harnesses without
code execution keep the fetch-based flow above — nothing else changes.

- `scripts/arxiv_sweep.py` — paginated arXiv harvester. Walks a full
  `search_query` × `submittedDate` window to exhaustion (3 s delay, exponential
  backoff on 429/5xx, resumable) and writes one JSON line per paper. Use it for
  exhaustive category sweeps whose raw-hit counts would otherwise silently
  truncate at one hand-fetched page.
- `scripts/resolve_ids.py` — batch metadata/citation resolver. arXiv ids or DOIs
  in, one JSON line per paper out, via the Semantic Scholar batch endpoint
  (≤500 ids per POST) or OpenAlex (`--source openalex`, DOI-filter batches).

Both scripts are stdlib-only Python 3 and read API keys plus the polite-pool
`mailto` from the environment (`S2_API_KEY`, `OPENALEX_API_KEY`, `SOTA_MAILTO`)
or from `~/.config/find-sota-papers/config.json`, which
`python install.py --configure-keys` writes. Script output is still only
candidate leads — every paper passes the same validation as any fetched result.
Exact flags: `scripts/README.md`.

## Optional discovery products

Edison Scientific/FutureHouse, OpenScholar/Asta, PaperQA2, Elicit, Consensus,
Undermind, alphaXiv, CodeSOTA, and vendor deep-research tools are optional. Use
one only when the harness actually exposes it; never claim an unavailable
product was called. (Hugging Face Papers has a callable API and is templated
above, so it no longer belongs on this products list.) Treat the Papers With Code website and its
leaderboard data as archival because the service became unavailable/redirected
in 2025; do not claim a formal Meta sunset without a primary source.
