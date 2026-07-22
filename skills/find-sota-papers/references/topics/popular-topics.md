# Popular Research Fields — snapshot 2026-07-20

A dated seed list of the research **fields** that were demonstrably active when it
was written, each with a one-sentence **intuition**, a column of **hot sub-areas**
that doubles as query vocabulary, and a live URL that evidenced it. Its jobs are
to give you a starting vocabulary for the `topics` field, and to carry the
**topic keys** that select institution list files.

> **This is a snapshot, not a live signal — and it will go stale.** The skill it
> belongs to treats unavailable archival leaderboards as non-current, so it has
> to say the same about its own snapshot. Every field below was evidenced by a page fetched on
> 2026-07-20 and nothing here has been re-checked since. Use it to *phrase* a
> search, never as evidence that something is currently SOTA — that is what a
> run of the skill is for. When it starts feeling dated, regenerate it rather
> than trusting it.

Scope: the major fields of AI/ML research and its scientific applications — the
areas this project is used for. Rows are deliberately **broad fields** (CV, NLP,
RL, robotics, bioinformatics, …); the specific movement within each lives in the
*Hot sub-areas* column. Intuitions are one sentence by design, matching the
`minimalism` presentation the skill emits.

## How this connects to the institution filter

A field key here can carry its own **institution list file** under
`institutions/`, indexed by `institutions.md` beside this file. When
`institutions` is `reputable`:

- `institutions/general.md` — the **general list** of 147 institutions — always
  applies;
- if the topic matches a key that has a file — the keyed fields in the table
  below (`robotics`, `bioinformatics`, `ai4science`, `medical`,
  `autonomous-driving`, `ai-safety`, `speech`, `recsys`) — the accept-list is the
  general list **plus** that file's entries; a cross-disciplinary topic can match
  more than one, and their entries are then unioned;
- if the topic matches nothing here, the **general list alone** applies. That is
  the ordinary case for any topic outside this snapshot, and it is never a
  reason to skip the filter.

So this list does not gate anything. It only widens the accept-list where a
general-purpose ranking under-serves a specialty — robotics being the case that
motivated it. The authoritative statement of what a key matches lives in that
key's file, not here: this file is topic vocabulary and gets regenerated.

## The fields

| Field | Topic key | Intuition | Hot sub-areas (mid-2026) | Evidenced by |
|---|---|---|---|---|
| Natural language processing / LLMs | — | Train a transformer by next-token prediction over massive text, then instruction-tune and RL-align it into a general reasoning and generation engine. | Test-time-compute reasoning, diffusion LMs, long-context & linear attention, RL with verifiable rewards | [LLM research papers 2026](https://magazine.sebastianraschka.com/p/llm-research-papers-2026-part1) |
| Computer vision | — | Turn raw pixels into semantic, geometric, or generative structure — detection, segmentation, 3D, image and video synthesis — with convolutional or transformer backbones. | 3D Gaussian splatting & novel-view synthesis, video generation, open-vocabulary detection/segmentation | [CVPR 2026 technical program](https://cvpr.thecvf.com/Conferences/2026/News/Technical_Program) |
| Multimodal / vision-language models | — | Feed visual tokens into a language model — or align both in a shared space — so one network reasons and generates across images, video, and text. | Any-to-any models, document/OCR VLMs, video-language, unified understanding + generation | [VLM survey of 26K papers (arXiv:2510.09586)](https://arxiv.org/abs/2510.09586) |
| Reinforcement learning | — | Optimize a policy by trial and error against a reward signal — now the core recipe for aligning and "agentifying" LLMs. | RL with verifiable rewards (RLVR), agentic RL, preference optimization, offline RL | [Agentic RL survey (arXiv:2509.02547)](https://arxiv.org/abs/2509.02547) |
| Generative modeling / diffusion & flow | — | Train a network to reverse a noising process — predicting the score or velocity that transports noise to data — then generate by integrating that transport. | Flow matching, few-step & consistency samplers, autoregressive image models | [ICML 2026 awards](https://blog.icml.cc/2026/07/05/announcing-the-icml-2026-awards/) |
| LLM agents / agentic AI | — | Wrap a model in a perceive-plan-act loop that emits tool calls, observes each result, and iterates until a multi-step task is done. | Coding agents, GUI / computer-use agents, tool use, agent memory & context engineering | [Agentic programming survey (arXiv:2508.11126)](https://arxiv.org/abs/2508.11126) |
| Robotics | `robotics` | Fuse a vision-language model with an action decoder so one policy maps camera frames plus an instruction straight to motor commands, trained by imitation over multi-embodiment data. | Vision-language-action (VLA) models, dexterous manipulation, humanoids, robot foundation models | [CoRL 2025 papers](https://github.com/smallfryy/corl-2025-papers) |
| ML systems / efficient ML ⚠ | — | Cut the compute, memory, and latency of large models through quantization, conditional Mixture-of-Experts routing, and serving tricks like KV-cache management. | Quantization, mixture-of-experts, speculative decoding, long-context KV-cache serving | [arXiv:2603.19172](https://arxiv.org/abs/2603.19172) |
| AI safety / interpretability | `ai-safety` | Reverse-engineer the circuits and features inside a trained network so alignment rests on verified internal mechanisms, not just input-output behavior. | Mechanistic interpretability, sparse autoencoders, activation steering, scalable oversight | [Mech-interp for alignment survey (arXiv:2602.11180)](https://arxiv.org/abs/2602.11180) |
| Graph machine learning ⚠ | — | Build node and graph embeddings by passing and aggregating messages along edges, making each representation a permutation-invariant function of its neighborhood. | Graph foundation models, scalable GNNs, geometric / equivariant networks | [arXiv:2603.22984](https://arxiv.org/abs/2603.22984) |
| Speech & audio | `speech` | Tokenize continuous audio into discrete units and model them autoregressively, unifying recognition, synthesis, and generation as next-token prediction over speech tokens. | Spoken language models, neural TTS / voice cloning, streaming ASR, audio generation | [Spoken language models survey (arXiv:2504.08528)](https://arxiv.org/abs/2504.08528) |
| Recommender systems & information retrieval | `recsys` | Assign items semantic-ID token sequences and train a sequence model to generate the next item, collapsing retrieval and ranking into one decoder. | Generative retrieval & semantic IDs, LLM-based recommenders, retrieval-augmented generation | [RecSys 2025 accepted contributions](https://recsys.acm.org/recsys25/accepted-contributions/) |
| Time-series analysis & forecasting ⚠ | — | Pretrain a transformer on heterogeneous temporal data so it forecasts unseen series zero-shot by in-context learning, with no task-specific retraining. | Forecasting foundation models, zero-shot forecasting, anomaly detection | [arXiv:2510.26777](https://arxiv.org/abs/2510.26777) |
| Autonomous driving | `autonomous-driving` | Replace the hand-built perception-prediction-planning stack with a learned world model that rolls out future sensor states and plans by scoring imagined futures. | Driving world models, end-to-end driving, occupancy prediction, closed-loop simulation | [Driving world-models survey (arXiv:2502.10498)](https://arxiv.org/abs/2502.10498) |
| Bioinformatics / computational biology | `bioinformatics` | Pretrain transformers on amino-acid and nucleotide sequences so learned evolutionary constraints decode into structure, function, and de-novo designs. | Protein language models, structure prediction, genomics foundation models, de-novo design | [Transformers in Protein survey (arXiv:2505.20098)](https://arxiv.org/abs/2505.20098) |
| AI for Science | `ai4science` | Train neural surrogates that learn a physical system's dynamics from data, replacing or accelerating expensive numerical solvers for weather, molecules, and materials. | Weather/climate models, ML interatomic potentials, materials discovery, PDE surrogates | [AIMIP Phase 1 AI weather/climate eval (arXiv:2605.06944)](https://arxiv.org/abs/2605.06944) |
| Medical / healthcare AI | `medical` | Self-supervise foundation models on large clinical image and text corpora, then adapt them with little labeled data to diagnostic tasks. | Medical-imaging foundation models, clinical LLMs, pathology/radiology, EHR modeling | [Medical-imaging FM review (arXiv:2506.09095)](https://arxiv.org/abs/2506.09095) |
| ML theory & optimization ⚠ | — | Prove how gradient descent drives feature learning — analyzing training-dynamics phases, lazy vs. feature-learning regimes, and loss-landscape geometry. | Feature-learning dynamics, optimizer analysis, generalization, scaling laws | [Alternating gradient flows (arXiv:2506.06489)](https://arxiv.org/abs/2506.06489) |

⚠ **Weaker evidence.** These rows rest on an individual arXiv paper rather than a
conference-level trend statistic or a trending listing — enough to show the field
is active, but not to show it is *rising* the way a program-wide theme breakdown
does. Flagged rather than dropped, and flagged rather than quietly presented as
equal to the conference-evidenced rows.

## Regenerating this file

Ask the skill's usual sources what is moving — Hugging Face trending papers,
recent arXiv listings in cs.AI / cs.LG / cs.CV / cs.CL / cs.RO / q-bio, and
accepted-paper theme breakdowns from the last NeurIPS / ICML / ICLR / CVPR / ACL /
CoRL / RecSys — then rewrite the table, bump the snapshot date, and keep one live
URL per row. Keep rows at the level of a broad field and push the specifics into
*Hot sub-areas*. Drop a field when you can no longer evidence it; a row you cannot
re-evidence is the whole failure mode this file warns about at the top.
