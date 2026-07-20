# Evaluation & Reward Schema (`find-sota-papers/eval@1`)

Every CLI run of the skill writes a result file to `results/`. This document
defines how those runs get scored, what an evaluation record contains, and how
the record converts into training signal.

The evaluation GUI (`evaluate_results_gui.html`) implements this document. If the
two ever disagree, this file is the specification and the GUI is the bug.

```
results/<run_id>.md        →  evaluate_results_gui.html  →  evaluations/<run_id>__<rater>.json
```

## Why these signals

The obvious feedback for a paper search is "did you like it?" — one number, no
structure, and nothing you can train on. Every dimension below exists because a
published evaluation harness for research agents found it carried information the
single number did not:

| Signal group | Mirrors | Why it isn't redundant |
|---|---|---|
| Rubric dimensions (coverage, relevance, organization, depth, instruction-following, readability) | ScholarQABench / OpenScholar human eval; DeepResearch Bench **RACE** (comprehensiveness, depth, instruction-following, readability) | A run can be broad and shallow, or deep and off-brief. One satisfaction score cannot say which. |
| Binary verifiable checks | **RLVR** (Tülu 3): reward from a verification function, not a judge | Link resolution and date-floor compliance have ground truth. Rating them on a Likert scale throws that certainty away. |
| Per-paper item labels | ResearchQA rubric items; PRM-style per-step labels | Localizes the failure. "3/5 satisfied" tells you nothing about *which* papers were wrong. |
| Grounding triple (resolves / hallucinated / stale) | `urlhealth` (arXiv 2604.03173); ALCE & OpenScholar citation precision/recall | The failure this skill exists to prevent needs its own dedicated signal, not an inference from satisfaction. |
| Cost + wall-clock, kept separate from quality | **AstaBench** cost-vs-accuracy Pareto reporting | Quality and cost trade off. Collapsing them hides whether a run was good *for its price*. |
| Weighted aggregation with visible components | **Rubrics as Rewards** (arXiv 2507.17746) | A single opaque scalar can't be debugged. Explicit per-criterion weights stay inspectable. |
| Pairwise preference between runs | Chatbot Arena; TRL/OpenAI DPO formats | Absolute Likert ratings drift between sessions and raters; relative judgments are far more stable. |
| `lead_time_s` on the annotation itself | Label Studio annotation export | A rubric answered in 20 seconds is a different quality of evidence than one answered in 8 minutes. |

## The scales

Four scales are asked directly, exactly as requested. Two are **bipolar** — the
middle is best, both ends are failures — and mixing them up inverts the reward,
so the record stores the polarity with the value.

| Key | Question | 1 | 3 | 5 | Polarity |
|---|---|---|---|---|---|
| `satisfaction` | How good were the search results? | very unsatisfied | neutral | very satisfied | unipolar ↑ |
| `time_cost` | How long did the run take? | far too long | about right | far too short | **bipolar**, 3 best |
| `sota_freshness` | How current is the selected work? | too old | mixed | genuinely SOTA | unipolar ↑ |
| `token_cost` | What did it cost to produce? | far too much | acceptable | efficient | unipolar ↑ |

`satisfaction` carries a **required free-text reason**. It is the only field a
rater cannot skip: an unexplained score tells you a run was bad without telling
you what to change, and it is the field most often revisited months later.

`time_cost` is bipolar because "too short" is a real failure here — a search that
returns in 40 seconds almost certainly skipped the deepening loop. The record
therefore also stores `direction: too_long | just_right | too_short`, because the
two failures need opposite fixes and the reward term alone cannot distinguish
them.

## Record format

One JSON file per evaluation: `evaluations/<run_id>__<rater>.json`. A second
evaluation of the same run by the same rater gets a `__2` suffix — disagreement
over time is signal, not a conflict to resolve by overwriting.

```jsonc
{
  "schema": "find-sota-papers/eval@1",
  "eval_id": "vlm-manipulation_2026-07-19__hangyu",
  "run_id": "vlm-manipulation_2026-07-19",
  "result_file": "results/vlm-manipulation_2026-07-19.md",
  "rated_at": "2026-07-19T18:04:22Z",
  "rater": "hangyu",
  "lead_time_s": 214,

  // Copied from the result file's frontmatter so the record stands alone.
  "run": {
    "prompt": "...",
    "constraints": { "...": "..." },
    "funnel":    { "found": 96, "merged": 71, "filtered": 44, "verified": 31, "selected": 28 },
    "grounding": { "links_checked": 31, "non_resolving": 0, "unknown_fields": 3 },
    "cost":      { "wall_clock_s": 512, "tokens_total": "unknown", "subagents": 4 }
  },

  "scales": {
    "satisfaction":   { "value": 4, "polarity": "unipolar", "reason": "Strong on..." },
    "time_cost":      { "value": 2, "polarity": "bipolar",  "direction": "too_long" },
    "sota_freshness": { "value": 5, "polarity": "unipolar" },
    "token_cost":     { "value": 3, "polarity": "unipolar" }
  },

  "rubric": {
    "coverage": 4, "relevance": 5, "organization": 4,
    "depth": 3, "instruction_following": 5, "readability": 4
  },

  // Binary, ground-truthable. null = not checked (excluded from the reward).
  "checks": {
    "links_resolve": true,
    "no_fabricated_citation": true,
    "no_duplicates": true,
    "date_floor_respected": true,
    "count_or_shortfall_honest": true,
    "constraints_honored": true
  },

  "items": [
    { "candidate_id": "arXiv:2503.01234", "label": "relevant",
      "link_ok": true, "flags": [] },
    { "candidate_id": "arXiv:2411.05678", "label": "borderline",
      "link_ok": true, "flags": ["not-sota"] }
  ],

  "preference": {
    "best_item":  "arXiv:2503.01234",
    "worst_item": "arXiv:2411.05678",
    "vs_run": null,                    // another run_id, when comparing two runs
    "verdict": null                    // "this" | "other" | "tie" | "both_bad"
  },

  "freeform": {
    "reason": "…",                     // mirrors scales.satisfaction.reason
    "missing": "No coverage of diffusion-policy variants.",
    "improvement": "Search the benchmark leaderboard before the arXiv sweep."
  },

  "outcome": { "would_reuse": true, "would_cite_count": 6 },

  "reward": {
    "scalar": 0.781,
    "veto": false,
    "components": [
      { "key": "satisfaction", "tier": "essential", "weight": 1.0, "normalized": 0.75 }
    ]
  }
}
```

`items[].flags` is an open vocabulary; the GUI offers `not-sota`, `too-old`,
`off-topic`, `duplicate`, `link-broken`, `wrong-metric`, `preprint-only`.

## Reward aggregation

Explicit weighted mean over normalized criteria, per Rubrics-as-Rewards — chosen
over a learned scalar because every component stays visible and arguable:

```
reward = Σ (wⱼ · cⱼ) / Σ wⱼ            cⱼ ∈ [0,1],  reward ∈ [0,1]
```

Weight tiers, also from RaR: **essential 1.0**, **pitfall 0.9**, **important
0.7**, **optional 0.3**.

| Criterion | Tier | Weight | Normalization |
|---|---|---|---|
| `satisfaction` | essential | 1.0 | `(v−1)/4` |
| `sota_freshness` | essential | 1.0 | `(v−1)/4` |
| `rubric.relevance` | essential | 1.0 | `(v−1)/4` |
| `rubric.instruction_following` | pitfall | 0.9 | `(v−1)/4` |
| `checks.*` (each answered check) | pitfall | 0.9 | `1` / `0` |
| `link_precision` (derived) | pitfall | 0.9 | `#link_ok / #items` |
| `rubric.coverage` | important | 0.7 | `(v−1)/4` |
| `rubric.depth` | important | 0.7 | `(v−1)/4` |
| `item_precision` (derived) | important | 0.7 | `(#relevant + 0.5·#borderline) / #items` |
| `rubric.organization` | optional | 0.3 | `(v−1)/4` |
| `rubric.readability` | optional | 0.3 | `(v−1)/4` |
| `time_cost` | optional | 0.3 | `1 − |v−3| / 2`  ← bipolar |
| `token_cost` | optional | 0.3 | `(v−1)/4` |

Unanswered criteria drop out of **both** sums, so a partial evaluation stays
comparable to a complete one rather than being silently penalized for the
questions the rater skipped.

**The veto.** `checks.no_fabricated_citation === false` sets `reward.veto`. The
scalar is still computed — the run may have been excellent apart from this — but a
vetoed run must never be used as a positive training example. Fabrication is the
one failure this skill exists to prevent; letting a high average paper over it
would train exactly the behavior being prevented.

## Derived training views

The record is the source of truth; these are projections, generated on demand by
`evaluations/export.py`, never hand-maintained.

**Preference pairs** — TRL / OpenAI DPO columns, from two evaluated runs of the
same or near-identical prompt. `chosen` is the higher-reward run, or the explicit
`preference.verdict` when the rater compared them directly (a stated preference
always beats an inferred one):

```jsonl
{"prompt": "<the user request>", "chosen": "<report A>", "rejected": "<report B>"}
```

**Rubric reward** — for reward-model or RaR-style training, keeping the
components so a learned reward can be checked against its parts:

```jsonl
{"prompt": "...", "completion": "...", "reward": 0.781, "components": [...], "veto": false}
```

**Item relevance** — per-paper labels for training or evaluating the ranking
stage in isolation:

```jsonl
{"prompt": "...", "candidate_id": "arXiv:2503.01234", "label": "relevant", "link_ok": true}
```

**Verifiable rewards** — the RLVR slice: binary, no judge, no rater drift.

```jsonl
{"prompt": "...", "check": "links_resolve", "pass": true}
```

## Reading the archive

Rules of thumb once `evaluations/` holds more than a handful of records:

- **Report reward against cost, never alone.** A run at 0.82 for 500k tokens and
  one at 0.78 for 90k are not ranked by the scalar. Plot the pair and keep the
  frontier — this is AstaBench's argument, and it survives contact with real use.
- **Trust the checks over the scales.** Binary checks are ground truth; Likert
  values drift across raters and weeks. When they disagree, the check is right.
- **Two evaluations of one run are data.** Rater disagreement bounds how much
  precision the scalar can carry; collapsing it hides that ceiling.
- **Read `freeform.missing` first.** Recall failures are invisible to every other
  field on this page — nothing in a result file can report the paper it never
  found. It is the one signal that only a human reader can produce.

## Sources

- Rubrics as Rewards — `https://arxiv.org/abs/2507.17746`
- RL with Rubric Anchors — `https://arxiv.org/abs/2508.12790`
- RLVR / Tülu 3 — `https://arxiv.org/abs/2411.15124`
- DeepResearch Bench (RACE / FACT) — `https://arxiv.org/abs/2506.11763`
- ScholarQABench / OpenScholar — `https://arxiv.org/abs/2411.14199`
- ResearchQA — `https://arxiv.org/abs/2509.00496`
- PaperBench — `https://arxiv.org/abs/2504.01848`
- AstaBench — `https://allenai.org/blog/astabench`
- Chatbot Arena — `https://arxiv.org/abs/2403.04132`
- ALCE (citation precision/recall) — `https://arxiv.org/abs/2305.14627`
- Resolvable-citation metrics (`urlhealth`) — `https://arxiv.org/abs/2604.03173`
- TRL dataset formats — `https://huggingface.co/docs/trl/en/dataset_formats`
- OpenAI DPO format — `https://developers.openai.com/api/docs/guides/direct-preference-optimization`
- Inspect eval logs (`model_usage`, `total_time`, `working_time`) — `https://inspect.aisi.org.uk/eval-logs.html`
- Label Studio export (`lead_time`) — `https://labelstud.io/guide/export`
