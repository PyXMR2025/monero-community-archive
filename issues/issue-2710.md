---
title: 'OSX: library not found for -lssl'
source_url: https://github.com/monero-project/monero/issues/2710
author: danrmiller
assignees: []
labels:
- cmake
created_at: '2017-10-23T00:49:19+00:00'
updated_at: '2017-10-30T19:27:43+00:00'
type: issue
status: closed
closed_at: '2017-10-30T19:27:43+00:00'
---

# Original Description
I don't know if I need to set an environment variable. You can see the VERBOSE=1 output [here](https://build.getmonero.org/builders/monero-static-osx-10.12/builds/2532/steps/compile/logs/stdio), and the same line that is erroring with -lssl also knows libssl is at /usr/local/opt/openssl/lib/libssl.a

```
[ 91%] Linking CXX executable ../../bin/monero-wallet-rpc
cd /Users/buildbot/slave/monero-static-osx-10_12/build/build/release/src/wallet && /usr/local/Cellar/cmake/3.8.2/bin/cmake -E cmake_link_script CMakeFiles/wallet_rpc_server.dir/link.txt --verbose=1
/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++   -DZMQ_STATIC -fno-strict-aliasing -maes -std=c++11 -D_GNU_SOURCE   -Wall -Wextra -Wpointer-arith -Wundef -Wvla -Wwrite-strings -Wno-error=extra -Wno-error=deprecated-declarations -Wno-unused-parameter -Wno-unused-variable -Wno-error=unused-variable -Wno-error=undef -Wno-error=uninitialized -Wno-reorder -Wno-missing-field-initializers -march=x86-64   -fno-strict-aliasing -DGTEST_HAS_TR1_TUPLE=0 -DNDEBUG -Ofast  -isysroot /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.12.sdk -Wl,-search_paths_first -Wl,-headerpad_max_install_names    CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o  -o ../../bin/monero-wallet-rpc ../../lib/libwallet.a ../../contrib/epee/src/libepee.a ../rpc/librpc.a ../cryptonote_core/libcryptonote_core.a ../crypto/libcncrypto.a ../common/libcommon.a ../libversion.a /usr/local/lib/libboost_chrono.a /usr/local/lib/libboost_program_options.a /usr/local/lib/libboost_filesystem.a /usr/local/lib/libboost_thread-mt.a ../mnemonics/libmnemonics.a ../blockchain_db/libblockchain_db.a ../../external/db_drivers/liblmdb/liblmdb.a ../ringct/libringct.a ../cryptonote_basic/libcryptonote_basic.a ../checkpoints/libcheckpoints.a /usr/local/lib/libboost_serialization.a -framework IOKit ../blocks/libblocks.a ../common/libcommon.a /usr/local/lib/libboost_date_time.a ../../external/unbound/libunbound.a /usr/local/opt/openssl/lib/libssl.a /usr/local/opt/openssl/lib/libcrypto.a /usr/local/lib/libboost_regex.a ../cryptonote_protocol/libcryptonote_protocol.a ../p2p/libp2p.a ../../contrib/epee/src/libepee.a ../crypto/libcncrypto.a ../../external/easylogging++/libeasylogging.a -lssl -lcrypto ../libversion.a /usr/local/lib/libboost_chrono.a /usr/local/lib/libboost_program_options.a /usr/local/lib/libboost_filesystem.a /usr/local/lib/libboost_thread-mt.a /usr/local/lib/libboost_system.a ../../external/miniupnpc/libminiupnpc.a 
ld: library not found for -lssl
clang: error: linker command failed with exit code 1 (use -v to see invocation)
```



```
```


# Discussion History
## danrmiller | 2017-10-23T04:11:01+00:00
+cmake

## moneromooo-monero | 2017-10-23T09:15:06+00:00
Sounds like https://github.com/monero-project/monero/pull/2663

# Action History
- Created by: danrmiller | 2017-10-23T00:49:19+00:00
- Closed at: 2017-10-30T19:27:43+00:00
