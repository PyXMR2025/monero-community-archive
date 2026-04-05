---
title: hwloc lib
source_url: https://github.com/xmrig/xmrig/issues/1085
author: zhekafun
assignees: []
labels:
- question
created_at: '2019-07-30T11:01:35+00:00'
updated_at: '2023-05-01T14:03:40+00:00'
type: issue
status: closed
closed_at: '2019-08-02T11:36:11+00:00'
---

# Original Description
CMake Error at /usr/share/cmake-3.5/Modules/FindPackageHandleStandardArgs.cmake:148 (message):
  Could NOT find HWLOC (missing: HWLOC_LIBRARY)
Call Stack (most recent call first):
  /usr/share/cmake-3.5/Modules/FindPackageHandleStandardArgs.cmake:388 (_FPHSA_FAILURE_MESSAGE)
  cmake/FindHWLOC.cmake:25 (find_package_handle_standard_args)
  src/backend/cpu/cpu.cmake:27 (find_package)
  src/backend/backend.cmake:1 (include)
  CMakeLists.txt:28 (include)


# Discussion History
## xmrig | 2019-07-30T12:33:13+00:00
Install libhwloc-dev or hwloc-devel or hwloc or something similar (depends of your distribution) or build without hwloc support `-DWITH_HWLOC=OFF`.
Thank you.

## zhekafun | 2019-07-31T17:08:22+00:00
what about for msys builds for win 64?

## xmrig | 2019-08-01T02:19:22+00:00
xmrig-deps already updated.
Thank you.

## jiaxu2000 | 2019-08-06T04:19:20+00:00
I download xmrig-deps 3.4 from https://github.com/xmrig/xmrig-deps/releases
But the problem still exists

win 64 and win 32

# cmake .. -G "Unix Makefiles" -DXMRIG_DEPS=c:/xmrig-deps-3.4/gcc/x86
.........

CMake Error at C:/msys32/mingw32/share/cmake-3.15/Modules/FindPackageHandleStandardArgs.cmake:137 (message):
  Could NOT find HWLOC (missing: HWLOC_LIBRARY HWLOC_INCLUDE_DIR)
Call Stack (most recent call first):
  C:/msys32/mingw32/share/cmake-3.15/Modules/FindPackageHandleStandardArgs.cmake:378 (_FPHSA_FAILURE_MESSAGE)
  cmake/FindHWLOC.cmake:25 (find_package_handle_standard_args)
  src/backend/cpu/cpu.cmake:27 (find_package)
  src/backend/backend.cmake:1 (include)
  CMakeLists.txt:28 (include)


-- Configuring incomplete, errors occurred!


-- Configuring incomplete, errors occurred!




## RizkiRama99 | 2019-10-25T14:40:54+00:00
I have already gotten a solution for this issue ...
https://junglecrypto.blogspot.com/2019/10/how-to-fix-hwloc-issue-when-running.html

## varunkhadse | 2019-10-27T11:17:07+00:00
@jiaxu2000 try referring toh this https://github.com/xmrig/xmrig/issues/1085#issuecomment-516398890.

## MarcKarasek | 2020-06-02T15:27:13+00:00
I have crosscompiled hwloc and am trying to set -DXMRIG_DEPS on cmake cmdline.  It is throwing this error:   Could NOT find HWLOC (missing: HWLOC_LIBRARY)

The above link to the blog is no longer valid.   Does anyone have a fix for this?

## MarcKarasek | 2020-06-02T15:34:07+00:00
Manually setting the HW_LOC and UV_LOC in a .cmake file fixes this.
set(HWLOC_LIBRARY <path>/libhwloc.la)
set(HWLOC_INCLUDE_DIR <path>include)
set(UV_LIBRARY <path>/libuv.la)
set(UV_INCLUDE_DIR <path>/include)

Setting XMRIG_DEPS finds openssl just fine.  So the UV and HWLOC parts of cmake when trying to use XMRIG_DEPS is broken

## MuteObserver | 2021-03-08T20:53:12+00:00
> Manually setting the HW_LOC and UV_LOC in a .cmake file fixes this.
> set(HWLOC_LIBRARY /libhwloc.la)
> set(HWLOC_INCLUDE_DIR include)
> set(UV_LIBRARY /libuv.la)
> set(UV_INCLUDE_DIR /include)
> 
> Setting XMRIG_DEPS finds openssl just fine. So the UV and HWLOC parts of cmake when trying to use XMRIG_DEPS is broken

This seems to solve the issue consistently for me.
Thank-you for the followup comment; **please note this solution is working under similar circumstances a year later.**
Unorthodox situation of building in an Android Termux environment _(for experiment's sake)_; things expectedly messy.
~mute

## Joe23232 | 2021-06-21T14:38:42+00:00
> Setting XMRIG_DEPS finds openssl just fine. So the UV and HWLOC parts of cmake when trying to use XMRIG_DEPS is broken

@MarcKarasek  How would I set this mate?

## revdeluxe | 2021-11-12T17:00:28+00:00
> Install libhwloc-dev or hwloc-devel or hwloc or something similar (depends of your distribution) or build without hwloc support `-DWITH_HWLOC=OFF`. Thank you.

is there a chance to include this to the source?
if some people got APT install issues/ Network issues(server related not the source)

anyways it worked for me. thanks

## afl45 | 2023-04-01T12:04:16+00:00
Hi, I join this conversation. I installed the hwloc package and built without the hwloc support but its still not working. does anyone have a solution ?

`[afl_xmr_hp_pm@pc-130 build]$ cmake ..
-- The C compiler identification is GNU 12.2.1
-- The CXX compiler identification is GNU 12.2.1
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
-- Performing Test VAES_SUPPORTED
-- Performing Test VAES_SUPPORTED - Success
-- Looking for syslog.h
-- Looking for syslog.h - found
-- Found HWLOC: /usr/lib64/libhwloc.so  
CMake Error at /usr/share/cmake/Modules/FindPackageHandleStandardArgs.cmake:230 (message):
  Could NOT find UV (missing: UV_LIBRARY UV_INCLUDE_DIR)
Call Stack (most recent call first):
  /usr/share/cmake/Modules/FindPackageHandleStandardArgs.cmake:600 (_FPHSA_FAILURE_MESSAGE)
  cmake/FindUV.cmake:25 (find_package_handle_standard_args)
  CMakeLists.txt:197 (find_package)
`

## LUIZNETO31 | 2023-05-01T14:02:55+00:00
Resolve este problema apenas usando estes comando 
sudo apt-get update
sudo apt-get install libhwloc-dev

# Action History
- Created by: zhekafun | 2019-07-30T11:01:35+00:00
- Closed at: 2019-08-02T11:36:11+00:00
