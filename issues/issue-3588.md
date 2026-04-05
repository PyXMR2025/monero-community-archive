---
title: Certain Algorithms especially Cryptonite Variants are very sensitive to compiler
  optimization
source_url: https://github.com/xmrig/xmrig/issues/3588
author: jianmingyong
assignees: []
labels: []
created_at: '2024-11-22T01:29:54+00:00'
updated_at: '2025-06-28T10:29:11+00:00'
type: issue
status: closed
closed_at: '2025-06-28T10:29:11+00:00'
---

# Original Description
Most of the Cryptonite algorithms including UPX/2 are very sensitive to compiler optimization flags.

This had been proven to be true with linux GCC-10 onwards. The hash will not be generated correctly and thus resulting in 25% rejection rate.

If you are mining using cryptonite variant algorithm, please consider using GCC-9 and below. Alternatively you can set the crypto related C files to be compiled with -O2 flag to reduce the compiler optimization.

If you are using ubuntu, 20.04 lts provides gcc-9 by default (in build-essential). 22.04 lts provides gcc-11 so you need to manually install gcc-9 or change the compile flag to -O2 for crypto related file to ensure you aren’t mining air.

# Discussion History
# Action History
- Created by: jianmingyong | 2024-11-22T01:29:54+00:00
- Closed at: 2025-06-28T10:29:11+00:00
