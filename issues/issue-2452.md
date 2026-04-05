---
title: Unable to build xmrig for Windows.
source_url: https://github.com/xmrig/xmrig/issues/2452
author: Joe23232
assignees: []
labels:
- question
created_at: '2021-06-22T11:32:09+00:00'
updated_at: '2021-06-28T12:24:34+00:00'
type: issue
status: closed
closed_at: '2021-06-28T12:24:34+00:00'
---

# Original Description
Hi I am trying to build it on Windows and I am having some issues with it.

I am following the MSYS method.

![image](https://user-images.githubusercontent.com/34926497/122917127-014dbf80-d3a1-11eb-8743-8bbe033fe46c.png)

I am doing number `4`.

```cmd
$ "c:\Program Files\CMake\bin\cmake.exe" .. -G "Unix Makefiles" -DXMRIG_DEPS=c:/xmrig-deps/gcc/x64
-- The C compiler identification is GNU 10.2.0
-- The CXX compiler identification is GNU 10.2.0
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: C:/msys64/usr/bin/cc.exe - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Check for working CXX compiler: C:/msys64/usr/bin/c++.exe - skipped
-- Detecting CXX compile features
-- Detecting CXX compile features - done
CMake Error at C:/Program Files/CMake/share/cmake-3.20/Modules/FindPackageHandleStandardArgs.cmake:230 (message):
  Could NOT find HWLOC (missing: HWLOC_LIBRARY HWLOC_INCLUDE_DIR)
Call Stack (most recent call first):
  C:/Program Files/CMake/share/cmake-3.20/Modules/FindPackageHandleStandardArgs.cmake:594 (_FPHSA_FAILURE_MESSAGE)
  cmake/FindHWLOC.cmake:25 (find_package_handle_standard_args)
  src/backend/cpu/cpu.cmake:30 (find_package)
  src/backend/backend.cmake:1 (include)
  CMakeLists.txt:44 (include)
```

I want to be able to build with HWLOC.

I am not too sure how to build this?

# Discussion History
## PostGresSQL | 2021-06-22T12:05:13+00:00
https://cmake.org/download/
Make sure you have cmake installed
Make sure you compile it with MSYS2 instead of VS 2017.
You can find optimizing CMake options here
https://xmrig.com/docs/miner/cmake-options


## Joe23232 | 2021-06-22T12:11:01+00:00
@FullStack116   This is Windows 10 mate :)

## PostGresSQL | 2021-06-22T12:11:36+00:00
> @FullStack116 This is Windows 10 mate :)

updated my previous post

## PostGresSQL | 2021-06-22T12:19:09+00:00
> @FullStack116 This is Windows 10 mate :)

Also steps i did to make it work

Create folder c:\xmrig-deps
[Download ](https://github.com/xmrig/xmrig-deps) the most recent version of xmrig prebuilt dependencies  by using the green Code button and Download ZIP
Get cmake [here ](https://cmake.org/download/) get the windows source, unzip it.


Get msys2. Then run it (c:\msys64\mingw64.exe). You get a prompt.

Per https://xmrig.com/docs/miner/build/windows:

1. pacman -S mingw-w64-x86_64-gcc git make

2. git clone https://github.com/xmrig/xmrig.git

3. mkdir xmrig/build && cd xmrig/build

4. cmake/bin/cmake.exe .. -G “Unix Makefiles” -DXMRIG_DEPS=/j/crypto/monero/git/xmrig-deps/gcc/x64

5. make -j$(nproc)

## Joe23232 | 2021-06-22T12:43:30+00:00
@FullStack116 Hey man thanks for your response

> Download the most recent version of xmrig prebuilt dependencies by using the green Code button and Download ZIP

So am I able to still disable the donate level?

## PostGresSQL | 2021-06-22T12:44:42+00:00
> @FullStack116 Hey man thanks for your response
> 
> > Download the most recent version of xmrig prebuilt dependencies by using the green Code button and Download ZIP
> 
> So am I able to still disable the donate level?

yes

Prebuilt xmrig requires 1% donation. To get rid of this:

git clone xmrig’s repo. Change src/donation.h to:

constexpr const int kDefaultDonateLevel = 0;
constexpr const int kMinimumDonateLevel = 0;

## Joe23232 | 2021-06-22T12:45:53+00:00
@FullStack116  Thanks for that mate :)

> Download the most recent version of xmrig prebuilt dependencies by using the green Code button and Download ZIP

Hey man sorry I don't quite understand what do you mean by _green code button_?

Edit: I think you meant it on the right hand side, there is a green button, right?

## Joe23232 | 2021-06-22T12:58:22+00:00
@FullStack116 

That seems to work, thanks :)

# Action History
- Created by: Joe23232 | 2021-06-22T11:32:09+00:00
- Closed at: 2021-06-28T12:24:34+00:00
