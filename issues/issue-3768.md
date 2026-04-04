---
title: Problem with step "[ 51%] Linking CXX executable ../../bin/monero-wallet-rpc"
source_url: https://github.com/monero-project/monero/issues/3768
author: fokinkostya
assignees: []
labels:
- invalid
created_at: '2018-05-07T04:04:02+00:00'
updated_at: '2018-06-20T08:57:01+00:00'
type: issue
status: closed
closed_at: '2018-06-20T08:57:01+00:00'
---

# Original Description
Originally in attempt to compile the project an error message "/usr/bin/ld: warning: libssl.so.1.0.0, needed by /usr/lib/gcc/x86_64-linux-gnu/5/../../../x86_64-linux-gnu/libunbound.so, may conflict with libssl.so.1.1" was given.
I have compiled openssl-1.0.0. Began to give an error message "can not be used when making a shared object; recompile with -fPIC". I have rebuilt openssl with parameter - fPIC, now just gives an unclear error message.

` make
mkdir -p build/release
cd build/release && cmake -D BUILD_TESTS=ON -D CMAKE_BUILD_TYPE=release ../.. && make
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
-- Found OpenSSL: /usr/local/lib/libssl.a;/usr/local/lib/libcrypto.a (found version "1.0.0s")
-- Using OpenSSL include dir at /usr/local/include
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
-- Found MiniUPnPc: /usr/include/miniupnpc
-- Found miniupnpc API version 10
-- Using in-tree miniupnpc
-- Looking for libunbound
-- Found libunbound include (unbound.h) in /usr/include
-- Found libunbound shared library
-- Using 64-bit LMDB from source tree
-- Building on x86_64 for native
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
  Imported targets not available for Boost version 106700
Call Stack (most recent call first):
  /usr/share/cmake-3.5/Modules/FindBoost.cmake:763 (_Boost_COMPONENT_DEPENDENCIES)
  /usr/share/cmake-3.5/Modules/FindBoost.cmake:1332 (_Boost_MISSING_DEPENDENCIES)
  CMakeLists.txt:778 (find_package)


CMake Warning at /usr/share/cmake-3.5/Modules/FindBoost.cmake:725 (message):
  Imported targets not available for Boost version 106700
Call Stack (most recent call first):
  /usr/share/cmake-3.5/Modules/FindBoost.cmake:763 (_Boost_COMPONENT_DEPENDENCIES)
  /usr/share/cmake-3.5/Modules/FindBoost.cmake:1332 (_Boost_MISSING_DEPENDENCIES)
  CMakeLists.txt:778 (find_package)


CMake Warning at /usr/share/cmake-3.5/Modules/FindBoost.cmake:725 (message):
  Imported targets not available for Boost version 106700
Call Stack (most recent call first):
  /usr/share/cmake-3.5/Modules/FindBoost.cmake:763 (_Boost_COMPONENT_DEPENDENCIES)
  /usr/share/cmake-3.5/Modules/FindBoost.cmake:1332 (_Boost_MISSING_DEPENDENCIES)
  CMakeLists.txt:778 (find_package)


CMake Warning at /usr/share/cmake-3.5/Modules/FindBoost.cmake:725 (message):
  Imported targets not available for Boost version 106700
Call Stack (most recent call first):
  /usr/share/cmake-3.5/Modules/FindBoost.cmake:763 (_Boost_COMPONENT_DEPENDENCIES)
  /usr/share/cmake-3.5/Modules/FindBoost.cmake:1332 (_Boost_MISSING_DEPENDENCIES)
  CMakeLists.txt:778 (find_package)


CMake Warning at /usr/share/cmake-3.5/Modules/FindBoost.cmake:725 (message):
  Imported targets not available for Boost version 106700
Call Stack (most recent call first):
  /usr/share/cmake-3.5/Modules/FindBoost.cmake:763 (_Boost_COMPONENT_DEPENDENCIES)
  /usr/share/cmake-3.5/Modules/FindBoost.cmake:1332 (_Boost_MISSING_DEPENDENCIES)
  CMakeLists.txt:778 (find_package)


CMake Warning at /usr/share/cmake-3.5/Modules/FindBoost.cmake:725 (message):
  Imported targets not available for Boost version 106700
Call Stack (most recent call first):
  /usr/share/cmake-3.5/Modules/FindBoost.cmake:763 (_Boost_COMPONENT_DEPENDENCIES)
  /usr/share/cmake-3.5/Modules/FindBoost.cmake:1332 (_Boost_MISSING_DEPENDENCIES)
  CMakeLists.txt:778 (find_package)


CMake Warning at /usr/share/cmake-3.5/Modules/FindBoost.cmake:725 (message):
  Imported targets not available for Boost version 106700
Call Stack (most recent call first):
  /usr/share/cmake-3.5/Modules/FindBoost.cmake:763 (_Boost_COMPONENT_DEPENDENCIES)
  /usr/share/cmake-3.5/Modules/FindBoost.cmake:1332 (_Boost_MISSING_DEPENDENCIES)
  CMakeLists.txt:778 (find_package)


CMake Warning at /usr/share/cmake-3.5/Modules/FindBoost.cmake:725 (message):
  Imported targets not available for Boost version 106700
Call Stack (most recent call first):
  /usr/share/cmake-3.5/Modules/FindBoost.cmake:763 (_Boost_COMPONENT_DEPENDENCIES)
  /usr/share/cmake-3.5/Modules/FindBoost.cmake:1332 (_Boost_MISSING_DEPENDENCIES)
  CMakeLists.txt:778 (find_package)


CMake Warning at /usr/share/cmake-3.5/Modules/FindBoost.cmake:725 (message):
  Imported targets not available for Boost version 106700
Call Stack (most recent call first):
  /usr/share/cmake-3.5/Modules/FindBoost.cmake:763 (_Boost_COMPONENT_DEPENDENCIES)
  /usr/share/cmake-3.5/Modules/FindBoost.cmake:1332 (_Boost_MISSING_DEPENDENCIES)
  CMakeLists.txt:778 (find_package)


-- Found Boost Version: 106700
-- Found Readline: /usr/include
-- Looking for rl_copy_text
-- Looking for rl_copy_text - found
-- Looking for rl_filename_completion_function
-- Looking for rl_filename_completion_function - found
-- Found readline library at: /usr
-- Found Git: /usr/bin/git
-- Found GTest: /usr/lib/libgtest.a
-- Found Doxygen: /usr/bin/doxygen (found version "1.8.11")
-- Performing Test HAVE_C11
-- Performing Test HAVE_C11 - Success
-- Configuring done
-- Generating done
-- Build files have been written to: /root/.monero/monero/build/release
make[1]: Entering directory '/root/.monero/monero/build/release'
make[2]: Entering directory '/root/.monero/monero/build/release'
make[3]: Entering directory '/root/.monero/monero/build/release'
Scanning dependencies of target generate_translations_header
make[3]: Leaving directory '/root/.monero/monero/build/release'
make[3]: Entering directory '/root/.monero/monero/build/release'
[  0%] Creating directories for 'generate_translations_header'
[  0%] No download step for 'generate_translations_header'
[  0%] No patch step for 'generate_translations_header'
[  1%] No update step for 'generate_translations_header'
[  1%] Performing configure step for 'generate_translations_header'
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
lrelease version 5.5.1
-- Configuring done
-- Generating done
-- Build files have been written to: /root/.monero/monero/build/release/translations
[  2%] Performing build step for 'generate_translations_header'
make[4]: Entering directory '/root/.monero/monero/build/release/translations'
make[5]: Entering directory '/root/.monero/monero/build/release/translations'
make[6]: Entering directory '/root/.monero/monero/build/release/translations'
Scanning dependencies of target generate_translations_header
make[6]: Leaving directory '/root/.monero/monero/build/release/translations'
make[6]: Entering directory '/root/.monero/monero/build/release/translations'
[ 50%] Building C object CMakeFiles/generate_translations_header.dir/generate_translations_header.c.o
[100%] Linking C executable generate_translations_header
Updating 'monero.qm'...
    Generated 0 translation(s) (0 finished and 0 unfinished)
    Ignored 737 untranslated source text(s)
Updating 'monero_sv.qm'...
    Generated 737 translation(s) (737 finished and 0 unfinished)
Updating 'monero_fr.qm'...
    Generated 737 translation(s) (737 finished and 0 unfinished)
Updating 'monero_it.qm'...
    Generated 380 translation(s) (376 finished and 4 unfinished)
    Ignored 357 untranslated source text(s)
Generating embedded translations header
make[6]: Leaving directory '/root/.monero/monero/build/release/translations'
[100%] Built target generate_translations_header
make[5]: Leaving directory '/root/.monero/monero/build/release/translations'
make[4]: Leaving directory '/root/.monero/monero/build/release/translations'
[  3%] Performing install step for 'generate_translations_header'

[  3%] Completed 'generate_translations_header'
make[3]: Leaving directory '/root/.monero/monero/build/release'
[  3%] Built target generate_translations_header
make[3]: Entering directory '/root/.monero/monero/build/release'
Scanning dependencies of target libminiupnpc-static
make[3]: Leaving directory '/root/.monero/monero/build/release'
make[3]: Entering directory '/root/.monero/monero/build/release'
[  4%] Building C object external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-static.dir/igd_desc_parse.c.o
[  4%] Building C object external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-static.dir/miniupnpc.c.o
[  4%] Building C object external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-static.dir/minixml.c.o
[  5%] Building C object external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-static.dir/minisoap.c.o
[  5%] Building C object external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-static.dir/minissdpc.c.o
[  5%] Building C object external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-static.dir/miniwget.c.o
[  6%] Building C object external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-static.dir/upnpcommands.c.o
[  6%] Building C object external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-static.dir/upnpdev.c.o
[  6%] Building C object external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-static.dir/upnpreplyparse.c.o
[  7%] Building C object external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-static.dir/upnperrors.c.o
[  7%] Building C object external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-static.dir/connecthostport.c.o
[  7%] Building C object external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-static.dir/portlistingparse.c.o
[  8%] Building C object external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-static.dir/receivedata.c.o
[  8%] Linking C static library libminiupnpc.a
make[3]: Leaving directory '/root/.monero/monero/build/release'
[  8%] Built target libminiupnpc-static
make[3]: Entering directory '/root/.monero/monero/build/release'
Scanning dependencies of target lmdb
make[3]: Leaving directory '/root/.monero/monero/build/release'
make[3]: Entering directory '/root/.monero/monero/build/release'
[  8%] Building C object external/db_drivers/liblmdb/CMakeFiles/lmdb.dir/mdb.c.o
[  9%] Building C object external/db_drivers/liblmdb/CMakeFiles/lmdb.dir/midl.c.o
[  9%] Linking C static library liblmdb.a
make[3]: Leaving directory '/root/.monero/monero/build/release'
[  9%] Built target lmdb
make[3]: Entering directory '/root/.monero/monero/build/release'
Scanning dependencies of target easylogging
make[3]: Leaving directory '/root/.monero/monero/build/release'
make[3]: Entering directory '/root/.monero/monero/build/release'
[  9%] Building CXX object external/easylogging++/CMakeFiles/easylogging.dir/easylogging++.cc.o
[  9%] Linking CXX static library libeasylogging.a
make[3]: Leaving directory '/root/.monero/monero/build/release'
[  9%] Built target easylogging
make[3]: Entering directory '/root/.monero/monero/build/release'
Scanning dependencies of target epee_readline
make[3]: Leaving directory '/root/.monero/monero/build/release'
make[3]: Entering directory '/root/.monero/monero/build/release'
[  9%] Building CXX object contrib/epee/src/CMakeFiles/epee_readline.dir/readline_buffer.cpp.o
[ 10%] Linking CXX static library libepee_readline.a
make[3]: Leaving directory '/root/.monero/monero/build/release'
[ 10%] Built target epee_readline
make[3]: Entering directory '/root/.monero/monero/build/release'
Scanning dependencies of target epee
make[3]: Leaving directory '/root/.monero/monero/build/release'
make[3]: Entering directory '/root/.monero/monero/build/release'
[ 11%] Building CXX object contrib/epee/src/CMakeFiles/epee.dir/hex.cpp.o
[ 11%] Building CXX object contrib/epee/src/CMakeFiles/epee.dir/http_auth.cpp.o
[ 11%] Building CXX object contrib/epee/src/CMakeFiles/epee.dir/mlog.cpp.o
[ 12%] Building CXX object contrib/epee/src/CMakeFiles/epee.dir/net_utils_base.cpp.o
[ 12%] Building CXX object contrib/epee/src/CMakeFiles/epee.dir/string_tools.cpp.o
[ 12%] Building CXX object contrib/epee/src/CMakeFiles/epee.dir/wipeable_string.cpp.o
[ 13%] Building C object contrib/epee/src/CMakeFiles/epee.dir/memwipe.c.o
[ 13%] Building CXX object contrib/epee/src/CMakeFiles/epee.dir/connection_basic.cpp.o
[ 13%] Building CXX object contrib/epee/src/CMakeFiles/epee.dir/network_throttle.cpp.o
[ 14%] Building CXX object contrib/epee/src/CMakeFiles/epee.dir/network_throttle-detail.cpp.o
[ 14%] Linking CXX static library libepee.a
make[3]: Leaving directory '/root/.monero/monero/build/release'
[ 14%] Built target epee
make[3]: Entering directory '/root/.monero/monero/build/release'
Scanning dependencies of target genversion
make[3]: Leaving directory '/root/.monero/monero/build/release'
make[3]: Entering directory '/root/.monero/monero/build/release'
[ 14%] Generating ../version.cpp
-- You are currently on commit 7ed94d3
-- The most recent tag was at c29890c
-- You are ahead of or behind a tagged release
make[3]: Leaving directory '/root/.monero/monero/build/release'
[ 14%] Built target genversion
make[3]: Entering directory '/root/.monero/monero/build/release'
Scanning dependencies of target obj_version
make[3]: Leaving directory '/root/.monero/monero/build/release'
make[3]: Entering directory '/root/.monero/monero/build/release'
[ 14%] Building CXX object src/CMakeFiles/obj_version.dir/__/version.cpp.o
make[3]: Leaving directory '/root/.monero/monero/build/release'
[ 15%] Built target obj_version
make[3]: Entering directory '/root/.monero/monero/build/release'
Scanning dependencies of target version
make[3]: Leaving directory '/root/.monero/monero/build/release'
make[3]: Entering directory '/root/.monero/monero/build/release'
[ 15%] Linking CXX static library libversion.a
make[3]: Leaving directory '/root/.monero/monero/build/release'
[ 15%] Built target version
make[3]: Entering directory '/root/.monero/monero/build/release'
Scanning dependencies of target obj_common
make[3]: Leaving directory '/root/.monero/monero/build/release'
make[3]: Entering directory '/root/.monero/monero/build/release'
[ 15%] Building CXX object src/common/CMakeFiles/obj_common.dir/base58.cpp.o
[ 15%] Building CXX object src/common/CMakeFiles/obj_common.dir/command_line.cpp.o
[ 17%] Building CXX object src/common/CMakeFiles/obj_common.dir/dns_utils.cpp.o
[ 17%] Building CXX object src/common/CMakeFiles/obj_common.dir/download.cpp.o
[ 17%] Building CXX object src/common/CMakeFiles/obj_common.dir/util.cpp.o
[ 18%] Building CXX object src/common/CMakeFiles/obj_common.dir/i18n.cpp.o
[ 18%] Building CXX object src/common/CMakeFiles/obj_common.dir/password.cpp.o
[ 18%] Building CXX object src/common/CMakeFiles/obj_common.dir/perf_timer.cpp.o
[ 19%] Building CXX object src/common/CMakeFiles/obj_common.dir/threadpool.cpp.o
[ 19%] Building CXX object src/common/CMakeFiles/obj_common.dir/updates.cpp.o
[ 19%] Building CXX object src/common/CMakeFiles/obj_common.dir/stack_trace.cpp.o
make[3]: Leaving directory '/root/.monero/monero/build/release'
[ 19%] Built target obj_common
make[3]: Entering directory '/root/.monero/monero/build/release'
Scanning dependencies of target obj_cncrypto
make[3]: Leaving directory '/root/.monero/monero/build/release'
make[3]: Entering directory '/root/.monero/monero/build/release'
[ 20%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/aesb.c.o
[ 20%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/blake256.c.o
[ 20%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/chacha.c.o
[ 21%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/crypto-ops-data.c.o
[ 21%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/crypto-ops.c.o
[ 21%] Building CXX object src/crypto/CMakeFiles/obj_cncrypto.dir/crypto.cpp.o
[ 22%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/groestl.c.o
[ 22%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/hash-extra-blake.c.o
[ 22%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/hash-extra-groestl.c.o
[ 23%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/hash-extra-jh.c.o
[ 23%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/hash-extra-skein.c.o
[ 23%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/hash.c.o
[ 24%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/jh.c.o
[ 24%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/keccak.c.o
[ 24%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/oaes_lib.c.o
[ 25%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/random.c.o
[ 25%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/skein.c.o
[ 25%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/slow-hash.c.o
[ 26%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/tree-hash.c.o
make[3]: Leaving directory '/root/.monero/monero/build/release'
[ 26%] Built target obj_cncrypto
make[3]: Entering directory '/root/.monero/monero/build/release'
Scanning dependencies of target cncrypto
make[3]: Leaving directory '/root/.monero/monero/build/release'
make[3]: Entering directory '/root/.monero/monero/build/release'
[ 27%] Linking CXX static library libcncrypto.a
make[3]: Leaving directory '/root/.monero/monero/build/release'
[ 27%] Built target cncrypto
make[3]: Entering directory '/root/.monero/monero/build/release'
Scanning dependencies of target common
make[3]: Leaving directory '/root/.monero/monero/build/release'
make[3]: Entering directory '/root/.monero/monero/build/release'
[ 27%] Linking CXX static library libcommon.a
make[3]: Leaving directory '/root/.monero/monero/build/release'
[ 27%] Built target common
make[3]: Entering directory '/root/.monero/monero/build/release'
Scanning dependencies of target obj_device
make[3]: Leaving directory '/root/.monero/monero/build/release'
make[3]: Entering directory '/root/.monero/monero/build/release'
[ 28%] Building CXX object src/device/CMakeFiles/obj_device.dir/device.cpp.o
[ 28%] Building CXX object src/device/CMakeFiles/obj_device.dir/device_default.cpp.o
[ 28%] Building CXX object src/device/CMakeFiles/obj_device.dir/log.cpp.o
make[3]: Leaving directory '/root/.monero/monero/build/release'
[ 28%] Built target obj_device
make[3]: Entering directory '/root/.monero/monero/build/release'
Scanning dependencies of target obj_ringct_basic
make[3]: Leaving directory '/root/.monero/monero/build/release'
make[3]: Entering directory '/root/.monero/monero/build/release'
[ 28%] Building CXX object src/ringct/CMakeFiles/obj_ringct_basic.dir/rctOps.cpp.o
[ 28%] Building CXX object src/ringct/CMakeFiles/obj_ringct_basic.dir/rctTypes.cpp.o
[ 29%] Building C object src/ringct/CMakeFiles/obj_ringct_basic.dir/rctCryptoOps.c.o
[ 29%] Building CXX object src/ringct/CMakeFiles/obj_ringct_basic.dir/bulletproofs.cc.o
make[3]: Leaving directory '/root/.monero/monero/build/release'
[ 29%] Built target obj_ringct_basic
make[3]: Entering directory '/root/.monero/monero/build/release'
Scanning dependencies of target ringct_basic
make[3]: Leaving directory '/root/.monero/monero/build/release'
make[3]: Entering directory '/root/.monero/monero/build/release'
[ 29%] Linking CXX static library libringct_basic.a
make[3]: Leaving directory '/root/.monero/monero/build/release'
[ 29%] Built target ringct_basic
make[3]: Entering directory '/root/.monero/monero/build/release'
[ 29%] Generating stagenet_blocks.o
[ 30%] Generating blocks.o
[ 30%] Generating testnet_blocks.o
Scanning dependencies of target blocks
make[3]: Leaving directory '/root/.monero/monero/build/release'
make[3]: Entering directory '/root/.monero/monero/build/release'
[ 31%] Building C object src/blocks/CMakeFiles/blocks.dir/blockexports.c.o
[ 31%] Linking C static library libblocks.a
make[3]: Leaving directory '/root/.monero/monero/build/release'
[ 31%] Built target blocks
make[3]: Entering directory '/root/.monero/monero/build/release'
Scanning dependencies of target device
make[3]: Leaving directory '/root/.monero/monero/build/release'
make[3]: Entering directory '/root/.monero/monero/build/release'
[ 32%] Linking CXX static library libdevice.a
make[3]: Leaving directory '/root/.monero/monero/build/release'
[ 32%] Built target device
make[3]: Entering directory '/root/.monero/monero/build/release'
Scanning dependencies of target obj_ringct
make[3]: Leaving directory '/root/.monero/monero/build/release'
make[3]: Entering directory '/root/.monero/monero/build/release'
[ 34%] Building CXX object src/ringct/CMakeFiles/obj_ringct.dir/rctSigs.cpp.o
make[3]: Leaving directory '/root/.monero/monero/build/release'
[ 34%] Built target obj_ringct
make[3]: Entering directory '/root/.monero/monero/build/release'
Scanning dependencies of target obj_checkpoints
make[3]: Leaving directory '/root/.monero/monero/build/release'
make[3]: Entering directory '/root/.monero/monero/build/release'
[ 34%] Building CXX object src/checkpoints/CMakeFiles/obj_checkpoints.dir/checkpoints.cpp.o
make[3]: Leaving directory '/root/.monero/monero/build/release'
[ 34%] Built target obj_checkpoints
make[3]: Entering directory '/root/.monero/monero/build/release'
Scanning dependencies of target checkpoints
make[3]: Leaving directory '/root/.monero/monero/build/release'
make[3]: Entering directory '/root/.monero/monero/build/release'
[ 34%] Linking CXX static library libcheckpoints.a
make[3]: Leaving directory '/root/.monero/monero/build/release'
[ 34%] Built target checkpoints
make[3]: Entering directory '/root/.monero/monero/build/release'
Scanning dependencies of target obj_cryptonote_basic
make[3]: Leaving directory '/root/.monero/monero/build/release'
make[3]: Entering directory '/root/.monero/monero/build/release'
[ 35%] Building CXX object src/cryptonote_basic/CMakeFiles/obj_cryptonote_basic.dir/account.cpp.o
[ 35%] Building CXX object src/cryptonote_basic/CMakeFiles/obj_cryptonote_basic.dir/cryptonote_basic_impl.cpp.o
[ 35%] Building CXX object src/cryptonote_basic/CMakeFiles/obj_cryptonote_basic.dir/cryptonote_format_utils.cpp.o
[ 36%] Building CXX object src/cryptonote_basic/CMakeFiles/obj_cryptonote_basic.dir/difficulty.cpp.o
[ 36%] Building CXX object src/cryptonote_basic/CMakeFiles/obj_cryptonote_basic.dir/hardfork.cpp.o
[ 36%] Building CXX object src/cryptonote_basic/CMakeFiles/obj_cryptonote_basic.dir/miner.cpp.o
make[3]: Leaving directory '/root/.monero/monero/build/release'
[ 36%] Built target obj_cryptonote_basic
make[3]: Entering directory '/root/.monero/monero/build/release'
Scanning dependencies of target cryptonote_basic
make[3]: Leaving directory '/root/.monero/monero/build/release'
make[3]: Entering directory '/root/.monero/monero/build/release'
[ 36%] Linking CXX static library libcryptonote_basic.a
make[3]: Leaving directory '/root/.monero/monero/build/release'
[ 36%] Built target cryptonote_basic
make[3]: Entering directory '/root/.monero/monero/build/release'
Scanning dependencies of target ringct
make[3]: Leaving directory '/root/.monero/monero/build/release'
make[3]: Entering directory '/root/.monero/monero/build/release'
[ 36%] Linking CXX static library libringct.a
make[3]: Leaving directory '/root/.monero/monero/build/release'
[ 36%] Built target ringct
make[3]: Entering directory '/root/.monero/monero/build/release'
Scanning dependencies of target obj_cryptonote_core
make[3]: Leaving directory '/root/.monero/monero/build/release'
make[3]: Entering directory '/root/.monero/monero/build/release'
[ 37%] Building CXX object src/cryptonote_core/CMakeFiles/obj_cryptonote_core.dir/blockchain.cpp.o
[ 37%] Building CXX object src/cryptonote_core/CMakeFiles/obj_cryptonote_core.dir/cryptonote_core.cpp.o
[ 37%] Building CXX object src/cryptonote_core/CMakeFiles/obj_cryptonote_core.dir/tx_pool.cpp.o
[ 38%] Building CXX object src/cryptonote_core/CMakeFiles/obj_cryptonote_core.dir/cryptonote_tx_utils.cpp.o
make[3]: Leaving directory '/root/.monero/monero/build/release'
[ 38%] Built target obj_cryptonote_core
make[3]: Entering directory '/root/.monero/monero/build/release'
Scanning dependencies of target obj_multisig
make[3]: Leaving directory '/root/.monero/monero/build/release'
make[3]: Entering directory '/root/.monero/monero/build/release'
[ 38%] Building CXX object src/multisig/CMakeFiles/obj_multisig.dir/multisig.cpp.o
make[3]: Leaving directory '/root/.monero/monero/build/release'
[ 38%] Built target obj_multisig
make[3]: Entering directory '/root/.monero/monero/build/release'
Scanning dependencies of target multisig
make[3]: Leaving directory '/root/.monero/monero/build/release'
make[3]: Entering directory '/root/.monero/monero/build/release'
[ 39%] Linking CXX static library libmultisig.a
make[3]: Leaving directory '/root/.monero/monero/build/release'
[ 39%] Built target multisig
make[3]: Entering directory '/root/.monero/monero/build/release'
Scanning dependencies of target obj_blockchain_db
make[3]: Leaving directory '/root/.monero/monero/build/release'
make[3]: Entering directory '/root/.monero/monero/build/release'
[ 40%] Building CXX object src/blockchain_db/CMakeFiles/obj_blockchain_db.dir/blockchain_db.cpp.o
[ 40%] Building CXX object src/blockchain_db/CMakeFiles/obj_blockchain_db.dir/lmdb/db_lmdb.cpp.o
make[3]: Leaving directory '/root/.monero/monero/build/release'
[ 40%] Built target obj_blockchain_db
make[3]: Entering directory '/root/.monero/monero/build/release'
Scanning dependencies of target blockchain_db
make[3]: Leaving directory '/root/.monero/monero/build/release'
make[3]: Entering directory '/root/.monero/monero/build/release'
[ 41%] Linking CXX static library libblockchain_db.a
make[3]: Leaving directory '/root/.monero/monero/build/release'
[ 41%] Built target blockchain_db
make[3]: Entering directory '/root/.monero/monero/build/release'
Scanning dependencies of target cryptonote_core
make[3]: Leaving directory '/root/.monero/monero/build/release'
make[3]: Entering directory '/root/.monero/monero/build/release'
[ 41%] Linking CXX static library libcryptonote_core.a
make[3]: Leaving directory '/root/.monero/monero/build/release'
[ 41%] Built target cryptonote_core
make[3]: Entering directory '/root/.monero/monero/build/release'
Scanning dependencies of target obj_mnemonics
make[3]: Leaving directory '/root/.monero/monero/build/release'
make[3]: Entering directory '/root/.monero/monero/build/release'
[ 42%] Building CXX object src/mnemonics/CMakeFiles/obj_mnemonics.dir/electrum-words.cpp.o
make[3]: Leaving directory '/root/.monero/monero/build/release'
[ 42%] Built target obj_mnemonics
make[3]: Entering directory '/root/.monero/monero/build/release'
Scanning dependencies of target mnemonics
make[3]: Leaving directory '/root/.monero/monero/build/release'
make[3]: Entering directory '/root/.monero/monero/build/release'
[ 42%] Linking CXX static library libmnemonics.a
make[3]: Leaving directory '/root/.monero/monero/build/release'
[ 42%] Built target mnemonics
make[3]: Entering directory '/root/.monero/monero/build/release'
Scanning dependencies of target obj_rpc
make[3]: Leaving directory '/root/.monero/monero/build/release'
make[3]: Entering directory '/root/.monero/monero/build/release'
[ 42%] Building CXX object src/rpc/CMakeFiles/obj_rpc.dir/core_rpc_server.cpp.o
[ 43%] Building CXX object src/rpc/CMakeFiles/obj_rpc.dir/instanciations.cpp.o
make[3]: Leaving directory '/root/.monero/monero/build/release'
[ 43%] Built target obj_rpc
make[3]: Entering directory '/root/.monero/monero/build/release'
Scanning dependencies of target obj_rpc_base
make[3]: Leaving directory '/root/.monero/monero/build/release'
make[3]: Entering directory '/root/.monero/monero/build/release'
[ 43%] Building CXX object src/rpc/CMakeFiles/obj_rpc_base.dir/rpc_args.cpp.o
make[3]: Leaving directory '/root/.monero/monero/build/release'
[ 43%] Built target obj_rpc_base
make[3]: Entering directory '/root/.monero/monero/build/release'
Scanning dependencies of target rpc_base
make[3]: Leaving directory '/root/.monero/monero/build/release'
make[3]: Entering directory '/root/.monero/monero/build/release'
[ 43%] Linking CXX static library librpc_base.a
make[3]: Leaving directory '/root/.monero/monero/build/release'
[ 43%] Built target rpc_base
make[3]: Entering directory '/root/.monero/monero/build/release'
Scanning dependencies of target obj_p2p
make[3]: Leaving directory '/root/.monero/monero/build/release'
make[3]: Entering directory '/root/.monero/monero/build/release'
[ 43%] Building CXX object src/p2p/CMakeFiles/obj_p2p.dir/net_node.cpp.o
make[3]: Leaving directory '/root/.monero/monero/build/release'
[ 43%] Built target obj_p2p
make[3]: Entering directory '/root/.monero/monero/build/release'
Scanning dependencies of target p2p
make[3]: Leaving directory '/root/.monero/monero/build/release'
make[3]: Entering directory '/root/.monero/monero/build/release'
[ 43%] Linking CXX static library libp2p.a
make[3]: Leaving directory '/root/.monero/monero/build/release'
[ 43%] Built target p2p
make[3]: Entering directory '/root/.monero/monero/build/release'
Scanning dependencies of target obj_cryptonote_protocol
make[3]: Leaving directory '/root/.monero/monero/build/release'
make[3]: Entering directory '/root/.monero/monero/build/release'
[ 43%] Building CXX object src/cryptonote_protocol/CMakeFiles/obj_cryptonote_protocol.dir/block_queue.cpp.o
[ 43%] Building CXX object src/cryptonote_protocol/CMakeFiles/obj_cryptonote_protocol.dir/cryptonote_protocol_handler-base.cpp.o
make[3]: Leaving directory '/root/.monero/monero/build/release'
[ 43%] Built target obj_cryptonote_protocol
make[3]: Entering directory '/root/.monero/monero/build/release'
Scanning dependencies of target cryptonote_protocol
make[3]: Leaving directory '/root/.monero/monero/build/release'
make[3]: Entering directory '/root/.monero/monero/build/release'
[ 44%] Linking CXX static library libcryptonote_protocol.a
make[3]: Leaving directory '/root/.monero/monero/build/release'
[ 44%] Built target cryptonote_protocol
make[3]: Entering directory '/root/.monero/monero/build/release'
Scanning dependencies of target rpc
make[3]: Leaving directory '/root/.monero/monero/build/release'
make[3]: Entering directory '/root/.monero/monero/build/release'
[ 45%] Linking CXX static library librpc.a
make[3]: Leaving directory '/root/.monero/monero/build/release'
[ 45%] Built target rpc
make[3]: Entering directory '/root/.monero/monero/build/release'
Scanning dependencies of target obj_daemon_messages
make[3]: Leaving directory '/root/.monero/monero/build/release'
make[3]: Entering directory '/root/.monero/monero/build/release'
[ 46%] Building CXX object src/rpc/CMakeFiles/obj_daemon_messages.dir/message.cpp.o
[ 46%] Building CXX object src/rpc/CMakeFiles/obj_daemon_messages.dir/daemon_messages.cpp.o
make[3]: Leaving directory '/root/.monero/monero/build/release'
[ 46%] Built target obj_daemon_messages
make[3]: Entering directory '/root/.monero/monero/build/release'
Scanning dependencies of target obj_daemon_rpc_server
make[3]: Leaving directory '/root/.monero/monero/build/release'
make[3]: Entering directory '/root/.monero/monero/build/release'
[ 46%] Building CXX object src/rpc/CMakeFiles/obj_daemon_rpc_server.dir/daemon_handler.cpp.o
[ 47%] Building CXX object src/rpc/CMakeFiles/obj_daemon_rpc_server.dir/zmq_server.cpp.o
make[3]: Leaving directory '/root/.monero/monero/build/release'
[ 47%] Built target obj_daemon_rpc_server
make[3]: Entering directory '/root/.monero/monero/build/release'
Scanning dependencies of target obj_serialization
make[3]: Leaving directory '/root/.monero/monero/build/release'
make[3]: Entering directory '/root/.monero/monero/build/release'
[ 47%] Building CXX object src/serialization/CMakeFiles/obj_serialization.dir/json_object.cpp.o
make[3]: Leaving directory '/root/.monero/monero/build/release'
[ 47%] Built target obj_serialization
make[3]: Entering directory '/root/.monero/monero/build/release'
Scanning dependencies of target serialization
make[3]: Leaving directory '/root/.monero/monero/build/release'
make[3]: Entering directory '/root/.monero/monero/build/release'
[ 47%] Linking CXX static library libserialization.a
make[3]: Leaving directory '/root/.monero/monero/build/release'
[ 47%] Built target serialization
make[3]: Entering directory '/root/.monero/monero/build/release'
Scanning dependencies of target daemon_messages
make[3]: Leaving directory '/root/.monero/monero/build/release'
make[3]: Entering directory '/root/.monero/monero/build/release'
[ 48%] Linking CXX static library libdaemon_messages.a
make[3]: Leaving directory '/root/.monero/monero/build/release'
[ 48%] Built target daemon_messages
make[3]: Entering directory '/root/.monero/monero/build/release'
Scanning dependencies of target daemon_rpc_server
make[3]: Leaving directory '/root/.monero/monero/build/release'
make[3]: Entering directory '/root/.monero/monero/build/release'
[ 48%] Linking CXX static library libdaemon_rpc_server.a
make[3]: Leaving directory '/root/.monero/monero/build/release'
[ 48%] Built target daemon_rpc_server
make[3]: Entering directory '/root/.monero/monero/build/release'
Scanning dependencies of target obj_wallet
make[3]: Leaving directory '/root/.monero/monero/build/release'
make[3]: Entering directory '/root/.monero/monero/build/release'
[ 48%] Building CXX object src/wallet/CMakeFiles/obj_wallet.dir/wallet2.cpp.o
[ 50%] Building CXX object src/wallet/CMakeFiles/obj_wallet.dir/wallet_args.cpp.o
[ 50%] Building CXX object src/wallet/CMakeFiles/obj_wallet.dir/ringdb.cpp.o
[ 50%] Building CXX object src/wallet/CMakeFiles/obj_wallet.dir/node_rpc_proxy.cpp.o
make[3]: Leaving directory '/root/.monero/monero/build/release'
[ 50%] Built target obj_wallet
make[3]: Entering directory '/root/.monero/monero/build/release'
Scanning dependencies of target wallet
make[3]: Leaving directory '/root/.monero/monero/build/release'
make[3]: Entering directory '/root/.monero/monero/build/release'
[ 50%] Linking CXX static library ../../lib/libwallet.a
make[3]: Leaving directory '/root/.monero/monero/build/release'
[ 50%] Built target wallet
make[3]: Entering directory '/root/.monero/monero/build/release'
Scanning dependencies of target wallet_rpc_server
make[3]: Leaving directory '/root/.monero/monero/build/release'
make[3]: Entering directory '/root/.monero/monero/build/release'
[ 50%] Building CXX object src/wallet/CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o
[ 51%] Linking CXX executable ../../bin/monero-wallet-rpc
CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o: In function `boost::re_detail_106700::perl_matcher<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > >, boost::regex_traits<char, boost::cpp_regex_traits<char> > >::unwind_extra_block(bool)':
wallet_rpc_server.cpp:(.text._ZN5boost16re_detail_10670012perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEESaINS_9sub_matchISC_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE18unwind_extra_blockEb[_ZN5boost16re_detail_10670012perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEESaINS_9sub_matchISC_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE18unwind_extra_blockEb]+0x2c): undefined reference to `boost::re_detail_106700::put_mem_block(void*)'
CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o: In function `void boost::serialization::throw_exception<boost::archive::portable_binary_iarchive_exception>(boost::archive::portable_binary_iarchive_exception const&)':
wallet_rpc_server.cpp:(.text._ZN5boost13serialization15throw_exceptionINS_7archive34portable_binary_iarchive_exceptionEEEvRKT_[_ZN5boost13serialization15throw_exceptionINS_7archive34portable_binary_iarchive_exceptionEEEvRKT_]+0x36): undefined reference to `boost::archive::archive_exception::archive_exception(boost::archive::archive_exception const&)'
CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o: In function `void boost::serialization::throw_exception<boost::archive::archive_exception>(boost::archive::archive_exception const&)':
wallet_rpc_server.cpp:(.text._ZN5boost13serialization15throw_exceptionINS_7archive17archive_exceptionEEEvRKT_[_ZN5boost13serialization15throw_exceptionINS_7archive17archive_exceptionEEEvRKT_]+0x1d): undefined reference to `boost::archive::archive_exception::archive_exception(boost::archive::archive_exception const&)'
CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o: In function `epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::timed_wait_server_stop(unsigned long)':
wallet_rpc_server.cpp:(.text._ZN4epee9net_utils18boosted_tcp_serverINS0_4http19http_custom_handlerINS0_23connection_context_baseEEEE22timed_wait_server_stopEm[_ZN4epee9net_utils18boosted_tcp_serverINS0_4http19http_custom_handlerINS0_23connection_context_baseEEEE22timed_wait_server_stopEm]+0x121): undefined reference to `boost::thread::do_try_join_until_noexcept(boost::detail::mono_platform_timepoint const&, bool&)'
CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o: In function `void boost::re_detail_106700::raise_error<boost::regex_traits_wrapper<boost::regex_traits<char, boost::cpp_regex_traits<char> > > >(boost::regex_traits_wrapper<boost::regex_traits<char, boost::cpp_regex_traits<char> > > const&, boost::regex_constants::error_type)':
wallet_rpc_server.cpp:(.text._ZN5boost16re_detail_10670011raise_errorINS_20regex_traits_wrapperINS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEEEEEvRKT_NS_15regex_constants10error_typeE[_ZN5boost16re_detail_10670011raise_errorINS_20regex_traits_wrapperINS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEEEEEvRKT_NS_15regex_constants10error_typeE]+0xb5): undefined reference to `boost::re_detail_106700::raise_runtime_error(std::runtime_error const&)'
wallet_rpc_server.cpp:(.text._ZN5boost16re_detail_10670011raise_errorINS_20regex_traits_wrapperINS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEEEEEvRKT_NS_15regex_constants10error_typeE[_ZN5boost16re_detail_10670011raise_errorINS_20regex_traits_wrapperINS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEEEEEvRKT_NS_15regex_constants10error_typeE]+0xe8): undefined reference to `boost::re_detail_106700::get_default_error_string(boost::regex_constants::error_type)'
CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o: In function `__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > boost::re_detail_106700::re_is_set_member<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, char, boost::regex_traits<char, boost::cpp_regex_traits<char> >, unsigned int>(__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, __gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, boost::re_detail_106700::re_set_long<unsigned int> const*, boost::re_detail_106700::regex_data<char, boost::regex_traits<char, boost::cpp_regex_traits<char> > > const&, bool)':
wallet_rpc_server.cpp:(.text._ZN5boost16re_detail_10670016re_is_set_memberIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEEcNS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEjEET_SH_SH_PKNS0_11re_set_longIT2_EERKNS0_10regex_dataIT0_T1_EEb[_ZN5boost16re_detail_10670016re_is_set_memberIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEEcNS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEjEET_SH_SH_PKNS0_11re_set_longIT2_EERKNS0_10regex_dataIT0_T1_EEb]+0x15e): undefined reference to `boost::re_detail_106700::cpp_regex_traits_implementation<char>::transform_primary(char const*, char const*) const'
wallet_rpc_server.cpp:(.text._ZN5boost16re_detail_10670016re_is_set_memberIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEEcNS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEjEET_SH_SH_PKNS0_11re_set_longIT2_EERKNS0_10regex_dataIT0_T1_EEb[_ZN5boost16re_detail_10670016re_is_set_memberIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEEcNS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEjEET_SH_SH_PKNS0_11re_set_longIT2_EERKNS0_10regex_dataIT0_T1_EEb]+0x34f): undefined reference to `boost::re_detail_106700::cpp_regex_traits_implementation<char>::transform(char const*, char const*) const'
CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o: In function `boost::re_detail_106700::perl_matcher<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > >, boost::regex_traits<char, boost::cpp_regex_traits<char> > >::extend_stack()':
wallet_rpc_server.cpp:(.text._ZN5boost16re_detail_10670012perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEESaINS_9sub_matchISC_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE12extend_stackEv[_ZN5boost16re_detail_10670012perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEESaINS_9sub_matchISC_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE12extend_stackEv]+0x18): undefined reference to `boost::re_detail_106700::get_mem_block()'
CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o: In function `boost::re_detail_106700::perl_matcher<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > >, boost::regex_traits<char, boost::cpp_regex_traits<char> > >::match_imp()':
wallet_rpc_server.cpp:(.text._ZN5boost16re_detail_10670012perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEESaINS_9sub_matchISC_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE9match_impEv[_ZN5boost16re_detail_10670012perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEESaINS_9sub_matchISC_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE9match_impEv]+0xa): undefined reference to `boost::re_detail_106700::get_mem_block()'
wallet_rpc_server.cpp:(.text._ZN5boost16re_detail_10670012perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEESaINS_9sub_matchISC_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE9match_impEv[_ZN5boost16re_detail_10670012perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEESaINS_9sub_matchISC_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE9match_impEv]+0xf9): undefined reference to `boost::re_detail_106700::verify_options(unsigned int, boost::regex_constants::_match_flags)'
wallet_rpc_server.cpp:(.text._ZN5boost16re_detail_10670012perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEESaINS_9sub_matchISC_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE9match_impEv[_ZN5boost16re_detail_10670012perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEESaINS_9sub_matchISC_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE9match_impEv]+0x12b): undefined reference to `boost::re_detail_106700::put_mem_block(void*)'
wallet_rpc_server.cpp:(.text._ZN5boost16re_detail_10670012perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEESaINS_9sub_matchISC_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE9match_impEv[_ZN5boost16re_detail_10670012perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEESaINS_9sub_matchISC_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE9match_impEv]+0x1ee): undefined reference to `boost::re_detail_106700::put_mem_block(void*)'
CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o: In function `epee::serialization::convert_to_integral<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, unsigned long, false>::convert(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, unsigned long&)':
wallet_rpc_server.cpp:(.text._ZN4epee13serialization19convert_to_integralINSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEmLb0EE7convertERKS7_Rm[_ZN4epee13serialization19convert_to_integralINSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEmLb0EE7convertERKS7_Rm]+0x2bb): undefined reference to `boost::re_detail_106700::perl_matcher<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > >, boost::regex_traits<char, boost::cpp_regex_traits<char> > >::construct_init(boost::basic_regex<char, boost::regex_traits<char, boost::cpp_regex_traits<char> > > const&, boost::regex_constants::_match_flags)'
CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o: In function `boost::re_detail_106700::perl_matcher<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > >, boost::regex_traits<char, boost::cpp_regex_traits<char> > >::find_imp()':
wallet_rpc_server.cpp:(.text._ZN5boost16re_detail_10670012perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEESaINS_9sub_matchISC_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE8find_impEv[_ZN5boost16re_detail_10670012perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEESaINS_9sub_matchISC_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE8find_impEv]+0xa): undefined reference to `boost::re_detail_106700::get_mem_block()'
wallet_rpc_server.cpp:(.text._ZN5boost16re_detail_10670012perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEESaINS_9sub_matchISC_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE8find_impEv[_ZN5boost16re_detail_10670012perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEESaINS_9sub_matchISC_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE8find_impEv]+0x138): undefined reference to `boost::re_detail_106700::verify_options(unsigned int, boost::regex_constants::_match_flags)'
wallet_rpc_server.cpp:(.text._ZN5boost16re_detail_10670012perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEESaINS_9sub_matchISC_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE8find_impEv[_ZN5boost16re_detail_10670012perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEESaINS_9sub_matchISC_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE8find_impEv]+0x17f): undefined reference to `boost::re_detail_106700::put_mem_block(void*)'
wallet_rpc_server.cpp:(.text._ZN5boost16re_detail_10670012perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEESaINS_9sub_matchISC_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE8find_impEv[_ZN5boost16re_detail_10670012perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEESaINS_9sub_matchISC_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE8find_impEv]+0x2d3): undefined reference to `boost::re_detail_106700::put_mem_block(void*)'
CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o: In function `bool boost::regex_search<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > >, char, boost::regex_traits<char, boost::cpp_regex_traits<char> > >(__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, __gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, boost::match_results<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > > >&, boost::basic_regex<char, boost::regex_traits<char, boost::cpp_regex_traits<char> > > const&, boost::regex_constants::_match_flags, __gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >)':
wallet_rpc_server.cpp:(.text._ZN5boost12regex_searchIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEESaINS_9sub_matchISB_EEEcNS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEEEbT_SJ_RNS_13match_resultsISJ_T0_EERKNS_11basic_regexIT1_T2_EENS_15regex_constants12_match_flagsESJ_[_ZN5boost12regex_searchIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEESaINS_9sub_matchISB_EEEcNS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEEEbT_SJ_RNS_13match_resultsISJ_T0_EERKNS_11basic_regexIT1_T2_EENS_15regex_constants12_match_flagsESJ_]+0x131): undefined reference to `boost::re_detail_106700::perl_matcher<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > >, boost::regex_traits<char, boost::cpp_regex_traits<char> > >::construct_init(boost::basic_regex<char, boost::regex_traits<char, boost::cpp_regex_traits<char> > > const&, boost::regex_constants::_match_flags)'
CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o: In function `epee::net_utils::http::simple_http_connection_handler<epee::net_utils::connection_context_base>::parse_cached_header(epee::net_utils::http::http_header_info&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, unsigned long)':
wallet_rpc_server.cpp:(.text._ZN4epee9net_utils4http30simple_http_connection_handlerINS0_23connection_context_baseEE19parse_cached_headerERNS1_16http_header_infoERKNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEm[_ZN4epee9net_utils4http30simple_http_connection_handlerINS0_23connection_context_baseEE19parse_cached_headerERNS1_16http_header_infoERKNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEm]+0x349): undefined reference to `boost::re_detail_106700::perl_matcher<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > >, boost::regex_traits<char, boost::cpp_regex_traits<char> > >::construct_init(boost::basic_regex<char, boost::regex_traits<char, boost::cpp_regex_traits<char> > > const&, boost::regex_constants::_match_flags)'
../../lib/libwallet.a(wallet2.cpp.o): In function `boost::archive::detail::common_iarchive<boost::archive::binary_iarchive>::vload(boost::archive::class_name_type&)':
wallet2.cpp:(.text._ZN5boost7archive6detail15common_iarchiveINS0_15binary_iarchiveEE5vloadERNS0_15class_name_typeE[_ZN5boost7archive6detail15common_iarchiveINS0_15binary_iarchiveEE5vloadERNS0_15class_name_typeE]+0x1): undefined reference to `boost::archive::basic_binary_iarchive<boost::archive::binary_iarchive>::load_override(boost::archive::class_name_type&)'
../../lib/libwallet.a(wallet2.cpp.o): In function `boost::archive::portable_binary_oarchive::portable_binary_oarchive(std::ostream&, unsigned int)':
wallet2.cpp:(.text._ZN5boost7archive24portable_binary_oarchiveC2ERSoj[_ZN5boost7archive24portable_binary_oarchiveC5ERSoj]+0x233): undefined reference to `boost::archive::archive_exception::archive_exception(boost::archive::archive_exception const&)'
../cryptonote_basic/libcryptonote_basic.a(miner.cpp.o): In function `bool boost::regex_match<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > >, char, boost::regex_traits<char, boost::cpp_regex_traits<char> > >(__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, __gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, boost::match_results<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > > >&, boost::basic_regex<char, boost::regex_traits<char, boost::cpp_regex_traits<char> > > const&, boost::regex_constants::_match_flags)':
miner.cpp:(.text._ZN5boost11regex_matchIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEESaINS_9sub_matchISB_EEEcNS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEEEbT_SJ_RNS_13match_resultsISJ_T0_EERKNS_11basic_regexIT1_T2_EENS_15regex_constants12_match_flagsE[_ZN5boost11regex_matchIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEESaINS_9sub_matchISB_EEEcNS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEEEbT_SJ_RNS_13match_resultsISJ_T0_EERKNS_11basic_regexIT1_T2_EENS_15regex_constants12_match_flagsE]+0xf4): undefined reference to `boost::re_detail_106700::perl_matcher<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > >, boost::regex_traits<char, boost::cpp_regex_traits<char> > >::construct_init(boost::basic_regex<char, boost::regex_traits<char, boost::cpp_regex_traits<char> > > const&, boost::regex_constants::_match_flags)'
collect2: error: ld returned 1 exit status
src/wallet/CMakeFiles/wallet_rpc_server.dir/build.make:133: recipe for target 'bin/monero-wallet-rpc' failed
make[3]: *** [bin/monero-wallet-rpc] Error 1
make[3]: Leaving directory '/root/.monero/monero/build/release'
CMakeFiles/Makefile2:2294: recipe for target 'src/wallet/CMakeFiles/wallet_rpc_server.dir/all' failed
make[2]: *** [src/wallet/CMakeFiles/wallet_rpc_server.dir/all] Error 2
make[2]: Leaving directory '/root/.monero/monero/build/release'
Makefile:138: recipe for target 'all' failed
make[1]: *** [all] Error 2
make[1]: Leaving directory '/root/.monero/monero/build/release'
Makefile:64: recipe for target 'release-all' failed
make: *** [release-all] Error 2
`

# Discussion History
## fokinkostya | 2018-05-15T02:38:12+00:00
?

## moneromooo-monero | 2018-05-16T23:31:51+00:00
Are you linking with the same boost you're using headers from ?
You can run make with VERBOSE=1 to get the commands printed.

## moneromooo-monero | 2018-06-20T08:53:52+00:00
Reopen if you can give more info.

+invalid


# Action History
- Created by: fokinkostya | 2018-05-07T04:04:02+00:00
- Closed at: 2018-06-20T08:57:01+00:00
