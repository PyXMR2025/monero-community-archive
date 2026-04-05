---
title: 'xmrig/src/base/io/Console.h:32:10: fatal error: uv.h: No such file or directory'
source_url: https://github.com/xmrig/xmrig/issues/1896
author: Sharaykaka
assignees: []
labels: []
created_at: '2020-10-14T18:28:20+00:00'
updated_at: '2020-11-26T10:34:38+00:00'
type: issue
status: closed
closed_at: '2020-11-26T10:34:38+00:00'
---

# Original Description
steps i did:

- apt-get update
- 
- 
- apt-get install build-essential git cmake libuvl-dev libssl-dev libhwloc-dev -y
- 
- apt-get install libcurl4-openssl-dev
- 
- git clone http://github.com/xmrig/xmrig.git
- 
- cd xmrig;mkdir build;cd build
- 
- cmake .. -DUV_INCLUDE_DIR=path/to/libuv/include -DUV_LIBRARY=path/to/libuv.a
- 
(everything went fine till here)
- 
- make



Output:


Scanning dependencies of target ethash
[  0%] Building C object src/3rdparty/libethash/CMakeFiles/ethash.dir/ethash_internal.c.o
[  1%] Building C object src/3rdparty/libethash/CMakeFiles/ethash.dir/keccakf800.c.o
[  1%] Linking C static library libethash.a
[  1%] Built target ethash
Scanning dependencies of target xmrig-asm
[  2%] Building ASM object CMakeFiles/xmrig-asm.dir/src/crypto/cn/asm/cn_main_loop.S.o
[  2%] Building ASM object CMakeFiles/xmrig-asm.dir/src/crypto/cn/asm/CryptonightR_template.S.o
[  3%] Linking C static library libxmrig-asm.a
[  3%] Built target xmrig-asm
Scanning dependencies of target argon2-sse2
[  4%] Building C object src/3rdparty/argon2/CMakeFiles/argon2-sse2.dir/arch/x86_64/lib/argon2-sse2.c.o
[  4%] Linking C static library libargon2-sse2.a
[  4%] Built target argon2-sse2
Scanning dependencies of target argon2-avx512f
[  4%] Building C object src/3rdparty/argon2/CMakeFiles/argon2-avx512f.dir/arch/x86_64/lib/argon2-avx512f.c.o
[  4%] Linking C static library libargon2-avx512f.a
[  4%] Built target argon2-avx512f
Scanning dependencies of target argon2-avx2
[  4%] Building C object src/3rdparty/argon2/CMakeFiles/argon2-avx2.dir/arch/x86_64/lib/argon2-avx2.c.o
[  5%] Linking C static library libargon2-avx2.a
[  5%] Built target argon2-avx2
Scanning dependencies of target argon2-xop
[  6%] Building C object src/3rdparty/argon2/CMakeFiles/argon2-xop.dir/arch/x86_64/lib/argon2-xop.c.o
[  6%] Linking C static library libargon2-xop.a
[  6%] Built target argon2-xop
Scanning dependencies of target argon2-ssse3
[  7%] Building C object src/3rdparty/argon2/CMakeFiles/argon2-ssse3.dir/arch/x86_64/lib/argon2-ssse3.c.o
[  7%] Linking C static library libargon2-ssse3.a
[  7%] Built target argon2-ssse3
Scanning dependencies of target argon2
[  7%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/argon2.c.o
[  7%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/core.c.o
[  8%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/encoding.c.o
[  8%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/genkat.c.o
[  9%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/impl-select.c.o
[  9%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/blake2/blake2.c.o
[  9%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/arch/x86_64/lib/argon2-arch.c.o
[ 10%] Linking C static library libargon2.a
[ 10%] Built target argon2
Scanning dependencies of target xmrig
[ 11%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuLaunchData.cpp.o
[ 11%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/rx/HashAesKernel.cpp.o
[ 11%] Building CXX object CMakeFiles/xmrig.dir/src/base/crypto/Algorithm.cpp.o
[ 12%] Building CXX object CMakeFiles/xmrig.dir/src/base/crypto/Coin.cpp.o
[ 12%] Building CXX object CMakeFiles/xmrig.dir/src/base/crypto/keccak.cpp.o
[ 13%] Building CXX object CMakeFiles/xmrig.dir/src/base/crypto/sha3.cpp.o
[ 13%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/Console.cpp.o
In file included from /content/xmrig/src/base/io/Console.cpp:26:0:
/content/xmrig/src/base/io/Console.h:32:10: fatal error: uv.h: No such file or directory
 #include <uv.h>
          ^~~~~~
compilation terminated.
CMakeFiles/xmrig.dir/build.make:140: recipe for target 'CMakeFiles/xmrig.dir/src/base/io/Console.cpp.o' failed
make[2]: *** [CMakeFiles/xmrig.dir/src/base/io/Console.cpp.o] Error 1
CMakeFiles/Makefile2:79: recipe for target 'CMakeFiles/xmrig.dir/all' failed
make[1]: *** [CMakeFiles/xmrig.dir/all] Error 2
Makefile:83: recipe for target 'all' failed
make: *** [all] Error 2

I am Using Ubuntu 

# Discussion History
## Saikatsaha1996 | 2020-10-14T18:32:36+00:00
> steps i did:
> 
> * apt-get update
> * apt-get install build-essential git cmake libuvl-dev libssl-dev libhwloc-dev -y
> * apt-get install libcurl4-openssl-dev
> * git clone [http://github.com/xmrig/xmrig.git](https://github.com/xmrig/xmrig.git)
> * cd xmrig;mkdir build;cd build
> * cmake .. -DUV_INCLUDE_DIR=path/to/libuv/include -DUV_LIBRARY=path/to/libuv.a
> 
> ## (everything went fine till here)
> * make
> 
> Output:
> 
> Scanning dependencies of target ethash
> [ 0%] Building C object src/3rdparty/libethash/CMakeFiles/ethash.dir/ethash_internal.c.o
> [ 1%] Building C object src/3rdparty/libethash/CMakeFiles/ethash.dir/keccakf800.c.o
> [ 1%] Linking C static library libethash.a
> [ 1%] Built target ethash
> Scanning dependencies of target xmrig-asm
> [ 2%] Building ASM object CMakeFiles/xmrig-asm.dir/src/crypto/cn/asm/cn_main_loop.S.o
> [ 2%] Building ASM object CMakeFiles/xmrig-asm.dir/src/crypto/cn/asm/CryptonightR_template.S.o
> [ 3%] Linking C static library libxmrig-asm.a
> [ 3%] Built target xmrig-asm
> Scanning dependencies of target argon2-sse2
> [ 4%] Building C object src/3rdparty/argon2/CMakeFiles/argon2-sse2.dir/arch/x86_64/lib/argon2-sse2.c.o
> [ 4%] Linking C static library libargon2-sse2.a
> [ 4%] Built target argon2-sse2
> Scanning dependencies of target argon2-avx512f
> [ 4%] Building C object src/3rdparty/argon2/CMakeFiles/argon2-avx512f.dir/arch/x86_64/lib/argon2-avx512f.c.o
> [ 4%] Linking C static library libargon2-avx512f.a
> [ 4%] Built target argon2-avx512f
> Scanning dependencies of target argon2-avx2
> [ 4%] Building C object src/3rdparty/argon2/CMakeFiles/argon2-avx2.dir/arch/x86_64/lib/argon2-avx2.c.o
> [ 5%] Linking C static library libargon2-avx2.a
> [ 5%] Built target argon2-avx2
> Scanning dependencies of target argon2-xop
> [ 6%] Building C object src/3rdparty/argon2/CMakeFiles/argon2-xop.dir/arch/x86_64/lib/argon2-xop.c.o
> [ 6%] Linking C static library libargon2-xop.a
> [ 6%] Built target argon2-xop
> Scanning dependencies of target argon2-ssse3
> [ 7%] Building C object src/3rdparty/argon2/CMakeFiles/argon2-ssse3.dir/arch/x86_64/lib/argon2-ssse3.c.o
> [ 7%] Linking C static library libargon2-ssse3.a
> [ 7%] Built target argon2-ssse3
> Scanning dependencies of target argon2
> [ 7%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/argon2.c.o
> [ 7%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/core.c.o
> [ 8%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/encoding.c.o
> [ 8%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/genkat.c.o
> [ 9%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/impl-select.c.o
> [ 9%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/blake2/blake2.c.o
> [ 9%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/arch/x86_64/lib/argon2-arch.c.o
> [ 10%] Linking C static library libargon2.a
> [ 10%] Built target argon2
> Scanning dependencies of target xmrig
> [ 11%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuLaunchData.cpp.o
> [ 11%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/rx/HashAesKernel.cpp.o
> [ 11%] Building CXX object CMakeFiles/xmrig.dir/src/base/crypto/Algorithm.cpp.o
> [ 12%] Building CXX object CMakeFiles/xmrig.dir/src/base/crypto/Coin.cpp.o
> [ 12%] Building CXX object CMakeFiles/xmrig.dir/src/base/crypto/keccak.cpp.o
> [ 13%] Building CXX object CMakeFiles/xmrig.dir/src/base/crypto/sha3.cpp.o
> [ 13%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/Console.cpp.o
> In file included from /content/xmrig/src/base/io/Console.cpp:26:0:
> /content/xmrig/src/base/io/Console.h:32:10: fatal error: uv.h: No such file or directory
> #include <uv.h>
> ^~~~~~
> compilation terminated.
> CMakeFiles/xmrig.dir/build.make:140: recipe for target 'CMakeFiles/xmrig.dir/src/base/io/Console.cpp.o' failed
> make[2]: *** [CMakeFiles/xmrig.dir/src/base/io/Console.cpp.o] Error 1
> CMakeFiles/Makefile2:79: recipe for target 'CMakeFiles/xmrig.dir/all' failed
> make[1]: *** [CMakeFiles/xmrig.dir/all] Error 2
> Makefile:83: recipe for target 'all' failed
> make: *** [all] Error 2
> 
> I am Using Ubuntu


1) pkg upgrade -y
2) pkg install git cmake libuv clang nano -y
3) git clone --single-branch https://github.com/xmrig/xmrig.git
4) cd xmrig
5) mkdir build && cd build
6) cmake .. -DWITH_HTTPD=OFF -DWITH_TLS=OFF -DWITH_OPENCL=OFF -DWITH_CUDA=OFF -DCMAKE_BUILD_TYPE=Release -DWITH_HWLOC=OFF
7) ls
8) make 
9) cp ../src/config.json config.json
10) nano config.json

11) donate.v2.xmrig.com:3333
12) xmr.pool.minergate.com:45700
13) CONTROL+\ ,donate.v2.xmrig.com:3333, replace with ( your pool address ) , y enter
14) Control +\ , and past   YOUR_WALLET_ADDRESS , replace with ( your user name or wallet address) , y enter, and scroll down and check your all details.. 
15) control + x 
16) y enter
17) ./xmrig-notls
28) enjoy...!

## Sharaykaka | 2020-10-14T18:50:02+00:00
Thanks for the response @Saikatsaha1996

but I ran into another error

after 

make

Scanning dependencies of target ethash
[  0%] Building C object src/3rdparty/libethash/CMakeFiles/ethash.dir/ethash_internal.c.o
[  1%] Building C object src/3rdparty/libethash/CMakeFiles/ethash.dir/keccakf800.c.o
[  1%] Linking C static library libethash.a
[  1%] Built target ethash
Scanning dependencies of target xmrig-asm
[  2%] Building ASM object CMakeFiles/xmrig-asm.dir/src/crypto/cn/asm/cn_main_loop.S.o
[  3%] Building ASM object CMakeFiles/xmrig-asm.dir/src/crypto/cn/asm/CryptonightR_template.S.o
[  3%] Linking C static library libxmrig-asm.a
[  3%] Built target xmrig-asm
Scanning dependencies of target cpuid
[  4%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/cpuid_main.c.o
[  4%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/asm-bits.c.o
[  5%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/recog_amd.c.o
[  6%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/recog_intel.c.o
[  6%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/libcpuid_util.c.o
[  7%] Linking C static library libcpuid.a
[  7%] Built target cpuid
Scanning dependencies of target argon2-sse2
[  7%] Building C object src/3rdparty/argon2/CMakeFiles/argon2-sse2.dir/arch/x86_64/lib/argon2-sse2.c.o
[  8%] Linking C static library libargon2-sse2.a
[  8%] Built target argon2-sse2
Scanning dependencies of target argon2-avx512f
[  9%] Building C object src/3rdparty/argon2/CMakeFiles/argon2-avx512f.dir/arch/x86_64/lib/argon2-avx512f.c.o
[ 10%] Linking C static library libargon2-avx512f.a
[ 10%] Built target argon2-avx512f
Scanning dependencies of target argon2-avx2
[ 11%] Building C object src/3rdparty/argon2/CMakeFiles/argon2-avx2.dir/arch/x86_64/lib/argon2-avx2.c.o
[ 11%] Linking C static library libargon2-avx2.a
[ 11%] Built target argon2-avx2
Scanning dependencies of target argon2-xop
[ 12%] Building C object src/3rdparty/argon2/CMakeFiles/argon2-xop.dir/arch/x86_64/lib/argon2-xop.c.o
[ 12%] Linking C static library libargon2-xop.a
[ 12%] Built target argon2-xop
Scanning dependencies of target argon2-ssse3
[ 12%] Building C object src/3rdparty/argon2/CMakeFiles/argon2-ssse3.dir/arch/x86_64/lib/argon2-ssse3.c.o
[ 13%] Linking C static library libargon2-ssse3.a
[ 13%] Built target argon2-ssse3
Scanning dependencies of target argon2
[ 13%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/argon2.c.o
[ 14%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/core.c.o
[ 14%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/encoding.c.o
[ 15%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/genkat.c.o
[ 15%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/impl-select.c.o
[ 16%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/blake2/blake2.c.o
[ 17%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/arch/x86_64/lib/argon2-arch.c.o
[ 17%] Linking C static library libargon2.a
[ 17%] Built target argon2
Scanning dependencies of target xmrig-notls
[ 18%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/cpu/CpuLaunchData.cpp.o
[ 18%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/crypto/Algorithm.cpp.o
[ 19%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/crypto/Coin.cpp.o
[ 20%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/crypto/keccak.cpp.o
[ 20%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/crypto/sha3.cpp.o
[ 21%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/io/Console.cpp.o
In file included from /content/xmrig/src/base/io/Console.cpp:28:0:
/content/xmrig/src/base/tools/Handle.h: In static member function ‘static void xmrig::Handle::close(T) [with T = uv_fs_event_s*]’:
/content/xmrig/src/base/tools/Handle.h:83:9: error: ‘uv_fs_event_stop’ was not declared in this scope
         uv_fs_event_stop(handle);
         ^~~~~~~~~~~~~~~~
/content/xmrig/src/base/tools/Handle.h:83:9: note: suggested alternative: ‘uv_fs_event_t’
         uv_fs_event_stop(handle);
         ^~~~~~~~~~~~~~~~
         uv_fs_event_t
/content/xmrig/src/base/io/Console.cpp: In constructor ‘xmrig::Console::Console(xmrig::IConsoleListener*)’:
/content/xmrig/src/base/io/Console.cpp:46:28: error: ‘UV_TTY_MODE_RAW’ was not declared in this scope
     uv_tty_set_mode(m_tty, UV_TTY_MODE_RAW);
                            ^~~~~~~~~~~~~~~
/content/xmrig/src/base/io/Console.cpp:47:97: error: invalid conversion from ‘void (*)(uv_handle_t*, size_t, uv_buf_t*) {aka void (*)(uv_handle_s*, long unsigned int, uv_buf_t*)}’ to ‘uv_alloc_cb {aka uv_buf_t (*)(uv_handle_s*, long unsigned int)}’ [-fpermissive]
     uv_read_start(reinterpret_cast<uv_stream_t*>(m_tty), Console::onAllocBuffer, Console::onRead);
                                                                                                 ^
In file included from /content/xmrig/src/base/io/Console.h:32:0,
                 from /content/xmrig/src/base/io/Console.cpp:26:
/usr/include/uv.h:618:15: note:   initializing argument 2 of ‘int uv_read_start(uv_stream_t*, uv_alloc_cb, uv_read_cb)’
 UV_EXTERN int uv_read_start(uv_stream_t*, uv_alloc_cb alloc_cb,
               ^~~~~~~~~~~~~
/content/xmrig/src/base/io/Console.cpp:47:97: error: invalid conversion from ‘void (*)(uv_stream_t*, ssize_t, const uv_buf_t*) {aka void (*)(uv_stream_s*, long int, const uv_buf_t*)}’ to ‘uv_read_cb {aka void (*)(uv_stream_s*, long int, uv_buf_t)}’ [-fpermissive]
     uv_read_start(reinterpret_cast<uv_stream_t*>(m_tty), Console::onAllocBuffer, Console::onRead);
                                                                                                 ^
In file included from /content/xmrig/src/base/io/Console.h:32:0,
                 from /content/xmrig/src/base/io/Console.cpp:26:
/usr/include/uv.h:618:15: note:   initializing argument 3 of ‘int uv_read_start(uv_stream_t*, uv_alloc_cb, uv_read_cb)’
 UV_EXTERN int uv_read_start(uv_stream_t*, uv_alloc_cb alloc_cb,
               ^~~~~~~~~~~~~
At global scope:
cc1plus: warning: unrecognized command line option ‘-Wno-class-memaccess’
CMakeFiles/xmrig-notls.dir/build.make:127: recipe for target 'CMakeFiles/xmrig-notls.dir/src/base/io/Console.cpp.o' failed
make[2]: *** [CMakeFiles/xmrig-notls.dir/src/base/io/Console.cpp.o] Error 1
CMakeFiles/Makefile2:80: recipe for target 'CMakeFiles/xmrig-notls.dir/all' failed
make[1]: *** [CMakeFiles/xmrig-notls.dir/all] Error 2
Makefile:83: recipe for target 'all' failed
make: *** [all] Error 2


## Saikatsaha1996 | 2020-10-14T18:53:32+00:00
> Thanks for the response
> 
> but I ran into another error
> 
> after
> 
> make
> 
> Scanning dependencies of target ethash
> [ 0%] Building C object src/3rdparty/libethash/CMakeFiles/ethash.dir/ethash_internal.c.o
> [ 1%] Building C object src/3rdparty/libethash/CMakeFiles/ethash.dir/keccakf800.c.o
> [ 1%] Linking C static library libethash.a
> [ 1%] Built target ethash
> Scanning dependencies of target xmrig-asm
> [ 2%] Building ASM object CMakeFiles/xmrig-asm.dir/src/crypto/cn/asm/cn_main_loop.S.o
> [ 3%] Building ASM object CMakeFiles/xmrig-asm.dir/src/crypto/cn/asm/CryptonightR_template.S.o
> [ 3%] Linking C static library libxmrig-asm.a
> [ 3%] Built target xmrig-asm
> Scanning dependencies of target cpuid
> [ 4%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/cpuid_main.c.o
> [ 4%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/asm-bits.c.o
> [ 5%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/recog_amd.c.o
> [ 6%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/recog_intel.c.o
> [ 6%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/libcpuid_util.c.o
> [ 7%] Linking C static library libcpuid.a
> [ 7%] Built target cpuid
> Scanning dependencies of target argon2-sse2
> [ 7%] Building C object src/3rdparty/argon2/CMakeFiles/argon2-sse2.dir/arch/x86_64/lib/argon2-sse2.c.o
> [ 8%] Linking C static library libargon2-sse2.a
> [ 8%] Built target argon2-sse2
> Scanning dependencies of target argon2-avx512f
> [ 9%] Building C object src/3rdparty/argon2/CMakeFiles/argon2-avx512f.dir/arch/x86_64/lib/argon2-avx512f.c.o
> [ 10%] Linking C static library libargon2-avx512f.a
> [ 10%] Built target argon2-avx512f
> Scanning dependencies of target argon2-avx2
> [ 11%] Building C object src/3rdparty/argon2/CMakeFiles/argon2-avx2.dir/arch/x86_64/lib/argon2-avx2.c.o
> [ 11%] Linking C static library libargon2-avx2.a
> [ 11%] Built target argon2-avx2
> Scanning dependencies of target argon2-xop
> [ 12%] Building C object src/3rdparty/argon2/CMakeFiles/argon2-xop.dir/arch/x86_64/lib/argon2-xop.c.o
> [ 12%] Linking C static library libargon2-xop.a
> [ 12%] Built target argon2-xop
> Scanning dependencies of target argon2-ssse3
> [ 12%] Building C object src/3rdparty/argon2/CMakeFiles/argon2-ssse3.dir/arch/x86_64/lib/argon2-ssse3.c.o
> [ 13%] Linking C static library libargon2-ssse3.a
> [ 13%] Built target argon2-ssse3
> Scanning dependencies of target argon2
> [ 13%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/argon2.c.o
> [ 14%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/core.c.o
> [ 14%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/encoding.c.o
> [ 15%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/genkat.c.o
> [ 15%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/impl-select.c.o
> [ 16%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/blake2/blake2.c.o
> [ 17%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/arch/x86_64/lib/argon2-arch.c.o
> [ 17%] Linking C static library libargon2.a
> [ 17%] Built target argon2
> Scanning dependencies of target xmrig-notls
> [ 18%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/cpu/CpuLaunchData.cpp.o
> [ 18%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/crypto/Algorithm.cpp.o
> [ 19%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/crypto/Coin.cpp.o
> [ 20%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/crypto/keccak.cpp.o
> [ 20%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/crypto/sha3.cpp.o
> [ 21%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/io/Console.cpp.o
> In file included from /content/xmrig/src/base/io/Console.cpp:28:0:
> /content/xmrig/src/base/tools/Handle.h: In static member function ‘static void xmrig::Handle::close(T) [with T = uv_fs_event_s*]’:
> /content/xmrig/src/base/tools/Handle.h:83:9: error: ‘uv_fs_event_stop’ was not declared in this scope
> uv_fs_event_stop(handle);
> ^~~~~~~~~~~~~~~~
> /content/xmrig/src/base/tools/Handle.h:83:9: note: suggested alternative: ‘uv_fs_event_t’
> uv_fs_event_stop(handle);
> ^~~~~~~~~~~~~~~~
> uv_fs_event_t
> /content/xmrig/src/base/io/Console.cpp: In constructor ‘xmrig::Console::Console(xmrig::IConsoleListener*)’:
> /content/xmrig/src/base/io/Console.cpp:46:28: error: ‘UV_TTY_MODE_RAW’ was not declared in this scope
> uv_tty_set_mode(m_tty, UV_TTY_MODE_RAW);
> ^~~~~~~~~~~~~~~
> /content/xmrig/src/base/io/Console.cpp:47:97: error: invalid conversion from ‘void (_)(uv_handle_t_, size_t, uv_buf_t*) {aka void (_)(uv_handle_s_, long unsigned int, uv_buf_t*)}’ to ‘uv_alloc_cb {aka uv_buf_t (_)(uv_handle_s_, long unsigned int)}’ [-fpermissive]
> uv_read_start(reinterpret_cast<uv_stream_t*>(m_tty), Console::onAllocBuffer, Console::onRead);
> ^
> In file included from /content/xmrig/src/base/io/Console.h:32:0,
> from /content/xmrig/src/base/io/Console.cpp:26:
> /usr/include/uv.h:618:15: note: initializing argument 2 of ‘int uv_read_start(uv_stream_t*, uv_alloc_cb, uv_read_cb)’
> UV_EXTERN int uv_read_start(uv_stream_t*, uv_alloc_cb alloc_cb,
> ^~~~~~~~~~~~~
> /content/xmrig/src/base/io/Console.cpp:47:97: error: invalid conversion from ‘void (_)(uv_stream_t_, ssize_t, const uv_buf_t*) {aka void (_)(uv_stream_s_, long int, const uv_buf_t*)}’ to ‘uv_read_cb {aka void (_)(uv_stream_s_, long int, uv_buf_t)}’ [-fpermissive]
> uv_read_start(reinterpret_cast<uv_stream_t*>(m_tty), Console::onAllocBuffer, Console::onRead);
> ^
> In file included from /content/xmrig/src/base/io/Console.h:32:0,
> from /content/xmrig/src/base/io/Console.cpp:26:
> /usr/include/uv.h:618:15: note: initializing argument 3 of ‘int uv_read_start(uv_stream_t*, uv_alloc_cb, uv_read_cb)’
> UV_EXTERN int uv_read_start(uv_stream_t*, uv_alloc_cb alloc_cb,
> ^~~~~~~~~~~~~
> At global scope:
> cc1plus: warning: unrecognized command line option ‘-Wno-class-memaccess’
> CMakeFiles/xmrig-notls.dir/build.make:127: recipe for target 'CMakeFiles/xmrig-notls.dir/src/base/io/Console.cpp.o' failed
> make[2]: *** [CMakeFiles/xmrig-notls.dir/src/base/io/Console.cpp.o] Error 1
> CMakeFiles/Makefile2:80: recipe for target 'CMakeFiles/xmrig-notls.dir/all' failed
> make[1]: *** [CMakeFiles/xmrig-notls.dir/all] Error 2
> Makefile:83: recipe for target 'all' failed
> make: *** [all] Error 2

Try again with this i think you can install without error..

pkg upgrade -y

pkg install git cmake libuv clang nano -y

git clone --single-branch https://github.com/xmrig/xmrig.git

cd xmrig

mkdir build && cd build

cmake .. -DWITH_HTTPD=OFF -DWITH_TLS=OFF -DWITH_OPENCL=OFF -DWITH_CUDA=OFF -DCMAKE_BUILD_TYPE=Release -DWITH_HWLOC=OFF

ls

make

cp ../src/config.json config.json

nano config.json

donate.v2.xmrig.com:3333

xmr.pool.minergate.com:45700

CONTROL+\ ,donate.v2.xmrig.com:3333, replace with ( your pool address ) , y enter

Control +\ , and past YOUR_WALLET_ADDRESS , replace with ( your user name or wallet address) , y enter, and scroll down and check your all details..

control + x

y enter

./xmrig-notls

enjoy...!

## Sharaykaka | 2020-10-14T19:10:26+00:00
yes I was following the same steps you gave  initially I was getting the error at 13 % but after your steps, it reached till 21%  any other way do to this ?

## Saikatsaha1996 | 2020-10-14T19:12:27+00:00
Which device you using now ?

## Sharaykaka | 2020-10-14T19:13:18+00:00
Intel(R) Xeon(R) CPU @ 2.20GHz


less /proc/cpuinfo

processor       : 0
vendor_id       : GenuineIntel
cpu family      : 6
model           : 79
model name      : Intel(R) Xeon(R) CPU @ 2.20GHz
stepping        : 0
microcode       : 0x1
cpu MHz         : 2200.000
cache size      : 56320 KB
physical id     : 0
siblings        : 2
core id         : 0
cpu cores       : 1
apicid          : 0
initial apicid  : 0
fpu             : yes
fpu_exception   : yes
cpuid level     : 13
wp              : yes

## Saikatsaha1996 | 2020-10-14T19:15:30+00:00
Its windows?

## Sharaykaka | 2020-10-14T19:16:36+00:00
Ubuntu 64bit

## Saikatsaha1996 | 2020-10-14T19:18:59+00:00
When i am used Ubuntu i also got error thats why i am using now android and pc.. and got good results

## Sharaykaka | 2020-10-14T19:20:14+00:00
too ab mai kya karu bhai ?

What should i do now bro ?

## xmrig | 2020-10-14T19:21:24+00:00
https://xmrig.com/docs/miner/build/ubuntu

`libcurl4-openssl-dev` not required for ages and `libuv1-dev` not `libuvl-dev`, etc.
Thank you.

## Saikatsaha1996 | 2020-10-14T19:21:57+00:00
Humko v ubuntu ka baramey jada pata nahi hay.. 
:(

## Saikatsaha1996 | 2020-10-14T19:25:28+00:00
Ha i think ab ho jayaga..
Mera v windows my mera graphic card nahi use kar paraha hu..2gb nvidia GeForce 710 graphic hay but dikha raha "out of memory"..

## Saikatsaha1996 | 2020-10-14T19:26:09+00:00
> https://xmrig.com/docs/miner/build/ubuntu
> 
> `libcurl4-openssl-dev` not required for ages and `libuv1-dev` not `libuvl-dev`, etc.
> Thank you.

If you free Can i get 2 help ?

## Sharaykaka | 2020-10-14T19:30:13+00:00
It got solved thanks for everything

## Saikatsaha1996 | 2020-10-14T19:34:31+00:00
Ohh nice

## Sharaykaka | 2020-10-14T19:50:31+00:00
@yazeed44

## DeadManWalkingTO | 2020-10-20T21:27:06+00:00
Problem solved.
Now this issue can be closed.
Thank you!

# Action History
- Created by: Sharaykaka | 2020-10-14T18:28:20+00:00
- Closed at: 2020-11-26T10:34:38+00:00
