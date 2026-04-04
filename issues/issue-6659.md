---
title: Cannot get Block Template
source_url: https://github.com/monero-project/monero/issues/6659
author: 1rV1N-git
assignees: []
labels: []
created_at: '2020-06-17T06:03:09+00:00'
updated_at: '2020-06-18T08:43:50+00:00'
type: issue
status: closed
closed_at: '2020-06-18T08:43:50+00:00'
---

# Original Description
v0.16.0.0 release 

2020-06-17 05:44:29.061	[RPC1]	INFO	daemon.rpc	src/rpc/core_rpc_server.h:148	[127.0.0.1:55670 INC] Calling RPC method getblocktemplate
2020-06-17 05:44:29.061	[RPC1]	INFO	perf.daemon.rpc	src/common/perf_timer.cpp:120	PERF             ----------
2020-06-17 05:44:29.065	[RPC1]	INFO	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:82	Tx not found in txpool: 
2020-06-17 05:44:29.065	[RPC1]	INFO	perf.daemon.rpc	src/common/perf_timer.cpp:156	PERF     4356    getblocktemplate
2020-06-17 05:44:29.066	[RPC1]	ERROR	net	contrib/epee/include/net/abstract_tcp_server2.inl:427	Exception at [connection<t_protocol_handler>::handle_read], what=Tx not found in txpool: 


# Discussion History
## 1rV1N-git | 2020-06-17T08:14:40+00:00
2020-06-17 08:07:41.782	[RPC0]	INFO	daemon.rpc	src/rpc/core_rpc_server.h:97	HTTP [127.0.0.1] POST /json_rpc
2020-06-17 08:07:41.782	[RPC0]	INFO	daemon.rpc	src/rpc/core_rpc_server.h:148	[127.0.0.1:58170 INC] Calling RPC method getblocktemplate
2020-06-17 08:07:41.782	[RPC0]	INFO	perf.daemon.rpc	src/common/perf_timer.cpp:120	PERF             ----------
2020-06-17 08:07:41.783	[RPC0]	DEBUG	txpool	src/cryptonote_core/tx_pool.cpp:1346	Filling block template, median weight 300000, 15 txes in the pool
2020-06-17 08:07:41.784	[RPC0]	DEBUG	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:601	DB map size:     100155748352
2020-06-17 08:07:41.784	[RPC0]	DEBUG	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:602	Space used:      89840316416
2020-06-17 08:07:41.784	[RPC0]	DEBUG	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:603	Space remaining: 10315431936
2020-06-17 08:07:41.784	[RPC0]	DEBUG	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:604	Size threshold:  0
2020-06-17 08:07:41.784	[RPC0]	DEBUG	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:606	Percent used: 89.7006  Percent threshold: 90.0000
2020-06-17 08:07:41.784	[RPC0]	DEBUG	txpool	src/cryptonote_core/tx_pool.cpp:1359	Considering <7f95052d0cc80766f7b5fd8b8741e1e691c574959c72c5672c0714b7912dfe21>, weight 1772, current block weight 0/599400, current coinbase 1.615125161952
2020-06-17 08:07:41.785	[RPC0]	DEBUG	txpool	src/cryptonote_core/tx_pool.cpp:1450	  added, new block weight 1772/599400, coinbase 1.615224651952
2020-06-17 08:07:41.785	[RPC0]	DEBUG	txpool	src/cryptonote_core/tx_pool.cpp:1359	Considering <2de896096cd80ba561f5b2594bc3ecdcc7c3841b1ab644ba15073ab959408ce7>, weight 1775, current block weight 1772/599400, current coinbase 1.615224651952
2020-06-17 08:07:41.785	[RPC0]	DEBUG	txpool	src/cryptonote_core/tx_pool.cpp:1450	  added, new block weight 3547/599400, coinbase 1.615243771952
2020-06-17 08:07:41.785	[RPC0]	DEBUG	txpool	src/cryptonote_core/tx_pool.cpp:1359	Considering <66ba2a4f267be9609c352eaa00a515c2290eadf51c8651cc6748f3050aba67c6>, weight 1775, current block weight 3547/599400, current coinbase 1.615243771952
2020-06-17 08:07:41.786	[RPC0]	DEBUG	txpool	src/cryptonote_core/tx_pool.cpp:1450	  added, new block weight 5322/599400, coinbase 1.615262891952
2020-06-17 08:07:41.786	[RPC0]	DEBUG	txpool	src/cryptonote_core/tx_pool.cpp:1359	Considering <fcd98e547d02750fb4f1a807ff6bc82f4f0dd82fff70b9c85166a69127382f60>, weight 1775, current block weight 5322/599400, current coinbase 1.615262891952
2020-06-17 08:07:41.786	[RPC0]	DEBUG	txpool	src/cryptonote_core/tx_pool.cpp:1450	  added, new block weight 7097/599400, coinbase 1.615282011952
2020-06-17 08:07:41.786	[RPC0]	DEBUG	txpool	src/cryptonote_core/tx_pool.cpp:1359	Considering <456dcc754d906b91835f6080a9c519718d8dd87f240ccef9a791243833ea64f2>, weight 1776, current block weight 7097/599400, current coinbase 1.615282011952
2020-06-17 08:07:41.787	[RPC0]	DEBUG	txpool	src/cryptonote_core/tx_pool.cpp:1450	  added, new block weight 8873/599400, coinbase 1.615301141952
2020-06-17 08:07:41.787	[RPC0]	DEBUG	txpool	src/cryptonote_core/tx_pool.cpp:1359	Considering <608fc66221538f126b53246f0ccaedf0e8232735a44f0728c5f38914b0bff0e1>, weight 2608, current block weight 8873/599400, current coinbase 1.615301141952
2020-06-17 08:07:41.787	[RPC0]	DEBUG	txpool	src/cryptonote_core/tx_pool.cpp:1450	  added, new block weight 11481/599400, coinbase 1.615329231952
2020-06-17 08:07:41.787	[RPC0]	DEBUG	txpool	src/cryptonote_core/tx_pool.cpp:1359	Considering <9c200a588535df6c407bfa57060af1277fba6ef28c840bbd8b4ee85a54a6965f>, weight 2611, current block weight 11481/599400, current coinbase 1.615329231952
2020-06-17 08:07:41.788	[RPC0]	DEBUG	txpool	src/cryptonote_core/tx_pool.cpp:1450	  added, new block weight 14092/599400, coinbase 1.615357351952
2020-06-17 08:07:41.788	[RPC0]	DEBUG	txpool	src/cryptonote_core/tx_pool.cpp:1359	Considering <403c5e73b31480d0a71b3db2c1b78ed3c0a9a7f9df042598dbe3f46aa65852db>, weight 1771, current block weight 14092/599400, current coinbase 1.615357351952
2020-06-17 08:07:41.788	[RPC0]	DEBUG	txpool	src/cryptonote_core/tx_pool.cpp:1450	  added, new block weight 15863/599400, coinbase 1.615376421952
2020-06-17 08:07:41.788	[RPC0]	DEBUG	txpool	src/cryptonote_core/tx_pool.cpp:1359	Considering <5489284e118bff04aa85e84a8a0f90124ea9021bc66976af78cf6c3f33700755>, weight 1771, current block weight 15863/599400, current coinbase 1.615376421952
2020-06-17 08:07:41.789	[RPC0]	DEBUG	txpool	src/cryptonote_core/tx_pool.cpp:1450	  added, new block weight 17634/599400, coinbase 1.615395491952
2020-06-17 08:07:41.789	[RPC0]	DEBUG	txpool	src/cryptonote_core/tx_pool.cpp:1359	Considering <f628489d7d30b87c24fbc47e5aa8c4511fe5d80a081c9c06f8afe81746f66430>, weight 1771, current block weight 17634/599400, current coinbase 1.615395491952
2020-06-17 08:07:41.789	[RPC0]	DEBUG	txpool	src/cryptonote_core/tx_pool.cpp:1450	  added, new block weight 19405/599400, coinbase 1.615414561952
2020-06-17 08:07:41.790	[RPC0]	DEBUG	txpool	src/cryptonote_core/tx_pool.cpp:1359	Considering <334cda8a27ff5d5d4b9c938b53ddb405cd8f829b4bb2bd1fae84484cf8a0f65d>, weight 8416, current block weight 19405/599400, current coinbase 1.615414561952
2020-06-17 08:07:41.790	[RPC0]	DEBUG	txpool	src/cryptonote_core/tx_pool.cpp:1450	  added, new block weight 27821/599400, coinbase 1.615505181952
2020-06-17 08:07:41.790	[RPC0]	DEBUG	txpool	src/cryptonote_core/tx_pool.cpp:1359	Considering <adb15c1eefeb0f8e5b1dc9dc9460e991023104b622fb5a145dc158eb6fb4f12c>, weight 8416, current block weight 27821/599400, current coinbase 1.615505181952
2020-06-17 08:07:41.790	[RPC0]	INFO	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:82	Tx not found in txpool: 
2020-06-17 08:07:41.790	[RPC0]	INFO	perf.daemon.rpc	src/common/perf_timer.cpp:156	PERF     8252    getblocktemplate
2020-06-17 08:07:41.790	[RPC0]	ERROR	net	contrib/epee/include/net/abstract_tcp_server2.inl:427	Exception at [connection<t_protocol_handler>::handle_read], what=Tx not found in txpool: 


## moneromooo-monero | 2020-06-17T10:22:47+00:00
Try with #6648

## 1rV1N-git | 2020-06-17T11:39:40+00:00
Thanks
I built with this commit
I'm waiting a day for test


## 1rV1N-git | 2020-06-18T08:43:47+00:00
@moneromooo-monero Seems ok

# Action History
- Created by: 1rV1N-git | 2020-06-17T06:03:09+00:00
- Closed at: 2020-06-18T08:43:50+00:00
