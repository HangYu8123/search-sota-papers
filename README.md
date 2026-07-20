# Find SOTA Papers

An agent skill that finds **state-of-the-art research papers** for a field and topic
under explicit constraints — and verifies every paper actually exists before listing
it, so you don't get fabricated citations.

It ships as independent pieces — the skill works alone; everything else is optional:

| | |
|---|---|
| `skills/find-sota-papers/SKILL.md` | The skill, in the open [Agent Skills](https://agentskills.io) format. Works in Claude, ChatGPT/Codex, and other compatible clients. |
| `skills/find-sota-papers/agents/openai.yaml` | OpenAI Responses API agent definition — lets Codex discover the skill through the agents interface. |
| `.codex-plugin/plugin.json` | ChatGPT/Codex plugin manifest — used by `install.py` to build the marketplace package. |
| `find_papers_gui.html` | A prompt builder. Set the constraints with fields and buttons, copy the prompt. No server, no dependencies — double-click it. |
| `evaluate_results_gui.html` | Score a finished run and save the feedback record. Same deal — one static page. |
| `serve_evaluations.py` | Optional localhost helper so the evaluation GUI writes into `evaluations/` without a save dialog. |
| `EVALUATION.md` | The feedback schema, reward math, and which published harness each signal comes from. |
| `skills/find-sota-papers/references/topics/popular-topics.md` | A dated snapshot of active research topics with one-line intuitions — a starting vocabulary, and the topic keys that select institution list files. |
| `skills/find-sota-papers/references/topics/institutions.md` · `institutions/` | The reputable-institutions index — topic key → list file, plus the resolution procedure, affiliation ladder, and matching rules — and the lists themselves, one file per topic key. |
| `skills/find-sota-papers/references/result-file.md` | The `find-sota-papers/result@1` schema — naming, frontmatter keys, and section order for on-disk run records. |
| `results/` · `evaluations/` | Where runs and their evaluations accumulate. |

## Why it exists

General LLMs **fabricate 78–90% of citations** on open-ended recent-literature
queries ([OpenScholar, *Nature* 2026](https://www.nature.com/articles/s41586-025-10072-4)).
This skill is retrieval-grounded by construction: it never lists a paper from memory,
it fetches every candidate to confirm the link resolves, and it **refuses to pad** the
list — if fewer papers survive verification than you asked for, it reports the
shortfall and why.

Search is iterative rather than single-shot. Each lane seeds several phrasings,
harvests the vocabulary the literature actually uses, re-searches with those terms,
then walks the citation graph in both directions — and keeps going until two rounds
turn up nothing new. A first-page result set is where it starts, not what it returns.

When the active agent supports real subagents, the skill also searches distinct
directions in parallel, merges their evidence in the main agent, and validates the
combined candidates across scholarly sources in a separate parallel wave. This keeps
raw search noise out of the main context, broadens coverage, and speeds up independent
discovery and verification without giving up one coherent final ranking.

## Install

```bash
python install.py --target packages   # build Claude + ChatGPT packages in dist/
python install.py --dry-run           # preview all installs, change nothing
```

Or pick a target:

```bash
python install.py --target claude-code                      # ~/.claude/skills/
python install.py --target codex                            # ~/.agents/skills/
python install.py --target chatgpt                          # personal plugin marketplace
python install.py --target claude-code --scope project      # ./.claude/skills/
python install.py --target claude-zip                       # Claude upload package
python install.py --target chatgpt-zip                      # portable plugin marketplace
```

Then start a new agent session. What each surface needs:

### Claude Code
Copied to `~/.claude/skills/find-sota-papers/` (user) or `.claude/skills/find-sota-papers/`
(project). Nothing else to do — invoke it as `/find-sota-papers` or just ask in
plain language.

### Codex (CLI / IDE)
Copied to `~/.agents/skills/find-sota-papers/` (user) or `.agents/skills/find-sota-papers/`
(project). Invoke via the `/skills` menu or `$find-sota-papers`.

> Codex is mid-migration on this path: current docs use `.agents/skills`, but some
> builds and Codex's own bundled installer still read `~/.codex/skills`. If the skill
> doesn't appear, re-run with `--legacy-codex` to install to both.

### claude.ai (web / desktop)
Upload the Claude package:

1. `python install.py --target claude-zip` → produces
   `dist/find-sota-papers-claude.zip`
2. Enable **Code Execution and File Creation** (Settings → Capabilities)
3. Settings → Customize → **Skills** → **+** → **Upload a skill**

Custom skills here are per-user and **do not sync** to Claude Code or the API — each
surface needs its own copy.

### ChatGPT
For a local install in ChatGPT Work mode / the desktop app:

1. Run `python install.py --target chatgpt`.
2. Restart ChatGPT.
3. Open **Plugins**, choose the **Personal** source, and install
   **Find SOTA Papers**.

For distribution, run `python install.py --target chatgpt-zip`. Extract
`dist/find-sota-papers-chatgpt.zip`, register the extracted marketplace with
`codex plugin marketplace add <extracted-folder>`, restart ChatGPT, and install it
from the Plugins directory. The package includes the required
`.codex-plugin/plugin.json` wrapper and the skill itself.

If your workspace does not expose Work mode or Plugins, install the bare skill in
Codex with `python install.py --target codex`; it uses the same `SKILL.md` workflow.

### Package contents

| Artifact | Install surface | Archive root |
|---|---|---|
| `dist/find-sota-papers-claude.zip` | claude.ai custom skill | `find-sota-papers/SKILL.md` |
| `dist/find-sota-papers-chatgpt.zip` | ChatGPT/Codex plugin marketplace | marketplace + `plugins/find-sota-papers/` |

## Use it

Ask in plain language, or build a precise prompt with `find_papers_gui.html`:

> Find the SOTA papers on vision-language-action models for robot manipulation.
> Since 2024-01, at least 50 citations, 30 papers, grouped by technique, minimal
> format, and include the classic work they all build on.

### The constraints

| Constraint | Default | Notes |
|---|---|---|
| Field | required | AI, Robotics, CV, NLP, … |
| Topics | required | The specific direction |
| SOTA requirements | required | A benchmark + metric, or "current best approaches" |
| Other requirements | — | e.g. must have public code, open weights |
| No earlier than | — | `YYYY-MM` or `YYYY-MM-DD` |
| Min citations | — | Total and/or per month since publication |
| Institutions | `any` | `reputable` keeps only papers with an author from the curated accept-list |
| List by | `category` | `category` (tech track) or `timeline` |
| Present as | `minimalism` | `minimalism` (5-liner) or `abstract` (short intro) |
| Include classic work | `yes` | Adds a shared foundational ancestor, labeled |
| Multi-agent | `auto` | `auto` uses workers when useful; `yes` requests parallel work; `no` forces sequential execution |
| Number of papers | `30` | |
| Result file | `auto` | Writes `results/<slug>_<date>.md` when the agent can write files; a path overrides the location, `no` suppresses it |
| Links | always | Not optional — every paper carries a working link |

**`minimalism`** gives you, per paper: linked title, then one sentence each for
intuition, core contribution, experiment setup, and results vs. named baselines.

## Results on disk

Run from a CLI agent (Claude Code, Codex), the skill saves every run to
`results/<slug>_<date>.md` alongside the chat report — named from your topic, never
overwriting an earlier run. It is the same report, wrapped in machine-readable
metadata:

- **frontmatter** — the resolved constraints, the funnel (`found → merged → filtered
  → verified → selected`), grounding tallies, wall-clock and token cost;
- **a verification ledger** — one row per listed paper with its canonical id, link,
  citation count and source, and which checks actually cleared;
- **a dropped-candidates table** — every candidate that didn't make it, with the
  concrete reason.

The ledger is the part worth having. A list of papers tells you what survived; the
ledger and the drop table tell you what the run *did*, which is the only way to tell
a thin field from a shallow search after the fact. Full schema:
`skills/find-sota-papers/references/result-file.md`.

## Evaluating a run

```bash
python serve_evaluations.py        # opens the GUI, saves straight into evaluations/
```

Or just double-click `evaluate_results_gui.html` and drop a result file on it — the
helper only removes the save dialog.

You rate satisfaction (and *why* — the one required field), whether the run took too
long or suspiciously little time, how current the selection really is, and what it
cost. Then, because those five numbers can't localize a failure, it also collects a
six-dimension quality rubric, binary checks that have actual ground truth, and a
per-paper relevance label. It computes a weighted reward live as you go, and a
fabricated citation vetoes the run outright.

Records land in `evaluations/<run_id>__<rater>.json`. To turn the archive into
training data:

```bash
python evaluations/export.py            # preference pairs, rubric rewards, item labels, RLVR checks
python evaluations/export.py --stats    # summary, including reward against token cost
```

The dimensions aren't invented — each one is carried by a published harness for
research agents (ScholarQABench, DeepResearch Bench's RACE/FACT, AstaBench's
cost-vs-accuracy reporting, Rubrics-as-Rewards weighting, RLVR's verifiable slice,
ALCE citation precision). `EVALUATION.md` documents which signal comes from where,
the exact reward math, and how to read the archive once it has more than a few
records in it.

## Filtering to reputable institutions

Set **Institutions** to `reputable` and the skill keeps only papers with at least
one author affiliated with an organization on a curated accept-list — 147
universities, industry labs, and national research organizations, plus a topic
file where a general-purpose ranking under-serves a specialty. Robotics is the
first: ten organizations whose robotics output matters but that don't rank into
a top-100 sorted by overall AI volume — see `institutions/robotics.md` for the
list.

The general list always applies. If your topic matches a key that has its own
file, you get both; if it matches nothing, you get the general list alone.
The lists are indexed by topic:
`skills/find-sota-papers/references/topics/institutions.md` is the index and the
procedure, and the lists themselves sit beside it in
`references/topics/institutions/` — `general.md` (always) plus one file per topic
key (`robotics.md` today). A run loads only the files its topic selects, and
adding an institution or a whole new topic file is a content edit under that
folder.

Two things worth knowing before you switch it on:

- **It costs papers, and sometimes for the wrong reason.** Affiliation metadata
  is far sparser than citation metadata, and it is sparsest on the recent
  preprints this skill is most useful for. For one 2026 VLA paper, OpenAlex
  returned institutions for **0 of 18** authors and the arXiv abstract page
  carried none — while the paper's own HTML listed every one. So the skill reads
  the paper itself rather than trusting an empty API field.
- **"Couldn't tell" is reported separately from "not on the list."** A paper
  dropped because nobody published its affiliations is a gap in the sources, not
  a verdict on the lab, and the run report keeps the two counts apart. If the
  unresolved share gets large, the filter is partly measuring metadata
  availability, and the report says so.

The tiers in the list are a coarse reputational band from a curated snapshot, not
a measured ranking — the file says so at the top, and the skill won't quote a
tier number back to you as though it were a published rank.

## Optional multi-agent acceleration

Set **Multi-agent** to `auto` (default), `yes`, or `no` in the GUI or prompt. `no`
creates no workers and runs every lane sequentially. `auto` uses real subagents only
when available and useful; `yes` explicitly requests parallel work but still falls
back sequentially when the host has no subagent capability.

When enabled, the main agent remains the orchestrator and final writer. It chooses a small set of
non-overlapping search lanes, waits for all candidate ledgers, deduplicates them, then
assigns link, metadata/citation, and SOTA-claim checks across source platforms such as
arXiv/DOI, Semantic Scholar/OpenAlex/Crossref, and official benchmark or project pages.
Missing or failed worker assignments are completed sequentially before ranking.

This provides parallel speed, broader independent search paths, source specialization,
auditable cross-checks, and more main-agent context for synthesis. On a host without
native subagents, the same lane and validation phases run sequentially, so results and
grounding requirements do not depend on multi-agent support.

## Requirements

Only two ordinary agent capabilities: **web search** and **URL fetch** — the skill
refuses to run without them rather than falling back on model memory. No API keys,
no paid services: it uses public web search plus the arXiv, Semantic Scholar,
OpenAlex and CrossRef APIs, all callable anonymously. Native subagents are optional.
`install.py` needs Python 3 and has no dependencies; installation is unchanged by
the multi-agent preference.

Two anonymous-access caveats the skill handles by switching sources rather than
failing: Semantic Scholar throttles anonymous traffic through one shared pool (it
retries with backoff), and OpenAlex has been usage-metered since Feb 2026, giving
roughly 100 anonymous searches/day (it reserves those for cross-checks). A free
key for either raises the ceiling but is not required.

## Notes

- Citation counts differ between sources; the skill states which it used and when.
- The newest SOTA work has ~0 citations by nature, so citation floors carry a
  3-month recency exemption rather than silently excluding it.
- "SOTA" is benchmark-relative — pin the benchmark and metric when one exists.
- `.github/HarnessFlow/` is an unrelated vendored helper pack used to build this
  project. It is not a dependency; nothing here references it.
# search-sota-papers
