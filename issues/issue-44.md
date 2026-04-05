---
title: Can't build on Ubuntu
source_url: https://github.com/xmrig/xmrig/issues/44
author: jpascal
assignees: []
labels: []
created_at: '2017-07-20T16:38:31+00:00'
updated_at: '2017-07-29T04:51:09+00:00'
type: issue
status: closed
closed_at: '2017-07-29T04:51:09+00:00'
---

# Original Description
Can't build on Linux 3.19.0-66-generic #74~14.04.1-Ubuntu SMP Tue Jul 19 19:56:11 UTC 2016 x86_64 x86_64 x86_64 GNU/Linux

GCC:
```
gcc -v
Using built-in specs.
COLLECT_GCC=gcc
COLLECT_LTO_WRAPPER=/usr/lib/gcc/x86_64-linux-gnu/4.9/lto-wrapper
Target: x86_64-linux-gnu
Configured with: ../src/configure -v --with-pkgversion='Ubuntu 4.9.4-2ubuntu1~14.04.1' --with-bugurl=file:///usr/share/doc/gcc-4.9/README.Bugs --enable-languages=c,c++,java,go,d,fortran,objc,obj-c++ --prefix=/usr --program-suffix=-4.9 --enable-shared --enable-linker-build-id --libexecdir=/usr/lib --without-included-gettext --enable-threads=posix --with-gxx-include-dir=/usr/include/c++/4.9 --libdir=/usr/lib --enable-nls --with-sysroot=/ --enable-clocale=gnu --enable-libstdcxx-debug --enable-libstdcxx-time=yes --enable-gnu-unique-object --disable-vtable-verify --enable-plugin --with-system-zlib --disable-browser-plugin --enable-java-awt=gtk --enable-gtk-cairo --with-java-home=/usr/lib/jvm/java-1.5.0-gcj-4.9-amd64/jre --enable-java-home --with-jvm-root-dir=/usr/lib/jvm/java-1.5.0-gcj-4.9-amd64 --with-jvm-jar-dir=/usr/lib/jvm-exports/java-1.5.0-gcj-4.9-amd64 --with-arch-directory=amd64 --with-ecj-jar=/usr/share/java/eclipse-ecj.jar --enable-objc-gc --enable-multiarch --disable-werror --with-arch-32=i686 --with-abi=m64 --with-multilib-list=m32,m64,mx32 --enable-multilib --with-tune=generic --enable-checking=release --build=x86_64-linux-gnu --host=x86_64-linux-gnu --target=x86_64-linux-gnu
Thread model: posix
gcc version 4.9.4 (Ubuntu 4.9.4-2ubuntu1~14.04.1) 
```

Log:
``` 
Scanning dependencies of target jansson
[  2%] Building C object src/3rdparty/jansson/CMakeFiles/jansson.dir/hashtable.c.o
[  4%] Building C object src/3rdparty/jansson/CMakeFiles/jansson.dir/memory.c.o
[  6%] Building C object src/3rdparty/jansson/CMakeFiles/jansson.dir/dump.c.o
[  8%] Building C object src/3rdparty/jansson/CMakeFiles/jansson.dir/error.c.o
[ 10%] Building C object src/3rdparty/jansson/CMakeFiles/jansson.dir/strbuffer.c.o
[ 12%] Building C object src/3rdparty/jansson/CMakeFiles/jansson.dir/hashtable_seed.c.o
[ 14%] Building C object src/3rdparty/jansson/CMakeFiles/jansson.dir/load.c.o
[ 16%] Building C object src/3rdparty/jansson/CMakeFiles/jansson.dir/pack_unpack.c.o
[ 18%] Building C object src/3rdparty/jansson/CMakeFiles/jansson.dir/strconv.c.o
[ 20%] Building C object src/3rdparty/jansson/CMakeFiles/jansson.dir/value.c.o
[ 22%] Building C object src/3rdparty/jansson/CMakeFiles/jansson.dir/utf.c.o
Linking C static library libjansson.a
[ 22%] Built target jansson
Scanning dependencies of target cpuid
[ 24%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/cpuid_main.c.o
[ 26%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/asm-bits.c.o
[ 28%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/recog_amd.c.o
[ 30%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/recog_intel.c.o
[ 32%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/libcpuid_util.c.o
Linking C static library libcpuid.a
[ 32%] Built target cpuid
Scanning dependencies of target xmrig
[ 34%] Building CXX object CMakeFiles/xmrig.dir/src/App.cpp.o
[ 36%] Building CXX object CMakeFiles/xmrig.dir/src/log/ConsoleLog.cpp.o
[ 38%] Building CXX object CMakeFiles/xmrig.dir/src/log/FileLog.cpp.o
[ 40%] Building CXX object CMakeFiles/xmrig.dir/src/log/Log.cpp.o
[ 42%] Building CXX object CMakeFiles/xmrig.dir/src/Mem.cpp.o
[ 44%] Building CXX object CMakeFiles/xmrig.dir/src/net/Client.cpp.o
/home/jpascal/miner/xmrig/src/net/Client.cpp: In member function ‘int64_t Client::send(char*, size_t)’:
/home/jpascal/miner/xmrig/src/net/Client.cpp:112:119: error: invalid user-defined conversion from ‘Client::send(char*, size_t)::<lambda(uv_timer_t*)>’ to ‘uv_timer_cb {aka void (*)(uv_timer_s*, int)}’ [-fpermissive]
     uv_timer_start(&m_responseTimer, [](uv_timer_t *handle) { getClient(handle->data)->close(); }, kResponseTimeout, 0);
                                                                                                                       ^
/home/jpascal/miner/xmrig/src/net/Client.cpp:112:59: note: candidate is: Client::send(char*, size_t)::<lambda(uv_timer_t*)>::operator void (*)(uv_timer_t*)() const <near match>
     uv_timer_start(&m_responseTimer, [](uv_timer_t *handle) { getClient(handle->data)->close(); }, kResponseTimeout, 0);
                                                           ^
/home/jpascal/miner/xmrig/src/net/Client.cpp:112:59: note:   no known conversion from ‘void (*)(uv_timer_t*) {aka void (*)(uv_timer_s*)}’ to ‘uv_timer_cb {aka void (*)(uv_timer_s*, int)}’
/home/jpascal/miner/xmrig/src/net/Client.cpp: In member function ‘int64_t Client::submit(const JobResult&)’:
/home/jpascal/miner/xmrig/src/net/Client.cpp:176:60: warning: format ‘%llu’ expects argument of type ‘long long unsigned int’, but argument 4 has type ‘int64_t {aka long int}’ [-Wformat=]
              m_sequence, m_rpcId, result.jobId, nonce, data);
                                                            ^
/home/jpascal/miner/xmrig/src/net/Client.cpp:176:60: warning: format ‘%llu’ expects argument of type ‘long long unsigned int’, but argument 4 has type ‘int64_t {aka long int}’ [-Wformat=]
In file included from /home/jpascal/miner/xmrig/src/net/Client.cpp:30:0:
/home/jpascal/miner/xmrig/src/net/Client.cpp: In member function ‘int Client::resolve(const char*)’:
/home/jpascal/miner/xmrig/src/net/Client.cpp:239:91: error: could not convert ‘r’ from ‘const int’ to ‘uv_err_t {aka uv_err_s}’
             LOG_ERR("[%s:%u] getaddrinfo error: \"%s\"", host, m_url.port(), uv_strerror(r));
                                                                                           ^
/home/jpascal/miner/xmrig/src/log/Log.h:73:65: note: in definition of macro ‘LOG_ERR’
 #define LOG_ERR(x, ...)    Log::i()->message(Log::ERR,     x, ##__VA_ARGS__)
                                                                 ^
/home/jpascal/miner/xmrig/src/net/Client.cpp: In member function ‘void Client::connect(sockaddr*)’:
/home/jpascal/miner/xmrig/src/net/Client.cpp:282:93: error: could not convert ‘(const sockaddr*)addr’ from ‘const sockaddr*’ to ‘sockaddr_in’
     uv_tcp_connect(req, m_socket, reinterpret_cast<const sockaddr*>(addr), Client::onConnect);
                                                                                             ^
/home/jpascal/miner/xmrig/src/net/Client.cpp: In member function ‘void Client::ping()’:
/home/jpascal/miner/xmrig/src/net/Client.cpp:421:135: warning: format ‘%lld’ expects argument of type ‘long long int’, but argument 4 has type ‘int64_t {aka long int}’ [-Wformat=]
     snprintf(req, 128, "{\"id\":%lld,\"jsonrpc\":\"2.0\",\"method\":\"keepalived\",\"params\":{\"id\":\"%s\"}}\n", m_sequence, m_rpcId);
                                                                                                                                       ^
/home/jpascal/miner/xmrig/src/net/Client.cpp:421:135: warning: format ‘%lld’ expects argument of type ‘long long int’, but argument 4 has type ‘int64_t {aka long int}’ [-Wformat=]
/home/jpascal/miner/xmrig/src/net/Client.cpp: In member function ‘void Client::reconnect()’:
/home/jpascal/miner/xmrig/src/net/Client.cpp:443:116: error: invalid user-defined conversion from ‘Client::reconnect()::<lambda(uv_timer_t*)>’ to ‘uv_timer_cb {aka void (*)(uv_timer_s*, int)}’ [-fpermissive]
     uv_timer_start(&m_retriesTimer, [](uv_timer_t *handle) { getClient(handle->data)->connect(); }, m_retryPause, 0);
                                                                                                                    ^
/home/jpascal/miner/xmrig/src/net/Client.cpp:443:58: note: candidate is: Client::reconnect()::<lambda(uv_timer_t*)>::operator void (*)(uv_timer_t*)() const <near match>
     uv_timer_start(&m_retriesTimer, [](uv_timer_t *handle) { getClient(handle->data)->connect(); }, m_retryPause, 0);
                                                          ^
/home/jpascal/miner/xmrig/src/net/Client.cpp:443:58: note:   no known conversion from ‘void (*)(uv_timer_t*) {aka void (*)(uv_timer_s*)}’ to ‘uv_timer_cb {aka void (*)(uv_timer_s*, int)}’
/home/jpascal/miner/xmrig/src/net/Client.cpp: In member function ‘void Client::startTimeout()’:
/home/jpascal/miner/xmrig/src/net/Client.cpp:466:120: error: invalid user-defined conversion from ‘Client::startTimeout()::<lambda(uv_timer_t*)>’ to ‘uv_timer_cb {aka void (*)(uv_timer_s*, int)}’ [-fpermissive]
     uv_timer_start(&m_keepAliveTimer, [](uv_timer_t *handle) { getClient(handle->data)->ping(); }, kKeepAliveTimeout, 0);
                                                                                                                        ^
/home/jpascal/miner/xmrig/src/net/Client.cpp:466:60: note: candidate is: Client::startTimeout()::<lambda(uv_timer_t*)>::operator void (*)(uv_timer_t*)() const <near match>
     uv_timer_start(&m_keepAliveTimer, [](uv_timer_t *handle) { getClient(handle->data)->ping(); }, kKeepAliveTimeout, 0);
                                                            ^
/home/jpascal/miner/xmrig/src/net/Client.cpp:466:60: note:   no known conversion from ‘void (*)(uv_timer_t*) {aka void (*)(uv_timer_s*)}’ to ‘uv_timer_cb {aka void (*)(uv_timer_s*, int)}’
In file included from /home/jpascal/miner/xmrig/src/net/Client.cpp:30:0:
/home/jpascal/miner/xmrig/src/net/Client.cpp: In static member function ‘static void Client::onConnect(uv_connect_t*, int)’:
/home/jpascal/miner/xmrig/src/net/Client.cpp:498:116: error: could not convert ‘status’ from ‘int’ to ‘uv_err_t {aka uv_err_s}’
             LOG_ERR("[%s:%u] connect error: \"%s\"", client->m_url.host(), client->m_url.port(), uv_strerror(status));
                                                                                                                    ^
/home/jpascal/miner/xmrig/src/log/Log.h:73:65: note: in definition of macro ‘LOG_ERR’
 #define LOG_ERR(x, ...)    Log::i()->message(Log::ERR,     x, ##__VA_ARGS__)
                                                                 ^
/home/jpascal/miner/xmrig/src/net/Client.cpp:510:74: error: invalid conversion from ‘void (*)(uv_handle_t*, size_t, uv_buf_t*) {aka void (*)(uv_handle_s*, long unsigned int, uv_buf_t*)}’ to ‘uv_alloc_cb {aka uv_buf_t (*)(uv_handle_s*, long unsigned int)}’ [-fpermissive]
     uv_read_start(client->m_stream, Client::onAllocBuffer, Client::onRead);
                                                                          ^
In file included from /home/jpascal/miner/xmrig/src/log/Log.h:28:0,
                 from /home/jpascal/miner/xmrig/src/net/Client.cpp:30:
/usr/include/uv.h:593:15: note: initializing argument 2 of ‘int uv_read_start(uv_stream_t*, uv_alloc_cb, uv_read_cb)’
 UV_EXTERN int uv_read_start(uv_stream_t*, uv_alloc_cb alloc_cb,
               ^
/home/jpascal/miner/xmrig/src/net/Client.cpp:510:74: error: invalid conversion from ‘void (*)(uv_stream_t*, ssize_t, const uv_buf_t*) {aka void (*)(uv_stream_s*, long int, const uv_buf_t*)}’ to ‘uv_read_cb {aka void (*)(uv_stream_s*, long int, uv_buf_t)}’ [-fpermissive]
     uv_read_start(client->m_stream, Client::onAllocBuffer, Client::onRead);
                                                                          ^
In file included from /home/jpascal/miner/xmrig/src/log/Log.h:28:0,
                 from /home/jpascal/miner/xmrig/src/net/Client.cpp:30:
/usr/include/uv.h:593:15: note: initializing argument 3 of ‘int uv_read_start(uv_stream_t*, uv_alloc_cb, uv_read_cb)’
 UV_EXTERN int uv_read_start(uv_stream_t*, uv_alloc_cb alloc_cb,
               ^
In file included from /home/jpascal/miner/xmrig/src/net/Client.cpp:30:0:
/home/jpascal/miner/xmrig/src/net/Client.cpp: In static member function ‘static void Client::onRead(uv_stream_t*, ssize_t, const uv_buf_t*)’:
/home/jpascal/miner/xmrig/src/net/Client.cpp:522:112: error: could not convert ‘nread’ from ‘ssize_t {aka long int}’ to ‘uv_err_t {aka uv_err_s}’
             LOG_ERR("[%s:%u] read error: \"%s\"", client->m_url.host(), client->m_url.port(), uv_strerror(nread));
                                                                                                                ^
/home/jpascal/miner/xmrig/src/log/Log.h:73:65: note: in definition of macro ‘LOG_ERR’
 #define LOG_ERR(x, ...)    Log::i()->message(Log::ERR,     x, ##__VA_ARGS__)
                                                                 ^
/home/jpascal/miner/xmrig/src/net/Client.cpp: In static member function ‘static void Client::onResolved(uv_getaddrinfo_t*, int, addrinfo*)’:
/home/jpascal/miner/xmrig/src/net/Client.cpp:561:108: error: could not convert ‘status’ from ‘int’ to ‘uv_err_t {aka uv_err_s}’
         LOG_ERR("[%s:%u] DNS error: \"%s\"", client->m_url.host(), client->m_url.port(), uv_strerror(status));
                                                                                                            ^
/home/jpascal/miner/xmrig/src/log/Log.h:73:65: note: in definition of macro ‘LOG_ERR’
 #define LOG_ERR(x, ...)    Log::i()->message(Log::ERR,     x, ##__VA_ARGS__)
                                                                 ^
make[2]: *** [CMakeFiles/xmrig.dir/src/net/Client.cpp.o] Ошибка 1
make[1]: *** [CMakeFiles/xmrig.dir/all] Ошибка 2
make: *** [all] Ошибка 2
```

# Discussion History
## xmrig | 2017-07-20T16:54:31+00:00
You need gcc/g++ version 5.4 or newer.

## jpascal | 2017-07-20T17:09:00+00:00
I build success on 4.9 after reinstall libuv from sources from github. Thanks

## xmrig | 2017-07-20T17:31:28+00:00
Thank you little surprised, that old gcc fine too.

# Action History
- Created by: jpascal | 2017-07-20T16:38:31+00:00
- Closed at: 2017-07-29T04:51:09+00:00
