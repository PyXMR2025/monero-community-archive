---
title: RandomX Enhancement for processors with AVX but without AVX2
source_url: https://github.com/xmrig/xmrig/issues/1122
author: kio3i0j9024vkoenio
assignees: []
labels:
- question
created_at: '2019-08-17T16:54:42+00:00'
updated_at: '2019-08-17T19:31:38+00:00'
type: issue
status: closed
closed_at: '2019-08-17T19:31:38+00:00'
---

# Original Description
Any chance for RandomX speed optimizations for processors that lack AVX2 but have AVX?

Like the Opteron 6200 & 6300 Family that have SSE4, AES, AVX instructions:

AMD Opteron 6200 series microprocessor family
http://www.cpu-world.com/CPUs/Bulldozer/TYPE-Opteron%206200%20series.html

AMD Opteron 6300 series microprocessor family
http://www.cpu-world.com/CPUs/Bulldozer/TYPE-Opteron%206300%20series.html

Or the Sandy Bridge Xeon's that have SSE4, AES, AVX instructions::

Intel Xeon E5-2600 microprocessor family
http://www.cpu-world.com/CPUs/Xeon/TYPE-Xeon%20E5-2600.html




# Discussion History
## xmrig | 2019-08-17T17:03:55+00:00
RandomX don't use AVX at all.
Thank you.

## kio3i0j9024vkoenio | 2019-08-17T19:31:03+00:00
RandomX's functions Blake2 and Argon2 can use AVX2 for speeding up those functions.

See Here:

Unoptimized BLAKE2b #60
https://github.com/tevador/RandomX/issues/60

`tevador: Yes, we are using the reference implementations for both Blake2 and Argon2 since neither is performance-critical. Supporting optimized implementations may be desirable.`

However after looking at the code that is referenced:
http://bench.cr.yp.to/web-impl/amd64-cannon-crypto_hash.html

It appears that just doing compiler option "-funroll-loops" speeds up BLAKE2b by 40% which is even faster than the AVX2 implementation.

This brings up questions about what are the best compiler options for compiling XMrig 3.0.0 which I will ask in another thread.

# Action History
- Created by: kio3i0j9024vkoenio | 2019-08-17T16:54:42+00:00
- Closed at: 2019-08-17T19:31:38+00:00
