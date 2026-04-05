---
title: Build on Android Pixel XL Fails Running Termux or Linux Deploy
source_url: https://github.com/xmrig/xmrig/issues/2164
author: michaelmannelson
assignees: []
labels: []
created_at: '2021-03-08T14:30:16+00:00'
updated_at: '2021-11-13T01:08:26+00:00'
type: issue
status: closed
closed_at: '2021-04-12T14:01:53+00:00'
---

# Original Description
**Describe the bug**
xmrig 6.10.0 fails to build when attempted within a Termux or Linux Deploy container of Ubuntu/Debian

**To Reproduce**
1) Follow the steps found at https://www.youtube.com/watch?v=kUcpjhzARWk for setting up Termux on Android OR Follow the steps found at https://www.youtube.com/watch?v=q_2XEM7qzQE for setting up Linux Deploy on rooted Android
2) Follow the steps found under "Basic build" at https://xmrig.com/docs/miner/build/ubuntu

**Expected behavior**
After running "make", the output should produce an executable binary of xmrig

**Required data**
 - Miner log as text or screenshot: see build output below
 - Config file or command line (without wallets): see build output below
 - OS: Android Pixel XL 10.0.0 (QP1A.191005.007.A3, Dec 2019) (marlin) that is running Termux 0.101 and Linux Deploy 2.6.0 which both are running Ubuntu 18.04 LTS

**Additional context**

```
root@localhost:~/xmrig/build# uname -a
Linux localhost 3.18.137-g72a7a64494e #1 SMP PREEMPT Fri Sep 27 18:40:34 UTC 2019 armv8l armv8l armv8l GNU/Linux

```

Cmake and Build output:

```
root@localhost:~/xmrig/build# cmake ..
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
-- Looking for syslog.h
-- Looking for syslog.h - found
-- Found HWLOC: /usr/lib/arm-linux-gnueabihf/libhwloc.so  
-- Found UV: /usr/lib/arm-linux-gnueabihf/libuv.a  
-- Looking for __builtin___clear_cache
-- Looking for __builtin___clear_cache - not found
-- WITH_MSR=OFF
-- Found OpenSSL: /usr/lib/arm-linux-gnueabihf/libcrypto.so (found version "1.1.0g") 
-- Configuring done
-- Generating done
-- Build files have been written to: /root/xmrig/build
root@localhost:~/xmrig/build# make -j$(nproc)
Scanning dependencies of target argon2
Scanning dependencies of target ethash
[  0%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/argon2.c.o
[  0%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/core.c.o
[  1%] Building C object src/3rdparty/libethash/CMakeFiles/ethash.dir/keccakf800.c.o
[  1%] Building C object src/3rdparty/libethash/CMakeFiles/ethash.dir/ethash_internal.c.o
cc: error: unrecognized command line option '-maes'; did you mean '-mapcs'?
src/3rdparty/argon2/CMakeFiles/argon2.dir/build.make:62: recipe for target 'src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/argon2.c.o' failed
make[2]: *** [src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/argon2.c.o] Error 1
make[2]: *** Waiting for unfinished jobs....
cc: error: unrecognized command line option '-maes'; did you mean '-mapcs'?
src/3rdparty/argon2/CMakeFiles/argon2.dir/build.make:86: recipe for target 'src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/core.c.o' failed
make[2]: *** [src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/core.c.o] Error 1
CMakeFiles/Makefile2:123: recipe for target 'src/3rdparty/argon2/CMakeFiles/argon2.dir/all' failed
make[1]: *** [src/3rdparty/argon2/CMakeFiles/argon2.dir/all] Error 2
make[1]: *** Waiting for unfinished jobs....
cc: error: unrecognized command line option '-maes'; did you mean '-mapcs'?
src/3rdparty/libethash/CMakeFiles/ethash.dir/build.make:86: recipe for target 'src/3rdparty/libethash/CMakeFiles/ethash.dir/keccakf800.c.o' failed
make[2]: *** [src/3rdparty/libethash/CMakeFiles/ethash.dir/keccakf800.c.o] Error 1
make[2]: *** Waiting for unfinished jobs....
cc: error: unrecognized command line option '-maes'; did you mean '-mapcs'?
src/3rdparty/libethash/CMakeFiles/ethash.dir/build.make:62: recipe for target 'src/3rdparty/libethash/CMakeFiles/ethash.dir/ethash_internal.c.o' failed
make[2]: *** [src/3rdparty/libethash/CMakeFiles/ethash.dir/ethash_internal.c.o] Error 1
CMakeFiles/Makefile2:178: recipe for target 'src/3rdparty/libethash/CMakeFiles/ethash.dir/all' failed
make[1]: *** [src/3rdparty/libethash/CMakeFiles/ethash.dir/all] Error 2
Makefile:83: recipe for target 'all' failed
make: *** [all] Error 2
```

I also tried running "cmake -DARM_TARGET=ON .." and it still fails to build and this is the output from that:

```
root@localhost:~/xmrig/build# cmake -DARM_TARGET=ON .. 
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
-- Looking for syslog.h
-- Looking for syslog.h - found
-- Found HWLOC: /usr/lib/arm-linux-gnueabihf/libhwloc.so  
-- Found UV: /usr/lib/arm-linux-gnueabihf/libuv.a  
-- Looking for __builtin___clear_cache
-- Looking for __builtin___clear_cache - not found
-- WITH_MSR=OFF
-- Found OpenSSL: /usr/lib/arm-linux-gnueabihf/libcrypto.so (found version "1.1.0g") 
-- Configuring done
-- Generating done
-- Build files have been written to: /root/xmrig/build
root@localhost:~/xmrig/build# make
Scanning dependencies of target ethash
[  0%] Building C object src/3rdparty/libethash/CMakeFiles/ethash.dir/ethash_internal.c.o
cc: error: unrecognized command line option '-maes'; did you mean '-mapcs'?
src/3rdparty/libethash/CMakeFiles/ethash.dir/build.make:62: recipe for target 'src/3rdparty/libethash/CMakeFiles/ethash.dir/ethash_internal.c.o' failed
make[2]: *** [src/3rdparty/libethash/CMakeFiles/ethash.dir/ethash_internal.c.o] Error 1
CMakeFiles/Makefile2:178: recipe for target 'src/3rdparty/libethash/CMakeFiles/ethash.dir/all' failed
make[1]: *** [src/3rdparty/libethash/CMakeFiles/ethash.dir/all] Error 2
Makefile:83: recipe for target 'all' failed
make: *** [all] Error 2
```

# Discussion History
## michaelmannelson | 2021-03-09T20:50:50+00:00
I got it to compile in Termux using "cmake -DARM_TARGET=8 .." and then calling make. Took awhile to compile but it looks like it working.

As for Linux Deploy on Android Pixel XL, I got this error:

```
... Previous code above successfully compiled ...
[ 80%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/cn/CnHash.cpp.o
In file included from /root/xmrig/src/crypto/cn/soft_aes.h:31:0,
                 from /root/xmrig/src/crypto/cn/CryptoNight_arm.h:35,
                 from /root/xmrig/src/crypto/cn/CnHash.cpp:35:
/root/xmrig/src/crypto/cn/sse2neon.h:122:2: error: #error "Unsupported target. Must be either ARMv7-A+NEON or ARMv8-A."
 #error "Unsupported target. Must be either ARMv7-A+NEON or ARMv8-A."
  ^~~~~
In file included from /root/xmrig/src/crypto/cn/soft_aes.h:31:0,
                 from /root/xmrig/src/crypto/cn/CryptoNight_arm.h:35,
                 from /root/xmrig/src/crypto/cn/CnHash.cpp:35:
/root/xmrig/src/crypto/cn/sse2neon.h:7150:9: warning: '#pragma GCC pop_options' without a corresponding '#pragma GCC push_options' [-Wpragmas]
 #pragma GCC pop_options
         ^~~
In file included from /root/xmrig/src/crypto/cn/CnHash.cpp:35:0:
/root/xmrig/src/crypto/cn/CryptoNight_arm.h: In function '__m128i aes_round_tweak_div(const __m128i&, const __m128i&)':
/root/xmrig/src/crypto/cn/CryptoNight_arm.h:367:29: warning: requested alignment 16 is larger than 8 [-Wattributes]
     alignas(16) uint32_t k[4];
                             ^
/root/xmrig/src/crypto/cn/CryptoNight_arm.h:368:29: warning: requested alignment 16 is larger than 8 [-Wattributes]
     alignas(16) uint32_t x[4];
                             ^
At global scope:
cc1plus: warning: unrecognized command line option '-Wno-class-memaccess'
CMakeFiles/xmrig.dir/build.make:4310: recipe for target 'CMakeFiles/xmrig.dir/src/crypto/cn/CnHash.cpp.o' failed
make[2]: *** [CMakeFiles/xmrig.dir/src/crypto/cn/CnHash.cpp.o] Error 1
CMakeFiles/Makefile2:68: recipe for target 'CMakeFiles/xmrig.dir/all' failed
make[1]: *** [CMakeFiles/xmrig.dir/all] Error 2
Makefile:83: recipe for target 'all' failed
make: *** [all] Error 2

```


# Action History
- Created by: michaelmannelson | 2021-03-08T14:30:16+00:00
- Closed at: 2021-04-12T14:01:53+00:00
