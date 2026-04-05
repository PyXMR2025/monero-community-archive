---
title: Fails to identify raspberry pi 4 as aarch64
source_url: https://github.com/xmrig/xmrig/issues/2202
author: grahamreeds
assignees: []
labels: []
created_at: '2021-03-23T13:11:58+00:00'
updated_at: '2021-04-23T07:10:17+00:00'
type: issue
status: closed
closed_at: '2021-04-01T14:02:41+00:00'
---

# Original Description
When compiling, compilation fails with an error from within sse2neon.h
According to the error message it is "Unsupported target. Must be either ARMv7-A+NEON or ARMv8-A."

Running uname-a gives
```Linux raspberrypi 5.10.17-v8+ #1403 SMP PREEMPT Mon Feb 22 11:37:54 GMT 2021 aarch64 GNU/Linux```

Running cmake
```-- Use ARM_TARGET=8 (aarch64)
-- WITH_MSR=OFF
-- Configuring done
-- Generating done
-- Build files have been written to: /home/pi/xmrig/build```

make
[  1%] Built target ethash
[  4%] Built target argon2
[  4%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/cn/CnHash.cpp.o
In file included from /home/pi/xmrig/src/crypto/cn/soft_aes.h:31,
                 from /home/pi/xmrig/src/crypto/cn/CryptoNight_arm.h:35,
                 from /home/pi/xmrig/src/crypto/cn/CnHash.cpp:35:
/home/pi/xmrig/src/crypto/cn/sse2neon.h:122:2: error: #error "Unsupported target. Must be either ARMv7-A+NEON or ARMv8-A."
 #error "Unsupported target. Must be either ARMv7-A+NEON or ARMv8-A."
  ^~~~~
In file included from /home/pi/xmrig/src/crypto/cn/soft_aes.h:31,
                 from /home/pi/xmrig/src/crypto/cn/CryptoNight_arm.h:35,
                 from /home/pi/xmrig/src/crypto/cn/CnHash.cpp:35:
/home/pi/xmrig/src/crypto/cn/sse2neon.h:7150:9: warning: ‘#pragma GCC pop_options’ without a corresponding ‘#pragma GCC push_options’ [-Wpragmas]
 #pragma GCC pop_options
         ^~~
In file included from /home/pi/xmrig/src/crypto/cn/CnHash.cpp:35:
/home/pi/xmrig/src/crypto/cn/CryptoNight_arm.h: In function ‘__m128i aes_round_tweak_div(const __m128i&, const __m128i&)’:
/home/pi/xmrig/src/crypto/cn/CryptoNight_arm.h:367:29: warning: requested alignment 16 is larger than 8 [-Wattributes]
     alignas(16) uint32_t k[4];
                             ^
```
Raspberry Pi 4/8 with fresh copy of Raspberry Os. Update and upgrade ran. arm_64bit added to config.txt.

# Discussion History
## killamah | 2021-03-25T19:42:27+00:00
Same here , but in my case it's a T585 Samsung with Octacore 2 X A53 Cortex 64b. 
Whit this cmake the compilation is full done but when run xmrig i get : Bus Error:

cmake .. -DARM_TARGET=7

## grahamreeds | 2021-03-26T13:39:39+00:00
Even with the -DARM_TARGET option I get the exact same issue.

## Spudz76 | 2021-03-27T23:07:45+00:00
The compiler toolchain must also be 64-bit or `__aarch64__` will not be defined, leading to that error on ARMv8.

Setting for ARMv7 only bypasses [the logic](https://github.com/xmrig/xmrig/blob/master/src/crypto/cn/sse2neon.h#L103) and turns on neon-only, and then should work on 32-bit ARMv7 but there must be something ARMv8 doesn't like about that (maybe it would work if the kernel was 32-bit, so the CPU was in full 32-bit mode? but that would be a step backward...)

Does `gcc -v` say for target?  It probably says something like `arm-linux-gnueabihf` which means 32-bit (even though you have the `aarch64` kernel and OS in general).  It should say `aarch64-linux-gnu`... or of course `__aarch64__` won't be defined.  If it is wrong then you need to locate and install the 64-bit toolchain, I don't know anything about RPi so have no tips on that part - also likely different depending which version of the OS you've installed.

Source: [random blog](https://qengineering.eu/install-raspberry-64-os.html) scroll down slightly to the "Version check" section.

## grahamreeds | 2021-04-01T14:02:31+00:00
D'OH!  My bad.

 I had installed 32bit RaspbianOS not the 64bit.  If you download the image [here](https://downloads.raspberrypi.org/raspios_lite_arm64/images/raspios_lite_arm64-2020-08-24/2020-08-20-raspios-buster-arm64-lite.zip) and use the imager tool to write it to the sd card, Xmrig will compile fine.

## jgabriel98 | 2021-04-22T21:40:45+00:00
I've installed the 32bit OS imagem.
but upgraded with `rpi-update` and enabled 64bit kernel by adding `arm_64bit=1` into **/boot/config.txt**

So now `uname -a` gives _aarch64_: 
`Linux raspberrypi 5.10.31-v8+ #1412 SMP PREEMPT Wed Apr 21 15:47:05 BST 2021 aarch64 GNU/Linux`

but `gcc -v gives` _armv6_: 
```
Using built-in specs.
COLLECT_GCC=gcc
COLLECT_LTO_WRAPPER=/usr/lib/gcc/arm-linux-gnueabihf/8/lto-wrapper
Target: arm-linux-gnueabihf
Configured with: ../src/configure -v --with-pkgversion='Raspbian 8.3.0-6+rpi1' --with-bugurl=file:///usr/share/doc/gcc-8/README.Bugs --enable-languages=c,ada,c++,go,d,fortran,objc,obj-c++ --prefix=/usr --with-gcc-major-version-only --program-suffix=-8 --program-prefix=arm-linux-gnueabihf- --enable-shared --enable-linker-build-id --libexecdir=/usr/lib --without-included-gettext --enable-threads=posix --libdir=/usr/lib --enable-nls --enable-bootstrap --enable-clocale=gnu --enable-libstdcxx-debug --enable-libstdcxx-time=yes --with-default-libstdcxx-abi=new --enable-gnu-unique-object --disable-libitm --disable-libquadmath --disable-libquadmath-support --enable-plugin --with-system-zlib --with-target-system-zlib --enable-objc-gc=auto --enable-multiarch --disable-sjlj-exceptions --with-arch=armv6 --with-fpu=vfp --with-float=hard --disable-werror --enable-checking=release --build=arm-linux-gnueabihf --host=arm-linux-gnueabihf --target=arm-linux-gnueabihf
Thread model: posix
gcc version 8.3.0 (Raspbian 8.3.0-6+rpi1) 
```

how can i upgrade de build toolchain to 64bit ?

## Spudz76 | 2021-04-23T05:57:23+00:00
Install actual 64-bit image.  Sometimes that doesn't even come with the 64-bit compiler, as some form of evil trolling.  There does exist an image with 64-bit everything, people have found it...

## grahamreeds | 2021-04-23T07:10:17+00:00
https://downloads.raspberrypi.org/raspios_lite_arm64/images/

There's even been a release a couple of weeks ago.

GR

On Fri, 23 Apr 2021, 06:57 Tony Butler, ***@***.***> wrote:

> Install actual 64-bit image. Sometimes that doesn't even come with the
> 64-bit compiler, as some form of evil trolling. There does exist an image
> with 64-bit everything, people have found it...
>
> —
> You are receiving this because you modified the open/close state.
> Reply to this email directly, view it on GitHub
> <https://github.com/xmrig/xmrig/issues/2202#issuecomment-825407842>, or
> unsubscribe
> <https://github.com/notifications/unsubscribe-auth/ABGL3HHJ24GDSYXLHRF5QC3TKED5FANCNFSM4ZVE3G5A>
> .
>


# Action History
- Created by: grahamreeds | 2021-03-23T13:11:58+00:00
- Closed at: 2021-04-01T14:02:41+00:00
