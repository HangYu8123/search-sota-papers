# Result File Format (`find-sota-papers/result@1`)

The standardized on-disk form of a search run. Read this when the skill is
invoked in a harness that can write files (Step 13 of `SKILL.md`).

A result file is **the same report the user sees in chat**, plus machine-readable
run metadata and an audit ledger. It is the unit that the evaluation GUI
(`evaluate_results_gui.html`) loads and scores, so the field names and section
order below are a contract, not a suggestion — a renamed field silently drops a
reward signal.

## Where it goes

Resolve the output directory in this order, first hit wins:

1. An explicit path in the user's request.
2. `results/` under the current working directory — create it if missing.

Running from this repo therefore writes to `FindPapers/results/`. When the skill
runs in a harness with **no** file-write tool, skip the file, emit the report to
chat only, and say so in one line.

## Naming

`<slug>_<YYYY-MM-DD>.md`

- `slug` — derived from `topics` (fall back to `field` when topics are empty):
  lowercase, ASCII, non-alphanumerics collapsed to single hyphens, trimmed to
  **60 characters** at a hyphen boundary. Drop stopwords (`a`, `the`, `for`,
  `of`, `on`, `in`, `and`, `with`) only if needed to fit.
- `<YYYY-MM-DD>` — the run date.
- On collision, append `-2`, `-3`, … Never overwrite an existing result file: an
  earlier run may already have an evaluation pointing at its `run_id`.

`run_id` **is** the file basename. Example:
`vision-language-action-models-manipulation_2026-07-19` →
`results/vision-language-action-models-manipulation_2026-07-19.md`.

## Frontmatter

YAML, first thing in the file. Every key is required; write `unknown` (not a
guess, not an omission) for anything you could not determine — a missing key
breaks the parser, `unknown` does not.

```yaml
---
schema: find-sota-papers/result@1
run_id: vision-language-action-models-manipulation_2026-07-19
created: 2026-07-19T14:32:11Z        # ISO 8601, UTC
harness: claude-code                  # claude-code | codex | chatgpt | claude.ai | other
model: claude-opus-4-8                # or unknown
prompt: |
  <the user's request, verbatim>
constraints:
  field: Robotics
  topics: vision-language-action models for manipulation
  sota_requirements: highest success rate on RLBench and CALVIN
  other_requirements: public code                 # or null
  no_earlier_than: 2024-01                        # or null
  min_citations:
    total: 50                                     # or null
    per_month: null
  institutions: any                               # any | reputable
  institutions_accept_list: null                  # null when `any`; else "general" or "general + robotics"
  listing: category                               # category | timeline
  presentation: minimalism                        # minimalism | abstract
  include_classic: true
  multi_agent: auto                               # auto | yes | no
  num_papers: 30
  discovery_floor: 100                            # absolute min unique candidates before filtering, independent of num_papers
  sub_areas: null                                 # null when derived from topics; else the explicit lane list the user supplied
  relationship_graph: true                        # true | false
funnel:                 # the Step-9 honesty trail; each number must be real
  found: 138            # raw candidates across all discovery lanes
  merged: 97            # after dedup by candidate_id — must clear the discovery floor
  snowball_added: 18    # of merged, the count that entered via citation/reference expansion
  filtered: 44          # after date floor + relevance
  verified: 31          # LIVE after validation
  selected: 28          # actually listed below
grounding:
  links_checked: 31     # candidates whose canonical page was fetched
  non_resolving: 0      # fetched and 4xx/5xx/connection-failed
  unknown_fields: 3     # fields written `unknown` rather than guessed
  citation_source: Semantic Scholar
  citation_checked: 2026-07-19
cost:
  wall_clock_s: 512     # or unknown
  tokens_total: unknown # only if the harness actually reports it — never estimate
  searches: 24
  fetches: 47
  subagents: 4          # 0 when multi_agent resolved to sequential
shortfall: 28 of 30 — 3 candidates below the 50-citation floor, 1 link never resolved.
---
```

`shortfall: null` when the count was met. `tokens_total` stays `unknown` unless
the harness surfaces a real number; a fabricated cost figure poisons the
token-cost reward signal it feeds.

## Body — fixed section order

Headings must match exactly. The evaluation GUI locates content by heading.

```markdown
# SOTA Papers — <field> · <topics>

## Run summary

<one line restating resolved constraints: since <date> · SOTA = <criterion>
· cites total≥<X>/month≥<Y> · <N> papers · list by <mode> · <presentation>>

Found 138 → merged 97 → filtered 44 → verified 31 → selected 28.
Citation counts via Semantic Scholar (2026-07-19).
28 of 30 — 3 below the citation floor, 1 unresolved link.

## Classic / foundational

- **[Title](https://…)** — one line on why the selected works build on it.

<!-- or, when none was found: -->
No single common ancestor emerged across the selected papers — skipped.

## Papers

### <Category A | 2026>

**[Title](https://…)** — authors, venue, date
- *Intuition:* … ([paper evidence](https://…))
- *Contribution:* … ([paper evidence](https://…))
- *Setup:* … ([setup evidence](https://…))
- *Results:* … vs <named baselines>. ([result/benchmark evidence](https://…))

### <Category B | 2025>
…

## Relationship graph

<!-- only when relationship_graph was on; omit the whole section otherwise -->

2 tracks: diffusion policies (P1–P8) · autoregressive VLAs (P9–P14).
P1 <Title>, P2 <Title>, … C1 <Classic work title>

P3 --cites--> P1
P1 --cites--> C1
P7 --builds-on--> P2  ("we build directly on …")
P14 — disconnected: no citation link to any other selected paper.

## Verification ledger

| # | candidate_id | title | link | date | citations | source | citation_evidence | sota_evidence | content_evidence | affiliation | affiliation_evidence | checks | verdict |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | arXiv:2503.01234 | … | https://arxiv.org/abs/2503.01234 | 2025-03 | 142 | S2 | https://api.semanticscholar.org/… | https://benchmark.example/… | https://arxiv.org/html/2503.01234 | Stanford University | https://arxiv.org/html/2503.01234 | canonical+meta+citation+sota+affiliation | LIVE |

## Dropped candidates

| candidate_id | title | reason |
|---|---|---|
| arXiv:2402.09876 | … | citation floor: 31 < 50 |

## Discovery manifest

<!-- one row per discovery lane; makes lane breadth and snowballing auditable -->

| lane | seed queries | raw hits | curated | snowball-adds |
|---|---|---:|---:|---:|
| diffusion policies for manipulation | "diffusion policy", "flow-matching policy", "action chunking" | 41 | 12 | 3 |
| sim-to-real RL | "sim-to-real reinforcement learning manipulation", … | 33 | 9 | 2 |
| … | … | … | … | … |
| **totals** | | **138** | **97** | **18** |

Lane count must satisfy `max(6, 2 × S)` (S = named sub-areas); the `raw`,
`curated`, and `snowball-adds` totals must reconcile with the funnel's `found`,
`merged`, and `snowball_added`.

## Coverage & limitations

- Discovery lanes run and what each covered (the manifest above is the ledger).
- Whether the effective discovery floor was `k × num_papers` or the absolute
  `discovery_floor`, and if the escape hatch was used, that it was.
- Snowball outcome: `snowball_added`, or the saturation note if expansion dried up.
- Sources that refused automated fetch, and the fallback used.
- Fields left `unknown` and why.

## Evaluate this run

Open `evaluate_results_gui.html`, load this file, and save the result to
`evaluations/`. Run id: `vision-language-action-models-manipulation_2026-07-19`.
```

## Rules that make the file scoreable

- **The ledger is the per-item spine.** One row per `LIVE` paper listed under
  `## Papers`, in the same order, with matching titles and links. The evaluation
  GUI builds its per-paper labels from these rows; a paper missing from the
  ledger cannot be scored, and a ledger row with no paper reads as a phantom.
- **`checks`** is a `+`-joined subset of `canonical`, `meta`, `citation`, `sota`,
  `affiliation` — the Step-5 checks actually completed for that candidate.
  `affiliation` appears only on runs where `institutions` was `reputable`.
- **`affiliation`** names the accept-list institution that qualified the paper,
  or `—` when `institutions` was `any`. One institution is enough; listing every
  affiliation of every author is noise.
- **Evidence columns preserve provenance.** `citation_evidence` is the exact
  fetched URL that supplied the count; `sota_evidence` supports benchmark/SOTA
  status; `content_evidence` supports intuition, contribution, setup, and result
  claims; `affiliation_evidence` supports the qualifying institution and is `—`
  when the institution filter is off. Put multiple URLs in one cell with `<br>`.
  Encode a literal pipe in any table value as `&#124;` so the evaluation parser
  does not split one field into multiple columns.
- **Institution drops carry which kind they were.** Use
  `institution: not on accept-list (<resolved institutions>)` when affiliations
  were established and none matched, and `institution: affiliation unresolved`
  when the ladder ran and the sources published none. These are different
  findings — the first is the filter working, the second is a gap in the
  metadata — and the *Coverage & limitations* section should carry the
  `unresolved` count whenever it is above roughly a fifth of the verified set.
- **Every dropped candidate gets a row and a concrete reason.** "Dropped" with no
  reason is indistinguishable from a candidate silently lost, and the shortfall
  gate depends on the difference.
- **The relationship graph never adds a paper.** Its `P1…Pn` ids follow the order
  papers appear under `## Papers`, and no edge line may use the
  `**[Title](url)**` shape — the evaluation GUI falls back to counting linked
  bold titles when a ledger is missing, so an edge written that way is read as an
  extra paper that has no ledger row.
- **`selected` must equal the number of papers under `## Papers`** (excluding the
  classic work) **and** the number of ledger rows. If the three disagree, the run
  is wrong, not the file.
- **The discovery manifest reconciles with the funnel.** Its lane count meets
  `max(6, 2 × S)`, and its `raw` / `curated` / `snowball-adds` column totals match
  `found` / `merged` / `snowball_added`. A `snowball_added` of 0 means snowballing
  did not run — a bug, not a finding (see `references/search-depth.md`).
- Write the file **after** the report is final, in one pass. A partially written
  result file will still be picked up by the GUI as a complete run.
