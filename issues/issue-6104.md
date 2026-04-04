---
title: '[RELEASE] ios build fails on release-v0.15 branch'
source_url: https://github.com/monero-project/monero/issues/6104
author: naughtyfox
assignees: []
labels: []
created_at: '2019-11-06T10:32:26+00:00'
updated_at: '2020-01-12T02:11:42+00:00'
type: issue
status: closed
closed_at: '2020-01-12T02:11:42+00:00'
---

# Original Description
Hi! I'm trying to build `release-v0.15` branch for ios, but I get the following error:
```
CMake Error at src/wallet/CMakeLists.txt:142 (add_library):
  Error evaluating generator expression:

    $<TARGET_OBJECTS:obj_rpc_base>

  Objects of target "obj_rpc_base" referenced but no such target exists.


CMake Error at src/wallet/CMakeLists.txt:142 (add_library):
  No SOURCES given to target: wallet_merged
```

I think the problem is caused be this condition - https://github.com/monero-project/monero/blob/69c488a479609df2838c14cd0cf500242758f449/src/CMakeLists.txt#L120-L123

but it's required in https://github.com/monero-project/monero/blob/69c488a479609df2838c14cd0cf500242758f449/src/wallet/CMakeLists.txt#L61-L63

and used in cycle https://github.com/monero-project/monero/blob/69c488a479609df2838c14cd0cf500242758f449/src/wallet/CMakeLists.txt#L139-L141

# Discussion History
## moneromooo-monero | 2019-11-06T11:30:39+00:00
Does this help ?

```
diff --git a/src/CMakeLists.txt b/src/CMakeLists.txt
index df7f3407f..dbd890247 100644
--- a/src/CMakeLists.txt
+++ b/src/CMakeLists.txt
@@ -119,8 +119,8 @@ if(NOT IOS)
   add_subdirectory(blockchain_db)
 endif()
 add_subdirectory(mnemonics)
+add_subdirectory(rpc)
 if(NOT IOS)
-  add_subdirectory(rpc)
   add_subdirectory(serialization)
 endif()
 add_subdirectory(wallet)
diff --git a/src/rpc/CMakeLists.txt b/src/rpc/CMakeLists.txt
index ebb1e767f..ee330eb02 100644
--- a/src/rpc/CMakeLists.txt
+++ b/src/rpc/CMakeLists.txt
@@ -83,12 +83,13 @@ monero_private_headers(rpc
 monero_private_headers(daemon_rpc_server
   ${daemon_rpc_server_private_headers})
 
-
 monero_add_library(rpc_base
   ${rpc_base_sources}
   ${rpc_base_headers}
   ${rpc_base_private_headers})
 
+if(NOT IOS)
+
 monero_add_library(rpc
   ${rpc_sources}
   ${rpc_headers}
@@ -104,6 +105,8 @@ monero_add_library(daemon_rpc_server
   ${daemon_rpc_server_headers}
   ${daemon_rpc_server_private_headers})
 
+endif()
+
 
 target_link_libraries(rpc_base
   PUBLIC
@@ -115,6 +118,8 @@ target_link_libraries(rpc_base
   PRIVATE
     ${EXTRA_LIBRARIES})
 
+if(NOT IOS)
+
 target_link_libraries(rpc
   PUBLIC
     rpc_base
@@ -152,3 +157,5 @@ target_link_libraries(daemon_rpc_server
     ${EXTRA_LIBRARIES})
 target_include_directories(daemon_rpc_server PUBLIC ${ZMQ_INCLUDE_PATH})
 target_include_directories(obj_daemon_rpc_server PUBLIC ${ZMQ_INCLUDE_PATH})
+
+endif()
```

## naughtyfox | 2019-11-06T11:51:55+00:00
it fails with another error:
```CMake Error at src/wallet/CMakeLists.txt:142 (add_library):
  Error evaluating generator expression:

    $<TARGET_OBJECTS:obj_blockchain_db>

  Objects of target "obj_blockchain_db" referenced but no such target exists.


CMake Error at src/wallet/CMakeLists.txt:142 (add_library):
  No SOURCES given to target: wallet_merged
```

## moneromooo-monero | 2019-11-06T12:14:56+00:00
Try this one instead:

```
diff --git a/src/CMakeLists.txt b/src/CMakeLists.txt
index df7f3407f..2037ec3fa 100644
--- a/src/CMakeLists.txt
+++ b/src/CMakeLists.txt
@@ -115,12 +115,12 @@ add_subdirectory(lmdb)
 add_subdirectory(multisig)
 add_subdirectory(net)
 add_subdirectory(hardforks)
-if(NOT IOS)
+#if(NOT IOS)
   add_subdirectory(blockchain_db)
-endif()
+#endif()
 add_subdirectory(mnemonics)
+add_subdirectory(rpc)
 if(NOT IOS)
-  add_subdirectory(rpc)
   add_subdirectory(serialization)
 endif()
 add_subdirectory(wallet)
diff --git a/src/rpc/CMakeLists.txt b/src/rpc/CMakeLists.txt
index ebb1e767f..ee330eb02 100644
--- a/src/rpc/CMakeLists.txt
+++ b/src/rpc/CMakeLists.txt
@@ -83,12 +83,13 @@ monero_private_headers(rpc
 monero_private_headers(daemon_rpc_server
   ${daemon_rpc_server_private_headers})
 
-
 monero_add_library(rpc_base
   ${rpc_base_sources}
   ${rpc_base_headers}
   ${rpc_base_private_headers})
 
+if(NOT IOS)
+
 monero_add_library(rpc
   ${rpc_sources}
   ${rpc_headers}
@@ -104,6 +105,8 @@ monero_add_library(daemon_rpc_server
   ${daemon_rpc_server_headers}
   ${daemon_rpc_server_private_headers})
 
+endif()
+
 
 target_link_libraries(rpc_base
   PUBLIC
@@ -115,6 +118,8 @@ target_link_libraries(rpc_base
   PRIVATE
     ${EXTRA_LIBRARIES})
 
+if(NOT IOS)
+
 target_link_libraries(rpc
   PUBLIC
     rpc_base
@@ -152,3 +157,5 @@ target_link_libraries(daemon_rpc_server
     ${EXTRA_LIBRARIES})
 target_include_directories(daemon_rpc_server PUBLIC ${ZMQ_INCLUDE_PATH})
 target_include_directories(obj_daemon_rpc_server PUBLIC ${ZMQ_INCLUDE_PATH})
+
+endif()
```

Note I have no idea why these are disabled for IOS, so they might be buggy there...

## moneromooo-monero | 2019-11-06T12:15:43+00:00
Actually, try removing blockchain_db from src/wallet/CMakeLists.txt first. It should not need it...

## naughtyfox | 2019-11-06T12:19:35+00:00
I tried your first patch and removed `blockchain_db` from src/wallet/CMakeLists.txt and it started to compile. But not finished yet to report results :)

## naughtyfox | 2019-11-06T12:42:45+00:00
I encountered compile-time error:
```fatal error: 'hidapi/hidapi.h' file not found```
but I think it's another problem. I guess, first patch + removing `blockchain_db` from dependencies works fine. Thank you.

## moneromooo-monero | 2019-11-06T13:06:26+00:00
Thanks, I'll PR once we're sure it works, since rpc might have been taken out because it doesn't work with IOS. So let me know once you've installed hidapi etc.

## naughtyfox | 2019-11-06T15:48:56+00:00
I uninstalled `hidapi` on mac os and the build became successful. Can't say if it functions ok on ios for now, since it some needs time before our guys can test it

## moneromooo-monero | 2019-11-06T16:53:25+00:00
OK, that seems good enough for now, since there's nothing platform specific there, so I'll PR. Thanks for confirming.

## xiphon | 2019-11-06T19:26:49+00:00
@naughtyfox 

could you provide the steps to reproduce it? What command do you run to produce IOS build?

## naughtyfox | 2019-11-07T11:54:52+00:00
@xiphon Sure
```        
cd monero/build/${ARCH} && cmake ${BUILD_FLAGS} -DBOOST_DEBUG=1 -D BOOST_IGNORE_SYSTEM_PATHS=ON -D EMBEDDED_WALLET=ON \
                -D USE_DEVICE_LEDGER=0 -D BUILD_TESTS=OFF -D ARCH=${ARCH} -D STATIC=ON -D BUILD_64=ON \
                -D CMAKE_BUILD_TYPE=${MONERO_BUILD_TYPE} -D IOS=true -D BUILD_TAG="ios" -D BOOST_INCLUDEDIR=${BOOST} \
                -D BOOST_LIBRARYDIR=${BOOST_LIB} -D OPENSSL_ROOT_DIR=${OPENSSL} \
                -D OPENSSL_CRYPTO_LIBRARY=${OPENSSL}/libcrypto.a -D OPENSSL_SSL_LIBRARY=${OPENSSL}/libssl.a \
                -D SODIUM_INCLUDE_PATH=${SODIUM_INCLUDE} \
                -D SODIUM_LIBRARY=${SODIUM_LIB} \
                -D CMAKE_POSITION_INDEPENDENT_CODE:BOOL=true -D EMBEDDED_WALLET=ON ../..    
cd monero/build/${ARCH} && make -j8 wallet_merged epee easylogging lmdb unbound VERBOSE=1



## xiphon | 2019-11-07T12:24:32+00:00
I don't see `BUILD_GUI_DEPS` defined, so it shouldn't pass the following condition 
https://github.com/monero-project/monero/blob/a48ef0a65afd2d89b9a81479f587b5b516a31c9c/src/wallet/CMakeLists.txt#L118


Thus it shouldn't trigger the following error (https://github.com/monero-project/monero/issues/6104#issuecomment-550276242)
```
CMake Error at src/wallet/CMakeLists.txt:142 (add_library):
  No SOURCES given to target: wallet_merged
```



## naughtyfox | 2019-11-07T12:36:20+00:00
`BUILD_GUI_DEPS` is set indirectly by `EMBEDDED_WALLET=ON`. This is my patch.

## naughtyfox | 2019-11-07T12:41:28+00:00
@moneromooo-monero  btw, `blockchain_db` is needed by wallet libraries. This is android build snippet, but it shows the dependency nevertheless:
```
  ../../../../../external-libs/monero/lib/armeabi-v7a/monero/libwallet_merged.a(blockchain.cpp.o):/build/monero/src/cryptonote_core/blockchain.cpp:function cryptonote::Blockchain::init(cryptonote::BlockchainDB*, cryptonote::network_type, bool, cryptonote::test_options const*, boost::multiprecision::number<boost::multiprecision::backends::cpp_int_backend<128u, 128u, (boost::multiprecision::cpp_integer_type)0, (boost::multiprecision::cpp_int_check_type)0, void>, (boost::multiprecision::expression_template_option)0>, std::__ndk1::function<epee::span<unsigned char const> const (cryptonote::network_type)> const&): error: undefined reference to 'cryptonote::BlockchainDB::is_open() const'
```

## xiphon | 2019-11-09T12:49:50+00:00
@naughtyfox 

Please check https://github.com/monero-project/monero/pull/6112 patch

## naughtyfox | 2019-11-11T10:01:07+00:00
the patch looks good for me

# Action History
- Created by: naughtyfox | 2019-11-06T10:32:26+00:00
- Closed at: 2020-01-12T02:11:42+00:00
