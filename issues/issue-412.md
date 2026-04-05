---
title: Trouble build xmrig on Debian 8.7
source_url: https://github.com/xmrig/xmrig/issues/412
author: alexfriman24
assignees: []
labels:
- libuv
created_at: '2018-02-23T09:34:58+00:00'
updated_at: '2018-02-23T10:03:38+00:00'
type: issue
status: closed
closed_at: '2018-02-23T10:03:38+00:00'
---

# Original Description
**test@srv:/home/test/xmrig/build#** cmake ..
-- The C compiler identification is GNU 4.9.2
-- The CXX compiler identification is GNU 4.9.2
-- Check for working C compiler: /usr/bin/cc
-- Check for working C compiler: /usr/bin/cc -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working CXX compiler: /usr/bin/c++
-- Check for working CXX compiler: /usr/bin/c++ -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Found UV: /usr/lib/x86_64-linux-gnu/libuv.so
-- Looking for syslog.h
-- Looking for syslog.h - found
-- Found mhd: /usr/include
-- Configuring done
-- Generating done
-- Build files have been written to: /home/test/xmrig/build

**test@srv:/home/test/xmrig/build#** make
Scanning dependencies of target cpuid
[  2%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/cpuid_main.c.o
[  4%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/asm-bits.c.o
[  6%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/recog_amd.c.o
[  8%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/recog_intel.c.o
[ 11%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/libcpuid_util.c.o
Linking C static library libcpuid.a
[ 11%] Built target cpuid
Scanning dependencies of target xmrig
[ 13%] Building CXX object CMakeFiles/xmrig.dir/src/api/Api.cpp.o
[ 15%] Building CXX object CMakeFiles/xmrig.dir/src/api/ApiState.cpp.o
/home/test/xmrig/src/api/ApiState.cpp: In member function ‘void ApiState::genId()’:
/home/test/xmrig/src/api/ApiState.cpp:143:53: error: no match for ‘operator<’ (operand types are ‘uv_err_t {aka uv_err_s}’ and ‘int’)
     if (uv_interface_addresses(&interfaces, &count) < 0) {
                                                     ^
/home/test/xmrig/src/api/ApiState.cpp:150:58: error: ‘uv_interface_address_t’ has no member named ‘phys_addr’
             const size_t addrSize = sizeof(interfaces[i].phys_addr);
                                                          ^
/home/test/xmrig/src/api/ApiState.cpp:154:41: error: ‘uv_interface_address_t’ has no member named ‘phys_addr’
             memcpy(input, interfaces[i].phys_addr, addrSize);
                                         ^
CMakeFiles/xmrig.dir/build.make:77: ошибка выполнения рецепта для цели «CMakeFiles/xmrig.dir/src/api/ApiState.cpp.o»
make[2]: *** [CMakeFiles/xmrig.dir/src/api/ApiState.cpp.o] Ошибка 1
CMakeFiles/Makefile2:60: ошибка выполнения рецепта для цели «CMakeFiles/xmrig.dir/all»
make[1]: *** [CMakeFiles/xmrig.dir/all] Ошибка 2
Makefile:76: ошибка выполнения рецепта для цели «all»
make: *** [all] Ошибка 2
test@srv:/home/test/xmrig/build#


**root@srv:/home/test/xmrig/build#** lsb_release -a
No LSB modules are available.
Distributor ID: Debian
Description:    Debian GNU/Linux 8.7 (jessie)
Release:        8.7
Codename:       jessie



**root@srv:/home/test/xmrig/build#** gcc -v
Using built-in specs.
COLLECT_GCC=gcc
COLLECT_LTO_WRAPPER=/usr/lib/gcc/x86_64-linux-gnu/4.9/lto-wrapper
Target: x86_64-linux-gnu
Configured with: ../src/configure -v --with-pkgversion='Debian 4.9.2-10' --with-bugurl=file:///usr/share/doc/gcc-4.9/README.Bugs --enable-languages=c,c++,java,go,d,fortran,objc,obj-c++ --prefix=/usr --program-suffix=-4.9 --enable-shared --enable-linker-build-id --libexecdir=/usr/lib --without-included-gettext --enable-threads=posix --with-gxx-include-dir=/usr/include/c++/4.9 --libdir=/usr/lib --enable-nls --with-sysroot=/ --enable-clocale=gnu --enable-libstdcxx-debug --enable-libstdcxx-time=yes --enable-gnu-unique-object --disable-vtable-verify --enable-plugin --with-system-zlib --disable-browser-plugin --enable-java-awt=gtk --enable-gtk-cairo --with-java-home=/usr/lib/jvm/java-1.5.0-gcj-4.9-amd64/jre --enable-java-home --with-jvm-root-dir=/usr/lib/jvm/java-1.5.0-gcj-4.9-amd64 --with-jvm-jar-dir=/usr/lib/jvm-exports/java-1.5.0-gcj-4.9-amd64 --with-arch-directory=amd64 --with-ecj-jar=/usr/share/java/eclipse-ecj.jar --enable-objc-gc --enable-multiarch --with-arch-32=i586 --with-abi=m64 --with-multilib-list=m32,m64,mx32 --enable-multilib --with-tune=generic --enable-checking=release --build=x86_64-linux-gnu --host=x86_64-linux-gnu --target=x86_64-linux-gnu
Thread model: posix
gcc version 4.9.2 (Debian 4.9.2-10)




**Hi gays, what's the problem in phase 15%?
Thank you in advance.**

# Discussion History
## xmrig | 2018-02-23T09:42:39+00:00
libuv 0.10 not supported, you need libuv 1.x.x.
Thank you.

## alexfriman24 | 2018-02-23T10:03:38+00:00
thx:)

# Action History
- Created by: alexfriman24 | 2018-02-23T09:34:58+00:00
- Closed at: 2018-02-23T10:03:38+00:00
