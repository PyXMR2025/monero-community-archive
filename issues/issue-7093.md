---
title: 'ERROR : Unable to send transaction(s) via Dandelion++ stem'
source_url: https://github.com/monero-project/monero/issues/7093
author: ghost
assignees: []
labels: []
created_at: '2020-12-08T02:00:38+00:00'
updated_at: '2021-10-06T02:49:18+00:00'
type: issue
status: closed
closed_at: '2021-10-06T02:49:18+00:00'
---

# Original Description
2020-12-08 01:38:14.279	[P2P7]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:377	SYNCHRONIZATION started
2020-12-08 01:38:17.783	    7f4cfe1f9700	INFO	stacktrace	src/common/stack_trace.cpp:133	Exception: std::runtime_error
2020-12-08 01:38:17.783	    7f4cfe1f9700	INFO	stacktrace	src/common/stack_trace.cpp:134	Unwound call stack:
2020-12-08 01:38:17.787	    7f4cfe1f9700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [1]  0x111) [0x558e144cc181]:__wrap___cxa_throw+0x111) [0x558e144cc181]
2020-12-08 01:38:17.787	    7f4cfe1f9700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [2] ./monero/build/Linux/master/release/bin/monerod(+0x46323b) [0x558e1404023b] 
2020-12-08 01:38:17.787	    7f4cfe1f9700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [3]  0x142) [0x558e1481c8e2]:_alloc_cache+0x142) [0x558e1481c8e2]
2020-12-08 01:38:17.787	    7f4cfe1f9700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [4]  0x293) [0x558e14483b13]:_slow_hash+0x293) [0x558e14483b13]
2020-12-08 01:38:17.787	    7f4cfe1f9700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [5]  0xe6) [0x558e1446cad6]:_ZN10cryptonote18get_block_longhashEPKNS_10BlockchainERKNS_5blockERN6crypto4hashEmPKS7_i+0xe6) [0x558e1446cad6]
2020-12-08 01:38:17.787	    7f4cfe1f9700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [6]  0x21) [0x558e1446cca1]:_ZN10cryptonote18get_block_longhashEPKNS_10BlockchainERKNS_5blockEmi+0x21) [0x558e1446cca1]
2020-12-08 01:38:17.787	    7f4cfe1f9700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [7]  0xa9) [0x558e14418fe9]:_ZNK10cryptonote10Blockchain21block_longhash_workerEmRKN4epee4spanIKNS_5blockEEERSt13unordered_mapIN6crypto4hashESA_St4hashISA_ESt8equal_toISA_ESaISt4pairIKSA_SA_EEE+0xa9) [0x558e14418fe9]
2020-12-08 01:38:17.787	    7f4cfe1f9700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [8]  0x4d1) [0x558e144c4fb1]:_ZN5tools10threadpool3runEb+0x4d1) [0x558e144c4fb1]
2020-12-08 01:38:17.787	    7f4cfe1f9700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [9] ./monero/build/Linux/master/release/bin/monerod(+0xea44f5) [0x558e14a814f5] 
2020-12-08 01:38:17.787	    7f4cfe1f9700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [10]  0x7fa3) [0x7f67386c9fa3]:_64-linux-gnu/libpthread.so.0(+0x7fa3) [0x7f67386c9fa3]
2020-12-08 01:38:17.787	    7f4cfe1f9700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [11]  0x3f) [0x7f67385fa4cf]:_64-linux-gnu/libc.so.6(clone+0x3f) [0x7f67385fa4cf]
2020-12-08 01:38:17.787	    7f4cfe1f9700	INFO	stacktrace	src/common/stack_trace.cpp:172	
2020-12-08 01:38:18.165	    7f4cfe1f9700	INFO	stacktrace	src/common/stack_trace.cpp:133	Exception: std::runtime_error
2020-12-08 01:38:18.165	    7f4cfe1f9700	INFO	stacktrace	src/common/stack_trace.cpp:134	Unwound call stack:
2020-12-08 01:38:18.168	    7f4cfe1f9700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [1]  0x111) [0x558e144cc181]:__wrap___cxa_throw+0x111) [0x558e144cc181]
2020-12-08 01:38:18.168	    7f4cfe1f9700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [2] ./monero/build/Linux/master/release/bin/monerod(+0x46323b) [0x558e1404023b] 
2020-12-08 01:38:18.168	    7f4cfe1f9700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [3]  0x31) [0x558e1481f651]:_ZN7randomx6VmBaseINS_18LargePageAllocatorELb0EE8allocateEv+0x31) [0x558e1481f651]
2020-12-08 01:38:18.168	    7f4cfe1f9700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [4]  0x103) [0x558e1481cb93]:_create_vm+0x103) [0x558e1481cb93]
2020-12-08 01:38:18.168	    7f4cfe1f9700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [5]  0x49c) [0x558e14483d1c]:_slow_hash+0x49c) [0x558e14483d1c]
2020-12-08 01:38:18.168	    7f4cfe1f9700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [6]  0xe6) [0x558e1446cad6]:_ZN10cryptonote18get_block_longhashEPKNS_10BlockchainERKNS_5blockERN6crypto4hashEmPKS7_i+0xe6) [0x558e1446cad6]
2020-12-08 01:38:18.168	    7f4cfe1f9700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [7]  0x21) [0x558e1446cca1]:_ZN10cryptonote18get_block_longhashEPKNS_10BlockchainERKNS_5blockEmi+0x21) [0x558e1446cca1]
2020-12-08 01:38:18.168	    7f4cfe1f9700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [8]  0xa9) [0x558e14418fe9]:_ZNK10cryptonote10Blockchain21block_longhash_workerEmRKN4epee4spanIKNS_5blockEEERSt13unordered_mapIN6crypto4hashESA_St4hashISA_ESt8equal_toISA_ESaISt4pairIKSA_SA_EEE+0xa9) [0x558e14418fe9]
2020-12-08 01:38:18.168	    7f4cfe1f9700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [9]  0x4d1) [0x558e144c4fb1]:_ZN5tools10threadpool3runEb+0x4d1) [0x558e144c4fb1]
2020-12-08 01:38:18.168	    7f4cfe1f9700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [10] ./monero/build/Linux/master/release/bin/monerod(+0xea44f5) [0x558e14a814f5] 
2020-12-08 01:38:18.168	    7f4cfe1f9700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [11]  0x7fa3) [0x7f67386c9fa3]:_64-linux-gnu/libpthread.so.0(+0x7fa3) [0x7f67386c9fa3]
2020-12-08 01:38:18.168	    7f4cfe1f9700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [12]  0x3f) [0x7f67385fa4cf]:_64-linux-gnu/libc.so.6(clone+0x3f) [0x7f67385fa4cf]
2020-12-08 01:38:18.168	    7f4cfe1f9700	INFO	stacktrace	src/common/stack_trace.cpp:172	
2020-12-08 01:38:41.690	[P2P2]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1627	Synced 2247350/2247350
2020-12-08 01:38:41.690	[P2P2]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:2368	SYNCHRONIZED OK
2020-12-08 01:38:41.690	[P2P2]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:2408	
2020-12-08 01:38:41.690	[P2P2]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:2408	**********************************************************************
2020-12-08 01:38:41.690	[P2P2]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:2408	You are now synchronized with the network. You may now start monero-wallet-cli.
2020-12-08 01:38:41.690	[P2P2]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:2408	
2020-12-08 01:38:41.690	[P2P2]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:2408	Use the "help" command to see the list of available commands.
2020-12-08 01:38:41.690	[P2P2]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:2408	**********************************************************************
2020-12-08 01:38:42.102	    7f4cfcdf5700	INFO	stacktrace	src/common/stack_trace.cpp:133	Exception: std::runtime_error
2020-12-08 01:38:42.102	    7f4cfcdf5700	INFO	stacktrace	src/common/stack_trace.cpp:134	Unwound call stack:
2020-12-08 01:38:42.107	    7f4cfcdf5700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [1]  0x111) [0x558e144cc181]:__wrap___cxa_throw+0x111) [0x558e144cc181]
2020-12-08 01:38:42.107	    7f4cfcdf5700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [2] ./monero/build/Linux/master/release/bin/monerod(+0x46323b) [0x558e1404023b] 
2020-12-08 01:38:42.107	    7f4cfcdf5700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [3]  0x31) [0x558e1481f651]:_ZN7randomx6VmBaseINS_18LargePageAllocatorELb0EE8allocateEv+0x31) [0x558e1481f651]
2020-12-08 01:38:42.107	    7f4cfcdf5700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [4]  0x103) [0x558e1481cb93]:_create_vm+0x103) [0x558e1481cb93]
2020-12-08 01:38:42.107	    7f4cfcdf5700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [5]  0x49c) [0x558e14483d1c]:_slow_hash+0x49c) [0x558e14483d1c]
2020-12-08 01:38:42.107	    7f4cfcdf5700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [6]  0xe6) [0x558e1446cad6]:_ZN10cryptonote18get_block_longhashEPKNS_10BlockchainERKNS_5blockERN6crypto4hashEmPKS7_i+0xe6) [0x558e1446cad6]
2020-12-08 01:38:42.107	    7f4cfcdf5700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [7]  0x21) [0x558e1446cca1]:_ZN10cryptonote18get_block_longhashEPKNS_10BlockchainERKNS_5blockEmi+0x21) [0x558e1446cca1]
2020-12-08 01:38:42.107	    7f4cfcdf5700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [8]  0xa9) [0x558e14418fe9]:_ZNK10cryptonote10Blockchain21block_longhash_workerEmRKN4epee4spanIKNS_5blockEEERSt13unordered_mapIN6crypto4hashESA_St4hashISA_ESt8equal_toISA_ESaISt4pairIKSA_SA_EEE+0xa9) [0x558e14418fe9]
2020-12-08 01:38:42.107	    7f4cfcdf5700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [9]  0x4d1) [0x558e144c4fb1]:_ZN5tools10threadpool3runEb+0x4d1) [0x558e144c4fb1]
2020-12-08 01:38:42.107	    7f4cfcdf5700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [10] ./monero/build/Linux/master/release/bin/monerod(+0xea44f5) [0x558e14a814f5] 
2020-12-08 01:38:42.107	    7f4cfcdf5700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [11]  0x7fa3) [0x7f67386c9fa3]:_64-linux-gnu/libpthread.so.0(+0x7fa3) [0x7f67386c9fa3]
2020-12-08 01:38:42.107	    7f4cfcdf5700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [12]  0x3f) [0x7f67385fa4cf]:_64-linux-gnu/libc.so.6(clone+0x3f) [0x7f67385fa4cf]
2020-12-08 01:38:42.107	    7f4cfcdf5700	INFO	stacktrace	src/common/stack_trace.cpp:172	
2020-12-08 01:38:44.422	[P2P7]	ERROR	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:577	Unable to send transaction(s) via Dandelion++ stem


# Discussion History
## selsta | 2020-12-08T02:03:04+00:00
Can you post the output of "status" and "sync_info" ?

## ghost | 2020-12-08T02:19:34+00:00
> Can you post the output of "status" and "sync_info" ?

I've seen this error some times, restarted will be ok.
this is from log:
2020-12-08 01:39:20.867	    7f4d16ffd700	INFO	msgwriter	src/common/scoped_message_writer.h:102	Height: 2247351, target: 2247351 (100%)
2020-12-08 01:39:20.867	    7f4d16ffd700	INFO	msgwriter	src/common/scoped_message_writer.h:102	Downloading at 15 kB/s
2020-12-08 01:39:20.867	    7f4d16ffd700	INFO	msgwriter	src/common/scoped_message_writer.h:102	16 peers
2020-12-08 01:39:20.867	    7f4d16ffd700	INFO	msgwriter	src/common/scoped_message_writer.h:102	96.253.127.130:18080      3269913a94068815  normal            0         1398608  1 kB/s, 0 blocks / 0 MB queued
2020-12-08 01:39:20.867	    7f4d16ffd700	INFO	msgwriter	src/common/scoped_message_writer.h:102	176.107.178.164:18080     51ea288ac8fcc55e  normal            0         2247351  1 kB/s, 0 blocks / 0 MB queued
2020-12-08 01:39:20.867	    7f4d16ffd700	INFO	msgwriter	src/common/scoped_message_writer.h:102	24.10.95.70:18080         6aaefd67fb97c690  normal            0         2247351  1 kB/s, 0 blocks / 0 MB queued
2020-12-08 01:39:20.867	    7f4d16ffd700	INFO	msgwriter	src/common/scoped_message_writer.h:102	159.253.175.92:18080      222af9a04159860e  normal            0         2247351  1 kB/s, 0 blocks / 0 MB queued
2020-12-08 01:39:20.867	    7f4d16ffd700	INFO	msgwriter	src/common/scoped_message_writer.h:102	167.71.57.44:18080        356758c6454db863  normal            0         2247351  1 kB/s, 0 blocks / 0 MB queued
2020-12-08 01:39:20.867	    7f4d16ffd700	INFO	msgwriter	src/common/scoped_message_writer.h:102	24.21.94.251:18080        06cf8db2e44254e1  normal            0         2247351  1 kB/s, 0 blocks / 0 MB queued
2020-12-08 01:39:20.867	    7f4d16ffd700	INFO	msgwriter	src/common/scoped_message_writer.h:102	159.69.60.223:18080       e85e5b2b854a4d80  normal            0         1  0 kB/s, 0 blocks / 0 MB queued
2020-12-08 01:39:20.867	    7f4d16ffd700	INFO	msgwriter	src/common/scoped_message_writer.h:102	75.113.64.220:18080       a2992d8c2fee78d9  normal            0         2203581  1 kB/s, 0 blocks / 0 MB queued
2020-12-08 01:39:20.867	    7f4d16ffd700	INFO	msgwriter	src/common/scoped_message_writer.h:102	98.116.55.35:18080        0339bb4b5467c2bc  normal            0         2247022  1 kB/s, 0 blocks / 0 MB queued
2020-12-08 01:39:20.867	    7f4d16ffd700	INFO	msgwriter	src/common/scoped_message_writer.h:102	165.227.4.64:18080        b1f08964b92a32f0  normal            0         2247350  1 kB/s, 0 blocks / 0 MB queued
2020-12-08 01:39:20.867	    7f4d16ffd700	INFO	msgwriter	src/common/scoped_message_writer.h:102	46.190.32.26:18080        59a52e6152515625  normal            0         2247351  1 kB/s, 0 blocks / 0 MB queued
2020-12-08 01:39:20.867	    7f4d16ffd700	INFO	msgwriter	src/common/scoped_message_writer.h:102	173.44.114.122:18080      d4f0821206eb08cf  normal            0         2247351  1 kB/s, 0 blocks / 0 MB queued
2020-12-08 01:39:20.867	    7f4d16ffd700	INFO	msgwriter	src/common/scoped_message_writer.h:102	97.75.139.86:18080        572eeba6381018c0  normal            0         2247350  1 kB/s, 0 blocks / 0 MB queued
2020-12-08 01:39:20.867	    7f4d16ffd700	INFO	msgwriter	src/common/scoped_message_writer.h:102	216.18.178.238:18080      da8bb443cb6c3739  normal            0         2247350  1 kB/s, 0 blocks / 0 MB queued
2020-12-08 01:39:20.867	    7f4d16ffd700	INFO	msgwriter	src/common/scoped_message_writer.h:102	47.205.66.164:18080       1d9d08db8e7b23f6  normal            0         2247350  1 kB/s, 0 blocks / 0 MB queued
2020-12-08 01:39:20.868	    7f4d16ffd700	INFO	msgwriter	src/common/scoped_message_writer.h:102	95.217.1.205:18080        0d4fbeb50e1b5589  normal            0         2247350  1 kB/s, 0 blocks / 0 MB queued
2020-12-08 01:39:20.868	    7f4d16ffd700	INFO	msgwriter	src/common/scoped_message_writer.h:102	0 spans, 0 MB

## selsta | 2021-10-06T02:49:18+00:00
Should not be an issue anymore with v0.17.2.3

# Action History
- Created by: ghost | 2020-12-08T02:00:38+00:00
- Closed at: 2021-10-06T02:49:18+00:00
