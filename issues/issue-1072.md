---
title: Rx dataset not reinitialized when seed_hash change
source_url: https://github.com/xmrig/xmrig/issues/1072
author: minerrocks
assignees: []
labels:
- bug
created_at: '2019-07-24T22:46:24+00:00'
updated_at: '2019-07-28T09:57:13+00:00'
type: issue
status: closed
closed_at: '2019-07-28T09:57:13+00:00'
---

# Original Description
https://github.com/xmrig/xmrig/blob/02c03b0465e34b1430c440d095d1299e5709bd91/src/backend/cpu/CpuWorker.cpp#L82-L88


Rx dataset not reinitialized when seed_hash change.
Noticed when seed hash changed for loki at block 361600, and hashrate dropped on all pools.
Xmrig should check if seed hash changed and reinitialize rx dataset.
Right now only restart of xmrig helps.

# Discussion History
## xmrig | 2019-07-25T00:25:12+00:00
v2.99.1-beta released https://github.com/xmrig/xmrig/releases/tag/v2.99.1-beta
Thank you.

# Action History
- Created by: minerrocks | 2019-07-24T22:46:24+00:00
- Closed at: 2019-07-28T09:57:13+00:00
