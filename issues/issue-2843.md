---
title: error installing on RBPI  3
source_url: https://github.com/xmrig/xmrig/issues/2843
author: Tinkl
assignees: []
labels: []
created_at: '2021-12-28T12:25:22+00:00'
updated_at: '2021-12-28T14:15:12+00:00'
type: issue
status: closed
closed_at: '2021-12-28T14:15:12+00:00'
---

# Original Description
pi@raspberrypi:~ $ git clone https://github.com/xmrig/xmrig.git
Cloning into 'xmrig'...
remote: Enumerating objects: 26057, done.
remote: Counting objects: 100% (2043/2043), done.
remote: Compressing objects: 100% (934/934), done.
remote: Total 26057 (delta 1283), reused 1692 (delta 1103), pack-reused 24014
Receiving objects: 100% (26057/26057), 12.22 MiB | 3.32 MiB/s, done.
Resolving deltas: 100% (19035/19035), done.
pi@raspberrypi:~ $ cd xmrig
pi@raspberrypi:~/xmrig $ mkdir build
pi@raspberrypi:~/xmrig $ cd build
pi@raspberrypi:~/xmrig/build $ cmake ..
-- The C compiler identification is GNU 8.3.0
-- The CXX compiler identification is GNU 8.3.0
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
-- Performing Test VAES_SUPPORTED
-- Performing Test VAES_SUPPORTED - Failed
-- Use ARM_TARGET=7 (armv7l)
-- Looking for syslog.h
-- Looking for syslog.h - found
-- Found HWLOC: /usr/lib/arm-linux-gnueabihf/libhwloc.so
-- Found UV: /usr/lib/arm-linux-gnueabihf/libuv.a
-- Looking for __builtin___clear_cache
-- Looking for __builtin___clear_cache - found
-- WITH_MSR=OFF
-- Found OpenSSL: /usr/lib/arm-linux-gnueabihf/libcrypto.so (found version "1.1.                                1d")
-- Configuring done
-- Generating done
-- Build files have been written to: /home/pi/xmrig/build
pi@raspberrypi:~/xmrig/build $ make
Scanning dependencies of target ghostrider
[  0%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_bla                                ke.c.o
[  0%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_bmw                                .c.o
[  1%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_cub                                ehash.c.o
[  1%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_ech                                o.c.o
[  1%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_fug                                ue.c.o
[  2%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_gro                                estl.c.o
[  2%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_ham                                si.c.o
[  3%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_jh.                                c.o
[  3%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_kec                                cak.c.o
[  3%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_luf                                fa.c.o
[  4%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_sha                                bal.c.o
[  4%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_sha                                vite.c.o
[  4%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_sim                                d.c.o
[  5%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_sha                                2.c.o
[  5%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_ske                                in.c.o
[  6%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_whi                                rlpool.c.o
[  6%] Building CXX object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/ghost                                rider.cpp.o
In file included from /home/pi/xmrig/src/crypto/ghostrider/ghostrider.cpp:57:
/home/pi/xmrig/src/crypto/ghostrider/../../crypto/cn/sse2neon.h:122:2: error: #e                                rror "Unsupported target. Must be either ARMv7-A+NEON or ARMv8-A."
 #error "Unsupported target. Must be either ARMv7-A+NEON or ARMv8-A."
  ^~~~~
In file included from /home/pi/xmrig/src/crypto/ghostrider/ghostrider.cpp:57:
/home/pi/xmrig/src/crypto/ghostrider/../../crypto/cn/sse2neon.h:7594:9: warning:                                 ‘#pragma GCC pop_options’ without a corresponding ‘#pragma GCC push_options’ [-                                Wpragmas]
 #pragma GCC pop_options
         ^~~
make[2]: *** [src/crypto/ghostrider/CMakeFiles/ghostrider.dir/build.make:271: sr                                c/crypto/ghostrider/CMakeFiles/ghostrider.dir/ghostrider.cpp.o] Error 1
make[1]: *** [CMakeFiles/Makefile2:221: src/crypto/ghostrider/CMakeFiles/ghostri                                der.dir/all] Error 2
make: *** [Makefile:84: all] Error 2
pi@raspberrypi:~/xmrig/build $ ./xmrig -o gulf.moneroocean.stream:10128 -u 4617htx7bVBH3JHsL7AyoC9AuYR4BgmbgDFgWs8V425j6FE4Bo4hTH2NpFV7Bmx79ebCC9mPrNtjSfipVkuJqidoKM9jkuQ -p raspberrypi
-bash: ./xmrig: No such file or directory


# Discussion History
# Action History
- Created by: Tinkl | 2021-12-28T12:25:22+00:00
- Closed at: 2021-12-28T14:15:12+00:00
