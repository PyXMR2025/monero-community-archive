---
title: 'Proof-of-Time for Monero PoW: Achieving Instant Finality, Eliminating Re-orgs
  and Preventing Selfish Mining, Irrelevance of 51% attacks (Adapt or Perish)'
source_url: https://github.com/monero-project/research-lab/issues/147
author: r-a-d-a-n-n-e
assignees: []
labels: []
created_at: '2025-10-01T18:38:47+00:00'
updated_at: '2025-10-18T17:09:51+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
[Proof-of-Time Blueprint.pdf](https://github.com/user-attachments/files/22646314/Proof-of-Time.Blueprint.pdf)

# Abstract

The Proof-of-Time protocol augments the RandomX PoW model by binding a timechain subset model.  In tandem with modest PoW model adjustments, it achieves instant finality, eliminates block reorganizations and selfish mining, and defends community tenets by averting the PoW model from becoming subservient to PoS, precluding network and community split.


Proof-of-Time introduces a 30-second grace period deadlines derived from RandomX hash outputs bound to the public key, allowing miners to compete effectively with lower-deadline solutions.  The system supports both solo mining and shared mining models, enabling proportional rewards and optional hashrate sampling, without bloating the blockchain and eliminating the need for pools.  Through decentralized time consensus, without the need for OS clock synchronization, it renders 51% dominance inconsequential and features a maximum block time that prevents chain death.


Drawing from a reference ANNE datachain Proof-of-Spacetime (PoST) implementation, the Proof-of-Time model presents a decentralized timekeeping system that incentivizes network participation, offering a secure, lightweight, low-bandwidth-compatible solution with no network-wide aftermath rollbacks.


Time emerges as an integral aspect of PoW through probabilistic block production, empowering the network to self-govern and make decisions before it acts.


# 1.  Introduction

The "longest chain" principle in Proof-of-Work consensus, albeit foundational to many blockchains, represents a probabilistic mechanism that introduces inherent vulnerabilities, including block reorganizations, selfish mining, and susceptibility to 51% attacks, thereby necessitating dependence on external validation layers to achieve practical finality.  It is far from an unassailable feature.  Such an approach represents a structural limitation of asynchronous mining, where chain selection favors propagation speed over deterministic security, compromising network autonomy, stability, and reliability.


The Monero blockchain can become a self-regulating entity, overcoming these challenges.  This Proof-of-Time (PoT) proposal delivers a strategic response, addresses this constriction directly within the PoW framework by integrating hash-derived deadlines and a 30-second grace period atop the RandomX algorithm, enabling instant finality through network-wide selection of the lowest virtual-time solution, thereby eliminating re-org risks. PoT supplies a structural opportunity in asynchronous mining, where chain selection prioritizes speed of propagation alongside deterministic security, augmenting network autonomy without superseding Monero's Proof-of-Work or its core egalitarian mining ethos.


This proposal serves as a blueprint for implementation.  It documents technical and incentive specifications that collectively provide a comprehensive, actionable framework for developers.  We explore how PoT integrates with existing architecture, assess its security against network threats, highlight its potential to bolster stability and reliability, and position it as an evolution of the PoW consensus model, reinforcing the longest chain rule with security intrinsic to the PoW protocol.


# 2.  Proof-of-Time Protocol: Conceptual Framework

PoT integrates a timechain model into the PoW blockchain, wherein time is an inherent feature of the PoW mining process itself, governed by network time consensus, rather than universal clocks, blended with PoW consensus.  Nodes auto-adjust their time offsets based on peer reports, and miners compete to submit solutions with the lowest deadlines within a defined timeframe.

## 2.1 Timechain Concept

Endogenous time is calculated based on the local system clock, adjusted to blockchain genesis time, and a dynamic offset derived from peer interactions.

No centralized time source or OS clock synchronization is required.  Nodes achieve consensus through peer reports from their connected subset (e.g., 10-20 peers in a 10,000-node mesh), forming transient segments that converge asynchronously via P2P propagation.  In such large-scale P2P networks, all views are inherently partial by design.  Each node samples only its direct connections, with global alignment emerging via gossip over 3-5 hops.  Each node computes its time using this formula:

`chain_time = floor((system_time - MONERO_EPOCH + 500 + ms_adjust) / 1000)`

**Where:**

- system_time is the current time in milliseconds since the Unix epoch (January 1, 1970, 00:00:00 UTC),
- MONERO_EPOCH is April 18, 2014, 19:00:00 UTC (genesis time),
- 500 ms provides a rounding offset to align seconds (biasing toward the nearest whole second for precision in integer division)
- The variable "ms_adjust" represents a millisecond offset that is updated based on the binned mode approximation of the median time reported by connected peers (recommended for partial P2P views), or the direct median for full-sample scenarios.  This mechanism facilitates decentralized synchronization.  Typically, the offset can range from -86,400,000 milliseconds (representing a day) to much larger values, such as ±31,536,000,000 milliseconds (representing a year).  This range is managed via a 64-bit long to ensure robustness against significant clock drifts.  Updates are additive, preserving prior adjustments via ms_adjust += delta.  It prevents oscillation or over-correction in noisy networks, allowing incremental corrections over multiple recalibrations without resets to zero.

Nodes sustain a chain time offset extrapolated from at least five peer reports (prioritizing well-connected, non-rebroadcast peers sorted by clock diff reliability).  The offset recalibrates when a significant majority of peers (e.g., 70%) indicate deviation (e.g., improbably high >10 seconds; categorized by diff thresholds: "potentially problematic" if >1999 ms, "borderline" if ≥500 ms, "acceptable" if <500 ms), securing time alignment and preventing network fragmentation, with ms_adjust computed via the recommended binned mode (detailed below) or the direct median formula:

`ms_adjust = (median_peer_chain_time * 1000) - (system_time - MONERO_EPOCH + 500)`

Binned Mode is best for partial views.  Collect ms-level clock diffs from problematic peers - absolute value of diff (|diff| ≥500 ms), round each to the nearest 500 ms bin, increment frequencies in the bin and its neighbors (±500 ms, ±1,000 ms for smoothing), then set ms_adjust += -mode_bin (mode = most frequent bin).  This cluster offsets robustly in limited samples (e.g., 10-20 peers), approximating the network median without complete chain_time data and handling noise from gossip delays.

Thereby, the individual "chain_time" matches the network median even for grossly erroneous local clocks.  The binned mode offers a robust approximation in the standard partial P2P scenario, such as using message differences from 10 to 20 peers within a 10,000-node network.  Over iterations, it converges to the direct median, which provides precise alignment with complete second-level samples.  Action thresholds require a minimum of five problematic instances out of the total peer group, along with a minimum threshold of 70% to initiate any adjustments.  Assessing at least five samples against the threshold strikes a balance between early detection and evidence strength, and effectively filters out noise while enabling a robust synchronization process.

If 70% or more of the peers demonstrate a "good enough" alignment, no further action is required.  Otherwise, the system will recommend self-adjustment through DataGrouping binned mode analysis or the direct median formula above, provided that the necessary conditions are satisfied.

The recalibration procedure accounts for propagation delays (an extreme example, 15 seconds - **see 2.2, 2.3, 4.1**, the intents, due to their negligible size ~150 bytes, propagate within a small delta (e.g., <5 seconds)), and the 30-second grace period, maintaining consensus within a practical range.  The system leverages peer connectivity and produces a perfect alignment without the need for operating system intervention  (e.g., in a simulation with five peers reporting chain_times [329467195, 329467198, 329467200, 329467203, 329467208] s, the direct median is 329467200 seconds; a node with +4s drift adjusts ms_adjust to -4500 ms, yielding chain_time = 329467200s - aligning precisely without OS intervention.   Using binned mode on corresponding diffs [-5000, -2000, 0, +3000, +8000] ms, problematic bins (-5000, -2000, +3000, +8000) smooth to cluster around 0 ms, yielding approximate ms_adjust ≈0 ms and refining iteratively.  If ≥70% peers show "good enough" alignment, no action; otherwise, recommend self-adjustment via binned mode or direct median analysis if conditions met.

|Peer|Input Drift (ms)|Pre-Adjustment chain_time (s)|Median Consensus chain_time (s)|ms_adjust (ms)|Post-Adjustment chain_time (s)|
|--- |--- |--- |--- |--- |--- |
|P1|-86,400,000 (-1 day)|329,380,800|329,467,200|86,400,000|329,467,200|
|P2|-3,600,000 (-1 hour)|329,463,600|329,467,200|3,600,000|329,467,200|
|P3|-5,000|329,467,195|329,467,200|5,000|329,467,200|
|P4|-2,000|329,467,198|329,467,200|2,000|329,467,200|
|P5|0|329,467,200|329,467,200|0|329,467,200|
|P6|3,000|329,467,203|329,467,200|-3,000|329,467,200|
|P7|8,000|329,467,208|329,467,200|-8,000|329,467,200|
|P8|+3,600,000 (+1 hour)|329,470,800|329,467,200|-3,600,000|329,467,200|
|P9|+86,400,000 (+1 day)|329,553,600|329,467,200|-86,400,000|329,467,200|
|P10|+31,557,600,000 (+1 year)|361,024,800|329,467,200|-31,557,600,000|329,467,200|


This design delivers time-consensus that is asynchronous, lightweight, resilient, and fully decentralized.  Nodes "vote" via medians, not elections.

### 2.1.1 Timechain Alignment Assessment

During the initial 1-3 block intervals (roughly 2-6 minutes) before complete median stabilization through the whole Monero network, local segments might experience transient time variances of a theoretical extreme example ~10-15 seconds due to asynchronous P2P propagation and partial peer views, but this has a negligible impact thanks to the protocol's built-in buffers and deterministic design.  Miners with grossly erroneous local clocks cannot submit valid intents until their chain time aligns.  No blocks are invalidated, re-orgs are impossible, and mining/intent submission remains fair and continuous.

#### What Happens in the Transient Phase (1-3 Blocks):

#### Local Segment Formation and Variance:

Nodes start with their initial chain_time (based on local ms_adjust), forming "segments" of 10-20 peers.  In a 10k-node mesh, these partial segments enable scalable gossip, with variances arising from hop delays but resolving rapidly.  Early medians may differ slightly (e.g., Segment A at 329,467,200 seconds, Segment B at 329,467,205 seconds) because reports haven't fully gossiped across the ~3-5 hop diameter of the network.

#### Buffered Operations During Variance:

Miners submit their intent deadlines based on local "chain_time." The 30-second grace period, initiated upon the first valid intent, accommodates even improbably high worst-case scenario propagation delays of ~10-15 seconds and a segment variance of ~10-15 seconds.  Late intents from desynced segments are still accepted if within the window relative to the last block's embedded timestamp (which carries the producer's median-aligned time).  As a result, there are no missed blocks - all competitive solutions vie fairly.

The winning block's timestamp is set by the miner's adjusted chain time, serving as a reliable report from peers.  Nodes use this data to refine their consensus through median recalibrations.  Subsequent blocks propagate this aligned timestamp, accelerating network-wide convergence (e.g., after Block N, ~50% of the network incorporates the adjustment; by N+2, ~90%).

Nonce iteration and difficulty targets remain unaffected - variances don't alter hash validity or rewards, as deadlines normalize to the local view but rank network-wide by absolute value.

#### Impact on the Large Network

In a 10k-node net, <1% of intents might arrive 5-10s "late" in transient segments, but the grace period rejects only those >30s off the triggering intent, preventing exploits.  No chain forks occur because PoT's instant finality deterministically selects the lowest deadline per block, while the variances only slightly shuffle the submission order without affecting the outcomes.

Self-healing convergence occurs rapidly.  Gossip-based P2P models, as simulated in ns-3 for blockchain networks, demonstrate 80-90% alignment within one block (approximately 2 minutes) and wide alignment (with less than 2 seconds of global variance) by three blocks, as the medians average out via overlapping segments.  The recommended binned mode further enhances this in partial samples by clustering problematic ms diffs into 500 ms bins with neighbor smoothing, approximating the direct median and accelerating convergence in noisy conditions (e.g., mode of binned diffs yields ~0 ms adjust in balanced transients, even with 10-20 peer views).  In a worst-case scenario, a partitioned 20% of the net will self-adjust upon reconnection, buffered by a maximum block time of 2.5 minutes to prevent stalls.

1.  From **"Improvements of Blockchain's Block Broadcasting: An Incentive-Based Approach"** (ePrint 2018/1152, Authors: Qingzhao Zhang et al. - https://eprint.iacr.org/2018/1152.pdf). This paper uses ns-3 simulations to model P2P block propagation in a 1000-node network, showing fast convergence via block sharding. A technique that divides data into small pieces for parallel relay across local segments, analogous to PoT's lightweight intent gossip (~150 bytes) propagating deadlines and hashes through overlapping peer subsets for rapid time consensus.

- Page 1 (Section I, Introduction): "In our simulation in Section VII-A, block sharding shortens the synchronization latency by about 90%." - demonstrates rapid latency reduction for network-wide alignment, implying 80-90% faster convergence in early blocks - mirroring the 80-90% alignment within one block in PoT's transient phase as intents gossip across 3-5 hops in partial views.
- Page 8 (Section VII-A, Simulation Results): "Compared with the baseline, block sharding can speed up the synchronization 30 times and shorten the time cost by over 90%." - quantifies convergence speedup, with 90%+ efficiency gains after initial propagation, supporting <2s global variance by block 3 in segmented networks via redundant paths that self-heal partitions, much like PoT's additive adjustments over gossip iterations.

2.  From **"Computer Network Simulation with ns-3: A Systematic Literature Review"** (Electronics 2020, 9(2), 272; Authors: Campanile et al. - [https://www.mdpi.com/2079-9292/9/2/272](https://www.mdpi.com/2079-9292/9/2/272)) This review surveys 128 ns-3 papers on P2P/blockchain simulations, highlighting convergence in gossip-based protocols (e.g., epidemic routing for alignment).

- Page 18 (Reference [6] at [https://dl.acm.org/doi/pdf/10.1145/3199902.3199907](https://dl.acm.org/doi/pdf/10.1145/3199902.3199907)): "Implementation of epidemic routing with IP convergence layer in ns-3 [6]..." The simulations in the cited work [6,128] demonstrate fast convergence, with protocols reaching ~90% message delivery within 3-5 hops and latency under 2 seconds in 1000-node P2P setups (scaled from smaller dynamic network tests) - "Fast convergence" in epidemic (gossip) models aligns with PoT's P2P propagation, where 80-90% node alignment occurs within 1-2 intervals, as in ns-3 tests for overlapping segments.
- Page 25 (Reference [128] at [https://resilinets.org/papers/Alenazi-Cheng-Zhang-Sterbenz-Epidemic-2015.pdf](https://resilinets.org/papers/Alenazi-Cheng-Zhang-Sterbenz-Epidemic-2015.pdf)): "Epidemic routing protocol implementation in ns-3 [128]"... Simulations [in Alenazi et al.] achieve 100% message delivery across 1-8 hops, with latencies dropping ~80% in 10-50 node dynamic P2P setups, supporting the 80-90% alignment by first block and <2 s variance by block 3, via hop-based gossip in partitioned nets, directly analogous to PoT's median averaging over 3-5 hops.

Like Bitcoin's orphan rate (<0.1% from propagation delays), Monero's historical re-orgs are rare (~1-2 blocks deep, <1% frequency), and PoT eliminates them.  The transient time wobble adds zero extra risk.

## 2.2 RandomX Hash-Derived Deadlines

We propose a nominal adaptation to the Monero mining system inspired by the PoST nonce-derived deadlines concept.  Deadlines can be derived from PoW RandomX and computed in real-time, as seconds.  A deadline represents an estimated time elapsed from the last block timestamp, where lower values indicate higher-quality solutions relative to the current difficulty.

The valid RandomX hash result converts to a deadline by normalizing its quality relative to the difficulty target and scaling to a maximum range:

`deadline = floor((RandomX_hash_as_256bit_int × 180) / target)`

The target is the current network difficulty target (the maximum acceptable 256-bit hash value).

To prevent turbo blocks and excessive delays, we clamp the deadline:

`deadline = min(180, max(90, floor((RandomX_hash_as_256bit_int × 180) / target)))`

The formula normalizes hash quality to produce a pseudo-time value, simulating a probabilistic "mining race" without real clocks, creating a natural ranking system for contending solutions.  Valid hashes are uniformly spread within the range [0, target], resulting in deadlines that are too uniformly spread between [0, 180] seconds, regardless of the current difficulty.

If the difficulty doubles, it means the target halves, and the expected time to find a valid solution also doubles.  However, the relative quality of the solutions found and the distribution of deadlines remain consistent.  This consistency helps maintain fairness.  Block times, therefore, stay on target at around 2 minutes, with the winning deadline typically at 90 seconds.

Lower deadlines reflect smaller RandomX hash outputs relative to the target, incentivizing rapid nonce iteration without altering core hash computations.  The 90-second floor mandates that even exceptionally lucky hashes (near-perfect quality) map to no lower than the network target block time, preventing turbo blocks by enforcing a minimum deadline threshold while keeping such solutions competitively superior (as they tie for the lowest possible value).

The deadline is valid if the underlying hash meets the network difficulty.  If a deadline falls below a configurable target (global or miner-specific), the miner submits their solution, deadline, and public key via RPC.

Public key-bound hashes and deadlines secure exclusive submission rights for the miner.  Signing the submission with a private key or a seed stored securely in an encrypted local node config warrants its security.  Any alteration of the solution triggers a mismatch with the public key or height, resulting in a protocol-level rejection that preserves solution integrity.

The network verifies the RandomX hash output against the difficulty target, recomputing the deadline to detect tampering.

Nodes reconfirm the RandomX hash and deadline, computing compliance against the difficulty target and miner identity.  Peers reject duplicate submissions from the same public key, enforcing the one-solution rule, with valid intents held in a temporary pool until the grace period ends.

In cases of identical deadlines, the block with the lowest block hash breaks the tie, providing a deterministic and equitable resolution.

The difficulty adjustments control the expected lowest achievable deadline, targeting 2-minute block times, which enhances fairness by ranking solutions temporally without altering core hash computations.

## 2.3 Grace Period and Instant Finality

A 30-second grace period triggers with the submission of the first valid solution intent (hash, deadline, public key), which miners may broadcast up to 30 seconds before their deadline elapses from the last block timestamp.

This window accommodates network propagation delays, allowing all miners a fair chance to submit.  Nodes retain these intents until the period concludes, selecting the solution with the lowest deadline, while rejecting late submissions to force submission and transparency.

Nodes automatically discard any worse (higher-deadline) solutions received, as they cannot compete with pending better ones.  The timechain, with offsets adjusted based on the median time reported by a significant majority of peers (e.g., 70%), secures alignment with the honest chain, sustaining fairness and robustness, permitting for network latency and segmentation.

All peers evaluate intents at the end of the 30-second window.  It does not matter when the grace window actually starts on all the nodes.  It does not have to last 30 seconds for all and be simultaneous across the whole network.  This flexibility arises because the grace period is triggered individually by each node based on the last block timestamp and the deadline of the first received solution intent.

The solution intents propagate within a small delta (e.g., <5 seconds).  Nodes calculate the remaining grace time relative to their local chain time offset, adjusted by peer reports, allowing peers to consider late-arriving intents if received before the 30-second window expires network-wide.

For instance, if a node receives a 90-second deadline submitted 60 seconds after the last block timestamp, it validates and broadcasts the intent, triggering the 30-second grace period immediately for the network at the first valid submission step.  Even if a node receives the first solution delayed, the system checks the submission timestamp as soon as it arrives, calculating remaining grace relative to its offset clock.

To further bulwark equitable network play and sufficient time for intent propagation, submissions must arrive with at least 30 seconds remaining until the deadline elapses (i.e., submission_time ≤ last_block_timestamp + deadline - 30); intents arriving later are invalid and discarded, averting miners from delaying broadcasts to exploit timing edges (e.g., a 90-second deadline submitted at the 80-second mark, leaving only 10 seconds, would be rejected).

Miners stop mining upon receiving a grace trigger, broadcast of the first solution, as continued nonce iteration yields worse deadlines due to elapsed time.  In theory, a miner could persist with intensive computation and submit a better solution by the end of the grace period; however, this is detectable via submission patterns and penalized by network consensus (e.g., flagging greedy attempts as anomalous, leading to peer disconnection through cool-off periods or black-listing).

A dishonest miner who delays submission too close to the end of the grace period forks to an invalid single-node chain, losing all peers.  No one can override victory or cause disagreements at the network-wide level.  The difficulty targets a best-block time of 2 minutes, without cumulative difficulty.

This process, governed by the decentralized timechain, achieves instant finality, rewarding the miner with the lowest deadline and eliminating selfish mining and re-org vulnerabilities.

## 2.4 Maximum Block Time


To prevent chain death and guarantee continuity, PoT sets a maximum block time of 2.5 minutes, aiming for a 2-minute target, even under extreme conditions.  Mining starts immediately after the prior block is finalized and continues uninterrupted on the current block template until the grace period is triggered.

Miners broadcast valid solution intents (hashes meeting the adjusted difficulty threshold, where the effective target = (max_deadline_threshold / 180) × base_target) as they find them.  The grace period begins only when the first valid intent is received, with a deadline that is less than or equal to the time elapsed since the last block timestamp.

The maximum acceptable deadline threshold scales linearly with elapsed time to accommodate low hashrate conditions:

`max_deadline_threshold = min(270, t_elapsed + 45)`

Where t_elapsed is the chain_time since the last block timestamp.  This adjustment is computed deterministically by all nodes using the decentralized time consensus.

**Examples:**

- At t_elapsed = 45s: threshold = 135s (effective target = (3/4) × base_target; early acceptance only for above-average solutions)
- At t_elapsed = 90s (1.5-min target): threshold = 180s (effective target = base_target; normal operation)
- At t_elapsed = 150s (2.5-min max): threshold = 195s (effective target = (11/10) × base_target; accepts inferior solutions)
- Hard cap at 270s (4.5 minutes total, emergency liveness)

For instance, at 2.5 minutes (t_elapsed = 150 seconds), the threshold rises to 195 seconds, so a miner finding a hash that would convert to a 170-second deadline (rejected under the 180s cap) produce a 170-second deadline under the base target (i.e., base_target < hash ≤ effective_target) would now be accepted as valid, triggering the grace period and allowing competition among other arriving intents up to that threshold.  Once a valid block is produced (via the lowest deadline intent within the threshold, with grace if triggered), the threshold resets to operate within the standard 90-180 seconds range for the next block.

This mechanism preserves existing difficulty adjustment for base hash requirements but adds a deadline acceptance window that expands during delays.

It averts stagnation without rollbacks or reorganizations by accepting progressively inferior yet still competitive solutions.  Continuous operation of the honest chain is guaranteed even during extended periods of low activity.  For example, hashrate drops of over 90%, while targeting winning deadlines of 90 seconds under normal 2-minute block time conditions.

# 3.  Deadline-based Solo and Share Mining

We propose to reinforce the egalitarian mining ethos with a mixed mining model.  The goal is to abandon the need for and use of centralized mining pools by dividing miners into two groups: solo miners and shared miners.

The coinbase will be revised to support multi-output.

### 3.0.1 Prior considerations - P2P network protections

To strengthen defenses against sybil attacks and spam, including potential key rotation by high-hashrate miners, the P2P layer enforces a strict limit of one intent per peer submitted strictly via localhost connection, applies ban scores to nodes submitting excessive intents, and curates peer connections to prevent flooding, making rotation and multi-intent blasting resource-intensive and unprofitable without meaningful gains in odds.

To diminish Sybil risks from attackers running multiple nodes attempting key rotation, a node reputation system based on connection duration and historical behavior solves the concern.  We can use the rank to multiply the deadlines for new or low-reputation nodes.

## 3.1 Solo mining

Solo mining remains a core option, where individual miners compete to find valid RandomX hashes and derive low deadlines, submitting intents (hash, public key, deadline) via mining before the grace period triggers. Nodes collect and verify these intents within the 30-second grace period to select the lowest-deadline solution and claim block rewards. 

Every 5th block, the solo miner with the lowest deadline wins the full block reward.

For all other blocks, the solo miner with the lowest deadline wins half the reward.

### 3.1.1 Solo Mining Handicap

We propose a limit of 5 block wins or fewer for any solo miner within a rolling 10-block era.  Once a miner achieves the set wins within the rolling era, they are given a handicap in the form of a deadline multiplier penalty, which applies for the duration of the block era.  For example, all their submitted deadlines are automatically increased by 50%.  This adjustment encourages players to engage in solo mining.

While it does not prevent a miner from winning more blocks within the rolling window, it significantly increases the difficulty due to the handicap.  The handicap can be adjusted further based on any subsequent wins.

### 3.1.2 Solo Mining Hashrate Sampling

Applying deadline-derived hashrate sampling to solo mining, as detailed in section 3.2.3, can improve fairness by creating more accurate handicaps.  By averaging these hashrate estimates over a period, we can adjust penalties for dominant players, promoting long-term fairness and minimizing luck-based disparities without complicating the lowest-deadline win mechanic.

Additionally, solo miner hashrate samples can enhance peer reliability scoring in the recovery mechanisms outlined in section 4.2.

## 3.2 Share Mining

We offer three deadline-based share mining models for consideration.  Each has a varying degree of simplicity, fairness, and security.  All three options eliminate the need for second-layer pools at a low cost.

All three models prioritize low-hashrate participants, deter high-hashrate dominance through single-intent submission, and an inverted handicap model empowers smaller operations and mitigates spam risks.

In all three models, the remaining half of the non-solo mining rounds split rewards between 21 shared miners.

Share mining deadlines are not capped or clamped.

We recommend implementing the model discussed in section 3.2.3 below.  Although it may not be the simplest option, it is provably fair and allows for a granular level of customization.

### 3.2.1 Native Top-21 Solutions Model


Shared miners submit exactly one intent per block round, choosing their best solution before the next block finalizes.  The network ranks all submitted intents by deadline, where lower values indicate stronger solutions.

The open deadline range accepts solutions from 0 seconds upward without caps, allowing even slow solutions from modest hardware to compete as long as they rank in the top 21.

Nodes maintain a simple map of all single intents received, comparing new submissions against the current top-21 threshold.  If a new deadline beats the 21st-place solution, it displaces the worst existing entry.

To level the playing field for smaller miners, the handicap targets those who repeatedly win, identified by their public keys.  Nodes keep track of win counts over a rolling 10-block era.

If a miner achieves three or more wins within this window, cumulative penalties accrue for their subsequent rounds.  The first time a miner reaches this threshold, their unclamped deadline multiplies by 3.  In the case of a second offense, the penalty multiplier increases to 5, and so on.

If the handicapped deadline is greater than the current top-21 after intent submission, the solution is void.  Penalties reset completely after 10 rolling rounds without any additional shared wins.

The model is the most lightweight option, relies entirely on the PoT deadline system for fairness, and promotes quality over quantity to determine rewards.

### 3.2.2 Unweighted Deadline Lottery

In this model, the 21 miners win through an unweighted lottery among all valid entries.

Shared miners submit exactly one intent per block round, with the network verifying that the hash meets the base difficulty and the deadline derivation is correct.

The lottery treats all valid entries equally, providing each participant with the same chance of winning, regardless of the quality of their submission.   It utilizes a Verifiable Random Function (VRF) seeded by the hash of the previous block to select random 21 winners from the pool.

The open deadline range accepts solutions from 0 seconds upward without caps or lower thresholds, allowing even higher-derived deadlines from modest hardware to compete as long as they qualify as valid intents.

To level the playing field for smaller miners, the handicap targets those who repeatedly win, identified by their public keys.  Nodes keep track of win counts over a rolling 10-block era.

If a miner achieves three wins within this window, all their subsequent solutions become void until the block era resets.

The effect is to reduce the competitiveness of high-hashrate miners in repeated wins, encouraging them to opt for solo mining where their advantages are less diluted.  Low-hashrate miners gain relative ground without the quality thresholds that could exclude them.

The model relies entirely on the PoT deadline system for fair, verifiable competition.  It encourages higher peer participation based on quantity rather than a quality model that determines rewards, empowering low-end hardware without centralized pools.

### 3.2.3 Weighted Deadline Lottery

This model draws inspiration from PRS workshares, replacing them with verifiable PoT deadlines for direct hashrate sampling, where rewards reflect genuine computational effort without the workshares overhead.

Shared miners submit exactly one intent per block round.  The network verifies that the hash meets the base difficulty and the deadline calculation is correct, then derives an estimated hashrate sample using the formula:

estimated_hashrate = difficulty_target / (deadline × elapsed_time)

This raw estimated_hashrate serves as a proxy for the miner's effective computational contribution in that round: a lower deadline (indicating higher hash quality and thus "earlier" virtual solve time) implies a stronger sample, scaled by the actual elapsed time since the last block to account for varying mining durations.  Individual values are noisy due to hashing luck, but they converge reliably over multiple samples.

The result provides a proxy for the relative contribution.  A lower deadline indicates better hash quality, suggesting a higher effective hashrate.  It is true even though individual samples can be noisy due to luck, and low-hashrate miners sometimes produce strong derived deadlines.  Over a rolling 20-block era, nodes average these raw estimated_hashrate values to compute a close estimate per public key (converging to real hashrate within acceptable variance, estimated at 5-20%, depending on submission frequency and era luck).  The greater the block era, the higher the degree of accuracy.

To prevent key rotation and reduce the exploitation of noisy single samples, a public key that has fewer than five samples in the rolling era will have its average estimated hashrate adjusted downward by multiplying the hashrate by (number of samples / 5).  Such a method guarantees that new or rarely used keys receive proportionally fewer tickets, thereby reducing the incentive for sybil-based dominance.

For the lottery, the estimated relative hashrate (normalized against the network average) scales the ticket weight: 

`ticket_weight = max(1, estimated_relative_hashrate × 100)`

The x100 is just a scaling knob to make the lottery more "proportional".  The estimated relative hashrate is the average hashrate of a miner divided by the average hashrate of the network.  It is determined by summing all participants' averaged hashrates and then dividing by the number of participants, rewarding higher average performance (e.g., a sample indicating 2× network share yields about 200 tickets) while providing a baseline for modest contributors (e.g., 0.1× yields 10 tickets).

The total ticket pool across all shared miners sets proportional odds, and a VRF, seeded by the previous block hash, randomly selects 21 winners from the pool, guaranteeing fairness and resistance to manipulation.  We can prevent share mining hashrate inflation by limiting the total number of tickets per public key to 200.

An inverted handicap addresses serial winners more effectively.  If a miner achieves three wins within a rolling 20-block period, all subsequent deadlines are limited to one ticket until the first win lapses over 20 blocks.

This model encourages high-hashrate miners to shift toward solo mining, where their strengths can shine without dilution, while keeping shared rounds accessible to smaller participants, and it relies entirely on the PoT deadline system for fairness and allows granular customizations for ticket scaling, era span, or high-end hashrate barring, while promoting decentralization through effort-based proportionality.

## 3.3 Assessment of Incentive


The three share mining models offer varied incentive structures to balance fairness, participation, and proportionality, all while integrating with the solo mining rewards (0.6 XMR block reward every 5th block, half otherwise) to promote peer decentralization.	

The Native Top-21 Solutions Model incentivizes quality over quantity by directly rewarding the top 21 deadlines, favoring consistent high-hashrate miners with strong samples but potentially marginalizing low-hashrate participants unless they get lucky.  The handicap encourages turnover, boosting small-miner opportunities through resets after 10 blocks. 

The Unweighted Deadline Lottery promotes inclusivity by treating all valid submissions equally, offering the same chances regardless of the quality of their deadlines.  This approach democratizes rewards for users with lower-end hardware, attracting more participants.  However, it may diminish the importance of effort-based proportionality and could discourage intensive computation, which, however, is not essential within the scope of share mining.

Compared to the existing Monero model dominated by centralized pools (capturing ~90% of hashrate), these models are fairer for smaller miners overall, as solo cycles and deadline-based lotteries/top-selections offer significant payouts without 1–2% fees or centralization risks, with the weighted variant providing the most stable proportionality.

They all excel in decentralization by enforcing single intents, handicaps, and L1 participation to distribute power, outperforming pool concentration. 

Although models introduce lottery variance in shared rounds, potentially reducing income stability compared to pool shares, we can mitigate it by solo guarantees and era averaging.

While the unweighted model risks under-rewarding effort, the top-21 model favors elites slightly more.  The recommended Weighted Deadline Lottery strikes a proportional middle ground, using era-averaged hashrate estimates to scale tickets, rewarding sustained effort while capping at 200 to prevent dominance.  It best aligns incentives with computational contribution, motivating upgrades without excluding modest setups.

All discussed mining models promote a more equitable ecosystem than the current pool-dominated system.  They reward effort proportionally across hashrate levels while reducing systemic risks, such as 51% pool dominance.

## 3.4 Assessment of Security

Across the three share mining models, the PoT's core features collectively eliminate re-orgs, selfish mining, and withholding, while the maximum block time upholds liveness.

The Native Top-21 Solutions Model provides strong verifiability through direct deadline ranking and hash recomputation, with cumulative handicaps preventing serial dominance.  Its quality emphasis could increase Sybil attack risk if high-hashrate actors rotate keys for multiple top entries; nonetheless, P2P curbs make this approach costly, requiring 100 to 400 intents and 100 to 400 Sybil nodes, which makes it unprofitable.

The Unweighted Deadline Lottery fights spam resistance by treating all participants equally and preventing more than three rewards within a rolling era.  While its focus on quantity may lead to flooding, this risk is again mitigated by single-intent rules and VRF based on the previous block hash, making predictions difficult.

The Weighted Deadline Lottery strikes the most layered defense, with era-averaged hashrate sampling converging to 5–20% accuracy to normalize luck, ticket caps, and one-ticket handicaps post-three wins; the VRF lottery adds cryptographic fairness, while its noise tolerance prevents manipulation via randomly chosen samples.

In all models, high-hashrate key rotation remains theoretically possible but impractical due to P2P enforcement, accruing negative costs without odds gains, and handicaps dilute edges on winning keys.

The decentralized verification, which involves deadline recomputation, helps prevent forgery while grace periods are in place to ensure fair propagation.

Compared to the current Monero mining model, these changes make 51% dominance significantly more expensive, as deterministic finality secures reward locking on-chain without reliance on probabilistic confirmations or external dependencies.  It creates a secure and fair framework that is resilient to centralization and exploitation.

# 4.  Implementation Considerations

## 4.1 Time Collusion and Impact on Grace Period


If a majority of peers collude to report a fake time (e.g., an hour ahead), this could shift the ms_adjust value.  It is not a relevant threat, as colluders would only harm themselves within their immediate peer bubble.  Such skews misalign submissions, causing late or invalid intents that peers detect as greedy or hacked attempts (e.g., submitting quality solutions late in the grace period).  In such an event, the bubble disconnects colluders, isolating them without affecting the rest of the network.

The core design's 30-second grace period, combined with the strict submission rules in sections 2.2 and 2.3 (e.g., rejecting late arrivals, grace triggers individually per node based on received intents and decentralized time offsets via median peer reports), provides ample buffer for typical network asynchrony.

Intents propagation, due to their negligible size of around 150 bytes, should occur globally in under 5 to 10 seconds, even on 90s-era and 56k modem bandwidth.

Withholding blocks is inherently futile because miners must broadcast intents early to trigger and participate in the grace period, with delays leading to rejection rather than overrides, shifting the paradigm from probabilistic longest-chain re-orgs to deterministic intent-based selection without history rewrites. 

Clock adjustments weigh in a fuzzy, network-distributed manner:

Each peer's ms_adjust is the median made of offsets of connected peers, with outliers (e.g., reports deviating significantly from the majority) ignored to prevent skewing.  If colluders form a tight-knit peer circle, they only alter their own isolated bubble, effectively forking themselves into irrelevance.  If they infiltrate broader peer groups, they become the minority outliers and are discounted, as adjustments require consensus from a significant majority (e.g., 70%) of peers.

Miners gain nothing from skewing clocks, as grace triggers on first valid solutions and finality locks rewards regardless.  Monero's highly distributed nature ensures honest segments dominate, rendering collusion impractical and self-defeating.  No gain in rewards or attacks, only fragmentation and self-rejection.

The protocol can implement a hard cutoff to mitigate extreme cases.  Peers can disregard an offset from a peer if it deviates by more than a predetermined threshold.

Empirical tests show that honest clock drifts rarely exceed a few seconds.  Even if a miner's node starts with a time offset of 35 seconds, it will adjust to align with the honest majority through peer reports.  This process ensures that submissions align correctly without disrupting the network.

## 4.2 Forked Peer Reconciliation and Recovery Mechanism

In rare instances of network partitions or temporary node isolation, we incorporate a controlled recovery function to enable affected nodes to detect divergence, validate the honest chain, and seamlessly rejoin it.

This mechanism upholds the PoT guarantee of no block re-orgs in the canonical chain under normal connected conditions.  By treating finalized blocks instantly as immutable once integrated into the one chain, it limits recovery to shallow minority forks, thwarting abuse while permitting swift, non-disruptive reconnection without any risk of malicious history rewrites.

A core security pillar is robust eclipse attack resistance, achieved through a dynamic, multi-level quorum system.  Nodes seek agreement not just from immediate level of connected peers, but via recursive queries across 2-3 hops to sample an effective ~200 peers network-wide (scaled proportionally for smaller chains, e.g., 20 for testnets), requiring a minimum 70% consensus on the alternative tip verified at a depth of three or more blocks to confirm chain integrity before any recovery action.

Divergence detection activates as nodes establish or re-establish connections with peers, leveraging Monero's established connectivity model.  Nodes periodically query peers for the current chain tip (block hash and height) via a lightweight extension to existing P2P messaging.

If a peer reports a differing tip at the same or greater height, the node requests a concise chain summary, comprising block headers with timestamps, deadlines, and hashes, from the suspected forked node point onward.  The node then traces backward until identifying a matching block hash, establishing the last common ancestor.

If no ancestor emerges within a practical depth of 100 blocks, the peer's chain is treated as incompatible, resulting in the disconnection of the peer and an increment to its ban score to deter spam or adversarial chain feeds.  Deeper reconciliation in such cases requires manual intervention via "--allow-deep-recovery" config option.

We identify recovery targets for viable divergences by aggregating reports from a selected group of reliable peers.  By calculating agreement levels based on their reliability scores, we obtain weighted agreement scores.  These ensure a broad consensus and avert low-trust peers from disproportionately influencing decisions.  Thus, the highest-scoring block serves as the recovery anchor for majority alignment with minimal data exchange.

Should multiple anchors tie in score, an extremely theoretical scenario arising solely from perfectly synchronized block production in isolated partitions, a tiebreaker selects the one with the greatest implied forward progress, based on the maximum reported height among agreeing peers.  The peer-reported chain replaces the local peer chain only if its agreement score exceeds the local peer by a configurable margin of at least 10%, ensuring decisions resist minor hashing luck variances.

Recovery activation remains strictly conditional to maintain security - the peer-reported chain must fully validate under PoT rules, including hash compliance with difficulty, accurate deadline derivation, adherence to grace periods, and absence of duplicate intents. 

During this process, the node re-verifies the entire post-fork segment sequentially, as if mining it in real-time, to confirm the chain's integrity against potential manipulation from the partition.  Hash compliance ensures that each block's RandomX proof-of-work meets the era's difficulty target, adjusted for both forged and weakened hashes.  Accurate deadline calculations confirm that the temporal ranking remains unchanged, preserving the integrity of the block with the lowest deadline.  Adherence to grace periods confirms that intents are broadcast at least 30 seconds before the deadline, relative to timestamps and peer offsets.  This measure prevents the use of withheld solutions that could lead to selfish mining and forks.  The review for duplicate intents monitors key reuse, effectively invalidating any Sybil attack attempts that threaten competition.  If any compliance issues arise, the recovery process will be re-initiated, seeking agreement from further peers.  Only those with a demonstrably honest history will be considered acceptable.

Auto recovery depth is restricted to forks no deeper than 10 blocks (measured from the common ancestor identified in the initial 100-block search), consistent with Monero's existing practices for shallow re-org handling.  Deeper potential recoveries halt automation, logging a critical alert and requiring manual override via "--allow-deep-recovery" with explicit confirmation to mitigate contrived malicious chains.  A temporal safeguard protects PoT's instant finality by prohibiting auto recovery for fork points older than one hour, ensuring that blocks finalized in real-time through the grace period's deterministic selection remain immutable in the canonical chain, even if a minority fork later attempts reconnection.

Recovery execution utilizes Monero's database primitives to revert the local state to the common ancestor, removing the peer's blocks, transactions, and associated state changes.  The node then sequentially validates and appends the majority chain's blocks, recalibrating time offsets, deadlines, and rewards as needed, while reintegrating any compatible local pending transactions or intents.  Upon completion, it broadcasts the updated tip to peers and resumes PoT mining on the refreshed block template, discarding any unsubmitted intents from the prior divergent path.

A command-line interface will support manual recovery oversight for operators.

This function extends Monero's existing sync architecture with PoT-aligned scoring, preserving backward compatibility for length-based decisions during transitional phases.  Rigorous testnet evaluations, simulating partitions via delayed connections, will confirm recoveries complete in under one minute for shallow forks, reinforcing network convergence post-disruption while fully safeguarding against re-orgs and 51% threats.

## 4.3 Integration with Difficulty Adjustment Mechanisms

The PoT protocol closely interacts with Monero's difficulty adjustment algorithm, which aims for a 2-minute block time based on the direct median of recent block times.

To meet the target in the deadline-based system, we must algorithmically calibrate the base difficulty so that the expected lowest deadline across the network is about 90 seconds, based on a uniform distribution of deadlines between 0 and 180 seconds before clamping.

During implementation, the difficulty adjustment loop should use feedback from observed winning deadlines instead of relying solely on block timestamps.  An increased difficulty can raise the distribution if the average deadlines trend below 90 seconds, indicating over-achievement.

Conversely, if deadlines frequently exceed 150 seconds or trigger the maximum block time threshold, difficulty decreases to encourage more valid solutions.

This approach ensures long-term stability and prevents drift from the target block time.  Simulations using historical Monero hashrate data can fine-tune the adjustment parameters, avoiding oscillations.  Compatibility is high, as the core difficulty formula remains unchanged, with PoT adding a deadline-derived modifier only during extended delays (via the max_deadline_threshold scaling).

## 4.4 P2P Network Modifications and Anti-Spam Measures

Implementing PoT requires enhancements to Monero's P2P layer to handle solution intent broadcasts efficiently and securely.  While blocks already propagate via the existing "new block" messages, PoT introduces lightweight intents as precursors that broadcast before and during the grace period to collect competing solutions before the winning one assembles the block.

These intents are formatted as a new, compact message type (estimated ~150 bytes each, including the RandomX hash, deadline, public key, and signature), relayed similarly to transactions for rapid dissemination with minimal bandwidth overhead.

To prevent spam or sybil attacks, such as key rotation for multiple submissions, nodes must enforce strict rules: one intent per public key per block height, validated at receipt.  Excessive submissions from a single peer trigger ban scores, with temporary disconnections for violators.  Incoming intents are limited to one per connection every ten seconds during grace periods, and nodes only prioritize broadcasting those with deadlines better than the current known best.

These changes build on Monero's existing peer management, adding minimal complexity.  Backward compatibility during a transition period could allow legacy nodes to observe but not participate in PoT mining, ensuring a smooth hard fork.  Testing on the Monero testnet should verify propagation times remain under 5 seconds globally, aligning with the 30-second grace period.

## 4.5 Mining Software Compatibility

PoT is fully backward-compatible with existing RandomX mining software, requiring only minor updates to compute and submit deadlines from valid hashes.  Miners would integrate a simple post-hash processing step: convert the hash to a 256-bit integer, apply the deadline formula, and clamp as specified.  Submission occurs via RPC to the local node if the deadline meets a user-configurable threshold (e.g., below 150 seconds).

Miners benefit from the single-intent rule, which reduces the need for high-volume submissions and supports CPU-friendly configurations.  Open-source miners, such as XMRig, can be enhanced with a PoT module.  Workers refresh their block template every 30 seconds if no valid deadlines occur, and update the embedded timestamp to align with the latest chain_time (2.1) to prevent stale computations during ongoing nonce iteration.  It updates the embedded timestamp to synchronize with the latest block time on the blockchain, which helps prevent stale computations during ongoing nonce iterations.

Implementation should include safeguards against tampering, such as signing intents with the miner's private key for verification.

## 4.6 Privacy and Security Implications for Miner Identities

PoT attaches deadlines to public keys, and in theory, the repeated use of the same key could allow observers to link mining activity across different blocks.  The use of stealth addresses mitigates the risk through unlinkability of rewards in multi-output coinbases.

To further enhance privacy in this context, miners can leverage subaddress-derived keys for intent submissions.  These ephemeral keys, generated from a secure seed, prevent long-term linkage without exposing the primary wallet, aligning with Monero's hierarchical deterministic structure and rendering activity tracking infeasible even under extended observation.

Security-wise, the system resists forgery through hash recomputation and signature checks, with network rejection of altered intents.  We recommend key management in the node config.  For example, encryption of the configuration file, with the node prompting users for a password on startup to decrypt and access private seeds securely, and encrypt the config again once loaded into memory.

## 4.7 Fork Deployment and Transition Strategy

As a consensus-altering upgrade, PoT necessitates a hard fork, scheduled at a predetermined block height to allow ample preparation.

During transition, a hybrid mode could permit legacy PoW blocks alongside the PoT model, with nodes preferring PoT-finalized blocks after activation.

After the fork, monitoring tools should track triggers of grace periods, distributions of deadlines, and applications for handicaps to detect any anomalies and prompt necessary adjustments to ensure that the correct scaling conditions were applied.  This structured approach minimizes disruption, drawing on the history of successful upgrades such as RandomX integration.


## 4.8 Performance and Scalability Impacts

PoT introduces a lightweight overhead, which includes storing intents in a temporary pool (potentially reaching a few thousand per block during periods of high participation) and clearing after a grace period.  The computational costs for deadline verification are minimal, especially when compared to the costs associated with RandomX hashing.  Bandwidth usage remains low, with intents contributing approximately 1-2% to typical P2P traffic.

Scalability benefits include elimination of re-org processing, as instant finality averts network rollbacks, improving node sync times.  Benchmarks on varied hardware (e.g., Raspberry Pi for low-end nodes) should confirm no regressions in sync speed or resource usage, positioning PoT as a net positive for long-term network growth.

# 5.  Conclusion

PoT marries with PoW through native integration, and together foster a far more equitable ecosystem, eradicating centralization risks from pools and rendering traditional 51% attacks irrelevant by eliminating re-orgs and selfish mining.  Attackers with the majority of the hashrate can only mine forward at a probable loss under the handicap system, without the ability to rewrite history or censor, thus enhancing network resilience through deterministic finality and transparent intents.

Its simplicity supports low-bandwidth resilience, while Monero connectivity secures time consensus.  Security analysis demonstrates that tamper-resistant deadlines and rejected colluding segments render timing collusions ineffective, and pose only a negligible risk and no ability to affect the overall network.  Replacing cumulative difficulty with a maximum block time ensures liveness without rollbacks.

Overall, Monero has the opportunity to become the leader of the resurgence of PoW blockchains and prove once again that PoW is far superior to PoS through resilient, deterministic enhancements.

# Acknowledgments

We thank the Monero community in advance for their input and the developers for considering this proposal.

Primary credit goes to Mr. Scatman of the ANNE Network for devising and implementing the PoST protocol, which facilitated this transition to PoT. 

The PRS framework, developed by Dr. Karl Kreder of the QUAI Network, inspired the Weighted Deadline Lottery model and warrants recognition.

# Limitations

This study is provided free of charge, as is, without guarantees of any kind, expressed or implied.  Although the PoST is fully implemented, tested, and deployed on the ANNE mainnet, the authors of this proposal might lack comprehensive knowledge of the Monero protocol, and there are no research papers available on PoST.  In light of the Monero situation, we endeavored to transpose the PoST model and document the PoT model to the best of our ability.

There might be solvable imprecisions or nuances beyond the scope of this proposal.  Such challenges, through further research and revisions, can be resolved.  The proposal achieves its fundamental purpose by evidently demonstrating that deterministic security is perfectly solvable within the native scope of PoW.  It is delivered to encourage an in-depth exploration of technical feasibility and adaptability to Monero.

# Research Bounty

A substantial, compelling, and negotiable bounty awaits one or more Monero developers who will conduct in-depth research into the technical feasibility of implementing the Proof-of-Time model into Monero under the following conditions.

- Thorough research will demonstrate the technical feasibility and deliver necessary adaptations to this proposal.
- Monero developers will reach a consensus and agree on the PoT implementation.
- The Monero community will reach consensus.
- A CCS implementation proposal reaches the Funding Required step.
- A complete, partial, or adapted implementation of this proposal will qualify for the full bounty, as long as any form of PoS research and implementation is proven redundant and unequivocally rejected.

Once all conditions aggregate, the bounty will be due, paid as a lump sum that has been negotiated and agreed upon in advance.  For more info, please message me on Matrix.

Meanwhile, we offer free and ongoing consultation to any Monero developer who aims to solve any challenges that may arise during the research and implementation process.


# Discussion History
## tevador | 2025-10-02T04:39:07+00:00
I see several problems with this:

1. It introduces a new assumption that `chain_time` converges across the whole network. However, this might not be true in practice, especially becauses a sybil-attacked node can be fed nearly arbitrary time offsets.
2. The "forked peer reconciliation" mechanism is insufficient to prevent chain splits. A chain split can still occur if (1) an alternate chain forks off more than 100 blocks in the past (this won't happen on its own, but it can happen in a 51% attack scenario) or (2) neither of the alternate chains has a 70% peer majority.
3. 51% attacks are still possible. The attacker just needs to meet 2 conditions: (1) the fork point must not be more than 100 blocks in the past and (2) the attacker needs to own >70% of the network nodes (this is easy). The attack will succeed via the forked peer reconciliation mechanism.
4. Selfish mining is still possible due to the use of smallest-hash tie breaking (SHTB). Details are described in [this paper](https://ieeexplore.ieee.org/document/8835227).
5. The "solo mining handicap" does nothing. A miner can easily mine using several different public keys.

## r-a-d-a-n-n-e | 2025-10-02T08:35:51+00:00
Thanks for your response, Tevador. I have limited time, so I'll quickly and somewhat abruptly respond to your first 'chain_time' concern and come back later to address the rest. Understandable at a surface level, since you voice real vulnerabilities in P2P blockchain networks.

The concern is ultimately invalid for PoT. It conflates probabilistic vulnerabilities with PoT's deterministic security. The protocol does not rely on an unproven "assumption" of convergence. Any skews are ineffective, self-isolating, and neutralized at the protocol level (outlier rejection, quorum, isolation).

PoT's time consensus emerges from partial, gossip-based peer samples (10-20 direct connections in a 10k-node mesh), not a fragile global assumption. My blueprint explicitly addresses that convergence is not assumed but achieved asynchronously via P2P gossip in partial segments, with ns-3 simulations showing 80-90% alignment within one block (~2 minutes) and <2 seconds global variance by three blocks (Section 2.1.1). The binned mode clusters only 'problematic' diffs via smoothing, approximating the honest median without full data. PoT extends this with additive ms_adjust updates (preventing oscillation) and binned mode for noisy partial views, with negligible impact due to 30-second grace buffers.

The segments are overlapping and self-healing through median/binned aggregation. Monero already handles similar time convergence for block timestamps via Median Time Past (MTP), I believe, resisting skew by ignoring outliers and requiring majority honest peers.

Sybil attacks (fake identities skewing reports) fail because adjustments need a 70% deviation consensus. Sybils in a local bubble (<70%) are ignored as 'outliers'. It's self-defeating. A global skew isn't possible. The blueprint suggests reputation-based peer curation (Section 3.0.1), which solves these concerns.

Feeding arbitrary offsets requires monopolizing connections, but Monero's outbound diversity (8+ random peers) and ban scores make >70% control resource-intensive. See Bitcoin eclipse analysis: https://eprint.iacr.org/2015/263.pdf

"The distributed clock synchronization algorithm is employed to synchronize the logical clocks between nodes, ensuring that these logical clocks tend towards a unified global clock. ... As shown in Figure 13, in the blockchain network of 200 nodes, the maximum clock offset between nodes does not exceed 900ms. Such an offset is sufficient to ensure the blockchain network works correctly, since the average block generation time is 2s, which is much larger than 900 ms." https://arxiv.org/abs/2501.01146 ( (PoVF paper, Section 6.2 - gossip-based sync bounds offsets despite dynamics, analogous to PoT).

I will come back with a much more detailed response later :)

## MrScatman | 2025-10-02T09:34:39+00:00
Greetings tevador,

I'll speak from the perspective of ANNE, which uses a working PoST, which informed the PoT proposal.   

**1)  chain_time doesn't converge across the network.**   
It converges in local peer networks (eg, think of this like a peer subnet or a bubble).   There is an expected gradient over the network whole.   If I have 20 peers; me and my peers have an understanding of time.   I came to that understanding via comparing myself to my peers, not to the network.   I don't care about the network, I only care about my peers.  That IS my network, as far as I care.    I need not communicate with every node on the network, and in fact, do not want to.     Each of my peers are also apart of their own peer "subnet" (the peers they see and communicate with).   They may adjust a bit this way or a bit that way.. at any given time.   It is self adjusting, self correcting... like a 3-body problem but with time offsets.    This informs their local understanding of time (offset).   Sybil attack by altering clock of some cluster of attacking nodes at best alters the offsets of the local subnets it holds majority "time offset" weight in (if any).  A successful attacking result is the big group of hypothetical attacking nodes (altering their time clocks) create their own isolated world.    Like mining blocks for 10 days with no internet connection.  

In ANNE, nodes determine who they connect to, if they want/accept new peers, and a handful of other parameters that the node operator uses to decide what type of "rando  peer risk" they want to take on.    In ANNE, peers are a bit more than just an IP and a port.  (can explain at depth later)   If you join a bot net with your pc, then you're in a bot net, right?    If you join a hypothetical sybil attacking peer subnet/bubble where all the IPs in your peer list are running rogue code or up to nefarious deeds --  and in this hypothetical, a majority of the IPs you are peering with are purposefully altering their reported clock times --- then that's exactly what you will see!!    Your node would think it was the odd man out and adjust its internal offset of time.   I'd argue it did exactly what it should.   It's only mechanism of understanding time is its own clock, the timestamp of the last block, and its peers.   There is no centralized time.    It is fuzzy.    As such, whatever offset is used for any given node IS the best time offset for that node, considering the peers and protocol.    This scenario doesn't compromise the network.  This can be discussed more, if desired.

**2)  There are no rollbacks.**   Protocol does not have an auto mechanism to rollback and alter chain history (re-org) with a better chain of blocks.   Proof of Time removes this as a possibility.  (in ANNE, it is Proof of Space Time, where Space is referring to disk space used in hard drive mining)

There is no 51% attack.   It doesn't exist in this model.   A chain cannot be rolled back by seeing a longer chain with more work.    The only way ANY rollback occurs is via manual intervention by the node operator (via direct access or remote administration).   
   
Example:  A miner loses internet connection.   A miner node mines a block, thinks it is the best block, and then moves on to the next block.   There are safeguards/detection to try to prevent this case from happening (which only affects a single node) -- but when it does, a manual pop off of blocks is needed.   Protocol will NEVER identify this and do this automatically.  By design.   It is the small cost paid for miners that lose internet connectivity ---  in order to NOT have chain-ending chain-altering business-killing threat vectors. 

If one wants to mine they must mine the current block that is being mined.    There is no notifying the network that you have 10 better blocks (which you are only now letting the network know about) so the network must rug-pull and change history.  Undo TXs that hit exchanges.   Undo.. everything.   Yikes!   Unacceptable.  Unusable, really.    My node CANNOT be rollback because of "late information".    The idea of allowing such is utterly unacceptable to me, thus, I designed a solution that honored Proof of Work yet didn't require such things.   My node is anti-fragile and not open to such attacks.    I'd argue far greater than a sybil attack is literally the allowable design of rollbacks and re-orgs!    This is a flaw in the design.    So, I made something that fit my requirements.   I started with an existing solution/code, stripped it down to its bones, and then built a proper solution to these key flaws I saw on the blockchain side of the equation.    In ANNE, Block solutions expire.    In most other crypto projects, time-it-takes-to-build-a-reorg chain is the defense against this attack.   They raise difficulty and then can posit that this is their "security" -- total hashing power.    This leads to the arms-race and greater and greater hash which helps "secure" the chain, from very problem it allowed (re-orgs, 51% attacks)..    I remove the problem then also remove the arms-race.   An arms-race isn't needed if the security model isn't defending against 51% attacks and rollbacks.

A valid block has an expiration time window for which it must be seen.   There is no peer majority rule.   Peers see a valid solution within the solution window.  This triggers "grace period" (on their node); an allowed window to give the network time to propagate the best  valid solution.   If a node misses this window --- it is --- sorry Charlie.   This window is akin to any other chains "rollback" window, which is, in theory for them is, unlimited.  (ie, 100 block rollback if ok if someone was selfish mining with majority hash and dropped a longer/more work chain on the network).    No block is finalized in the grace window (thus no rollback when a better block is seen) -- block solutions are only collected/noted as the best and sent around.    After the window expires, the best solution is accepted, block finalized and the next round begins.     No late information about better chains or more work is relevant.   It missed the time window, thus has expired.

**3) There are no 51% attacks possible in ANNE.**  Protocol ensures they are an impossibility.   
So, this could be ensured in Monero as well -- but requires protocol changes.

**4)  No, selfish mining is not possible.**    One must put aside the current thinking and think with these new rules.   Blocks expire.   Only a 1 block solution can be submit.  Hard to be selfish with a 1 block solution and no ability to rollback your fellow peer's chain!!!.  :)   There is no notion of selfish mining because there are no rollbacks to put a longer chain in place.    This protocol was crafted by design to eliminate these unnecessary artifacts that were forced due to "longest chain" or "most work" foundational rules.   No such rules exist in this new model.  

**5)  Irrelevant Solo Handicap?** 
As it stands, I can concur with this point, with respect to Monero.   
In HD mining the solo mining handicap does exactly what it says it does.  It was created with the understanding that people have multiple keys.   Granted, in non-hard-drive mining (like Monero uses) it would need creative adjustments to hold the same relevance.  In HD mining there is a cost associated with building plots (used for mining) that are tied to a specific mining ID.

I'd be happy to have a video chat to discuss any of these points (if that is a better format for any monero devs who would be involved at the implementation level).   I didn't write the Monero PoT proposal (I read it and served as a guide to author radanne).   I can speak on how PoST works -- and clarify specific details as they pertain to ANNE.   I can also help at the hypothetical implementation solutions level of applying its thinking to Monero with respect to any aspect of this.  Ie, pick my brain -- it likes to solve things.  :)

Proof Of Time can work with Monero while preserving the integrity of PoW...  not fall victim to any elaborate unproven Rubes and it can enable an anti-fragile 800 lb gorilla called Monero to continue being the best possible tech in the payments space.   

## tevador | 2025-10-02T11:32:21+00:00
@r-a-d-a-n-n-e

> PoT's time consensus emerges from partial, gossip-based peer samples (10-20 direct connections in a 10k-node mesh), not a fragile global assumption.

Peers are not global, but blocks are. If I understand it correctly, miners set the block timestamp to their `chain_time` and other network nodes then use the block timestamp to decide if a block is valid or not. Skewed `chain_time` across the network might cause part of the network to accept a block, while another part will reject it. So I still see an implicit assumption that `chain_time` converges globally.

> The segments are overlapping and self-healing through median/binned aggregation. Monero already handles similar time convergence for block timestamps via Median Time Past (MTP), I believe, resisting skew by ignoring outliers and requiring majority honest peers.
>
> Sybil attacks (fake identities skewing reports) fail because adjustments need a 70% deviation consensus. Sybils in a local bubble (<70%) are ignored as 'outliers'. It's self-defeating. A global skew isn't possible. The blueprint suggests reputation-based peer curation (Section 3.0.1), which solves these concerns.

There is a big difference between those two.

Monero's MTP gives 1 vote to each block, which requires proof of work and can't be easily sybil attacked.

Your protocol gives 1 vote to each peer, which can be easily sybil attacked (yes, even >70% is possible).

> Feeding arbitrary offsets requires monopolizing connections, but Monero's outbound diversity (8+ random peers) and ban scores make >70% control resource-intensive. See Bitcoin eclipse analysis: https://eprint.iacr.org/2015/263.pdf

An eclipse attack requires the attacker to control *all* connections of a peer. We're talking about a sybil attack, which simply needs the majority of outbound connections to be malicious. Proof of work only needs 1 honest peer, your protocol needs >30% of honest peers. That's a clear security downgrade.

@MrScatman

> 2) There are no rollbacks. Protocol does not have an auto mechanism to rollback and alter chain history (re-org) with a better chain of blocks

Every protocol without rollbacks will inevitably chain split (either spontaneously or maliciously).

However, section 4.2 describes such a mechanism, which is a contradiction to your statement.

> 3) There are no 51% attacks possible in ANNE.

The 51% attack works by exploiting the peer reconciliation mechanism described in section 4.2.

> 4) No, selfish mining is not possible. One must put aside the current thinking and think with these new rules. Blocks expire. Only a 1 block solution can be submit. Hard to be selfish with a 1 block solution and no ability to rollback your fellow peer's chain!!!. :) There is no notion of selfish mining because there are no rollbacks to put a longer chain in place. This protocol was crafted by design to eliminate these unnecessary artifacts that were forced due to "longest chain" or "most work" foundational rules. No such rules exist in this new model.

Perhaps I'm misunderstanding, but imagine the following case:

Block B1 is published, then 29 seconds later, a competing block B2 is published. The PoW hash of B2 is smaller than the PoW hash of B1. Does the network "reorg" to block B2, or stay with B1?

If the network reorgs to B2, then selfish mining is easy. A selfish miner who mines a block B2 with a low hash value will simply withhold that block until 29 seconds after block B1 is found, causing the honest miners to waste hashes on the soon-to-be-orphaned block B1.

## SamsungGalaxyPlayer | 2025-10-02T11:45:47+00:00
I'm being blunt because there is a lot of content here without any actionable path forward, and a casual reader might mistake this to work as advertised.

**This method does not work.** One clear example that demonstrates this is that using the public key as a primary anti-sybil measure (e.g. in 4.4) is in direct opposition to 4.6. 4.6 says miners should avoid public key reuse to protect their privacy, entirely negating the "benefit" of the anti-sybil mechanism (upon which the network security relies). In any case, public keys are free to generate unless you have an account onboarding process for miners or similar, but obviously that has other major drawbacks. A well written proposal would not have proposed these two directly conflicting things in tandem.

"the P2P layer enforces a strict limit of one intent per peer submitted strictly via localhost connection" ??? Again, this makes no sense and is unenforceable.

I also second all of tevador's concerns.

## MrScatman | 2025-10-02T12:57:06+00:00
What sort of dev is responding to this?

How many lines of code did you write in Monero's protocol? 
Did you write Monero or did you come on later to _babysit_ the code?  (this is a type of persona)
Do you even babysit the code or are you just in the "protect the protocol" peanut-gallery?  (a viable/valuable cohort/persona, by the way)
 
Per the few responses I saw -- and the misconceptions and statements-of-fact that are in fact,  false; 
I can safely surmise y'all are not the people to spend any time engaging with about this.

Where is the fella/gal who WROTE MONERO?  
 
In general ---- even if I did run in to the top dev of the project and they turned out to be the standard _mask ignorance with arrogance low EQ_ dev  (god forbid) --- I have no such time or desire to aid in the forced mental clarity of the fogged mind.   I have my own project WITH NO SUCH PROBLEMS OR FLAWS OR DRAMA.   People hollering you can't break a 7 minute mile and I'm running under 4 already.   So, pardon me, but we're not in the same universe and I know better than to waste any time trying to drag people up.   I solve, build and do.  I don't babysit.  I'm not pitching.

Menero is easily forked to add in PoT.  In fact, any coin stuck with the same set of problems of old-think is.   And when faced with a Monero tech that rolls back and rug pulls or one that is rock solid and has zero rollbacks and no 51% possible, which does the market choose?   I know which one I would use.   Y'all remind me of how BSV was in this area.  I used that  coin a bit until it rugged a 100  block re-org.   Then their devs did their standard mental gymnastics.  Instead of acknowledge the foreseen-and-accepted-flaw in the design they inherited..  they danced around it.
 
I have **zero** desire to fork monero -- but you better damn well believe I'll help whoever is smart enough to see -- or at least give their selves a "chance" to see.   Coins like Monero are going to get forked to ELIMINATE the rollback and 51% attack vectors  -- and PoT is a solution.  It is being used, now, already.

 I will say no more in _this_ forum.    Good luck Radanne!   

## r-a-d-a-n-n-e | 2025-10-03T11:48:52+00:00
@tevador @Rucknium @vtnerd

I'll give a levelled response to all of this, mostly general, not personal, with one obvious exception.

If you worked under my management, I may fire at least half of you. Why? Because as a team, you are self-evidently incompetent. You failed to resolve the security of the consensus protocol in 11 years, or, in extent, in 16 years, since the "longest chain" flaw was introduced in the *alpha* version of Bitcoin, and Monero inherited it as a holy grail. Reliance on external layers for network security is the epitome of absurdity, and you position it into the NP-problem scope? Peer-to-peer cash for the world, huh?

Some of you charge the top US rates for COMMUNITY WORK. One of you charges 2x the US presidential annual salary. If there's a definition of a leech, you just got one; sucking but not delivering. The better part of your team needs to send the leeches to get a corporate job instead, a job where the quality and quantity of their contribution is subject to due oversight. Then they can start delivering, and so can you.

Under the current development environment, what do we, as the Monero community, that is your "employer", get? FCMP. Let's reach the upper levels of Bitcoin transaction volume, shall we?

avg 452,054 tx/day × 365 days = 165,000,000 p/a

4000 bytes ×165,000,000=660,000,000,000bytes=660GB

 That's the lowest accrued at that volume.

Since at that volume, many would be m/o, we can say 1TB bloat p/a.

 The same volume on BCH would be about 18x less (225b/tx)

1TB bloat per year isn't analogous to scalability, nor is it sustainable at this time. Not only does it reduce the number of full nodes, but it also puts out the small guy, even with pruning. It also games the guys who matter most - the small to mid-sized businesses, hindering adoption by increasing business expense, or forcing centralization onto third-party payment processors, which are regulated by the state. The market isn't ready to support such bloat. I understand it's a calculated risk. Monero won't get adopted to that level anytime soon, right? Very scientific approach, blimey. The trade-off isn't simply acceptable.

And here you are, collectively admitting a community-rejected proposal just because the baby cried for four hours. The almost-author himself proclaimed it computationally expensive and participation-limiting. Is the aim to game out the small guy, yet again? The non-solution is technically and philosophically incongruous with Monero tenets.

Consider this a threat. Should you go ahead with any form of PoS implementation, you will split/erode the community and likely the network. I won't upgrade my nodes, divert my hashpower if possible, dump my coins, and withdraw my existing and upcoming products from the ecosystem. So will many others, they already announced.

Now, please, everyone, come here and thumb me down. I hope I insulted those who deserve it to the highest possible degree. Every thumb down accounts for one NPC who could not suck up blunt, but very valid and constructive feedback.

If you're man enough to accept it and reflect, here's the deal. You misconstrue the AoP proposal as something we're obliged to defend. I could not care less if it's AoP, SoP,  PoP, or BoB that resolves the deterministic security of the Monero network, as long as it remains strictly within the scope of PoW and it's small-guy friendly. As stated, it is delivered to encourage an in-depth exploration of technical feasibility and adaptability to Monero; however, not by me or Mr Scatman. What he said. I'll help whoever is smart enough to see - or at least give their selves a "chance" to see.

It's beyond absurd to presume a write-up should solve your problems for you. Look at you, nay-sayers. You cherry-pick and rely on scientific papers someone else wrote. Do you know how these papers were written? Someone did the work, the experiment, before they happened. You're not doing the work or the experiment. You're leeching off them and cosplaying.

As you did with workshares. Dr K proved his solutions work; there's enough empirical data from 120k GPU miners in the first year. Spectacular. Look at Monero. Why don't we have even 1/10th of that in 11 years? Laughing stock.

The assumption of fragile global chain_time convergence, vulnerable to Sybil-fed offsets, is false. Convergence isn't assumed; it's enforced through decentralized gossip in partial segments, with binned aggregation of problematic diffs. Updates require ≥70% deviation consensus across *ordered* samples, discounting Sybil minorities as noise, isolating attacked bubbles without chain impact. Sybil "votes" aren't equal. The keyword is deterministic security. Identify each peer with a key pair. Get creative, thinking in that realm, and start coding. Options for deterministic conditions are endless.

Skewing peer reports affects local chain_time computation (via median/binned aggregation), and can be *rejected*; you got the means to do that. Deadlines are computed as elapsed time from the last block's embedded timestamp (global, median-aligned from honest producers) - not local chain_time. A Sybil-skewed node might miscalculate its "elapsed" (e.g., submit too early/late), rendering intents invalid/rejected network-wide (see and understand section 2.3). Forging a valid low deadline still demands RandomX PoW to produce a qualifying hash (uniform [0, target] distribution), tying "votes" to hashrate cost. Sybils can't spam low deadlines without majority mining power, as each intent requires a unique, verifiable PoW solution (one per key, signed, recomputed by nodes). Spam is *detectable* and *rejected*; ban scores are applied. Skew isolates the attacker to self-forked bubbles (see and understand section 4.1).

The 51% fork worry stems from a gross misunderstanding. You claim a contradiction between my proposal and Mr. Scatman's statement. For crying out loud, can you read? PoT draws on PoST, which doesn't mean in mirrors it. If you want PoST instead of PoT, we're at your disposal. You can go for a strictly manual option, problem solved. But auto is too feasible with the right conditions. A single peer recovers to rejoin the canonical chain. It cannot force onto others nor override what is provably the canonical chain! Validation gets a large enough sample, rechecks *every* post-fork intent under PoW/deadline rules. >70% node control is far from "easy" in deterministic security architecture, because you can *detect* and *reject*.

MTP vs PoT isn't a downgrade. MTP medians PoW-secured block timestamps (1 vote/block, Sybil-resistant via hashrate). PoT medians peer-reported chain_times (aggregated from local PoW timestamps + offsets, not raw peer count). Quality emerges from PoW-tied block production. One honest PoW block propagates its median-aligned timestamp absolutely via gossip. Research: Gossip sync bounds offsets <900 ms in 200-node adversarial nets, < 2s blocks. PoT bolsters security via deterministic finality, not weakens it. This ties "votes" to verifiable PoW blocks (not peers). Sybils can't fabricate chain_times without hashrate control. Deadlines rank separately by hash quality, but consensus anchors on PoW-anchored reports. Skewed peers get discounted or banned.

Your imagination highlights a classic selfish mining vector, but it misses PoT's core shift from probabilistic chains to deterministic, time-bound finality, which neutralizes withholding entirely. 

In the scenario, B1's intent triggers the 30-second grace at t=0 (say, its deadline=90s submitted at t=60s post-last block), locking all nodes into collecting intents until t=30s - finalizing the lowest-deadline block (B1) without re-org risk. A withheld B2 arriving at t=29s (89s post-last block) would be ranked by its deadline: if lower than B1's, it wins outright during grace (no re-org needed, as finality hasn't closed). If higher, it's discarded. But withholding delays B2's submission past its own deadline. PoT requires intents ≥30s before their deadline elapses (submission_time ≤ last_timestamp + deadline - 30s), rejecting late ones to force early broadcasts and avert exploits.

Selfish miners can't "orphan" B1 post-grace. Continued mining yields worse deadlines (elapsed time inflates them), detectable via patterns and penalized with bans (Section 2.3). Honest miners halt on the trigger, wasting no hashes. Unlike propagation races, PoT ranks deadlines absolutely from PoW-derived pseudo-time, buffered by grace for ~15s delays (ns-3 validated). Withholding self-sabotages, as rewards lock on the canonical block via lowest-deadline determinism.

That NPC who burst in misreads PoT's layered defenses, pitting privacy against security in a false dichotomy while overlooking enforceable mechanics. Section 4.6 recommends subaddress-derived ephemeral keys, but anti-Sybil (4.4) tracks reputation and hashrate samples over rolling eras (3.1.1, 3.2.3). Not raw keys. Rotation resets handicaps and samples (downweighted for <5 submissions or more), forcing attackers to rebuild effort-based "votes" via PoW-derived deadlines, costing sustained hashrate, not free keys. VRF-seeded verification (3.2.2-3.2.3) ties submissions to verifiable hashes, rendering spam unprofitable. Sybil needs the majority of mining power to dominate low-deadline rankings, not infinite keys. One intent per peer" means miners submit locally via RPC to their node, with nodes relaying one-per-key-per-height globally. Peers enforce via duplicate rejection and ban scores on excess (4.4), verifiable by recomputing deadlines. Floods trigger disconnections, as in Monero's existing anti-spam defenses. It's not unenforceable "peer connection" limits but protocol-level validation, scalable, and Sybil-resistant. Any attempt to spoof multi-submissions from afar triggers duplicate rejection on relay. It's verifiable and self-policing. PoT upgrades resilience, not undermines it.

I could forever continue on and on, and throw some muscles with scientific papers, as there are many to be found that hold, and often analogously, strongly support PoT. But I refuse to entertain any counterproductive "nay" feedback. Your feedback isn't required and, at this stage, no longer desired.  You can't even read between the lines and got it all the other way round.

We are the guys with the ultimate solution, and you are the guys who don't have a valid solution. As Mr Scatman stated, your misconceptions and statements of fact are, in fact, false. You are expected to conduct research, deliver adaptation to this proposal, and address any challenges en route.

If none of you can't do that, that's your loss, and sadly, a tragic loss for Monero. Whoever can do that, the door remains open. To such a person, we'll help in any way we can, for the sake of Monero. That's what matters to me. Ergo, my bounty offer stands.  All you have to do is ask questions instead of being adversarial. My conditions stand for anyone who wants to level up. Otherwise, I'll rest my case. I can lead the horse to the water, but I can't force him to drink. 

My DM is open. Consultation with Mr Scatman is not optional. Adapt or perish.

## tevador | 2025-10-03T21:17:06+00:00
This stopped being a respecful discussion a couple comments ago, but I will ignore the personal attacks and threats and post one final comment before this issue is closed.

Yes, Monero has been under attack and some weaknesses of the current consensus mechanism have been shown, but we have to be careful when working on a solution to make sure we don't introduce "a cure worse than the disease". In general, we should favor simpler proposals that don't have apparent weaknesses and can be rolled out gradually or as a soft-fork.

Any decentralized consensus mechanism must pivot from a scarce resource to prevent sybil attacks. With proof of work, that resouce is computational power and the implicit assumption is that the majority of the hashrate is controlled by honest actors. There is simply no safe and decentralized mechanism to prevent 51% attacks with only proof of work.

To quote myself, here is a proof by contradiction that no permissionless consensus algorithm based solely on proof of work can prevent 51% attacks:

> Let there be such a consensus algorithm. Let H be the honest actors and A the attacker. If hr(A) > hr(H), there must be some strategy S that H can employ for their chain to always win. Then let hr(A) < hr(H) and let A employ strategy S. The attacker wins.

Simply put, anything you do to make a minority's chain win can be replicated by the majority attacker. Information gathered on the P2P layer, such as block arrival time, is not something that can be used for consensus. That information is lost for future blockchain verifiers.

Any attempts to "fix" 51% attacks without adding other scarce resources to the mix (staked coins, disk space etc.) will inevitably result in a chain split and will require subjectivity (manually selecting the "correct" chain). Satoshi Nakamoto knew this very well when [he wrote this about 51% attacks in 2008](https://www.metzdowd.com/pipermail/cryptography/2008-November/014832.html):

>  This touches on a key point. Even though everyone present may see the shenanigans going on, there's no way to take advantage of that fact.
>
>  It is strictly necessary that the longest chain is always considered the valid one. Nodes that were present may remember that one branch was there first and got replaced by another, but there would be no way for them to convince those who were not present of this. We can't have subfactions of nodes that cling to one branch that they think was first, others that saw another branch first, and others that joined later and never saw what happened. The CPU power proof-of-work vote must have the final say. The only way for everyone to stay on the same page is to believe that the longest chain is always the valid one, no matter what.

So there are only 2 ways forward:

1. Stay with PoW, optionally fix selfish mining and accept that 51% attacks can happen. Examples: #98 #144  #146
2. Introduce another "scarce resource". Examples: #135 #145

---

Now, to address some of your comments:

> Updates require ≥70% deviation consensus across ordered samples, discounting Sybil minorities as noise

In a sybil attack, the attacker will easily control >70% of nodes (this actually happened in 2020).

> isolating attacked bubbles without chain impact

You can't say it's without impact if the bubble contains, for example, a node used by a large exchange that can be easily defrauded as a result of this isolation.

> Sybil "votes" aren't equal. The keyword is deterministic security. Identify each peer with a key pair. Get creative, thinking in that realm, and start coding. Options for deterministic conditions are endless.

[Citation needed]

There is no decentralized way to tell if a peer is part of sybil attack. An attacker can generate as many key pairs as they want. See what I wrote above about scarce resources. Network nodes and key pairs are not scarce resources, so you can't base consensus on them.

> Skew isolates the attacker to self-forked bubbles (see and understand section 4.1).

This is not an acceptable property at all (see the exchange example above).

> PoT draws on PoST, which doesn't mean in mirrors it.

Your PoT proposal clearly includes section 4.2, which talks about a peer reconciliation mechanism.

> You can go for a strictly manual option, problem solved.

Strictly manual option means: Everytime you connect to the network, you need to manually select the correct chain. How is that in any way acceptable?

> override what is provably the canonical chain

Except you can't prove that. See the Satoshi Nakamoto quote above.

> Sybils can't fabricate chain_times without hashrate control.

Your proposal, chapter 2.1, clearly says that:

`chain_time = floor((system_time - MONERO_EPOCH + 500 + ms_adjust) / 1000)`

where `ms_adjust` is based on reported peer time and can be up to a year off. So if sybil peers make `ms_adjust` to be 1 year, the sybil attacked node will have `chain_time` approximately 1 year in the future. I don't see any PoW protection for `ms_adjust` in your proposal.

> A withheld B2 arriving at t=29s (89s post-last block) would be ranked by its deadline: if lower than B1's, it wins outright during grace (no re-org needed, as finality hasn't closed). If higher, it's discarded.

Yes, so we agree on this. As long as B2 has a lower deadline, the attacker overrides the honest block B1. This is called selfish mining. It limits reorgs to 1 block, but that's enough for the selfish miner to get an edge.

> Your feedback isn't required and, at this stage, no longer desired.

If you don't want feedback, please don't post your proposals here.

In summary:

1) You came here with a proposal. Commendable.
2) I reviewed your proposal (for free) and found flaws.
3) You got angry and started insulting everyone.

Try to submit a paper to a peer reviewed scientific journal. You won't get far with this approach.

@Rucknium please close.

## r-a-d-a-n-n-e | 2025-10-04T08:52:41+00:00
Yes, please, hurry and ask the boss to close this issue, so you don't look even worse than you already do. Imagine quoting Satoshi to defend Satoshi's 16-year-old bug under a proposal that tackles the very bug, and still wonder why I say your feedback isn't valid. Your approach seems focused on dismissing the concept entirely by cherry-picking statements and taking them out of context, rather than genuinely exploring it. Why should I want feedback from someone who repeatedly shows a lack of understanding? You're not asking questions about something that is very clearly new to you; you're outright dismissing it. It feels futile.

@Rucknium I could respond to each new point Tevador makes and explain why none of it is valid. If you want, leave this issue open, and I will come back later to address it. However, at this stage, I'm not sure if there's a point. Is there no one who is at least willing to consider PoT with an open mind?

## tevador | 2025-10-04T09:52:09+00:00
This issue will be closed not because I said so but because of your inability to have a civil discussion without personal attacks and threats.

Your last comment where you rushed to attack me personally instead of presenting counter arguments is proving my point.

[Ad hominem](https://en.wikipedia.org/wiki/Ad_hominem) has no place in research lab discussions.

## r-a-d-a-n-n-e | 2025-10-04T13:01:36+00:00
Nothing proves your point @tevador, on the contrary, you continue disproving your points. There wasn't any ad hominem. If there were, my arguments would lack substance, which isn't true. My feedback provided direct and valid criticism of your overall approach and highlighted other key issues, supported by substance. I didn't rush to attack. I stated some facts ahead of my full response because you beg to close this issue. Hence, I asked @Rucknium if there is even a point to continue. If there isn't, by all means, close the issue. If there is, I will clarify the details as soon as I can, as I stated prior, I'm not in a position to give immediate/full responses until the 20th.

## tevador | 2025-10-04T21:15:54+00:00
You are only complaining about the fact that I'm finding holes in your proposal. You are in no position to criticize my approach when I'm providing feedback on your proposal in my own free time. The only thing you are allowed to do it to disprove my points, which you are clearly unable to do.

> There wasn't any ad hominem

You attack and insult people rather than adressing their arguments against your proposal. That's the very definition of ad hominem.

> quoting Satoshi to defend Satoshi's 16-year-old bug under a proposal that tackles the very bug

The longest chain rule is not a bug, it's a feature. As I proved above, **you cannot fix 51% attacks with proof of work** without introducing chain-splitting vulnerabilities. Satoshi Nakamoto correctly considered chain splits to be much worse than potentially long reorgs.

It's true that your proposal (minus section 4.2) "fixes" 51% attacks, but only at the cost of chain splitting (what you call "local bubbles"). For example, [Publish or Perish](https://www.researchgate.net/publication/312184074_Publish_or_Perish_A_Backward-Compatible_Defense_Against_Selfish_Mining_in_Bitcoin) with k=∞ achieves the exact same thing and the paper is only 16 pages including simulation results and references (your 29-page proposal notably lacks both of these).


## A60AB5450353F40E | 2025-10-05T07:21:39+00:00
@r-a-d-a-n-n-e instead of implementing a whole new system why not just fix PoW/NC?

BCH is at risk too, and this is the direction I have in mind: https://github.com/zawy12/difficulty-algorithms/issues/30

Much simpler than a whole new add-on consensus system.

Another thing, currently XMR and BCH are near in real world value of their block rewards, so security is nearly the same. Ultimately, all networks are protected by their economy: bigger economy, more hashes each blocks can bid for, more security. Still, ASIC vs CPU makes a big difference.

XMR touted its ASIC-resistance as a selling point and has been obsessing over being CPU-only. I think that was a mistake. Had you stuck with original PoW you'd have your own dedicated ASICs by now, and miners would be committed. With CPU algo, you're not competing for hashes just with all other coins, you're competing for general compute with all other buyers of CPU cycles, which there is an ocean of. Just 5% of one Google's datacenter has enough "hash" to take over XMR (~100k CPUs).

You can't buy what's not for sale. Anyone with money can rent 100k CPUs from anywhere, there's plenty of supply out there. They can't simply rent the equivalent in ASICs, because they're all already busy doing the one thing they were made for: mining their algo.

ShadowOfHarbringer tried to bring this up on your Reddit (removed by automod, I don't even try to post on Reddit anymore), he summarized what I've been talking about in other places:

- ASIC miner market creates "sunk cost" fallacy for miners that have heavily invested in thousands of specialized expensive devices consuming a lot of power. Once they are "in", it's difficult to get "out" without massive loss. So this incentivizes them to protect their network and defend them against attackers, otherwise if the network gets wrecked, they end up with useless pile of trash that can be only used as portable electric heaters
- ASIC-protected network cannot be easily attacked by Google, Amazon, Microsoft Azure or other cloud vendor by simply buying up processing power, like NON-ASIC networks
- Specialized Mining Devices are much more scarce to purchase and lend. Also owners of the miners might be reluctant to lend their devices for cheap to get their networks attacked, this destroys their business model long-term. This makes entry into this market harder than entry into CPU-only model; theoretically
- Mining(SHA256d) is multi-billion industry right now. Which means tens of thousands or more people are "in" it. All of these people will be incentivized to not let attacker harm the networks they mine, it's huge.
- Any corporate attacker or government attacker aiming to attack any ASIC-protected network would have to spend A LOT first on renting/building factories, then A LOT on buying power at market prices, then A LOT on hiring people to watch these factories 24/7. And then (in many societies, especially some democracies) they would have to explain to their society / their shareholders, why they are spending gazillions of money regularly in order to attack some coin. This would be quite an operation, quite difficult one.
- ASIC miners have already proven they are going to defend their network from attack. They did this for BCH in 2018, when BSV attacked it. Unfortunately this did not happen yet for CPU coins at similar (huge) scale.

Overall, attacking an ASIC-protected coin seems like a much bigger hassle than CPU-protected coin for the attackers, so maybe it would be good to reconsider this stance?

## tevador | 2025-10-05T09:57:42+00:00
@A60AB5450353F40E Thanks for the [link](https://github.com/zawy12/difficulty-algorithms/issues/30). I'll quote one section from there which is relevant to this proposal:

> Coins should not use peer time because a median from peers is a consensus mechanism that does not have POW security. This allows a Sybil attack to slow a victim's network time up to the point that blocks with honest timestamps will be more than the FTL past the victim's network time, causing him to reject the blocks [...]

---

> XMR touted its ASIC-resistance as a selling point and has been obsessing over being CPU-only. I think that was a mistake.

This should be a seperate discussion because it's unrelated to the current proposal.

## coffnix | 2025-10-05T12:14:39+00:00
I am fully in favor of the anti ASIC model, because I believe it is the only real way to keep a network decentralized. RandomX was created precisely to neutralize the unfair advantage of proprietary hardware, making it unfeasible or economically absurd to develop specific ASICs and favoring the use of common CPUs, this brings mining back to the people, not to factories and corporations.

When I say one CPU equals one vote, I mean that every person with a computer has the same weight in the network, without privileges for those who control chip production lines. With ASICs this is impossible, whoever dominates manufacturing and logistics monopolizes mining and, in practice, sets the rules of the system.

In my view, ASICs raise entry barriers and concentrate power in the hands of a few, if only those with capital and factories can mine, the network stops being free and becomes a digital oligopoly. CPUs are everywhere and allow anyone to participate, this increases censorship resistance, spreads power geographically, and reduces single points of failure.

Keeping the anti ASIC ideal reduces the risk of coordinated attacks and prevents a single entity from capturing the global hash, the cost to dominate a CPU based network is very high and broadly distributed, this economic pressure is what sustains security in the long run. That is why, for me, anti ASIC together with the one CPU equals one vote principle is the foundation of a fair, secure, and truly democratic network.

As for Proof of Time, it has merits, but it is not a silver bullet. Time can be forged by malicious nodes in eclipse scenarios, any protocol that derives consensus from logical clocks must treat bias, outliers, and quorum with extreme care, otherwise it becomes a vector for network splits and segment capture. The practical conclusion is straightforward, POT does not replace RandomX PoW, which has already proven resilience over time and to Qubic’s bogus 51% attack, POT serves as a complement with well defined boundaries against economic selfish mining, but only as an additional layer on top of RandomX, not a full replacement.

If the idea is to experiment, it is better to treat POT as an auxiliary layer, not an engine swap, use POT deadlines or intents as fairness telemetry and ordering inside pools, while consensus remains purely RandomX. This way you can harvest some practical finality gains and reduce withholding at the pool scope, without opening the attack surface of the base protocol.

Thanks to @r-a-d-a-n-n-e for the blueprint and the technical provocation, serious debate is born when someone pokes the comfort zone. The critique here is engineering, not politics, the design has to hold up on real networks with real latencies and real adversaries, which requires validating assumptions about time convergence, fork reconciliation, and targeted Sybil resistance before talking about a hard fork.

A concrete path is to test POT in decentralized pools like p2pool through a proxy that accepts intents, computes deadlines, and applies internal selection and payout rules, while keeping the winning block under standard RandomX. If it works, great, it becomes an operational improvement for the pool, if it does not, the main chain stays intact and the experiment dies in the right scope.

Another good suggestion would be to adjust rewards, where we could keep payouts for both cases, paying more to whoever announces the block earlier and also paying partial rewards to orphaned blocks, which would make it unappealing to delay block announcements using POT and its timestamp logic, and would privilege higher payment for whoever publishes first, which would disincentivize selfish mining in most cases. Let us think this through carefully, discuss the possibilities, and treat code as code, sharing example implementations and testing many approaches so that the best code wins against the current financial attack threat. We know this is not a cyber attack, it is a financial attack, so I believe the ideal solution should be based on financially disincentivizing selfish mining.

## tevador | 2025-10-05T12:37:54+00:00
> higher payment for whoever publishes first

Unverifiable. New nodes joining the network can't know which block was published first. See the Satoshi Nakamoto quote from 2008.

## A60AB5450353F40E | 2025-10-05T17:51:23+00:00
>This should be a seperate discussion because it's unrelated to the current proposal.

Got it, moved here: https://github.com/monero-project/research-lab/issues/148

and addressed @coffnix 's comments.

## r-a-d-a-n-n-e | 2025-10-08T12:07:08+00:00
@tevador, permit me to set the record straight with the utmost clarity. You are scarcely placed to presume the authority to prescribe who may utter what, least of all beneath my own proposal. I cannot but regard your dismissive and peremptory demeanour with profound disquiet.

I award no prizes for voluntary hours. My own are offered without charge, in like manner, in service to Monero. Upon this point, at the very least, I am confident that we may agree. In my earlier response, I addressed every technical matter you raised, counterpoising it with my candid criticism, and I continue to do so. Ad hominem attacks are not equivalent to criticism of dismissive hubris. You have devoted little of your leisure time to the matter, for all your replies are curt, couched in absolutes, and bereft of justification. Your frame of mind appears fixed upon discovering holes, rather than devising remedies for those you mistakenly perceive as such. Is it a subterfuge or constructive feedback? I shall leave it to the audience to judge.

I endorse any PoW-only proposals that truly resolve the issues at hand. The pertinent question is, do they solve problems and to what extent? The notion of lucky transactions is intriguing, to be sure, but by your own concession, you harbour considerable reservations about its implementation - rendering it akin to a partially formed remedy that even you cannot fully endorse. A commendable endeavour in any case. The other proposals only mitigate selfish mining.

PoT constitutes a subset of PoW, a straightforward adjunct implementation, and remains compliant with the longest chain rule. It is an extension thereof that fortifies it, rather than abolishes it. One must indeed exercise due caution to ensure that the deterministic conditions are applied with precision and subjected to rigorous testing.

The longest chain rule constitutes a flaw (indeed, a bug), conceded by Satoshi himself, rather than a holy grail. One may apply patches and endeavour to mitigate sundry issues to a limited degree, yet one cannot resolve them comprehensively without a solution that addresses them all at once. Even the infamous PoS finality layer falls short of achieving this. Unfinalised blocks remain subject to the existing conditions, the layer itself introduces new attack vectors, whilst being excessively complex and computationally expensive - it is not a valid solution then.

With the right solution, a hard fork is inevitable, but a smooth legacy transition is feasible, as I have pointed out. One might deploy non-consensus-altering soft fork simulations upon the mainnet and empirically substantiate every facet thereof prior to the switch. This elucidates and rebuts your apprehension of "a cure worse than the disease", whilst you may rest assured that the community will gladly support such an endeavoured experiment and scientific exploration financially.

Your argument is a classic proof by contradiction against pure PoW's ability to resist 51% attacks. It incisively exposes the vulnerability in probabilistic longest-chain consensus. A majority attacker can replicate any minority strategy to overwrite history, as the system lacks a verifiable tiebreaker beyond chain length.

Satoshi articulated this as a limitation, not as a feature, in the Bitcoin whitepaper:

> "To modify a past block, an attacker would have to redo the proof-of-work of the block and all blocks after it and then catch up with and surpass the work of the honest nodes." 

He modelled the risk probabilistically, likening it to a "Gambler's Ruin problem," where success hinges on exponential honest majority outpacing the attacker economically, and further conceded the fragility:

> "The CPU power proof-of-work vote must have the final say. The only way for everyone to stay on the same page is to believe that the longest chain is always the valid one, no matter what." 

https://satoshi.nakamotoinstitute.org/emails/cryptography/6/ 

To suggest this means that peer-to-peer cash-for-the-world has to forever rely on "features" of assumption of honesty, faith, and the fragility of external layers is untrue. Satoshi was not a priest. He used the word honest in Bitcoin WP 16x in relation to the honest majority/nodes - a distinct limitation, not protocol strength - as it relies on external validation layers. Notice that Bitcoin came into existence as an alpha version, not a set-in-stone protocol, which is also why Monero exists.

He signifies the terms "believe and no matter what" in the context of the as-is solution, not in the context of universal, forever facts, and indicates that the external vote should evolve beyond subjective probabilistic measures. What is needed are resolutions that fortify the PoW framework deterministically without scarce alternatives like stake, and without supplanting the longest chain rule or the PoW consensus model.

The contradiction collapses because PoT grace anchors evaluations to the prior block verifiable timestamp (secured by the chain_time producer, itself median-aggregated from honest peers), not local skew or ephemeral P2P artefacts lost to future nodes.

PoT resolves the attack vectors by supplanting length-based races with an absolute, verifiable deadline. Each deadline is derived from a RandomX hash. A nominal extension to extant PoW mining and validation, resulting in a pseudo-time deadline attained through normalisation. Within the grace period, initiated by the first valid intent, nodes continue to collect and rank all outstanding/pending submissions deterministically by lowest deadline, embedding the winner as the immutable block timestamp. This achieves instant finality.

Yet you posit...

> "Yes, so we agree on this. As long as B2 has a lower deadline, the attacker overrides the honest block B1. This is called selfish mining. It limits reorgs to 1 block, but that's enough for the selfish miner to get an edge." 

We do not concur on this matter. You have misconstrued it from its proper context, compelling me once more to reiterate and recast what has already been articulated:

PoT requires that intents be submitted at least 30 seconds prior to their deadline (submission_time ≤ last_timestamp + deadline - 30 seconds), rejecting belated submissions to enforce timely broadcasts and prevent potential exploits. It is designated a deadline for a reason. "Late" arriving deadlines cannot have better seconds, and should they fare too close to the end of the grace (which you will ascertain through rigorous testing), it is detectable - one can safely infer that someone is meddling, can reject, apply banscores, enforces a cool-off interlude, blacklists, or nukes the perpetrator on repeated offense, adieu, selfish miner.

Post-grace arrival exceeds the window, as deadlines are pseudo-times elapsed from the global prior timestamp. Such "selfish mining" is analogous to self-sabotage, not overwrite. There is no block reorganisation. We are discussing intents - the block is neither forged nor propagated until a solution is agreed upon deterministically. This elucidates and rebuts your concern apropos selfish mining reorganisation.

Regarding Sybil attacks, Sections 3.0.1 and 4.4 outline P2P protections for mining (e.g., one intent per peer via localhost, ban scores for excess submissions), whilst the core protocol in Sections 2.1, 2.3, and 4.1 fortifies against both non-mining (report-flooding) and mining Sybils targeting chain_time. PoT is fully resilient in its proposed form, leveraging deterministic security that is not static but creatively extensible. 

Fundamental defences include 70% deviation thresholds for updates, outlier discounting in median/binned aggregation, and the additive ms_adjust to avert oscillation. This ensures skew attempts fail without peer ranking. Block timestamps, as PoW-anchored global deadline references, further secure the system. Peer ranking is an optional enhancement for flood robustness, not a critical feature. If requested, I can detail a peer-weighted model linking votes to verifiable PoW effort, enforcing scarcity beyond simple key pairs (Section 4.6). Your concern applies to probabilistic PoW, where Sybils enable eclipse attacks and local dominance, but not the PoT deterministically fortified model.

Non-mining Sybils flooding reports cannot meaningfully skew chain_time, as local computation - floor((system_time - MONERO_EPOCH + 500 + ms_adjust) / 1000) - relies on aggregation alone (Section 2.1). Updates trigger only on ≥70% deviation across ≥5 prioritised samples, treating high offsets (and optionally low-rep reports) as noise. Binned mode rounds diffs to 500 ms bins, smoothing neighbours to cluster toward the honest median, even without ranking. Skewed views miscompute elapsed time, invalidating intents on grace checks (submission_time ≤ last_timestamp + deadline - 30s, Section 2.3), whilst block timestamps embed the producer's median-aligned chain_time as a verifiable PoW artefact. Even if Sybils temporarily dominate a bubble (network segment), block timestamps embed the median-aligned chain_time, serving as a global reference for deadlines.

Attackers self-isolate through binned mode, with skewed mining nodes submitting invalid intents that fail propagation (duplicate bans, low-rep discount). Non-mining Sybils cost resources without gain, mining ones require a high hashrate for low deadlines that survive recomputation. One intent per mining peer is unquestionably enforceable. Reputation develops through database primitives if necessary, but the current layers are sufficient. For empirical grounding, Monero 2020 Sybil attack involved multiple malicious nodes attempting thousands of connections to target IP deanonymisation. It caused no consensus skew or divergence despite transient peer manipulation, validating PoW+PoT's upgraded security.

Even in a targeted ≥70% Sybil flood on a local segment (10-20 peers), the impact is transient and self-correcting, with no fraud or chain-wide effect (Sections 2.1, 2.3, 4.1-4.2). The node's ms_adjust shifts additively, diverging its chain_time locally, but non-miners produce no intents or blocks. Validation uses the embedded block timestamp as the absolute reference. Recompute RandomX hash for difficulty, derive deadline from hash/target (Section 2.2), and check grace adherence against it (no Sybil input). The node detects the attack via anomalous offsets, disconnects attackers, acquires new peers (optionally via config-specified trusted ones), and self-corrects via ongoing aggregation. Invalid skewed intents are discarded universally. Honest majority ensures flow, with bans on duplicates/anomalies. Rewards lock deterministically, preventing double-spends or forks. Empirical tests confirm honest drifts rarely exceed seconds (Sections 2.1, 4.1), and binned mode smooths persistent offsets as anomalies for isolation. Simulations will validate this robustness.

Yet you posit... 

> "This is not an acceptable property at all" 

...against “Skew isolates the attacker to self-forked bubbles” – it lacks context, given the above, also as previously explained. Local attackers are foreseeable, detectable, and isolatable without local or global harm. The claim that PoT fixes 51% attacks at the "cost of chain splitting" (likening to Publish or Perish) is a false equivalence. PoP relies on probabilistic races with re-org risks and uncle rewards, whereas PoT rejects late intents mechanically, ensuring liveness without orphans or forks. There is no "length" to publish against. Bubbles are transient local skews that self-correct via aggregation, not splits. They do not diverge from the canonical chain.

Local skew does not override global anchors as nodes compute internally, but intents/blocks validate against embedded timestamps (verifiable PoW artefacts, Section 2.3). Sybil minorities discount as outliers in binned mode (|diff| ≥500 ms smoothed to honest medians, Section 2.1); honest gossip pulls ms_adjust back via 70% thresholds. There is no fork threat. Only attackers self-fork to irrelevance (Section 4.1).

In other words, the "chain splitting" concern is a misreading of terminology. The PoT blueprint explicitly uses "self-forking" in Section 4.1 to describe colluding or Sybil bubbles: "If colluders form a tight-knit peer circle, they only alter their own isolated bubble, effectively forking themselves into irrelevance." This is not a global chain split or re-org (which PoT eliminates deterministically). It is a local, self-defeating divergence where the bubble's skewed local chain_time fails validation (late per grace check, Section 2.3) and fails propagation, dying out without impacting the canonical chain or the attacked honest nodes. Bubbles self-correct for honest nodes, whilst self-forking attackers to irrelevance through cool-off interlude, blacklists, or nukes. It is indisputably acceptable because it is the strength of the protocol where transient local errors (seconds, ns-3 gossip <5s) self-extinguish, ensuring liveness and finality without forks, which is far superior to probabilistic block reorganisations.

**Vital Note: Mitigating Miner Isolation**
Miners must maximise the number of their peers in order to propagate their intents effectively and maintain the accuracy of their clock times. When a miner has but few peers, they may encounter difficulties in adjusting their clock, which could precipitate potential forks should their time deviate beyond the grace period.

A mining consortium siloed internally resembles a Sybil botnet in a temporal enclave, the sole "splitting" danger for minor segments. To counter this, add an automated/configurable mechanism for solo miners to connect to diverse peers, ensuring broad samples and preventing isolation.

The above elucidates and rebuts your concern apropos "Sybil attack against the chain_time", and "chain splitting".

Regarding recovery mechanisms, you posit...

> "Strictly manual option means: Everytime you connect to the network, you need to manually select the correct chain. How is that in any way acceptable?"

This is a clear misinterpretation of the proposed design. Standard bootstrap uses automated IBD, resolving 99%+ cases without intervention. It should not need to be spelt out. We never proposed overriding/replacing any of the existing sync features or any PoW features for that matter. Only to deterministically fortify that which can be fortified and advocate only for necessary and PoW+PoT-compliant adjustments to be adopted.

The manual or automatic recovery mechanism is a targeted safeguard for rare divergences, not invoked "every time you connect." Rare shallow forks (<10 blocks from common ancestor) can auto-resolve via quorum (70% tip consensus sampling ~200 peers over 2-3 hops, Section 4.2), with sequential revalidation (recomputing PoW/deadlines) in <1 minute. Acceptability is self-evident. It acts as a precision valve against engineered deep attacks, prioritising immutability in rare extremes over the automated, hands-off syncing of everyday connections, much like Monero's manual resync (deleting LMDB files or "--pop-blocks" for anomalies), used only when critical, not routinely.

You further posit... 

> "Except you can't prove that."  

Indeed, I can, and so can you. That is the very purpose of logic, systemic thinking, and empirical testing.

Recovery proves the canonical via deterministic recomputation, incapable of override. From the common ancestor, it revalidates the alternative sequentially, recomputing every RandomX hash for difficulty, deriving deadlines (floor((hash × 180) / target), Section 2.2), verifying grace (submission_time ≤ prior_timestamp + deadline - 30s), and uniqueness (no key duplicates). Forged chains fail universally, as deadlines anchor to embedded timestamps (verifiable PoW artefacts from honest producers, Section 2.3). Each node runs the math offline. Quorum (70% consensus, >10% margin over local) selects the highest-scoring tip, tiebroken by height/progress. Honest majority prevails, affirming the recomputable canonical.

The above elucidates and rebuts your concern apropos the "recovery mechanism".

To conclude this matter, I did not say that I do not want feedback. I appreciate quality feedback and discussion - I bid it welcome. Should you shift the nature of your feedback from dismissive to constructive and direct it towards clarifying and resolving perceived setbacks, then we may collaborate in creating value for Monero by discussing further.

PoT is not a threat to PoW, and it is not a replacement nor an alteration of existing PoW features. It is an extension and evolution, moving it into the next phase of adoption, instead of dicking around with reorgs. Impossible for adoption, yet here we are worrying about a time Sybil attack and attacker forks, which are easily handled, as I clarified. The current system already allows attacks that massively damage reputation and confidence. That dear fellow is utterly unacceptable. It can seldom be made any worse with deterministic upgrades.

@riz878 
Thank you for your kind feedback and highlighting PoT's targeted scope factually as a PoW evolution, not revolution, and the peer median as the pillar deserving rigorous audits.

Your TLA+ suggestion for formal verification is spot on, needed for convergence proofs. The ns-3 sim snippet is a great starting point. Section 2.1.1 already cites analogous gossip models (80-90% alignment in 1 block).

Weighted lottery indeed dilutes and discourages the pools, whilst promoting solo viability. As I suggested to Tevador, one might deploy non-consensus-altering soft fork simulations upon the mainnet and empirically substantiate every facet thereof prior to the switch.

@A60AB5450353F40E 
Thank you for your input. Although I cannot agree that ASIC is the right way forward for Monero, you still made a relevant contribution to my proposal.

First, understand that Monero's vision is largely incompatible with Satoshi's vision. Monero is committed to perpetual decentralisation through the ASIC-resistant mining algorithm, which stands in stark contrast to Satoshi's prescient vision for Bitcoin. Satoshi anticipated that, as the network expanded, mining would inevitably consolidate among "specialists with server farms of specialised hardware," accepting such centralisation as a natural evolution whilst advocating for a single node per farm to maintain broader participation. The "stakiness" of ASICs resembles Proof of Stake due to its capital lock-in and exclusion of smaller participants. It creates significant barriers to mining access and encourages vendor monopolies, favouring industrial stakeholders and rendering upgrades outdated every 12 to 18 months. It loosely mirrors PoS's wealth concentration, and Monero's RandomX counters this, striving for egalitarian participation. ASICs are not acceptable for Monero.

Here is my observation regarding @zawy12 proposal you linked. PoT and his proposal are moderately analogous, as they both address PoW evolutions against time manipulation, emphasising local time to resist Sybil/eclipse attacks and maintaining tight bounds for convergence. They share goals of stable blocks and selfish mining resistance, with fast sync. PoT is more holistic (timechain + deadline auctions for instant finality, eliminating re-orgs deterministically), whilst his is incremental (monotonic timestamps + RTT for difficulty precision, still probabilistic). PoT ties votes to PoW-derived pseudo-times for Sybil-proof quorums. Zawy12's proposal depends solely on local clocks, but it could serve as inspiration for PoT's timestamp limits. PoT achieves broader determinism without chain splits. 

Despite PoT might seem complex at first glance, it is far from a whole new system. It is a mere extension to PoW, codable in ~2000 lines of code. Piece of cake, once understood. If PoT is something BCH lead devs would be interested in, I would be happy to discuss and help.

@coffnix 
I appreciate your constructive feedback. In light of my above response to Tevador, I trust you will find greater clarity regarding how PoT addresses the subject of "time can be forged by malicious nodes". Have read and share your reflections.

PoT may not be a silver bullet, especially not on paper, but given proper deterministic conditions, one cannot get any closer. The current PoST implementation serves as the ultimate fortification of PoW. PoT is an equally robust enhancement to PoW without supplanting it. Rather, it functions as an auxiliary model that requires only nominal adjustments to the PoW model, as you enunciate, "not an engine swap."

I prefer to see mining pools abolished through proposed mining models and deterministic conditions rather than used for testing. Though I agree that testing via p2pool is a valid approach.

I am not convinced that there is any tangible benefit in providing a higher payment to the first to publish, nor whether such an approach would be desirable within the framework of PoT. Being the first to publish does not secure a win, as the quality of the PoW solution is paramount. PoT already precludes late submissions to enforce promptness and transparency. See Section 2.3: Submissions must arrive with at least 30 seconds remaining until the deadline elapses (i.e., submission_time ≤ last_block_timestamp + deadline - 30); intents arriving later are invalid and discarded, averting miners from delaying broadcasts to exploit timing edges (e.g., a 90-second deadline submitted at the 80-second mark, leaving only 10 seconds, would be rejected).

Without in-depth deliberation, I imagine that it would be verifiable by incorporating local time within the propagation intent, validated against the deadline, the timestamp of the last block, and in accordance with propagation time. In theory, it should be feasible to ascertain which non-winning valid intent was propagated first or to grant a bonus to the winning intent. Though this introduces additional complexity, it aims to establish a financial incentive in the form of a consolidation prize or bonus, rather than enhancing security. An intriguing incentive, nevertheless.

I am astounded by Tevador’s remark, “Unverifiable. New nodes joining the network cannot ascertain which block was published first.”

This remark is so misplaced and erroneous that it plainly reveals either a lack of comprehension of the proposal in its entirety or suggests conduct driven by ill intent. I have elucidated throughout the proposal and in my thorough responses to cursory comments that the winning block does not propagate until consensus is reached. The very purpose of intents and the grace period is to supplant the probabilistic race; thus, the assertion that one "cannot know which block was published first" is nonsensical in the context of PoW+PoT. PoT eliminates the attack vectors by replacing length-based races with an absolute, verifiable deadline and by incorporating appropriate deterministic conditions.

@Rucknium, I trust that my response clarifies all concerns presently raised. I should be most grateful if there exists a genuine interest in the scientific exploration of the PoT's technical feasibility and adaptability of Monero, and if such inquiries could henceforth be undertaken sincerely and constructively by those with the requisite expertise. Regrettably, such an approach has thus far been conspicuously lacking.


## tevador | 2025-10-09T16:12:47+00:00
> I trust that my response clarifies all concerns presently raised.

Unfortunately, no. You keep repeating arguments that have already been refuted.

> There is no block reorganisation. We are discussing intents - the block is neither forged nor propagated until a solution is agreed upon deterministically.

You can call it what you want, but the fact is that the withheld block B2 causes the honest miners to waste hashes on block B1 (and its child block attempts), which will eventually lose the race to block B2. The wasted hashes mean that the honest miners will be paid a lower portion of the block rewards than their portion of the network hashrate. I recommend reading some papers on selfish mining.

> Updates trigger only on ≥70% deviation [...]

What if >70% of the network nodes are malicious? You keep ignoring this case. It happened on the Monero network in 2020.

> Even if Sybils temporarily dominate a bubble (network segment), block timestamps embed the median-aligned chain_time, serving as a global reference for deadlines.

Even if you consider blocks to be PoW protected time references, the following attack is still possible:

1) The attacker skews the local time of some honest node.
2) The attacker submits a low-difficulty block that will be valid only in the local bubble (section 2.4).
3) The grace period elapses without a competing block being seen by the honest node.
4) The honest node is now permanently split from the canonical chain. It will never accept any canonical chain blocks because they will be considered "late".

> Local attackers are foreseeable, detectable, and isolatable without local or global harm.

I see no evidence for this claim.

>  Forged chains fail universally, as deadlines anchor to embedded timestamps (verifiable PoW artefacts from honest producers, Section 2.3). Each node runs the math offline. Quorum (70% consensus, >10% margin over local) selects the highest-scoring tip, tiebroken by height/progress. Honest majority prevails, affirming the recomputable canonical.

I don't see any evidence that "forged chains" fail any of the rules.

Imagine the following scenario: The Internet temporarily splits (e.g. as a result of an undersea cable failure). The two separated networks will each produce blocks that follow the local rules regarding timestamps etc. Both are valid alternate histories.

In Bitcoin, once the networks reconnect, everyone will instantly agree which chain to follow due to the longest chain rule.

In your proposal, the chains will stay split forever (or until a manual intervention).

Just like the netsplit case, an attacker can forge a completely valid alternate chain history (by "netsplitting themself").

> Standard bootstrap uses automated IBD, resolving 99%+ cases without intervention.

IBD in Bitcoin works 100% of the time thanks to the longest chain rule. Your proposal fails in the case of two competing chain histories. The new node won't be able to decide which chain history to follow.

> I am astounded by Tevador’s remark, “Unverifiable. New nodes joining the network cannot ascertain which block was published first.”
>
>This remark is so misplaced and erroneous that it plainly reveals either a lack of comprehension of the proposal in its entirety or suggests conduct driven by ill intent. I have elucidated throughout the proposal and in my thorough responses to cursory comments that the winning block does not propagate until consensus is reached. The very purpose of intents and the grace period is to supplant the probabilistic race; thus, the assertion that one "cannot know which block was published first" is nonsensical in the context of PoW+PoT. PoT eliminates the attack vectors by replacing length-based races with an absolute, verifiable deadline and by incorporating appropriate deterministic conditions.

In case you didn't understand: A new node joining the network in October 2025 cannot know which of the two equally valid competing chain histories from September 2025 was published first. Nodes that were present in September 2025 could have "reached consensus" which history was there first, but this consensus doesn't trustlessly transfer to new nodes joining the network. One of the alternate chains could be fabricated by an attacker and propagated by their sybil nodes. While this will not reorg nodes that are already fully synced, no new nodes will be able to complete IBD without a manual intervention.

## r-a-d-a-n-n-e | 2025-10-14T21:02:52+00:00
Just a quick note. @tevador, thanks for your response. I thought I would have my response ready by now, clarifying the details and concerns once and for all, but other priorities have taken precedence. I will follow up by the end of this week.

## r-a-d-a-n-n-e | 2025-10-17T11:48:11+00:00
Thanks for your response, @tevador.

I categorically disagree with your concerns, for none correspond to the truthful reality of Proof of Time. Still, the detail you provided is helpful - essential for constructive feedback. May my response inspire productive outcomes.

I must first reject your charge. Kindly refrain from claiming refuted points when your own superficial comments have sidestepped the facts, offering no reasonable rebuttal. I find it abhorrent to reason that a hasty dismissal should take priority over proper discussion and mutual understanding. The more you reveal of your thinking, the better I can assist.

## Selfish Mining
First, let us denominate properly. Intents are precursors (4.4), not blocks.

Even if the idea of selfish mining had any validity within the framework of PoW fortified by PoT, it is not comparable to what selfish mining entails in probabilistic PoW, where attackers can withhold not just one block but entire chains of them, orphaning honest efforts across multiple depths.

In the context of PoT and selfish mining, B1 is not a block. B2 is not a block. Both are intents comprising a hash, deadline, public key and signature, not the block itself. Referring to them as I1 and I2 is correct.

A valid intent receipt triggers a peer status change from "LIVE" to "GRACE". Once the honest peer miner receives this information, it stops hashing as their peer will reject its submissions. If such a miner and peer continue using hijacked protocols, it is folly.

No extensions to a putative I1 occur, and a withheld I2 is peremptorily rejected if tardy, on relay. A held-back I2, sent too late, is rejected by honest peers from the start because it does not meet the key condition that it must arrive at least 30 seconds before its deadline. There is no speed contest as we know it, but a strict temporal rule derived from honest PoW assets. Honest contributions waste nothing out of the ordinary.

If you, however, refer to the scenario of a B2 mined in private and published block right after the grace period, you have a reasonable point to a limited extent. What you are missing is that the grace period is a transparency mandate that collates the valid intents.

For instance, the selfish miner alters the code to reject incoming intents, isolates his own intent to prevent honest competition, and through sheer comparative luck produces a superior intent. Then, it declares itself the victor, forges a B2, and broadcasts the block.

Broadcast of an intent must occur before or during the grace period. Its secrecy violates not its quality but the mandate of transparent submission:

Honest nodes, receiving only I1, gather and confirm submissions as usual, selecting the I1 deadline as canonical. B2 arrives without any trace of its I2 deadline in the shared record, appearing as an unsupported claim. When nodes validate the block, if its deadline has no matching submission time from the grace window, it fails the mandate outright. B2 violated the grace requirement for timely disclosure.

Ergo, _"better"_ without timely disclosure means nothing. Withheld I(n) or B(n) is a loser, every single time. The purported "selfish mining" ploy in PoT is thus a mirage, a self-defeating isolation through ostracism.

## Sybil Attack
The worry that Proof of Time succumbs to a Sybil-induced skew on an honest node, resulting in the acceptance of low-difficulty bubble blocks and their ongoing isolation, is structurally impossible. Your example stems from a misunderstanding of the relative time dynamics and lacks consideration of the operator's sovereignty and associated responsibilities.

First, let's not conflate relative time and proof of time. The offset (relative time) is not the endogenous time - the timestamp of the block and the time of the solution is - the proof of time.

I will use your attack-steps scenario to elucidate how an honest peer defends forking:

> 1) "Attacker skews the local time of some honest node"

The skew will not easily occur due to PoT defaults, and it is conditionally unattainable. There are several defence layers in place.

### Operator's Sovereignty
1. For a skew to have even a negligible chance of occurring, the honest peer would first need to accept more than 70% malicious peers. No peers are included in the time offset sample unless they align on the same chain, share common block, and have the same height, with validated bidirectional reachability (both outbound and inbound connectivity checked regularly). Node operators would benefit from a visual indicator interface.

2. Monero node operators are already empowered with choice through daemon configuration options:

"--add-priority-node" and "--add-peer": honest peers communicate, diluting Sybil dominance in gossip.
"--in-peers" and "--out-peers": limits exposure to unsolicited fakes

A good addition would be "--get-more-peers" and "--max-connections" options.

These options collectively empower operators to curate a resilient topology, where the chain_time samples draw from operator-chosen reliables, not Sybil swarms.

3. The previously mentioned peer quality/ranking model can take this to another level, especially in terms of empowering node operators with a choice, or, if you will, automating it. Peers are not equal.

NB: The above provisions are prudent, defensive and recommended, especially for high-risk peers such as an exchange, but not vital in defence against a Sybil attack. The offset is a relative time (not proof of time) that imposes the n-body problem onto the attackers, which to date has not been solved by foremost physicists.

### Relative Time
The n-body problem is a foundational conundrum in celestial mechanics and chaos theory. It extends the 3-body challenge to any number of gravitational bodies, rendering analytical prediction of their orbits all but impossible. While two bodies afford stable, exact solutions like ellipses, three or more unleash chaotic feedback. Initial variations cascade into divergent, unforeseeable paths.

In Proof of Time, this chaos analogy demolishes Sybil attacks on local chain_time skews, recasting the attacker as a deluded orbital conductor. Flooding an honest node (A) with deviant reports might nudge its clock, but A propagates offsets to peers B and C via gossip, where each recalibrates medians from partial views to global convergence of n-bodies. B loops back to A and C, C to A and B, birthing an n-body nightmare across 2-3+ hops. Sustained, fork-worthy skews demand prescient mastery of this intractability. PoT thrives in this chaos - a Sybil attack is utterly infeasible amid P2P delays and operator-weighted peers.

Imagine this scenario: your node has 10 honest peers. It needs to accept, bidirectionally connect and maintain the connection with an additional 24 Sybil peers to incur ≈ 70.6% of them. They may attempt to bypass the n-body problem by hijacking the relative time with a custom offset formula, in vain.

Their flood is clearly predictable and detectable because their bulk of relative time is misaligned. It is distinctly anomalous. Why on Earth would you accept it? You would not. You would notice their offset is far off from your time and the time of your honest peers. You would process the Sybils' reports through binned mode to align with honest medians, discounting their anomalies as noise. Should they persist, you will blacklist them, forcing them to fork off into irrelevance, and you may acquire new peers if required. You continue neglecting this vital piece of information, hence the rehashing.

The Sybils would have to bide their time patiently, over a prolonged period. It would require gradually tweaking the clocks by ramping up the weight in bubbles. But to what end? If they pulled it off, and suppose in the most extreme scenario they shifted everyone's clock using 90% of fake nodes reporting a time one minute out, while the 10% of honest nodes stayed true, then all the decent nodes would adjust by that one minute too. Splendid achievement, the show goes on. The same rules still apply. Nothing changes because there is no "real" time. It is irrelevant if the network thinks it is 2040. Who gives a damn?

> 2) "Attacker submits a low-difficulty block valid only in the local bubble" 
> 3) Grace period elapses without a competing block seen by the honest node:
> 4) Honest node permanently splits from the canonical chain, rejecting it as "late"
> I see no evidence for this claim.

Your peer just stopped the "attack" before any of the above could happen. If you do not trust or feel confident in the basics of n-body defence combined with flood detection, I would strongly advise strengthening the defences with the peer ranking model. There's worry solved.

## Longest chain antithesis

> The Internet temporarily splits (e.g. as a result of an undersea cable failure). The two separated networks will each produce blocks that follow the local rules regarding timestamps etc. Both are valid alternate histories.
> 
> In Bitcoin, once the networks reconnect, everyone will instantly agree which chain to follow due to the longest chain rule.
> 
> In your proposal, the chains will stay split forever (or until a manual intervention). Just like the netsplit case, an attacker can forge a completely valid alternate chain history (by "netsplitting themself").

First, an attacker's self-netsplit forges no valid alternate chain. Private blocks lack gossiped intents and violate the transparency mandate upon audit, as I explained above. It serves a dual defence in relation to selfish mining and netsplits. Such blocks are rejected outright by canonical peers, isolating the attackers.

Once the chain is alternate, your peer cannot "see" its best block. If the block heights and IDs of two chains diverge, they represent different chains that are irrelevant to each other. This divergence does not qualify as "valid" within the context of a single chain. It is simply "valid" in a broader sense akin to two separate entities.

The assertion that a temporary Internet disruption from an undersea cable failure would generate a chain divergence in PoT, with separated networks producing "alternate histories", is somewhat valid (two separate entities), but theoretical and extreme. It ignores a high degree of Internet redundancy, equipped with automatic rerouting protocols and assumes cable cuts may cause regional isolation when they do not.

There are undersea cables (20 transatlantic routes, ~50+ Asia-Europe, ~30 transpacific) and intracontinental cables (100 in Europe (e.g., Baltic Sea loops), ~80 in Asia (e.g., South China Sea), ~40 in Africa (e.g., West Coast to Europe), and ~50 in the Americas (e.g., US to South America), plus satellite connections, and counting.

Monero has thousands of nodes spread across the globe, using a wide range of connections. A cable cut typically only affects latency and does not stop the propagation of information. So long as a node in the affected region can still connect beyond the region via any route, it will relay/receive information to/from other nodes within its reach. The latency is not relevant.

For example, the probability of North America experiencing seclusion from other continents due to submarine cable failures is vanishingly small for simultaneous failure of all ~20 transatlantic cables in a single day (assuming an average annual fault rate of 0.33 per cable from global data, yielding a daily probability of ~0.0009 per cable, and independent failures).

`P(all 20 cables fail in one day) = (0.33 / 365)^20 ≈ 1.22 × 10^{-61}`

This calculation comprises key variables: cable count (20 active transatlantic routes as of 2025), failure rates (200 global faults/year across 597 cables), redundancy (multiple routes with automatic rerouting via excess capacity or dark fibre), satellite backups, and alternative paths (via South America, Asia-Pacific, or overland Canada/Alaska links). The ratio of seclusion probability to connectivity probability reflects near-certain resilience even under worst-case cuts, as no historical incident has caused intercontinental isolation.

Support comes from the paper "Submarine Cables and Internet Resiliency" by Yoshio Tanaka (Internet Initiative Japan, 2018), which analyses outage probabilities and redundancy.

Excerpt: "Once this cable was damaged, certain traffic had to be rerouted via longer alternative routes, resulting in increased latency... We see that RTTs more than tripled, from 97ms to over 320ms. This latency spike continued for days after the cable break, as repairs to submarine cables can take weeks."
[https://www.iij.ad.jp/en/dev/iir/pdf/iir_vol41_focus2_EN.pdf](https://www.iij.ad.jp/en/dev/iir/pdf/iir_vol41_focus2_EN.pdf)

The paper emphasises that while cuts cause temporary latency spikes, the mesh structure and rerouting guarantee no full outages in well-connected regions, with models indicating that cables achieve 99% availability despite an average of over nine outage days per annum.

If an exchange is in a hypothetical isolated region, then it is its responsibility to halt deposits and withdrawals. That is not different from the longest chain rule.

Your argument draws on a non-affecting scenario that might occur with a daily probability of ~0.0009 failures per cable - it vastly overstates the risk. The chances that an unknown asteroid might hit Earth are far greater than the chances of global internet fragmentation.

The annual probability of a significant asteroid hitting Earth is approximately 1 in 10,000 (10^{-4}), per NASA estimates for near-Earth objects.

For daily P, this translates to ~2.74 × 10^{-7}. Compared to the cable seclusion P (1.22 × 10^{-61}), the asteroid impact is ~10^{54} times more likely.

Maybe you need an asteroid-resistant planetary shield encompassing low orbit, Monero-dedicated satellites guaranteeing 100% uptime, and a series of ion cannons to defend against potential alien attacks.

On a serious note, the concern regarding netsplits in PoT, separated segments producing divergent blocks, leading to permanent splits upon reconnection, highlights nothing but transitional challenges during rare disruptions, and it exposes the longest chain rule's antithesis:

The longest chain flaw invites 51% attacks, reorgs, and selfish mining, solvable only by escalating hash wars that require city-scale power to "defend" and that governments or corporations can outmuscle at will. They can alter the history of 1000s blocks easily and laugh, but we cannot defend against that. And there is no reason we should have to. Their server farms are useless against PoW+PoT.

Protecting Monero should be the primary objective, so we do not get rick'rolled by a government, or a corporation, or a malicious entity with our pants down, unable to fight back because we are small and poor.

PoT ditches this "dumb" longest chain rule - there can be only one canonical chain called Monero. Instead, you need to empower peers with choice. No forks are protocol-intended. Nor resolved by "better chain seen". You stay on "your divergent chain" unless manual intervention - correct.

Sharing the same block height and the last common block indicates that the chains are the same. If common block diverges, it is a different chain altogether and irrelevant to yours.

For instance, if peer A is at height 9999, and peers B and C are both at height 10000, but C has a different block ID than B, they all share common top block at height 9999.

How do A and B know to take B's block (canonical) but not C's (divergent)? Who is to say C is divergent? **The node operator is sovereign and must make that decision.** It is like the BCH fork from BTC. If you already peer with C, accepting their blocks means aligning with them. Up until 9999, you peer with all. Receiving B's block makes C divergent; receiving C's makes B divergent. Since you entered this scenario with **YOUR** peers, you now have a choice between two chains. In this extreme case, you need to decide which chain to follow. Forks are removed from the base protocol and are not common unless they are malicious or intentionally created.

For a recovery scenario encountering two "Monero" chains, the action processes the request from one peer and the data provided by the other. If valid, one takes it. It is a choice, but good luck sustaining a rogue chain without exchanges, the dev team, and tier-1 (community-enforced) peers.

### How do PoW+PoT vs PoW with the longest chain rule compare?
The longest chain rule exposes Monero to reorgs, selfish mining, and 51% attacks, costing millions to billions in trust. PoW+PoT eliminates all attack vectors through the discussed deterministic security and operator interfaces.

The longest chain rule centralises on hash power (pools dominate, vulnerable to adversary capture). PoW+PoT protocol decentralises hash power. The security relies on the deterministic protocol rather than on the dependency on hash power. More hash power leads to more blocks won, but it cannot change historical records and is unbreakable without the need to engage in foolish hash wars.

The longest chain rule resolves netsplits probabilistically (risking theft during delays); The PoT proposed recovery mechanism can auto-resolve shallow divergences. Rare deep divergences can be left to the choice of the sovereign operator instead. Your assertion that _"the chains will stay split forever"_ is unreasonably overdramatic. We can manage our nodes, thank you very much. Equip us with the right tools. The last thing we need is to keep experiencing protocol-level enforced ill-willed roulette.

The longest chain rule poses risks of rug pulls that undermine confidence. In contrast, PoW+PoT instant finality signifies trust, and manual intervention in critical situations is preferable. This approach gives the operator the ability to make decisions rather than relying on the unpredictable nature of the longest chain rule, which can undergo 1000s of block reorganisations at any moment without anyone being able to foresee, let alone defend, such events. How is that even remotely acceptable?

Your deep recovery solution? Contrary to Section 4.2, no large quorum is needed. Instead, empower operators with a choice to sync recover to a select peer.

Add a default native and web GUI, plus a notification system. 

Great start - [https://github.com/everoddandeven/monerod-gui](https://github.com/everoddandeven/monerod-gui)

Upgrade it with a curated list of Tier 1 peers ranked by quality, updated in regular intervals, along with sync-recovery features.

## IBD with Proof of Time
Monero daemon uses default DNS seed nodes for initial peer discovery and bootstrap on the mainnet over Clearnet. I find this level of centralisation paradoxical in correlation with the longest chain fervour and IBD.

Your concern that a new node with Proof of Time cannot decide which chain history to follow in the presence of competing histories overlooks the deterministic validation and ignores how Monero's hardcoded seed nodes utilise DNS-resolvers. Even without hardcoded resolves, there always has to be a seed peer.

How, then, could indecision arise when the seeds anchor themselves to the dominant history? In other words, in PoT, the seed peer or any other nth-level connected peer cannot relay a peer that is not part of the canonical chain. Hence, this annuls your IBD premise.

A more decentralised solution would empower the node operators with a public list of top seed Clearnet peers ranked by quality. Since PoT transforms PoW into a deterministic fortress vulnerable only to a global cataclysm, add a "Days of PoW with instant finality" counter for the fancy — it will look truly amazing in a few years or so.

## Thought-provoking bonus: Multisig Brick'n'Roll
For a protocol-changing upgrade, we can introduce a new version-brick feature at a specific block height. This approach is a responsible method as exchanges, merchants, and all operators alike will be notified immediately, and will be unable to process deposits or withdrawals if their nodes become "bricked," requiring them to upgrade to the new version.

In case anyone would say, "That's centralisation!" Please. Stop. Monero is centralised in its development, as is any other network, regardless of what anyone claims, and pretending otherwise is misguided or disingenuous. The multisig brick feature is a proper way to deploy hard forks, helping us avoid the hard-fork dramas.

## 
To wrap this up, I clarified the concept of Proof of Time for you and the audience while addressing all your concerns. If you would like to explore any specific details further, ask, and I will follow up.

So, when do we proceed with making Monero awesome?

## SamsungGalaxyPlayer | 2025-10-17T14:22:51+00:00
This proposal seems to boil down to a requirement that nodes only connect to other nodes that they trust. And nodes syncing the network for the first time need to find a peer that they trust as well. This is much less resilient than the current Nakamoto consensus (and it is a substantial centralizing pressure); in Monero consensus today, a node only needs to find one trustworthy peer (and it always knows who is the most trustworthy, even without knowing anything about the node operator's identity).

A node in your model that doesn't carefully curate their nodes runs at risk of connecting to primarily "garbage" peers and being convinced of a malicious network state. Attempting to filter out these garbage peers would rely on non-verifiable decisions. Non-verifiable decisions run the risk of splitting the network.

Requiring node operators to carefully and manually curate the nodes that they connect to (e.g. through the UI that you recommend above) isn't an acceptable requirement for Monero's consensus. And no, this is not the case currently. You may set a priority peer, but if that peer sends your node incorrect data, it will instead trust the more trustworthy information from the other nodes.

Your equivalency comparison to seed nodes isn't correct. Monero nodes can today connect to even one more node in conjunction, to learn of bad data from a seed node. While a malicious seed node is certainly worrisome, it doesn't lead to as bad consequences as would occur in a similar catastrophic case with your proposal. In Monero's case today, seed nodes only serve _one_ purpose: to be a convenient initial connection point to the network. If that fails, any single honest node can serve the same function. And if there's ever a dispute between two nodes, those two nodes can compare consensus state and immediately, verifiably know which of the two is correct.

Nodes need to come to consensus to form a robust network, and assuming node "sovereignty" with each node picking different rules runs conflict to that. To state the obvious, of two nodes pick different, "sovereign" answers, there are two different networks.

> PoW+PoT eliminates all attack vectors through the discussed deterministic security and operator interfaces.

This wide-reaching claim is clearly false. "Deterministic" is in direct opposition to your point about nodes needing to make their own decisions as sovereign individuals.

## tevador | 2025-10-17T19:45:45+00:00
## Selfish Mining

Propagating "precursors" doesn't change anything. The attacker will still withhold and broadcast the winning "intent" I2 after I1 is found by the honest network. In the meantime, the attacker is already working on the next block (with prev_id set to the hash of the wothheld block B2).

Note that the winning intent I2 is broadcast during the grace period, so it's valid. So you can stop repeating that late intents are rejected.

> A valid intent receipt triggers a peer status change from "LIVE" to "GRACE". Once the honest peer miner receives this information, it stops hashing [...]

Nobody will stop hashing because it's not a Nash equilibrium. If miners are supposed to stop hashing during the grace period, any non-compliant miner will increase their chances of winning the next block by breaking this rule (because they will have an extra 30 seconds of hashing).

So in the end, honest miners will waste hashes on I1 and its child block attempts, while the attacker gets to privately mine on top of their winning I2. Classic selfish mining.

## Sybil Attack

> For a skew to have even a negligible chance of occurring, the honest peer would first need to accept more than 70% malicious peers. No peers are included in the time offset sample unless they align on the same chain, share common block, and have the same height, with validated bidirectional reachability (both outbound and inbound connectivity checked regularly).

Sybil nodes will easily meet all these requirements.

> These options collectively empower operators to curate a resilient topology, where the chain_time samples draw from operator-chosen reliables, not Sybil swarms.

So essentially, everyone should only connect to their friends. How is that supposed to be a global network? This will only increase the chance of users being partitioned into a separate network.

> Imagine this scenario: your node has 10 honest peers. It needs to accept, bidirectionally connect and maintain the connection with an additional 24 Sybil peers to incur ≈ 70.6% of them. They may attempt to bypass the n-body problem by hijacking the relative time with a custom offset formula, in vain.

This scenario is irrelevant.

A much more common scenario will be:

Your node comes online (e.g. after a week of being offline) and connects to 10 peers. 7 of those 10 peers have local time 1 year in the future. Does the node accept this offset or not?

If not, why is `ms_adjust` even in the specification?

If yes, then time skew is possible.

## Netsplit

Your wall of text doesn't change the fact that your proposal implicitly assumes that network splits don't occur. Nakamoto consensus works even with netsplits, so your proposal is strictly worse in this aspect.

> It ignores a high degree of Internet redundancy, equipped with automatic rerouting protocols and assumes cable cuts may cause regional isolation when they do not.

It's irrelevant how resilient you think the internet is.

Several countries have publicly demonstrated their ability to disconnect from the global internet, for example [China](https://www.theregister.com/2025/08/21/china_port_443_block_outage/) and [Russia](https://www.businessinsider.com/russia-tested-cutting-off-internet-access-report-kremlin-runet-2024-12). Any coin using your protocol can be killed in those countries with a simple flip of a switch that disconnects them from the internet for 1 hour in the middle of the night.

> Your concern that a new node with Proof of Time cannot decide which chain history to follow in the presence of competing histories overlooks the deterministic validation and ignores how Monero's hardcoded seed nodes utilise DNS-resolvers. Even without hardcoded resolves, there always has to be a seed peer.

Yes, Monero has seed peers (both DNS and IP based ones). But those peers don't determine which chain is valid. They just give you a list of peers to connect to.

> How, then, could indecision arise when the seeds anchor themselves to the dominant history? In other words, in PoT, the seed peer or any other nth-level connected peer cannot relay a peer that is not part of the canonical chain. Hence, this annuls your IBD premise.

So essentially, in your protocol, the "correct" chain is determined by the developer running the seed node hardcoded in the code. I would call this consensus mechanism Proof of Seed Node (PoSN). It has nothing to do with Proof of Work.

> A more decentralised solution would empower the node operators with a public list of top seed Clearnet peers ranked by quality.

That's a different one, Proof of Peer List (PoPL). Again, has nothing to do with Proof of Work. The developer decides who gets to be on the list. If you add any kind of peer voting to this, the attacker will easily win with >70% of sybil peers.

---

> To wrap this up, I clarified the concept of Proof of Time for you and the audience while addressing all your concerns. If you would like to explore any specific details further, ask, and I will follow up.

So far you are failing to defend your proposal against several flaws mentioned above.

AFAIK, there is nobody in the Monero Research Lab or Monero development teams who wants to implement your proposal, but you are always free to fork Monero yourself.

## r-a-d-a-n-n-e | 2025-10-17T21:46:22+00:00

I am delighted to conclude that you lot are plagued by cognitive dissonance and can scarcely grapple with systemic issues unless someone else writes a comprehensive paper, spelling out every facet you yourselves could not puzzle through. Let those 16-year-old shortcomings stand as testament to this.

Make no mistake. I did not come here to defend my proposal. I made that plain in the blueprint and in my previous reply. Nor do I possess the time or inclination to lead you by the hand. My purpose was to ascertain whether any sharp minds might step forward to pursue the exploration and research for which I have offered a bounty and assistance. What you are about here does not qualify.

Thus, I shall bring this tiresome charade to a swift end.

1) No, the selfish mining is not feasible. You are deliberately spouting drivel, neglecting the temporal rules I explained in detail.
2) Yes, such a local screw is possible, but would be temporary and inconsequential, particularly in the scenario you mentioned, and all the more so amid the further nuances you have overlooked, likely beyond the reach of your imaginative capacity.
3) No, the peers are not trusted friends - you cannot even read, much less reason, beyond the confines of your narrow worldview.
4) No, the correct chain is not determined by the developer. Never heard of PoPL - that is not what I advised. All that a disconnection means is that the nodes will reconcile or sync recover upon reconnection. Far preferable to all the attack vectors you uphold.

Your responses twist the essence of this proposal, lack any consideration of nuances, and I shall waste no more time on this.

If you don’t believe it or don’t get it, I don’t have the time to try to convince you, sorry.

That NPC's retort is a figment of delusion and merits no response.

God save Monero.

## r-a-d-a-n-n-e | 2025-10-18T11:24:27+00:00
I shall grant one final endeavour to bring you lot to your senses, given the ongoing discourse on X, which even those bereft of technical acumen can grasp. It is indeed strange that you cannot.

The longest chain rule has become your creed. A sacrosanct house of cards, precarious and inviolable. Hallowed be the Satoshi.

It solves the problem of keeping the network in line, as it was partially correctly pointed out by Tevador - it resolves the extreme cases.

But does it truly? Suppose China were to sever their Internet for an entire month. They muster 51% of hashpower and forge the longest chain in seclusion. This they could accomplish with Bitcoin, Monero, or any such network, with scant effort.

Then, they unleash 2.3k blocks at once. Under the longest chain rule, the whole world would revert to the Chinese ledger, erasing a month's ledger of history, rewards, transactions, you name it. This is the danger that you defend so passionately.

With PoT, such a calamity would be averted. China would, in effect, spawn their own Monero CH, yet this would not affect the rest of us. Alright then. If that is their fancy, so be it. Individual operators in China could still elect to resynchronise with the global Monero chain once isolation ends.

This proposal warrants no further debate. You have been furnished with ample particulars to render it operational.

## tevador | 2025-10-18T11:59:27+00:00
> No, the selfish mining is not feasible. You are deliberately spouting drivel, neglecting the temporal rules I explained in detail.

Despite your denial, your proposal is vulnerable to selfish mining and there is no way to fix that because it relies on instant finality. Using deterministic tie breaking instead of smaller hash tie breaking would make selfish mining less profitable, but would not eliminate it.

> Yes, such a local screw is possible, but would be temporary and inconsequential, particularly in the scenario you mentioned, and all the more so amid the further nuances you have overlooked, likely beyond the reach of your imaginative capacity.

You can't say it's inconsequential because a local time skew together with section 2.4 (maximum block time) clearly imply that sybil attacked nodes can get permanently split from the main chain.

> No, the peers are not trusted friends

You wrote (exact quote): "These options collectively empower operators to curate a resilient topology, where the chain_time samples draw from operator-chosen reliables, not Sybil swarms.".

In other words, your protocol requires each node operator to manually select trusted nodes to connect to in order to avoid sybil attacks.

> No, the correct chain is not determined by the developer.

Yes, it is. You wrote (exact quote): "How, then, could indecision arise when the seeds anchor themselves to the dominant history?"

In other words, any node starting IBD will always select the chain history presented by the seed node, even if there are multiple equally valid histories to choose from. A malicious seed node can feed arbitrary chain histories to new nodes joining the network.

> Suppose China were to sever their Internet for an entire month. They muster 51% of hashpower and forge the longest chain in seclusion. This they could accomplish with Bitcoin, Monero, or any such network, with scant effort.
>
> Then, they unleash 2.3k blocks at once. Under the longest chain rule, the whole world would revert to the Chinese ledger, erasing a month's ledger of history, rewards, transactions, you name it. This is the danger that you defend so passionately.

A whole country disconnecting for 1 month is far too long not to be noticed. If they had enough hashrate for a 51% attack, they can do that easily without disconnecting the whole internet. Your scenario is completely unrealistic.

On the other hand, my scenario is much more plausible, e.g. China disconnected from the global internet for 1 hour in August 2025. Your protocol would create 2 irreconcilable chains in this case.

> This proposal warrants no further debate.

I agree. The issue can be closed.

# Action History
- Created by: r-a-d-a-n-n-e | 2025-10-01T18:38:47+00:00
