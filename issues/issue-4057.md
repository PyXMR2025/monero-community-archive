---
title: Make Source code for Ubunto 17.04 failing at 42%
source_url: https://github.com/monero-project/monero/issues/4057
author: spencershaw
assignees: []
labels:
- invalid
created_at: '2018-06-26T11:54:34+00:00'
updated_at: '2018-07-12T22:49:01+00:00'
type: issue
status: closed
closed_at: '2018-07-12T22:49:01+00:00'
---

# Original Description
Fails at 42%. Just hangs.
... 
spencer@Aleph1:~/monero$ sudo -s
root@Aleph1:~/monero# make
mkdir -p build/release
cd build/release && cmake -D BUILD_TESTS=ON -D CMAKE_BUILD_TYPE=release ../.. && make
-- Building without build tag
-- Could not find DEVELOPER_LOCAL_TOOLS in env (not required)
-- BOOST_IGNORE_SYSTEM_PATHS defaults to OFF
-- Could not find DEVELOPER_LIBUNBOUND_OLD in env (not required)
-- Building for a 64-bit system
-- Building internal libraries as static
-- Could not find DATABASE in env (not required unless you want to change database type from default: lmdb)
-- Using LMDB as default DB type
-- Stack trace on exception enabled (using easylogging++)
-- Using OpenSSL include dir at /usr/include
-- Checking for module 'libpcsclite'
--   No package 'libpcsclite' found
-- Could NOT find PCSC (missing: PCSC_LIBRARY PCSC_INCLUDE_DIR)
-- Found miniupnpc API version 10
-- Using in-tree miniupnpc
-- Looking for libunbound
-- Found libunbound include (unbound.h) in /usr/include
-- Found libunbound shared library
-- Using 64-bit LMDB from source tree
-- Could not find PCSC
-- Building on x86_64 for native
-- Using C security hardening flags:  -Wformat -Wformat-security -fstack-protector -fstack-protector-strong
-- Using C++ security hardening flags:  -Wformat -Wformat-security -fstack-protector -fstack-protector-strong
-- Using linker security hardening flags:  -pie -Wl,-z,relro -Wl,-z,now -Wl,-z,noexecstack
-- AES support enabled
-- Found Boost Version: 106200
-- Could not find GNU readline library so building without readline support
-- Found Git: /usr/bin/git
-- Configuring done
-- Generating done
-- Build files have been written to: /home/spencer/monero/build/release
make[1]: Entering directory '/home/spencer/monero/build/release'
make[2]: Entering directory '/home/spencer/monero/build/release'
make[3]: Entering directory '/home/spencer/monero/build/release'
make[3]: Leaving directory '/home/spencer/monero/build/release'
[  3%] Built target generate_translations_header
make[3]: Entering directory '/home/spencer/monero/build/release'
make[3]: Leaving directory '/home/spencer/monero/build/release'
[  8%] Built target libminiupnpc-static
make[3]: Entering directory '/home/spencer/monero/build/release'
make[3]: Leaving directory '/home/spencer/monero/build/release'
[  9%] Built target lmdb
make[3]: Entering directory '/home/spencer/monero/build/release'
make[3]: Leaving directory '/home/spencer/monero/build/release'
[ 10%] Built target easylogging
make[3]: Entering directory '/home/spencer/monero/build/release'
make[3]: Leaving directory '/home/spencer/monero/build/release'
make[3]: Entering directory '/home/spencer/monero/build/release'
[ 10%] Building CXX object contrib/epee/src/CMakeFiles/epee.dir/hex.cpp.o
[ 10%] Building CXX object contrib/epee/src/CMakeFiles/epee.dir/http_auth.cpp.o
[ 11%] Building CXX object contrib/epee/src/CMakeFiles/epee.dir/mlog.cpp.o
[ 11%] Building CXX object contrib/epee/src/CMakeFiles/epee.dir/net_utils_base.cpp.o
[ 11%] Building CXX object contrib/epee/src/CMakeFiles/epee.dir/string_tools.cpp.o
[ 12%] Building CXX object contrib/epee/src/CMakeFiles/epee.dir/wipeable_string.cpp.o
[ 12%] Building C object contrib/epee/src/CMakeFiles/epee.dir/memwipe.c.o
[ 12%] Building CXX object contrib/epee/src/CMakeFiles/epee.dir/connection_basic.cpp.o
[ 13%] Building CXX object contrib/epee/src/CMakeFiles/epee.dir/network_throttle.cpp.o
[ 13%] Building CXX object contrib/epee/src/CMakeFiles/epee.dir/network_throttle-detail.cpp.o
[ 13%] Linking CXX static library libepee.a
make[3]: Leaving directory '/home/spencer/monero/build/release'
[ 13%] Built target epee
make[3]: Entering directory '/home/spencer/monero/build/release'
make[3]: Leaving directory '/home/spencer/monero/build/release'
[ 13%] Built target genversion
make[3]: Entering directory '/home/spencer/monero/build/release'
make[3]: Leaving directory '/home/spencer/monero/build/release'
[ 14%] Built target obj_version
make[3]: Entering directory '/home/spencer/monero/build/release'
make[3]: Leaving directory '/home/spencer/monero/build/release'
[ 14%] Built target version
make[3]: Entering directory '/home/spencer/monero/build/release'
make[3]: Leaving directory '/home/spencer/monero/build/release'
[ 21%] Built target obj_cncrypto
make[3]: Entering directory '/home/spencer/monero/build/release'
make[3]: Leaving directory '/home/spencer/monero/build/release'
[ 22%] Built target cncrypto
make[3]: Entering directory '/home/spencer/monero/build/release'
make[3]: Leaving directory '/home/spencer/monero/build/release'
[ 26%] Built target obj_common
make[3]: Entering directory '/home/spencer/monero/build/release'
make[3]: Leaving directory '/home/spencer/monero/build/release'
[ 27%] Built target common
make[3]: Entering directory '/home/spencer/monero/build/release'
make[3]: Leaving directory '/home/spencer/monero/build/release'
[ 29%] Built target obj_ringct_basic
make[3]: Entering directory '/home/spencer/monero/build/release'
make[3]: Leaving directory '/home/spencer/monero/build/release'
[ 29%] Built target ringct_basic
make[3]: Entering directory '/home/spencer/monero/build/release'
make[3]: Leaving directory '/home/spencer/monero/build/release'
[ 29%] Built target obj_ringct
make[3]: Entering directory '/home/spencer/monero/build/release'
make[3]: Leaving directory '/home/spencer/monero/build/release'
[ 30%] Built target obj_device
make[3]: Entering directory '/home/spencer/monero/build/release'
make[3]: Leaving directory '/home/spencer/monero/build/release'
[ 32%] Built target blocks
make[3]: Entering directory '/home/spencer/monero/build/release'
make[3]: Leaving directory '/home/spencer/monero/build/release'
[ 32%] Built target device
make[3]: Entering directory '/home/spencer/monero/build/release'
make[3]: Leaving directory '/home/spencer/monero/build/release'
[ 32%] Built target obj_checkpoints
make[3]: Entering directory '/home/spencer/monero/build/release'
make[3]: Leaving directory '/home/spencer/monero/build/release'
[ 32%] Built target checkpoints
make[3]: Entering directory '/home/spencer/monero/build/release'
make[3]: Leaving directory '/home/spencer/monero/build/release'
[ 34%] Built target obj_cryptonote_basic
make[3]: Entering directory '/home/spencer/monero/build/release'
make[3]: Leaving directory '/home/spencer/monero/build/release'
[ 34%] Built target cryptonote_basic
make[3]: Entering directory '/home/spencer/monero/build/release'
make[3]: Leaving directory '/home/spencer/monero/build/release'
[ 34%] Built target ringct
make[3]: Entering directory '/home/spencer/monero/build/release'
make[3]: Leaving directory '/home/spencer/monero/build/release'
[ 36%] Built target obj_cryptonote_core
make[3]: Entering directory '/home/spencer/monero/build/release'
make[3]: Leaving directory '/home/spencer/monero/build/release'
[ 37%] Built target obj_multisig
make[3]: Entering directory '/home/spencer/monero/build/release'
make[3]: Leaving directory '/home/spencer/monero/build/release'
[ 37%] Built target multisig
make[3]: Entering directory '/home/spencer/monero/build/release'
make[3]: Leaving directory '/home/spencer/monero/build/release'
[ 38%] Built target obj_blockchain_db
make[3]: Entering directory '/home/spencer/monero/build/release'
make[3]: Leaving directory '/home/spencer/monero/build/release'
[ 40%] Built target blockchain_db
make[3]: Entering directory '/home/spencer/monero/build/release'
make[3]: Leaving directory '/home/spencer/monero/build/release'
[ 40%] Built target cryptonote_core
make[3]: Entering directory '/home/spencer/monero/build/release'
make[3]: Leaving directory '/home/spencer/monero/build/release'
[ 40%] Built target obj_mnemonics
make[3]: Entering directory '/home/spencer/monero/build/release'
make[3]: Leaving directory '/home/spencer/monero/build/release'
[ 40%] Built target mnemonics
make[3]: Entering directory '/home/spencer/monero/build/release'
make[3]: Leaving directory '/home/spencer/monero/build/release'
[ 41%] Built target obj_daemon_rpc_server
make[3]: Entering directory '/home/spencer/monero/build/release'
make[3]: Leaving directory '/home/spencer/monero/build/release'
[ 42%] Built target obj_rpc_base
make[3]: Entering directory '/home/spencer/monero/build/release'
make[3]: Leaving directory '/home/spencer/monero/build/release'
[ 42%] Built target rpc_base
make[3]: Entering directory '/home/spencer/monero/build/release'
make[3]: Leaving directory '/home/spencer/monero/build/release'
make[3]: Entering directory '/home/spencer/monero/build/release'
[ 42%] Building CXX object src/rpc/CMakeFiles/obj_rpc.dir/core_rpc_server.cpp.o
^Csrc/rpc/CMakeFiles/obj_rpc.dir/build.make:62: recipe for target 'src/rpc/CMakeFiles/obj_rpc.dir/core_rpc_server.cpp.o' failed
make[3]: *** [src/rpc/CMakeFiles/obj_rpc.dir/core_rpc_server.cpp.o] Interrupt
CMakeFiles/Makefile2:1863: recipe for target 'src/rpc/CMakeFiles/obj_rpc.dir/all' failed
make[2]: *** [src/rpc/CMakeFiles/obj_rpc.dir/all] Interrupt
Makefile:140: recipe for target 'all' failed
make[1]: *** [all] Interrupt
Makefile:64: recipe for target 'release-all' failed
make: *** [release-all] Interrupt

root@Aleph1:~/monero# make
mkdir -p build/release
cd build/release && cmake -D BUILD_TESTS=ON -D CMAKE_BUILD_TYPE=release ../.. && make
-- Building without build tag
-- Could not find DEVELOPER_LOCAL_TOOLS in env (not required)
-- BOOST_IGNORE_SYSTEM_PATHS defaults to OFF
-- Could not find DEVELOPER_LIBUNBOUND_OLD in env (not required)
-- Building for a 64-bit system
-- Building internal libraries as static
-- Could not find DATABASE in env (not required unless you want to change database type from default: lmdb)
-- Using LMDB as default DB type
-- Stack trace on exception enabled (using easylogging++)
-- Using OpenSSL include dir at /usr/include
-- Checking for module 'libpcsclite'
--   No package 'libpcsclite' found
-- Could NOT find PCSC (missing: PCSC_LIBRARY PCSC_INCLUDE_DIR)
-- Found miniupnpc API version 10
-- Using in-tree miniupnpc
-- Looking for libunbound
-- Found libunbound include (unbound.h) in /usr/include
-- Found libunbound shared library
-- Using 64-bit LMDB from source tree
-- Could not find PCSC
-- Building on x86_64 for native
-- Using C security hardening flags:  -Wformat -Wformat-security -fstack-protector -fstack-protector-strong
-- Using C++ security hardening flags:  -Wformat -Wformat-security -fstack-protector -fstack-protector-strong
-- Using linker security hardening flags:  -pie -Wl,-z,relro -Wl,-z,now -Wl,-z,noexecstack
-- AES support enabled
-- Found Boost Version: 106200
-- Could not find GNU readline library so building without readline support
-- Found Git: /usr/bin/git
-- Configuring done
-- Generating done
-- Build files have been written to: /home/spencer/monero/build/release
make[1]: Entering directory '/home/spencer/monero/build/release'
make[2]: Entering directory '/home/spencer/monero/build/release'
make[3]: Entering directory '/home/spencer/monero/build/release'
make[3]: Leaving directory '/home/spencer/monero/build/release'
[  3%] Built target generate_translations_header
make[3]: Entering directory '/home/spencer/monero/build/release'
make[3]: Leaving directory '/home/spencer/monero/build/release'
[  8%] Built target libminiupnpc-static
make[3]: Entering directory '/home/spencer/monero/build/release'
make[3]: Leaving directory '/home/spencer/monero/build/release'
[  9%] Built target lmdb
make[3]: Entering directory '/home/spencer/monero/build/release'
make[3]: Leaving directory '/home/spencer/monero/build/release'
[ 10%] Built target easylogging
make[3]: Entering directory '/home/spencer/monero/build/release'
make[3]: Leaving directory '/home/spencer/monero/build/release'
[ 13%] Built target epee
make[3]: Entering directory '/home/spencer/monero/build/release'
make[3]: Leaving directory '/home/spencer/monero/build/release'
[ 13%] Built target genversion
make[3]: Entering directory '/home/spencer/monero/build/release'
make[3]: Leaving directory '/home/spencer/monero/build/release'
[ 14%] Built target obj_version
make[3]: Entering directory '/home/spencer/monero/build/release'
make[3]: Leaving directory '/home/spencer/monero/build/release'
[ 14%] Built target version
make[3]: Entering directory '/home/spencer/monero/build/release'
make[3]: Leaving directory '/home/spencer/monero/build/release'
[ 21%] Built target obj_cncrypto
make[3]: Entering directory '/home/spencer/monero/build/release'
make[3]: Leaving directory '/home/spencer/monero/build/release'
[ 22%] Built target cncrypto
make[3]: Entering directory '/home/spencer/monero/build/release'
make[3]: Leaving directory '/home/spencer/monero/build/release'
[ 26%] Built target obj_common
make[3]: Entering directory '/home/spencer/monero/build/release'
make[3]: Leaving directory '/home/spencer/monero/build/release'
[ 27%] Built target common
make[3]: Entering directory '/home/spencer/monero/build/release'
make[3]: Leaving directory '/home/spencer/monero/build/release'
[ 29%] Built target obj_ringct_basic
make[3]: Entering directory '/home/spencer/monero/build/release'
make[3]: Leaving directory '/home/spencer/monero/build/release'
[ 29%] Built target ringct_basic
make[3]: Entering directory '/home/spencer/monero/build/release'
make[3]: Leaving directory '/home/spencer/monero/build/release'
[ 29%] Built target obj_ringct
make[3]: Entering directory '/home/spencer/monero/build/release'
make[3]: Leaving directory '/home/spencer/monero/build/release'
[ 30%] Built target obj_device
make[3]: Entering directory '/home/spencer/monero/build/release'
make[3]: Leaving directory '/home/spencer/monero/build/release'
[ 32%] Built target blocks
make[3]: Entering directory '/home/spencer/monero/build/release'
make[3]: Leaving directory '/home/spencer/monero/build/release'
[ 32%] Built target device
make[3]: Entering directory '/home/spencer/monero/build/release'
make[3]: Leaving directory '/home/spencer/monero/build/release'
[ 32%] Built target obj_checkpoints
make[3]: Entering directory '/home/spencer/monero/build/release'
make[3]: Leaving directory '/home/spencer/monero/build/release'
[ 32%] Built target checkpoints
make[3]: Entering directory '/home/spencer/monero/build/release'
make[3]: Leaving directory '/home/spencer/monero/build/release'
[ 34%] Built target obj_cryptonote_basic
make[3]: Entering directory '/home/spencer/monero/build/release'
make[3]: Leaving directory '/home/spencer/monero/build/release'
[ 34%] Built target cryptonote_basic
make[3]: Entering directory '/home/spencer/monero/build/release'
make[3]: Leaving directory '/home/spencer/monero/build/release'
[ 34%] Built target ringct
make[3]: Entering directory '/home/spencer/monero/build/release'
make[3]: Leaving directory '/home/spencer/monero/build/release'
[ 36%] Built target obj_cryptonote_core
make[3]: Entering directory '/home/spencer/monero/build/release'
make[3]: Leaving directory '/home/spencer/monero/build/release'
[ 37%] Built target obj_multisig
make[3]: Entering directory '/home/spencer/monero/build/release'
make[3]: Leaving directory '/home/spencer/monero/build/release'
[ 37%] Built target multisig
make[3]: Entering directory '/home/spencer/monero/build/release'
make[3]: Leaving directory '/home/spencer/monero/build/release'
[ 38%] Built target obj_blockchain_db
make[3]: Entering directory '/home/spencer/monero/build/release'
make[3]: Leaving directory '/home/spencer/monero/build/release'
[ 40%] Built target blockchain_db
make[3]: Entering directory '/home/spencer/monero/build/release'
make[3]: Leaving directory '/home/spencer/monero/build/release'
[ 40%] Built target cryptonote_core
make[3]: Entering directory '/home/spencer/monero/build/release'
make[3]: Leaving directory '/home/spencer/monero/build/release'
[ 40%] Built target obj_mnemonics
make[3]: Entering directory '/home/spencer/monero/build/release'
make[3]: Leaving directory '/home/spencer/monero/build/release'
[ 40%] Built target mnemonics
make[3]: Entering directory '/home/spencer/monero/build/release'
make[3]: Leaving directory '/home/spencer/monero/build/release'
[ 41%] Built target obj_daemon_rpc_server
make[3]: Entering directory '/home/spencer/monero/build/release'
make[3]: Leaving directory '/home/spencer/monero/build/release'
[ 42%] Built target obj_rpc_base
make[3]: Entering directory '/home/spencer/monero/build/release'
make[3]: Leaving directory '/home/spencer/monero/build/release'
[ 42%] Built target rpc_base
make[3]: Entering directory '/home/spencer/monero/build/release'
make[3]: Leaving directory '/home/spencer/monero/build/release'
make[3]: Entering directory '/home/spencer/monero/build/release'
[ 42%] Building CXX object src/rpc/CMakeFiles/obj_rpc.dir/core_rpc_server.cpp.o


# Discussion History
## moneromooo-monero | 2018-06-26T21:20:35+00:00
Did you wait for that file to finish compiling ?

## moneromooo-monero | 2018-07-12T22:10:38+00:00
+invalid


# Action History
- Created by: spencershaw | 2018-06-26T11:54:34+00:00
- Closed at: 2018-07-12T22:49:01+00:00
