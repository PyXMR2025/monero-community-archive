---
title: cmake . error
source_url: https://github.com/xmrig/xmrig/issues/1504
author: panyi1981
assignees: []
labels:
- question
created_at: '2020-01-16T13:13:14+00:00'
updated_at: '2020-08-28T16:42:31+00:00'
type: issue
status: closed
closed_at: '2020-08-28T16:42:31+00:00'
---

# Original Description
I'v downloaded source file (xmrig-5.5.1.tar.gz) and encountered the following error when I executing the command "cmake ." Thanks a lot if you could appoint something in my operation process.(OS: ubuntu _18.04.3)_

**panyi@panyi-desktop:~/xmrig-5.5.1$ cmake .
CMake Error at /usr/share/cmake-3.10/Modules/FindPackageHandleStandardArgs.cmake:137 (message):
  Could NOT find HWLOC (missing: HWLOC_LIBRARY HWLOC_INCLUDE_DIR)
Call Stack (most recent call first):
  /usr/share/cmake-3.10/Modules/FindPackageHandleStandardArgs.cmake:378 (_FPHSA_FAILURE_MESSAGE)
  cmake/FindHWLOC.cmake:25 (find_package_handle_standard_args)
  src/backend/cpu/cpu.cmake:30 (find_package)
  src/backend/backend.cmake:1 (include)
  CMakeLists.txt:37 (include)**


# Discussion History
## xmrig | 2020-01-16T13:42:32+00:00
https://xmrig.com/docs/miner/ubuntu-build

## electroape | 2020-01-19T13:50:20+00:00
Just ran into similiar problems building on Windows. Instruction aren't clear\right. 

This part :
> CMake build:
> 
> mkdir build
> cd build
> cmake .. -G "Unix Makefiles" -DXMRIG_DEPS=c:/xmrig-deps/gcc/x64
> make

Should go more like this :
> CMake build:
> 
> Unpack archives with sources and dependencies to %MSYS%\home\\%user%\\
> Folders with archives and dependencies should be named 'xmrig-master' and 'xmrig-deps' respectively, if that's not the case then rename folders or change command below to point respective folders
> cd xmrig-master
> mkdir build
> cd build
> cmake .. -G "Unix Makefiles" -DXMRIG_DEPS=../xmrig-deps/gcc/x64
> make


# Action History
- Created by: panyi1981 | 2020-01-16T13:13:14+00:00
- Closed at: 2020-08-28T16:42:31+00:00
