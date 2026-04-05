---
title: More Apple M1 improvements possible
source_url: https://github.com/xmrig/xmrig/issues/2529
author: risner
assignees: []
labels: []
created_at: '2021-08-11T01:09:13+00:00'
updated_at: '2021-08-12T21:48:57+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Astrobwt only has AVX2 assembly?
https://github.com/xmrig/xmrig/tree/master/src/crypto/astrobwt

Argon only has x86?
https://github.com/xmrig/xmrig/tree/master/src/3rdparty/argon2/arch

These two don’t seem to have arm or SIMD/Neon instructions?


# Discussion History
## risner | 2021-08-11T15:45:32+00:00
@Spudz76 Do you know enough about these two (Astrobwt/Argon) to confirm they are not yet optimized on M1 ARM?

## Spudz76 | 2021-08-12T06:10:50+00:00
Likely aren't; I think last time I was through there everything ARM was reference code (no ASM).

## risner | 2021-08-12T07:30:52+00:00
https://github.com/turtlecoin/violetminer
This argon2id seems to have arm neon code?
GPL3

https://github.com/deroproject/astrobwt/tree/master/vendor/golang.org/x/crypto
This go Project has salsa20 and other .s files for arm?
BSD3clause

## risner | 2021-08-12T21:48:57+00:00
Just found this too:
https://simd-everywhere.github.io/blog/2020/06/22/transitioning-to-arm-with-simde.html

That is an Intel SSE/AVX to NEON package that:
"With almost no source code changes, you can recompile your x86 SIMD code for Arm (or POWER, or WebAssembly, etc.)."

So that might make it easy?

# Action History
- Created by: risner | 2021-08-11T01:09:13+00:00
