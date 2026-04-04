---
title: Windows 64bit Build Failure - "Could NOT find OpenSSL"
source_url: https://github.com/monero-project/monero/issues/3925
author: ryannathans
assignees: []
labels: []
created_at: '2018-06-04T15:00:16+00:00'
updated_at: '2021-09-19T04:59:07+00:00'
type: issue
status: closed
closed_at: '2018-06-04T15:03:23+00:00'
---

# Original Description
Fresh mingw64, following readme exactly, building master

```
make release-static-win64
mkdir -p build/release
cd build/release && cmake -G "MSYS Makefiles" -D STATIC=ON -D ARCH="x86-64" -D BUILD_64=ON -D CMAKE_BUILD_TYPE=Release -D BUILD_TAG="win-x64" -D CMAKE_TOOLCHAIN_FILE=../../cmake/64-bit-toolchain.cmake -D MSYS2_FOLDER=c:/msys64 ../.. && make
-- The C compiler identification is GNU 7.3.0
-- The CXX compiler identification is GNU 7.3.0
-- Check for working C compiler: G:/msys64/mingw64/bin/x86_64-w64-mingw32-gcc.exe
-- Check for working C compiler: G:/msys64/mingw64/bin/x86_64-w64-mingw32-gcc.exe -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Detecting C compile features
-- Detecting C compile features - done
-- Check for working CXX compiler: G:/msys64/mingw64/bin/x86_64-w64-mingw32-g++.exe
-- Check for working CXX compiler: G:/msys64/mingw64/bin/x86_64-w64-mingw32-g++.exe -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Building build tag win-x64
-- Could not find DEVELOPER_LOCAL_TOOLS in env (not required)
-- BOOST_IGNORE_SYSTEM_PATHS defaults to OFF
-- Could not find DEVELOPER_LIBUNBOUND_OLD in env (not required)
-- Building for a 64-bit system
-- Building internal libraries as static
-- MSYS location: G:/msys64
-- Could not find DATABASE in env (not required unless you want to change database type from default: lmdb)
-- Using LMDB as default DB type
-- looking for liblzma
-- Could not find libunwind (missing: LIBUNWIND_INCLUDE_DIR LIBUNWIND_LIBRARIES)
-- Stack trace on exception disabled
CMake Error at G:/msys64/mingw64/share/cmake-3.11/Modules/FindPackageHandleStandardArgs.cmake:137 (message):
  Could NOT find OpenSSL, try to set the path to OpenSSL root folder in the
  system variable OPENSSL_ROOT_DIR (missing: OPENSSL_CRYPTO_LIBRARY
  OPENSSL_INCLUDE_DIR)
Call Stack (most recent call first):
  G:/msys64/mingw64/share/cmake-3.11/Modules/FindPackageHandleStandardArgs.cmake:378 (_FPHSA_FAILURE_MESSAGE)
  G:/msys64/mingw64/share/cmake-3.11/Modules/FindOpenSSL.cmake:390 (find_package_handle_standard_args)
  CMakeLists.txt:406 (find_package)


-- Configuring incomplete, errors occurred!
See also "C:/Monero/monero-master/build/release/CMakeFiles/CMakeOutput.log".
make: *** [Makefile:111: release-static-win64] Error 1

```

# Discussion History
## ryannathans | 2018-06-04T15:03:23+00:00
Fixed by editing makefile MSYS2_FOLDER=c:/msys64 to my actual installation location on drive g

Perhaps readme should be updated to suggest this lol

## shalinn79 | 2021-09-19T04:38:42+00:00




> Fixed by editing makefile MSYS2_FOLDER=c:/msys64 to my actual installation location on drive g
> 
> Perhaps readme should be updated to suggest this lol

@ryannathans I am getting this issue as well.  But I don't see anywhere where MSYS2_FOLDER is hardcoded.  Can you please point me which specific file you made this change?

## ryannathans | 2021-09-19T04:55:35+00:00
Seems like makefile might be different now, don't know. No idea, maybe search for files containing c: or something

## shalinn79 | 2021-09-19T04:59:07+00:00
> Seems like makefile might be different now, don't know. No idea, maybe search for files containing c: or something

I got it.  Modified the file monero\cmake\64-bit-toolchain.cmake. 

Thanks.

# Action History
- Created by: ryannathans | 2018-06-04T15:00:16+00:00
- Closed at: 2018-06-04T15:03:23+00:00
