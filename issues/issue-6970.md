---
title: 'sync_info  and height  exception '
source_url: https://github.com/monero-project/monero/issues/6970
author: ghost
assignees: []
labels: []
created_at: '2020-11-03T02:49:34+00:00'
updated_at: '2020-12-07T07:33:11+00:00'
type: issue
status: closed
closed_at: '2020-11-03T17:53:11+00:00'
---

# Original Description
```
sync_info
2020-11-03 02:17:13.386	E Exception at [console_handler], what=basic_string::_M_create
```

height: It's always 99% ,Never 100% (Latest-height+2? )
 ```

status
Height: 2222156/2222158 (99.9%) on mainnet, not mining, net hash 1.50 GH/s, v14, 32(out)+0(in) connections, uptime 0d 0h 3m 3s
status
Height: 2222156/2222158 (99.9%) on mainnet, not mining, net hash 1.50 GH/s, v14, 32(out)+0(in) connections, uptime 0d 0h 3m 23s
status
Height: 2222156/2222158 (99.9%) on mainnet, not mining, net hash 1.50 GH/s, v14, 32(out)+0(in) connections, uptime 0d 0h 4m 27s
status
Height: 2222156/2222158 (99.9%) on mainnet, not mining, net hash 1.50 GH/s, v14, 32(out)+0(in) connections, uptime 0d 0h 5m 6s
status
Height: 2222158/2222160 (99.9%) on mainnet, not mining, net hash 1.50 GH/s, v14, 32(out)+0(in) connections, uptime 0d 0h 9m 45s
status
Height: 2222160/2222162 (99.9%) on mainnet, not mining, net hash 1.51 GH/s, v14, 32(out)+0(in) connections, uptime 0d 0h 14m 28s
status
Height: 2222163/2222165 (99.9%) on mainnet, not mining, net hash 1.50 GH/s, v14, 32(out)+0(in) connections, uptime 0d 0h 18m 4s
status
Height: 2222164/2222166 (99.9%) on mainnet, not mining, net hash 1.50 GH/s, v14, 32(out)+0(in) connections, uptime 0d 0h 19m 4s
status
Height: 2222170/2222171 (99.9%) on mainnet, not mining, net hash 1.49 GH/s, v14, 32(out)+0(in) connections, uptime 0d 0h 27m 45s
status
Height: 2222170/2222172 (99.9%) on mainnet, not mining, net hash 1.49 GH/s, v14, 32(out)+0(in) connections, uptime 0d 0h 27m 52s

```
logs:
```
2020-11-03 02:45:36.139	    7f253d9f8700	INFO	stacktrace	src/common/stack_trace.cpp:133	Exception: std::runtime_error
2020-11-03 02:45:36.139	    7f253d9f8700	INFO	stacktrace	src/common/stack_trace.cpp:134	Unwound call stack:
2020-11-03 02:45:36.144	    7f253d9f8700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [1]  0x111) [0x55d3e54d7141]:__wrap___cxa_throw+0x111) [0x55d3e54d7141]
2020-11-03 02:45:36.144	    7f253d9f8700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [2] ./monero/build/Linux/master/release/bin/monerod(+0x4610db) [0x55d3e50570db] 
2020-11-03 02:45:36.144	    7f253d9f8700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [3]  0x31) [0x55d3e5829991]:_ZN7randomx6VmBaseINS_18LargePageAllocatorELb0EE8allocateEv+0x31) [0x55d3e5829991]
2020-11-03 02:45:36.144	    7f253d9f8700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [4]  0x103) [0x55d3e5826ed3]:_create_vm+0x103) [0x55d3e5826ed3]
2020-11-03 02:45:36.144	    7f253d9f8700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [5]  0x49c) [0x55d3e548f51c]:_slow_hash+0x49c) [0x55d3e548f51c]
2020-11-03 02:45:36.144	    7f253d9f8700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [6]  0xe6) [0x55d3e54782d6]:_ZN10cryptonote18get_block_longhashEPKNS_10BlockchainERKNS_5blockERN6crypto4hashEmPKS7_i+0xe6) [0x55d3e54782d6]
2020-11-03 02:45:36.144	    7f253d9f8700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [7]  0x21) [0x55d3e54784a1]:_ZN10cryptonote18get_block_longhashEPKNS_10BlockchainERKNS_5blockEmi+0x21) [0x55d3e54784a1]
2020-11-03 02:45:36.144	    7f253d9f8700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [8]  0xa9) [0x55d3e54246b9]:_ZNK10cryptonote10Blockchain21block_longhash_workerEmRKN4epee4spanIKNS_5blockEEERSt13unordered_mapIN6crypto4hashESA_St4hashISA_ESt8equal_toISA_ESaISt4pairIKSA_SA_EEE+0xa9) [0x55d3e54246b9]
2020-11-03 02:45:36.144	    7f253d9f8700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [9]  0x4d1) [0x55d3e54cff71]:_ZN5tools10threadpool3runEb+0x4d1) [0x55d3e54cff71]
2020-11-03 02:45:36.144	    7f253d9f8700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [10] ./monero/build/Linux/master/release/bin/monerod(+0xe954f5) [0x55d3e5a8b4f5] 
2020-11-03 02:45:36.144	    7f253d9f8700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [11]  0x7fa3) [0x7f3ef0cf4fa3]:_64-linux-gnu/libpthread.so.0(+0x7fa3) [0x7f3ef0cf4fa3]
2020-11-03 02:45:36.144	    7f253d9f8700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [12]  0x3f) [0x7f3ef0c254cf]:_64-linux-gnu/libc.so.6(clone+0x3f) [0x7f3ef0c254cf]
2020-11-03 02:45:36.144	    7f253d9f8700	INFO	stacktrace	src/common/stack_trace.cpp:172	
```

# Discussion History
## ghost | 2020-11-03T14:07:21+00:00
Now, 11 hours later , everything was back to normal and I didn't do anything.  odd!
```

status
Height: 2222446/2222448 (99.9%) on mainnet, not mining, net hash 1.45 GH/s, v14, 32(out)+0(in) connections, uptime 0d 9h  
status
Height: 2222499/2222499 (100.0%) on mainnet, not mining, net hash 1.47 GH/s, v14, 32(out)+0(in) connections, uptime 0d 11h 45m 25s

```

## moneromooo-monero | 2020-11-03T14:10:55+00:00
Probably fixed  by https://github.com/monero-project/monero/pull/6972

## ghost | 2020-11-03T15:04:27+00:00
 Is it because I connected to a bad peers? 

## moneromooo-monero | 2020-11-03T15:44:12+00:00
Yes.

## ghost | 2020-11-03T17:18:17+00:00
Also, I get a message : W Unable to send transaction(s), no available connections

edit : Only once, At the start-up monerod, maybe network problem.

## Palethorn | 2020-12-06T19:05:08+00:00
I'm still having this issue. Resynced the node, didn't help.

```
2020-12-06 19:03:33.601 I Monero 'Oxygen Orion' (v0.17.1.5-release)
Height: 2246428/2246430 (99.9%) on mainnet, not mining, net hash 1.62 GH/s, v14, 13(out)+41(in) connections, uptime 3d 8h 22m 7s
```

## Palethorn | 2020-12-07T07:33:11+00:00
Fixed by adding --ban-list on ticket #7064

# Action History
- Created by: ghost | 2020-11-03T02:49:34+00:00
- Closed at: 2020-11-03T17:53:11+00:00
