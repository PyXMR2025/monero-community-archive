---
title: Unable to build 0.14.1.2 on Debian 10
source_url: https://github.com/monero-project/monero/issues/5963
author: fafrd
assignees: []
labels: []
created_at: '2019-10-06T03:51:09+00:00'
updated_at: '2019-10-07T12:58:11+00:00'
type: issue
status: closed
closed_at: '2019-10-07T12:58:11+00:00'
---

# Original Description
On Debian 10 "buster", my build ends like:
```
-- Configuring incomplete, errors occurred!
See also "/home/monero/current/build/release/CMakeFiles/CMakeOutput.log".
See also "/home/monero/current/build/release/CMakeFiles/CMakeError.log".
```

Inside CMakeError.log, I see the following:
```
Run Build Command:"/usr/bin/make" "cmTC_0c7bf/fast"
make[1]: Entering directory '/home/monero/monero-0.14.1.2/build/release/CMakeFiles/CMakeTmp'
/usr/bin/make -f CMakeFiles/cmTC_0c7bf.dir/build.make CMakeFiles/cmTC_0c7bf.dir/build
make[2]: Entering directory '/home/monero/monero-0.14.1.2/build/release/CMakeFiles/CMakeTmp'
Building C object CMakeFiles/cmTC_0c7bf.dir/CheckFunctionExists.c.o
/usr/bin/cc   -pthread -DCHECK_FUNCTION_EXISTS=memset_s   -o CMakeFiles/cmTC_0c7bf.dir/CheckFunctionExists.c.o   -c /usr/share/cmake-3.13/Modules/CheckFunctionExists.c
Linking C executable cmTC_0c7bf
/usr/bin/cmake -E cmake_link_script CMakeFiles/cmTC_0c7bf.dir/link.txt --verbose=1
/usr/bin/cc  -pthread -DCHECK_FUNCTION_EXISTS=memset_s    -rdynamic CMakeFiles/cmTC_0c7bf.dir/CheckFunctionExists.c.o  -o cmTC_0c7bf  -L/home/monero/current/build/release/CMakeFiles/CMakeTmp/string.h -Wl,-rpath,/home/monero/current/build/release/CMakeFiles/CMakeTmp/string.h -lc
/usr/bin/ld: CMakeFiles/cmTC_0c7bf.dir/CheckFunctionExists.c.o: in function `main':
CheckFunctionExists.c:(.text+0x10): undefined reference to `memset_s'
collect2: error: ld returned 1 exit status
make[2]: *** [CMakeFiles/cmTC_0c7bf.dir/build.make:87: cmTC_0c7bf] Error 1
make[2]: Leaving directory '/home/monero/monero-0.14.1.2/build/release/CMakeFiles/CMakeTmp'
make[1]: *** [Makefile:121: cmTC_0c7bf/fast] Error 2
make[1]: Leaving directory '/home/monero/monero-0.14.1.2/build/release/CMakeFiles/CMakeTmp'
```

What is ```undefined reference to `memset_s'```?

# Discussion History
## moneromooo-monero | 2019-10-06T18:26:13+00:00
It means memset_s is not found in the libraries given.

Paste what comes before "-- Configuring incomplete, errors occurred!", that's what will tell us where the problem is.

## fafrd | 2019-10-06T23:56:26+00:00
Here's the whole log: 

```
ls: cannot access '.git/config': No such file or directory
fatal: not a git repository (or any of the parent directories): .git
mkdir -p build/release
cd build/release && cmake -D BUILD_TESTS=ON -D CMAKE_BUILD_TYPE=release ../.. && make
-- CMake version 3.13.4
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
-- The ASM compiler identification is GNU
-- Found assembler: /usr/bin/cc
-- Building without build tag
-- Found Git: /usr/bin/git (found version "2.20.1") 
-- Checking submodules
fatal: not a git repository (or any of the parent directories): .git
fatal: not a git repository (or any of the parent directories): .git
-- Submodule 'external/miniupnp' is up-to-date
fatal: not a git repository (or any of the parent directories): .git
fatal: not a git repository (or any of the parent directories): .git
-- Submodule 'external/unbound' is up-to-date
fatal: not a git repository (or any of the parent directories): .git
fatal: not a git repository (or any of the parent directories): .git
-- Submodule 'external/rapidjson' is up-to-date
fatal: not a git repository (or any of the parent directories): .git
fatal: not a git repository (or any of the parent directories): .git
-- Submodule 'external/trezor-common' is up-to-date
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
-- Performing Test _pthread_c
-- Performing Test _pthread_c - Success
-- Performing Test _pthread_cxx
-- Performing Test _pthread_cxx - Success
-- Found OpenSSL: /usr/lib/x86_64-linux-gnu/libcrypto.so (found version "1.1.1d")  
-- Using OpenSSL include dir at /usr/include
-- Found HIDAPI: /usr/lib/x86_64-linux-gnu/libhidapi-libusb.so  
-- Looking for memset_s in c
-- Looking for memset_s in c - not found
-- Looking for explicit_bzero in c
-- Looking for explicit_bzero in c - found
-- Looking for strptime
-- Looking for strptime - found
-- Found MiniUPnPc: /usr/include/miniupnpc  
-- Found miniupnpc API version 17
-- Using in-tree miniupnpc
CMake Error at external/CMakeLists.txt:41 (add_subdirectory):
  add_subdirectory given source "miniupnp/miniupnpc" which is not an existing
  directory.


CMake Error at external/CMakeLists.txt:42 (set_property):
  set_property could not find TARGET libminiupnpc-static.  Perhaps it has not
  yet been created.


CMake Error at external/CMakeLists.txt:46 (set_property):
  set_property could not find TARGET libminiupnpc-static.  Perhaps it has not
  yet been created.


-- Looking for libunbound
-- Found libunbound include (unbound.h) in /usr/include
-- Found libunbound shared library
-- Using 64-bit LMDB from source tree
-- Looking for backtrace
-- Looking for backtrace - found
-- backtrace facility detected in default set of libraries
-- Backtrace_LIBRARY: 
-- Found Backtrace: /usr/include  
-- Using HIDAPI include dir at /usr/include/hidapi
-- Found Protobuf: /usr/lib/x86_64-linux-gnu/libprotobuf.so;-pthread (found version "3.6.1") 
-- Protobuf lib: /usr/lib/x86_64-linux-gnu/libprotobuf.so, inc: /usr/include, protoc: /usr/bin/protoc
CMake Warning at cmake/CheckTrezor.cmake:126 (message):
  Trezor protobuf messages could not be regenerated (err=1, python ).OUT: ,
  ERR: Traceback (most recent call last):

    File "tools/build_protob.py", line 21, in <module>
      "trezor-common submodule seems to be missing.\n"

  ValueError: trezor-common submodule seems to be missing.

  Use "git submodule update --init --recursive" to retrieve it.

  .Please read src/device_trezor/trezor/tools/README.md
Call Stack (most recent call first):
  CMakeLists.txt:522 (include)


-- Building on x86_64 for native
-- Performing Test CC_SUPPORTS_MARCH_NATIVE
-- Performing Test CC_SUPPORTS_MARCH_NATIVE - Success
-- AES support enabled
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
-- Performing Test _fcf_protection=full_c
-- Performing Test _fcf_protection=full_c - Success
-- Performing Test _fcf_protection=full_cxx
-- Performing Test _fcf_protection=full_cxx - Success
-- Performing Test _fstack_clash_protection_c
-- Performing Test _fstack_clash_protection_c - Success
-- Performing Test _fstack_clash_protection_cxx
-- Performing Test _fstack_clash_protection_cxx - Success
-- Performing Test _mmitigate_rop_c
-- Performing Test _mmitigate_rop_c - Success
-- Performing Test _mmitigate_rop_cxx
-- Performing Test _mmitigate_rop_cxx - Success
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
-- Using C security hardening flags:  -Wformat -Wformat-security -fstack-protector -fstack-protector-strong -fcf-protection=full -fstack-clash-protection -mmitigate-rop
-- Using C++ security hardening flags:  -Wformat -Wformat-security -fstack-protector -fstack-protector-strong -fcf-protection=full -fstack-clash-protection -mmitigate-rop
-- Using linker security hardening flags:  -pie -Wl,-z,relro -Wl,-z,now -Wl,-z,noexecstack
-- Found Boost Version: 106700
-- Found Readline: /usr/include  
-- Looking for rl_copy_text
-- Looking for rl_copy_text - found
-- Looking for rl_filename_completion_function
-- Looking for rl_filename_completion_function - found
-- Found readline library at: /usr
-- Found Git: /usr/bin/git
-- Trezor support disabled
-- Could NOT find GTest (missing: GTEST_LIBRARY GTEST_INCLUDE_DIR GTEST_MAIN_LIBRARY) 
-- GTest not found on the system: will use GTest bundled with this source
CMake Warning at tests/functional_tests/CMakeLists.txt:59 (message):
  functional_tests_rpc skipped, needs the 'requests' python module


-- Found Doxygen: /usr/bin/doxygen (found version "1.8.13") found components:  doxygen dot 
-- Performing Test HAVE_C11
-- Performing Test HAVE_C11 - Success
-- Found PythonInterp: /usr/bin/python (found version "2.7.16") 
-- Configuring incomplete, errors occurred!
See also "/home/monero/current/build/release/CMakeFiles/CMakeOutput.log".
See also "/home/monero/current/build/release/CMakeFiles/CMakeError.log".
make: *** [Makefile:99: release-all] Error 1
```

## xiphon | 2019-10-07T00:29:37+00:00
Did you download Github-provided sources archive? It can't be used to build Monero.

You have to download the sources using `git clone`. See https://github.com/monero-project/monero#cloning-the-repository

## fafrd | 2019-10-07T12:58:11+00:00
Ah, makes sense. Yeah, I just downloaded the source from the releases page.

Once I did a `clone --recursive` and checked out the tag I wanted it built perfectly. Thank you!

# Action History
- Created by: fafrd | 2019-10-06T03:51:09+00:00
- Closed at: 2019-10-07T12:58:11+00:00
