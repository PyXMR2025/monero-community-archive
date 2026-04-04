---
title: Does not compile on arch
source_url: https://github.com/monero-project/monero/issues/42
author: dmp1ce
assignees: []
labels: []
created_at: '2014-06-15T13:50:34+00:00'
updated_at: '2014-06-16T17:05:23+00:00'
type: issue
status: closed
closed_at: '2014-06-16T17:05:23+00:00'
---

# Original Description
I'm experiencing the same issue as seen here: 

https://github.com/bitmonero-project/bitmonero/issues/8

```
make
mkdir -p build/release
cd build/release && cmake -D CMAKE_BUILD_TYPE=Release ../..
-- The C compiler identification is GNU 4.9.0
-- The CXX compiler identification is GNU 4.9.0
-- Check for working C compiler: /usr/bin/cc
-- Check for working C compiler: /usr/bin/cc -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working CXX compiler: /usr/bin/c++
-- Check for working CXX compiler: /usr/bin/c++ -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Boost version: 1.55.0
-- Found the following Boost libraries:
--   system
--   filesystem
--   thread
--   date_time
--   chrono
--   regex
--   serialization
--   program_options
-- Found Git: /usr/bin/git
-- Found PythonInterp: /usr/bin/python (found version "3.4.1") 
-- Looking for include file pthread.h
-- Looking for include file pthread.h - not found
-- Could NOT find Threads (missing:  Threads_FOUND) 
-- Configuring done
-- Generating done
-- Build files have been written to: /home/david/src/bitmonero/build/release
cd build/release && make
make[1]: Entering directory '/home/david/src/bitmonero/build/release'
make[2]: Entering directory '/home/david/src/bitmonero/build/release'
make[3]: Entering directory '/home/david/src/bitmonero/build/release'
Scanning dependencies of target version
make[3]: Leaving directory '/home/david/src/bitmonero/build/release'
make[3]: Entering directory '/home/david/src/bitmonero/build/release'
fatal: No names found, cannot describe anything.
CMake Warning at src/version.cmake:3 (message):
  Cannot determine current revision.  Make sure that you are building either
  from a Git working tree or from a source archive.


make[3]: Leaving directory '/home/david/src/bitmonero/build/release'
[  0%] Built target version
make[3]: Entering directory '/home/david/src/bitmonero/build/release'
Scanning dependencies of target upnpc-static
make[3]: Leaving directory '/home/david/src/bitmonero/build/release'
make[3]: Entering directory '/home/david/src/bitmonero/build/release'
[  1%] Building C object external/miniupnpc/CMakeFiles/upnpc-static.dir/igd_desc_parse.c.o
[  2%] Building C object external/miniupnpc/CMakeFiles/upnpc-static.dir/miniupnpc.c.o
[  3%] Building C object external/miniupnpc/CMakeFiles/upnpc-static.dir/minixml.c.o
[  4%] Building C object external/miniupnpc/CMakeFiles/upnpc-static.dir/minisoap.c.o
[  5%] Building C object external/miniupnpc/CMakeFiles/upnpc-static.dir/miniwget.c.o
[  6%] Building C object external/miniupnpc/CMakeFiles/upnpc-static.dir/upnpc.c.o
[  7%] Building C object external/miniupnpc/CMakeFiles/upnpc-static.dir/upnpcommands.c.o
[  8%] Building C object external/miniupnpc/CMakeFiles/upnpc-static.dir/upnpreplyparse.c.o
[  9%] Building C object external/miniupnpc/CMakeFiles/upnpc-static.dir/upnperrors.c.o
[ 10%] Building C object external/miniupnpc/CMakeFiles/upnpc-static.dir/connecthostport.c.o
[ 11%] Building C object external/miniupnpc/CMakeFiles/upnpc-static.dir/portlistingparse.c.o
[ 12%] Building C object external/miniupnpc/CMakeFiles/upnpc-static.dir/receivedata.c.o
[ 13%] Building C object external/miniupnpc/CMakeFiles/upnpc-static.dir/minissdpc.c.o
Linking C static library libminiupnpc.a
make[3]: Leaving directory '/home/david/src/bitmonero/build/release'
[ 13%] Built target upnpc-static
make[3]: Entering directory '/home/david/src/bitmonero/build/release'
Scanning dependencies of target common
make[3]: Leaving directory '/home/david/src/bitmonero/build/release'
make[3]: Entering directory '/home/david/src/bitmonero/build/release'
[ 14%] Building CXX object src/CMakeFiles/common.dir/common/base58.cpp.o
[ 15%] Building CXX object src/CMakeFiles/common.dir/common/command_line.cpp.o
[ 16%] Building CXX object src/CMakeFiles/common.dir/common/util.cpp.o
Linking CXX static library libcommon.a
make[3]: Leaving directory '/home/david/src/bitmonero/build/release'
[ 16%] Built target common
make[3]: Entering directory '/home/david/src/bitmonero/build/release'
Scanning dependencies of target cryptonote_core
make[3]: Leaving directory '/home/david/src/bitmonero/build/release'
make[3]: Entering directory '/home/david/src/bitmonero/build/release'
[ 17%] Building CXX object src/CMakeFiles/cryptonote_core.dir/cryptonote_core/checkpoints.cpp.o
[ 18%] Building CXX object src/CMakeFiles/cryptonote_core.dir/cryptonote_core/blockchain_storage.cpp.o
[ 19%] Building CXX object src/CMakeFiles/cryptonote_core.dir/cryptonote_core/difficulty.cpp.o
[ 20%] Building CXX object src/CMakeFiles/cryptonote_core.dir/cryptonote_core/cryptonote_format_utils.cpp.o
[ 21%] Building CXX object src/CMakeFiles/cryptonote_core.dir/cryptonote_core/miner.cpp.o
[ 22%] Building CXX object src/CMakeFiles/cryptonote_core.dir/cryptonote_core/account.cpp.o
[ 23%] Building CXX object src/CMakeFiles/cryptonote_core.dir/cryptonote_core/cryptonote_core.cpp.o
[ 24%] Building CXX object src/CMakeFiles/cryptonote_core.dir/cryptonote_core/cryptonote_basic_impl.cpp.o
[ 25%] Building CXX object src/CMakeFiles/cryptonote_core.dir/cryptonote_core/tx_pool.cpp.o
Linking CXX static library libcryptonote_core.a
make[3]: Leaving directory '/home/david/src/bitmonero/build/release'
[ 25%] Built target cryptonote_core
make[3]: Entering directory '/home/david/src/bitmonero/build/release'
Scanning dependencies of target crypto
make[3]: Leaving directory '/home/david/src/bitmonero/build/release'
make[3]: Entering directory '/home/david/src/bitmonero/build/release'
[ 26%] Building C object src/CMakeFiles/crypto.dir/crypto/crypto-ops.c.o
[ 27%] Building C object src/CMakeFiles/crypto.dir/crypto/random.c.o
[ 28%] Building C object src/CMakeFiles/crypto.dir/crypto/slow-hash.c.o
/home/david/src/bitmonero/src/crypto/slow-hash.c: In function ‘cn_slow_hash’:
/home/david/src/bitmonero/src/crypto/slow-hash.c:199:5: warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]
     U64(a)[0] = U64(&state.k[0])[0] ^ U64(&state.k[32])[0];
     ^
/home/david/src/bitmonero/src/crypto/slow-hash.c:199:5: warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]
/home/david/src/bitmonero/src/crypto/slow-hash.c:199:5: warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]
/home/david/src/bitmonero/src/crypto/slow-hash.c:200:5: warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]
     U64(a)[1] = U64(&state.k[0])[1] ^ U64(&state.k[32])[1];
     ^
/home/david/src/bitmonero/src/crypto/slow-hash.c:200:5: warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]
/home/david/src/bitmonero/src/crypto/slow-hash.c:201:5: warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]
     U64(b)[0] = U64(&state.k[16])[0] ^ U64(&state.k[48])[0];
     ^
/home/david/src/bitmonero/src/crypto/slow-hash.c:201:5: warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]
/home/david/src/bitmonero/src/crypto/slow-hash.c:201:5: warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]
/home/david/src/bitmonero/src/crypto/slow-hash.c:202:5: warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]
     U64(b)[1] = U64(&state.k[16])[1] ^ U64(&state.k[48])[1];
     ^
/home/david/src/bitmonero/src/crypto/slow-hash.c:202:5: warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]
/home/david/src/bitmonero/src/crypto/slow-hash.c:210:9: warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]
         p = &long_state[state_index(a)];
         ^
/home/david/src/bitmonero/src/crypto/slow-hash.c:222:9: warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]
         p = &long_state[state_index(a)];
         ^
[ 29%] Building C object src/CMakeFiles/crypto.dir/crypto/hash.c.o
[ 30%] Building C object src/CMakeFiles/crypto.dir/crypto/keccak.c.o
[ 31%] Building C object src/CMakeFiles/crypto.dir/crypto/aesb.c.o
[ 32%] Building C object src/CMakeFiles/crypto.dir/crypto/crypto-ops-data.c.o
[ 33%] Building CXX object src/CMakeFiles/crypto.dir/crypto/crypto.cpp.o
[ 34%] Building C object src/CMakeFiles/crypto.dir/crypto/hash-extra-jh.c.o
[ 35%] Building C object src/CMakeFiles/crypto.dir/crypto/tree-hash.c.o
[ 36%] Building C object src/CMakeFiles/crypto.dir/crypto/oaes_lib.c.o
[ 37%] Building C object src/CMakeFiles/crypto.dir/crypto/blake256.c.o
[ 38%] Building C object src/CMakeFiles/crypto.dir/crypto/hash-extra-groestl.c.o
[ 39%] Building C object src/CMakeFiles/crypto.dir/crypto/jh.c.o
[ 40%] Building C object src/CMakeFiles/crypto.dir/crypto/hash-extra-skein.c.o
[ 41%] Building C object src/CMakeFiles/crypto.dir/crypto/groestl.c.o
/home/david/src/bitmonero/src/crypto/groestl.c: In function ‘Init’:
/home/david/src/bitmonero/src/crypto/groestl.c:210:9: warning: comparison between signed and unsigned integer expressions [-Wsign-compare]
   for(;i<(SIZE512/sizeof(uint32_t));i++)
         ^
[ 42%] Building C object src/CMakeFiles/crypto.dir/crypto/chacha8.c.o
[ 43%] Building C object src/CMakeFiles/crypto.dir/crypto/hash-extra-blake.c.o
[ 44%] Building C object src/CMakeFiles/crypto.dir/crypto/skein.c.o
/home/david/src/bitmonero/src/crypto/skein.c:80:5: warning: "SKEIN_256_NIST_MAX_HASH_BITS" is not defined [-Wundef]
 #if SKEIN_256_NIST_MAX_HASH_BITS
     ^
/home/david/src/bitmonero/src/crypto/skein.c: In function ‘Skein_256_Final’:
/home/david/src/bitmonero/src/crypto/skein.c:1360:9: warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]
         ((u64b_t *)ctx->b)[0]= Skein_Swap64((u64b_t) i); /* build the counter block */
         ^
/home/david/src/bitmonero/src/crypto/skein.c: In function ‘Skein_512_Final’:
/home/david/src/bitmonero/src/crypto/skein.c:1560:9: warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]
         ((u64b_t *)ctx->b)[0]= Skein_Swap64((u64b_t) i); /* build the counter block */
         ^
/home/david/src/bitmonero/src/crypto/skein.c: In function ‘Skein1024_Final’:
/home/david/src/bitmonero/src/crypto/skein.c:1758:9: warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]
         ((u64b_t *)ctx->b)[0]= Skein_Swap64((u64b_t) i); /* build the counter block */
         ^
/home/david/src/bitmonero/src/crypto/skein.c: In function ‘Init’:
/home/david/src/bitmonero/src/crypto/skein.c:1944:5: warning: "SKEIN_256_NIST_MAX_HASH_BITS" is not defined [-Wundef]
 #if SKEIN_256_NIST_MAX_HASH_BITS
     ^
[ 45%] Building CXX object src/CMakeFiles/crypto.dir/crypto/electrum-words.cpp.o
Linking CXX static library libcrypto.a
make[3]: Leaving directory '/home/david/src/bitmonero/build/release'
[ 45%] Built target crypto
make[3]: Entering directory '/home/david/src/bitmonero/build/release'
Scanning dependencies of target connectivity_tool
make[3]: Leaving directory '/home/david/src/bitmonero/build/release'
make[3]: Entering directory '/home/david/src/bitmonero/build/release'
[ 46%] Building CXX object src/CMakeFiles/connectivity_tool.dir/connectivity_tool/conn_tool.cpp.o
Linking CXX executable connectivity_tool
/tmp/cc1Hj3sj.ltrans18.ltrans.o: In function `handle_request_stat(boost::program_options::variables_map&, unsigned long)':
cc1Hj3sj.ltrans18.o:(.text+0xe7e): undefined reference to `crypto::crypto_ops::generate_signature(crypto::hash const&, crypto::public_key const&, crypto::secret_key const&, crypto::signature&)'
cc1Hj3sj.ltrans18.o:(.text+0x1273): undefined reference to `crypto::crypto_ops::generate_signature(crypto::hash const&, crypto::public_key const&, crypto::secret_key const&, crypto::signature&)'
/tmp/cc1Hj3sj.ltrans27.ltrans.o: In function `tools::get_proof_of_trust_hash(nodetool::proof_of_trust const&)':
cc1Hj3sj.ltrans27.o:(.text+0xcf4): undefined reference to `cn_fast_hash'
/tmp/cc1Hj3sj.ltrans29.ltrans.o: In function `generate_and_print_keys()':
cc1Hj3sj.ltrans29.o:(.text+0x49b): undefined reference to `crypto::crypto_ops::generate_keys(crypto::public_key&, crypto::secret_key&, crypto::secret_key const&, bool)'
/tmp/cc1Hj3sj.ltrans29.ltrans.o: In function `main':
cc1Hj3sj.ltrans29.o:(.text.startup+0x1ac): undefined reference to `command_line::arg_help'
cc1Hj3sj.ltrans29.o:(.text.startup+0x6ef): undefined reference to `command_line::arg_help'
collect2: error: ld returned 1 exit status
src/CMakeFiles/connectivity_tool.dir/build.make:96: recipe for target 'src/connectivity_tool' failed
make[3]: *** [src/connectivity_tool] Error 1
make[3]: Leaving directory '/home/david/src/bitmonero/build/release'
CMakeFiles/Makefile2:228: recipe for target 'src/CMakeFiles/connectivity_tool.dir/all' failed
make[2]: *** [src/CMakeFiles/connectivity_tool.dir/all] Error 2
make[2]: Leaving directory '/home/david/src/bitmonero/build/release'
Makefile:127: recipe for target 'all' failed
make[1]: *** [all] Error 2
make[1]: Leaving directory '/home/david/src/bitmonero/build/release'
Makefile:20: recipe for target 'build-release' failed
make: *** [build-release] Error 2

```


# Discussion History
## dmp1ce | 2014-06-15T14:39:46+00:00
https://github.com/monero-project/bitmonero/pull/33 solve the build issue for me.


## monero-project | 2014-06-16T17:05:23+00:00
Yup, fixed with #33 and closed.


# Action History
- Created by: dmp1ce | 2014-06-15T13:50:34+00:00
- Closed at: 2014-06-16T17:05:23+00:00
