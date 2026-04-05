---
title: problem finding libuv when compiling
source_url: https://github.com/xmrig/xmrig/issues/72
author: ghost
assignees: []
labels: []
created_at: '2017-08-27T20:56:00+00:00'
updated_at: '2021-06-22T19:45:22+00:00'
type: issue
status: closed
closed_at: '2017-10-02T12:02:10+00:00'
---

# Original Description
Hello,

I compiled the latest version of libuv and it is in my home folder and added the folder to the LD_LIBRARY_PATH, when I compile xmrig I get the following error:

CMake Error at /net/planck/.raid10/home/amr/programs/logs/tmp/cmake-3.9.1/Modules/FindPackageHandleStandardArgs.cmake:137 (message):
  Could NOT find UV (missing: UV_LIBRARY UV_INCLUDE_DIR)
Call Stack (most recent call first):
  /net/planck/.raid10/home/amr/programs/logs/tmp/cmake-3.9.1/Modules/FindPackageHandleStandardArgs.cmake:377 (_FPHSA_FAILURE_MESSAGE)
  cmake/FindUV.cmake:8 (find_package_handle_standard_args)
  CMakeLists.txt:131 (find_package)

Any help is appreciated.
Thanks in advance

# Discussion History
## xmrig | 2017-08-27T21:14:37+00:00
You need explicitly specify path to libuv when run cmake
`cmake .. -DUV_INCLUDE_DIR=path/to/libuv/include -DUV_LIBRARY=path/to/libuv.a`

## ghost | 2017-08-27T21:25:29+00:00
Thanks. cmake completed without problems.
Now when I do 'make' I get

Scanning dependencies of target jansson
[  1%] Building C object src/3rdparty/jansson/CMakeFiles/jansson.dir/dump.c.o
cc1: error: invalid option argument ‘-Ofast’
cc1: error: unrecognized command line option "-ftree-loop-if-convert-stores"
make[2]: *** [src/3rdparty/jansson/CMakeFiles/jansson.dir/dump.c.o] Error 1
make[1]: *** [src/3rdparty/jansson/CMakeFiles/jansson.dir/all] Error 2
make: *** [all] Error 2



## xmrig | 2017-08-27T21:55:01+00:00
What your compiler version? Probably to old compiler.

## ghost | 2017-08-28T21:03:44+00:00
Thanks for your reply. 
You are right, gcc was version 4.8
I installed version 5 in my home folder and added it to $PATH but still my system executes 'make' of the old version.
Any advice?

## xmrig | 2017-08-28T21:06:41+00:00
`cmake .. -DCMAKE_C_COMPILER=gcc-5 -DCMAKE_CXX_COMPILER=g++-5`
Or whatever you compiler named or full path.

## ghost | 2017-08-29T19:04:06+00:00
Thanks!

I followed your instructions and cmake finished ok.
Now, 'make' reaches 83% then gives me the following error:


[ 83%] Building CXX object CMakeFiles/xmrig.dir/src/Cpu.cpp.o
/home/user/xmrig/src/Summary.cpp: In function ‘void print_threads()’:
/home/user/xmrig/src/Summary.cpp:95:44: error: expected ‘)’ before ‘PRIX64’
         snprintf(buf, 32, ", affinity=0x%" PRIX64, Options::i()->affinity());
                                            ^
/home/user/xmrig/src/Summary.cpp:95:76: warning: spurious trailing ‘%’ in format [-Wformat=]
         snprintf(buf, 32, ", affinity=0x%" PRIX64, Options::i()->affinity());
                                                                            ^
/home/user/xmrig/src/Summary.cpp:95:76: warning: too many arguments for format [-Wformat-extra-args]
/home/user/xmrig/src/Summary.cpp:95:76: warning: spurious trailing ‘%’ in format [-Wformat=]
/home/user/xmrig/src/Summary.cpp:95:76: warning: too many arguments for format [-Wformat-extra-args]
make[2]: *** [CMakeFiles/xmrig.dir/src/Summary.cpp.o] Error 1
make[2]: *** Waiting for unfinished jobs....
[ 85%] Building C object CMakeFiles/xmrig.dir/src/crypto/c_keccak.c.o
[ 87%] Building C object CMakeFiles/xmrig.dir/src/crypto/c_groestl.c.o
/home/user/xmrig/src/net/Client.cpp: In member function ‘int64_t Client::submit(const JobResult&)’:
/home/user/xmrig/src/net/Client.cpp:174:36: error: expected ‘)’ before ‘PRIu64’
     snprintf(req, 345, "{\"id\":%" PRIu64 ",\"jsonrpc\":\"2.0\",\"method\":\"submit\",\"params\":{\"id\":\"%s\",\"job_id\":\"%s\",\"nonce\":\"%s\",\"result\":\"%s\"}}\n",
                                    ^
/home/user/xmrig/src/net/Client.cpp:175:60: warning: spurious trailing ‘%’ in format [-Wformat=]
              m_sequence, m_rpcId, result.jobId, nonce, data);
                                                            ^
/home/user/xmrig/src/net/Client.cpp:175:60: warning: too many arguments for format [-Wformat-extra-args]
/home/user/xmrig/src/net/Client.cpp:175:60: warning: spurious trailing ‘%’ in format [-Wformat=]
/home/user/xmrig/src/net/Client.cpp:175:60: warning: too many arguments for format [-Wformat-extra-args]
In file included from /home/user/xmrig/src/net/Client.cpp:29:0:
/home/user/xmrig/src/net/Client.cpp: In member function ‘void Client::parseNotification(const char*, const json_t*, const json_t*)’:
/home/user/xmrig/src/net/Client.cpp:351:54: error: expected ‘)’ before ‘PRId64’
             LOG_ERR("[%s:%u] error: \"%s\", code: %" PRId64, m_url.host(), m_url.port(), json_string_value(json_object_get(error, "message")), json_integer_value(json_object_get(error, "code")));
                                                      ^
/home/user/xmrig/src/log/Log.h:73:60: note: in definition of macro ‘LOG_ERR’
 #define LOG_ERR(x, ...)    Log::i()->message(Log::ERR,     x, ##__VA_ARGS__)
                                                            ^
/home/user/xmrig/src/net/Client.cpp: In member function ‘void Client::parseResponse(int64_t, const json_t*, const json_t*)’:
/home/user/xmrig/src/net/Client.cpp:384:54: error: expected ‘)’ before ‘PRId64’
             LOG_ERR("[%s:%u] error: \"%s\", code: %" PRId64, m_url.host(), m_url.port(), message, json_integer_value(json_object_get(error, "code")));
                                                      ^
/home/user/xmrig/src/log/Log.h:73:60: note: in definition of macro ‘LOG_ERR’
 #define LOG_ERR(x, ...)    Log::i()->message(Log::ERR,     x, ##__VA_ARGS__)
                                                            ^
/home/user/xmrig/src/net/Client.cpp: In member function ‘void Client::ping()’:
/home/user/xmrig/src/net/Client.cpp:425:36: error: expected ‘)’ before ‘PRId64’
     snprintf(req, 160, "{\"id\":%" PRId64 ",\"jsonrpc\":\"2.0\",\"method\":\"keepalived\",\"params\":{\"id\":\"%s\"}}\n", m_sequence, m_rpcId);
                                    ^
/home/user/xmrig/src/net/Client.cpp:425:142: warning: spurious trailing ‘%’ in format [-Wformat=]
     snprintf(req, 160, "{\"id\":%" PRId64 ",\"jsonrpc\":\"2.0\",\"method\":\"keepalived\",\"params\":{\"id\":\"%s\"}}\n", m_sequence, m_rpcId);
                                                                                                                                              ^
/home/user/xmrig/src/net/Client.cpp:425:142: warning: too many arguments for format [-Wformat-extra-args]
/home/user/xmrig/src/net/Client.cpp:425:142: warning: spurious trailing ‘%’ in format [-Wformat=]
/home/user/xmrig/src/net/Client.cpp:425:142: warning: too many arguments for format [-Wformat-extra-args]
In file included from /home/user/xmrig/src/net/Network.cpp:30:0:
/home/user/xmrig/src/net/Network.cpp: In member function ‘virtual void Network::onResultAccepted(Client*, int64_t, uint32_t, uint64_t, const char*)’:
/home/user/xmrig/src/net/Network.cpp:141:72: error: expected ‘:’ before ‘PRId64’
         LOG_INFO(m_options->colors() ? "\x1B[01;31mrejected\x1B[0m (%" PRId64 "/%" PRId64 ") diff \x1B[01;37m%u\x1B[0m \x1B[31m\"%s\"\x1B[0m \x1B[01;30m(%" PRIu64 " ms)"
                                                                        ^
/home/user/xmrig/src/log/Log.h:76:60: note: in definition of macro ‘LOG_INFO’
 #define LOG_INFO(x, ...)   Log::i()->message(Log::INFO,    x, ##__VA_ARGS__)
                                                            ^
/home/user/xmrig/src/net/Network.cpp:141:72: error: ‘PRId64’ was not declared in this scope
         LOG_INFO(m_options->colors() ? "\x1B[01;31mrejected\x1B[0m (%" PRId64 "/%" PRId64 ") diff \x1B[01;37m%u\x1B[0m \x1B[31m\"%s\"\x1B[0m \x1B[01;30m(%" PRIu64 " ms)"
                                                                        ^
/home/user/xmrig/src/log/Log.h:76:60: note: in definition of macro ‘LOG_INFO’
 #define LOG_INFO(x, ...)   Log::i()->message(Log::INFO,    x, ##__VA_ARGS__)
                                                            ^
/home/user/xmrig/src/net/Network.cpp:148:72: error: expected ‘:’ before ‘PRId64’
         LOG_INFO(m_options->colors() ? "\x1B[01;32maccepted\x1B[0m (%" PRId64 "/%" PRId64 ") diff \x1B[01;37m%u\x1B[0m \x1B[01;30m(%" PRIu64 " ms)"
                                                                        ^
/home/user/xmrig/src/log/Log.h:76:60: note: in definition of macro ‘LOG_INFO’
 #define LOG_INFO(x, ...)   Log::i()->message(Log::INFO,    x, ##__VA_ARGS__)
                                                            ^
/home/user/xmrig/src/net/Network.cpp:148:72: error: ‘PRId64’ was not declared in this scope
         LOG_INFO(m_options->colors() ? "\x1B[01;32maccepted\x1B[0m (%" PRId64 "/%" PRId64 ") diff \x1B[01;37m%u\x1B[0m \x1B[01;30m(%" PRIu64 " ms)"
                                                                        ^
/home/user/xmrig/src/log/Log.h:76:60: note: in definition of macro ‘LOG_INFO’
 #define LOG_INFO(x, ...)   Log::i()->message(Log::INFO,    x, ##__VA_ARGS__)
                                                            ^
make[2]: *** [CMakeFiles/xmrig.dir/src/net/Network.cpp.o] Error 1
make[2]: *** [CMakeFiles/xmrig.dir/src/net/Client.cpp.o] Error 1
make[1]: *** [CMakeFiles/xmrig.dir/all] Error 2
make: *** [all] Error 2


Your help is greatly appreciated.
Thanks!

## xmrig | 2017-08-29T20:44:04+00:00
Sorry I missed your reply. I made fix for this errors. Please check.

## ghost | 2017-08-29T21:00:04+00:00
No worries, thanks for your reply.

I just compiled the source again. Now I get the following error:

[100%] Linking CXX executable xmrig
/home/user/libuv/lib/libuv.a(libuv_la-linux-core.o): In function `uv_uptime':
/home/user/libuv-1.x/src/unix/linux-core.c:544: undefined reference to `clock_gettime'
/home/user/libuv-1.x/src/unix/linux-core.c:542: undefined reference to `clock_gettime'
/home/user/libuv/lib/libuv.a(libuv_la-linux-core.o): In function `uv__hrtime':
/home/user/libuv-1.x/src/unix/linux-core.c:468: undefined reference to `clock_gettime'
/home/user/libuv-1.x/src/unix/linux-core.c:456: undefined reference to `clock_getres'
collect2: error: ld returned 1 exit status
make[2]: *** [xmrig] Error 1
make[1]: *** [CMakeFiles/xmrig.dir/all] Error 2
make: *** [all] Error 2



## xmrig | 2017-08-29T21:26:32+00:00
That bad.
Try rebuild libuv with gcc5 `CC=gcc-5 ./configure && make`.
If it not help, remove this line https://github.com/xmrig/xmrig/blob/master/CMakeLists.txt#L153 or link with dynamic libuv.so.

Also what system is it?

## ghost | 2017-08-29T21:57:19+00:00
Thanks again.
I tried to rebuild libuv using gcc-5, I am getting multiple 'Assertion failed' instances and the make check ends with errors:

make[1]: *** [check-TESTS] Error 1
make[1]: Leaving directory `/home/user/libuv-1.14.0/build'
make: *** [check-am] Error 2
 
I tried to remove the line you mentioned in the CMakeLists but I am getting the same error.
The systemis CentOS 6.5 with kernel 2.6.32 
What else should I do?
Do you think it will work if I link with dynamic libuv.so? can you please give me some instructions on how to do the linking?

Thanks  

## xmrig | 2017-08-29T22:01:19+00:00
When run cmake `-DUV_LIBRARY=path/to/libuv.so`.
If it not help, I have no idea what to do next(
Later will try install CentOS.

## mnik247 | 2017-08-29T22:14:55+00:00
I recompiled libuv-1.10.2-1.el7.src.rpm (from EPEL repo for CentOS 7) on CentOS 6 and then use it.

## ghost | 2017-08-29T23:00:22+00:00
@mnik247 Thanks for the suggestion but i managed to rebuild libuv from source using gcc-5.

@xmrig  After reading a bit on stack exchange, I managed to solve the problem:
Before running cmake, I had to run `export LDFLAGS=-lrt`

Thanks a lot for all your help. Really appreciate it. 





## xmrig | 2017-08-29T23:08:01+00:00
Oh thank you `-lrt` exactly right solution.

## predatoryniple | 2017-10-17T16:55:14+00:00
The build error, please help
2>App.obj : error LNK2019: ссылка на неразрешенный внешний символ "public: __cdecl FileLog::FileLog(char const *)" (??0FileLog@@QEAA@PEBD@Z) в функции "public: __cdecl App::App(int,char * *)" (??0App@@QEAA@HPEAPEAD@Z)

## michaelpalumbo | 2018-03-11T17:43:04+00:00
I also had the same issue as OP, so I ran the brew install commands for libuv and libmicrohttp each separately and then tried cmake ..     cmake worked fine after, and the make did too. used a macbook from 2008. 

## vasilevskykv | 2018-10-29T06:02:14+00:00
Hello, how to install and compile  libuv. I have a problem in compilation of xmrrig:
Could NOT find UV (missing: UV_LIBRARY UV_INCLUDE_DIR)
Where can I write a path to UV_LIBRARY and UV_INCLUDE_DIR?

## vasilevskykv | 2018-10-29T06:10:08+00:00
cmake .. -DUV_INCLUDE_DIR=path/to/libuv/include -DUV_LIBRARY=path/to/libuv.a  doesn't work.
What do .. mean?
Besides I use Jetbrains CLion. 

## fant4545 | 2019-03-27T11:16:29+00:00
Hey. compile version of msvc ..
I enter the team
cmake .. -G "Visual Studio 15 2017 Win64" -DXMRIG_DEPS = C: \ xmrig-deps-3.3 \ msvc2017 \ x64

I get this output
# cmake. -G "Visual Studio 15 2017 Win64" -DXMRIG_DEPS = C: \ xmrig-deps-3.3 \ msvc2017 \ x64
- Selecting Windows SDK version 10.0.17763.0 to target Windows 6.1.7601.
-
The C compiler identification is MSVC 19.16.27027.1
- The CXX compiler identification is MSVC 19.16.27027.1
- Check for working C compiler: C: / Program Files (x86) / Microsoft Visual Studio / 2017 / Professional / VC / Tools / MSVC / 14.16.27023 / bin / Hostx86 / x64 / cl.exe
-
Check for working C compiler: C: / Program Files (x86) / Microsoft Visual Studio / 2017 / Professional / VC / Tools / MSVC / 14.16.27023 / bin / Hostx86 / x64 / cl.exe - works
- Detecting C compiler ABI info
- Detecting C compiler ABI info - done
- Detecting C compile features
- Detecting C compile features - done
-
Check for working CXX compiler: C: / Program Files (x86) / Microsoft Visual Studio / 2017 / Professional / VC / Tools / MSVC / 14.16.27023 / bin / Hostx86 / x64 / cl.exe
- Check for working CXX compiler: C: / Program Files (x86) / Microsoft Visual Studio / 2017 / Professional / VC / Tools / MSVC / 14.16.27023 / bin / Hostx86 / x64 / cl.exe - works
- Detecting CXX compiler ABI info
-
Detecting CXX compiler ABI info - done
- Detecting CXX compile features
- Detecting CXX compile features - done
CMake Error at C: /msys64/mingw64/share/cmake-3.13/Modules/FindPackageHandleStandardArgs.cmake: 137 (message):
  Could NOT find UV (missing: UV_LIBRARY)
Call Stack (most recent call first):
  C: / msys64 / mingw64 / share / cmake-3.
13 / Modules / FindPackageHandleStandardArgs.cmake: 378 (_FPHSA_FAILURE_MESSAGE)
  cmake / FindUV.cmake: 25 (find_package_handle_standard_args)
  CMakeLists.txt: 206 (find_package)


- Configuring incomplete, errors occurred!
See also "C: /xmrig-2.14.1/CMakeFiles/CMakeOutput.log".
What needs to be corrected for correct compilation?

## xmrig | 2019-03-27T11:25:51+00:00
For MSVC please use official cmake installed into Program Files not a MSYS2 version of cmake.
Thank you.

## Selausekut | 2021-06-22T19:45:22+00:00
compilation terminated.
make[2]: *** [CMakeFiles/xmrig.dir/build.make:154: CMakeFiles/xmrig.dir/src/base/io/Async.cpp.o] Error 1
make[1]: *** [CMakeFiles/Makefile2:74: CMakeFiles/xmrig.dir/all] Error 2
make: *** [Makefile:84: all] Error 2

# Action History
- Created by: ghost | 2017-08-27T20:56:00+00:00
- Closed at: 2017-10-02T12:02:10+00:00
