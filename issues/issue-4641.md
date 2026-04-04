---
title: monerod fails to start
source_url: https://github.com/monero-project/monero/issues/4641
author: wililupy
assignees: []
labels: []
created_at: '2018-10-18T02:02:39+00:00'
updated_at: '2018-10-18T18:20:06+00:00'
type: issue
status: closed
closed_at: '2018-10-18T18:20:06+00:00'
---

# Original Description
Hello,
I just upgraded to monero-gui v0.13.0.2-release for Mac. I had to upgrade openssl on my mac to get the GUI to work properly, but now the daemon is not starting.

I have this in my ~/.bitmonero/bitmonero.log:

```2018-10-18 01:54:03.757	     0x1193a35c0	INFO 	net.p2p	src/p2p/net_node.inl:377	Added node: 5.9.100.248:18080
2018-10-18 01:54:03.762	     0x1193a35c0	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:917	Set server type to: 2 from name: P2P, prefix_name = P2P
2018-10-18 01:54:03.762	     0x1193a35c0	INFO 	net.p2p	src/p2p/net_node.inl:571	Binding on 0.0.0.0:18080
2018-10-18 01:54:03.763	     0x1193a35c0	FATAL	net	contrib/epee/include/net/abstract_tcp_server2.inl:856	Error starting server: bind: Address already in use
2018-10-18 01:54:03.763	     0x1193a35c0	ERROR	net.p2p	src/p2p/net_node.inl:573	Failed to bind server
2018-10-18 01:54:03.764	     0x1193a35c0	INFO 	global	src/daemon/core.h:103	Deinitializing core...
2018-10-18 01:54:03.764	     0x1193a35c0	ERROR	daemon	src/daemon/core.h:108	Failed to deinitialize core...
2018-10-18 01:54:03.764	     0x1193a35c0	INFO 	global	src/daemon/protocol.h:75	Stopping cryptonote protocol...
2018-10-18 01:54:03.764	     0x1193a35c0	INFO 	global	src/daemon/protocol.h:79	Cryptonote protocol stopped successfully
2018-10-18 01:54:03.764	     0x1193a35c0	ERROR	daemon	src/daemon/main.cpp:295	Exception in main! Failed to initialize p2p server.
2018-10-18 02:06:09.802	     0x10e5e75c0	INFO 	logging	contrib/epee/src/mlog.cpp:242	New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-10-18 02:06:09.802	     0x10e5e75c0	INFO 	logging	contrib/epee/src/mlog.cpp:242	New log categories: *:INFO,global:INFO,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-10-18 02:06:09.803	     0x10e5e75c0	INFO 	global	src/daemon/main.cpp:287	Monero 'Beryllium Bullet' (v0.13.0.2-release)
2018-10-18 02:06:09.803	     0x10e5e75c0	INFO 	daemon	src/daemon/main.cpp:289	Moving from main() into the daemonize now.
2018-10-18 02:06:09.803	     0x10e5e75c0	INFO 	global	src/daemon/protocol.h:53	Initializing cryptonote protocol...
2018-10-18 02:06:09.803	     0x10e5e75c0	INFO 	global	src/daemon/protocol.h:58	Cryptonote protocol initialized OK
2018-10-18 02:06:09.803	     0x10e5e75c0	INFO 	global	src/daemon/p2p.h:63	Initializing p2p server...
2018-10-18 02:06:09.803	     0x10e5e75c0	INFO 	net.throttle	contrib/epee/src/network_throttle-detail.cpp:162	Setting LIMIT: 2048 kbps
2018-10-18 02:06:09.804	     0x10e5e75c0	INFO 	net.p2p	src/p2p/net_node.inl:1929	Set limit-up to 2048 kB/s
2018-10-18 02:06:09.804	     0x10e5e75c0	INFO 	net.throttle	contrib/epee/src/network_throttle-detail.cpp:162	Setting LIMIT: 8192 kbps
2018-10-18 02:06:09.804	     0x10e5e75c0	INFO 	net.throttle	contrib/epee/src/network_throttle-detail.cpp:162	Setting LIMIT: 8192 kbps
2018-10-18 02:06:09.804	     0x10e5e75c0	INFO 	net.p2p	src/p2p/net_node.inl:1942	Set limit-down to 8192 kB/s
2018-10-18 02:06:09.804	     0x10e5e75c0	INFO 	net.throttle	contrib/epee/src/network_throttle-detail.cpp:162	Setting LIMIT: 2048 kbps
2018-10-18 02:06:09.804	     0x10e5e75c0	INFO 	net.p2p	src/p2p/net_node.inl:1964	Set limit-up to 2048 kB/s
2018-10-18 02:06:09.804	     0x10e5e75c0	INFO 	net.throttle	contrib/epee/src/network_throttle-detail.cpp:162	Setting LIMIT: 8192 kbps
2018-10-18 02:06:09.804	     0x10e5e75c0	INFO 	net.throttle	contrib/epee/src/network_throttle-detail.cpp:162	Setting LIMIT: 8192 kbps
2018-10-18 02:06:09.804	     0x10e5e75c0	INFO 	net.p2p	src/p2p/net_node.inl:1968	Set limit-down to 8192 kB/s
2018-10-18 02:06:09.804	  0x700000b72000	INFO 	net.dns	src/common/dns_utils.cpp:252	adding trust anchor: . IN DS 19036 8 2 49AAC11D7B6F6446702E54A1607371607A1A41855200FD2CE1CDDE32F24E8FB5

2018-10-18 02:06:09.804	  0x700000b72000	INFO 	net.dns	src/common/dns_utils.cpp:252	adding trust anchor: . IN DS 20326 8 2 E06D44B80B8F1D39A95C0B0D7C65D08458E880409BBC683457104237C7F8EC8D

2018-10-18 02:06:09.920	  0x700000cfb000	INFO 	net.p2p	src/p2p/net_node.inl:481	dns_threads[3] addr_str: seeds.moneroseeds.li  number of results: 0
2018-10-18 02:06:09.920	  0x700000c78000	INFO 	net.p2p	src/p2p/net_node.inl:481	dns_threads[2] addr_str: seeds.moneroseeds.ch  number of results: 0
2018-10-18 02:06:09.921	  0x700000b72000	INFO 	net.p2p	src/p2p/net_node.inl:481	dns_threads[0] addr_str: seeds.moneroseeds.se  number of results: 0
2018-10-18 02:06:09.921	  0x700000bf5000	INFO 	net.p2p	src/p2p/net_node.inl:481	dns_threads[1] addr_str: seeds.moneroseeds.ae.org  number of results: 0
2018-10-18 02:06:09.921	     0x10e5e75c0	INFO 	net.p2p	src/p2p/net_node.inl:519	DNS seed node lookup either timed out or failed, falling back to defaults
2018-10-18 02:06:09.922	     0x10e5e75c0	INFO 	net.p2p	src/p2p/net_node.inl:360	Resolving node address: host=107.152.130.98, port=18080
2018-10-18 02:06:09.929	     0x10e5e75c0	INFO 	net.p2p	src/p2p/net_node.inl:377	Added node: 107.152.130.98:18080
2018-10-18 02:06:09.929	     0x10e5e75c0	INFO 	net.p2p	src/p2p/net_node.inl:360	Resolving node address: host=161.67.132.39, port=18080
2018-10-18 02:06:09.929	     0x10e5e75c0	INFO 	net.p2p	src/p2p/net_node.inl:377	Added node: 161.67.132.39:18080
2018-10-18 02:06:09.929	     0x10e5e75c0	INFO 	net.p2p	src/p2p/net_node.inl:360	Resolving node address: host=163.172.182.165, port=18080
2018-10-18 02:06:09.929	     0x10e5e75c0	INFO 	net.p2p	src/p2p/net_node.inl:377	Added node: 163.172.182.165:18080
2018-10-18 02:06:09.929	     0x10e5e75c0	INFO 	net.p2p	src/p2p/net_node.inl:360	Resolving node address: host=195.154.123.123, port=18080
2018-10-18 02:06:09.930	     0x10e5e75c0	INFO 	net.p2p	src/p2p/net_node.inl:377	Added node: 195.154.123.123:18080
2018-10-18 02:06:09.930	     0x10e5e75c0	INFO 	net.p2p	src/p2p/net_node.inl:360	Resolving node address: host=198.74.231.92, port=18080
2018-10-18 02:06:09.930	     0x10e5e75c0	INFO 	net.p2p	src/p2p/net_node.inl:377	Added node: 198.74.231.92:18080
2018-10-18 02:06:09.930	     0x10e5e75c0	INFO 	net.p2p	src/p2p/net_node.inl:360	Resolving node address: host=212.83.172.165, port=18080
2018-10-18 02:06:09.930	     0x10e5e75c0	INFO 	net.p2p	src/p2p/net_node.inl:377	Added node: 212.83.172.165:18080
2018-10-18 02:06:09.930	     0x10e5e75c0	INFO 	net.p2p	src/p2p/net_node.inl:360	Resolving node address: host=212.83.175.67, port=18080
2018-10-18 02:06:09.930	     0x10e5e75c0	INFO 	net.p2p	src/p2p/net_node.inl:377	Added node: 212.83.175.67:18080
2018-10-18 02:06:09.930	     0x10e5e75c0	INFO 	net.p2p	src/p2p/net_node.inl:360	Resolving node address: host=5.9.100.248, port=18080
2018-10-18 02:06:09.930	     0x10e5e75c0	INFO 	net.p2p	src/p2p/net_node.inl:377	Added node: 5.9.100.248:18080
2018-10-18 02:06:09.935	     0x10e5e75c0	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:917	Set server type to: 2 from name: P2P, prefix_name = P2P
2018-10-18 02:06:09.935	     0x10e5e75c0	INFO 	net.p2p	src/p2p/net_node.inl:571	Binding on 0.0.0.0:18080
2018-10-18 02:06:09.935	     0x10e5e75c0	FATAL	net	contrib/epee/include/net/abstract_tcp_server2.inl:856	Error starting server: bind: Address already in use
2018-10-18 02:06:09.935	     0x10e5e75c0	ERROR	net.p2p	src/p2p/net_node.inl:573	Failed to bind server
2018-10-18 02:06:09.936	     0x10e5e75c0	INFO 	global	src/daemon/core.h:103	Deinitializing core...
2018-10-18 02:06:09.936	     0x10e5e75c0	ERROR	daemon	src/daemon/core.h:108	Failed to deinitialize core...
2018-10-18 02:06:09.936	     0x10e5e75c0	INFO 	global	src/daemon/protocol.h:75	Stopping cryptonote protocol...
2018-10-18 02:06:09.936	     0x10e5e75c0	INFO 	global	src/daemon/protocol.h:79	Cryptonote protocol stopped successfully
2018-10-18 02:06:09.936	     0x10e5e75c0	ERROR	daemon	src/daemon/main.cpp:295	Exception in main! Failed to initialize p2p server.

```

When I try to run monerod --log-level 1 this is the output I get:

```
2018-10-18 01:54:02,714 INFO  [default] Page size: 4096
2018-10-18 01:54:03.719	     0x1193a35c0	INFO 	global	src/daemon/main.cpp:287	Monero 'Beryllium Bullet' (v0.13.0.2-release)
2018-10-18 01:54:03.719	     0x1193a35c0	INFO 	daemon	src/daemon/main.cpp:289	Moving from main() into the daemonize now.
2018-10-18 01:54:03.719	     0x1193a35c0	INFO 	global	src/daemon/protocol.h:53	Initializing cryptonote protocol...
2018-10-18 01:54:03.719	     0x1193a35c0	INFO 	global	src/daemon/protocol.h:58	Cryptonote protocol initialized OK
2018-10-18 01:54:03.719	     0x1193a35c0	INFO 	global	src/daemon/p2p.h:63	Initializing p2p server...
2018-10-18 01:54:03.719	     0x1193a35c0	INFO 	net.throttle	contrib/epee/src/network_throttle-detail.cpp:162	Setting LIMIT: 2048 kbps
2018-10-18 01:54:03.719	     0x1193a35c0	INFO 	net.p2p	src/p2p/net_node.inl:1929	Set limit-up to 2048 kB/s
2018-10-18 01:54:03.719	     0x1193a35c0	INFO 	net.throttle	contrib/epee/src/network_throttle-detail.cpp:162	Setting LIMIT: 8192 kbps
2018-10-18 01:54:03.720	     0x1193a35c0	INFO 	net.throttle	contrib/epee/src/network_throttle-detail.cpp:162	Setting LIMIT: 8192 kbps
2018-10-18 01:54:03.720	     0x1193a35c0	INFO 	net.p2p	src/p2p/net_node.inl:1942	Set limit-down to 8192 kB/s
2018-10-18 01:54:03.720	     0x1193a35c0	INFO 	net.throttle	contrib/epee/src/network_throttle-detail.cpp:162	Setting LIMIT: 2048 kbps
2018-10-18 01:54:03.720	     0x1193a35c0	INFO 	net.p2p	src/p2p/net_node.inl:1964	Set limit-up to 2048 kB/s
2018-10-18 01:54:03.720	     0x1193a35c0	INFO 	net.throttle	contrib/epee/src/network_throttle-detail.cpp:162	Setting LIMIT: 8192 kbps
2018-10-18 01:54:03.720	     0x1193a35c0	INFO 	net.throttle	contrib/epee/src/network_throttle-detail.cpp:162	Setting LIMIT: 8192 kbps
2018-10-18 01:54:03.720	     0x1193a35c0	INFO 	net.p2p	src/p2p/net_node.inl:1968	Set limit-down to 8192 kB/s
2018-10-18 01:54:03.720	  0x70000118b000	INFO 	net.dns	src/common/dns_utils.cpp:252	adding trust anchor: . IN DS 19036 8 2 49AAC11D7B6F6446702E54A1607371607A1A41855200FD2CE1CDDE32F24E8FB5

2018-10-18 01:54:03.720	  0x70000118b000	INFO 	net.dns	src/common/dns_utils.cpp:252	adding trust anchor: . IN DS 20326 8 2 E06D44B80B8F1D39A95C0B0D7C65D08458E880409BBC683457104237C7F8EC8D

2018-10-18 01:54:03.747	  0x70000118b000	INFO 	net.p2p	src/p2p/net_node.inl:481	dns_threads[0] addr_str: seeds.moneroseeds.se  number of results: 0
2018-10-18 01:54:03.748	  0x70000120e000	INFO 	net.p2p	src/p2p/net_node.inl:481	dns_threads[1] addr_str: seeds.moneroseeds.ae.org  number of results: 0
2018-10-18 01:54:03.748	  0x700001291000	INFO 	net.p2p	src/p2p/net_node.inl:481	dns_threads[2] addr_str: seeds.moneroseeds.ch  number of results: 0
2018-10-18 01:54:03.749	  0x700001314000	INFO 	net.p2p	src/p2p/net_node.inl:481	dns_threads[3] addr_str: seeds.moneroseeds.li  number of results: 0
2018-10-18 01:54:03.749	     0x1193a35c0	INFO 	net.p2p	src/p2p/net_node.inl:519	DNS seed node lookup either timed out or failed, falling back to defaults
2018-10-18 01:54:03.749	     0x1193a35c0	INFO 	net.p2p	src/p2p/net_node.inl:360	Resolving node address: host=107.152.130.98, port=18080
2018-10-18 01:54:03.757	     0x1193a35c0	INFO 	net.p2p	src/p2p/net_node.inl:377	Added node: 107.152.130.98:18080
2018-10-18 01:54:03.757	     0x1193a35c0	INFO 	net.p2p	src/p2p/net_node.inl:360	Resolving node address: host=161.67.132.39, port=18080
2018-10-18 01:54:03.757	     0x1193a35c0	INFO 	net.p2p	src/p2p/net_node.inl:377	Added node: 161.67.132.39:18080
2018-10-18 01:54:03.757	     0x1193a35c0	INFO 	net.p2p	src/p2p/net_node.inl:360	Resolving node address: host=163.172.182.165, port=18080
2018-10-18 01:54:03.757	     0x1193a35c0	INFO 	net.p2p	src/p2p/net_node.inl:377	Added node: 163.172.182.165:18080
2018-10-18 01:54:03.757	     0x1193a35c0	INFO 	net.p2p	src/p2p/net_node.inl:360	Resolving node address: host=195.154.123.123, port=18080
2018-10-18 01:54:03.757	     0x1193a35c0	INFO 	net.p2p	src/p2p/net_node.inl:377	Added node: 195.154.123.123:18080
2018-10-18 01:54:03.757	     0x1193a35c0	INFO 	net.p2p	src/p2p/net_node.inl:360	Resolving node address: host=198.74.231.92, port=18080
2018-10-18 01:54:03.757	     0x1193a35c0	INFO 	net.p2p	src/p2p/net_node.inl:377	Added node: 198.74.231.92:18080
2018-10-18 01:54:03.757	     0x1193a35c0	INFO 	net.p2p	src/p2p/net_node.inl:360	Resolving node address: host=212.83.172.165, port=18080
2018-10-18 01:54:03.757	     0x1193a35c0	INFO 	net.p2p	src/p2p/net_node.inl:377	Added node: 212.83.172.165:18080
2018-10-18 01:54:03.757	     0x1193a35c0	INFO 	net.p2p	src/p2p/net_node.inl:360	Resolving node address: host=212.83.175.67, port=18080
2018-10-18 01:54:03.757	     0x1193a35c0	INFO 	net.p2p	src/p2p/net_node.inl:377	Added node: 212.83.175.67:18080
2018-10-18 01:54:03.757	     0x1193a35c0	INFO 	net.p2p	src/p2p/net_node.inl:360	Resolving node address: host=5.9.100.248, port=18080
2018-10-18 01:54:03.757	     0x1193a35c0	INFO 	net.p2p	src/p2p/net_node.inl:377	Added node: 5.9.100.248:18080
2018-10-18 01:54:03.762	     0x1193a35c0	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:917	Set server type to: 2 from name: P2P, prefix_name = P2P
2018-10-18 01:54:03.762	     0x1193a35c0	INFO 	net.p2p	src/p2p/net_node.inl:571	Binding on 0.0.0.0:18080
2018-10-18 01:54:03.763	     0x1193a35c0	FATAL	net	contrib/epee/include/net/abstract_tcp_server2.inl:856	Error starting server: bind: Address already in use
2018-10-18 01:54:03.763	     0x1193a35c0	ERROR	net.p2p	src/p2p/net_node.inl:573	Failed to bind server
2018-10-18 01:54:03.764	     0x1193a35c0	INFO 	global	src/daemon/core.h:103	Deinitializing core...
2018-10-18 01:54:03.764	     0x1193a35c0	ERROR	daemon	src/daemon/core.h:108	Failed to deinitialize core...
2018-10-18 01:54:03.764	     0x1193a35c0	INFO 	global	src/daemon/protocol.h:75	Stopping cryptonote protocol...
2018-10-18 01:54:03.764	     0x1193a35c0	INFO 	global	src/daemon/protocol.h:79	Cryptonote protocol stopped successfully
2018-10-18 01:54:03.764	     0x1193a35c0	ERROR	daemon	src/daemon/main.cpp:295	Exception in main! Failed to initialize p2p server.

```

Not quite sure what to do here. I do see an weird entry about `2018-10-18 01:43:41.651      0x10d7c55c0        INFO    global  src/blockchain_d
b/lmdb/db_lmdb.cpp:4071 ESC[1;33mMigrating blockchain from DB version 1 to 2 - t
his may take a while:ESC[0m` but I have no idea how to check the status of the db migration. Any pointers?

Thanks!


# Discussion History
## wililupy | 2018-10-18T02:35:29+00:00
Looks like the database needs to update. I restarted my mac and then ran monerod and I can see the update status. Its about 50% complete as of now. Once this completes, I'll update this issue.

## moneromooo-monero | 2018-10-18T08:37:30+00:00
You have a process using the port monerod is trying to use. Most likely another monerod.
And what wililupy said about the db update. You probably ran a monerod earlier that's still running and upgrading the db while you try to run another one.

## wililupy | 2018-10-18T18:20:06+00:00
So I ended up deleting the lmdb directory and had Monero-GUI re-sync and now everything is working properly.

# Action History
- Created by: wililupy | 2018-10-18T02:02:39+00:00
- Closed at: 2018-10-18T18:20:06+00:00
