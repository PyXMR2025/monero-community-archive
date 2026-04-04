---
title: MinGW 64 build failed (logs attached)
source_url: https://github.com/monero-project/monero/issues/3560
author: Keksov
assignees: []
labels: []
created_at: '2018-04-05T13:45:12+00:00'
updated_at: '2018-04-06T18:06:11+00:00'
type: issue
status: closed
closed_at: '2018-04-06T18:04:47+00:00'
---

# Original Description
UPDATE. SOLUTION: `cd /usr/src && git clone --recursive https://github.com/monero-project/monero` instead of downloading zip from git

ErrorLog file contains a lot of errors so it's not clear wich one is a real one...
[CMakeError.log](https://github.com/monero-project/monero/files/1880209/CMakeError.log)
[CMakeOutput.log](https://github.com/monero-project/monero/files/1880208/CMakeOutput.log)

I added the new target to makefile
```
debug-static-win64:
	mkdir -p build/debug
	cd build/debug && cmake -G "MSYS Makefiles" -D STATIC=ON -D ARCH="x86-64" -D BUILD_64=ON -D CMAKE_BUILD_TYPE=Debug -D BUILD_TAG="win-x64" -D CMAKE_TOOLCHAIN_FILE=../../cmake/64-bit-toolchain.cmake -D MSYS2_FOLDER=c:/msys64 ../.. && $(MAKE)
```

make debug-static-win64 output:
```
 MINGW64 /usr/src/monero-0.12.0.0
$ make debug-static-win64
mkdir -p build/debug
cd build/debug && cmake -G "MSYS Makefiles" -D STATIC=ON -D ARCH="x86-64" -D BUILD_64=ON -D CMAKE_BUILD_TYPE=Debug -D BUILD_TAG="win-x64" -D CMAKE_TOOLCHAIN_FILE=../../cmake/64-bit-toolchain.cmake -D MSYS2_FOLDER=c:/msys64 ../.. && make
-- The C compiler identification is GNU 7.3.0
-- The CXX compiler identification is GNU 7.3.0
-- Check for working C compiler: C:/msys64/mingw64/bin/x86_64-w64-mingw32-gcc.exe
-- Check for working C compiler: C:/msys64/mingw64/bin/x86_64-w64-mingw32-gcc.exe -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Detecting C compile features
-- Detecting C compile features - done
-- Check for working CXX compiler: C:/msys64/mingw64/bin/x86_64-w64-mingw32-g++.exe
-- Check for working CXX compiler: C:/msys64/mingw64/bin/x86_64-w64-mingw32-g++.exe -- works
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
-- MSYS location: C:/msys64
-- Could not find DATABASE in env (not required unless you want to change database type from default: lmdb)
-- Using LMDB as default DB type
-- looking for liblzma
-- liblzma found
-- Could not find libunwind (missing: LIBUNWIND_INCLUDE_DIR)
-- Stack trace on exception disabled
-- Found OpenSSL: C:/msys64/mingw64/lib/libcrypto.a (found version "1.0.2o")
-- Using OpenSSL include dir at C:/msys64/mingw64/include
-- Could NOT find PCSC (missing: PCSC_LIBRARY PCSC_INCLUDE_DIR)
-- Looking for memset_s in c
-- Looking for memset_s in c - not found
-- Looking for explicit_bzero in c
-- Looking for explicit_bzero in c - not found
-- Looking for strptime
-- Looking for strptime - not found
-- Could NOT find MiniUPnPc (missing: MINIUPNP_INCLUDE_DIR MINIUPNP_LIBRARY)
-- Using miniupnpc from local source tree for static build
-- Looking for libunbound
CMake Error at external/CMakeLists.txt:82 (add_subdirectory):
  The source directory

    C:/msys64/usr/src/monero-0.12.0.0/external/unbound

  does not contain a CMakeLists.txt file.


-- Using 64-bit LMDB from source tree
-- Looking for pthread.h
-- Looking for pthread.h - found
-- Looking for pthread_create
-- Looking for pthread_create - found
-- Found Threads: TRUE
-- Building on  for x86-64
-- Performing Test _Wformat_c
-- Performing Test _Wformat_c - Success
-- Performing Test _Wformat_cxx
-- Performing Test _Wformat_cxx - Success
-- Performing Test _Wformat_security_c
-- Performing Test _Wformat_security_c - Success
-- Performing Test _Wformat_security_cxx
-- Performing Test _Wformat_security_cxx - Success
-- Performing Test _fstack_protector_c
-- Performing Test _fstack_protector_c - Success
-- Performing Test _fstack_protector_cxx
-- Performing Test _fstack_protector_cxx - Success
-- Performing Test _fstack_protector_strong_c
-- Performing Test _fstack_protector_strong_c - Success
-- Performing Test _fstack_protector_strong_cxx
-- Performing Test _fstack_protector_strong_cxx - Success
-- Looking for -Wl,-z,relro linker flag
-- Looking for -Wl,-z,relro linker flag - not found
-- Looking for -Wl,-z,now linker flag
-- Looking for -Wl,-z,now linker flag - not found
-- Looking for -Wl,-z,noexecstack linker flag
-- Looking for -Wl,-z,noexecstack linker flag - not found
-- Looking for -Wl,-z,noexecheap linker flag
-- Looking for -Wl,-z,noexecheap linker flag - not found
-- Looking for -Wl,--dynamicbase linker flag
-- Looking for -Wl,--dynamicbase linker flag - found
-- Looking for -Wl,--nxcompat linker flag
-- Looking for -Wl,--nxcompat linker flag - found
-- Using C security hardening flags:  -Wformat -Wformat-security -fstack-protector -fstack-protector-strong
-- Using C++ security hardening flags:  -Wformat -Wformat-security -fstack-protector -fstack-protector-strong
-- Using linker security hardening flags:  -Wl,--dynamicbase -Wl,--nxcompat
-- AES support enabled
CMake Warning at C:/msys64/mingw64/share/cmake-3.10/Modules/FindBoost.cmake:801 (message):
  New Boost version may have incorrect or missing dependencies and imported
  targets
Call Stack (most recent call first):
  C:/msys64/mingw64/share/cmake-3.10/Modules/FindBoost.cmake:907 (_Boost_COMPONENT_DEPENDENCIES)
  C:/msys64/mingw64/share/cmake-3.10/Modules/FindBoost.cmake:1542 (_Boost_MISSING_DEPENDENCIES)
  CMakeLists.txt:786 (find_package)


CMake Warning at C:/msys64/mingw64/share/cmake-3.10/Modules/FindBoost.cmake:801 (message):
  New Boost version may have incorrect or missing dependencies and imported
  targets
Call Stack (most recent call first):
  C:/msys64/mingw64/share/cmake-3.10/Modules/FindBoost.cmake:907 (_Boost_COMPONENT_DEPENDENCIES)
  C:/msys64/mingw64/share/cmake-3.10/Modules/FindBoost.cmake:1542 (_Boost_MISSING_DEPENDENCIES)
  CMakeLists.txt:786 (find_package)


CMake Warning at C:/msys64/mingw64/share/cmake-3.10/Modules/FindBoost.cmake:801 (message):
  New Boost version may have incorrect or missing dependencies and imported
  targets
Call Stack (most recent call first):
  C:/msys64/mingw64/share/cmake-3.10/Modules/FindBoost.cmake:907 (_Boost_COMPONENT_DEPENDENCIES)
  C:/msys64/mingw64/share/cmake-3.10/Modules/FindBoost.cmake:1542 (_Boost_MISSING_DEPENDENCIES)
  CMakeLists.txt:786 (find_package)


CMake Warning at C:/msys64/mingw64/share/cmake-3.10/Modules/FindBoost.cmake:801 (message):
  New Boost version may have incorrect or missing dependencies and imported
  targets
Call Stack (most recent call first):
  C:/msys64/mingw64/share/cmake-3.10/Modules/FindBoost.cmake:907 (_Boost_COMPONENT_DEPENDENCIES)
  C:/msys64/mingw64/share/cmake-3.10/Modules/FindBoost.cmake:1542 (_Boost_MISSING_DEPENDENCIES)
  CMakeLists.txt:786 (find_package)


CMake Warning at C:/msys64/mingw64/share/cmake-3.10/Modules/FindBoost.cmake:801 (message):
  New Boost version may have incorrect or missing dependencies and imported
  targets
Call Stack (most recent call first):
  C:/msys64/mingw64/share/cmake-3.10/Modules/FindBoost.cmake:907 (_Boost_COMPONENT_DEPENDENCIES)
  C:/msys64/mingw64/share/cmake-3.10/Modules/FindBoost.cmake:1542 (_Boost_MISSING_DEPENDENCIES)
  CMakeLists.txt:786 (find_package)


CMake Warning at C:/msys64/mingw64/share/cmake-3.10/Modules/FindBoost.cmake:801 (message):
  New Boost version may have incorrect or missing dependencies and imported
  targets
Call Stack (most recent call first):
  C:/msys64/mingw64/share/cmake-3.10/Modules/FindBoost.cmake:907 (_Boost_COMPONENT_DEPENDENCIES)
  C:/msys64/mingw64/share/cmake-3.10/Modules/FindBoost.cmake:1542 (_Boost_MISSING_DEPENDENCIES)
  CMakeLists.txt:786 (find_package)


CMake Warning at C:/msys64/mingw64/share/cmake-3.10/Modules/FindBoost.cmake:801 (message):
  New Boost version may have incorrect or missing dependencies and imported
  targets
Call Stack (most recent call first):
  C:/msys64/mingw64/share/cmake-3.10/Modules/FindBoost.cmake:907 (_Boost_COMPONENT_DEPENDENCIES)
  C:/msys64/mingw64/share/cmake-3.10/Modules/FindBoost.cmake:1542 (_Boost_MISSING_DEPENDENCIES)
  CMakeLists.txt:786 (find_package)


CMake Warning at C:/msys64/mingw64/share/cmake-3.10/Modules/FindBoost.cmake:801 (message):
  New Boost version may have incorrect or missing dependencies and imported
  targets
Call Stack (most recent call first):
  C:/msys64/mingw64/share/cmake-3.10/Modules/FindBoost.cmake:907 (_Boost_COMPONENT_DEPENDENCIES)
  C:/msys64/mingw64/share/cmake-3.10/Modules/FindBoost.cmake:1542 (_Boost_MISSING_DEPENDENCIES)
  CMakeLists.txt:786 (find_package)


CMake Warning at C:/msys64/mingw64/share/cmake-3.10/Modules/FindBoost.cmake:801 (message):
  New Boost version may have incorrect or missing dependencies and imported
  targets
Call Stack (most recent call first):
  C:/msys64/mingw64/share/cmake-3.10/Modules/FindBoost.cmake:907 (_Boost_COMPONENT_DEPENDENCIES)
  C:/msys64/mingw64/share/cmake-3.10/Modules/FindBoost.cmake:1542 (_Boost_MISSING_DEPENDENCIES)
  CMakeLists.txt:786 (find_package)


CMake Warning at C:/msys64/mingw64/share/cmake-3.10/Modules/FindBoost.cmake:801 (message):
  New Boost version may have incorrect or missing dependencies and imported
  targets
Call Stack (most recent call first):
  C:/msys64/mingw64/share/cmake-3.10/Modules/FindBoost.cmake:907 (_Boost_COMPONENT_DEPENDENCIES)
  C:/msys64/mingw64/share/cmake-3.10/Modules/FindBoost.cmake:1542 (_Boost_MISSING_DEPENDENCIES)
  CMakeLists.txt:786 (find_package)


-- Found Boost Version: 106600
-- Could NOT find Readline (missing: Readline_INCLUDE_DIR)
-- Looking for rl_copy_text
-- Looking for rl_copy_text - not found
-- Looking for rl_filename_completion_function
-- Looking for rl_filename_completion_function - not found
-- Looking for rl_copy_text
-- Looking for rl_copy_text - found
-- Looking for rl_filename_completion_function
-- Looking for rl_filename_completion_function - found
-- Could not find GNU readline library so building without readline support
-- Found Git: C:/msys64/usr/bin/git.exe
Doxygen: graphviz not found - graphs disabled
-- Could NOT find Doxygen (missing: DOXYGEN_EXECUTABLE)
-- Performing Test HAVE_C11
-- Performing Test HAVE_C11 - Success
-- Configuring incomplete, errors occurred!
See also "C:/msys64/usr/src/monero-0.12.0.0/build/debug/CMakeFiles/CMakeOutput.log".
See also "C:/msys64/usr/src/monero-0.12.0.0/build/debug/CMakeFiles/CMakeError.log".
make: *** [Makefile:115: debug-static-win64] Error 1

```



# Discussion History
## whidrasl | 2018-04-06T12:14:07+00:00
https://github.com/monero-project/monero/issues/3523

# Action History
- Created by: Keksov | 2018-04-05T13:45:12+00:00
- Closed at: 2018-04-06T18:04:47+00:00
