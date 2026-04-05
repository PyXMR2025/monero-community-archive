---
title: Optimization for 32-bit code
source_url: https://github.com/xmrig/xmrig/issues/264
author: yuhong
assignees: []
labels:
- enhancement
created_at: '2017-12-14T07:59:20+00:00'
updated_at: '2018-11-05T14:36:55+00:00'
type: issue
status: closed
closed_at: '2018-11-05T14:36:55+00:00'
---

# Original Description
Raymond mentions an optimization that can be used:
https://blogs.msdn.microsoft.com/oldnewthing/20171213-00/?p=97575
https://blogs.msdn.microsoft.com/oldnewthing/20141208-00/?p=43453

# Discussion History
## xmrig | 2017-12-15T02:35:40+00:00
Thank you looks very interesting, also part 2 now available: https://blogs.msdn.microsoft.com/oldnewthing/20171214-00/?p=97577

## yuhong | 2017-12-18T23:44:18+00:00
For fun, I did a 128-bit add using PCMPGTQ in SSE4.2:
__m128i int128addsse42(__m128i a, __m128i b)
{
	__m128i retval;
	__m128i zeros = _mm_setzero_si128();
	__m128i ones = _mm_cmpeq_epi8(zeros, zeros);
	__m128i constant = _mm_slli_epi64(ones, 63);
	retval = _mm_add_epi64(a, b);
	__m128i result = _mm_cmpgt_epi64(_mm_xor_si128(a, constant), _mm_xor_si128(retval, constant));
	retval = _mm_sub_epi64(retval, _mm_slli_si128(result, 8));
	return retval;
}
Might not be worth using though.

# Action History
- Created by: yuhong | 2017-12-14T07:59:20+00:00
- Closed at: 2018-11-05T14:36:55+00:00
