---
title: Compile warning on aarch64
source_url: https://github.com/xmrig/xmrig/issues/942
author: lhirlimann
assignees: []
labels: []
created_at: '2019-02-22T21:30:26+00:00'
updated_at: '2019-03-03T17:53:13+00:00'
type: issue
status: closed
closed_at: '2019-03-03T17:53:12+00:00'
---

# Original Description
[ 63%] Building CXX object CMakeFiles/xmrig.dir/src/workers/MultiWorker.cpp.o
/home/ludovic/src/xmrig/src/workers/MultiWorker.cpp: In member function ‘bool MultiWorker<N>::verify2(xmrig::Variant, const char*) [with long unsigned int N = 1]’:
/home/ludovic/src/xmrig/src/workers/MultiWorker.cpp:228:19: warning: ‘void* memcpy(void*, const void*, size_t)’ accessing 32 bytes at offsets [0, 32] and 0 overlaps 32 bytes at offset 0 [-Wrestrict]
             memcpy(referenceValue + i * 32, referenceValue, 32);

[ludovic@pie3 build]$ gcc -v
Using built-in specs.
COLLECT_GCC=gcc
COLLECT_LTO_WRAPPER=/usr/libexec/gcc/aarch64-redhat-linux/8/lto-wrapper
Target: aarch64-redhat-linux
Configured with: ../configure --enable-bootstrap --enable-languages=c,c++,fortran,objc,obj-c++,ada,go,lto --prefix=/usr --mandir=/usr/share/man --infodir=/usr/share/info --with-bugurl=http://bugzilla.redhat.com/bugzilla --enable-shared --enable-threads=posix --enable-checking=release --enable-multilib --with-system-zlib --enable-__cxa_atexit --disable-libunwind-exceptions --enable-gnu-unique-object --enable-linker-build-id --with-gcc-major-version-only --with-linker-hash-style=gnu --enable-plugin --enable-initfini-array --with-isl --disable-libmpx --enable-gnu-indirect-function --build=aarch64-redhat-linux
Thread model: posix
gcc version 8.2.1 20181215 (Red Hat 8.2.1-6) (GCC) 
[ludovic@pie3 build]$

# Discussion History
## MarosMacko | 2019-02-28T20:02:35+00:00
Same on Windows build

## xmrig | 2019-03-03T17:53:12+00:00
Solved by https://github.com/xmrig/xmrig/commit/f2574c2a418ac93922feb791a74c3cbfd68798de
Thank you.

# Action History
- Created by: lhirlimann | 2019-02-22T21:30:26+00:00
- Closed at: 2019-03-03T17:53:12+00:00
