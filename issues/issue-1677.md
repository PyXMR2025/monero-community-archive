---
title: compilation failed on arm ubuntu
source_url: https://github.com/xmrig/xmrig/issues/1677
author: zhaoxl
assignees: []
labels: []
created_at: '2020-05-15T08:05:48+00:00'
updated_at: '2020-08-19T01:24:39+00:00'
type: issue
status: closed
closed_at: '2020-08-19T01:24:39+00:00'
---

# Original Description
**device model:**
PHICOMM N1 (S905)

**system:**
Linux version 5.1.0-aml-s905 (root@vbox) (gcc version 7.4.1 20181213 [linaro-7.4-2019.02 revision 56ec6f6b99cc167ff0c2f8e1a2eed33b1edc85d4] (Linaro GCC 7.4-2019.02)) #5.89 SMP PREEMPT Tue Jun 18 09:58:51 MSK 2019

No LSB modules are available.
Distributor ID:	Ubuntu
Description:	Ubuntu 19.04
Release:	19.04
Codename:	disco

**cpu info:**
Architecture:        aarch64
Byte Order:          Little Endian
CPU(s):              4
On-line CPU(s) list: 0-3
Thread(s) per core:  1
Core(s) per socket:  4
Socket(s):           1
Vendor ID:           ARM
Model:               4
Model name:          Cortex-A53
Stepping:            r0p4
CPU max MHz:         1512.0000
CPU min MHz:         100.0000
BogoMIPS:            48.00
L1d cache:           unknown size
L1i cache:           unknown size
L2 cache:            unknown size
Flags:               fp asimd evtstrm aes pmull sha1 sha2 crc32 cpuid

**ld:**
GNU ld (GNU Binutils for Ubuntu) 2.32

**g++:**
Using built-in specs.
COLLECT_GCC=g++
COLLECT_LTO_WRAPPER=/usr/lib/gcc/aarch64-linux-gnu/6/lto-wrapper
Target: aarch64-linux-gnu
Configured with: ../src/configure -v --with-pkgversion='Ubuntu/Linaro 6.5.0-2ubuntu1~18.04' --with-bugurl=file:///usr/share/doc/gcc-6/README.Bugs --enable-languages=c,ada,c++,go,d,fortran,objc,obj-c++ --prefix=/usr --with-as=/usr/bin/aarch64-linux-gnu-as --with-ld=/usr/bin/aarch64-linux-gnu-ld --program-suffix=-6 --program-prefix=aarch64-linux-gnu- --enable-shared --enable-linker-build-id --libexecdir=/usr/lib --without-included-gettext --enable-threads=posix --libdir=/usr/lib --enable-nls --with-sysroot=/ --enable-clocale=gnu --enable-libstdcxx-debug --enable-libstdcxx-time=yes --with-default-libstdcxx-abi=new --enable-gnu-unique-object --disable-libquadmath --enable-plugin --enable-default-pie --with-system-zlib --enable-multiarch --enable-fix-cortex-a53-843419 --disable-werror --enable-checking=release --build=aarch64-linux-gnu --host=aarch64-linux-gnu --target=aarch64-linux-gnu
Thread model: posix
gcc version 6.5.0 20181026 (Ubuntu/Linaro 6.5.0-2ubuntu1~18.04)

**cmake result:**
****@aml:~/xmrig/build$ cmake ..
-- The C compiler identification is GNU 6.5.0
-- The CXX compiler identification is GNU 6.5.0
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
-- Use ARM_TARGET=8 (aarch64)
-- Performing Test XMRIG_ARM_CRYPTO
-- Performing Test XMRIG_ARM_CRYPTO - Success
-- Looking for syslog.h
-- Looking for syslog.h - found
-- Found HWLOC: /usr/lib/aarch64-linux-gnu/libhwloc.so
-- Found UV: /usr/lib/aarch64-linux-gnu/libuv.a
-- Looking for __builtin___clear_cache
-- Looking for __builtin___clear_cache - found
-- WITH_MSR=OFF
-- Found OpenSSL: /usr/lib/aarch64-linux-gnu/libcrypto.so (found version "1.0.2g")
-- Configuring done
-- Generating done
-- Build files have been written to: /home/zhaoxiaolong/xmrig/build


**exception info:**
****@aml:~/xmrig/build$ make
Scanning dependencies of target argon2
[  0%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/argon2.c.o
[  0%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/core.c.o
[  1%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/encoding.c.o
[  1%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/genkat.c.o
......
[ 95%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/log/backends/SysLog.cpp.o
[ 96%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Tls.cpp.o
[ 96%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/tls/ServerTls.cpp.o
[ 97%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/tls/TlsConfig.cpp.o
[ 97%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/tls/TlsContext.cpp.o
[ 98%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/tls/TlsGen.cpp.o
[ 98%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/https/HttpsClient.cpp.o
[ 99%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/https/HttpsContext.cpp.o
[ 99%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/https/HttpsServer.cpp.o
[100%] Linking CXX executable xmrig
/usr/bin/aarch64-linux-gnu-ld: /usr/lib/gcc/aarch64-linux-gnu/6/../../../aarch64-linux-gnu/libuv.a(libuv_la-process.o): relocation R_AARCH64_ADR_PREL_PG_HI21 against symbol `__stack_chk_guard@@GLIBC_2.17' which may bind externally can not be used when making a shared object; recompile with -fPIC
/usr/bin/aarch64-linux-gnu-ld: /usr/lib/gcc/aarch64-linux-gnu/6/../../../aarch64-linux-gnu/libuv.a(libuv_la-process.o)(.text+0x10): unresolvable R_AARCH64_ADR_PREL_PG_HI21 relocation against symbol `__stack_chk_guard@@GLIBC_2.17'
/usr/bin/aarch64-linux-gnu-ld: final link failed: bad value
collect2: error: ld returned 1 exit status
make[2]: *** [CMakeFiles/xmrig.dir/build.make:5300: xmrig] Error 1
make[1]: *** [CMakeFiles/Makefile2:68: CMakeFiles/xmrig.dir/all] Error 2
make: *** [Makefile:84: all] Error 2

### **think! 3Q!! **

# Discussion History
# Action History
- Created by: zhaoxl | 2020-05-15T08:05:48+00:00
- Closed at: 2020-08-19T01:24:39+00:00
