---
title: Higher ban frequency
source_url: https://github.com/seraphis-migration/monero/issues/373
author: j-berman
assignees: []
labels: []
created_at: '2026-05-12T20:28:47+00:00'
updated_at: '2026-05-13T01:26:56+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Some people are noting their nodes are banning peers in higher frequency.

u/Torir says:

> Seeing messages like "Peer d0b4219a13d44d658b8065a2e8cefbd5 has missed 129 out of 170 total requests (75%)"

Missing requests may imply the peer is behind other nodes, or that the peer is kicking txs from the pool after notifying of the hash but before receiving the request for the tx. The latter is possible when the pool is at capacity and consistently receiving new txs as seems to the case on beta stressnet.

#372 also described a way in which nodes might be getting banned from re-relaying reorged out invalid txs.

Logs showing the definitive cause of these bans would help narrow down the issue.

# Discussion History
## j-berman | 2026-05-12T22:12:04+00:00
Note: when merging master [into the `fcmp++-beta-stressnet` branch](https://github.com/seraphis-migration/monero/commit/61ded9f6d250b5b8492b29e6bed81408c8947f13), I accidentally removed a mutex used in tx relay v2 to prevent bans when resolving conflicts. I added it back [here](https://github.com/seraphis-migration/monero/commit/d3a1af23182bdb1207d58c7e987e2f421be4e521). ~~`fcmp++-stage` had the same issue and I added it back [here](https://github.com/seraphis-migration/monero/commit/3ca7cc6cae1faf57f18ccf8865bf1580e4c7e7a7)~~ (EDIT: `fcmp++-stage` did not in fact have the same issue, @jeffro256 correctly kept the lock on rebase).

v1.1 [didn't have this issue](https://github.com/seraphis-migration/monero/blob/v0.19.0.0-beta.1.1/src/cryptonote_protocol/cryptonote_protocol_handler.inl#L1015), and @selsta reported experiencing bans with v1.1. So the issue remains open.

Still seeking definitive cause of the bans.

## selsta | 2026-05-12T22:13:36+00:00
To clarify, I did not see super frequent bans but like 3 overall. It's possible these were nodes that were overloaded and didn't reply correctly.

## nahuhh | 2026-05-12T23:33:40+00:00
When i saw bans while performing reorgs, i think it was caused by a timeout downloading the subsequent span _while_ the node was busy syncing the prior one

# Action History
- Created by: j-berman | 2026-05-12T20:28:47+00:00
