---
title: xmrig-2.6.0-beta2-gcc-win64 minor bug
source_url: https://github.com/xmrig/xmrig/issues/547
author: juanpc2018
assignees: []
labels: []
created_at: '2018-04-12T16:27:15+00:00'
updated_at: '2020-08-29T04:13:27+00:00'
type: issue
status: closed
closed_at: '2020-08-29T04:13:27+00:00'
---

# Original Description
Hi,

seems xmrig-2.6.0-beta2-gcc-win64
does Not detect properly the **L2/L3** cache in the system...

for example:
i have 2x 6386 CPU´s, according to CPU-Z each **L2** has 8x2MB = 32MB, & **L3** 6MB = 12MB.

 * VERSIONS:     XMRig/2.6.0-beta2 libuv/1.19.2 gcc/7.3.0
 * HUGE PAGES:   available, enabled
 * CPU:          AMD Opteron(tm) Processor 6386 SE               (2) x64 AES-NI
 * CPU L2/L3:    **64.0 MB/24.0 MB**
 * THREADS:      16, cryptonight, av=1, donate=1%, affinity=0xAAAAAAAA
 * POOL #1:      bytecoin.uk:7777
 * COMMANDS:     hashrate, pause, resume

L1 Data: 16 x 16 KB = 256KB
L1 Instructions: 8x64 = 512KB

the proof that CPU-Z v1.83 is right, is that i can use all 32-cores, but Hash Rate does not increase.
16-core or 32-cores is the same: 1130H/s. 1190H/s Peak.
because CryptoNight v6 needs 2MB per core, and cannot mix L2 & L3 at same time.
v7 unknown.

MMX(+), SSE, SSE2, SSE3, SSSE3, SSE4.1, SSE4.2, SSE4A, x86-64, AMD-V, AES, AVX, XOP, FMA3, FMA4


# Discussion History
# Action History
- Created by: juanpc2018 | 2018-04-12T16:27:15+00:00
- Closed at: 2020-08-29T04:13:27+00:00
