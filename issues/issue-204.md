---
title: ubunto 16.04 error
source_url: https://github.com/xmrig/xmrig/issues/204
author: gtimeg77
assignees: []
labels:
- bug
created_at: '2017-11-17T19:22:03+00:00'
updated_at: '2018-03-14T23:25:20+00:00'
type: issue
status: closed
closed_at: '2018-03-14T23:25:20+00:00'
---

# Original Description
/root/xmrig/src/api/ApiState.cpp: In function 'double normalize(double)':
/root/xmrig/src/api/ApiState.cpp:60:12: error: 'floor' is not a member of 'std'
     return std::floor(d * 100.0) / 100.0;
            ^
/root/xmrig/src/api/ApiState.cpp:60:12: note: suggested alternative:
In file included from /usr/include/features.h:367:0,
                 from /usr/include/math.h:26,
                 from /root/xmrig/src/api/ApiState.cpp:24:
/usr/include/x86_64-linux-gnu/bits/mathcalls.h:184:1: note:   'floor'
 __MATHCALLX (floor,, (_Mdouble_ __x), (__const__));
 ^
CMakeFiles/xmrig.dir/build.make:86: recipe for target 'CMakeFiles/xmrig.dir/src/api/ApiState.cpp.o' failed
make[2]: *** [CMakeFiles/xmrig.dir/src/api/ApiState.cpp.o] Error 1
CMakeFiles/Makefile2:67: recipe for target 'CMakeFiles/xmrig.dir/all' failed
make[1]: *** [CMakeFiles/xmrig.dir/all] Error 2
Makefile:83: recipe for target 'all' failed
make: *** [all] Error 2
root@2:~/xmrig/build#


# Discussion History
## xmrig | 2017-11-17T19:45:11+00:00
Fixed. Thank you.

## gtimeg77 | 2017-11-17T23:17:12+00:00
c++: internal compiler error: Killed (program cc1plus)
Please submit a full bug report,
with preprocessed source if appropriate.
See <file:///usr/share/doc/gcc-5/README.Bugs> for instructions.
CMakeFiles/xmrig.dir/build.make:110: recipe for target 'CMakeFiles/xmrig.dir/src/api/NetworkState.cpp.o' failed
make[2]: *** [CMakeFiles/xmrig.dir/src/api/NetworkState.cpp.o] Error 4
CMakeFiles/Makefile2:67: recipe for target 'CMakeFiles/xmrig.dir/all' failed
make[1]: *** [CMakeFiles/xmrig.dir/all] Error 2
Makefile:83: recipe for target 'all' failed
make: *** [all] Error 2
root@2:~/xmrig/build#


# Action History
- Created by: gtimeg77 | 2017-11-17T19:22:03+00:00
- Closed at: 2018-03-14T23:25:20+00:00
