---
title: debian build problem
source_url: https://github.com/monero-project/monero/issues/38
author: zba
assignees: []
labels: []
created_at: '2014-06-13T18:25:38+00:00'
updated_at: '2017-06-12T04:26:31+00:00'
type: issue
status: closed
closed_at: '2014-08-21T09:16:09+00:00'
---

# Original Description
Hi, I having build error.

debian sid

-- The C compiler identification is GNU 4.9.0
-- The CXX compiler identification is GNU 4.9.0
-- Boost version: 1.55.0

>    $ git log  -1 |head -1
>   commit 94cc5a7d718a0dc0efe28af8dfc0955c8525a9a1

branch  **master**

make[1]: Entering directory '/home/user/github/bitmonero'
mkdir -p build/release
cd build/release && cmake -D CMAKE_BUILD_TYPE=Release ../..
-- The C compiler identification is GNU 4.9.0
-- The CXX compiler identification is GNU 4.9.0
-- Check for working C compiler: /usr/lib/ccache/cc
-- Check for working C compiler: /usr/lib/ccache/cc -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working CXX compiler: /usr/lib/ccache/c++
-- Check for working CXX compiler: /usr/lib/ccache/c++ -- works
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
-- Found PythonInterp: /usr/bin/python (found version "2.7.6") 
-- Looking for include file pthread.h
-- Looking for include file pthread.h - not found
-- Could NOT find Threads (missing:  Threads_FOUND) 
-- Configuring done
-- Generating done
-- Build files have been written to: /home/user/github/bitmonero/build/release
cd build/release && make
make[2]: Entering directory '/home/user/github/bitmonero/build/release'
make[3]: Entering directory '/home/user/github/bitmonero/build/release'
make[4]: Entering directory '/home/user/github/bitmonero/build/release'
Scanning dependencies of target version
make[4]: Leaving directory '/home/user/github/bitmonero/build/release'
make[4]: Entering directory '/home/user/github/bitmonero/build/release'
fatal: No names found, cannot describe anything.
CMake Warning at src/version.cmake:3 (message):
  Cannot determine current revision.  Make sure that you are building either
  from a Git working tree or from a source archive.

make[4]: Leaving directory '/home/user/github/bitmonero/build/release'
[  0%] Built target version
make[4]: Entering directory '/home/user/github/bitmonero/build/release'
Scanning dependencies of target upnpc-static
make[4]: Leaving directory '/home/user/github/bitmonero/build/release'
make[4]: Entering directory '/home/user/github/bitmonero/build/release'
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
make[4]: Leaving directory '/home/user/github/bitmonero/build/release'
[ 13%] Built target upnpc-static
make[4]: Entering directory '/home/user/github/bitmonero/build/release'
Scanning dependencies of target common
make[4]: Leaving directory '/home/user/github/bitmonero/build/release'
make[4]: Entering directory '/home/user/github/bitmonero/build/release'
[ 14%] Building CXX object src/CMakeFiles/common.dir/common/base58.cpp.o
[ 15%] Building CXX object src/CMakeFiles/common.dir/common/util.cpp.o  
[ 16%] Building CXX object src/CMakeFiles/common.dir/common/command_line.cpp.o  
Linking CXX static library libcommon.a
make[4]: Leaving directory '/home/user/github/bitmonero/build/release'
[ 16%] Built target common
make[4]: Entering directory '/home/user/github/bitmonero/build/release'
Scanning dependencies of target cryptonote_core
make[4]: Leaving directory '/home/user/github/bitmonero/build/release'
make[4]: Entering directory '/home/user/github/bitmonero/build/release'
[ 17%] Building CXX object src/CMakeFiles/cryptonote_core.dir/cryptonote_core/blockchain_storage.cpp.o
[ 18%] Building CXX object src/CMakeFiles/cryptonote_core.dir/cryptonote_core/checkpoints.cpp.o  
[ 19%] Building CXX object src/CMakeFiles/cryptonote_core.dir/cryptonote_core/cryptonote_basic_impl.cpp.o  
[ 20%] Building CXX object src/CMakeFiles/cryptonote_core.dir/cryptonote_core/cryptonote_format_utils.cpp.o  
[ 21%] Building CXX object src/CMakeFiles/cryptonote_core.dir/cryptonote_core/difficulty.cpp.o  
[ 22%] Building CXX object src/CMakeFiles/cryptonote_core.dir/cryptonote_core/tx_pool.cpp.o  
[ 23%] Building CXX object src/CMakeFiles/cryptonote_core.dir/cryptonote_core/account.cpp.o  
[ 24%] Building CXX object src/CMakeFiles/cryptonote_core.dir/cryptonote_core/cryptonote_core.cpp.o  
[ 25%] Building CXX object src/CMakeFiles/cryptonote_core.dir/cryptonote_core/miner.cpp.o  
Linking CXX static library libcryptonote_core.a
make[4]: Leaving directory '/home/user/github/bitmonero/build/release'
[ 25%] Built target cryptonote_core
make[4]: Entering directory '/home/user/github/bitmonero/build/release'
Scanning dependencies of target crypto
make[4]: Leaving directory '/home/user/github/bitmonero/build/release'
make[4]: Entering directory '/home/user/github/bitmonero/build/release'
[ 26%] Building C object src/CMakeFiles/crypto.dir/crypto/aesb.c.o
[ 27%] Building C object src/CMakeFiles/crypto.dir/crypto/blake256.c.o  
[ 28%] Building C object src/CMakeFiles/crypto.dir/crypto/chacha8.c.o  
[ 29%] Building C object src/CMakeFiles/crypto.dir/crypto/crypto-ops-data.c.o  
[ 30%] Building C object src/CMakeFiles/crypto.dir/crypto/crypto-ops.c.o  
[ 31%] Building C object src/CMakeFiles/crypto.dir/crypto/groestl.c.o  
/home/user/github/bitmonero/src/crypto/groestl.c: In function ‘Init’:
/home/user/github/bitmonero/src/crypto/groestl.c:210:9: warning: comparison between signed and unsigned integer expressions [-Wsign-compare]
   for(;i<(SIZE512/sizeof(uint32_t));i++)
         ^
[ 32%] Building C object src/CMakeFiles/crypto.dir/crypto/hash-extra-blake.c.o
[ 33%] Building C object src/CMakeFiles/crypto.dir/crypto/hash-extra-groestl.c.o  
[ 34%] Building C object src/CMakeFiles/crypto.dir/crypto/hash-extra-jh.c.o  
[ 35%] Building C object src/CMakeFiles/crypto.dir/crypto/hash-extra-skein.c.o  
[ 36%] Building C object src/CMakeFiles/crypto.dir/crypto/hash.c.o  
[ 37%] Building C object src/CMakeFiles/crypto.dir/crypto/jh.c.o  
[ 38%] Building C object src/CMakeFiles/crypto.dir/crypto/keccak.c.o  
[ 39%] Building C object src/CMakeFiles/crypto.dir/crypto/oaes_lib.c.o  
[ 40%] Building C object src/CMakeFiles/crypto.dir/crypto/random.c.o  
[ 41%] Building C object src/CMakeFiles/crypto.dir/crypto/skein.c.o  
/home/user/github/bitmonero/src/crypto/skein.c:80:5: warning: "SKEIN_256_NIST_MAX_HASH_BITS" is not defined [-Wundef]
 #if SKEIN_256_NIST_MAX_HASH_BITS
     ^
/home/user/github/bitmonero/src/crypto/skein.c:1944:5: warning: "SKEIN_256_NIST_MAX_HASH_BITS" is not defined [-Wundef]
 #if SKEIN_256_NIST_MAX_HASH_BITS
     ^
/home/user/github/bitmonero/src/crypto/skein.c: In function ‘Skein_256_Final’:
/home/user/github/bitmonero/src/crypto/skein.c:1360:9: warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing](%28u64b_t *%29ctx->b)[0]= Skein_Swap64((u64b_t) i); /\* build the counter block _/
         ^
/home/user/github/bitmonero/src/crypto/skein.c: In function ‘Skein_512_Final’:
/home/user/github/bitmonero/src/crypto/skein.c:1560:9: warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing](%28u64b_t *%29ctx->b)[0]= Skein_Swap64((u64b_t) i); /_ build the counter block _/
         ^
/home/user/github/bitmonero/src/crypto/skein.c: In function ‘Skein1024_Final’:
/home/user/github/bitmonero/src/crypto/skein.c:1758:9: warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing](%28u64b_t *%29ctx->b)[0]= Skein_Swap64((u64b_t) i); /_ build the counter block _/
         ^
[ 42%] Building C object src/CMakeFiles/crypto.dir/crypto/slow-hash.c.o
/home/user/github/bitmonero/src/crypto/slow-hash.c: In function ‘cn_slow_hash’:
/home/user/github/bitmonero/src/crypto/slow-hash.c:199:5: warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]
     U64(a)[0] = U64(&state.k[0])[0] ^ U64(&state.k[32])[0];
     ^
/home/user/github/bitmonero/src/crypto/slow-hash.c:199:5: warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]
/home/user/github/bitmonero/src/crypto/slow-hash.c:199:5: warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]
/home/user/github/bitmonero/src/crypto/slow-hash.c:200:5: warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]
     U64(a)[1] = U64(&state.k[0])[1] ^ U64(&state.k[32])[1];
     ^
/home/user/github/bitmonero/src/crypto/slow-hash.c:200:5: warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]
/home/user/github/bitmonero/src/crypto/slow-hash.c:201:5: warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]
     U64(b)[0] = U64(&state.k[16])[0] ^ U64(&state.k[48])[0];
     ^
/home/user/github/bitmonero/src/crypto/slow-hash.c:201:5: warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]
/home/user/github/bitmonero/src/crypto/slow-hash.c:201:5: warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]
/home/user/github/bitmonero/src/crypto/slow-hash.c:202:5: warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]
     U64(b)[1] = U64(&state.k[16])[1] ^ U64(&state.k[48])[1];
     ^
/home/user/github/bitmonero/src/crypto/slow-hash.c:202:5: warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]
/home/user/github/bitmonero/src/crypto/slow-hash.c:210:9: warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]
         p = &long_state[state_index(a)];
         ^
/home/user/github/bitmonero/src/crypto/slow-hash.c:222:9: warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]
         p = &long_state[state_index(a)];
         ^
[ 43%] Building C object src/CMakeFiles/crypto.dir/crypto/tree-hash.c.o
[ 44%] Building CXX object src/CMakeFiles/crypto.dir/crypto/crypto.cpp.o  
[ 45%] Building CXX object src/CMakeFiles/crypto.dir/crypto/electrum-words.cpp.o  
Linking CXX static library libcrypto.a
make[4]: Leaving directory '/home/user/github/bitmonero/build/release'
[ 45%] Built target crypto
make[4]: Entering directory '/home/user/github/bitmonero/build/release'
Scanning dependencies of target connectivity_tool
make[4]: Leaving directory '/home/user/github/bitmonero/build/release'
make[4]: Entering directory '/home/user/github/bitmonero/build/release'
[ 46%] Building CXX object src/CMakeFiles/connectivity_tool.dir/connectivity_tool/conn_tool.cpp.o
Linking CXX executable connectivity_tool
/tmp/cccRSnOo.ltrans21.ltrans.o: In function `generate_signature':
/home/user/github/bitmonero/src/crypto/crypto.h:142: undefined reference to`crypto::crypto_ops::generate_signature(crypto::hash const&, crypto::public_key const&, crypto::secret_key const&, crypto::signature&)'
/home/user/github/bitmonero/src/crypto/crypto.h:142: undefined reference to `crypto::crypto_ops::generate_signature(crypto::hash const&, crypto::public_key const&, crypto::secret_key const&, crypto::signature&)'
/tmp/cccRSnOo.ltrans27.ltrans.o: In function`cn_fast_hash':
/home/user/github/bitmonero/src/crypto/hash.h:36: undefined reference to `cn_fast_hash'
/tmp/cccRSnOo.ltrans29.ltrans.o: In function`generate_keys':
/home/user/github/bitmonero/src/crypto/crypto.h:106: undefined reference to `crypto::crypto_ops::generate_keys(crypto::public_key&, crypto::secret_key&, crypto::secret_key const&, bool)'
/tmp/cccRSnOo.ltrans29.ltrans.o: In function`main':
/home/user/github/bitmonero/src/connectivity_tool/conn_tool.cpp:297: undefined reference to `command_line::arg_help'
/tmp/cccRSnOo.ltrans29.ltrans.o: In function`operator()':
/home/user/github/bitmonero/src/connectivity_tool/conn_tool.cpp:319: undefined reference to `command_line::arg_help'
collect2: error: ld returned 1 exit status
src/CMakeFiles/connectivity_tool.dir/build.make:100: recipe for target 'src/connectivity_tool' failed
make[4]: *_\* [src/connectivity_tool] Error 1
make[4]: Leaving directory '/home/user/github/bitmonero/build/release'
CMakeFiles/Makefile2:231: recipe for target 'src/CMakeFiles/connectivity_tool.dir/all' failed
make[3]: **\* [src/CMakeFiles/connectivity_tool.dir/all] Error 2
make[3]: Leaving directory '/home/user/github/bitmonero/build/release'
Makefile:126: recipe for target 'all' failed
make[2]: **\* [all] Error 2
make[2]: Leaving directory '/home/user/github/bitmonero/build/release'
Makefile:20: recipe for target 'build-release' failed
make[1]: **\* [build-release] Error 2
make[1]: Leaving directory '/home/user/github/bitmonero'


# Discussion History
## mikezackles | 2014-06-13T18:38:02+00:00
This might be a fix: mikezackles/bitmonero@c8626dff3fedd86cf697e49aec00c9e17c9015d8


## zba | 2014-06-13T18:41:17+00:00
@mikezackles  thanks already trying. 


## zba | 2014-06-13T18:45:09+00:00
It helped, but i just not lucky today :)

Linking CXX executable bitmonerod
lto1: internal compiler error: Segmentation fault


## zba | 2014-06-13T19:05:55+00:00
@mikezackles may be it will be usefull for you, tried with gcc-4.7 mikezackles/bitmonero@c8626df

got the error

```
 Linking CXX executable connectivity_tool
 /usr/bin/ld.bfd.real: /tmp/ccaCM9hE.ltrans0.ltrans.o: undefined reference to symbol '__cxa_free_exception@@CXXABI_1.3'
 //usr/lib/x86_64-linux-gnu/libstdc++.so.6: error adding symbols: DSO missing from command line
 collect2: error: ld returned 1 exit status
  src/CMakeFiles/connectivity_tool.dir/build.make:100: recipe for target 'src/connectivity_tool' failed
  make[4]: *** [src/connectivity_tool] Error 1
```

will try same with master branch


## mikezackles | 2014-06-13T19:22:27+00:00
Just a guess, but that last one sounds like it can't find libstdc++.  Is it installed?


## zba | 2014-06-13T19:50:38+00:00
seems yes, 

$ apt-cache policy libstdc++6-4.7-dev 
libstdc++6-4.7-dev:
  Installed: 4.7.3-14
  Candidate: 4.7.3-14

I also tried with 4.8 - same error 

$ apt-cache policy libstdc++-4.8-dev 
libstdc++-4.8-dev:
  Installed: 4.8.3-3
  Candidate: 4.8.3-3

however 

$ apt-cache policy libstdc++6
libstdc++6:
  Installed: 4.9.0-6
  Candidate: 4.9.0-6

I not sure, may be it is incompatible somehow... I not c++ programmer to guess it.


## fluffypony | 2014-08-02T09:24:31+00:00
@zba what Debian version are you running? And 32 bit / 64 bit? We're busy putting together a platform list to get compilation working on everything.


## zba | 2014-08-04T04:05:12+00:00
@fluffypony 
I tryed current sid would to try again, because it passed some time. amd64 architecture.

On stable it is impossible to build current HEAD because 

> Detected version of Boost is too old.  Requested version was 1.53 (or
>   newer).

stable has 1.49


## zba | 2014-08-04T05:05:18+00:00
I tested with debian sid, - it builds fine now, testting with debian-test


## zba | 2014-08-04T06:11:47+00:00
done build on current testing


## fluffypony | 2014-08-21T09:16:09+00:00
Fixed by using boost >= 1.53 (somewhat problematic for older operating systems that use binary packages, but in those cases boost should be built from source)


## eightsixeight | 2015-04-26T15:51:21+00:00
thanks fluffy , any idea on how to force the corect boost dir ?


## fluffypony | 2015-04-26T16:02:54+00:00
@Fcases I'm pretty sure CMake's FindBoost will find the highest installed version, as long as you actually have installed Boost.


## eightsixeight | 2015-04-26T16:03:44+00:00
:~/boost_1_58_0# ./b2 --with=all cxxflags="-std=c++11" --target=shared,static install
is what im using to install you in monero-dev ?


## ghost | 2017-06-07T17:02:09+00:00
FYI, this is still an issue. Boost 1.58, latest CMake and GCC 5.4. I tried many of the fixes that were pointed out in this branch and in other forked ones, but none work.

## danrmiller | 2017-06-12T04:26:31+00:00
I would make a new issue with the exact error output you get now, since this closed issue is several years old.

# Action History
- Created by: zba | 2014-06-13T18:25:38+00:00
- Closed at: 2014-08-21T09:16:09+00:00
