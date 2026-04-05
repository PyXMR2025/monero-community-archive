---
title: Fail build on Centos 6.9 Final
source_url: https://github.com/xmrig/xmrig/issues/364
author: kriwelz
assignees: []
labels:
- question
created_at: '2018-01-26T11:15:21+00:00'
updated_at: '2018-04-29T11:57:56+00:00'
type: issue
status: closed
closed_at: '2018-03-14T22:48:59+00:00'
---

# Original Description
its a fresh install, and when i tried to make it shows these errors 

[root@bot build]# make
Scanning dependencies of target cpuid
[  2%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/cpuid_main.c.o
cc1: error: invalid option argument '-Ofast'
cc1: error: unrecognized command line option "-ftree-loop-if-convert-stores"
make[2]: *** [src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/cpuid_main.c.o] Error 1
make[1]: *** [src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/all] Error 2
make: *** [all] Error 2

any help?

# Discussion History
## ghost | 2018-01-26T20:45:01+00:00
cmake options ?you point to libuv?

## kriwelz | 2018-01-27T00:45:17+00:00
Yes, I just follow the instructions. I already update my gcc to 6.4 too,
after reading another post with similar issues, but mine still having
trouble.

On Jan 27, 2018 3:45 AM, "Bonyo Chen" <notifications@github.com> wrote:

> cmake options ?you point to libuv?
>
> —
> You are receiving this because you authored the thread.
> Reply to this email directly, view it on GitHub
> <https://github.com/xmrig/xmrig/issues/364#issuecomment-360899454>, or mute
> the thread
> <https://github.com/notifications/unsubscribe-auth/ACKcx6yCacfIDc_FDmXhLVPSeSyOQ9hjks5tOjlRgaJpZM4RuKtt>
> .
>


## ghost | 2018-01-27T11:45:36+00:00
cmake options ?you point to libuv? you point to your new gcc when you cmake ?
-D options ?
cmake -DCMAKE_C_COMPILER=? -DCMAKE_CXX_COMPILER=? -DWITH_LIBUV=pathtolibuv.1 and not 0.1
are you sure you compile with the right gcc and the right libuv ?
there is not only one post with the same error you have, find and read more posts. provide more info on what have you done before this error, maybe ? 
try to edit Cmake requirements file to lower the gcc version requirement if you cant cmake with your new gcc. but make sure you use libuv 1 and not 0.10

## kriwelz | 2018-01-27T11:49:28+00:00
Can you be so kind to point me how to check and make sure which version I
have and how to fix?
I will post my system versions when I got back to it in few hours.

On Jan 27, 2018 6:45 PM, "Bonyo Chen" <notifications@github.com> wrote:

> cmake options ?you point to libuv? you point to your new gcc when you
> cmake ?
> -D options ?
> cmake -DCMAKE_C_COMPILER=? -DCMAKE_CXX_COMPILER=?
> -DWITH_LIBUV=pathtolibuv.1 and not 0.1
> are you sure you compile with the right gcc and the right libuv ?
> there is not only one post with the same error you have, find and read
> more posts. provide more info on what have you done before this error,
> maybe ?
> try to edit Cmake requirements file to lower the gcc version requirement
> if you cant cmake with your new gcc. but make sure you use libuv 1 and not
> 0.10
>
> —
> You are receiving this because you authored the thread.
> Reply to this email directly, view it on GitHub
> <https://github.com/xmrig/xmrig/issues/364#issuecomment-360979475>, or mute
> the thread
> <https://github.com/notifications/unsubscribe-auth/ACKcx9eLYr_70ZsisPpnQzdgFFgK6VbXks5tOwxjgaJpZM4RuKtt>
> .
>


## xmrig | 2018-01-31T08:54:41+00:00
Older version of gcc not support `-Ofast`, you need specify name/path to your gcc/g++ when run cmake.
Thank you.

## tkalfaoglu | 2018-02-05T08:44:12+00:00
Ok, here is the solution:
https://www.softwarecollections.org/en/scls/rhscl/devtoolset-7/
do this and then you can compile it.. that simple..
Oh yes and update the libuv..
The cmake becomes:
cmake .. -DCMAKE_BUILD_TYPE=Release -DUV_LIBRARY=/usr/local/lib/libuv.a  -DWITH_HTTPD=OFF


## cityvigil | 2018-04-29T11:57:56+00:00
copy from How can i install on centos 6? #52  

vinchch

I've go also error when compiling with the latest kernel on centos 6
got the same error: version `GLIBC_2.14' not found
btw, I found a binary that works great here

https://cryptodev.one/dev/download-compiled-x86_64-binaries-xmrig-centos-6-x-7-x/

# Action History
- Created by: kriwelz | 2018-01-26T11:15:21+00:00
- Closed at: 2018-03-14T22:48:59+00:00
