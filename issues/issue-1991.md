---
title: Apple M1 processor
source_url: https://github.com/xmrig/xmrig/issues/1991
author: xmrig
assignees: []
labels:
- META
- randomx
created_at: '2020-12-21T10:24:40+00:00'
updated_at: '2021-05-26T15:33:16+00:00'
type: issue
status: closed
closed_at: '2021-04-12T14:27:38+00:00'
---

# Original Description
v5.7.0 brings official support for Apple M1 processor on macOS for [compile from source](https://xmrig.com/docs/miner/build/macos) and binary downloads.
ARMv8 architecture is already supported, but macOS disallows fast Just-In-Time (JIT) compiler support required for RandomX, so [secure JIT mode](https://developer.apple.com/documentation/apple_silicon/porting_just-in-time_compilers_to_apple_silicon?language=objc) was added, it has negative performance impact.

Hashrate slightly above 2300 H/s https://xmrig.com/benchmark?cpu=Apple+M1 + [Reddit discussion
](https://www.reddit.com/r/MoneroMining/comments/keg3ch/apple_m1_hashes_2330_hs_175_watts/)

ARM macOS has the following disadvantages which reduce the hashrate:

* Enforced Hardened Runtime, it means RandomX JIT compiler can work only in slow secure mode.
* Any kind of CPU affinity not supported.
* Huge pages not supported.

# Discussion History
## iComUA | 2021-01-02T22:52:17+00:00
why does not it work Apple M1 GPU?
when turned on OpenCL I get an error

## neucc1997 | 2021-01-11T06:41:52+00:00
> why does not it work Apple M1 GPU?
> when turned on OpenCL I get an error

Because OpenCL is special for AMD GPUs for mining. According to the section "Beckends" from the site: https://xmrig.com/wizard

## ghost | 2021-01-12T23:47:57+00:00
Is there no way to enable the JIT entitlement? 

## xmrig | 2021-01-13T13:07:58+00:00
@SpiritedByte You can create Xcode project by adding `-G Xcode` to cmake command and change entitlements, but all it useless on ARM.
Thank you.

## AndyRPH | 2021-03-01T02:54:43+00:00
Apple's documentation seems to say that you can waive the hardened runtime issues and allow JIT code to create, write, and execute memory.  Is there more that is needed to allow randomX to run in fast mode beyond the first two entitlements listed in this doc?   

https://developer.apple.com/documentation/security/hardened_runtime


## rovo79 | 2021-05-26T15:12:05+00:00
@xmrig
Recent RandomX release improves execution related to JIT limitations on M1?

https://github.com/tevador/RandomX/releases/tag/v1.1.9

> Benchmark v1.1.9
> This release brings support for the new ARM-based Apple silicon and a small speed-up for all CPUs.
> 
> Full list of changes:
> 
> Apple silicon: force W^X, enable hardware AES #198
> Remove unnecessary first-load initialization code #201
> Fix illegal instruction crash on some ARM systems #202
> Optimized dataset read #211
> Faster W^X policy for apple silicon macs #212
> Fix typo for M1 Mac build #213
> 

## SChernykh | 2021-05-26T15:24:58+00:00
It's all already implemented in xmrig.

## rovo79 | 2021-05-26T15:27:46+00:00
@SChernykh I didn't realize. I thought because v1.19 was released 4 days ago, it hadn't made its way into XMrig yet.

## SChernykh | 2021-05-26T15:30:42+00:00
xmrig uses its own implementation which diverged from tevador's repository long time ago.

## rovo79 | 2021-05-26T15:33:16+00:00
> xmrig uses its own implementation which diverged from tevador's repository long time ago.

TodayILearned

# Action History
- Created by: xmrig | 2020-12-21T10:24:40+00:00
- Closed at: 2021-04-12T14:27:38+00:00
