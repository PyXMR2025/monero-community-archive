---
title: unrecognized command line option ‘-maes’ - PPC64
source_url: https://github.com/xmrig/xmrig/issues/709
author: asanchez500
assignees: []
labels:
- wontfix
created_at: '2018-06-30T22:47:48+00:00'
updated_at: '2018-07-01T08:29:28+00:00'
type: issue
status: closed
closed_at: '2018-07-01T08:29:28+00:00'
---

# Original Description
I get this error when trying to run make. I am testing on a PS3 POWER 7 CPU. Which is PPC64. I am not to sure if I need to change C FLAGS since the -maes option is for x86. I think the PS3 can crank out atleast 2K H/s hopefully. I am running Red Ribbon Debian 8 Jessie. 

  2%] Building CXX object CMakeFiles/xmrig.dir/src/core/Config.cpp.o
c++: error: unrecognized command line option ‘-maes’
make[2]: *** [CMakeFiles/xmrig.dir/src/core/Config.cpp.o] Error 1
make[1]: *** [CMakeFiles/xmrig.dir/all] Error 2
make: *** [all] Error 2 

Here is my CPU info:
Architecture:          ppc64
Byte Order:            Big Endian
CPU(s):                2
On-line CPU(s) list:   0,1
Thread(s) per core:    2
Core(s) per socket:    1
Socket(s):             1
Model:                 SonyPS3
L1d cache:             32K
L1i cache:             32K

# Discussion History
## xmrig | 2018-07-01T08:29:28+00:00
POWER not supported.
Thank you.

# Action History
- Created by: asanchez500 | 2018-06-30T22:47:48+00:00
- Closed at: 2018-07-01T08:29:28+00:00
