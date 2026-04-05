---
title: Raspberry Pi-3B-Centos7 xmrig flags.cmake
source_url: https://github.com/xmrig/xmrig/issues/356
author: rainmo
assignees: []
labels: []
created_at: '2018-01-22T09:19:55+00:00'
updated_at: '2018-02-07T06:42:10+00:00'
type: issue
status: closed
closed_at: '2018-02-07T06:42:10+00:00'
---

# Original Description
I modified these code，and re-complied，get a new problem.
if (XMRIG_ARMv8)
        set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} **-mcpu=cortex-a53**")
        set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} **-mcpu=cortex-a53 -mfloat-abi=hard -mfpu=neon-fp-armv8 -mneon-for-64bits**")
    elseif (XMRIG_ARMv7)
        set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} **-mfpu=neon**")
        set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} **-mfpu=neon-vfpv4**")

+++++++++++++++++++++++++++
make[2]: *** [CMakeFiles/xmrig.dir/src/crypto/CryptoNight.cpp.o] Error 1
make[1]: *** [CMakeFiles/xmrig.dir/all] Error 2
make: *** [all] Error 2

**RP-3B has a ArmV8 CPU, But when I show cpu edtion, it displays Armv7l. So I do not know what really is. 
Can you tell me what is right settings, cause the last complied edtion is really rally slow. Thank you.**


# Discussion History
# Action History
- Created by: rainmo | 2018-01-22T09:19:55+00:00
- Closed at: 2018-02-07T06:42:10+00:00
