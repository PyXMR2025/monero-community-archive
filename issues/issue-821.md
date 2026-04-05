---
title: CPU huge hash drop and algorithm variation (40%)
source_url: https://github.com/xmrig/xmrig/issues/821
author: foomor
assignees: []
labels: []
created_at: '2018-10-19T10:43:50+00:00'
updated_at: '2018-11-05T15:05:36+00:00'
type: issue
status: closed
closed_at: '2018-11-05T15:05:36+00:00'
---

# Original Description
Hi,
Testing most xmr miners with v7 and v8 there is a huge impact after v8 around 40% down.

With v7 on  Xeon E5-2670 v2 (25MB L3 cache) I was able to utilitze x5 cache (--av=7) and get best performance.
With v7 I am getting best performance at x2 cache (--av=2)

2 Threads, cpu affinity 0,1 core
v7:

2T av=7: **326**H/s (20MB)
2T av=6: 299H/s (16MB)
2T av=5: 261H/s (12MB)
2T av=2: 206H/s (8MB)

v8:

2T av=7: 135H/s (20MB)
2T av=6: 137H/s (16MB)
2T av=5: 133H/s (12MB)
2T av=2: **197**H/s (8MB)

This is on 2.8.1
Similar results with latest xmr-stack and xmrigCC


# Discussion History
## xmrig | 2018-10-19T11:14:01+00:00
Actually all answered in another issue in another miner repository, I saw your comment, in additional only av=1 and av=2 use special fast ASM implementations for `cn/2`, other av use slow C++ implementation.
Thank you.

## foomor | 2018-10-19T11:59:19+00:00
thanks for the reply,

Yes I saw the other thread after I've posted here.

In v7, asm optimizations makes no significant difference (or there is no code for that).

What you mean (and what SChernykh means) is that asm optimizations on v8 are only ready up to x2 cache? Are there plans to extend it?

thanks again

## xmrig | 2018-10-20T05:01:39+00:00
Exactly right asm optimizations only ready up to x2, @SChernykh have plans to extend it, need more time, but everyone should prepared for worst case: hashrate will never fully recovered in this usage case.
Thank you.

# Action History
- Created by: foomor | 2018-10-19T10:43:50+00:00
- Closed at: 2018-11-05T15:05:36+00:00
