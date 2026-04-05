---
title: xeon phi optimizations
source_url: https://github.com/xmrig/xmrig/issues/1405
author: xrataj00
assignees: []
labels:
- question
created_at: '2019-12-11T20:16:14+00:00'
updated_at: '2019-12-21T19:46:02+00:00'
type: issue
status: closed
closed_at: '2019-12-21T19:46:02+00:00'
---

# Original Description
Hello, are there any possible optimizations of randomx for xeon phi x200? Are any if its features like AVX512 any help here? Thanks.  

# Discussion History
## tevador | 2019-12-12T17:39:00+00:00
RandomX only uses 128-bit SIMD, so anything wider than SSE2 is not useful (including AVX and AVX512). The Xeon Phis also don't have sufficient on-chip cache and their core clock is very low. I'd be surprised if any substantial optimizations were possible.

# Action History
- Created by: xrataj00 | 2019-12-11T20:16:14+00:00
- Closed at: 2019-12-21T19:46:02+00:00
