---
title: How can i install on centos 6?
source_url: https://github.com/xmrig/xmrig/issues/52
author: mik2141797
assignees: []
labels: []
created_at: '2017-08-04T10:08:37+00:00'
updated_at: '2018-04-17T16:47:40+00:00'
type: issue
status: closed
closed_at: '2017-10-02T12:02:45+00:00'
---

# Original Description
when i try compiled i get errors

[root@179 build]# cmake3 .. -DCMAKE_BUILD_TYPE=Release -DUV_LIBRARY=/usr/lib/x86_64-linux-gnu/libuv.a
CMake Error at /usr/share/cmake3/Modules/FindPackageHandleStandardArgs.cmake:148 (message):
  Could NOT find UV (missing: UV_INCLUDE_DIR)
Call Stack (most recent call first):
  /usr/share/cmake3/Modules/FindPackageHandleStandardArgs.cmake:388 (_FPHSA_FAILURE_MESSAGE)
  cmake/FindUV.cmake:8 (find_package_handle_standard_args)
  CMakeLists.txt:131 (find_package)


# Discussion History
## xmrig | 2017-08-04T10:20:14+00:00
You need libuv version 1 (development files), As I know in centos 6 libuv version is 0.10 this version not supported. Anyway looks like you don't installed any libuv.

## mik2141797 | 2017-08-04T10:31:23+00:00
ok i install https://github.com/libuv/libuv/tree/v1.9.1
Now that I run "make" i get
Scanning dependencies of target jansson
[  1%] Building C object src/3rdparty/jansson/CMakeFiles/jansson.dir/dump.c.o
cc1: error: invalid option argument ‘-Ofast’
cc1: error: unrecognized command line option "-ftree-loop-if-convert-stores"
make[2]: *** [src/3rdparty/jansson/CMakeFiles/jansson.dir/dump.c.o] Error 1
make[1]: *** [src/3rdparty/jansson/CMakeFiles/jansson.dir/all] Error 2
make: *** [all] Error 2


## xmrig | 2017-08-04T10:36:12+00:00
What version of your compiler? `gcc -v` `g++ -v`
You can try replace `-Ofast` to `-O2` and remove `-ftree-loop-if-convert-stores` from CMakeLists.txt

## mik2141797 | 2017-08-04T10:47:38+00:00
gcc version 4.4.7 20120313 (Red Hat 4.4.7-18) (GCC)

Now:

[  1%] Building C object src/3rdparty/jansson/CMakeFiles/jansson.dir/dump.c.o
[  3%] Building C object src/3rdparty/jansson/CMakeFiles/jansson.dir/error.c.o
[  5%] Building C object src/3rdparty/jansson/CMakeFiles/jansson.dir/hashtable.c.o
[  7%] Building C object src/3rdparty/jansson/CMakeFiles/jansson.dir/hashtable_seed.c.o
/opt/xmrig/src/3rdparty/jansson/hashtable_seed.c: In function ‘json_object_seed’:
/opt/xmrig/src/3rdparty/jansson/hashtable_seed.c:203: warning: implicit declaration of function ‘__atomic_test_and_set’
/opt/xmrig/src/3rdparty/jansson/hashtable_seed.c:203: error: ‘__ATOMIC_RELAXED’ undeclared (first use in this function)
/opt/xmrig/src/3rdparty/jansson/hashtable_seed.c:203: error: (Each undeclared identifier is reported only once
/opt/xmrig/src/3rdparty/jansson/hashtable_seed.c:203: error: for each function it appears in.)
/opt/xmrig/src/3rdparty/jansson/hashtable_seed.c:208: warning: implicit declaration of function ‘__atomic_store_n’
/opt/xmrig/src/3rdparty/jansson/hashtable_seed.c:208: error: ‘__ATOMIC_RELEASE’ undeclared (first use in this function)
/opt/xmrig/src/3rdparty/jansson/hashtable_seed.c:215: warning: implicit declaration of function ‘__atomic_load_n’
/opt/xmrig/src/3rdparty/jansson/hashtable_seed.c:215: error: ‘__ATOMIC_ACQUIRE’ undeclared (first use in this function)
make[2]: *** [src/3rdparty/jansson/CMakeFiles/jansson.dir/hashtable_seed.c.o] Error 1
make[1]: *** [src/3rdparty/jansson/CMakeFiles/jansson.dir/all] Error 2
make: *** [all] Error 2


## xmrig | 2017-08-04T10:49:55+00:00
Too old compiler you need at least 4.9, preferably 5.4 or later.

## Axam | 2017-08-04T15:09:16+00:00
Would suggest to use at least GCC 5.4. 6.x and 7.x are better.

For GCC 5.3.1:
sudo yum install centos-release-scl cmake3
sudo yum install devtoolset-4-gcc devtoolset-4-gcc-c++
sudo scl enable devtoolset-4 bash
cmake3 . -DCMAKE_BUILD_TYPE=Release
make

For GCC 6.x:
sudo yum install centos-release-scl cmake3
sudo yum install devtoolset-6-gcc devtoolset-6-gcc-c++
sudo scl enable devtoolset-6 bash
cmake3 . -DCMAKE_BUILD_TYPE=Release
make

## Omnividente | 2017-08-04T23:57:44+00:00
gcc version 6.3.1 20170216 (Red Hat 6.3.1-3) (GCC)

```
[ 46%] Building CXX object CMakeFiles/xmrig.dir/src/net/Client.cpp.o
/opt/xmrig/src/net/Client.cpp: In member function ‘int64_t Client::submit(const JobResult&)’:
/opt/xmrig/src/net/Client.cpp:174:36: error: expected ‘)’ before ‘PRIu64’
     snprintf(req, 345, "{\"id\":%" PRIu64 ",\"jsonrpc\":\"2.0\",\"method\":\"submit\",\"params\":{\"id\":\"%s\",\"job_id\":\"%s\",\"nonce\":\"%s\",\"result\":\"%s\"}}\n",
                                    ^~~~~~
/opt/xmrig/src/net/Client.cpp:175:60: warning: spurious trailing ‘%’ in format [-Wformat=]
              m_sequence, m_rpcId, result.jobId, nonce, data);
                                                            ^
/opt/xmrig/src/net/Client.cpp:175:60: warning: too many arguments for format [-Wformat-extra-args]
In file included from /opt/xmrig/src/net/Client.cpp:29:0:
/opt/xmrig/src/net/Client.cpp: In member function ‘void Client::parseNotification(const char*, const json_t*, const json_t*)’:
/opt/xmrig/src/net/Client.cpp:351:54: error: expected ‘)’ before ‘PRId64’
             LOG_ERR("[%s:%u] error: \"%s\", code: %" PRId64, m_url.host(), m_url.port(), json_string_value(json_object_get(error, "message")), json_integer_value(json_object_get(error, "code")));
                                                      ^
/opt/xmrig/src/log/Log.h:73:60: note: in definition of macro ‘LOG_ERR’
 #define LOG_ERR(x, ...)    Log::i()->message(Log::ERR,     x, ##__VA_ARGS__)
                                                            ^
/opt/xmrig/src/net/Client.cpp: In member function ‘void Client::parseResponse(int64_t, const json_t*, const json_t*)’:
/opt/xmrig/src/net/Client.cpp:384:54: error: expected ‘)’ before ‘PRId64’
             LOG_ERR("[%s:%u] error: \"%s\", code: %" PRId64, m_url.host(), m_url.port(), message, json_integer_value(json_object_get(error, "code")));
                                                      ^
/opt/xmrig/src/log/Log.h:73:60: note: in definition of macro ‘LOG_ERR’
 #define LOG_ERR(x, ...)    Log::i()->message(Log::ERR,     x, ##__VA_ARGS__)
                                                            ^
/opt/xmrig/src/net/Client.cpp: In member function ‘void Client::ping()’:
/opt/xmrig/src/net/Client.cpp:425:36: error: expected ‘)’ before ‘PRId64’
     snprintf(req, 160, "{\"id\":%" PRId64 ",\"jsonrpc\":\"2.0\",\"method\":\"keepalived\",\"params\":{\"id\":\"%s\"}}\n", m_sequence, m_rpcId);
                                    ^~~~~~
/opt/xmrig/src/net/Client.cpp:425:142: warning: spurious trailing ‘%’ in format [-Wformat=]
     snprintf(req, 160, "{\"id\":%" PRId64 ",\"jsonrpc\":\"2.0\",\"method\":\"keepalived\",\"params\":{\"id\":\"%s\"}}\n", m_sequence, m_rpcId);
                                                                                                                                              ^
/opt/xmrig/src/net/
```Client.cpp:425:142: warning: too many arguments for format [-Wformat-extra-args]
make[2]: *** [CMakeFiles/xmrig.dir/src/net/Client.cpp.o] Error 1
make[1]: *** [CMakeFiles/xmrig.dir/all] Error 2
make: *** [all] Error 2



## xmrig | 2017-08-05T08:59:01+00:00
Interesting try add `add_definitions(/D__STDC_FORMAT_MACROS)` to end of CMakeLists.txt file.

## weizn11 | 2017-08-13T07:04:56+00:00
Excuse me, how can I solve this problem?

[ 79%] Building CXX object CMakeFiles/xmrig.dir/src/Mem_unix.cpp.o
/opt/rh/xmrig/src/Mem_unix.cpp: In static member function ‘static bool Mem::allocate(int, int, bool)’:
/opt/rh/xmrig/src/Mem_unix.cpp:50:106: error: ‘MAP_HUGETLB’ was not declared in this scope
     m_memory = static_cast<uint8_t*>(mmap(0, size, PROT_READ | PROT_WRITE, MAP_PRIVATE | MAP_ANONYMOUS | MAP_HUGETLB | MAP_POPULATE, 0, 0));
                                                                                                          ^~~~~~~~~~~
make[2]: *** [CMakeFiles/xmrig.dir/src/Mem_unix.cpp.o] Error 1
make[1]: *** [CMakeFiles/xmrig.dir/all] Error 2
make: *** [all] Error 2

## mnik247 | 2017-08-29T11:10:15+00:00
to @xmrig 
Thanks, fixed make  on Centos 6 for GCC 6.x:
"add add_definitions(/D__STDC_FORMAT_MACROS) to end of CMakeLists.txt file."

## kixgkqir | 2017-12-21T12:49:57+00:00
Hello guys, Iḿ trying to compile in centos6, with GCC 6.x and "add add_definitions(/D__STDC_FORMAT_MACROS) to end of CMakeLists.txt file.", but I have this error message bellow. Could you help me?

[ 17%] Building CXX object CMakeFiles/xmrig.dir/src/api/ApiState.cpp.o
/root/xmrig/src/api/ApiState.cpp: In member function ‘void ApiState::genId()’:
/root/xmrig/src/api/ApiState.cpp:143:53: error: no match for ‘operator<’ (operand types are ‘uv_err_t {aka uv_err_s}’ and ‘int’)
     if (uv_interface_addresses(&interfaces, &count) < 0) {
         ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^~~
/root/xmrig/src/api/ApiState.cpp:150:58: error: ‘uv_interface_address_t {aka struct uv_interface_address_s}’ has no member named ‘phys_addr’
             const size_t addrSize = sizeof(interfaces[i].phys_addr);
                                                          ^~~~~~~~~
/root/xmrig/src/api/ApiState.cpp:154:41: error: ‘uv_interface_address_t {aka struct uv_interface_address_s}’ has no member named ‘phys_addr’
             memcpy(input, interfaces[i].phys_addr, addrSize);
                                         ^~~~~~~~~
make[2]: *** [CMakeFiles/xmrig.dir/src/api/ApiState.cpp.o] Error 1
make[1]: *** [CMakeFiles/xmrig.dir/all] Error 2
make: *** [all] Error 2


## dkarma | 2018-02-16T22:48:48+00:00
same as kixgkqir above:
Scanning dependencies of target xmrig
[  2%] Building CXX object CMakeFiles/xmrig.dir/src/api/Api.cpp.o
[  5%] Building CXX object CMakeFiles/xmrig.dir/src/api/ApiState.cpp.o
/root/xmrig/src/api/ApiState.cpp: In member function ‘void ApiState::genId()’:
/root/xmrig/src/api/ApiState.cpp:143:53: error: no match for ‘operator<’ (operand types are ‘uv_err_t {aka uv_err_s}’ and ‘int’)
     if (uv_interface_addresses(&interfaces, &count) < 0) {
         ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^~~
/root/xmrig/src/api/ApiState.cpp:150:58: error: ‘uv_interface_address_t {aka struct uv_interface_address_s}’ has no member named ‘phys_addr’
             const size_t addrSize = sizeof(interfaces[i].phys_addr);
                                                          ^~~~~~~~~
/root/xmrig/src/api/ApiState.cpp:154:41: error: ‘uv_interface_address_t {aka struct uv_interface_address_s}’ has no member named ‘phys_addr’
             memcpy(input, interfaces[i].phys_addr, addrSize);
                                         ^~~~~~~~~
CMakeFiles/xmrig.dir/build.make:80: recipe for target 'CMakeFiles/xmrig.dir/src/api/ApiState.cpp.o' failed
make[2]: *** [CMakeFiles/xmrig.dir/src/api/ApiState.cpp.o] Error 1
CMakeFiles/Makefile2:63: recipe for target 'CMakeFiles/xmrig.dir/all' failed
make[1]: *** [CMakeFiles/xmrig.dir/all] Error 2
Makefile:75: recipe for target 'all' failed
make: *** [all] Error 2

using gcc 6:
gcc (GCC) 6.3.1 20170216 (Red Hat 6.3.1-3)



## AkKrock | 2018-03-16T15:24:39+00:00
Hi there, I suggest to use in Centos without install. Please see below work:
https://github.com/davidtavarez/portable-monero-miners
Works like a charm. I guess there are performance disadvantage but give it a try.
Centos is too hard to understand, so AppImage it!

Ofcourse more thanks to xmrig!

## ratkobucic | 2018-04-08T18:17:39+00:00
> Hi there, I suggest to use in Centos without install. Please see below work:
> https://github.com/davidtavarez/portable-monero-miners

Not working on CentOS 6.9
Errors like this:
> ./XMRig-x86_64.AppImage: /lib64/libc.so.6: version `GLIBC_2.14' not found (required by /tmp/.mount_XMRig-F0TBjM/usr/bin/../lib/libgmp.so.10)

## vinchch | 2018-04-17T16:47:40+00:00
I've go also error when compiling with the latest kernel on centos 6
got the same error: version `GLIBC_2.14' not found
btw, I found a binary that works great here

https://cryptodev.one/dev/download-compiled-x86_64-binaries-xmrig-centos-6-x-7-x/

# Action History
- Created by: mik2141797 | 2017-08-04T10:08:37+00:00
- Closed at: 2017-10-02T12:02:45+00:00
