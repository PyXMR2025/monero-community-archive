---
title: Cannot fully sync with 0.14
source_url: https://github.com/monero-project/monero/issues/5188
author: zeroedout
assignees: []
labels: []
created_at: '2019-02-24T02:26:00+00:00'
updated_at: '2019-03-10T19:09:15+00:00'
type: issue
status: closed
closed_at: '2019-03-10T19:03:03+00:00'
---

# Original Description
Hello, my monerod is getting stuck at a certain block. Here is the [bitmonero.log](https://github.com/monero-project/monero/files/2897500/bitmonero.log) and output of [mdb_stat.log](https://github.com/monero-project/monero/files/2897499/mdb_stat.log). I've tried deleting and resyncing from scratch twice now, the last time it went further in the blockchain before getting stuck. I've also tried changing the block sync size.

The most interesting errors seem to be:
`2019-02-24 01:50:03.783 [P2P2]  ERROR   verify  src/cryptonote_core/blockchain.cpp:1637 Block recognized as orphaned and rejected, id = <4923f1dfce7db2ac2572828561a8afd07ba03fb54285179b8651e09b0ead2285>, height 1488003, parent in alt 0, parent in main 0 (parent <e906c8caea0bd9985a0cf14056aeee977e57fb06129b6c58fa9b81cad17f5bb7>, current top <29eda2c65f9896d80bc1c9ac7578b2b1764717c444c2b1a8136f6232c44018c6>, chain height 148`
and
`2019-02-24 01:50:05.151 [P2P5]  WARN    net.p2p src/p2p/net_node.inl:1605       [157.7.142.234:18080 OUT] back ping invoke wrong response "OK" from157.7.142.234:18080, hsh_peer_id=4111372854448335031, rsp.peer_id=2019-02-24 01:50:09.691 [P2P5]  ERROR   net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1037    [85.194.238.130:18080 OUT] Got block with unknown parent which was not requested - querying block has0`

This is on Arch Linux. I'm happy to provide any more information. I've tried resyncing twice now, the last time it went further in the blockchain before getting stuck. I've also tried changing the block sync size and I've deleted the p2pstate.bin file to no effect. 






# Discussion History
## Gingeropolous | 2019-02-24T05:06:19+00:00
are u compiling yourself or using built bot binaries?

## zeroedout | 2019-02-24T08:26:47+00:00
Compiling myself using the AUR build script. 

## moneromooo-monero | 2019-02-24T10:11:31+00:00
You should have an error before that. The first error you show basically says "we've already seen this block, and we already saw it was bad at the time".

## zeroedout | 2019-02-24T19:50:46+00:00
I should... but I don't see anything relevant in the log. It just keeps repeating that error and won't sync further in the blockchain. 

## moneromooo-monero | 2019-03-05T13:43:19+00:00
That is very likely fixed by https://github.com/monero-project/monero/pull/5193

## moneromooo-monero | 2019-03-08T00:55:37+00:00
There are binaries now on https://ww.getmonero.org/downloads/ with this patch.

## moneromooo-monero | 2019-03-10T18:56:21+00:00
99% sure it's fixed, reopen if not.

+resolved


## zeroedout | 2019-03-10T19:03:03+00:00
Yes thank you, I was able to fully sync. 

# Action History
- Created by: zeroedout | 2019-02-24T02:26:00+00:00
- Closed at: 2019-03-10T19:03:03+00:00
