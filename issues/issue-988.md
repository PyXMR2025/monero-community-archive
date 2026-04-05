---
title: Compiling CpuThread.cpp Error
source_url: https://github.com/xmrig/xmrig/issues/988
author: Hacker-One
assignees: []
labels: []
created_at: '2019-03-14T02:33:44+00:00'
updated_at: '2019-03-23T15:02:03+00:00'
type: issue
status: closed
closed_at: '2019-03-23T15:02:03+00:00'
---

# Original Description
**System OS:Centos5.11-i386
Cmake version:2.8.3
GCC version:5.4.0**

> cmake .. -DWITH_HTTPD=OFF -DWITH_TLS=OFF -DBUILD_STATIC=ON -DWITH_EMBEDDED_CONFIG=ON -DCMAKE_BUILD_TYPE=Release -DUV_INCLUDE_DIR=/usr/local/include -DUV_LIBRARY=/usr/local/lib/libuv.a

When I run command 'make' code error in 'Building CXX object CMakeFiles/xmrig-notls.dir/src/workers/CpuThread.cpp.o'.
example:
`/tmp/cc1RohAp.s:103474: Error: no such instruction: `aesenc 48(%esp),%xmm5'
/tmp/cc1RohAp.s:103475: Error: no such instruction: `aesenc 48(%esp),%xmm4'
/tmp/cc1RohAp.s:103476: Error: no such instruction: `aesenc 48(%esp),%xmm3'
/tmp/cc1RohAp.s:103477: Error: no such instruction: `aesenc 48(%esp),%xmm2'
/tmp/cc1RohAp.s:103478: Error: no such instruction: `aesenc 48(%esp),%xmm1'
/tmp/cc1RohAp.s:103479: Error: no such instruction: `aesenc 48(%esp),%xmm0'
/tmp/cc1RohAp.s:103480: Error: no such instruction: `aesenc (%esp),%xmm7'
/tmp/cc1RohAp.s:103481: Error: no such instruction: `aesenc (%esp),%xmm6'
/tmp/cc1RohAp.s:103482: Error: no such instruction: `aesenc (%esp),%xmm5'
/tmp/cc1RohAp.s:103483: Error: no such instruction: `aesenc (%esp),%xmm4'
/tmp/cc1RohAp.s:103484: Error: no such instruction: `aesenc (%esp),%xmm3'
/tmp/cc1RohAp.s:103485: Error: no such instruction: `aesenc (%esp),%xmm2'
/tmp/cc1RohAp.s:103486: Error: no such instruction: `aesenc (%esp),%xmm1'
/tmp/cc1RohAp.s:103487: Error: no such instruction: `aesenc (%esp),%xmm0'
/tmp/cc1RohAp.s:103488: Error: no such instruction: `aesenc 16(%esp),%xmm6'
/tmp/cc1RohAp.s:103489: Error: no such instruction: `aesenc 16(%esp),%xmm5'
/tmp/cc1RohAp.s:103490: Error: no such instruction: `aesenc 16(%esp),%xmm4'
/tmp/cc1RohAp.s:103491: Error: no such instruction: `aesenc 16(%esp),%xmm3'
/tmp/cc1RohAp.s:103492: Error: no such instruction: `aesenc 16(%esp),%xmm2'
/tmp/cc1RohAp.s:103493: Error: no such instruction: `aesenc 16(%esp),%xmm1'
/tmp/cc1RohAp.s:103494: Error: no such instruction: `aesenc 16(%esp),%xmm0'
/tmp/cc1RohAp.s:103495: Error: no such instruction: `aesenc 16(%esp),%xmm7'
/tmp/cc1RohAp.s:103496: Error: no such instruction: `aesenc 96(%esp),%xmm7'
/tmp/cc1RohAp.s:103497: Error: no such instruction: `aesenc 96(%esp),%xmm6'
/tmp/cc1RohAp.s:103498: Error: no such instruction: `aesenc 96(%esp),%xmm5'
/tmp/cc1RohAp.s:103499: Error: no such instruction: `aesenc 96(%esp),%xmm4'
/tmp/cc1RohAp.s:103500: Error: no such instruction: `aesenc 96(%esp),%xmm3'
/tmp/cc1RohAp.s:103501: Error: no such instruction: `aesenc 96(%esp),%xmm2'
/tmp/cc1RohAp.s:103502: Error: no such instruction: `aesenc 96(%esp),%xmm1'
/tmp/cc1RohAp.s:103503: Error: no such instruction: `aesenc 96(%esp),%xmm0'
/tmp/cc1RohAp.s:103504: Error: no such instruction: `aesenc 128(%esp),%xmm7'
/tmp/cc1RohAp.s:103505: Error: no such instruction: `aesenc 128(%esp),%xmm6'
/tmp/cc1RohAp.s:103506: Error: no such instruction: `aesenc 128(%esp),%xmm5'
/tmp/cc1RohAp.s:103507: Error: no such instruction: `aesenc 128(%esp),%xmm4'
/tmp/cc1RohAp.s:103508: Error: no such instruction: `aesenc 128(%esp),%xmm3'
/tmp/cc1RohAp.s:103509: Error: no such instruction: `aesenc 128(%esp),%xmm2'
/tmp/cc1RohAp.s:103510: Error: no such instruction: `aesenc 128(%esp),%xmm1'
/tmp/cc1RohAp.s:103511: Error: no such instruction: `aesenc 128(%esp),%xmm0'
/tmp/cc1RohAp.s:103762: Error: no such instruction: `aesenc 144(%esp),%xmm3'
/tmp/cc1RohAp.s:103774: Error: no such instruction: `aesenc 128(%esp),%xmm2'
/tmp/cc1RohAp.s:103777: Error: no such instruction: `aesenc 112(%esp),%xmm1'
/tmp/cc1RohAp.s:103784: Error: no such instruction: `aesenc 160(%esp),%xmm7'
/tmp/cc1RohAp.s:103792: Error: no such instruction: `aesenc 176(%esp),%xmm5'
make[2]: *** [CMakeFiles/xmrig-notls.dir/src/workers/CpuThread.cpp.o] Error 1
make[1]: *** [CMakeFiles/xmrig-notls.dir/all] Error 2
make: *** [all] Error 2`

# Discussion History
# Action History
- Created by: Hacker-One | 2019-03-14T02:33:44+00:00
- Closed at: 2019-03-23T15:02:03+00:00
