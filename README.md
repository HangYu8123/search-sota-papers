# Find SOTA Papers

An agent skill that finds **state-of-the-art research papers** for a field and topic
under explicit constraints — and verifies every paper actually exists before listing
it, so you don't get fabricated citations.

## Why it exists

In OpenScholar's recent-literature evaluation, vanilla GPT-4o without retrieval
fabricated citations in **78–90% of tested cases**
([*Nature*, 2026](https://www.nature.com/articles/s41586-025-10072-4)).
This skill is retrieval-grounded by construction: it never lists a paper from memory,
it fetches every candidate to confirm the link resolves, and it **refuses to pad** the
list — if fewer papers survive verification than you asked for, it reports the
shortfall and why.

## Key design

- **Iterative search, not single-shot.** Each lane seeds several phrasings, harvests
  the vocabulary the literature actually uses, re-searches with those terms, then walks
  the citation graph in both directions — and keeps going until two consecutive rounds
  turn up nothing new.
- **Multi-agent acceleration.** When the host supports subagents, distinct search
  directions run in parallel and candidates are validated across scholarly sources in a
  separate parallel wave. Falls back to sequential execution transparently.
- **Institution filtering.** Set `institutions` to `reputable` to keep only papers
  from a curated accept-list of 147 universities, labs, and research organizations —
  with topic-specific extensions (robotics today, more later).
- **Structured result files.** CLI runs save a machine-readable record to
  `results/<slug>_<date>.md` with frontmatter, a verification ledger, and a
  dropped-candidates table. Each LIVE row preserves canonical, citation, SOTA,
  content, and applicable affiliation evidence URLs.
- **Evaluation pipeline.** Rate runs with `evaluate_results_gui.html`, export to
  preference pairs / rubric rewards / RLVR checks via `evaluations/export.py`.
  Schema and reward math: `EVALUATION.md`.
- **Explicit capability fallbacks.** Live web search and HTTPS fetch are required.
  Semantic Scholar batch calls use optional HTTP POST and fall back to individual
  GETs; result files require optional filesystem writes. A free OpenAlex API key
  is strongly recommended because anonymous daily credit is very limited.
  `install.py` itself needs only Python 3 and has no dependencies.

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

Then start a new agent session:

- **Claude Code** — invoke as `/find-sota-papers` or ask in plain language.
- **Codex** — invoke via `/skills` or `$find-sota-papers`. If the skill doesn't
  appear, re-run with `--legacy-codex` to install to `~/.codex/skills` as well.
- **claude.ai** — run `--target claude-zip`, then Settings → Customize → Skills →
  Upload. Enable *Code Execution and File Creation* first.
- **ChatGPT** — run `--target chatgpt`, restart, open Plugins → Personal → install
  **Find SOTA Papers**. Or use `--target chatgpt-zip` for a portable marketplace
  package.

## Use it

Ask in plain language, or build a precise prompt with **`find_papers_gui.html`** —
a single static page, no server, no dependencies — double-click it, set the
constraints with fields and buttons, copy the prompt:

> Find the SOTA papers on vision-language-action models for robot manipulation.
> Since 2024-01, at least 50 citations, 30 papers, grouped by technique, minimal
> format, and include the classic work they all build on.

### The constraints

| Constraint | Default | Notes |
|---|---|---|
| Field | required | AI, Robotics, CV, NLP, ... |
| Topics | required | The specific direction |
| SOTA requirements | required | The bar a paper must clear to count as state of the art — a benchmark + metric, or "current best approaches" |
| Other requirements | — | e.g. must have public code, open weights |
| No earlier than | — | `YYYY-MM` or `YYYY-MM-DD` |
| Min citations | — | Total and/or per month since publication |
| Institutions | `any` | `reputable` keeps only papers from the curated accept-list |
| List by | `category` | `category` (tech track) or `timeline` |
| Present as | `minimalism` | `minimalism` (5-liner) or `abstract` (short intro) |
| Include classic work | `yes` | Adds a shared foundational ancestor, labeled |
| Relationship graph | `yes` | Maps how the selected papers relate — who cites whom, stated build-on links, and which are on separate tracks |
| Multi-agent | `auto` | `auto` / `yes` / `no` — parallel search when available |
| Number of papers | `30` | |
| Result file | `auto` | Writes to `results/`; a path overrides; `no` suppresses |
| Links | always | Every paper carries a working link |

**`minimalism`** gives you, per paper: linked title, then one sentence each for
intuition, core contribution, experiment setup, and results vs. named baselines.

## Project layout

| | |
|---|---|
| `skills/find-sota-papers/SKILL.md` | The skill itself, in the open [Agent Skills](https://agentskills.io) format. |
| `skills/find-sota-papers/references/` | Routed API, search-depth, orchestration, graph, result-schema, topic, and institution guidance. |
| `find_papers_gui.html` | Prompt builder — set constraints, copy the prompt. |
| `evaluate_results_gui.html` | Score a finished run and save feedback. |
| `install.py` | Install or package for Claude, Codex, ChatGPT. |
| `EVALUATION.md` | Feedback schema, reward math, published-harness sources. |
| `results/` · `evaluations/` | Where runs and their evaluations accumulate. |

## Notes

- Citation counts differ between sources; the skill states which it used and when.
- Every supplied total or per-month citation minimum is a hard floor. There is no
  implicit recency exemption; omit the floor when uncited new work should qualify.
- "SOTA" is benchmark-relative — pin the benchmark and metric when one exists.
- `.github/HarnessFlow/` is an unrelated vendored helper pack; nothing here references it.
