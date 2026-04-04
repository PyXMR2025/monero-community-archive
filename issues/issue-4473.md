---
title: Cannot compile release v0.12 on Ubuntu 18 (GCC 7)
source_url: https://github.com/monero-project/monero/issues/4473
author: rotavele
assignees: []
labels: []
created_at: '2018-09-29T21:40:41+00:00'
updated_at: '2018-10-06T18:40:50+00:00'
type: issue
status: closed
closed_at: '2018-10-06T18:40:50+00:00'
---

# Original Description
This is the error I am getting trying to compile the latest updates to the release branch for V0.12. Please let me know if I can give more complete information.

`In function ‘bool cryptonote::construct_miner_tx(size_t, size_t, uint64_t, size_t, uint64_t, const cryptonote::account_public_address&, cryptonote::transaction&, const blobdata&, size_t, uint8_t)’:
cc1plus: error: ‘void* __builtin_memset(void*, int, long unsigned int)’: specified size 18446744073709551608 exceeds maximum object size 9223372036854775807 [-Werror=stringop-overflow=]`

# Discussion History
## rotavele | 2018-09-29T21:44:32+00:00
Additional output:
```
make -j32
mkdir -p build/release
cd build/release && cmake -D BUILD_TESTS=ON -D CMAKE_BUILD_TYPE=release ../.. && make
-- The C compiler identification is GNU 7.3.0
-- The CXX compiler identification is GNU 7.3.0
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
-- Found OpenSSL: /usr/lib/x86_64-linux-gnu/libcrypto.so (found version "1.1.0g")
-- Using OpenSSL include dir at /usr/include
-- Found PkgConfig: /usr/bin/pkg-config (found version "0.29.1")
-- Checking for module 'libpcsclite'
--   No package 'libpcsclite' found
-- Could NOT find PCSC (missing: PCSC_LIBRARY PCSC_INCLUDE_DIR)
-- Looking for memset_s in c
-- Looking for memset_s in c - not found
-- Looking for explicit_bzero in c
-- Looking for explicit_bzero in c - found
-- Looking for strptime
-- Looking for strptime - found
-- Found MiniUPnPc: /usr/include/miniupnpc
-- Found miniupnpc API version 10
-- Using in-tree miniupnpc
-- Looking for libunbound
-- Found libunbound include (unbound.h) in /usr/include
-- Found libunbound shared library
-- Using 64-bit LMDB from source tree
-- Could not find PCSC
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
-- Found Boost Version: 106501
-- Found Readline: /usr/include
-- Looking for rl_copy_text
-- Looking for rl_copy_text - found
-- Looking for rl_filename_completion_function
-- Looking for rl_filename_completion_function - found
-- Found readline library at: /usr
-- Found Git: /usr/bin/git
-- Could NOT find GTest (missing: GTEST_LIBRARY GTEST_MAIN_LIBRARY)
-- GTest not found on the system: will use GTest bundled with this source
-- Found Doxygen: /usr/bin/doxygen (found version "1.8.13") found components:  doxygen dot
-- Performing Test HAVE_C11
-- Performing Test HAVE_C11 - Success
-- Configuring done
-- Generating done
-- Build files have been written to: /home/monerouser/monero/build/release
make[1]: Entering directory '/home/monerouser/monero/build/release'
make[2]: Entering directory '/home/monerouser/monero/build/release'
make[3]: Entering directory '/home/monerouser/monero/build/release'
make[3]: Entering directory '/home/monerouser/monero/build/release'
make[3]: Entering directory '/home/monerouser/monero/build/release'
make[3]: Entering directory '/home/monerouser/monero/build/release'
make[3]: Entering directory '/home/monerouser/monero/build/release'
make[3]: Entering directory '/home/monerouser/monero/build/release'
make[3]: Entering directory '/home/monerouser/monero/build/release'
make[3]: Entering directory '/home/monerouser/monero/build/release'
make[3]: Entering directory '/home/monerouser/monero/build/release'
make[3]: Entering directory '/home/monerouser/monero/build/release'
make[3]: Entering directory '/home/monerouser/monero/build/release'
make[3]: Entering directory '/home/monerouser/monero/build/release'
make[3]: Entering directory '/home/monerouser/monero/build/release'
make[3]: Entering directory '/home/monerouser/monero/build/release'
make[3]: Entering directory '/home/monerouser/monero/build/release'
make[3]: Entering directory '/home/monerouser/monero/build/release'
make[3]: Entering directory '/home/monerouser/monero/build/release'
make[3]: Entering directory '/home/monerouser/monero/build/release'
make[3]: Entering directory '/home/monerouser/monero/build/release'
make[3]: Entering directory '/home/monerouser/monero/build/release'
make[3]: Entering directory '/home/monerouser/monero/build/release'
make[3]: Entering directory '/home/monerouser/monero/build/release'
make[3]: Entering directory '/home/monerouser/monero/build/release'
make[3]: Entering directory '/home/monerouser/monero/build/release'
make[3]: Entering directory '/home/monerouser/monero/build/release'
make[3]: Entering directory '/home/monerouser/monero/build/release'
Scanning dependencies of target genversion
make[3]: Leaving directory '/home/monerouser/monero/build/release'
Scanning dependencies of target obj_cncrypto
Scanning dependencies of target generate_translations_header
Scanning dependencies of target obj_cryptonote_basic
Scanning dependencies of target obj_multisig
Scanning dependencies of target obj_cryptonote_core
Scanning dependencies of target obj_rpc_base
Scanning dependencies of target obj_mnemonics
Scanning dependencies of target obj_daemon_rpc_server
make[3]: Entering directory '/home/monerouser/monero/build/release'
make[3]: Leaving directory '/home/monerouser/monero/build/release'
Scanning dependencies of target obj_ringct
[  0%] Generating stagenet_blocks.o
[  0%] Generating blocks.o
Scanning dependencies of target lmdb
Scanning dependencies of target easylogging
Scanning dependencies of target libminiupnpc-static
Scanning dependencies of target obj_checkpoints
Scanning dependencies of target googletest
Scanning dependencies of target obj_device
make[3]: Entering directory '/home/monerouser/monero/build/release'
[  1%] Generating testnet_blocks.o
Scanning dependencies of target obj_ringct_basic
make[3]: Leaving directory '/home/monerouser/monero/build/release'
Scanning dependencies of target obj_p2p
Scanning dependencies of target obj_daemon_messages
Scanning dependencies of target obj_daemonizer
make[3]: Entering directory '/home/monerouser/monero/build/release'
make[3]: Leaving directory '/home/monerouser/monero/build/release'
Scanning dependencies of target obj_blockchain_db
Scanning dependencies of target obj_cryptonote_protocol
Scanning dependencies of target obj_rpc
Scanning dependencies of target obj_serialization
make[3]: Entering directory '/home/monerouser/monero/build/release'
Scanning dependencies of target obj_wallet
make[3]: Leaving directory '/home/monerouser/monero/build/release'
make[3]: Leaving directory '/home/monerouser/monero/build/release'
make[3]: Leaving directory '/home/monerouser/monero/build/release'
make[3]: Leaving directory '/home/monerouser/monero/build/release'
[  1%] Generating ../version.cpp
make[3]: Entering directory '/home/monerouser/monero/build/release'
make[3]: Entering directory '/home/monerouser/monero/build/release'
make[3]: Leaving directory '/home/monerouser/monero/build/release'
make[3]: Entering directory '/home/monerouser/monero/build/release'
make[3]: Leaving directory '/home/monerouser/monero/build/release'
make[3]: Leaving directory '/home/monerouser/monero/build/release'
make[3]: Leaving directory '/home/monerouser/monero/build/release'
make[3]: Entering directory '/home/monerouser/monero/build/release'
[  1%] Creating directories for 'generate_translations_header'
make[3]: Entering directory '/home/monerouser/monero/build/release'
make[3]: Entering directory '/home/monerouser/monero/build/release'
make[3]: Entering directory '/home/monerouser/monero/build/release'
make[3]: Leaving directory '/home/monerouser/monero/build/release'
make[3]: Entering directory '/home/monerouser/monero/build/release'
make[3]: Entering directory '/home/monerouser/monero/build/release'
make[3]: Leaving directory '/home/monerouser/monero/build/release'
Scanning dependencies of target blocks
make[3]: Leaving directory '/home/monerouser/monero/build/release'
make[3]: Entering directory '/home/monerouser/monero/build/release'
[  1%] Building CXX object external/easylogging++/CMakeFiles/easylogging.dir/easylogging++.cc.o
make[3]: Leaving directory '/home/monerouser/monero/build/release'
[  2%] Building CXX object src/rpc/CMakeFiles/obj_rpc_base.dir/rpc_args.cpp.o
make[3]: Entering directory '/home/monerouser/monero/build/release'
[  2%] Creating directories for 'googletest'
[  2%] Building C object external/db_drivers/liblmdb/CMakeFiles/lmdb.dir/midl.c.o
[  2%] Building CXX object src/daemonizer/CMakeFiles/obj_daemonizer.dir/posix_fork.cpp.o
[  3%] Building CXX object src/multisig/CMakeFiles/obj_multisig.dir/multisig.cpp.o
make[3]: Entering directory '/home/monerouser/monero/build/release'
[  3%] Building C object external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-static.dir/igd_desc_parse.c.o
[  3%] Building C object external/db_drivers/liblmdb/CMakeFiles/lmdb.dir/mdb.c.o
-- You are currently on commit 517faceb
[  3%] Building C object external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-static.dir/minisoap.c.o
[  3%] Building C object external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-static.dir/minixml.c.o
[  3%] Building CXX object src/ringct/CMakeFiles/obj_ringct.dir/rctSigs.cpp.o
[  4%] Building C object external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-static.dir/miniupnpc.c.o
[  4%] Building CXX object src/mnemonics/CMakeFiles/obj_mnemonics.dir/electrum-words.cpp.o
make[3]: Leaving directory '/home/monerouser/monero/build/release'
make[3]: Leaving directory '/home/monerouser/monero/build/release'
[  4%] Building CXX object src/checkpoints/CMakeFiles/obj_checkpoints.dir/checkpoints.cpp.o
-- The most recent tag was at 558da368
-- You are ahead of or behind a tagged release
make[3]: Leaving directory '/home/monerouser/monero/build/release'
make[3]: Leaving directory '/home/monerouser/monero/build/release'
[  5%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/aesb.c.o
[  6%] Building C object external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-static.dir/minissdpc.c.o
[  6%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/blake256.c.o
make[3]: Leaving directory '/home/monerouser/monero/build/release'
make[3]: Leaving directory '/home/monerouser/monero/build/release'
make[3]: Leaving directory '/home/monerouser/monero/build/release'
make[3]: Leaving directory '/home/monerouser/monero/build/release'
make[3]: Entering directory '/home/monerouser/monero/build/release'
make[3]: Entering directory '/home/monerouser/monero/build/release'
[  6%] Building C object src/blocks/CMakeFiles/blocks.dir/blockexports.c.o
make[3]: Entering directory '/home/monerouser/monero/build/release'
make[3]: Entering directory '/home/monerouser/monero/build/release'
[  7%] Building CXX object src/ringct/CMakeFiles/obj_ringct_basic.dir/rctOps.cpp.o
make[3]: Leaving directory '/home/monerouser/monero/build/release'
[  7%] Building CXX object src/device/CMakeFiles/obj_device.dir/device.cpp.o
make[3]: Entering directory '/home/monerouser/monero/build/release'
make[3]: Entering directory '/home/monerouser/monero/build/release'
make[3]: Entering directory '/home/monerouser/monero/build/release'
make[3]: Entering directory '/home/monerouser/monero/build/release'
[  8%] Building CXX object src/rpc/CMakeFiles/obj_daemon_messages.dir/message.cpp.o
[  8%] Building CXX object src/serialization/CMakeFiles/obj_serialization.dir/json_object.cpp.o
[  9%] Building CXX object src/cryptonote_basic/CMakeFiles/obj_cryptonote_basic.dir/account.cpp.o
[  9%] Built target genversion
[  9%] Building CXX object src/p2p/CMakeFiles/obj_p2p.dir/net_node.cpp.o
[ 10%] Building CXX object src/blockchain_db/CMakeFiles/obj_blockchain_db.dir/blockchain_db.cpp.o
[ 10%] Building CXX object src/rpc/CMakeFiles/obj_daemon_rpc_server.dir/daemon_handler.cpp.o
make[3]: Leaving directory '/home/monerouser/monero/build/release'
[ 11%] Building CXX object src/cryptonote_core/CMakeFiles/obj_cryptonote_core.dir/blockchain.cpp.o
[ 11%] Building CXX object src/cryptonote_protocol/CMakeFiles/obj_cryptonote_protocol.dir/block_queue.cpp.o
make[3]: Entering directory '/home/monerouser/monero/build/release'
make[3]: Leaving directory '/home/monerouser/monero/build/release'
[ 11%] Building CXX object src/cryptonote_basic/CMakeFiles/obj_cryptonote_basic.dir/cryptonote_basic_impl.cpp.o
make[3]: Entering directory '/home/monerouser/monero/build/release'
[ 11%] Building CXX object src/rpc/CMakeFiles/obj_rpc.dir/core_rpc_server.cpp.o
[ 12%] Linking C static library libblocks.a
[ 12%] Building CXX object src/wallet/CMakeFiles/obj_wallet.dir/wallet2.cpp.o
make[3]: Leaving directory '/home/monerouser/monero/build/release'
[ 12%] Building CXX object src/wallet/CMakeFiles/obj_wallet.dir/wallet_args.cpp.o
[ 13%] Building CXX object src/wallet/CMakeFiles/obj_wallet.dir/ringdb.cpp.o
[ 13%] Built target blocks
[ 13%] No download step for 'generate_translations_header'
[ 13%] Building CXX object src/rpc/CMakeFiles/obj_daemon_messages.dir/daemon_messages.cpp.o
[ 13%] No download step for 'googletest'
[ 14%] Building CXX object src/rpc/CMakeFiles/obj_daemon_rpc_server.dir/zmq_server.cpp.o
[ 14%] No patch step for 'generate_translations_header'
[ 14%] No patch step for 'googletest'
[ 15%] No update step for 'generate_translations_header'
[ 16%] No update step for 'googletest'
[ 16%] Building CXX object src/rpc/CMakeFiles/obj_rpc.dir/instanciations.cpp.o
make[3]: Entering directory '/home/monerouser/monero/build/release'
[ 16%] Performing configure step for 'generate_translations_header'
[ 16%] Performing configure step for 'googletest'
Scanning dependencies of target obj_version
make[3]: Leaving directory '/home/monerouser/monero/build/release'
make[3]: Entering directory '/home/monerouser/monero/build/release'
[ 17%] Building CXX object src/cryptonote_protocol/CMakeFiles/obj_cryptonote_protocol.dir/cryptonote_protocol_handler-base.cpp.o
[ 17%] Building CXX object src/CMakeFiles/obj_version.dir/__/version.cpp.o
[ 17%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/chacha.c.o
make[3]: Leaving directory '/home/monerouser/monero/build/release'
[ 17%] Building C object external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-static.dir/miniwget.c.o
[ 17%] Built target obj_version
[ 18%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/crypto-ops-data.c.o
-- The C compiler identification is GNU 7.3.0
-- The CXX compiler identification is GNU 7.3.0
make[3]: Entering directory '/home/monerouser/monero/build/release'
Scanning dependencies of target version
make[3]: Leaving directory '/home/monerouser/monero/build/release'
-- The CXX compiler identification is GNU 7.3.0
make[3]: Entering directory '/home/monerouser/monero/build/release'
-- Check for working C compiler: /usr/bin/cc
[ 18%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/crypto-ops.c.o
[ 18%] Linking CXX static library libversion.a
make[3]: Leaving directory '/home/monerouser/monero/build/release'
-- The C compiler identification is GNU 7.3.0
[ 18%] Built target version
-- Check for working CXX compiler: /usr/bin/c++
[ 19%] Building CXX object src/device/CMakeFiles/obj_device.dir/device_default.cpp.o
[ 19%] Building C object external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-static.dir/upnpcommands.c.o
-- Check for working C compiler: /usr/bin/cc -- works
-- Detecting C compiler ABI info
-- Check for working CXX compiler: /usr/bin/c++ -- works
-- Detecting CXX compiler ABI info
-- Detecting C compiler ABI info - done
-- Detecting C compile features
-- Detecting CXX compiler ABI info - done
-- Detecting CXX compile features
[ 20%] Building C object external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-static.dir/upnpdev.c.o
[ 20%] Building C object external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-static.dir/upnpreplyparse.c.o
[ 20%] Building C object external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-static.dir/upnperrors.c.o
-- Detecting C compile features - done
-- Check for working CXX compiler: /usr/bin/c++
[ 21%] Building C object external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-static.dir/connecthostport.c.o
-- Check for working CXX compiler: /usr/bin/c++ -- works
-- Detecting CXX compiler ABI info
[ 21%] Building C object external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-static.dir/portlistingparse.c.o
-- Detecting CXX compiler ABI info - done
[ 21%] Building C object external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-static.dir/receivedata.c.o
-- Detecting CXX compile features
make[3]: Leaving directory '/home/monerouser/monero/build/release'
-- Detecting CXX compile features - done
-- Check for working C compiler: /usr/bin/cc
[ 21%] Built target obj_daemonizer
[ 21%] Building CXX object src/device/CMakeFiles/obj_device.dir/log.cpp.o
[ 22%] Linking C static library libminiupnpc.a
make[3]: Leaving directory '/home/monerouser/monero/build/release'
[ 22%] Built target libminiupnpc-static
[ 22%] Building CXX object src/wallet/CMakeFiles/obj_wallet.dir/node_rpc_proxy.cpp.o
-- Check for working C compiler: /usr/bin/cc -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Detecting C compile features
-- Detecting CXX compile features - done
CMake Warning at CMakeLists.txt:38 (message):
  lrelease program not found, translation files not built


-- Configuring done
-- Generating done
-- Build files have been written to: /home/monerouser/monero/build/release/translations
-- Detecting C compile features - done
-- Found PythonInterp: /usr/bin/python (found version "2.7.15")
-- Looking for pthread.h
[ 23%] Performing build step for 'generate_translations_header'
make[4]: Entering directory '/home/monerouser/monero/build/release/translations'
make[5]: Entering directory '/home/monerouser/monero/build/release/translations'
make[6]: Entering directory '/home/monerouser/monero/build/release/translations'
Scanning dependencies of target generate_translations_header
make[6]: Leaving directory '/home/monerouser/monero/build/release/translations'
make[6]: Entering directory '/home/monerouser/monero/build/release/translations'
[ 50%] Building C object CMakeFiles/generate_translations_header.dir/generate_translations_header.c.o
-- Looking for pthread.h - found
-- Looking for pthread_create
[100%] Linking C executable generate_translations_header
[ 23%] Building CXX object src/crypto/CMakeFiles/obj_cncrypto.dir/crypto.cpp.o
Generating embedded translations header
make[6]: Leaving directory '/home/monerouser/monero/build/release/translations'
[100%] Built target generate_translations_header
make[5]: Leaving directory '/home/monerouser/monero/build/release/translations'
make[4]: Leaving directory '/home/monerouser/monero/build/release/translations'
-- Looking for pthread_create - not found
-- Looking for pthread_create in pthreads
[ 24%] Performing install step for 'generate_translations_header'

[ 24%] Completed 'generate_translations_header'
make[3]: Leaving directory '/home/monerouser/monero/build/release'
-- Looking for pthread_create in pthreads - not found
-- Looking for pthread_create in pthread
[ 24%] Built target generate_translations_header
[ 24%] Building CXX object src/blockchain_db/CMakeFiles/obj_blockchain_db.dir/lmdb/db_lmdb.cpp.o
-- Looking for pthread_create in pthread - found
-- Found Threads: TRUE
-- Configuring done
-- Generating done
-- Build files have been written to: /home/monerouser/monero/build/release/tests/gtest
[ 25%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/groestl.c.o
[ 26%] Performing build step for 'googletest'
make[4]: Entering directory '/home/monerouser/monero/build/release/tests/gtest'
[ 27%] Linking C static library liblmdb.a
make[5]: Entering directory '/home/monerouser/monero/build/release/tests/gtest'
make[6]: Entering directory '/home/monerouser/monero/build/release/tests/gtest'
make[3]: Leaving directory '/home/monerouser/monero/build/release'
Scanning dependencies of target gtest
[ 27%] Built target lmdb
make[3]: Entering directory '/home/monerouser/monero/build/release'
make[6]: Leaving directory '/home/monerouser/monero/build/release/tests/gtest'
make[6]: Entering directory '/home/monerouser/monero/build/release/tests/gtest'
Scanning dependencies of target obj_common
[ 25%] Building CXX object CMakeFiles/gtest.dir/src/gtest-all.cc.o
make[3]: Leaving directory '/home/monerouser/monero/build/release'
make[3]: Entering directory '/home/monerouser/monero/build/release'
[ 27%] Building CXX object src/common/CMakeFiles/obj_common.dir/base58.cpp.o
[ 27%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/hash-extra-blake.c.o
[ 27%] Building CXX object src/common/CMakeFiles/obj_common.dir/command_line.cpp.o
[ 27%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/hash-extra-groestl.c.o
[ 28%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/hash-extra-jh.c.o
[ 28%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/hash-extra-skein.c.o
[ 28%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/hash.c.o
[ 29%] Building CXX object src/common/CMakeFiles/obj_common.dir/dns_utils.cpp.o
[ 30%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/jh.c.o
[ 30%] Building CXX object src/ringct/CMakeFiles/obj_ringct_basic.dir/rctTypes.cpp.o
[ 30%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/keccak.c.o
make[3]: Leaving directory '/home/monerouser/monero/build/release'
[ 30%] Built target obj_rpc_base
[ 30%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/oaes_lib.c.o
[ 31%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/random.c.o
[ 31%] Building C object src/ringct/CMakeFiles/obj_ringct_basic.dir/rctCryptoOps.c.o
[ 31%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/skein.c.o
[ 32%] Building CXX object src/ringct/CMakeFiles/obj_ringct_basic.dir/bulletproofs.cc.o
[ 32%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/slow-hash.c.o
[ 34%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/tree-hash.c.o
[ 34%] Building CXX object src/cryptonote_core/CMakeFiles/obj_cryptonote_core.dir/cryptonote_core.cpp.o
make[3]: Leaving directory '/home/monerouser/monero/build/release'
[ 34%] Built target obj_multisig
[ 34%] Building CXX object src/common/CMakeFiles/obj_common.dir/download.cpp.o
[ 34%] Building CXX object src/cryptonote_core/CMakeFiles/obj_cryptonote_core.dir/tx_pool.cpp.o
make[3]: Leaving directory '/home/monerouser/monero/build/release'
[ 34%] Built target obj_cncrypto
[ 35%] Building CXX object src/cryptonote_core/CMakeFiles/obj_cryptonote_core.dir/cryptonote_tx_utils.cpp.o
[ 35%] Building CXX object src/common/CMakeFiles/obj_common.dir/util.cpp.o
[ 35%] Building CXX object src/cryptonote_basic/CMakeFiles/obj_cryptonote_basic.dir/cryptonote_format_utils.cpp.o
[ 36%] Building CXX object src/cryptonote_basic/CMakeFiles/obj_cryptonote_basic.dir/difficulty.cpp.o
[ 36%] Building CXX object src/cryptonote_basic/CMakeFiles/obj_cryptonote_basic.dir/hardfork.cpp.o
[ 36%] Building CXX object src/cryptonote_basic/CMakeFiles/obj_cryptonote_basic.dir/miner.cpp.o
[ 37%] Linking CXX static library libeasylogging.a
[ 38%] Building CXX object src/common/CMakeFiles/obj_common.dir/i18n.cpp.o
make[3]: Leaving directory '/home/monerouser/monero/build/release'
make[3]: Leaving directory '/home/monerouser/monero/build/release'
[ 38%] Built target easylogging
make[3]: Entering directory '/home/monerouser/monero/build/release'
[ 38%] Built target obj_device
make[3]: Entering directory '/home/monerouser/monero/build/release'
Scanning dependencies of target epee
Scanning dependencies of target epee_readline
make[3]: Leaving directory '/home/monerouser/monero/build/release'
make[3]: Entering directory '/home/monerouser/monero/build/release'
make[3]: Leaving directory '/home/monerouser/monero/build/release'
make[3]: Entering directory '/home/monerouser/monero/build/release'
[ 39%] Building CXX object contrib/epee/src/CMakeFiles/epee_readline.dir/readline_buffer.cpp.o
[ 39%] Building CXX object contrib/epee/src/CMakeFiles/epee.dir/hex.cpp.o
[ 39%] Building CXX object contrib/epee/src/CMakeFiles/epee.dir/http_auth.cpp.o
[ 40%] Building CXX object contrib/epee/src/CMakeFiles/epee.dir/mlog.cpp.o
[ 40%] Building CXX object src/common/CMakeFiles/obj_common.dir/password.cpp.o
[ 50%] Linking CXX static library libgtest.a
[ 40%] Building CXX object src/common/CMakeFiles/obj_common.dir/perf_timer.cpp.o
make[6]: Leaving directory '/home/monerouser/monero/build/release/tests/gtest'
[ 50%] Built target gtest
make[6]: Entering directory '/home/monerouser/monero/build/release/tests/gtest'
Scanning dependencies of target gtest_main
make[6]: Leaving directory '/home/monerouser/monero/build/release/tests/gtest'
make[6]: Entering directory '/home/monerouser/monero/build/release/tests/gtest'
[ 75%] Building CXX object CMakeFiles/gtest_main.dir/src/gtest_main.cc.o
[ 40%] Building CXX object contrib/epee/src/CMakeFiles/epee.dir/net_utils_base.cpp.o
make[3]: Leaving directory '/home/monerouser/monero/build/release'
[ 40%] Built target obj_ringct
[ 40%] Building CXX object contrib/epee/src/CMakeFiles/epee.dir/string_tools.cpp.o
[ 41%] Building CXX object src/common/CMakeFiles/obj_common.dir/threadpool.cpp.o
[100%] Linking CXX static library libgtest_main.a
make[6]: Leaving directory '/home/monerouser/monero/build/release/tests/gtest'
[100%] Built target gtest_main
make[5]: Leaving directory '/home/monerouser/monero/build/release/tests/gtest'
make[4]: Leaving directory '/home/monerouser/monero/build/release/tests/gtest'
[ 41%] Building CXX object src/common/CMakeFiles/obj_common.dir/updates.cpp.o
[ 42%] No install step for 'googletest'
[ 42%] Completed 'googletest'
make[3]: Leaving directory '/home/monerouser/monero/build/release'
[ 42%] Built target googletest
[ 42%] Building CXX object src/common/CMakeFiles/obj_common.dir/stack_trace.cpp.o
[ 43%] Building CXX object contrib/epee/src/CMakeFiles/epee.dir/wipeable_string.cpp.o
make[3]: Leaving directory '/home/monerouser/monero/build/release'
[ 43%] Built target obj_ringct_basic
[ 43%] Building C object contrib/epee/src/CMakeFiles/epee.dir/memwipe.c.o
[ 43%] Building CXX object contrib/epee/src/CMakeFiles/epee.dir/connection_basic.cpp.o
[ 44%] Building CXX object contrib/epee/src/CMakeFiles/epee.dir/network_throttle.cpp.o
[ 44%] Building CXX object contrib/epee/src/CMakeFiles/epee.dir/network_throttle-detail.cpp.o
[ 44%] Linking CXX static library libepee_readline.a
make[3]: Leaving directory '/home/monerouser/monero/build/release'
[ 44%] Built target epee_readline
make[3]: Leaving directory '/home/monerouser/monero/build/release'
[ 44%] Built target obj_serialization
make[3]: Leaving directory '/home/monerouser/monero/build/release'
[ 44%] Built target obj_daemon_messages
In function ‘bool cryptonote::construct_miner_tx(size_t, size_t, uint64_t, size_t, uint64_t, const cryptonote::account_public_address&, cryptonote::transaction&, const blobdata&, size_t, uint8_t)’:
cc1plus: error: ‘void* __builtin_memset(void*, int, long unsigned int)’: specified size 18446744073709551608 exceeds maximum object size 9223372036854775807 [-Werror=stringop-overflow=]
make[3]: Leaving directory '/home/monerouser/monero/build/release'
[ 44%] Built target obj_p2p
make[3]: Leaving directory '/home/monerouser/monero/build/release'
[ 44%] Built target obj_cryptonote_protocol
cc1plus: all warnings being treated as errors
src/cryptonote_core/CMakeFiles/obj_cryptonote_core.dir/build.make:134: recipe for target 'src/cryptonote_core/CMakeFiles/obj_cryptonote_core.dir/cryptonote_tx_utils.cpp.o' failed
make[3]: *** [src/cryptonote_core/CMakeFiles/obj_cryptonote_core.dir/cryptonote_tx_utils.cpp.o] Error 1
make[3]: *** Waiting for unfinished jobs....
make[3]: Leaving directory '/home/monerouser/monero/build/release'
[ 44%] Built target obj_checkpoints
make[3]: Leaving directory '/home/monerouser/monero/build/release'
[ 44%] Built target obj_common
make[3]: Leaving directory '/home/monerouser/monero/build/release'
[ 44%] Built target obj_daemon_rpc_server
make[3]: Leaving directory '/home/monerouser/monero/build/release'
[ 44%] Built target obj_blockchain_db
make[3]: Leaving directory '/home/monerouser/monero/build/release'
[ 44%] Built target obj_mnemonics
make[3]: Leaving directory '/home/monerouser/monero/build/release'
CMakeFiles/Makefile2:1317: recipe for target 'src/cryptonote_core/CMakeFiles/obj_cryptonote_core.dir/all' failed
make[2]: *** [src/cryptonote_core/CMakeFiles/obj_cryptonote_core.dir/all] Error 2
make[2]: *** Waiting for unfinished jobs....
[ 44%] Linking CXX static library libepee.a
make[3]: Leaving directory '/home/monerouser/monero/build/release'
[ 44%] Built target epee

make[3]: Leaving directory '/home/monerouser/monero/build/release'
[ 44%] Built target obj_cryptonote_basic
make[3]: Leaving directory '/home/monerouser/monero/build/release'
[ 44%] Built target obj_rpc
make[3]: Leaving directory '/home/monerouser/monero/build/release'
[ 44%] Built target obj_wallet
make[2]: Leaving directory '/home/monerouser/monero/build/release'
Makefile:140: recipe for target 'all' failed
make[1]: *** [all] Error 2
make[1]: Leaving directory '/home/monerouser/monero/build/release'
Makefile:64: recipe for target 'release-all' failed
make: *** [release-all] Error 2
```

## rotavele | 2018-09-29T22:13:50+00:00
Perhaps I need an earlier version of GCC.

EDIT:
Ok. Downgrading to gcc6 worked. On Ubuntu I did this with the following shell commands.
```
sudo apt update
sudo apt install gcc-6 g++-6
sudo update-alternatives --install "/usr/bin/gcc" "gcc" "/usr/bin/gcc-6" 60 --slave "/usr/bin/g++" "g++" "/usr/bin/g++-6"
sudo update-alternatives --config gcc
gcc --version
g++ --version
```

## moneromooo-monero | 2018-09-30T08:45:15+00:00
It's going to be a step by step process. Can you first try this patch (it will create incorrect code, I just want to know if it get rid of the error:

<pre>
diff --git a/src/cryptonote_core/cryptonote_tx_utils.cpp b/src/cryptonote_core/cryptonote_tx_utils.cpp
index fb2af9c..15943d7 100644
--- a/src/cryptonote_core/cryptonote_tx_utils.cpp
+++ b/src/cryptonote_core/cryptonote_tx_utils.cpp
@@ -135,6 +135,7 @@ namespace cryptonote
       CHECK_AND_ASSERT_MES(max_outs >= out_amounts.size(), false, "max_out exceeded");
     }
 
+#if 0
     uint64_t summary_amounts = 0;
     for (size_t no = 0; no < out_amounts.size(); no++)
     {
@@ -167,6 +168,7 @@ namespace cryptonote
     tx.vin.push_back(in);
 
     tx.invalidate_hashes();
+#endif
 
     //LOG_PRINT("MINER_TX generated ok, block_reward=" << print_money(block_reward) << "("  << print_money(block_reward - fee) << "+" << print_money(fee)
     //  << "), current_block_size=" << current_block_size << ", already_generated_coins=" << already_generated_coins << ", tx_id=" << get_transaction_hash(tx), LOG_LEVEL_2);
</pre>


## moneromooo-monero | 2018-09-30T11:10:40+00:00
Ignore what I asked, please try the patch linked above instead.

## moneromooo-monero | 2018-10-06T18:22:10+00:00
I'll call this fixed then.

+resolved

# Action History
- Created by: rotavele | 2018-09-29T21:40:41+00:00
- Closed at: 2018-10-06T18:40:50+00:00
