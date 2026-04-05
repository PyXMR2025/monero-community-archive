---
title: Cant build on FreeBSD (xmrirg v2.9.2)
source_url: https://github.com/xmrig/xmrig/issues/909
author: pboguk
assignees: []
labels:
- bug
created_at: '2019-01-16T07:37:13+00:00'
updated_at: '2019-01-19T17:43:22+00:00'
type: issue
status: closed
closed_at: '2019-01-19T17:43:22+00:00'
---

# Original Description
Hello,

11.1-RELEASE FreeBSD(different HW in all cases)
Always get 
[ 98%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/Asm.cpp.o
[100%] Linking CXX executable xmrig
/usr/bin/ld: undefined reference to symbol `pthread_condattr_init@@FBSD_1.0' (try adding -lthr)
//lib/libthr.so.3: could not read symbols: Bad value
c++: error: linker command failed with exit code 1 (use -v to see invocation)
*** Error code 1


On FreeBSD 10.3  I get:

CMakeFiles/xmrig.dir/src/common/Platform_unix.cpp.o: In function `Platform::setThreadAffinity(unsigned long)':
Platform_unix.cpp:(.text+0xe7): undefined reference to `pthread_setaffinity_np'
/usr/local/lib/libuv.a(libuv_la-thread.o): In function `uv_thread_create':
(.text+0x13): undefined reference to `pthread_create'





# Discussion History
## pboguk | 2019-01-16T08:19:54+00:00
Also, on 10.4-RELEASE I get 
[ 75%] Building CXX object CMakeFiles/xmrig.dir/src/Mem_unix.cpp.o
/usr/home/pboguk/xmrig/src/Mem_unix.cpp:105:5: error: use of undeclared identifier '__builtin___clear_cache'
    __builtin___clear_cache(reinterpret_cast<char*>(p), reinterpret_cast<char*>(p) + size);


## xmrig | 2019-01-16T08:38:58+00:00
About pthread errors please add `pthread` https://github.com/xmrig/xmrig/blob/master/CMakeLists.txt#L161 here, it should help, if not enough also add `rt` and `dl`.

About second error, what compiler version do you use?
Thank you.

## pboguk | 2019-01-16T09:01:31+00:00
Changing to
    161         set(EXTRA_LIBS kvm pthread rt dl)

Did the thing. Now it builds as usual in both cases.

Thank you!



## pboguk | 2019-01-16T09:15:17+00:00
Regarding

Also, on 10.4-RELEASE I get
[ 75%] Building CXX object CMakeFiles/xmrig.dir/src/Mem_unix.cpp.o
/usr/home/pboguk/xmrig/src/Mem_unix.cpp:105:5: error: use of undeclared identifier '__builtin___clear_cache'

I updated GCC and now it buids without error.

Thank you for great project!

## lisergey | 2019-01-16T09:20:54+00:00
@pboguk , pls do not forget that 11.1-RELEASE is End-of-Life on September 30, 2018
and 10.3 is EoL on 30 April 30, 2018, 10.4 is EoL on October 31, 2018
that is to mention that cause might be EoL

## pboguk | 2019-01-16T09:22:59+00:00
@lisergey, I know it, but I need to keep these versions to test  old legasy SW:(

## lisergey | 2019-01-16T09:27:34+00:00
> @lisergey, I know it, but I need to keep these versions to test old legasy SW:(

Did you try build xmrig-v2.9.2 on supported releases? 12.0, 11.2?

## pboguk | 2019-01-16T09:31:16+00:00
I've already built on 10x and 11x using advice from developer(see before in topic).
So 12.0, 11.2 shoud not have problems.

## xmrig | 2019-01-16T10:58:06+00:00
Build restored in master branch, I checked on FreeBSD 10.3 with clang 3.4.1.
Thank you.

# Action History
- Created by: pboguk | 2019-01-16T07:37:13+00:00
- Closed at: 2019-01-19T17:43:22+00:00
