---
title: If I want to run xmrig on all Linux platforms does that mean I need to build
  binaries on each platform?
source_url: https://github.com/xmrig/xmrig/issues/796
author: rocke
assignees: []
labels:
- review later
created_at: '2018-10-14T00:31:52+00:00'
updated_at: '2020-08-28T16:24:51+00:00'
type: issue
status: closed
closed_at: '2020-08-28T16:24:51+00:00'
---

# Original Description
If I want to run xmrig on all Linux platforms does that mean I need to build binaries on each platform? From centos5.0-7.0 ub14.0-16.0 Debian to all platforms?

# Discussion History
## snipeTR | 2018-10-14T00:56:41+00:00
Use docker. 

## adevelopcr | 2018-10-14T10:08:05+00:00
you can build it statically but you may face a problem with gethotname function so you can impelement it using raw sockets and dns protocol refrences and may use some dns servers like google and voila you have a binary that doesn't depend on glibc

## xmrig | 2018-10-14T11:26:07+00:00
@adevelopcr I was never try do it, but musl should help with full static executable https://github.com/xmrig/xmrig/search?q=musl&type=Issues

## rocke | 2018-10-15T04:19:00+00:00
@xmrig 

> ./xmrig: /lib64/libc.so.6: version `GLIBC_2.14' not found (required by ./xmrig)

I compiled the binaries on Centos7. I have run the above error in CentOS 6.10. How can I do static compilation? Let xmrig run on all Linux systems.

## adevelopcr | 2018-10-15T16:37:39+00:00
@xmrig see this if you are interested : 

https://gist.github.com/fffaraz/9d9170b57791c28ccda9255b48315168

## srwx666 | 2018-10-16T07:11:43+00:00
Just do opposite
compile on oldest box (old glibc), and it will work on latest, best without additional options,
only one disadvantage that You will need on old box newer compiler 5.9 probably at least, and compiled static libuv from sources.
that's it, tested and it's working


## adevelopcr | 2018-10-16T10:35:17+00:00
Or build on alpine Linux

## ratkobucic | 2018-10-16T10:35:46+00:00
It will not compile on CentOS 6.10... not even with SCL devtoolset-7

## srwx666 | 2018-10-16T16:02:16+00:00
[root@localhost xmrig]# cat /etc/redhat-release
CentOS release 6.9 (Final)
[root@localhost xmrig]# cd build
[root@localhost build]# cmake3 .. -DCMAKE_BUILD_TYPE=Release -DUV_LIBRARY=/root/libuv-1.23.2/.libs/libuv.a -DUV_INCLUDE_DIR=/root/libuv-1.23.2/include/ -DWITH_LIBCPUID=OFF -DWITH_HTTPD=OFF -DWITH_TLS=OFF


bla bla bla

[root@localhost build]# make
Scanning dependencies of target xmrig-asm
[  2%] Building ASM object CMakeFiles/xmrig-asm.dir/src/crypto/asm/cnv2_main_loop.S.o
[  4%] Linking C static library libxmrig-asm.a
[  4%] Built target xmrig-asm
Scanning dependencies of target xmrig

bla bla bla

[ 95%] Building CXX object CMakeFiles/xmrig.dir/src/common/log/SysLog.cpp.o
[ 97%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/Asm.cpp.o
[100%] Linking CXX executable xmrig
[100%] Built target xmrig

[root@localhost build]# ldd xmrig
        linux-vdso.so.1 =>  (0x00007fff4e748000)
        libpthread.so.0 => /lib64/libpthread.so.0 (0x00007fdb5a6a8000)
        librt.so.1 => /lib64/librt.so.1 (0x00007fdb5a49f000)
        libdl.so.2 => /lib64/libdl.so.2 (0x00007fdb5a29b000)
        libm.so.6 => /lib64/libm.so.6 (0x00007fdb5a017000)
        libc.so.6 => /lib64/libc.so.6 (0x00007fdb59c82000)
        /lib64/ld-linux-x86-64.so.2 (0x00007fdb5a8cb000)


comments ?







## ratkobucic | 2018-10-16T17:42:18+00:00
Yes, manage to build it myself on CentOS release 6.9 (Final)
Have issues on CentOS 6.10... could be some header/devlib is changed meanwhile :) Will test more 

```
[root@test build]# cat /etc/issue
CentOS release 6.9 (Final)
...
[100%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/Asm.cpp.o
Linking CXX executable xmrig
[100%] Built target xmrig
[root@test build]#
```

## stefanszl | 2018-10-25T15:10:34+00:00
Hi guys, i have this problem when i`m trying to compile version 2.8.3 on ubuntu 12.04
root@CMS1:/var/tmp/xmrig/build# cmake ..
-- The C compiler identification is GNU
-- The CXX compiler identification is GNU
-- Check for working C compiler: /usr/bin/gcc
-- Check for working C compiler: /usr/bin/gcc -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working CXX compiler: /usr/bin/c++
-- Check for working CXX compiler: /usr/bin/c++ -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Found UV: /usr/local/lib/libuv.a
-- Found OpenSSL: /usr/lib/i386-linux-gnu/libssl.so;/usr/lib/i386-linux-gnu/libcrypto.so (found version "1..1")
-- Looking for syslog.h
-- Looking for syslog.h - found
-- Found MHD: /usr/lib/libmicrohttpd.so
-- Configuring done
-- Generating done
-- Build files have been written to: /var/tmp/xmrig/build
root@CMS1:/var/tmp/xmrig/build# make
Scanning dependencies of target cpuid
[  1%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/cpuid_main.c.o
[  3%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/asm-bits.c.o
[  5%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/recog_amd.c.o
[  7%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/recog_intel.c.o
[  9%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/libcpuid_util.c.o
Linking C static library libcpuid.a
[  9%] Built target cpuid
Scanning dependencies of target xmrig
[ 11%] Building CXX object CMakeFiles/xmrig.dir/src/api/NetworkState.cpp.o
cc1plus: error: unrecognized command line option '-std=c++11'
cc1plus: warning: unrecognized command line option "-Wno-class-memaccess" [enabled by default]
make[2]: *** [CMakeFiles/xmrig.dir/src/api/NetworkState.cpp.o] Error 1
make[1]: *** [CMakeFiles/xmrig.dir/all] Error 2
make: *** [all] Error 2
root@CMS1:/var/tmp/xmrig/build#


## ghost | 2018-11-02T23:23:54+00:00
> 
> 
> If I want to run xmrig on all Linux platforms does that mean I need to build binaries on each platform? From centos5.0-7.0 ub14.0-16.0 Debian to all platforms?

https://github.com/lotus1313/xmrig

## 0xman | 2018-11-30T23:12:34+00:00
@rocke if you still need a fully static miner i can hook you up!

## muyuxx | 2019-03-26T02:10:14+00:00
hi，guys，any help？
build error in centos final 6.8
gcc 6.1 libuv 1.22
[ 76%] Building CXX object CMakeFiles/xmrig.dir/src/App_unix.cpp.o
[ 78%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/Json_unix.cpp.o
[ 79%] Building CXX object CMakeFiles/xmrig.dir/src/common/Platform_unix.cpp.o
[ 81%] Building CXX object CMakeFiles/xmrig.dir/src/Mem_unix.cpp.o
[ 82%] Building CXX object CMakeFiles/xmrig.dir/src/core/cpu/AdvancedCpuInfo.cpp.o
[ 84%] Building CXX object CMakeFiles/xmrig.dir/src/core/cpu/Cpu.cpp.o
[ 85%] Building C object CMakeFiles/xmrig.dir/src/crypto/c_groestl.c.o
[ 87%] Building C object CMakeFiles/xmrig.dir/src/crypto/c_blake256.c.o
[ 89%] Building C object CMakeFiles/xmrig.dir/src/crypto/c_jh.c.o
[ 90%] Building C object CMakeFiles/xmrig.dir/src/crypto/c_skein.c.o
[ 92%] Building CXX object CMakeFiles/xmrig.dir/src/common/log/SysLog.cpp.o
[ 93%] Building CXX object CMakeFiles/xmrig.dir/src/common/net/Tls.cpp.o
[ 95%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/Asm.cpp.o
[ 96%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/CryptonightR_gen.cpp.o
[ 98%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/cn_gpu_avx.cpp.o
/tmp/cc2XMPe8.s: Assembler messages:
/tmp/cc2XMPe8.s:984: Error: suffix or operands invalid for `vpsrldq'
/tmp/cc2XMPe8.s:985: Error: suffix or operands invalid for `vpslldq'
/tmp/cc2XMPe8.s:1715: Error: suffix or operands invalid for `vpsrldq'
/tmp/cc2XMPe8.s:1716: Error: suffix or operands invalid for `vpslldq'
/tmp/cc2XMPe8.s:1717: Error: suffix or operands invalid for `vpor'
/tmp/cc2XMPe8.s:1718: Error: suffix or operands invalid for `vpor'
/tmp/cc2XMPe8.s:1720: Error: suffix or operands invalid for `vpxor'
/tmp/cc2XMPe8.s:1721: Error: suffix or operands invalid for `vpxor'
/tmp/cc2XMPe8.s:1768: Error: suffix or operands invalid for `vpsrldq'
/tmp/cc2XMPe8.s:1769: Error: suffix or operands invalid for `vpslldq'
/tmp/cc2XMPe8.s:1770: Error: suffix or operands invalid for `vpor'
/tmp/cc2XMPe8.s:1772: Error: suffix or operands invalid for `vpxor'
/tmp/cc2XMPe8.s:1774: Error: suffix or operands invalid for `vpxor'
/tmp/cc2XMPe8.s:2049: Error: suffix or operands invalid for `vpsrldq'
/tmp/cc2XMPe8.s:2050: Error: suffix or operands invalid for `vpslldq'
/tmp/cc2XMPe8.s:2051: Error: suffix or operands invalid for `vpor'
/tmp/cc2XMPe8.s:2577: Error: suffix or operands invalid for `vpsrldq'
/tmp/cc2XMPe8.s:2578: Error: suffix or operands invalid for `vpslldq'
/tmp/cc2XMPe8.s:2579: Error: suffix or operands invalid for `vpor'
/tmp/cc2XMPe8.s:2580: Error: suffix or operands invalid for `vpxor'
/tmp/cc2XMPe8.s:2582: Error: suffix or operands invalid for `vpxor'
/tmp/cc2XMPe8.s:2624: Error: suffix or operands invalid for `vpsrldq'
/tmp/cc2XMPe8.s:2625: Error: suffix or operands invalid for `vpslldq'
/tmp/cc2XMPe8.s:2626: Error: suffix or operands invalid for `vpor'
/tmp/cc2XMPe8.s:2629: Error: suffix or operands invalid for `vpxor'
/tmp/cc2XMPe8.s:2631: Error: suffix or operands invalid for `vpxor'
/tmp/cc2XMPe8.s:2635: Error: suffix or operands invalid for `vpxor'
/tmp/cc2XMPe8.s:2639: Error: no such instruction: `vperm2i128 $65,%ymm2,%ymm2,%ymm0'
/tmp/cc2XMPe8.s:2641: Error: suffix or operands invalid for `vpxor'
make[2]: *** [CMakeFiles/xmrig.dir/src/crypto/cn_gpu_avx.cpp.o] Error 1
make[1]: *** [CMakeFiles/xmrig.dir/all] Error 2
make: *** [all] Error 2
[root@localhost build]# 


any help？

## trasherdk | 2019-03-26T03:04:53+00:00
@muyuxx 
This could be a case of `too old toolchain`.

Check: https://github.com/nodegit/nodegit/issues/1240#issuecomment-283472210


## muyuxx | 2019-03-27T07:01:47+00:00
oh my god 
i got it
[ 73%] Building CXX object CMakeFiles/xmrig.dir/src/workers/Workers.cpp.o
[ 75%] Building CXX object CMakeFiles/xmrig.dir/src/xmrig.cpp.o
[ 76%] Building CXX object CMakeFiles/xmrig.dir/src/App_unix.cpp.o
[ 78%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/Json_unix.cpp.o
[ 79%] Building CXX object CMakeFiles/xmrig.dir/src/common/Platform_unix.cpp.o
[ 81%] Building CXX object CMakeFiles/xmrig.dir/src/Mem_unix.cpp.o
[ 82%] Building CXX object CMakeFiles/xmrig.dir/src/core/cpu/AdvancedCpuInfo.cpp.o
[ 84%] Building CXX object CMakeFiles/xmrig.dir/src/core/cpu/Cpu.cpp.o
[ 85%] Building C object CMakeFiles/xmrig.dir/src/crypto/c_groestl.c.o
[ 87%] Building C object CMakeFiles/xmrig.dir/src/crypto/c_blake256.c.o
[ 89%] Building C object CMakeFiles/xmrig.dir/src/crypto/c_jh.c.o
[ 90%] Building C object CMakeFiles/xmrig.dir/src/crypto/c_skein.c.o
[ 92%] Building CXX object CMakeFiles/xmrig.dir/src/common/log/SysLog.cpp.o
[ 93%] Building CXX object CMakeFiles/xmrig.dir/src/common/net/Tls.cpp.o
[ 95%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/Asm.cpp.o
[ 96%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/CryptonightR_gen.cpp.o
[ 98%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/cn_gpu_avx.cpp.o
[100%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/cn_gpu_ssse3.cpp.o
Linking CXX executable xmrig
[100%] Built target xmrig
[root@localhost build]# 


thank you


## jasonwee | 2019-05-26T08:35:27+00:00
@muyuxx how exactly did you solve it? encountered similar issue

```
[ 96%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/CryptonightR_gen.cpp.o
[ 98%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/cn_gpu_avx.cpp.o
/tmp/ccfqDwSA.s: Assembler messages:
/tmp/ccfqDwSA.s:975: Error: suffix or operands invalid for `vpsrldq'
/tmp/ccfqDwSA.s:976: Error: suffix or operands invalid for `vpslldq'
/tmp/ccfqDwSA.s:1692: Error: suffix or operands invalid for `vpsrldq'
/tmp/ccfqDwSA.s:1693: Error: suffix or operands invalid for `vpslldq'
/tmp/ccfqDwSA.s:1694: Error: suffix or operands invalid for `vpor'
/tmp/ccfqDwSA.s:1695: Error: suffix or operands invalid for `vpor'
/tmp/ccfqDwSA.s:1696: Error: suffix or operands invalid for `vpxor'
/tmp/ccfqDwSA.s:1697: Error: suffix or operands invalid for `vpxor'
/tmp/ccfqDwSA.s:1742: Error: suffix or operands invalid for `vpsrldq'
/tmp/ccfqDwSA.s:1743: Error: suffix or operands invalid for `vpslldq'
/tmp/ccfqDwSA.s:1744: Error: suffix or operands invalid for `vpor'
/tmp/ccfqDwSA.s:1747: Error: suffix or operands invalid for `vpxor'
/tmp/ccfqDwSA.s:1750: Error: suffix or operands invalid for `vpxor'
/tmp/ccfqDwSA.s:2020: Error: suffix or operands invalid for `vpsrldq'
/tmp/ccfqDwSA.s:2021: Error: suffix or operands invalid for `vpslldq'
/tmp/ccfqDwSA.s:2022: Error: suffix or operands invalid for `vpor'
/tmp/ccfqDwSA.s:2545: Error: suffix or operands invalid for `vpsrldq'
/tmp/ccfqDwSA.s:2546: Error: suffix or operands invalid for `vpslldq'
/tmp/ccfqDwSA.s:2547: Error: suffix or operands invalid for `vpor'
/tmp/ccfqDwSA.s:2548: Error: suffix or operands invalid for `vpxor'
/tmp/ccfqDwSA.s:2550: Error: suffix or operands invalid for `vpxor'
/tmp/ccfqDwSA.s:2592: Error: suffix or operands invalid for `vpsrldq'
/tmp/ccfqDwSA.s:2593: Error: suffix or operands invalid for `vpslldq'
/tmp/ccfqDwSA.s:2594: Error: suffix or operands invalid for `vpor'
/tmp/ccfqDwSA.s:2597: Error: suffix or operands invalid for `vpxor'
/tmp/ccfqDwSA.s:2599: Error: suffix or operands invalid for `vpxor'
/tmp/ccfqDwSA.s:2603: Error: suffix or operands invalid for `vpxor'
/tmp/ccfqDwSA.s:2607: Error: no such instruction: `vperm2i128 $65,%ymm2,%ymm2,%ymm0'
/tmp/ccfqDwSA.s:2609: Error: suffix or operands invalid for `vpxor'
make[2]: *** [CMakeFiles/xmrig-notls.dir/src/crypto/cn_gpu_avx.cpp.o] Error 1
make[1]: *** [CMakeFiles/xmrig-notls.dir/all] Error 2
make: *** [all] Error 2
```

## jasonwee | 2019-05-26T14:29:02+00:00
okay, self solved, my solution was because gcc is too old, gcc-4 and binutils. upgrade both to gcc-6 and binutils 2.27-10 and then followed by export right CC and CXX

# Action History
- Created by: rocke | 2018-10-14T00:31:52+00:00
- Closed at: 2020-08-28T16:24:51+00:00
