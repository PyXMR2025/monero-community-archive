---
title: Cross compiling for ARMv8 tries compiling x86 sources.
source_url: https://github.com/xmrig/xmrig/issues/1313
author: 4reeeal
assignees: []
labels:
- arm
created_at: '2019-11-25T16:42:47+00:00'
updated_at: '2019-11-25T20:41:58+00:00'
type: issue
status: closed
closed_at: '2019-11-25T20:41:58+00:00'
---

# Original Description
I have attached my [CMakeCache.txt](https://github.com/xmrig/xmrig/files/3887546/CMakeCache.txt) for review, in-case I have missed/incorrectly set any parameters.

I have gone through the flags.cmake + a couple issue threads related to mine & have added parameters such as

DARM_TARGET=8
XMRIG_ARM=ON
XMRIG_ARMv8=ON (ARMv7 trips up with "-mfpu=neon")

and of course ARM_TARGET=ON

If CMAKE_SYSTEM_NAME / VERSION affects anything at all, they're definitely incorrect according to CMake, it proceeds to build either way.

All is fine up until BasicCpuInfo.cpp (cpuid.h non-existent). I kept tweaking the source to keep the build going (I ain't care if the final bin was broke at this point), & the massive red flag that had me decide something was wrong war earlier was when it tried compiling CryptoNight_x86.h with an aarch64 compiler lol

Any suggestions? I'll try them with a fresh copy of xmrig.

# Discussion History
## xmrig | 2019-11-25T16:57:19+00:00
`ARM_TARGET=ON` it wrong, possible values is `7` and `8`, but usually don't need specify any ARM option, `ARM_TARGET` option added only as workaround if detection based on `CMAKE_SYSTEM_PROCESSOR` fails https://github.com/xmrig/xmrig/blob/master/cmake/cpu.cmake#L11

Also don't need edit any file, right way to set cmake option is `cmake .. -DARM_TARGET=8`.
Thank you.

## 4reeeal | 2019-11-25T20:41:58+00:00
Sorted; thank you for clarifying

# Action History
- Created by: 4reeeal | 2019-11-25T16:42:47+00:00
- Closed at: 2019-11-25T20:41:58+00:00
