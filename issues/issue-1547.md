---
title: Inlining failed in call to always_inline
source_url: https://github.com/xmrig/xmrig/issues/1547
author: grahamreeds
assignees: []
labels: []
created_at: '2020-02-11T00:26:16+00:00'
updated_at: '2021-04-12T15:01:43+00:00'
type: issue
status: closed
closed_at: '2021-04-12T15:01:43+00:00'
---

# Original Description
Compilation on RPI3b+ with Raspbian-lite and arm_64bit=1 specified in config.txt.

While compiling CnHash.cpp I get the following error:
```
In file included from /home/pi/xmrig/src/crypto/cn/SSE2NEON.h:123,
                           from /home/pi/xmrig/src/crypto/cn/soft_aes.h:31,
                           from /home/pi/xmrig/src/crypto/cn/CryptoNight_arm.h:34,
                           from /home/pi/xmrig/src/crypto/cn/CnHash.cpp:35:
/usr/lib/gcc/arm-linux-gnueabihf/8/include/arm_neon.h: In function •__m128i _mm_set_epi32(int, int, int, int)•:
/usr/lib/gcc/arm-linux-gnueabihf/8/include/arm_neon.h:10369:1: error: inlining failed in call to always_inline •int32x4_t vld1q_s32(const int32_t*)•: target specific option mismatch vld1q_s32(const int32_t * __a)
```

# Discussion History
## grahamreeds | 2020-02-11T01:07:21+00:00
By modifying cmake/flags.cmake and commenting out lines 26-28 I managed to get further.

Now it is lots of errors from randomx.cpp regarding JitCompilerA64 has not been declared.

## grahamreeds | 2020-02-12T16:00:11+00:00
Just having a quick look.  This seems to be related to line 59 of randomx.cmake.  Since the cmake program is 32bit the size of void pointer is just 4.  I tried manjaro but kept crashing when I tried to set the wifi ssid and key.  I will have a go at commenting this out later and forcing it down that codepath.  I am also dubious about if the RPi has AES instructions.

## grahamreeds | 2020-02-12T23:55:50+00:00
Okay. I looked at the CHECK_CXX_COMPILER_FLAG and that is an unreliable way to determine if a chip has a particular feature.  On gcc6.5 that function returns fails but on gcc8 it succeeds.

One way of determining if a chip has a feature is to look in /proc/cpuinfo.

So I removed the include and CHECK_ lines and added the following that looks for aes in the output of /proc/cpuinfo.

```
set(cat_cmd "cat")
set(cat_arg "/proc/cpuinfo")
message (STATUS "cmd: ${cat_cmd} ${cat_arg}")
execute_process(COMMAND ${cat_cmd} ${cat_arg}
        WORKING_DIRECTORY ${PROJECT_SOURCE_DIR}
        RESULT_VARIABLE cat_result
        OUTPUT_VARIABLE cat_ver)
message (STATUS "${cat_ver}")

string(FIND ${cat_ver} "aes" AES_PRESENT)
message (STATUS "aes present: ${AES_PRESENT}")

if (${AES_PRESENT} EQUAL -1)
        set(XMRIG_ARM_CRYPTO false)
else ()
        set(XMRIG_ARM_CRYPTO true)
endif ()
```

Obviously you can tidy it up and remove the copious amounts of output but you get the idea.

Here is a list of cpuinfo results. [https://github.com/randombit/cpuinfo/tree/master/arm](url)

# Action History
- Created by: grahamreeds | 2020-02-11T00:26:16+00:00
- Closed at: 2021-04-12T15:01:43+00:00
