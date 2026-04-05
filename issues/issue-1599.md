---
title: compiler xmrig %99 and errors occured
source_url: https://github.com/xmrig/xmrig/issues/1599
author: muyuxx
assignees: []
labels: []
created_at: '2020-03-21T00:40:46+00:00'
updated_at: '2020-03-21T08:57:18+00:00'
type: issue
status: closed
closed_at: '2020-03-21T08:57:18+00:00'
---

# Original Description
hi guys,how can i fix it
centos6.8
gcc6.1
cmake3


[ 96%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/astrobwt/sha3.cpp.o
[ 96%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/astrobwt/Salsa20.cpp.o
[ 97%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/log/backends/SysLog.cpp.o
[ 97%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Tls.cpp.o
[ 98%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpsClient.cpp.o
[ 98%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/Assembly.cpp.o
[ 99%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/cn/r/CryptonightR_gen.cpp.o
[ 99%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/cn/gpu/cn_gpu_avx.cpp.o
[100%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/cn/gpu/cn_gpu_ssse3.cpp.o
[100%] Linking CXX executable xmrig
/usr/lib/../lib64/libuv.a: error adding symbols: Malformed archive
collect2: error: ld returned 1 exit status
make[2]: *** [xmrig] Error 1
make[1]: *** [CMakeFiles/xmrig.dir/all] Error 2
make: *** [all] Error 2





# Discussion History
## trasherdk | 2020-03-21T02:25:06+00:00
Install, or compile, a recent version of `libuv`.
My version is `libuv-1.23.2` [compiled from source](https://dist.libuv.org/dist/).

# Action History
- Created by: muyuxx | 2020-03-21T00:40:46+00:00
- Closed at: 2020-03-21T08:57:18+00:00
