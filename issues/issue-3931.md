---
title: PANIC! failed to add (again) block while chain switching during the rollback!
source_url: https://github.com/monero-project/monero/issues/3931
author: stoffu
assignees: []
labels: []
created_at: '2018-06-05T08:08:44+00:00'
updated_at: '2025-12-19T16:54:28+00:00'
type: issue
status: closed
closed_at: '2025-12-19T16:54:28+00:00'
---

# Original Description
When I was testing syncing from scratch using v0.12.2.0 built myself on OSX, I encountered following errors:
```
2018-06-05 03:23:04.095	[P2P0]	ERROR	blockchain	src/cryptonote_core/blockchain.cpp:939	Failed to switch to alternative blockchain
2018-06-05 03:23:04.138	[P2P0]	ERROR	blockchain	src/cryptonote_core/blockchain.cpp:883	PANIC! failed to add (again) block while chain switching during the rollback!
2018-06-05 03:23:04.138	[P2P0]	ERROR	blockchain	src/cryptonote_core/blockchain.cpp:950	The block was inserted as invalid while connecting new alternative chain, block_id: <7109e6c518717d56f4ea9eb58812f03b98363dbcf78cd8a613df74523d854886>
```
There also appear the following error occasionally:
```
2018-06-05 03:54:02.230	[P2P5]	ERROR	blockchain	src/cryptonote_core/blockchain.cpp:3936	usable is negative
```

Here's a bit more logs where I switched the log level from `0` to `0,blockchain:DEBUG`:

```
2018-06-05 03:22:39.533	[P2P4]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[45.76.110.150:18080 OUT]  Synced 1581672/1588050
2018-06-05 03:22:41.310	[P2P9]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[45.76.110.150:18080 OUT]  Synced 1581692/1588050
2018-06-05 03:22:41.915	[P2P0]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[45.76.110.150:18080 OUT]  Synced 1581712/1588050
2018-06-05 03:22:42.297	[P2P8]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[45.76.110.150:18080 OUT]  Synced 1581732/1588050
2018-06-05 03:22:42.850	[P2P3]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[45.76.110.150:18080 OUT]  Synced 1581752/1588050
2018-06-05 03:22:44.423	[P2P9]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[45.76.110.150:18080 OUT]  Synced 1581772/1588050
2018-06-05 03:22:47.866	[P2P4]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[37.10.71.87:18080 OUT]  Synced 1581792/1588050
2018-06-05 03:22:47.957	[P2P4]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[37.10.71.87:18080 OUT]  Synced 1581812/1588050
2018-06-05 03:22:48.008	[P2P4]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[37.10.71.87:18080 OUT]  Synced 1581824/1588050
2018-06-05 03:22:50.127	[P2P6]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[45.76.110.150:18080 OUT]  Synced 1581844/1588050
2018-06-05 03:23:03.841	[P2P0]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[37.10.71.87:18080 OUT]  Synced 1581864/1588050
2018-06-05 03:23:03.989	[P2P0]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[37.10.71.87:18080 OUT]  Synced 1581884/1588050
2018-06-05 03:23:04.012	[P2P0]	INFO 	global	src/cryptonote_core/blockchain.cpp:1534	----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 1581881
id:	<7109e6c518717d56f4ea9eb58812f03b98363dbcf78cd8a613df74523d854886>
PoW:	<d3c693d2083888c03bc8dfbca4f32d9692e094722d8cbf4a90aa4c1400000000>
difficulty:	50454937567
2018-06-05 03:23:04.038	[P2P0]	INFO 	global	src/cryptonote_core/blockchain.cpp:1534	----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 1581882
id:	<fade9c6c28337e945198e747d391f9e57d725e1def6d9c7cf99edfb7e32865ac>
PoW:	<c1ca2169cf89d7d4dc76fc7b86c1dc012c4567ff5eb0651ee8736a0b00000000>
difficulty:	50327383695
2018-06-05 03:23:04.065	[P2P0]	INFO 	global	src/cryptonote_core/blockchain.cpp:1534	----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 1581883
id:	<21bd3e12be99b5155193797996a77c96de2fe55bafdb60abcb6a6957abe22232>
PoW:	<7f4089a4d9c01173c77e9bb506fbadd8810bd43520f2371da7cb540200000000>
difficulty:	50328137674
2018-06-05 03:23:04.091	[P2P0]	INFO 	global	src/cryptonote_core/blockchain.cpp:1523	###### REORGANIZE on height: 1581881 of 1581883 with cum_difficulty 15197147278442072
 alternative blockchain size: 4 with cum_difficulty 15197197565916922
2018-06-05 03:23:04.095	[P2P0]	ERROR	blockchain	src/cryptonote_core/blockchain.cpp:939	Failed to switch to alternative blockchain
2018-06-05 03:23:04.095	[P2P0]	WARN 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:2781	WARNING: batch transaction mode already enabled, but asked to enable batch mode
2018-06-05 03:23:04.138	[P2P0]	ERROR	blockchain	src/cryptonote_core/blockchain.cpp:883	PANIC! failed to add (again) block while chain switching during the rollback!
2018-06-05 03:23:04.138	[P2P0]	ERROR	blockchain	src/cryptonote_core/blockchain.cpp:950	The block was inserted as invalid while connecting new alternative chain, block_id: <7109e6c518717d56f4ea9eb58812f03b98363dbcf78cd8a613df74523d854886>
sync_info
Height: 1581881, target: 1588050 (99.6115%)
Downloading at 1574 kB/s
8 peers
108.39.253.113:18080      cde8d64ecd29245e  1578782  2 kB/s, 0 blocks / 0 MB queued
71.10.89.159:18080        58152a069fbd1eee  1547696  1 kB/s, 0 blocks / 0 MB queued
69.85.84.31:18080         3827ff2502d554e3  1587299  457 kB/s, 0 blocks / 0 MB queued
27.219.24.14:18080        a7733748adbcc202  1296836  0 kB/s, 0 blocks / 0 MB queued
37.10.71.87:18080         9d061f4c6ff9dba3  1588050  0 kB/s, 0 blocks / 0 MB queued
193.70.41.139:18080       42cd22eefd208071  1588050  418 kB/s, 40 blocks / 6.92823 MB queued
82.216.180.220:18080      6529ed935a1c078e  1588050  385 kB/s, 40 blocks / 4.09451 MB queued
37.59.97.202:18080        9e01b2563f46eea6  1588050  311 kB/s, 40 blocks / 4.17519 MB queued
10 spans, 15.1979 MB
69.85.84.31:18080         20 (1582168 - 1582187)  -
193.70.41.139:18080       20 (1583063 - 1583082, 5196 kB)  563 kB/s (1)
37.59.97.202:18080        20 (1583083 - 1583102, 1461 kB)  670 kB/s (0.88)
82.216.180.220:18080      20 (1583103 - 1583122, 1769 kB)  465 kB/s (0.85)
37.59.97.202:18080        20 (1583123 - 1583142, 2713 kB)  287 kB/s (0.88)
193.70.41.139:18080       20 (1583143 - 1583162, 1731 kB)  525 kB/s (1)
82.216.180.220:18080      20 (1583163 - 1583182, 2325 kB)  459 kB/s (0.85)
193.70.41.139:18080       20 (1583183 - 1583202)  -
82.216.180.220:18080      20 (1583203 - 1583222)  -
37.59.97.202:18080        20 (1583223 - 1583242)  -
version
Monero 'Lithium Luna' (v0.12.2.0-release)
2018-06-05 03:29:12.031	[P2P7]	INFO 	global	src/blockchain_db/lmdb/db_lmdb.cpp:588	[batch] DB resize needed
2018-06-05 03:29:12.078	[P2P7]	INFO 	global	src/blockchain_db/lmdb/db_lmdb.cpp:504	LMDB Mapsize increased.  Old: 61307MiB, New: 62331MiB
sync_info
Height: 1581881, target: 1588055 (99.6112%)
Downloading at 1376 kB/s
8 peers
73.54.147.5:18080         adaf06b95129c675  442156  0 kB/s, 0 blocks / 0 MB queued
92.7.4.226:18080          037c25199ee3a566  1318640  0 kB/s, 0 blocks / 0 MB queued
69.85.84.31:18080         3827ff2502d554e3  1587299  361 kB/s, 120 blocks / 11.8937 MB queued
27.219.24.14:18080        a7733748adbcc202  1308596  1 kB/s, 0 blocks / 0 MB queued
193.70.41.139:18080       42cd22eefd208071  1588054  232 kB/s, 120 blocks / 13.5071 MB queued
82.216.180.220:18080      6529ed935a1c078e  1588054  229 kB/s, 60 blocks / 9.09515 MB queued
64.229.63.116:18080       a8a03308d6897fda  1588054  148 kB/s, 0 blocks / 0 MB queued
37.59.97.202:18080        9e01b2563f46eea6  1588055  405 kB/s, 140 blocks / 11.0811 MB queued
26 spans, 45.577 MB
64.229.63.116:18080       20 (1582130 - 1582149)  -
82.216.180.220:18080      20 (1583353 - 1583372, 2493 kB)  265 kB/s (0.26)
82.216.180.220:18080      20 (1583373 - 1583392)  -
69.85.84.31:18080         20 (1583828 - 1583847, 2001 kB)  533 kB/s (1)
69.85.84.31:18080         20 (1583848 - 1583867, 1504 kB)  492 kB/s (1)
69.85.84.31:18080         20 (1583868 - 1583887, 1849 kB)  430 kB/s (1)
37.59.97.202:18080        20 (1583888 - 1583907, 1319 kB)  157 kB/s (0.8)
69.85.84.31:18080         20 (1583908 - 1583927, 2124 kB)  477 kB/s (1)
69.85.84.31:18080         20 (1583928 - 1583947, 2330 kB)  726 kB/s (1)
37.59.97.202:18080        20 (1583948 - 1583967, 1409 kB)  395 kB/s (0.8)
69.85.84.31:18080         20 (1583968 - 1583987, 2084 kB)  505 kB/s (1)
37.59.97.202:18080        20 (1583988 - 1584007, 1400 kB)  408 kB/s (0.8)
69.85.84.31:18080         20 (1584008 - 1584027)  -
37.59.97.202:18080        20 (1584028 - 1584047)  -
82.216.180.220:18080      20 (1584562 - 1584581, 1397 kB)  95 kB/s (0.26)
193.70.41.139:18080       20 (1584563 - 1584582, 1510 kB)  322 kB/s (0.56)
193.70.41.139:18080       20 (1584583 - 1584602, 2546 kB)  748 kB/s (0.56)
37.59.97.202:18080        20 (1584603 - 1584622, 1210 kB)  416 kB/s (0.8)
37.59.97.202:18080        20 (1584623 - 1584642, 1620 kB)  615 kB/s (0.8)
193.70.41.139:18080       20 (1584643 - 1584662, 1680 kB)  526 kB/s (0.56)
37.59.97.202:18080        20 (1584663 - 1584682, 2021 kB)  567 kB/s (0.8)
193.70.41.139:18080       20 (1584683 - 1584702, 2902 kB)  696 kB/s (0.56)
37.59.97.202:18080        20 (1584703 - 1584722, 2099 kB)  354 kB/s (0.8)
193.70.41.139:18080       20 (1584723 - 1584742, 3714 kB)  212 kB/s (0.56)
82.216.180.220:18080      20 (1584743 - 1584762, 5204 kB)  108 kB/s (0.26)
193.70.41.139:18080       20 (1584763 - 1584782, 1153 kB)  206 kB/s (0.56)
2018-06-05 03:47:43.225	[P2P5]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:310	[94.67.208.147:18080 OUT] Sync data returned a new top block candidate: 1581881 -> 1588066 [Your node is 6185 blocks (8 days) behind] 
SYNCHRONIZATION started
2018-06-05 03:48:25.136	[P2P4]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:310	[103.253.40.189:18080 OUT] Sync data returned a new top block candidate: 1581881 -> 1588068 [Your node is 6187 blocks (8 days) behind] 
SYNCHRONIZATION started
2018-06-05 03:48:27.322	[P2P9]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:310	[64.229.63.116:18080 OUT] Sync data returned a new top block candidate: 1581881 -> 1588068 [Your node is 6187 blocks (8 days) behind] 
SYNCHRONIZATION started
2018-06-05 03:54:02.230	[P2P5]	ERROR	blockchain	src/cryptonote_core/blockchain.cpp:3936	usable is negative
2018-06-05 03:57:29.022	[P2P4]	ERROR	blockchain	src/cryptonote_core/blockchain.cpp:3936	usable is negative
2018-06-05 03:58:13.033	[P2P8]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:310	[190.141.89.13:18080 OUT] Sync data returned a new top block candidate: 1581881 -> 1588685 [Your node is 6804 blocks (9 days) behind] 
SYNCHRONIZATION started
2018-06-05 04:01:47.127	[P2P8]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:310	[71.13.18.253:18080 OUT] Sync data returned a new top block candidate: 1581881 -> 1588078 [Your node is 6197 blocks (8 days) behind] 
SYNCHRONIZATION started
2018-06-05 04:06:33.968	[P2P1]	ERROR	blockchain	src/cryptonote_core/blockchain.cpp:3936	usable is negative
2018-06-05 04:30:09.462	[P2P3]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:310	[67.42.30.57:18080 OUT] Sync data returned a new top block candidate: 1581881 -> 1588088 [Your node is 6207 blocks (8 days) behind] 
SYNCHRONIZATION started
2018-06-05 04:30:28.466	[P2P5]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:310	[111.231.109.238:18080 OUT] Sync data returned a new top block candidate: 1581881 -> 1578866 [Your node is 3015 blocks (4 days) ahead] 
SYNCHRONIZATION started
2018-06-05 04:34:42.304	[P2P1]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:310	[91.121.87.10:28080 OUT] Sync data returned a new top block candidate: 1581881 -> 1588094 [Your node is 6213 blocks (8 days) behind] 
SYNCHRONIZATION started
2018-06-05 04:34:51.927	[P2P7]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:310	[47.147.196.208:18080 OUT] Sync data returned a new top block candidate: 1581881 -> 1588094 [Your node is 6213 blocks (8 days) behind] 
SYNCHRONIZATION started
2018-06-05 04:35:07.801	[P2P5]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:310	[219.88.234.15:18080 OUT] Sync data returned a new top block candidate: 1581881 -> 1586776 [Your node is 4895 blocks (6 days) behind] 
SYNCHRONIZATION started
2018-06-05 04:35:09.081	[P2P4]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:310	[47.222.1.180:18080 OUT] Sync data returned a new top block candidate: 1581881 -> 1588094 [Your node is 6213 blocks (8 days) behind] 
SYNCHRONIZATION started
sync_info
Height: 1581881, target: 1588094 (99.6088%)
Downloading at 196 kB/s
8 peers
85.214.216.207:18080      b1e7560affc7508d  1588094  180 kB/s, 0 blocks / 0 MB queued
185.205.12.118:18080      360d8824ede90342  1587299  7 kB/s, 0 blocks / 0 MB queued
88.103.173.171:18080      7b93b6a509f7687a  980800  3 kB/s, 0 blocks / 0 MB queued
198.204.238.106:18080     31b83bb4be364606  898196  2 kB/s, 0 blocks / 0 MB queued
172.245.127.213:18080     5e23087e382572d7  1577292  0 kB/s, 0 blocks / 0 MB queued
123.53.181.5:18080        8e5c425ad5483cb0  1546151  2 kB/s, 0 blocks / 0 MB queued
73.54.147.5:18080         adaf06b95129c675  570064  2 kB/s, 0 blocks / 0 MB queued
27.219.24.14:18080        a7733748adbcc202  1348576  0 kB/s, 0 blocks / 0 MB queued
39 spans, 93.4337 MB
185.205.12.118:18080      20 (1581882 - 1581901)  -
85.214.216.207:18080      20 (1582244 - 1582263)  -
                          20 (1587422 - 1587441, 1143 kB)  706 kB/s (0.66)
                          20 (1587442 - 1587461, 4219 kB)  603 kB/s (0.66)
                          20 (1587462 - 1587481, 3416 kB)  934 kB/s (0.66)
                          20 (1587473 - 1587492, 2882 kB)  143 kB/s (0.08)
                          20 (1587493 - 1587512, 2196 kB)  305 kB/s (1)
                          20 (1587513 - 1587532, 2172 kB)  969 kB/s (0.66)
                          20 (1587533 - 1587552, 3198 kB)  627 kB/s (0.66)
                          20 (1587553 - 1587572, 2698 kB)  278 kB/s (1)
                          20 (1587573 - 1587592, 2299 kB)  178 kB/s (0.82)
                          20 (1587593 - 1587612, 5002 kB)  1314 kB/s (0.66)
                          20 (1587613 - 1587632, 1976 kB)  405 kB/s (1)
                          20 (1587633 - 1587652, 3852 kB)  179 kB/s (0.08)
                          20 (1587653 - 1587672, 2935 kB)  380 kB/s (0.82)
                          20 (1587673 - 1587692, 2614 kB)  405 kB/s (1)
                          20 (1587693 - 1587712, 2241 kB)  548 kB/s (0.66)
                          20 (1587713 - 1587732, 2948 kB)  468 kB/s (0.66)
                          20 (1587733 - 1587752, 2516 kB)  387 kB/s (1)
                          20 (1587753 - 1587772, 3141 kB)  397 kB/s (0.82)
                          20 (1587773 - 1587792, 2621 kB)  1113 kB/s (0.66)
                          20 (1587793 - 1587812, 1826 kB)  510 kB/s (1)
                          20 (1587813 - 1587832, 2936 kB)  645 kB/s (0.82)
                          20 (1587833 - 1587852, 2254 kB)  945 kB/s (0.66)
                          20 (1587853 - 1587872, 2357 kB)  769 kB/s (1)
                          20 (1587873 - 1587892, 1969 kB)  109 kB/s (0.08)
                          20 (1587893 - 1587912, 1716 kB)  619 kB/s (0.82)
                          20 (1587913 - 1587932, 2906 kB)  1276 kB/s (1)
                          20 (1587933 - 1587952, 2125 kB)  165 kB/s (0.08)
                          20 (1587953 - 1587972, 1931 kB)  1160 kB/s (1)
                          20 (1587973 - 1587992, 2440 kB)  455 kB/s (0.82)
                          20 (1587993 - 1588012, 1351 kB)  708 kB/s (1)
                          20 (1588013 - 1588032, 2692 kB)  125 kB/s (0.08)
                          20 (1588033 - 1588052, 6108 kB)  922 kB/s (1)
                          11 (1588053 - 1588063, 3243 kB)  979 kB/s (0.82)
                          1 (1588064 - 1588064, 244 kB)  52 kB/s (0.08)
                          1 (1588065 - 1588065, 221 kB)  55 kB/s (0.08)
                          20 (1588066 - 1588085, 2420 kB)  415 kB/s (0.66)
                          2 (1588086 - 1588087, 608 kB)  518 kB/s (0.66)
2018-06-05 04:42:03.758	[P2P8]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:310	[37.59.56.102:18080 OUT] Sync data returned a new top block candidate: 1581881 -> 1588095 [Your node is 6214 blocks (8 days) behind] 
SYNCHRONIZATION started
2018-06-05 04:44:57.437	[P2P7]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:310	[90.252.39.118:18080 OUT] Sync data returned a new top block candidate: 1581881 -> 1588096 [Your node is 6215 blocks (8 days) behind] 
SYNCHRONIZATION started
2018-06-05 05:01:15.961	[P2P1]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:310	[94.130.161.41:18080 OUT] Sync data returned a new top block candidate: 1581881 -> 1588100 [Your node is 6219 blocks (8 days) behind] 
SYNCHRONIZATION started
2018-06-05 05:01:53.303	[P2P4]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:310	[212.83.130.45:18080 OUT] Sync data returned a new top block candidate: 1581881 -> 1588101 [Your node is 6220 blocks (8 days) behind] 
SYNCHRONIZATION started
2018-06-05 05:11:58.317	[P2P4]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:310	[24.95.42.32:18080 OUT] Sync data returned a new top block candidate: 1581881 -> 1588108 [Your node is 6227 blocks (8 days) behind] 
SYNCHRONIZATION started
2018-06-05 05:15:01.368	[P2P1]	ERROR	blockchain	src/cryptonote_core/blockchain.cpp:3936	usable is negative
2018-06-05 05:17:06.486	[P2P5]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:310	[107.191.99.227:18080 OUT] Sync data returned a new top block candidate: 1581881 -> 1588110 [Your node is 6229 blocks (8 days) behind] 
SYNCHRONIZATION started
2018-06-05 05:23:16.241	[P2P2]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:310	[185.21.223.231:18080 OUT] Sync data returned a new top block candidate: 1581881 -> 1588114 [Your node is 6233 blocks (8 days) behind] 
SYNCHRONIZATION started
2018-06-05 05:47:19.729	[P2P3]	INFO 	global	src/blockchain_db/lmdb/db_lmdb.cpp:588	[batch] DB resize needed
2018-06-05 05:47:19.919	[P2P3]	INFO 	global	src/blockchain_db/lmdb/db_lmdb.cpp:504	LMDB Mapsize increased.  Old: 62331MiB, New: 63355MiB
2018-06-05 05:47:19.920	[P2P3]	INFO 	global	src/blockchain_db/lmdb/db_lmdb.cpp:588	[batch] DB resize needed
2018-06-05 05:47:19.931	[P2P3]	INFO 	global	src/blockchain_db/lmdb/db_lmdb.cpp:504	LMDB Mapsize increased.  Old: 63355MiB, New: 64379MiB
2018-06-05 05:47:19.931	[P2P3]	INFO 	global	src/blockchain_db/lmdb/db_lmdb.cpp:588	[batch] DB resize needed
2018-06-05 05:47:19.944	[P2P3]	INFO 	global	src/blockchain_db/lmdb/db_lmdb.cpp:504	LMDB Mapsize increased.  Old: 64379MiB, New: 65403MiB
2018-06-05 06:21:00.152	[P2P3]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:310	[149.202.80.233:18080 OUT] Sync data returned a new top block candidate: 1581881 -> 1588143 [Your node is 6262 blocks (8 days) behind] 
SYNCHRONIZATION started
status
Height: 1581881/1588150 (99.6%) on mainnet, not mining, net hash 420.46 MH/s, v7, up to date, 8(out)+0(in) connections, uptime 0d 14h 58m 40s
2018-06-05 07:23:55.162	[P2P3]	INFO 	global	src/blockchain_db/lmdb/db_lmdb.cpp:588	[batch] DB resize needed
2018-06-05 07:23:55.284	[P2P3]	INFO 	global	src/blockchain_db/lmdb/db_lmdb.cpp:504	LMDB Mapsize increased.  Old: 65403MiB, New: 66427MiB
2018-06-05 07:23:55.285	[P2P3]	INFO 	global	src/blockchain_db/lmdb/db_lmdb.cpp:588	[batch] DB resize needed
2018-06-05 07:23:55.295	[P2P3]	INFO 	global	src/blockchain_db/lmdb/db_lmdb.cpp:504	LMDB Mapsize increased.  Old: 66427MiB, New: 67451MiB
2018-06-05 07:23:55.296	[P2P3]	INFO 	global	src/blockchain_db/lmdb/db_lmdb.cpp:588	[batch] DB resize needed
2018-06-05 07:23:55.307	[P2P3]	INFO 	global	src/blockchain_db/lmdb/db_lmdb.cpp:504	LMDB Mapsize increased.  Old: 67451MiB, New: 68475MiB
2018-06-05 07:23:55.308	[P2P3]	INFO 	global	src/blockchain_db/lmdb/db_lmdb.cpp:588	[batch] DB resize needed
2018-06-05 07:23:55.317	[P2P3]	INFO 	global	src/blockchain_db/lmdb/db_lmdb.cpp:504	LMDB Mapsize increased.  Old: 68475MiB, New: 69499MiB
2018-06-05 07:23:55.318	[P2P3]	INFO 	global	src/blockchain_db/lmdb/db_lmdb.cpp:588	[batch] DB resize needed
2018-06-05 07:23:55.327	[P2P3]	INFO 	global	src/blockchain_db/lmdb/db_lmdb.cpp:504	LMDB Mapsize increased.  Old: 69499MiB, New: 70523MiB
2018-06-05 07:23:55.329	[P2P3]	INFO 	global	src/blockchain_db/lmdb/db_lmdb.cpp:588	[batch] DB resize needed
2018-06-05 07:23:55.339	[P2P3]	INFO 	global	src/blockchain_db/lmdb/db_lmdb.cpp:504	LMDB Mapsize increased.  Old: 70523MiB, New: 71547MiB
2018-06-05 07:23:55.340	[P2P3]	INFO 	global	src/blockchain_db/lmdb/db_lmdb.cpp:588	[batch] DB resize needed
2018-06-05 07:23:55.350	[P2P3]	INFO 	global	src/blockchain_db/lmdb/db_lmdb.cpp:504	LMDB Mapsize increased.  Old: 71547MiB, New: 72571MiB
2018-06-05 07:23:55.351	[P2P3]	INFO 	global	src/blockchain_db/lmdb/db_lmdb.cpp:588	[batch] DB resize needed
2018-06-05 07:23:55.361	[P2P3]	INFO 	global	src/blockchain_db/lmdb/db_lmdb.cpp:504	LMDB Mapsize increased.  Old: 72571MiB, New: 73595MiB
2018-06-05 07:23:55.362	[P2P3]	INFO 	global	src/blockchain_db/lmdb/db_lmdb.cpp:588	[batch] DB resize needed
2018-06-05 07:23:55.371	[P2P3]	INFO 	global	src/blockchain_db/lmdb/db_lmdb.cpp:504	LMDB Mapsize increased.  Old: 73595MiB, New: 74619MiB
2018-06-05 07:23:55.372	[P2P3]	INFO 	global	src/blockchain_db/lmdb/db_lmdb.cpp:588	[batch] DB resize needed
2018-06-05 07:23:55.381	[P2P3]	INFO 	global	src/blockchain_db/lmdb/db_lmdb.cpp:504	LMDB Mapsize increased.  Old: 74619MiB, New: 75643MiB
2018-06-05 07:23:55.383	[P2P3]	INFO 	global	src/blockchain_db/lmdb/db_lmdb.cpp:588	[batch] DB resize needed
2018-06-05 07:23:55.393	[P2P3]	INFO 	global	src/blockchain_db/lmdb/db_lmdb.cpp:504	LMDB Mapsize increased.  Old: 75643MiB, New: 76667MiB
2018-06-05 07:23:55.394	[P2P3]	INFO 	global	src/blockchain_db/lmdb/db_lmdb.cpp:588	[batch] DB resize needed
2018-06-05 07:23:55.404	[P2P3]	INFO 	global	src/blockchain_db/lmdb/db_lmdb.cpp:504	LMDB Mapsize increased.  Old: 76667MiB, New: 77691MiB
2018-06-05 07:23:55.405	[P2P3]	INFO 	global	src/blockchain_db/lmdb/db_lmdb.cpp:588	[batch] DB resize needed
2018-06-05 07:23:55.415	[P2P3]	INFO 	global	src/blockchain_db/lmdb/db_lmdb.cpp:504	LMDB Mapsize increased.  Old: 77691MiB, New: 78715MiB
2018-06-05 07:23:55.416	[P2P3]	INFO 	global	src/blockchain_db/lmdb/db_lmdb.cpp:588	[batch] DB resize needed
2018-06-05 07:23:55.428	[P2P3]	INFO 	global	src/blockchain_db/lmdb/db_lmdb.cpp:504	LMDB Mapsize increased.  Old: 78715MiB, New: 79739MiB
2018-06-05 07:23:55.428	[P2P3]	INFO 	global	src/blockchain_db/lmdb/db_lmdb.cpp:588	[batch] DB resize needed
2018-06-05 07:23:55.438	[P2P3]	INFO 	global	src/blockchain_db/lmdb/db_lmdb.cpp:504	LMDB Mapsize increased.  Old: 79739MiB, New: 80763MiB
2018-06-05 07:23:55.438	[P2P3]	INFO 	global	src/blockchain_db/lmdb/db_lmdb.cpp:588	[batch] DB resize needed
2018-06-05 07:23:55.448	[P2P3]	INFO 	global	src/blockchain_db/lmdb/db_lmdb.cpp:504	LMDB Mapsize increased.  Old: 80763MiB, New: 81787MiB
2018-06-05 07:23:55.449	[P2P3]	INFO 	global	src/blockchain_db/lmdb/db_lmdb.cpp:588	[batch] DB resize needed
2018-06-05 07:23:55.458	[P2P3]	INFO 	global	src/blockchain_db/lmdb/db_lmdb.cpp:504	LMDB Mapsize increased.  Old: 81787MiB, New: 82811MiB
2018-06-05 07:23:55.461	[P2P3]	INFO 	global	src/blockchain_db/lmdb/db_lmdb.cpp:588	[batch] DB resize needed
2018-06-05 07:23:55.470	[P2P3]	INFO 	global	src/blockchain_db/lmdb/db_lmdb.cpp:504	LMDB Mapsize increased.  Old: 82811MiB, New: 83835MiB
2018-06-05 07:23:55.471	[P2P3]	INFO 	global	src/blockchain_db/lmdb/db_lmdb.cpp:588	[batch] DB resize needed
2018-06-05 07:23:55.481	[P2P3]	INFO 	global	src/blockchain_db/lmdb/db_lmdb.cpp:504	LMDB Mapsize increased.  Old: 83835MiB, New: 84859MiB
2018-06-05 07:23:55.482	[P2P3]	INFO 	global	src/blockchain_db/lmdb/db_lmdb.cpp:588	[batch] DB resize needed
2018-06-05 07:23:55.492	[P2P3]	INFO 	global	src/blockchain_db/lmdb/db_lmdb.cpp:504	LMDB Mapsize increased.  Old: 84859MiB, New: 85883MiB
status
Height: 1581881/1588199 (99.6%) on mainnet, not mining, net hash 420.46 MH/s, v7, up to date, 8(out)+0(in) connections, uptime 0d 16h 0m 34s
set_log 0,blockchain:DEBUG
Log categories are now *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO,blockchain:DEBUG
2018-06-05 07:36:56.724	[P2P4]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582329 - 1588199 start at 6180 and end at 6203
2018-06-05 07:36:56.726	[P2P4]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5871 / 5871
2018-06-05 07:36:58.848	[P2P5]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582329 - 1588199 start at 6180 and end at 6203
2018-06-05 07:36:58.850	[P2P5]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5871 / 5871
2018-06-05 07:37:03.726	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1581880 - 1587298 start at 6179 and end at 6200
2018-06-05 07:37:03.728	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5419 / 5419
2018-06-05 07:37:04.405	[P2P6]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582329 - 1588199 start at 6180 and end at 6203
2018-06-05 07:37:04.407	[P2P6]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5871 / 5871
2018-06-05 07:37:08.255	[P2P0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582329 - 1588199 start at 6180 and end at 6203
2018-06-05 07:37:08.257	[P2P0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5871 / 5871
2018-06-05 07:37:10.788	[P2P8]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582860 - 1588199 start at 6183 and end at 6203
2018-06-05 07:37:10.790	[P2P8]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5340 / 5340
2018-06-05 07:37:13.212	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582880 - 1588199 start at 6183 and end at 6203
2018-06-05 07:37:13.215	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5320 / 5320
2018-06-05 07:37:15.679	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582800 - 1588199 start at 6182 and end at 6203
2018-06-05 07:37:15.680	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5400 / 5400
2018-06-05 07:37:17.937	[P2P8]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582920 - 1588199 start at 6183 and end at 6203
2018-06-05 07:37:17.939	[P2P8]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5280 / 5280
2018-06-05 07:37:18.806	[P2P4]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582940 - 1588199 start at 6183 and end at 6203
2018-06-05 07:37:18.808	[P2P4]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5260 / 5260
2018-06-05 07:37:22.152	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1581880 - 1588199 start at 6179 and end at 6203
2018-06-05 07:37:22.154	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 6320 / 6320
2018-06-05 07:37:22.467	[P2P4]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582960 - 1588199 start at 6183 and end at 6203
2018-06-05 07:37:22.468	[P2P4]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5240 / 5240
2018-06-05 07:37:23.179	[P2P5]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582840 - 1588199 start at 6182 and end at 6203
2018-06-05 07:37:23.181	[P2P5]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5360 / 5360
2018-06-05 07:37:26.841	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582900 - 1588199 start at 6183 and end at 6203
2018-06-05 07:37:26.843	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5300 / 5300
2018-06-05 07:37:29.629	[P2P4]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582820 - 1588199 start at 6182 and end at 6203
2018-06-05 07:37:29.631	[P2P4]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5380 / 5380
2018-06-05 07:37:30.178	[P2P2]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583020 - 1588199 start at 6183 and end at 6203
2018-06-05 07:37:30.180	[P2P2]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5180 / 5180
2018-06-05 07:37:31.983	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582980 - 1588199 start at 6183 and end at 6203
2018-06-05 07:37:31.984	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5220 / 5220
2018-06-05 07:37:33.143	[P2P0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583000 - 1588199 start at 6183 and end at 6203
2018-06-05 07:37:33.144	[P2P0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5200 / 5200
2018-06-05 07:37:34.606	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583100 - 1588199 start at 6183 and end at 6203
2018-06-05 07:37:34.608	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5100 / 5100
2018-06-05 07:37:43.892	[P2P8]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1581880 - 1588199 start at 6179 and end at 6203
2018-06-05 07:37:43.895	[P2P8]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 6320 / 6320
2018-06-05 07:37:48.726	[P2P2]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583120 - 1588199 start at 6184 and end at 6203
2018-06-05 07:37:48.728	[P2P2]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5080 / 5080
2018-06-05 07:37:49.071	[P2P4]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583160 - 1588199 start at 6184 and end at 6203
2018-06-05 07:37:49.072	[P2P4]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5040 / 5040
2018-06-05 07:37:53.864	[P2P4]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583040 - 1588199 start at 6183 and end at 6203
2018-06-05 07:37:53.866	[P2P4]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5160 / 5160
2018-06-05 07:37:57.278	[P2P5]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583180 - 1588199 start at 6184 and end at 6203
2018-06-05 07:37:57.280	[P2P5]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5020 / 5020
2018-06-05 07:37:59.219	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583140 - 1588199 start at 6184 and end at 6203
2018-06-05 07:37:59.220	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5060 / 5060
2018-06-05 07:38:04.388	[P2P0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583220 - 1588199 start at 6184 and end at 6203
2018-06-05 07:38:04.389	[P2P0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4980 / 4980
2018-06-05 07:38:04.648	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583200 - 1588199 start at 6184 and end at 6203
2018-06-05 07:38:04.649	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5000 / 5000
2018-06-05 07:38:10.094	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583240 - 1588199 start at 6184 and end at 6203
2018-06-05 07:38:10.096	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4960 / 4960
2018-06-05 07:38:12.352	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583260 - 1588199 start at 6184 and end at 6203
2018-06-05 07:38:12.354	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4940 / 4940
2018-06-05 07:38:12.523	[P2P2]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583060 - 1588199 start at 6183 and end at 6203
2018-06-05 07:38:12.525	[P2P2]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5140 / 5140
2018-06-05 07:38:24.472	[P2P4]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583300 - 1588199 start at 6184 and end at 6203
2018-06-05 07:38:24.474	[P2P4]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4900 / 4900
2018-06-05 07:38:30.416	[P2P4]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583280 - 1588199 start at 6184 and end at 6203
2018-06-05 07:38:30.417	[P2P4]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4920 / 4920
2018-06-05 07:38:34.390	[P2P0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583320 - 1588199 start at 6184 and end at 6203
2018-06-05 07:38:34.391	[P2P0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4880 / 4880
diff
BH: 1581881, TH: 52414a638ea758e10f51affaae8a8a9ee2a7d27b9dc29686abb95bf95aca8fc1, DIFF: 50454937567, HR: 420457813 H/s
2018-06-05 07:38:39.349	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583340 - 1588199 start at 6184 and end at 6203
2018-06-05 07:38:39.350	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4860 / 4860
2018-06-05 07:38:39.742	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583380 - 1588199 start at 6185 and end at 6203
2018-06-05 07:38:39.744	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4820 / 4820
2018-06-05 07:38:48.185	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583400 - 1588200 start at 6185 and end at 6203
2018-06-05 07:38:48.186	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4801 / 4801
2018-06-05 07:38:48.295	[P2P8]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583080 - 1588199 start at 6183 and end at 6203
2018-06-05 07:38:48.297	[P2P8]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5120 / 5120
2018-06-05 07:38:48.565	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583360 - 1588200 start at 6185 and end at 6203
2018-06-05 07:38:48.567	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4841 / 4841
2018-06-05 07:38:58.580	[P2P2]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583420 - 1588200 start at 6185 and end at 6203
2018-06-05 07:38:58.581	[P2P2]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4781 / 4781
2018-06-05 07:39:06.084	[P2P5]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583460 - 1588200 start at 6185 and end at 6203
2018-06-05 07:39:06.085	[P2P5]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4741 / 4741
2018-06-05 07:39:07.371	[P2P6]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583520 - 1588200 start at 6185 and end at 6203
2018-06-05 07:39:07.372	[P2P6]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4681 / 4681
2018-06-05 07:39:10.788	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583440 - 1588200 start at 6185 and end at 6203
2018-06-05 07:39:10.789	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4761 / 4761
2018-06-05 07:39:14.023	[P2P6]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583480 - 1588200 start at 6185 and end at 6203
2018-06-05 07:39:14.025	[P2P6]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4721 / 4721
sync_i2018-06-05 07:39:16.058	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583500 - 1588200 start at 6185 and end at 6203
2018-06-05 07:39:16.059	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4701 / 4701
nfo
Height: 1581881, target: 1588201 (99.6021%)
Downloading at 774 kB/s
8 peers
207.38.169.62:18080       04558f0eab5f22f3  1588201  95 kB/s, 80 blocks / 10.3602 MB queued
118.244.204.223:18080     297ae41bf477abe9  1546040  2 kB/s, 0 blocks / 0 MB queued
69.142.164.211:18080      ddd05c9cd6f5a6c1  1588201  80 kB/s, 60 blocks / 13.5012 MB queued
163.172.11.137:18080      38d2bcd3d6f406fe  1588201  231 kB/s, 432 blocks / 61.6677 MB queued
206.221.177.178:18080     aa44ff665e0d48b4  1588201  94 kB/s, 693 blocks / 82.4677 MB queued
37.97.184.163:18080       d3f65066fca19f39  1588201  81 kB/s, 80 blocks / 8.49217 MB queued
34.228.4.121:18080        be1d18f7a8e903aa  1588201  189 kB/s, 897 blocks / 117.481 MB queued
73.54.147.5:18080         adaf06b95129c675  1306168  2 kB/s, 0 blocks / 0 MB queued
158 spans, 386.26 MB
163.172.11.137:18080      20 (1583041 - 1583060, 4755 kB)  107 kB/s (0.38)
69.142.164.211:18080      20 (1583061 - 1583080, 5752 kB)  79 kB/s (0.08)
34.228.4.121:18080        20 (1583081 - 1583100, 1262 kB)  353 kB/s (0.62)
206.221.177.178:18080     20 (1583101 - 1583120, 1924 kB)  120 kB/s (0.35)
207.38.169.62:18080       20 (1583121 - 1583140, 2784 kB)  111 kB/s (0.12)
34.228.4.121:18080        20 (1583141 - 1583160, 1662 kB)  129 kB/s (0.62)
206.221.177.178:18080     20 (1583161 - 1583180, 1942 kB)  256 kB/s (0.35)
34.228.4.121:18080        20 (1583181 - 1583200, 2837 kB)  194 kB/s (0.62)
37.97.184.163:18080       20 (1583201 - 1583220, 1035 kB)  122 kB/s (0.13)
206.221.177.178:18080     20 (1583221 - 1583240, 2676 kB)  233 kB/s (0.35)
207.38.169.62:18080       20 (1583241 - 1583260, 2033 kB)  170 kB/s (0.12)
37.97.184.163:18080       20 (1583261 - 1583280, 2578 kB)  106 kB/s (0.13)
34.228.4.121:18080        20 (1583281 - 1583300, 4944 kB)  265 kB/s (0.62)
206.221.177.178:18080     20 (1583301 - 1583320, 3763 kB)  172 kB/s (0.35)
207.38.169.62:18080       20 (1583321 - 1583340, 2549 kB)  100 kB/s (0.12)
163.172.11.137:18080      20 (1583341 - 1583360, 3254 kB)  93 kB/s (0.38)
34.228.4.121:18080        20 (1583361 - 1583380, 2139 kB)  150 kB/s (0.62)
37.97.184.163:18080       20 (1583381 - 1583400, 1798 kB)  104 kB/s (0.13)
206.221.177.178:18080     20 (1583401 - 1583420, 2193 kB)  97 kB/s (0.35)
207.38.169.62:18080       20 (1583421 - 1583440, 2993 kB)  104 kB/s (0.12)
34.228.4.121:18080        20 (1583441 - 1583460, 3303 kB)  130 kB/s (0.62)
37.97.184.163:18080       20 (1583461 - 1583480, 3079 kB)  128 kB/s (0.13)
69.142.164.211:18080      20 (1583481 - 1583500, 2101 kB)  82 kB/s (0.08)
163.172.11.137:18080      20 (1583501 - 1583520, 3775 kB)  210 kB/s (0.38)
206.221.177.178:18080     20 (1583521 - 1583540)  -
34.228.4.121:18080        20 (1583541 - 1583560)  -
163.172.11.137:18080      20 (1583561 - 1583580)  -
207.38.169.62:18080       20 (1583581 - 1583600)  -
37.97.184.163:18080       20 (1583601 - 1583620)  -
69.142.164.211:18080      20 (1583621 - 1583640)  -
69.142.164.211:18080      20 (1584016 - 1584035, 5647 kB)  69 kB/s (0.08)
163.172.11.137:18080      20 (1584699 - 1584718, 2102 kB)  74 kB/s (0.38)
206.221.177.178:18080     20 (1584719 - 1584738, 3056 kB)  167 kB/s (0.35)
34.228.4.121:18080        20 (1584739 - 1584758, 5195 kB)  103 kB/s (0.62)
206.221.177.178:18080     20 (1584759 - 1584778, 1708 kB)  112 kB/s (0.35)
163.172.11.137:18080      20 (1584779 - 1584798, 2723 kB)  70 kB/s (0.38)
206.221.177.178:18080     20 (1584799 - 1584818, 2667 kB)  106 kB/s (0.35)
206.221.177.178:18080     20 (1584819 - 1584838, 1757 kB)  163 kB/s (0.35)
34.228.4.121:18080        20 (1584839 - 1584858, 1949 kB)  163 kB/s (0.62)
163.172.11.137:18080      20 (1584859 - 1584878, 3580 kB)  132 kB/s (0.38)
206.221.177.178:18080     20 (1584879 - 1584898, 1199 kB)  120 kB/s (0.35)
34.228.4.121:18080        20 (1584899 - 1584918, 2757 kB)  238 kB/s (0.62)
206.221.177.178:18080     20 (1584919 - 1584938, 3376 kB)  133 kB/s (0.35)
34.228.4.121:18080        20 (1584939 - 1584958, 1877 kB)  137 kB/s (0.62)
163.172.11.137:18080      20 (1584959 - 1584978, 3012 kB)  102 kB/s (0.38)
34.228.4.121:18080        20 (1584979 - 1584998, 2422 kB)  124 kB/s (0.62)
206.221.177.178:18080     20 (1584999 - 1585018, 2779 kB)  756 kB/s (0.35)
206.221.177.178:18080     20 (1585019 - 1585038, 2319 kB)  324 kB/s (0.35)
206.221.177.178:18080     20 (1585039 - 1585058, 3615 kB)  131 kB/s (0.35)
34.228.4.121:18080        20 (1585059 - 1585078, 1158 kB)  147 kB/s (0.62)
163.172.11.137:18080      20 (1585079 - 1585098, 2646 kB)  165 kB/s (0.38)
34.228.4.121:18080        20 (1585099 - 1585118, 2071 kB)  97 kB/s (0.62)
163.172.11.137:18080      20 (1585119 - 1585138, 1836 kB)  124 kB/s (0.38)
206.221.177.178:18080     20 (1585139 - 1585158, 1700 kB)  251 kB/s (0.35)
34.228.4.121:18080        20 (1585159 - 1585178, 2409 kB)  139 kB/s (0.62)
163.172.11.137:18080      20 (1585179 - 1585198, 1539 kB)  95 kB/s (0.38)
34.228.4.121:18080        20 (1585199 - 1585218, 993 kB)  279 kB/s (0.62)
163.172.11.137:18080      20 (1585219 - 1585238, 6027 kB)  158 kB/s (0.38)
34.228.4.121:18080        20 (1585239 - 1585258, 5652 kB)  154 kB/s (0.62)
34.228.4.121:18080        20 (1585259 - 1585278, 2122 kB)  186 kB/s (0.62)
163.172.11.137:18080      20 (1585279 - 1585298, 2936 kB)  163 kB/s (0.38)
34.228.4.121:18080        20 (1585299 - 1585318, 1697 kB)  193 kB/s (0.62)
163.172.11.137:18080      20 (1585319 - 1585338, 2620 kB)  152 kB/s (0.38)
34.228.4.121:18080        20 (1585339 - 1585358, 1247 kB)  223 kB/s (0.62)
34.228.4.121:18080        20 (1585359 - 1585378, 1548 kB)  115 kB/s (0.62)
163.172.11.137:18080      20 (1585379 - 1585398, 2182 kB)  115 kB/s (0.38)
34.228.4.121:18080        20 (1585399 - 1585418, 3299 kB)  340 kB/s (0.62)
34.228.4.121:18080        20 (1585419 - 1585438, 2800 kB)  179 kB/s (0.62)
163.172.11.137:18080      20 (1585439 - 1585458, 1871 kB)  108 kB/s (0.38)
34.228.4.121:18080        20 (1585459 - 1585478, 3617 kB)  138 kB/s (0.62)
34.228.4.121:18080        20 (1585479 - 1585498, 4449 kB)  228 kB/s (0.62)
206.221.177.178:18080     20 (1586669 - 1586688, 3001 kB)  1107 kB/s (0.35)
34.228.4.121:18080        20 (1586689 - 1586708, 2263 kB)  1310 kB/s (0.62)
206.221.177.178:18080     20 (1586709 - 1586728, 1086 kB)  833 kB/s (0.35)
34.228.4.121:18080        20 (1586729 - 1586748, 2603 kB)  943 kB/s (0.62)
206.221.177.178:18080     20 (1586749 - 1586768, 2018 kB)  921 kB/s (0.35)
163.172.11.137:18080      20 (1586764 - 1586783, 3114 kB)  725 kB/s (0.38)
34.228.4.121:18080        20 (1586784 - 1586803, 1952 kB)  582 kB/s (0.62)
34.228.4.121:18080        20 (1586804 - 1586823, 4660 kB)  562 kB/s (0.62)
206.221.177.178:18080     20 (1586807 - 1586826, 4355 kB)  336 kB/s (0.35)
34.228.4.121:18080        20 (1586827 - 1586846, 3042 kB)  158 kB/s (0.62)
163.172.11.137:18080      20 (1586847 - 1586866, 4441 kB)  83 kB/s (0.38)
206.221.177.178:18080     20 (1586867 - 1586886, 3941 kB)  174 kB/s (0.35)
34.228.4.121:18080        20 (1586887 - 1586906, 3020 kB)  165 kB/s (0.62)
206.221.177.178:18080     20 (1586907 - 1586926, 1739 kB)  295 kB/s (0.35)
34.228.4.121:18080        20 (1586927 - 1586946, 921 kB)  223 kB/s (0.62)
206.221.177.178:18080     20 (1586947 - 1586966, 2236 kB)  210 kB/s (0.35)
34.228.4.121:18080        20 (1586967 - 1586986, 3174 kB)  135 kB/s (0.62)
206.221.177.178:18080     20 (1586987 - 1587006, 2405 kB)  151 kB/s (0.35)
163.172.11.137:18080      20 (1587007 - 1587026, 2221 kB)  109 kB/s (0.38)
34.228.4.121:18080        20 (1587027 - 1587046, 2203 kB)  158 kB/s (0.62)
206.221.177.178:18080     20 (1587047 - 1587066, 2611 kB)  104 kB/s (0.35)
163.172.11.137:18080      20 (1587067 - 1587086, 1835 kB)  93 kB/s (0.38)
163.172.11.137:18080      20 (1587070 - 1587089, 2070 kB)  85 kB/s (0.38)
34.228.4.121:18080        20 (1587090 - 1587109, 3024 kB)  284 kB/s (0.62)
206.221.177.178:18080     20 (1587110 - 1587129, 3368 kB)  299 kB/s (0.35)
34.228.4.121:18080        20 (1587130 - 1587149, 2321 kB)  197 kB/s (0.62)
206.221.177.178:18080     20 (1587150 - 1587169, 2604 kB)  259 kB/s (0.35)
34.228.4.121:18080        20 (1587170 - 1587189, 2356 kB)  696 kB/s (0.62)
206.221.177.178:18080     20 (1587190 - 1587209, 1359 kB)  1130 kB/s (0.35)
163.172.11.137:18080      20 (1587210 - 1587229, 2435 kB)  170 kB/s (0.38)
206.221.177.178:18080     20 (1587230 - 1587249, 1386 kB)  954 kB/s (0.35)
34.228.4.121:18080        20 (1587250 - 1587269, 2262 kB)  197 kB/s (0.62)
206.221.177.178:18080     20 (1587255 - 1587274, 2217 kB)  193 kB/s (0.35)
34.228.4.121:18080        20 (1587275 - 1587294, 2193 kB)  419 kB/s (0.62)
34.228.4.121:18080        20 (1587295 - 1587314, 1105 kB)  391 kB/s (0.62)
206.221.177.178:18080     20 (1587315 - 1587334, 1991 kB)  308 kB/s (0.35)
34.228.4.121:18080        20 (1587335 - 1587354, 5963 kB)  126 kB/s (0.62)
206.221.177.178:18080     20 (1587355 - 1587374, 2034 kB)  97 kB/s (0.35)
206.221.177.178:18080     20 (1587375 - 1587394, 1810 kB)  94 kB/s (0.35)
206.221.177.178:18080     20 (1587395 - 1587414, 2684 kB)  145 kB/s (0.35)
34.228.4.121:18080        20 (1587415 - 1587434, 952 kB)  114 kB/s (0.62)
34.228.4.121:18080        20 (1587435 - 1587454, 2978 kB)  216 kB/s (0.62)
                          20 (1587442 - 1587461, 4219 kB)  603 kB/s (0.66)
                          20 (1587462 - 1587481, 3416 kB)  934 kB/s (0.66)
                          20 (1587473 - 1587492, 2882 kB)  143 kB/s (0.08)
                          20 (1587493 - 1587512, 2196 kB)  305 kB/s (1)
                          20 (1587513 - 1587532, 2172 kB)  969 kB/s (0.66)
                          20 (1587533 - 1587552, 3198 kB)  627 kB/s (0.66)
                          20 (1587553 - 1587572, 2698 kB)  278 kB/s (1)
                          20 (1587573 - 1587592, 2299 kB)  178 kB/s (0.82)
                          20 (1587593 - 1587612, 5002 kB)  1314 kB/s (0.66)
                          20 (1587613 - 1587632, 1976 kB)  405 kB/s (1)
                          20 (1587633 - 1587652, 3852 kB)  179 kB/s (0.08)
                          20 (1587653 - 1587672, 2935 kB)  380 kB/s (0.82)
                          20 (1587673 - 1587692, 2614 kB)  405 kB/s (1)
                          20 (1587693 - 1587712, 2241 kB)  548 kB/s (0.66)
                          20 (1587713 - 1587732, 2948 kB)  468 kB/s (0.66)
                          20 (1587733 - 1587752, 2516 kB)  387 kB/s (1)
                          20 (1587753 - 1587772, 3141 kB)  397 kB/s (0.82)
                          20 (1587773 - 1587792, 2621 kB)  1113 kB/s (0.66)
                          20 (1587793 - 1587812, 1826 kB)  510 kB/s (1)
                          20 (1587813 - 1587832, 2936 kB)  645 kB/s (0.82)
                          20 (1587833 - 1587852, 2254 kB)  945 kB/s (0.66)
                          20 (1587853 - 1587872, 2357 kB)  769 kB/s (1)
                          20 (1587873 - 1587892, 1969 kB)  109 kB/s (0.08)
                          20 (1587893 - 1587912, 1716 kB)  619 kB/s (0.82)
                          20 (1587913 - 1587932, 2906 kB)  1276 kB/s (1)
                          20 (1587933 - 1587952, 2125 kB)  165 kB/s (0.08)
                          20 (1587953 - 1587972, 1931 kB)  1160 kB/s (1)
                          20 (1587973 - 1587992, 2440 kB)  455 kB/s (0.82)
                          20 (1587993 - 1588012, 1351 kB)  708 kB/s (1)
                          20 (1588013 - 1588032, 2692 kB)  125 kB/s (0.08)
                          20 (1588033 - 1588052, 6108 kB)  922 kB/s (1)
                          11 (1588053 - 1588063, 3243 kB)  979 kB/s (0.82)
                          1 (1588064 - 1588064, 244 kB)  52 kB/s (0.08)
                          1 (1588065 - 1588065, 221 kB)  55 kB/s (0.08)
                          20 (1588066 - 1588085, 2420 kB)  415 kB/s (0.66)
                          2 (1588086 - 1588087, 608 kB)  518 kB/s (0.66)
34.228.4.121:18080        20 (1588088 - 1588107, 3398 kB)  541 kB/s (0.62)
34.228.4.121:18080        19 (1588108 - 1588126, 2202 kB)  195 kB/s (0.62)
206.221.177.178:18080     10 (1588127 - 1588136, 1147 kB)  670 kB/s (0.35)
206.221.177.178:18080     20 (1588137 - 1588156, 1577 kB)  168 kB/s (0.35)
206.221.177.178:18080     3 (1588157 - 1588159, 206 kB)  339 kB/s (0.35)
34.228.4.121:18080        13 (1588160 - 1588172, 537 kB)  85 kB/s (0.62)
163.172.11.137:18080      12 (1588173 - 1588184, 683 kB)  536 kB/s (0.38)
34.228.4.121:18080        1 (1588185 - 1588185, 280 kB)  383 kB/s (0.62)
34.228.4.121:18080        4 (1588186 - 1588189, 641 kB)  828 kB/s (0.62)
2018-06-05 07:39:18.065	[P2P6]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583560 - 1588200 start at 6185 and end at 6203
2018-06-05 07:39:18.066	[P2P6]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4641 / 4641
2018-06-05 07:39:18.591	[P2P4]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583580 - 1588200 start at 6185 and end at 6203
2018-06-05 07:39:18.593	[P2P4]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4621 / 4621
2018-06-05 07:39:23.907	[P2P0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583660 - 1588200 start at 6186 and end at 6203
2018-06-05 07:39:23.908	[P2P0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4541 / 4541
2018-06-05 07:39:27.859	[P2P6]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583540 - 1588200 start at 6185 and end at 6203
2018-06-05 07:39:27.861	[P2P6]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4661 / 4661
2018-06-05 07:39:28.605	[P2P0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583600 - 1588201 start at 6185 and end at 6203
2018-06-05 07:39:28.606	[P2P0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4602 / 4602
2018-06-05 07:39:30.334	[P2P0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583680 - 1588201 start at 6186 and end at 6203
2018-06-05 07:39:30.335	[P2P0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4522 / 4522
2018-06-05 07:39:34.339	[P2P5]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583620 - 1588201 start at 6186 and end at 6203
2018-06-05 07:39:34.340	[P2P5]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4582 / 4582
2018-06-05 07:39:35.543	[P2P8]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583700 - 1588201 start at 6186 and end at 6203
2018-06-05 07:39:35.544	[P2P8]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4502 / 4502
2018-06-05 07:39:37.840	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583720 - 1588201 start at 6186 and end at 6203
2018-06-05 07:39:37.841	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4482 / 4482
2018-06-05 07:39:39.645	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583740 - 1588201 start at 6186 and end at 6203
2018-06-05 07:39:39.647	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4462 / 4462
2018-06-05 07:39:39.665	[P2P5]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583760 - 1588201 start at 6186 and end at 6203
2018-06-05 07:39:39.667	[P2P5]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4442 / 4442
2018-06-05 07:39:43.778	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583860 - 1588201 start at 6186 and end at 6203
2018-06-05 07:39:43.780	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4342 / 4342
2018-06-05 07:39:48.592	[P2P8]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583880 - 1588201 start at 6187 and end at 6203
2018-06-05 07:39:48.593	[P2P8]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4322 / 4322
2018-06-05 07:39:51.869	[P2P2]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583820 - 1588201 start at 6186 and end at 6203
2018-06-05 07:39:51.870	[P2P2]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4382 / 4382
2018-06-05 07:39:55.873	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583640 - 1588201 start at 6186 and end at 6203
2018-06-05 07:39:55.874	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4562 / 4562
2018-06-05 07:39:57.234	[P2P2]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583900 - 1588201 start at 6187 and end at 6203
2018-06-05 07:39:57.235	[P2P2]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4302 / 4302
2018-06-05 07:39:57.910	[P2P4]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583800 - 1588201 start at 6186 and end at 6203
2018-06-05 07:39:57.911	[P2P4]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4402 / 4402
2018-06-05 07:39:59.634	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583920 - 1588201 start at 6187 and end at 6203
2018-06-05 07:39:59.635	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4282 / 4282
2018-06-05 07:40:00.778	[P2P8]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583840 - 1588201 start at 6186 and end at 6203
2018-06-05 07:40:00.779	[P2P8]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4362 / 4362
2018-06-05 07:40:01.744	[P2P6]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584000 - 1588201 start at 6187 and end at 6203
2018-06-05 07:40:01.746	[P2P6]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4202 / 4202
2018-06-05 07:40:06.086	[P2P2]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583960 - 1588201 start at 6187 and end at 6203
2018-06-05 07:40:06.198	[P2P2]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4242 / 4242
2018-06-05 07:40:06.894	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584055 - 1588201 start at 6187 and end at 6203
2018-06-05 07:40:06.896	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4147 / 4147
2018-06-05 07:40:10.976	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584095 - 1588201 start at 6187 and end at 6203
2018-06-05 07:40:10.978	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4107 / 4107
2018-06-05 07:40:11.182	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583980 - 1588201 start at 6187 and end at 6203
2018-06-05 07:40:11.184	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4222 / 4222
2018-06-05 07:40:12.729	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584075 - 1588202 start at 6187 and end at 6203
2018-06-05 07:40:12.730	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4128 / 4128
2018-06-05 07:40:13.608	[P2P5]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584020 - 1588202 start at 6187 and end at 6203
2018-06-05 07:40:13.609	[P2P5]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4183 / 4183
2018-06-05 07:40:13.747	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583780 - 1588202 start at 6186 and end at 6203
2018-06-05 07:40:13.749	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4423 / 4423
2018-06-05 07:40:13.969	[P2P0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584115 - 1588202 start at 6187 and end at 6203
2018-06-05 07:40:13.970	[P2P0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4088 / 4088
2018-06-05 07:40:15.427	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584135 - 1588202 start at 6188 and end at 6203
2018-06-05 07:40:15.428	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4068 / 4068
2018-06-05 07:40:17.917	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584215 - 1588203 start at 6188 and end at 6203
2018-06-05 07:40:17.918	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3989 / 3989
2018-06-05 07:40:17.991	[P2P0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584155 - 1588203 start at 6188 and end at 6203
2018-06-05 07:40:17.992	[P2P0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4049 / 4049
2018-06-05 07:40:18.023	[P2P4]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584195 - 1588203 start at 6188 and end at 6203
2018-06-05 07:40:18.024	[P2P4]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4009 / 4009
2018-06-05 07:40:18.321	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584175 - 1588203 start at 6188 and end at 6203
2018-06-05 07:40:18.322	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4029 / 4029
2018-06-05 07:40:19.274	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584235 - 1588203 start at 6188 and end at 6203
2018-06-05 07:40:19.275	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3969 / 3969
2018-06-05 07:40:20.365	[P2P8]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584255 - 1588203 start at 6188 and end at 6203
2018-06-05 07:40:20.367	[P2P8]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3949 / 3949
2018-06-05 07:40:20.784	[P2P5]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584295 - 1588203 start at 6188 and end at 6203
2018-06-05 07:40:20.784	[P2P5]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3909 / 3909
2018-06-05 07:40:21.480	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584275 - 1588203 start at 6188 and end at 6203
2018-06-05 07:40:21.481	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3929 / 3929
2018-06-05 07:40:22.056	[P2P2]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584335 - 1588203 start at 6188 and end at 6203
2018-06-05 07:40:22.056	[P2P2]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3869 / 3869
2018-06-05 07:40:22.948	[P2P0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584355 - 1588203 start at 6188 and end at 6203
2018-06-05 07:40:22.948	[P2P0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3849 / 3849
2018-06-05 07:40:24.004	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584395 - 1588203 start at 6189 and end at 6203
2018-06-05 07:40:24.005	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3809 / 3809
2018-06-05 07:40:24.198	[P2P2]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584375 - 1588203 start at 6188 and end at 6203
2018-06-05 07:40:24.199	[P2P2]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3829 / 3829
2018-06-05 07:40:24.914	[P2P2]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584435 - 1588203 start at 6189 and end at 6203
2018-06-05 07:40:24.915	[P2P2]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3769 / 3769
2018-06-05 07:40:25.166	[P2P5]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584315 - 1588203 start at 6188 and end at 6203
2018-06-05 07:40:25.167	[P2P5]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3889 / 3889
2018-06-05 07:40:25.583	[P2P5]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584415 - 1588203 start at 6189 and end at 6203
2018-06-05 07:40:25.584	[P2P5]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3789 / 3789
2018-06-05 07:40:28.321	[P2P0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583940 - 1588203 start at 6187 and end at 6203
2018-06-05 07:40:28.322	[P2P0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4264 / 4264
2018-06-05 07:40:29.683	[P2P4]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583940 - 1588203 start at 6187 and end at 6203
2018-06-05 07:40:29.684	[P2P4]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4264 / 4264
2018-06-05 07:40:30.160	[P2P2]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583940 - 1588203 start at 6187 and end at 6203
2018-06-05 07:40:30.161	[P2P2]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4264 / 4264
2018-06-05 07:40:35.432	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584655 - 1588203 start at 6190 and end at 6203
2018-06-05 07:40:35.433	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3549 / 3549
2018-06-05 07:40:35.814	[P2P4]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583959 - 1588203 start at 6187 and end at 6203
2018-06-05 07:40:35.815	[P2P4]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4245 / 4245
2018-06-05 07:40:38.568	[P2P5]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583959 - 1588203 start at 6187 and end at 6203
2018-06-05 07:40:38.569	[P2P5]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4245 / 4245
2018-06-05 07:40:41.966	[P2P5]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583959 - 1588203 start at 6187 and end at 6203
2018-06-05 07:40:41.967	[P2P5]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4245 / 4245
2018-06-05 07:40:43.182	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583978 - 1588203 start at 6187 and end at 6203
2018-06-05 07:40:43.184	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4226 / 4226
2018-06-05 07:40:43.225	[P2P8]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583959 - 1588203 start at 6187 and end at 6203
2018-06-05 07:40:43.226	[P2P8]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4245 / 4245
2018-06-05 07:40:46.472	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583978 - 1588203 start at 6187 and end at 6203
2018-06-05 07:40:46.473	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4226 / 4226
2018-06-05 07:40:47.031	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1585598 - 1588203 start at 6193 and end at 6203
2018-06-05 07:40:47.031	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 2606 / 2606
2018-06-05 07:40:49.127	[P2P6]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583997 - 1588203 start at 6187 and end at 6203
2018-06-05 07:40:49.128	[P2P6]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4207 / 4207
2018-06-05 07:40:49.711	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1585618 - 1588203 start at 6193 and end at 6203
2018-06-05 07:40:49.712	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 2586 / 2586
2018-06-05 07:40:50.783	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1585578 - 1588203 start at 6193 and end at 6203
2018-06-05 07:40:50.784	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 2626 / 2626
2018-06-05 07:40:51.938	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1585638 - 1588203 start at 6193 and end at 6203
2018-06-05 07:40:51.938	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 2566 / 2566
2018-06-05 07:40:53.210	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1585678 - 1588203 start at 6194 and end at 6203
2018-06-05 07:40:53.210	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 2526 / 2526
2018-06-05 07:40:53.353	[P2P8]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1585698 - 1588203 start at 6194 and end at 6203
2018-06-05 07:40:53.354	[P2P8]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 2506 / 2506
2018-06-05 07:40:54.324	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1585738 - 1588204 start at 6194 and end at 6203
2018-06-05 07:40:54.324	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 2467 / 2467
2018-06-05 07:40:56.828	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1585758 - 1588204 start at 6194 and end at 6203
2018-06-05 07:40:56.828	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 2447 / 2447
2018-06-05 07:40:57.236	[P2P5]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1585798 - 1588204 start at 6194 and end at 6203
2018-06-05 07:40:57.236	[P2P5]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 2407 / 2407
2018-06-05 07:40:58.290	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1585778 - 1588204 start at 6194 and end at 6203
2018-06-05 07:40:58.291	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 2427 / 2427
2018-06-05 07:40:58.799	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1585718 - 1588204 start at 6194 and end at 6203
2018-06-05 07:40:58.799	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 2487 / 2487
2018-06-05 07:40:59.933	[P2P2]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1585818 - 1588204 start at 6194 and end at 6203
2018-06-05 07:40:59.933	[P2P2]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 2387 / 2387
2018-06-05 07:40:59.959	[P2P6]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1585658 - 1588204 start at 6193 and end at 6203
2018-06-05 07:40:59.959	[P2P6]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 2547 / 2547
2018-06-05 07:41:01.348	[P2P4]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1585838 - 1588205 start at 6194 and end at 6203
2018-06-05 07:41:01.348	[P2P4]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 2368 / 2368
2018-06-05 07:41:04.641	[P2P2]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1585858 - 1588205 start at 6194 and end at 6203
2018-06-05 07:41:04.641	[P2P2]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 2348 / 2348
2018-06-05 07:41:04.694	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1585898 - 1588205 start at 6194 and end at 6203
2018-06-05 07:41:04.695	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 2308 / 2308
2018-06-05 07:41:09.991	[P2P2]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1585978 - 1588205 start at 6195 and end at 6203
2018-06-05 07:41:09.991	[P2P2]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 2228 / 2228
2018-06-05 07:41:10.415	[P2P2]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1585938 - 1588205 start at 6195 and end at 6203
2018-06-05 07:41:10.415	[P2P2]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 2268 / 2268
2018-06-05 07:41:10.655	[P2P6]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1585958 - 1588205 start at 6195 and end at 6203
2018-06-05 07:41:10.655	[P2P6]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 2248 / 2248
2018-06-05 07:41:11.836	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1585918 - 1588205 start at 6194 and end at 6203
2018-06-05 07:41:11.836	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 2288 / 2288
2018-06-05 07:41:12.906	[P2P5]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1585878 - 1588205 start at 6194 and end at 6203
2018-06-05 07:41:12.907	[P2P5]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 2328 / 2328
2018-06-05 07:41:15.267	[P2P6]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1586018 - 1588205 start at 6195 and end at 6203
2018-06-05 07:41:15.267	[P2P6]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 2188 / 2188
2018-06-05 07:41:15.367	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1585998 - 1588205 start at 6195 and end at 6203
2018-06-05 07:41:15.367	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 2208 / 2208
2018-06-05 07:41:17.151	[P2P8]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583978 - 1588205 start at 6187 and end at 6203
2018-06-05 07:41:17.152	[P2P8]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4228 / 4228
2018-06-05 07:41:18.627	[P2P6]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1586058 - 1588205 start at 6195 and end at 6203
2018-06-05 07:41:18.627	[P2P6]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 2148 / 2148
2018-06-05 07:41:19.545	[P2P8]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1586118 - 1588205 start at 6195 and end at 6203
2018-06-05 07:41:19.545	[P2P8]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 2088 / 2088
2018-06-05 07:41:23.222	[P2P4]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1586038 - 1588205 start at 6195 and end at 6203
2018-06-05 07:41:23.222	[P2P4]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 2168 / 2168
2018-06-05 07:41:23.976	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1586158 - 1588205 start at 6195 and end at 6203
2018-06-05 07:41:23.976	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 2048 / 2048
2018-06-05 07:41:27.015	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1586098 - 1588205 start at 6195 and end at 6203
2018-06-05 07:41:27.015	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 2108 / 2108
2018-06-05 07:41:29.736	[P2P4]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583997 - 1588205 start at 6187 and end at 6203
2018-06-05 07:41:29.737	[P2P4]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4209 / 4209
2018-06-05 07:41:29.898	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1586078 - 1588205 start at 6195 and end at 6203
2018-06-05 07:41:29.898	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 2128 / 2128
2018-06-05 07:41:32.946	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1586138 - 1588205 start at 6195 and end at 6203
2018-06-05 07:41:32.946	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 2068 / 2068
2018-06-05 07:42:06.397	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584016 - 1588205 start at 6187 and end at 6203
2018-06-05 07:42:06.397	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4190 / 4190
2018-06-05 07:42:28.891	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584035 - 1588205 start at 6187 and end at 6203
2018-06-05 07:42:28.892	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4171 / 4171
2018-06-05 07:42:32.991	[P2P2]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584035 - 1588205 start at 6187 and end at 6203
2018-06-05 07:42:32.992	[P2P2]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4171 / 4171
2018-06-05 07:42:33.052	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584035 - 1588205 start at 6187 and end at 6203
2018-06-05 07:42:33.053	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4171 / 4171
2018-06-05 07:42:33.928	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584035 - 1588205 start at 6187 and end at 6203
2018-06-05 07:42:33.929	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4171 / 4171
2018-06-05 07:42:37.007	[P2P4]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584054 - 1588205 start at 6187 and end at 6203
2018-06-05 07:42:37.008	[P2P4]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4152 / 4152
2018-06-05 07:42:37.506	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584114 - 1588205 start at 6187 and end at 6203
2018-06-05 07:42:37.507	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4092 / 4092
2018-06-05 07:42:38.946	[P2P0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584073 - 1588205 start at 6187 and end at 6203
2018-06-05 07:42:38.947	[P2P0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4133 / 4133
2018-06-05 07:42:41.253	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584092 - 1588205 start at 6187 and end at 6203
2018-06-05 07:42:41.254	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4114 / 4114
2018-06-05 07:42:42.974	[P2P6]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584094 - 1588205 start at 6187 and end at 6203
2018-06-05 07:42:42.975	[P2P6]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4112 / 4112
2018-06-05 07:42:44.060	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584054 - 1588205 start at 6187 and end at 6203
2018-06-05 07:42:44.061	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4152 / 4152
2018-06-05 07:42:44.070	[P2P5]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584035 - 1588205 start at 6187 and end at 6203
2018-06-05 07:42:44.071	[P2P5]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4171 / 4171
2018-06-05 07:42:54.488	[P2P8]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584054 - 1588205 start at 6187 and end at 6203
2018-06-05 07:42:54.489	[P2P8]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4152 / 4152
2018-06-05 07:42:55.200	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584093 - 1588205 start at 6187 and end at 6203
2018-06-05 07:42:55.201	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4113 / 4113
2018-06-05 07:42:57.391	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584234 - 1588205 start at 6188 and end at 6203
2018-06-05 07:42:57.392	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3972 / 3972
2018-06-05 07:42:58.091	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584214 - 1588205 start at 6188 and end at 6203
2018-06-05 07:42:58.092	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3992 / 3992
2018-06-05 07:42:58.275	[P2P6]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584054 - 1588205 start at 6187 and end at 6203
2018-06-05 07:42:58.277	[P2P6]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4152 / 4152
2018-06-05 07:43:00.284	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584274 - 1588205 start at 6188 and end at 6203
2018-06-05 07:43:00.285	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3932 / 3932
2018-06-05 07:43:01.869	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584073 - 1588205 start at 6187 and end at 6203
2018-06-05 07:43:01.870	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4133 / 4133
2018-06-05 07:43:02.631	[P2P0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584314 - 1588205 start at 6188 and end at 6203
2018-06-05 07:43:02.632	[P2P0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3892 / 3892
2018-06-05 07:43:03.307	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584294 - 1588205 start at 6188 and end at 6203
2018-06-05 07:43:03.308	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3912 / 3912
2018-06-05 07:43:03.586	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584254 - 1588205 start at 6188 and end at 6203
2018-06-05 07:43:03.587	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3952 / 3952
2018-06-05 07:43:05.087	[P2P0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584334 - 1588205 start at 6188 and end at 6203
2018-06-05 07:43:05.088	[P2P0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3872 / 3872
2018-06-05 07:43:06.538	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584092 - 1588205 start at 6187 and end at 6203
2018-06-05 07:43:06.540	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4114 / 4114
2018-06-05 07:43:07.261	[P2P0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584394 - 1588205 start at 6189 and end at 6203
2018-06-05 07:43:07.262	[P2P0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3812 / 3812
2018-06-05 07:43:07.844	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584035 - 1588205 start at 6187 and end at 6203
2018-06-05 07:43:07.845	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4171 / 4171
2018-06-05 07:43:08.970	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584374 - 1588205 start at 6188 and end at 6203
2018-06-05 07:43:08.971	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3832 / 3832
2018-06-05 07:43:09.466	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584111 - 1588205 start at 6187 and end at 6203
2018-06-05 07:43:09.468	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4095 / 4095
2018-06-05 07:43:09.663	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584354 - 1588205 start at 6188 and end at 6203
2018-06-05 07:43:09.664	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3852 / 3852
2018-06-05 07:43:09.839	[P2P2]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584054 - 1588205 start at 6187 and end at 6203
2018-06-05 07:43:09.840	[P2P2]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4152 / 4152
2018-06-05 07:43:10.120	[P2P5]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584414 - 1588205 start at 6189 and end at 6203
2018-06-05 07:43:10.121	[P2P5]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3792 / 3792
2018-06-05 07:43:12.516	[P2P8]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584474 - 1588205 start at 6189 and end at 6203
2018-06-05 07:43:12.517	[P2P8]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3732 / 3732
2018-06-05 07:43:12.597	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584434 - 1588205 start at 6189 and end at 6203
2018-06-05 07:43:12.598	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3772 / 3772
2018-06-05 07:43:14.381	[P2P8]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584454 - 1588205 start at 6189 and end at 6203
2018-06-05 07:43:14.382	[P2P8]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3752 / 3752
2018-06-05 07:43:14.706	[P2P2]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584494 - 1588205 start at 6189 and end at 6203
2018-06-05 07:43:14.707	[P2P2]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3712 / 3712
2018-06-05 07:43:14.792	[P2P2]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584073 - 1588205 start at 6187 and end at 6203
2018-06-05 07:43:14.793	[P2P2]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4133 / 4133
2018-06-05 07:43:15.300	[P2P6]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584130 - 1588205 start at 6188 and end at 6203
2018-06-05 07:43:15.301	[P2P6]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4076 / 4076
2018-06-05 07:43:17.218	[P2P0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584534 - 1588205 start at 6189 and end at 6203
2018-06-05 07:43:17.219	[P2P0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3672 / 3672
2018-06-05 07:43:18.601	[P2P5]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584514 - 1588205 start at 6189 and end at 6203
2018-06-05 07:43:18.601	[P2P5]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3692 / 3692
2018-06-05 07:43:18.922	[P2P8]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584554 - 1588205 start at 6189 and end at 6203
2018-06-05 07:43:18.923	[P2P8]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3652 / 3652
2018-06-05 07:43:19.439	[P2P4]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584092 - 1588205 start at 6187 and end at 6203
2018-06-05 07:43:19.440	[P2P4]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4114 / 4114
2018-06-05 07:43:20.039	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584574 - 1588205 start at 6189 and end at 6203
2018-06-05 07:43:20.040	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3632 / 3632
2018-06-05 07:43:20.619	[P2P5]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584614 - 1588206 start at 6189 and end at 6203
2018-06-05 07:43:20.620	[P2P5]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3593 / 3593
2018-06-05 07:43:21.977	[P2P8]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584149 - 1588206 start at 6188 and end at 6203
2018-06-05 07:43:21.978	[P2P8]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4058 / 4058
2018-06-05 07:43:22.307	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584654 - 1588206 start at 6190 and end at 6203
2018-06-05 07:43:22.308	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3553 / 3553
2018-06-05 07:43:23.042	[P2P0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584634 - 1588206 start at 6189 and end at 6203
2018-06-05 07:43:23.042	[P2P0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3573 / 3573
2018-06-05 07:43:23.251	[P2P0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584111 - 1588206 start at 6187 and end at 6203
2018-06-05 07:43:23.252	[P2P0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4096 / 4096
2018-06-05 07:43:25.231	[P2P0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584674 - 1588206 start at 6190 and end at 6203
2018-06-05 07:43:25.231	[P2P0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3533 / 3533
2018-06-05 07:43:27.387	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584694 - 1588206 start at 6190 and end at 6203
2018-06-05 07:43:27.388	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3513 / 3513
2018-06-05 07:43:27.745	[P2P8]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584714 - 1588206 start at 6190 and end at 6203
2018-06-05 07:43:27.746	[P2P8]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3493 / 3493
2018-06-05 07:43:28.090	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584594 - 1588206 start at 6189 and end at 6203
2018-06-05 07:43:28.091	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3613 / 3613
2018-06-05 07:43:30.182	[P2P6]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584130 - 1588206 start at 6188 and end at 6203
2018-06-05 07:43:30.183	[P2P6]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4077 / 4077
2018-06-05 07:43:30.271	[P2P6]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584168 - 1588206 start at 6188 and end at 6203
2018-06-05 07:43:30.272	[P2P6]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4039 / 4039
2018-06-05 07:43:32.118	[P2P8]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584754 - 1588206 start at 6190 and end at 6203
2018-06-05 07:43:32.119	[P2P8]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3453 / 3453
2018-06-05 07:43:33.456	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584734 - 1588206 start at 6190 and end at 6203
2018-06-05 07:43:33.457	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3473 / 3473
2018-06-05 07:43:34.335	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584794 - 1588206 start at 6190 and end at 6203
2018-06-05 07:43:34.336	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3413 / 3413
2018-06-05 07:43:36.582	[P2P5]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584149 - 1588206 start at 6188 and end at 6203
2018-06-05 07:43:36.583	[P2P5]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4058 / 4058
2018-06-05 07:43:37.169	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584834 - 1588206 start at 6190 and end at 6203
2018-06-05 07:43:37.169	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3373 / 3373
2018-06-05 07:43:37.231	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584187 - 1588206 start at 6188 and end at 6203
2018-06-05 07:43:37.232	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4020 / 4020
2018-06-05 07:43:37.748	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584774 - 1588206 start at 6190 and end at 6203
2018-06-05 07:43:37.748	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3433 / 3433
2018-06-05 07:43:39.641	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584854 - 1588206 start at 6190 and end at 6203
2018-06-05 07:43:39.642	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3353 / 3353
2018-06-05 07:43:41.152	[P2P2]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584814 - 1588206 start at 6190 and end at 6203
2018-06-05 07:43:41.153	[P2P2]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3393 / 3393
2018-06-05 07:43:42.192	[P2P0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584894 - 1588206 start at 6190 and end at 6203
2018-06-05 07:43:42.193	[P2P0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3313 / 3313
2018-06-05 07:43:46.500	[P2P8]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584206 - 1588206 start at 6188 and end at 6203
2018-06-05 07:43:46.501	[P2P8]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4001 / 4001
2018-06-05 07:43:46.629	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584934 - 1588206 start at 6191 and end at 6203
2018-06-05 07:43:46.630	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3273 / 3273
2018-06-05 07:43:47.281	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584168 - 1588206 start at 6188 and end at 6203
2018-06-05 07:43:47.282	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4039 / 4039
2018-06-05 07:43:47.467	[P2P8]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584914 - 1588206 start at 6191 and end at 6203
2018-06-05 07:43:47.468	[P2P8]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3293 / 3293
2018-06-05 07:43:47.616	[P2P8]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584874 - 1588206 start at 6190 and end at 6203
2018-06-05 07:43:47.617	[P2P8]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3333 / 3333
2018-06-05 07:43:49.879	[P2P2]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584954 - 1588206 start at 6191 and end at 6203
2018-06-05 07:43:49.880	[P2P2]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3253 / 3253
2018-06-05 07:43:52.408	[P2P2]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584974 - 1588207 start at 6191 and end at 6203
2018-06-05 07:43:52.409	[P2P2]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3234 / 3234
2018-06-05 07:43:55.929	[P2P4]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1585014 - 1588207 start at 6191 and end at 6203
2018-06-05 07:43:55.929	[P2P4]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3194 / 3194
2018-06-05 07:43:56.489	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584225 - 1588207 start at 6188 and end at 6203
2018-06-05 07:43:56.490	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3983 / 3983
2018-06-05 07:43:56.674	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584187 - 1588207 start at 6188 and end at 6203
2018-06-05 07:43:56.675	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4021 / 4021
2018-06-05 07:43:57.146	[P2P2]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584054 - 1588207 start at 6187 and end at 6203
2018-06-05 07:43:57.147	[P2P2]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4154 / 4154
2018-06-05 07:43:57.187	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1585034 - 1588207 start at 6191 and end at 6203
2018-06-05 07:43:57.188	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3174 / 3174
2018-06-05 07:44:00.340	[P2P0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1585074 - 1588207 start at 6191 and end at 6203
2018-06-05 07:44:00.341	[P2P0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3134 / 3134
2018-06-05 07:44:03.803	[P2P8]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584994 - 1588207 start at 6191 and end at 6203
2018-06-05 07:44:03.804	[P2P8]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3214 / 3214
2018-06-05 07:44:04.223	[P2P8]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1585094 - 1588207 start at 6191 and end at 6203
2018-06-05 07:44:04.224	[P2P8]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3114 / 3114
2018-06-05 07:44:04.699	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584244 - 1588207 start at 6188 and end at 6203
2018-06-05 07:44:04.700	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3964 / 3964
2018-06-05 07:44:06.964	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584073 - 1588207 start at 6187 and end at 6203
2018-06-05 07:44:06.965	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4135 / 4135
2018-06-05 07:44:07.368	[P2P6]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1585054 - 1588207 start at 6191 and end at 6203
2018-06-05 07:44:07.368	[P2P6]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3154 / 3154
2018-06-05 07:44:09.761	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584092 - 1588207 start at 6187 and end at 6203
2018-06-05 07:44:09.762	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4116 / 4116
2018-06-05 07:44:11.053	[P2P6]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584206 - 1588207 start at 6188 and end at 6203
2018-06-05 07:44:11.054	[P2P6]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4002 / 4002
2018-06-05 07:44:11.180	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584263 - 1588207 start at 6188 and end at 6203
2018-06-05 07:44:11.181	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3945 / 3945
2018-06-05 07:44:12.002	[P2P5]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584111 - 1588207 start at 6187 and end at 6203
2018-06-05 07:44:12.003	[P2P5]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4097 / 4097
2018-06-05 07:44:12.485	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584092 - 1588207 start at 6187 and end at 6203
2018-06-05 07:44:12.487	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4116 / 4116
2018-06-05 07:44:13.824	[P2P2]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584073 - 1588207 start at 6187 and end at 6203
2018-06-05 07:44:13.825	[P2P2]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4135 / 4135
2018-06-05 07:44:14.774	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584282 - 1588207 start at 6188 and end at 6203
2018-06-05 07:44:14.775	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3926 / 3926
2018-06-05 07:44:23.262	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584073 - 1588208 start at 6187 and end at 6203
2018-06-05 07:44:23.263	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4136 / 4136
2018-06-05 07:44:24.046	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584092 - 1588208 start at 6187 and end at 6203
2018-06-05 07:44:24.047	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4117 / 4117
2018-06-05 07:44:24.792	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584092 - 1588208 start at 6187 and end at 6203
2018-06-05 07:44:24.793	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4117 / 4117
2018-06-05 07:44:25.483	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584092 - 1588208 start at 6187 and end at 6203
2018-06-05 07:44:25.485	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4117 / 4117
2018-06-05 07:44:25.736	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584092 - 1588208 start at 6187 and end at 6203
2018-06-05 07:44:25.737	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4117 / 4117
2018-06-05 07:44:26.335	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584092 - 1588208 start at 6187 and end at 6203
2018-06-05 07:44:26.336	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4117 / 4117
2018-06-05 07:44:28.200	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584285 - 1588208 start at 6188 and end at 6203
2018-06-05 07:44:28.201	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3924 / 3924
2018-06-05 07:44:29.328	[P2P8]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584265 - 1588208 start at 6188 and end at 6203
2018-06-05 07:44:29.329	[P2P8]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3944 / 3944
2018-06-05 07:44:30.573	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584361 - 1588208 start at 6188 and end at 6203
2018-06-05 07:44:30.574	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3848 / 3848
2018-06-05 07:44:30.692	[P2P4]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584210 - 1588208 start at 6188 and end at 6203
2018-06-05 07:44:30.693	[P2P4]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3999 / 3999
2018-06-05 07:44:35.455	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584190 - 1588208 start at 6188 and end at 6203
2018-06-05 07:44:35.456	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4019 / 4019
2018-06-05 07:44:35.543	[P2P0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584190 - 1588208 start at 6188 and end at 6203
2018-06-05 07:44:35.544	[P2P0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4019 / 4019
2018-06-05 07:44:36.380	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584190 - 1588208 start at 6188 and end at 6203
2018-06-05 07:44:36.381	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4019 / 4019
2018-06-05 07:44:38.536	[P2P4]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584190 - 1588208 start at 6188 and end at 6203
2018-06-05 07:44:38.537	[P2P4]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4019 / 4019
2018-06-05 07:44:39.589	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584190 - 1588208 start at 6188 and end at 6203
2018-06-05 07:44:39.590	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4019 / 4019
2018-06-05 07:44:40.694	[P2P5]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584481 - 1588208 start at 6189 and end at 6203
2018-06-05 07:44:40.695	[P2P5]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3728 / 3728
2018-06-05 07:44:40.860	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584209 - 1588208 start at 6188 and end at 6203
2018-06-05 07:44:40.861	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4000 / 4000
2018-06-05 07:44:42.455	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584461 - 1588208 start at 6189 and end at 6203
2018-06-05 07:44:42.456	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3748 / 3748
2018-06-05 07:44:42.855	[P2P6]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584501 - 1588208 start at 6189 and end at 6203
2018-06-05 07:44:42.856	[P2P6]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3708 / 3708
2018-06-05 07:44:44.263	[P2P2]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584521 - 1588208 start at 6189 and end at 6203
2018-06-05 07:44:44.264	[P2P2]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3688 / 3688
2018-06-05 07:44:45.791	[P2P0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584581 - 1588208 start at 6189 and end at 6203
2018-06-05 07:44:45.792	[P2P0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3628 / 3628
2018-06-05 07:44:47.624	[P2P0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584621 - 1588208 start at 6189 and end at 6203
2018-06-05 07:44:47.625	[P2P0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3588 / 3588
2018-06-05 07:44:48.248	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584541 - 1588208 start at 6189 and end at 6203
2018-06-05 07:44:48.249	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3668 / 3668
2018-06-05 07:44:48.270	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584561 - 1588208 start at 6189 and end at 6203
2018-06-05 07:44:48.271	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3648 / 3648
2018-06-05 07:44:49.065	[P2P0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584641 - 1588208 start at 6190 and end at 6203
2018-06-05 07:44:49.065	[P2P0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3568 / 3568
2018-06-05 07:44:50.114	[P2P8]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584601 - 1588208 start at 6189 and end at 6203
2018-06-05 07:44:50.115	[P2P8]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3608 / 3608
2018-06-05 07:44:52.347	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584721 - 1588208 start at 6190 and end at 6203
2018-06-05 07:44:52.348	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3488 / 3488
2018-06-05 07:44:52.633	[P2P8]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584681 - 1588208 start at 6190 and end at 6203
2018-06-05 07:44:52.634	[P2P8]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3528 / 3528
2018-06-05 07:44:53.226	[P2P0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584661 - 1588208 start at 6190 and end at 6203
2018-06-05 07:44:53.227	[P2P0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3548 / 3548
2018-06-05 07:44:54.714	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584190 - 1588208 start at 6188 and end at 6203
2018-06-05 07:44:54.715	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4019 / 4019
2018-06-05 07:44:55.392	[P2P0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584781 - 1588208 start at 6190 and end at 6203
2018-06-05 07:44:55.393	[P2P0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3428 / 3428
2018-06-05 07:44:57.141	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584741 - 1588208 start at 6190 and end at 6203
2018-06-05 07:44:57.142	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3468 / 3468
2018-06-05 07:44:58.486	[P2P8]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584761 - 1588208 start at 6190 and end at 6203
2018-06-05 07:44:58.487	[P2P8]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3448 / 3448
2018-06-05 07:44:58.987	[P2P8]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584821 - 1588208 start at 6190 and end at 6203
2018-06-05 07:44:58.988	[P2P8]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3388 / 3388
2018-06-05 07:44:59.019	[P2P2]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584701 - 1588208 start at 6190 and end at 6203
2018-06-05 07:44:59.020	[P2P2]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3508 / 3508
2018-06-05 07:45:01.392	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584861 - 1588208 start at 6190 and end at 6203
2018-06-05 07:45:01.393	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3348 / 3348
2018-06-05 07:45:03.670	[P2P0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584801 - 1588208 start at 6190 and end at 6203
2018-06-05 07:45:03.670	[P2P0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3408 / 3408
2018-06-05 07:45:04.193	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584881 - 1588208 start at 6190 and end at 6203
2018-06-05 07:45:04.193	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3328 / 3328
2018-06-05 07:45:04.378	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584841 - 1588208 start at 6190 and end at 6203
2018-06-05 07:45:04.379	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3368 / 3368
2018-06-05 07:45:04.632	[P2P2]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584921 - 1588208 start at 6191 and end at 6203
2018-06-05 07:45:04.633	[P2P2]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3288 / 3288
2018-06-05 07:45:04.876	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584901 - 1588208 start at 6191 and end at 6203
2018-06-05 07:45:04.877	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3308 / 3308
2018-06-05 07:45:07.656	[P2P6]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584961 - 1588208 start at 6191 and end at 6203
2018-06-05 07:45:07.657	[P2P6]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3248 / 3248
2018-06-05 07:45:09.634	[P2P8]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584209 - 1588208 start at 6188 and end at 6203
2018-06-05 07:45:09.636	[P2P8]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4000 / 4000
2018-06-05 07:45:10.095	[P2P2]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584209 - 1588208 start at 6188 and end at 6203
2018-06-05 07:45:10.096	[P2P2]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4000 / 4000
2018-06-05 07:45:11.556	[P2P2]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584981 - 1588208 start at 6191 and end at 6203
2018-06-05 07:45:11.556	[P2P2]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3228 / 3228
2018-06-05 07:45:12.464	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584941 - 1588208 start at 6191 and end at 6203
2018-06-05 07:45:12.465	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3268 / 3268
2018-06-05 07:45:12.897	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584209 - 1588208 start at 6188 and end at 6203
2018-06-05 07:45:12.898	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4000 / 4000
2018-06-05 07:45:12.987	[P2P5]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584228 - 1588208 start at 6188 and end at 6203
2018-06-05 07:45:12.988	[P2P5]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3981 / 3981
2018-06-05 07:45:16.158	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584209 - 1588208 start at 6188 and end at 6203
2018-06-05 07:45:16.159	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4000 / 4000
2018-06-05 07:45:19.537	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584228 - 1588208 start at 6188 and end at 6203
2018-06-05 07:45:19.538	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3981 / 3981
2018-06-05 07:45:20.031	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584228 - 1588208 start at 6188 and end at 6203
2018-06-05 07:45:20.032	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3981 / 3981
2018-06-05 07:45:20.189	[P2P5]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584328 - 1588208 start at 6188 and end at 6203
2018-06-05 07:45:20.190	[P2P5]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3881 / 3881
2018-06-05 07:45:20.238	[P2P4]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584308 - 1588208 start at 6188 and end at 6203
2018-06-05 07:45:20.239	[P2P4]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3901 / 3901
2018-06-05 07:45:23.156	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1581880 - 1588208 start at 6179 and end at 6203
2018-06-05 07:45:23.157	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 6329 / 6329
2018-06-05 07:45:26.006	[P2P5]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584247 - 1588208 start at 6188 and end at 6203
2018-06-05 07:45:26.007	[P2P5]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3962 / 3962
2018-06-05 07:45:27.843	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584428 - 1588208 start at 6189 and end at 6203
2018-06-05 07:45:27.844	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3781 / 3781
2018-06-05 07:45:28.035	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584288 - 1588208 start at 6188 and end at 6203
2018-06-05 07:45:28.036	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3921 / 3921
2018-06-05 07:45:30.703	[P2P2]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584266 - 1588208 start at 6188 and end at 6203
2018-06-05 07:45:30.704	[P2P2]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3943 / 3943
2018-06-05 07:45:31.157	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584488 - 1588208 start at 6189 and end at 6203
2018-06-05 07:45:31.158	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3721 / 3721
2018-06-05 07:45:32.905	[P2P8]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584285 - 1588208 start at 6188 and end at 6203
2018-06-05 07:45:32.906	[P2P8]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3924 / 3924
2018-06-05 07:45:33.416	[P2P6]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584508 - 1588208 start at 6189 and end at 6203
2018-06-05 07:45:33.417	[P2P6]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3701 / 3701
2018-06-05 07:45:35.099	[P2P6]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584304 - 1588208 start at 6188 and end at 6203
2018-06-05 07:45:35.100	[P2P6]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3905 / 3905
2018-06-05 07:45:38.713	[P2P4]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584307 - 1588208 start at 6188 and end at 6203
2018-06-05 07:45:38.714	[P2P4]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3902 / 3902
2018-06-05 07:45:38.961	[P2P6]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584548 - 1588208 start at 6189 and end at 6203
2018-06-05 07:45:38.962	[P2P6]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3661 / 3661
2018-06-05 07:45:40.137	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584307 - 1588208 start at 6188 and end at 6203
2018-06-05 07:45:40.138	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3902 / 3902
2018-06-05 07:45:40.679	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584307 - 1588208 start at 6188 and end at 6203
2018-06-05 07:45:40.680	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3902 / 3902
2018-06-05 07:45:40.689	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1581880 - 1587298 start at 6179 and end at 6200
2018-06-05 07:45:40.691	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5419 / 5419
2018-06-05 07:45:41.069	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584326 - 1588208 start at 6188 and end at 6203
2018-06-05 07:45:41.070	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3883 / 3883
2018-06-05 07:45:47.078	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584326 - 1588208 start at 6188 and end at 6203
2018-06-05 07:45:47.079	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3883 / 3883
2018-06-05 07:45:47.240	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584708 - 1588208 start at 6190 and end at 6203
2018-06-05 07:45:47.241	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3501 / 3501
2018-06-05 07:45:47.428	[P2P4]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584688 - 1588208 start at 6190 and end at 6203
2018-06-05 07:45:47.429	[P2P4]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3521 / 3521
2018-06-05 07:45:47.831	[P2P6]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584307 - 1588208 start at 6188 and end at 6203
2018-06-05 07:45:47.832	[P2P6]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3902 / 3902
2018-06-05 07:45:48.860	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584728 - 1588208 start at 6190 and end at 6203
2018-06-05 07:45:48.860	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3481 / 3481
2018-06-05 07:45:57.565	[P2P2]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584326 - 1588208 start at 6188 and end at 6203
2018-06-05 07:45:57.566	[P2P2]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3883 / 3883
2018-06-05 07:45:57.733	[P2P6]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584326 - 1588208 start at 6188 and end at 6203
2018-06-05 07:45:57.733	[P2P6]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3883 / 3883
2018-06-05 07:45:58.953	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584365 - 1588208 start at 6188 and end at 6203
2018-06-05 07:45:58.954	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3844 / 3844
2018-06-05 07:45:59.856	[P2P6]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584326 - 1588208 start at 6188 and end at 6203
2018-06-05 07:45:59.857	[P2P6]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3883 / 3883
2018-06-05 07:46:00.146	[P2P4]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1585138 - 1588208 start at 6191 and end at 6203
2018-06-05 07:46:00.146	[P2P4]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3071 / 3071
2018-06-05 07:46:02.333	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584385 - 1588208 start at 6189 and end at 6203
2018-06-05 07:46:02.334	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3824 / 3824
2018-06-05 07:46:03.571	[P2P8]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584345 - 1588208 start at 6188 and end at 6203
2018-06-05 07:46:03.572	[P2P8]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3864 / 3864
2018-06-05 07:46:03.634	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1585238 - 1588208 start at 6192 and end at 6203
2018-06-05 07:46:03.634	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 2971 / 2971
2018-06-05 07:46:05.602	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1585198 - 1588208 start at 6192 and end at 6203
2018-06-05 07:46:05.602	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3011 / 3011
2018-06-05 07:46:05.935	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1585338 - 1588208 start at 6192 and end at 6203
2018-06-05 07:46:05.935	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 2871 / 2871
2018-06-05 07:46:07.418	[P2P2]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584364 - 1588208 start at 6188 and end at 6203
2018-06-05 07:46:07.419	[P2P2]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3845 / 3845
2018-06-05 07:46:07.865	[P2P2]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1585298 - 1588208 start at 6192 and end at 6203
2018-06-05 07:46:07.866	[P2P2]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 2911 / 2911
2018-06-05 07:46:07.896	[P2P5]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1585458 - 1588208 start at 6193 and end at 6203
2018-06-05 07:46:07.896	[P2P5]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 2751 / 2751
2018-06-05 07:46:10.528	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1581880 - 1588208 start at 6179 and end at 6203
2018-06-05 07:46:10.530	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 6329 / 6329
2018-06-05 07:46:10.970	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584383 - 1588208 start at 6188 and end at 6203
2018-06-05 07:46:10.971	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3826 / 3826
2018-06-05 07:46:11.333	[P2P6]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1585658 - 1588208 start at 6193 and end at 6203
2018-06-05 07:46:11.333	[P2P6]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 2551 / 2551
2018-06-05 07:46:11.437	[P2P2]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1585538 - 1588208 start at 6193 and end at 6203
2018-06-05 07:46:11.437	[P2P2]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 2671 / 2671
2018-06-05 07:46:14.036	[P2P8]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1586058 - 1588208 start at 6195 and end at 6203
2018-06-05 07:46:14.036	[P2P8]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 2151 / 2151
2018-06-05 07:46:14.586	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1585918 - 1588208 start at 6194 and end at 6203
2018-06-05 07:46:14.586	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 2291 / 2291
2018-06-05 07:46:14.646	[P2P8]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1585398 - 1588208 start at 6192 and end at 6203
2018-06-05 07:46:14.647	[P2P8]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 2811 / 2811
2018-06-05 07:46:14.721	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584402 - 1588208 start at 6189 and end at 6203
2018-06-05 07:46:14.722	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3807 / 3807
2018-06-05 07:46:17.718	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1586138 - 1588208 start at 6195 and end at 6203
2018-06-05 07:46:17.718	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 2071 / 2071
2018-06-05 07:46:18.581	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584421 - 1588208 start at 6189 and end at 6203
2018-06-05 07:46:18.582	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3788 / 3788
2018-06-05 07:46:20.942	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1581880 - 1588208 start at 6179 and end at 6203
2018-06-05 07:46:20.945	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 6329 / 6329
2018-06-05 07:46:22.044	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584440 - 1588208 start at 6189 and end at 6203
2018-06-05 07:46:22.045	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3769 / 3769
2018-06-05 07:46:26.511	[P2P0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584326 - 1588208 start at 6188 and end at 6203
2018-06-05 07:46:26.512	[P2P0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3883 / 3883
2018-06-05 07:46:28.026	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584459 - 1588208 start at 6189 and end at 6203
2018-06-05 07:46:28.027	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3750 / 3750
2018-06-05 07:46:31.793	[P2P2]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584345 - 1588208 start at 6188 and end at 6203
2018-06-05 07:46:31.794	[P2P2]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3864 / 3864
2018-06-05 07:46:31.822	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584478 - 1588208 start at 6189 and end at 6203
2018-06-05 07:46:31.822	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3731 / 3731
2018-06-05 07:46:34.795	[P2P0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584364 - 1588208 start at 6188 and end at 6203
2018-06-05 07:46:34.796	[P2P0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3845 / 3845
2018-06-05 07:46:34.823	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584497 - 1588208 start at 6189 and end at 6203
2018-06-05 07:46:34.824	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3712 / 3712
2018-06-05 07:46:38.697	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584383 - 1588208 start at 6188 and end at 6203
2018-06-05 07:46:38.698	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3826 / 3826
2018-06-05 07:46:38.799	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584516 - 1588208 start at 6189 and end at 6203
2018-06-05 07:46:38.800	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3693 / 3693
2018-06-05 07:46:42.827	[P2P6]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584535 - 1588208 start at 6189 and end at 6203
2018-06-05 07:46:42.828	[P2P6]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3674 / 3674
2018-06-05 07:46:46.902	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584402 - 1588208 start at 6189 and end at 6203
2018-06-05 07:46:46.902	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3807 / 3807
2018-06-05 07:46:49.939	[P2P8]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584554 - 1588208 start at 6189 and end at 6203
2018-06-05 07:46:49.939	[P2P8]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3655 / 3655
2018-06-05 07:46:53.027	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584573 - 1588208 start at 6189 and end at 6203
2018-06-05 07:46:53.027	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3636 / 3636
2018-06-05 07:46:53.739	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3006	lo 0.000181148386, qlo 0.000181150000, mask 10000
2018-06-05 07:46:53.739	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3030	Using 0.000181150000/kB fee
2018-06-05 07:46:53.984	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584421 - 1588208 start at 6189 and end at 6203
2018-06-05 07:46:53.985	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3788 / 3788
2018-06-05 07:46:54.383	[P2P6]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3006	lo 0.000181148386, qlo 0.000181150000, mask 10000
2018-06-05 07:46:54.383	[P2P6]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3030	Using 0.000181150000/kB fee
2018-06-05 07:46:56.511	[P2P2]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584592 - 1588208 start at 6189 and end at 6203
2018-06-05 07:46:56.512	[P2P2]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3617 / 3617
2018-06-05 07:46:56.770	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584345 - 1588208 start at 6188 and end at 6203
2018-06-05 07:46:56.771	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3864 / 3864
2018-06-05 07:47:00.861	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584440 - 1588208 start at 6189 and end at 6203
2018-06-05 07:47:00.861	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3769 / 3769
2018-06-05 07:47:03.163	[P2P8]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584611 - 1588208 start at 6189 and end at 6203
2018-06-05 07:47:03.163	[P2P8]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3598 / 3598
2018-06-05 07:47:07.298	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584630 - 1588208 start at 6189 and end at 6203
2018-06-05 07:47:07.299	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3579 / 3579
2018-06-05 07:47:07.578	[P2P4]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584459 - 1588208 start at 6189 and end at 6203
2018-06-05 07:47:07.579	[P2P4]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3750 / 3750
2018-06-05 07:47:10.212	[P2P2]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584649 - 1588208 start at 6190 and end at 6203
2018-06-05 07:47:10.213	[P2P2]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3560 / 3560
2018-06-05 07:47:11.222	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584478 - 1588208 start at 6189 and end at 6203
2018-06-05 07:47:11.223	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3731 / 3731
2018-06-05 07:47:13.611	[P2P4]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584497 - 1588208 start at 6189 and end at 6203
2018-06-05 07:47:13.612	[P2P4]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3712 / 3712
2018-06-05 07:47:14.455	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584364 - 1588208 start at 6188 and end at 6203
2018-06-05 07:47:14.455	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3845 / 3845
2018-06-05 07:47:15.124	[P2P2]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584668 - 1588208 start at 6190 and end at 6203
2018-06-05 07:47:15.125	[P2P2]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3541 / 3541
2018-06-05 07:47:17.179	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584516 - 1588208 start at 6189 and end at 6203
2018-06-05 07:47:17.180	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3693 / 3693
2018-06-05 07:47:17.590	[P2P6]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1581880 - 1587298 start at 6179 and end at 6200
2018-06-05 07:47:17.593	[P2P6]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5419 / 5419
2018-06-05 07:47:18.711	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1581880 - 1588208 start at 6179 and end at 6203
2018-06-05 07:47:18.714	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 6329 / 6329
2018-06-05 07:47:19.065	[P2P0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584687 - 1588208 start at 6190 and end at 6203
2018-06-05 07:47:19.066	[P2P0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3522 / 3522
2018-06-05 07:47:19.786	[P2P0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1581880 - 1588208 start at 6179 and end at 6203
2018-06-05 07:47:19.788	[P2P0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 6329 / 6329
2018-06-05 07:47:20.366	[P2P8]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584535 - 1588208 start at 6189 and end at 6203
2018-06-05 07:47:20.367	[P2P8]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3674 / 3674
2018-06-05 07:47:21.502	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584706 - 1588208 start at 6190 and end at 6203
2018-06-05 07:47:21.503	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3503 / 3503
2018-06-05 07:47:23.029	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1581921 - 1588208 start at 6179 and end at 6203
2018-06-05 07:47:23.031	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 6288 / 6288
2018-06-05 07:47:24.173	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584725 - 1588208 start at 6190 and end at 6203
2018-06-05 07:47:24.174	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3484 / 3484
2018-06-05 07:47:25.970	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1581940 - 1588208 start at 6179 and end at 6203
2018-06-05 07:47:25.972	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 6269 / 6269
2018-06-05 07:47:26.198	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584554 - 1588208 start at 6189 and end at 6203
2018-06-05 07:47:26.199	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3655 / 3655
2018-06-05 07:47:28.038	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1581959 - 1588208 start at 6179 and end at 6203
2018-06-05 07:47:28.040	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 6250 / 6250
2018-06-05 07:47:28.538	[P2P2]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584744 - 1588208 start at 6190 and end at 6203
2018-06-05 07:47:28.539	[P2P2]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3465 / 3465
2018-06-05 07:47:29.019	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584573 - 1588208 start at 6189 and end at 6203
2018-06-05 07:47:29.020	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3636 / 3636
2018-06-05 07:47:30.725	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1581978 - 1588208 start at 6179 and end at 6203
2018-06-05 07:47:30.728	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 6231 / 6231
2018-06-05 07:47:32.224	[P2P2]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584592 - 1588208 start at 6189 and end at 6203
2018-06-05 07:47:32.225	[P2P2]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3617 / 3617
2018-06-05 07:47:32.573	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584383 - 1588208 start at 6188 and end at 6203
2018-06-05 07:47:32.573	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3826 / 3826
2018-06-05 07:47:33.317	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1581997 - 1588208 start at 6179 and end at 6203
2018-06-05 07:47:33.319	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 6212 / 6212
2018-06-05 07:47:33.812	[P2P6]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584763 - 1588208 start at 6190 and end at 6203
2018-06-05 07:47:33.813	[P2P6]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3446 / 3446
2018-06-05 07:47:34.588	[P2P5]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584611 - 1588208 start at 6189 and end at 6203
2018-06-05 07:47:34.589	[P2P5]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3598 / 3598
2018-06-05 07:47:36.265	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584782 - 1588208 start at 6190 and end at 6203
2018-06-05 07:47:36.266	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3427 / 3427
2018-06-05 07:47:36.612	[P2P2]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582016 - 1588208 start at 6179 and end at 6203
2018-06-05 07:47:36.614	[P2P2]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 6193 / 6193
2018-06-05 07:47:36.856	[P2P5]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584630 - 1588208 start at 6189 and end at 6203
2018-06-05 07:47:36.857	[P2P5]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3579 / 3579
2018-06-05 07:47:38.566	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584649 - 1588208 start at 6190 and end at 6203
2018-06-05 07:47:38.567	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3560 / 3560
2018-06-05 07:47:38.921	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582035 - 1588208 start at 6179 and end at 6203
2018-06-05 07:47:38.923	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 6174 / 6174
2018-06-05 07:47:40.508	[P2P5]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584801 - 1588208 start at 6190 and end at 6203
2018-06-05 07:47:40.509	[P2P5]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3408 / 3408
2018-06-05 07:47:40.884	[P2P2]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584668 - 1588208 start at 6190 and end at 6203
2018-06-05 07:47:40.884	[P2P2]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3541 / 3541
2018-06-05 07:47:41.544	[P2P0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582054 - 1588208 start at 6179 and end at 6203
2018-06-05 07:47:41.546	[P2P0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 6155 / 6155
2018-06-05 07:47:43.712	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584687 - 1588208 start at 6190 and end at 6203
2018-06-05 07:47:43.713	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3522 / 3522
2018-06-05 07:47:43.756	[P2P0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584820 - 1588208 start at 6190 and end at 6203
2018-06-05 07:47:43.757	[P2P0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3389 / 3389
2018-06-05 07:47:44.369	[P2P5]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582073 - 1588208 start at 6179 and end at 6203
2018-06-05 07:47:44.371	[P2P5]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 6136 / 6136
2018-06-05 07:47:46.205	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584706 - 1588209 start at 6190 and end at 6203
2018-06-05 07:47:46.205	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3504 / 3504
2018-06-05 07:47:46.322	[P2P6]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582092 - 1588209 start at 6180 and end at 6203
2018-06-05 07:47:46.323	[P2P6]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 6118 / 6118
2018-06-05 07:47:46.793	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584839 - 1588209 start at 6190 and end at 6203
2018-06-05 07:47:46.793	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3371 / 3371
2018-06-05 07:47:48.169	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582111 - 1588209 start at 6180 and end at 6203
2018-06-05 07:47:48.171	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 6099 / 6099
2018-06-05 07:47:48.578	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584725 - 1588209 start at 6190 and end at 6203
2018-06-05 07:47:48.578	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3485 / 3485
2018-06-05 07:47:50.758	[P2P5]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582130 - 1588209 start at 6180 and end at 6203
2018-06-05 07:47:50.760	[P2P5]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 6080 / 6080
2018-06-05 07:47:51.270	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584402 - 1588209 start at 6189 and end at 6203
2018-06-05 07:47:51.270	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3808 / 3808
2018-06-05 07:47:52.286	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584744 - 1588209 start at 6190 and end at 6203
2018-06-05 07:47:52.287	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3466 / 3466
2018-06-05 07:47:52.293	[P2P8]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582130 - 1588209 start at 6180 and end at 6203
2018-06-05 07:47:52.294	[P2P8]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 6080 / 6080
2018-06-05 07:47:54.685	[P2P0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582149 - 1588209 start at 6180 and end at 6203
2018-06-05 07:47:54.687	[P2P0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 6061 / 6061
2018-06-05 07:47:58.179	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582168 - 1588209 start at 6180 and end at 6203
2018-06-05 07:47:58.181	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 6042 / 6042
2018-06-05 07:47:59.112	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582189 - 1588209 start at 6180 and end at 6203
2018-06-05 07:47:59.113	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 6021 / 6021
2018-06-05 07:47:59.554	[P2P0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584783 - 1588209 start at 6190 and end at 6203
2018-06-05 07:47:59.554	[P2P0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3427 / 3427
2018-06-05 07:48:03.563	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582208 - 1588209 start at 6180 and end at 6203
2018-06-05 07:48:03.565	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 6002 / 6002
2018-06-05 07:48:03.587	[P2P6]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582208 - 1588209 start at 6180 and end at 6203
2018-06-05 07:48:03.589	[P2P6]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 6002 / 6002
2018-06-05 07:48:04.003	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1581880 - 1588209 start at 6179 and end at 6203
2018-06-05 07:48:04.005	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 6330 / 6330
2018-06-05 07:48:04.012	[P2P8]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584803 - 1588209 start at 6190 and end at 6203
2018-06-05 07:48:04.012	[P2P8]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3407 / 3407
2018-06-05 07:48:04.194	[P2P0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1581880 - 1587298 start at 6179 and end at 6200
2018-06-05 07:48:04.195	[P2P0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5419 / 5419
2018-06-05 07:48:08.803	[P2P4]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1581941 - 1587298 start at 6179 and end at 6200
2018-06-05 07:48:08.805	[P2P4]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5358 / 5358
2018-06-05 07:48:08.837	[P2P4]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582247 - 1588209 start at 6180 and end at 6203
2018-06-05 07:48:08.839	[P2P4]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5963 / 5963
2018-06-05 07:48:09.201	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582267 - 1588209 start at 6180 and end at 6203
2018-06-05 07:48:09.202	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5943 / 5943
2018-06-05 07:48:10.813	[P2P2]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584843 - 1588209 start at 6190 and end at 6203
2018-06-05 07:48:10.814	[P2P2]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3367 / 3367
2018-06-05 07:48:10.949	[P2P0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1581960 - 1587298 start at 6179 and end at 6200
2018-06-05 07:48:10.951	[P2P0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5339 / 5339
2018-06-05 07:48:11.598	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1581880 - 1588209 start at 6179 and end at 6203
2018-06-05 07:48:11.600	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 6330 / 6330
2018-06-05 07:48:13.221	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1581979 - 1587298 start at 6179 and end at 6200
2018-06-05 07:48:13.223	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5320 / 5320
2018-06-05 07:48:14.571	[P2P2]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582287 - 1588209 start at 6180 and end at 6203
2018-06-05 07:48:14.573	[P2P2]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5923 / 5923
2018-06-05 07:48:15.340	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582307 - 1588209 start at 6180 and end at 6203
2018-06-05 07:48:15.341	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5903 / 5903
2018-06-05 07:48:16.279	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1581998 - 1587298 start at 6179 and end at 6200
2018-06-05 07:48:16.281	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5301 / 5301
2018-06-05 07:48:18.217	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584441 - 1588209 start at 6189 and end at 6203
2018-06-05 07:48:18.218	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3769 / 3769
2018-06-05 07:48:20.753	[P2P2]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582017 - 1587298 start at 6179 and end at 6200
2018-06-05 07:48:20.755	[P2P2]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5282 / 5282
2018-06-05 07:48:22.267	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582327 - 1588209 start at 6180 and end at 6203
2018-06-05 07:48:22.269	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5883 / 5883
2018-06-05 07:48:23.633	[P2P4]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582036 - 1587298 start at 6179 and end at 6200
2018-06-05 07:48:23.635	[P2P4]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5263 / 5263
2018-06-05 07:48:25.903	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582346 - 1588209 start at 6181 and end at 6203
2018-06-05 07:48:25.905	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5864 / 5864
2018-06-05 07:48:26.195	[P2P2]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582055 - 1587298 start at 6179 and end at 6200
2018-06-05 07:48:26.196	[P2P2]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5244 / 5244
2018-06-05 07:48:27.352	[P2P8]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582387 - 1588209 start at 6181 and end at 6203
2018-06-05 07:48:27.354	[P2P8]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5823 / 5823
2018-06-05 07:48:28.680	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582074 - 1587298 start at 6179 and end at 6200
2018-06-05 07:48:28.682	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5225 / 5225
2018-06-05 07:48:29.663	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582407 - 1588209 start at 6181 and end at 6203
2018-06-05 07:48:29.664	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5803 / 5803
2018-06-05 07:48:30.619	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582093 - 1587298 start at 6180 and end at 6200
2018-06-05 07:48:30.621	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5206 / 5206
2018-06-05 07:48:30.641	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582427 - 1588209 start at 6181 and end at 6203
2018-06-05 07:48:30.643	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5783 / 5783
2018-06-05 07:48:32.736	[P2P5]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582112 - 1587298 start at 6180 and end at 6200
2018-06-05 07:48:32.737	[P2P5]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5187 / 5187
2018-06-05 07:48:34.423	[P2P2]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582467 - 1588209 start at 6181 and end at 6203
2018-06-05 07:48:34.425	[P2P2]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5743 / 5743
2018-06-05 07:48:36.120	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582447 - 1588209 start at 6181 and end at 6203
2018-06-05 07:48:36.122	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5763 / 5763
2018-06-05 07:48:36.331	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582131 - 1587298 start at 6180 and end at 6200
2018-06-05 07:48:36.333	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5168 / 5168
2018-06-05 07:48:38.897	[P2P6]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1581880 - 1588209 start at 6179 and end at 6203
2018-06-05 07:48:38.900	[P2P6]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 6330 / 6330
2018-06-05 07:48:39.536	[P2P4]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582487 - 1588210 start at 6181 and end at 6203
2018-06-05 07:48:39.538	[P2P4]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5724 / 5724
2018-06-05 07:48:46.865	[P2P4]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582507 - 1588210 start at 6181 and end at 6203
2018-06-05 07:48:46.867	[P2P4]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5704 / 5704
2018-06-05 07:48:47.112	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582150 - 1587298 start at 6180 and end at 6200
2018-06-05 07:48:47.114	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5149 / 5149
2018-06-05 07:48:48.188	[P2P0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582527 - 1588210 start at 6181 and end at 6203
2018-06-05 07:48:48.190	[P2P0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5684 / 5684
2018-06-05 07:48:51.762	[P2P4]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584461 - 1588210 start at 6189 and end at 6203
2018-06-05 07:48:51.762	[P2P4]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3750 / 3750
2018-06-05 07:48:53.907	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582547 - 1588210 start at 6181 and end at 6203
2018-06-05 07:48:53.908	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5664 / 5664
2018-06-05 07:48:56.267	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582169 - 1587298 start at 6180 and end at 6200
2018-06-05 07:48:56.268	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5130 / 5130
2018-06-05 07:49:02.686	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582567 - 1588211 start at 6181 and end at 6203
2018-06-05 07:49:02.687	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5645 / 5645
2018-06-05 07:49:03.595	[P2P8]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582587 - 1588211 start at 6181 and end at 6203
2018-06-05 07:49:03.597	[P2P8]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5625 / 5625
2018-06-05 07:49:03.760	[P2P4]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582188 - 1587298 start at 6180 and end at 6200
2018-06-05 07:49:03.761	[P2P4]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5111 / 5111
2018-06-05 07:49:06.301	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582586 - 1588211 start at 6181 and end at 6203
2018-06-05 07:49:06.302	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5626 / 5626
2018-06-05 07:49:07.446	[P2P8]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1581880 - 1588209 start at 6179 and end at 6203
2018-06-05 07:49:07.447	[P2P8]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 6330 / 6330
2018-06-05 07:49:08.532	[P2P5]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582627 - 1588211 start at 6182 and end at 6203
2018-06-05 07:49:08.533	[P2P5]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5585 / 5585
2018-06-05 07:49:10.832	[P2P0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582607 - 1588211 start at 6182 and end at 6203
2018-06-05 07:49:10.833	[P2P0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5605 / 5605
2018-06-05 07:49:11.199	[P2P4]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582647 - 1588211 start at 6182 and end at 6203
2018-06-05 07:49:11.200	[P2P4]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5565 / 5565
2018-06-05 07:49:13.391	[P2P8]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584481 - 1588211 start at 6189 and end at 6203
2018-06-05 07:49:13.392	[P2P8]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3731 / 3731
2018-06-05 07:49:13.536	[P2P5]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582667 - 1588211 start at 6182 and end at 6203
2018-06-05 07:49:13.538	[P2P5]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5545 / 5545
2018-06-05 07:49:13.952	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582207 - 1587298 start at 6180 and end at 6200
2018-06-05 07:49:13.954	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5092 / 5092
2018-06-05 07:49:18.001	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582686 - 1588211 start at 6182 and end at 6203
2018-06-05 07:49:18.002	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5526 / 5526
2018-06-05 07:49:19.327	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582626 - 1588211 start at 6182 and end at 6203
2018-06-05 07:49:19.328	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5586 / 5586
2018-06-05 07:49:20.800	[P2P5]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582226 - 1587298 start at 6180 and end at 6200
2018-06-05 07:49:20.801	[P2P5]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5073 / 5073
2018-06-05 07:49:21.072	[P2P5]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584501 - 1588211 start at 6189 and end at 6203
2018-06-05 07:49:21.072	[P2P5]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3711 / 3711
2018-06-05 07:49:22.712	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582705 - 1588211 start at 6182 and end at 6203
2018-06-05 07:49:22.714	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5507 / 5507
2018-06-05 07:49:25.436	[P2P6]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582245 - 1587298 start at 6180 and end at 6200
2018-06-05 07:49:25.437	[P2P6]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5054 / 5054
2018-06-05 07:49:26.528	[P2P4]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582724 - 1588211 start at 6182 and end at 6203
2018-06-05 07:49:26.529	[P2P4]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5488 / 5488
2018-06-05 07:49:27.396	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582645 - 1588211 start at 6182 and end at 6203
2018-06-05 07:49:27.397	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5567 / 5567
2018-06-05 07:49:29.162	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582264 - 1587298 start at 6180 and end at 6200
2018-06-05 07:49:29.164	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5035 / 5035
2018-06-05 07:49:29.855	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582743 - 1588211 start at 6182 and end at 6203
2018-06-05 07:49:29.856	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5469 / 5469
2018-06-05 07:49:31.902	[P2P0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582283 - 1587298 start at 6180 and end at 6200
2018-06-05 07:49:31.904	[P2P0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5016 / 5016
2018-06-05 07:49:34.160	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1516336 - 1526335 start at 5923 and end at 5962
2018-06-05 07:49:34.165	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 9936 / 10000
2018-06-05 07:49:34.937	[P2P0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582664 - 1588211 start at 6182 and end at 6203
2018-06-05 07:49:34.939	[P2P0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5548 / 5548
2018-06-05 07:49:35.708	[P2P6]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582762 - 1588211 start at 6182 and end at 6203
2018-06-05 07:49:35.709	[P2P6]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5450 / 5450
2018-06-05 07:49:40.166	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582781 - 1588211 start at 6182 and end at 6203
2018-06-05 07:49:40.167	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5431 / 5431
2018-06-05 07:49:51.669	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584521 - 1588211 start at 6189 and end at 6203
2018-06-05 07:49:51.670	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3691 / 3691
2018-06-05 07:50:01.211	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582302 - 1587298 start at 6180 and end at 6200
2018-06-05 07:50:01.212	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4997 / 4997
2018-06-05 07:50:01.288	[P2P2]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582683 - 1588211 start at 6182 and end at 6203
2018-06-05 07:50:01.290	[P2P2]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5529 / 5529
2018-06-05 07:50:02.192	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582800 - 1588211 start at 6182 and end at 6203
2018-06-05 07:50:02.193	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5412 / 5412
2018-06-05 07:50:08.035	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582321 - 1587298 start at 6180 and end at 6200
2018-06-05 07:50:08.036	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4978 / 4978
2018-06-05 07:50:10.890	[P2P2]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582340 - 1587298 start at 6181 and end at 6200
2018-06-05 07:50:10.891	[P2P2]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4959 / 4959
2018-06-05 07:50:13.750	[P2P5]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582359 - 1587298 start at 6181 and end at 6200
2018-06-05 07:50:13.751	[P2P5]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4940 / 4940
2018-06-05 07:50:18.069	[P2P8]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582378 - 1587298 start at 6181 and end at 6200
2018-06-05 07:50:18.070	[P2P8]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4921 / 4921
2018-06-05 07:50:21.855	[P2P0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582397 - 1587298 start at 6181 and end at 6200
2018-06-05 07:50:21.857	[P2P0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4902 / 4902
2018-06-05 07:50:23.008	[P2P6]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582819 - 1588211 start at 6182 and end at 6203
2018-06-05 07:50:23.010	[P2P6]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5393 / 5393
2018-06-05 07:50:23.408	[P2P8]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582702 - 1588211 start at 6182 and end at 6203
2018-06-05 07:50:23.410	[P2P8]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5510 / 5510
2018-06-05 07:50:25.235	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582416 - 1587298 start at 6181 and end at 6200
2018-06-05 07:50:25.237	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4883 / 4883
2018-06-05 07:50:29.558	[P2P4]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1581880 - 1588211 start at 6179 and end at 6203
2018-06-05 07:50:29.560	[P2P4]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 6332 / 6332
2018-06-05 07:50:33.212	[P2P0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582838 - 1588211 start at 6182 and end at 6203
2018-06-05 07:50:33.214	[P2P0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5374 / 5374
2018-06-05 07:50:36.373	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582721 - 1588211 start at 6182 and end at 6203
2018-06-05 07:50:36.375	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5491 / 5491
2018-06-05 07:50:37.484	[P2P5]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582435 - 1587298 start at 6181 and end at 6200
2018-06-05 07:50:37.485	[P2P5]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4864 / 4864
2018-06-05 07:50:47.203	[P2P6]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582740 - 1588211 start at 6182 and end at 6203
2018-06-05 07:50:47.205	[P2P6]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5472 / 5472
2018-06-05 07:50:58.002	[P2P6]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582759 - 1588211 start at 6182 and end at 6203
2018-06-05 07:50:58.003	[P2P6]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5453 / 5453
2018-06-05 07:51:00.746	[P2P6]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582454 - 1587298 start at 6181 and end at 6200
2018-06-05 07:51:00.747	[P2P6]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4845 / 4845
2018-06-05 07:51:03.897	[P2P2]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1577776 - 1578865 start at 6163 and end at 6167
2018-06-05 07:51:03.898	[P2P2]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 976 / 1090
2018-06-05 07:51:04.228	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582778 - 1588211 start at 6182 and end at 6203
2018-06-05 07:51:04.229	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5434 / 5434
2018-06-05 07:51:08.467	[P2P2]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584541 - 1588211 start at 6189 and end at 6203
2018-06-05 07:51:08.468	[P2P2]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3671 / 3671
2018-06-05 07:51:13.044	[P2P2]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582797 - 1588211 start at 6182 and end at 6203
2018-06-05 07:51:13.045	[P2P2]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5415 / 5415
2018-06-05 07:51:13.807	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582473 - 1587298 start at 6181 and end at 6200
2018-06-05 07:51:13.808	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4826 / 4826
2018-06-05 07:51:24.182	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582816 - 1588211 start at 6182 and end at 6203
2018-06-05 07:51:24.183	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5396 / 5396
2018-06-05 07:51:26.628	[P2P5]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582492 - 1587298 start at 6181 and end at 6200
2018-06-05 07:51:26.629	[P2P5]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4807 / 4807
2018-06-05 07:51:31.980	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582835 - 1588211 start at 6182 and end at 6203
2018-06-05 07:51:31.982	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5377 / 5377
2018-06-05 07:51:36.378	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582511 - 1587298 start at 6181 and end at 6200
2018-06-05 07:51:36.380	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4788 / 4788
2018-06-05 07:51:37.712	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582854 - 1588211 start at 6183 and end at 6203
2018-06-05 07:51:37.714	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5358 / 5358
2018-06-05 07:51:39.119	[P2P6]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582530 - 1587298 start at 6181 and end at 6200
2018-06-05 07:51:39.121	[P2P6]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4769 / 4769
2018-06-05 07:51:39.601	[P2P8]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1581880 - 1588211 start at 6179 and end at 6203
2018-06-05 07:51:39.602	[P2P8]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 6332 / 6332
2018-06-05 07:51:41.320	[P2P2]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582549 - 1587298 start at 6181 and end at 6200
2018-06-05 07:51:41.321	[P2P2]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4750 / 4750
2018-06-05 07:51:44.444	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582568 - 1587298 start at 6181 and end at 6200
2018-06-05 07:51:44.446	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4731 / 4731
2018-06-05 07:51:45.787	[P2P2]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582873 - 1588211 start at 6183 and end at 6203
2018-06-05 07:51:45.788	[P2P2]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5339 / 5339
2018-06-05 07:51:51.328	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582587 - 1587298 start at 6181 and end at 6200
2018-06-05 07:51:51.330	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4712 / 4712
2018-06-05 07:51:55.925	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582606 - 1587298 start at 6182 and end at 6200
2018-06-05 07:51:55.926	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4693 / 4693
2018-06-05 07:52:01.936	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582625 - 1587298 start at 6182 and end at 6200
2018-06-05 07:52:01.938	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4674 / 4674
2018-06-05 07:52:03.574	[P2P5]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582892 - 1588211 start at 6183 and end at 6203
2018-06-05 07:52:03.575	[P2P5]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5320 / 5320
2018-06-05 07:52:18.509	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584561 - 1588211 start at 6189 and end at 6203
2018-06-05 07:52:18.510	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3651 / 3651
2018-06-05 07:52:19.115	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1516336 - 1526335 start at 5923 and end at 5962
2018-06-05 07:52:19.120	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 9936 / 10000
2018-06-05 07:52:19.209	[P2P2]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582644 - 1587298 start at 6182 and end at 6200
2018-06-05 07:52:19.211	[P2P2]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4655 / 4655
2018-06-05 07:52:21.309	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1581880 - 1588211 start at 6179 and end at 6203
2018-06-05 07:52:21.311	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 6332 / 6332
2018-06-05 07:52:23.307	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582911 - 1588211 start at 6183 and end at 6203
2018-06-05 07:52:23.308	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5301 / 5301
2018-06-05 07:52:26.542	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582663 - 1587298 start at 6182 and end at 6200
2018-06-05 07:52:26.543	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4636 / 4636
2018-06-05 07:52:28.173	[P2P5]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1581880 - 1588211 start at 6179 and end at 6203
2018-06-05 07:52:28.175	[P2P5]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 6332 / 6332
2018-06-05 07:52:31.543	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582682 - 1587298 start at 6182 and end at 6200
2018-06-05 07:52:31.545	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4617 / 4617
2018-06-05 07:52:33.158	[P2P8]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584581 - 1588211 start at 6189 and end at 6203
2018-06-05 07:52:33.159	[P2P8]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3631 / 3631
2018-06-05 07:52:35.362	[P2P8]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1581880 - 1588212 start at 6179 and end at 6203
2018-06-05 07:52:35.364	[P2P8]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 6333 / 6333
2018-06-05 07:52:37.598	[P2P5]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582701 - 1587298 start at 6182 and end at 6200
2018-06-05 07:52:37.599	[P2P5]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4598 / 4598
2018-06-05 07:52:38.302	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582930 - 1588212 start at 6183 and end at 6203
2018-06-05 07:52:38.304	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5283 / 5283
2018-06-05 07:52:41.041	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582720 - 1587298 start at 6182 and end at 6200
2018-06-05 07:52:41.042	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4579 / 4579
2018-06-05 07:52:46.101	[P2P5]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582739 - 1587298 start at 6182 and end at 6200
2018-06-05 07:52:46.102	[P2P5]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4560 / 4560
2018-06-05 07:52:50.880	[P2P6]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1581880 - 1588212 start at 6179 and end at 6203
2018-06-05 07:52:50.882	[P2P6]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 6333 / 6333
2018-06-05 07:52:57.647	[P2P5]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582949 - 1588212 start at 6183 and end at 6203
2018-06-05 07:52:57.648	[P2P5]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5264 / 5264
2018-06-05 07:53:17.157	[P2P4]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582758 - 1587298 start at 6182 and end at 6200
2018-06-05 07:53:17.159	[P2P4]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4541 / 4541
2018-06-05 07:53:19.440	[P2P0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582968 - 1588213 start at 6183 and end at 6203
2018-06-05 07:53:19.441	[P2P0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5246 / 5246
2018-06-05 07:53:27.419	[P2P4]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1581880 - 1588213 start at 6179 and end at 6203
2018-06-05 07:53:27.421	[P2P4]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 6334 / 6334
2018-06-05 07:53:32.348	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1581880 - 1588213 start at 6179 and end at 6203
2018-06-05 07:53:32.351	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 6334 / 6334
2018-06-05 07:53:46.672	[P2P6]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582987 - 1588214 start at 6183 and end at 6203
2018-06-05 07:53:46.674	[P2P6]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5228 / 5228
2018-06-05 07:53:48.740	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582777 - 1587298 start at 6182 and end at 6200
2018-06-05 07:53:48.742	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4522 / 4522
2018-06-05 07:53:49.116	[P2P4]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584601 - 1588214 start at 6189 and end at 6203
2018-06-05 07:53:49.117	[P2P4]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3614 / 3614
2018-06-05 07:53:51.713	[P2P5]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583006 - 1588214 start at 6183 and end at 6203
2018-06-05 07:53:51.715	[P2P5]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5209 / 5209
2018-06-05 07:53:56.187	[P2P8]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583025 - 1588214 start at 6183 and end at 6203
2018-06-05 07:53:56.189	[P2P8]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5190 / 5190
2018-06-05 07:54:08.394	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582796 - 1587298 start at 6182 and end at 6200
2018-06-05 07:54:08.396	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4503 / 4503
2018-06-05 07:54:11.006	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584621 - 1588214 start at 6189 and end at 6203
2018-06-05 07:54:11.007	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3594 / 3594
2018-06-05 07:54:13.267	[P2P0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583044 - 1588214 start at 6183 and end at 6203
2018-06-05 07:54:13.269	[P2P0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5171 / 5171
2018-06-05 07:54:13.617	[P2P5]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582815 - 1587298 start at 6182 and end at 6200
2018-06-05 07:54:13.619	[P2P5]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4484 / 4484
2018-06-05 07:54:17.561	[P2P5]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1581880 - 1588214 start at 6179 and end at 6203
2018-06-05 07:54:17.563	[P2P5]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 6335 / 6335
2018-06-05 07:54:31.283	[P2P5]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1581880 - 1588214 start at 6179 and end at 6203
2018-06-05 07:54:31.285	[P2P5]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 6335 / 6335
2018-06-05 07:54:33.546	[P2P6]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582834 - 1587298 start at 6182 and end at 6200
2018-06-05 07:54:33.548	[P2P6]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4465 / 4465
2018-06-05 07:54:36.392	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1581880 - 1588214 start at 6179 and end at 6203
2018-06-05 07:54:36.394	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 6335 / 6335
2018-06-05 07:54:36.503	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584641 - 1588214 start at 6190 and end at 6203
2018-06-05 07:54:36.504	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3574 / 3574
2018-06-05 07:54:39.557	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583063 - 1588214 start at 6183 and end at 6203
2018-06-05 07:54:39.559	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5152 / 5152
2018-06-05 07:54:41.194	[P2P5]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1581880 - 1585327 start at 6179 and end at 6192
2018-06-05 07:54:41.196	[P2P5]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3272 / 3448
2018-06-05 07:54:47.295	[P2P6]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582853 - 1587298 start at 6183 and end at 6200
2018-06-05 07:54:47.297	[P2P6]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4446 / 4446
2018-06-05 07:54:57.299	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584661 - 1588214 start at 6190 and end at 6203
2018-06-05 07:54:57.300	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3554 / 3554
2018-06-05 07:54:57.941	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1581880 - 1588214 start at 6179 and end at 6203
2018-06-05 07:54:57.943	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 6335 / 6335
2018-06-05 07:55:01.124	[P2P5]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582872 - 1587298 start at 6183 and end at 6200
2018-06-05 07:55:01.126	[P2P5]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4427 / 4427
2018-06-05 07:55:08.724	[P2P0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583082 - 1588215 start at 6183 and end at 6203
2018-06-05 07:55:08.725	[P2P0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5134 / 5134
2018-06-05 07:55:13.774	[P2P4]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583101 - 1588215 start at 6183 and end at 6203
2018-06-05 07:55:13.775	[P2P4]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5115 / 5115
2018-06-05 07:55:14.768	[P2P6]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582891 - 1587298 start at 6183 and end at 6200
2018-06-05 07:55:14.769	[P2P6]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4408 / 4408
2018-06-05 07:55:21.227	[P2P0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583120 - 1588215 start at 6184 and end at 6203
2018-06-05 07:55:21.228	[P2P0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5096 / 5096
2018-06-05 07:55:26.291	[P2P6]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:310	[145.239.79.192:18080 OUT] Sync data returned a new top block candidate: 1581881 -> 1588217 [Your node is 6336 blocks (8 days) behind] 
SYNCHRONIZATION started
2018-06-05 07:55:27.033	[P2P4]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582910 - 1587298 start at 6183 and end at 6200
2018-06-05 07:55:27.035	[P2P4]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4389 / 4389
2018-06-05 07:55:28.522	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1581880 - 1588216 start at 6179 and end at 6203
2018-06-05 07:55:28.524	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 6337 / 6337
2018-06-05 07:55:34.248	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584681 - 1588217 start at 6190 and end at 6203
2018-06-05 07:55:34.248	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3537 / 3537
2018-06-05 07:55:36.001	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583139 - 1588217 start at 6184 and end at 6203
2018-06-05 07:55:36.002	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5079 / 5079
2018-06-05 07:55:40.051	[P2P4]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582929 - 1587298 start at 6183 and end at 6200
2018-06-05 07:55:40.052	[P2P4]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4370 / 4370
2018-06-05 07:55:53.217	[P2P0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583158 - 1588217 start at 6184 and end at 6203
2018-06-05 07:55:53.218	[P2P0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5060 / 5060
2018-06-05 07:55:55.390	[P2P4]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582948 - 1587298 start at 6183 and end at 6200
2018-06-05 07:55:55.392	[P2P4]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4351 / 4351
2018-06-05 07:55:59.202	[P2P0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1581880 - 1588218 start at 6179 and end at 6203
2018-06-05 07:55:59.204	[P2P0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 6339 / 6339
2018-06-05 07:56:10.219	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582967 - 1587298 start at 6183 and end at 6200
2018-06-05 07:56:10.221	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4332 / 4332
2018-06-05 07:56:15.162	[P2P0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584701 - 1588218 start at 6190 and end at 6203
2018-06-05 07:56:15.163	[P2P0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3518 / 3518
2018-06-05 07:56:15.275	[P2P4]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583177 - 1588218 start at 6184 and end at 6203
2018-06-05 07:56:15.277	[P2P4]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5042 / 5042
2018-06-05 07:56:24.128	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1581880 - 1587298 start at 6179 and end at 6200
2018-06-05 07:56:24.131	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5419 / 5419
2018-06-05 07:56:33.269	[P2P5]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1581880 - 1587547 start at 6179 and end at 6201
2018-06-05 07:56:33.272	[P2P5]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5668 / 5668
2018-06-05 07:56:36.387	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582986 - 1587298 start at 6183 and end at 6200
2018-06-05 07:56:36.388	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4313 / 4313
2018-06-05 07:56:43.776	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1581921 - 1587547 start at 6179 and end at 6201
2018-06-05 07:56:43.777	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5627 / 5627
2018-06-05 07:56:44.504	[P2P2]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583196 - 1588218 start at 6184 and end at 6203
2018-06-05 07:56:44.505	[P2P2]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5023 / 5023
2018-06-05 07:56:48.514	[P2P0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583215 - 1588218 start at 6184 and end at 6203
2018-06-05 07:56:48.515	[P2P0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5004 / 5004
2018-06-05 07:56:49.167	[P2P5]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1581880 - 1588218 start at 6179 and end at 6203
2018-06-05 07:56:49.169	[P2P5]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 6339 / 6339
2018-06-05 07:56:52.796	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584721 - 1588218 start at 6190 and end at 6203
2018-06-05 07:56:52.796	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3498 / 3498
2018-06-05 07:56:58.197	[P2P5]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583005 - 1587298 start at 6183 and end at 6200
2018-06-05 07:56:58.198	[P2P5]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4294 / 4294
2018-06-05 07:56:59.203	[P2P8]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583234 - 1588218 start at 6184 and end at 6203
2018-06-05 07:56:59.204	[P2P8]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4985 / 4985
2018-06-05 07:57:06.512	[P2P0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1581940 - 1587547 start at 6179 and end at 6201
2018-06-05 07:57:06.513	[P2P0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5608 / 5608
2018-06-05 07:57:10.399	[P2P8]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1581880 - 1588218 start at 6179 and end at 6203
2018-06-05 07:57:10.401	[P2P8]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 6339 / 6339
2018-06-05 07:57:10.639	[P2P0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1581959 - 1587547 start at 6179 and end at 6201
2018-06-05 07:57:10.641	[P2P0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5589 / 5589
2018-06-05 07:57:16.215	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1581978 - 1587547 start at 6179 and end at 6201
2018-06-05 07:57:16.217	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5570 / 5570
2018-06-05 07:57:19.906	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583253 - 1588218 start at 6184 and end at 6203
2018-06-05 07:57:19.908	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4966 / 4966
2018-06-05 07:57:20.273	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583024 - 1587298 start at 6183 and end at 6200
2018-06-05 07:57:20.274	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4275 / 4275
2018-06-05 07:57:30.438	[P2P8]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1581997 - 1587547 start at 6179 and end at 6201
2018-06-05 07:57:30.440	[P2P8]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5551 / 5551
2018-06-05 07:57:33.657	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583043 - 1587298 start at 6183 and end at 6200
2018-06-05 07:57:33.659	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4256 / 4256
2018-06-05 07:57:35.196	[P2P0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583272 - 1588218 start at 6184 and end at 6203
2018-06-05 07:57:35.198	[P2P0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4947 / 4947
2018-06-05 07:57:37.406	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1581880 - 1581885 start at 6179 and end at 6179
2018-06-05 07:57:43.040	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583291 - 1588218 start at 6184 and end at 6203
2018-06-05 07:57:43.041	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4928 / 4928
2018-06-05 07:57:49.735	[P2P0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583062 - 1587298 start at 6183 and end at 6200
2018-06-05 07:57:49.737	[P2P0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4237 / 4237
2018-06-05 07:57:53.461	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582016 - 1587547 start at 6179 and end at 6201
2018-06-05 07:57:53.463	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5532 / 5532
2018-06-05 07:57:54.176	[P2P6]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583310 - 1588218 start at 6184 and end at 6203
2018-06-05 07:57:54.178	[P2P6]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4909 / 4909
2018-06-05 07:57:54.509	[P2P6]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584741 - 1588218 start at 6190 and end at 6203
2018-06-05 07:57:54.510	[P2P6]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3478 / 3478
2018-06-05 07:58:04.254	[P2P0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1581880 - 1588218 start at 6179 and end at 6203
2018-06-05 07:58:04.256	[P2P0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 6339 / 6339
2018-06-05 07:58:06.121	[P2P2]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583329 - 1588218 start at 6184 and end at 6203
2018-06-05 07:58:06.122	[P2P2]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4890 / 4890
2018-06-05 07:58:07.291	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583081 - 1587298 start at 6183 and end at 6200
2018-06-05 07:58:07.293	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4218 / 4218
2018-06-05 07:58:07.689	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582035 - 1587547 start at 6179 and end at 6201
2018-06-05 07:58:07.691	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5513 / 5513
2018-06-05 07:58:09.555	[P2P4]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583100 - 1587298 start at 6183 and end at 6200
2018-06-05 07:58:09.556	[P2P4]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4199 / 4199
2018-06-05 07:58:12.520	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583119 - 1587298 start at 6184 and end at 6200
2018-06-05 07:58:12.521	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4180 / 4180
2018-06-05 07:58:13.445	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1579824 - 1580207 start at 6171 and end at 6172
2018-06-05 07:58:13.445	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 208 / 384
2018-06-05 07:58:13.736	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582054 - 1587547 start at 6179 and end at 6201
2018-06-05 07:58:13.738	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5494 / 5494
2018-06-05 07:58:15.420	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583348 - 1588218 start at 6184 and end at 6203
2018-06-05 07:58:15.421	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4871 / 4871
2018-06-05 07:58:15.646	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583138 - 1587298 start at 6184 and end at 6200
2018-06-05 07:58:15.647	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4161 / 4161
2018-06-05 07:58:18.223	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583157 - 1587298 start at 6184 and end at 6200
2018-06-05 07:58:18.224	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4142 / 4142
2018-06-05 07:58:19.174	[P2P4]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1581880 - 1588218 start at 6179 and end at 6203
2018-06-05 07:58:19.175	[P2P4]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 6339 / 6339
2018-06-05 07:58:20.760	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583176 - 1587298 start at 6184 and end at 6200
2018-06-05 07:58:20.761	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4123 / 4123
2018-06-05 07:58:21.696	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583367 - 1588218 start at 6185 and end at 6203
2018-06-05 07:58:21.696	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4852 / 4852
2018-06-05 07:58:21.720	[P2P6]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582073 - 1587547 start at 6179 and end at 6201
2018-06-05 07:58:21.721	[P2P6]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5475 / 5475
2018-06-05 07:58:26.133	[P2P6]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583386 - 1588218 start at 6185 and end at 6203
2018-06-05 07:58:26.133	[P2P6]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4833 / 4833
2018-06-05 07:58:27.912	[P2P6]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583195 - 1587298 start at 6184 and end at 6200
2018-06-05 07:58:27.913	[P2P6]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4104 / 4104
2018-06-05 07:58:30.548	[P2P0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582092 - 1587547 start at 6180 and end at 6201
2018-06-05 07:58:30.550	[P2P0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5456 / 5456
2018-06-05 07:58:30.627	[P2P4]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583405 - 1588218 start at 6185 and end at 6203
2018-06-05 07:58:30.629	[P2P4]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4814 / 4814
2018-06-05 07:58:32.624	[P2P8]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583214 - 1587298 start at 6184 and end at 6200
2018-06-05 07:58:32.626	[P2P8]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4085 / 4085
2018-06-05 07:58:36.759	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583424 - 1588218 start at 6185 and end at 6203
2018-06-05 07:58:36.761	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4795 / 4795
2018-06-05 07:58:39.018	[P2P4]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582111 - 1587547 start at 6180 and end at 6201
2018-06-05 07:58:39.020	[P2P4]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5437 / 5437
2018-06-05 07:58:42.401	[P2P2]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584761 - 1588218 start at 6190 and end at 6203
2018-06-05 07:58:42.402	[P2P2]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3458 / 3458
2018-06-05 07:58:42.592	[P2P4]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583233 - 1587298 start at 6184 and end at 6200
2018-06-05 07:58:42.594	[P2P4]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4066 / 4066
2018-06-05 07:58:44.913	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583443 - 1588218 start at 6185 and end at 6203
2018-06-05 07:58:44.914	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4776 / 4776
2018-06-05 07:58:49.729	[P2P2]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1516336 - 1526335 start at 5923 and end at 5962
2018-06-05 07:58:49.734	[P2P2]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 9936 / 10000
2018-06-05 07:58:50.703	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583252 - 1587298 start at 6184 and end at 6200
2018-06-05 07:58:50.705	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4047 / 4047
2018-06-05 07:58:55.823	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583462 - 1588218 start at 6185 and end at 6203
2018-06-05 07:58:55.824	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4757 / 4757
2018-06-05 07:58:55.953	[P2P5]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582130 - 1587547 start at 6180 and end at 6201
2018-06-05 07:58:55.955	[P2P5]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5418 / 5418
2018-06-05 07:58:57.784	[P2P6]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1577776 - 1578866 start at 6163 and end at 6167
2018-06-05 07:58:57.785	[P2P6]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 976 / 1091
2018-06-05 07:58:59.251	[P2P6]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584781 - 1588218 start at 6190 and end at 6203
2018-06-05 07:58:59.252	[P2P6]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3438 / 3438
2018-06-05 07:58:59.418	[P2P0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583271 - 1587298 start at 6184 and end at 6200
2018-06-05 07:58:59.419	[P2P0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4028 / 4028
2018-06-05 07:59:02.657	[P2P6]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1581880 - 1587298 start at 6179 and end at 6200
2018-06-05 07:59:02.659	[P2P6]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5419 / 5419
2018-06-05 07:59:04.872	[P2P0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582149 - 1587547 start at 6180 and end at 6201
2018-06-05 07:59:04.874	[P2P0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5399 / 5399
2018-06-05 07:59:08.119	[P2P6]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583481 - 1588218 start at 6185 and end at 6203
2018-06-05 07:59:08.120	[P2P6]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4738 / 4738
2018-06-05 07:59:08.323	[P2P4]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583290 - 1587298 start at 6184 and end at 6200
2018-06-05 07:59:08.324	[P2P4]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4009 / 4009
2018-06-05 07:59:16.566	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583500 - 1588218 start at 6185 and end at 6203
2018-06-05 07:59:16.567	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4719 / 4719
2018-06-05 07:59:16.653	[P2P5]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583309 - 1587298 start at 6184 and end at 6200
2018-06-05 07:59:16.654	[P2P5]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3990 / 3990
2018-06-05 07:59:17.035	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582168 - 1587547 start at 6180 and end at 6201
2018-06-05 07:59:17.036	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5380 / 5380
2018-06-05 07:59:21.431	[P2P6]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583328 - 1587298 start at 6184 and end at 6200
2018-06-05 07:59:21.432	[P2P6]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3971 / 3971
2018-06-05 07:59:25.725	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582187 - 1587547 start at 6180 and end at 6201
2018-06-05 07:59:25.727	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5361 / 5361
2018-06-05 07:59:26.084	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583347 - 1587298 start at 6184 and end at 6200
2018-06-05 07:59:26.085	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3952 / 3952
2018-06-05 07:59:29.856	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583519 - 1588218 start at 6185 and end at 6203
2018-06-05 07:59:29.858	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4700 / 4700
2018-06-05 07:59:30.667	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1581880 - 1588218 start at 6179 and end at 6203
2018-06-05 07:59:30.670	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 6339 / 6339
2018-06-05 07:59:30.742	[P2P8]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583366 - 1587298 start at 6185 and end at 6200
2018-06-05 07:59:30.743	[P2P8]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3933 / 3933
2018-06-05 07:59:33.603	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583385 - 1587298 start at 6185 and end at 6200
2018-06-05 07:59:33.604	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3914 / 3914
2018-06-05 07:59:36.770	[P2P8]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583404 - 1587298 start at 6185 and end at 6200
2018-06-05 07:59:36.771	[P2P8]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3895 / 3895
2018-06-05 07:59:39.833	[P2P5]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582206 - 1587547 start at 6180 and end at 6201
2018-06-05 07:59:39.835	[P2P5]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5342 / 5342
2018-06-05 07:59:42.154	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584801 - 1588218 start at 6190 and end at 6203
2018-06-05 07:59:42.155	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3418 / 3418
2018-06-05 07:59:45.298	[P2P4]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583538 - 1588218 start at 6185 and end at 6203
2018-06-05 07:59:45.299	[P2P4]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4681 / 4681
2018-06-05 07:59:47.764	[P2P6]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583423 - 1587298 start at 6185 and end at 6200
2018-06-05 07:59:47.765	[P2P6]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3876 / 3876
2018-06-05 07:59:52.187	[P2P5]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583442 - 1587298 start at 6185 and end at 6200
2018-06-05 07:59:52.188	[P2P5]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3857 / 3857
2018-06-05 07:59:53.117	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583557 - 1588218 start at 6185 and end at 6203
2018-06-05 07:59:53.118	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4662 / 4662
2018-06-05 07:59:53.248	[P2P6]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582225 - 1587547 start at 6180 and end at 6201
2018-06-05 07:59:53.250	[P2P6]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5323 / 5323
2018-06-05 07:59:54.817	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1581880 - 1588218 start at 6179 and end at 6203
2018-06-05 07:59:54.819	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 6339 / 6339
2018-06-05 07:59:56.036	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583461 - 1587298 start at 6185 and end at 6200
2018-06-05 07:59:56.037	[P2P9]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3838 / 3838
2018-06-05 07:59:56.780	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583576 - 1588218 start at 6185 and end at 6203
2018-06-05 07:59:56.782	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4643 / 4643
2018-06-05 07:59:59.281	[P2P6]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583595 - 1588218 start at 6185 and end at 6203
2018-06-05 07:59:59.283	[P2P6]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4624 / 4624
2018-06-05 08:00:08.319	[P2P6]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583480 - 1587298 start at 6185 and end at 6200
2018-06-05 08:00:08.320	[P2P6]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3819 / 3819
2018-06-05 08:00:15.561	[P2P5]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584821 - 1588218 start at 6190 and end at 6203
2018-06-05 08:00:15.562	[P2P5]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3398 / 3398
2018-06-05 08:00:26.835	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583499 - 1587298 start at 6185 and end at 6200
2018-06-05 08:00:26.836	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3800 / 3800
2018-06-05 08:00:27.251	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583614 - 1588218 start at 6185 and end at 6203
2018-06-05 08:00:27.253	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4605 / 4605
2018-06-05 08:00:28.763	[P2P4]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582244 - 1587547 start at 6180 and end at 6201
2018-06-05 08:00:28.765	[P2P4]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5304 / 5304
2018-06-05 08:00:42.063	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583633 - 1588218 start at 6186 and end at 6203
2018-06-05 08:00:42.064	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4586 / 4586
2018-06-05 08:01:00.498	[P2P4]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583652 - 1588218 start at 6186 and end at 6203
2018-06-05 08:01:00.499	[P2P4]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4567 / 4567
2018-06-05 08:01:00.518	[P2P8]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583518 - 1587298 start at 6185 and end at 6200
2018-06-05 08:01:00.519	[P2P8]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3781 / 3781
2018-06-05 08:01:01.332	[P2P6]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582263 - 1587547 start at 6180 and end at 6201
2018-06-05 08:01:01.334	[P2P6]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5285 / 5285
2018-06-05 08:01:05.256	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583537 - 1587298 start at 6185 and end at 6200
2018-06-05 08:01:05.258	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3762 / 3762
2018-06-05 08:01:08.805	[P2P5]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1584841 - 1588218 start at 6190 and end at 6203
2018-06-05 08:01:08.806	[P2P5]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3378 / 3378
2018-06-05 08:01:09.795	[P2P0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583671 - 1588218 start at 6186 and end at 6203
2018-06-05 08:01:09.797	[P2P0]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4548 / 4548
2018-06-05 08:01:10.900	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583556 - 1587298 start at 6185 and end at 6200
2018-06-05 08:01:10.901	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3743 / 3743
2018-06-05 08:01:16.732	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583690 - 1588218 start at 6186 and end at 6203
2018-06-05 08:01:16.733	[P2P3]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 4529 / 4529
2018-06-05 08:01:17.406	[P2P8]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1582282 - 1587547 start at 6180 and end at 6201
2018-06-05 08:01:17.407	[P2P8]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 5266 / 5266
2018-06-05 08:01:19.500	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3860	Blocks 1583575 - 1587298 start at 6185 and end at 6200
2018-06-05 08:01:19.501	[P2P7]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3935	usable: 3724 / 3724
```

~~I'm still running the same daemon instance without quiting.~~ Not anymore since I had to reboot the computer for some other reason.

# Discussion History
## selsta | 2025-12-19T16:54:18+00:00
Closing as it appears not relevant anymore.

# Action History
- Created by: stoffu | 2018-06-05T08:08:44+00:00
- Closed at: 2025-12-19T16:54:28+00:00
