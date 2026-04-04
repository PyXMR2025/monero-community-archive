---
title: 'New crash with #1599 due to `Exception: cryptonote::OUTPUT_DNE`'
source_url: https://github.com/monero-project/monero/issues/1611
author: ghost
assignees: []
labels: []
created_at: '2017-01-22T13:55:24+00:00'
updated_at: '2017-01-22T21:23:01+00:00'
type: issue
status: closed
closed_at: '2017-01-22T21:23:00+00:00'
---

# Original Description
Built #1599. Ubuntu 16.04, ARMv8. Here's the whole log.

```
nodey@odroidc2:~$ monerod --detach
2017-01-22 13:54:33.784	      7fb5244000	INFO 	default	contrib/epee/src/mlog.cpp:143	Mew log categories: *:INFO
2017-01-22 13:54:33.785	      7fb5244000	INFO 	global	src/daemon/main.cpp:265	Monero 'Wolfram Warptangent' (v0.10.1.0-39aaea8)
2017-01-22 13:54:33.785	      7fb5244000	INFO 	daemon	src/daemon/main.cpp:267	Moving from main() into the daemonize now.
2017-01-22 13:54:33.786	      7fb5244000	INFO 	msgwriter	src/common/scoped_message_writer.h:94	Forking to background...
Forking to background...
nodey@odroidc2:~$ debug
2017-01-22 13:54:35.430	      7fb5244000	INFO 	global	src/daemon/rpc.h:63	Core rpc server initialized OK on port: 18081
2017-01-22 13:54:35.430	      7fb5244000	INFO 	global	src/daemon/core.h:74	Initializing core...
2017-01-22 13:54:35.431	      7fb5244000	INFO 	cn	src/cryptonote_core/cryptonote_core.cpp:233	Locking /home/nodey/.bitmonero/.daemon_lock
2017-01-22 13:54:35.431	      7fb5244000	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:318	Loading blockchain from folder /home/nodey/.bitmonero/lmdb ...
2017-01-22 13:54:35.432	      7fb5244000	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:468	DB map size:     16106127360
2017-01-22 13:54:35.432	      7fb5244000	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:469	Space used:      9464995840
2017-01-22 13:54:35.432	      7fb5244000	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:470	Space remaining: 6641131520
2017-01-22 13:54:35.432	      7fb5244000	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:471	Size threshold:  0
2017-01-22 13:54:35.432	      7fb5244000	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:473	Percent used: 0.5877  Percent threshold: 0.8000
2017-01-22 13:54:35.433	      7fb5244000	INFO 	hardfork	src/cryptonote_core/hardfork.cpp:197	reorganizing from 1210026
2017-01-22 13:54:35.700	      7fb5244000	INFO 	hardfork	src/cryptonote_core/hardfork.cpp:206	reorganization done
2017-01-22 13:54:35.700	      7fb5244000	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:504	[check_and_resize_for_batch] checking DB size
2017-01-22 13:54:35.700	      7fb5244000	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:468	DB map size:     16106127360
2017-01-22 13:54:35.700	      7fb5244000	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:469	Space used:      9464995840
2017-01-22 13:54:35.700	      7fb5244000	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:470	Space remaining: 6641131520
2017-01-22 13:54:35.700	      7fb5244000	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:471	Size threshold:  0
2017-01-22 13:54:35.700	      7fb5244000	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:473	Percent used: 0.5877  Percent threshold: 0.8000
2017-01-22 13:54:35.719	      7fb5244000	INFO 	blockchain	src/cryptonote_core/blockchain.cpp:380	Blockchain initialized. last block: 1220104, d12.h21.m30.s45 time ago, current difficulty: 6408835023
2017-01-22 13:54:35.720	      7fb5244000	INFO 	checkpoints	src/cryptonote_core/checkpoints.cpp:204	Blockchain checkpoints file not found
2017-01-22 13:54:36.081	      7fb5244000	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:504	[check_and_resize_for_batch] checking DB size
2017-01-22 13:54:36.081	      7fb5244000	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:468	DB map size:     16106127360
2017-01-22 13:54:36.081	      7fb5244000	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:469	Space used:      9464995840
2017-01-22 13:54:36.081	      7fb5244000	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:470	Space remaining: 6641131520
2017-01-22 13:54:36.081	      7fb5244000	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:471	Size threshold:  0
2017-01-22 13:54:36.081	      7fb5244000	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:473	Percent used: 0.5877  Percent threshold: 0.8000
2017-01-22 13:54:36.082	      7fb5244000	INFO 	checkpoints	src/cryptonote_core/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 233000 <4f69bec2af6c0852412bdd10c19e6af10c8d738fe2618b5511a98efd03ab477e>
2017-01-22 13:54:36.082	      7fb5244000	INFO 	checkpoints	src/cryptonote_core/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 250000 <f59d31839bd909ec8830b4f7f66ff213f0bd006334c8523daee452725e5c7a79>
2017-01-22 13:54:36.082	      7fb5244000	INFO 	checkpoints	src/cryptonote_core/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 300000 <0c1cd46df6ccff90ec4ab493281f2583c344cd62216c427628990fe9db1bb8b6>
2017-01-22 13:54:36.082	      7fb5244000	INFO 	checkpoints	src/cryptonote_core/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 325000 <4260d56368267bc2a70dd58d73c5ecf23b4e4d96e63c29a868e4a679b0741c7f>
2017-01-22 13:54:36.082	      7fb5244000	INFO 	checkpoints	src/cryptonote_core/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 350000 <74da79f6a136969abd6364bd3d37af273c408d6471e8ab598e80569b42415f86>
2017-01-22 13:54:36.082	      7fb5244000	INFO 	checkpoints	src/cryptonote_core/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 375000 <c80c23e387585e12ffb6649d678e9ba328181797b9583a6d8911b77e25375737>
2017-01-22 13:54:36.082	      7fb5244000	INFO 	checkpoints	src/cryptonote_core/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 400000 <1b2b0e7a30e59691491529a3d506d1ba3d6052d0f6b52198b7330b28a6f1b6ac>
2017-01-22 13:54:36.082	      7fb5244000	INFO 	checkpoints	src/cryptonote_core/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 450000 <4d098b511ca97723e81737c448343cfd4e6dadb3d8a0e757c6e4d595e6e48357>
2017-01-22 13:54:36.082	      7fb5244000	INFO 	checkpoints	src/cryptonote_core/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 500000 <2428f0dbe49796be05ed81b347f53e1f7f44aed0abf641446ec2b94cae066b02>
2017-01-22 13:54:36.083	      7fb5244000	INFO 	checkpoints	src/cryptonote_core/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 550000 <c2e80a636438bd9f7a7ab432a6ad297e35540d80ff5b868bca098124cad2ff8c>
2017-01-22 13:54:36.083	      7fb5244000	INFO 	checkpoints	src/cryptonote_core/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 600000 <f5828ebf7d7d1cb61762c4dfe3ccf4ecab2e1aad23e8113668d981713b7a54c5>
2017-01-22 13:54:36.083	      7fb5244000	INFO 	checkpoints	src/cryptonote_core/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 650000 <1d567f2b491324375a825895c5e7b52857b38e4fed0e42c40909c2d52240b4e0>
2017-01-22 13:54:36.083	      7fb5244000	INFO 	checkpoints	src/cryptonote_core/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 700000 <12be9b3d210b93f574d2526abb9c1ab2a881b479131fd0d4f7dac93875f503cd>
2017-01-22 13:54:36.083	      7fb5244000	INFO 	checkpoints	src/cryptonote_core/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 800000 <2ced10aa85357ab6c14bb12b6b56d1dde28940820dda30911b73a5cc9a301760>
2017-01-22 13:54:36.083	      7fb5244000	INFO 	checkpoints	src/cryptonote_core/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 850000 <00e2b557dde9fd4a9e2e3dd7ddac962f5ca475eb1095bc50aa757fd1218ab0a5>
2017-01-22 13:54:36.083	      7fb5244000	INFO 	checkpoints	src/cryptonote_core/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 900000 <d9958d0e7dcf91a5a7b11de225927bf7efc6eb26240315ce12372be902cc1337>
2017-01-22 13:54:36.083	      7fb5244000	INFO 	checkpoints	src/cryptonote_core/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 913193 <5292d5d56f6ba4de33a58d9a34d263e2cb3c6fee0aed2286fd4ac7f36d53c85f>
2017-01-22 13:54:36.083	      7fb5244000	INFO 	checkpoints	src/cryptonote_core/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 913269 <f8302e6b8ba1c49aad9a854b8d6c79d8272c6239dcbba5a75ed0784c1d4f56a1>
2017-01-22 13:54:36.083	      7fb5244000	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:504	[check_and_resize_for_batch] checking DB size
2017-01-22 13:54:36.083	      7fb5244000	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:468	DB map size:     16106127360
2017-01-22 13:54:36.083	      7fb5244000	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:469	Space used:      9464995840
2017-01-22 13:54:36.083	      7fb5244000	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:470	Space remaining: 6641131520
2017-01-22 13:54:36.083	      7fb5244000	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:471	Size threshold:  0
2017-01-22 13:54:36.084	      7fb5244000	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:473	Percent used: 0.5877  Percent threshold: 0.8000
2017-01-22 13:54:36.084	      7fb5244000	INFO 	checkpoints	src/cryptonote_core/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 1 <771fbcd656ec1464d3a02ead5e18644030007a0fc664c0a964d30922821a8148>
2017-01-22 13:54:36.084	      7fb5244000	INFO 	checkpoints	src/cryptonote_core/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 10 <c0e3b387e47042f72d8ccdca88071ff96bff1ac7cde09ae113dbb7ad3fe92381>
2017-01-22 13:54:36.084	      7fb5244000	INFO 	checkpoints	src/cryptonote_core/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 100 <ac3e11ca545e57c49fca2b4e8c48c03c23be047c43e471e1394528b1f9f80b2d>
2017-01-22 13:54:36.084	      7fb5244000	INFO 	checkpoints	src/cryptonote_core/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 1000 <5acfc45acffd2b2e7345caf42fa02308c5793f15ec33946e969e829f40b03876>
2017-01-22 13:54:36.084	      7fb5244000	INFO 	checkpoints	src/cryptonote_core/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 10000 <c758b7c81f928be3295d45e230646de8b852ec96a821eac3fea4daf3fcac0ca2>
2017-01-22 13:54:36.084	      7fb5244000	INFO 	checkpoints	src/cryptonote_core/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 22231 <7cb10e29d67e1c069e6e11b17d30b809724255fee2f6868dc14cfc6ed44dfb25>
2017-01-22 13:54:36.084	      7fb5244000	INFO 	checkpoints	src/cryptonote_core/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 29556 <53c484a8ed91e4da621bb2fa88106dbde426fe90d7ef07b9c1e5127fb6f3a7f6>
2017-01-22 13:54:36.084	      7fb5244000	INFO 	checkpoints	src/cryptonote_core/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 50000 <0fe8758ab06a8b9cb35b7328fd4f757af530a5d37759f9d3e421023231f7b31c>
2017-01-22 13:54:36.084	      7fb5244000	INFO 	checkpoints	src/cryptonote_core/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 80000 <a62dcd7b536f22e003ebae8726e9e7276f63d594e264b6f0cd7aab27b66e75e3>
2017-01-22 13:54:36.085	      7fb5244000	INFO 	checkpoints	src/cryptonote_core/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 202612 <bbd604d2ba11ba27935e006ed39c9bfdd99b76bf4a50654bc1e1e61217962698>
2017-01-22 13:54:36.085	      7fb5244000	INFO 	checkpoints	src/cryptonote_core/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 202613 <e2aa337e78df1f98f462b3b1e560c6b914dec47b610698b7b7d1e3e86b6197c2>
2017-01-22 13:54:36.085	      7fb5244000	INFO 	checkpoints	src/cryptonote_core/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 202614 <c29e3dc37d8da3e72e506e31a213a58771b24450144305bcba9e70fa4d6ea6fb>
2017-01-22 13:54:36.085	      7fb5244000	INFO 	checkpoints	src/cryptonote_core/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 205000 <5d3d7a26e6dc7535e34f03def711daa8c263785f73ec1fadef8a45880fde8063>
2017-01-22 13:54:36.085	      7fb5244000	INFO 	checkpoints	src/cryptonote_core/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 220000 <9613f455933c00e3e33ac315cc6b455ee8aa0c567163836858c2d9caff111553>
2017-01-22 13:54:36.085	      7fb5244000	INFO 	checkpoints	src/cryptonote_core/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 230300 <bae7a80c46859db355556e3a9204a337ae8f24309926a1312323fdecf1920e61>
2017-01-22 13:54:36.085	      7fb5244000	INFO 	checkpoints	src/cryptonote_core/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 230700 <93e631240ceac831da1aebfc5dac8f722c430463024763ebafa888796ceaeedf>
2017-01-22 13:54:36.085	      7fb5244000	INFO 	checkpoints	src/cryptonote_core/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 231350 <b5add137199b820e1ea26640e5c3e121fd85faa86a1e39cf7e6cc097bdeb1131>
2017-01-22 13:54:36.085	      7fb5244000	INFO 	checkpoints	src/cryptonote_core/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 232150 <955de8e6b6508af2c24f7334f97beeea651d78e9ade3ab18fec3763be3201aa8>
2017-01-22 13:54:36.085	      7fb5244000	INFO 	checkpoints	src/cryptonote_core/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 249380 <654fb0a81ce3e5caf7e3264a70f447d4bd07586c08fa50f6638cc54da0a52b2d>
2017-01-22 13:54:36.085	      7fb5244000	INFO 	checkpoints	src/cryptonote_core/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 460000 <75037a7aed3e765db96c75bcf908f59d690a5f3390baebb9edeafd336a1c4831>
2017-01-22 13:54:36.085	      7fb5244000	INFO 	checkpoints	src/cryptonote_core/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 500000 <2428f0dbe49796be05ed81b347f53e1f7f44aed0abf641446ec2b94cae066b02>
2017-01-22 13:54:36.085	      7fb5244000	INFO 	checkpoints	src/cryptonote_core/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 600000 <f5828ebf7d7d1cb61762c4dfe3ccf4ecab2e1aad23e8113668d981713b7a54c5>
2017-01-22 13:54:36.085	      7fb5244000	INFO 	checkpoints	src/cryptonote_core/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 700000 <12be9b3d210b93f574d2526abb9c1ab2a881b479131fd0d4f7dac93875f503cd>
2017-01-22 13:54:36.086	      7fb5244000	INFO 	checkpoints	src/cryptonote_core/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 825000 <56503f9ad766774b575be3aff73245e9d159be88132c93d1754764f28da2ff60>
2017-01-22 13:54:36.086	      7fb5244000	INFO 	checkpoints	src/cryptonote_core/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 900000 <d9958d0e7dcf91a5a7b11de225927bf7efc6eb26240315ce12372be902cc1337>
2017-01-22 13:54:36.086	      7fb5244000	INFO 	checkpoints	src/cryptonote_core/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 913193 <5292d5d56f6ba4de33a58d9a34d263e2cb3c6fee0aed2286fd4ac7f36d53c85f>
2017-01-22 13:54:36.086	      7fb5244000	INFO 	checkpoints	src/cryptonote_core/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 1000000 <a886ef5149902d8342475fee9bb296341b891ac67c4842f47a833f23c00ed721>
2017-01-22 13:54:36.086	      7fb5244000	INFO 	checkpoints	src/cryptonote_core/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 1100000 <3fd720c5c8b3072fc1ccda922dec1ef25f9ed88a1e6ad4103d0fe00b180a5903>
2017-01-22 13:54:36.086	      7fb5244000	INFO 	checkpoints	src/cryptonote_core/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 1150000 <1dd16f626d18e1e988490dfd06de5920e22629c972c58b4d8daddea0038627b2>
2017-01-22 13:54:36.086	      7fb5244000	INFO 	checkpoints	src/cryptonote_core/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 1200000 <fa7d13a90850882060479d100141ff84286599ae39c3277c8ea784393f882d1f>
2017-01-22 13:54:36.086	      7fb5244000	INFO 	global	src/daemon/core.h:79	Core initialized OK
2017-01-22 13:54:36.086	      7fb5244000	INFO 	global	src/daemon/rpc.h:68	Starting core rpc server...
2017-01-22 13:54:36.086	      7fb5244000	INFO 	net.http	contrib/epee/include/net/http_server_impl_base.h:85	Run net_service loop( 2 threads)...
2017-01-22 13:54:36.086	[SRV_MAIN]	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:820	Run server thread name: RPC
2017-01-22 13:54:36.087	[SRV_MAIN]	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:820	Run server thread name: RPC
2017-01-22 13:54:36.087	[SRV_MAIN]	INFO 	global	src/daemon/rpc.h:73	Core rpc server started ok
2017-01-22 13:54:36.087	[SRV_MAIN]	INFO 	global	src/daemon/p2p.h:78	Starting p2p net loop...
2017-01-22 13:54:36.087	      7fb2b861e0	INFO 	net.p2p	src/p2p/net_node.inl:593	Thread monitor number of peers - start
2017-01-22 13:54:36.087	[SRV_MAIN]	INFO 	net.p2p	src/p2p/net_node.inl:621	Run net_service loop( 10 threads)...
2017-01-22 13:54:36.087	[SRV_MAIN]	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:820	Run server thread name: P2P
2017-01-22 13:54:36.087	[SRV_MAIN]	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:820	Run server thread name: P2P
2017-01-22 13:54:36.087	[P2P0]	INFO 	net.p2p	src/p2p/connection_basic.cpp:165	Spawned connection p2p#1 to 0.0.0.0 currently we have sockets count:2
2017-01-22 13:54:36.087	[SRV_MAIN]	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:820	Run server thread name: P2P
2017-01-22 13:54:36.087	[SRV_MAIN]	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:820	Run server thread name: P2P
2017-01-22 13:54:36.087	[SRV_MAIN]	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:820	Run server thread name: P2P
2017-01-22 13:54:36.087	[SRV_MAIN]	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:820	Run server thread name: P2P
2017-01-22 13:54:36.088	[SRV_MAIN]	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:820	Run server thread name: P2P
2017-01-22 13:54:36.088	[P2P0]	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:85	test, connection constructor set m_connection_type=2
2017-01-22 13:54:36.088	[SRV_MAIN]	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:820	Run server thread name: P2P
2017-01-22 13:54:36.088	[SRV_MAIN]	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:820	Run server thread name: P2P
2017-01-22 13:54:36.088	[SRV_MAIN]	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:820	Run server thread name: P2P
2017-01-22 13:54:36.088	[SRV_MAIN]	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:827	JOINING all threads
2017-01-22 13:54:36.088	[P2P0]	INFO 	net.p2p	src/p2p/net_node.inl:1549	[89.232.72.221:10863 3306abfa-bed0-f8ae-c53e-519400dc9c1e INC] NEW CONNECTION
2017-01-22 13:54:36.089	[P2P0]	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:270	 connection type P2P 192.168.0.21:18080 <--> 89.232.72.221:10863
2017-01-22 13:54:36.089	[P2P2]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:286	[89.232.72.221:10863 INC] Sync data returned a new top block candidate: 1220105 -> 1009962 [Your node is 210143 blocks (291 days) ahead] 
SYNCHRONIZATION started
2017-01-22 13:54:36.090	[P2P2]	INFO 	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:287	Remote blockchain height: 1009962, id: <810aa020207f495a06e55dd4b0bd0ae0e89c4481fae3558f538b2985e80fa285>
2017-01-22 13:54:36.090	[P2P2]	INFO 	net.p2p	src/p2p/connection_basic.cpp:165	Spawned connection p2p#2 to 0.0.0.0 currently we have sockets count:3
2017-01-22 13:54:36.090	[P2P2]	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:85	test, connection constructor set m_connection_type=2
2017-01-22 13:54:36.427	[P2P1]	INFO 	net	contrib/epee/include/storages/levin_abstract_invoke2.h:125	Failed to invoke command 1007 return code -6
2017-01-22 13:54:36.427	[P2P1]	ERROR	net.p2p	src/p2p/net_node.inl:1396	[89.232.72.221:10863 INC] COMMAND_REQUEST_SUPPORT_FLAGS invoke failed. (-6, LEVIN_ERROR_CONNECTION_HANDLER_NOT_DEFINED)
2017-01-22 13:54:37.103	[P2P2]	INFO 	net.p2p	src/p2p/net_node.inl:975	Considering connecting (out) to peer: 3408723755020624071 83.160.124.112:18080
2017-01-22 13:54:37.104	[P2P2]	INFO 	net.p2p	src/p2p/connection_basic.cpp:165	Spawned connection p2p#3 to 0.0.0.0 currently we have sockets count:4
2017-01-22 13:54:37.104	[P2P2]	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:85	test, connection constructor set m_connection_type=2
2017-01-22 13:54:37.104	[P2P4]	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:1008	
**********************************************************************
The daemon will start synchronizing with the network. It may take up to several hours.

You can set the level of process detailization* through "set_log <level|categories>" command*, where <level> is between 0 (no details) and 4 (very verbose), or custom category based levels (eg, *:WARNING)

Use "help" command to see the list of available commands.

Note: in case you need to interrupt the process, use "exit" command. Otherwise, the current progress won't be saved.
**********************************************************************
2017-01-22 13:54:37.138	[P2P2]	INFO 	net.p2p	src/p2p/net_node.inl:1549	[83.160.124.112:18080 dbba7f97-ba4f-6c9b-54cd-bfd37ba5c3bc OUT] NEW CONNECTION
2017-01-22 13:54:37.139	[P2P2]	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:270	 connection type P2P 192.168.0.21:37800 <--> 83.160.124.112:18080
2017-01-22 13:54:37.283	[P2P3]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:286	[83.160.124.112:18080 OUT] Sync data returned a new top block candidate: 1220105 -> 1229388 [Your node is 9283 blocks (12 days) behind] 
SYNCHRONIZATION started
2017-01-22 13:54:37.283	[P2P3]	INFO 	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:287	Remote blockchain height: 1229388, id: <aeb3fd0ef19fbda82a2c98cdfdf258031699d685a626ce42fc0b88c70befdbc9>
2017-01-22 13:54:37.284	[P2P2]	INFO 	net.p2p	src/p2p/net_node.inl:975	Considering connecting (out) to peer: 1705557811183118083 80.101.109.52:18080
2017-01-22 13:54:37.284	[P2P2]	INFO 	net.p2p	src/p2p/connection_basic.cpp:165	Spawned connection p2p#4 to 0.0.0.0 currently we have sockets count:5
2017-01-22 13:54:37.284	[P2P2]	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:85	test, connection constructor set m_connection_type=2
2017-01-22 13:54:37.291	[P2P0]	INFO 	net.p2p	src/p2p/connection_basic.cpp:165	Spawned connection p2p#5 to 0.0.0.0 currently we have sockets count:6
2017-01-22 13:54:37.291	[P2P0]	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:85	test, connection constructor set m_connection_type=2
2017-01-22 13:54:37.292	[P2P0]	INFO 	net.p2p	src/p2p/net_node.inl:1549	[83.160.124.112:34209 0cee8e2b-d844-b602-1299-7b60a80ffa13 INC] NEW CONNECTION
2017-01-22 13:54:37.292	[P2P0]	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:270	 connection type P2P 192.168.0.21:18080 <--> 83.160.124.112:34209
2017-01-22 13:54:37.307	[P2P2]	INFO 	net.p2p	src/p2p/net_node.inl:1549	[80.101.109.52:18080 995fc5f3-1dc0-44b2-2a15-fa51c3a2145e OUT] NEW CONNECTION
2017-01-22 13:54:37.308	[P2P2]	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:270	 connection type P2P 192.168.0.21:36722 <--> 80.101.109.52:18080
2017-01-22 13:54:37.358	[P2P5]	INFO 	net.p2p	src/p2p/net_node.inl:1555	[83.160.124.112:34209 0cee8e2b-d844-b602-1299-7b60a80ffa13 INC] CLOSE CONNECTION
2017-01-22 13:54:37.358	[P2P5]	INFO 	net.p2p	src/p2p/connection_basic.cpp:173	Destructing connection p2p#1 to 83.160.124.112
2017-01-22 13:54:37.381	[P2P1]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:286	[80.101.109.52:18080 OUT] Sync data returned a new top block candidate: 1220105 -> 1229388 [Your node is 9283 blocks (12 days) behind] 
SYNCHRONIZATION started
2017-01-22 13:54:37.381	[P2P1]	INFO 	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:287	Remote blockchain height: 1229388, id: <aeb3fd0ef19fbda82a2c98cdfdf258031699d685a626ce42fc0b88c70befdbc9>
2017-01-22 13:54:37.382	[P2P1]	INFO 	net.p2p	src/p2p/connection_basic.cpp:165	Spawned connection p2p#6 to 0.0.0.0 currently we have sockets count:6
2017-01-22 13:54:37.382	[P2P1]	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:85	test, connection constructor set m_connection_type=2
2017-01-22 13:54:37.382	[P2P1]	INFO 	net.p2p	src/p2p/net_node.inl:1549	[80.101.109.52:45586 9689302e-8113-bc06-141d-1d0098c4ecfe INC] NEW CONNECTION
2017-01-22 13:54:37.382	[P2P1]	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:270	 connection type P2P 192.168.0.21:18080 <--> 80.101.109.52:45586
2017-01-22 13:54:37.383	[P2P2]	INFO 	net.p2p	src/p2p/net_node.inl:975	Considering connecting (out) to peer: 1705557811183118083 80.101.109.52:18080
2017-01-22 13:54:37.383	[P2P2]	INFO 	net.p2p	src/p2p/net_node.inl:978	Peer is used
2017-01-22 13:54:37.383	[P2P2]	INFO 	net.p2p	src/p2p/net_node.inl:975	Considering connecting (out) to peer: 15270222189757260946 68.5.111.70:18080
2017-01-22 13:54:37.383	[P2P2]	INFO 	net.p2p	src/p2p/connection_basic.cpp:165	Spawned connection p2p#7 to 0.0.0.0 currently we have sockets count:7
2017-01-22 13:54:37.383	[P2P2]	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:85	test, connection constructor set m_connection_type=2
2017-01-22 13:54:37.426	[P2P1]	INFO 	net.p2p	src/p2p/net_node.inl:1555	[80.101.109.52:45586 9689302e-8113-bc06-141d-1d0098c4ecfe INC] CLOSE CONNECTION
2017-01-22 13:54:37.426	[P2P1]	INFO 	net.p2p	src/p2p/connection_basic.cpp:173	Destructing connection p2p#5 to 80.101.109.52
2017-01-22 13:54:37.847	[P2P4]	INFO 	net.p2p	src/p2p/connection_basic.cpp:165	Spawned connection p2p#8 to 0.0.0.0 currently we have sockets count:7
2017-01-22 13:54:37.847	[P2P4]	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:85	test, connection constructor set m_connection_type=2
2017-01-22 13:54:37.847	[P2P4]	INFO 	net.p2p	src/p2p/net_node.inl:1549	[163.172.76.47:55720 f7d8e75b-a186-32fd-c175-c1ad1d614a42 INC] NEW CONNECTION
2017-01-22 13:54:37.848	[P2P4]	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:270	 connection type P2P 192.168.0.21:18080 <--> 163.172.76.47:55720
2017-01-22 13:54:37.873	[P2P1]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:286	[163.172.76.47:55720 INC] Sync data returned a new top block candidate: 1220105 -> 1229388 [Your node is 9283 blocks (12 days) behind] 
SYNCHRONIZATION started
2017-01-22 13:54:37.873	[P2P1]	INFO 	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:287	Remote blockchain height: 1229388, id: <aeb3fd0ef19fbda82a2c98cdfdf258031699d685a626ce42fc0b88c70befdbc9>
2017-01-22 13:54:37.874	[P2P1]	INFO 	net.p2p	src/p2p/connection_basic.cpp:165	Spawned connection p2p#9 to 0.0.0.0 currently we have sockets count:8
2017-01-22 13:54:37.874	[P2P1]	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:85	test, connection constructor set m_connection_type=2
2017-01-22 13:54:37.886	[P2P9]	INFO 	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:981	80.101.109.52:18080 OUT-->>NOTIFY_REQUEST_GET_OBJECTS: blocks.size()=200, txs.size()=0requested blocks count=200 / 200
2017-01-22 13:54:37.891	[P2P8]	WARN 	net.p2p	src/p2p/net_node.inl:1334	[0.0.0.0:0 OUT] back ping connect failed to 163.172.76.47:18095
2017-01-22 13:54:38.113	[P2P6]	WARN 	net.p2p	src/p2p/net_node.inl:1334	[0.0.0.0:0 OUT] back ping connect failed to 89.232.72.221:18080
2017-01-22 13:54:38.116	[P2P5]	INFO 	net.p2p	src/p2p/connection_basic.cpp:165	Spawned connection p2p#10 to 0.0.0.0 currently we have sockets count:9
2017-01-22 13:54:38.116	[P2P5]	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:85	test, connection constructor set m_connection_type=2
2017-01-22 13:54:38.116	[P2P5]	INFO 	net.p2p	src/p2p/net_node.inl:1549	[104.140.201.42:35052 6ec05d42-f259-f83f-62f1-e4724d06d7bc INC] NEW CONNECTION
2017-01-22 13:54:38.116	[P2P5]	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:270	 connection type P2P 192.168.0.21:18080 <--> 104.140.201.42:35052
2017-01-22 13:54:38.222	[P2P1]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:286	[104.140.201.42:35052 INC] Sync data returned a new top block candidate: 1220105 -> 1229388 [Your node is 9283 blocks (12 days) behind] 
SYNCHRONIZATION started
2017-01-22 13:54:38.222	[P2P1]	INFO 	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:287	Remote blockchain height: 1229388, id: <aeb3fd0ef19fbda82a2c98cdfdf258031699d685a626ce42fc0b88c70befdbc9>
2017-01-22 13:54:38.222	[P2P1]	INFO 	net.p2p	src/p2p/connection_basic.cpp:165	Spawned connection p2p#11 to 0.0.0.0 currently we have sockets count:10
2017-01-22 13:54:38.222	[P2P1]	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:85	test, connection constructor set m_connection_type=2
2017-01-22 13:54:38.293	[P2P4]	INFO 	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:981	163.172.76.47:55720 INC-->>NOTIFY_REQUEST_GET_OBJECTS: blocks.size()=200, txs.size()=0requested blocks count=200 / 200
2017-01-22 13:54:38.304	[P2P4]	INFO 	net.p2p	src/p2p/net_node.inl:1549	[104.140.201.42:18080 bd4924b3-8584-12a2-9405-50410c0bc246 OUT] NEW CONNECTION
2017-01-22 13:54:39.038	[P2P1]	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:504	[check_and_resize_for_batch] checking DB size
2017-01-22 13:54:39.039	[P2P1]	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:558	[get_estimated_batch_size] m_height: 1220105  block_start: 1219605  block_stop: 1220104
2017-01-22 13:54:39.043	[P2P1]	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:582	average block size across recent 500 blocks: 13244
2017-01-22 13:54:39.043	[P2P1]	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:586	estimated average block size for batch: 13244
2017-01-22 13:54:39.043	[P2P1]	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:511	calculated batch size: 297990016
2017-01-22 13:54:39.043	[P2P1]	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:520	increase size: 536870912
2017-01-22 13:54:39.043	[P2P1]	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:468	DB map size:     16106127360
2017-01-22 13:54:39.043	[P2P1]	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:469	Space used:      9464995840
2017-01-22 13:54:39.043	[P2P1]	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:470	Space remaining: 6641131520
2017-01-22 13:54:39.043	[P2P1]	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:471	Size threshold:  297990016
2017-01-22 13:54:39.044	[P2P1]	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:473	Percent used: 0.5877  Percent threshold: 0.8000
2017-01-22 13:54:39.147	[P2P7]	INFO 	net.p2p	src/p2p/connection_basic.cpp:165	Spawned connection p2p#12 to 0.0.0.0 currently we have sockets count:11
2017-01-22 13:54:39.147	[P2P7]	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:85	test, connection constructor set m_connection_type=2
2017-01-22 13:54:39.148	[P2P7]	INFO 	net.p2p	src/p2p/net_node.inl:1549	[107.167.93.58:48404 fc45a14b-ad97-1ea3-9c6a-990b9a631808 INC] NEW CONNECTION
2017-01-22 13:54:39.148	[P2P7]	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:270	 connection type P2P 192.168.0.21:18080 <--> 107.167.93.58:48404
2017-01-22 13:54:39.945	[P2P1]	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:78	Attempting to get output pubkey by global index (amount 2, index 13523, count 13510), but key does not exist
2017-01-22 13:54:39.946	[P2P1]	ERROR	stacktrace	src/common/stack_trace.cpp:111	Exception: cryptonote::OUTPUT_DNE
2017-01-22 13:54:39.946	[P2P1]	ERROR	stacktrace	src/common/stack_trace.cpp:112	Unwound call stack:
2017-01-22 13:54:39.948	[P2P1]	ERROR	stacktrace	src/common/stack_trace.cpp:138	     1                  0x63c06c __cxa_throw + 0x74
2017-01-22 13:54:39.949	[P2P1]	ERROR	stacktrace	src/common/stack_trace.cpp:138	     2                  0x5ffe04 void (anonymous namespace)::throw1<cryptonote::OUTPUT_DNE>(cryptonote::OUTPUT_DNE const&) [clone .constprop.1498] + 0xe4
2017-01-22 13:54:39.950	[P2P1]	ERROR	stacktrace	src/common/stack_trace.cpp:138	     3                  0x570eb8 cryptonote::BlockchainLMDB::get_output_key(unsigned long const&, std::vector<unsigned long, std::allocator<unsigned long> > const&, std::vector<cryptonote::output_data_t, std::allocator<cryptonote::output_data_t> >&) + 0x530
2017-01-22 13:54:39.951	[P2P1]	ERROR	stacktrace	src/common/stack_trace.cpp:138	     4                  0x5aebb0 cryptonote::Blockchain::output_scan_worker(unsigned long, std::vector<unsigned long, std::allocator<unsigned long> > const&, std::vector<cryptonote::output_data_t, std::allocator<cryptonote::output_data_t> >&, std::unordered_map<crypto::hash, cryptonote::transaction, std::hash<crypto::hash>, std::equal_to<crypto::hash>, std::allocator<std::pair<crypto::hash const, cryptonote::transaction> > >&) const + 0x30
2017-01-22 13:54:39.952	[P2P1]	ERROR	stacktrace	src/common/stack_trace.cpp:138	     5                  0x5bea50 cryptonote::Blockchain::prepare_handle_incoming_blocks(std::__cxx11::list<cryptonote::block_complete_entry, std::allocator<cryptonote::block_complete_entry> > const&) + 0xf30
2017-01-22 13:54:39.954	[P2P1]	ERROR	stacktrace	src/common/stack_trace.cpp:138	     6                  0x523ccc cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::handle_response_get_objects(int, cryptonote::NOTIFY_RESPONSE_GET_OBJECTS::request&, cryptonote::cryptonote_connection_context&) + 0xe9c
2017-01-22 13:54:39.955	[P2P1]	ERROR	stacktrace	src/common/stack_trace.cpp:138	     7                  0x648ab0 int epee::net_utils::buff_to_t_adapter<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>, cryptonote::NOTIFY_RESPONSE_GET_OBJECTS::request, cryptonote::cryptonote_connection_context, boost::_bi::bind_t<int, boost::_mfi::mf3<int, cryptonote::t_cryptonote_protocol_handler<cryptonote::core>, int, cryptonote::NOTIFY_RESPONSE_GET_OBJECTS::request&, cryptonote::cryptonote_connection_context&>, boost::_bi::list4<boost::_bi::value<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*>, boost::arg<1>, boost::arg<2>, boost::arg<3> > > >(cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, boost::_bi::bind_t<int, boost::_mfi::mf3<int, cryptonote::t_cryptonote_protocol_handler<cryptonote::core>, int, cryptonote::NOTIFY_RESPONSE_GET_OBJECTS::request&, cryptonote::cryptonote_connection_context&>, boost::_bi::list4<boost::_bi::value<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*>, boost::arg<1>, boost::arg<2>, boost::arg<3> > >, cryptonote::cryptonote_connection_context&) [clone .constprop.864] + 0x400
2017-01-22 13:54:39.956	[P2P1]	ERROR	stacktrace	src/common/stack_trace.cpp:138	     8                  0x64aa88 int nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::handle_invoke_map<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >(bool, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&, bool&) [clone .constprop.830] + 0x1d48
2017-01-22 13:54:39.957	[P2P1]	ERROR	stacktrace	src/common/stack_trace.cpp:138	     9                  0x51b8a0 nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::notify(int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&) + 0x38
2017-01-22 13:54:39.958	[P2P1]	ERROR	stacktrace	src/common/stack_trace.cpp:138	     a                  0x502578 epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >::handle_recv(void const*, unsigned long) + 0x5b0
2017-01-22 13:54:39.960	[P2P1]	ERROR	stacktrace	src/common/stack_trace.cpp:138	     b                  0x4eff3c epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::handle_read(boost::system::error_code const&, unsigned long) + 0x1ec
2017-01-22 13:54:39.961	[P2P1]	ERROR	stacktrace	src/common/stack_trace.cpp:134	     c                  0x4fd4f0
2017-01-22 13:54:39.962	[P2P1]	ERROR	stacktrace	src/common/stack_trace.cpp:134	     d                  0x4fe2cc
2017-01-22 13:54:39.963	[P2P1]	ERROR	stacktrace	src/common/stack_trace.cpp:138	     e                  0x4ca594 boost::asio::detail::epoll_reactor::descriptor_state::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long) + 0x19c
2017-01-22 13:54:39.964	[P2P1]	ERROR	stacktrace	src/common/stack_trace.cpp:138	     f                  0x6070f0 boost::asio::detail::task_io_service::run(boost::system::error_code&) [clone .constprop.1342] + 0x2c8
2017-01-22 13:54:39.965	[P2P1]	ERROR	stacktrace	src/common/stack_trace.cpp:138	    10                  0x4f1970 epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread() + 0x158
2017-01-22 13:54:39.966	[P2P1]	ERROR	stacktrace	src/common/stack_trace.cpp:138	    11                  0x7fb4d0ccf8 boost::this_thread::interruption_requested() + 0x128
2017-01-22 13:54:39.967	[P2P1]	ERROR	stacktrace	src/common/stack_trace.cpp:138	    12                  0x7fb51f4fc4 start_thread + 0xa4
```


# Discussion History
## moneromooo-monero | 2017-01-22T17:24:39+00:00
Stack trace please...

## ghost | 2017-01-22T18:27:37+00:00
Forgot your advice that 'stack trace' isn't the same as a proper stack trace

## ghost | 2017-01-22T21:23:00+00:00
Closing because I've update to `daf6662` and the stalling issue is back. Have reopened that previous issue. Let's work through that one first.

# Action History
- Created by: ghost | 2017-01-22T13:55:24+00:00
- Closed at: 2017-01-22T21:23:00+00:00
