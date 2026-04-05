---
title: unable to compile beta/evo on arm
source_url: https://github.com/xmrig/xmrig/issues/1203
author: shadat
assignees: []
labels: []
created_at: '2019-09-28T16:05:37+00:00'
updated_at: '2019-09-28T16:42:22+00:00'
type: issue
status: closed
closed_at: '2019-09-28T16:42:22+00:00'
---

# Original Description
i am trying to compile the new version with JIT for arm

> [  4%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuWorker.cpp.o
In file included from /home/fa/xmrigbeta/xmrig/src/crypto/randomx/randomx.h:35:0,
                 from /home/fa/xmrigbeta/xmrig/src/backend/cpu/CpuWorker.cpp:43:
/home/fa/xmrigbeta/xmrig/src/crypto/randomx/intrin_portable.h: In function ‘rx_vec_f128 rx_swap_vec_f128(rx_vec_f128)’:
/home/fa/xmrigbeta/xmrig/src/crypto/randomx/intrin_portable.h:412:39: error: ‘vcopyq_laneq_f64’ was not declared in this scope
  temp = vcopyq_laneq_f64(temp, 1, a, 1);
                                       ^
/home/fa/xmrigbeta/xmrig/src/crypto/randomx/intrin_portable.h: In function ‘rx_vec_f128 rx_set_vec_f128(uint64_t, uint64_t)’:
/home/fa/xmrigbeta/xmrig/src/crypto/randomx/intrin_portable.h:420:66: error: ‘vcopyq_laneq_u64’ was not declared in this scope
  return vreinterpretq_f64_u64(vcopyq_laneq_u64(temp0, 1, temp1, 0));
                                                                  ^
At global scope:
cc1plus: warning: unrecognized command line option ‘-Wno-class-memaccess’
CMakeFiles/xmrig.dir/build.make:1310: recipe for target 'CMakeFiles/xmrig.dir/src/backend/cpu/CpuWorker.cpp.o' failed
make[2]: *** [CMakeFiles/xmrig.dir/src/backend/cpu/CpuWorker.cpp.o] Error 1
CMakeFiles/Makefile2:67: recipe for target 'CMakeFiles/xmrig.dir/all' failed
make[1]: *** [CMakeFiles/xmrig.dir/all] Error 2
Makefile:83: recipe for target 'all' failed
make: *** [all] Error 2

i am aware that i am running a pretty old gcc, but not sure if this is the issue

> Using built-in specs.
COLLECT_GCC=gcc
COLLECT_LTO_WRAPPER=/usr/lib/gcc/aarch64-linux-gnu/5/lto-wrapper
Target: aarch64-linux-gnu
Configured with: ../src/configure -v --with-pkgversion='Ubuntu/Linaro 5.4.0-6ubuntu1 16.04.11' --with-bugurl=file:///usr/share/doc/gcc-5/README.Bugs --enable-languages=c,ada,c++,java,go,d,fortran,objc,obj-c++ --prefix=/usr --program-suffix=-5 --enable-shared --enable-linker-build-id --libexecdir=/usr/lib --without-included-gettext --enable-threads=posix --libdir=/usr/lib --enable-nls --with-sysroot=/ --enable-clocale=gnu --enable-libstdcxx-debug --enable-libstdcxx-time=yes --with-default-libstdcxx-abi=new --enable-gnu-unique-object --disable-libquadmath --enable-plugin --with-system-zlib --disable-browser-plugin --enable-java-awt=gtk --enable-gtk-cairo --with-java-home=/usr/lib/jvm/java-1.5.0-gcj-5-arm64/jre --enable-java-home --with-jvm-root-dir=/usr/lib/jvm/java-1.5.0-gcj-5-arm64 --with-jvm-jar-dir=/usr/lib/jvm-exports/java-1.5.0-gcj-5-arm64 --with-arch-directory=aarch64 --with-ecj-jar=/usr/share/java/eclipse-ecj.jar --enable-multiarch --enable-fix-cortex-a53-843419 --disable-werror --enable-checking=release --build=aarch64-linux-gnu --host=aarch64-linux-gnu --target=aarch64-linux-gnu
Thread model: posix
gcc version 5.4.0 20160609 (Ubuntu/Linaro 5.4.0-6ubuntu1~16.04.11)

are those neon instructions? doesn't look like my cpu has neon

cat /proc/cpuinfo 
processor	: 0
BogoMIPS	: 19.84
Features	: fp asimd aes pmull sha1 sha2 crc32
CPU implementer	: 0x41
CPU architecture: 8
CPU variant	: 0x0
CPU part	: 0xd03
CPU revision	: 3


# Discussion History
## shadat | 2019-09-28T16:42:22+00:00
switched to armbian 
gcc version 8.3.0 (Debian 8.3.0-6) 
problem solved

# Action History
- Created by: shadat | 2019-09-28T16:05:37+00:00
- Closed at: 2019-09-28T16:42:22+00:00
