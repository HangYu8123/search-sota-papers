---
schema: find-sota-papers/result@1
run_id: reinforcement-learning-vla-world-model-diffusion-policy_2026-07-20
created: 2026-07-20T14:08:53Z
harness: codex
model: gpt-5
prompt: |
  Use the find-sota-papers skill to find state-of-the-art research papers matching the constraints below.

  Field: Robotics
  Topics: Reinforcement Learning, Vision Language Action Model, VLA, World Model, Diffusion Policy
  SOTA requirements: Best performance at the time, validated with real robots, promising for real world/industrial application.
  Other requirements: SOTA performance on realistic tasks; Industrial Level productions; Real world tasks; Must have real robots.
  No earlier than: 2026-03
  Minimum citations (total): 3
  Minimum citations (per month since publication): 1
  Institutions: reputable — keep only papers with at least one author affiliated with an institution on the skill's curated reputable-institutions accept-list, indexed by topic in references/topics/institutions.md; apply the general list, plus the matched topic's list file when the topic has one, and report institution drops separately from papers whose affiliation could not be established
  Number of papers: 40
  List by: category — group the papers by category / technique track
  Present as: minimalism — title (linked), then one sentence each for intuition, core contribution, experiment setup, and results vs. named baselines
  Include classic work: yes — if the selected SOTA papers share a common prior classic work, include it (clearly labeled)
  Relationship graph: yes — after selecting the final papers, map how they relate to each other — citation edges taken from fetched reference data, build-on edges only where a paper says in its own words that it builds on another, and separate research tracks reported as disconnected clusters; emit it as a plain edge list under a "Relationship graph" heading, and never invent an edge you could not evidence
  Multi-agent: auto — use real subagents for parallel discovery and validation when available and useful; otherwise run sequentially

  Every paper must include a working link. Verify each paper resolves to a real arXiv / DOI / Semantic Scholar entry before listing it — do not list papers from memory and do not fabricate any title, author, link, or citation count. Do not pad the list to reach the requested count: if fewer papers survive verification, return those and state the shortfall and why.
constraints:
  field: Robotics
  topics: Reinforcement Learning, Vision Language Action Model, VLA, World Model, Diffusion Policy
  sota_requirements: best performance at the time, validated with real robots, promising for real-world or industrial application
  other_requirements: realistic tasks, industrial-level production relevance, physical real robots
  no_earlier_than: 2026-03
  min_citations:
    total: 3
    per_month: 1
  institutions: reputable
  institutions_accept_list: general + robotics
  listing: category
  presentation: minimalism
  include_classic: true
  multi_agent: auto
  num_papers: 40
  relationship_graph: true
funnel:
  found: 714
  merged: 656
  filtered: 58
  verified: 35
  selected: 35
grounding:
  links_checked: 58
  non_resolving: 0
  unknown_fields: 0
  citation_source: Semantic Scholar; lower verified count used on OpenAlex conflicts
  citation_checked: 2026-07-20
cost:
  wall_clock_s: unknown
  tokens_total: unknown
  searches: unknown
  fetches: unknown
  subagents: 3
shortfall: 35 of 40 — ten otherwise-eligible papers failed the lower-source citation rule; the remaining drops failed physical-robot, best-at-time, or institution gates.
---

# SOTA Papers — Robotics · Reinforcement Learning, VLA, World Models, Diffusion Policies

## Run summary

Since 2026-03 · SOTA = best-at-time named-baseline performance on realistic physical-robot tasks with industrial promise · citations total≥3 and ≥1/month · reputable institution from `general + robotics` · requested 40 · grouped by technique · minimalism.

Found 714 → merged 656 → filtered 58 → verified 35 → selected 35. Citation counts use Semantic Scholar checked 2026-07-20, with the lower verified count applied wherever OpenAlex disagreed. Shortfall: **35 of 40**; no padding.

## Classic / foundational

- **[Diffusion Policy: Visuomotor Policy Learning via Action Diffusion](https://arxiv.org/abs/2303.04137)** — classic action-diffusion policy cited by 21 of the 35 selected papers.
- **[π0: A Vision-Language-Action Flow Model for General Robot Control](https://arxiv.org/abs/2410.24164)** — foundational flow-matching VLA cited by 27 selected papers.
- **[π0.5: a Vision-Language-Action Model with Open-World Generalization](https://arxiv.org/abs/2504.16054)** — the immediate open-world foundation/baseline cited by 25 selected papers.

## Papers

### World models and diffusion / flow policies

**[Multi-View Video Diffusion Policy: A 3D Spatio-Temporal-Aware Video Action Model](https://arxiv.org/abs/2604.03181)** — Peiyan Li, Yixiang Chen, Yuan Xu, et al.; arXiv; 2026-04-03
- *Intuition:* Predicting coordinated future views gives the action policy implicit 3D and temporal structure. ([paper](https://arxiv.org/html/2604.03181v1))
- *Contribution:* MV-VDP couples multi-view video diffusion with action generation in a 3D-aware video-action model. ([paper](https://arxiv.org/html/2604.03181v1))
- *Setup:* A Franka Research 3 with three ZED2i cameras performs three base and four unseen physical tasks from only ten demonstrations. ([setup](https://arxiv.org/html/2604.03181v1))
- *Results:* It averages 57.10% versus BridgeVLA 41.42%, UVA 5.70%, π0.5 1.40%, and DP3 0%. ([results](https://arxiv.org/html/2604.03181v1))

**[World-Value-Action Model: Implicit Planning for Vision-Language-Action Systems](https://arxiv.org/abs/2604.14732)** — Runze Li, Hongyin Zhang, Junxi Jin, et al.; arXiv; 2026-04-16
- *Intuition:* A learned value over imagined futures can turn world-action prediction into implicit planning. ([paper](https://arxiv.org/html/2604.14732v2))
- *Contribution:* WAV jointly models future observations, values, and actions inside one VLA. ([paper](https://arxiv.org/html/2604.14732v2))
- *Setup:* A dual-arm Piper executes bowl organization, towel flattening, and drawer-open/place/close tasks over 15 trials per task. ([setup](https://arxiv.org/html/2604.14732v2))
- *Results:* WAV averages 75.6% versus the same-backbone GE-ACT at 35.6%, while scoring 98.1 on LIBERO versus VLA-Adapter 97.3 and OpenVLA-OFT 97.1. ([results](https://arxiv.org/html/2604.14732v2))

**[HarmoWAM: Harmonizing Generalizable and Precise Manipulation via Adaptive World Action Models](https://arxiv.org/abs/2605.10942)** — Qiuxuan Feng, Jiale Yu, Jiaming Liu, et al.; arXiv; 2026-05-11
- *Intuition:* World prediction and direct action control should be weighted adaptively so visual generalization does not sacrifice precision. ([paper](https://arxiv.org/html/2605.10942v1))
- *Contribution:* HarmoWAM introduces adaptive world/action harmonization for precise in-distribution and robust OOD manipulation. ([paper](https://arxiv.org/html/2605.10942v1))
- *Setup:* Dual Franka Research 3 arms with three RealSense cameras run four single-arm and two dual-arm physical tasks. ([setup](https://arxiv.org/html/2605.10942v1))
- *Results:* It reaches 89% ID success versus Cosmos-Policy 78%, π0.5 74%, and Wan+AnyPos 67%, with reported OOD gains of 33/29 points over the leading VLA/WAM baselines. ([results](https://arxiv.org/html/2605.10942v1))

**[OFlow: Injecting Object-Aware Temporal Flow Matching for Robust Robotic Manipulation](https://arxiv.org/abs/2604.17876)** — Kuanning Wang, Ke Fan, Chenhao Qiu, et al.; arXiv; 2026-04-20
- *Intuition:* Forecast object-specific semantic motion instead of forcing one latent stream to represent every scene change. ([paper](https://arxiv.org/html/2604.17876v1))
- *Contribution:* OFlow unifies object-aware temporal latent forecasting with continuous action flow matching. ([paper](https://arxiv.org/html/2604.17876v1))
- *Setup:* An ARX X5 arm with two RealSense D435 cameras runs seven physical tasks including moving pickup, handover, stacking, and towel folding. ([setup](https://arxiv.org/html/2604.17876v1))
- *Results:* It averages 69% versus GR00T-N1.5 51% and π0 41%, including 75% handover success versus 50% and 45%. ([results](https://arxiv.org/html/2604.17876v1))

**[Pri4R: Learning World Dynamics for Vision-Language-Action Models with Privileged 4D Representation](https://arxiv.org/abs/2603.01549)** — Jisoo Kim, Jungbin Cho, Sanghyeok Chu, et al.; arXiv; 2026-03-02
- *Intuition:* Privileged 4D supervision can teach dynamics during training without burdening deployment. ([paper](https://arxiv.org/html/2603.01549v2))
- *Contribution:* Pri4R distills 4D world dynamics into ordinary VLAs with no inference-time 4D input or overhead. ([paper](https://arxiv.org/html/2603.01549v2))
- *Setup:* An OMY 6-DoF robot with wrist/external depth cameras is tested on unseen-spatial and OOD physical tasks. ([setup](https://arxiv.org/html/2603.01549v2))
- *Results:* Pri4R raises OpenVLA-OFT from 60→80 unseen-spatial and 50→66.7 OOD, and π0.5 from 30→60 and 33.8→50. ([results](https://arxiv.org/html/2603.01549v2))

**[LaWAM: Latent World Action Models for Efficient Dynamics-Aware Robot Policies](https://arxiv.org/abs/2606.15768)** — Jialei Chen, Kai Wang, Kanghao Chen, et al.; arXiv; 2026-06-14
- *Intuition:* Predict compact latent dynamics rather than pixels to retain world awareness at control-loop latency. ([paper](https://arxiv.org/html/2606.15768v1))
- *Contribution:* LaWAM is a latent world-action model reporting up to 24× lower latency than pixel-space WAMs. ([paper](https://arxiv.org/html/2606.15768v1))
- *Setup:* Franka Panda pick/place and drawer tasks plus Quanta X1 bimanual towel folding are evaluated over 30 trials each. ([setup](https://arxiv.org/html/2606.15768v1))
- *Results:* It averages 90.0% versus π0.5 83.3%, GR00T-N1.6 68.9%, Fast-WAM 63.3%, and LingBot-VA 53.3% at 187 ms. ([results](https://arxiv.org/html/2606.15768v1))

**[Feedback World Model Enables Precise Guidance of Diffusion Policy](https://arxiv.org/abs/2605.15705)** — Tuo An, Jindou Jia, Gen Li, et al.; arXiv; 2026-05-15
- *Intuition:* A world model is most useful when it predicts corrective feedback that can steer the next denoising step. ([paper](https://arxiv.org/html/2605.15705v1))
- *Contribution:* The method guides a diffusion policy with predicted execution feedback without collecting extra rollout data. ([paper](https://arxiv.org/html/2605.15705v1))
- *Setup:* A Galaxea R1 Lite performs peach pick-and-place and drawer opening under OOD initial poses. ([setup](https://arxiv.org/html/2605.15705v1))
- *Results:* Feedback guidance raises the same diffusion policy from 40→80% on peach placement and 20→70% on drawer opening while reducing world-model error by 65.4%/76.4%. ([results](https://arxiv.org/html/2605.15705v1))

### Generalist foundation VLAs and cross-embodiment systems

**[Qwen-VLA: Unifying Vision-Language-Action Modeling across Tasks, Environments, and Robot Embodiments](https://arxiv.org/abs/2605.30280)** — Qiuyue Wang, Mingsheng Li, Jian Guan, et al.; arXiv; 2026-05-28
- *Intuition:* One pretrained model can share visual-language-action structure across tasks, scenes, and robot bodies. ([paper](https://arxiv.org/pdf/2605.30280))
- *Contribution:* Qwen-VLA unifies multi-embodiment pretraining and physical-robot post-training in a generalist foundation policy. ([paper](https://arxiv.org/pdf/2605.30280))
- *Setup:* Physical ALOHA evaluations cover in-domain and OOD task, scene, and embodiment shifts. ([setup](https://arxiv.org/pdf/2605.30280))
- *Results:* It scores 83.6% in-domain versus π0.5 71.6% and GR00T-N1.6 28.6%, and 76.9% OOD, 35.4 points above π0.5. ([results](https://arxiv.org/pdf/2605.30280))

**[Qwen-RobotManip Technical Report: Alignment Unlocks Scale for Robotic Manipulation Foundation Models](https://arxiv.org/abs/2606.17846)** — Haoqi Yuan, Zhixuan Liang, An-Jen Chen, et al.; arXiv; 2026-06-16
- *Intuition:* Scaling robot data only pays off when multimodal representations and action behavior are explicitly aligned. ([paper](https://arxiv.org/pdf/2606.17846))
- *Contribution:* Qwen-RobotManip couples large-scale pretraining with alignment/post-training for a manipulation foundation model. ([paper](https://arxiv.org/pdf/2606.17846))
- *Setup:* AgileX ALOHA, Franka, UR, and ARX robots are evaluated across more than 80 physical tasks. ([setup](https://arxiv.org/pdf/2606.17846))
- *Results:* It reaches 88.6% real in-domain success versus π0.5 42.9% and StarVLA 20.0%, plus 87.5% OOD versus StarVLA 0.0%. ([results](https://arxiv.org/pdf/2606.17846))

**[RLDX-1 Technical Report](https://arxiv.org/abs/2605.03269)** — Dongyoung Kim, Huiwon Jang, Myungkyu Koo, et al.; arXiv; 2026-05-05
- *Intuition:* A generalist VLA needs separate but jointly attended streams for motion, memory, vision, language, and physical sensing. ([paper](https://arxiv.org/html/2605.03269))
- *Contribution:* RLDX-1 introduces a Multi-Stream Action Transformer plus rare-scenario synthesis and real-time inference engineering. ([paper](https://arxiv.org/html/2605.03269))
- *Setup:* Physical OpenArm, ALLEX humanoid, and Franka/tactile systems test dexterity, memory, contact, and dynamic skills. ([setup](https://arxiv.org/html/2605.03269))
- *Results:* On ALLEX functional tasks it averages 86.8% versus GR00T 44.8% and π0.5 39.1%, including 91.7% on memory tasks versus 29.2%/33.3%. ([results](https://arxiv.org/html/2605.03269))

**[StarVLA-α: Reducing Complexity in Vision-Language-Action Systems](https://arxiv.org/abs/2604.11757)** — Ji-lu Ye, Ning Gao, Senqiao Yang, et al.; arXiv; 2026-04-13
- *Intuition:* A simpler VLA can preserve generality while reducing the architectural and training burden of larger systems. ([paper](https://arxiv.org/pdf/2604.11757))
- *Contribution:* StarVLA-α streamlines VLA modeling and deployment while retaining cross-task and cross-robot performance. ([paper](https://arxiv.org/pdf/2604.11757))
- *Setup:* Eleven physical RoboChallenge ARX5 tasks plus Franka Research 3 OOD tests are reported. ([setup](https://arxiv.org/pdf/2604.11757))
- *Results:* It averages 33.6 success/54.5 progress versus π0.5 12.7/27.6 and π0 3.6/14.7. ([results](https://arxiv.org/pdf/2604.11757))

**[Hy-Embodied-0.5-VLA: From Vision-Language-Action Models to a Real-World Robot Learning Stack](https://arxiv.org/abs/2606.14409)** — Heng Zhang, Lingzhu Xiang, Haitao Lin, et al.; arXiv; 2026-06-12
- *Intuition:* Reliable deployment needs a complete data, supervised post-training, reinforcement-learning, and systems stack—not only a pretrained checkpoint. ([paper](https://arxiv.org/pdf/2606.14409))
- *Contribution:* The paper turns HY-Embodied into an end-to-end real-world learning stack with RPRO reinforcement post-training. ([paper](https://arxiv.org/pdf/2606.14409))
- *Setup:* Dobot X-Trainer, JAKA K1, Astribot S1, and Unitree G1 systems run bottle, cap, USB, and zipper tasks. ([setup](https://arxiv.org/pdf/2606.14409))
- *Results:* RPRO reaches 99/99/98/94% versus π0.6* 95/95/95/89 and DAgger 93/88/86/83, with shorter completion times on every task. ([results](https://arxiv.org/pdf/2606.14409))

**[HEX: Humanoid-Aligned Experts for Cross-Embodiment Whole-Body Manipulation](https://arxiv.org/abs/2604.07993)** — Shuanghao Bai, Meng Li, Xinyuan Lv, et al.; arXiv; 2026-04-09
- *Intuition:* Experts aligned to humanoid morphology can share skills across bodies without erasing embodiment-specific control. ([paper](https://arxiv.org/html/2604.07993))
- *Contribution:* HEX combines humanoid-aligned experts with cross-embodiment training for whole-body manipulation. ([paper](https://arxiv.org/html/2604.07993))
- *Setup:* Tienkung 2.0/3.0 humanoids execute seven real whole-body tasks and a long-horizon box-convey sequence after training on seven embodiments and 12M+ frames. ([setup](https://arxiv.org/html/2604.07993))
- *Results:* Generalization averages 61.8% versus π0.5 44.3%, GR00T-N1.5 41.0%, and SwitchVLA 22.4%, with 79.8% overall success at 73.34 ms. ([results](https://arxiv.org/html/2604.07993))

**[MMaDA-VLA: Large Diffusion Vision-Language-Action Model with Unified Multi-Modal Instruction and Generation](https://arxiv.org/abs/2603.25406)** — Yang Liu, Pengxiang Ding, Teng-Long Jiang, et al.; arXiv; 2026-03-26
- *Intuition:* Instruction understanding and multimodal generation should share one diffusion model so perception and action improve together. ([paper](https://arxiv.org/pdf/2603.25406))
- *Contribution:* MMaDA-VLA unifies multimodal instruction following, generation, and diffusion action prediction at scale. ([paper](https://arxiv.org/pdf/2603.25406))
- *Setup:* An AgileX Piper with external/wrist RealSense cameras performs dynamic pickup, stacking, drawer storage, and long-horizon tableware organization. ([setup](https://arxiv.org/pdf/2603.25406))
- *Results:* It scores 83.3–93.3% on four real settings versus GR00T-N1.6 56.7–70.0%, and reports 98.0 LIBERO and 4.78 CALVIN average length. ([results](https://arxiv.org/pdf/2603.25406))

**[A1: A Fully Transparent Open-Source, Adaptive and Efficient Truncated Vision-Language-Action Model](https://arxiv.org/abs/2604.05672)** — Kaidong Zhang, Jian Zhang, Rongtao Xu, et al.; arXiv; 2026-04-07
- *Intuition:* An openly inspectable truncated VLA can deliver useful adaptation and latency without requiring a closed giant model. ([paper](https://arxiv.org/html/2604.05672))
- *Contribution:* A1 provides a transparent adaptive VLA with truncated computation and an open deployment stack. ([paper](https://arxiv.org/html/2604.05672))
- *Setup:* Franka, AgiBot, OpenArm, and Dobot platforms cover seven tasks/3,000+ trajectories plus the 30-task physical RoboChallenge. ([setup](https://arxiv.org/html/2604.05672))
- *Results:* Its four-platform average is 56.7% versus π0.5 47.5% and π0 40.8%, and RoboChallenge is 29.00% versus π0 28.33%, X-VLA 21.33%, and RDT-1B 15.00%, with up to 72% less flow latency. ([results](https://arxiv.org/html/2604.05672))

### Memory, planning, and long-horizon execution

**[MEM: Multi-Scale Embodied Memory for Vision Language Action Models](https://arxiv.org/abs/2603.03596)** — Marcel Torne, Karl Pertsch, Homer Walke, et al.; arXiv; 2026-03-04
- *Intuition:* Recent visual detail and long-term semantic state need different memory representations. ([paper](https://arxiv.org/pdf/2603.03596))
- *Contribution:* MEM combines compressed short-term video memory with text-based long-term memory inside an end-to-end VLA. ([paper](https://arxiv.org/pdf/2603.03596))
- *Setup:* Single-arm, dual-arm, and mobile robots execute six memory categories and tasks lasting up to 15 minutes, including kitchen cleanup and grilled-cheese preparation. ([setup](https://arxiv.org/pdf/2603.03596))
- *Results:* MEM is the only method strong across all six categories versus No Memory, Pool Memory, and Proprio Memory, while matching π0.6 on dexterous non-memory tasks. ([results](https://arxiv.org/pdf/2603.03596))

**[ReMem-VLA: Empowering Vision-Language-Action Model with Memory via Dual-Level Recurrent Queries](https://arxiv.org/abs/2603.12942)** — Hang Li, Fengyi Shen, Dong Chen, et al.; arXiv; 2026-03-13
- *Intuition:* Recurrent queries can preserve both fine recent context and coarse long-range task state without replaying full history. ([paper](https://arxiv.org/pdf/2603.12942))
- *Contribution:* ReMem-VLA adds dual-level recurrent visual-memory queries to a generalist VLA. ([paper](https://arxiv.org/pdf/2603.12942))
- *Setup:* A UR5/Robotiq/RealSense system performs four long-memory physical tasks over 50 trials each. ([setup](https://arxiv.org/pdf/2603.12942))
- *Results:* It averages 82.5% success versus MemoryVLA 8% and π0.5 11%. ([results](https://arxiv.org/pdf/2603.12942))

**[See, Plan, Rewind: Progress-Aware Vision-Language-Action Models for Robust Robotic Manipulation](https://arxiv.org/abs/2603.09292)** — Tianhe Dai, Mingfei Han, Tingwen Du, et al.; arXiv; 2026-03-10
- *Intuition:* Long-horizon policies should detect stalled progress and rewind their plans before errors compound. ([paper](https://arxiv.org/pdf/2603.09292))
- *Contribution:* The framework adds explicit visual progress estimation, planning, and recovery to VLA execution. ([paper](https://arxiv.org/pdf/2603.09292))
- *Setup:* Physical long-horizon manipulation tasks test multi-stage execution and recovery from failed intermediate states. ([setup](https://arxiv.org/pdf/2603.09292))
- *Results:* It scores 70/30/40% on three real tasks versus MolmoAct 50/0/0. ([results](https://arxiv.org/pdf/2603.09292))

**[RoboClaw: An Agentic Framework for Scalable Long-Horizon Robotic Tasks](https://arxiv.org/abs/2603.11558)** — Ruiying Li, Yunlang Zhou, Yuyao Zhu, et al.; arXiv; 2026-03-12
- *Intuition:* An agent should compose, monitor, and improve reusable robot subskills instead of treating a long task as one flat action sequence. ([paper](https://arxiv.org/pdf/2603.11558))
- *Contribution:* RoboClaw provides an agentic data-and-policy framework for scalable long-horizon execution and correction. ([paper](https://arxiv.org/pdf/2603.11558))
- *Setup:* An AgiBot G01 dual-arm mobile robot performs long-horizon vanity-table organization. ([setup](https://arxiv.org/pdf/2603.11558))
- *Results:* It improves success by 25 points over π0.5-only and product-of-subskills baselines while reducing human time by 53.7%. ([results](https://arxiv.org/pdf/2603.11558))

**[Long-Horizon Manipulation via Trace-Conditioned VLA Planning](https://arxiv.org/abs/2604.21924)** — Ian Liu, An-Chieh Cheng, Rui Yan, et al.; arXiv; 2026-04-23
- *Intuition:* Compact execution traces let a slow manager plan while a fast VLA executor handles continuous control. ([paper](https://arxiv.org/html/2604.21924))
- *Contribution:* LoHo-Manip conditions hierarchical VLA planning on task traces for multi-step and OOD execution. ([paper](https://arxiv.org/html/2604.21924))
- *Setup:* A Franka with top/wrist RealSense cameras runs one-, two-, and three-step ID/OOD tasks from 100 demonstrations. ([setup](https://arxiv.org/html/2604.21924))
- *Results:* Versus same-data π0.5, it scores 93% vs 86% one-step ID, 70% vs 60% two-step ID, 75% vs 0% two-step OOD, and 60% vs 0% three-step OOD. ([results](https://arxiv.org/html/2604.21924v1/x7.png))

**[IntentVLA: Short-Horizon Intent Modeling for Aliased Robot Manipulation](https://arxiv.org/abs/2605.14712)** — Shijie Lian, Bin Yu, Xiaopeng Lin, et al.; arXiv; 2026-05-14
- *Intuition:* Predicting near-term intent disambiguates visually similar states that require different actions. ([paper](https://arxiv.org/html/2605.14712))
- *Contribution:* IntentVLA adds short-horizon intent modeling for history-dependent manipulation. ([paper](https://arxiv.org/html/2605.14712))
- *Setup:* Dual Franka Research 3 arms clean four snacks into a bag using 300 demonstrations and 50 trials per model. ([setup](https://arxiv.org/html/2605.14712))
- *Results:* It completes at least two/three snacks in 62%/32% of trials versus π0.5 44%/18%, with 1.86 versus 1.44 expected placements. ([results](https://arxiv.org/html/2605.14712))

**[AtomicVLA: Unlocking the Potential of Atomic Skill Learning in Robots](https://arxiv.org/abs/2603.07648)** — Likui Zhang, Tao Tang, Zhihao Zhan, et al.; arXiv; 2026-03-08
- *Intuition:* Learning reusable atomic skills makes long-horizon behavior easier to compose and generalize. ([paper](https://arxiv.org/pdf/2603.07648))
- *Contribution:* AtomicVLA trains and composes atomic manipulation units inside a general VLA. ([paper](https://arxiv.org/pdf/2603.07648))
- *Setup:* A Franka runs three long-horizon and five short physical tasks from 550 demonstrations. ([setup](https://arxiv.org/pdf/2603.07648))
- *Results:* Long-task success averages 56.7% (63.3% for AtomicVLA*) versus π0.5 45% and π0 36.7%. ([results](https://arxiv.org/pdf/2603.07648))

**[TiPToP: A Modular Open-Vocabulary Planning System for Robotic Manipulation](https://arxiv.org/abs/2603.09971)** — William Shen, Nishanth Kumar, Sahit Chintalapudi, et al.; arXiv; 2026-03-10
- *Intuition:* Open-vocabulary perception and planning can exploit pretrained models without any robot-policy training data. ([paper](https://arxiv.org/html/2603.09971))
- *Contribution:* TiPToP modularizes task interpretation, target selection, planning, and execution for zero-shot manipulation. ([paper](https://arxiv.org/html/2603.09971))
- *Setup:* Franka DROID rigs plus independent UR5e/WidowX deployments cover 28 scenes, 165 comparison trials, and 173 diagnostics. ([setup](https://arxiv.org/html/2603.09971))
- *Results:* With zero robot training data it reaches 60.0% distractor-scene success versus π0.5-DROID 26.7% and is about 2× faster on single-step tasks. ([results](https://arxiv.org/html/2603.09971))

### Contact-rich, dexterous, deformable, and dynamic control

**[UniDex: A Robot Foundation Suite for Universal Dexterous Hand Control from Egocentric Human Videos](https://arxiv.org/abs/2603.22264)** — Gu Zhang, Qicheng Xu, Haozhe Zhang, et al.; arXiv; 2026-03-23
- *Intuition:* Egocentric human video can supply transferable dexterous priors across robot hands with very different kinematics. ([paper](https://arxiv.org/pdf/2603.22264))
- *Contribution:* UniDex is a foundation suite for universal hand control and zero-shot cross-hand transfer. ([paper](https://arxiv.org/pdf/2603.22264))
- *Setup:* A Franka arm uses Inspire, Wuji, and Oymotion hands on five physical tool-use tasks. ([setup](https://arxiv.org/pdf/2603.22264))
- *Results:* It reaches 81.0% progress/76.0% success versus Diffusion Policy 29/22, DP3 35/30, and π0 38/35, plus 60%/40% zero-shot transfer. ([results](https://arxiv.org/pdf/2603.22264))

**[ForceVLA2: Unleashing Hybrid Force-Position Control with Force Awareness for Contact-Rich Manipulation](https://arxiv.org/abs/2603.15169)** — Yang Li, Zhaxizhuoma, Hongru Jiang, et al.; arXiv; 2026-03-16
- *Intuition:* Contact-rich work needs a VLA to reason over force while switching continuously between force and position control. ([paper](https://arxiv.org/pdf/2603.15169))
- *Contribution:* ForceVLA2 integrates force awareness with hybrid force-position action generation. ([paper](https://arxiv.org/pdf/2603.15169))
- *Setup:* A force-sensing Kinova Gen3/AG-95 system performs five physical contact-rich tasks. ([setup](https://arxiv.org/pdf/2603.15169))
- *Results:* It averages 66% versus π0 18%, π0.5 31%, ACP 16%, and π0-with-force 17%. ([results](https://arxiv.org/pdf/2603.15169))

**[TacVLA: Contact-Aware Tactile Fusion for Robust Vision-Language-Action Manipulation](https://arxiv.org/abs/2603.12665)** — Kaidi Zhang, Heng Zhang, Zhengtong Xu, et al.; arXiv; 2026-03-13
- *Intuition:* Explicit tactile fusion keeps VLA control grounded when vision is occluded and constraints are locked. ([paper](https://arxiv.org/html/2603.12665))
- *Contribution:* TacVLA adds contact-aware tactile representation and fusion to VLA manipulation. ([paper](https://arxiv.org/html/2603.12665))
- *Setup:* A tactile Franka performs four constraint-locked disassembly tasks and in-box picking with 50 demonstrations per task. ([setup](https://arxiv.org/html/2603.12665))
- *Results:* Mean disassembly is 83.75% versus π0.5 63.75%, image Diffusion Policy 48.75%, and DP3 31.25%; heavy-occlusion picking is 70% versus π0.5 10%. ([results](https://arxiv.org/html/2603.12665))

**[AT-VLA: Adaptive Tactile Injection for Enhanced Feedback Reaction in Vision-Language-Action Models](https://arxiv.org/abs/2605.07308)** — Xiaoqi Li, Mu Cai, Jiadong Xu, et al.; arXiv; 2026-05-08
- *Intuition:* Tactile evidence should be injected only when fast contact feedback is necessary, preserving the VLA's visual-language priors. ([paper](https://arxiv.org/html/2605.07308))
- *Contribution:* AT-VLA adaptively injects touch into the action stream with a 0.04-second tactile control loop. ([paper](https://arxiv.org/html/2605.07308))
- *Setup:* An AgiBot Genie1 performs unzip, stamp, wipe, and unscrew tasks with dual arms, three cameras, and an Xense tactile gripper. ([setup](https://arxiv.org/html/2605.07308))
- *Results:* It scores 0.33/0.46/0.67/0.53 versus GO-1 0.20/0.13/0.07/0.27 and π0.5 0/0.20/0.33/0.46. ([results](https://arxiv.org/html/2605.07308))

**[Dexora: Open-source VLA for High-DoF Bimanual Dexterity](https://arxiv.org/abs/2605.18722)** — Zongzheng Zhang, Jin-Li Pang, Zhuo Yang, et al.; arXiv; 2026-05-18
- *Intuition:* Open hardware, simulation, data, and policy weights can make high-DoF dexterity reproducible instead of bespoke. ([paper](https://arxiv.org/html/2605.18722))
- *Contribution:* Dexora releases a 36-DoF bimanual hand platform, MuJoCo twin, large real/sim corpus, and VLA. ([paper](https://arxiv.org/html/2605.18722))
- *Setup:* Six real tasks cover pen use, book retrieval, cutting, plate placement, dough handling, and cap twisting. ([setup](https://arxiv.org/html/2605.18722))
- *Results:* Dexterous success averages 66.7% versus GR00T-N1 51.7%, π0 26.7%, and Diffusion Policy 6.7%. ([results](https://arxiv.org/html/2605.18722))

**[DeMaVLA: A Vision-Language-Action Foundation Model for Generalizable Deformable Manipulation](https://arxiv.org/abs/2605.31286)** — Taiyi Su, Jian Zhu, Tianjian Wang, et al.; arXiv; 2026-05-29
- *Intuition:* Industrial deformable handling benefits from broad real demonstrations plus targeted human corrections. ([paper](https://arxiv.org/html/2605.31286))
- *Contribution:* DeMaVLA combines roughly 5,000 hours of dual-arm pretraining with real HIL-DAgger post-training. ([paper](https://arxiv.org/html/2605.31286))
- *Setup:* An ALOHA-style dual-arm robot runs five-minute shirt, skirt, pants, and towel pipelines from random basket drops. ([setup](https://arxiv.org/html/2605.31286))
- *Results:* One checkpoint averages 92.5% versus fine-tuned π0 76.3%, including towel folding 100% versus 55%. ([results](https://arxiv.org/html/2605.31286))

**[Towards Generalizable Robotic Manipulation in Dynamic Environments](https://arxiv.org/abs/2603.15620)** — Heng Fan, Shangru Li, Shuhang Wang, et al.; arXiv; 2026-03-16
- *Intuition:* Dynamic manipulation needs both historical motion and a short forecast of object-centric futures. ([paper](https://arxiv.org/abs/2603.15620))
- *Contribution:* PUMA combines historical optical flow with world queries, alongside the 35-task/110K-trajectory DOMINO dataset. ([paper](https://arxiv.org/abs/2603.15620))
- *Setup:* Two physical AgileX Piper arms execute five moving-target tasks over 20 trials each. ([setup](https://arxiv.org/pdf/2603.15620))
- *Results:* PUMA averages 42% versus π0.5 24%, RDT-1B 8%, and ACT 7%. ([results](https://arxiv.org/pdf/2603.15620))

**[FASTER: Rethinking Real-Time Flow VLAs](https://arxiv.org/abs/2603.19199)** — Yuxiang Lu, Zhe Liu, Xianzhe Fan, et al.; arXiv; 2026-03-19
- *Intuition:* Flow policies should prioritize imminent actions so the robot can react before the whole chunk finishes denoising. ([paper](https://arxiv.org/abs/2603.19199))
- *Contribution:* FASTER adds a horizon-aware flow schedule and streaming client/server execution for immediate reaction. ([paper](https://arxiv.org/abs/2603.19199))
- *Setup:* AgileX Piper table tennis and Cobot Magic picking/folding test dynamic control on consumer and datacenter GPUs. ([setup](https://arxiv.org/pdf/2603.19199))
- *Results:* It accelerates immediate action sampling by 10× over original π0.5 and X-VLA and leads Sync, Naive Async, and Training-time RTC on both tested GPUs. ([results](https://arxiv.org/pdf/2603.19199))

**[Towards Human-Like Manipulation through RL-Augmented Teleoperation and Mixture-of-Dexterous-Experts VLA](https://arxiv.org/abs/2603.08122)** — Tutian Tang, Xingyu Ji, Wanli Xing, et al.; arXiv; 2026-03-09
- *Intuition:* RL-trained atomic skills can both assist teleoperation and serve as callable primitives for a dexterous VLA. ([paper](https://arxiv.org/abs/2603.08122))
- *Contribution:* IMCopilot and MoDE-VLA combine shared autonomy, force/tactile residual fusion, and mixture-of-expert control. ([paper](https://arxiv.org/abs/2603.08122))
- *Setup:* A 63-DoF bimanual humanoid system performs gear assembly, charger insertion, test-tube rearrangement, and apple peeling. ([setup](https://arxiv.org/html/2603.08122))
- *Results:* MoDE-VLA averages 34% versus π0 15%, while IMCopilot-assisted teleoperation succeeds on 80/90 trials versus direct teleoperation 31/90. ([results](https://arxiv.org/html/2603.08122))

### Data-efficient adaptation and generative supervision

**[GuidedVLA: Specifying Task-Relevant Factors via Plug-and-Play Action Attention Specialization](https://arxiv.org/abs/2605.12369)** — Xiaosong Jia, Bowen Yang, Zuhao Ge, et al.; arXiv; 2026-05-12
- *Intuition:* Explicitly supervising selected attention heads can prevent the action decoder from relying on visual shortcuts. ([paper](https://arxiv.org/abs/2605.12369))
- *Contribution:* GuidedVLA specializes heads for object grounding, spatial geometry, and temporal skill logic. ([paper](https://arxiv.org/abs/2605.12369))
- *Setup:* Six real tasks across ALOHA and PSI-Bot/RealMan are tested under position, scene, and lighting shifts. ([setup](https://arxiv.org/html/2605.12369))
- *Results:* It averages 75.8% versus base π0 55.8% ID, 67.5% versus 44.2% under scene shift, and 79.2% versus 57.5% under lighting shift. ([results](https://arxiv.org/html/2605.12369))

**[FOCA: Future-Oriented Conditioning for Data-Efficient Vision-Language-Action Adaptation](https://arxiv.org/abs/2606.20867)** — Duc M. Nguyen, Ngoc Diep, Binh Gia Nguyen, et al.; arXiv; 2026-06-18
- *Intuition:* Few demonstrations become more useful when the policy predicts task-grounded future interactions and aligns them with goal observations. ([paper](https://arxiv.org/abs/2606.20867))
- *Contribution:* FOCA learns future-conditioned latent representations and supports action-free co-training with world-model video. ([paper](https://arxiv.org/abs/2606.20867))
- *Setup:* Physical bimanual ALOHA table setup, open-bag, and shoelace tasks test 20–100% data regimes. ([setup](https://arxiv.org/pdf/2606.20867))
- *Results:* With 40%/100% data it reaches 55%/60% table setup versus π0 10%/10% and FOCA-alone 20%/45%, and reaches 95% on shoelace tying. ([results](https://arxiv.org/pdf/2606.20867))

**[GEM: Generative Supervision Helps Embodied Intelligence](https://arxiv.org/abs/2605.28548)** — Ruowen Zhao, Bangguo Li, Zuyan Liu, et al.; arXiv; 2026-05-27
- *Intuition:* Generating depth during pretraining forces an embodied VLM to learn spatial and physical structure that text supervision misses. ([paper](https://arxiv.org/abs/2605.28548))
- *Contribution:* GEM jointly trains depth generation with embodied reasoning on the GEM-4M corpus and transfers it into GEM-VLA. ([paper](https://arxiv.org/abs/2605.28548))
- *Setup:* A real UR5 performs cloth folding, backpack unzipping, and long-horizon table bussing over 50 runs per task. ([setup](https://arxiv.org/pdf/2605.28548))
- *Results:* GEM-VLA averages 43.0% versus no-depth GEM-VLA 40.7%, Qwen3VL-T-SFT 33.7%, π0.5 28.7%, and π0-FAST 22.3%. ([results](https://arxiv.org/pdf/2605.28548))

## Relationship graph

Including the three common foundational works, the fetched graph has two connected components: a foundation-connected component containing P1–P3 and P5–P35, and isolated P4 (OFlow). Without the classic hubs, the evidenced selected-paper edges form small VLA/memory clusters and leave all other technique tracks disconnected.

P1 Multi-View Video Diffusion Policy; P2 WAV; P3 HarmoWAM; P4 OFlow; P5 Pri4R; P6 LaWAM; P7 Feedback World Model; P8 Qwen-VLA; P9 Qwen-RobotManip; P10 RLDX-1; P11 StarVLA-α; P12 Hy-Embodied-0.5-VLA; P13 HEX; P14 MMaDA-VLA; P15 A1; P16 MEM; P17 ReMem-VLA; P18 See, Plan, Rewind; P19 RoboClaw; P20 LoHo-Manip; P21 IntentVLA; P22 AtomicVLA; P23 TiPToP; P24 UniDex; P25 ForceVLA2; P26 TacVLA; P27 AT-VLA; P28 Dexora; P29 DeMaVLA; P30 PUMA; P31 FASTER; P32 MoDE-VLA; P33 GuidedVLA; P34 FOCA; P35 GEM; C1 Diffusion Policy; C2 π0; C3 π0.5.

P8 --cites--> P30
P9 --cites--> P10
P9 --cites--> P11
P12 --cites--> P8
P12 --cites--> P11
P12 --cites--> P16
P20 --cites--> P16
P34 --cites--> P16
P1 --cites--> C1
P1 --cites--> C2
P1 --cites--> C3
P2 --cites--> C1
P2 --cites--> C2
P3 --cites--> C2
P5 --cites--> C1
P5 --cites--> C2
P5 --cites--> C3
P6 --cites--> C2
P6 --cites--> C3
P7 --cites--> C1
P8 --cites--> C1
P8 --cites--> C2
P9 --cites--> C1
P9 --cites--> C2
P9 --cites--> C3
P11 --cites--> C1
P11 --cites--> C3
P12 --cites--> C2
P13 --cites--> C3
P14 --cites--> C1
P14 --cites--> C2
P14 --cites--> C3
P15 --cites--> C2
P16 --cites--> C1
P16 --cites--> C2
P16 --cites--> C3
P17 --cites--> C2
P17 --cites--> C3
P18 --cites--> C1
P18 --cites--> C2
P18 --cites--> C3
P19 --cites--> C2
P20 --cites--> C1
P20 --cites--> C2
P20 --cites--> C3
P21 --cites--> C3
P22 --cites--> C2
P22 --cites--> C3
P23 --cites--> C2
P23 --cites--> C3
P24 --cites--> C1
P24 --cites--> C2
P25 --cites--> C1
P25 --cites--> C2
P25 --cites--> C3
P26 --cites--> C1
P26 --cites--> C3
P27 --cites--> C1
P27 --cites--> C2
P27 --cites--> C3
P28 --cites--> C1
P28 --cites--> C2
P28 --cites--> C3
P29 --cites--> C2
P29 --cites--> C3
P30 --cites--> C2
P30 --cites--> C3
P31 --cites--> C1
P31 --cites--> C2
P31 --cites--> C3
P32 --cites--> C1
P32 --cites--> C2
P32 --cites--> C3
P33 --cites--> C1
P33 --cites--> C2
P33 --cites--> C3
P34 --cites--> C1
P34 --cites--> C2
P34 --cites--> C3
P35 --cites--> C1
P35 --cites--> C3
P4 — disconnected: no fetched citation edge to another selected or classic paper.

No eligible `--builds-on-->` edge survived: the explicit build-on statements found pointed to π0.7 and HY-Embodied-0.5, both excluded by the lower-source citation rule. Citation edges came from fetched Semantic Scholar reference data or the source paper's fetched reference list.

## Verification ledger

| # | candidate_id | title | link | date | citations | source | citation_evidence | sota_evidence | content_evidence | affiliation | affiliation_evidence | checks | verdict |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | arXiv:2604.03181 | Multi-View Video Diffusion Policy | https://arxiv.org/abs/2604.03181 | 2026-04-03 | 6 (1.69/mo) | S2 | https://api.semanticscholar.org/graph/v1/paper/ARXIV:2604.03181?fields=title,publicationDate,citationCount,externalIds | https://arxiv.org/html/2604.03181v1 | https://arxiv.org/html/2604.03181v1 | Chinese Academy of Sciences | https://arxiv.org/html/2604.03181v1 | canonical+meta+citation+sota+affiliation | LIVE |
| 2 | arXiv:2604.14732 | World-Value-Action Model | https://arxiv.org/abs/2604.14732 | 2026-04-16 | 5 (1.60/mo) | S2 | https://api.semanticscholar.org/graph/v1/paper/ARXIV:2604.14732?fields=title,publicationDate,citationCount,externalIds | https://arxiv.org/html/2604.14732v2 | https://arxiv.org/html/2604.14732v2 | Westlake University | https://arxiv.org/html/2604.14732v2 | canonical+meta+citation+sota+affiliation | LIVE |
| 3 | arXiv:2605.10942 | HarmoWAM | https://arxiv.org/abs/2605.10942 | 2026-05-11 | 5 (2.17/mo) | S2 | https://api.semanticscholar.org/graph/v1/paper/ARXIV:2605.10942?fields=title,publicationDate,citationCount,externalIds | https://arxiv.org/html/2605.10942v1 | https://arxiv.org/html/2605.10942v1 | Peking University | https://arxiv.org/html/2605.10942v1 | canonical+meta+citation+sota+affiliation | LIVE |
| 4 | arXiv:2604.17876 | OFlow | https://arxiv.org/abs/2604.17876 | 2026-04-20 | 3 (1.003/mo) | S2 | https://api.semanticscholar.org/graph/v1/paper/ARXIV:2604.17876?fields=title,publicationDate,citationCount,externalIds | https://arxiv.org/html/2604.17876v1 | https://arxiv.org/html/2604.17876v1 | University of Southern California | https://arxiv.org/html/2604.17876v1 | canonical+meta+citation+sota+affiliation | LIVE |
| 5 | arXiv:2603.01549 | Pri4R | https://arxiv.org/abs/2603.01549 | 2026-03-02 | 5 (1.09/mo) | S2 | https://api.semanticscholar.org/graph/v1/paper/ARXIV:2603.01549?fields=title,publicationDate,citationCount,externalIds | https://arxiv.org/html/2603.01549v2 | https://arxiv.org/html/2603.01549v2 | KAIST | https://arxiv.org/html/2603.01549v2 | canonical+meta+citation+sota+affiliation | LIVE |
| 6 | arXiv:2606.15768 | LaWAM | https://arxiv.org/abs/2606.15768 | 2026-06-14 | 4 (3.38/mo) | S2 | https://api.semanticscholar.org/graph/v1/paper/ARXIV:2606.15768?fields=title,publicationDate,citationCount,externalIds | https://arxiv.org/html/2606.15768v1 | https://arxiv.org/html/2606.15768v1 | Tsinghua University | https://arxiv.org/html/2606.15768v1 | canonical+meta+citation+sota+affiliation | LIVE |
| 7 | arXiv:2605.15705 | Feedback World Model Enables Precise Guidance of Diffusion Policy | https://arxiv.org/abs/2605.15705 | 2026-05-15 | 3 (1.38/mo) | S2 | https://api.semanticscholar.org/graph/v1/paper/ARXIV:2605.15705?fields=title,publicationDate,citationCount,externalIds | https://arxiv.org/html/2605.15705v1 | https://arxiv.org/html/2605.15705v1 | Nanyang Technological University | https://arxiv.org/html/2605.15705v1 | canonical+meta+citation+sota+affiliation | LIVE |
| 8 | arXiv:2605.30280 | Qwen-VLA | https://arxiv.org/abs/2605.30280 | 2026-05-28 | 12 (6.89/mo) | S2 | https://api.semanticscholar.org/graph/v1/paper/ARXIV:2605.30280?fields=title,publicationDate,citationCount,externalIds | https://arxiv.org/pdf/2605.30280 | https://arxiv.org/pdf/2605.30280 | Alibaba Cloud | https://www.alibabacloud.com/en/solutions/generative-ai/qwen | canonical+meta+citation+sota+affiliation | LIVE |
| 9 | arXiv:2606.17846 | Qwen-RobotManip Technical Report | https://arxiv.org/abs/2606.17846 | 2026-06-16 | 11 (9.85/mo) | S2 | https://api.semanticscholar.org/graph/v1/paper/ARXIV:2606.17846?fields=title,publicationDate,citationCount,externalIds | https://arxiv.org/pdf/2606.17846 | https://arxiv.org/pdf/2606.17846 | Alibaba Cloud | https://www.alibabacloud.com/en/solutions/generative-ai/qwen | canonical+meta+citation+sota+affiliation | LIVE |
| 10 | arXiv:2605.03269 | RLDX-1 Technical Report | https://arxiv.org/abs/2605.03269 | 2026-05-05 | 10 (4.00/mo) | S2 | https://api.semanticscholar.org/graph/v1/paper/ARXIV:2605.03269?fields=title,publicationDate,citationCount,externalIds | https://arxiv.org/html/2605.03269 | https://arxiv.org/html/2605.03269 | KAIST | https://arxiv.org/html/2605.03269 | canonical+meta+citation+sota+affiliation | LIVE |
| 11 | arXiv:2604.11757 | StarVLA-α | https://arxiv.org/abs/2604.11757 | 2026-04-13 | 9 (2.80/mo) | S2 | https://api.semanticscholar.org/graph/v1/paper/ARXIV:2604.11757?fields=title,publicationDate,citationCount,externalIds | https://arxiv.org/pdf/2604.11757 | https://arxiv.org/pdf/2604.11757 | HKUST | https://arxiv.org/pdf/2604.11757 | canonical+meta+citation+sota+affiliation | LIVE |
| 12 | arXiv:2606.14409 | Hy-Embodied-0.5-VLA | https://arxiv.org/abs/2606.14409 | 2026-06-12 | 6 (4.81/mo) | S2 | https://api.semanticscholar.org/graph/v1/paper/ARXIV:2606.14409?fields=title,publicationDate,citationCount,externalIds | https://arxiv.org/pdf/2606.14409 | https://arxiv.org/pdf/2606.14409 | Tencent Robotics X | https://arxiv.org/pdf/2606.14409 | canonical+meta+citation+sota+affiliation | LIVE |
| 13 | arXiv:2604.07993 | HEX | https://arxiv.org/abs/2604.07993 | 2026-04-09 | 7 (2.09/mo) | S2 | https://api.semanticscholar.org/graph/v1/paper/ARXIV:2604.07993?fields=title,publicationDate,citationCount,externalIds | https://arxiv.org/html/2604.07993 | https://arxiv.org/html/2604.07993 | Peking University | https://arxiv.org/html/2604.07993 | canonical+meta+citation+sota+affiliation | LIVE |
| 14 | arXiv:2603.25406 | MMaDA-VLA | https://arxiv.org/abs/2603.25406 | 2026-03-26 | 6 (1.57/mo) | S2 | https://api.semanticscholar.org/graph/v1/paper/ARXIV:2603.25406?fields=title,publicationDate,citationCount,externalIds | https://arxiv.org/pdf/2603.25406 | https://arxiv.org/pdf/2603.25406 | Westlake University | https://arxiv.org/pdf/2603.25406 | canonical+meta+citation+sota+affiliation | LIVE |
| 15 | arXiv:2604.05672 | A1 | https://arxiv.org/abs/2604.05672 | 2026-04-07 | 4 (1.17/mo) | S2 | https://api.semanticscholar.org/graph/v1/paper/ARXIV:2604.05672?fields=title,publicationDate,citationCount,externalIds | https://arxiv.org/html/2604.05672 | https://arxiv.org/html/2604.05672 | Sun Yat-sen University | https://arxiv.org/html/2604.05672 | canonical+meta+citation+sota+affiliation | LIVE |
| 16 | arXiv:2603.03596 | MEM | https://arxiv.org/abs/2603.03596 | 2026-03-04 | 36 (7.94/mo) | S2 | https://api.semanticscholar.org/graph/v1/paper/ARXIV:2603.03596?fields=title,publicationDate,citationCount,externalIds | https://arxiv.org/pdf/2603.03596 | https://arxiv.org/pdf/2603.03596 | Stanford University | https://arxiv.org/pdf/2603.03596 | canonical+meta+citation+sota+affiliation | LIVE |
| 17 | arXiv:2603.12942 | ReMem-VLA | https://arxiv.org/abs/2603.12942 | 2026-03-13 | 14 (3.30/mo) | S2 | https://api.semanticscholar.org/graph/v1/paper/ARXIV:2603.12942?fields=title,publicationDate,citationCount,externalIds | https://arxiv.org/pdf/2603.12942 | https://arxiv.org/pdf/2603.12942 | Technical University of Munich | https://arxiv.org/pdf/2603.12942 | canonical+meta+citation+sota+affiliation | LIVE |
| 18 | arXiv:2603.09292 | See, Plan, Rewind | https://arxiv.org/abs/2603.09292 | 2026-03-10 | 5 (1.15/mo) | S2 | https://api.semanticscholar.org/graph/v1/paper/ARXIV:2603.09292?fields=title,publicationDate,citationCount,externalIds | https://arxiv.org/pdf/2603.09292 | https://arxiv.org/pdf/2603.09292 | University of Science and Technology of China | https://arxiv.org/pdf/2603.09292 | canonical+meta+citation+sota+affiliation | LIVE |
| 19 | arXiv:2603.11558 | RoboClaw | https://arxiv.org/abs/2603.11558 | 2026-03-12 | 12 (2.81/mo) | S2 | https://api.semanticscholar.org/graph/v1/paper/ARXIV:2603.11558?fields=title,publicationDate,citationCount,externalIds | https://arxiv.org/pdf/2603.11558 | https://arxiv.org/pdf/2603.11558 | National University of Singapore | https://arxiv.org/pdf/2603.11558 | canonical+meta+citation+sota+affiliation | LIVE |
| 20 | arXiv:2604.21924 | Long-Horizon Manipulation via Trace-Conditioned VLA Planning | https://arxiv.org/abs/2604.21924 | 2026-04-23 | 3 (1.04/mo) | S2 | https://api.semanticscholar.org/graph/v1/paper/ARXIV:2604.21924?fields=title,publicationDate,citationCount,externalIds | https://arxiv.org/html/2604.21924 | https://arxiv.org/html/2604.21924 | UC San Diego | https://arxiv.org/html/2604.21924 | canonical+meta+citation+sota+affiliation | LIVE |
| 21 | arXiv:2605.14712 | IntentVLA | https://arxiv.org/abs/2605.14712 | 2026-05-14 | 3 (1.36/mo) | S2 | https://api.semanticscholar.org/graph/v1/paper/ARXIV:2605.14712?fields=title,publicationDate,citationCount,externalIds | https://arxiv.org/html/2605.14712 | https://arxiv.org/html/2605.14712 | Huazhong University of Science and Technology | https://arxiv.org/html/2605.14712 | canonical+meta+citation+sota+affiliation | LIVE |
| 22 | arXiv:2603.07648 | AtomicVLA | https://arxiv.org/abs/2603.07648 | 2026-03-08 | 6 (1.36/mo) | S2 | https://api.semanticscholar.org/graph/v1/paper/ARXIV:2603.07648?fields=title,publicationDate,citationCount,externalIds | https://arxiv.org/pdf/2603.07648 | https://arxiv.org/pdf/2603.07648 | Sun Yat-sen University | https://arxiv.org/pdf/2603.07648 | canonical+meta+citation+sota+affiliation | LIVE |
| 23 | arXiv:2603.09971 | TiPToP | https://arxiv.org/abs/2603.09971 | 2026-03-10 | 7 (1.61/mo) | S2 | https://api.semanticscholar.org/graph/v1/paper/ARXIV:2603.09971?fields=title,publicationDate,citationCount,externalIds | https://arxiv.org/html/2603.09971 | https://arxiv.org/html/2603.09971 | MIT | https://arxiv.org/html/2603.09971 | canonical+meta+citation+sota+affiliation | LIVE |
| 24 | arXiv:2603.22264 | UniDex | https://arxiv.org/abs/2603.22264 | 2026-03-23 | 14 (3.58/mo) | S2 | https://api.semanticscholar.org/graph/v1/paper/ARXIV:2603.22264?fields=title,publicationDate,citationCount,externalIds | https://arxiv.org/pdf/2603.22264 | https://arxiv.org/pdf/2603.22264 | Tsinghua University | https://arxiv.org/pdf/2603.22264 | canonical+meta+citation+sota+affiliation | LIVE |
| 25 | arXiv:2603.15169 | ForceVLA2 | https://arxiv.org/abs/2603.15169 | 2026-03-16 | 12 (2.90/mo) | S2 | https://api.semanticscholar.org/graph/v1/paper/ARXIV:2603.15169?fields=title,publicationDate,citationCount,externalIds | https://arxiv.org/pdf/2603.15169 | https://arxiv.org/pdf/2603.15169 | Shanghai Jiao Tong University | https://arxiv.org/pdf/2603.15169 | canonical+meta+citation+sota+affiliation | LIVE |
| 26 | arXiv:2603.12665 | TacVLA | https://arxiv.org/abs/2603.12665 | 2026-03-13 | 13 (3.07/mo) | S2 | https://api.semanticscholar.org/graph/v1/paper/ARXIV:2603.12665?fields=title,publicationDate,citationCount,externalIds | https://arxiv.org/html/2603.12665 | https://arxiv.org/html/2603.12665 | Purdue University | https://arxiv.org/html/2603.12665 | canonical+meta+citation+sota+affiliation | LIVE |
| 27 | arXiv:2605.07308 | AT-VLA | https://arxiv.org/abs/2605.07308 | 2026-05-08 | 4 (1.67/mo) | S2 | https://api.semanticscholar.org/graph/v1/paper/ARXIV:2605.07308?fields=title,publicationDate,citationCount,externalIds | https://arxiv.org/html/2605.07308 | https://arxiv.org/html/2605.07308 | Peking University | https://arxiv.org/html/2605.07308 | canonical+meta+citation+sota+affiliation | LIVE |
| 28 | arXiv:2605.18722 | Dexora | https://arxiv.org/abs/2605.18722 | 2026-05-18 | 5 (2.42/mo) | S2 | https://api.semanticscholar.org/graph/v1/paper/ARXIV:2605.18722?fields=title,publicationDate,citationCount,externalIds | https://arxiv.org/html/2605.18722 | https://arxiv.org/html/2605.18722 | Tsinghua University | https://arxiv.org/html/2605.18722 | canonical+meta+citation+sota+affiliation | LIVE |
| 29 | arXiv:2605.31286 | DeMaVLA | https://arxiv.org/abs/2605.31286 | 2026-05-29 | 3 (1.76/mo) | S2 | https://api.semanticscholar.org/graph/v1/paper/ARXIV:2605.31286?fields=title,publicationDate,citationCount,externalIds | https://arxiv.org/html/2605.31286 | https://arxiv.org/html/2605.31286 | Tongji University | https://arxiv.org/html/2605.31286 | canonical+meta+citation+sota+affiliation | LIVE |
| 30 | arXiv:2603.15620 | Towards Generalizable Robotic Manipulation in Dynamic Environments | https://arxiv.org/abs/2603.15620 | 2026-03-16 | 8 (1.93/mo) | S2 | https://api.semanticscholar.org/graph/v1/paper/ARXIV:2603.15620?fields=title,publicationDate,citationCount,externalIds | https://arxiv.org/pdf/2603.15620 | https://arxiv.org/abs/2603.15620 | Huazhong University of Science and Technology | https://arxiv.org/pdf/2603.15620 | canonical+meta+citation+sota+affiliation | LIVE |
| 31 | arXiv:2603.19199 | FASTER | https://arxiv.org/abs/2603.19199 | 2026-03-19 | 8 (1.98/mo) | S2 | https://api.semanticscholar.org/graph/v1/paper/ARXIV:2603.19199?fields=title,publicationDate,citationCount,externalIds | https://arxiv.org/pdf/2603.19199 | https://arxiv.org/abs/2603.19199 | University of Hong Kong | https://arxiv.org/pdf/2603.19199 | canonical+meta+citation+sota+affiliation | LIVE |
| 32 | arXiv:2603.08122 | RL-Augmented Teleoperation and MoDE-VLA | https://arxiv.org/abs/2603.08122 | 2026-03-09 | 6 (1.37/mo) | S2 | https://api.semanticscholar.org/graph/v1/paper/ARXIV:2603.08122?fields=title,publicationDate,citationCount,externalIds | https://arxiv.org/html/2603.08122 | https://arxiv.org/abs/2603.08122 | Shanghai Jiao Tong University | https://arxiv.org/html/2603.08122 | canonical+meta+citation+sota+affiliation | LIVE |
| 33 | arXiv:2605.12369 | GuidedVLA | https://arxiv.org/abs/2605.12369 | 2026-05-12 | 4 (1.76/mo) | S2 | https://api.semanticscholar.org/graph/v1/paper/ARXIV:2605.12369?fields=title,publicationDate,citationCount,externalIds | https://arxiv.org/html/2605.12369 | https://arxiv.org/abs/2605.12369 | Fudan University | https://arxiv.org/html/2605.12369 | canonical+meta+citation+sota+affiliation | LIVE |
| 34 | arXiv:2606.20867 | FOCA | https://arxiv.org/abs/2606.20867 | 2026-06-18 | 3 (2.85/mo) | S2 | https://api.semanticscholar.org/graph/v1/paper/ARXIV:2606.20867?fields=title,publicationDate,citationCount,externalIds | https://arxiv.org/pdf/2606.20867 | https://arxiv.org/abs/2606.20867 | Max Planck Society | https://arxiv.org/pdf/2606.20867 | canonical+meta+citation+sota+affiliation | LIVE |
| 35 | arXiv:2605.28548 | GEM | https://arxiv.org/abs/2605.28548 | 2026-05-27 | 3 (1.69/mo) | S2 | https://api.semanticscholar.org/graph/v1/paper/ARXIV:2605.28548?fields=title,publicationDate,citationCount,externalIds | https://arxiv.org/pdf/2605.28548 | https://arxiv.org/abs/2605.28548 | Tsinghua University | https://arxiv.org/pdf/2605.28548 | canonical+meta+citation+sota+affiliation | LIVE |

## Dropped candidates

| candidate_id | title | reason |
|---|---|---|
| arXiv:2603.16666 | Fast-WAM | citation conflict: Semantic Scholar 106, OpenAlex 0; required lower verified count fails total and velocity floors. |
| arXiv:2603.10448 | DiT4DiT | citation conflict: Semantic Scholar 28, OpenAlex 0; lower verified count fails. |
| arXiv:2603.08519 | AtomVLA | citation conflict: Semantic Scholar 11, OpenAlex 0; lower verified count fails. |
| arXiv:2604.27792 | Motubrain | institution: affiliation unresolved; OpenAlex also reported 0 citations against Semantic Scholar 21. |
| arXiv:2604.08168 | ViVa | citation conflict: Semantic Scholar 8, OpenAlex 0; lower verified count fails. |
| arXiv:2605.06481 | OA-WAM | physical-robot gate: evaluation is simulation only. |
| arXiv:2604.26848 | STARRY | citation conflict: Semantic Scholar 4, OpenAlex 0; lower verified count fails. |
| arXiv:2603.27670 | ProgressVLA | citation conflict: Semantic Scholar 5, OpenAlex 0; lower verified count fails. |
| arXiv:2604.05656 | SnapFlow | physical-robot gate: simulation only; institution: not on accept-list (Jilin University, Chongqing University, University of Liverpool). |
| arXiv:2603.03195 | Chain of World | physical-robot gate: simulation only. |
| arXiv:2603.24393 | 3D-Mix for VLA | physical-robot gate: simulation only. |
| arXiv:2604.15483 | π0.7 | citation conflict: Semantic Scholar 79, OpenAlex 0; lower verified count fails. |
| arXiv:2605.02881 | MolmoAct2 | citation conflict: Semantic Scholar 19, OpenAlex 0; lower verified count fails. |
| arXiv:2604.07430 | HY-Embodied-0.5 | citation conflict: Semantic Scholar 8, OpenAlex 0; lower verified count fails. |
| arXiv:2603.05377 | OpenFrontier | SOTA gate: physical deployment is real, but the paper reports competitive rather than best-at-time headline performance. |
| arXiv:2603.14363 | AerialVLA | physical-robot gate: all reported experiments are simulated. |
| arXiv:2603.10126 | AR-VLA | institution: not on accept-list (INSAIT; Sofia University). |
| arXiv:2603.09298 | CORAL | institution: not on accept-list (Frontier Robotics). |
| arXiv:2605.30877 | Wall-OSS-0.5 | institution: not on accept-list (X Square Robot Team). |
| arXiv:2606.01955 | WALL-WM | institution: not on accept-list (X Square Robot Team). |
| arXiv:2604.23073 | RL Token | institution: affiliation unresolved; acknowledgements credit Physical Intelligence, but no author-affiliation block establishes an author affiliation. |
| arXiv:2605.00416 | Learning while Deploying | citation conflict: Semantic Scholar 5, OpenAlex 0; lower verified count fails. |
| arXiv:2603.15257 | HapticVLA | institution: not on accept-list (all authors at Skolkovo Institute of Science and Technology). |

## Coverage & limitations

- Three real subagents ran parallel VLA, world-model/diffusion, and RL/industrial discovery/validation lanes; their manifests record 42 searches plus canonical arXiv, PDF/HTML, Semantic Scholar, project-page, and OpenAlex checks.
- The discovery pool was deduplicated by arXiv ID, then 58 high-relevance candidates received full date, citation, physical-hardware, named-baseline, and `general + robotics` institution validation.
- Citation metadata is unusually unstable for this very recent window: ten otherwise-eligible papers were excluded because OpenAlex returned 0 while Semantic Scholar returned ≥3; the skill's lower-source conflict rule controlled.
- Institution failures are separate: six confirmed no-matches (SnapFlow, AR-VLA, CORAL, Wall-OSS-0.5, WALL-WM, HapticVLA) and two unresolved affiliations (Motubrain, RL Token).
- Canonical links for all 58 validation candidates resolved; arXiv PDF was used where HTML was unavailable or incomplete.
- The relationship graph is evidence-limited: reference-data edges are not claims of intellectual dependence, and no eligible explicit build-on statement survived filtering.

## Evaluate this run

Open `evaluate_results_gui.html`, load this file, and save the result to `evaluations/`. Run id: `reinforcement-learning-vla-world-model-diffusion-policy_2026-07-20`.
