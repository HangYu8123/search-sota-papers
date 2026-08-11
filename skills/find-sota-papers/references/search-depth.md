# Search depth and coverage gates

Read this file before Step 2. Apply the same search requirements in parallel and
sequential execution.

## Deepening loop

For every discovery lane:

1. **Seed:** run at least three materially different queries: user wording,
   canonical field terminology, and benchmark/method terminology.
2. **Harvest:** extract method, architecture, benchmark, dataset, task, author,
   venue, and arXiv-category vocabulary from fetched results.
3. **Refine:** run at least three new queries using harvested vocabulary.
4. **Snowball:** for the strongest 3–5 candidates, inspect citations and
   references to find newer work and possible classic ancestors. This is a
   **floor, not an option** — see *Snowball floor* below.
5. **Saturate:** stop only after two consecutive rounds add no candidate or an
   explicit lane budget is reached. Record the budget and saturation reason.

Search snippets select pages to open; they never support final claims.

## Lane decomposition and count

Coverage comes from breadth of lanes, not depth of one lane. Before searching,
**decompose the request into discovery lanes** — one lane per **named method,
benchmark, sub-direction, or model family** appearing in `topics` +
`sota_requirements` + `other_requirements`, plus adjacent-work and snowball lanes,
plus the three **mandatory high-recall harvest lanes** defined in the next
section (survey-mining, curated-list, venue-sweep).

Run at least:

```text
lanes >= max(6, 2 * S)
```

where `S` is the number of distinct named sub-areas. The `6` floor means even a
single-term topic still fans into method / benchmark / venue / adjacent-work
phrasings; the `2 * S` term means a union topic like "RL + imitation learning +
diffusion policy + sim-to-real" earns proportionally more lanes (that breadth is
exactly why the deepest past runs surveyed an order of magnitude more work). When
the user supplies an explicit **sub-areas / lanes** list, give each item its own
lane and count it toward `S`; when they do not, derive the sub-areas yourself from
the topic wording and canonical terminology.

Every lane meets the per-lane floor below and is recorded in the **discovery
manifest** — one row per lane: `lane · seed queries · raw hits · curated
candidates · snowball-adds`. Carry that table into the result file so an
under-searched lane is visible and auditable rather than hidden inside an
aggregate `found` number.

## Mandatory high-recall harvest lanes

Keyword lanes share one blind spot: they only find what the harvested vocabulary
can phrase. Anything whose title and abstract use different words — camera-ready
versions, renamed model families, industry releases announced venue-first — is
invisible to every keyword lane at once. **Every run therefore includes at least
one lane of each of the three types below**, at every depth tier, in addition to
the keyword lanes. Each is one ordinary manifest row (prefix the lane id
`H-survey`, `H-list`, `H-venue`), counts toward the `max(6, 2 × S)` lane floor,
and remains mandatory even when keyword lanes alone would satisfy that count.

Harvested entries are **leads, not evidence**: every paper found this way enters
the merged pool as an ordinary candidate and passes through validation like any
other. The survey, repo, or program page that surfaced it is recorded as the
lane's source, never cited as verification.

### Survey-mining lane (`H-survey`)

1. Find 1–3 recent surveys/reviews of the topic (search the topic plus
   "survey" / "review" on arXiv and Semantic Scholar; prefer the newest and
   most-cited).
2. Pull each survey's **structured reference list in one call** — the Semantic
   Scholar `/paper/{id}/references` endpoint or OpenAlex `referenced_works`
   (templates in `references/sources.md`) — instead of scraping the PDF
   bibliography.
3. Curate the in-scope references into candidates. A single 200-entry reference
   list typically yields dozens of candidates for one fetch; it is the cheapest
   recall in the whole run.

Thorough and exhaustive tiers mine at least 3 surveys when that many exist.

### Curated-list lane (`H-list`)

1. Search for community-curated collections: GitHub `awesome-<topic>` lists,
   conference-collection repos, lab reading lists, model-family indexes. Query
   patterns: `awesome <topic> github`, `<topic> paper list github`,
   `<venue> <year> papers github`.
2. Fetch the raw README/markdown of the 2–3 best-maintained hits (most stars,
   most recent commit) and harvest every in-scope entry.
3. Record each source repo URL and its last-update date in the lane notes — a
   stale list is still useful for lineage, but say that it is stale.

This is the lane that catches **model-family lineages** (every version of a
family, not just the flagship, plus backbone models and anchoring datasets —
label those as such) and industry-lab releases that topic keywords miss.

### Venue-sweep lane (`H-venue`)

1. Name the field's top 2–3 venues with an edition inside or overlapping the
   date window.
2. Fetch their accepted-paper listings directly: CVF open access
   (`openaccess.thecvf.com`), PMLR (`proceedings.mlr.press`), NeurIPS
   (`papers.nips.cc`), ACL Anthology (`aclanthology.org/venues/`), OpenReview
   venue pages, or the venue's own program page.
3. Filter the listing's titles for in-scope work and add matches as candidates.

This is the only systematic way to catch peer-reviewed papers whose
camera-ready title or abstract differs from — or never had — an arXiv version.

### When a harvest lane finds nothing

A genuinely new topic may have no survey, no awesome-list, or no in-window venue
edition. The lane still runs: record the ≥3 locating queries tried and the empty
harvest in its manifest row, exactly like any other demonstrated-scarcity claim.
An unrun harvest lane is under-searching; a run-and-empty one is a finding.

## Effort floors

| Scope | Searches | Fetches | Rounds |
|---|---:|---:|---:|
| Each discovery lane | 6 | 5 | 2 plus snowballing |
| Each harvest lane (`H-survey` / `H-list` / `H-venue`) | 3 | 3 | 1 |
| Whole task, `num_papers <= 10` | 10 | 15 | — |
| Whole task, default `num_papers ~= 30` | 20 | 40 | — |
| Whole task, `num_papers >= 50` | 30 | 70 | — |

These are floors, not targets. Set a maximum query/fetch/time budget per lane in
the discovery manifest so a broad request cannot run without a bound. If the
user requests an impractically large list, state a safe batch size and complete
that batch rather than silently weakening validation.

## Snowball floor

Snowballing (citation/reference expansion) is the single highest-yield way to
find non-obvious SOTA that keyword lanes miss — and it is the step runs most often
skip. It is **mandatory and counted**, not best-effort.

For the strongest `K = min(10, merged)` candidates in the merged pool (ranked by
SOTA fit + citation signal), fetch **both directions**:

- **backward references** — what the candidate says it builds on,
- **forward citations** — what has since cited the candidate, and
- **similar papers** — the Semantic Scholar Recommendations API (template in
  `references/sources.md`) surfaces similar-but-not-citing work that no
  citation edge reaches; count its in-scope adds as `from_snowball = yes`
  exactly like the other two directions.

Run the same expansion once more on the **top `K` verified papers** after Step 5,
so anything a late-arriving strong paper points to is not missed.

Require at least:

```text
snowball_added >= max(10, num_papers / 3)
```

distinct new **in-scope** candidates to enter the merged pool from snowballing —
or keep expanding further candidates until two consecutive expansion rounds
surface no new in-scope paper (record that saturation). Track the total as
`snowball_added` in the funnel and as the `snowball-adds` column of the discovery
manifest. **A run that added zero has not snowballed and must go back** before
reporting any shortfall or scarcity.

## Discovery floor

After deduplication in Step 4, require **both** of these to hold:

```text
merged >= 3 * num_papers          # 4 * num_papers when institutions == reputable
merged >= discovery_floor         # absolute floor, default 100, independent of num_papers
```

i.e. `merged >= max(k * num_papers, discovery_floor)` with `k = 3` (`4` when
`institutions == reputable`). The absolute floor is the point: a small
`num_papers` request must **not** license a shallow survey. "Top 10" still means
surveying at least ~100 unique candidates before any filtering, so the final ten
are selected from a real field rather than the first ten that turned up.
`discovery_floor` defaults to `100` and is user-settable — `100` standard,
`150` thorough, `250` exhaustive; a larger final list simply lets the `k *
num_papers` term bind instead.

`merged` counts unique candidates, not repeated lane hits. If below the effective
floor, return to discovery. Proceed below it only after all three conditions hold:

1. two additional rounds ran after missing the floor;
2. those rounds used at least two new phrasings and two previously untried
   sources;
3. they produced no candidate.

Record this escape under Coverage & limitations, and state which floor bound (the
`k * num_papers` term or the absolute `discovery_floor`). Missing the floor
without the escape is under-searching, not demonstrated scarcity.

## Bulk enumeration (when code execution exists)

When the harness can run Python 3, prefer the bundled sweeper for any lane that
wants a whole arXiv category × date window: `scripts/arxiv_sweep.py` walks the
window to exhaustion (paginated, rate-limit-polite, resumable) and writes one
JSON line per paper for triage — replacing dozens of hand-issued fetches whose
raw-hit counts otherwise silently truncate at one page. Batch-resolve the
survivors' metadata and citation counts with `scripts/resolve_ids.py`. See the
*Bundled helper scripts* section of `references/sources.md` and
`scripts/README.md` for flags. Harnesses without code execution keep the
fetch-based flow; every floor above is unchanged either way.

## Query craft

- Search method, comparison, benchmark, venue, and current-year phrasings.
- Include site-scoped arXiv/venue/project queries alongside open-web queries.
- Search both old and new names for a renamed subfield.
- Treat a thin source response as a query/source problem until at least two
  sources and two phrasings agree.
