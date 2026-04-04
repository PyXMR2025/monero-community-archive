---
title: monerod stuck syncing on block 1288623
source_url: https://github.com/monero-project/monero/issues/4931
author: jagerman
assignees: []
labels: []
created_at: '2018-12-03T05:56:30+00:00'
updated_at: '2018-12-13T01:25:07+00:00'
type: issue
status: closed
closed_at: '2018-12-13T01:25:07+00:00'
---

# Original Description
With a fresh monero compiled from the current release-0.13 branch (commit ab6c17cc154914df61778ad48577ed70d8b03f88) I get stuck at block 1288623 when syncing from scratch.  I've tried popping blocks (1, 10, 1000), and deleting p2pstate.bin (and both at once), but I still get suck at the same place.  There are a few other closed reports (#2562 and #2795) that seem related, but have been closed as resolved.


Running `monerod --log-level 1,\*verify\*:DEBUG` gives these errors initially:

```
2018-12-03 05:44:55.805	[P2P1]	ERROR	verify	src/cryptonote_core/blockchain.cpp:3455	Block with id: <2d40896daae685856e0769438dfe9aca5a5f11777d9c23649f9c8d2157ff9339> has at least one transaction (id: <b177b6898937e62ab4df3085a23621cf4e48b5fe0c61ae2807c47d3ecf58a1a1>) with wrong inputs.
2018-12-03 05:44:55.806	[P2P1]	INFO 	blockchain	src/cryptonote_core/blockchain.cpp:2123	BLOCK ADDED AS INVALID: <2d40896daae685856e0769438dfe9aca5a5f11777d9c23649f9c8d2157ff9339>
, prev_id=<7f2adedab33ffe9e417e68c74f644e3517bc9138a2557f394c59d6f3b5ff2430>, m_invalid_blocks count=1
2018-12-03 05:44:55.806	[P2P1]	ERROR	verify	src/cryptonote_core/blockchain.cpp:3458	Block with id <2d40896daae685856e0769438dfe9aca5a5f11777d9c23649f9c8d2157ff9339> added as invalid because of wrong inputs in transactions
```

This block id looks like the right one for that height: https://moneroblocks.info/search/1288623

After this there are also a number of errors repeatedly:
```
2018-12-03 05:46:08.193	[P2P5]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1037	[5.200.23.88:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
```
and:
```
2018-12-03 05:46:08.920	[P2P8]	ERROR	verify	src/cryptonote_core/blockchain.cpp:1604	Block recognized as orphaned and rejected, id = <bad4e7644641bac9702f52f7c920b9fb58ebf5f5b956649d300b73ec27996795>, height 1288624, parent in alt 0, parent in main 0 (parent <2d40896daae685856e0769438dfe9aca5a5f11777d9c23649f9c8d2157ff9339>, current top <7f2adedab33ffe9e417e68c74f644e3517bc9138a2557f394c59d6f3b5ff2430>, chain height 1288623)
```

The full log from `--log-level 1,\*verify\*:DEBUG` is here: https://jagerman.com/bitmonero-debug.log
I ran it a second time for a minute with `--log-level 4`; the full 30MB log of that is here: https://jagerman.com/bitmonero-verbose.log

# Discussion History
## moneromooo-monero | 2018-12-03T18:00:48+00:00
Probably fixed  by https://github.com/monero-project/monero/pull/4920

## moneromooo-monero | 2018-12-05T12:58:20+00:00
Did it fix it ?

## jagerman | 2018-12-06T15:20:44+00:00
> Did it fix it ?

It did!

## moneromooo-monero | 2018-12-13T01:16:55+00:00
+resolved

# Action History
- Created by: jagerman | 2018-12-03T05:56:30+00:00
- Closed at: 2018-12-13T01:25:07+00:00
