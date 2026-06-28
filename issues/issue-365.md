---
title: Sporadic double spends & broken rescan_spent
source_url: https://github.com/seraphis-migration/monero/issues/365
author: j-berman
assignees: []
labels:
- upstream
created_at: '2026-05-08T22:13:13+00:00'
updated_at: '2026-06-26T17:09:12+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Reported by u/kico in the stressnet channel:

> rescan_spent on cli seems to really do nothing

# Discussion History
## j-berman | 2026-05-09T03:13:48+00:00
Helpful logs from u/kico that indicate `rescan_spent` isn't identifying the spends as expected:

[8terjt.log](https://github.com/user-attachments/files/27544950/8terjt.log)

Can see double spend errors for a tx with the same key images before *and* after `rescan_spent`.

Plus, `rescan_spent` *is* identifying some spends previously marked as unspent, which is also unexpected. The wallet should be identifying all spends during the normal refresh flow.

## j-berman | 2026-05-13T18:31:03+00:00
Multiple users have complained about sporadic double spend errors. May be a regression from #185

## j-berman | 2026-06-15T20:33:44+00:00
EDIT: this was incorrect

This should fix the issue of a wallet marking spent txs as unspent during normal refresh flow: https://github.com/monero-project/monero/pull/10781

Still unsure as to cause of broken `rescan_spent`

## j-berman | 2026-06-26T17:08:50+00:00
@Rucknium reproduced this issue with log level 2 in daemon and wallet, with a daemon that's modified to log even more output to help see what's happening.

Here are the relevant logs:
[monerod_relevant.zip](https://github.com/user-attachments/files/29389997/monerod_relevant.zip)
[wallet_rpc_relevant_1.zip](https://github.com/user-attachments/files/29390078/wallet_rpc_relevant_1.zip)
[wallet_rpc_relevant_2.zip](https://github.com/user-attachments/files/29390084/wallet_rpc_relevant_2.zip)
[wallet_rpc_relevant_3.zip](https://github.com/user-attachments/files/29390098/wallet_rpc_relevant_3.zip)

`monerod` was running beta stressnet at [this commit](https://github.com/j-berman/monero/commit/c237a4a2ad3d3087b9cf20969c57781580bbff83), and `wallet-rpc-server` at [this commit](https://github.com/seraphis-migration/monero/tree/28970229c3fda2a7e86855bb4504fdb24ebdaf78).


#### My take

The node accepts a tx into its pool, but looks like before the node could relay the tx, the node dies. Then an upstream bug in the re-relay logic prevents the node from ever re-relaying the tx. Thus, even after restart, the tx ends up stuck in the node's pool, un-relayed, never to be relayed again.

The wallet therefore never sees this tx it constructed in the daemon's pool because the daemon's using a restricted RPC, which doesn't show txs that have yet to be relayed. After 500s the wallet marks the tx as failed, marking its key images as available-for-use. Then later, upon constructing a subsequent tx with the same key image and submitting to a daemon, the daemon sees a double spend of the earlier tx's key images and rejects the subsequent tx.

#### Immediate proposed fix

Ensure that the node would re-relay the tx even on restart if it does not relay the tx before shutting off.

I implemented this [here](https://github.com/j-berman/monero/commit/bf4af1e742403e754bad154fa396a02832babecf), and @Rucknium is currently running it to see if it prevents the double spend error from occurring again.

#### Other issues

1. The node dying.
   - From the logs, looks like the node dies while handling a wallet's request for pool txs, which unnecessarily reads unpruned blobs from the db.
   - I suspect the long term solution [here](https://github.com/seraphis-migration/monero/issues/293#issuecomment-3906086569) would significantly help prevent the node from over-exerting load when serving pool txs.

2. The node taking a while to relay the tx in the first place.
   - In the logs, note a large gap between strand executions that relay txs in the queue shortly before the node dies.
   - I haven't looked further into why this may have happened. Maybe related to the node gummed up handling serving the large pool?

#### Isolated helpful logs

`monerod`

```
# Note this is just showing the last time the re-relay loop was attempted, this tx hash is irrelevant
2026-06-25 04:17:54.771	[P2P1]	INFO	cn	src/cryptonote_core/cryptonote_core.cpp:1202	Going to re-relay block/fluff/stem tx <218af73a87d199174435dfa605460530edfaa17e45f2c86066bb83e7169fa6d2>

...

# Here is the "problem" tx hash that the wallet submits and daemon never relays
2026-06-25 04:18:35.508	[RPC0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3965	No previously valid verID provided for tx <362388b3439323efd91e3ed6f58bfdbf05b77a278cce858c5f4f7dd820bac7a2>, continuing to input verification as normal...
2026-06-25 04:18:35.567	[RPC0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3998	Input verification for tx <362388b3439323efd91e3ed6f58bfdbf05b77a278cce858c5f4f7dd820bac7a2> succeeded. Setting verID to <f2a51c363e989fa0dd4e75e32786745250b3b7046a9e418e25e469368e484c80>
2026-06-25 04:18:35.567	[RPC0]	INFO	txpool	src/cryptonote_core/tx_pool.cpp:1894	Adding tx to transient lists <362388b3439323efd91e3ed6f58bfdbf05b77a278cce858c5f4f7dd820bac7a2> at time 1782361115 , with receive_time for other container: 1782361115 , sensitive? 1
2026-06-25 04:18:35.569	[RPC0]	INFO	txpool	src/cryptonote_core/tx_pool.cpp:395	Transaction added to pool: txid <362388b3439323efd91e3ed6f58bfdbf05b77a278cce858c5f4f7dd820bac7a2> weight: 7650 fee/byte: 6500, count: 8401, pool total weight: 67274466
2026-06-25 04:18:35.570	[RPC0]	DEBUG	cn	src/cryptonote_core/cryptonote_core.cpp:870	tx added to pool: <362388b3439323efd91e3ed6f58bfdbf05b77a278cce858c5f4f7dd820bac7a2>
2026-06-25 04:18:35.570	[RPC0]	INFO	daemon.rpc	src/rpc/core_rpc_server.cpp:1652	Now relaying tx <362388b3439323efd91e3ed6f58bfdbf05b77a278cce858c5f4f7dd820bac7a2>
2026-06-25 04:18:35.570	[RPC0]	INFO	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:861	Attempting to send 1
2026-06-25 04:18:35.570	[RPC0]	INFO	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:871	First tx we're sending is <362388b3439323efd91e3ed6f58bfdbf05b77a278cce858c5f4f7dd820bac7a2>
2026-06-25 04:18:35.570	[RPC0]	INFO	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:933	Dispatching Dandelion++ notify
2026-06-25 04:18:35.570	[RPC0]	INFO	daemon.rpc	src/rpc/core_rpc_server.cpp:1661	Finished handling relay for <362388b3439323efd91e3ed6f58bfdbf05b77a278cce858c5f4f7dd820bac7a2>
...

2026-06-25 04:18:35.811	[P2P3]	INFO	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:587	Strand is executing Dandelion++ notify for 1 txs
2026-06-25 04:18:35.811	[P2P3]	INFO	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:594	Attempting to stem 1 txs

...

# I suspect (but don't know 1000%) that this is **not** the tx above, but a prior one. Note the large gap from the prior "Attempting to stem" to this. I think something gummed up the strand executor
2026-06-25 04:19:58.518	[P2P3]	INFO	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:604	Sent 1 transaction(s) to bbbb7036-5b6e-4ee4-8b08-b9ca92ae9a4e using Dandelion++ stem

...

# This shows the node dying while reading pool txs from the db, then restarting 30s later
2026-06-25 04:20:00.107	[RPC0]	INFO	perf.txpool	src/common/perf_timer.cpp:161	PERF    54951      get_transaction_info
2026-06-25 04:20:00.187	[RPC0]	DEBUG	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:663	DB map size:     651759222784
2026-06-25 04:20:00.395	[RPC0]	DEBUG	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:664	Space used:      63032324096
2026-06-25 04:20:00.619	[RPC0]	DEBUG	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:665	Space remaining: 588726898688
2026-06-25 04:20:00.863	[RPC0]	DEBUG	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:666	Size threshold:  0
2026-06-25 04:20:01.419	[RPC0]	DEBUG	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:668	Percent used: 9.6711  Percent threshold: 90.0000
2026-06-25 04:20:33.026	    795976880ac0	INFO	logging	contrib/epee/src/mlog.cpp:274	New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,daemon.rpc:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO
2026-06-25 04:20:33.026	    795976880ac0	INFO	logging	contrib/epee/src/mlog.cpp:274	New log categories: *:DEBUG
2026-06-25 04:20:33.027	    795976880ac0	INFO	global	src/daemon/main.cpp:298	Monero 'Fluorine Fermi' (v0.19.0.0-beta.2.0-c237a4a2a)
2026-06-25 04:20:33.027	    795976880ac0	INFO	daemon	src/daemon/main.cpp:360	Moving from main() into the daemonize now.
2026-06-25 04:20:33.027	    795976880ac0	INFO	global	src/daemon/protocol.h:57	Initializing cryptonote protocol...
2026-06-25 04:20:33.028	    795976880ac0	INFO	global	src/daemon/protocol.h:62	Cryptonote protocol initialized OK

...

# Tx is still in the pool
2026-06-25 04:20:48.007	    795976880ac0	INFO	txpool	src/cryptonote_core/tx_pool.cpp:1894	Adding tx to transient lists <362388b3439323efd91e3ed6f58bfdbf05b77a278cce858c5f4f7dd820bac7a2> at time 1782361248 , with receive_time for other container: 1782361115 , sensitive? 1

...

# Note this is showing the next time the node re-attempted the re-relay loop, but the problem tx hash doesn't ever get re-relayed
2026-06-25 04:20:53.524	[P2P0]	INFO	cn	src/cryptonote_core/cryptonote_core.cpp:1202	Going to re-relay block/fluff/stem tx <a33e07ede4c3a1105088fc1d4fdb80ba471c2b87ccf4a1a680699a182fe93900>

...

# The double spend error
2026-06-25 09:28:54.524	[RPC1]	INFO	txpool	src/cryptonote_core/tx_pool.cpp:1622	Marking <362388b3439323efd91e3ed6f58bfdbf05b77a278cce858c5f4f7dd820bac7a2> as double spending <5ed50ac6620fcd9d262893e37bb42baad3b59505b62ac049c18a9eceb554dd93>
2026-06-25 09:28:54.526	[RPC1]	INFO	txpool	src/cryptonote_core/tx_pool.cpp:251	Transaction with id= <119a87fa00c870970628d8e1f19bfb918e927d68d21931f22d0a115a7d6aa520> used already spent key images

...

# I asked @Rucknium to run a new commit that would check the state of the problem tx in the pool, helping confirm the tx never relayed and had absurdly high `last_relayed_time` thus preventing re-relay
# https://github.com/j-berman/monero/commit/6245f444b44e13f2e82c7d21c7369589693907fc
# note: this is not contained in the logs linked above, ruck just dm'd this log snippet to me to confirm
2026-06-25 23:52:21.450           7bbb349bdac0        INFO    txpool  src/cryptonote_core/tx_pool.cpp:2042    Initializing pool tx <362388b3439323efd91e3ed6f58bfdbf05b77a278cce858c5f4f7dd820bac7a2> , last relayed time: 18446744073709551615 , relay method: 1

```


Wallet RPC

```
2026-06-25 04:18:35.580	[RPC0]	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7915	transaction <362388b3439323efd91e3ed6f58bfdbf05b77a278cce858c5f4f7dd820bac7a2> generated ok and sent to daemon, key_images: [<5ed50ac6620fcd9d262893e37bb42baad3b59505b62ac049c18a9eceb554dd93>]
2026-06-25 04:18:35.580	[RPC0]	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:2235	Setting SPENT at 0: ki <5ed50ac6620fcd9d262893e37bb42baad3b59505b62ac049c18a9eceb554dd93>, amount 0.035314862036
2026-06-25 04:18:35.580	[RPC0]	INFO	wallet.wallet2	src/wallet/wallet2.cpp:7930	Transaction successfully sent. <<362388b3439323efd91e3ed6f58bfdbf05b77a278cce858c5f4f7dd820bac7a2>>

...

2026-06-25 04:21:06.788	[RPC0]	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:4193	Checking m_unconfirmed_txs entry <362388b3439323efd91e3ed6f58bfdbf05b77a278cce858c5f4f7dd820bac7a2>
2026-06-25 04:21:06.788	[RPC0]	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:4205	New state of that entry: 0

...

2026-06-25 04:29:20.470	[RPC0]	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:4282	Checking m_unconfirmed_txs entry <362388b3439323efd91e3ed6f58bfdbf05b77a278cce858c5f4f7dd820bac7a2>
2026-06-25 04:29:20.470	[RPC0]	INFO	wallet.wallet2	src/wallet/wallet2.cpp:4095	Pending txid <362388b3439323efd91e3ed6f58bfdbf05b77a278cce858c5f4f7dd820bac7a2> not in pool after 500 seconds, marking as failed
2026-06-25 04:29:20.470	[RPC0]	INFO	wallet.wallet2	src/wallet/wallet2.cpp:4054	Resetting spent status for output 0: <5ed50ac6620fcd9d262893e37bb42baad3b59505b62ac049c18a9eceb554dd93> (spent=0)
2026-06-25 04:29:20.470	[RPC0]	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:2244	Setting UNSPENT: ki <5ed50ac6620fcd9d262893e37bb42baad3b59505b62ac049c18a9eceb554dd93>, amount 0.035314862036
2026-06-25 04:29:20.470	[RPC0]	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:4294	Resulting state of that entry: 2
...

2026-06-25 09:28:54.545	[RPC0]	WARNING	net.http	src/wallet/wallet_errors.h:1014	/distsrc-base/build/distsrc-8ed2f782517d-x86_64-linux-gnu/src/wallet/wallet2.cpp:7848:N5tools5error11tx_rejectedE: transaction was rejected by daemon, status = Failed, tx:
2026-06-25 09:28:54.545	[RPC0]	WARNING	net.http	src/wallet/wallet_errors.h:1014	{
2026-06-25 09:28:54.545	[RPC0]	WARNING	net.http	src/wallet/wallet_errors.h:1014	  "version": 2, 
2026-06-25 09:28:54.545	[RPC0]	WARNING	net.http	src/wallet/wallet_errors.h:1014	  "unlock_time": 0, 
2026-06-25 09:28:54.545	[RPC0]	WARNING	net.http	src/wallet/wallet_errors.h:1014	  "vin": [ {
2026-06-25 09:28:54.545	[RPC0]	WARNING	net.http	src/wallet/wallet_errors.h:1014	      "key": {
2026-06-25 09:28:54.545	[RPC0]	WARNING	net.http	src/wallet/wallet_errors.h:1014	        "amount": 0, 
2026-06-25 09:28:54.545	[RPC0]	WARNING	net.http	src/wallet/wallet_errors.h:1014	        "key_offsets": [ ], 
2026-06-25 09:28:54.545	[RPC0]	WARNING	net.http	src/wallet/wallet_errors.h:1014	        "k_image": "5ed50ac6620fcd9d262893e37bb42baad3b59505b62ac049c18a9eceb554dd93"
2026-06-25 09:28:54.545	[RPC0]	WARNING	net.http	src/wallet/wallet_errors.h:1014	      }
2026-06-25 09:28:54.545	[RPC0]	WARNING	net.http	src/wallet/wallet_errors.h:1014	    }], 
2026-06-25 09:28:54.545	[RPC0]	WARNING	net.http	src/wallet/wallet_errors.h:1014	  "vout": [ {
2026-06-25 09:28:54.545	[RPC0]	WARNING	net.http	src/wallet/wallet_errors.h:1014	      "amount": 0, 
2026-06-25 09:28:54.545	[RPC0]	WARNING	net.http	src/wallet/wallet_errors.h:1014	      "target": {
2026-06-25 09:28:54.545	[RPC0]	WARNING	net.http	src/wallet/wallet_errors.h:1014	        "carrot_v1": {
2026-06-25 09:28:54.545	[RPC0]	WARNING	net.http	src/wallet/wallet_errors.h:1014	          "key": "7694e9a81670448b32704cd81b771e2f701c5e0657963c13bed2e07055d1e328", 
2026-06-25 09:28:54.545	[RPC0]	WARNING	net.http	src/wallet/wallet_errors.h:1014	          "view_tag": "daefa1", 
2026-06-25 09:28:54.545	[RPC0]	WARNING	net.http	src/wallet/wallet_errors.h:1014	          "encrypted_janus_anchor": "25f16cf4ee11efd85abf01d6bd80ec61"
2026-06-25 09:28:54.545	[RPC0]	WARNING	net.http	src/wallet/wallet_errors.h:1014	        }
2026-06-25 09:28:54.545	[RPC0]	WARNING	net.http	src/wallet/wallet_errors.h:1014	      }
2026-06-25 09:28:54.545	[RPC0]	WARNING	net.http	src/wallet/wallet_errors.h:1014	    }, {
2026-06-25 09:28:54.545	[RPC0]	WARNING	net.http	src/wallet/wallet_errors.h:1014	      "amount": 0, 
2026-06-25 09:28:54.545	[RPC0]	WARNING	net.http	src/wallet/wallet_errors.h:1014	      "target": {
2026-06-25 09:28:54.545	[RPC0]	WARNING	net.http	src/wallet/wallet_errors.h:1014	        "carrot_v1": {
2026-06-25 09:28:54.545	[RPC0]	WARNING	net.http	src/wallet/wallet_errors.h:1014	          "key": "8100bc582befafa4009aab97d17c3f6fed1070e9964154a50387a5df7b71c349", 
2026-06-25 09:28:54.545	[RPC0]	WARNING	net.http	src/wallet/wallet_errors.h:1014	          "view_tag": "92b0a7", 
2026-06-25 09:28:54.545	[RPC0]	WARNING	net.http	src/wallet/wallet_errors.h:1014	          "encrypted_janus_anchor": "e53a1a8ff406b6ff8b59d78b9df0c775"
2026-06-25 09:28:54.545	[RPC0]	WARNING	net.http	src/wallet/wallet_errors.h:1014	        }
2026-06-25 09:28:54.545	[RPC0]	WARNING	net.http	src/wallet/wallet_errors.h:1014	      }
2026-06-25 09:28:54.545	[RPC0]	WARNING	net.http	src/wallet/wallet_errors.h:1014	    }
2026-06-25 09:28:54.545	[RPC0]	WARNING	net.http	src/wallet/wallet_errors.h:1014	  ], 
2026-06-25 09:28:54.545	[RPC0]	WARNING	net.http	src/wallet/wallet_errors.h:1014	  "extra": [ 1, 168, 160, 20, 252, 125, 151, 194, 79, 97, 22, 198, 127, 126, 49, 222, 23, 60, 245, 111, 15, 114, 117, 56, 202, 107, 248, 16, 34, 250, 201, 154, 107, 2, 9, 1, 178, 87, 8, 255, 96, 228, 247, 159
2026-06-25 09:28:54.545	[RPC0]	WARNING	net.http	src/wallet/wallet_errors.h:1014	  ], 
2026-06-25 09:28:54.545	[RPC0]	WARNING	net.http	src/wallet/wallet_errors.h:1014	  "rct_signatures": {
2026-06-25 09:28:54.545	[RPC0]	WARNING	net.http	src/wallet/wallet_errors.h:1014	    "type": 7, 
2026-06-25 09:28:54.545	[RPC0]	WARNING	net.http	src/wallet/wallet_errors.h:1014	    "txnFee": 49725000, 
2026-06-25 09:28:54.545	[RPC0]	WARNING	net.http	src/wallet/wallet_errors.h:1014	    "ecdhInfo": [ {
2026-06-25 09:28:54.545	[RPC0]	WARNING	net.http	src/wallet/wallet_errors.h:1014	        "amount": "0979ea327b6017df"
2026-06-25 09:28:54.545	[RPC0]	WARNING	net.http	src/wallet/wallet_errors.h:1014	      }, {
2026-06-25 09:28:54.545	[RPC0]	WARNING	net.http	src/wallet/wallet_errors.h:1014	        "amount": "eef593e8c2560201"
2026-06-25 09:28:54.545	[RPC0]	WARNING	net.http	src/wallet/wallet_errors.h:1014	      }], 
2026-06-25 09:28:54.545	[RPC0]	WARNING	net.http	src/wallet/wallet_errors.h:1014	    "outPk": [ "ab5ef73d02c88d249602d295f2c3a227040312223cdf4f2a3c683e4604fb70ca", "02c04f50b820c6b69d507cd27249fd7ea1e3b2b9d35cdd795280ce42fa276398"]
2026-06-25 09:28:54.545	[RPC0]	WARNING	net.http	src/wallet/wallet_errors.h:1014	  }, 
2026-06-25 09:28:54.545	[RPC0]	WARNING	net.http	src/wallet/wallet_errors.h:1014	  "rctsig_prunable": {
2026-06-25 09:28:54.545	[RPC0]	WARNING	net.http	src/wallet/wallet_errors.h:1014	    "nbp": 1, 
2026-06-25 09:28:54.545	[RPC0]	WARNING	net.http	src/wallet/wallet_errors.h:1014	    "bpp": [ {
2026-06-25 09:28:54.545	[RPC0]	WARNING	net.http	src/wallet/wallet_errors.h:1014	        "A": "a235178bcd536854a5a51e44b689bae5f64722cfbf3ba8de8cdc3754dc10368e", 
2026-06-25 09:28:54.545	[RPC0]	WARNING	net.http	src/wallet/wallet_errors.h:1014	        "A1": "b0c785710f55cf03c2b3f240f7e778498ab62b5863f72741d9ce8e76117a20bb", 
2026-06-25 09:28:54.545	[RPC0]	WARNING	net.http	src/wallet/wallet_errors.h:1014	        "B": "511b6acc12b24a8fdfe84aac8d0e3d38c89d4b897b4586c5da6a47a62751042d", 
2026-06-25 09:28:54.545	[RPC0]	WARNING	net.http	src/wallet/wallet_errors.h:1014	        "r1": "b2a377831a193093c857920041c3fa289c6cc008ca3e60a9c58f78793bb6a302", 
2026-06-25 09:28:54.545	[RPC0]	WARNING	net.http	src/wallet/wallet_errors.h:1014	        "s1": "ea80f9be88ba735053ddae7ee6bb943268b0254344b42d5a0d7ad48c26173d0c", 
2026-06-25 09:28:54.545	[RPC0]	WARNING	net.http	src/wallet/wallet_errors.h:1014	        "d1": "2d08fefb26b959d05820f289d6a917cabf27f2b59506f2e415e1a9ebadd17102", 
2026-06-25 09:28:54.545	[RPC0]	WARNING	net.http	src/wallet/wallet_errors.h:1014	        "L": [ "f0fd8ca3bdf64be634dacce00c04c74160fb8813487b7ec0f1aca3321cb5edc8", "a53448f293a759ca5bb9678b13f698c79a595ffe4397a86bccd91dc64281ea88", "c6b2ca38cf1f16a10eb8360db0bfdaf7b2427d85d89bd5cf3a4ae99b7ab1b39a", "24a44a63cc3f06541b310c3536363773f6f5e50d16094f209f1aebebaa90a8b8", "f93c9852d62f8df73827bf65b718d95f07d017ab7bf3b6538b6dc49aaeebc6e5", "d8c4e884d7f3e9c054b014893834de00fe8ab41c8df7e0222cc98fe45666b240", "b78ee530eeeee2a93c6481c9310432a038010c70abb9aae77065d6b46e1c24ae"
2026-06-25 09:28:54.545	[RPC0]	WARNING	net.http	src/wallet/wallet_errors.h:1014	        ], 
2026-06-25 09:28:54.546	[RPC0]	WARNING	net.http	src/wallet/wallet_errors.h:1014	        "R": [ "5f75f8803d087e4dd24280cd8929904cad7ef3121cb534cb099980fdca10f918", "538493d4d5db390923e9c1001b661072274bc939658b931924091a5edb71c579", "1c7675f249cc5ca650738302f23f4d7b4bb0fc79f597277526ae2399265f4a44", "b9ca1851072973af438ba7559e029f74a4cde5e29adbd789f42d2038f576ee3b", "e2c6e6d7f051c3e5a253c2e964b4d05fd2d776458417adb42df5090673424c13", "356a0b8d068be25f39dd3a1fe3d73eb08a40cbdab36aa184034cdb2f6de66de4", "9c435b318d4b36751919333adcc5745774dfe95b5c925d3c870ad2232f050e8e"
2026-06-25 09:28:54.546	[RPC0]	WARNING	net.http	src/wallet/wallet_errors.h:1014	        ]
2026-06-25 09:28:54.546	[RPC0]	WARNING	net.http	src/wallet/wallet_errors.h:1014	      }
2026-06-25 09:28:54.546	[RPC0]	WARNING	net.http	src/wallet/wallet_errors.h:1014	    ], 
2026-06-25 09:28:54.546	[RPC0]	WARNING	net.http	src/wallet/wallet_errors.h:1014	    "reference_block": 3030418, 
2026-06-25 09:28:54.546	[RPC0]	WARNING	net.http	src/wallet/wallet_errors.h:1014	    "n_tree_layers": 6, 
2026-06-25 09:28:54.546	[RPC0]	WARNING	net.http	src/wallet/wallet_errors.h:1014	    "fcmp_pp": "7d1daec21c2eacee7b5c439d134073ddb098d17ac4e6f31492c6a20ef9dd4019be17c04a60a3c58a40236e69a933edf512313ee5d123101172eb029715a9899478c1a02d249de6064e3dae4d7e3ccea2bf789b6e712bdabd6946ec2ebcea49dbb0fcb8d6d80b6cadbc25043910ac11726b4c912726f2fa3518d120955226745ae776365057985c8873d013140d35cb5fc1de9a35ea8f9e1a473a37741f40e8e4fa46cc487234ec9ce5117477f7d268f42bfd442e4abacca576e1e5ecbbfa85bd993f449f41a1f6c10c964d03ec0a963b5ae16d041e8475137b5ac6caedd1f487d3cce3b1d516854a637ffb7ba248905b790994126df796fb8beae8d90d451f6fd22379d32bdcb49d679f528e4170baf08929870efc34a563f4367eb86c08209712c6f4c82ac415f24a6313d29bd150ba5267d82fa4924a5f14c0f52640d34a0f0a7b4251b008e7a9bc5b3d69a55fae46511b05d386fe5b4619613dad7cc2a40a5b0b3bc565290995a85f2303aaf6baefd49f5b299845631607d4356fb3a8de08e88e942b1b7dc392ba05ab978f1686cdf58d736ecbb3711de079a7845af93108b85506cba771851976a82a56afb2df451e5dce0b392143b6089303a78e4a250a9a6f9eb5e53a7438863c504e5788943872656fdbc8d3a4971a3d0b96e4a66904dc7eabc864ecea72724f07ca48fd6ff625865589b2695fa5bc8212afe566676f928f5d5ae000010dfd4c7d6634ceb4bc8743aadd4369c1ce576733410250bc72d293d93e31c8975f8fb5c16144b57010df8a6a58d405b4b631ecc502627d543150ba7a118410b61264bf86eeb5443d5f98f1ec7049faa7253d510e54619989802b3814288e2d0129dbdd44fc7306749b11a7daffdadf02a5219268b53369d5932e1e7b3c127c75a985f696733b519a77eac05223e1820b702c20f0f246d6a5980a89cd90904f60bf55a8e7966f5bcce3605a06c8b4a6fdcc5d3e3afc1ce454b2abb72096ee8454129b5391c966d5f15d0a1088a5426b76cf040865768f9d6d12c96c1821685983d2ee606e86f2350630ad0617e59ead27c84528451abf62af0c3beb0289c135a605e104f1e3122d02687fdc64ce1378db807241d6242874eba85ef4fef86caf17c7204a924a913634843f07570d49a3ca59a49816151e63e4cde9d17a643eadbd7e4f9fd5cdf20b46ac8e252372fbb5a7f65c3ae6f2963cf384a32188fb28024d37a0e63c6ca15bcc1ca0aa6eb31756e0d660ba1ea9832ecdb5e69ab2f57da6027e3b1cd016c0515ac01dbf9c908d683d7d2f7b04c97122da347650d02764a1f44137db717e7388ec7a740b8ad9408dcfad1b543f7bf5b12a3be4e3aea969c52011f5382163fc913a4dd387e82443a7064b4eb38d7f883a73284d5deceb849df0a3e7140960936ce2417926b66a69ff6c24c284a31e2114dff231d0b411ad1794883e0700b52392c57b4d1d93313d8b465124fd7152ff8dd50e1a920356caeba5c83c0d14bbf41b26f58ebc527dedae4319d90fbfd13f1405cbac5311936a1d220a640310d0bfb99d1bdfa5bc5ce57484bca2c306e28a34930ea5672bd82fd48372507ad5dd9695c9bcbf554349884117a15d4579ae4e5e256a0e07bcd8204c7cf4c90c9f70679d833d585adb48325470a6373d670ad934f3fc26a3d5b0037225d1f1b23a2adfdb7a3207fafd33fb942f9bcf0db5977d3904711c4a630d37171e1fd0c38ce2b718ede6fc3047df5091494645b7fa16e89dc272321180ad11eb9455d9789ddbfb1efc8ce933f9df904a0e147e1874952b520a6ef08c656cf868adf1bb9e5addf84522f316947f915824af96382174ca493085de3f9a7559c056f1a4c15e633d6bab182c76e5d31ee5479ab47b5fa60e178d3f5ad6c776dd6e3f263906060de08a0475d79e362f7ec1105ef2de38e36daa4d19e4ac8bc43c9f64669d70c2dd84aeacb0dce5bd7e97595a38b8e19225808d9520cc18f75b4e0ff3ac1660dd5c1bb68725b42346d6e0654993d46d96e8f0da666caef2d87014e2944ab3e14cf50201bc8aacdef781a68d31e3b5b1873a6e5a25d83604c2af8b3514affc03ed0dd31815a7fc67cf34abcf9089e05f727c6cccc8b309c0c900d53b7dce0f0939a7ce30cc68bd0be6db3334ea0bbe0c0b8eb1f174938b60d963e961d1cf2d5a482d96a6b7de78c725218d54d64e3d159501e916b8e32e563f14037317fcd578328f0db2d54cffccc4179472047894b2931645c9ce2a4b75827164b3faa19c5b9a1081541332084eadacdd95db7c5b500847bca647838700f1aceb3d904555913af4fd129970dfeced3f57f7ac4dbc03ab9eac628854770c71494cb3618168804f20e8f0363a39786c0403fe939e26531a05ef13f9c0d3c50fff158117261960e17ac97e25857399ba691f4f1e5ab7a25a08a6a802e66807ce9280c77b60ef64029b8661f083cd75dcb201d3269c257a41a3de9ea086789e1d08610b6d88b6e188c0bd4b768896dcc22bdf42079630aafd83d23059c6f9ddfe9d64f8dd726d29cc3e9275d0382e81860d57f616ca58f584f8ef9c1760f9aa7bd6d2162715ec8557d332f9ad1bafbb77527feef1301efe89ec9184c21182f8f4340d968f92922fcdaa53638ac99e6d8d0517059226751a0f1029bd60b495c646bf6406301b036172c77b0dcd8921e667af2e6dbcf39e6e1606f32ae6acb55b9f14fc92d7d4b940877b834d9f37de17d4061731d9a33d191ddbbf86ddfb5ca2d446bd02b5a8f271b3802de29f480fb564e6cf6a1b48e7ff1dfa41b2ba4537033b34ab1a3735ad7ece99de4ea985426ebd7a136c7b9b384c21edc820b8a71a1176d4dfec04b5bbfbc6ea1cf19594eb3097cbb35cd5744a4f10aa711ba49cb4475ffeeb6339bc0c0d8d095e6f9024419696cea833802484e5954a9be4af753f53f48f5b2f8ab1c5387ffd8d57552f8f1f0ca6ba3753f07ff3313823a1b5b155a76c3402a8c2126e3095a8515eedfd0dd424ff432fad812694956374448df1feb077b1ff2024cc595190ddec43efe5dc8aa043b8c5fbba9c0ea9bccd0b7d73308a01eb536bf22de085f42d9aaec1e759a61a3b38a2e58829da4dbfdd4a9a0eabebb4a639fa9fccb435205953afeb29d1886086b04d553cacb8be502800f5589c7e4b9d2cf59b73f78c512abbf0087175f269ea3f2be63bfd7e5b748676497241bc747c2f3ac7f73dbc4f2d3dea80da346adb9b50b87a5e7bfc1ea73bdf1a67f55b46bf1ca65f7487085bc106ef6945914a7473d741c78cffe98502b984b5b54190930e1f8ed45c3cb85442e31ecf788f8787468f14b387d7740694ed0effdeed2e805ee04a81c44099a69be471802e01efcc04677163b939b5fd030bae99f557364772bfb0a6795e14481de6b5fad7b346d3efa756c190585c3b00335d7e89643654da66c9690bf416fd95898f32ca5920a849252cb9d7c466d4b5c6283bdb9a214021ca48f5865bfaab3a529150adda487beaca2b42a9ae720fda9fe4152ed11ca277482edcd23ac5e9a736e600694aed10bb4e857b6aa1e8c3e49e3a3032e43634251ab16af83acafa3209d69274a3826eb54a9dcb11a50a9c6602a03a0e40758022da56246bb7c2761d0eafe450b7e61983c75edf8b47f1182f7c18e35953821f3a39237cfc0da190dc1ff7b1de9f5a1ea4aaa3f0511fd5729b112f423112d1d11bf38d4b126eea3f57e65dd3709d9698ea9991da397bc32abe1850e132973732f5b3868c963c5bdcd38459967535673d45ce9e56d0b2643e3921abbcc9cd536d98c9c1dee8af03a2501643f65f49962f6518e4f9a3a42f761b700cea22833c9cca8611eeb1dbfb7f7da0de09c7b879d47a937422bf671fbb7e0cefc9cc330f1b59394bfcfa2d12b51809b3736e01f338f6dfe1f8412adb29e1aedb4d0ef8047f3467f9e5444152603b7a6cedcb2b47e6aa244a669749bfd148a8f0c044bd2c2944f5a6bf115c962dc19eb599911d3f53dc29ec25a457745ab42269e3546b4cf83e87e6cf2adb7f03b10374f75a1ca4b629600477627c85a2fbb48107874787eccdf73c05d6032e49e745063961393c1aaba474a7dadeeec9e922f65dde754218db7efb50dce5c0fa330423ba274bee095886898cddef6d44192971a6608e388c0a36afc631caf33c11b91da9dba625511f1e856bda3b6eb29e87f8ae0a083dce43bdc5d5a4c62c079f622a3983df27c3c30912ec7e038f24061bd86fa71306f1d27c5c4717a38b860ae227ff46785fc376a883207dde96f19dd67d9afe50961ace5084274713dca8dfe994638a8862519f7321f47ba0e95bc943bcc09f019f0aac0f1347c94b6bea5090eba97e2c888e2dd3a5f18fe9133b0b06d1e6fd71475727d06a6bf107d6582848329e2552d9f96992ed8e761f7db6543f700691c046660d4f960727330a04ae5e783ee9a2074842297caf061bf1b6d1cbf4564d4a9cebc2545294c584d97ab75bf9bfe192c72ab50b7ab5c119db872076a80d3c7a808e890f33d3a8cf04ae7d5cea666fe3041755693f971ec0b8073543e4b4f6a653c94f27b3a5ead5e349104cc905201bdd9470a8b425dfa3d74fcc6780859089d12ed9c22c9c2db1d43d9cd45033b00bde8f527c77107523936e4bec4544ce34ba4baedf354c3e494a6b83e4dca3298c59bece0c1deada84fc835c608bb65074445e01e796130a02fa99ed22538b90dc74ad06319f89915d1a867189afd1dc4cd0468d0f4a404956f0f25b323c1c7d879d12b2f58635ab3e9cf1d666d57b33108daeee69609ddb036138bc017a86349b66f767f52c733769d40e54eb37d926dd5584148ab17eb4bfa24d03c5c2ab5aa83801cb882ae9f1fcefc77d96eb06cc495dc84970584299ff7150edc909af66cb4be1449b90833c9ec6a546c84c57b9b295e70c8157363f30d8f248ab0457c6c780d726c3afa674f2300db2c51fa123d489adf78cdfccccd6f88eb7ea65f749bef1a80004c1a80f187ac46bce0a23b2a9ecc8de573be0cfe1f18cc1c7d238ea2f33380f355a5faafe4af59c19551c5d177a8646b34c324341ac153cf744c6c3bfe98de3c8366700abd2a119044e55b6fdc97ec6706f32e365cca040f34c00ece7282d8ffdaa2ce3029b9153b1b6e3151c4ee24b47869b1c28dbbea59c641a758daac71a91886674437f39587335f67f49e649884e792554cfe5437120cdd7c124752b2ac54b2271b68b1ea588a3f4a2224a8e996da4c48cb34753d0853f5d063266f007a25a9fd1f6425839b92c07e86bc944fb84b0d8d450524bb0f49eb46ed1cf17b713f1fe507eecc672be58a77fecabfb2da909c1363a66f2980cc83e85cacdff77c4b493cb57ee6c07713c54ea8fe4eeaaa9651594a518e5538038bd8c7298286ed0247b4650df8512a8cdd87b2a89a8f33b6d33f963378ef5625c75cb7df6ff46847551b7938ddd9d4ec9e3b00da2f758a3ec83d4c611feda07343274d47438361311d3307c51b3c40f0eb68f38d3ebab199f445394f8d904a8a6e78d992b3a692baf751a937c5058e3d60d0c3fa64ddd79bf2e2818a8a05661d50f8ba27cf7364bdc63c90888349e4e1c5410f5494566838187d6030756ce6b1f238d94059f0a9c07f02655c62d25e273f8505db216b5f0643e51aafbb3a3ab7883127dbd505b3c8ed3e790aa37fbd6f0651532c8278deefde67c6f5417a26980349fba0b3f4b2877ada1305133a0a5807a609afbcd24250c5fc65bf12c4d0e311a3e5a779c719e278cd7346e296db5feabb96b342cb93100187287ca1bfe8db8b5a8d4d1241027fb7e58b21c8c809de23ee61e99156e59663dabf40761f58e7a047e528816fd531ffb9a6cd26eff246d5dd0c71df7f6ac057bb640c4d40e71794fcc4cc53bc576ff0a8632aab3fb52fe75784f4cd6ec7417b65977b614e866af11a9e2cb7f0c2be833661db3824f45220587061bf65d2e79b22791c07561c646f02ee7d40134077e5a357ebc2828be5a0d2f758a8fcbccf4eaf5b5ca102a9e6be0c6044c1a82887eabe18612c322bcab3477dd6afaf386a2e19b18eb059af4a7337d662536aee832d182c72a61df30016065efa598532009f6b1243296e005d447e3401099838fa6a593c4b68a6f3d674b7b57e5b7b5a4da0b455227009c6126a3d23b86f286ead47fed30272d498691c3faad8cd0bd04da7c7879559b379c203218f1a53a4245fa290ded57c3c965a19c9991676e51ba6f8f5c2595b746d532abc83579139bc758cafe8860b74844a3080d556ef24f013ea39d6f712448d98173cf76069e28e916054326d2cd1d475e3b975ecc03d72dc9c1e6d94950aa6034119b0ea6d59354b2788f491c5845049a7ece6c2b78aa6ff697e0e7d4e678c23054f0e1af3ca3df382a97ee3f86930092be76c373cd874b8da6ab49cb50be925ed6e61198acf9643db01b4e526fed411526a2405c88e33c6910e3f0bee108b8987483571c6a37bc5e43d0254a70f3519e029ddf83b97daeebb5fae995d80c47236eb33f9fc66927743cb920a28eaafd3c8545e2810efb84fa3e2af73ccc116e4be9e0dd99842990e3c11e73478df91f240dc2de560101af467c3c6c5c941e8f961736b9028fa843d85147b0f62e7ecfc42e3f77cd9aaefd2af1db501dd75c5664144bd0dc7e4cb6f9d14592d17bc2084aed27ab7f00de199b2e75d064cea4fe74b00f96f5881329f9cb22ae549a79957e9323e50eb8c4607bfeed04b0a7edbfa212ef768feec5062e0607dc9432c271d0aef018a2b65ff40cdc227f37c423dae804806b9d6066cc7cc8c8f2a092c5db2156a35c50fc986d38ac060ca1ff92ba102b5e700927dcc438d4a1e2a2539c528934f415b41465b882147c59040c5a1079ef7cadfba9c6b0dcb7fef462a9e2bc9c6c2aee05e209651128e3bb3986e75a627293725014c2881f66ff8e7b33679e66fe3894d840d5e5c8ffce1c26b776f8c811640bc798af7dac74d73862f8b414d35ccad31fe02b353c5a5192f730046fd6f3e28746f54c41843f5cd8c7833d0d41618aefde2285fa6d578e7b7d6370b0e1801dda3b5bb4e737525725d62a04295113ba1025d08b52270b9b0c4b2efae940bda5cebf90187f2b284c3326c3cf3fef39b8db6b246ec020c96ed97b251c25dd6f7cb6eb4efa79323741301a7baff1dab016a0611c0246ad84c8c7963ef73ba758e40361839b817c9748217af36f876597aa4e68a1ab0a5b794f0accd911045a5e46c4cc8522551d32edeb3587b94f94d75c5b4d32da50ee83a72623ff9e0ff575d201cfeb39e1a904269e28c4cb3b2385431b6b4acdaffb75cb5e4003593dd1c9d938cf48fadd29ad00d8b6904b12b7ca09c54939502cc7b1f1a0d98c74b7853384874313d656576feda2523c7f8ca43fd5fa6462f2e982c39dd982f339d6819e5b1f948180a8ceef49a61d2bc2bda7335ea4e0d04b34a67e6b82c54f04ee9b783c81c467c1bff7c1e46a54fe488b0b0566168f5bf582619979d34a4e5cc4257184f6cc3628ef8b28d38961281f62677df6e4ca8306ad076e43b1d8c5b9c7e531d26974e081702493a054d8cd53a391203c7d383a34b09966c2764f37cb18be71001970f96bde191377c3f04ed03ae6497306324a0cfaffb757e3462c7a83eec67a52d4243c4230b7bf3bbf6bedbf524fedd6af9c6b7658185cc7e1f0bc453d214d7493a40a008fcc66cdba81248f62f833801cf031e36f8192395fac1b6d9d3d69c4f6e9559959e246b610994d15f04573e002a6dfb454b741d6ba0c8ca8b8fe33c0b84d874f4d8fd90bdc0480b658fb1579a8cc1d98c7a8520a5f1d62ba33a2d56babc21cee7f8e86154c83d39efb836eda497b36c1f24c6306511795eaa93c551bf9c5263f794c0da590ba51cc1bfabff8dfa97b733330706f07c6f1c708bee199c641924ba47e88f0d4bb38fe0f5b7c9a45e9d481e5956ffd37377b520f52bc945cad9b5dac4b2c706b87cf1064edd8443ceaebdbbfc98e427cd4a2e57cdb720d9f0525ac0da6799b7c89b50ad709a25a8c8897e204582981056fb7c2bcefcf8826dfd6df69c2fa907a8b6691f789ba22fbb92c2edfd53fc7d4e6b306c2ee168a3219410e03f9e63d66255a734d18d33692f196a54c5d7c15c7c1720438d5d5cd03d13446af599a10467869569541cbefa080796a3a7a0398d62e848a6c81c33e3014d4d2ebae6b22af005a7e486c79a12b530fe2b3ba93de1ad86b10fda712a51cf6d4af30bf3e046d3692b61e2b09f425fa9b4754d862e9112783c89b51d02fbf2735d8762742ed33692aabcb91352ede806f986c5a0e1ff7ce6293d9d8426030f16fcf80b567b7ac591eeb518a2ed5fcada587645263ad3d1b43f27eab89675c08b3cfa3cf73f564983fa3fdec5d20b3795c53417fc357b1d5ea99c2d85ec1272827423f3ed33e92e9360d82a29695878d0bc6ecf6692d3a90cb17155e0f2c415a7ce4ddd575553a517a93a2a776d7d3e24c407f1c69dadca750915d38cad69dbf5fe4c203407c4314f9b38046e4e95ef38d24ccff12d1001f3e3c94fbcb547bb4f3dc3aacd7e1466a5e46b6fed3becf99ffb66c944c101cc071b9fe16bff203edf290ce6e47899b83f3f9a866fe1e0dcaeb2545fc9e9b5454c7f78f15f23d5c83261c9f29b3418d80fc90ea8368d89a3dcbcf98566d849709fc9b1130177c888ea22da342b56621ab2226f99067e8494fc7dc72d6b680c4a05a803c505ee61014eb55fb09226061de43e071f06e3def915fc118fefbea428823daaf7babb7a7b231c1cf5f2fcfb55bce9600eb3b2388509fb2081fa8a861d031d8159fd30934906fe397727179b5b1fe4960e6acf422d1bc12a81c17941a5d5bdce4d1b91d488e7f0acfb70858c40f9b4f36e6be21", 
2026-06-25 09:28:54.546	[RPC0]	WARNING	net.http	src/wallet/wallet_errors.h:1014	    "pseudoOuts": [ "bbc9323bd1e43285b46ac9bd898abb552c1f57e8b7548b98185314fbe2709ec7"]
2026-06-25 09:28:54.546	[RPC0]	WARNING	net.http	src/wallet/wallet_errors.h:1014	  }
2026-06-25 09:28:54.546	[RPC0]	WARNING	net.http	src/wallet/wallet_errors.h:1014	} (double spend)

```

# Action History
- Created by: j-berman | 2026-05-08T22:13:13+00:00
