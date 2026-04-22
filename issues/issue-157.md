---
title: Protects your miner from pools that grow too large or mine dishonestly
source_url: https://github.com/monero-project/research-lab/issues/157
author: tnzxpool
assignees: []
labels: []
created_at: '2026-04-18T16:14:04+00:00'
updated_at: '2026-04-20T11:39:05+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Hi All,
Please preserve the protocol!
I followed kowalabearhugs's suggestion and browsed the threads, including this one. I delved into even the most fascinating solutions, and I understood the dilemma and this thirst for solution.
I thought, from a miner's point of view, what the problem was...

"They're robbing me, they're breaking the Monero chain... what can I do?"
And I did this:  https://github.com/xmrigger/xmrigger
Concept: https://xmrigger.github.io/xmrigger-proxy/demo.html
(I haven't tested the federation live because I'm honestly short on hardware resources.)
It's a concept I currently use for other things as well, and it opens up large WSS connections, used to work with the proxy, with differentiated buckets and channels available to developers.

Sometimes could be better to leave, because the pool is in danger of a high hashrate, which interrupts mining and diverts it.
I also thought that the pool itself, any one of them, could automatically limit its own access or hashrate, adopting the criterion and dropping the last connected ones so as not to enter the danger zone and suddenly lose all the miners... that's a nice punishment.

Tnzx

# Discussion History
## tnzxpool | 2026-04-20T11:39:05+00:00
Cross-referencing the prior discussions for context (should have been in the original post). The research-lab proposals on selfish mining mitigation form a stack of defenses at different layers:

* #140 (Detective Mining, Lee & Kim 2019 — https://eprint.iacr.org/2019/486) filed by fluffypony — pool layer. The paper's core observation — that pools must leak their private tip via `prevhash` in Stratum jobs — is what this implementation relies on as well. The difference is in the response: #140 proposes active counter-template construction at the pool; this implementation does passive detection at the proxy with evacuation to a fallback pool. It's a lighter subset of the same paper, working without pool cooperation.
* #144 (Publish or Perish) and #146 (Share or Perish) by tevador — consensus layer. #144 introduces uncle blocks + lateness-based fork choice. #146 refines this with workshares instead of uncles, making long reorgs effectively infeasible for α=0.33 attackers. Both require consensus adoption.
* #141 (closed) by venture-life — earlier proposal for stratum-level deterministic tie-breaking + reward splitting on orphans. Referenced by #144 as the origin of the reward-splitting intuition.
* #136 — broader context on PoW centralization.

The layers compose rather than compete: an xmrigger user benefits from #140's deployment at their pool, and from #144/#146 being adopted at consensus. The contribution here is deployability at the individual miner level, while the larger proposals mature.

**On parameter choices — where I'd welcome feedback:**

The defaults are calibrated empirically rather than derived, and several are genuinely debatable:

* **Hashrate concentration threshold.** Initially set closer to the Eyal–Sirer theoretical bound (~30%), but raised to 43% after cross-checking against observed hashrate shares of legitimate large pools, which routinely operate well above 30%. A 30% trigger would cause evacuations from honest pools. 43% reflects the operational threshold commonly used when discussing pool concentration risk, but it could still be tuned.
* **Divergence time window (20s).** Chosen as a multiple of observed block propagation delay (1–2s) with margin. It's a coarse heuristic: a multi-block selfish-mine race on Monero's 120s block time is well over 20s, so the guard would trigger on sustained forks — but shorter events may not. I'm unsure what the right calibration is, and it likely depends on empirical data from the actual selfish-mining incidents.
* **Grace period and poll interval.** Same character — defensible defaults, not derived from first principles.

If anyone has thoughts on more principled defaults, or on empirical traces from the recent selfish-mining incidents that could inform them, that would be particularly useful.

# Action History
- Created by: tnzxpool | 2026-04-18T16:14:04+00:00
