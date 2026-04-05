---
title: Do we still have a room to optimise for cpu minig?
source_url: https://github.com/xmrig/xmrig/issues/112
author: yoyohip
assignees: []
labels: []
created_at: '2017-09-17T10:44:53+00:00'
updated_at: '2017-10-02T11:54:30+00:00'
type: issue
status: closed
closed_at: '2017-10-02T11:54:30+00:00'
---

# Original Description
Hi,
I  made 64bit optimised version of c_groestl.c .
It just change __attribute__((aligned(16))) to __declspec(align(16)) and some things to fit with your project. The source codes is opt_64 from grostl site.
Unfortunately, the exe is almost same hash as your build.
I also try to include simd virsion of blake256. it also same situation.
Do you think  we still have a way to make more faster cpu miner?
Or the codes are well tested. So we have no chance to optimise?
by the way it is just my feel, to make /md is little bit firster than /mt.
Just I want to say you. sorry  my poor english.
Thank you.

# Discussion History
## xmrig | 2017-09-17T13:29:59+00:00
It will be nice optimize these hashes, but it will increase hashrate less than 1% anyway.

95-99% of execution time takes that loop https://github.com/xmrig/xmrig/blob/master/src/crypto/CryptoNight_p.h#L327
Also SSE2 vectored  version of that loop slower that current version.

Only way to optimize calculate multiple hashes in singe thread (double already implemented), but it still limited by CPU cache.
Thank you.

# Action History
- Created by: yoyohip | 2017-09-17T10:44:53+00:00
- Closed at: 2017-10-02T11:54:30+00:00
