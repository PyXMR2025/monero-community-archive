---
title: v.2.10.1-dev breaks on OS X
source_url: https://github.com/xmrig/xmrig/issues/925
author: blitss
assignees:
- xmrig
labels:
- bug
created_at: '2019-02-04T21:01:56+00:00'
updated_at: '2019-02-10T15:57:32+00:00'
type: issue
status: closed
closed_at: '2019-02-10T15:57:32+00:00'
---

# Original Description
Hey there,

Just saying that latest dev version breaks at the 
```
[2019-02-05 00:55:41] thread 3 error: "hash self-test failed".
[2019-02-05 00:55:41] thread 7 error: "hash self-test failed".
[2019-02-05 00:55:41] thread 5 error: "hash self-test failed".
[2019-02-05 00:55:41] thread 1 error: "hash self-test failed".
[2019-02-05 00:55:41] thread 4 error: "hash self-test failed".
[2019-02-05 00:55:41] thread 2 error: "hash self-test failed".
[2019-02-05 00:55:41] thread 6 error: "hash self-test failed".
[2019-02-05 00:55:41] thread 0 error: "hash self-test failed".
```
and doesn't produce any hashrate at all. 
v.2.9.2 is fine

# Discussion History
## xmrig | 2019-02-04T22:41:58+00:00
Please show cmake output from fresh run and first lines from miner output.
Thank you.

## blitss | 2019-02-05T08:36:07+00:00
Hi @xmrig 
Sorry, didn't have time to do this yesterday. Cmake and everything is like usual with v2.9.2 (should I show it with some debug flags?). Everything but mining doesn't work no matter which also I use.
I can send the first lines later
Do you have any clues which commit might cause that so I can test on a specific branch?

## xmrig | 2019-02-05T18:37:01+00:00
If you use multihash mode, this commit 3https://github.com/xmrig/xmrig/commit/a6a0fb965a8fde9aaeeca103f26255f9951d2e7d should solve the issue, otherwise still need information, usual cmake output is OK as well.

I dev branch added new algorithm `cn/gpu` and it can be broken in some environment.
Thank you.

## blitss | 2019-02-07T11:21:13+00:00
@xmrig hope it will help, latest dev branch. Latest commit didn't resolve the issue, neither is reverting to last 3 of them. v2.10.0 works

```
Andreys-iMac-2:build andrey$ cmake -LA ..  -DOPENSSL_ROOT_DIR=/usr/local/opt/openssl
-- Configuring done
-- Generating done
-- Build files have been written to: /Users/andrey/xmrig/build
-- Cache values
ARM_TARGET:BOOL=OFF
BUILD_STATIC:BOOL=OFF
CMAKE_AR:FILEPATH=/Library/Developer/CommandLineTools/usr/bin/ar
CMAKE_ASM_COMPILER:FILEPATH=/Library/Developer/CommandLineTools/usr/bin/cc
CMAKE_ASM_FLAGS:STRING=
CMAKE_ASM_FLAGS_DEBUG:STRING=-g
CMAKE_ASM_FLAGS_MINSIZEREL:STRING=-Os -DNDEBUG
CMAKE_ASM_FLAGS_RELEASE:STRING=-O3 -DNDEBUG
CMAKE_ASM_FLAGS_RELWITHDEBINFO:STRING=-O2 -g -DNDEBUG
CMAKE_BUILD_TYPE:STRING=
CMAKE_COLOR_MAKEFILE:BOOL=ON
CMAKE_CXX_COMPILER:FILEPATH=/Library/Developer/CommandLineTools/usr/bin/c++
CMAKE_CXX_FLAGS:STRING=
CMAKE_CXX_FLAGS_DEBUG:STRING=-g
CMAKE_CXX_FLAGS_MINSIZEREL:STRING=-Os -DNDEBUG
CMAKE_CXX_FLAGS_RELEASE:STRING=-O3 -DNDEBUG
CMAKE_CXX_FLAGS_RELWITHDEBINFO:STRING=-O2 -g -DNDEBUG
CMAKE_C_COMPILER:FILEPATH=/Library/Developer/CommandLineTools/usr/bin/cc
CMAKE_C_FLAGS:STRING=
CMAKE_C_FLAGS_DEBUG:STRING=-g
CMAKE_C_FLAGS_MINSIZEREL:STRING=-Os -DNDEBUG
CMAKE_C_FLAGS_RELEASE:STRING=-O3 -DNDEBUG
CMAKE_C_FLAGS_RELWITHDEBINFO:STRING=-O2 -g -DNDEBUG
CMAKE_EXE_LINKER_FLAGS:STRING=
CMAKE_EXE_LINKER_FLAGS_DEBUG:STRING=
CMAKE_EXE_LINKER_FLAGS_MINSIZEREL:STRING=
CMAKE_EXE_LINKER_FLAGS_RELEASE:STRING=
CMAKE_EXE_LINKER_FLAGS_RELWITHDEBINFO:STRING=
CMAKE_EXPORT_COMPILE_COMMANDS:BOOL=OFF
CMAKE_INSTALL_NAME_TOOL:FILEPATH=/usr/bin/install_name_tool
CMAKE_INSTALL_PREFIX:PATH=/usr/local
CMAKE_LINKER:FILEPATH=/Library/Developer/CommandLineTools/usr/bin/ld
CMAKE_MAKE_PROGRAM:FILEPATH=/usr/bin/make
CMAKE_MODULE_LINKER_FLAGS:STRING=
CMAKE_MODULE_LINKER_FLAGS_DEBUG:STRING=
CMAKE_MODULE_LINKER_FLAGS_MINSIZEREL:STRING=
CMAKE_MODULE_LINKER_FLAGS_RELEASE:STRING=
CMAKE_MODULE_LINKER_FLAGS_RELWITHDEBINFO:STRING=
CMAKE_NM:FILEPATH=/Library/Developer/CommandLineTools/usr/bin/nm
CMAKE_OBJCOPY:FILEPATH=CMAKE_OBJCOPY-NOTFOUND
CMAKE_OBJDUMP:FILEPATH=/Library/Developer/CommandLineTools/usr/bin/objdump
CMAKE_OSX_ARCHITECTURES:STRING=
CMAKE_OSX_DEPLOYMENT_TARGET:STRING=
CMAKE_OSX_SYSROOT:STRING=
CMAKE_RANLIB:FILEPATH=/Library/Developer/CommandLineTools/usr/bin/ranlib
CMAKE_SHARED_LINKER_FLAGS:STRING=
CMAKE_SHARED_LINKER_FLAGS_DEBUG:STRING=
CMAKE_SHARED_LINKER_FLAGS_MINSIZEREL:STRING=
CMAKE_SHARED_LINKER_FLAGS_RELEASE:STRING=
CMAKE_SHARED_LINKER_FLAGS_RELWITHDEBINFO:STRING=
CMAKE_SKIP_INSTALL_RPATH:BOOL=NO
CMAKE_SKIP_RPATH:BOOL=NO
CMAKE_STATIC_LINKER_FLAGS:STRING=
CMAKE_STATIC_LINKER_FLAGS_DEBUG:STRING=
CMAKE_STATIC_LINKER_FLAGS_MINSIZEREL:STRING=
CMAKE_STATIC_LINKER_FLAGS_RELEASE:STRING=
CMAKE_STATIC_LINKER_FLAGS_RELWITHDEBINFO:STRING=
CMAKE_STRIP:FILEPATH=/Library/Developer/CommandLineTools/usr/bin/strip
CMAKE_VERBOSE_MAKEFILE:BOOL=FALSE
MHD_INCLUDE_DIR:PATH=/usr/local/include
MHD_LIBRARY:FILEPATH=/usr/local/lib/libmicrohttpd.dylib
OPENSSL_CRYPTO_LIBRARY:FILEPATH=/usr/local/opt/openssl/lib/libcrypto.dylib
OPENSSL_INCLUDE_DIR:PATH=/usr/local/opt/openssl/include
OPENSSL_SSL_LIBRARY:FILEPATH=/usr/local/opt/openssl/lib/libssl.dylib
PKG_CONFIG_EXECUTABLE:FILEPATH=PKG_CONFIG_EXECUTABLE-NOTFOUND
UV_INCLUDE_DIR:PATH=/usr/local/include
UV_LIBRARY:FILEPATH=/usr/local/lib/libuv.a
WITH_AEON:BOOL=ON
WITH_ASM:BOOL=ON
WITH_CN_GPU:BOOL=ON
WITH_CN_PICO:BOOL=ON
WITH_DEBUG_LOG:BOOL=OFF
WITH_HTTPD:BOOL=ON
WITH_LIBCPUID:BOOL=ON
WITH_SUMO:BOOL=ON
WITH_TLS:BOOL=ON
```

```
Andreys-iMac-2:build andrey$ VERBOSE=1 make
/usr/local/Cellar/cmake/3.13.4/bin/cmake -S/Users/andrey/xmrig -B/Users/andrey/xmrig/build --check-build-system CMakeFiles/Makefile.cmake 0
/usr/local/Cellar/cmake/3.13.4/bin/cmake -E cmake_progress_start /Users/andrey/xmrig/build/CMakeFiles /Users/andrey/xmrig/build/CMakeFiles/progress.marks
/Library/Developer/CommandLineTools/usr/bin/make -f CMakeFiles/Makefile2 all
/Library/Developer/CommandLineTools/usr/bin/make -f src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/build.make src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/depend
cd /Users/andrey/xmrig/build && /usr/local/Cellar/cmake/3.13.4/bin/cmake -E cmake_depends "Unix Makefiles" /Users/andrey/xmrig /Users/andrey/xmrig/src/3rdparty/libcpuid /Users/andrey/xmrig/build /Users/andrey/xmrig/build/src/3rdparty/libcpuid /Users/andrey/xmrig/build/src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/DependInfo.cmake --color=
/Library/Developer/CommandLineTools/usr/bin/make -f src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/build.make src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/build
[  1%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/cpuid_main.c.o
cd /Users/andrey/xmrig/build/src/3rdparty/libcpuid && /Library/Developer/CommandLineTools/usr/bin/cc -DNDEBUG -DRAPIDJSON_SSE2 -DUNICODE -DVERSION=\"0.4.0\" -D__STDC_FORMAT_MACROS  -Wall -maes -O3 -DNDEBUG -Ofast -funroll-loops -fmerge-all-constants -Os   -o CMakeFiles/cpuid.dir/cpuid_main.c.o   -c /Users/andrey/xmrig/src/3rdparty/libcpuid/cpuid_main.c
[  3%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/asm-bits.c.o
cd /Users/andrey/xmrig/build/src/3rdparty/libcpuid && /Library/Developer/CommandLineTools/usr/bin/cc -DNDEBUG -DRAPIDJSON_SSE2 -DUNICODE -DVERSION=\"0.4.0\" -D__STDC_FORMAT_MACROS  -Wall -maes -O3 -DNDEBUG -Ofast -funroll-loops -fmerge-all-constants -Os   -o CMakeFiles/cpuid.dir/asm-bits.c.o   -c /Users/andrey/xmrig/src/3rdparty/libcpuid/asm-bits.c
[  5%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/recog_amd.c.o
cd /Users/andrey/xmrig/build/src/3rdparty/libcpuid && /Library/Developer/CommandLineTools/usr/bin/cc -DNDEBUG -DRAPIDJSON_SSE2 -DUNICODE -DVERSION=\"0.4.0\" -D__STDC_FORMAT_MACROS  -Wall -maes -O3 -DNDEBUG -Ofast -funroll-loops -fmerge-all-constants -Os   -o CMakeFiles/cpuid.dir/recog_amd.c.o   -c /Users/andrey/xmrig/src/3rdparty/libcpuid/recog_amd.c
[  6%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/recog_intel.c.o
cd /Users/andrey/xmrig/build/src/3rdparty/libcpuid && /Library/Developer/CommandLineTools/usr/bin/cc -DNDEBUG -DRAPIDJSON_SSE2 -DUNICODE -DVERSION=\"0.4.0\" -D__STDC_FORMAT_MACROS  -Wall -maes -O3 -DNDEBUG -Ofast -funroll-loops -fmerge-all-constants -Os   -o CMakeFiles/cpuid.dir/recog_intel.c.o   -c /Users/andrey/xmrig/src/3rdparty/libcpuid/recog_intel.c
[  8%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/libcpuid_util.c.o
cd /Users/andrey/xmrig/build/src/3rdparty/libcpuid && /Library/Developer/CommandLineTools/usr/bin/cc -DNDEBUG -DRAPIDJSON_SSE2 -DUNICODE -DVERSION=\"0.4.0\" -D__STDC_FORMAT_MACROS  -Wall -maes -O3 -DNDEBUG -Ofast -funroll-loops -fmerge-all-constants -Os   -o CMakeFiles/cpuid.dir/libcpuid_util.c.o   -c /Users/andrey/xmrig/src/3rdparty/libcpuid/libcpuid_util.c
[ 10%] Linking C static library libcpuid.a
cd /Users/andrey/xmrig/build/src/3rdparty/libcpuid && /usr/local/Cellar/cmake/3.13.4/bin/cmake -P CMakeFiles/cpuid.dir/cmake_clean_target.cmake
cd /Users/andrey/xmrig/build/src/3rdparty/libcpuid && /usr/local/Cellar/cmake/3.13.4/bin/cmake -E cmake_link_script CMakeFiles/cpuid.dir/link.txt --verbose=1
/Library/Developer/CommandLineTools/usr/bin/ar qc libcpuid.a  CMakeFiles/cpuid.dir/cpuid_main.c.o CMakeFiles/cpuid.dir/asm-bits.c.o CMakeFiles/cpuid.dir/recog_amd.c.o CMakeFiles/cpuid.dir/recog_intel.c.o CMakeFiles/cpuid.dir/libcpuid_util.c.o
/Library/Developer/CommandLineTools/usr/bin/ranlib libcpuid.a
[ 10%] Built target cpuid
/Library/Developer/CommandLineTools/usr/bin/make -f CMakeFiles/xmrig-asm.dir/build.make CMakeFiles/xmrig-asm.dir/depend
cd /Users/andrey/xmrig/build && /usr/local/Cellar/cmake/3.13.4/bin/cmake -E cmake_depends "Unix Makefiles" /Users/andrey/xmrig /Users/andrey/xmrig /Users/andrey/xmrig/build /Users/andrey/xmrig/build /Users/andrey/xmrig/build/CMakeFiles/xmrig-asm.dir/DependInfo.cmake --color=
/Library/Developer/CommandLineTools/usr/bin/make -f CMakeFiles/xmrig-asm.dir/build.make CMakeFiles/xmrig-asm.dir/build
[ 11%] Building ASM object CMakeFiles/xmrig-asm.dir/src/crypto/asm/cn_main_loop.S.o
/Library/Developer/CommandLineTools/usr/bin/cc -DHAVE_SYSLOG_H -DNDEBUG -DRAPIDJSON_SSE2 -DUNICODE -DXMRIG_NO_IPBC -D__STDC_FORMAT_MACROS -I/Users/andrey/xmrig/src/3rdparty/libcpuid -I/usr/local/opt/openssl/include -I/usr/local/include -I/Users/andrey/xmrig/src -I/Users/andrey/xmrig/src/3rdparty  -O3 -DNDEBUG   -o CMakeFiles/xmrig-asm.dir/src/crypto/asm/cn_main_loop.S.o -c /Users/andrey/xmrig/src/crypto/asm/cn_main_loop.S
[ 13%] Linking C static library libxmrig-asm.a
/usr/local/Cellar/cmake/3.13.4/bin/cmake -P CMakeFiles/xmrig-asm.dir/cmake_clean_target.cmake
/usr/local/Cellar/cmake/3.13.4/bin/cmake -E cmake_link_script CMakeFiles/xmrig-asm.dir/link.txt --verbose=1
/Library/Developer/CommandLineTools/usr/bin/ar qc libxmrig-asm.a  CMakeFiles/xmrig-asm.dir/src/crypto/asm/cn_main_loop.S.o
/Library/Developer/CommandLineTools/usr/bin/ranlib libxmrig-asm.a
[ 13%] Built target xmrig-asm
/Library/Developer/CommandLineTools/usr/bin/make -f CMakeFiles/xmrig.dir/build.make CMakeFiles/xmrig.dir/depend
cd /Users/andrey/xmrig/build && /usr/local/Cellar/cmake/3.13.4/bin/cmake -E cmake_depends "Unix Makefiles" /Users/andrey/xmrig /Users/andrey/xmrig /Users/andrey/xmrig/build /Users/andrey/xmrig/build /Users/andrey/xmrig/build/CMakeFiles/xmrig.dir/DependInfo.cmake --color=
/Library/Developer/CommandLineTools/usr/bin/make -f CMakeFiles/xmrig.dir/build.make CMakeFiles/xmrig.dir/build
[ 15%] Building CXX object CMakeFiles/xmrig.dir/src/api/NetworkState.cpp.o
/Library/Developer/CommandLineTools/usr/bin/c++  -DHAVE_SYSLOG_H -DNDEBUG -DRAPIDJSON_SSE2 -DUNICODE -DXMRIG_NO_IPBC -D__STDC_FORMAT_MACROS -I/Users/andrey/xmrig/src/3rdparty/libcpuid -I/usr/local/opt/openssl/include -I/usr/local/include -I/Users/andrey/xmrig/src -I/Users/andrey/xmrig/src/3rdparty  -Wall -fno-exceptions -fno-rtti -Wno-missing-braces -maes -O3 -DNDEBUG -Ofast -funroll-loops -fmerge-all-constants   -std=c++11 -o CMakeFiles/xmrig.dir/src/api/NetworkState.cpp.o -c /Users/andrey/xmrig/src/api/NetworkState.cpp
[ 16%] Building CXX object CMakeFiles/xmrig.dir/src/App.cpp.o
/Library/Developer/CommandLineTools/usr/bin/c++  -DHAVE_SYSLOG_H -DNDEBUG -DRAPIDJSON_SSE2 -DUNICODE -DXMRIG_NO_IPBC -D__STDC_FORMAT_MACROS -I/Users/andrey/xmrig/src/3rdparty/libcpuid -I/usr/local/opt/openssl/include -I/usr/local/include -I/Users/andrey/xmrig/src -I/Users/andrey/xmrig/src/3rdparty  -Wall -fno-exceptions -fno-rtti -Wno-missing-braces -maes -O3 -DNDEBUG -Ofast -funroll-loops -fmerge-all-constants   -std=c++11 -o CMakeFiles/xmrig.dir/src/App.cpp.o -c /Users/andrey/xmrig/src/App.cpp
[ 18%] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/String.cpp.o
/Library/Developer/CommandLineTools/usr/bin/c++  -DHAVE_SYSLOG_H -DNDEBUG -DRAPIDJSON_SSE2 -DUNICODE -DXMRIG_NO_IPBC -D__STDC_FORMAT_MACROS -I/Users/andrey/xmrig/src/3rdparty/libcpuid -I/usr/local/opt/openssl/include -I/usr/local/include -I/Users/andrey/xmrig/src -I/Users/andrey/xmrig/src/3rdparty  -Wall -fno-exceptions -fno-rtti -Wno-missing-braces -maes -O3 -DNDEBUG -Ofast -funroll-loops -fmerge-all-constants   -std=c++11 -o CMakeFiles/xmrig.dir/src/base/tools/String.cpp.o -c /Users/andrey/xmrig/src/base/tools/String.cpp
[ 20%] Building CXX object CMakeFiles/xmrig.dir/src/common/config/CommonConfig.cpp.o
/Library/Developer/CommandLineTools/usr/bin/c++  -DHAVE_SYSLOG_H -DNDEBUG -DRAPIDJSON_SSE2 -DUNICODE -DXMRIG_NO_IPBC -D__STDC_FORMAT_MACROS -I/Users/andrey/xmrig/src/3rdparty/libcpuid -I/usr/local/opt/openssl/include -I/usr/local/include -I/Users/andrey/xmrig/src -I/Users/andrey/xmrig/src/3rdparty  -Wall -fno-exceptions -fno-rtti -Wno-missing-braces -maes -O3 -DNDEBUG -Ofast -funroll-loops -fmerge-all-constants   -std=c++11 -o CMakeFiles/xmrig.dir/src/common/config/CommonConfig.cpp.o -c /Users/andrey/xmrig/src/common/config/CommonConfig.cpp
[ 21%] Building CXX object CMakeFiles/xmrig.dir/src/common/config/ConfigLoader.cpp.o
/Library/Developer/CommandLineTools/usr/bin/c++  -DHAVE_SYSLOG_H -DNDEBUG -DRAPIDJSON_SSE2 -DUNICODE -DXMRIG_NO_IPBC -D__STDC_FORMAT_MACROS -I/Users/andrey/xmrig/src/3rdparty/libcpuid -I/usr/local/opt/openssl/include -I/usr/local/include -I/Users/andrey/xmrig/src -I/Users/andrey/xmrig/src/3rdparty  -Wall -fno-exceptions -fno-rtti -Wno-missing-braces -maes -O3 -DNDEBUG -Ofast -funroll-loops -fmerge-all-constants   -std=c++11 -o CMakeFiles/xmrig.dir/src/common/config/ConfigLoader.cpp.o -c /Users/andrey/xmrig/src/common/config/ConfigLoader.cpp
[ 23%] Building CXX object CMakeFiles/xmrig.dir/src/common/config/ConfigWatcher.cpp.o
/Library/Developer/CommandLineTools/usr/bin/c++  -DHAVE_SYSLOG_H -DNDEBUG -DRAPIDJSON_SSE2 -DUNICODE -DXMRIG_NO_IPBC -D__STDC_FORMAT_MACROS -I/Users/andrey/xmrig/src/3rdparty/libcpuid -I/usr/local/opt/openssl/include -I/usr/local/include -I/Users/andrey/xmrig/src -I/Users/andrey/xmrig/src/3rdparty  -Wall -fno-exceptions -fno-rtti -Wno-missing-braces -maes -O3 -DNDEBUG -Ofast -funroll-loops -fmerge-all-constants   -std=c++11 -o CMakeFiles/xmrig.dir/src/common/config/ConfigWatcher.cpp.o -c /Users/andrey/xmrig/src/common/config/ConfigWatcher.cpp
[ 25%] Building CXX object CMakeFiles/xmrig.dir/src/common/Console.cpp.o
/Library/Developer/CommandLineTools/usr/bin/c++  -DHAVE_SYSLOG_H -DNDEBUG -DRAPIDJSON_SSE2 -DUNICODE -DXMRIG_NO_IPBC -D__STDC_FORMAT_MACROS -I/Users/andrey/xmrig/src/3rdparty/libcpuid -I/usr/local/opt/openssl/include -I/usr/local/include -I/Users/andrey/xmrig/src -I/Users/andrey/xmrig/src/3rdparty  -Wall -fno-exceptions -fno-rtti -Wno-missing-braces -maes -O3 -DNDEBUG -Ofast -funroll-loops -fmerge-all-constants   -std=c++11 -o CMakeFiles/xmrig.dir/src/common/Console.cpp.o -c /Users/andrey/xmrig/src/common/Console.cpp
[ 26%] Building CXX object CMakeFiles/xmrig.dir/src/common/crypto/Algorithm.cpp.o
/Library/Developer/CommandLineTools/usr/bin/c++  -DHAVE_SYSLOG_H -DNDEBUG -DRAPIDJSON_SSE2 -DUNICODE -DXMRIG_NO_IPBC -D__STDC_FORMAT_MACROS -I/Users/andrey/xmrig/src/3rdparty/libcpuid -I/usr/local/opt/openssl/include -I/usr/local/include -I/Users/andrey/xmrig/src -I/Users/andrey/xmrig/src/3rdparty  -Wall -fno-exceptions -fno-rtti -Wno-missing-braces -maes -O3 -DNDEBUG -Ofast -funroll-loops -fmerge-all-constants   -std=c++11 -o CMakeFiles/xmrig.dir/src/common/crypto/Algorithm.cpp.o -c /Users/andrey/xmrig/src/common/crypto/Algorithm.cpp
[ 28%] Building CXX object CMakeFiles/xmrig.dir/src/common/crypto/keccak.cpp.o
/Library/Developer/CommandLineTools/usr/bin/c++  -DHAVE_SYSLOG_H -DNDEBUG -DRAPIDJSON_SSE2 -DUNICODE -DXMRIG_NO_IPBC -D__STDC_FORMAT_MACROS -I/Users/andrey/xmrig/src/3rdparty/libcpuid -I/usr/local/opt/openssl/include -I/usr/local/include -I/Users/andrey/xmrig/src -I/Users/andrey/xmrig/src/3rdparty  -Wall -fno-exceptions -fno-rtti -Wno-missing-braces -maes -O3 -DNDEBUG -Ofast -funroll-loops -fmerge-all-constants   -std=c++11 -o CMakeFiles/xmrig.dir/src/common/crypto/keccak.cpp.o -c /Users/andrey/xmrig/src/common/crypto/keccak.cpp
[ 30%] Building CXX object CMakeFiles/xmrig.dir/src/common/log/BasicLog.cpp.o
/Library/Developer/CommandLineTools/usr/bin/c++  -DHAVE_SYSLOG_H -DNDEBUG -DRAPIDJSON_SSE2 -DUNICODE -DXMRIG_NO_IPBC -D__STDC_FORMAT_MACROS -I/Users/andrey/xmrig/src/3rdparty/libcpuid -I/usr/local/opt/openssl/include -I/usr/local/include -I/Users/andrey/xmrig/src -I/Users/andrey/xmrig/src/3rdparty  -Wall -fno-exceptions -fno-rtti -Wno-missing-braces -maes -O3 -DNDEBUG -Ofast -funroll-loops -fmerge-all-constants   -std=c++11 -o CMakeFiles/xmrig.dir/src/common/log/BasicLog.cpp.o -c /Users/andrey/xmrig/src/common/log/BasicLog.cpp
[ 31%] Building CXX object CMakeFiles/xmrig.dir/src/common/log/ConsoleLog.cpp.o
/Library/Developer/CommandLineTools/usr/bin/c++  -DHAVE_SYSLOG_H -DNDEBUG -DRAPIDJSON_SSE2 -DUNICODE -DXMRIG_NO_IPBC -D__STDC_FORMAT_MACROS -I/Users/andrey/xmrig/src/3rdparty/libcpuid -I/usr/local/opt/openssl/include -I/usr/local/include -I/Users/andrey/xmrig/src -I/Users/andrey/xmrig/src/3rdparty  -Wall -fno-exceptions -fno-rtti -Wno-missing-braces -maes -O3 -DNDEBUG -Ofast -funroll-loops -fmerge-all-constants   -std=c++11 -o CMakeFiles/xmrig.dir/src/common/log/ConsoleLog.cpp.o -c /Users/andrey/xmrig/src/common/log/ConsoleLog.cpp
[ 33%] Building CXX object CMakeFiles/xmrig.dir/src/common/log/FileLog.cpp.o
/Library/Developer/CommandLineTools/usr/bin/c++  -DHAVE_SYSLOG_H -DNDEBUG -DRAPIDJSON_SSE2 -DUNICODE -DXMRIG_NO_IPBC -D__STDC_FORMAT_MACROS -I/Users/andrey/xmrig/src/3rdparty/libcpuid -I/usr/local/opt/openssl/include -I/usr/local/include -I/Users/andrey/xmrig/src -I/Users/andrey/xmrig/src/3rdparty  -Wall -fno-exceptions -fno-rtti -Wno-missing-braces -maes -O3 -DNDEBUG -Ofast -funroll-loops -fmerge-all-constants   -std=c++11 -o CMakeFiles/xmrig.dir/src/common/log/FileLog.cpp.o -c /Users/andrey/xmrig/src/common/log/FileLog.cpp
[ 35%] Building CXX object CMakeFiles/xmrig.dir/src/common/log/Log.cpp.o
/Library/Developer/CommandLineTools/usr/bin/c++  -DHAVE_SYSLOG_H -DNDEBUG -DRAPIDJSON_SSE2 -DUNICODE -DXMRIG_NO_IPBC -D__STDC_FORMAT_MACROS -I/Users/andrey/xmrig/src/3rdparty/libcpuid -I/usr/local/opt/openssl/include -I/usr/local/include -I/Users/andrey/xmrig/src -I/Users/andrey/xmrig/src/3rdparty  -Wall -fno-exceptions -fno-rtti -Wno-missing-braces -maes -O3 -DNDEBUG -Ofast -funroll-loops -fmerge-all-constants   -std=c++11 -o CMakeFiles/xmrig.dir/src/common/log/Log.cpp.o -c /Users/andrey/xmrig/src/common/log/Log.cpp
[ 36%] Building CXX object CMakeFiles/xmrig.dir/src/common/net/Client.cpp.o
/Library/Developer/CommandLineTools/usr/bin/c++  -DHAVE_SYSLOG_H -DNDEBUG -DRAPIDJSON_SSE2 -DUNICODE -DXMRIG_NO_IPBC -D__STDC_FORMAT_MACROS -I/Users/andrey/xmrig/src/3rdparty/libcpuid -I/usr/local/opt/openssl/include -I/usr/local/include -I/Users/andrey/xmrig/src -I/Users/andrey/xmrig/src/3rdparty  -Wall -fno-exceptions -fno-rtti -Wno-missing-braces -maes -O3 -DNDEBUG -Ofast -funroll-loops -fmerge-all-constants   -std=c++11 -o CMakeFiles/xmrig.dir/src/common/net/Client.cpp.o -c /Users/andrey/xmrig/src/common/net/Client.cpp
[ 38%] Building CXX object CMakeFiles/xmrig.dir/src/common/net/Job.cpp.o
/Library/Developer/CommandLineTools/usr/bin/c++  -DHAVE_SYSLOG_H -DNDEBUG -DRAPIDJSON_SSE2 -DUNICODE -DXMRIG_NO_IPBC -D__STDC_FORMAT_MACROS -I/Users/andrey/xmrig/src/3rdparty/libcpuid -I/usr/local/opt/openssl/include -I/usr/local/include -I/Users/andrey/xmrig/src -I/Users/andrey/xmrig/src/3rdparty  -Wall -fno-exceptions -fno-rtti -Wno-missing-braces -maes -O3 -DNDEBUG -Ofast -funroll-loops -fmerge-all-constants   -std=c++11 -o CMakeFiles/xmrig.dir/src/common/net/Job.cpp.o -c /Users/andrey/xmrig/src/common/net/Job.cpp
[ 40%] Building CXX object CMakeFiles/xmrig.dir/src/common/net/Pool.cpp.o
/Library/Developer/CommandLineTools/usr/bin/c++  -DHAVE_SYSLOG_H -DNDEBUG -DRAPIDJSON_SSE2 -DUNICODE -DXMRIG_NO_IPBC -D__STDC_FORMAT_MACROS -I/Users/andrey/xmrig/src/3rdparty/libcpuid -I/usr/local/opt/openssl/include -I/usr/local/include -I/Users/andrey/xmrig/src -I/Users/andrey/xmrig/src/3rdparty  -Wall -fno-exceptions -fno-rtti -Wno-missing-braces -maes -O3 -DNDEBUG -Ofast -funroll-loops -fmerge-all-constants   -std=c++11 -o CMakeFiles/xmrig.dir/src/common/net/Pool.cpp.o -c /Users/andrey/xmrig/src/common/net/Pool.cpp
[ 41%] Building CXX object CMakeFiles/xmrig.dir/src/common/net/strategies/FailoverStrategy.cpp.o
/Library/Developer/CommandLineTools/usr/bin/c++  -DHAVE_SYSLOG_H -DNDEBUG -DRAPIDJSON_SSE2 -DUNICODE -DXMRIG_NO_IPBC -D__STDC_FORMAT_MACROS -I/Users/andrey/xmrig/src/3rdparty/libcpuid -I/usr/local/opt/openssl/include -I/usr/local/include -I/Users/andrey/xmrig/src -I/Users/andrey/xmrig/src/3rdparty  -Wall -fno-exceptions -fno-rtti -Wno-missing-braces -maes -O3 -DNDEBUG -Ofast -funroll-loops -fmerge-all-constants   -std=c++11 -o CMakeFiles/xmrig.dir/src/common/net/strategies/FailoverStrategy.cpp.o -c /Users/andrey/xmrig/src/common/net/strategies/FailoverStrategy.cpp
[ 43%] Building CXX object CMakeFiles/xmrig.dir/src/common/net/strategies/SinglePoolStrategy.cpp.o
/Library/Developer/CommandLineTools/usr/bin/c++  -DHAVE_SYSLOG_H -DNDEBUG -DRAPIDJSON_SSE2 -DUNICODE -DXMRIG_NO_IPBC -D__STDC_FORMAT_MACROS -I/Users/andrey/xmrig/src/3rdparty/libcpuid -I/usr/local/opt/openssl/include -I/usr/local/include -I/Users/andrey/xmrig/src -I/Users/andrey/xmrig/src/3rdparty  -Wall -fno-exceptions -fno-rtti -Wno-missing-braces -maes -O3 -DNDEBUG -Ofast -funroll-loops -fmerge-all-constants   -std=c++11 -o CMakeFiles/xmrig.dir/src/common/net/strategies/SinglePoolStrategy.cpp.o -c /Users/andrey/xmrig/src/common/net/strategies/SinglePoolStrategy.cpp
[ 45%] Building CXX object CMakeFiles/xmrig.dir/src/common/net/SubmitResult.cpp.o
/Library/Developer/CommandLineTools/usr/bin/c++  -DHAVE_SYSLOG_H -DNDEBUG -DRAPIDJSON_SSE2 -DUNICODE -DXMRIG_NO_IPBC -D__STDC_FORMAT_MACROS -I/Users/andrey/xmrig/src/3rdparty/libcpuid -I/usr/local/opt/openssl/include -I/usr/local/include -I/Users/andrey/xmrig/src -I/Users/andrey/xmrig/src/3rdparty  -Wall -fno-exceptions -fno-rtti -Wno-missing-braces -maes -O3 -DNDEBUG -Ofast -funroll-loops -fmerge-all-constants   -std=c++11 -o CMakeFiles/xmrig.dir/src/common/net/SubmitResult.cpp.o -c /Users/andrey/xmrig/src/common/net/SubmitResult.cpp
[ 46%] Building CXX object CMakeFiles/xmrig.dir/src/common/Platform.cpp.o
/Library/Developer/CommandLineTools/usr/bin/c++  -DHAVE_SYSLOG_H -DNDEBUG -DRAPIDJSON_SSE2 -DUNICODE -DXMRIG_NO_IPBC -D__STDC_FORMAT_MACROS -I/Users/andrey/xmrig/src/3rdparty/libcpuid -I/usr/local/opt/openssl/include -I/usr/local/include -I/Users/andrey/xmrig/src -I/Users/andrey/xmrig/src/3rdparty  -Wall -fno-exceptions -fno-rtti -Wno-missing-braces -maes -O3 -DNDEBUG -Ofast -funroll-loops -fmerge-all-constants   -std=c++11 -o CMakeFiles/xmrig.dir/src/common/Platform.cpp.o -c /Users/andrey/xmrig/src/common/Platform.cpp
[ 48%] Building CXX object CMakeFiles/xmrig.dir/src/core/Config.cpp.o
/Library/Developer/CommandLineTools/usr/bin/c++  -DHAVE_SYSLOG_H -DNDEBUG -DRAPIDJSON_SSE2 -DUNICODE -DXMRIG_NO_IPBC -D__STDC_FORMAT_MACROS -I/Users/andrey/xmrig/src/3rdparty/libcpuid -I/usr/local/opt/openssl/include -I/usr/local/include -I/Users/andrey/xmrig/src -I/Users/andrey/xmrig/src/3rdparty  -Wall -fno-exceptions -fno-rtti -Wno-missing-braces -maes -O3 -DNDEBUG -Ofast -funroll-loops -fmerge-all-constants   -std=c++11 -o CMakeFiles/xmrig.dir/src/core/Config.cpp.o -c /Users/andrey/xmrig/src/core/Config.cpp
[ 50%] Building CXX object CMakeFiles/xmrig.dir/src/core/Controller.cpp.o
/Library/Developer/CommandLineTools/usr/bin/c++  -DHAVE_SYSLOG_H -DNDEBUG -DRAPIDJSON_SSE2 -DUNICODE -DXMRIG_NO_IPBC -D__STDC_FORMAT_MACROS -I/Users/andrey/xmrig/src/3rdparty/libcpuid -I/usr/local/opt/openssl/include -I/usr/local/include -I/Users/andrey/xmrig/src -I/Users/andrey/xmrig/src/3rdparty  -Wall -fno-exceptions -fno-rtti -Wno-missing-braces -maes -O3 -DNDEBUG -Ofast -funroll-loops -fmerge-all-constants   -std=c++11 -o CMakeFiles/xmrig.dir/src/core/Controller.cpp.o -c /Users/andrey/xmrig/src/core/Controller.cpp
[ 51%] Building CXX object CMakeFiles/xmrig.dir/src/Mem.cpp.o
/Library/Developer/CommandLineTools/usr/bin/c++  -DHAVE_SYSLOG_H -DNDEBUG -DRAPIDJSON_SSE2 -DUNICODE -DXMRIG_NO_IPBC -D__STDC_FORMAT_MACROS -I/Users/andrey/xmrig/src/3rdparty/libcpuid -I/usr/local/opt/openssl/include -I/usr/local/include -I/Users/andrey/xmrig/src -I/Users/andrey/xmrig/src/3rdparty  -Wall -fno-exceptions -fno-rtti -Wno-missing-braces -maes -O3 -DNDEBUG -Ofast -funroll-loops -fmerge-all-constants   -std=c++11 -o CMakeFiles/xmrig.dir/src/Mem.cpp.o -c /Users/andrey/xmrig/src/Mem.cpp
[ 53%] Building CXX object CMakeFiles/xmrig.dir/src/net/Network.cpp.o
/Library/Developer/CommandLineTools/usr/bin/c++  -DHAVE_SYSLOG_H -DNDEBUG -DRAPIDJSON_SSE2 -DUNICODE -DXMRIG_NO_IPBC -D__STDC_FORMAT_MACROS -I/Users/andrey/xmrig/src/3rdparty/libcpuid -I/usr/local/opt/openssl/include -I/usr/local/include -I/Users/andrey/xmrig/src -I/Users/andrey/xmrig/src/3rdparty  -Wall -fno-exceptions -fno-rtti -Wno-missing-braces -maes -O3 -DNDEBUG -Ofast -funroll-loops -fmerge-all-constants   -std=c++11 -o CMakeFiles/xmrig.dir/src/net/Network.cpp.o -c /Users/andrey/xmrig/src/net/Network.cpp
[ 55%] Building CXX object CMakeFiles/xmrig.dir/src/net/strategies/DonateStrategy.cpp.o
/Library/Developer/CommandLineTools/usr/bin/c++  -DHAVE_SYSLOG_H -DNDEBUG -DRAPIDJSON_SSE2 -DUNICODE -DXMRIG_NO_IPBC -D__STDC_FORMAT_MACROS -I/Users/andrey/xmrig/src/3rdparty/libcpuid -I/usr/local/opt/openssl/include -I/usr/local/include -I/Users/andrey/xmrig/src -I/Users/andrey/xmrig/src/3rdparty  -Wall -fno-exceptions -fno-rtti -Wno-missing-braces -maes -O3 -DNDEBUG -Ofast -funroll-loops -fmerge-all-constants   -std=c++11 -o CMakeFiles/xmrig.dir/src/net/strategies/DonateStrategy.cpp.o -c /Users/andrey/xmrig/src/net/strategies/DonateStrategy.cpp
[ 56%] Building CXX object CMakeFiles/xmrig.dir/src/Summary.cpp.o
/Library/Developer/CommandLineTools/usr/bin/c++  -DHAVE_SYSLOG_H -DNDEBUG -DRAPIDJSON_SSE2 -DUNICODE -DXMRIG_NO_IPBC -D__STDC_FORMAT_MACROS -I/Users/andrey/xmrig/src/3rdparty/libcpuid -I/usr/local/opt/openssl/include -I/usr/local/include -I/Users/andrey/xmrig/src -I/Users/andrey/xmrig/src/3rdparty  -Wall -fno-exceptions -fno-rtti -Wno-missing-braces -maes -O3 -DNDEBUG -Ofast -funroll-loops -fmerge-all-constants   -std=c++11 -o CMakeFiles/xmrig.dir/src/Summary.cpp.o -c /Users/andrey/xmrig/src/Summary.cpp
[ 58%] Building CXX object CMakeFiles/xmrig.dir/src/workers/CpuThread.cpp.o
/Library/Developer/CommandLineTools/usr/bin/c++  -DHAVE_SYSLOG_H -DNDEBUG -DRAPIDJSON_SSE2 -DUNICODE -DXMRIG_NO_IPBC -D__STDC_FORMAT_MACROS -I/Users/andrey/xmrig/src/3rdparty/libcpuid -I/usr/local/opt/openssl/include -I/usr/local/include -I/Users/andrey/xmrig/src -I/Users/andrey/xmrig/src/3rdparty  -Wall -fno-exceptions -fno-rtti -Wno-missing-braces -maes -O3 -DNDEBUG -Ofast -funroll-loops -fmerge-all-constants   -std=c++11 -o CMakeFiles/xmrig.dir/src/workers/CpuThread.cpp.o -c /Users/andrey/xmrig/src/workers/CpuThread.cpp
[ 60%] Building CXX object CMakeFiles/xmrig.dir/src/workers/Handle.cpp.o
/Library/Developer/CommandLineTools/usr/bin/c++  -DHAVE_SYSLOG_H -DNDEBUG -DRAPIDJSON_SSE2 -DUNICODE -DXMRIG_NO_IPBC -D__STDC_FORMAT_MACROS -I/Users/andrey/xmrig/src/3rdparty/libcpuid -I/usr/local/opt/openssl/include -I/usr/local/include -I/Users/andrey/xmrig/src -I/Users/andrey/xmrig/src/3rdparty  -Wall -fno-exceptions -fno-rtti -Wno-missing-braces -maes -O3 -DNDEBUG -Ofast -funroll-loops -fmerge-all-constants   -std=c++11 -o CMakeFiles/xmrig.dir/src/workers/Handle.cpp.o -c /Users/andrey/xmrig/src/workers/Handle.cpp
[ 61%] Building CXX object CMakeFiles/xmrig.dir/src/workers/Hashrate.cpp.o
/Library/Developer/CommandLineTools/usr/bin/c++  -DHAVE_SYSLOG_H -DNDEBUG -DRAPIDJSON_SSE2 -DUNICODE -DXMRIG_NO_IPBC -D__STDC_FORMAT_MACROS -I/Users/andrey/xmrig/src/3rdparty/libcpuid -I/usr/local/opt/openssl/include -I/usr/local/include -I/Users/andrey/xmrig/src -I/Users/andrey/xmrig/src/3rdparty  -Wall -fno-exceptions -fno-rtti -Wno-missing-braces -maes -O3 -DNDEBUG -Ofast -funroll-loops -fmerge-all-constants   -std=c++11 -o CMakeFiles/xmrig.dir/src/workers/Hashrate.cpp.o -c /Users/andrey/xmrig/src/workers/Hashrate.cpp
[ 63%] Building CXX object CMakeFiles/xmrig.dir/src/workers/MultiWorker.cpp.o
/Library/Developer/CommandLineTools/usr/bin/c++  -DHAVE_SYSLOG_H -DNDEBUG -DRAPIDJSON_SSE2 -DUNICODE -DXMRIG_NO_IPBC -D__STDC_FORMAT_MACROS -I/Users/andrey/xmrig/src/3rdparty/libcpuid -I/usr/local/opt/openssl/include -I/usr/local/include -I/Users/andrey/xmrig/src -I/Users/andrey/xmrig/src/3rdparty  -Wall -fno-exceptions -fno-rtti -Wno-missing-braces -maes -O3 -DNDEBUG -Ofast -funroll-loops -fmerge-all-constants   -std=c++11 -o CMakeFiles/xmrig.dir/src/workers/MultiWorker.cpp.o -c /Users/andrey/xmrig/src/workers/MultiWorker.cpp
[ 65%] Building CXX object CMakeFiles/xmrig.dir/src/workers/Worker.cpp.o
/Library/Developer/CommandLineTools/usr/bin/c++  -DHAVE_SYSLOG_H -DNDEBUG -DRAPIDJSON_SSE2 -DUNICODE -DXMRIG_NO_IPBC -D__STDC_FORMAT_MACROS -I/Users/andrey/xmrig/src/3rdparty/libcpuid -I/usr/local/opt/openssl/include -I/usr/local/include -I/Users/andrey/xmrig/src -I/Users/andrey/xmrig/src/3rdparty  -Wall -fno-exceptions -fno-rtti -Wno-missing-braces -maes -O3 -DNDEBUG -Ofast -funroll-loops -fmerge-all-constants   -std=c++11 -o CMakeFiles/xmrig.dir/src/workers/Worker.cpp.o -c /Users/andrey/xmrig/src/workers/Worker.cpp
[ 66%] Building CXX object CMakeFiles/xmrig.dir/src/workers/Workers.cpp.o
/Library/Developer/CommandLineTools/usr/bin/c++  -DHAVE_SYSLOG_H -DNDEBUG -DRAPIDJSON_SSE2 -DUNICODE -DXMRIG_NO_IPBC -D__STDC_FORMAT_MACROS -I/Users/andrey/xmrig/src/3rdparty/libcpuid -I/usr/local/opt/openssl/include -I/usr/local/include -I/Users/andrey/xmrig/src -I/Users/andrey/xmrig/src/3rdparty  -Wall -fno-exceptions -fno-rtti -Wno-missing-braces -maes -O3 -DNDEBUG -Ofast -funroll-loops -fmerge-all-constants   -std=c++11 -o CMakeFiles/xmrig.dir/src/workers/Workers.cpp.o -c /Users/andrey/xmrig/src/workers/Workers.cpp
[ 68%] Building CXX object CMakeFiles/xmrig.dir/src/xmrig.cpp.o
/Library/Developer/CommandLineTools/usr/bin/c++  -DHAVE_SYSLOG_H -DNDEBUG -DRAPIDJSON_SSE2 -DUNICODE -DXMRIG_NO_IPBC -D__STDC_FORMAT_MACROS -I/Users/andrey/xmrig/src/3rdparty/libcpuid -I/usr/local/opt/openssl/include -I/usr/local/include -I/Users/andrey/xmrig/src -I/Users/andrey/xmrig/src/3rdparty  -Wall -fno-exceptions -fno-rtti -Wno-missing-braces -maes -O3 -DNDEBUG -Ofast -funroll-loops -fmerge-all-constants   -std=c++11 -o CMakeFiles/xmrig.dir/src/xmrig.cpp.o -c /Users/andrey/xmrig/src/xmrig.cpp
[ 70%] Building CXX object CMakeFiles/xmrig.dir/src/App_unix.cpp.o
/Library/Developer/CommandLineTools/usr/bin/c++  -DHAVE_SYSLOG_H -DNDEBUG -DRAPIDJSON_SSE2 -DUNICODE -DXMRIG_NO_IPBC -D__STDC_FORMAT_MACROS -I/Users/andrey/xmrig/src/3rdparty/libcpuid -I/usr/local/opt/openssl/include -I/usr/local/include -I/Users/andrey/xmrig/src -I/Users/andrey/xmrig/src/3rdparty  -Wall -fno-exceptions -fno-rtti -Wno-missing-braces -maes -O3 -DNDEBUG -Ofast -funroll-loops -fmerge-all-constants   -std=c++11 -o CMakeFiles/xmrig.dir/src/App_unix.cpp.o -c /Users/andrey/xmrig/src/App_unix.cpp
[ 71%] Building CXX object CMakeFiles/xmrig.dir/src/common/Platform_mac.cpp.o
/Library/Developer/CommandLineTools/usr/bin/c++  -DHAVE_SYSLOG_H -DNDEBUG -DRAPIDJSON_SSE2 -DUNICODE -DXMRIG_NO_IPBC -D__STDC_FORMAT_MACROS -I/Users/andrey/xmrig/src/3rdparty/libcpuid -I/usr/local/opt/openssl/include -I/usr/local/include -I/Users/andrey/xmrig/src -I/Users/andrey/xmrig/src/3rdparty  -Wall -fno-exceptions -fno-rtti -Wno-missing-braces -maes -O3 -DNDEBUG -Ofast -funroll-loops -fmerge-all-constants   -std=c++11 -o CMakeFiles/xmrig.dir/src/common/Platform_mac.cpp.o -c /Users/andrey/xmrig/src/common/Platform_mac.cpp
[ 73%] Building CXX object CMakeFiles/xmrig.dir/src/Mem_unix.cpp.o
/Library/Developer/CommandLineTools/usr/bin/c++  -DHAVE_SYSLOG_H -DNDEBUG -DRAPIDJSON_SSE2 -DUNICODE -DXMRIG_NO_IPBC -D__STDC_FORMAT_MACROS -I/Users/andrey/xmrig/src/3rdparty/libcpuid -I/usr/local/opt/openssl/include -I/usr/local/include -I/Users/andrey/xmrig/src -I/Users/andrey/xmrig/src/3rdparty  -Wall -fno-exceptions -fno-rtti -Wno-missing-braces -maes -O3 -DNDEBUG -Ofast -funroll-loops -fmerge-all-constants   -std=c++11 -o CMakeFiles/xmrig.dir/src/Mem_unix.cpp.o -c /Users/andrey/xmrig/src/Mem_unix.cpp
[ 75%] Building CXX object CMakeFiles/xmrig.dir/src/core/cpu/AdvancedCpuInfo.cpp.o
/Library/Developer/CommandLineTools/usr/bin/c++  -DHAVE_SYSLOG_H -DNDEBUG -DRAPIDJSON_SSE2 -DUNICODE -DXMRIG_NO_IPBC -D__STDC_FORMAT_MACROS -I/Users/andrey/xmrig/src/3rdparty/libcpuid -I/usr/local/opt/openssl/include -I/usr/local/include -I/Users/andrey/xmrig/src -I/Users/andrey/xmrig/src/3rdparty  -Wall -fno-exceptions -fno-rtti -Wno-missing-braces -maes -O3 -DNDEBUG -Ofast -funroll-loops -fmerge-all-constants   -std=c++11 -o CMakeFiles/xmrig.dir/src/core/cpu/AdvancedCpuInfo.cpp.o -c /Users/andrey/xmrig/src/core/cpu/AdvancedCpuInfo.cpp
[ 76%] Building CXX object CMakeFiles/xmrig.dir/src/core/cpu/Cpu.cpp.o
/Library/Developer/CommandLineTools/usr/bin/c++  -DHAVE_SYSLOG_H -DNDEBUG -DRAPIDJSON_SSE2 -DUNICODE -DXMRIG_NO_IPBC -D__STDC_FORMAT_MACROS -I/Users/andrey/xmrig/src/3rdparty/libcpuid -I/usr/local/opt/openssl/include -I/usr/local/include -I/Users/andrey/xmrig/src -I/Users/andrey/xmrig/src/3rdparty  -Wall -fno-exceptions -fno-rtti -Wno-missing-braces -maes -O3 -DNDEBUG -Ofast -funroll-loops -fmerge-all-constants   -std=c++11 -o CMakeFiles/xmrig.dir/src/core/cpu/Cpu.cpp.o -c /Users/andrey/xmrig/src/core/cpu/Cpu.cpp
[ 78%] Building C object CMakeFiles/xmrig.dir/src/crypto/c_groestl.c.o
/Library/Developer/CommandLineTools/usr/bin/cc -DHAVE_SYSLOG_H -DNDEBUG -DRAPIDJSON_SSE2 -DUNICODE -DXMRIG_NO_IPBC -D__STDC_FORMAT_MACROS -I/Users/andrey/xmrig/src/3rdparty/libcpuid -I/usr/local/opt/openssl/include -I/usr/local/include -I/Users/andrey/xmrig/src -I/Users/andrey/xmrig/src/3rdparty  -Wall -maes -O3 -DNDEBUG -Ofast -funroll-loops -fmerge-all-constants   -o CMakeFiles/xmrig.dir/src/crypto/c_groestl.c.o   -c /Users/andrey/xmrig/src/crypto/c_groestl.c
[ 80%] Building C object CMakeFiles/xmrig.dir/src/crypto/c_blake256.c.o
/Library/Developer/CommandLineTools/usr/bin/cc -DHAVE_SYSLOG_H -DNDEBUG -DRAPIDJSON_SSE2 -DUNICODE -DXMRIG_NO_IPBC -D__STDC_FORMAT_MACROS -I/Users/andrey/xmrig/src/3rdparty/libcpuid -I/usr/local/opt/openssl/include -I/usr/local/include -I/Users/andrey/xmrig/src -I/Users/andrey/xmrig/src/3rdparty  -Wall -maes -O3 -DNDEBUG -Ofast -funroll-loops -fmerge-all-constants   -o CMakeFiles/xmrig.dir/src/crypto/c_blake256.c.o   -c /Users/andrey/xmrig/src/crypto/c_blake256.c
[ 81%] Building C object CMakeFiles/xmrig.dir/src/crypto/c_jh.c.o
/Library/Developer/CommandLineTools/usr/bin/cc -DHAVE_SYSLOG_H -DNDEBUG -DRAPIDJSON_SSE2 -DUNICODE -DXMRIG_NO_IPBC -D__STDC_FORMAT_MACROS -I/Users/andrey/xmrig/src/3rdparty/libcpuid -I/usr/local/opt/openssl/include -I/usr/local/include -I/Users/andrey/xmrig/src -I/Users/andrey/xmrig/src/3rdparty  -Wall -maes -O3 -DNDEBUG -Ofast -funroll-loops -fmerge-all-constants   -o CMakeFiles/xmrig.dir/src/crypto/c_jh.c.o   -c /Users/andrey/xmrig/src/crypto/c_jh.c
[ 83%] Building C object CMakeFiles/xmrig.dir/src/crypto/c_skein.c.o
/Library/Developer/CommandLineTools/usr/bin/cc -DHAVE_SYSLOG_H -DNDEBUG -DRAPIDJSON_SSE2 -DUNICODE -DXMRIG_NO_IPBC -D__STDC_FORMAT_MACROS -I/Users/andrey/xmrig/src/3rdparty/libcpuid -I/usr/local/opt/openssl/include -I/usr/local/include -I/Users/andrey/xmrig/src -I/Users/andrey/xmrig/src/3rdparty  -Wall -maes -O3 -DNDEBUG -Ofast -funroll-loops -fmerge-all-constants   -o CMakeFiles/xmrig.dir/src/crypto/c_skein.c.o   -c /Users/andrey/xmrig/src/crypto/c_skein.c
[ 85%] Building CXX object CMakeFiles/xmrig.dir/src/common/log/SysLog.cpp.o
/Library/Developer/CommandLineTools/usr/bin/c++  -DHAVE_SYSLOG_H -DNDEBUG -DRAPIDJSON_SSE2 -DUNICODE -DXMRIG_NO_IPBC -D__STDC_FORMAT_MACROS -I/Users/andrey/xmrig/src/3rdparty/libcpuid -I/usr/local/opt/openssl/include -I/usr/local/include -I/Users/andrey/xmrig/src -I/Users/andrey/xmrig/src/3rdparty  -Wall -fno-exceptions -fno-rtti -Wno-missing-braces -maes -O3 -DNDEBUG -Ofast -funroll-loops -fmerge-all-constants   -std=c++11 -o CMakeFiles/xmrig.dir/src/common/log/SysLog.cpp.o -c /Users/andrey/xmrig/src/common/log/SysLog.cpp
[ 86%] Building CXX object CMakeFiles/xmrig.dir/src/api/Api.cpp.o
/Library/Developer/CommandLineTools/usr/bin/c++  -DHAVE_SYSLOG_H -DNDEBUG -DRAPIDJSON_SSE2 -DUNICODE -DXMRIG_NO_IPBC -D__STDC_FORMAT_MACROS -I/Users/andrey/xmrig/src/3rdparty/libcpuid -I/usr/local/opt/openssl/include -I/usr/local/include -I/Users/andrey/xmrig/src -I/Users/andrey/xmrig/src/3rdparty  -Wall -fno-exceptions -fno-rtti -Wno-missing-braces -maes -O3 -DNDEBUG -Ofast -funroll-loops -fmerge-all-constants   -std=c++11 -o CMakeFiles/xmrig.dir/src/api/Api.cpp.o -c /Users/andrey/xmrig/src/api/Api.cpp
[ 88%] Building CXX object CMakeFiles/xmrig.dir/src/api/ApiRouter.cpp.o
/Library/Developer/CommandLineTools/usr/bin/c++  -DHAVE_SYSLOG_H -DNDEBUG -DRAPIDJSON_SSE2 -DUNICODE -DXMRIG_NO_IPBC -D__STDC_FORMAT_MACROS -I/Users/andrey/xmrig/src/3rdparty/libcpuid -I/usr/local/opt/openssl/include -I/usr/local/include -I/Users/andrey/xmrig/src -I/Users/andrey/xmrig/src/3rdparty  -Wall -fno-exceptions -fno-rtti -Wno-missing-braces -maes -O3 -DNDEBUG -Ofast -funroll-loops -fmerge-all-constants   -std=c++11 -o CMakeFiles/xmrig.dir/src/api/ApiRouter.cpp.o -c /Users/andrey/xmrig/src/api/ApiRouter.cpp
[ 90%] Building CXX object CMakeFiles/xmrig.dir/src/common/api/Httpd.cpp.o
/Library/Developer/CommandLineTools/usr/bin/c++  -DHAVE_SYSLOG_H -DNDEBUG -DRAPIDJSON_SSE2 -DUNICODE -DXMRIG_NO_IPBC -D__STDC_FORMAT_MACROS -I/Users/andrey/xmrig/src/3rdparty/libcpuid -I/usr/local/opt/openssl/include -I/usr/local/include -I/Users/andrey/xmrig/src -I/Users/andrey/xmrig/src/3rdparty  -Wall -fno-exceptions -fno-rtti -Wno-missing-braces -maes -O3 -DNDEBUG -Ofast -funroll-loops -fmerge-all-constants   -std=c++11 -o CMakeFiles/xmrig.dir/src/common/api/Httpd.cpp.o -c /Users/andrey/xmrig/src/common/api/Httpd.cpp
[ 91%] Building CXX object CMakeFiles/xmrig.dir/src/common/api/HttpRequest.cpp.o
/Library/Developer/CommandLineTools/usr/bin/c++  -DHAVE_SYSLOG_H -DNDEBUG -DRAPIDJSON_SSE2 -DUNICODE -DXMRIG_NO_IPBC -D__STDC_FORMAT_MACROS -I/Users/andrey/xmrig/src/3rdparty/libcpuid -I/usr/local/opt/openssl/include -I/usr/local/include -I/Users/andrey/xmrig/src -I/Users/andrey/xmrig/src/3rdparty  -Wall -fno-exceptions -fno-rtti -Wno-missing-braces -maes -O3 -DNDEBUG -Ofast -funroll-loops -fmerge-all-constants   -std=c++11 -o CMakeFiles/xmrig.dir/src/common/api/HttpRequest.cpp.o -c /Users/andrey/xmrig/src/common/api/HttpRequest.cpp
[ 93%] Building CXX object CMakeFiles/xmrig.dir/src/common/net/Tls.cpp.o
/Library/Developer/CommandLineTools/usr/bin/c++  -DHAVE_SYSLOG_H -DNDEBUG -DRAPIDJSON_SSE2 -DUNICODE -DXMRIG_NO_IPBC -D__STDC_FORMAT_MACROS -I/Users/andrey/xmrig/src/3rdparty/libcpuid -I/usr/local/opt/openssl/include -I/usr/local/include -I/Users/andrey/xmrig/src -I/Users/andrey/xmrig/src/3rdparty  -Wall -fno-exceptions -fno-rtti -Wno-missing-braces -maes -O3 -DNDEBUG -Ofast -funroll-loops -fmerge-all-constants   -std=c++11 -o CMakeFiles/xmrig.dir/src/common/net/Tls.cpp.o -c /Users/andrey/xmrig/src/common/net/Tls.cpp
[ 95%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/Asm.cpp.o
/Library/Developer/CommandLineTools/usr/bin/c++  -DHAVE_SYSLOG_H -DNDEBUG -DRAPIDJSON_SSE2 -DUNICODE -DXMRIG_NO_IPBC -D__STDC_FORMAT_MACROS -I/Users/andrey/xmrig/src/3rdparty/libcpuid -I/usr/local/opt/openssl/include -I/usr/local/include -I/Users/andrey/xmrig/src -I/Users/andrey/xmrig/src/3rdparty  -Wall -fno-exceptions -fno-rtti -Wno-missing-braces -maes -O3 -DNDEBUG -Ofast -funroll-loops -fmerge-all-constants   -std=c++11 -o CMakeFiles/xmrig.dir/src/crypto/Asm.cpp.o -c /Users/andrey/xmrig/src/crypto/Asm.cpp
[ 96%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/cn_gpu_avx.cpp.o
/Library/Developer/CommandLineTools/usr/bin/c++  -DHAVE_SYSLOG_H -DNDEBUG -DRAPIDJSON_SSE2 -DUNICODE -DXMRIG_NO_IPBC -D__STDC_FORMAT_MACROS -I/Users/andrey/xmrig/src/3rdparty/libcpuid -I/usr/local/opt/openssl/include -I/usr/local/include -I/Users/andrey/xmrig/src -I/Users/andrey/xmrig/src/3rdparty  -Wall -fno-exceptions -fno-rtti -Wno-missing-braces -maes -O3 -DNDEBUG -Ofast -funroll-loops -fmerge-all-constants   -std=c++11 -mavx2 -o CMakeFiles/xmrig.dir/src/crypto/cn_gpu_avx.cpp.o -c /Users/andrey/xmrig/src/crypto/cn_gpu_avx.cpp
[ 98%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/cn_gpu_ssse3.cpp.o
/Library/Developer/CommandLineTools/usr/bin/c++  -DHAVE_SYSLOG_H -DNDEBUG -DRAPIDJSON_SSE2 -DUNICODE -DXMRIG_NO_IPBC -D__STDC_FORMAT_MACROS -I/Users/andrey/xmrig/src/3rdparty/libcpuid -I/usr/local/opt/openssl/include -I/usr/local/include -I/Users/andrey/xmrig/src -I/Users/andrey/xmrig/src/3rdparty  -Wall -fno-exceptions -fno-rtti -Wno-missing-braces -maes -O3 -DNDEBUG -Ofast -funroll-loops -fmerge-all-constants   -std=c++11 -o CMakeFiles/xmrig.dir/src/crypto/cn_gpu_ssse3.cpp.o -c /Users/andrey/xmrig/src/crypto/cn_gpu_ssse3.cpp
[100%] Linking CXX executable xmrig
/usr/local/Cellar/cmake/3.13.4/bin/cmake -E cmake_link_script CMakeFiles/xmrig.dir/link.txt --verbose=1
/Library/Developer/CommandLineTools/usr/bin/c++   -Wall -fno-exceptions -fno-rtti -Wno-missing-braces -maes -O3 -DNDEBUG -Ofast -funroll-loops -fmerge-all-constants -Wl,-search_paths_first -Wl,-headerpad_max_install_names  CMakeFiles/xmrig.dir/src/api/NetworkState.cpp.o CMakeFiles/xmrig.dir/src/App.cpp.o CMakeFiles/xmrig.dir/src/base/tools/String.cpp.o CMakeFiles/xmrig.dir/src/common/config/CommonConfig.cpp.o CMakeFiles/xmrig.dir/src/common/config/ConfigLoader.cpp.o CMakeFiles/xmrig.dir/src/common/config/ConfigWatcher.cpp.o CMakeFiles/xmrig.dir/src/common/Console.cpp.o CMakeFiles/xmrig.dir/src/common/crypto/Algorithm.cpp.o CMakeFiles/xmrig.dir/src/common/crypto/keccak.cpp.o CMakeFiles/xmrig.dir/src/common/log/BasicLog.cpp.o CMakeFiles/xmrig.dir/src/common/log/ConsoleLog.cpp.o CMakeFiles/xmrig.dir/src/common/log/FileLog.cpp.o CMakeFiles/xmrig.dir/src/common/log/Log.cpp.o CMakeFiles/xmrig.dir/src/common/net/Client.cpp.o CMakeFiles/xmrig.dir/src/common/net/Job.cpp.o CMakeFiles/xmrig.dir/src/common/net/Pool.cpp.o CMakeFiles/xmrig.dir/src/common/net/strategies/FailoverStrategy.cpp.o CMakeFiles/xmrig.dir/src/common/net/strategies/SinglePoolStrategy.cpp.o CMakeFiles/xmrig.dir/src/common/net/SubmitResult.cpp.o CMakeFiles/xmrig.dir/src/common/Platform.cpp.o CMakeFiles/xmrig.dir/src/core/Config.cpp.o CMakeFiles/xmrig.dir/src/core/Controller.cpp.o CMakeFiles/xmrig.dir/src/Mem.cpp.o CMakeFiles/xmrig.dir/src/net/Network.cpp.o CMakeFiles/xmrig.dir/src/net/strategies/DonateStrategy.cpp.o CMakeFiles/xmrig.dir/src/Summary.cpp.o CMakeFiles/xmrig.dir/src/workers/CpuThread.cpp.o CMakeFiles/xmrig.dir/src/workers/Handle.cpp.o CMakeFiles/xmrig.dir/src/workers/Hashrate.cpp.o CMakeFiles/xmrig.dir/src/workers/MultiWorker.cpp.o CMakeFiles/xmrig.dir/src/workers/Worker.cpp.o CMakeFiles/xmrig.dir/src/workers/Workers.cpp.o CMakeFiles/xmrig.dir/src/xmrig.cpp.o CMakeFiles/xmrig.dir/src/App_unix.cpp.o CMakeFiles/xmrig.dir/src/common/Platform_mac.cpp.o CMakeFiles/xmrig.dir/src/Mem_unix.cpp.o CMakeFiles/xmrig.dir/src/core/cpu/AdvancedCpuInfo.cpp.o CMakeFiles/xmrig.dir/src/core/cpu/Cpu.cpp.o CMakeFiles/xmrig.dir/src/crypto/c_groestl.c.o CMakeFiles/xmrig.dir/src/crypto/c_blake256.c.o CMakeFiles/xmrig.dir/src/crypto/c_jh.c.o CMakeFiles/xmrig.dir/src/crypto/c_skein.c.o CMakeFiles/xmrig.dir/src/common/log/SysLog.cpp.o CMakeFiles/xmrig.dir/src/api/Api.cpp.o CMakeFiles/xmrig.dir/src/api/ApiRouter.cpp.o CMakeFiles/xmrig.dir/src/common/api/Httpd.cpp.o CMakeFiles/xmrig.dir/src/common/api/HttpRequest.cpp.o CMakeFiles/xmrig.dir/src/common/net/Tls.cpp.o CMakeFiles/xmrig.dir/src/crypto/Asm.cpp.o CMakeFiles/xmrig.dir/src/crypto/cn_gpu_avx.cpp.o CMakeFiles/xmrig.dir/src/crypto/cn_gpu_ssse3.cpp.o  -o xmrig libxmrig-asm.a /usr/local/opt/openssl/lib/libssl.dylib /usr/local/opt/openssl/lib/libcrypto.dylib /usr/local/lib/libuv.a /usr/local/lib/libmicrohttpd.dylib src/3rdparty/libcpuid/libcpuid.a 
[100%] Built target xmrig
/usr/local/Cellar/cmake/3.13.4/bin/cmake -E cmake_progress_start /Users/andrey/xmrig/build/CMakeFiles 0
```

```
Andreys-iMac-2:build andrey$ ./xmrig -o xmr.pool.hashto.cash:80 -O 31f2da90-b4e1-11e7-8c37-3ffdf979bc3d:x
 * ABOUT        XMRig/2.10.1-dev clang/9.1.0
 * LIBS         libuv/1.25.0 OpenSSL/1.0.2q microhttpd/0.9.62 
 * CPU          Intel(R) Core(TM) i9-9900K CPU @ 3.60GHz (1) x64 AES AVX2
 * CPU L2/L3    2.0 MB/16.0 MB
 * THREADS      8, cryptonight, av=0, donate=5%
 * ASSEMBLY     auto:intel
 * POOL #1      xmr.pool.hashto.cash:80 variant auto
 * COMMANDS     hashrate, pause, resume
[2019-02-07 15:20:49] use pool xmr.pool.hashto.cash:80  195.201.169.235 
[2019-02-07 15:20:49] new job from xmr.pool.hashto.cash:80 diff 1100 algo cn/2
[2019-02-07 15:20:49] thread 4 error: "hash self-test failed".
[2019-02-07 15:20:49] thread 2 error: "hash self-test failed".
[2019-02-07 15:20:49] thread 5 error: "hash self-test failed".
[2019-02-07 15:20:49] thread 1 error: "hash self-test failed".
[2019-02-07 15:20:49] thread 0 error: "hash self-test failed".
[2019-02-07 15:20:49] thread 3 error: "hash self-test failed".
[2019-02-07 15:20:49] thread 6 error: "hash self-test failed".
[2019-02-07 15:20:49] thread 7 error: "hash self-test failed".
```

## xmrig | 2019-02-08T20:49:32+00:00
This issue should be finally fixed, please check recent changes.
Thank you.

## blitss | 2019-02-10T15:57:28+00:00
Yes, it was fixed. 
XMRig shows only 16Gb of RAM even though I have 24Gb.

![image](https://user-images.githubusercontent.com/17164985/52535961-f664d800-2d6d-11e9-8251-8bafa3875663.png)


# Action History
- Created by: blitss | 2019-02-04T21:01:56+00:00
- Closed at: 2019-02-10T15:57:32+00:00
