# Result File Format (`find-sota-papers/result@1`)

The standardized on-disk form of a search run. Read this when the skill is
invoked in a harness that can write files (Step 12 of `SKILL.md`).

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
funnel:                 # the Step-9 honesty trail; each number must be real
  found: 96             # raw candidates across all discovery lanes
  merged: 71            # after dedup by candidate_id
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

Found 96 → merged 71 → filtered 44 → verified 31 → selected 28.
Citation counts via Semantic Scholar (2026-07-19).
28 of 30 — 3 below the citation floor, 1 unresolved link.

## Classic / foundational

- **[Title](https://…)** — one line on why the selected works build on it.

<!-- or, when none was found: -->
No single common ancestor emerged across the selected papers — skipped.

## Papers

### <Category A | 2026>

**[Title](https://…)** — authors, venue, date
- *Intuition:* …
- *Contribution:* …
- *Setup:* …
- *Results:* … vs <named baselines>.

### <Category B | 2025>
…

## Verification ledger

| # | candidate_id | title | link | date | citations | source | affiliation | checks | verdict |
|---|---|---|---|---|---|---|---|---|---|
| 1 | arXiv:2503.01234 | … | https://arxiv.org/abs/2503.01234 | 2025-03 | 142 | S2 | Stanford University | canonical+meta+citation+sota+affiliation | LIVE |

## Dropped candidates

| candidate_id | title | reason |
|---|---|---|
| arXiv:2402.09876 | … | citation floor: 31 < 50 |

## Coverage & limitations

- Discovery lanes run and what each covered.
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
- **`selected` must equal the number of papers under `## Papers`** (excluding the
  classic work) **and** the number of ledger rows. If the three disagree, the run
  is wrong, not the file.
- Write the file **after** the report is final, in one pass. A partially written
  result file will still be picked up by the GUI as a complete run.
