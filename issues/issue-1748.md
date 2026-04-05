---
title: Configuring incomplete, errors occurred!
source_url: https://github.com/xmrig/xmrig/issues/1748
author: HeavyDestroy
assignees: []
labels: []
created_at: '2020-06-25T05:31:25+00:00'
updated_at: '2020-06-25T06:11:33+00:00'
type: issue
status: closed
closed_at: '2020-06-25T05:51:07+00:00'
---

# Original Description
root@ahmad-syaufi:~/xmrig/build# cmake ..
-- The C compiler identification is GNU 7.5.0
-- The CXX compiler identification is GNU 7.5.0
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /usr/bin/cc - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Check for working CXX compiler: /usr/bin/c++ - skipped
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Looking for syslog.h
-- Looking for syslog.h - found
CMake Error at /usr/local/share/cmake-3.18/Modules/FindPackageHandleStandardArgs.cmake:165 (message):
  Could NOT find HWLOC (missing: HWLOC_LIBRARY HWLOC_INCLUDE_DIR)
Call Stack (most recent call first):
  /usr/local/share/cmake-3.18/Modules/FindPackageHandleStandardArgs.cmake:458 (_FPHSA_FAILURE_MESSAGE)
  cmake/FindHWLOC.cmake:25 (find_package_handle_standard_args)
  src/backend/cpu/cpu.cmake:30 (find_package)
  src/backend/backend.cmake:1 (include)
  CMakeLists.txt:39 (include)


-- Configuring incomplete, errors occurred!
See also "/root/xmrig/build/CMakeFiles/CMakeOutput.log"

# Discussion History
## HeavyDestroy | 2020-06-25T05:40:43+00:00
root@ahmad-syaufi:~/xmrig/build# cmake .. -DWITH_HWLOC=OFF
CMake Error at /usr/local/share/cmake-3.18/Modules/FindPackageHandleStandardArgs.cmake:165 (message):
  Could NOT find UV (missing: UV_LIBRARY UV_INCLUDE_DIR)
Call Stack (most recent call first):
  /usr/local/share/cmake-3.18/Modules/FindPackageHandleStandardArgs.cmake:458 (_FPHSA_FAILURE_MESSAGE)
  cmake/FindUV.cmake:25 (find_package_handle_standard_args)
  CMakeLists.txt:169 (find_package)


-- Configuring incomplete, errors occurred!
See also "/root/xmrig/build/CMakeFiles/CMakeOutput.log"

## HeavyDestroy | 2020-06-25T05:43:51+00:00
root@ahmad-syaufi:~/xmrig/build# cmake -G "Visual Studio 16 2019" -DCMAKE_BUILD_TYPE=Release -DXMRIG_DEPS=C:\src\xmrig-deps\msvc2019\x64 -DCMAKE_VERBOSE_MAKEFILE=ON -DWITH_OPENCL=OFF -DWITH_CUDA=OFF -DWITH_ARGON2=OFF ..
CMake Error: Could not create named generator Visual Studio 16 2019

Generators
* Unix Makefiles               = Generates standard UNIX makefiles.
  Green Hills MULTI            = Generates Green Hills MULTI files
                                 (experimental, work-in-progress).
  Ninja                        = Generates build.ninja files.
  Ninja Multi-Config           = Generates build-<Config>.ninja files.
  Watcom WMake                 = Generates Watcom WMake makefiles.
  CodeBlocks - Ninja           = Generates CodeBlocks project files.
  CodeBlocks - Unix Makefiles  = Generates CodeBlocks project files.
  CodeLite - Ninja             = Generates CodeLite project files.
  CodeLite - Unix Makefiles    = Generates CodeLite project files.
  Sublime Text 2 - Ninja       = Generates Sublime Text 2 project files.  Sublime Text 2 - Unix Makefiles
                               = Generates Sublime Text 2 project files.  Kate - Ninja                 = Generates Kate project files.
  Kate - Unix Makefiles        = Generates Kate project files.
  Eclipse CDT4 - Ninja         = Generates Eclipse CDT 4.0 project files.
  Eclipse CDT4 - Unix Makefiles= Generates Eclipse CDT 4.0 project files.

root@ahmad-syaufi:~/xmrig/build# make
make: *** No targets specified and no makefile found.  Stop.

## HeavyDestroy | 2020-06-25T05:51:07+00:00
fixed :
add-apt-repository universe
sudo apt-get install -y libuv-dev
sudo apt-get install -y libuv1-dev

# Action History
- Created by: HeavyDestroy | 2020-06-25T05:31:25+00:00
- Closed at: 2020-06-25T05:51:07+00:00
