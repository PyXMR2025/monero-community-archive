---
title: Protects your miner from pools that grow too large or mine dishonestly
source_url: https://github.com/monero-project/research-lab/issues/157
author: tnzxpool
assignees: []
labels: []
created_at: '2026-04-18T16:14:04+00:00'
updated_at: '2026-04-18T16:14:04+00:00'
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
# Action History
- Created by: tnzxpool | 2026-04-18T16:14:04+00:00
