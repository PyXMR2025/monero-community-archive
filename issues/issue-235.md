---
title: compile error under ubuntu
source_url: https://github.com/xmrig/xmrig/issues/235
author: khunpoum
assignees: []
labels: []
created_at: '2017-12-03T16:03:50+00:00'
updated_at: '2017-12-07T04:35:54+00:00'
type: issue
status: closed
closed_at: '2017-12-07T04:35:54+00:00'
---

# Original Description
iam follow instructions at https://github.com/xmrig/xmrig/wiki/Ubuntu-Build and  after "cmake .." then take compiler error:

```
...
-- Looking for CL_VERSION_2_0
-- Looking for CL_VERSION_2_0 - not found
-- Looking for CL_VERSION_1_2
-- Looking for CL_VERSION_1_2 - not found
-- Looking for CL_VERSION_1_1
-- Looking for CL_VERSION_1_1 - not found
-- Looking for CL_VERSION_1_0
-- Looking for CL_VERSION_1_0 - not found
-- Could NOT find OpenCL (missing:  OpenCL_LIBRARY OpenCL_INCLUDE_DIR) 
-- Looking for syslog.h
-- Looking for syslog.h - found
CMake Error: The following variables are used in this project, but they are set to NOTFOUND.
Please set them or make sure they are set and tested correctly in the CMake files:
OpenCL_LIBRARY (ADVANCED)
    linked by target "xmrig-amd" in directory /root/xmr-ring/xmrig-amd-2.4.3-beta2

-- Configuring incomplete, errors occurred!
See also "/root/xmr-ring/xmrig-amd-2.4.3-beta2/build/CMakeFiles/CMakeOutput.log".
See also "/root/xmr-ring/xmrig-amd-2.4.3-beta2/build/CMakeFiles/CMakeError.log".
```


i have OpenCL:
```
ls /opt/amdgpu-pro/lib/x86_64-linux-gnu
libamdocl12cl64.so  libdrm_amdgpu.so.1	    libdrm.so.2      libkms.so.1      libOpenCL.so
libamdocl64.so	    libdrm_amdgpu.so.1.0.0  libdrm.so.2.4.0  libkms.so.1.0.0  libOpenCL.so.1
```

# Discussion History
## khunpoum | 2017-12-03T16:39:35+00:00
sloved after iam add path directly

```
rm -rf CMakeFiles
rm -rf CMakeCache.txt
cmake -D UV_LIBRARY=/usr/local/lib/libuv.so -D OpenCL_INCLUDE_DIR=/opt/amdgpu-pro/lib/x86_64-linux-gnu  -D OpenCL_LIBRARY=/opt/amdgpu-pro/lib/x86_64-linux-gnu/libOpenCL.so ..
```

next i have error after "make"
```
Scanning dependencies of target xmrig-amd
[  2%] Building CXX object CMakeFiles/xmrig-amd.dir/src/api/Api.cpp.o
In file included from /root/xmr-ring/xmrig-amd-2.4.3-beta2/src/workers/OclThread.h:31:0,
                 from /root/xmr-ring/xmrig-amd-2.4.3-beta2/src/api/ApiState.h:32,
                 from /root/xmr-ring/xmrig-amd-2.4.3-beta2/src/api/Api.cpp:28:
/root/xmr-ring/xmrig-amd-2.4.3-beta2/src/amd/GpuContext.h:31:22: fatal error: CL/cl.h: No such file or directory
 #   include <CL/cl.h>
                      ^
compilation terminated.
CMakeFiles/xmrig-amd.dir/build.make:62: recipe for target 'CMakeFiles/xmrig-amd.dir/src/api/Api.cpp.o' failed
make[2]: *** [CMakeFiles/xmrig-amd.dir/src/api/Api.cpp.o] Error 1
CMakeFiles/Makefile2:67: recipe for target 'CMakeFiles/xmrig-amd.dir/all' failed
make[1]: *** [CMakeFiles/xmrig-amd.dir/all] Error 2
Makefile:83: recipe for target 'all' failed
make: *** [all] Error 2
```

## khunpoum | 2017-12-03T16:46:13+00:00
slove it after install
```
sudo apt-get install -y opencl-headers
```

# Action History
- Created by: khunpoum | 2017-12-03T16:03:50+00:00
- Closed at: 2017-12-07T04:35:54+00:00
