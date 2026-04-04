---
title: 'Docker Build failed - make: *** [release-static] Error 1'
source_url: https://github.com/monero-project/monero/issues/3563
author: easyhash
assignees: []
labels: []
created_at: '2018-04-05T19:21:22+00:00'
updated_at: '2018-09-14T11:08:54+00:00'
type: issue
status: closed
closed_at: '2018-09-14T11:08:54+00:00'
---

# Original Description
```
# docker version
Client:
 Version:      17.09.0-ce
 API version:  1.32
 Go version:   go1.8.3
 Git commit:   afdb6d4
 Built:        Tue Sep 26 22:42:18 2017
 OS/Arch:      linux/amd64

Server:
 Version:      17.09.0-ce
 API version:  1.32 (minimum version 1.12)
 Go version:   go1.8.3
 Git commit:   afdb6d4
 Built:        Tue Sep 26 22:40:56 2017
 OS/Arch:      linux/amd64
 Experimental: false
```

```
git clone https://github.com/monero-project/monero.git
cd /monero
docker build --no-cache -t easyhash/monero:manual .
```
```
...
Step 27/32 : RUN rm -rf build &&     if [ -z "$NPROC" ];then make -j$(nproc) release-static;else make -j$NPROC release-static;fi
 ---> Running in 9f6fce8cfb39
mkdir -p build/release
cd build/release && cmake -D STATIC=ON -D ARCH="x86-64" -D BUILD_64=ON -D CMAKE_BUILD_TYPE=release ../.. && make
-- The C compiler identification is GNU 5.4.0
-- The CXX compiler identification is GNU 5.4.0
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
-- Building without build tag
-- Could not find DEVELOPER_LOCAL_TOOLS in env (not required)
-- BOOST_IGNORE_SYSTEM_PATHS defaults to OFF
-- Could not find DEVELOPER_LIBUNBOUND_OLD in env (not required)
-- Building for a 64-bit system
-- Building internal libraries as static
-- Could not find DATABASE in env (not required unless you want to change database type from default: lmdb)
-- Using LMDB as default DB type
-- Stack trace on exception enabled (using easylogging++)
-- Looking for pthread.h
-- Looking for pthread.h - found
-- Looking for pthread_create
-- Looking for pthread_create - not found
-- Check if compiler accepts -pthread
-- Check if compiler accepts -pthread - yes
-- Found Threads: TRUE  
-- Found OpenSSL: /usr/local/openssl-1.0.2n/libssl.a;/usr/local/openssl-1.0.2n/libcrypto.a (found version "1.0.2n") 
-- Using OpenSSL include dir at /usr/local/openssl-1.0.2n/include
-- Found PkgConfig: /usr/bin/pkg-config (found version "0.29.1") 
-- Checking for module 'libpcsclite'
--   No package 'libpcsclite' found
-- Could NOT find PCSC (missing:  PCSC_LIBRARY PCSC_INCLUDE_DIR) 
-- Looking for memset_s in c
-- Looking for memset_s in c - not found
-- Looking for explicit_bzero in c
-- Looking for explicit_bzero in c - not found
-- Looking for strptime
-- Looking for strptime - found
-- Could NOT find MiniUPnPc (missing:  MINIUPNP_INCLUDE_DIR MINIUPNP_LIBRARY) 
-- Using miniupnpc from local source tree for static build
-- Looking for libunbound
CMake Error at external/CMakeLists.txt:82 (add_subdirectory):
  The source directory

    /src/external/unbound

  does not contain a CMakeLists.txt file.


-- Using 64-bit LMDB from source tree
-- Building on x86_64 for x86-64
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
-- Looking for -pie linker flag
-- Looking for -pie linker flag - found
-- Looking for -Wl,-z,relro linker flag
-- Looking for -Wl,-z,relro linker flag - found
-- Looking for -Wl,-z,now linker flag
-- Looking for -Wl,-z,now linker flag - found
-- Looking for -Wl,-z,noexecstack linker flag
-- Looking for -Wl,-z,noexecstack linker flag - found
-- Looking for -Wl,-z,noexecheap linker flag
-- Looking for -Wl,-z,noexecheap linker flag - not found
-- Using C security hardening flags:  -Wformat -Wformat-security -fstack-protector -fstack-protector-strong
-- Using C++ security hardening flags:  -Wformat -Wformat-security -fstack-protector -fstack-protector-strong
-- Using linker security hardening flags:  -pie -Wl,-z,relro -Wl,-z,now -Wl,-z,noexecstack
-- AES support enabled
CMake Warning at /usr/share/cmake-3.5/Modules/FindBoost.cmake:725 (message):
  Imported targets not available for Boost version 106600
Call Stack (most recent call first):
  /usr/share/cmake-3.5/Modules/FindBoost.cmake:763 (_Boost_COMPONENT_DEPENDENCIES)
  /usr/share/cmake-3.5/Modules/FindBoost.cmake:1332 (_Boost_MISSING_DEPENDENCIES)
  CMakeLists.txt:786 (find_package)


CMake Warning at /usr/share/cmake-3.5/Modules/FindBoost.cmake:725 (message):
  Imported targets not available for Boost version 106600
Call Stack (most recent call first):
  /usr/share/cmake-3.5/Modules/FindBoost.cmake:763 (_Boost_COMPONENT_DEPENDENCIES)
  /usr/share/cmake-3.5/Modules/FindBoost.cmake:1332 (_Boost_MISSING_DEPENDENCIES)
  CMakeLists.txt:786 (find_package)


CMake Warning at /usr/share/cmake-3.5/Modules/FindBoost.cmake:725 (message):
  Imported targets not available for Boost version 106600
Call Stack (most recent call first):
  /usr/share/cmake-3.5/Modules/FindBoost.cmake:763 (_Boost_COMPONENT_DEPENDENCIES)
  /usr/share/cmake-3.5/Modules/FindBoost.cmake:1332 (_Boost_MISSING_DEPENDENCIES)
  CMakeLists.txt:786 (find_package)


CMake Warning at /usr/share/cmake-3.5/Modules/FindBoost.cmake:725 (message):
  Imported targets not available for Boost version 106600
Call Stack (most recent call first):
  /usr/share/cmake-3.5/Modules/FindBoost.cmake:763 (_Boost_COMPONENT_DEPENDENCIES)
  /usr/share/cmake-3.5/Modules/FindBoost.cmake:1332 (_Boost_MISSING_DEPENDENCIES)
  CMakeLists.txt:786 (find_package)


CMake Warning at /usr/share/cmake-3.5/Modules/FindBoost.cmake:725 (message):
  Imported targets not available for Boost version 106600
Call Stack (most recent call first):
  /usr/share/cmake-3.5/Modules/FindBoost.cmake:763 (_Boost_COMPONENT_DEPENDENCIES)
  /usr/share/cmake-3.5/Modules/FindBoost.cmake:1332 (_Boost_MISSING_DEPENDENCIES)
  CMakeLists.txt:786 (find_package)


CMake Warning at /usr/share/cmake-3.5/Modules/FindBoost.cmake:725 (message):
  Imported targets not available for Boost version 106600
Call Stack (most recent call first):
  /usr/share/cmake-3.5/Modules/FindBoost.cmake:763 (_Boost_COMPONENT_DEPENDENCIES)
  /usr/share/cmake-3.5/Modules/FindBoost.cmake:1332 (_Boost_MISSING_DEPENDENCIES)
  CMakeLists.txt:786 (find_package)


CMake Warning at /usr/share/cmake-3.5/Modules/FindBoost.cmake:725 (message):
  Imported targets not available for Boost version 106600
Call Stack (most recent call first):
  /usr/share/cmake-3.5/Modules/FindBoost.cmake:763 (_Boost_COMPONENT_DEPENDENCIES)
  /usr/share/cmake-3.5/Modules/FindBoost.cmake:1332 (_Boost_MISSING_DEPENDENCIES)
  CMakeLists.txt:786 (find_package)


CMake Warning at /usr/share/cmake-3.5/Modules/FindBoost.cmake:725 (message):
  Imported targets not available for Boost version 106600
Call Stack (most recent call first):
  /usr/share/cmake-3.5/Modules/FindBoost.cmake:763 (_Boost_COMPONENT_DEPENDENCIES)
  /usr/share/cmake-3.5/Modules/FindBoost.cmake:1332 (_Boost_MISSING_DEPENDENCIES)
  CMakeLists.txt:786 (find_package)


CMake Warning at /usr/share/cmake-3.5/Modules/FindBoost.cmake:725 (message):
  Imported targets not available for Boost version 106600
Call Stack (most recent call first):
  /usr/share/cmake-3.5/Modules/FindBoost.cmake:763 (_Boost_COMPONENT_DEPENDENCIES)
  /usr/share/cmake-3.5/Modules/FindBoost.cmake:1332 (_Boost_MISSING_DEPENDENCIES)
  CMakeLists.txt:786 (find_package)


-- Found Boost Version: 106600
-- Looking for rl_copy_text
-- Looking for rl_copy_text - not found
-- Looking for rl_filename_completion_function
-- Looking for rl_filename_completion_function - not found
-- Looking for rl_copy_text
-- Looking for rl_copy_text - not found
-- Looking for rl_filename_completion_function
-- Looking for rl_filename_completion_function - not found
-- Could not find GNU readline library so building without readline support
-- Found Git: /usr/bin/git
-- Found Doxygen: /usr/bin/doxygen (found version "1.8.11") 
-- Performing Test HAVE_C11
-- Performing Test HAVE_C11 - Success
-- Configuring incomplete, errors occurred!
See also "/src/build/release/CMakeFiles/CMakeOutput.log".
See also "/src/build/release/CMakeFiles/CMakeError.log".
Makefile:68: recipe for target 'release-static' failed
make: *** [release-static] Error 1
The command '/bin/sh -c rm -rf build &&     if [ -z "$NPROC" ];then make -j$(nproc) release-static;else make -j$NPROC release-static;fi' returned a non-zero code: 2
```

# Discussion History
## anonimal | 2018-04-05T19:48:13+00:00
As stated in the README: https://github.com/monero-project/monero#cloning-the-repository

`$ git clone --recursive https://github.com/monero-project/monero`

## moneromooo-monero | 2018-04-06T17:24:24+00:00
I think that's the docker config that needs updating to get submodules.

## homdx | 2018-06-11T21:28:28+00:00
My commit is fix you issue?
https://github.com/monero-project/monero/pull/3879

## moneromooo-monero | 2018-09-14T11:06:22+00:00
I'll call that fixed, open a new bug if it breaks again.

+resolved

# Action History
- Created by: easyhash | 2018-04-05T19:21:22+00:00
- Closed at: 2018-09-14T11:08:54+00:00
