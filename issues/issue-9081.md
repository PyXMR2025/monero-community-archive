---
title: Error with blockchain after abnormal shutdown
source_url: https://github.com/monero-project/monero/issues/9081
author: developergames2d
assignees: []
labels:
- reproduction needed
- more info needed
created_at: '2023-11-29T10:31:28+00:00'
updated_at: '2024-01-02T15:46:36+00:00'
type: issue
status: closed
closed_at: '2024-01-02T15:46:36+00:00'
---

# Original Description
After abnormal shutdown I can't to continue download local blockchain ".../lmdb/data.mdb": in logs print:
[29.11.2023 15:04] 2023-11-29 08:04:14.546 I Monero 'Fluorine Fermi' (v0.18.3.1-release) 
Error: Couldn't connect to daemon: 127.0.0.1:18081
[29.11.2023 15:05] 2023-11-29 08:05:47.031 I Monero 'Fluorine Fermi' (v0.18.3.1-release) 
Error: Couldn't connect to daemon: 127.0.0.1:18081
[29.11.2023 17:29] 2023-11-29 10:29:55.191 I Monero 'Fluorine Fermi' (v0.18.3.1-release) 
Error: Couldn't connect to daemon: 127.0.0.1:18081
[29.11.2023 17:30] 2023-11-29 10:29:59.568 I Monero 'Fluorine Fermi' (v0.18.3.1-release) 
Error: Couldn't connect to daemon: 127.0.0.1:18081

When I run monerod.exe, it creates new mdb-file on disk C:\ (although all exe-files placed on other disk) and tries to load blockchain at height 0!

# Discussion History
## selsta | 2023-11-29T14:44:30+00:00
Did your system crash / have power loss / force shutdown during sync? If yes it likely means your blockchain is corrupted. You have to delete it any resync from scratch.

## developergames2d | 2023-11-29T17:53:23+00:00
> Did your system crash / have power loss / force shutdown during sync? If yes it likely means your blockchain is corrupted. You have to delete it any resync from scratch.

Why make such an unreliable system? Why can't I just cut the file to the point where the data is intact and continue downloading? Why didn’t the developers even want to organize blockchain downloads using the torrent file method? I downloaded some 110 GB for 12 days...

## selsta | 2023-11-29T18:01:24+00:00
> Why make such an unreliable system?

You can set the database to `--db-sync-mode safe`, then it won't corrupt on a crash but it will also sync slower.

We currently use the fast sync method for the initial blockchain sync and switch over to the safe sync method once the blockchain is fully downloaded and verified.

> Why can't I just cut the file to the point where the data is intact and continue downloading?

Because it's a database with a complex internal structure, not a sequential file that can be simply cut at a specific point.

> Why didn’t the developers even want to organize blockchain downloads using the torrent file method? I downloaded some 110 GB for 12 days...

We already use a P2P system to download the blockchain, using torrent for this doesn't make sense.

If you have a fast SSD you can sync up in less than 24h, I assume you use an HDD, that's why you are syncing up so slowly.

## developergames2d | 2023-11-29T18:10:04+00:00
> > Why didn’t the developers even want to organize blockchain downloads using the torrent file method? I downloaded some 110 GB for 12 days...
> 
> We already use a P2P system to download the blockchain, using torrent for this doesn't make sense.
> 
> If you have a fast SSD you can sync up in less than 24h, I assume you use an HDD, that's why you are syncing up so slowly.

My HDD can to write 160MB/s, my 5G-Wi-Fi can to download 20MB/s, but the blockchain was downloaded average on ~100KB/s. 

> > Why can't I just cut the file to the point where the data is intact and continue downloading?
> 
> Because it's a database with a complex internal structure, not a sequential file that can be simply cut at a specific point.

I thought that blockchain has structure as BLOCK_1-NONSE_1-BLOCK_2-NONSE_2..., where SHA256 after each nonse lower some value. This file could be trimmed to the last NONSE...


## selsta | 2023-11-29T18:19:34+00:00
> My HDD can to write 160MB/s, my 5G-Wi-Fi can to download 20MB/s, but the blockchain was downloaded average on ~100KB/s.

Your download speed is mostly irrelevant because it's not the bottleneck, you don't just download but also simultanouly verify the blockchain. This is the resource intensive part that requires a disk with fast random IO speeds. SSDs are ideal for this, a HDD will be slow.

## selsta | 2023-11-29T18:30:44+00:00
> I thought that blockchain has structure as BLOCK_1-NONSE_1-BLOCK_2-NONSE_2..., where SHA256 after each nonse lower some value. This file could be trimmed to the last NONSE...

What you are describing is a simplified conceptual data structure for a blockchain, in real-world applications this is more complex.

We use LMDB (B-tree internally) to store the blockchain data. It's simply not possible to cut the database file like you are suggesting.

## MoneroArbo | 2023-11-29T18:32:41+00:00
A useful flag here might be might be:

`--block-sync-size=x`

where x is the number of blocks to write to disk at once. Default is only 100, but even with full blocks setting it to 500 would only be 150 MB sync'd at a time.

I think you can do something similar but measured in bytes with something like:

`--db-sync-mode=safe:sync:250000000bytes`

250000000 bytes (~250 MB) is the default here so I'm not 100% how it relates to the block-sync-size, if it just uses whichever number is smaller, or if these are in fact slightly different settings.

Anyway, playing around with these settings *may* help with HDD syncing speed

**edit:** this is more of a support thing but I'm not sure the DB is actually corrupted, though with an abnormal shutdown it is likely. But the logs given are wallet logs, not daemon logs, and when you run monerod.exe the issue very likely is that you did not tell it about your custom blockchain location, so it starts over from scratch at the default location. You will need to start it from the command line using something like:

`monerod.exe --data-dir D:\path\to\folder\containing\lmdb\and\p2pstate.bin\`

then report back with whatever output that gives you

# Action History
- Created by: developergames2d | 2023-11-29T10:31:28+00:00
- Closed at: 2024-01-02T15:46:36+00:00
