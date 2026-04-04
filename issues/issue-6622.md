---
title: monerod throws errors
source_url: https://github.com/monero-project/monero/issues/6622
author: kulak
assignees: []
labels: []
created_at: '2020-06-02T16:46:17+00:00'
updated_at: '2020-06-05T05:54:24+00:00'
type: issue
status: closed
closed_at: '2020-06-05T05:54:24+00:00'
---

# Original Description
On:

```
Linux horse2 5.6.15-1-MANJARO #1 SMP PREEMPT Wed May 27 20:38:56 UTC 2020 x86_64 GNU/Linux
```

I'd like to point out that it is the current monero package from official Manjaro repository at version:

```
Monero 'Nitrogen Nebula' (v0.16.0.0-release)
```

The system was syncing and it seems to have reached 99% and then I've got this:

```
2020-06-01 23:16:10.009 [P2P8]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1582    Synced 2092512/2111421 (99%, 18909 left)
2020-06-01 23:16:12.462 [P2P8]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1582    Synced 2092532/2111421 (99%, 18889 left, 83% of total synced, estimated 14.8 minutes left)
2020-06-01 23:16:13.199     7f97426fa700        INFO    stacktrace      src/common/stack_trace.cpp:133  Exception: std::runtime_error
2020-06-01 23:16:13.199     7f97426fa700        INFO    stacktrace      src/common/stack_trace.cpp:134  Unwound call stack:
2020-06-01 23:16:14.319     7f97426fa700        INFO    stacktrace      src/common/stack_trace.cpp:172      [1]  0x119) [0x56477b57b44c]:__cxa_throw+0x119) [0x56477b57b44c]
2020-06-01 23:16:14.319     7f97426fa700        INFO    stacktrace      src/common/stack_trace.cpp:172      [2] /usr/bin/monerod(+0x37215e) [0x56477b5c015e] 
2020-06-01 23:16:14.319     7f97426fa700        INFO    stacktrace      src/common/stack_trace.cpp:172      [3]  0x198) [0x56477bc46ca8]:_alloc_cache+0x198) [0x56477bc46ca8]
2020-06-01 23:16:14.319     7f97426fa700        INFO    stacktrace      src/common/stack_trace.cpp:172      [4]  0x2ac) [0x56477ba6a34c]:_slow_hash+0x2ac) [0x56477ba6a34c]
2020-06-01 23:16:14.319     7f97426fa700        INFO    stacktrace      src/common/stack_trace.cpp:172      [5]  0xb9) [0x56477ba531c9]:_ZN10cryptonote18get_block_longhashEPKNS_10BlockchainERKNS_5blockERN6crypto4hashEmi+0xb9) [0x56477ba531c9]
2020-06-01 23:16:14.319     7f97426fa700        INFO    stacktrace      src/common/stack_trace.cpp:172      [6]  0x27) [0x56477ba53337]:_ZN10cryptonote18get_block_longhashEPKNS_10BlockchainERKNS_5blockEmi+0x27) [0x56477ba53337]
2020-06-01 23:16:14.320     7f97426fa700        INFO    stacktrace      src/common/stack_trace.cpp:172      [7]  0xb7) [0x56477b9f7697]:_ZNK10cryptonote10Blockchain21block_longhash_workerEmRKN4epee4spanIKNS_5blockEEERSt13unordered_mapIN6crypto4hashESA_St4hashISA_ESt8equal_toISA_ESaISt4pairIKSA_SA_EEE+0xb7) [0x56477b9f7697]
2020-06-01 23:16:14.320     7f97426fa700        INFO    stacktrace      src/common/stack_trace.cpp:172      [8]  0x43a) [0x56477baad45a]:_ZN5tools10threadpool3runEb+0x43a) [0x56477baad45a]
2020-06-01 23:16:14.320     7f97426fa700        INFO    stacktrace      src/common/stack_trace.cpp:172      [9]  0x11857) [0x7fa9cb99d857]:_thread.so.1.72.0(+0x11857) [0x7fa9cb99d857]
2020-06-01 23:16:14.320     7f97426fa700        INFO    stacktrace      src/common/stack_trace.cpp:172      [10] /usr/lib/libpthread.so.0(+0x9422) [0x7fa9cb2c8422] 
2020-06-01 23:16:14.320     7f97426fa700        INFO    stacktrace      src/common/stack_trace.cpp:172      [11] /usr/lib/libc.so.6(clone+0x43) [0x7fa9cb1f7bf3] 
2020-06-01 23:16:14.320     7f97426fa700        INFO    stacktrace      src/common/stack_trace.cpp:172  
2020-06-01 23:16:16.119     7f97426fa700        INFO    stacktrace      src/common/stack_trace.cpp:133  Exception: std::runtime_error
2020-06-01 23:16:16.119     7f97426fa700        INFO    stacktrace      src/common/stack_trace.cpp:134  Unwound call stack:
2020-06-01 23:16:16.240     7f97426fa700        INFO    stacktrace      src/common/stack_trace.cpp:172      [1]  0x119) [0x56477b57b44c]:__cxa_throw+0x119) [0x56477b57b44c]
2020-06-01 23:16:16.240     7f97426fa700        INFO    stacktrace      src/common/stack_trace.cpp:172      [2] /usr/bin/monerod(+0x37215e) [0x56477b5c015e] 
2020-06-01 23:16:16.240     7f97426fa700        INFO    stacktrace      src/common/stack_trace.cpp:172      [3]  0x1c) [0x56477bc4988c]:_ZN7randomx6VmBaseINS_18LargePageAllocatorELb1EE8allocateEv+0x1c) [0x56477bc4988c]
2020-06-01 23:16:16.240     7f97426fa700        INFO    stacktrace      src/common/stack_trace.cpp:172      [4]  0xef) [0x56477bc46f2f]:_create_vm+0xef) [0x56477bc46f2f]
2020-06-01 23:16:16.240     7f97426fa700        INFO    stacktrace      src/common/stack_trace.cpp:172      [5]  0x471) [0x56477ba6a511]:_slow_hash+0x471) [0x56477ba6a511]
2020-06-01 23:16:16.240     7f97426fa700        INFO    stacktrace      src/common/stack_trace.cpp:172      [6]  0xb9) [0x56477ba531c9]:_ZN10cryptonote18get_block_longhashEPKNS_10BlockchainERKNS_5blockERN6crypto4hashEmi+0xb9) [0x56477ba531c9]
2020-06-01 23:16:16.240     7f97426fa700        INFO    stacktrace      src/common/stack_trace.cpp:172      [7]  0x27) [0x56477ba53337]:_ZN10cryptonote18get_block_longhashEPKNS_10BlockchainERKNS_5blockEmi+0x27) [0x56477ba53337]
2020-06-01 23:16:16.240     7f97426fa700        INFO    stacktrace      src/common/stack_trace.cpp:172      [8]  0xb7) [0x56477b9f7697]:_ZNK10cryptonote10Blockchain21block_longhash_workerEmRKN4epee4spanIKNS_5blockEEERSt13unordered_mapIN6crypto4hashESA_St4hashISA_ESt8equal_toISA_ESaISt4pairIKSA_SA_EEE+0xb7) [0x56477b9f7697]
2020-06-01 23:16:16.240     7f97426fa700        INFO    stacktrace      src/common/stack_trace.cpp:172      [9]  0x43a) [0x56477baad45a]:_ZN5tools10threadpool3runEb+0x43a) [0x56477baad45a]
2020-06-01 23:16:16.241     7f97426fa700        INFO    stacktrace      src/common/stack_trace.cpp:172      [10]  0x11857) [0x7fa9cb99d857]:_thread.so.1.72.0(+0x11857) [0x7fa9cb99d857]
2020-06-01 23:16:16.241     7f97426fa700        INFO    stacktrace      src/common/stack_trace.cpp:172      [11] /usr/lib/libpthread.so.0(+0x9422) [0x7fa9cb2c8422] 
2020-06-01 23:16:16.241     7f97426fa700        INFO    stacktrace      src/common/stack_trace.cpp:172      [12] /usr/lib/libc.so.6(clone+0x43) [0x7fa9cb1f7bf3] 
2020-06-01 23:16:16.241     7f97426fa700        INFO    stacktrace      src/common/stack_trace.cpp:172  
2020-06-01 23:16:16.241     7f9742bfb700        INFO    stacktrace      src/common/stack_trace.cpp:133  Exception: std::runtime_error
2020-06-01 23:16:16.241     7f9742bfb700        INFO    stacktrace      src/common/stack_trace.cpp:134  Unwound call stack:
2020-06-01 23:16:16.243     7f9742bfb700        INFO    stacktrace      src/common/stack_trace.cpp:172      [1]  0x119) [0x56477b57b44c]:__cxa_throw+0x119) [0x56477b57b44c]
2020-06-01 23:16:16.243     7f9742bfb700        INFO    stacktrace      src/common/stack_trace.cpp:172      [2] /usr/bin/monerod(+0x37215e) [0x56477b5c015e] 
2020-06-01 23:16:16.243     7f9742bfb700        INFO    stacktrace      src/common/stack_trace.cpp:172      [3]  0x1c) [0x56477bc4988c]:_ZN7randomx6VmBaseINS_18LargePageAllocatorELb1EE8allocateEv+0x1c) [0x56477bc4988c]
2020-06-01 23:16:16.243     7f9742bfb700        INFO    stacktrace      src/common/stack_trace.cpp:172      [4]  0xef) [0x56477bc46f2f]:_create_vm+0xef) [0x56477bc46f2f]
2020-06-01 23:16:16.243     7f9742bfb700        INFO    stacktrace      src/common/stack_trace.cpp:172      [5]  0x471) [0x56477ba6a511]:_slow_hash+0x471) [0x56477ba6a511]
2020-06-01 23:16:16.243     7f9742bfb700        INFO    stacktrace      src/common/stack_trace.cpp:172      [6]  0xb9) [0x56477ba531c9]:_ZN10cryptonote18get_block_longhashEPKNS_10BlockchainERKNS_5blockERN6crypto4hashEmi+0xb9) [0x56477ba531c9]
2020-06-01 23:16:16.243     7f9742bfb700        INFO    stacktrace      src/common/stack_trace.cpp:172      [7]  0x27) [0x56477ba53337]:_ZN10cryptonote18get_block_longhashEPKNS_10BlockchainERKNS_5blockEmi+0x27) [0x56477ba53337]
2020-06-01 23:16:16.243     7f9742bfb700        INFO    stacktrace      src/common/stack_trace.cpp:172      [8]  0xb7) [0x56477b9f7697]:_ZNK10cryptonote10Blockchain21block_longhash_workerEmRKN4epee4spanIKNS_5blockEEERSt13unordered_mapIN6crypto4hashESA_St4hashISA_ESt8equal_toISA_ESaISt4pairIKSA_SA_EEE+0xb7) [0x56477b9f7697]
2020-06-01 23:16:16.243     7f9742bfb700        INFO    stacktrace      src/common/stack_trace.cpp:172      [9]  0x43a) [0x56477baad45a]:_ZN5tools10threadpool3runEb+0x43a) [0x56477baad45a]
2020-06-01 23:16:16.243     7f9742bfb700        INFO    stacktrace      src/common/stack_trace.cpp:172      [10]  0x11857) [0x7fa9cb99d857]:_thread.so.1.72.0(+0x11857) [0x7fa9cb99d857]
```

# Discussion History
## moneromooo-monero | 2020-06-02T22:51:52+00:00
Is there an actual problem to go with these ?

## kulak | 2020-06-04T04:37:40+00:00
I installed it on old machine.  I just checked and it does not support AES encryption.  Could it be the reason for the errors?

## moneromooo-monero | 2020-06-04T11:24:22+00:00
No. You likely don't have enough RAM or don't have huge pages enabled.

## kulak | 2020-06-05T05:54:24+00:00
You are correct. It was related to huge memory configuration on Linux.

# Action History
- Created by: kulak | 2020-06-02T16:46:17+00:00
- Closed at: 2020-06-05T05:54:24+00:00
