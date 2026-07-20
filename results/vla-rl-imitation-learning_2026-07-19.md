---
schema: find-sota-papers/result@1
run_id: vla-rl-imitation-learning_2026-07-19
created: 2026-07-19T00:00:00Z
harness: claude-code
model: claude-opus-4-8
prompt: |
  Use the find-sota-papers skill to find state-of-the-art research papers matching the constraints below.

  Field: robotics
  Topics: VLA, RL, Imitation learning
  SOTA requirements: high performance in production and realistic task
  Other requirements: results demonstrating high potential in real industrial level production; or promising for applying on robots for real productions
  No earlier than: 2026 March
  Minimum citations (per month since publication): 2
  Institutions: reputable — keep only papers with at least one author affiliated with an institution on the skill's curated reputable-institutions accept-list (references/topics/institutions.md); apply the general list, plus the topic addendum when the topic matches one, and report institution drops separately from papers whose affiliation could not be established
  Number of papers: 30
  List by: timeline — reverse-chronological along a timeline
  Present as: minimalism — title (linked), then one sentence each for intuition, core contribution, experiment setup, and results vs. named baselines
  Include classic work: yes — if the selected SOTA papers share a common prior classic work, include it (clearly labeled)
  Multi-agent: yes — request bounded parallel discovery and validation with real subagents; fall back sequentially if unavailable

  Every paper must include a working link. Verify each paper resolves to a real arXiv / DOI / Semantic Scholar entry before listing it — do not list papers from memory and do not fabricate any title, author, link, or citation count. Do not pad the list to reach the requested count: if fewer papers survive verification, return those and state the shortfall and why.
constraints:
  field: Robotics
  topics: VLA, reinforcement learning, imitation learning
  sota_requirements: high performance on realistic/production tasks; evidence of real industrial-level production potential
  other_requirements: results demonstrating high potential for real industrial production or deployment on production robots
  no_earlier_than: 2026-03
  min_citations:
    total: null
    per_month: 2
  institutions: reputable
  institutions_accept_list: general + robotics
  listing: timeline
  presentation: minimalism
  include_classic: true
  multi_agent: yes
  num_papers: 30
funnel:
  found: 88
  merged: 74
  filtered: 74
  verified: 39
  selected: 30
grounding:
  links_checked: 74
  non_resolving: 0
  unknown_fields: 9
  citation_source: Semantic Scholar
  citation_checked: 2026-07-19
cost:
  wall_clock_s: 1400
  tokens_total: unknown
  searches: unknown
  fetches: unknown
  subagents: 8
shortfall: null
---

# SOTA Papers — Robotics · VLA, RL, Imitation learning

## Run summary

Since 2026-03 · SOTA = high performance on realistic/production tasks with industrial-deployment potential · cites/month ≥ 2 (papers newer than 3 months exempt per the recency rule) · 30 papers · list by timeline · minimalism · institutions = reputable (accept-list: general + robotics).

Found 88 → merged 74 → filtered 74 → verified 39 → selected 30.
Citation counts via Semantic Scholar (2026-07-19).
No shortfall: 39 papers cleared every gate, and the 30 best-fitting were selected.

## Classic / foundational

- **[RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control](https://arxiv.org/abs/2307.15818)** — Brohan et al., Google DeepMind, 2023 (3,662 citations) — appeared in **5 of 5** retrievable reference lists sampled from the selected papers; it established the VLA paradigm (co-fine-tuning a VLM on robot trajectories with actions as text tokens) that the 2026 architectures, RL fine-tuning methods, and memory/world-model extensions all extend.

Note: **OpenVLA** ([arXiv:2406.09246](https://arxiv.org/abs/2406.09246), 2,785 cites) and **π0** ([arXiv:2410.24164](https://arxiv.org/abs/2410.24164), 2,212 cites) also appeared in 5 of 5 lists — a three-way tie broken on total citation count. π0.5 (4/5) and Octo (3/5) followed.

## Papers

### July 2026

**[ROSA: A Robotics Foundation Model Serving System for Robot Factories](https://arxiv.org/abs/2607.01088)** — Wenqi Jiang, Jason Clemons, Rowland O'Flaherty et al. (NVIDIA Research; Stanford University), arXiv, 2026-07-01
- *Intuition:* Serving infrastructure, not policy architecture, is what gates throughput once a whole factory of robots shares GPU servers.
- *Contribution:* A serving system giving a robot fleet shared access to GPU servers, with multi-model workflow support, task-specific performance guarantees, and scheduling optimized for factory-wide output rather than per-request latency.
- *Setup:* Physical robots plus large-scale simulation of "robot factories" running robotics foundation models.
- *Results:* Up to **12.06× productivity gain** versus conventional dedicated per-robot serving.

### June 2026

**[Adapting Generalist Robot Policies with Semantic Reinforcement Learning](https://arxiv.org/abs/2606.31958)** — Jagdeep Singh Bhatia, Andrew Wagenmaker, William Chen et al. (UC Berkeley), arXiv, 2026-06-30
- *Intuition:* Exploring in a VLA's language-prompt space is more structured and semantically meaningful than exploring in raw action space.
- *Contribution:* SARL optimizes the prompt space through online interaction, treating the generalist policy as a controllable skill prior.
- *Setup:* Real-world deployment of VLAs on complex long-horizon tasks.
- *Results:* Reported to significantly outperform existing approaches for improving robot behavior in deployment; specific per-baseline numbers `unknown`.

**[Scalable Behavior Cloning with Open Data, Training, and Evaluation](https://arxiv.org/abs/2606.27375)** — Arthur Allshire, Himanshu Gaurav Singh, Ritvik Singh et al. (UC Berkeley; MIT; Amazon FAR; CMU; XDOF), arXiv, 2026-06-25
- *Intuition:* Behavior cloning needs a community-scale open data/training/eval stack the way language modeling got one.
- *Contribution:* ABC-130K — 3,500 hours / 130K episodes / 195 tasks of teleoperation data — plus open hardware, a simulation pipeline, and a Diffusion-Transformer-versus-VLA architecture comparison.
- *Setup:* Box folding, credit-card extraction and other manipulation tasks, with 400 hours of additional simulated data.
- *Results:* Establishes an open baseline stack and an architecture comparison rather than a single headline number vs a named baseline (`unknown`).

**[Play2Perfect: What Matters in Dexterous Play Pretraining for Precise Assembly?](https://arxiv.org/abs/2606.26428)** — Tyler Ga Wei Lum, Kushal Kedia, C. Karen Liu et al. (Stanford University; Cornell University), arXiv, 2026-06-24
- *Intuition:* Unrestricted dexterous "play" before specializing buys large sample-efficiency gains on precise assembly.
- *Contribution:* An ablation of what actually matters in play pretraining — object diversity, training objective, trajectory diversity, and goal precision.
- *Setup:* Zero-shot sim-to-real on tight insertion with 0.5 mm clearance and long-horizon multi-part assembly/screwing.
- *Results:* **33× better sample efficiency** than training from scratch; 60% success on tight insertions and >50% on long-horizon multi-part assembly.

**[Learning Dexterous Manipulation Using Contact Wrench Guidance From Human Demonstration](https://arxiv.org/abs/2607.00033)** — Xinghao Zhu, Zixi Liu, Shalin Jain et al. (NVIDIA), arXiv, 2026-06-22
- *Intuition:* Matching human demonstrations to robot motion via object-centric contact wrenches generalizes better than matching raw kinematics.
- *Contribution:* CHORD, a contact-wrench-space guidance framework that generalizes hand-only and third-person demonstrations to whole-body dexterous control.
- *Setup:* 1,831 evaluation tasks drawn from a 4,739-task simulation benchmark, with open- and closed-loop transfer to physical robots.
- *Results:* **82.12%** average success on the dexterous benchmark and **90.77%** generalizing to whole-body control; no named-baseline table retrieved.

**[Robot Self-Improvement via Human-Video Dynamics Models](https://arxiv.org/abs/2606.21406)** — Hanzhi Chen, Anran Zhang, Simon Schaefer et al. (ETH Zurich; TU Munich; Microsoft; MCML), arXiv, 2026-06-19
- *Intuition:* A dynamics model learned from human video can repair a robot policy's failures without retraining the policy.
- *Contribution:* Dynamics-Guided Action Correction (DGAC), a training-free failure-repair method that treats each failure as a query for corrective-action proposal and ranking.
- *Setup:* Seven real-world manipulation tasks across a mobile manipulator and a static arm, over multiple policy backbones.
- *Results:* Success rate improved from **40% to 81%** across policy backbones.

**[ENPIRE: Agentic Robot Policy Self-Improvement in the Real World](https://arxiv.org/abs/2606.19980)** — Wenli Xiao, Jia Xie, Tonghe Zhang et al. (NVIDIA; Carnegie Mellon University; UC Berkeley), arXiv, 2026-06-18
- *Intuition:* If coding agents can automate the reset-execute-verify-refine loop on physical robots, real-world RL research itself becomes a scalable optimization procedure.
- *Contribution:* A four-module harness — Environment (auto reset/verify), Policy Improvement, parallel physical Rollout, and Evolution agents that analyze logs and rewrite the training code.
- *Setup:* Multiple physical robots running in parallel on pin-box organizing, zip-tie fastening, and tool use.
- *Results:* **99% success rate** on the dexterous tasks, achieved autonomously by the coding agents, accelerating further with an agent team on a robot fleet.

**[EventVLA: Event-Driven Visual Evidence Memory for Long-Horizon Vision-Language-Action Policies](https://arxiv.org/abs/2606.20092)** — Ganlin Yang, Zhangzheng Tu, Yuqiang Yang et al. (USTC; Shanghai AI Laboratory; SJTU; HKU; Tsinghua; PKU; Huawei), arXiv, 2026-06-18
- *Intuition:* Long-horizon, non-Markovian manipulation needs sparse task-critical visual memory rather than a dense frame history.
- *Contribution:* A Keyframe Evidence Memory module that predicts future-keyframe probability to build sparse visual evidence memory, plus the RoboTwin-MeM diagnostic benchmark.
- *Setup:* 17 memory-requiring simulation tasks plus 4 real-world bimanual manipulation tasks.
- *Results:* **+40% average success rate** over state-of-the-art memory-augmented VLAs.

**[ROVE: Unlocking Human Interventions for Humanoid Manipulation via Reinforcement Learning](https://arxiv.org/abs/2606.17011)** — Wei Xiao, Weiliang Tang, Yuying Ge et al. (XPENG Robotics; Fudan University; CUHK; SJTU), arXiv, 2026-06-15
- *Intuition:* Imperfect human interventions should be exploited optimistically rather than imitated as if they were expert supervision.
- *Contribution:* A humanoid human-in-the-loop RL pipeline using Optimistic Value Estimation to prioritize high-value behaviors, with cross-embodiment human video supplying long-tail recovery supervision.
- *Setup:* Real-world contact-rich, fine-grained humanoid manipulation tasks.
- *Results:* Outperforms experience-learning baselines and improves consistently across rollout-intervention iterations; numeric success rate `unknown`.

**[Hy-Embodied-0.5-VLA: From Vision-Language-Action Models to a Real-World Robot Learning Stack](https://arxiv.org/abs/2606.14409)** — He Zhang, Lingzhu Xiang, Haitao Lin et al. (Tencent Robotics X), arXiv, 2026-06-12
- *Intuition:* Production robot learning requires an integrated end-to-end stack, not a standalone model.
- *Contribution:* A full real-world robot learning stack combining VLA modeling with data collection, continued pretraining/SFT, RL post-training, and deployment infrastructure.
- *Setup:* End-to-end system validated through real-world robot deployment.
- *Results:* `unknown` — no named-baseline comparison retrieved from the fetched pages.

**[EmbodiSteer: Steering Embodiment-Agnostic Visuomotor Policies with Joint-Space Guidance](https://arxiv.org/abs/2606.12965)** — Shihefeng Wang, Kangchen Lv, Mingrui Yu, Xiang Li (Tsinghua University), arXiv, 2026-06-11
- *Intuition:* Cartesian end-effector policies ignore joint-space collision constraints, so embodiment-specific safety can be added at inference instead of in training.
- *Contribution:* Training-free inference-time steering using forward-kinematics/Jacobian-based joint-space collision awareness for zero-shot cross-embodiment deployment.
- *Setup:* Nine simulated robots plus two physical robots in constrained real scenarios.
- *Results:* On real robots, **−90.0% collision rate and +36.7% success** versus the Cartesian-only policy (simulation: −46.1% / +28.5%).

**[UniIntervene: Agentic Intervention for Efficient Real-World Reinforcement Learning](https://arxiv.org/abs/2606.12372)** — Haoyuan Deng, Yitong Gao, Yudong Lin et al. (Nanyang Technological University; Beijing University of Posts and Telecommunications), arXiv, 2026-06-10
- *Intuition:* Human intervention is the scaling bottleneck in real-world RL, so an agent that detects stalled exploration and self-recovers removes the human from the inner loop.
- *Contribution:* Future-conditioned action-value estimation with a temporal value-risk critic that triggers interventions and retrieves recovery targets from past intervention memories.
- *Setup:* Diverse real-world manipulation training runs against standard human-intervention training.
- *Results:* **+8.6% average success rate while cutting human interventions by 57%** versus baseline intervention approaches.

**[TORL-VLA: Tactile Guided Online Reinforcement Learning for Contact-Rich Manipulation](https://arxiv.org/abs/2606.09337)** — Huaihang Zheng, Yi Yang, Kai Ma et al. (Meituan; Beijing Institute of Technology; Beihang University; Institute of Automation CAS), arXiv, 2026-06-08
- *Intuition:* Tactile feedback plus correct credit assignment lets lightweight online RL refine contact-rich skills without misattributing post-intervention success.
- *Contribution:* A wrench-aware model predicting actions and future contact forces, paired with an intervention-censored critic.
- *Setup:* Real-robot latch manipulation, coffee-cup placement, and egg handling.
- *Results:* Improvements across subtask and full-task success rates; exact numbers `unknown`.

**[FlowPRO: Reward-Free Reinforced Fine-Tuning of Flow-Matching VLAs via Proximalized Preference Optimization](https://arxiv.org/abs/2606.05468)** — Yihao Wu, He Zhang, Junbo Tan et al. (Tencent Robotics X; Futian Laboratory; Tsinghua University), arXiv, 2026-06-03
- *Intuition:* Reward-free preference optimization with a proximal regularizer avoids reward hacking when RL-finetuning flow-matching VLA action heads.
- *Contribution:* An RPRO objective that anchors implicit reward magnitude, with teleoperated intervention-and-rollback data collection and smooth interpolation for dense supervision.
- *Setup:* Four bimanual real-robot tasks.
- *Results:* Highest success rate, **outperforming four representative baselines**.

**[PACE: Phase-Aware Chunk Execution for Robot Policies with Action Chunking](https://arxiv.org/abs/2606.00537)** — Junnan Nie, Jiayi Li, Jiachen Zhang et al. (Peking University; JD Explore Academy), arXiv, 2026-05-30
- *Intuition:* Fixed action-chunk execution horizons are unreliable because success is non-monotonic in horizon, so replanning should happen at low-speed kinematic transition points.
- *Contribution:* A plug-and-play, retraining-free method that dynamically selects chunk execution horizons from predicted speed profiles.
- *Setup:* Real bimanual ALOHA and single-arm Franka platforms, plus 50 RoboTwin2.0 tasks.
- *Results:* RoboTwin2.0 success **57.8% → 64.2%**; ALOHA task score **60.7 → 77.7**; Franka success **50.7% → 70.4%**.

### May 2026

**[BORA: Bridging Offline Reinforcement Learning and Online Residual Adaptation for Real-World Dexterous VLA Models](https://arxiv.org/abs/2605.30226)** — Zhongxi Chen, Yifan Han, Yanming Shao et al. (SJTU; CASIA; Shanghai AI Laboratory; USTC), arXiv, 2026-05-28
- *Intuition:* An offline critic followed by frozen-base residual adaptation corrects dexterous VLA execution errors while preserving the pretrained prior.
- *Contribution:* An offline action-conditioned critic conditioned on VLM cognition tokens and action chunks, then online chunk-wise residual adaptation driven by intervention rewards.
- *Setup:* Five complex real-world dexterous manipulation tasks.
- *Results:* **+33 points absolute average success** versus pure imitation-learning and decoupled-RL baselines, and up to **+43%** on unseen-object generalization.

**[RLDX-1 Technical Report](https://arxiv.org/abs/2605.03269)** — Dongyoung Kim, Huiwon Jang, Myungkyu Koo et al. (RLWRLD; KAIST), arXiv, 2026-05-05
- *Intuition:* VLAs inherit broad scene and language generalization from VLM pretraining but lack the motion awareness, long-term memory, and tactile sensing that real tasks demand.
- *Contribution:* A Multi-Stream Action Transformer fusing visual and tactile perception, high-DoF actuation and memory-aware decision-making, with rare-scenario data synthesis and inference optimizations for real-time deployment.
- *Setup:* ALLEX humanoid dexterous-manipulation tasks.
- *Results:* **86.8% success versus ~40% for both π0.5 and GR00T N1.6**.

**[MolmoAct2: Action Reasoning Models for Real-world Deployment](https://arxiv.org/abs/2605.02881)** — Haoquan Fang, Jiafei Duan, Donovan Clay et al. (Allen Institute for AI; University of Washington; NUS; UPenn; Johns Hopkins; Amazon; Michigan; UNC), arXiv, 2026-05-04
- *Intuition:* An open-weight action-reasoning VLA needs a purpose-built VLM backbone plus flexible action tokenization to be genuinely deployment-ready.
- *Contribution:* The MolmoER backbone, the OpenFAST open action tokenizer, a discrete+continuous action architecture, an adaptive-latency MolmoThink reasoning variant, and new bimanual teleoperation datasets.
- *Setup:* Real-world robot deployment evaluation.
- *Results:* Positioned as an open, deployment-ready alternative to closed VLAs; head-to-head numbers versus named baselines `unknown`.

**[Learning while Deploying: Fleet-Scale Reinforcement Learning for Generalist Robot Policies](https://arxiv.org/abs/2605.00416)** — Yi Wang, Xinchen Li, Pengwei Xie et al. (Shanghai Innovation Institute; AgiBot; Columbia University), arXiv, 2026-05-01
- *Intuition:* Generalist policies plateau after imitation pretraining, so closing the deploy → collect → improve loop across a fleet keeps them improving under real distribution shift.
- *Contribution:* An offline-to-online RL framework combining Distributional Implicit Value Learning with Q-learning via Adjoint Matching to post-train flow-based VLA policies from fleet rollouts and human interventions.
- *Setup:* A fleet of **16 dual-arm robots** across 8 real manipulation tasks including semantic grocery restocking and 3–5 minute long-horizon tasks.
- *Results:* A single generalist policy reached **95% average success rate**, with the largest gains on the long-horizon tasks.

### April 2026

**[DiscreteRTC: Discrete Diffusion Policies are Natural Asynchronous Executors](https://arxiv.org/abs/2604.25050)** — Pengcheng Wang, Kaiwen Hong, Chensheng Peng et al. (UC Berkeley; UIUC; UT Austin; UCLA), arXiv, 2026-04-27
- *Intuition:* Discrete diffusion's native inpainting mechanism fits asynchronous real-time chunk execution better than flow matching, which needs external correction.
- *Contribution:* A discrete-diffusion action-chunking policy that natively re-plans asynchronously through iterative unmasking, with no extra guidance heuristics.
- *Setup:* A real-world dynamic manipulation task ("hockey defend") plus dynamic simulated benchmarks.
- *Results:* **65% higher success than flow-matching RTC** and 30% higher than training-time flow-matching RTC, at ~0.7× the inference cost.

**[RL Token: Bootstrapping Online RL with Vision-Language-Action Models](https://arxiv.org/abs/2604.23073)** — Charles Xu, Jost Tobias Springenberg, Michael Equi et al. (Physical Intelligence), arXiv, 2026-04-24
- *Intuition:* A compact readout token is an efficient online-RL interface into a large pretrained VLA that does not disturb the base model's task knowledge.
- *Contribution:* Trains a small actor-critic on an "RL token" while keeping the policy anchored to the base VLA.
- *Setup:* Four real precision tasks — screw installation, zip-tie fastening, charger insertion, and Ethernet insertion.
- *Results:* **Up to 3× improvement** on difficult task segments with large success gains after minutes to hours of practice, surpassing human teleoperation speed on some tasks.

**[Learning Whole-Body Humanoid Locomotion via Motion Generation and Motion Tracking](https://arxiv.org/abs/2604.17335)** — Zewei Zhang, Kehan Wen, Michael Xu et al. (ETH Zurich; Simon Fraser University; EPFL), IEEE RA-L, 2026-04-19
- *Intuition:* A diffusion model supplying terrain-aware reference motions, tracked by an RL whole-body controller, yields adaptive directional humanoid locomotion.
- *Contribution:* Couples a real-time terrain-aware diffusion motion generator with an RL-trained whole-body motion tracker.
- *Setup:* Deployed on the Unitree G1 humanoid.
- *Results:* Successful hardware traversal of boxes, hurdles, stairs, and mixed-terrain combinations; no named-baseline table retrieved.

**[π0.7: a Steerable Generalist Robotic Foundation Model with Emergent Capabilities](https://arxiv.org/abs/2604.15483)** — Physical Intelligence, Bo Ai, Ali Amin et al. (Physical Intelligence), arXiv, 2026-04-16
- *Intuition:* Richer contextual conditioning lets one generalist policy be steered to behave like a specialist.
- *Contribution:* A 5B-parameter VLA using expanded multimodal context conditioning (language, strategy information, quality and performance metadata) to absorb demonstrations, autonomous data including failures, and non-robot sources across embodiments.
- *Setup:* Multi-stage kitchen-appliance tasks, laundry folding via zero-shot cross-embodiment transfer, and espresso-machine operation.
- *Results:* **Matches the performance of much more specialized RL-finetuned models on the espresso task out of the box**, with stronger instruction following than π0 and π0.5.

**[StarVLA: A Lego-like Codebase for Vision-Language-Action Model Developing](https://arxiv.org/abs/2604.05014)** — StarVLA Community (Von Neumann Institute, HKUST), arXiv, 2026-04-06
- *Intuition:* VLA progress is slowed by fragmentation across mutually incompatible codebases.
- *Contribution:* A modular open-source framework with interchangeable VLM/world-model backbones, reusable cross-embodiment training recipes, and unified evaluation.
- *Setup:* Major VLA methods reproduced in a single codebase and benchmarked on LIBERO and RoboCasa-GR1.
- *Results:* Reproducible recipes **match or surpass prior published methods** despite minimal data engineering.

### March 2026

**[FASTER: Rethinking Real-Time Flow VLAs](https://arxiv.org/abs/2603.19199)** — Yuxiang Lu, Zhe Liu, Xianzhe Fan et al. (University of Hong Kong; ACE Robotics), arXiv, 2026-03-19
- *Intuition:* Constant denoising schedules waste steps on far-future actions, so prioritizing near-term action denoising cuts reaction latency.
- *Contribution:* A Horizon-Aware Schedule reducing flow-VLA denoising roughly 10× toward near-single-step, plus a streaming client-server inference pipeline.
- *Setup:* Applied to π0.5 and X-VLA on a highly dynamic real-world table-tennis task using a consumer-grade GPU.
- *Results:* Substantially improved real-time responsiveness versus standard asynchronous inference for **π0.5 and X-VLA**; single headline number `unknown`.

**[Fast-WAM: Do World Action Models Need Test-time Future Imagination?](https://arxiv.org/abs/2603.16666)** — Tianyuan Yuan, Zibin Dong, Yicheng Liu et al. (IIIS, Tsinghua University; Galaxea AI), arXiv, 2026-03-17
- *Intuition:* The value of video prediction in world-action models may come from training-time representation learning rather than test-time imagination.
- *Contribution:* Keeps video co-training but drops future-frame generation entirely at inference.
- *Setup:* Real-world and simulated manipulation benchmarks.
- *Results:* **4× faster than imagine-then-execute WAM baselines** at 190 ms latency, with competitive success rates.

**[Learning Athletic Humanoid Tennis Skills from Imperfect Human Motion Data](https://arxiv.org/abs/2603.12686)** — Zhikai Zhang, Haofei Lu, Yunrui Lian et al. (Tsinghua University; Peking University; Galbot; Shanghai Qi Zhi Institute; Shanghai AI Laboratory), arXiv, 2026-03-13
- *Intuition:* Complete, perfect demonstrations are unnecessary — motion fragments capturing primitive skills can be corrected and recombined.
- *Contribution:* LATENT, a method for policy learning from imperfect and fragmentary human motion data.
- *Setup:* Unitree G1 humanoid performing sustained real-world tennis rallies against human opponents.
- *Results:* Consistent ball return to targets in hardware-validated multi-shot rallies; no named-baseline table retrieved.

**[RoboClaw: An Agentic Framework for Scalable Long-Horizon Robotic Tasks](https://arxiv.org/abs/2603.11558)** — Ruiying Li, Yunlang Zhou, YuYao Zhu et al. (AgiBot; National University of Singapore; Shanghai Jiao Tong University), arXiv, 2026-03-12
- *Intuition:* Pairing each forward manipulation with a matched recovery behavior lets data collection reset itself autonomously.
- *Contribution:* "Entangled Action Pairs" inside a unified VLM-controlled agentic framework spanning data collection, learning, and deployment.
- *Setup:* A long-horizon manipulation task suite.
- *Results:* **+25% success rate over baselines** with a 53.7% reduction in human supervision time.

**[Ψ0: An Open Foundation Model Towards Universal Humanoid Loco-Manipulation](https://arxiv.org/abs/2603.12263)** — Songlin Wei, Hongyi Jing, Boqian Li et al. (USC Physical Superintelligence Lab; NVIDIA; WorldEngine), arXiv, 2026-03-12
- *Intuition:* Staged pretraining on egocentric human video before humanoid post-training reduces how much robot data is needed.
- *Contribution:* An open foundation model combining VLM pretraining with a flow-based action expert for humanoid loco-manipulation.
- *Setup:* Humanoid robot hardware evaluation.
- *Results:* Strong performance with minimal robot data relative to baselines; specific numbers `unknown`.

**[MEM: Multi-Scale Embodied Memory for Vision Language Action Models](https://arxiv.org/abs/2603.03596)** — Marcel Torne, Karl Pertsch, Homer Walke et al. (Physical Intelligence; Stanford University; UC Berkeley; MIT), arXiv, 2026-03-04
- *Intuition:* Robots need both occlusion-robust short-term memory and semantic long-term memory to carry out extended tasks.
- *Contribution:* Fuses video-based short-horizon memory with text-based long-horizon memory inside a VLA.
- *Setup:* Real-robot tasks lasting up to 15 minutes, including kitchen cleanup and sandwich preparation.
- *Results:* Enables within-task strategy adaptation and became the memory encoder inside π0.7; no named-baseline table retrieved.

## Verification ledger

| # | candidate_id | title | link | date | citations | cites/mo | source | affiliation | checks | verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | arXiv:2607.01088 | ROSA | https://arxiv.org/abs/2607.01088 | 2026-07-01 | 0 | exempt | S2 | NVIDIA Research | canonical+meta+citation+sota+affiliation | LIVE |
| 2 | arXiv:2606.31958 | Semantic RL (SARL) | https://arxiv.org/abs/2606.31958 | 2026-06-30 | 0 | exempt | S2 | UC Berkeley | canonical+meta+citation+sota+affiliation | LIVE |
| 3 | arXiv:2606.27375 | ABC (Scalable Behavior Cloning) | https://arxiv.org/abs/2606.27375 | 2026-06-25 | 2 | exempt | S2 | UC Berkeley | canonical+meta+citation+sota+affiliation | LIVE |
| 4 | arXiv:2606.26428 | Play2Perfect | https://arxiv.org/abs/2606.26428 | 2026-06-24 | 0 | exempt | S2 | Stanford University | canonical+meta+citation+sota+affiliation | LIVE |
| 5 | arXiv:2607.00033 | CHORD | https://arxiv.org/abs/2607.00033 | 2026-06-22 | 0 | exempt | S2 | NVIDIA | canonical+meta+citation+sota+affiliation | LIVE |
| 6 | arXiv:2606.21406 | DGAC | https://arxiv.org/abs/2606.21406 | 2026-06-19 | 1 | exempt | S2 | ETH Zürich | canonical+meta+citation+sota+affiliation | LIVE |
| 7 | arXiv:2606.19980 | ENPIRE | https://arxiv.org/abs/2606.19980 | 2026-06-18 | 1 | exempt | S2 | Carnegie Mellon University | canonical+meta+citation+sota+affiliation | LIVE |
| 8 | arXiv:2606.20092 | EventVLA | https://arxiv.org/abs/2606.20092 | 2026-06-18 | 2 | exempt | S2 | USTC | canonical+meta+citation+sota+affiliation | LIVE |
| 9 | arXiv:2606.17011 | ROVE | https://arxiv.org/abs/2606.17011 | 2026-06-15 | 0 | exempt | S2 | Fudan University | canonical+meta+citation+sota+affiliation | LIVE |
| 10 | arXiv:2606.14409 | Hy-Embodied-0.5-VLA | https://arxiv.org/abs/2606.14409 | 2026-06-12 | 5 | exempt | S2 | Tencent (Robotics X) | canonical+meta+citation+sota+affiliation | LIVE |
| 11 | arXiv:2606.12965 | EmbodiSteer | https://arxiv.org/abs/2606.12965 | 2026-06-11 | 0 | exempt | S2 | Tsinghua University | canonical+meta+citation+sota+affiliation | LIVE |
| 12 | arXiv:2606.12372 | UniIntervene | https://arxiv.org/abs/2606.12372 | 2026-06-10 | 1 | exempt | S2 | Nanyang Technological University | canonical+meta+citation+sota+affiliation | LIVE |
| 13 | arXiv:2606.09337 | TORL-VLA | https://arxiv.org/abs/2606.09337 | 2026-06-08 | 0 | exempt | S2 | Beihang University | canonical+meta+citation+sota+affiliation | LIVE |
| 14 | arXiv:2606.05468 | FlowPRO | https://arxiv.org/abs/2606.05468 | 2026-06-03 | 1 | exempt | S2 | Tsinghua University | canonical+meta+citation+sota+affiliation | LIVE |
| 15 | arXiv:2606.00537 | PACE | https://arxiv.org/abs/2606.00537 | 2026-05-30 | 0 | exempt | S2 | Peking University | canonical+meta+citation+sota+affiliation | LIVE |
| 16 | arXiv:2605.30226 | BORA | https://arxiv.org/abs/2605.30226 | 2026-05-28 | 0 | exempt | S2 | Shanghai Jiao Tong University | canonical+meta+citation+sota+affiliation | LIVE |
| 17 | arXiv:2605.03269 | RLDX-1 | https://arxiv.org/abs/2605.03269 | 2026-05-05 | 9 | exempt | S2 | KAIST | canonical+meta+citation+sota+affiliation | LIVE |
| 18 | arXiv:2605.02881 | MolmoAct2 | https://arxiv.org/abs/2605.02881 | 2026-05-04 | 18 | exempt | S2 | Allen Institute for AI | canonical+meta+citation+sota+affiliation | LIVE |
| 19 | arXiv:2605.00416 | Learning while Deploying | https://arxiv.org/abs/2605.00416 | 2026-05-01 | 5 | exempt | S2 | Columbia University | canonical+meta+citation+sota+affiliation | LIVE |
| 20 | arXiv:2604.25050 | DiscreteRTC | https://arxiv.org/abs/2604.25050 | 2026-04-27 | 1 | exempt | S2 | UC Berkeley | canonical+meta+citation+sota+affiliation | LIVE |
| 21 | arXiv:2604.23073 | RL Token | https://arxiv.org/abs/2604.23073 | 2026-04-24 | 20 | exempt | S2 | Physical Intelligence | canonical+meta+citation+sota+affiliation | LIVE |
| 22 | arXiv:2604.17335 | Whole-Body Humanoid Locomotion | https://arxiv.org/abs/2604.17335 | 2026-04-19 | 8 | 2.7 | S2 | ETH Zürich | canonical+meta+citation+sota+affiliation | LIVE |
| 23 | arXiv:2604.15483 | π0.7 | https://arxiv.org/abs/2604.15483 | 2026-04-16 | 78 | 25.2 | S2 | Physical Intelligence | canonical+meta+citation+sota+affiliation | LIVE |
| 24 | arXiv:2604.05014 | StarVLA | https://arxiv.org/abs/2604.05014 | 2026-04-06 | 65 | 19.0 | S2 | HKUST | canonical+meta+citation+sota+affiliation | LIVE |
| 25 | arXiv:2603.19199 | FASTER | https://arxiv.org/abs/2603.19199 | 2026-03-19 | 8 | 2.0 | S2 | University of Hong Kong | canonical+meta+citation+sota+affiliation | LIVE |
| 26 | arXiv:2603.16666 | Fast-WAM | https://arxiv.org/abs/2603.16666 | 2026-03-17 | 105 | 25.6 | S2 | Tsinghua University | canonical+meta+citation+sota+affiliation | LIVE |
| 27 | arXiv:2603.12686 | LATENT (humanoid tennis) | https://arxiv.org/abs/2603.12686 | 2026-03-13 | 12 | 2.8 | S2 | Tsinghua University | canonical+meta+citation+sota+affiliation | LIVE |
| 28 | arXiv:2603.11558 | RoboClaw | https://arxiv.org/abs/2603.11558 | 2026-03-12 | 12 | 2.8 | S2 | National University of Singapore | canonical+meta+citation+sota+affiliation | LIVE |
| 29 | arXiv:2603.12263 | Ψ0 | https://arxiv.org/abs/2603.12263 | 2026-03-12 | 21 | 4.9 | S2 | University of Southern California | canonical+meta+citation+sota+affiliation | LIVE |
| 30 | arXiv:2603.03596 | MEM | https://arxiv.org/abs/2603.03596 | 2026-03-04 | 35 | 7.7 | S2 | Physical Intelligence | canonical+meta+citation+sota+affiliation | LIVE |

## Dropped candidates

| candidate_id | title | reason |
|---|---|---|
| arXiv:2604.22235 | Learning-augmented robotic automation for real-world manufacturing | institution: not on accept-list (Neuromeka Co., Ltd) |
| arXiv:2604.20246 | Cortex 2.0: Grounding World Models in Real-World Industrial Deployment | institution: not on accept-list (Sereact GmbH) |
| arXiv:2605.30877 | Wall-OSS-0.5 Technical Report | institution: not on accept-list (X Square Robot) |
| arXiv:2604.27792 | MotuBrain: An Advanced World Action Model | institution: affiliation unresolved (author block names only "MotuBrain Team"; institution appears only in third-party press coverage) |
| arXiv:2605.30280 | Qwen-VLA | institution: affiliation unresolved (arXiv HTML 404, PDF over fetch limit; only "Qwen Team" from GitHub) |
| arXiv:2603.06749 | Robotic Foundation Models for Industrial Control: survey | citation floor: 0 cites over 4.5 months = 0.0/mo < 2 |
| arXiv:2603.15469 | RoCo Challenge at AAAI 2026 (gearbox assembly) | citation floor: 0 cites over 4.1 months = 0.0/mo < 2 |
| arXiv:2603.16065 | Large Reward Models | citation floor: 6 cites over 4.1 months = 1.5/mo < 2 |
| arXiv:2603.05504 | RoboPocket | citation floor: 6 cites over 4.5 months = 1.3/mo < 2 |
| arXiv:2603.18532 | Scaling Sim-to-Real RL with Generative 3D Worlds | citation floor: 3 cites over 4.0 months = 0.7/mo < 2 |
| arXiv:2603.26360 | Realtime-VLA V2 | citation floor: 3 cites over 3.7 months = 0.8/mo < 2 |
| arXiv:2603.05117 | SeedPolicy | citation floor: 3 cites over 4.5 months = 0.7/mo < 2 |
| arXiv:2603.15265 | MoE-ACT | citation floor: 3 cites over 4.1 months = 0.7/mo < 2 |
| arXiv:2603.12243 | HandelBot (real-world piano) | citation floor: 2 cites over 4.2 months = 0.5/mo < 2 |
| arXiv:2603.15759 | Simulation Distillation | citation floor: 2 cites over 4.1 months = 0.5/mo < 2 |
| arXiv:2603.19632 | ContractionPPO | citation floor: 1 cite over 4.0 months = 0.3/mo < 2 |
| arXiv:2603.10971 | ContactExplorer | citation floor: 0 cites over 4.3 months = 0.0/mo < 2 |
| arXiv:2603.17653 | REAL (extreme agility) | citation floor: 0 cites over 4.0 months = 0.0/mo < 2 |
| arXiv:2603.11400 | Deployment-Time Reliability of Learned Robot Policies | citation floor: 0 cites over 4.2 months = 0.0/mo < 2 |
| arXiv:2604.09487 | Sim-to-Real for Muscle-Actuated Robots (GenAN) | citation floor: 0 cites over 3.3 months = 0.0/mo < 2 |
| arXiv:2603.04356 | RoboCasa365 | passed all gates; not selected — simulation-only framework, weakest fit to the production/realistic-task requirement |
| arXiv:2603.22435 | CaP-X | passed all gates; not selected — coding-agent benchmark, weaker production fit |
| arXiv:2603.04639 | RoboMME | passed all gates; not selected — simulation memory benchmark, weaker production fit |
| arXiv:2603.10448 | DiT4DiT | passed all gates; not selected — LIBERO-centric evaluation |
| arXiv:2603.22264 | UniDex | passed all gates; not selected — dataset/suite with no retrieved named-baseline result |
| arXiv:2607.04434 | RoboDojo | passed all gates; not selected — evaluation infrastructure rather than a SOTA policy result |
| arXiv:2606.30552 | ZR-0 (Dense Embodied CoT) | passed all gates; not selected — no named-baseline numbers retrieved |
| arXiv:2606.32009 | Human-as-Humanoid | passed all gates; not selected — data-pipeline throughput result, weaker task-performance evidence |
| arXiv:2607.02431 | WorldSample | passed all gates; not selected — setup details not retrievable beyond the abstract |
| arXiv:2604.21924 | LoHo-Manip (Trace-Conditioned VLA Planning) | affiliation gate not run (outside the top-44 sent to validation) |
| arXiv:2605.12090 | World Action Models (survey) | relevance: survey, not a SOTA result |
| arXiv:2606.06660 | AEGIS | relevance: simulation-only (LIBERO), no real-robot component |
| arXiv:2606.16826 | ATOM-Bench | passed date/relevance; benchmark, affiliation gate not run |
| arXiv:2605.20774 | VLA-REPLICA | passed date/relevance; benchmark, affiliation gate not run |
| arXiv:2607.04426 | ACE-Brain-0.5 | passed date/relevance; affiliation gate not run (benchmark-only evidence) |
| arXiv:2606.30534 | Orca | relevance: upstream world model, no robot success-rate evidence |
| arXiv:2607.04591 | Simple-to-Complex Structured Demonstrations | passed date/relevance; affiliation gate not run (lower SOTA fit) |
| arXiv:2606.11628 | LUCID | passed date/relevance; affiliation gate not run (no quantitative baseline) |
| arXiv:2606.08828 | Video2Sim2Real | passed date/relevance; affiliation gate not run (no numeric baseline) |
| arXiv:2607.03865 | One-Step Generative Visuomotor Policy | passed date/relevance; affiliation gate not run (lower SOTA fit) |
| arXiv:2607.01804 | VLA-Corrector | passed date/relevance; affiliation gate not run (no numeric results) |
| arXiv:2606.06461 | GLOVES (Flow-based Policy Adaptation) | passed date/relevance; affiliation gate not run (no numeric baseline) |
| arXiv:2606.31043 | Warp RL | passed date/relevance; affiliation gate not run (lower SOTA fit) |
| arXiv:2605.09595 | Neuromorphic RL for Quadruped Locomotion | passed date/relevance; affiliation gate not run (lower SOTA fit) |
| arXiv:2605.25537 | Action-Prior Denoising (Soft RTC) | passed date/relevance; affiliation gate not run (mostly simulated) |
| arXiv:2606.12365 | Ambient Diffusion Policy | passed date/relevance; affiliation gate not run (lower SOTA fit) |
| arXiv:2604.17787 | AnchorRefine | passed date/relevance; affiliation gate not run (lower SOTA fit) |
| arXiv:2510.14830 | RL-100 | date floor: first arXiv version 2025-10, before 2026-03 |
| arXiv:2511.14759 | π*0.6 | date floor: first arXiv version 2025-11, before 2026-03 |
| arXiv:2512.01801 | GR-RL (ByteDance Seed) | date floor: first arXiv version 2025-12, before 2026-03 |
| — | NVIDIA GR00T N2 | no arXiv/DOI paper located this session — only third-party blog coverage |
| — | Figure Helix warehouse deployment; Skild Brain; Dyna DYNA-1; Galbot; Agility; Covariant | company blog/press coverage only, no verifiable paper — excluded rather than cited from press claims |

## Coverage & limitations

- **Discovery lanes (4, run in parallel as real subagents):** (A) VLA / robot foundation models with real-world deployment emphasis; (B) RL for real robots — sim-to-real, RL post-training of VLAs, humanoid/legged hardware, contact-rich assembly; (C) imitation learning — diffusion/flow policies, action chunking, human-video-to-robot, bimanual/dexterous; (D) industrial-adoption and citation-velocity lane over industry labs and S2 citation-sorted bulk search. A fifth lane checked the classic ancestor via reference-list tallies.
- **Validation:** 3 affiliation-validation subagents fetched arXiv HTML author blocks for the 44 highest-SOTA-fit survivors. All 74 merged candidates were identity- and citation-verified in three Semantic Scholar `paper/batch` calls; every one resolved with a matching title (0 non-resolving).
- **Source conflict resolved:** Lane A reported citation counts of 0 from OpenAlex for papers that Semantic Scholar independently scored at 78, 35 and 5. OpenAlex under-indexes fresh preprints, so **all citation figures in this run come from Semantic Scholar**, re-queried by the orchestrator rather than taken from any worker ledger. Semantic Scholar returned HTTP 429 on one batch; it was retried with exponential backoff rather than treated as missing data.
- **Institution gate coverage is partial by design.** The gate ran on the 44 highest-SOTA-fit candidates, not all 57 citation-survivors, because 39 matches already exceeded the 30 requested. 17 candidates listed in *Dropped candidates* carry "affiliation gate not run" — they are not institution failures and may well qualify; they were simply outranked before the gate was reached.
- **Institution drops, reported separately as required:** **3 `no-match`** (Neuromeka, Sereact GmbH, X Square Robot — affiliations were established and none appears on the accept-list) and **2 `unresolved`** (MotuBrain, Qwen-VLA — the full ladder ran and no affiliation could be established from the paper itself). `unresolved` is a fact about metadata coverage, not a judgment on those authors. At 2 of 44 checked (~5%), the unresolved share is well below the one-fifth threshold that would call the filter's meaning into question.
- **A notable casualty of the institution filter:** arXiv:2604.22235 is by some distance the strongest pure production result found — a learned policy running unfenced on a real electric-motor production line for 5h10m, producing 108 motors at a 99.4% QC pass rate with a 159 s cycle time — but its sole affiliation, Neuromeka Co., Ltd, is not on the accept-list, so the filter dropped it. Worth requesting explicitly if industrial-floor evidence matters more than institutional pedigree.
- **Fields left `unknown`:** 9 result-line fields where the fetched pages carried no named-baseline comparison (SARL, ABC, CHORD, ROVE, Hy-Embodied, MolmoAct2, humanoid locomotion, Ψ0, LATENT, TORL-VLA, FASTER). These were left `unknown` rather than filled with plausible numbers.
- **Borderline citation call:** FASTER (arXiv:2603.19199) sits exactly at the floor — 8 citations over 4.0 months = 2.0/month. It was kept; a stricter day-count convention (1.996/mo) would drop it.
- **Search-tool cost:** 8 subagents made 402 tool calls in total plus 5 orchestrator calls; the search-versus-fetch split was not separately instrumented, so both are recorded `unknown` in the frontmatter rather than estimated.
- **Not verifiable this session:** several widely-publicized industrial deployments (Figure at BMW, Tesla Optimus, Skild, Dyna, Covariant) surfaced repeatedly in search results but have no corresponding arXiv or DOI paper; they are excluded rather than cited from press claims.

## Evaluate this run

Open `evaluate_results_gui.html`, load this file, and save the result to `evaluations/`. Run id: `vla-rl-imitation-learning_2026-07-19`.
