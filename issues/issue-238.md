---
title: 'Static compile '
source_url: https://github.com/xmrig/xmrig/issues/238
author: nyacat
assignees: []
labels: []
created_at: '2017-12-04T14:35:50+00:00'
updated_at: '2018-03-12T09:24:32+00:00'
type: issue
status: closed
closed_at: '2017-12-24T01:18:23+00:00'
---

# Original Description
I'm try to static compile.
I've change CMakeLists.txt to 
>set(CMAKE_EXE_LINKER_FLAGS " -static")
>add_executable(xmrig ${HEADERS} ${SOURCES} ${SOURCES_OS} ${SOURCES_CPUID} 
  ${HEADERS_CRYPTO} ${SOURCES_CRYPTO} ${SOURCES_SYSLOG} ${HTTPD_SOURCES})
>target_link_libraries(xmrig ${UV_LIBRARIES} ${MHD_LIBRARY} ${EXTRA_LIBS} ${CPUID_LIB} -static-libgcc -static-libstdc++)

But..When it mine for some time(e.g 1hr)
then get

> Segmentation fault

>[2017-12-04 22:07:49] speed 2.5s/60s/15m 1578.8 1599.6 1593.9 H/s max: 2297.7 H/s
>[2017-12-04 22:08:45] no active pools, stop mining
>[2017-12-04 22:08:49] speed 2.5s/60s/15m n/a 1607.9 1597.4 H/s max: 2297.7 H/s
>Segmentation fault

>real    70m5.320s
>user    1399m57.060s
>sys     0m7.096s


# Discussion History
## xmrig | 2017-12-07T04:45:31+00:00
I was trying build fully static executable, but when you compile you probably see some warnings related to DNS functions. So miner crashed when try resolve DNS name. I did't really investigate how solve this issue.
Thank you.

## nyacat | 2017-12-07T05:15:03+00:00
But I didn't saw anything about DNS...when it compile.
Only have this:
`17:43:40 [100%] Linking CXX executable xmrig`
`17:43:40 /usr/lib/gcc/x86_64-redhat-linux/7/../../../../lib64/libuv.a(libuv_la-core.o): In function uv__getpwuid_r': (.text+0x1860): warning: Using 'getpwuid_r' in statically linked applications requires at runtime the shared libraries from the glibc version used for linking`

`17:43:40 /usr/lib/gcc/x86_64-redhat-linux/7/../../../../lib64/libuv.a(libuv_la-getaddrinfo.o): In function uv__getaddrinfo_work': (.text+0x255): warning: Using 'getaddrinfo' in statically linked applications requires at runtime the shared libraries from the glibc version used for linking`

`17:43:40 [100%] Built target xmrig`

## xmrig | 2017-12-07T05:18:29+00:00
Second warning `Using 'getaddrinfo' in statically linked applications requires at runtime the shared libraries from the glibc version used for linking` This function used to resolve DNS names.

## nyacat | 2017-12-07T05:20:08+00:00
OK....So, will it be fixed?

## xmrig | 2017-12-07T05:29:42+00:00
It known issue, but not priority task now and it probably hard to fix, maybe need patch libuv or use some alternative DNS resolver.

## GoodiesHQ | 2017-12-21T22:01:09+00:00
This exact issue with `getaddrinfo` has bitten me in the ass on multiple occasions. If you really want a completely static version of this, you're going to have to get a little creative. Since this is an issue with Glibc, you can use a different libc implementation. Musl is the most complete one I know of. However, it only supports C libraries by default. Since libstdc++ is apart of GC, you need to compile GCC and link it against Musl. I ended up using this project to build standalone Musl compilers for C and C++: https://github.com/pattop/musl-cross-make

Once you do that, I build libuv using the new C compiler, and Xmrig using the new C++ compiler. The results are very pleasing. Completely static build and it doesn't use glibc so the `getaddrinfo` issue doesn't exist.

```
[user@Arch]: ~/Projects/xmrig/build>$ file xmrig 
xmrig: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), statically linked, stripped

[user@Arch]: ~/Projects/xmrig/build>$ ls -ho xmrig 
-rwxr-xr-x 1 user 1.3M Dec 21 13:36 xmrig

[user@Arch]: ~/Projects/xmrig/build>$ ./xmrig 
 * VERSIONS:     XMRig/2.4.2 libuv/1.12.1-dev gcc/7.2.0
 * HUGE PAGES:   available, disabled
 * CPU:          Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz (1) x64 AES-NI
 * THREADS:      2, cryptonight, av=1, donate=2%
 * POOL #1:      pool.monero.hashvault.pro:5555
 * COMMANDS:     hashrate, pause, resume
[2017-12-21 13:42:21] use pool pool.monero.hashvault.pro:5555 45.32.210.133
[2017-12-21 13:42:21] new job from pool.monero.hashvault.pro:5555 diff 5000
[2017-12-21 13:42:27] Ctrl+C received, exiting
[2017-12-21 13:42:27] no active pools, stop mining
[user@Arch]: ~/Projects/xmrig/build>$ 
```

## nyacat | 2017-12-24T01:18:23+00:00
thanks dude! you save me 

## cgansk | 2017-12-25T07:51:16+00:00
Hi sir,@GoodiesHQ im tottaly noobs,can u please give the compile tutorial step by steps?

## ghost | 2017-12-29T16:39:36+00:00
this builds with lmhttpd but without gnutls, haven't findout out why
run it in an alpine chroot/container/whateverjail
```bash
#!/bin/sh

cd /
jobs=$(cat /proc/cpuinfo | grep -i "cpu cores" | wc -l)
apk add alpine-sdk cmake libuv-dev
wget https://ftp.gnu.org/gnu/libmicrohttpd/libmicrohttpd-latest.tar.gz
tar xf libmicrohttpd-latest.tar.gz
cd libmicrohttpd-*
./configure --enable-static --disable-shared
make -j $jobs install
cd /
git clone --depth=1 https://github.com/xmrig/xmrig
mkdir xmrig/build && cd xmrig/build || exit 1
mhdpath=$(ls -d /libmicrohttpd-*/)
sed '/add_executable/iset(CMAKE_EXE_LINKER_FLAGS " -static")' -i ../CMakeLists.txt
cmake .. -DMHD_INCLUDE_DIR=${mhdpath}/src/include -DMHD_LIBRARY=/${mhdpath}/src/microhttpd/.libs/libmicrohttpd.a
make -j $jobs
```

## kronoscrasher | 2018-01-03T10:47:44+00:00
Hey @GoodiesHQ mate, maybe you coud share your binary?
Or develop extensive instruction in building it in static, on a fair donation?)

## andreworg | 2018-01-03T11:17:54+00:00
thanks @untoreh. nice trick with /proc/cpuinfo. you could also use nproc:

> make -j $(nproc)

see nproc(1) for details.

## cdarken | 2018-01-26T17:17:49+00:00
@knorhaan you should put instructions how to build it

## ghost | 2018-03-09T10:37:36+00:00
@GoodiesHQ please help me ,I did what you said to complie the libuv  ：

`CC=x86_64-linux-musl-gcc ./configure --disable-shared --enable-static --host=x86_64-linux-musl
`
But it has never passed ,

 Could you tell you the steps? please.........






## DataPools | 2018-03-10T22:43:02+00:00
@GoodiesHQ Thanks! I have a fully static version of xmrig thanks to musl and your instructions.

## 0xIslamTaha | 2018-03-12T09:24:31+00:00
@GoodiesHQ @DataPools 
Could u please add steps to compile xmrig?

# Action History
- Created by: nyacat | 2017-12-04T14:35:50+00:00
- Closed at: 2017-12-24T01:18:23+00:00
