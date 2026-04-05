---
title: Issue during make using g++-7
source_url: https://github.com/xmrig/xmrig/issues/251
author: sh17156
assignees: []
labels:
- bug
created_at: '2017-12-10T13:29:31+00:00'
updated_at: '2018-03-14T23:34:49+00:00'
type: issue
status: closed
closed_at: '2018-03-14T23:34:49+00:00'
---

# Original Description

[  2%] Building CXX object CMakeFiles/xmrig.dir/src/net/Client.cpp.o
g++-7: internal compiler error: Killed (program cc1plus)
Please submit a full bug report,
with preprocessed source if appropriate.
See <file:///usr/share/doc/gcc-7/README.Bugs> for instructions.
CMakeFiles/xmrig.dir/build.make:278: recipe for target 'CMakeFiles/xmrig.dir/src/net/Client.cpp.o' failed
make[2]: *** [CMakeFiles/xmrig.dir/src/net/Client.cpp.o] Error 4
CMakeFiles/Makefile2:67: recipe for target 'CMakeFiles/xmrig.dir/all' failed
make[1]: *** [CMakeFiles/xmrig.dir/all] Error 2
Makefile:83: recipe for target 'all' failed
make: *** [all] Error 2


# Discussion History
## xmrig | 2017-12-11T10:23:09+00:00
Looks like internal gcc error. You need submit this bug to gcc team.
Thank you.

# Action History
- Created by: sh17156 | 2017-12-10T13:29:31+00:00
- Closed at: 2018-03-14T23:34:49+00:00
