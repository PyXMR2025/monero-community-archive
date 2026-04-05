---
title: Increase the performance of non-AES processors.
source_url: https://github.com/xmrig/xmrig/issues/631
author: sergneo
assignees: []
labels: []
created_at: '2018-05-15T10:36:01+00:00'
updated_at: '2019-03-27T14:24:29+00:00'
type: issue
status: closed
closed_at: '2019-03-27T14:24:24+00:00'
---

# Original Description
Why don't you want to optimize your code for non-AES processors using SSE4 instructions. JCE miner better performance by 30%. Can you give me a reason?

# Discussion History
## 2010phenix | 2018-05-15T12:11:43+00:00
@sergneo any source code this optimize to look on?

## xmrig | 2018-05-17T04:04:38+00:00
Usually all SSE stuff slowdown cryptonight algorithm, for hardware AES there is no choice, because AES-NI use SSE registers, for soft AES possible create fully SSE free version, it may faster. So I really skeptical about SSE4, please point where it mentioned, probably debugging helps to know used any of SSE or not, if the miner allow debugging.

Anyway reason is pretty simple, I can't delivery all in one moment from TODO, need time, there is queue and soft AES not in top priority.
Thank you.

## sergneo | 2018-05-17T05:31:18+00:00
JC miner writes that SSE4 is used, but the code it closed is not known exactly whether it is true.
```

                +--------------------------------------+
                | JC Expert Cryptonote CPU Miner 0.27e |
                +--------------------------------------+


For Windows 64-bits
Analyzing Processors topology...
Intel(R) Core(TM)2 Quad CPU Q9300 @ 2.50GHz
Assembly codename: core2_sse4
  SSE2          : Yes
  SSE3          : Yes
  SSE4          : Yes
  AES           : No
  AVX           : No
  AVX2          : No

Auto-configuration, selected CPUs will be highlighted...
Found CPU 0, with:
  L1 Cache:    32 KB
  L2 Cache:  3072 KB, shared with CPU 1
Found CPU 1, with:
  L1 Cache:    32 KB
  L2 Cache:  3072 KB, shared with CPU 0
Found CPU 2, with:
  L1 Cache:    32 KB
  L2 Cache:  3072 KB, shared with CPU 3
Found CPU 3, with:
  L1 Cache:    32 KB
  L2 Cache:  3072 KB, shared with CPU 2

Preparing 4 Mining Threads...

+-- Thread 0 config -----------------------------+
| Run on CPU:             0                      |
| Use cache:              yes                    |
| Multi-hash:             no                     |
| Assembly module:        core2_sse4             |
+------------------------------------------------+

+-- Thread 1 config -----------------------------+
| Run on CPU:             1                      |
| Use cache:              yes                    |
| Multi-hash:             no                     |
| Assembly module:        core2_sse4             |
+------------------------------------------------+

+-- Thread 2 config -----------------------------+
| Run on CPU:             2                      |
| Use cache:              yes                    |
| Multi-hash:             no                     |
| Assembly module:        core2_sse4             |
+------------------------------------------------+

+-- Thread 3 config -----------------------------+
| Run on CPU:             3                      |
| Use cache:              yes                    |
| Multi-hash:             no                     |
| Assembly module:        core2_sse4             |
+------------------------------------------------+

Cryptonight Variation: Cryptonight V7 fork of April-2018

```
Xeon E5440 2.83GHz overclocked via the bus 370MHz  
Monero7
XMRig-2.5.3 - 106 H/s
JC Expert Cryptonote CPU Miner - 137 H/s

## xmrig | 2019-03-27T14:24:24+00:00
Current versions include assembly code for such CPUs and current Monero algorithm.
Thank you.

# Action History
- Created by: sergneo | 2018-05-15T10:36:01+00:00
- Closed at: 2019-03-27T14:24:24+00:00
