---
title: Node behind, failing to sync after reorg
source_url: https://github.com/seraphis-migration/monero/issues/379
author: Torir2035
assignees: []
labels: []
created_at: '2026-05-13T01:20:11+00:00'
updated_at: '2026-05-13T03:04:21+00:00'
type: issue
status: closed
closed_at: '2026-05-13T03:04:21+00:00'
---

# Original Description
Symptoms: node stuck at height 3001516. A brief look at the logs suggest it is disconnecting from peers while trying to download large packets.
[bitmonero-fcmp-testnet.log.gz](https://github.com/user-attachments/files/27678182/bitmonero-fcmp-testnet.log.gz)

```
Remote Host                        Peer_ID   State   Prune_Seed          Height  DL kB/s, Queued Blocks / MB
83.99.142.174:28080       b3018692c8f0ea65  normal            186       2492671  0 kB/s, 0 blocks / 0 MB queued
88.99.195.15:28282        04fc953da6349919  normal            183       3001176  0 kB/s, 0 blocks / 0 MB queued
83.205.173.85:28080       c45ad0611a6109e2  synchronizing     0         3001535  11 kB/s, 2 blocks / 0 MB queued
50.27.93.192:28080        2d60196022746306  synchronizing     0         3001535  10 kB/s, 2 blocks / 0 MB queued
146.60.103.153:28080      3dba90d73ee32545  synchronizing     187       3001535  10 kB/s, 2 blocks / 0 MB queued
8 spans, 11.5674 MB
[.o..o...]
83.205.173.85:28080       1/184 (3001516 - 3001516)  -
50.27.93.192:28080        1/184 (3001517 - 3001517, 5755 kB)  268 kB/s (1)
50.27.93.192:28080        1/184 (3001518 - 3001518)  -
146.60.103.153:28080      1/184 (3001519 - 3001519)  -
194.58.47.153:28080       1/184 (3001520 - 3001520, 5811 kB)  250 kB/s (0.93)
83.205.173.85:28080       1/184 (3001521 - 3001521)  -
146.60.103.153:28080      1/184 (3001522 - 3001522)  -
50.27.93.192:28080        1/184 (3001523 - 3001523)  -

```

# Discussion History
## Torir2035 | 2026-05-13T02:25:39+00:00
Update: The node was stuck on a 25kB/s connection. I moved the node to a connection with a faster speed and it was able to catch up to the network.

## Torir2035 | 2026-05-13T03:04:21+00:00
Closing since this was an issue with the node's bandwidth. The node was functioning as designed and blocking nodes that were giving it slow downloads.

# Action History
- Created by: Torir2035 | 2026-05-13T01:20:11+00:00
- Closed at: 2026-05-13T03:04:21+00:00
