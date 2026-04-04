---
title: '  --db-sync-mode fastest:async:  --block-sync-size=1, Still only 1 OUT Connection'
source_url: https://github.com/monero-project/monero/issues/5596
author: ghost
assignees: []
labels:
- invalid
created_at: '2019-06-01T01:52:35+00:00'
updated_at: '2019-06-15T17:17:52+00:00'
type: issue
status: closed
closed_at: '2019-06-15T17:17:52+00:00'
---

# Original Description
There's something wrong with the peer-to-peer communication protocol.  I can only connect to 1 peer using   --db-sync-mode fastest:async:  --block-sync-size=1 (fastest config found so far).  This has been going on for over 12 hours now.  There are plenty of peers available to sync the blockchain as can be seen here ( https://monerohash.com/nodes-distribution.html ) but it will just not connect to more than one at a time since about block 1,300,000-1,400,000.  I've only been using about 1% of my download bandwidth since then and my hard drive is barely even active the network is so slow.  I also haven't seen any IN peer connections for the entire blockchain sync.  This means that others are probably having the same issues.  My bandwidth can support others trying to sync but, it isn't being utilized.  I'm only moderately technically inclined but it is completely obvious that for a peer-to-peer network, this is just not right.  The only OUT peer I am downloading from is 37.59.97.202  with Longitude :2.3387 and Latitude :48.8582 which is the Eiffel Tower in France?  I'm in the southwest of the U.S.

# Discussion History
## moneromooo-monero | 2019-06-01T09:52:39+00:00
Works for me. But you're essentially (1) increasing the nework overhead by a lot, and (2) telling other peers it's you when they see someone sync a block at a time.
For incoming peers, fix your firewall/router to forward connections to the machine running monerod.


## ghost | 2019-06-02T08:10:34+00:00
If the network overhead needs to be increased to allow a blockchain sync to not take a month, so be it.  If others "see" me, why would that matter?  Is this program not secure or something?

## moneromooo-monero | 2019-06-02T08:17:32+00:00
This is a bug tracker, not a troll site. See reddit for trolling.

+invalid

## ghost | 2019-06-02T08:24:01+00:00
You just lost a node.  Good luck keeping this coin alive with that kind of attitude.  DELETE!

## moneromooo-monero | 2019-06-03T10:52:51+00:00
Let's reuse this to track the speed based on block size, since I remember someone else mentioning it once. If the original reporter wants to make *constructive* comments, they're welcome to.

Testing on current mainnet, from height 1848500:

20 block batches:
=119.756 (270 blocks)
=111.774 (274)
=116.678 (276)
=116.918 (276)
=112.557 (277)

1 block batches:
=122.12 (270)
=122.645 (270)

So it appears block sync size 1 is slower. This is on SSD. If anyone wants to try this out, especially someone with spinning disk, please post your timings here. You can pop blocks with monero-blockchain-import --pop-blocks N to get back to the same starting point.

-invalid


## hyc | 2019-06-03T20:10:15+00:00
Tests on my old Dell Precision M4400 laptop (8GB DDR2 DRAM) using eSATA HDD. (It's quite an old drive, Western Digital WDC WD20 EARX-00PASB0). Tests were run multiple times, syncing from a local node over 1Gbit ethernet. The other node has 16GB DDR3, and most of the blockchain is cached.

The target blockchain height is 1848832. I copied the data.mdb file from the other node to this machine, then ran `monero-blockchain-import --pop-blocks 3000` to start each test. After the first run, all of the relevant local blockchain data is cached in RAM so there were no disk reads during subsequent tests. I'm running with `--db-sync-mode=fast:async:10000` so the daemon isn't waiting for disk writes. As such, the speed of the HDD doesn't actually affect this test at all. I reran each test 3 times to get an average result but this turned out to be unnecessary, the timing was the same on each run (within a few tens of milliseconds).

````
Size    Time
100     55
 50     53
 20     52
 10     51
  5     51
  3     51
  2     54
  1     84
````

## moneromooo-monero | 2019-06-04T14:52:06+00:00
It's interesting to see how very small batches are enough to get all the speedup we'll get. I suspect there's some bad asymptotic behaviour somewhere. Possibly in the block queue.

## moneromooo-monero | 2019-06-15T10:38:24+00:00
OK, so it looks like it's actually in the right ballpark and it does not need changing. We'll revisit if someone  actually has some data showing otherwise.

+invalid

# Action History
- Created by: ghost | 2019-06-01T01:52:35+00:00
- Closed at: 2019-06-15T17:17:52+00:00
