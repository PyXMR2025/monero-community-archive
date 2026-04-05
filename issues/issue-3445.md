---
title: Add support for Scash
source_url: https://github.com/xmrig/xmrig/issues/3445
author: bitcartel
assignees: []
labels: []
created_at: '2024-03-15T04:43:06+00:00'
updated_at: '2025-06-16T19:53:15+00:00'
type: issue
status: closed
closed_at: '2025-06-16T19:53:15+00:00'
---

# Original Description
Scash is a newly launched network: https://s.cash , https://twitter.com/scashnetwork

There is currently no mining pool support, so would be great if Xmrig could add support. Miners discord channel: https://discord.com/invite/T4Jcw2c95V

PoW being used is RandomX v1.2.1 with commitments, where the commitment value must meet the block target. Details are in protocol spec here: https://github.com/scash-project/sips/blob/main/scash-protocol-spec.md

There is a cpuminer available here: https://github.com/scash-project/cpuminer-scash/

If needed, available to help implement and test. Thanks!

# Discussion History
## bitcartel | 2024-04-08T17:21:42+00:00
There is a closed source miner called SRBMiner (fork of Xmrig?) which has now added support for mining Scash to a pool.

https://github.com/doktor83/SRBMiner-Multi/releases/tag/2.5.2

It would be great if Xmrig could add support too, so users have an open source miner to run.

# Action History
- Created by: bitcartel | 2024-03-15T04:43:06+00:00
- Closed at: 2025-06-16T19:53:15+00:00
