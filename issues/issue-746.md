---
title: Is there a version for PPC64?
source_url: https://github.com/xmrig/xmrig/issues/746
author: asanchez500
assignees: []
labels:
- wontfix
created_at: '2018-08-30T02:38:57+00:00'
updated_at: '2018-09-22T06:08:02+00:00'
type: issue
status: closed
closed_at: '2018-09-22T06:08:02+00:00'
---

# Original Description
Hello I am trying to compile and install for couple of PS3's I have running Debian linux. There arch is PPC64. This is what CMake gives me... 

root@debianz:~/Desktop/xmrig# cmake -DCMAKE_TOOLCHAIN_FILE=/root/Desktop/ppc64-cmake-file
-- The C compiler identification is GNU 6.3.0
-- The CXX compiler identification is GNU 6.3.0
-- Check for working C compiler: /usr/bin/powerpc64-linux-gnu-gcc
-- Check for working C compiler: /usr/bin/powerpc64-linux-gnu-gcc -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Detecting C compile features
-- Detecting C compile features - done
-- Check for working CXX compiler: /usr/bin/g++
-- Check for working CXX compiler: /usr/bin/g++ -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Detecting CXX compile features
-- Detecting CXX compile features - done
CMake Error at CMakeLists.txt:11 (include):
  include could not find load file:

    cmake/cpu.cmake


CMake Error at CMakeLists.txt:175 (find_package):
  By not providing "FindUV.cmake" in CMAKE_MODULE_PATH this project has asked
  CMake to find a package configuration file provided by "UV", but CMake did
  not find one.

  Could not find a package configuration file provided by "UV" with any of
  the following names:

    UVConfig.cmake
    uv-config.cmake

  Add the installation prefix of "UV" to CMAKE_PREFIX_PATH or set "UV_DIR" to
  a directory containing one of the above files.  If "UV" provides a separate
  development package or SDK, be sure it has been installed.


-- Configuring incomplete, errors occurred!
See also "/root/Desktop/xmrig/CMakeFiles/CMakeOutput.log" 

I am willing to do any testing possible if need be if some one is willing to help me get this running. I am also willing to pay on gitcoin if need be. Please and thank you. I'm wanting to see if the PS3 can crank out a decent hash rate for Monero since the Monero network is rather low and doesn't seem to grow in difficulty like BitCoin and so much for ASIC's and Monero. So I guess my next best bet was a gaming console. So we shall see. Please let me know if you can help. Please and thank you. 

# Discussion History
## yuhong | 2018-09-01T09:05:58+00:00
https://github.com/nioroso-x3/xmr-stak-power would be the best starting point, but you will have to do the AES in software which will slow it down.

# Action History
- Created by: asanchez500 | 2018-08-30T02:38:57+00:00
- Closed at: 2018-09-22T06:08:02+00:00
