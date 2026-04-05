---
title: Hashrate dropped 30% for CNv2 on ARMv7 compared to CNv1
source_url: https://github.com/xmrig/xmrig/issues/865
author: bladeFury
assignees: []
labels:
- arm
created_at: '2018-11-02T12:37:07+00:00'
updated_at: '2018-11-05T03:23:20+00:00'
type: issue
status: closed
closed_at: '2018-11-05T03:23:20+00:00'
---

# Original Description
I've done some test, found out that the hashrate loss is due to `VARIANT2_INTEGER_MATH` macro,  this line : https://github.com/xmrig/xmrig/blob/2b0b71b9f695466f8b434fbbbcbfecfb3f9ecd60/src/crypto/CryptoNight_monero.h#L116
Seems "load" `sqrt_result_0` is very slow.  I did the following tests:

change [line 116](https://github.com/xmrig/xmrig/blob/2b0b71b9f695466f8b434fbbbcbfecfb3f9ecd60/src/crypto/CryptoNight_monero.h#L116) to `cl ^= sqrt_result_##part; \` -> slow
change [line 116](https://github.com/xmrig/xmrig/blob/2b0b71b9f695466f8b434fbbbcbfecfb3f9ecd60/src/crypto/CryptoNight_monero.h#L116) to `cl ^= 12345;\` -> fast

Could you do some optimization with this macro or give me some hint ?
@SChernykh @xmrig 

# Discussion History
## SChernykh | 2018-11-02T12:52:51+00:00
When you do `cl ^= 12345;` you basically remove integer math entirely. Compiler sees that you don't use any results and removes it from the loop.

## bladeFury | 2018-11-02T13:05:11+00:00
@SChernykh `cl ^= 12345` still calculate `cl = cl XOR 12345`, so compiler can't remove this from loop because it's changing `cl` every loop, right?
And I checked the assembly code , `movw	r2, #12345` and `eors	r1, r2` is still there.


## SChernykh | 2018-11-02T13:08:35+00:00
Compiler removes div and sqrt code completely if it sees that results are not used. This is why it gets faster.

## bladeFury | 2018-11-02T13:27:59+00:00
@SChernykh ohh I got it, Compilers are really doing a lot work, Thanks for pointing it out.

Is there any optimization possibilities for this snippet? 30% hr drop seems a lot compared to other cpus.

# Action History
- Created by: bladeFury | 2018-11-02T12:37:07+00:00
- Closed at: 2018-11-05T03:23:20+00:00
