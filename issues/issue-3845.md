---
title: Daemon hangs after "DB resize needed" on ARM Debian
source_url: https://github.com/monero-project/monero/issues/3845
author: Lafudoci
assignees: []
labels: []
created_at: '2018-05-23T17:00:13+00:00'
updated_at: '2026-01-10T22:50:26+00:00'
type: issue
status: closed
closed_at: '2022-03-16T15:40:08+00:00'
---

# Original Description
Recently my daemon hangs at "DB resize needed" while sync. But when I restart it, the resize seems working. Few hours late it hangs again at "DB resize needed". It's running on ASUS tinker (almost the same with raspberry Pi). Before it ran a node for months without issue.

Log at starting (restart after a hang)
```
2018-05-23 09:49:05.005	        b6f93000	INFO 	logging	contrib/epee/src/mlog.cpp:185	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-05-23 09:49:05.005	        b6f93000	INFO 	logging	contrib/epee/src/mlog.cpp:185	New log categories: *:INFO,global:INFO,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-05-23 09:49:05.006	        b6f93000	INFO 	global	src/daemon/main.cpp:279	Monero 'Lithium Luna' (v0.12.0.0-master-9ccd84b2)
2018-05-23 09:49:05.007	        b6f93000	INFO 	daemon	src/daemon/main.cpp:281	Moving from main() into the daemonize now.
2018-05-23 09:49:05.009	        b6f93000	INFO 	global	src/daemon/protocol.h:53	Initializing cryptonote protocol...
2018-05-23 09:49:05.009	        b6f93000	INFO 	global	src/daemon/protocol.h:58	Cryptonote protocol initialized OK
2018-05-23 09:49:05.011	        b6f93000	INFO 	global	src/daemon/p2p.h:63	Initializing p2p server...
2018-05-23 09:49:05.012	        b6f93000	INFO 	net.throttle	contrib/epee/src/network_throttle-detail.cpp:162	Setting LIMIT: 2048 kbps
2018-05-23 09:49:05.012	        b6f93000	INFO 	net.p2p	src/p2p/net_node.inl:1875	Set limit-up to 2048 kB/s
2018-05-23 09:49:05.012	        b6f93000	INFO 	net.throttle	contrib/epee/src/network_throttle-detail.cpp:162	Setting LIMIT: 8192 kbps
2018-05-23 09:49:05.012	        b6f93000	INFO 	net.throttle	contrib/epee/src/network_throttle-detail.cpp:162	Setting LIMIT: 8192 kbps
2018-05-23 09:49:05.013	        b6f93000	INFO 	net.p2p	src/p2p/net_node.inl:1888	Set limit-down to 8192 kB/s
2018-05-23 09:49:05.013	        b6f93000	INFO 	net.throttle	contrib/epee/src/network_throttle-detail.cpp:162	Setting LIMIT: 2048 kbps
2018-05-23 09:49:05.013	        b6f93000	INFO 	net.p2p	src/p2p/net_node.inl:1910	Set limit-up to 2048 kB/s
2018-05-23 09:49:05.013	        b6f93000	INFO 	net.throttle	contrib/epee/src/network_throttle-detail.cpp:162	Setting LIMIT: 8192 kbps
2018-05-23 09:49:05.013	        b6f93000	INFO 	net.throttle	contrib/epee/src/network_throttle-detail.cpp:162	Setting LIMIT: 8192 kbps
2018-05-23 09:49:05.013	        b6f93000	INFO 	net.p2p	src/p2p/net_node.inl:1914	Set limit-down to 8192 kB/s
2018-05-23 09:49:05.167	        b2ef0450	INFO 	net.p2p	src/p2p/net_node.inl:457	dns_threads[1] addr_str: seeds.moneroseeds.ae.org  number of results: 0
2018-05-23 09:49:05.329	        b26f0450	INFO 	net.p2p	src/p2p/net_node.inl:457	dns_threads[2] addr_str: seeds.moneroseeds.ch  number of results: 0
2018-05-23 09:49:06.043	        b36f0450	INFO 	net.p2p	src/p2p/net_node.inl:457	dns_threads[0] addr_str: seeds.moneroseeds.se  number of results: 0
2018-05-23 09:49:06.653	        b1cff450	INFO 	net.p2p	src/p2p/net_node.inl:457	dns_threads[3] addr_str: seeds.moneroseeds.li  number of results: 0
2018-05-23 09:49:06.653	        b6f93000	INFO 	net.p2p	src/p2p/net_node.inl:495	DNS seed node lookup either timed out or failed, falling back to defaults
2018-05-23 09:49:06.653	        b6f93000	INFO 	net.p2p	src/p2p/net_node.inl:357	Added seed node: 107.152.130.98:18080
2018-05-23 09:49:06.654	        b6f93000	INFO 	net.p2p	src/p2p/net_node.inl:357	Added seed node: 161.67.132.39:18080
2018-05-23 09:49:06.654	        b6f93000	INFO 	net.p2p	src/p2p/net_node.inl:357	Added seed node: 163.172.182.165:18080
2018-05-23 09:49:06.654	        b6f93000	INFO 	net.p2p	src/p2p/net_node.inl:357	Added seed node: 195.154.123.123:18080
2018-05-23 09:49:06.654	        b6f93000	INFO 	net.p2p	src/p2p/net_node.inl:357	Added seed node: 198.74.231.92:18080
2018-05-23 09:49:06.654	        b6f93000	INFO 	net.p2p	src/p2p/net_node.inl:357	Added seed node: 212.83.172.165:18080
2018-05-23 09:49:06.654	        b6f93000	INFO 	net.p2p	src/p2p/net_node.inl:357	Added seed node: 212.83.175.67:18080
2018-05-23 09:49:06.655	        b6f93000	INFO 	net.p2p	src/p2p/net_node.inl:357	Added seed node: 5.9.100.248:18080
2018-05-23 09:49:06.697	        b6f93000	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:803	Set server type to: 2 from name: P2P, prefix_name = P2P
2018-05-23 09:49:06.697	        b6f93000	INFO 	net.p2p	src/p2p/net_node.inl:546	Binding on 0.0.0.0:18080
2018-05-23 09:49:06.697	        b6f93000	INFO 	net.p2p	src/p2p/net_node.inl:551	[1;32mNet service bound to 0.0.0.0:18080[0m
2018-05-23 09:49:10.702	        b6f93000	INFO 	net.p2p	src/p2p/net_node.inl:2016	No IGD was found.
2018-05-23 09:49:10.703	        b6f93000	INFO 	global	src/daemon/p2p.h:68	p2p server initialized OK
2018-05-23 09:49:10.708	        b6f93000	INFO 	global	src/daemon/rpc.h:63	Initializing core RPC server...
2018-05-23 09:49:10.711	        b6f93000	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:803	Set server type to: 1 from name: RPC, prefix_name = RPC
2018-05-23 09:49:10.713	        b6f93000	INFO 	global	contrib/epee/include/net/http_server_impl_base.h:76	Binding on 10.1.1.61:18083
2018-05-23 09:49:10.714	        b6f93000	INFO 	global	src/daemon/rpc.h:69	core RPC server initialized OK on port: 18083
2018-05-23 09:49:10.714	        b6f93000	INFO 	global	src/daemon/core.h:86	Initializing core...
2018-05-23 09:49:10.717	        b6f93000	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:427	Loading blockchain from folder /home/linaro/.bitmonero/lmdb ...
2018-05-23 09:49:10.720	        b6f93000	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:528	DB map size:     59450634240
2018-05-23 09:49:10.720	        b6f93000	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:529	Space used:      50716438528
2018-05-23 09:49:10.720	        b6f93000	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:530	Space remaining: 8734195712
2018-05-23 09:49:10.720	        b6f93000	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:531	Size threshold:  0
2018-05-23 09:49:10.720	        b6f93000	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:533	Percent used: 0.8531  Percent threshold: 0.8000
2018-05-23 09:49:10.721	        b6f93000	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:552	Threshold met (percent-based)
2018-05-23 09:49:10.721	        b6f93000	WARN 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1181	LMDB memory map needs to be resized, doing that now.
2018-05-23 09:49:10.721	        b6f93000	INFO 	global	src/blockchain_db/lmdb/db_lmdb.cpp:504	LMDB Mapsize increased.  Old: 56696MiB, New: 57720MiB
2018-05-23 09:49:15.400	        b6f93000	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:564	[check_and_resize_for_batch] checking DB size
2018-05-23 09:49:15.400	        b6f93000	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:528	DB map size:     60524376064
2018-05-23 09:49:15.400	        b6f93000	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:529	Space used:      50716438528
2018-05-23 09:49:15.400	        b6f93000	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:530	Space remaining: 9807937536
2018-05-23 09:49:15.400	        b6f93000	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:531	Size threshold:  0
2018-05-23 09:49:15.400	        b6f93000	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:533	Percent used: 0.8380  Percent threshold: 0.8000
2018-05-23 09:49:15.401	        b6f93000	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:552	Threshold met (percent-based)
2018-05-23 09:49:15.401	        b6f93000	INFO 	global	src/blockchain_db/lmdb/db_lmdb.cpp:588	[batch] DB resize needed
2018-05-23 09:49:15.401	        b6f93000	INFO 	global	src/blockchain_db/lmdb/db_lmdb.cpp:504	LMDB Mapsize increased.  Old: 57720MiB, New: 58744MiB
2018-05-23 09:49:18.058	        b6f93000	INFO 	blockchain	src/cryptonote_core/blockchain.cpp:4381	Loading precomputed blocks (191524 bytes)
2018-05-23 09:49:18.064	        b6f93000	INFO 	blockchain	src/cryptonote_core/blockchain.cpp:4392	precomputed blocks hash: <1d3df1a177bd6f752d87c0d7b960e502605742721afb39953265f1e0f7f9b01f>, expected 1d3df1a177bd6f752d87c0d7b960e502605742721afb39953265f1e0f7f9b01f
2018-05-23 09:49:18.077	        b6f93000	INFO 	blockchain	src/cryptonote_core/blockchain.cpp:441	63780463562
2018-05-23 09:49:18.085	        b6f93000	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:2087	transaction with hash 1028edfd8c5f7e80db749882b1f3b2cf310a106bdf4f914b45355dcb6ab21829 not found in db
2018-05-23 09:49:18.085	        b6f93000	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:525	Loading checkpoints
2018-05-23 09:49:18.086	        b6f93000	INFO 	checkpoints	src/checkpoints/checkpoints.cpp:220	Blockchain checkpoints file not found
2018-05-23 09:49:18.336	        b6f93000	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:564	[check_and_resize_for_batch] checking DB size
2018-05-23 09:49:18.336	        b6f93000	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:528	DB map size:     61598117888
2018-05-23 09:49:18.336	        b6f93000	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:529	Space used:      50716438528
2018-05-23 09:49:18.336	        b6f93000	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:530	Space remaining: 10881679360
2018-05-23 09:49:18.336	        b6f93000	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:531	Size threshold:  0
2018-05-23 09:49:18.336	        b6f93000	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:533	Percent used: 0.8233  Percent threshold: 0.8000
2018-05-23 09:49:18.337	        b6f93000	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:552	Threshold met (percent-based)
2018-05-23 09:49:18.337	        b6f93000	INFO 	global	src/blockchain_db/lmdb/db_lmdb.cpp:588	[batch] DB resize needed
2018-05-23 09:49:18.337	        b6f93000	INFO 	global	src/blockchain_db/lmdb/db_lmdb.cpp:504	LMDB Mapsize increased.  Old: 58744MiB, New: 59768MiB
2018-05-23 09:49:18.357	        b6f93000	INFO 	checkpoints	src/checkpoints/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 233000 <4f69bec2af6c0852412bdd10c19e6af10c8d738fe2618b5511a98efd03ab477e>
2018-05-23 09:49:18.371	        b6f93000	INFO 	checkpoints	src/checkpoints/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 250000 <f59d31839bd909ec8830b4f7f66ff213f0bd006334c8523daee452725e5c7a79>
2018-05-23 09:49:18.391	        b6f93000	INFO 	checkpoints	src/checkpoints/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 300000 <0c1cd46df6ccff90ec4ab493281f2583c344cd62216c427628990fe9db1bb8b6>
2018-05-23 09:49:18.404	        b6f93000	INFO 	checkpoints	src/checkpoints/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 325000 <4260d56368267bc2a70dd58d73c5ecf23b4e4d96e63c29a868e4a679b0741c7f>
2018-05-23 09:49:18.417	        b6f93000	INFO 	checkpoints	src/checkpoints/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 350000 <74da79f6a136969abd6364bd3d37af273c408d6471e8ab598e80569b42415f86>
2018-05-23 09:49:18.429	        b6f93000	INFO 	checkpoints	src/checkpoints/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 375000 <c80c23e387585e12ffb6649d678e9ba328181797b9583a6d8911b77e25375737>
2018-05-23 09:49:18.443	        b6f93000	INFO 	checkpoints	src/checkpoints/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 400000 <1b2b0e7a30e59691491529a3d506d1ba3d6052d0f6b52198b7330b28a6f1b6ac>
2018-05-23 09:49:18.457	        b6f93000	INFO 	checkpoints	src/checkpoints/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 450000 <4d098b511ca97723e81737c448343cfd4e6dadb3d8a0e757c6e4d595e6e48357>
2018-05-23 09:49:18.457	        b6f93000	INFO 	checkpoints	src/checkpoints/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 500000 <2428f0dbe49796be05ed81b347f53e1f7f44aed0abf641446ec2b94cae066b02>
2018-05-23 09:49:18.477	        b6f93000	INFO 	checkpoints	src/checkpoints/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 550000 <c2e80a636438bd9f7a7ab432a6ad297e35540d80ff5b868bca098124cad2ff8c>
2018-05-23 09:49:18.489	        b6f93000	INFO 	checkpoints	src/checkpoints/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 600000 <f5828ebf7d7d1cb61762c4dfe3ccf4ecab2e1aad23e8113668d981713b7a54c5>
2018-05-23 09:49:18.502	        b6f93000	INFO 	checkpoints	src/checkpoints/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 650000 <1d567f2b491324375a825895c5e7b52857b38e4fed0e42c40909c2d52240b4e0>
2018-05-23 09:49:18.515	        b6f93000	INFO 	checkpoints	src/checkpoints/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 700000 <12be9b3d210b93f574d2526abb9c1ab2a881b479131fd0d4f7dac93875f503cd>
2018-05-23 09:49:18.528	        b6f93000	INFO 	checkpoints	src/checkpoints/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 800000 <2ced10aa85357ab6c14bb12b6b56d1dde28940820dda30911b73a5cc9a301760>
2018-05-23 09:49:18.548	        b6f93000	INFO 	checkpoints	src/checkpoints/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 850000 <00e2b557dde9fd4a9e2e3dd7ddac962f5ca475eb1095bc50aa757fd1218ab0a5>
2018-05-23 09:49:18.561	        b6f93000	INFO 	checkpoints	src/checkpoints/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 900000 <d9958d0e7dcf91a5a7b11de225927bf7efc6eb26240315ce12372be902cc1337>
2018-05-23 09:49:18.569	        b6f93000	INFO 	checkpoints	src/checkpoints/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 913193 <5292d5d56f6ba4de33a58d9a34d263e2cb3c6fee0aed2286fd4ac7f36d53c85f>
2018-05-23 09:49:18.576	        b6f93000	INFO 	checkpoints	src/checkpoints/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 913269 <f8302e6b8ba1c49aad9a854b8d6c79d8272c6239dcbba5a75ed0784c1d4f56a1>
2018-05-23 09:49:18.589	        b6f93000	INFO 	checkpoints	src/checkpoints/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 1288616 <875ac1bc7aa6c5eedc5410abb9c694034f9e7f79dce4c60698baf37009cb6365>
2018-05-23 09:49:18.589	        b6f93000	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:564	[check_and_resize_for_batch] checking DB size
2018-05-23 09:49:18.589	        b6f93000	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:528	DB map size:     62671859712
2018-05-23 09:49:18.589	        b6f93000	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:529	Space used:      50716438528
2018-05-23 09:49:18.589	        b6f93000	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:530	Space remaining: 11955421184
2018-05-23 09:49:18.590	        b6f93000	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:531	Size threshold:  0
2018-05-23 09:49:18.590	        b6f93000	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:533	Percent used: 0.8092  Percent threshold: 0.8000
2018-05-23 09:49:18.590	        b6f93000	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:552	Threshold met (percent-based)
2018-05-23 09:49:18.590	        b6f93000	INFO 	global	src/blockchain_db/lmdb/db_lmdb.cpp:588	[batch] DB resize needed
2018-05-23 09:49:18.590	        b6f93000	INFO 	global	src/blockchain_db/lmdb/db_lmdb.cpp:504	LMDB Mapsize increased.  Old: 59768MiB, New: 60792MiB
2018-05-23 09:49:18.591	        b6f93000	INFO 	checkpoints	src/checkpoints/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 1 <771fbcd656ec1464d3a02ead5e18644030007a0fc664c0a964d30922821a8148>
2018-05-23 09:49:18.591	        b6f93000	INFO 	checkpoints	src/checkpoints/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 10 <c0e3b387e47042f72d8ccdca88071ff96bff1ac7cde09ae113dbb7ad3fe92381>
2018-05-23 09:49:18.594	        b6f93000	INFO 	checkpoints	src/checkpoints/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 100 <ac3e11ca545e57c49fca2b4e8c48c03c23be047c43e471e1394528b1f9f80b2d>
2018-05-23 09:49:18.595	        b6f93000	INFO 	checkpoints	src/checkpoints/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 1000 <5acfc45acffd2b2e7345caf42fa02308c5793f15ec33946e969e829f40b03876>
2018-05-23 09:49:18.607	        b6f93000	INFO 	checkpoints	src/checkpoints/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 10000 <c758b7c81f928be3295d45e230646de8b852ec96a821eac3fea4daf3fcac0ca2>
2018-05-23 09:49:18.620	        b6f93000	INFO 	checkpoints	src/checkpoints/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 22231 <7cb10e29d67e1c069e6e11b17d30b809724255fee2f6868dc14cfc6ed44dfb25>
2018-05-23 09:49:18.633	        b6f93000	INFO 	checkpoints	src/checkpoints/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 29556 <53c484a8ed91e4da621bb2fa88106dbde426fe90d7ef07b9c1e5127fb6f3a7f6>
2018-05-23 09:49:18.645	        b6f93000	INFO 	checkpoints	src/checkpoints/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 50000 <0fe8758ab06a8b9cb35b7328fd4f757af530a5d37759f9d3e421023231f7b31c>
2018-05-23 09:49:18.657	        b6f93000	INFO 	checkpoints	src/checkpoints/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 80000 <a62dcd7b536f22e003ebae8726e9e7276f63d594e264b6f0cd7aab27b66e75e3>
2018-05-23 09:49:18.670	        b6f93000	INFO 	checkpoints	src/checkpoints/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 202612 <bbd604d2ba11ba27935e006ed39c9bfdd99b76bf4a50654bc1e1e61217962698>
2018-05-23 09:49:18.671	        b6f93000	INFO 	checkpoints	src/checkpoints/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 202613 <e2aa337e78df1f98f462b3b1e560c6b914dec47b610698b7b7d1e3e86b6197c2>
2018-05-23 09:49:18.671	        b6f93000	INFO 	checkpoints	src/checkpoints/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 202614 <c29e3dc37d8da3e72e506e31a213a58771b24450144305bcba9e70fa4d6ea6fb>
2018-05-23 09:49:18.684	        b6f93000	INFO 	checkpoints	src/checkpoints/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 205000 <5d3d7a26e6dc7535e34f03def711daa8c263785f73ec1fadef8a45880fde8063>
2018-05-23 09:49:18.698	        b6f93000	INFO 	checkpoints	src/checkpoints/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 220000 <9613f455933c00e3e33ac315cc6b455ee8aa0c567163836858c2d9caff111553>
2018-05-23 09:49:18.711	        b6f93000	INFO 	checkpoints	src/checkpoints/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 230300 <bae7a80c46859db355556e3a9204a337ae8f24309926a1312323fdecf1920e61>
2018-05-23 09:49:18.718	        b6f93000	INFO 	checkpoints	src/checkpoints/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 230700 <93e631240ceac831da1aebfc5dac8f722c430463024763ebafa888796ceaeedf>
2018-05-23 09:49:18.724	        b6f93000	INFO 	checkpoints	src/checkpoints/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 231350 <b5add137199b820e1ea26640e5c3e121fd85faa86a1e39cf7e6cc097bdeb1131>
2018-05-23 09:49:18.731	        b6f93000	INFO 	checkpoints	src/checkpoints/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 232150 <955de8e6b6508af2c24f7334f97beeea651d78e9ade3ab18fec3763be3201aa8>
2018-05-23 09:49:18.744	        b6f93000	INFO 	checkpoints	src/checkpoints/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 249380 <654fb0a81ce3e5caf7e3264a70f447d4bd07586c08fa50f6638cc54da0a52b2d>
2018-05-23 09:49:18.757	        b6f93000	INFO 	checkpoints	src/checkpoints/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 460000 <75037a7aed3e765db96c75bcf908f59d690a5f3390baebb9edeafd336a1c4831>
2018-05-23 09:49:18.758	        b6f93000	INFO 	checkpoints	src/checkpoints/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 500000 <2428f0dbe49796be05ed81b347f53e1f7f44aed0abf641446ec2b94cae066b02>
2018-05-23 09:49:18.758	        b6f93000	INFO 	checkpoints	src/checkpoints/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 600000 <f5828ebf7d7d1cb61762c4dfe3ccf4ecab2e1aad23e8113668d981713b7a54c5>
2018-05-23 09:49:18.758	        b6f93000	INFO 	checkpoints	src/checkpoints/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 700000 <12be9b3d210b93f574d2526abb9c1ab2a881b479131fd0d4f7dac93875f503cd>
2018-05-23 09:49:18.766	        b6f93000	INFO 	checkpoints	src/checkpoints/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 825000 <56503f9ad766774b575be3aff73245e9d159be88132c93d1754764f28da2ff60>
2018-05-23 09:49:18.766	        b6f93000	INFO 	checkpoints	src/checkpoints/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 900000 <d9958d0e7dcf91a5a7b11de225927bf7efc6eb26240315ce12372be902cc1337>
2018-05-23 09:49:18.766	        b6f93000	INFO 	checkpoints	src/checkpoints/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 913193 <5292d5d56f6ba4de33a58d9a34d263e2cb3c6fee0aed2286fd4ac7f36d53c85f>
2018-05-23 09:49:18.780	        b6f93000	INFO 	checkpoints	src/checkpoints/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 1000000 <a886ef5149902d8342475fee9bb296341b891ac67c4842f47a833f23c00ed721>
2018-05-23 09:49:18.787	        b6f93000	INFO 	checkpoints	src/checkpoints/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 1100000 <3fd720c5c8b3072fc1ccda922dec1ef25f9ed88a1e6ad4103d0fe00b180a5903>
2018-05-23 09:49:18.799	        b6f93000	INFO 	checkpoints	src/checkpoints/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 1150000 <1dd16f626d18e1e988490dfd06de5920e22629c972c58b4d8daddea0038627b2>
2018-05-23 09:49:18.805	        b6f93000	INFO 	checkpoints	src/checkpoints/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 1200000 <fa7d13a90850882060479d100141ff84286599ae39c3277c8ea784393f882d1f>
2018-05-23 09:49:18.812	        b6f93000	INFO 	checkpoints	src/checkpoints/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 1300000 <31b34272343a44a9f4ac7de7a8fcf3b7d8a3124d7d6870affd510d2f37e74cd0>
2018-05-23 09:49:18.820	        b6f93000	INFO 	checkpoints	src/checkpoints/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 1390000 <a8f5649dd4ded60eedab475f2bec8c934681c07e3cf640e9be0617554f13ff6c>
2018-05-23 09:49:18.820	        b6f93000	INFO 	checkpoints	src/checkpoints/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 1450000 <ac94e8860093bc7c83e4e91215cba1d663421ecf4067a0ae609c3a8b52bcfac2>
2018-05-23 09:49:18.820	        b6f93000	INFO 	checkpoints	src/checkpoints/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 1530000 <01759bce497ec38e63c78b1038892169203bb78f87e488172f6b854fcd63ba7e>
2018-05-23 09:49:18.821	        b6f93000	INFO 	global	src/daemon/core.h:92	Core initialized OK
2018-05-23 09:49:18.821	        b6f93000	INFO 	global	src/daemon/rpc.h:74	Starting core RPC server...
2018-05-23 09:49:18.821	        b6f93000	INFO 	net.http	contrib/epee/include/net/http_server_impl_base.h:89	Run net_service loop( 2 threads)...
2018-05-23 09:49:18.821	[SRV_MAIN]	INFO 	global	src/daemon/rpc.h:79	core RPC server started ok
2018-05-23 09:49:18.833	[SRV_MAIN]	INFO 	daemon	src/daemon/daemon.cpp:173	Starting ZMQ server...
2018-05-23 09:49:18.834	[SRV_MAIN]	INFO 	daemon	src/daemon/daemon.cpp:177	ZMQ server started at 127.0.0.1:18082.
2018-05-23 09:49:18.834	[SRV_MAIN]	INFO 	global	src/daemon/p2p.h:78	Starting p2p net loop...
2018-05-23 09:49:18.834	[SRV_MAIN]	INFO 	net.p2p	src/p2p/net_node.inl:611	Run net_service loop( 10 threads)...
2018-05-23 09:49:19.835	[P2P1]	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:1353	[1;33m
**********************************************************************
The daemon will start synchronizing with the network. This may take a long time to complete.

You can set the level of process detailization through "set_log <level|categories>" command,
where <level> is between 0 (no details) and 4 (very verbose), or custom category based levels (eg, *:WARNING).

Use the "help" command to see the list of available commands.
Use "help <command>" to see a command's documentation.
**********************************************************************
```

Few hours later, it hangs after ""DB resize needed"" again.
```
2018-05-23 12:00:27.047	[P2P9]	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:564	[check_and_resize_for_batch] checking DB size
2018-05-23 12:00:27.047	[P2P9]	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:528	DB map size:     63745601536
2018-05-23 12:00:27.047	[P2P9]	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:529	Space used:      51181117440
2018-05-23 12:00:27.047	[P2P9]	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:530	Space remaining: 12564484096
2018-05-23 12:00:27.047	[P2P9]	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:531	Size threshold:  0
2018-05-23 12:00:27.047	[P2P9]	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:533	Percent used: 0.8029  Percent threshold: 0.8000
2018-05-23 12:00:27.048	[P2P9]	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:552	Threshold met (percent-based)
2018-05-23 12:00:27.048	[P2P9]	INFO 	global	src/blockchain_db/lmdb/db_lmdb.cpp:588	[batch] DB resize needed
2018-05-23 12:00:30.382	[P2P1]	INFO 	net.p2p.msg	src/cryptonote_protocol/cryptonote_protocol_handler.inl:804	[151.228.223.71:18080 OUT] Received NOTIFY_REQUEST_GET_OBJECTS (20 blocks, 0 txes)
2018-05-23 12:00:31.758	[P2P2]	INFO 	net.p2p	src/p2p/net_node.inl:921	[0.0.0.0:0 OUT] Connect failed to 195.226.50.184:18080
2018-05-23 12:00:36.759	[P2P2]	INFO 	net.p2p	src/p2p/net_node.inl:921	[0.0.0.0:0 OUT] Connect failed to 171.25.166.126:18080
2018-05-23 12:00:37.032	[P2P2]	INFO 	net.p2p	src/p2p/net_node.inl:1761	[93.158.203.58:18080 1025f997-7f89-2ee1-2ba5-c16a6e645330 OUT] NEW CONNECTION
2018-05-23 12:01:42.170	[P2P0]	INFO 	net.p2p	src/p2p/net_node.inl:1776	[93.158.203.58:18080 1025f997-7f89-2ee1-2ba5-c16a6e645330 OUT] CLOSE CONNECTION
```

# Discussion History
## moneromooo-monero | 2018-05-23T18:06:12+00:00
Do you get a warning about glibc when you start monerod?

If not, next time it does this:
gdb /path/to/monerod \`pidof monerod\`
thread apply all bt full

Post the output of this either here or fpaste.org or pastebin.mozilla.org or paste.debian.net.

## Lafudoci | 2018-05-24T06:13:15+00:00
@moneromooo-monero , sorry for my ignorance, do you mean run the gdb &  "thread apply all bt full" commands after next time the monerod hangs? Will it save outpost into a log file?

## moneromooo-monero | 2018-05-24T08:09:33+00:00
Yes, you need to run these two next time it hangs that way. The "thread apply all bt full" is from within gdb. It will save the output to the console. Press enter multiple times till you go through everything.


## Lafudoci | 2018-05-25T01:25:07+00:00
OK, here it is.
https://paste.fedoraproject.org/paste/WSuQEJONMM2KqHOltPZcbg

## moneromooo-monero | 2018-05-25T09:50:50+00:00
That looks like possibly a bug in the logger. It should not be locked on all threads it uses.

## Lafudoci | 2018-05-25T11:36:31+00:00
TBH, I have no idea what you just said XD. If there is anything I could help, please give me instructions.

## moneromooo-monero | 2018-05-25T12:05:31+00:00
If you're willing to do it, then running a debug build would give much better info in the log. I was hoping to see the internals of the mutex that are held, but you seem to be running a build without much debug info so that did not get included. So if you can run a debug build, please run thread apply all bt full again.

## Lafudoci | 2018-05-25T17:56:47+00:00
OK, I'll post when it's done.

## Lafudoci | 2018-05-26T09:08:37+00:00
Done, here it is :
https://paste.fedoraproject.org/paste/HcO4CMrQQzGnnrKu-Dyo1g

## moneromooo-monero | 2018-05-26T14:04:30+00:00
Thanks.
The interesting parts seems to be optimized out, unfortunately.
Maybe you repro this again, then:
- find the threads with el::base::Writer::initializeLogger in their stack (in this example, thread 24 only)
- switch to the thread: thread 24
- walk up the stack till you reach that level (in this exmaple level 7): up 7
- type "info locals"
- type: "print *ELPP"
- type: print ELPP->m_mutex

Some of those might fail, so there are several which might work.


## Lafudoci | 2018-05-26T16:18:33+00:00
I didn't terminate the monerd since last hang. So it's still thread 24 and # 7.
But it failed after "info locals".
```
(gdb) thread 24
[Switching to thread 24 (Thread 0x9e5ff450 (LWP 1424))]
#7  0xb641a90e in el::base::Writer::initializeLogger (this=0x9e5fdaf8, loggerId="global", lookup=true, needLock=true)
    at /home/linaro/monero/external/easylogging++/easylogging++.cc:2564
2564          m_logger->acquireLock();  // This should not be unlocked by checking m_proceed because
(gdb) info locals
No locals.
(gdb) print *ELPP
No symbol "ELPP" in current context.
(gdb) print ELPP->m_mutex
No symbol "ELPP" in current context.
(gdb)
```

## moneromooo-monero | 2018-05-26T19:24:27+00:00
Try: print *m_logger

## Lafudoci | 2018-05-27T01:42:07+00:00
```
(gdb) print *m_logger
$1 = {<el::base::threading::ThreadSafe> = {_vptr.ThreadSafe = 0xb644ca90 <vtable for el::Logger+8>, m_mutex = {<std::__recursive_mutex_base> = {_M_mutex = {__data = {__lock = 2,
            __count = 1, __owner = 1421, __kind = 1, __nusers = 1, {__spins = 0, __list = {__next = 0x0}}},
          __size = "\002\000\000\000\001\000\000\000\215\005\000\000\001\000\000\000\001\000\000\000\000\000\000", __align = 2}}, <No data fields>}}, <el::Loggable> = {
    _vptr.Loggable = 0xb644cab0 <vtable for el::Logger+40>}, m_id = "global", m_typedConfigurations = 0x810cec80, m_stream = <incomplete type>, m_parentApplicationName = "",
  m_isConfigured = true,
  m_configurations = {<el::base::utils::RegistryWithPred<el::Configuration, el::Configuration::Predicate>> = {<el::base::utils::AbstractRegistry<el::Configuration, std::vector<el::Configuration*, std::allocator<el::Configuration*> > >> = {<el::base::threading::ThreadSafe> = {_vptr.ThreadSafe = 0x7f85dc8c <vtable for el::Configurations+8>,
          m_mutex = {<std::__recursive_mutex_base> = {_M_mutex = {__data = {__lock = 0, __count = 0, __owner = 0, __kind = 1, __nusers = 0, {__spins = 0, __list = {__next = 0x0}}},
                __size = '\000' <repeats 12 times>, "\001\000\000\000\000\000\000\000\000\000\000", __align = 0}}, <No data fields>}}, m_list = std::vector of length 72, capacity 128 = {
          0x8100c550, 0x8100bde0, 0x810db430, 0x80feca30, 0x80feb3f0, 0x8101e5d8, 0x8100d2a0, 0x810dd290, 0x810dd7d0, 0x8100a460, 0x810dd4f0, 0x810dd410, 0x810dd368, 0x810dd560,
          0x8100b678, 0x8100b540, 0x810e2aa0, 0x810dd218, 0x810dd240, 0x810dcf88, 0x810dcfb0, 0x810dcfd8, 0x810dd000, 0x810dd028, 0x810dd050, 0x810dd078, 0x810ded90, 0x810dedb8,
          0x810dede0, 0x810dee08, 0x810dee30, 0x810dee58, 0x810dee80, 0x810dd170, 0x810dd198, 0x810dd1c0, 0x810defb0, 0x810defd8, 0x810df000, 0x810df028, 0x810df050, 0x810df078,
          0x810df0a0, 0x810df0c8, 0x810df0f0, 0x810df118, 0x810df140, 0x810df168, 0x810df190, 0x810df1b8, 0x810ce510, 0x810ce538, 0x810ce560, 0x810ce588, 0x810ce5b0, 0x810ce5d8,
          0x810ce600, 0x810ce628, 0x810ce650, 0x810ce678, 0x810ce6a0, 0x810ce6c8, 0x810ce6f0, 0x810ce718, 0x810ce740, 0x810e2a38, 0x810deea8, 0x810deef8, 0x810def48, 0x810ce998,
          0x810ce9e8, 0x810cea38}}, <No data fields>}, m_configurationFile = "", m_isFromFile = false}, m_unflushedCount = std::map with 7 elements = {[el::Level::Trace] = 0,
    [el::Level::Debug] = 0, [el::Level::Fatal] = 0, [el::Level::Error] = 0, [el::Level::Warning] = 0, [el::Level::Verbose] = 0, [el::Level::Info] = 0}, m_logStreamsReference = 0x80fe9128,
  m_logBuilder = std::shared_ptr (count 25, weak 0) 0x80fe8f88}
```


## moneromooo-monero | 2018-05-27T10:31:16+00:00
I added some logs here: https://github.com/moneromooo-monero/bitmonero/tree/dlt

These use stdout, since the problem seems log related.
Once you get the hang again, please paste the last... 200 lines from it.


## Lafudoci | 2018-05-27T11:04:24+00:00
Do you mean build debug from that repo "dlt" branch and get the log level 1 after hang?

## Lafudoci | 2018-05-27T11:32:10+00:00
I picked dlt commit to tag v0.12.1. It's building now.

## Lafudoci | 2018-05-28T01:37:43+00:00
Done, https://paste.fedoraproject.org/paste/ZhLABsExMKnAAoFkRKwqEQ

## moneromooo-monero | 2018-05-28T10:11:32+00:00
Thanks. I see no dlt logs here though. For this test, you can use default log levels. Maybe the dlt logs got buffered away since they use stdio and the logging system might not.

## Lafudoci | 2018-05-29T01:37:24+00:00
It's still running after last night I changed to default log level. It seems there was a successful db resize. But I did not see dlt in the log, not sure if I'm doing it right.
Here is the log around db resize: https://paste.fedoraproject.org/paste/hNdjHUwTmTHwNpw2WLj~AA

## moneromooo-monero | 2018-05-29T11:28:20+00:00
The dlt are printed to stdout, they will not be in the log. This is because the log system seems to be involved in the hang so I can't use it for those logs. You don't need a non default log level for this test though, and the dlt will log a LOT.
To check you have the right code: git grep "DLT:" external
This should show a few printf calls.

## Lafudoci | 2018-05-29T12:08:42+00:00
OK, git grep "DLT:" external got many codes and screen repeatedly showed lots of ELPP unlock msg below. So I think it's running the correct version.
```
DLT: 0xa19ff450: ELPP unlock
DLT: 0xa19ff450: entering initializeLogger
DLT: 0xa19ff450: locking initializeLogger
```
So will the DLT we needed show on screen after it hangs? But how can I save it for the last 200 lines?

## moneromooo-monero | 2018-05-29T12:26:17+00:00
After it hangs, they should stop. You can either copy them from the console, or redirect them with | tee output.txt

## Lafudoci | 2018-06-06T11:43:31+00:00
It' weird... between these days, there were 3 successful db resize without any issue. It's different from previous condition (hangs on every resize). @moneromooo-monero, will you recommend update to v12.2 and pick DLT commit then continue the test?

## moneromooo-monero | 2018-06-06T12:07:23+00:00
The extra logs probably change timings so that the deadlock condition never occured. You can try 0.12.2.0 if you want, since the deadlock was not fixed AFAIK.

## D4nte | 2018-08-04T07:31:36+00:00
Hi,

Encountering similar issue
```
2018-08-04 05:47:46.858 [P2P1]  INFO    global  src/blockchain_db/lmdb/db_lmdb.cpp:588  [batch] DB resize needed
2018-08-04 05:47:46.921 [P2P1]  INFO    global  src/blockchain_db/lmdb/db_lmdb.cpp:504  LMDB Mapsize increased.  Old: 65815MiB, New: 66839MiB
2018-08-04 05:47:53.415 [P2P1]  INFO    global  src/blockchain_db/lmdb/db_lmdb.cpp:588  [batch] DB resize needed
```
Once restarted, all good. Happens maybe once a day on a resource-limited device (old Intel NUC).

I compiled v0.12.3.0 locally on Ubuntu 18.04 LTS

Anything I can provide to assist with resolution?

## moneromooo-monero | 2018-08-04T12:46:50+00:00
Yes, an all thread stack trace:

gdb /path/to/monerod \`pidof monerod\`
thread apply all bt


## D4nte | 2018-08-05T02:31:35+00:00
[gdb.txt](https://github.com/monero-project/monero/files/2259987/gdb.txt)
here we go.

I'll try with a debug release later

## moneromooo-monero | 2018-08-05T09:55:08+00:00
From there:

thread 19
up 3
info locals
print ELPP
print *ELPP
print ELPP->m_mutex
print *m_logger

Also check in the log file whether an exception was logged.

## D4nte | 2018-08-05T10:23:40+00:00
Here is the exception:

```
2018-08-05 06:29:15.181 [P2P6]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:310     [45.79.204.241:51810 OUT] Sync data returned a new top block candidate: 1592828 -> 1632085 [
Your node is 39257 blocks (54 days) behind]
SYNCHRONIZATION started
2018-08-05 06:29:31.778 [P2P0]  INFO    stacktrace      src/common/stack_trace.cpp:124  Exception: std::runtime_error
2018-08-05 06:29:31.778 [P2P0]  INFO    stacktrace      src/common/stack_trace.cpp:125  Unwound call stack:
2018-08-05 06:29:32.044 [P2P0]  INFO    stacktrace      src/common/stack_trace.cpp:163      [1] /usr/local/bin/monerod:__cxa_throw+0x108 [0x55832d562e48]
2018-08-05 06:29:32.044 [P2P0]  INFO    stacktrace      src/common/stack_trace.cpp:163      [2] /usr/local/bin/monerod:epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connect
ion_context_t<cryptonote::cryptonote_connection_context> > >::host_count(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, int)+0x51e [0x55832d45462e]
2018-08-05 06:29:32.045 [P2P0]  INFO    stacktrace      src/common/stack_trace.cpp:163      [3] /usr/local/bin/monerod:epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connect
ion_context_t<cryptonote::cryptonote_connection_context> > >::shutdown()+0x1e2 [0x55832d454b42]
2018-08-05 06:29:32.045 [P2P0]  INFO    stacktrace      src/common/stack_trace.cpp:163      [4] /usr/local/bin/monerod:epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connect
ion_context_t<cryptonote::cryptonote_connection_context> > >::close()+0x98 [0x55832d454c38]
2018-08-05 06:29:32.045 [P2P0]  INFO    stacktrace      src/common/stack_trace.cpp:163      [5] /usr/local/bin/monerod:epee::levin::async_protocol_handler_config<nodetool::p2p_connection_context_t<crypton
ote::cryptonote_connection_context> >::close(boost::uuids::uuid)+0x3bd [0x55832d43110d]
2018-08-05 06:29:32.045 [P2P0]  INFO    stacktrace      src/common/stack_trace.cpp:163      [6] /usr/local/bin/monerod:nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::
do_handshake_with_peer(unsigned long&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&, bool)+0x5aa [0x55832d482fda]
2018-08-05 06:29:32.045 [P2P0]  INFO    stacktrace      src/common/stack_trace.cpp:163      [7] /usr/local/bin/monerod:nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::
check_connection_and_handshake_with_peer(epee::net_utils::network_address const&, unsigned long)+0x608 [0x55832d486ec8]
2018-08-05 06:29:32.045 [P2P0]  INFO    stacktrace      src/common/stack_trace.cpp:163      [8] /usr/local/bin/monerod:nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::
gray_peerlist_housekeeping()+0x139 [0x55832d4876d9]
2018-08-05 06:29:32.045 [P2P0]  INFO    stacktrace      src/common/stack_trace.cpp:163      [9] /usr/local/bin/monerod:nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::
idle_worker()+0xb9 [0x55832d424a99]
2018-08-05 06:29:32.045 [P2P0]  INFO    stacktrace      src/common/stack_trace.cpp:163      [10] /usr/local/bin/monerod:epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2
p_connection_context_t<cryptonote::cryptonote_connection_context> > >::global_timer_handler(boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connecti
on_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext_base>)+0x2a [0x55832d44070a]
2018-08-05 06:29:32.045 [P2P0]  INFO    stacktrace      src/common/stack_trace.cpp:163      [11] /usr/local/bin/monerod:boost::asio::detail::wait_handler<boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, ep
ee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::shared_ptr<epee::net_utils::boosted_tcp_serv
er<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext_base> >, boost::_bi::list2<boost::_bi::value<epee::net_utils:
:boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >*>, boost::_bi::value<boost::shared_ptr<epee::net_utils::boosted_tc
p_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext_base> > > > >::do_complete(boost::asio::detail::task_io
_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long)+0xee [0x55832d425cee]
2018-08-05 06:29:32.045 [P2P0]  INFO    stacktrace      src/common/stack_trace.cpp:163      [12] /usr/local/bin/monerod:epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2
p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread()+0x878 [0x55832d43dc28]
2018-08-05 06:29:32.045 [P2P0]  INFO    stacktrace      src/common/stack_trace.cpp:163      [13] /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.65.1+0x11bcd [0x7f77d2159bcd]
2018-08-05 06:29:32.045 [P2P0]  INFO    stacktrace      src/common/stack_trace.cpp:163      [14] /lib/x86_64-linux-gnu/libpthread.so.0+0x76db [0x7f77d15ec6db]
2018-08-05 06:29:32.045 [P2P0]  INFO    stacktrace      src/common/stack_trace.cpp:163      [15] /lib/x86_64-linux-gnu/libc.so.6:clone+0x3f [0x7f77d131588f]
2018-08-05 06:29:32.045 [P2P0]  INFO    stacktrace      src/common/stack_trace.cpp:163
2018-08-05 06:30:14.622 [P2P5]  INFO    global  src/blockchain_db/lmdb/db_lmdb.cpp:588  [batch] DB resize needed
```

Sorry, for the rest will need to wait for a re-occurrence.

## moneromooo-monero | 2018-10-19T10:56:27+00:00
That host_count exception is fixed, from a while ago. It is unrelated to the database code.

## Lafudoci | 2018-10-20T03:28:28+00:00
For update, my tinker board never happened this issue again after my last response at Jun. It went through 0.12 to 0.13. Now it's stable on release v0.13.0.2.

## moneromooo-monero | 2018-10-20T17:55:43+00:00
OK, thanks for confirming.

## selsta | 2022-03-16T15:40:08+00:00
No other similar reports, closing.

## alexscarter | 2026-01-09T23:18:47+00:00
Commenting on this as it appears to be an issue for me. Tried on an old intel x86_64 thinkpad and that seems to work flawlessly. The same cannot be said for my amd r9 5900x system. I tried the pre-packaged v0.18.4.4, and even building the debug version from source- both hang on the db resize. However, the binary I built from source doesn't send my system load average above 15, whereas the prebuilt would send the load average to 35+, completely rendering the system frozen. The cpu does not work that hard, but my M.2 shows usage during the freeze, along with files not being able to save, etc (other problems with a non-cooperating storage device). I'll post the log of

gdb /path/to/monerod `pidof monerod`
thread apply all bt

[gdb.txt](https://github.com/user-attachments/files/24537171/gdb.txt)
Let me know what else I can provide. Thanks!

## selsta | 2026-01-10T22:50:26+00:00
@xlae13 please open a new issue for this

# Action History
- Created by: Lafudoci | 2018-05-23T17:00:13+00:00
- Closed at: 2022-03-16T15:40:08+00:00
