---
title: '[ALPHA] Testnet stuck syncing'
source_url: https://github.com/seraphis-migration/monero/issues/313
author: ComputeryPony
assignees: []
labels: []
created_at: '2026-04-10T19:46:51+00:00'
updated_at: '2026-04-10T20:57:12+00:00'
type: issue
status: closed
closed_at: '2026-04-10T20:57:12+00:00'
---

# Original Description
I run a alpha testnet node built on the `fcmp++-alpha-stressnet` branch (commit `3421c8ca97efb18f9759d6de3cb049746e6284b6` specifically).
Normally I keep the node on but about 2 weeks ago I shutoff my node for a bit while away and yesterday restarted the node to have it catch back up.
The node synced to height 2969097 but has now gotten itself stuck. I left it on for several hours but the node never proceeded past this point.
Attached is a log-level 4 log of the node attempting to sync for a bit.

[log.txt.gz](https://github.com/user-attachments/files/26638775/log.txt.gz)

# Discussion History
## nahuhh | 2026-04-10T19:54:29+00:00
Whats the output of sync_info

## ComputeryPony | 2026-04-10T20:02:14+00:00
I just started the node to check so it'd only been running 5 minutes when checking this:
```
Height: 2969118, target: 2974618 (99.8151%)
Downloading at 1 kB/s
5 peers
Remote Host                        Peer_ID   State   Prune_Seed          Height  DL kB/s, Queued Blocks / MB
192.3.81.172:28080        d50d46cc3c3366de  normal            0         2892359  0 kB/s, 0 blocks / 0 MB queued
116.203.98.127:28080      d101176235b029ea  synchronizing     182       2974618  0 kB/s, 0 blocks / 0 MB queued
50.27.93.192:28080        aed03b5fc9a9f7e3  synchronizing     185       2974618  0 kB/s, 0 blocks / 0 MB queued
194.58.47.153:28080       fa35d67940d82ae8  synchronizing     180       2974618  1 kB/s, 0 blocks / 0 MB queued
57.129.112.93:28080       25159e72bbccda75  synchronizing     180       2974618  0 kB/s, 0 blocks / 0 MB queued
0 spans, 0 MB
[]
```

## nahuhh | 2026-04-10T20:15:10+00:00
Try grabbing a lvl 2 log from startup for like 60 seconds

## nahuhh | 2026-04-10T20:17:21+00:00
I dont remember how the pruning seeds are numbered, but maybe none of your peers have the next block?

## ComputeryPony | 2026-04-10T20:19:06+00:00
Will grab the lvl 2 log in a minute, I did happen to open wireshark to see if anything unusual was happening and I do see that for some reason almost every connection my node is making starts with the usual Handshake packet back and forth, then my node sends a ChainRequest and the other nodes simply never answer. The only exception seems to be node 192.3.81.173.
But if I'm seeing ChainResponses from that node I would expect to be making progress syncing, right?

## ComputeryPony | 2026-04-10T20:21:04+00:00
log level 2

[log2.txt.gz](https://github.com/user-attachments/files/26639301/log2.txt.gz)

## nahuhh | 2026-04-10T20:31:08+00:00
From your sync info, you only have one `0`Prune_seed peer. I believe 0 = full node. the node in your sync_info is below your sync height, so you cant grab anything from them.

so could very well just be that you dont have peers who have the next block

## ComputeryPony | 2026-04-10T20:33:00+00:00
Dang, I didn't think that many people were running pruned nodes on testnet.
Since I had already left this on for ~12 hours and still hadn't made any progress, is there likely no way for me to rejoin testnet without enabling pruning on my node?

## nahuhh | 2026-04-10T20:37:36+00:00
The chain is over 200gb, so many switched to pruned

## nahuhh | 2026-04-10T20:40:05+00:00
> is there likely no way for me to rejoin testnet without enabling pruning on my node?

enabling pruning wont change anything -- you still need to connect to a peer who had the span of blocks that you are missing. My "full" node doesnt have incoming connections. If yours does, i can try connecting to you.

otherwise i can do some ssh port forwarding and forward my full node port to my vps



## ComputeryPony | 2026-04-10T20:57:12+00:00
Thanks for the connection, sync complete :)
I'll leave incoming connections enabled so others can sync off mine.

# Action History
- Created by: ComputeryPony | 2026-04-10T19:46:51+00:00
- Closed at: 2026-04-10T20:57:12+00:00
