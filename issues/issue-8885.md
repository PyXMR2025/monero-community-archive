---
title: 'Node no longer syncs --Failed to query m_blocks: MDB_BAD_TXN--'
source_url: https://github.com/monero-project/monero/issues/8885
author: rothisbi
assignees: []
labels: []
created_at: '2023-05-31T13:28:55+00:00'
updated_at: '2025-04-04T16:55:43+00:00'
type: issue
status: closed
closed_at: '2023-06-01T17:05:02+00:00'
---

# Original Description
Dear all,

my node v0.18.2.2 on FreeBSD no longer syncs from block 2890276.

Last good log messages are


<pre>
2023-05-31 13:00:40.589 I SYNCHRONIZATION started
2023-05-31 13:00:42.269 I Synced 2890196/2897900 (99%, 7704 left)
2023-05-31 13:00:49.001 I Synced 2890216/2897900 (99%, 7684 left)
2023-05-31 13:01:21.513 I Synced 2890236/2897900 (99%, 7664 left)
2023-05-31 13:01:42.105 I Synced 2890256/2897900 (99%, 7644 left)
2023-05-31 13:02:06.275 I Synced 2890276/2897900 (99%, 7624 left)
</pre>

and then come error messages:
<pre>
2023-05-31 13:02:13.651 W Failed to query m_blocks: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-05-31 13:02:13.652 E Error adding transaction to txpool: Error adding txpool tx metadata to db transaction: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-05-31 13:02:13.652 W Failed to query m_blocks: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-05-31 13:02:13.652 E Exception at [core::handle_incoming_txs()], what=Failed to query m_blocks: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-05-31 13:02:13.653 W Failed to commit a transaction to the db: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-05-31 13:02:13.653 E Exception in cleanup_handle_incoming_blocks: Failed to commit a transaction to the db: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
</pre>

I can rollback a zfs-snapshot to a previous, well-known state. And when restarting monerod, it fails at same point.

Here is some debug output with loglevel=2:

<pre>
2023-05-31 12:03:03.768 I Synced 2890276/2897866 (99%, 7590 left) (17.778047 sec, 1.124983 blocks/sec), 90.812469 MB queued in 63 spans, stripe 2 -> 2: [mooooooooooooooooooo
oooooooooo.ooooooooooooooooo.oooooooooooo.ooo.o.....]
2023-05-31 12:03:03.768 D [130.61.138.150:18080 OUT]  next span in the queue has blocks 2890276-2890295, we need 2890276
2023-05-31 12:03:03.768 D block <68cccc801b0e41d0a53c82c61178b4d8172512dc97c2b7a1f8659e2e0db1b7ac> found in main chain
2023-05-31 12:03:03.768 D [get_estimated_batch_size] m_height: 2890276  block_start: 2889776  block_stop: 2890275
2023-05-31 12:03:03.768 D estimated average block size for batch: 79408
2023-05-31 12:03:03.768 D calculated batch size: 1786680064
2023-05-31 12:03:03.768 D increase size: 1786680064
2023-05-31 12:03:03.768 D DB map size:     69434211328
2023-05-31 12:03:03.768 D Space used:      60983902208
2023-05-31 12:03:03.768 D Space remaining: 8450309120
2023-05-31 12:03:03.768 D Size threshold:  1786680064
2023-05-31 12:03:03.768 D Percent used: 87.8298  Percent threshold: 90.0000
2023-05-31 12:03:03.769 D block_batches: 20

...

2023-05-31 12:03:10.394 I +++++ BLOCK SUCCESSFULLY ADDED
2023-05-31 12:03:10.394 I id:   <2a397749c384e45f64963face6d03981a716106a3f03e1100992c2d03cf95ecf>
2023-05-31 12:03:10.394 I PoW:  <0c86e813ba99b070a4a26bf257e3ac0ac9d428589939fba464a9120200000000>
2023-05-31 12:03:10.394 I HEIGHT 2890282, difficulty:   310732759729
2023-05-31 12:03:10.394 I block reward: 0.603569520000(0.600000000000 + 0.003569520000), coinbase_weight: 102, cumulative weight: 139070, 27(0/22)ms
2023-05-31 12:03:10.395 D Invalidating block template cache
2023-05-31 12:03:10.729 D Mixin: 15-15
2023-05-31 12:03:10.731 D RCT cache: tx <7a25f171e8ee00bd506eb26439ca688bca34425091787ae89f7f9c8574d93b90> missed
2023-05-31 12:03:10.736 I Transaction added to pool: txid <7a25f171e8ee00bd506eb26439ca688bca34425091787ae89f7f9c8574d93b90> weight: 1529 fee/byte: 4e+06
2023-05-31 12:03:10.736 D tx added: <7a25f171e8ee00bd506eb26439ca688bca34425091787ae89f7f9c8574d93b90>

...

2023-05-31 12:03:11.638 D RCT cache: tx <534310b1487e11afd1194fd26a68b464e904eba7869e09a8f9e4db92ceb78df6> missed
2023-05-31 12:03:11.643 I Transaction added to pool: txid <534310b1487e11afd1194fd26a68b464e904eba7869e09a8f9e4db92ceb78df6> weight: 1527 fee/byte: 20000
2023-05-31 12:03:11.643 D tx added: <534310b1487e11afd1194fd26a68b464e904eba7869e09a8f9e4db92ceb78df6>
2023-05-31 12:03:11.643 D Mixin: 15-15
2023-05-31 12:03:11.643 D RCT cache: tx <1699466d89f5ca0ce4f1c334ccbbdd409dd1fca7e033acedd4e35823f84d8689> missed
2023-05-31 12:03:11.648 I Transaction added to pool: txid <1699466d89f5ca0ce4f1c334ccbbdd409dd1fca7e033acedd4e35823f84d8689> weight: 1533 fee/byte: 20000
2023-05-31 12:03:11.648 D tx added: <1699466d89f5ca0ce4f1c334ccbbdd409dd1fca7e033acedd4e35823f84d8689>
2023-05-31 12:03:11.648 D Mixin: 15-15
2023-05-31 12:03:11.649 W Failed to query m_blocks: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-05-31 12:03:11.649 E Output does not exist! amount = 0, absolute_offset = 37199366
2023-05-31 12:03:11.649 E Failed to get output keys for tx with amount = 0.000000000000 and count indexes 16
2023-05-31 12:03:11.649 E Failed to check ring signature for tx <399cb54881df31a8037fce32751ba4e67232cd39602e17491ab5d9655672089c>  vin key with k_image: <b53a615b53c85bb7ff
b1f5d354b7902a653abb9c8835a6886ed315a735b3bedd>  sig_index: 0
2023-05-31 12:03:11.649 E   *pmax_used_block_height: 0
2023-05-31 12:03:11.649 I Error adding txpool tx metadata to db transaction: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-05-31 12:03:11.649 E Error adding transaction to txpool: Error adding txpool tx metadata to db transaction: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
</pre>

Any advice on how to work around this would be appreciated.

Thanks


BR

rothisbi

# Discussion History
## selsta | 2023-05-31T15:42:42+00:00
Where do you store the blockchain? Did you have a power outage / force shutdown during sync at some point?

## rothisbi | 2023-05-31T18:04:48+00:00
Blockchain is on SSD. Box has 18 days uptime. I can't remember if the last boot was due to some anomaly, but can't rule it out. When I rollback the 2023.05.14 snapshot, it syncs to the block mentioned. There is another snapshot from 2023.05.07, 
so I can run a sync from that date, which is before the last boot. Should I try this?  Thanks.

## selsta | 2023-05-31T18:05:56+00:00
> Should I try this? Thanks.

Yes, I would try this.

## rothisbi | 2023-05-31T18:07:45+00:00
OK, I will let you know.

## rothisbi | 2023-05-31T22:20:28+00:00
Unfortunately, it failed in about the same place as before.

<pre>
2023-05-31 18:11:02.245 I [192.151.151.98:18080 OUT] Sync data returned a new top block candidate: 2880214 -> 2898070 [Your node is 17856 blocks (24.8 days) behind] 
2023-05-31 18:11:02.245 I SYNCHRONIZATION started
2023-05-31 18:12:30.132 I Synced 2880234/2898070 (99%, 17836 left)
2023-05-31 18:13:02.470 I Synced 2880254/2898070 (99%, 17816 left)
2023-05-31 18:13:19.551 I Synced 2880274/2898070 (99%, 17796 left)
2023-05-31 18:13:42.362 I Synced 2880294/2898070 (99%, 17776 left, 0% of total synced, estimated 8.3 hours left)

...

2023-05-31 20:58:09.540 I [98.22.92.79:18080 OUT] Sync data returned a new top block candidate: 2890094 -> 2898153 [Your node is 8059 blocks (11.2 days) behind] 
2023-05-31 20:58:09.540 I SYNCHRONIZATION started
2023-05-31 20:58:16.345 I Synced 2890114/2898154 (99%, 8040 left)
2023-05-31 20:58:32.143 I Synced 2890134/2898154 (99%, 8020 left, 53% of total synced, estimated 2.1 hours left)
2023-05-31 20:58:55.078 I Synced 2890154/2898154 (99%, 8000 left)
2023-05-31 20:59:14.415 I Synced 2890174/2898154 (99%, 7980 left)
2023-05-31 20:59:25.672 I Synced 2890194/2898154 (99%, 7960 left)
2023-05-31 20:59:32.284 I Synced 2890214/2898154 (99%, 7940 left)
2023-05-31 20:59:45.328 I Synced 2890234/2898154 (99%, 7920 left)
2023-05-31 20:59:52.139 I Synced 2890254/2898154 (99%, 7900 left)
2023-05-31 21:00:06.994 I Synced 2890274/2898154 (99%, 7880 left)
2023-05-31 21:00:13.653 W Failed to query m_blocks: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-05-31 21:00:13.673 E Error adding transaction to txpool: Error adding txpool tx metadata to db transaction: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-05-31 21:00:13.673 W Failed to query m_blocks: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-05-31 21:00:13.686 E Exception at [core::handle_incoming_txs()], what=Failed to query m_blocks: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
</pre>

## Gingeropolous | 2023-06-01T02:23:06+00:00
what processor does your system have?

## rothisbi | 2023-06-01T04:37:34+00:00
It is a small box with an Intel N100 processor.

## rothisbi | 2023-06-01T17:05:23+00:00
I will resynchronize. Therefore, close this issue.

## mianumar | 2025-04-03T03:49:48+00:00
I also get this failed due to powercut, I need to download again 80 gigs :( Didn't find any solution on internet.

## selsta | 2025-04-04T16:55:42+00:00
@mianumar There is not really a solution, if your system often has power loss, try adding `--db-sync-mode safe`, it makes sync slower but also the database can't corrupt anymore.

# Action History
- Created by: rothisbi | 2023-05-31T13:28:55+00:00
- Closed at: 2023-06-01T17:05:02+00:00
