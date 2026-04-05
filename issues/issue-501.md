---
title: compiling error - xmrig-amd on ubuntu 17.04 - 32-bits :o
source_url: https://github.com/xmrig/xmrig/issues/501
author: poteus
assignees: []
labels: []
created_at: '2018-04-04T23:19:24+00:00'
updated_at: '2018-11-05T13:19:47+00:00'
type: issue
status: closed
closed_at: '2018-11-05T13:19:47+00:00'
---

# Original Description
I get the following error when compiling xmrig-amd in ubuntu 17.04 (32-bits)

/Miner/xmrig-amd/build$ make
[  2%] Building CXX object CMakeFiles/xmrig-amd.dir/src/api/Api.cpp.o
In file included from /home/pro/Documents/Miner/xmrig-amd/src/workers/OclThread.h:31:0,
                 from /home/pro/Documents/Miner/xmrig-amd/src/api/ApiState.h:32,
                 from /home/pro/Documents/Miner/xmrig-amd/src/api/Api.cpp:28:
/home/pro/Documents/Miner/xmrig-amd/src/amd/GpuContext.h:31:13: fatal error: CL/cl.h: No such file or directory
 #   include <CL/cl.h>
             ^~~~~~~~~
compilation terminated.
CMakeFiles/xmrig-amd.dir/build.make:62: recipe for target 'CMakeFiles/xmrig-amd.dir/src/api/Api.cpp.o' failed
make[2]: *** [CMakeFiles/xmrig-amd.dir/src/api/Api.cpp.o] Error 1
CMakeFiles/Makefile2:67: recipe for target 'CMakeFiles/xmrig-amd.dir/all' failed
make[1]: *** [CMakeFiles/xmrig-amd.dir/all] Error 2
Makefile:83: recipe for target 'all' failed
make: *** [all] Error 2

# Discussion History
## NmxMilk | 2018-04-10T08:50:15+00:00
You are on the wrong project!
Here it is xmrig and not xmrig-amd.
BTW, the error you're getting says you don't have the AMD SDK installed.

## poteus | 2018-04-10T12:29:18+00:00
Thanks, redirecting.

I installed AMD SDK, but it is a 32-bits linux distro, and I feel there must be a problem of compatibility during the compilation...  I have not found a lot of info on how to compile AMD SDK on a 32-bits box.  I just don't want to buy a 64-bits box to GPU mine this little baby.  Cheapy 🥇 

## xmrig | 2018-11-05T13:19:47+00:00
Recent versions not require any SDK.

# Action History
- Created by: poteus | 2018-04-04T23:19:24+00:00
- Closed at: 2018-11-05T13:19:47+00:00
