# Popular Research Topics — snapshot 2026-07-19

A dated seed list of research directions that were demonstrably active when it
was written, each with a one-sentence **intuition** and a live URL that
evidenced it. Its jobs are to give you a starting vocabulary for the `topics`
field, and to carry the **topic keys** that select institution list files.

> **This is a snapshot, not a live signal — and it will go stale.** The skill it
> belongs to treats unavailable archival leaderboards as non-current, so it has
> to say the same about its own snapshot. Every topic below was evidenced by a page fetched on
> 2026-07-19 and nothing here has been re-checked since. Use it to *phrase* a
> search, never as evidence that something is currently SOTA — that is what a
> run of the skill is for. When it starts feeling dated, regenerate it rather
> than trusting it.

Scope: AI/ML, NLP, CV, multimodal, agents, robotics, systems — the areas this
project is used for. Intuitions are one sentence by design, matching the
`minimalism` presentation the skill emits.

## How this connects to the institution filter

A topic key here can carry its own **institution list file** under
`institutions/`, indexed by `institutions.md` beside this file. When
`institutions` is `reputable`:

- `institutions/general.md` — the **general list** of 147 institutions — always
  applies;
- if the topic matches a key that has a file — marked **`robotics`** in the
  table below — the accept-list is the general list **plus** that file's
  entries, and that file is the only extra one loaded;
- if the topic matches nothing here, the **general list alone** applies. That is
  the ordinary case for any topic outside this snapshot, and it is never a
  reason to skip the filter.

So this list does not gate anything. It only widens the accept-list where a
general-purpose ranking under-serves a specialty — robotics being the case that
motivated it. The authoritative statement of what a key matches lives in that
key's file, not here: this file is topic vocabulary and gets regenerated.

## The topics

| Topic | Field | Topic key | Intuition | Evidenced by |
|---|---|---|---|---|
| Agentic AI / LLM agents | Agents | — | Wrap a model in a loop that plans, calls tools, and acts over many steps instead of returning a single answer. | [ICML 2026 workshop analysis](https://blog.icml.cc/2026/04/06/announcing-the-icml-2026-workshops-and-affinity-workshops/) |
| Agentic RL / RL with verifiable rewards (RLVR) | AI/ML | — | Reward the model only when a program can check the answer was right, removing the human preference labeller from the loop. | [arXiv:2606.28166](https://arxiv.org/abs/2606.28166) |
| World models / physical AI | AI/ML, Robotics | `robotics` | Learn to predict how the world changes under an action, so an agent can imagine consequences before committing to one. | [arXiv:2606.16533](https://arxiv.org/abs/2606.16533); [CVPR 2026 report](https://hirokatsukataoka.net/temp/presen/260611CVPR2026Report_FinalizedVer.pdf) |
| Vision-Language-Action (VLA) models | Robotics | `robotics` | Fuse a vision-language model with an action decoder so one network maps pixels plus an instruction straight to motor commands. | [ICLR 2026 VLA submissions analysis](https://mbreuss.github.io/blog_post_iclr_26_vla.html) |
| Embodied AI / spatial understanding & navigation | Robotics, CV | `robotics` | Teach agents to understand and act inside physical 3D space rather than classify isolated images. | [CVPR 2026 report](https://hirokatsukataoka.net/temp/presen/260611CVPR2026Report_FinalizedVer.pdf) |
| Video generation | Multimodal, CV | — | Extend diffusion to temporally coherent video, increasingly used as a stand-in for learned physics. | [CVPR 2026 report](https://hirokatsukataoka.net/temp/presen/260611CVPR2026Report_FinalizedVer.pdf) |
| Vision-language models / multimodal LLMs | Multimodal | — | Give a language model sight, so it reasons over images, video, and text jointly. | [CVPR 2026 report](https://hirokatsukataoka.net/temp/presen/260611CVPR2026Report_FinalizedVer.pdf) |
| Diffusion language models | NLP | — | Generate a whole sequence by iteratively denoising it in parallel instead of strictly left to right. | [arXiv:2508.10875](https://arxiv.org/abs/2508.10875) |
| Test-time compute scaling / inference-time reasoning | NLP, AI/ML | — | Let a model think longer at inference — longer chains, more attempts — instead of only scaling training. | [arXiv:2606.08231](https://arxiv.org/abs/2606.08231) |
| GUI / computer-use agents | Agents, Systems | — | Train agents to drive ordinary software by looking at the screen and clicking, so no custom API is needed. | [arXiv:2602.16855](https://arxiv.org/abs/2602.16855); [arXiv:2601.20650](https://arxiv.org/abs/2601.20650) |
| Coding agents / agentic software engineering | Agents | — | Hand a model a terminal, a filesystem, and a test suite, and let it iterate on its own code. | [Hugging Face trending papers](https://huggingface.co/papers/trending) |
| Context engineering / agent memory | Agents, Systems | — | Reliability now turns on curating exactly what enters a limited context window each step, not on prompt wording. | [arXiv:2606.24775](https://arxiv.org/abs/2606.24775) |
| Mechanistic interpretability | AI safety | — | Reverse-engineer the circuits inside a trained network to explain how it computes, not just what it outputs. | [arXiv:2606.24026](https://arxiv.org/abs/2606.24026); [arXiv:2606.26523](https://arxiv.org/abs/2606.26523) |
| Synthetic data for pretraining / scaling laws | AI/ML | — | With high-quality web text running out, generate the data instead and test whether the scaling curves still hold. | [arXiv:2606.19781](https://arxiv.org/abs/2606.19781) |
| Linear attention / state-space models for long context | AI/ML, Systems | — | Replace quadratic attention with recurrent or linear-time alternatives to read far longer sequences affordably. | [arXiv:2510.27258](https://arxiv.org/abs/2510.27258); [arXiv:2605.06946](https://arxiv.org/abs/2605.06946) |
| Speculative decoding / efficient inference | Systems | — | A small draft model guesses several tokens ahead and the large model verifies them at once, batching what used to be serial. | [arXiv:2607.05147](https://arxiv.org/abs/2607.05147) |
| Mixture-of-Experts architectures | AI/ML, Systems | — | Route each token to a few specialist sub-networks, so capacity grows without compute growing with it. | [arXiv:2605.17598](https://arxiv.org/abs/2605.17598) |
| AI4Science / protein and scientific foundation models | AI4Science | — | Apply language-model pretraining recipes to biological and chemical data to predict structure and design molecules. | [arXiv:2605.16331](https://arxiv.org/abs/2605.16331); [arXiv:2604.17406](https://arxiv.org/abs/2604.17406) |
| Document-parsing / OCR vision-language models | Multimodal | — | Let a VLM read a rendered document end to end — tables, formulas, layout — instead of chaining a classic OCR pipeline. | [Hugging Face trending papers](https://huggingface.co/papers/trending) |
| Retrieval-augmented / search agents | NLP, Agents | — | Let the model issue its own searches and read what comes back, grounding answers in retrieval rather than memory. | [Hugging Face trending papers](https://huggingface.co/papers/trending) |
| Small / on-device speech and language models | NLP, Systems | — | Compress capable models until they run on edge hardware instead of requiring a cloud GPU. | [Hugging Face trending papers](https://huggingface.co/papers/trending) |
| 3D Gaussian splatting / novel-view synthesis ⚠ | CV | — | Represent a scene as a cloud of soft blendable blobs, so it renders in real time yet still trains by gradient descent from photos. | [arXiv:2604.23551](https://arxiv.org/abs/2604.23551); [arXiv:2602.20342](https://arxiv.org/abs/2602.20342) |

⚠ **Weaker evidence.** This one rests on individual 2026-dated arXiv papers
rather than a conference-level trend statistic or a trending listing — active,
but not demonstrably *rising* the way the others are. Flagged rather than
dropped, and flagged rather than quietly presented as equal.

## Regenerating this file

Ask the skill's usual sources what is moving — Hugging Face trending papers,
recent arXiv listings in cs.AI / cs.LG / cs.CV / cs.CL / cs.RO, and accepted-paper
theme breakdowns from the last NeurIPS / ICML / ICLR / CVPR / CoRL / ICRA — then
rewrite the table, bump the snapshot date, and keep one live URL per row. Drop a
topic when you can no longer evidence it; a row you cannot re-evidence is the
whole failure mode this file warns about at the top.
