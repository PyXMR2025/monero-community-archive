---
title: horrible fix for iphone aarch64
source_url: https://github.com/xmrig/xmrig/issues/985
author: resistor4u
assignees: []
labels: []
created_at: '2019-03-12T20:09:18+00:00'
updated_at: '2019-08-02T12:01:23+00:00'
type: issue
status: closed
closed_at: '2019-08-02T12:01:23+00:00'
---

# Original Description
Building for iphone 6s worked with ~58 H/s before the March 9 fork. Now, using the same build settings, it fails to make with:
```
...
[ 88%] Building CXX object CMakeFiles/xmrig-notls.dir/src/common/cpu/BasicCpuInfo_arm.cpp.o
[ 90%] Building C object CMakeFiles/xmrig-notls.dir/src/crypto/c_groestl.c.o
/Users/mr_man/oldxmrig/pure_xmrig/src/common/cpu/BasicCpuInfo_arm.cpp:29:13: fatal error: 'sys/auxv.h' file not found
#   include <sys/auxv.h>
            ^~~~~~~~~~~~
1 error generated.
make[2]: *** [CMakeFiles/xmrig-notls.dir/build.make:661: CMakeFiles/xmrig-notls.dir/src/common/cpu/BasicCpuInfo_arm.cpp.o] Error 1
make[2]: *** Waiting for unfinished jobs....
[ 92%] Building C object CMakeFiles/xmrig-notls.dir/src/crypto/c_blake256.c.o
make[1]: *** [CMakeFiles/Makefile2:73: CMakeFiles/xmrig-notls.dir/all] Error 2
make: *** [Makefile:84: all] Error 2
```

I played with some of the calls in `src/Mem_unix.cpp` and `src/common/cpu/BasicCpuInfo_arm.cpp` as a workaround. It builds and runs, but with a dramatic reduction in hashrate. Instead of 58 H/s, I'm now getting about 14.7 H/s.

In `src/Mem_unix.cpp` I commented out lines 109-114. In `src/common/cpu/BasicCpuInfo_arm.cpp`, I commented out lines 29-32 and changed lines 44-53 to this:
```
{
#   ifdef XMRIG_ARMv8
    memcpy(m_brand, "Unknown", 5);
#   else
    memcpy(m_brand, "Unknown", 5);
#   endif

#   if __ARM_FEATURE_CRYPTO
    m_aes = true;
#   endif
}
```
These changes produce a working binary, but with a nearly 75% reduction in hashrate. @xmrig Is there a better way of doing this?

# Discussion History
## Spudz76 | 2019-03-18T16:12:52+00:00
I would adapt however [these devs did it for aarch64](https://botan.randombit.net/doxygen/cpuid__arm_8cpp_source.html#195)
Line 195 on down, replaces the auxv calls with internal ones so that it emulates, which I figure should plug in with the code here somewhat easily?

# Action History
- Created by: resistor4u | 2019-03-12T20:09:18+00:00
- Closed at: 2019-08-02T12:01:23+00:00
