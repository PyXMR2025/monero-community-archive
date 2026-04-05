---
title: 我无法运行xmrig在centos
source_url: https://github.com/xmrig/xmrig/issues/538
author: rocke
assignees: []
labels: []
created_at: '2018-04-11T11:24:46+00:00'
updated_at: '2018-11-05T13:24:13+00:00'
type: issue
status: closed
closed_at: '2018-11-05T13:24:13+00:00'
---

# Original Description
- cc1: error: invalid option argument ‘-Ofast’
- cc1: error: unrecognized command line option "-ftree-loop-if-convert-stores"
- make[2]: *** [src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/cpuid_main.c.o] Error 1
- make[1]: *** [src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/all] Error 2
- make: *** [all] Error 2


我的版本：CentOS release 6.8 (Final)

# Discussion History
## L1LjSHX | 2018-04-11T14:08:01+00:00
gcc version?

## c0mm4nd | 2018-04-21T12:06:52+00:00
In CentOS 6 's repo, the GCC version is 4.4.7 
https://gcc.gnu.org/onlinedocs/gcc-4.4.7/gcc/Option-Summary.html#Option-Summary

there is no -Ofast or -ftree-loop-if-convert-stores. If remove these options, new error shows: `unrecognized command line option "-std=c++11`. GCC 4.4.7 dont support C++11 standard

It's a fatal problem, if change the std, there will show lots of error: without C++11, there is no `nullptr`.

All in all, I recommand that you should update the gcc manually.

老哥用CentOS6你还是乖乖把gcc手动升级吧……要么干脆升到CentOS7.

## cityvigil | 2018-04-29T11:58:58+00:00
参与 这个 How can i install on centos 6? #52

vinchch

I've go also error when compiling with the latest kernel on centos 6
got the same error: version `GLIBC_2.14' not found
btw, I found a binary that works great here

https://cryptodev.one/dev/download-compiled-x86_64-binaries-xmrig-centos-6-x-7-x/

## tomneko | 2018-04-29T12:29:01+00:00
See also "Fail build on Centos 6.9 Final · Issue #364 · xmrig/xmrig"

I can build on CentOS6.9 by this way.

2018年4月29日(日) 20:58 cityvigil <notifications@github.com>:

> 参与 这个 How can i install on centos 6? #52
> <https://github.com/xmrig/xmrig/issues/52>
>
> vinchch
>
> I've go also error when compiling with the latest kernel on centos 6
> got the same error: version `GLIBC_2.14' not found
> btw, I found a binary that works great here
>
>
> https://cryptodev.one/dev/download-compiled-x86_64-binaries-xmrig-centos-6-x-7-x/
>
> —
> You are receiving this because you are subscribed to this thread.
> Reply to this email directly, view it on GitHub
> <https://github.com/xmrig/xmrig/issues/538#issuecomment-385246101>, or mute
> the thread
> <https://github.com/notifications/unsubscribe-auth/AAH3av49hkTAKIUb7vHv-AyEV-69tyupks5ttasDgaJpZM4TP2Nj>
> .
>
-- 
Gmail Mobileから送信 Tsutomu Hayashi


# Action History
- Created by: rocke | 2018-04-11T11:24:46+00:00
- Closed at: 2018-11-05T13:24:13+00:00
