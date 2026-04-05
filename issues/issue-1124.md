---
title: What is the best GCC compiler and compiler options for compiling XMrig 3.0.0
source_url: https://github.com/xmrig/xmrig/issues/1124
author: kio3i0j9024vkoenio
assignees: []
labels:
- review later
created_at: '2019-08-17T19:38:06+00:00'
updated_at: '2019-08-28T23:59:04+00:00'
type: issue
status: closed
closed_at: '2019-08-28T23:59:04+00:00'
---

# Original Description
As seen in another issue:
https://github.com/xmrig/xmrig/issues/1122#issuecomment-522254002

using the compiler option "-funroll-loops" speeds up BLAKE2b by 40%.

So my question is what is the best GCC compiler to use for compiling XMrig 3.0.0?

and what are the best compiler options to use?

Obviously I am looking to have the fastest XMrig RandomX implementations on my various rigs:

Opteron 63xx Servers, HP Xeon 8837 Servers, etc


# Discussion History
## xmrig | 2019-08-17T20:00:17+00:00
Whole Argon2/Blake2 not performance critical as it answered, in upcoming v3.1.0 Argon2 added as standalone algorithm with up to AVX512F optimizations #1107 but RandomX still use old/reference implementation, also use AVX2 for RandomX might be bad idea https://software.intel.com/en-us/forums/intel-isa-extensions/topic/710248 also compiler version is not important too.
Thank you.

## kio3i0j9024vkoenio | 2019-08-17T20:08:26+00:00
What about compiler options?

If using the compiler option "-funroll-loops" speeds up BLAKE2b by 40% doesn't that mean that certain options can improve RandomX's speed?


## xmrig | 2019-08-17T20:18:49+00:00
You can add it here https://github.com/xmrig/xmrig/blob/master/cmake/flags.cmake#L18 but if blake2b will get 200% (any number here) speedup it's still nothing, it not performance critical part of algorithm.

## kio3i0j9024vkoenio | 2019-08-28T23:58:45+00:00
Doing "-funroll-loops" speeds up 4x Xeon E7-8837's by 200 H/s which is a gain of 2.3%.
On 4x Opteron 6387's there is no change.

# Action History
- Created by: kio3i0j9024vkoenio | 2019-08-17T19:38:06+00:00
- Closed at: 2019-08-28T23:59:04+00:00
