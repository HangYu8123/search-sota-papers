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

**Never pay to route around a limit.** Do not call paid SERP/scraper services,
and do not evade a source's access controls. A blocked source is a cue to move
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

## Optional discovery products

Edison Scientific/FutureHouse, OpenScholar/Asta, PaperQA2, Elicit, Consensus,
Undermind, alphaXiv, CodeSOTA, Hugging Face Papers, and vendor deep-research tools
are optional. Use one only when the harness actually exposes it; never claim an
unavailable product was called. Treat the Papers With Code website and its
leaderboard data as archival because the service became unavailable/redirected
in 2025; do not claim a formal Meta sunset without a primary source.
