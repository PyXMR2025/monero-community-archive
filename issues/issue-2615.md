---
title: Mips64(EL) is it real?
source_url: https://github.com/xmrig/xmrig/issues/2615
author: Omnividente
assignees: []
labels: []
created_at: '2021-10-03T23:12:33+00:00'
updated_at: '2021-10-05T12:22:15+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Question in the topic. THX

# Discussion History
## Spudz76 | 2021-10-03T23:46:19+00:00
Should work, but of course untested as nobody has one.

## Spudz76 | 2021-10-03T23:47:40+00:00
Oops I was thinking ARM64

MIPS is unsupported regardless which type.  Unless the generic mining kernels happen to compile (probably will crash anyway / defaults to x86_64 if it's "not ARM" so...)

## Omnividente | 2021-10-04T00:22:15+00:00
> Oops I was thinking ARM64
> 
> MIPS is unsupported regardless which type. Unless the generic mining kernels happen to compile (probably will crash anyway / defaults to x86_64 if it's "not ARM" so...)

ARM works stably, but the speed is certainly ridiculous, 4-6kh on 128 cores :) Thanks for the answer, so I won't torment MIPS

## Spudz76 | 2021-10-04T06:22:21+00:00
Must be a bad/old ARM, [Neoverse-N1](https://xmrig.com/benchmark?cpu=ARM+Neoverse-N1) scores up around Ryzen speeds with 64 cores.

## Omnividente | 2021-10-05T12:21:29+00:00
> Should work, but of course untested as nobody has one.

When I try to build, I get an error:
`/root/xmrig/src/backend/cpu/platform/BasicCpuInfo.cpp:29:13: fatal error: cpuid.h: No such file or directory
   29 | #   include <cpuid.h>
      |             ^~~~~~~~~
compilation terminated.
`

# Action History
- Created by: Omnividente | 2021-10-03T23:12:33+00:00
