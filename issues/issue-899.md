---
title: Feature Request - Support Stellite's algorithm change from Cryptonight/XTL
  to CryptonightV2 with half iterations
source_url: https://github.com/xmrig/xmrig/issues/899
author: stellitedev
assignees: []
labels:
- enhancement
created_at: '2018-12-26T21:16:48+00:00'
updated_at: '2019-03-11T02:31:24+00:00'
type: issue
status: closed
closed_at: '2019-01-23T12:33:58+00:00'
---

# Original Description

# Summary

Due to the influx of FPGAs onto our network we're forking to Cryptonight V8 with half the iterations.

# Details
We're forking from version 4 directly to version 9, from 9th block version onwards we will have Cryptonight V8 with half the iterations.

# Testing the new variant

For convenience we have already set up a testnet pool (pool.testxtl.cryptopool.space:4444), you can use the following address for testing purposes.

```
Se3EkZfYDpXhaVqyBnAkkjfM1D3RWKeEECMJtAMjCuDE1qaQyEVUqcpXg6b49fCFSeKUD7Xvtzp5nFNPrFrFBVCG1C91AmN8d
```
Hope you take our request into consideration soon as we plan to implement this onto our mainnet as soon as possible and a good amount of our miners are fond of your software.

Thank you.

# Discussion History
## xmrig | 2019-01-14T14:32:35+00:00
* Name of this algorithm is `cn/half`, alias `cn/xtlv9` is also supported for compatibility reasons. Other coin (Masari) also will use this algorithm, so neutral name is used.
* Only miner and proxy (if used) update is required, no config changes required, users can continue use variant `xtl` and `msr`, proper algorithm will be selected by block version.

Special workaround for other coins who use `cn/msr`, may need add `!` before algorithm or variant name to disable block version checking, it also work for `cn/xtl` but it doesn't mater because only Stellite use this algorithm. Example: `"variant": "!msr"`.

Note for test pool, `variant` field not required, only `algo` is enough.

## Progress
* [x] CPU miner (dev branch)
* [x] Proxy (dev branch)
* [x] AMD miner (dev branch)
* [x] NVIDIA miner (dev branch)

## xmrig | 2019-01-16T18:50:42+00:00
Electronero (ETNX) coin use block version 17, so variant for this coin must be `!msr` since v2.9.

## xmrig | 2019-01-17T06:16:02+00:00
Update to v2.9.3 required for GPU miners and CPU (if assembly code not used) due bug, C++ code was produced invalid hashes (up to 13%).

## shopglobal | 2019-03-11T02:31:24+00:00
That makes sense @xmrig and thanks for the note

# Action History
- Created by: stellitedev | 2018-12-26T21:16:48+00:00
- Closed at: 2019-01-23T12:33:58+00:00
