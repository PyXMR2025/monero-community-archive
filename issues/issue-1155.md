---
title: Compilation error on CentOS 6, cmake3
source_url: https://github.com/xmrig/xmrig/issues/1155
author: TheCHIM
assignees: []
labels: []
created_at: '2019-09-02T06:36:27+00:00'
updated_at: '2022-05-01T14:05:05+00:00'
type: issue
status: closed
closed_at: '2019-09-13T16:28:41+00:00'
---

# Original Description
sudo yum install -y epel-release
sudo yum install -y git make cmake gcc gcc-c++ libstdc++-static libmicrohttpd-devel libuv-static
git clone https://github.com/xmrig/xmrig.git
cd xmrig
mkdir build
cd build
scl enable devtoolset-7 bash
cmake3 .. -DCMAKE_BUILD_TYPE=Release -DUV_LIBRARY=/usr/lib64/libuv.a
make

as a result:
`[ 18%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/Console.cpp.o
In file included from /Bitcoin/xmrig/src/base/io/Console.cpp:28:0:
/Bitcoin/xmrig/src/base/tools/Handle.h: In static member function ‘static void xmrig::Handle::close(T) [with T = uv_fs_event_s*]’:
/Bitcoin/xmrig/src/base/tools/Handle.h:83:32: error: ‘uv_fs_event_stop’ was not declared in this scope
         uv_fs_event_stop(handle);
                                ^
/Bitcoin/xmrig/src/base/io/Console.cpp: In constructor ‘xmrig::Console::Console(xmrig::IConsoleListener*)’:
/Bitcoin/xmrig/src/base/io/Console.cpp:43:28: error: ‘UV_TTY_MODE_RAW’ was not declared in this scope
     uv_tty_set_mode(m_tty, UV_TTY_MODE_RAW);
                            ^~~~~~~~~~~~~~~
/Bitcoin/xmrig/src/base/io/Console.cpp:44:97: error: invalid conversion from ‘void (*)(uv_handle_t*, size_t, uv_buf_t*) {aka void (*)(uv_handle_s*, long unsigned int, uv_buf_t*)}’ to ‘uv_alloc_cb {aka uv_buf_t (*)(uv_handle_s*, long unsigned int)}’ [-fpermissive]
 einterpret_cast<uv_stream_t*>(m_tty), Console::onAllocBuffer, Console::onRead);
                                                                              ^
In file included from /Bitcoin/xmrig/src/base/io/Console.h:29:0,
                 from /Bitcoin/xmrig/src/base/io/Console.cpp:26:
/usr/include/uv.h:618:15: note:   initializing argument 2 of ‘int uv_read_start(uv_stream_t*, uv_alloc_cb, uv_read_cb)’
 UV_EXTERN int uv_read_start(uv_stream_t*, uv_alloc_cb alloc_cb,
               ^~~~~~~~~~~~~
/Bitcoin/xmrig/src/base/io/Console.cpp:44:97: error: invalid conversion from ‘void (*)(uv_stream_t*, ssize_t, const uv_buf_t*) {aka void (*)(uv_stream_s*, long int, const uv_buf_t*)}’ to ‘uv_read_cb {aka void (*)(uv_stream_s*, long int, uv_buf_t)}’ [-fpermissive]
 einterpret_cast<uv_stream_t*>(m_tty), Console::onAllocBuffer, Console::onRead);
                                                                              ^
In file included from /Bitcoin/xmrig/src/base/io/Console.h:29:0,
                 from /Bitcoin/xmrig/src/base/io/Console.cpp:26:
/usr/include/uv.h:618:15: note:   initializing argument 3 of ‘int uv_read_start(uv_stream_t*, uv_alloc_cb, uv_read_cb)’
 UV_EXTERN int uv_read_start(uv_stream_t*, uv_alloc_cb alloc_cb,
               ^~~~~~~~~~~~~
At global scope:
cc1plus: warning: unrecognized command line option ‘-Wno-class-memaccess’
CMakeFiles/xmrig.dir/build.make:86: recipe for target 'CMakeFiles/xmrig.dir/src/base/io/Console.cpp.o' failed
make[2]: *** [CMakeFiles/xmrig.dir/src/base/io/Console.cpp.o] Error 1
CMakeFiles/Makefile2:110: recipe for target 'CMakeFiles/xmrig.dir/all' failed
make[1]: *** [CMakeFiles/xmrig.dir/all] Error 2
Makefile:83: recipe for target 'all' failed
make: *** [all] Error 2
`

# Discussion History
## xmrig | 2019-09-02T08:33:51+00:00
Probably libuv too old, miner works only with 1.x.x and 0.10.x not supported.
Thank you.

## PRIV8TOOL | 2022-05-01T14:05:04+00:00
i got this error : 



[ 10%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/Async.cpp.o
In file included from /home/pi/xmrig/src/base/io/Async.cpp:23:
/home/pi/xmrig/src/base/tools/Handle.h: In static member function 'static void xmrig::Handle::close(T) [with T = uv_fs_event_s*]':
/home/pi/xmrig/src/base/tools/Handle.h:77:9: error: 'uv_fs_event_stop' was not declared in this scope
         uv_fs_event_stop(handle);
         ^~~~~~~~~~~~~~~~
/home/pi/xmrig/src/base/tools/Handle.h:77:9: note: suggested alternative: 'uv_fs_event_t'
         uv_fs_event_stop(handle);
         ^~~~~~~~~~~~~~~~
         uv_fs_event_t
/home/pi/xmrig/src/base/io/Async.cpp: In constructor 'xmrig::Async::Async(xmrig::Async::Callback)':
/home/pi/xmrig/src/base/io/Async.cpp:137:133: error: invalid user-defined conversion from 'xmrig::Async::Async(xmrig::Async::Callback)::<lambda(uv_async_t*)>' to 'uv_async_cb' {aka 'void (*)(uv_async_s*, int)'} [-fpermissive]
     uv_async_init(uv_default_loop(), d_ptr->async, [](uv_async_t *handle) { static_cast<Async *>(handle->data)->d_ptr->callback(); });
                                                                                                                                     ^
/home/pi/xmrig/src/base/io/Async.cpp:137:73: note: candidate is: 'xmrig::Async::Async(xmrig::Async::Callback)::<lambda(uv_async_t*)>::operator void (*)(uv_async_t*)() const' <near match>
     uv_async_init(uv_default_loop(), d_ptr->async, [](uv_async_t *handle) { static_cast<Async *>(handle->data)->d_ptr->callback(); });
                                                                         ^
/home/pi/xmrig/src/base/io/Async.cpp:137:73: note:   no known conversion from 'void (*)(uv_async_t*)' {aka 'void (*)(uv_async_s*)'} to 'uv_async_cb' {aka 'void (*)(uv_async_s*, int)'}
In file included from /home/pi/xmrig/src/base/tools/Handle.h:23,
                 from /home/pi/xmrig/src/base/io/Async.cpp:23:
/usr/include/uv.h:1211:15: note:   initializing argument 3 of 'int uv_async_init(uv_loop_t*, uv_async_t*, uv_async_cb)'
 UV_EXTERN int uv_async_init(uv_loop_t*, uv_async_t* async,
               ^~~~~~~~~~~~~
/home/pi/xmrig/src/base/io/Async.cpp: In constructor 'xmrig::Async::Async(xmrig::IAsyncListener*)':
/home/pi/xmrig/src/base/io/Async.cpp:147:142: error: invalid user-defined conversion from 'xmrig::Async::Async(xmrig::IAsyncListener*)::<lambda(uv_async_t*)>' to 'uv_async_cb' {aka 'void (*)(uv_async_s*, int)'} [-fpermissive]
     uv_async_init(uv_default_loop(), d_ptr->async, [](uv_async_t *handle) { static_cast<Async *>(handle->data)->d_ptr->listener->onAsync(); });
                                                                                                                                              ^
/home/pi/xmrig/src/base/io/Async.cpp:147:73: note: candidate is: 'xmrig::Async::Async(xmrig::IAsyncListener*)::<lambda(uv_async_t*)>::operator void (*)(uv_async_t*)() const' <near match>
     uv_async_init(uv_default_loop(), d_ptr->async, [](uv_async_t *handle) { static_cast<Async *>(handle->data)->d_ptr->listener->onAsync(); });
                                                                         ^
/home/pi/xmrig/src/base/io/Async.cpp:147:73: note:   no known conversion from 'void (*)(uv_async_t*)' {aka 'void (*)(uv_async_s*)'} to 'uv_async_cb' {aka 'void (*)(uv_async_s*, int)'}
In file included from /home/pi/xmrig/src/base/tools/Handle.h:23,
                 from /home/pi/xmrig/src/base/io/Async.cpp:23:
/usr/include/uv.h:1211:15: note:   initializing argument 3 of 'int uv_async_init(uv_loop_t*, uv_async_t*, uv_async_cb)'
 UV_EXTERN int uv_async_init(uv_loop_t*, uv_async_t* async,
               ^~~~~~~~~~~~~
make[2]: *** [CMakeFiles/xmrig.dir/build.make:154: CMakeFiles/xmrig.dir/src/base/io/Async.cpp.o] Error 1
make[1]: *** [CMakeFiles/Makefile2:140: CMakeFiles/xmrig.dir/all] Error 2
make: *** [Makefile:84: all] Error 2
pi@raspberrypi:~/xmrig/build $ perl -v

This is perl 5, version 28, subversion 1 (v5.28.1) built for arm-linux-gnueabihf-thread-multi-64int
(with 65 registered patches, see perl -V for more detail)

Copyright 1987-2018, Larry Wall

Perl may be copied only under the terms of either the Artistic License or the
GNU General Public License, which may be found in the Perl 5 source kit.

Complete documentation for Perl, including FAQ lists, should be found on
this system using "man perl" or "perldoc perl".  If you have access to the
Internet, point your browser at http://www.perl.org/, the Perl Home Page.

# Action History
- Created by: TheCHIM | 2019-09-02T06:36:27+00:00
- Closed at: 2019-09-13T16:28:41+00:00
