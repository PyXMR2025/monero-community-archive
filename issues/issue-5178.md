---
title: '[RELEASE] failed to build current release-v0.13 branch on arm'
source_url: https://github.com/monero-project/monero/issues/5178
author: naughtyfox
assignees: []
labels: []
created_at: '2019-02-21T15:43:30+00:00'
updated_at: '2019-03-06T15:33:52+00:00'
type: issue
status: closed
closed_at: '2019-03-06T15:33:52+00:00'
---

# Original Description
I'm currently trying to build monero libs on `armv7-eabi` from `release-v0.13` branch (head: f96e431a15c510db4511f2ed6fe5ee5ab708a755) and get several errors:
```
[ 53%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/slow-hash.c.o
cd /home/user/src/monero/armv7/src/crypto && /opt/android/tool32/bin/clang -DAUTO_INITIALIZE_EASYLOGGINGPP -DBLOCKCHAIN_DB=DB_LMDB -DBUILD_TAG=android -DDEFAULT_DB_TYPE=\"lmdb\" -DEMBEDDED_WALLET -DFORCE_USE_HEAP=1 -DHAVE_STRPTIME -DMINIUPNP_STATICLIB -DPER_BLOCK_CHECKPOINT -DSTATICLIB -DUSE_DEVICE_LEDGER=0 -I/home/user/src/monero/external/rapidjson/include -I/home/user/src/monero/external/easylogging++ -I/home/user/src/monero/src -I/home/user/src/monero/contrib/epee/include -I/home/user/src/monero/external -I/home/user/src/monero/armv7/openssl-1.0.2n/include -I/home/user/src/monero/armv7/translations -I/home/user/src/monero/external/unbound/libunbound -I/home/user/src/monero/external/db_drivers/liblmdb -isystem /home/user/src/monero/armv7/boost/include -I/home/user/src/monero/armv7/libsodium-android-armv7-eabi/include  -pthread -march=armv7-a -fno-strict-aliasing -std=c11 -D_GNU_SOURCE   -Wall -Wextra -Wpointer-arith -Wundef -Wvla -Wwrite-strings -Wno-error=extra -Wno-error=deprecated-declarations -Wno-unused-parameter -Wno-unused-variable -Wno-error=unused-variable -Wno-error=undef -Wno-error=uninitialized -Wno-user-defined-warnings -Wno-error=inline-asm -Waggregate-return -Wnested-externs -Wold-style-definition -Wstrict-prototypes  -fPIC  -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -Wformat-security -fstack-protector -fstack-protector-strong -fno-strict-aliasing -mfpu=vfp4 -mfloat-abi=softfp -fPIE -DNDEBUG -O2  -fPIC   -Werror -o CMakeFiles/obj_cncrypto.dir/slow-hash.c.o   -c /home/user/src/monero/src/crypto/slow-hash.c
In file included from /home/user/src/monero/src/crypto/slow-hash.c:43:
/home/user/src/monero/src/crypto/CryptonightR_JIT.h:11:69: error: calling convention 'sysv_abi' ignored for this target [-Werror,-Wignored-attributes]
typedef void (*v4_random_math_JIT_func)(uint32_t* r) __attribute__((sysv_abi));
                                                                    ^
/home/user/src/monero/src/crypto/slow-hash.c:1497:5: error: implicit declaration of function 'use_v4_jit' is invalid in C99 [-Werror,-Wimplicit-function-declaration]
    VARIANT4_RANDOM_MATH_INIT();
    ^
/home/user/src/monero/src/crypto/slow-hash.c:270:13: note: expanded from macro 'VARIANT4_RANDOM_MATH_INIT'
  int jit = use_v4_jit(); \
            ^
/home/user/src/monero/src/crypto/slow-hash.c:1497:5: error: this function declaration is not a prototype [-Werror,-Wstrict-prototypes]
/home/user/src/monero/src/crypto/slow-hash.c:270:13: note: expanded from macro 'VARIANT4_RANDOM_MATH_INIT'
  int jit = use_v4_jit(); \
            ^
/home/user/src/monero/src/crypto/slow-hash.c:1497:5: error: use of undeclared identifier 'hp_jitfunc'
/home/user/src/monero/src/crypto/slow-hash.c:278:44: note: expanded from macro 'VARIANT4_RANDOM_MATH_INIT'
      int ret = v4_generate_JIT_code(code, hp_jitfunc, 4096); \
                                           ^
/home/user/src/monero/src/crypto/slow-hash.c:1535:7: error: use of undeclared identifier 'hp_jitfunc'
      VARIANT4_RANDOM_MATH(a1, c, r, b, b + AES_BLOCK_SIZE);
      ^
/home/user/src/monero/src/crypto/slow-hash.c:304:9: note: expanded from macro 'VARIANT4_RANDOM_MATH'
      (*hp_jitfunc)(r); \
        ^
5 errors generated.
src/crypto/CMakeFiles/obj_cncrypto.dir/build.make:470: recipe for target 'src/crypto/CMakeFiles/obj_cncrypto.dir/slow-hash.c.o' failed
make[3]: *** [src/crypto/CMakeFiles/obj_cncrypto.dir/slow-hash.c.o] Error 1
make[3]: Leaving directory '/home/user/src/monero/armv7'
CMakeFiles/Makefile2:812: recipe for target 'src/crypto/CMakeFiles/obj_cncrypto.dir/all' failed
make[2]: *** [src/crypto/CMakeFiles/obj_cncrypto.dir/all] Error 2
make[2]: Leaving directory '/home/user/src/monero/armv7'
CMakeFiles/Makefile2:787: recipe for target 'src/crypto/CMakeFiles/cncrypto.dir/rule' failed
make[1]: *** [src/crypto/CMakeFiles/cncrypto.dir/rule] Error 2
make[1]: Leaving directory '/home/user/src/monero/armv7'
Makefile:318: recipe for target 'cncrypto' failed
make: *** [cncrypto] Error 2
``` 

It seems the `slow-hash.c` code needs to be restructured a bit.
`armv8-a` errors are almost the same.

# Discussion History
## moneromooo-monero | 2019-02-21T19:14:58+00:00
Does https://github.com/moneromooo-monero/bitmonero/tree/cnv4a help ?

## Hoshpak | 2019-02-21T20:34:18+00:00
It produces the same errors for me when compiling for armv8-a.

## sedited | 2019-02-21T22:24:00+00:00
I observe the same error when compiling with depends accross armv8, armv7 and i686-linux. The patch on your cnv4a branch does not fix it @moneromooo-monero 

## naughtyfox | 2019-02-22T10:08:12+00:00
@moneromooo-monero I got almost the same errors with the patch:
```[  8%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/slow-hash.c.o
cd /home/sergey/src/monero/armv8/src/crypto && /opt/android/tool64/bin/clang -DAUTO_INITIALIZE_EASYLOGGINGPP -DBLOCKCHAIN_DB=DB_LMDB -DBUILD_TAG=android -DDEFAULT_DB_TYPE=\"lmdb\" -DEMBEDDED_WALLET -DFORCE_USE_HEAP=1 -DHAVE_STRPTIME -DMINIUPNP_STATICLIB -DPER_BLOCK_CHECKPOINT -DSTATICLIB -DUSE_DEVICE_LEDGER=0 -I/home/sergey/src/monero/external/rapidjson/include -I/home/sergey/src/monero/external/easylogging++ -I/home/sergey/src/monero/src -I/home/sergey/src/monero/contrib/epee/include -I/home/sergey/src/monero/external -I/home/sergey/src/monero/armv8/openssl-1.0.2n/include -I/home/sergey/src/monero/armv8/translations -I/home/sergey/src/monero/external/unbound/libunbound -I/home/sergey/src/monero/external/db_drivers/liblmdb -isystem /home/sergey/src/monero/armv8/boost/include -I/home/sergey/src/monero/armv8/libsodium-android-armv8-a/include  -Wno-unused-command-line-argument -pthread -march=armv8-a -fno-strict-aliasing -std=c11 -D_GNU_SOURCE   -Wall -Wextra -Wpointer-arith -Wundef -Wvla -Wwrite-strings -Wno-error=extra -Wno-error=deprecated-declarations -Wno-unused-parameter -Wno-unused-variable -Wno-error=unused-variable -Wno-error=undef -Wno-error=uninitialized -Wno-user-defined-warnings -Wno-error=inline-asm -Waggregate-return -Wnested-externs -Wold-style-definition -Wstrict-prototypes  -fPIC  -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -Wformat-security -fstack-protector -fstack-protector-strong -fno-strict-aliasing -mfix-cortex-a53-835769 -fPIE -DNDEBUG -O2  -fPIC   -Werror -o CMakeFiles/obj_cncrypto.dir/slow-hash.c.o   -c /home/sergey/src/monero/src/crypto/slow-hash.c
/home/sergey/src/monero/src/crypto/slow-hash.c:1497:5: error: implicit declaration of function 'use_v4_jit' is invalid in C99 [-Werror,-Wimplicit-function-declaration]
    VARIANT4_RANDOM_MATH_INIT();
    ^
/home/sergey/src/monero/src/crypto/slow-hash.c:270:13: note: expanded from macro 'VARIANT4_RANDOM_MATH_INIT'
  int jit = use_v4_jit(); \
            ^
/home/sergey/src/monero/src/crypto/slow-hash.c:1497:5: error: this function declaration is not a prototype [-Werror,-Wstrict-prototypes]
/home/sergey/src/monero/src/crypto/slow-hash.c:270:13: note: expanded from macro 'VARIANT4_RANDOM_MATH_INIT'
  int jit = use_v4_jit(); \
            ^
/home/sergey/src/monero/src/crypto/slow-hash.c:1497:5: error: use of undeclared identifier 'hp_jitfunc'
/home/sergey/src/monero/src/crypto/slow-hash.c:278:44: note: expanded from macro 'VARIANT4_RANDOM_MATH_INIT'
      int ret = v4_generate_JIT_code(code, hp_jitfunc, 4096); \
                                           ^
/home/sergey/src/monero/src/crypto/slow-hash.c:1535:7: error: use of undeclared identifier 'hp_jitfunc'
      VARIANT4_RANDOM_MATH(a1, c, r, b, b + AES_BLOCK_SIZE);
      ^
/home/sergey/src/monero/src/crypto/slow-hash.c:304:9: note: expanded from macro 'VARIANT4_RANDOM_MATH'
      (*hp_jitfunc)(r); \
        ^
4 errors generated.
src/crypto/CMakeFiles/obj_cncrypto.dir/build.make:470: recipe for target 'src/crypto/CMakeFiles/obj_cncrypto.dir/slow-hash.c.o' failed
make[3]: *** [src/crypto/CMakeFiles/obj_cncrypto.dir/slow-hash.c.o] Error 1
make[3]: Leaving directory '/home/sergey/src/monero/armv8'
CMakeFiles/Makefile2:812: recipe for target 'src/crypto/CMakeFiles/obj_cncrypto.dir/all' failed
make[2]: *** [src/crypto/CMakeFiles/obj_cncrypto.dir/all] Error 2
make[2]: Leaving directory '/home/sergey/src/monero/armv8'
CMakeFiles/Makefile2:787: recipe for target 'src/crypto/CMakeFiles/cncrypto.dir/rule' failed
make[1]: *** [src/crypto/CMakeFiles/cncrypto.dir/rule] Error 2
make[1]: Leaving directory '/home/sergey/src/monero/armv8'
Makefile:318: recipe for target 'cncrypto' failed
make: *** [cncrypto] Error 2
```

I think the problem now is using the macros at `slow-hash.c:1497` under ```#elif !defined NO_AES && (defined(__arm__) || defined(__aarch64__))```
conditions, but the functions are defined under ```#if !defined NO_AES && (defined(__x86_64__) || (defined(_MSC_VER) && defined(_WIN64)))``` macro conditions

## moneromooo-monero | 2019-02-22T10:19:14+00:00
The last patch in #4907 should fix it.

## naughtyfox | 2019-02-22T11:17:49+00:00
It builds now on both `v7` and `v8`. Looking forward for the patch to be merged into release :)

## moneromooo-monero | 2019-02-22T12:53:31+00:00
But does it run fine ?

## sedited | 2019-02-22T13:44:38+00:00
Your https://github.com/monero-project/monero/pull/4907 does indeed fix it, but I had to patch the cmake files a bit for cross compilation. The way `ARCH_ID`, `ARCH` and `-march` are currently handled is a bit convoluted, so I'm not quite sure that the patch actually does what I want to, but it works somehow. Can you add it to the patch you'll push to master?

```
diff --git a/CMakeLists.txt b/CMakeLists.txt
index 125642b14..371c92f36 100644
--- a/CMakeLists.txt
+++ b/CMakeLists.txt
@@ -115,6 +115,9 @@ string(TOLOWER ${CMAKE_BUILD_TYPE} CMAKE_BUILD_TYPE_LOWER)
 # to identify the target architecture, to direct logic in this cmake script.
 # Since ARCH is a cached variable, it will not be set on first cmake invocation.
 if (NOT ARCH OR ARCH STREQUAL "" OR ARCH STREQUAL "native" OR ARCH STREQUAL "default")
+  if(CMAKE_SYSTEM_PROCESSOR STREQUAL "")
+    set(CMAKE_SYSTEM_PROCESSOR ${CMAKE_HOST_SYSTEM_PROCESSOR})
+  endif()
   set(ARCH_ID "${CMAKE_SYSTEM_PROCESSOR}")
 else()
   set(ARCH_ID "${ARCH}")
diff --git a/contrib/depends/toolchain.cmake.in b/contrib/depends/toolchain.cmake.in
index 66168facb..f11e7e922 100644
--- a/contrib/depends/toolchain.cmake.in
+++ b/contrib/depends/toolchain.cmake.in
@@ -41,6 +41,8 @@ set (CMAKE_FIND_ROOT_PATH_MODE_PROGRAM NEVER) # Find programs on host
 set (CMAKE_FIND_ROOT_PATH_MODE_LIBRARY ONLY) # Find libs in target
 set (CMAKE_FIND_ROOT_PATH_MODE_INCLUDE ONLY) # Find includes in target
 
+set(CMAKE_SYSTEM_PROCESSOR ${CMAKE_HOST_SYSTEM_PROCESSOR} CACHE STRING "" FORCE)
+
 # specify the cross compiler to be used. Darwin uses clang provided by the SDK.
 if(CMAKE_SYSTEM_NAME STREQUAL "Darwin")
   SET(CMAKE_C_COMPILER @prefix@/native/bin/clang)
@@ -85,6 +87,11 @@ endif()
 
 if(ARCHITECTURE STREQUAL "i686" AND CMAKE_SYSTEM_NAME STREQUAL "Linux")
   SET(LINUX_32 ON)
+  SET(ARCH_ID "i386")
+endif()
+
+if(ARCHITECTURE STREQUAL "x86_64" AND CMAKE_SYSTEM_NAME STREQUAL "Linux")
+  SET(ARCH_ID "x86_64")
 endif()
 
 #Create a new global cmake flag that indicates building with depends
```

Does this still pass the slow hash unit tests?




## moneromooo-monero | 2019-02-22T15:53:45+00:00
Crypto tests still pass with that patch.
Now in https://github.com/monero-project/monero/pull/5184

## gavriilos | 2019-02-26T16:02:36+00:00
I am facing the same issue on `ARMv7` with the [`v0.14.0.0` tag](https://github.com/monero-project/monero/releases/tag/v0.14.0.0). Applying #5184 fixes the compilation error.
Later I get another error, though it may be unrelated: #5200

## moneromooo-monero | 2019-03-05T13:44:02+00:00
All fixed I think. Can you double check ?

## Lafudoci | 2019-03-06T15:10:37+00:00
My ARMv7 (ASUS tinker board) node just had a successful build on release-v0.13 branch.

## moneromooo-monero | 2019-03-06T15:27:52+00:00
Thanks.

+resolved

# Action History
- Created by: naughtyfox | 2019-02-21T15:43:30+00:00
- Closed at: 2019-03-06T15:33:52+00:00
