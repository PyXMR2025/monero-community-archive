---
title: Transactions remain in pool for up to several minutes while blocks are mined
source_url: https://github.com/monero-project/monero/issues/6951
author: woodser
assignees: []
labels: []
created_at: '2020-10-30T18:33:38+00:00'
updated_at: '2021-03-17T00:50:59+00:00'
type: issue
status: closed
closed_at: '2021-03-17T00:50:59+00:00'
---

# Original Description
Transactions can remain in the pool for up to several minutes while mining blocks on a local stagenet network whereas they should confirm in the next available block?

# Discussion History
## vtnerd | 2020-10-30T19:22:53+00:00
Transactions in the "stem" phase are excluded from mining, to prevent potential leaking of the stem path. The Dandelion++ paper doesn't mention what to do in this case; this was a decision made during development.

There is a [related issue](https://github.com/monero-project/monero/issues/6929) about transactions being "stuck" in the local mempool and not distributed widely. Based on your description its not clear whether the transaction was sent correctly yet still waiting for the Dandelion++ "embargo timer", or whether it triggered this other issue. `set_log +net.p2p.tx:DEBUG` will print messages specific to transaction relaying.

## moneromooo-monero | 2021-01-09T01:42:26+00:00
Should be better now. It can still happen if you relay to a peer that drops the tx on the floor though.

# Action History
- Created by: woodser | 2020-10-30T18:33:38+00:00
- Closed at: 2021-03-17T00:50:59+00:00
