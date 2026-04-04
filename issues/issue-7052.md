---
title: 'Exception: std::runtime_error'
source_url: https://github.com/monero-project/monero/issues/7052
author: D4nte
assignees: []
labels: []
created_at: '2020-12-01T22:36:23+00:00'
updated_at: '2022-02-19T01:02:11+00:00'
type: issue
status: closed
closed_at: '2022-02-19T01:02:11+00:00'
---

# Original Description
Hi,

I keep getting this error every 2 minutes.

version: 3942a1cd043bb103ca05184057aea5c86e3137e5, 3942a1cd043bb103ca05184057aea5c86e3137e5

Is it expected?

```
2020-12-01 22:23:03.290     7f5f898d6700        INFO    stacktrace      src/common/stack_trace.cpp:172  
2020-12-01 22:25:55.608     7f5f898d6700        INFO    stacktrace      src/common/stack_trace.cpp:133  Exception: std::runtime_error
2020-12-01 22:25:55.609     7f5f898d6700        INFO    stacktrace      src/common/stack_trace.cpp:134  Unwound call stack:
2020-12-01 22:25:55.623     7f5f898d6700        INFO    stacktrace      src/common/stack_trace.cpp:172      [1]  0x112) [0x5579dac4f23d]:__cxa_throw+0x112) [0x5579dac4f23d]
2020-12-01 22:25:55.623     7f5f898d6700        INFO    stacktrace      src/common/stack_trace.cpp:172      [2] /usr/local/bin/monerod(+0x34df6a) [0x5579dac8ef6a] 
2020-12-01 22:25:55.623     7f5f898d6700        INFO    stacktrace      src/common/stack_trace.cpp:172      [3]  0x1f) [0x5579db3074ff]:_ZN7randomx6VmBaseINS_18LargePageAllocatorELb1EE8allocateEv+0x1f) [0x5579db3074ff]
2020-12-01 22:25:55.623     7f5f898d6700        INFO    stacktrace      src/common/stack_trace.cpp:172      [4]  0xde) [0x5579db3047ae]:_create_vm+0xde) [0x5579db3047ae]
2020-12-01 22:25:55.623     7f5f898d6700        INFO    stacktrace      src/common/stack_trace.cpp:172      [5]  0x4cc) [0x5579db0f284c]:_slow_hash+0x4cc) [0x5579db0f284c]
2020-12-01 22:25:55.623     7f5f898d6700        INFO    stacktrace      src/common/stack_trace.cpp:172      [6]  0x132) [0x5579db0db992]:_ZN10cryptonote18get_block_longhashEPKNS_10BlockchainERKNS_5blockERN6crypto4hashEmPKS7_i+0x132) [0x5579db0db992]
2020-12-01 22:25:55.623     7f5f898d6700        INFO    stacktrace      src/common/stack_trace.cpp:172      [7]  0x28) [0x5579db0dbae8]:_ZN10cryptonote18get_block_longhashEPKNS_10BlockchainERKNS_5blockEmi+0x28) [0x5579db0dbae8]
2020-12-01 22:25:55.623     7f5f898d6700        INFO    stacktrace      src/common/stack_trace.cpp:172      [8]  0xb6) [0x5579db07be26]:_ZNK10cryptonote10Blockchain21block_longhash_workerEmRKN4epee4spanIKNS_5blockEEERSt13unordered_mapIN6crypto4hashESA_St4hashISA_ESt8equal_toISA_ESaISt4pairIKSA_SA_EEE+0xb6) [0x5579db07be26]
2020-12-01 22:25:55.623     7f5f898d6700        INFO    stacktrace      src/common/stack_trace.cpp:172      [9]  0x481) [0x5579db132361]:_ZN5tools10threadpool3runEb+0x481) [0x5579db132361]
2020-12-01 22:25:55.623     7f5f898d6700        INFO    stacktrace      src/common/stack_trace.cpp:172      [10]  0x1143b) [0x7f79748d243b]:_64-linux-gnu/libboost_thread.so.1.71.0(+0x1143b) [0x7f79748d243b]
2020-12-01 22:25:55.623     7f5f898d6700        INFO    stacktrace      src/common/stack_trace.cpp:172      [11]  0x9609) [0x7f7974516609]:_64-linux-gnu/libpthread.so.0(+0x9609) [0x7f7974516609]
2020-12-01 22:25:55.623     7f5f898d6700        INFO    stacktrace      src/common/stack_trace.cpp:172      [12]  0x43) [0x7f797443d293]:_64-linux-gnu/libc.so.6(clone+0x43) [0x7f797443d293]
2020-12-01 22:25:55.623     7f5f898d6700        INFO    stacktrace      src/common/stack_trace.cpp:172
```

# Discussion History
## selsta | 2020-12-01T22:37:28+00:00
Are you mining? What hardware are you using?

## D4nte | 2020-12-02T05:21:57+00:00
Hello, not mining, just running a full node.

Running on an old nuc. I now realize it is running an hdd.
- Intel(R) Celeron(R) CPU  N2820  @ 2.13GHz
- 4GB RAM




## moneromooo-monero | 2020-12-05T18:09:48+00:00
It's fine. It's falling back on slower small pages.

## moneromooo-monero | 2020-12-06T16:14:55+00:00
https://github.com/monero-project/monero/pull/7084

## Supermath101 | 2021-03-08T03:30:17+00:00
Hello. I'm experiencing this same issue on Manjaro (Arch Linux) when attempting to run a local full node. Monero version `0.17.1.9-1` from Pacman. It was working like normal for a while, then all the sudden at like 90-something percent done downloading the blockchain, the errors happened. Even after doing `monerod exit` and starting it up again, this still happens. However, you can only see these errors in the log file. It is weird how it somehow still progresses, but way slower than before.

## selsta | 2022-02-19T01:02:11+00:00
Harmless error message, also there is a patch open to make it spam less often.

# Action History
- Created by: D4nte | 2020-12-01T22:36:23+00:00
- Closed at: 2022-02-19T01:02:11+00:00
