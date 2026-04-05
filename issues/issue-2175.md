---
title: XMRig fails to compile on armv7 on three different distros
source_url: https://github.com/xmrig/xmrig/issues/2175
author: benthetechguy
assignees: []
labels:
- bug
- arm
created_at: '2021-03-12T04:40:02+00:00'
updated_at: '2021-03-13T04:20:41+00:00'
type: issue
status: closed
closed_at: '2021-03-13T04:20:41+00:00'
---

# Original Description
**Describe the bug**
XMRig fails to compile on armv7 on ubuntu, raspbian, and arch.

**To Reproduce**
Attempt to compile XMRig with static dependencies (dependencies build fine)

**Expected behavior**
XMRig successfully compiles.

**Required data**
An excerpt of the compilation output. The full output is [attached](https://github.com/xmrig/xmrig/files/6127649/compilation-output.txt).
```
In file included from /home/ben/xmrig/src/crypto/cn/soft_aes.h:31,
                 from /home/ben/xmrig/src/crypto/cn/CryptoNight_arm.h:35,
                 from /home/ben/xmrig/src/crypto/cn/CnHash.cpp:35:
/home/ben/xmrig/src/crypto/cn/sse2neon.h: In function 'uint8x16x4_t _sse2neon_vld1q_u8_x4(const uint8_t*)':
/home/ben/xmrig/src/crypto/cn/sse2neon.h:362:12: error: 'vld1q_u8_x4' was not declared in this scope; did you mean 'vld1q_u64'?
  362 |     return vld1q_u8_x4(p);
      |            ^~~~~~~~~~~
      |            vld1q_u64
```

**Additional context**
I attempted to compile XMRig on a raspberry pi 4 with armv7 (I know it supports aarch64 but i'm compiling for other devices) and on three different distros it has failed, with the same error. Note that I compiled the depends statically (the depends compiled just fine and this error looks like it's unrelated to that).

# Discussion History
## SChernykh | 2021-03-12T07:19:58+00:00
Try to use newer GCC version (GCC 10 at least).

## benthetechguy | 2021-03-12T15:13:07+00:00
I compiled using GCC 10.2

On Fri, Mar 12, 2021, 2:20 AM SChernykh ***@***.***> wrote:

> Try to use newer GCC version (GCC 10 at least).
>
> —
> You are receiving this because you authored the thread.
> Reply to this email directly, view it on GitHub
> <https://github.com/xmrig/xmrig/issues/2175#issuecomment-797290357>, or
> unsubscribe
> <https://github.com/notifications/unsubscribe-auth/AHAEV77BVNBYDP7CDEOYEO3TDG6C3ANCNFSM4ZBR3WLQ>
> .
>


## SChernykh | 2021-03-12T15:24:54+00:00
I see the problem now, will submit a PR that fixes it soon.
Edit: fixed in https://github.com/xmrig/xmrig/pull/2177

## benthetechguy | 2021-03-13T02:50:50+00:00
Cool, when I get back to my PC i'll try to compile and see what happens.

## benthetechguy | 2021-03-13T04:20:41+00:00
Update: The build went successfully. Thanks for the quick response and pull request.

# Action History
- Created by: benthetechguy | 2021-03-12T04:40:02+00:00
- Closed at: 2021-03-13T04:20:41+00:00
