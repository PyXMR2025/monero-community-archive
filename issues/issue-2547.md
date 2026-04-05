---
title: 'code-optimization '
source_url: https://github.com/xmrig/xmrig/issues/2547
author: ghost
assignees: []
labels: []
created_at: '2021-08-18T21:55:29+00:00'
updated_at: '2025-06-16T20:51:25+00:00'
type: issue
status: closed
closed_at: '2025-06-16T20:51:25+00:00'
---

# Original Description
focused on CN/0 [Intel Atom X5 Z8350 64bit]

performance increase from ~18H/s to min. 21H/s on specific CPU above (and don't *lol* - increase of ~17%)

`
template<Algorithm::Id ALGO, bool SOFT_AES, int interleave>
inline void cryptonight_single_hash(const uint8_t *__restrict__ input, size_t size, uint8_t *__restrict__ output, cryptonight_ctx **__restrict__ ctx, uint64_t height)
{
 ...
 cryptonight_hash_performance(...);
 ...
}
`

Just for test purposes separated in a function ...

`
inline void cryptonight_hash_performance(__m128i _ax0, __m128i _bx0, uint8_t *_l0, size_t _iterations, size_t _mask /*2MB*/) `{

	__m128i chcl;
	
	uint64_t* al0 = (uint64_t*)&_ax0;
	uint64_t* ah0 = ((uint64_t*)&_ax0) + 1;
	
	uint64_t idx0 = *al0;
	
	__m128i cx;
	uint64_t* pcx = (uint64_t*)&cx;

	__m128i* pAddress;
	__m128i* pSubAddress;
	uint64_t hi, lo;
	
	uint64_t* cl = (uint64_t*)&chcl;
	uint64_t* ch = ((uint64_t*)&chcl) + 1;
	
	for (size_t i = 0; i < _iterations /*524288*/; i++) {

		pAddress = reinterpret_cast</*const*/ __m128i *>(&_l0[idx0 & _mask]);

		cx = _mm_loadu_si128(pAddress);
		
		cx = _mm_aesenc_si128(cx, _ax0);
		*pAddress = _mm_xor_si128(_bx0, cx);
		pSubAddress = reinterpret_cast<__m128i *>(&_l0[/*idx0*/ *pcx & _mask]);
    		*cl = ((uint64_t*)pSubAddress)[0];
    		*ch = ((uint64_t*)pSubAddress)[1];
		
		lo = __umul128(/*idx0*/ *pcx, *cl, &hi);
	
		*al0 += hi;
		*ah0 += lo;
	
		*pSubAddress = _ax0;
	
		*al0 ^= *cl;
		*ah0 ^= *ch;
		
		idx0 = *al0;
	
		_bx0 = cx;	
	}
`
}
`

The code above helps compiling better assembly.
MSVC compiles a short and handy assembly.

/**
.text:00007FF76D35D580 loc_7FF76D35D580:                       ; CODE XREF: .text:00007FF76D35D5F9↓j
.text:00007FF76D35D580 and     eax, 1FFFF0h
.text:00007FF76D35D585 movdqu  xmm1, xmmword ptr [rax+rsi]
.text:00007FF76D35D58A aesenc  xmm1, xmm0
.text:00007FF76D35D58F movq    rcx, xmm1
.text:00007FF76D35D594 movdqa  xmm0, xmm1
.text:00007FF76D35D598 mov     r9, rcx
.text:00007FF76D35D59B pxor    xmm0, xmm2
.text:00007FF76D35D59F movdqu  xmmword ptr [rax+rsi], xmm0
.text:00007FF76D35D5A4 and     r9d, 1FFFF0h
.text:00007FF76D35D5AB movdqa  xmm2, xmm1
.text:00007FF76D35D5AF mov     r8, [r9+rsi]
.text:00007FF76D35D5B3 mov     r10, [r9+rsi+8]
.text:00007FF76D35D5B8 mov     rax, r8
.text:00007FF76D35D5BB mul     rcx
.text:00007FF76D35D5BE add     rdi, rax
.text:00007FF76D35D5C1 add     r11, rdx
.text:00007FF76D35D5C4 mov     [rsp+20h], r11
.text:00007FF76D35D5C9 xor     r11, r8
.text:00007FF76D35D5CC mov     [rsp+28h], rdi
.text:00007FF76D35D5D1 mov     rax, r11
.text:00007FF76D35D5D4 movdqa  xmm0, xmmword ptr [rsp+20h]
.text:00007FF76D35D5DA xor     rdi, r10
.text:00007FF76D35D5DD movdqu  xmmword ptr [r9+rsi], xmm0
.text:00007FF76D35D5E3 mov     [rsp+20h], r11
.text:00007FF76D35D5E8 mov     [rsp+28h], rdi
.text:00007FF76D35D5ED sub     rbp, 1
.text:00007FF76D35D5F1 jz      short loc_7FF76D35D5FB
.text:00007FF76D35D5F3 movdqa  xmm0, xmmword ptr [rsp+20h]
.text:00007FF76D35D5F9 jmp     short loc_7FF76D35D580
.text:00007FF76D35D5FB ; -------------
*/


# Discussion History
## DeeDeeRanged | 2021-08-21T11:52:31+00:00
Would it also work / compile under Linux and not just Windows?

# Action History
- Created by: ghost | 2021-08-18T21:55:29+00:00
- Closed at: 2025-06-16T20:51:25+00:00
