# Reputable Institutions — index and procedure

The entry point behind the `institutions` input. Read this when `institutions`
resolves to `reputable` (Step 6 of `SKILL.md`).

**This file holds the procedure, not the lists.** The lists live in
`institutions/`, one file per topic key, so a run loads only the lists it
actually needs instead of every topic ever added.

> **Provenance — read before trusting any ordering.** `general.md` and
> `robotics.md` are **curated lists supplied by the project owner**, snapshot
> **2026-07-19**, reproduced as supplied. The seven specialty files
> (`bioinformatics`, `ai4science`, `medical`, `autonomous-driving`, `ai-safety`,
> `speech`, `recsys`) were **generated on 2026-07-20** alongside a regeneration
> of `popular-topics.md`. **None** of these lists is independently re-derived and
> **no rank in any of them is verified**. Treat membership as a coarse
> reputational band, never as a measured score, and never report a tier or
> position back to the user as though it were a published rank.

The lists are deliberately **institution-level, not paper-level**. They say
nothing about whether a given paper is good — only "did anyone on this author
list come from an organization on the list."

## Topic index — which files to read

| File | Entries | Read it when |
|---|---|---|
| `institutions/general.md` | 147 — Tiers 1–4 (AI-specific signals) plus a broad research-excellence band (general research indices) | **Always**, on every run of the gate. |
| `institutions/robotics.md` | 10 robotics specialists, none duplicating a general entry | The topic matches `robotics`: robot learning, manipulation, locomotion, humanoids, embodied AI, navigation/SLAM, field robotics, robot foundation models. |
| `institutions/bioinformatics.md` | 9 computational-biology specialists | The topic matches `bioinformatics`: computational biology, protein/genomics foundation models, structure prediction, sequence analysis, single-cell / multi-omics, molecular design. |
| `institutions/ai4science.md` | 9 national labs and physics/forecasting centers | The topic matches `ai4science`: ML for physics/chemistry, materials discovery, interatomic potentials, weather/climate models, PDE / neural surrogates, scientific computing. |
| `institutions/medical.md` | 9 clinical-AI and medical-imaging institutions | The topic matches `medical`: healthcare AI, clinical foundation models / LLMs, medical imaging, computational pathology and radiology, EHR modeling. |
| `institutions/autonomous-driving.md` | 10 self-driving companies and automotive labs | The topic matches `autonomous-driving`: self-driving, robotaxis, driving world models, end-to-end driving, driving perception/prediction, ADAS. |
| `institutions/ai-safety.md` | 10 safety, interpretability, and evaluation orgs | The topic matches `ai-safety`: alignment, mechanistic interpretability, sparse autoencoders, activation steering, scalable oversight, capability evaluations, AI control. |
| `institutions/speech.md` | 8 speech-and-audio specialists | The topic matches `speech`: ASR, TTS / voice cloning, spoken language models, speaker/language ID, anti-spoofing, audio/music generation. |
| `institutions/recsys.md` | 7 recommendation-and-retrieval specialists | The topic matches `recsys`: recommender systems, information retrieval, generative retrieval / semantic IDs, learning-to-rank, neural ranking. |

**Every other topic — including every unkeyed topic in `popular-topics.md` —
resolves to `general.md` alone.** That is the ordinary case, not a failure.
Each file is linked directly from this table: read the ones the procedure below
selects, and no others.

## Resolving the accept-list

`general.md` is always in force. Topic files extend it; they never replace or
narrow it.

1. **Read `institutions/general.md`.** All 147 entries are one flat accept-list;
   the tier/band grouping records where an entry's reputation was measured and
   carries no precedence.
2. **Match the user's `topics` against the keys in *Topic index*.** A match is a
   plain reading of intent, not string equality: "VLA models for manipulation",
   "legged locomotion", and "robot learning" all match `robotics`.
3. **If a topic matches a key that has a file**, read that one file too; the
   accept-list is the general list **+** its entries. If more than one keyed file
   matches — a cross-disciplinary topic can — read each and **union** them. Topic
   files are purely additive and never conflict, so there is nothing to
   arbitrate.
4. **If no topic matches, or a matched topic has no file yet** — the accept-list
   is **the general list alone**. This is the normal case, not a failure, and it
   is never a reason to refuse the filter or to fall back to `any`.
5. **State in one line which accept-list you resolved** ("general list", or
   "general + robotics"), so the report says what it filtered on.

## Adding a topic file

A new topic file is a content change under `institutions/` plus one row in the
index above — no code and no `SKILL.md` change.

1. Create `institutions/<key>.md`, opening with the key, a one-line statement of
   **what the key matches** (authoritative *here*, not in `popular-topics.md`,
   which is regenerable topic vocabulary), and the "additive, never instead of
   `general.md`" note.
2. List only organizations **strong at that topic yet absent from `general.md`**
   — the reason `robotics` exists — each with a one-line focus. Re-slicing
   `general.md` into a "who is good at X" subset is **not** what these files are:
   those entries are already accepted on every run, and a hand-made subset would
   narrow the accept-list, drop listed institutions as `no-match`, and assert a
   per-subfield ranking nothing in this project measures.
3. If a topic has no organizations meeting (2), **do not create a file for it.**
   The general list alone is the correct, documented answer.

## Establishing a paper's affiliation

Affiliation metadata is **much sparser than citation metadata**, and the gap is
worst exactly where this skill spends most of its time: recent arXiv preprints.
Verified live on 2026-07-19 against `arXiv:2406.09246` (OpenVLA):

| Source | Result |
|---|---|
| arXiv **HTML full text** (`arxiv.org/html/<id>v<N>`) | **Affiliations present and readable** — Stanford, UC Berkeley, TRI, Google DeepMind, Physical Intelligence |
| arXiv **abs** page (`arxiv.org/abs/<id>`) | **No affiliations at all** — do not look here |
| arXiv API Atom (`arxiv:affiliation`) | Optional field, **effectively never populated** (0 of 5 sampled papers) |
| OpenAlex `authorships[].institutions[]` | Schema is rich, but **0 of 18 authors populated** for this preprint |
| Semantic Scholar `fields=authors.affiliations` | Author-**profile** level, not per-paper; frequently empty; throttled (live 429) |
| Crossref `author[].affiliation[]` | Publisher-deposited — useful only once a paper has a real venue DOI |

So work **down** this ladder and stop at the first source that answers:

1. **The paper itself.** `https://arxiv.org/html/<id>v<N>` (or the PDF first
   page) — the author block under the title. Authoritative, and the only source
   that reliably answers for a preprint. This is one extra fetch beyond the
   Step-5 canonical check, so do it only for candidates that survive to the
   institution gate, never for the whole candidate pool.
2. **OpenAlex**, for anything with a real venue DOI. Free single-entity GET:
   `https://api.openalex.org/works/doi:<lowercase-doi>` — note the DOI must be
   **lowercase** (`10.48550/arxiv.2406.09246`), and papers older than arXiv's
   DataCite DOIs (pre-2022) have no arXiv DOI at all. Read
   `authorships[].institutions[].{display_name,ror,lineage}` and
   `authorships[].raw_affiliation_strings[]`. A `filter=` query costs $0.0001,
   ten times less than a `search=` query — prefer it.
3. **Semantic Scholar** `?fields=authors.name,authors.affiliations` — treat a
   hit as weak evidence (it is the author's profile affiliation, which may be
   their current employer rather than their affiliation on this paper).
4. **Crossref** `/works/{doi}` → `author[].affiliation[].name`, for published
   versions.
5. **The project or venue page** — lab pages routinely name the institution.

If all five come back empty, the affiliation is `unresolved`. That is a
metadata-coverage fact about the sources, **not** evidence that the authors are
unaffiliated with a reputable institution — never record it as the latter.

## Matching rules

- **Match on whole words, never substrings.** Verified failure: `grep -i mit`
  against the OpenVLA HTML matched **29 times**, inside *submit*, *limit*, and
  *transmit*. Short acronyms (MIT, NUS, NTU, UCL, IIT, ANU, KIT, HKU) must be
  matched with word boundaries and, where possible, confirmed against a longer
  form in the same author block.
- **Several accept-list names differ by one word and are different
  institutions.** All of these pairs are on the list simultaneously:
  *University of Washington* vs *Washington University in St. Louis*;
  *Columbia University* vs *University of British Columbia*;
  *University of Sydney* vs *University of New South Wales (UNSW Sydney)*;
  *University of Pennsylvania* vs *Pennsylvania State University*. Read the
  whole name before recording a match — this exact confusion was caught during
  authoring, when substring matching folded all four pairs together.
- **`IIT` is ambiguous, and both readings can be on the list at once.** On a
  robotics topic the accept-list holds both *Indian Institute of Technology*
  (`general.md`, Tier 4) and *Istituto Italiano di Tecnologia*
  (`institutions/robotics.md`). Either way the paper is a `match`, so the outcome
  is never in doubt — but the ledger records *which* institution qualified it, so
  resolve the bare acronym from the city, department, or country in the same
  affiliation string before writing a name down. If it stays ambiguous, record
  the raw affiliation string rather than picking one.
- **Any one author qualifies the paper**, and any one of *that author's*
  affiliations qualifies the author. Multi-affiliation authors are common, not
  an edge case — OpenAlex returns two institutions for a single author on the
  Transformer paper.
- **Walk the lineage.** A lab, department, or institute resolves to a child
  record whose parent is the listed institution: "Stanford AI Lab" → Stanford,
  "MSR Asia" → Microsoft Research. OpenAlex exposes this as
  `institutions[].lineage`; ROR as `relationships[]` typed `parent`/`child`.
  Count a child as a match for its listed parent.
- **Industry labs are institutions here**, and their internal structure is
  messy: OpenAlex holds "Google DeepMind" and "Google Research" as distinct
  records under Alphabet. The Tier-1 entry is deliberately written
  "Google — DeepMind + Research", so both count.
- **Resolve name variants by retrieval, not by memory.** For a raw affiliation
  string that does not obviously match, call ROR's affiliation matcher —
  `https://api.ror.org/v2/organizations?affiliation=<url-encoded-string>` — and
  use the entry flagged `chosen: true`. ROR's own guidance is to **ignore the
  confidence score** and treat "nothing chosen" as unmatched. This handles
  acronyms, non-English names, and transliteration variants (Tsinghua/清华,
  Seoul National/서울대학교) without anyone hand-writing an alias table.
- **Do not invent an alias.** If a string cannot be resolved by retrieval, it is
  `unresolved` — the same standard the rest of this skill applies to titles,
  venues, and citation counts.

## Outcomes

Every candidate reaching the institution gate gets exactly one:

| Outcome | Meaning | Effect |
|---|---|---|
| `match` | An author's affiliation resolved to an accept-list entry (or its child) | Keep. Record the institution that matched and the evidence URL. |
| `no-match` | Affiliations were established, and none is on the accept-list | Drop. Reason: `institution: not on accept-list (<resolved institutions>)`. |
| `unresolved` | The full ladder ran and no affiliation could be established | Drop. Reason: `institution: affiliation unresolved`. |

`unresolved` and `no-match` are **different findings and must not be merged in
the report.** A run that drops eight papers because their affiliations were
never published has discovered a limitation of the sources; a run that drops
eight papers because they came from unlisted institutions has applied the
filter. Report the two counts separately, and when `unresolved` exceeds roughly
a fifth of the verified set, say so under *Coverage & limitations* — at that
point the filter is measuring metadata availability as much as institution
quality, and the user should know before reading the list.
