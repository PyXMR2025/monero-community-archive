---
title: Unable to compile with -DBUILD_SHARED_LIBS=1
source_url: https://github.com/monero-project/monero/issues/1782
author: sammy007
assignees: []
labels: []
created_at: '2017-02-23T22:05:24+00:00'
updated_at: '2017-03-19T21:28:07+00:00'
type: issue
status: closed
closed_at: '2017-03-19T21:28:07+00:00'
---

# Original Description
tag 0.10.2

```
cmake -DBUILD_SHARED_LIBS=1 .
make
```

```
../cryptonote_basic/libcryptonote_basic.so: undefined reference to `cryptonote::BlockchainDB::get_block_from_height(unsigned long const&) const'
collect2: error: ld returned 1 exit status
src/blockchain_utilities/CMakeFiles/cn_deserialize.dir/build.make:116: recipe for target 'bin/monero-utils-deserialize' failed
make[2]: *** [bin/monero-utils-deserialize] Error 1
CMakeFiles/Makefile2:1867: recipe for target 'src/blockchain_utilities/CMakeFiles/cn_deserialize.dir/all' failed
make[1]: *** [src/blockchain_utilities/CMakeFiles/cn_deserialize.dir/all] Error 2
make[1]: *** Waiting for unfinished jobs....
```


# Discussion History
## fluffypony | 2017-02-23T22:14:02+00:00
What platform? Also did you make clean first?

## sammy007 | 2017-02-23T22:36:29+00:00
Oh, sorry, Linux Ubuntu 16 LTS.

## sammy007 | 2017-02-23T22:36:44+00:00
Clean repo clone before compilation.

## moneromooo-monero | 2017-02-23T23:22:28+00:00
Try disabling LTO (-D USE_LTO=OFF in Makefile, or your command line).

## sammy007 | 2017-02-23T23:37:16+00:00
@moneromooo-monero 

```
--- a/CMakeLists.txt
+++ b/CMakeLists.txt
@@ -559,7 +559,7 @@ else()
   endif()

   if(NOT DEFINED USE_LTO_DEFAULT)
-    set(USE_LTO_DEFAULT true)
+    set(USE_LTO_DEFAULT false)
   endif()
   set(USE_LTO ${USE_LTO_DEFAULT} CACHE BOOL "Use Link-Time Optimization (Release mode only)")

@@ -569,6 +569,7 @@ else()
   endif()


+  set(USE_LTO false)
   if(USE_LTO)
     set(RELEASE_FLAGS "${RELEASE_FLAGS} -flto")
     if(STATIC)
```

also tried with `cmake -DUSE_LTO=OFF -DBUILD_SHARED_LIBS=1 .`. All the same.


## moneromooo-monero | 2017-02-24T00:08:39+00:00
Do you have a function definition in src/blockchain_db/blockchain_db.cpp, line 203, like this:

block BlockchainDB::get_block_from_height(const uint64_t& height) const
{
  blobdata bd = get_block_blob_from_height(height);
  block b;
  if (!parse_and_validate_block_from_blob(bd, b))
    throw new DB_ERROR("Failed to parse block from blob retrieved from the db");

  return b;
}


## sammy007 | 2017-02-24T00:10:58+00:00
Sure. I am building 0.10.2 from clean clone.

```c++
block BlockchainDB::get_block_from_height(const uint64_t& height) const
{
  blobdata bd = get_block_blob_from_height(height);
  block b;
  if (!parse_and_validate_block_from_blob(bd, b))
    throw new DB_ERROR("Failed to parse block from blob retrieved from the db");

  return b;
}
```

## moneromooo-monero | 2017-02-24T00:31:06+00:00
Which compiler/linker and versions ?

## sammy007 | 2017-02-24T00:39:39+00:00
g++ (Ubuntu 5.4.0-6ubuntu1~16.04.4) 5.4.0 20160609
GNU ld (GNU Binutils for Ubuntu) 2.26.1


## moneromooo-monero | 2017-02-24T09:02:53+00:00
Does this fix it ? https://github.com/monero-project/monero/pull/1794

## sammy007 | 2017-02-24T16:57:15+00:00
Nope.

```
[ 93%] Linking CXX executable ../../bin/monero-blockchain-import
../cryptonote_basic/libcryptonote_basic.so: undefined reference to `cryptonote::BlockchainDB::get_block_from_height(unsigned long const&) const'
collect2: error: ld returned 1 exit status
src/blockchain_utilities/CMakeFiles/cn_deserialize.dir/build.make:116: recipe for target 'bin/monero-utils-deserialize' failed
make[2]: *** [bin/monero-utils-deserialize] Error 1
CMakeFiles/Makefile2:1867: recipe for target 'src/blockchain_utilities/CMakeFiles/cn_deserialize.dir/all' failed
make[1]: *** [src/blockchain_utilities/CMakeFiles/cn_deserialize.dir/all] Error 2
make[1]: *** Waiting for unfinished jobs....
[ 93%] Linking CXX executable ../../bin/monero-blockchain-export
```

## hyc | 2017-02-24T18:16:39+00:00
The error message is clearly complaining about undefined symbols in the shared library, so addoing blockchain_db to various executables will do nothing to address this. Apparently MacOS is like Windows and doesn't like shared libraries with undefined symbols. (By the way, that means this ought to also be broken on Windows right now.)

But again, why are we supporting building Monero internal libraries as shared libraries in the first place? You can't securely deploy an app using such shared libraries.

Hm, I thought this ticket was against MacOS but it's against Ubuntu. Still the other question holds.

## sammy007 | 2017-02-24T18:20:42+00:00
I found this feature and using it in https://github.com/sammy007/monero-stratum to link with crypto libs and avoid copy pasting of whole `crypto` and `cryptonote_utils`, this is useful, why not keep it?

## moneromooo-monero | 2017-02-24T19:14:24+00:00
It's at link time for the executable, so it seems likely that adding the lib to the executable line line will alow the compiler to find the symbol, whether required by a dependent lib, or the binary itself, no ?

## Jaqueeee | 2017-02-25T14:44:36+00:00
I have the same problem on osx when building debug build. 
https://github.com/monero-project/monero/issues/1792

## sammy007 | 2017-03-02T06:59:21+00:00
@moneromooo-monero crossdep fixes issue, thanks a lot.

## kenshi84 | 2017-03-09T06:26:24+00:00
Given Issue #1851, it's surprising to me that PR #1804 solved this issue. @sammy007 Can you confirm?

I created another [patch](https://github.com/monero-project/monero/files/829486/diff_virtual.txt) for this - could you please try this by doing
```
git apply diff_virtual.txt
```
from the project root on the latest master b67877af6f7192a302453e542c266a5cfc3182a7?

## sammy007 | 2017-03-10T02:41:42+00:00
It compiles with your patch on https://github.com/monero-project/monero/commit/b67877af6f7192a302453e542c266a5cfc3182a7 @kenshi84 

## kenshi84 | 2017-03-17T02:39:15+00:00
Could you please close this issue which was solved by #1853?

# Action History
- Created by: sammy007 | 2017-02-23T22:05:24+00:00
- Closed at: 2017-03-19T21:28:07+00:00
