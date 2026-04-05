---
title: Slow block propagation
source_url: https://github.com/seraphis-migration/monero/issues/139
author: j-berman
assignees: []
labels: []
created_at: '2025-10-06T16:18:23+00:00'
updated_at: '2026-01-29T03:18:55+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
```
ofrnxmr@ofrnxmr:xmr.mx: Block propagation seems to be super weak. On my private testnet, from time to be notified of the block to time it downloaded/synced was like 3-5 seconds.
ofrnxmr@ofrnxmr:xmr.mx: Im seeing notification of the block at 15:25:55 and still being notified of at at 15:26:39
<p​lowsof> sech1 knows about this i think ^
<p​lowsof> related https://www.reddit.com/r/Monero/comments/1ncde8h/psa_p2pool_v410_update_will_speed_up_the_whole/
ofrnxmr@ofrnxmr:xmr.mx: Not sure why its not pulling the block as soon as it sees it, or if the node that has it is just not able to send it got some reason. All i know is that this wasnt an issue on my private testnet that spanned 4 different hosts and included tor (--proxy)
I dont think thats related @plow
<p​lowsof> will the whole thing just be a bit worse with fcmp's larger blocks?
ofrnxmr@ofrnxmr:xmr.mx: O am seeing the block asap, just not doesnloading it
"syncronization started" like 10times over 1minute before actually successfully downloading the block
<D​ataHoarder> 17:29:30 Block propagation seems to be super weak. On my private testnet, from time to be notified of the block to time it downloaded/synced was like 3-5 seconds.
<D​ataHoarder> this is what I mentioned yesterday
<D​ataHoarder> same with submit_block
<D​ataHoarder> ~20s or so
ofrnxmr@ofrnxmr:xmr.mx: its like 2mins
<D​ataHoarder> before block gets broadcasted, which then each receiver will do the same
<D​ataHoarder> 17:30:37 related
<D​ataHoarder> that's trying to broadcast so all check in parallel yes
spackle@spackle:monero.social: sometimes after finding a block my monerod will report being disconnected from the network a few seconds later
```

# Discussion History
## j-berman | 2025-10-07T02:21:11+00:00
I think the sporadic `tx <...> included reference block that was too high` errors may be related to this too. If a new tx hits a node and node starts processing the tx before the node finishes adding the tip block, nodes would see the error.

## j-berman | 2025-10-07T17:14:58+00:00
Seems a high likelihood this is caused by #140

## j-berman | 2025-10-08T20:57:48+00:00
Related issue... @spackle-xmr's [logs](https://github.com/seraphis-migration/monero/issues/140#issuecomment-3377549639) show the node is taking a very long time to relay a block after finding it, mainly because it's re-validating many txs in the pool in preparation for mining the next block, before relaying the found block.

It likely re-validates many txs in the pool because `RCT_VER_CACHE_SIZE = 8192`.

Plus, probably makes sense to relay a block immediately after finding it, before preparing to mine the next block.

Logs:

```
2025-10-07 15:28:06.719	I +++++ BLOCK SUCCESSFULLY ADDED
2025-10-07 15:28:06.719	I id:	<e9abe9c59f02d5a752265fd6040f714111c3e50983d4f4ba096297ed4d81a4e3>
2025-10-07 15:28:06.719	I PoW:	<5fc74c38eff2ff347b18bbf160e0070293e2d99b7a4e241866134c341f040000>
2025-10-07 15:28:06.719	I HEIGHT 2849916, difficulty:	789781
2025-10-07 15:28:06.719	I block reward: 0.693470670664(0.596910390664 + 0.096560280000), coinbase_weight: 107, cumulative weight: 4652675, 231(0/2)ms
2025-10-07 15:28:06.719	D Invalidating block template cache
2025-10-07 15:28:06.839	D Pruning not enabled, nothing to do
2025-10-07 15:28:06.839	D Filling block template, median weight 4358891, 22867 txes in the pool
2025-10-07 15:28:06.839	D DB map size:     211787681792
2025-10-07 15:28:06.839	D Space used:      14506741760
2025-10-07 15:28:06.839	D Space remaining: 197280940032
2025-10-07 15:28:06.839	D Size threshold:  0
2025-10-07 15:28:06.839	D Percent used: 6.8497  Percent threshold: 90.0000
2025-10-07 15:28:06.839	D Considering <d9b784492198f44f8a226ed9b0240678ee2000306df43c247ed5ef07aa7a2b5f>, weight 7180, current block weight 0/8717182, current coinbase 0.600000000000, relay method 4
2025-10-07 15:28:06.839	E Key image already spent in blockchain: ca92544425745e39e88f4514f588cfc54d405ffb6b118beb8ab8f916be3d2d14
2025-10-07 15:28:06.839	D   not ready to go
...
2025-10-07 15:28:09.144	D Considering <a34bccce94bb1c52871f5555ff33042cfeb369bae7eecf1dfb35a5a7ba21f95a>, weight 6498, current block weight 428868/8717182, current coinbase 0.608967240000, relay method 4
2025-10-07 15:28:09.144	D RCT cache: tx <a34bccce94bb1c52871f5555ff33042cfeb369bae7eecf1dfb35a5a7ba21f95a> missed
2025-10-07 15:28:09.180	D   added, new block weight 435366/8717182, coinbase 0.609097200000
2025-10-07 15:28:09.180	D Considering <7e9792c0d9cffe348c12ac5fe85a914e293cec6803b6034954e1328676272a7a>, weight 6498, current block weight 435366/8717182, current coinbase 0.609097200000, relay method 4
2025-10-07 15:28:09.180	D RCT cache: tx <7e9792c0d9cffe348c12ac5fe85a914e293cec6803b6034954e1328676272a7a> missed
2025-10-07 15:28:09.216	D   added, new block weight 441864/8717182, coinbase 0.609227160000
2025-10-07 15:28:09.216	D Considering <b96cd1379db7542864bbd17cefe59401079a54400e021b1402e72b20127ca693>, weight 6498, current block weight 441864/8717182, current coinbase 0.609227160000, relay method 4
2025-10-07 15:28:09.216	D RCT cache: tx <b96cd1379db7542864bbd17cefe59401079a54400e021b1402e72b20127ca693> missed
2025-10-07 15:28:09.252	D   added, new block weight 448362/8717182, coinbase 0.609357120000
...
2025-10-07 15:28:32.356	D Block template filled with 720 txes, weight 4678560/8717182, coinbase 0.690734070252 (including 0.093961080000 in fees)
2025-10-07 15:28:32.357	D Setting block template cache
2025-10-07 15:28:32.357	D miner::resume: 1 -> 0
2025-10-07 15:28:32.357	D MINING RESUMED
2025-10-07 15:28:32.357	I Failed to invoke command 1001 return code -2
2025-10-07 15:28:32.357	W [51.171.102.66:28080 OUT] COMMAND_HANDSHAKE Failed
2025-10-07 15:28:32.357	I [51.171.102.66:28080 OUT] Failed to HANDSHAKE with peer 51.171.102.66:28080
2025-10-07 15:28:32.357	D Handshake failed
2025-10-07 15:28:32.357	D get_next_needed_pruning_stripe: want height 2849917 (2849917 from blockchain, 2849917 from block queue), stripe 8 (4/12 on it and 0 on 1, 0 others) -> 1 (+1), current peers 110? 110? 110? 110? 
2025-10-07 15:28:32.358	D Considering connecting (out) to gray list peer: 94dfb6801854823e 38.6.155.70:18100, pruning seed 0 (stripe 1 needed)
2025-10-07 15:28:32.358	D block <14db73ad9614c6facaef7553344136a8d124aa615a6edd2d58c5eee2e76843cd> found in main chain
2025-10-07 15:28:32.358	D Selected peer: 94dfb6801854823e 38.6.155.70:18100, pruning seed 0 [peer_list=2] last_seen: never
2025-10-07 15:28:32.358	D Connecting to 38.6.155.70:18100(peer_type=2, last_seen: never)...
2025-10-07 15:28:32.358	D bulletproof+ clawback: 0
2025-10-07 15:28:32.358	D Spawned connection #762 to 0.0.0.0 currently we have sockets count:6
2025-10-07 15:28:32.358	D connections_ size now 1
2025-10-07 15:28:32.358	D [62.38.144.238:28080 OUT] COMMAND_TIMED_SYNC
2025-10-07 15:28:32.358	D Trying to connect to 38.6.155.70:18100, bind_ip = 0.0.0.0
2025-10-07 15:28:32.358	I [62.38.144.238:28080 OUT] 1348 bytes sent for category command-1002 initiated by us
2025-10-07 15:28:32.358	D [62.38.144.238:28080 OUT] LEVIN_PACKET_SENT. [len=1348, flags2, r?=?, cmd = 1002, ver=1
2025-10-07 15:28:32.359	D [62.38.144.238:28080 OUT] RELAYING FLUFFY BLOCK TO PEER
2025-10-07 15:28:32.359	D [85.86.209.47:28080 OUT] RELAYING FLUFFY BLOCK TO PEER
2025-10-07 15:28:32.359	D [181.89.154.82:28080 OUT] RELAYING FLUFFY BLOCK TO PEER
2025-10-07 15:28:32.359	D [172.103.161.225:28080 OUT] RELAYING FLUFFY BLOCK TO PEER
2025-10-07 15:28:32.361	I [172.103.161.225:28080 OUT] 4213921 bytes sent for category command-2008 initiated by us
2025-10-07 15:28:32.361	D [172.103.161.225:28080 OUT] LEVIN_PACKET_SENT. [len=4213921, flags1, r?=?, cmd = 2008, ver=1
2025-10-07 15:28:32.362	I [62.38.144.238:28080 OUT] 4213921 bytes sent for category command-2008 initiated by us
2025-10-07 15:28:32.362	D [62.38.144.238:28080 OUT] LEVIN_PACKET_SENT. [len=4213921, flags1, r?=?, cmd = 2008, ver=1
2025-10-07 15:28:32.362	I [181.89.154.82:28080 OUT] 4213921 bytes sent for category command-2008 initiated by us
2025-10-07 15:28:32.362	D [181.89.154.82:28080 OUT] LEVIN_PACKET_SENT. [len=4213921, flags1, r?=?, cmd = 2008, ver=1
2025-10-07 15:28:32.362	I [85.86.209.47:28080 OUT] 4213921 bytes sent for category command-2008 initiated by us


```

## j-berman | 2025-10-11T17:50:09+00:00
This should be helped by:

https://github.com/seraphis-migration/monero/pull/155
https://github.com/seraphis-migration/monero/pull/159
https://github.com/monero-project/monero/pull/10157


## spirobel | 2026-01-23T06:38:18+00:00
how would #159 help with slow block propagation? 
the assumption is that before this pr, it would not sync over the fluffy block notification protocol and instead refetch the block like during initial sync? 

## j-berman | 2026-01-26T18:55:01+00:00
> the assumption is that before this pr, it would not sync over the fluffy block notification protocol and instead refetch the block like during initial sync?

Yes, I figured having to move over to initial sync was slowing down new block notification. Plus, new nodes running #159 wouldn't strictly require older nodes update with #155 in order to receive their new blocks. So it would help on 2 fronts: 1) prevent reversion to IBD protocol, and 2) don't drop connections from older nodes that weren't running #155 yet.

#155 was the more significant fix for this issue of slow block propagation.


## spirobel | 2026-01-26T19:15:35+00:00
why was 128 mb picked for the limit in #159 ? any idea why it was only 4 mb before?

## j-berman | 2026-01-26T19:29:19+00:00
Because it would match the new block limit, which seemed both a sane / reasonable improvement

> any idea why it was only 4 mb before?

I assume it was a mistake where the original author wasn't thinking about how the fluffy block could still potentially be full of tx blobs when they chose it, and was only thinking about tx hashes (the comment reads `"but it does not includes transaction data"`)

## spirobel | 2026-01-27T03:36:10+00:00
> Because it would match the new block limit, which seemed both a sane / reasonable improvement

the 128 mb are larger than the 100 mb levin packet limit, it means blocks could be synced over the fluffy block notification, that can't be accepted during initial sync

## j-berman | 2026-01-27T05:28:55+00:00
If the limit was 100mb, you could still sync fluffy blocks that can't be synced during initial sync (e.g. you have 60mb of txs already, and only need 50mb more). Anything over 100mb on this fluffy block limit is a wash / inconsequential because of the packet limit

## spirobel | 2026-01-27T08:30:26+00:00
>Anything over 100mb on this fluffy block limit is a wash / inconsequential because of the packet limit

the levin 100mb packet limit is applied before the block is included when the block is being received through the fluffy block notification?

## j-berman | 2026-01-27T15:40:15+00:00
> it means blocks could be synced over the fluffy block notification, that can't be accepted during initial sync

The point I was making is that the fluffy block byte limit doesn't prevent this scenario from occurring. The fluffy block byte limit could even be 50mb, and it's still possible to sync a block via the current fluffy block protocol that's >100mb

## spirobel | 2026-01-29T03:18:55+00:00
yes that is true. Other levin limits might get violated as well, which means the final packet can't be serialized when synced through the inital block sync protocol / when wallets or other software fetch the block through the daemon rpc.

to prevent that we can put the fluffy block through the serialization code of the initial block sync protocol to see if the packet can be formed correctly. That means we know that the synced block will be valid through all possible paths before we add it

# Action History
- Created by: j-berman | 2025-10-06T16:18:23+00:00
