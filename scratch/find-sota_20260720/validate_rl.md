# RL / industrial-real-robot validation ledger (RL-1)

Validated on **2026-07-20**. Canonical identity and paper-first technical/affiliation evidence came from the linked arXiv paper. Citation counts came from the Semantic Scholar Graph API (`ARXIV:<id>`, batch fields `paperId,title,publicationDate,citationCount,externalIds,references.paperId,references.title`). Velocity is `citationCount / max(1, elapsed_days / 30.4375)`.

## Gate summary

- **LIVE: 14**
- **DROP: 1** — HapticVLA passes the date, citation, SOTA, and physical-robot gates, but every author is affiliated only with Skolkovo Institute of Science and Technology, which is absent from the curated general + robotics accept-lists.
- **CONFLICT: 1** — RL Token passes every technical/citation gate and the paper explicitly credits Physical Intelligence for the work, but the paper has no formal author-affiliation block, so at least one author's affiliation cannot be established paper-first.
- Citation gate: **16/16 pass** both total citations >=3 and velocity >=1 citation/month.
- Institution accept-list matches: **14 established matches**, **1 explicit no-match**, **1 affiliation unresolved**.

## Citation ledger

| arXiv | Semantic Scholar citations | publication date | elapsed days | elapsed months | citations/month | evidence |
|---|---:|---|---:|---:|---:|---|
| 2604.23073 | 20 | 2026-04-24 | 87 | 2.8583 | 6.9971 | [S2](https://api.semanticscholar.org/graph/v1/paper/ARXIV:2604.23073?fields=paperId,title,publicationDate,citationCount,externalIds) |
| 2603.12665 | 13 | 2026-03-13 | 129 | 4.2382 | 3.0673 | [S2](https://api.semanticscholar.org/graph/v1/paper/ARXIV:2603.12665?fields=paperId,title,publicationDate,citationCount,externalIds) |
| 2605.00416 | 5 | 2026-05-01 | 80 | 2.6283 | 1.9023 | [S2](https://api.semanticscholar.org/graph/v1/paper/ARXIV:2605.00416?fields=paperId,title,publicationDate,citationCount,externalIds) |
| 2603.15257 | 6 | 2026-03-16 | 126 | 4.1396 | 1.4494 | [S2](https://api.semanticscholar.org/graph/v1/paper/ARXIV:2603.15257?fields=paperId,title,publicationDate,citationCount,externalIds) |
| 2603.08122 | 6 | 2026-03-09 | 133 | 4.3696 | 1.3731 | [S2](https://api.semanticscholar.org/graph/v1/paper/ARXIV:2603.08122?fields=paperId,title,publicationDate,citationCount,externalIds) |
| 2604.07993 | 6 | 2026-04-09 | 102 | 3.3511 | 1.7904 | [S2](https://api.semanticscholar.org/graph/v1/paper/ARXIV:2604.07993?fields=paperId,title,publicationDate,citationCount,externalIds) |
| 2603.09971 | 7 | 2026-03-10 | 132 | 4.3368 | 1.6141 | [S2](https://api.semanticscholar.org/graph/v1/paper/ARXIV:2603.09971?fields=paperId,title,publicationDate,citationCount,externalIds) |
| 2605.18722 | 5 | 2026-05-18 | 63 | 2.0698 | 2.4157 | [S2](https://api.semanticscholar.org/graph/v1/paper/ARXIV:2605.18722?fields=paperId,title,publicationDate,citationCount,externalIds) |
| 2605.12369 | 4 | 2026-05-12 | 69 | 2.2669 | 1.7645 | [S2](https://api.semanticscholar.org/graph/v1/paper/ARXIV:2605.12369?fields=paperId,title,publicationDate,citationCount,externalIds) |
| 2605.07308 | 4 | 2026-05-08 | 73 | 2.3984 | 1.6678 | [S2](https://api.semanticscholar.org/graph/v1/paper/ARXIV:2605.07308?fields=paperId,title,publicationDate,citationCount,externalIds) |
| 2604.05672 | 4 | 2026-04-07 | 104 | 3.4168 | 1.1707 | [S2](https://api.semanticscholar.org/graph/v1/paper/ARXIV:2604.05672?fields=paperId,title,publicationDate,citationCount,externalIds) |
| 2605.31286 | 3 | 2026-05-29 | 52 | 1.7084 | 1.7560 | [S2](https://api.semanticscholar.org/graph/v1/paper/ARXIV:2605.31286?fields=paperId,title,publicationDate,citationCount,externalIds) |
| 2603.25406 | 6 | 2026-03-26 | 116 | 3.8111 | 1.5744 | [S2](https://api.semanticscholar.org/graph/v1/paper/ARXIV:2603.25406?fields=paperId,title,publicationDate,citationCount,externalIds) |
| 2604.21924 | 3 | 2026-04-23 | 88 | 2.8912 | 1.0376 | [S2](https://api.semanticscholar.org/graph/v1/paper/ARXIV:2604.21924?fields=paperId,title,publicationDate,citationCount,externalIds) |
| 2605.14712 | 3 | 2026-05-14 | 67 | 2.2012 | 1.3629 | [S2](https://api.semanticscholar.org/graph/v1/paper/ARXIV:2605.14712?fields=paperId,title,publicationDate,citationCount,externalIds) |
| 2605.28548 | 3 | 2026-05-27 | 54 | 1.7741 | 1.6910 | [S2](https://api.semanticscholar.org/graph/v1/paper/ARXIV:2605.28548?fields=paperId,title,publicationDate,citationCount,externalIds) |

## Candidate validation rows

### CONFLICT — [RL Token: Bootstrapping Online RL with Vision-Language-Action Models](https://arxiv.org/html/2604.23073)

- **Physical validation:** Four real-robot precision tasks: screw installation, zip-tie fastening (explicitly bimanual), charger insertion, and Ethernet insertion; 400–1,000 online episodes / about 15 minutes to 5 hours of actual robot data per task, at 50 Hz.
- **SOTA/result evidence:** Screw critical-phase success rises **20% -> 65%**; critical phases become up to **3x faster**; full-task success rises by **40 points** on screw and **60 points** on zip tie. On Ethernet, DAgger and DSRL reach comparable success, but RLT halves mean steps versus the base VLA; HIL-SERL and Probe-Learn-Distill fail to learn effectively.
- **Institution evidence:** The paper explicitly thanks “all of the people at Physical Intelligence” for hardware, data collection, robot operations, and infrastructure; Physical Intelligence is on the robotics accept-list. However, no author-affiliation block maps an author to PI.
- **Verdict reason:** Technical gates pass; **affiliation could not be formally established**, so do not silently count this as an institution drop or accept-list pass.

### LIVE — [TacVLA: Contact-Aware Tactile Fusion for Robust Vision-Language-Action Manipulation](https://arxiv.org/html/2603.12665)

- **Physical validation:** 7-DoF Franka with tactile sensors and two cameras; four constraint-locked disassembly tasks plus in-box picking, 50 demonstrations/task, including occlusion and disturbance tests.
- **SOTA/result evidence:** Mean disassembly success **83.75%**, versus fine-tuned pi0.5 **63.75%**, image Diffusion Policy **48.75%**, and 3D Diffusion Policy **31.25%**; heavy-occlusion picking is **70% vs 10%** for pi0.5.
- **Institution match:** Purdue University and Istituto Italiano di Tecnologia, both accepted (general / robotics lists).

### LIVE — [Learning while Deploying: Fleet-Scale Reinforcement Learning for Generalist Robot Policies](https://arxiv.org/html/2605.00416)

- **Physical validation:** A fleet of **16 AgiBot G1** dual-arm robots; four realistic grocery-restocking tasks and four 3–5 minute long-horizon tasks (Gongfu tea, fruit juice, cocktail, shoebox packing).
- **SOTA/result evidence:** LWD Online averages **0.95** across eight tasks, versus SFT **0.76**, RECAP **0.85**, HG-DAgger **0.85**, and LWD Offline **0.88**; long-horizon mean is **0.91** versus **0.68/0.77/0.73/0.79**, respectively.
- **Institution match:** Columbia University is in the author affiliations and the general accept-list (also Shanghai Innovation Institute / AGIBOT Finch).

### DROP — [HapticVLA: Contact-Rich Manipulation via Vision-Language-Action Model without Inference-Time Tactile Sensing](https://arxiv.org/html/2603.15257)

- **Physical validation:** Bimanual pair of LeRobot SO-101 arms, one tactile gripper, RealSense D435 plus wrist cameras; jar, waffle, and egg manipulation, 20 evaluations/task.
- **SOTA/result evidence:** Mean success **86.7%**; SA-RWFM teacher **75%**; X-VLA and VLA-0 **0%**; egg manipulation improves **45 points** over base SmolVLA.
- **Institution drop:** The paper says **all authors** are with Skolkovo Institute of Science and Technology; Skoltech is absent from both curated institution lists. This is an explicit no-match, not an unresolved affiliation.

### LIVE — [Towards Human-Like Manipulation through RL-Augmented Teleoperation and Mixture-of-Dexterous-Experts VLA](https://arxiv.org/html/2603.08122)

- **Physical validation:** 63-DoF bimanual dexterous humanoid system; gear assembly, charger plugging, test-tube rearrangement, and apple peeling (claimed first autonomous dual-dexterous-hand apple peeling).
- **SOTA/result evidence:** MoDE-VLA averages **34%** success versus pi0 **15%** (a **19-point** gain); gear and charger insertion improve by **20** and **10** points. IMCopilot teleoperation support reaches **89% (80/90)** versus direct teleoperation **34% (31/90)**.
- **Institution match:** Shanghai Jiao Tong University, Shanghai AI Laboratory, and National University of Singapore appear in the paper and accepted lists.

### LIVE — [HEX: Humanoid-Aligned Experts for Cross-Embodiment Whole-Body Manipulation](https://arxiv.org/html/2604.07993)

- **Physical validation:** Seven real whole-body tasks on **Tienkung 2.0 and 3.0** humanoids plus a long-horizon box-convey task; training spans seven humanoid embodiments and 12M+ frames.
- **SOTA/result evidence:** Generalization average **61.8%**, versus pi0.5 **44.3%**, GR00T N1.5 **41.0%**, and SwitchVLA **22.4%**; overall success **79.8%** at 73.34 ms, highest among compared methods; final box placement is about **15 points** above the strongest baseline.
- **Institution match:** Xi’an Jiaotong University and Peking University are accepted institutions.

### LIVE — [TiPToP: A Modular Open-Vocabulary Planning System for Robotic Manipulation](https://arxiv.org/html/2603.09971)

- **Physical validation:** Franka FR3 DROID rigs with wrist ZED stereo, independently evaluated; additional real deployment on UR5e and Trossen WidowX; 28 scenes / 165 comparison trials plus 173 diagnostic trials.
- **SOTA/result evidence:** With **zero robot training data**, distractor-scene success is **60.0%** versus pi0.5-DROID **26.7%**; TiPToP wins 6/8 distractor and 7/8 semantic scenes and is about 2x faster on single-step real tasks (e.g. can-to-mug **18.6 s vs 41.0 s**).
- **Institution match:** Paper-first MIT correspondence addresses and MIT support, plus named Penn external evaluation/author contributions; MIT and University of Pennsylvania are accepted.

### LIVE — [Dexora: Open-source VLA for High-DoF Bimanual Dexterity](https://arxiv.org/html/2605.18722)

- **Physical validation:** Open 36-DoF dual-arm/dual-12-DoF-hand platform and MuJoCo twin; 10K real and 100K simulation episodes; six real dexterous tasks including pen use, book retrieval, cutting, plate placement, dough handling, and cap twisting.
- **SOTA/result evidence:** Dexterous-task average **66.7%**, versus GR00T N1 **51.7%**, pi0 **26.7%**, and Diffusion Policy **6.7%**; also demonstrates transfer to Franka, ALOHA, and Unitree G1 embodiments.
- **Institution match:** Tsinghua University, BAAI, HKU, Shanghai Jiao Tong, ShanghaiTech, and Peking University are accepted.

### LIVE — [GuidedVLA: Specifying Task-Relevant Factors via Plug-and-Play Action Attention Specialization](https://arxiv.org/html/2605.12369)

- **Physical validation:** Six real tasks across ALOHA AgileX (household picking, bowl stacking, table cleaning) and PSI-Bot/RealMan (beaker placement, stacking, heating), 20 trials/setting under position, scene, and lighting shifts.
- **SOTA/result evidence:** GuidedVLA averages **75.8% vs 55.8%** for base pi0 in-domain, **67.5% vs 44.2%** under scene shift, and **79.2% vs 57.5%** under lighting shift; up to **52.7% relative gain**.
- **Institution match:** Fudan University, Shanghai Jiao Tong University, and University of Hong Kong are accepted.

### LIVE — [AT-VLA: Adaptive Tactile Injection for Enhanced Feedback Reaction in Vision-Language-Action Models](https://arxiv.org/html/2605.07308)

- **Physical validation:** AgiBot Genie1 with dual 7-DoF arms, three cameras, and Xense tactile gripper; unzip bag, stamp, wipe vase, unscrew lid plus two non-contact tasks, 15 trials/task; tactile closed loop in **0.04 s**.
- **SOTA/result evidence:** Overall success is **0.33/0.46/0.67/0.53** on unzip/stamp/wipe/unscrew, versus GO-1 **0.20/0.13/0.07/0.27** and pi0.5 **0/0.20/0.33/0.46**; it also beats tactile VTLA/RDP on three of four contact phases despite those baselines receiving idealized initial grasps.
- **Institution match:** Peking University is accepted.

### LIVE — [A1: A Fully Transparent Open-Source, Adaptive and Efficient Truncated Vision-Language-Action Model](https://arxiv.org/html/2604.05672)

- **Physical validation:** Franka, AgiBot, OpenArm, and Dobot-Arm, seven tasks and 3,000+ trajectories; additionally the 30-task multi-embodiment RoboChallenge real-robot benchmark.
- **SOTA/result evidence:** Four-platform real-world average **56.7%**, versus pi0.5 **47.5%** and pi0 **40.8%**; RoboChallenge **29.00%** versus pi0 **28.33%**, X-VLA **21.33%**, RDT-1B **15.00%**, while reducing per-episode flow latency by up to **72%**. Caveat: it ranks sixth overall on RoboChallenge, so the best-at-time claim is relative to the named open baselines, not the entire leaderboard.
- **Institution match:** Sun Yat-sen University is in the author affiliation line and general accept-list.

### LIVE — [DeMaVLA: A Vision-Language-Action Foundation Model for Generalizable Deformable Manipulation](https://arxiv.org/html/2605.31286)

- **Physical validation:** ALOHA-style dual-arm robot; complete 5-minute household folding pipelines for shirt, skirt, pants, and towel starting from random basket drops, 20 trials/task; pre-trained on about 5,000 hours real dual-arm demonstrations and post-trained with real HIL-DAgger corrections.
- **SOTA/result evidence:** One multi-task checkpoint averages **92.5%** versus fine-tuned pi0 **76.3%**, with towel folding **100% vs 55%** and mean completion time **2:18 vs 2:26**; single-task shirt folding **100% vs 80%**.
- **Institution match:** Tongji University is accepted (paper also lists AIRC, Midea Group).

### LIVE — [MMaDA-VLA: Large Diffusion Vision-Language-Action Model with Unified Multi-Modal Instruction and Generation](https://arxiv.org/pdf/2603.25406)

- **Physical validation:** AgileX Piper 6-DoF arm, gripper, RealSense D435 and wrist camera; dynamic pick-and-place, precision stacking, drawer storage, and long-horizon tableware organization.
- **SOTA/result evidence:** Real success is **83.3%–93.3%** across four settings versus GR00T N1.6 **56.7%–70.0%**; additionally reports then-SOTA LIBERO **98.0%** and CALVIN average length **4.78**.
- **Institution match:** Westlake University, Zhejiang University, Huawei, and HKUST(GZ) are accepted.

### LIVE — [Long-Horizon Manipulation via Trace-Conditioned VLA Planning (LoHo-Manip)](https://arxiv.org/html/2604.21924)

- **Physical validation:** Real Franka with top and wrist RealSense cameras, 100 demonstrations; one-, two-, and three-step tasks under ID and OOD objects/instructions; manager runs about 2 Hz and executor about 10 Hz.
- **SOTA/result evidence:** [Paper figure 7](https://arxiv.org/html/2604.21924v1/x7.png) reports LoHo-Manip vs same-data pi0.5: one-step ID **93% vs 86%**, two-step ID **70% vs 60%**, two-step OOD **75% vs 0%**, and three-step OOD **60% vs 0%**.
- **Institution match:** UC San Diego and NVIDIA are accepted.

### LIVE — [IntentVLA: Short-Horizon Intent Modeling for Aliased Robot Manipulation](https://arxiv.org/html/2605.14712)

- **Physical validation:** Dual Franka Research 3 arms with Robotiq 85 grippers and RealSense head/hand cameras; four-snack cleanup into a bag, 300 demonstrations and 50 trials/model.
- **SOTA/result evidence:** Versus pi0.5, at-least-two/three-snack completion is **62%/32% vs 44%/18%**, expected placed snacks **1.86 vs 1.44**, and IntentVLA alone collects all four within budget. It also leads AliasBench at **45.8%** versus Qwen3-VL-GR00T **9.0%**, MemoryVLA **14.9%**, and strongest direct-history baseline **28.1%**.
- **Institution match:** HUST, HIT, HKUST(GZ), Beihang, and USTC are accepted.

### LIVE — [GEM: Generative Supervision Helps Embodied Intelligence](https://arxiv.org/pdf/2605.28548)

- **Physical validation:** GEM-VLA on a real UR5; cloth folding, backpack unzipping, and long-horizon table bussing, 50 runs/task.
- **SOTA/result evidence:** Average all-task success **43.0%**, versus GEM-VLA without depth supervision **40.7%**, Qwen3VL-T-SFT **33.7%**, pi0.5 **28.7%**, and pi0-FAST **22.3%**; cloth-folding, both sleeve subtasks, unzipping, and table-bussing progress all lead the baselines.
- **Institution match:** Tsinghua University and Tencent Hunyuan are accepted.

## Relationship graph

Semantic Scholar `references.paperId` data were fetched for all 16 assigned S2 paper IDs and intersected with the same 16-ID set. The intersection was empty. Searches of the paper text for the other assigned titles/method names also found no within-set statement that one explicitly “builds on” another.

```text
# citation edges among the 16 assigned candidates: none evidenced
# explicit build-on edges among the 16 assigned candidates: none evidenced
```

Accordingly these papers must remain disconnected in the requested evidence-only relationship graph unless the root validation pass finds cross-set edges from other candidates; topical similarity alone is not an edge.
