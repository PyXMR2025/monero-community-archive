---
title: Centos 7 compile error
source_url: https://github.com/xmrig/xmrig/issues/1189
author: skoroneos
assignees: []
labels: []
created_at: '2019-09-22T07:23:34+00:00'
updated_at: '2019-12-22T19:33:26+00:00'
type: issue
status: closed
closed_at: '2019-12-22T19:33:26+00:00'
---

# Original Description
Greetings.
When trying to compile either the default branch or dev i get this error
The build is on a centos 7 with cmake3 and gcc-7
 
[root@localhost build]# make
[  1%] Building C object src/3rdparty/argon2/CMakeFiles/argon2-xop.dir/arch/x86_64/lib/argon2-xop.c.o
[  1%] Linking C static library libargon2-xop.a
[  1%] Built target argon2-xop
[  2%] Building C object src/3rdparty/argon2/CMakeFiles/argon2-ssse3.dir/arch/x86_64/lib/argon2-ssse3.c.o
[  3%] Linking C static library libargon2-ssse3.a
[  3%] Built target argon2-ssse3
[  4%] Building C object src/3rdparty/argon2/CMakeFiles/argon2-sse2.dir/arch/x86_64/lib/argon2-sse2.c.o
[  4%] Linking C static library libargon2-sse2.a
[  4%] Built target argon2-sse2
[  4%] Building C object src/3rdparty/argon2/CMakeFiles/argon2-avx512f.dir/arch/x86_64/lib/argon2-avx512f.c.o
[  5%] Linking C static library libargon2-avx512f.a
[  5%] Built target argon2-avx512f
[  6%] Building C object src/3rdparty/argon2/CMakeFiles/argon2-avx2.dir/arch/x86_64/lib/argon2-avx2.c.o
[  7%] Linking C static library libargon2-avx2.a
[  7%] Built target argon2-avx2
[  7%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/argon2.c.o
[  8%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/core.c.o
/root/tests/xmrig/src/3rdparty/argon2/lib/core.c: In function ‘store_block’:
/root/tests/xmrig/src/3rdparty/argon2/lib/core.c:539:1: internal compiler error: Segmentation fault
 }
 ^
Please submit a full bug report,
with preprocessed source if appropriate.
See <http://bugzilla.redhat.com/bugzilla> for instructions.
Preprocessed source stored into /tmp/ccT1JVCc.out file, please attach this to your bugreport.
make[2]: *** [src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/core.c.o] Error 1
make[1]: *** [src/3rdparty/argon2/CMakeFiles/argon2.dir/all] Error 2
make: *** [all] Error 2

[root@localhost build]# gcc -v
Using built-in specs.
COLLECT_GCC=gcc
COLLECT_LTO_WRAPPER=/opt/rh/devtoolset-7/root/usr/libexec/gcc/x86_64-redhat-linux/7/lto-wrapper
Target: x86_64-redhat-linux
Configured with: ../configure --enable-bootstrap --enable-languages=c,c++,fortran,lto --prefix=/opt/rh/devtoolset-7/root/usr --mandir=/opt/rh/devtoolset-7/root/usr/share/man --infodir=/opt/rh/devtoolset-7/root/usr/share/info --with-bugurl=http://bugzilla.redhat.com/bugzilla --enable-shared --enable-threads=posix --enable-checking=release --enable-multilib --with-system-zlib --enable-__cxa_atexit --disable-libunwind-exceptions --enable-gnu-unique-object --enable-linker-build-id --with-gcc-major-version-only --enable-plugin --with-linker-hash-style=gnu --enable-initfini-array --with-default-libstdcxx-abi=gcc4-compatible --with-isl=/builddir/build/BUILD/gcc-7.3.1-20180303/obj-x86_64-redhat-linux/isl-install --enable-libmpx --enable-gnu-indirect-function --with-tune=generic --with-arch_32=i686 --build=x86_64-redhat-linux
Thread model: posix
gcc version 7.3.1 20180303 (Red Hat 7.3.1-5) (GCC) 

# Discussion History
## xmrig | 2019-09-22T12:56:11+00:00
Probably system have no enough memory, if it right try create swap file, another option is disable argon2 algorithm `cmake .. -DWITH_ARGON2=OFF`.
Thank you.

# Action History
- Created by: skoroneos | 2019-09-22T07:23:34+00:00
- Closed at: 2019-12-22T19:33:26+00:00
