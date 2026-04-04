---
title: Problem syncing GUI 0.18.1.0
source_url: https://github.com/monero-project/monero/issues/8500
author: xmrca
assignees: []
labels: []
created_at: '2022-08-14T15:05:27+00:00'
updated_at: '2022-08-17T01:08:41+00:00'
type: issue
status: closed
closed_at: '2022-08-17T01:08:41+00:00'
---

# Original Description
Since upgrading to 0.18.1.0 I have a problem syncing. Running own node on Mac OS, firewall turned off like usually.

Any idea what might be happening and how I could get the wallet to sync again? 

14/08/2022 17:00] 2022-08-14 15:00:30.950 I Monero 'Fluorine Fermi' (v0.18.1.0-release)
Error: Couldn't connect to daemon: 127.0.0.1:18081
[14/08/2022 17:00] 2022-08-14 15:00:46.726 I Monero 'Fluorine Fermi' (v0.18.1.0-release)
Height: 2670925, target: 2689454 (99.311%)
Downloading at 57 kB/s
Next needed pruning seed: 5
4 peers
Remote Host Peer_ID State Prune_Seed Height DL kB/s, Queued Blocks / MB
162.218.65.54:59017 0000000000000000 before_handshake 0 0 0 kB/s, 0 blocks / 0 MB queued
176.223.130.246:18080 2e9f9a3dcf0296fe synchronizing 0 2689454 45 kB/s, 20 blocks / 0 MB queued
202.155.239.82:18080 023513740623125c synchronizing 0 2689454 11 kB/s, 0 blocks / 0 MB queued
75.108.79.254:18080 0000000000000000 before_handshake 0 0 1 kB/s, 0 blocks / 0 MB queued
1 spans, 0 MB
[.]
176.223.130.246:18080 20/184 (2670925 - 2670944) -

# Discussion History
## xmrca | 2022-08-14T15:31:23+00:00
Seems to sync now but very slowly...


2022-08-14 15:05:59.343	     0x107a83600	INFO	global	src/daemon/main.cpp:296	Monero 'Fluorine Fermi' (v0.18.1.0-release)
2022-08-14 15:05:59.344	     0x107a83600	INFO	msgwriter	src/common/scoped_message_writer.h:102	Forking to background...
2022-08-14 15:05:59.347	     0x107a83600	WARNING	daemon	src/daemon/executor.cpp:61	Monero 'Fluorine Fermi' (v0.18.1.0-release) Daemonised
2022-08-14 15:05:59.347	     0x107a83600	INFO	global	src/daemon/protocol.h:53	Initializing cryptonote protocol...
2022-08-14 15:05:59.347	     0x107a83600	INFO	global	src/daemon/protocol.h:58	Cryptonote protocol initialized OK
2022-08-14 15:05:59.348	     0x107a83600	INFO	global	src/daemon/core.h:64	Initializing core...
2022-08-14 15:05:59.349	     0x107a83600	INFO	global	src/cryptonote_core/cryptonote_core.cpp:519	Loading blockchain from folder /Volumes/T7/lmdb ...
2022-08-14 15:05:59.517	     0x107a83600	INFO	global	src/cryptonote_core/cryptonote_core.cpp:694	Loading checkpoints
2022-08-14 15:05:59.518	     0x107a83600	INFO	global	src/daemon/core.h:81	Core initialized OK
2022-08-14 15:05:59.518	     0x107a83600	INFO	global	src/daemon/p2p.h:64	Initializing p2p server...
2022-08-14 15:05:59.533	     0x107a83600	INFO	global	src/daemon/p2p.h:69	p2p server initialized OK
2022-08-14 15:05:59.533	     0x107a83600	INFO	global	src/daemon/rpc.h:63	Initializing core RPC server...
2022-08-14 15:05:59.534	     0x107a83600	INFO	global	contrib/epee/include/net/http_server_impl_base.h:79	Binding on 127.0.0.1 (IPv4):18081
2022-08-14 15:05:59.558	     0x107a83600	INFO	global	src/daemon/rpc.h:69	core RPC server initialized OK on port: 18081
2022-08-14 15:05:59.562	     0x107a83600	INFO	global	src/daemon/rpc.h:74	Starting core RPC server...
2022-08-14 15:05:59.562	[SRV_MAIN]	INFO	global	src/daemon/rpc.h:79	core RPC server started ok
2022-08-14 15:05:59.562	[SRV_MAIN]	INFO	global	src/daemon/p2p.h:79	Starting p2p net loop...
2022-08-14 15:06:00.564	[P2P6]	INFO	global	src/cryptonote_core/cryptonote_core.cpp:1816	
2022-08-14 15:06:00.564	[P2P6]	INFO	global	src/cryptonote_core/cryptonote_core.cpp:1816	**********************************************************************
2022-08-14 15:06:00.564	[P2P6]	INFO	global	src/cryptonote_core/cryptonote_core.cpp:1816	The daemon will start synchronizing with the network. This may take a long time to complete.
2022-08-14 15:06:00.564	[P2P6]	INFO	global	src/cryptonote_core/cryptonote_core.cpp:1816	
2022-08-14 15:06:00.564	[P2P6]	INFO	global	src/cryptonote_core/cryptonote_core.cpp:1816	You can set the level of process detailization through "set_log <level|categories>" command,
2022-08-14 15:06:00.564	[P2P6]	INFO	global	src/cryptonote_core/cryptonote_core.cpp:1816	where <level> is between 0 (no details) and 4 (very verbose), or custom category based levels (eg, *:WARNING).
2022-08-14 15:06:00.564	[P2P6]	INFO	global	src/cryptonote_core/cryptonote_core.cpp:1816	
2022-08-14 15:06:00.564	[P2P6]	INFO	global	src/cryptonote_core/cryptonote_core.cpp:1816	Use the "help" command to see the list of available commands.
2022-08-14 15:06:00.564	[P2P6]	INFO	global	src/cryptonote_core/cryptonote_core.cpp:1816	Use "help <command>" to see a command's documentation.
2022-08-14 15:06:00.564	[P2P6]	INFO	global	src/cryptonote_core/cryptonote_core.cpp:1816	**********************************************************************
2022-08-14 15:06:00.697	[P2P6]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:409	[176.223.130.246:18080 OUT] Sync data returned a new top block candidate: 2671030 -> 2689457 [Your node is 18427 blocks (25.6 days) behind] 
2022-08-14 15:06:00.697	[P2P6]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:409	SYNCHRONIZATION started
2022-08-14 15:06:02.801	  0x700010b3a000	WARNING	net.dns	src/common/dns_utils.cpp:346	Invalid DNSSEC TXT record signature for updates.moneropulse.org: validation failure <updates.moneropulse.org. TXT IN>: no signatures from 192.168.1.1 for key org. while building chain of trust
2022-08-14 15:06:39.233	[P2P7]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1679	Synced 2671050/2689458 (99%, 18408 left)
2022-08-14 15:07:17.359	[P2P7]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1679	Synced 2671070/2689458 (99%, 18388 left)
2022-08-14 15:08:02.567	[P2P7]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1679	Synced 2671090/2689459 (99%, 18369 left, 0% of total synced, estimated 10.3 hours left)
2022-08-14 15:08:36.616	[P2P7]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1679	Synced 2671110/2689459 (99%, 18349 left)
2022-08-14 15:09:21.986	[P2P7]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1679	Synced 2671130/2689460 (99%, 18330 left)
2022-08-14 15:09:47.950	[P2P7]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1679	Synced 2671150/2689460 (99%, 18310 left)
2022-08-14 15:10:28.581	[P2P7]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1679	Synced 2671170/2689460 (99%, 18290 left, 0% of total synced, estimated 9.7 hours left)
2022-08-14 15:11:13.456	[P2P7]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1679	Synced 2671190/2689460 (99%, 18270 left)
2022-08-14 15:11:35.988	[P2P7]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1679	Synced 2671210/2689460 (99%, 18250 left)
2022-08-14 15:12:07.357	[P2P7]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1679	Synced 2671230/2689460 (99%, 18230 left)
2022-08-14 15:12:47.991	[P2P7]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1679	Synced 2671250/2689460 (99%, 18210 left, 1% of total synced, estimated 9.3 hours left)
2022-08-14 15:13:19.819	[P2P7]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1679	Synced 2671270/2689460 (99%, 18190 left)
2022-08-14 15:13:45.539	[P2P7]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1679	Synced 2671290/2689461 (99%, 18171 left)
2022-08-14 15:14:33.169	[P2P7]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1679	Synced 2671310/2689461 (99%, 18151 left)
2022-08-14 15:15:04.687	[P2P7]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1679	Synced 2671330/2689461 (99%, 18131 left, 1% of total synced, estimated 9.1 hours left)
2022-08-14 15:16:04.276	[P2P7]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1679	Synced 2671350/2689461 (99%, 18111 left)
2022-08-14 15:16:26.238	[P2P7]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1679	Synced 2671370/2689461 (99%, 18091 left)
2022-08-14 15:17:04.600	[P2P7]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1679	Synced 2671390/2689462 (99%, 18072 left)
2022-08-14 15:17:40.116	[P2P7]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1679	Synced 2671410/2689462 (99%, 18052 left, 2% of total synced, estimated 9.2 hours left)
2022-08-14 15:18:32.918	[P2P7]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1679	Synced 2671430/2689462 (99%, 18032 left)
2022-08-14 15:19:03.588	[P2P7]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1679	Synced 2671450/2689462 (99%, 18012 left)
2022-08-14 15:26:23.206	[P2P5]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:409	[87.125.174.88:18080 OUT] Sync data returned a new top block candidate: 2671450 -> 2689466 [Your node is 18016 blocks (25.0 days) behind] 
2022-08-14 15:26:23.207	[P2P5]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:409	SYNCHRONIZATION started
2022-08-14 15:27:48.759	[P2P7]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1679	Synced 2671470/2689467 (99%, 17997 left, 2% of total synced, estimated 14.8 hours left)
2022-08-14 15:28:18.048	[P2P7]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1679	Synced 2671490/2689468 (99%, 17978 left)
2022-08-14 15:29:01.560	[P2P7]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1679	Synced 2671510/2689468 (99%, 17958 left)
2022-08-14 15:29:39.945	[P2P7]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1679	Synced 2671530/2689469 (99%, 17939 left)
2022-08-14 15:30:16.000	[P2P7]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1679	Synced 2671550/2689469 (99%, 17919 left, 2% of total synced, estimated 13.9 hours left)

## selsta | 2022-08-14T15:40:40+00:00
What is the output of "status" and "sync_info" ?

## xmrca | 2022-08-14T15:51:55+00:00
sync_info
[14/08/2022 17:50] 2022-08-14 15:50:05.075 I Monero 'Fluorine Fermi' (v0.18.1.0-release)
Height: 2672250/2689477 (99.4%) on mainnet, not mining, net hash 2.55 GH/s, v14, 3(out)+17(in) connections, uptime 0d 0h 44m 51s



## xmrca | 2022-08-14T15:52:38+00:00
status 

[14/08/2022 17:52] 2022-08-14 15:51:44.281 I Monero 'Fluorine Fermi' (v0.18.1.0-release)
Height: 2672310, target: 2689482 (99.3615%)
Downloading at 296 kB/s
Next needed pruning seed: 6
20 peers
Remote Host Peer_ID State Prune_Seed Height DL kB/s, Queued Blocks / MB
220.244.59.94:18080 0000000000000000 before_handshake 0 0 0 kB/s, 0 blocks / 0 MB queued
209.222.252.243:21965 0000000000000000 before_handshake 0 0 0 kB/s, 0 blocks / 0 MB queued
162.218.65.68:63095 c22cb383ea45c923 normal 0 1 0 kB/s, 0 blocks / 0 MB queued
95.211.243.182:50480 5b842980d7b7e79d synchronizing 184 2689482 38 kB/s, 20 blocks / 0 MB queued
23.88.43.143:56496 0000000000000000 before_handshake 0 0 0 kB/s, 0 blocks / 0 MB queued
40.131.160.202:53378 0000000000000000 before_handshake 0 0 0 kB/s, 0 blocks / 0 MB queued
91.198.115.221:25938 0000000000000000 before_handshake 0 0 0 kB/s, 0 blocks / 0 MB queued
91.198.115.104:56659 0000000000000000 before_handshake 0 0 0 kB/s, 0 blocks / 0 MB queued
209.222.252.47:16128 0000000000000000 before_handshake 0 0 0 kB/s, 0 blocks / 0 MB queued
87.98.224.123:18080 57a831f1910b0e7a normal 0 2517466 1 kB/s, 0 blocks / 0 MB queued
162.218.65.30:29254 ddc7c8ee278539e5 normal 0 1 0 kB/s, 0 blocks / 0 MB queued
51.75.162.171:58457 3610859212d3383c normal 0 2517466 1 kB/s, 0 blocks / 0 MB queued
91.198.115.183:40763 0000000000000000 before_handshake 0 0 0 kB/s, 0 blocks / 0 MB queued
51.68.214.143:45137 12360e212070e6a1 normal 0 2517466 1 kB/s, 0 blocks / 0 MB queued
162.218.65.244:46420 0000000000000000 before_handshake 0 0 0 kB/s, 0 blocks / 0 MB queued
192.99.154.164:51425 354400163384211f normal 0 2517466 1 kB/s, 0 blocks / 0 MB queued
162.218.65.207:14039 0000000000000000 before_handshake 0 0 0 kB/s, 0 blocks / 0 MB queued
91.198.115.30:7873 0000000000000000 before_handshake 0 0 0 kB/s, 0 blocks / 0 MB queued
162.218.65.87:61085 0000000000000000 before_handshake 0 0 0 kB/s, 0 blocks / 0 MB queued
176.223.130.246:18080 2e9f9a3dcf0296fe synchronizing 0 2689457 254 kB/s, 0 blocks / 0 MB queued
63 spans, 94.1749 MB
[moooooooooooooooooooooooooooooooooooooooooooooooo_oooooooooooo.o]
68.73.201.40:18080 20/184 (2672310 - 2672329, 1977 kB) 193 kB/s (0.05)
78.73.3.131:40552 20/184 (2672330 - 2672349, 2362 kB) 591 kB/s (0.13)
121.57.53.125:5280 20/184 (2672350 - 2672369, 1007 kB) 98 kB/s (0.02)
202.155.239.82:18080 20/184 (2672370 - 2672389, 1770 kB) 185 kB/s (0.05)
75.108.79.254:18080 20/184 (2672390 - 2672409, 1438 kB) 163 kB/s (0.04)
128.204.192.155:18080 20/184 (2672410 - 2672429, 1633 kB) 463 kB/s (0.16)
23.112.140.90:18080 20/184 (2672430 - 2672449, 1718 kB) 439 kB/s (0.1)
152.230.90.225:18080 20/184 (2672450 - 2672469, 1506 kB) 88 kB/s (0.03)
87.125.174.88:18080 20/184 (2672470 - 2672489, 1147 kB) 104 kB/s (0.03)
121.57.53.125:5280 20/184 (2672490 - 2672509, 995 kB) 86 kB/s (0.02)
78.73.3.131:40552 20/184 (2672510 - 2672529, 1230 kB) 404 kB/s (0.13)
213.253.113.168:18080 20/184 (2672530 - 2672549, 1433 kB) 205 kB/s (0.05)
68.73.201.40:18080 20/184 (2672550 - 2672569, 710 kB) 129 kB/s (0.05)
152.230.90.225:18080 20/184 (2672570 - 2672589, 1429 kB) 136 kB/s (0.03)
87.125.174.88:18080 20/184 (2672590 - 2672609, 1490 kB) 131 kB/s (0.03)
121.57.53.125:5280 20/184 (2672610 - 2672629, 992 kB) 67 kB/s (0.02)
23.112.140.90:18080 20/184 (2672630 - 2672649, 1198 kB) 256 kB/s (0.1)
75.108.79.254:18080 20/184 (2672650 - 2672669, 1143 kB) 140 kB/s (0.04)
128.204.192.155:18080 20/184 (2672670 - 2672689, 1373 kB) 464 kB/s (0.16)
78.73.3.131:40552 20/184 (2672690 - 2672709, 1556 kB) 511 kB/s (0.13)
23.112.140.90:18080 20/184 (2672710 - 2672729, 1858 kB) 463 kB/s (0.1)
173.176.29.111:51768 20/184 (2672730 - 2672749, 1954 kB) 747 kB/s (0.19)
68.73.201.40:18080 20/184 (2672750 - 2672769, 1814 kB) 215 kB/s (0.05)
87.125.174.88:18080 20/184 (2672770 - 2672789, 1687 kB) 104 kB/s (0.03)
202.155.239.82:18080 20/184 (2672790 - 2672809, 1314 kB) 229 kB/s (0.05)
128.204.192.155:18080 20/184 (2672810 - 2672829, 1454 kB) 811 kB/s (0.16)
75.108.79.254:18080 20/184 (2672830 - 2672849, 1135 kB) 125 kB/s (0.04)
152.230.90.225:18080 20/184 (2672850 - 2672869, 2007 kB) 93 kB/s (0.03)
217.180.209.41:18080 20/184 (2672870 - 2672889, 1330 kB) 539 kB/s (0.17)
68.73.201.40:18080 20/184 (2672890 - 2672909, 2076 kB) 448 kB/s (0.09)
213.253.113.168:18080 20/184 (2672910 - 2672929, 1571 kB) 402 kB/s (0.09)
152.230.90.225:18080 20/184 (2672930 - 2672949, 2168 kB) 154 kB/s (0.03)
202.155.239.82:18080 20/184 (2672950 - 2672969, 1153 kB) 281 kB/s (0.06)
23.112.140.90:18080 20/184 (2672970 - 2672989, 1319 kB) 278 kB/s (0.07)
68.73.201.40:18080 20/184 (2672990 - 2673009, 1745 kB) 226 kB/s (0.09)
217.180.209.41:18080 20/184 (2673010 - 2673029, 1427 kB) 313 kB/s (0.17)
213.253.113.168:18080 20/184 (2673030 - 2673049, 2723 kB) 322 kB/s (0.09)
157.211.233.141:53310 20/184 (2673050 - 2673069, 1977 kB) 211 kB/s (0.05)
128.204.192.155:18080 20/184 (2673070 - 2673089, 2054 kB) 364 kB/s (0.51)
198.54.133.60:54918 20/184 (2673090 - 2673109, 1996 kB) 1051 kB/s (0.15)
152.230.90.225:18080 20/184 (2673110 - 2673129, 2990 kB) 76 kB/s (0.03)
128.204.192.155:18080 20/184 (2673130 - 2673149, 1964 kB) 2261 kB/s (0.51)
176.9.0.187:18080 20/184 (2673150 - 2673169, 1838 kB) 4376 kB/s (1)
198.54.133.60:54918 20/184 (2673170 - 2673189, 1231 kB) 102 kB/s (0.15)
3.217.133.209:52872 20/184 (2673190 - 2673209, 1830 kB) 1391 kB/s (0.35)
157.211.233.141:53310 20/184 (2673210 - 2673229, 1224 kB) 138 kB/s (0.05)
217.180.209.41:18080 20/184 (2673230 - 2673249, 1312 kB) 1003 kB/s (0.17)
75.108.79.254:18080 20/184 (2673250 - 2673269, 1281 kB) 244 kB/s (0.05)
23.112.140.90:18080 20/184 (2673270 - 2673289, 1439 kB) 277 kB/s (0.07)
213.253.113.168:18080 20/184 (2673310 - 2673329, 1217 kB) 1916 kB/s (0.49)
157.211.233.141:53310 20/184 (2673330 - 2673349, 1456 kB) 249 kB/s (0.05)
217.180.209.41:18080 20/184 (2673350 - 2673369, 1508 kB) 633 kB/s (0.17)
3.217.133.209:52872 20/184 (2673370 - 2673389, 1534 kB) 1363 kB/s (0.35)
67.171.255.106:18080 20/184 (2673390 - 2673409, 1125 kB) 219 kB/s (0.06)
128.204.192.155:18080 20/184 (2673410 - 2673429, 1021 kB) 2648 kB/s (0.51)
176.9.0.187:18080 20/184 (2673430 - 2673449, 1161 kB) 3389 kB/s (1)
75.108.79.254:18080 20/184 (2673450 - 2673469, 1059 kB) 121 kB/s (0.05)
152.230.90.225:18080 20/184 (2673470 - 2673489, 1499 kB) 96 kB/s (0.03)
202.155.239.82:18080 20/184 (2673490 - 2673509, 1082 kB) 204 kB/s (0.06)
87.125.174.88:18080 20/184 (2673510 - 2673529, 1432 kB) 107 kB/s (0.03)
152.230.90.225:18080 20/184 (2673530 - 2673549, 735 kB) 123 kB/s (0.03)
95.211.243.182:50480 20/184 (2673550 - 2673569) -
24.144.51.151:18080 20/184 (2673570 - 2673589, 1337 kB) 53 kB/s (0.01)
[14/08/2022 17:52] 2022-08-14 15:50:51.668 I Monero 'Fluorine Fermi' (v0.18.1.0-release)
Height: 2672270/2689479 (99.4%) on mainnet, not mining, net hash 2.57 GH/s, v14, 8(out)+15(in) connections, uptime 0d 0h 46m 2s

## selsta | 2022-08-14T15:54:11+00:00
Seems it is syncing as expected? What kind of OS and hardware do you have and where is the blockchain saved?

## xmrca | 2022-08-14T16:03:06+00:00
Thank you for checking! 

I didn't see any syncing the first 10 minutes and thought something was wrong. Now that it started, it indeed keeps moving forward. It feels slow to me but maybe this is the normal speed for my set-up?

Node runs on a new SSD
OS Montery
3,3 GHz Dual-Core Intel Core i7
16 GB 2133 MHz LPDDR3
Intel Iris Graphics 550 1536 MB



## selsta | 2022-08-14T16:07:48+00:00
How many blocks does it sync in 10 minutes?

## xmrca | 2022-08-14T17:12:28+00:00
440 during the last 10 minutes

## selsta | 2022-08-14T17:41:52+00:00
From what year is your Mac? And is the SSD internal or external?

On a M1 Pro I sync about 3 blocks / second. You seem to sync 0.7 blocks / second. Seems to be on the slower side but not out of the ordinary.

## xmrca | 2022-08-14T19:12:12+00:00
SSD is external. Is that slower compared to internal? 

Mac is from beginning 2017 so 5,5 years old. I guess that could explain the difference between your 3 blocks per second and my 0,7 blocks? 

Guess it will become my way of practising patience while getting a habit of syncing regularly :)

## selsta | 2022-08-14T19:13:40+00:00
Yes, external SSD is slower. That likely explains it.

## xmrca | 2022-08-14T19:25:34+00:00
Thanks for following up!

## selsta | 2022-08-15T00:12:01+00:00
Were you able to sync up? Can this be closed?

## GuardedAirplane | 2022-08-16T03:30:58+00:00
I too have been having relatively slow sync speeds, but I am running in a LXC container on a ProxMox host. I have been bootstrapping over the last two weeks, but just started normal syncing again to see if maybe old transactions sync slower.

Being on ProxMox, I get graphs of CPU, Memory, Network, and IO Delay and nothing seems to be outside of normal operating ranges for the server (I run several other services and haven't noticed any being slow). The blockchain is being stored in a ZFS dataset on a 8xHDD RAID 10 pool with SLOG and L2ARC with recordsize=128KB (rough guess to the average blocksize now, so better info is appreciated). 

Does monerod have any performance metrics related to disk IO? My IO Delay is never above 1-2% according to ProxMox, but with CPU never going above 2% and me having 1Gig fiber I feel like that is the only thing that explains it. I get syncing a blockchain that has been around for years takes time, but I feel like there's some major bottleneck preventing it from going as fast as it should.

## hyc | 2022-08-16T03:37:26+00:00
That just sounds like not getting any fast peers, if overall system utilization is so low.

As an aside, LMDB and ZFS don't really play well together. 4KB pages and 128KB recordsize makes for very inefficient operation, and also ZFS support of mmap doesn't play well with the rest of the OS.

## selsta | 2022-08-16T03:42:24+00:00
@GuardedAirplane can you post the output of `sync_info` ? That should show if it is network related or not.

## GuardedAirplane | 2022-08-16T03:54:40+00:00
Looking at the time estimates, it looks like the initial guess of 7 days is slowly decreasing now (initialy it climbed to 2+ months which is why I decided to use the bootstrap method).

sync_info                                                                                                                                                                                                          
2022-08-16 03:45:12.670 I Synced 2534156/2690557 (94%, 156401 left)                                                                                                                                                
Height: 2534156, target: 2690557 (94.187%)                                                                                                                                                                         
Downloading at 5681 kB/s                                                                                                                                                                                           
Next needed pruning seed: 5                                                                                                                                                                                        
16 peers                                                                                                                                                                                                           
Remote Host                        Peer_ID   State   Prune_Seed          Height  DL kB/s, Queued Blocks / MB                                                                                                       
24.20.205.147:18080       ddbe315d66de0ce3  synchronizing     0         2690557  45 kB/s, 0 blocks / 0 MB queued                                                                                                   
168.119.137.28:18080      d8d5022b041bcbce  standby           0         2690557  36 kB/s, 0 blocks / 0 MB queued                                                                                                   
147.135.131.10:18080      e2a000ab0fb8e6d7  synchronizing     0         2690557  1 kB/s, 20 blocks / 1.74552 MB queued                                                                                             
212.193.55.161:18080      1886959f877d7078  synchronizing     0         2690557  1 kB/s, 0 blocks / 0 MB queued                                                                                                    
199.188.204.85:18080      67a5a55ca665046a  standby           0         2690556  50 kB/s, 80 blocks / 4.56174 MB queued                                                                                            
185.216.178.44:18080      ecbde5fdbcbc60dd  synchronizing     0         2690557  1 kB/s, 120 blocks / 8.096 MB queued                                                                                              
40.131.160.202:18080      31329f242ca0ea15  synchronizing     0         2690557  1 kB/s, 0 blocks / 0 MB queued                                                                                                    
209.222.252.83:15764      ddc7c8ee278539e5  normal            0         1  0 kB/s, 0 blocks / 0 MB queued                                                                                                          
75.180.225.7:18080        0000000000000000  before_handshake  0         0  0 kB/s, 0 blocks / 0 MB queued                                                                                                          
130.185.202.159:18080     93d821c4f58d4db9  synchronizing     0         2690557  1 kB/s, 60 blocks / 3.25439 MB queued                                                                                             
142.181.123.224:18080     de5c3151b7c6d6c6  synchronizing     0         2690557  44 kB/s, 360 blocks / 27.0252 MB queued                                                                                           
217.182.201.228:18080     ee5188b5101eb4c5  standby           0         2690557  1 kB/s, 500 blocks / 34.8066 MB queued                                                                                            
40.131.160.202:55354      0000000000000000  before_handshake  0         0  0 kB/s, 0 blocks / 0 MB queued                                                                                                          
209.97.135.247:34530      0000000000000000  before_handshake  0         0  0 kB/s, 0 blocks / 0 MB queued                                                                                                          
64.121.32.228:18080       f2a5dfaf23526a5f  normal            0         1  0 kB/s, 0 blocks / 0 MB queued                                                                                                          
74.201.73.218:18080       0439e60e6907f395  synchronizing     0         2690534  5500 kB/s, 400 blocks / 31.8726 MB queued                                                                                         
259 spans, 388.899 MB                                                                                                                                                                                              
[mooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
ooooooooooooooooooooooooooooo_ooooooooooooo_.ooo.o.]                                                                                                                                                               
74.201.73.218:18080       20/182 (2534156 - 2534175, 1922 kB)  19810 kB/s (0.81)                                                                                                                                   
168.119.137.28:18080      20/182 (2534176 - 2534195, 1899 kB)  4835 kB/s (0.9)                                                                                                                                     
147.135.131.10:18080      20/182 (2534196 - 2534215, 1777 kB)  7998 kB/s (0.19)                                                                                                                                    
74.201.73.218:18080       20/182 (2534216 - 2534235, 1432 kB)  25040 kB/s (0.81)                                                                                                                                   
207.229.153.229:18080     20/182 (2534236 - 2534255, 1624 kB)  7463 kB/s (0.46)                                                                                                                                    
74.201.73.218:18080       20/182 (2534256 - 2534275, 1949 kB)  27711 kB/s (0.81)                                                                                                                                   
212.193.55.161:18080      20/182 (2534276 - 2534295, 1326 kB)  2023 kB/s (0.11)                                                                                                                                    
74.201.73.218:18080       20/182 (2534296 - 2534315, 2016 kB)  31420 kB/s (0.81)                                                                                                                                   
74.201.73.218:18080       20/182 (2534316 - 2534335, 1605 kB)  24580 kB/s (0.81)                                                                                                                                   
147.135.131.10:18080      20/182 (2534336 - 2534355, 1744 kB)  8420 kB/s (0.19)                                                                                                                                    
207.229.153.229:18080     20/182 (2534356 - 2534375, 1267 kB)  7692 kB/s (0.46)                                                                                                                                    
74.201.73.218:18080       20/182 (2534376 - 2534395, 1934 kB)  20062 kB/s (0.81)                                                                                                                                   
168.119.137.28:18080      20/182 (2534396 - 2534415, 1489 kB)  5884 kB/s (0.9)                                                                                                                                     
74.201.73.218:18080       20/182 (2534416 - 2534435, 1157 kB)  21005 kB/s (0.81)                                                                                                                                   
142.181.123.224:18080     20/182 (2534436 - 2534455, 1573 kB)  2573 kB/s (0.35)                                                                                                                                    
147.135.131.10:18080      20/182 (2534456 - 2534475, 2363 kB)  8503 kB/s (0.19)                                                                                                                                    
74.201.73.218:18080       20/182 (2534476 - 2534495, 1081 kB)  20790 kB/s (0.81)                                                                                                                                   
207.229.153.229:18080     20/182 (2534496 - 2534515, 1504 kB)  7412 kB/s (0.46)                                                                                                                                    
74.201.73.218:18080       20/182 (2534516 - 2534535, 970 kB)  17581 kB/s (0.81)                                                                                                                                    
74.201.73.218:18080       20/182 (2534536 - 2534555, 1260 kB)  18749 kB/s (0.81)                                                                                                                                   
217.182.201.228:18080     20/182 (2534556 - 2534575, 1262 kB)  1274 kB/s (0.23)                                                                                                                                    
168.119.137.28:18080      20/182 (2534576 - 2534595, 1448 kB)  5771 kB/s (0.9)                                                                                                                                     
74.201.73.218:18080       20/182 (2534596 - 2534615, 1340 kB)  24095 kB/s (0.81)                                                                                                                                   
207.229.153.229:18080     20/182 (2534616 - 2534635, 1233 kB)  7548 kB/s (0.46)
74.201.73.218:18080       20/182 (2534636 - 2534655, 1070 kB)  19249 kB/s (0.81)
147.135.131.10:18080      20/182 (2534656 - 2534675, 1233 kB)  524 kB/s (0.19)
212.193.55.161:18080      20/182 (2534676 - 2534695, 1072 kB)  1922 kB/s (0.11)
74.201.73.218:18080       20/182 (2534696 - 2534715, 1389 kB)  22765 kB/s (0.81)
136.55.246.217:18080      20/182 (2534716 - 2534735, 1232 kB)  1260 kB/s (1)
74.201.73.218:18080       20/182 (2534736 - 2534755, 1774 kB)  23974 kB/s (0.81)
207.229.153.229:18080     20/182 (2534756 - 2534775, 1582 kB)  7213 kB/s (0.46)
168.119.137.28:18080      20/182 (2534776 - 2534795, 1810 kB)  7198 kB/s (0.9)
74.201.73.218:18080       20/182 (2534796 - 2534815, 2288 kB)  23685 kB/s (0.81)
74.201.73.218:18080       20/182 (2534816 - 2534835, 2562 kB)  11497 kB/s (0.81)
142.181.123.224:18080     20/182 (2534836 - 2534855, 1611 kB)  2577 kB/s (0.35)
207.229.153.229:18080     20/182 (2534856 - 2534875, 2244 kB)  8918 kB/s (0.46)
178.128.226.166:18080     20/182 (2534876 - 2534895, 1624 kB)  4041 kB/s (0.65)
74.201.73.218:18080       20/182 (2534896 - 2534915, 1166 kB)  5436 kB/s (0.81)
207.229.153.229:18080     20/182 (2534916 - 2534935, 1717 kB)  5102 kB/s (0.46)
212.193.55.161:18080      20/182 (2534936 - 2534955, 1935 kB)  1431 kB/s (0.11)
74.201.73.218:18080       20/182 (2534956 - 2534975, 1946 kB)  13630 kB/s (0.81)
217.182.201.228:18080     20/182 (2534976 - 2534995, 2342 kB)  1062 kB/s (0.23)
142.181.123.224:18080     20/182 (2534996 - 2535015, 1709 kB)  2749 kB/s (0.35)
74.201.73.218:18080       20/182 (2535016 - 2535035, 1777 kB)  2908 kB/s (0.81)
207.229.153.229:18080     20/182 (2535036 - 2535055, 1545 kB)  5100 kB/s (0.46)
136.55.246.217:18080      20/182 (2535056 - 2535075, 1511 kB)  1592 kB/s (1)
207.229.153.229:18080     20/182 (2535076 - 2535095, 1231 kB)  6513 kB/s (0.46)
207.229.153.229:18080     20/182 (2535096 - 2535115, 1658 kB)  4706 kB/s (0.46)
142.181.123.224:18080     20/182 (2535116 - 2535135, 1985 kB)  2622 kB/s (0.35)
74.201.73.218:18080       20/182 (2535136 - 2535155, 1223 kB)  3857 kB/s (0.81)
142.181.123.224:18080     20/182 (2535156 - 2535175, 1120 kB)  1878 kB/s (0.35)
104.63.131.202:18080      20/182 (2535176 - 2535195, 1277 kB)  3446 kB/s (0.16)
207.229.153.229:18080     20/182 (2535196 - 2535215, 1165 kB)  7001 kB/s (0.46)
212.193.55.161:18080      20/182 (2535216 - 2535235, 1169 kB)  1732 kB/s (0.11)
207.229.153.229:18080     20/182 (2535236 - 2535255, 1366 kB)  7783 kB/s (0.46)
136.55.246.217:18080      20/182 (2535256 - 2535275, 1470 kB)  5096 kB/s (1)
104.63.131.202:18080      20/182 (2535276 - 2535295, 1065 kB)  475 kB/s (0.16)
207.229.153.229:18080     20/182 (2535296 - 2535315, 1163 kB)  6780 kB/s (0.46)
142.181.123.224:18080     20/182 (2535316 - 2535335, 685 kB)  2465 kB/s (0.35)
147.135.131.10:18080      20/182 (2535336 - 2535355, 1228 kB)  2766 kB/s (0.19)
207.229.153.229:18080     20/182 (2535356 - 2535375, 847 kB)  6231 kB/s (0.46)
136.55.246.217:18080      20/182 (2535376 - 2535395, 655 kB)  5243 kB/s (1)
136.55.246.217:18080      20/182 (2535396 - 2535415, 1507 kB)  8434 kB/s (1)
207.229.153.229:18080     20/182 (2535416 - 2535435, 1624 kB)  7462 kB/s (0.46)
142.181.123.224:18080     20/183 (2535436 - 2535455, 1449 kB)  2522 kB/s (0.35)
212.193.55.161:18080      20/183 (2535456 - 2535475, 1505 kB)  854 kB/s (0.11)
142.181.123.224:18080     20/183 (2535476 - 2535495, 1200 kB)  1950 kB/s (0.35)
217.182.201.228:18080     20/183 (2535496 - 2535515, 1277 kB)  1441 kB/s (0.23)
212.193.55.161:18080      20/183 (2535516 - 2535535, 1277 kB)  944 kB/s (0.11)
207.229.153.229:18080     20/183 (2535536 - 2535555, 1371 kB)  3897 kB/s (0.46)
147.135.131.10:18080      20/183 (2535556 - 2535575, 1096 kB)  1497 kB/s (0.19)
136.55.246.217:18080      20/183 (2535576 - 2535595, 2034 kB)  6068 kB/s (1)
104.63.131.202:18080      20/183 (2535596 - 2535615, 2679 kB)  699 kB/s (0.16)
142.181.123.224:18080     20/183 (2535616 - 2535635, 1981 kB)  2360 kB/s (0.35)
147.135.131.10:18080      20/183 (2535636 - 2535655, 1650 kB)  2153 kB/s (0.19)
212.193.55.161:18080      20/183 (2535656 - 2535675, 1954 kB)  24 kB/s (0.11)
207.229.153.229:18080     20/183 (2535676 - 2535695, 1612 kB)  4540 kB/s (0.46)
104.63.131.202:18080      20/183 (2535696 - 2535715, 1740 kB)  22 kB/s (0.16)
136.55.246.217:18080      20/183 (2535716 - 2535735, 1846 kB)  8050 kB/s (1)
142.181.123.224:18080     20/183 (2535736 - 2535755, 1519 kB)  2257 kB/s (0.35)
217.182.201.228:18080     20/183 (2535756 - 2535775, 1620 kB)  1784 kB/s (0.23)
217.182.201.228:18080     20/183 (2535776 - 2535795, 1435 kB)  1584 kB/s (0.23)
147.135.131.10:18080      20/183 (2535796 - 2535815, 1855 kB)  2205 kB/s (0.19)
142.181.123.224:18080     20/183 (2535816 - 2535835, 1273 kB)  2137 kB/s (0.35)
217.182.201.228:18080     20/183 (2535836 - 2535855, 1661 kB)  1852 kB/s (0.23)
168.119.137.28:18080      20/183 (2535856 - 2535875, 1898 kB)  1870 kB/s (0.26)
207.229.153.229:18080     20/183 (2535876 - 2535895, 1592 kB)  4117 kB/s (0.46)
104.63.131.202:18080      20/183 (2535896 - 2535915, 1375 kB)  1637 kB/s (0.16)
178.128.226.166:18080     20/183 (2535916 - 2535935, 2502 kB)  5186 kB/s (0.65)
130.185.202.159:18080     20/183 (2535936 - 2535955, 1839 kB)  1417 kB/s (0.2)
207.229.153.229:18080     20/183 (2535956 - 2535975, 759 kB)  2459 kB/s (0.46)
212.193.55.161:18080      20/183 (2535976 - 2535995, 1321 kB)  700 kB/s (0.11)
142.181.123.224:18080     20/183 (2535996 - 2536015, 1142 kB)  1912 kB/s (0.35)
207.229.153.229:18080     20/183 (2536016 - 2536035, 1413 kB)  4110 kB/s (0.46)
147.135.131.10:18080      20/183 (2536036 - 2536055, 1282 kB)  1734 kB/s (0.19)
217.182.201.228:18080     20/183 (2536056 - 2536075, 1095 kB)  1251 kB/s (0.23)
207.229.153.229:18080     20/183 (2536076 - 2536095, 1303 kB)  3847 kB/s (0.46)
188.24.86.160:18080       20/183 (2536096 - 2536115, 1072 kB)  687 kB/s (0.11)
188.24.86.160:18080       20/183 (2536116 - 2536135, 1244 kB)  889 kB/s (0.11)
130.185.202.159:18080     20/183 (2536136 - 2536155, 1196 kB)  1093 kB/s (0.2)
207.229.153.229:18080     20/183 (2536156 - 2536175, 1445 kB)  4401 kB/s (0.46)
142.181.123.224:18080     20/183 (2536176 - 2536195, 1975 kB)  2229 kB/s (0.35)
207.229.153.229:18080     20/183 (2536196 - 2536215, 1358 kB)  3956 kB/s (0.46)
147.135.131.10:18080      20/183 (2536216 - 2536235, 1465 kB)  1941 kB/s (0.19)
212.193.55.161:18080      20/183 (2536236 - 2536255, 1680 kB)  1068 kB/s (0.11)
147.135.131.10:18080      20/183 (2536256 - 2536275, 2326 kB)  2682 kB/s (0.19)
130.185.202.159:18080     20/183 (2536276 - 2536295, 2453 kB)  1613 kB/s (0.2)
188.24.86.160:18080       20/183 (2536296 - 2536315, 1995 kB)  793 kB/s (0.11)
212.193.55.161:18080      20/183 (2536316 - 2536335, 1310 kB)  763 kB/s (0.11)
142.181.123.224:18080     20/183 (2536336 - 2536355, 1317 kB)  2031 kB/s (0.35)
142.181.123.224:18080     20/183 (2536356 - 2536375, 1789 kB)  2257 kB/s (0.35)
178.128.226.166:18080     20/183 (2536376 - 2536395, 1456 kB)  593 kB/s (0.1)
207.229.153.229:18080     20/183 (2536396 - 2536415, 1805 kB)  4565 kB/s (0.46)
136.55.246.217:18080      20/183 (2536416 - 2536435, 1519 kB)  8441 kB/s (0.97)
147.135.131.10:18080      20/183 (2536436 - 2536455, 2009 kB)  2534 kB/s (0.19)
142.181.123.224:18080     20/183 (2536456 - 2536475, 1821 kB)  2345 kB/s (0.35)
147.135.131.10:18080      20/183 (2536476 - 2536495, 1835 kB)  2383 kB/s (0.19)
104.63.131.202:18080      20/183 (2536496 - 2536515, 2438 kB)  161 kB/s (0.06)
147.135.131.10:18080      20/183 (2536516 - 2536535, 2089 kB)  2403 kB/s (0.19)
104.63.131.202:18080      20/183 (2536536 - 2536555, 1343 kB)  464 kB/s (0.06)
168.119.137.28:18080      20/183 (2536556 - 2536575, 1718 kB)  692 kB/s (0.1)
147.135.131.10:18080      20/183 (2536576 - 2536595, 2175 kB)  2463 kB/s (0.19)
130.185.202.159:18080     20/183 (2536596 - 2536615, 1785 kB)  1537 kB/s (0.22)
178.128.226.166:18080     20/183 (2536616 - 2536635, 1500 kB)  1188 kB/s (0.1)
136.55.246.217:18080      20/183 (2536636 - 2536655, 1738 kB)  6220 kB/s (0.97)
142.181.123.224:18080     20/183 (2536656 - 2536675, 2329 kB)  2553 kB/s (0.35)
104.63.131.202:18080      20/183 (2536676 - 2536695, 1247 kB)  542 kB/s (0.06)
207.229.153.229:18080     20/183 (2536696 - 2536715, 1504 kB)  3874 kB/s (0.46)
136.55.246.217:18080      20/183 (2536716 - 2536735, 1784 kB)  798 kB/s (0.97)
207.229.153.229:18080     20/183 (2536736 - 2536755, 1521 kB)  3067 kB/s (0.46)
142.181.123.224:18080     20/183 (2536756 - 2536775, 1505 kB)  345 kB/s (0.35)
147.135.131.10:18080      20/183 (2536776 - 2536795, 1129 kB)  687 kB/s (0.19)
185.216.178.44:18080      20/183 (2536796 - 2536815, 1224 kB)  1194 kB/s (0.16)
178.128.226.166:18080     20/183 (2536816 - 2536835, 873 kB)  510 kB/s (0.1)
147.135.131.10:18080      20/183 (2536836 - 2536855, 1513 kB)  1878 kB/s (0.19)
217.182.201.228:18080     20/183 (2536856 - 2536875, 1637 kB)  1821 kB/s (0.23)
136.55.246.217:18080      20/183 (2536876 - 2536895, 1792 kB)  5419 kB/s (0.97)
207.229.153.229:18080     20/183 (2536896 - 2536915, 1656 kB)  3430 kB/s (0.46)
142.181.123.224:18080     20/183 (2536916 - 2536935, 1883 kB)  2573 kB/s (0.35)
142.181.123.224:18080     20/183 (2536936 - 2536955, 2660 kB)  3080 kB/s (0.35)
136.55.246.217:18080      20/183 (2536956 - 2536975, 4303 kB)  9532 kB/s (0.97)
207.229.153.229:18080     20/183 (2536976 - 2536995, 1686 kB)  3459 kB/s (0.46)
136.55.246.217:18080      20/183 (2536996 - 2537015, 2698 kB)  9686 kB/s (0.97)
207.229.153.229:18080     20/183 (2537016 - 2537035, 1730 kB)  3687 kB/s (0.46)
147.135.131.10:18080      20/183 (2537036 - 2537055, 1633 kB)  2035 kB/s (0.19)
217.182.201.228:18080     20/183 (2537056 - 2537075, 1160 kB)  1140 kB/s (0.23)
185.216.178.44:18080      20/183 (2537076 - 2537095, 1690 kB)  1467 kB/s (0.16)
207.229.153.229:18080     20/183 (2537096 - 2537115, 986 kB)  3235 kB/s (0.46)
136.55.246.217:18080      20/183 (2537116 - 2537135, 1679 kB)  5424 kB/s (0.97)
185.216.178.44:18080      20/183 (2537136 - 2537155, 1522 kB)  1301 kB/s (0.16)
217.182.201.228:18080     20/183 (2537156 - 2537175, 1838 kB)  1817 kB/s (0.23)
217.182.201.228:18080     20/183 (2537176 - 2537195, 1495 kB)  1592 kB/s (0.23)
147.135.131.10:18080      20/183 (2537196 - 2537215, 1909 kB)  1902 kB/s (0.19)
185.216.178.44:18080      20/183 (2537216 - 2537235, 960 kB)  939 kB/s (0.16)
168.119.137.28:18080      20/183 (2537236 - 2537255, 1071 kB)  1393 kB/s (0.19)
130.185.202.159:18080     20/183 (2537256 - 2537275, 1063 kB)  976 kB/s (0.14)
136.55.246.217:18080      20/183 (2537276 - 2537295, 1539 kB)  7914 kB/s (0.34)
142.181.123.224:18080     20/183 (2537296 - 2537315, 1444 kB)  2073 kB/s (0.3)
142.181.123.224:18080     20/183 (2537316 - 2537335, 1390 kB)  2003 kB/s (0.3)
207.229.153.229:18080     20/183 (2537336 - 2537355, 1069 kB)  3091 kB/s (0.46)
147.135.131.10:18080      20/183 (2537356 - 2537375, 1318 kB)  1765 kB/s (0.19)
147.135.131.10:18080      20/183 (2537376 - 2537395, 749 kB)  1175 kB/s (0.19)
142.181.123.224:18080     20/183 (2537396 - 2537415, 1064 kB)  1803 kB/s (0.3)
207.229.153.229:18080     20/183 (2537416 - 2537435, 1296 kB)  3591 kB/s (0.46)
199.188.204.85:18080      20/183 (2537436 - 2537455, 1483 kB)  405 kB/s (0.03)
199.188.204.85:18080      20/183 (2537456 - 2537475, 1037 kB)  1145 kB/s (0.03)
147.135.131.10:18080      20/183 (2537476 - 2537495, 675 kB)  1046 kB/s (0.19)
168.119.137.28:18080      20/183 (2537496 - 2537515, 1150 kB)  1359 kB/s (0.19)
217.182.201.228:18080     20/183 (2537516 - 2537535, 1066 kB)  1212 kB/s (0.23)
142.181.123.224:18080     20/183 (2537536 - 2537555, 1027 kB)  1752 kB/s (0.3)
136.55.246.217:18080      20/183 (2537556 - 2537575, 1152 kB)  8936 kB/s (0.34)
207.229.153.229:18080     20/183 (2537576 - 2537595, 1032 kB)  2613 kB/s (0.46)
199.188.204.85:18080      20/183 (2537596 - 2537615, 1044 kB)  975 kB/s (0.03)
159.100.254.56:18080      20/183 (2537616 - 2537635, 987 kB)  1251 kB/s (0.25)
142.181.123.224:18080     20/183 (2537636 - 2537655, 1140 kB)  1731 kB/s (0.3)
136.55.246.217:18080      20/183 (2537656 - 2537675, 1432 kB)  10600 kB/s (0.34)
147.135.131.10:18080      20/183 (2537676 - 2537695, 1381 kB)  1737 kB/s (0.19)
199.188.204.85:18080      20/183 (2537696 - 2537715, 1530 kB)  396 kB/s (0.03)
147.135.131.10:18080      20/183 (2537716 - 2537735, 1260 kB)  1468 kB/s (0.19)
207.229.153.229:18080     20/183 (2537736 - 2537755, 1595 kB)  2989 kB/s (0.46)
136.55.246.217:18080      20/183 (2537756 - 2537775, 1532 kB)  5051 kB/s (0.34)
142.181.123.224:18080     20/183 (2537776 - 2537795, 2007 kB)  1766 kB/s (0.3)
136.55.246.217:18080      20/183 (2537796 - 2537815, 2184 kB)  6603 kB/s (0.34)
207.229.153.229:18080     20/183 (2537816 - 2537835, 2302 kB)  4360 kB/s (0.46)
142.181.123.224:18080     20/183 (2537836 - 2537855, 1279 kB)  1900 kB/s (0.3)
199.188.204.85:18080      20/183 (2537856 - 2537875, 1316 kB)  1165 kB/s (0.03)
147.135.131.10:18080      20/183 (2537876 - 2537895, 1667 kB)  2067 kB/s (0.19)
159.100.254.56:18080      20/183 (2537896 - 2537915, 1552 kB)  1578 kB/s (0.25)
199.188.204.85:18080      20/183 (2537916 - 2537935, 1728 kB)  33 kB/s (0.03)
159.100.254.56:18080      20/183 (2537936 - 2537955, 1631 kB)  1755 kB/s (0.25)
217.182.201.228:18080     20/183 (2537956 - 2537975, 1124 kB)  1250 kB/s (0.23)
217.182.201.228:18080     20/183 (2537976 - 2537995, 1213 kB)  1364 kB/s (0.23)
136.55.246.217:18080      20/183 (2537996 - 2538015, 933 kB)  5642 kB/s (0.34)
207.229.153.229:18080     20/183 (2538016 - 2538035, 1396 kB)  3616 kB/s (0.46)
142.181.123.224:18080     20/183 (2538036 - 2538055, 1175 kB)  2053 kB/s (0.3)
159.100.254.56:18080      20/183 (2538056 - 2538075, 1212 kB)  1433 kB/s (0.25)
159.100.254.56:18080      20/183 (2538076 - 2538095, 845 kB)  1103 kB/s (0.25)
199.188.204.85:18080      20/183 (2538096 - 2538115, 1274 kB)  24 kB/s (0.03)
142.181.123.224:18080     20/183 (2538116 - 2538135, 1011 kB)  1813 kB/s (0.3)
207.229.153.229:18080     20/183 (2538136 - 2538155, 1606 kB)  4321 kB/s (0.46)
136.55.246.217:18080      20/183 (2538156 - 2538175, 1674 kB)  8276 kB/s (0.34)
217.182.201.228:18080     20/183 (2538176 - 2538195, 862 kB)  1151 kB/s (0.23)
147.135.131.10:18080      20/183 (2538196 - 2538215, 836 kB)  1332 kB/s (0.19)
147.135.131.10:18080      20/183 (2538216 - 2538235, 1246 kB)  1696 kB/s (0.19)
136.55.246.217:18080      20/183 (2538236 - 2538255, 995 kB)  5112 kB/s (0.34)
159.100.254.56:18080      20/183 (2538256 - 2538275, 1008 kB)  1132 kB/s (0.25)
207.229.153.229:18080     20/183 (2538276 - 2538295, 1025 kB)  3153 kB/s (0.46)
217.182.201.228:18080     20/183 (2538296 - 2538315, 1375 kB)  920 kB/s (0.23)
142.181.123.224:18080     20/183 (2538316 - 2538335, 851 kB)  1780 kB/s (0.3)
142.181.123.224:18080     20/183 (2538336 - 2538355, 1149 kB)  1046 kB/s (0.3)
159.100.254.56:18080      20/183 (2538356 - 2538375, 1446 kB)  1447 kB/s (0.25)
168.119.137.28:18080      20/183 (2538376 - 2538395, 989 kB)  1121 kB/s (0.19)
217.182.201.228:18080     20/183 (2538396 - 2538415, 1485 kB)  1497 kB/s (0.23)
207.229.153.229:18080     20/183 (2538416 - 2538435, 1154 kB)  631 kB/s (0.46)
136.55.246.217:18080      20/183 (2538436 - 2538455, 1257 kB)  2544 kB/s (0.34)
147.135.131.10:18080      20/183 (2538456 - 2538475, 1779 kB)  2140 kB/s (0.19)
147.135.131.10:18080      20/183 (2538476 - 2538495, 1648 kB)  800 kB/s (0.19)
159.100.254.56:18080      20/183 (2538496 - 2538515, 1784 kB)  1739 kB/s (0.25)
217.182.201.228:18080     20/183 (2538516 - 2538535, 1299 kB)  1264 kB/s (0.23)
136.55.246.217:18080      20/183 (2538536 - 2538555, 1159 kB)  10007 kB/s (0.34)
142.181.123.224:18080     20/183 (2538556 - 2538575, 1363 kB)  2036 kB/s (0.3)
207.229.153.229:18080     20/183 (2538576 - 2538595, 1506 kB)  4077 kB/s (0.46)
159.100.254.56:18080      20/183 (2538596 - 2538615, 2030 kB)  2095 kB/s (0.25)
207.229.153.229:18080     20/183 (2538616 - 2538635, 1822 kB)  3096 kB/s (0.46)
142.181.123.224:18080     20/183 (2538636 - 2538655, 1671 kB)  1980 kB/s (0.3)
185.216.178.44:18080      20/183 (2538656 - 2538675, 1514 kB)  1200 kB/s (0.2)
217.182.201.228:18080     20/183 (2538676 - 2538695, 1303 kB)  1455 kB/s (0.23)
136.55.246.217:18080      20/183 (2538696 - 2538715, 1101 kB)  6272 kB/s (0.34)
207.229.153.229:18080     20/183 (2538716 - 2538735, 1814 kB)  3156 kB/s (0.46)
136.55.246.217:18080      20/183 (2538736 - 2538755, 1006 kB)  819 kB/s (0.34)
217.182.201.228:18080     20/183 (2538756 - 2538775, 1291 kB)  1367 kB/s (0.23)
142.181.123.224:18080     20/183 (2538776 - 2538795, 1808 kB)  2158 kB/s (0.3)
207.229.153.229:18080     20/183 (2538796 - 2538815, 2268 kB)  3770 kB/s (0.46)
168.119.137.28:18080      20/183 (2538816 - 2538835, 1355 kB)  1489 kB/s (0.19)
142.181.123.224:18080     20/183 (2538836 - 2538855, 1292 kB)  1824 kB/s (0.3)
130.185.202.159:18080     20/183 (2538856 - 2538875, 1425 kB)  979 kB/s (0.15)
217.182.201.228:18080     20/183 (2538876 - 2538895, 1019 kB)  1079 kB/s (0.23)
136.55.246.217:18080      20/183 (2538896 - 2538915, 1236 kB)  1140 kB/s (0.34)
199.188.204.85:18080      20/183 (2538916 - 2538935, 1129 kB)  1178 kB/s (0.13)
142.181.123.224:18080     20/183 (2538956 - 2538975, 4603 kB)  4025 kB/s (0.3)
185.216.178.44:18080      20/183 (2538976 - 2538995, 1058 kB)  1001 kB/s (0.2)
207.229.153.229:18080     20/183 (2538996 - 2539015, 1936 kB)  4830 kB/s (0.46)
217.182.201.228:18080     20/183 (2539016 - 2539035, 1305 kB)  1394 kB/s (0.23)
199.188.204.85:18080      20/183 (2539036 - 2539055, 977 kB)  1098 kB/s (0.13)
199.188.204.85:18080      20/183 (2539236 - 2539255)  -
185.216.178.44:18080      20/183 (2539256 - 2539275, 2287 kB)  1528 kB/s (0.2)
130.185.202.159:18080     20/183 (2539276 - 2539295, 1828 kB)  1188 kB/s (0.15)
217.182.201.228:18080     20/183 (2539296 - 2539315, 1618 kB)  1774 kB/s (0.23)
185.216.178.44:18080      20/183 (2539316 - 2539335)  -
147.135.131.10:18080      20/183 (2539336 - 2539355, 1745 kB)  2185 kB/s (0.31)
130.185.202.159:18080     20/183 (2539356 - 2539375)  -


## selsta | 2022-08-16T03:56:22+00:00
Network wise there are no issues. Do you have a non default `--db-sync-mode` set?

## GuardedAirplane | 2022-08-16T03:58:12+00:00
Just converted it to --db-sync-mode=veryfast:async after reading safe is really only for Windows users. I didn't notice that much of an improvement on the bootstrapping side with that setting though.

## selsta | 2022-08-16T03:59:29+00:00
veryfast does not exist, I would recommend to keep it at the default setting. What do you mean with "bootstrapping side" exactly?

## GuardedAirplane | 2022-08-16T04:05:07+00:00
Lol, just checked the help output and looks like my brain converted fastest to veryfast. 

Oh monero-blockchain-import and using the raw export from getmonero.com (I understand the security implications, but wanted to have a node now and move to "pure sync" node later).

## selsta | 2022-08-16T18:19:57+00:00
You can use ./monerod with `--bootstrap-daemon-address node:port`, which means the daemon syncs in the background while you can still transact by using a remote node for bootstrapping.

## GuardedAirplane | 2022-08-17T00:58:33+00:00
Looks like @hyc 's suggestion was correct. I changed the record size to 4k (deleted the old 128k version) and now it is syncing VERY fast!

## selsta | 2022-08-17T01:08:41+00:00
Closing as there is no clear bug here.

# Action History
- Created by: xmrca | 2022-08-14T15:05:27+00:00
- Closed at: 2022-08-17T01:08:41+00:00
