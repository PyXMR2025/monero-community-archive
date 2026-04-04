---
title: Error when build on ARM (mirabox)
source_url: https://github.com/monero-project/monero/issues/357
author: ghost
assignees: []
labels: []
created_at: '2015-08-01T18:56:31+00:00'
updated_at: '2015-08-01T19:03:19+00:00'
type: issue
status: closed
closed_at: '2015-08-01T19:03:19+00:00'
---

# Original Description
There is no AES support for ARMv7, so -maes causes gcc to abort.

``` sh
thaolx@mira /m/l/m/bitmonero> gcc -v
Using built-in specs.
COLLECT_GCC=gcc
COLLECT_LTO_WRAPPER=/usr/lib/gcc/arm-linux-gnueabihf/4.9/lto-wrapper
Target: arm-linux-gnueabihf
Configured with: ../src/configure -v --with-pkgversion='Debian 4.9.3-3' --with-bugurl=file:///usr/share/doc/gcc-4.9/README.Bugs --enable-languages=c,c++,java,go,d,fortran,objc,obj-c++ --prefix=/usr --program-suffix=-4.9 --enable-shared --enable-linker-build-id --libexecdir=/usr/lib --without-included-gettext --enable-threads=posix --with-gxx-include-dir=/usr/include/c++/4.9 --libdir=/usr/lib --enable-nls --with-sysroot=/ --enable-clocale=gnu --enable-libstdcxx-debug --enable-libstdcxx-time=yes --enable-gnu-unique-object --disable-libitm --disable-libquadmath --enable-plugin --with-system-zlib --disable-browser-plugin --enable-java-awt=gtk --enable-gtk-cairo --with-java-home=/usr/lib/jvm/java-1.5.0-gcj-4.9-armhf/jre --enable-java-home --with-jvm-root-dir=/usr/lib/jvm/java-1.5.0-gcj-4.9-armhf --with-jvm-jar-dir=/usr/lib/jvm-exports/java-1.5.0-gcj-4.9-armhf --with-arch-directory=arm --with-ecj-jar=/usr/share/java/eclipse-ecj.jar --enable-objc-gc --enable-multiarch --disable-sjlj-exceptions --with-arch=armv7-a --with-fpu=vfpv3-d16 --with-float=hard --with-mode=thumb --enable-checking=release --build=arm-linux-gnueabihf --host=arm-linux-gnueabihf --target=arm-linux-gnueabihf
Thread model: posix
gcc version 4.9.3 (Debian 4.9.3-3) 
```

Here is the buid log:

https://gist.github.com/anonymous/68ff35bc44b7510d140e


# Discussion History
## fluffypony | 2015-08-01T19:03:19+00:00
try `make release-arm7`, or use CMake to set NO_AES=ON.


# Action History
- Created by: ghost | 2015-08-01T18:56:31+00:00
- Closed at: 2015-08-01T19:03:19+00:00
