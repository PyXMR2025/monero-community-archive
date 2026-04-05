---
title: xmrig fails to build on Ubuntu?
source_url: https://github.com/xmrig/xmrig/issues/1279
author: unverified-contact
assignees: []
labels:
- libuv
created_at: '2019-11-13T02:26:55+00:00'
updated_at: '2019-11-13T04:59:50+00:00'
type: issue
status: closed
closed_at: '2019-11-13T04:59:49+00:00'
---

# Original Description
xmrig build fails for me with the error below on Ubuntu

I am running:
```
sudo apt-get install git build-essential cmake libuv1-dev libssl-dev libhwloc-dev
git clone https://github.com/xmrig/xmrig.git
cd xmrig && mkdir build && cd build
cmake ..
make
```

(To be sure I wasn't pulling code from the newer beta versions I also tried with the code from https://github.com/xmrig/xmrig/archive/v3.2.0.tar.gz and the same errors occurs).

```
[  5%] Building C object src/3rdparty/argon2/CMakeFiles/argon2-xop.dir/arch/x86_64/lib/argon2-xop.c.o
Linking C static library libargon2-xop.a
[  5%] Built target argon2-xop
Scanning dependencies of target argon2-avx512f
[  6%] Building C object src/3rdparty/argon2/CMakeFiles/argon2-avx512f.dir/arch/x86_64/lib/argon2-avx512f.c.o
Linking C static library libargon2-avx512f.a
[  6%] Built target argon2-avx512f
Scanning dependencies of target argon2
[  6%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/argon2.c.o
[  7%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/core.c.o
[  8%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/encoding.c.o
[  9%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/genkat.c.o
[  9%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/impl-select.c.o
[ 10%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/blake2/blake2.c.o
[ 11%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/arch/x86_64/lib/argon2-arch.c.o
[ 12%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/arch/x86_64/lib/cpu-flags.c.o
Linking C static library libargon2.a
[ 12%] Built target argon2
Scanning dependencies of target xmrig
[ 12%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuLaunchData.cpp.o
[ 13%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/Console.cpp.o
In file included from /root/xmrig-3.2.0/src/base/io/Console.cpp:28:0:
/root/xmrig-3.2.0/src/base/tools/Handle.h: In static member function ‘static void xmrig::Handle::close(T) [with T = uv_fs_event_s*]’:
/root/xmrig-3.2.0/src/base/tools/Handle.h:83:32: error: ‘uv_fs_event_stop’ was not declared in this scope
         uv_fs_event_stop(handle);
                                ^
/root/xmrig-3.2.0/src/base/io/Console.cpp: In constructor ‘xmrig::Console::Console(xmrig::IConsoleListener*)’:
/root/xmrig-3.2.0/src/base/io/Console.cpp:46:28: error: ‘UV_TTY_MODE_RAW’ was not declared in this scope
     uv_tty_set_mode(m_tty, UV_TTY_MODE_RAW);
                            ^
/root/xmrig-3.2.0/src/base/io/Console.cpp:47:97: error: invalid conversion from ‘void (*)(uv_handle_t*, size_t, uv_buf_t*) {aka void (*)(uv_handle_s*, long unsigned int, uv_buf_t*)}’ to ‘uv_alloc_cb {aka uv_buf_t (*)(uv_handle_s*, long unsigned int)}’ [-fpermissive]
     uv_read_start(reinterpret_cast<uv_stream_t*>(m_tty), Console::onAllocBuffer, Console::onRead);
                                                                                                 ^
In file included from /root/xmrig-3.2.0/src/base/io/Console.h:32:0,
                 from /root/xmrig-3.2.0/src/base/io/Console.cpp:26:
/usr/include/uv.h:593:15: error:   initializing argument 2 of ‘int uv_read_start(uv_stream_t*, uv_alloc_cb, uv_read_cb)’ [-fpermissive]
 UV_EXTERN int uv_read_start(uv_stream_t*, uv_alloc_cb alloc_cb,
               ^
/root/xmrig-3.2.0/src/base/io/Console.cpp:47:97: error: invalid conversion from ‘void (*)(uv_stream_t*, ssize_t, const uv_buf_t*) {aka void (*)(uv_stream_s*, long int, const uv_buf_t*)}’ to ‘uv_read_cb {aka void (*)(uv_stream_s*, long int, uv_buf_t)}’ [-fpermissive]
     uv_read_start(reinterpret_cast<uv_stream_t*>(m_tty), Console::onAllocBuffer, Console::onRead);
                                                                                                 ^
In file included from /root/xmrig-3.2.0/src/base/io/Console.h:32:0,
                 from /root/xmrig-3.2.0/src/base/io/Console.cpp:26:
/usr/include/uv.h:593:15: error:   initializing argument 3 of ‘int uv_read_start(uv_stream_t*, uv_alloc_cb, uv_read_cb)’ [-fpermissive]
 UV_EXTERN int uv_read_start(uv_stream_t*, uv_alloc_cb alloc_cb,
               ^
At global scope:
cc1plus: warning: unrecognized command line option "-Wno-class-memaccess" [enabled by default]
make[2]: *** [CMakeFiles/xmrig.dir/src/base/io/Console.cpp.o] Error 1
make[1]: *** [CMakeFiles/xmrig.dir/all] Error 2
make: *** [all] Error 2
```

```
root@ARB:~/xmrig-3.2.0/build# cat /etc/os-release
NAME="Ubuntu"
VERSION="14.04.6 LTS, Trusty Tahr"
ID=ubuntu
ID_LIKE=debian
PRETTY_NAME="Ubuntu 14.04.6 LTS"
VERSION_ID="14.04"
HOME_URL="http://www.ubuntu.com/"
SUPPORT_URL="http://help.ubuntu.com/"
BUG_REPORT_URL="http://bugs.launchpad.net/ubuntu/"
```

Any ideas?

# Discussion History
## xmrig | 2019-11-13T04:57:15+00:00
libuv1-dev package not available on Ubuntu 14.04, so you should build this library from source.
Thank you.

## unverified-contact | 2019-11-13T04:59:49+00:00
Apologies, Ubuntu 14 is super old and is actually EOL since April. I'll upgrade the dist first and then try again.

# Action History
- Created by: unverified-contact | 2019-11-13T02:26:55+00:00
- Closed at: 2019-11-13T04:59:49+00:00
