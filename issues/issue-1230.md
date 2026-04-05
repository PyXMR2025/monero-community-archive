---
title: Cmake Error could not find HWLOC
source_url: https://github.com/xmrig/xmrig/issues/1230
author: IRayofficial
assignees: []
labels: []
created_at: '2019-10-09T18:29:35+00:00'
updated_at: '2021-11-17T22:41:08+00:00'
type: issue
status: closed
closed_at: '2019-12-22T19:28:19+00:00'
---

# Original Description
pi@raspberrypi:~/xmrig/build $ cmake ..
-- The C compiler identification is GNU 8.3.0
-- The CXX compiler identification is GNU 8.3.0
-- Check for working C compiler: /usr/bin/cc
-- Check for working C compiler: /usr/bin/cc -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Detecting C compile features
-- Detecting C compile features - done
-- Check for working CXX compiler: /usr/bin/c++
-- Check for working CXX compiler: /usr/bin/c++ -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Use ARM_TARGET=7 (armv7l)
-- Looking for syslog.h
-- Looking for syslog.h - found
CMake Error at /usr/share/cmake-3.13/Modules/FindPackageHandleStandardArgs.cmake:137 (message):
  Could NOT find HWLOC (missing: HWLOC_LIBRARY HWLOC_INCLUDE_DIR)
Call Stack (most recent call first):
  /usr/share/cmake-3.13/Modules/FindPackageHandleStandardArgs.cmake:378 (_FPHSA_FAILURE_MESSAGE)
  cmake/FindHWLOC.cmake:25 (find_package_handle_standard_args)
  src/backend/cpu/cpu.cmake:29 (find_package)
  src/backend/backend.cmake:1 (include)
  CMakeLists.txt:29 (include)


-- Configuring incomplete, errors occurred!
See also "/home/pi/xmrig/build/CMakeFiles/CMakeOutput.log".


# Discussion History
## 0xman | 2019-10-10T11:23:59+00:00
did you install HWLOC ?

## RizkiRama99 | 2019-10-25T14:42:49+00:00
This is the way https://junglecrypto.blogspot.com/2019/10/how-to-fix-hwloc-issue-when-running.html

## 0xman | 2019-10-25T16:27:14+00:00
> This is the way https://junglecrypto.blogspot.com/2019/10/how-to-fix-hwloc-issue-when-running.html

what's with the link?

## RizkiRama99 | 2019-10-25T16:36:03+00:00
It contains articles about hwloc problems

## xmrig | 2019-10-25T16:57:58+00:00
@RizkiRama99 no one like short links, it looks and may dangerous by the way, I edited your comments.

## MarcKarasek | 2020-06-02T15:20:19+00:00
This is not closed..  If you are compiling your own hwloc and try to set XMRIG_DEPS it fails..


## JoanLab-Rob | 2021-11-17T22:41:08+00:00
CHECK THIS LINK, IT MAYBE HELPS SOME OF YOU GUYS: https://programmerah.com/xmr-could-not-find-hwloc-missing-hwloc_library-hwloc_include_dir-33513/

# Action History
- Created by: IRayofficial | 2019-10-09T18:29:35+00:00
- Closed at: 2019-12-22T19:28:19+00:00
