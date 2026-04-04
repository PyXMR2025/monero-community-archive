---
title: Make build failed
source_url: https://github.com/monero-project/monero/issues/6768
author: lh1008
assignees: []
labels: []
created_at: '2020-08-16T20:48:37+00:00'
updated_at: '2020-08-17T18:15:25+00:00'
type: issue
status: closed
closed_at: '2020-08-17T18:13:18+00:00'
---

# Original Description
Hello everyone,

This was while doing the Monero [Building Instructions](https://github.com/monero-project/monero#build-instructions). I git cloned and also installed all dependencies.

This is what I did, Ubuntu 18.04.4 LTS:

Terminal

Input:
`make`


Output:
`mkdir -p build/"Linux/release-v0.16"/release
cd build/"Linux/release-v0.16"/release && cmake -D BUILD_TESTS=ON -D CMAKE_BUILD_TYPE=release ../../../.. && make
-- CMake version 3.10.2
ccache NOT found!
-- Building without build tag
-- Checking submodules
-- Submodule 'external/miniupnp' is up-to-date
-- Submodule 'external/unbound' is up-to-date
-- Submodule 'external/rapidjson' is up-to-date
-- Submodule 'external/trezor-common' is up-to-date
-- Submodule 'external/randomx' is up-to-date
-- Could not find DEVELOPER_LOCAL_TOOLS in env (not required)
-- BOOST_IGNORE_SYSTEM_PATHS defaults to OFF
-- Could not find DEVELOPER_LIBUNBOUND_OLD in env (not required)
-- Building for a 64-bit system
-- Building internal libraries as static
-- Using LMDB as default DB type
-- Stack trace on exception enabled (using easylogging++)
-- Using OpenSSL include dir at /usr/include
-- Could NOT find MiniUPnPc (missing: MINIUPNP_INCLUDE_DIR MINIUPNP_LIBRARY) 
-- Using in-tree miniupnpc
-- Looking for libunbound
-- Found libunbound include (unbound.h) in /usr/include
-- Found libunbound shared library
-- Using 64-bit LMDB from source tree
-- Backtrace_LIBRARY: 
-- Performing Test _march=native_cxx
-- Performing Test _march=native_cxx - Success
-- Setting CXX flag -march=native
-- Performing Test _march=native_c
-- Performing Test _march=native_c - Success
-- Setting C flag -march=native
-- Using HIDAPI include dir at /usr/include/hidapi
-- Found Protobuf: /usr/lib/x86_64-linux-gnu/libprotobuf.so;-pthread (found version "3.0.0") 
-- Found Protobuf: /usr/lib/x86_64-linux-gnu/libprotobuf.so;-pthread;-pthread (found version "3.0.0") 
-- Protobuf lib: /usr/lib/x86_64-linux-gnu/libprotobuf.so, inc: /usr/include, protoc: /usr/bin/protoc
-- Trezor protobuf messages regenerated out: "."
-- Checking for module 'libusb-1.0'
--   No package 'libusb-1.0' found
-- Checking for module 'libusb'
--   Found libusb, version 0.1.12
-- LibUSB not found, try setting LibUSB_ROOT_DIR environment variable.
-- Building on x86_64 for native
-- AES support enabled
-- Performing Test _fcf_protection=full_c
-- Performing Test _fcf_protection=full_c - Failed
-- Performing Test _fcf_protection=full_cxx
-- Performing Test _fcf_protection=full_cxx - Failed
-- Using C security hardening flags:  -Wformat -Wformat-security -fstack-protector
-- Using C++ security hardening flags:  -Wformat -Wformat-security -fstack-protector -fstack-protector-strong -mmitigate-rop
-- Using linker security hardening flags:  -pie -Wl,-z,relro -Wl,-z,now -Wl,-z,noexecstack
-- Found Boost Version: 106501
-- Found readline library at: /usr
-- Found Git: /usr/bin/git
-- You are currently on commit 7bd1ed03d
-- The most recent tag was at 7bd1ed03d
-- You are building a tagged release
-- Trezor support enabled
-- Building tests
Traceback (most recent call last):
  File "<string>", line 1, in <module>
ImportError: No module named requests
CMake Warning at tests/functional_tests/CMakeLists.txt:73 (message):
  functional_tests_rpc skipped, needs the 'requests' python module


-- Not building debug utilities
-- Configuring done
-- Generating done
-- Build files have been written to: /home/siddha/monero/build/Linux/release-v0.16/release
make[1]: Entering directory '/home/siddha/monero/build/Linux/release-v0.16/release'
make[2]: Entering directory '/home/siddha/monero/build/Linux/release-v0.16/release'
make[3]: Entering directory '/home/siddha/monero/build/Linux/release-v0.16/release'
make[3]: Leaving directory '/home/siddha/monero/build/Linux/release-v0.16/release'
[  2%] Built target generate_translations_header
make[3]: Entering directory '/home/siddha/monero/build/Linux/release-v0.16/release'
make[3]: Leaving directory '/home/siddha/monero/build/Linux/release-v0.16/release'
[  6%] Built target libminiupnpc-static
make[3]: Entering directory '/home/siddha/monero/build/Linux/release-v0.16/release'
make[3]: Leaving directory '/home/siddha/monero/build/Linux/release-v0.16/release'
[  6%] Built target lmdb
make[3]: Entering directory '/home/siddha/monero/build/Linux/release-v0.16/release'
make[3]: Leaving directory '/home/siddha/monero/build/Linux/release-v0.16/release'
[  6%] Built target easylogging
make[3]: Entering directory '/home/siddha/monero/build/Linux/release-v0.16/release'
make[3]: Leaving directory '/home/siddha/monero/build/Linux/release-v0.16/release'
make[3]: Entering directory '/home/siddha/monero/build/Linux/release-v0.16/release'
[  7%] Building CXX object contrib/epee/src/CMakeFiles/epee.dir/byte_slice.cpp.o
[  7%] Building CXX object contrib/epee/src/CMakeFiles/epee.dir/byte_stream.cpp.o
[  7%] Building CXX object contrib/epee/src/CMakeFiles/epee.dir/hex.cpp.o
[  7%] Building CXX object contrib/epee/src/CMakeFiles/epee.dir/abstract_http_client.cpp.o
[  7%] Building CXX object contrib/epee/src/CMakeFiles/epee.dir/http_auth.cpp.o
[  8%] Building CXX object contrib/epee/src/CMakeFiles/epee.dir/mlog.cpp.o
[  8%] Building CXX object contrib/epee/src/CMakeFiles/epee.dir/net_helper.cpp.o
[  8%] Building CXX object contrib/epee/src/CMakeFiles/epee.dir/net_utils_base.cpp.o
[  8%] Building CXX object contrib/epee/src/CMakeFiles/epee.dir/string_tools.cpp.o
[  9%] Building CXX object contrib/epee/src/CMakeFiles/epee.dir/wipeable_string.cpp.o
[  9%] Building CXX object contrib/epee/src/CMakeFiles/epee.dir/levin_base.cpp.o
[  9%] Building C object contrib/epee/src/CMakeFiles/epee.dir/memwipe.c.o
[  9%] Building CXX object contrib/epee/src/CMakeFiles/epee.dir/connection_basic.cpp.o
[ 10%] Building CXX object contrib/epee/src/CMakeFiles/epee.dir/network_throttle.cpp.o
[ 10%] Building CXX object contrib/epee/src/CMakeFiles/epee.dir/network_throttle-detail.cpp.o
[ 10%] Building CXX object contrib/epee/src/CMakeFiles/epee.dir/mlocker.cpp.o
[ 10%] Building CXX object contrib/epee/src/CMakeFiles/epee.dir/buffer.cpp.o
[ 10%] Building CXX object contrib/epee/src/CMakeFiles/epee.dir/net_ssl.cpp.o
[ 11%] Building CXX object contrib/epee/src/CMakeFiles/epee.dir/int-util.cpp.o
[ 11%] Linking CXX static library libepee.a
make[3]: Leaving directory '/home/siddha/monero/build/Linux/release-v0.16/release'
[ 11%] Built target epee
make[3]: Entering directory '/home/siddha/monero/build/Linux/release-v0.16/release'
make[3]: Leaving directory '/home/siddha/monero/build/Linux/release-v0.16/release'
[ 11%] Built target epee_readline
make[3]: Entering directory '/home/siddha/monero/build/Linux/release-v0.16/release'
make[3]: Leaving directory '/home/siddha/monero/build/Linux/release-v0.16/release'
[ 11%] Built target genversion
make[3]: Entering directory '/home/siddha/monero/build/Linux/release-v0.16/release'
make[3]: Leaving directory '/home/siddha/monero/build/Linux/release-v0.16/release'
[ 11%] Built target obj_version
make[3]: Entering directory '/home/siddha/monero/build/Linux/release-v0.16/release'
make[3]: Leaving directory '/home/siddha/monero/build/Linux/release-v0.16/release'
[ 12%] Built target version
make[3]: Entering directory '/home/siddha/monero/build/Linux/release-v0.16/release'
make[3]: Leaving directory '/home/siddha/monero/build/Linux/release-v0.16/release'
[ 17%] Built target obj_cncrypto
make[3]: Entering directory '/home/siddha/monero/build/Linux/release-v0.16/release'
make[3]: Leaving directory '/home/siddha/monero/build/Linux/release-v0.16/release'
make[3]: Entering directory '/home/siddha/monero/build/Linux/release-v0.16/release'
[ 18%] Building CXX object external/randomx/CMakeFiles/randomx.dir/src/aes_hash.cpp.o
[ 18%] Building C object external/randomx/CMakeFiles/randomx.dir/src/argon2_ref.c.o
[ 18%] Building C object external/randomx/CMakeFiles/randomx.dir/src/argon2_ssse3.c.o
[ 18%] Building C object external/randomx/CMakeFiles/randomx.dir/src/argon2_avx2.c.o
[ 19%] Building CXX object external/randomx/CMakeFiles/randomx.dir/src/bytecode_machine.cpp.o
[ 19%] Building CXX object external/randomx/CMakeFiles/randomx.dir/src/cpu.cpp.o
[ 19%] Building CXX object external/randomx/CMakeFiles/randomx.dir/src/dataset.cpp.o
[ 19%] Building CXX object external/randomx/CMakeFiles/randomx.dir/src/soft_aes.cpp.o
[ 19%] Building CXX object external/randomx/CMakeFiles/randomx.dir/src/virtual_memory.cpp.o
[ 20%] Building CXX object external/randomx/CMakeFiles/randomx.dir/src/vm_interpreted.cpp.o
[ 20%] Building CXX object external/randomx/CMakeFiles/randomx.dir/src/allocator.cpp.o
[ 20%] Building CXX object external/randomx/CMakeFiles/randomx.dir/src/assembly_generator_x86.cpp.o
[ 20%] Building CXX object external/randomx/CMakeFiles/randomx.dir/src/instruction.cpp.o
[ 21%] Building CXX object external/randomx/CMakeFiles/randomx.dir/src/randomx.cpp.o
[ 21%] Building CXX object external/randomx/CMakeFiles/randomx.dir/src/superscalar.cpp.o
[ 21%] Building CXX object external/randomx/CMakeFiles/randomx.dir/src/vm_compiled.cpp.o
[ 21%] Building CXX object external/randomx/CMakeFiles/randomx.dir/src/vm_interpreted_light.cpp.o
[ 22%] Building C object external/randomx/CMakeFiles/randomx.dir/src/argon2_core.c.o
[ 22%] Building CXX object external/randomx/CMakeFiles/randomx.dir/src/blake2_generator.cpp.o
[ 22%] Building CXX object external/randomx/CMakeFiles/randomx.dir/src/instructions_portable.cpp.o
[ 22%] Building C object external/randomx/CMakeFiles/randomx.dir/src/reciprocal.c.o
/home/siddha/monero/external/randomx/src/reciprocal.c: In function ‘randomx_reciprocal’:
/home/siddha/monero/external/randomx/src/reciprocal.c:57:2: error: ‘for’ loop initial declarations are only allowed in C99 mode
  for (uint64_t bit = divisor; bit > 0; bit >>= 1)
  ^
/home/siddha/monero/external/randomx/src/reciprocal.c:57:2: note: use option -std=c99 or -std=gnu99 to compile your code
/home/siddha/monero/external/randomx/src/reciprocal.c:60:2: error: ‘for’ loop initial declarations are only allowed in C99 mode
  for (unsigned shift = 0; shift < bsr; shift++) {
  ^
external/randomx/CMakeFiles/randomx.dir/build.make:542: recipe for target 'external/randomx/CMakeFiles/randomx.dir/src/reciprocal.c.o' failed
make[3]: *** [external/randomx/CMakeFiles/randomx.dir/src/reciprocal.c.o] Error 1
make[3]: Leaving directory '/home/siddha/monero/build/Linux/release-v0.16/release'
CMakeFiles/Makefile2:402: recipe for target 'external/randomx/CMakeFiles/randomx.dir/all' failed
make[2]: *** [external/randomx/CMakeFiles/randomx.dir/all] Error 2
make[2]: Leaving directory '/home/siddha/monero/build/Linux/release-v0.16/release'
Makefile:140: recipe for target 'all' failed
make[1]: *** [all] Error 2
make[1]: Leaving directory '/home/siddha/monero/build/Linux/release-v0.16/release'
Makefile:102: recipe for target 'release-all' failed
make: *** [release-all] Error 2`

# Discussion History
## selsta | 2020-08-16T22:36:43+00:00
Can you try to clone from scratch and try again?

Ubuntu 18.04 CI compiled latest master successfully: https://github.com/monero-project/monero/runs/991126125

## lh1008 | 2020-08-17T13:02:28+00:00
Hey @selsta,

In `Run actions/checkout@v1` from  https://github.com/monero-project/monero/runs/991126125 in the `git -c http.extraheader="AUTHORIZATION: basic ***" fetch --tags --prune --progress --no-recurse-submodules origin +refs/heads/*:refs/remotes/origin/*` step, I get the following:

`fatal: unable to access 'https://github.com/monero-project/monero/': The requested URL returned error: 400`

Is that an internet connection problem? When I go directly to the link https://github.com/monero-project/monero/ it opens as usual.

## selsta | 2020-08-17T13:05:20+00:00
No I meant can you try to clone and build from scratch using this tutorial? https://github.com/monero-project/monero#build-instructions

Does it result in the same error?

## lh1008 | 2020-08-17T13:40:31+00:00
Let me try again. Yesterday I tried several times and got the same error each time I reached the `make`. That's when I decided to post this issue. 



## lh1008 | 2020-08-17T14:16:15+00:00
Hey @selsta,

I tried it again and I get to the same error. This time I cloned without the `--recursive`, I was asked to install all submodules, `git submodule update --init --force` but I get the same error:

/home/siddha/monero/external/randomx/src/reciprocal.c: In function ‘randomx_reciprocal’:
/home/siddha/monero/external/randomx/src/reciprocal.c:57:2: error: ‘for’ loop initial declarations are only allowed in C99 mode
  for (uint64_t bit = divisor; bit > 0; bit >>= 1)
  ^
/home/siddha/monero/external/randomx/src/reciprocal.c:57:2: note: use option -std=c99 or -std=gnu99 to compile your code
/home/siddha/monero/external/randomx/src/reciprocal.c:60:2: error: ‘for’ loop initial declarations are only allowed in C99 mode
  for (unsigned shift = 0; shift < bsr; shift++) {
  ^
external/randomx/CMakeFiles/randomx.dir/build.make:542: recipe for target 'external/randomx/CMakeFiles/randomx.dir/src/reciprocal.c.o' failed
make[3]: *** [external/randomx/CMakeFiles/randomx.dir/src/reciprocal.c.o] Error 1
make[3]: Leaving directory '/home/siddha/monero/build/Linux/release-v0.16/release'
CMakeFiles/Makefile2:402: recipe for target 'external/randomx/CMakeFiles/randomx.dir/all' failed
make[2]: *** [external/randomx/CMakeFiles/randomx.dir/all] Error 2
make[2]: Leaving directory '/home/siddha/monero/build/Linux/release-v0.16/release'
Makefile:140: recipe for target 'all' failed
make[1]: *** [all] Error 2
make[1]: Leaving directory '/home/siddha/monero/build/Linux/release-v0.16/release'
Makefile:102: recipe for target 'release-all' failed
make: *** [release-all] Error 2 

## lh1008 | 2020-08-17T14:17:28+00:00
I'm doing it again, following the exact same instructions.

`git clone --recursive https://github.com/monero-project/monero`

## selsta | 2020-08-17T14:18:03+00:00
I will try to setup a Ubuntu 18.04 VM and see if I can reproduce.

## lh1008 | 2020-08-17T14:20:10+00:00
Thank you :)

## lh1008 | 2020-08-17T14:21:53+00:00
Anyway I know I got further:

mkdir -p build/"Linux/release-v0.16"/release
cd build/"Linux/release-v0.16"/release && cmake -D BUILD_TESTS=ON -D CMAKE_BUILD_TYPE=release ../../../.. && make
-- CMake version 3.10.2
ccache NOT found!
-- Building without build tag
-- Checking submodules
-- Submodule 'external/miniupnp' is up-to-date
-- Submodule 'external/unbound' is up-to-date
-- Submodule 'external/rapidjson' is up-to-date
-- Submodule 'external/trezor-common' is up-to-date
-- Submodule 'external/randomx' is up-to-date
-- Could not find DEVELOPER_LOCAL_TOOLS in env (not required)
-- BOOST_IGNORE_SYSTEM_PATHS defaults to OFF
-- Could not find DEVELOPER_LIBUNBOUND_OLD in env (not required)
-- Building for a 64-bit system
-- Building internal libraries as static
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
-- Found OpenSSL: /usr/lib/x86_64-linux-gnu/libcrypto.so (found version "1.1.1") 
-- Using OpenSSL include dir at /usr/include
-- Found HIDAPI: /usr/lib/x86_64-linux-gnu/libhidapi-libusb.so  
-- Looking for memset_s in c
-- Looking for memset_s in c - not found
-- Looking for explicit_bzero in c
-- Looking for explicit_bzero in c - found
-- Looking for strptime
-- Looking for strptime - found
-- Could NOT find MiniUPnPc (missing: MINIUPNP_INCLUDE_DIR MINIUPNP_LIBRARY) 
-- Using in-tree miniupnpc
-- Looking for libunbound
-- Found libunbound include (unbound.h) in /usr/include
-- Found libunbound shared library
-- Using 64-bit LMDB from source tree
-- Looking for backtrace
-- Looking for backtrace - found
-- backtrace facility detected in default set of libraries
-- Backtrace_LIBRARY: 
-- Found Backtrace: /usr/include  
-- Performing Test _maes_cxx
-- Performing Test _maes_cxx - Success
-- Setting CXX flag -maes
-- Performing Test _maes_c
-- Performing Test _maes_c - Success
-- Setting C flag -maes
-- Performing Test HAVE_SSSE3
-- Performing Test HAVE_SSSE3 - Success
-- Performing Test HAVE_AVX2
-- Performing Test HAVE_AVX2 - Success
-- Performing Test HAVE_CXX_ATOMICS
-- Performing Test HAVE_CXX_ATOMICS - Success
-- Using HIDAPI include dir at /usr/include/hidapi
-- Found Protobuf: /usr/lib/x86_64-linux-gnu/libprotobuf.so;-pthread (found version "3.0.0") 
-- Found Protobuf: /usr/lib/x86_64-linux-gnu/libprotobuf.so;-pthread;-pthread (found version "3.0.0") 
-- Protobuf lib: /usr/lib/x86_64-linux-gnu/libprotobuf.so, inc: /usr/include, protoc: /usr/bin/protoc
-- Trezor protobuf messages regenerated out: "."
-- Found PkgConfig: /usr/bin/pkg-config (found version "0.29.1") 
-- Checking for module 'libusb-1.0'
--   No package 'libusb-1.0' found
-- Checking for module 'libusb'
--   Found libusb, version 0.1.12
-- LibUSB not found, try setting LibUSB_ROOT_DIR environment variable.
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
-- Performing Test _fstack_protector_strong_c - Failed
-- Performing Test _fstack_protector_strong_cxx
-- Performing Test _fstack_protector_strong_cxx - Success
-- Performing Test _fcf_protection=full_c
-- Performing Test _fcf_protection=full_c - Failed
-- Performing Test _fcf_protection=full_cxx
-- Performing Test _fcf_protection=full_cxx - Failed
-- Performing Test _fstack_clash_protection_c
-- Performing Test _fstack_clash_protection_c - Failed
-- Performing Test _fstack_clash_protection_cxx
-- Performing Test _fstack_clash_protection_cxx - Failed
-- Performing Test _mmitigate_rop_c
-- Performing Test _mmitigate_rop_c - Failed
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
-- Using C security hardening flags:  -Wformat -Wformat-security -fstack-protector
-- Using C++ security hardening flags:  -Wformat -Wformat-security -fstack-protector -fstack-protector-strong -mmitigate-rop
-- Using linker security hardening flags:  -pie -Wl,-z,relro -Wl,-z,now -Wl,-z,noexecstack
-- Found Boost Version: 106501
-- Found Readline: /usr/include  
-- Looking for rl_copy_text
-- Looking for rl_copy_text - found
-- Looking for rl_filename_completion_function
-- Looking for rl_filename_completion_function - found
-- Found readline library at: /usr
-- Found Git: /usr/bin/git
-- You are currently on commit 7bd1ed03d
-- The most recent tag was at 7bd1ed03d
-- You are building a tagged release
-- Trezor support enabled
-- Building tests
-- Found GTest: /usr/lib/libgtest.a  
Traceback (most recent call last):
  File "<string>", line 1, in <module>
ImportError: No module named requests
CMake Warning at tests/functional_tests/CMakeLists.txt:73 (message):
  functional_tests_rpc skipped, needs the 'requests' python module


-- Not building debug utilities
-- Found Doxygen: /usr/bin/doxygen (found version "1.8.13") found components:  doxygen dot 
-- Performing Test HAVE_C11
-- Performing Test HAVE_C11 - Success
-- Configuring done
-- Generating done
-- Build files have been written to: /home/siddha/monero/build/Linux/release-v0.16/release
make[1]: Entering directory '/home/siddha/monero/build/Linux/release-v0.16/release'
make[2]: Entering directory '/home/siddha/monero/build/Linux/release-v0.16/release'
make[3]: Entering directory '/home/siddha/monero/build/Linux/release-v0.16/release'
Scanning dependencies of target generate_translations_header
make[3]: Leaving directory '/home/siddha/monero/build/Linux/release-v0.16/release'
make[3]: Entering directory '/home/siddha/monero/build/Linux/release-v0.16/release'
[  0%] Creating directories for 'generate_translations_header'
[  0%] No download step for 'generate_translations_header'
[  0%] No patch step for 'generate_translations_header'
[  0%] No update step for 'generate_translations_header'
[  1%] Performing configure step for 'generate_translations_header'
-- The C compiler identification is GNU 4.8.5
-- The CXX compiler identification is GNU 7.5.0
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
lrelease: could not exec '/usr/lib/x86_64-linux-gnu/qt4/bin/lrelease': No such file or directory
CMake Warning at CMakeLists.txt:59 (message):
  lrelease program not working, translation files not built


-- Configuring done
-- Generating done
-- Build files have been written to: /home/siddha/monero/build/Linux/release-v0.16/release/translations
[  1%] Performing build step for 'generate_translations_header'
make[4]: Entering directory '/home/siddha/monero/build/Linux/release-v0.16/release/translations'
make[5]: Entering directory '/home/siddha/monero/build/Linux/release-v0.16/release/translations'
make[6]: Entering directory '/home/siddha/monero/build/Linux/release-v0.16/release/translations'
Scanning dependencies of target generate_translations_header
make[6]: Leaving directory '/home/siddha/monero/build/Linux/release-v0.16/release/translations'
make[6]: Entering directory '/home/siddha/monero/build/Linux/release-v0.16/release/translations'
[ 50%] Building C object CMakeFiles/generate_translations_header.dir/generate_translations_header.c.o
[100%] Linking C executable generate_translations_header
Generating embedded translations header
make[6]: Leaving directory '/home/siddha/monero/build/Linux/release-v0.16/release/translations'
[100%] Built target generate_translations_header
make[5]: Leaving directory '/home/siddha/monero/build/Linux/release-v0.16/release/translations'
make[4]: Leaving directory '/home/siddha/monero/build/Linux/release-v0.16/release/translations'
[  2%] Performing install step for 'generate_translations_header'

[  2%] Completed 'generate_translations_header'
make[3]: Leaving directory '/home/siddha/monero/build/Linux/release-v0.16/release'
[  2%] Built target generate_translations_header
make[3]: Entering directory '/home/siddha/monero/build/Linux/release-v0.16/release'
Scanning dependencies of target libminiupnpc-static
make[3]: Leaving directory '/home/siddha/monero/build/Linux/release-v0.16/release'
make[3]: Entering directory '/home/siddha/monero/build/Linux/release-v0.16/release'
[  3%] Building C object external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-static.dir/igd_desc_parse.c.o
[  3%] Building C object external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-static.dir/miniupnpc.c.o
[  3%] Building C object external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-static.dir/minixml.c.o
[  3%] Building C object external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-static.dir/minisoap.c.o
[  4%] Building C object external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-static.dir/minissdpc.c.o
[  4%] Building C object external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-static.dir/miniwget.c.o
[  4%] Building C object external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-static.dir/upnpcommands.c.o
[  4%] Building C object external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-static.dir/upnpdev.c.o
[  4%] Building C object external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-static.dir/upnpreplyparse.c.o
[  5%] Building C object external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-static.dir/upnperrors.c.o
[  5%] Building C object external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-static.dir/connecthostport.c.o
[  5%] Building C object external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-static.dir/portlistingparse.c.o
[  5%] Building C object external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-static.dir/receivedata.c.o
[  6%] Linking C static library libminiupnpc.a
make[3]: Leaving directory '/home/siddha/monero/build/Linux/release-v0.16/release'
[  6%] Built target libminiupnpc-static
make[3]: Entering directory '/home/siddha/monero/build/Linux/release-v0.16/release'
Scanning dependencies of target lmdb
make[3]: Leaving directory '/home/siddha/monero/build/Linux/release-v0.16/release'
make[3]: Entering directory '/home/siddha/monero/build/Linux/release-v0.16/release'
[  6%] Building C object external/db_drivers/liblmdb/CMakeFiles/lmdb.dir/mdb.c.o
[  6%] Building C object external/db_drivers/liblmdb/CMakeFiles/lmdb.dir/midl.c.o
[  6%] Linking C static library liblmdb.a
make[3]: Leaving directory '/home/siddha/monero/build/Linux/release-v0.16/release'
[  6%] Built target lmdb
make[3]: Entering directory '/home/siddha/monero/build/Linux/release-v0.16/release'
Scanning dependencies of target easylogging
make[3]: Leaving directory '/home/siddha/monero/build/Linux/release-v0.16/release'
make[3]: Entering directory '/home/siddha/monero/build/Linux/release-v0.16/release'
[  6%] Building CXX object external/easylogging++/CMakeFiles/easylogging.dir/easylogging++.cc.o
[  6%] Linking CXX static library libeasylogging.a
make[3]: Leaving directory '/home/siddha/monero/build/Linux/release-v0.16/release'
[  6%] Built target easylogging
make[3]: Entering directory '/home/siddha/monero/build/Linux/release-v0.16/release'
Scanning dependencies of target epee
make[3]: Leaving directory '/home/siddha/monero/build/Linux/release-v0.16/release'
make[3]: Entering directory '/home/siddha/monero/build/Linux/release-v0.16/release'
[  7%] Building CXX object contrib/epee/src/CMakeFiles/epee.dir/byte_slice.cpp.o
[  7%] Building CXX object contrib/epee/src/CMakeFiles/epee.dir/byte_stream.cpp.o
[  7%] Building CXX object contrib/epee/src/CMakeFiles/epee.dir/hex.cpp.o
[  7%] Building CXX object contrib/epee/src/CMakeFiles/epee.dir/abstract_http_client.cpp.o
[  7%] Building CXX object contrib/epee/src/CMakeFiles/epee.dir/http_auth.cpp.o
[  8%] Building CXX object contrib/epee/src/CMakeFiles/epee.dir/mlog.cpp.o
[  8%] Building CXX object contrib/epee/src/CMakeFiles/epee.dir/net_helper.cpp.o
[  8%] Building CXX object contrib/epee/src/CMakeFiles/epee.dir/net_utils_base.cpp.o
[  8%] Building CXX object contrib/epee/src/CMakeFiles/epee.dir/string_tools.cpp.o
[  9%] Building CXX object contrib/epee/src/CMakeFiles/epee.dir/wipeable_string.cpp.o
[  9%] Building CXX object contrib/epee/src/CMakeFiles/epee.dir/levin_base.cpp.o
[  9%] Building C object contrib/epee/src/CMakeFiles/epee.dir/memwipe.c.o
[  9%] Building CXX object contrib/epee/src/CMakeFiles/epee.dir/connection_basic.cpp.o
[ 10%] Building CXX object contrib/epee/src/CMakeFiles/epee.dir/network_throttle.cpp.o
[ 10%] Building CXX object contrib/epee/src/CMakeFiles/epee.dir/network_throttle-detail.cpp.o
[ 10%] Building CXX object contrib/epee/src/CMakeFiles/epee.dir/mlocker.cpp.o
[ 10%] Building CXX object contrib/epee/src/CMakeFiles/epee.dir/buffer.cpp.o
[ 10%] Building CXX object contrib/epee/src/CMakeFiles/epee.dir/net_ssl.cpp.o
[ 11%] Building CXX object contrib/epee/src/CMakeFiles/epee.dir/int-util.cpp.o
[ 11%] Linking CXX static library libepee.a
make[3]: Leaving directory '/home/siddha/monero/build/Linux/release-v0.16/release'
[ 11%] Built target epee
make[3]: Entering directory '/home/siddha/monero/build/Linux/release-v0.16/release'
Scanning dependencies of target epee_readline
make[3]: Leaving directory '/home/siddha/monero/build/Linux/release-v0.16/release'
make[3]: Entering directory '/home/siddha/monero/build/Linux/release-v0.16/release'
[ 11%] Building CXX object contrib/epee/src/CMakeFiles/epee_readline.dir/readline_buffer.cpp.o
[ 11%] Linking CXX static library libepee_readline.a
make[3]: Leaving directory '/home/siddha/monero/build/Linux/release-v0.16/release'
[ 11%] Built target epee_readline
make[3]: Entering directory '/home/siddha/monero/build/Linux/release-v0.16/release'
Scanning dependencies of target genversion
make[3]: Leaving directory '/home/siddha/monero/build/Linux/release-v0.16/release'
[ 11%] Built target genversion
make[3]: Entering directory '/home/siddha/monero/build/Linux/release-v0.16/release'
Scanning dependencies of target obj_version
make[3]: Leaving directory '/home/siddha/monero/build/Linux/release-v0.16/release'
make[3]: Entering directory '/home/siddha/monero/build/Linux/release-v0.16/release'
[ 11%] Building CXX object src/CMakeFiles/obj_version.dir/__/version.cpp.o
make[3]: Leaving directory '/home/siddha/monero/build/Linux/release-v0.16/release'
[ 11%] Built target obj_version
make[3]: Entering directory '/home/siddha/monero/build/Linux/release-v0.16/release'
Scanning dependencies of target version
make[3]: Leaving directory '/home/siddha/monero/build/Linux/release-v0.16/release'
make[3]: Entering directory '/home/siddha/monero/build/Linux/release-v0.16/release'
[ 12%] Linking CXX static library libversion.a
make[3]: Leaving directory '/home/siddha/monero/build/Linux/release-v0.16/release'
[ 12%] Built target version
make[3]: Entering directory '/home/siddha/monero/build/Linux/release-v0.16/release'
Scanning dependencies of target obj_cncrypto
make[3]: Leaving directory '/home/siddha/monero/build/Linux/release-v0.16/release'
make[3]: Entering directory '/home/siddha/monero/build/Linux/release-v0.16/release'
[ 12%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/aesb.c.o
[ 12%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/blake256.c.o
[ 12%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/chacha.c.o
[ 12%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/crypto-ops-data.c.o
[ 13%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/crypto-ops.c.o
[ 13%] Building CXX object src/crypto/CMakeFiles/obj_cncrypto.dir/crypto.cpp.o
[ 13%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/groestl.c.o
[ 13%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/hash-extra-blake.c.o
[ 14%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/hash-extra-groestl.c.o
[ 14%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/hash-extra-jh.c.o
[ 14%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/hash-extra-skein.c.o
[ 14%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/hash.c.o
[ 15%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/hmac-keccak.c.o
[ 15%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/jh.c.o
[ 15%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/keccak.c.o
[ 15%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/oaes_lib.c.o
[ 15%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/random.c.o
[ 16%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/skein.c.o
[ 16%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/slow-hash.c.o
[ 16%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/rx-slow-hash.c.o
[ 16%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/CryptonightR_JIT.c.o
[ 17%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/tree-hash.c.o
[ 17%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/CryptonightR_template.S.o
make[3]: Leaving directory '/home/siddha/monero/build/Linux/release-v0.16/release'
[ 17%] Built target obj_cncrypto
make[3]: Entering directory '/home/siddha/monero/build/Linux/release-v0.16/release'
Scanning dependencies of target randomx
make[3]: Leaving directory '/home/siddha/monero/build/Linux/release-v0.16/release'
make[3]: Entering directory '/home/siddha/monero/build/Linux/release-v0.16/release'
[ 18%] Building CXX object external/randomx/CMakeFiles/randomx.dir/src/aes_hash.cpp.o
[ 18%] Building C object external/randomx/CMakeFiles/randomx.dir/src/argon2_ref.c.o
[ 18%] Building C object external/randomx/CMakeFiles/randomx.dir/src/argon2_ssse3.c.o
[ 18%] Building C object external/randomx/CMakeFiles/randomx.dir/src/argon2_avx2.c.o
[ 19%] Building CXX object external/randomx/CMakeFiles/randomx.dir/src/bytecode_machine.cpp.o
[ 19%] Building CXX object external/randomx/CMakeFiles/randomx.dir/src/cpu.cpp.o
[ 19%] Building CXX object external/randomx/CMakeFiles/randomx.dir/src/dataset.cpp.o
[ 19%] Building CXX object external/randomx/CMakeFiles/randomx.dir/src/soft_aes.cpp.o
[ 19%] Building CXX object external/randomx/CMakeFiles/randomx.dir/src/virtual_memory.cpp.o
[ 20%] Building CXX object external/randomx/CMakeFiles/randomx.dir/src/vm_interpreted.cpp.o
[ 20%] Building CXX object external/randomx/CMakeFiles/randomx.dir/src/allocator.cpp.o
[ 20%] Building CXX object external/randomx/CMakeFiles/randomx.dir/src/assembly_generator_x86.cpp.o
[ 20%] Building CXX object external/randomx/CMakeFiles/randomx.dir/src/instruction.cpp.o
[ 21%] Building CXX object external/randomx/CMakeFiles/randomx.dir/src/randomx.cpp.o
[ 21%] Building CXX object external/randomx/CMakeFiles/randomx.dir/src/superscalar.cpp.o
[ 21%] Building CXX object external/randomx/CMakeFiles/randomx.dir/src/vm_compiled.cpp.o
[ 21%] Building CXX object external/randomx/CMakeFiles/randomx.dir/src/vm_interpreted_light.cpp.o
[ 22%] Building C object external/randomx/CMakeFiles/randomx.dir/src/argon2_core.c.o
[ 22%] Building CXX object external/randomx/CMakeFiles/randomx.dir/src/blake2_generator.cpp.o
[ 22%] Building CXX object external/randomx/CMakeFiles/randomx.dir/src/instructions_portable.cpp.o
[ 22%] Building C object external/randomx/CMakeFiles/randomx.dir/src/reciprocal.c.o
/home/siddha/monero/external/randomx/src/reciprocal.c: In function ‘randomx_reciprocal’:
/home/siddha/monero/external/randomx/src/reciprocal.c:57:2: error: ‘for’ loop initial declarations are only allowed in C99 mode
  for (uint64_t bit = divisor; bit > 0; bit >>= 1)
  ^
/home/siddha/monero/external/randomx/src/reciprocal.c:57:2: note: use option -std=c99 or -std=gnu99 to compile your code
/home/siddha/monero/external/randomx/src/reciprocal.c:60:2: error: ‘for’ loop initial declarations are only allowed in C99 mode
  for (unsigned shift = 0; shift < bsr; shift++) {
  ^
external/randomx/CMakeFiles/randomx.dir/build.make:542: recipe for target 'external/randomx/CMakeFiles/randomx.dir/src/reciprocal.c.o' failed
make[3]: *** [external/randomx/CMakeFiles/randomx.dir/src/reciprocal.c.o] Error 1
make[3]: Leaving directory '/home/siddha/monero/build/Linux/release-v0.16/release'
CMakeFiles/Makefile2:402: recipe for target 'external/randomx/CMakeFiles/randomx.dir/all' failed
make[2]: *** [external/randomx/CMakeFiles/randomx.dir/all] Error 2
make[2]: Leaving directory '/home/siddha/monero/build/Linux/release-v0.16/release'
Makefile:140: recipe for target 'all' failed
make[1]: *** [all] Error 2
make[1]: Leaving directory '/home/siddha/monero/build/Linux/release-v0.16/release'
Makefile:102: recipe for target 'release-all' failed
make: *** [release-all] Error 2


## selsta | 2020-08-17T14:32:38+00:00
I can compile fine using a fresh 18.04 LTS VM. The issue seems to be that your C compiler is outdated. Mine is:

```
-- The C compiler identification is GNU 7.5.0
-- The CXX compiler identification is GNU 7.5.0
```

your CMake log says:

```
-- The C compiler identification is GNU 4.8.5
-- The CXX compiler identification is GNU 7.5.0
```

Try to update gcc using your package manager.

## lh1008 | 2020-08-17T18:13:18+00:00
Hey @selsta,

Yes, I needed to update the gcc compiler. Thank you for your support. Have a great day. I'll be closing the issue.

## lh1008 | 2020-08-17T18:15:25+00:00
It worked, forgot to mention it in my last comment. I updated the gcc to version 9.3.0 and followed the instructions for building and it worked perfectly. 

# Action History
- Created by: lh1008 | 2020-08-16T20:48:37+00:00
- Closed at: 2020-08-17T18:13:18+00:00
