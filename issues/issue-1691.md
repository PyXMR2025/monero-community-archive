---
title: make error in aarch64
source_url: https://github.com/xmrig/xmrig/issues/1691
author: bigbeef
assignees: []
labels:
- arm
created_at: '2020-05-25T07:29:21+00:00'
updated_at: '2020-08-19T01:18:15+00:00'
type: issue
status: closed
closed_at: '2020-08-19T01:18:15+00:00'
---

# Original Description
**Describe the bug**
make error in aarch64

**os**
```
#1659  uname -a
Linux kpcq4 4.18.0-80.7.2.el7.aarch64 #1 SMP Thu Sep 12 16:13:20 UTC 2019 aarch64 aarch64 aarch64 GNU/Linux
```
**make log**
```
[ 29%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpResponse.cpp.o
[ 30%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/DaemonClient.cpp.o
[ 30%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/SelfSelectClient.cpp.o
[ 31%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/tools/TcpServer.cpp.o
[ 31%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/Hashrate.cpp.o
[ 32%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/Threads.cpp.o
[ 32%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/Worker.cpp.o
[ 33%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/Workers.cpp.o
[ 33%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/Cpu.cpp.o
[ 33%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuBackend.cpp.o
In file included from /root/xmrig/src/crypto/randomx/randomx.h:35:0,
                 from /root/xmrig/src/crypto/rx/RxDataset.h:35,
                 from /root/xmrig/src/backend/cpu/CpuBackend.cpp:44:
/root/xmrig/src/crypto/randomx/intrin_portable.h:385:22: fatal error: arm_acle.h: No such file or directory
 #include <arm_acle.h>
                      ^
compilation terminated.
make[2]: *** [CMakeFiles/xmrig.dir/src/backend/cpu/CpuBackend.cpp.o] Error 1
make[1]: *** [CMakeFiles/xmrig.dir/all] Error 2
make: *** [all] Error 2
```

# Discussion History
# Action History
- Created by: bigbeef | 2020-05-25T07:29:21+00:00
- Closed at: 2020-08-19T01:18:15+00:00
