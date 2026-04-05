---
title: Error compiling/linking XMRig 5.5.3 on Ubuntu
source_url: https://github.com/xmrig/xmrig/issues/1530
author: kio3i0j9024vkoenio
assignees: []
labels:
- libuv
created_at: '2020-02-02T18:04:05+00:00'
updated_at: '2020-02-23T23:24:04+00:00'
type: issue
status: closed
closed_at: '2020-02-23T23:24:04+00:00'
---

# Original Description
When compiling XMRig 5.5.3 source on Ubuntu 16.04 I am getting this error during the linking stage:

[100%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/cn/gpu/cn_gpu_ssse3.cpp.o
[100%] Linking CXX executable xmrig
CMakeFiles/xmrig.dir/src/base/kernel/Env.cpp.o: In function `xmrig::Env::hostname()':
Env.cpp:(.text+0x1bc): undefined reference to `uv_os_gethostname'
collect2: error: ld returned 1 exit status
CMakeFiles/xmrig.dir/build.make:4889: recipe for target 'xmrig' failed
make[2]: *** [xmrig] Error 1
CMakeFiles/Makefile2:73: recipe for target 'CMakeFiles/xmrig.dir/all' failed
make[1]: *** [CMakeFiles/xmrig.dir/all] Error 2
Makefile:83: recipe for target 'all' failed
make: *** [all] Error 2

How to produce:

wget https://github.com/xmrig/xmrig/archive/v5.5.3.tar.gz
tar xvf v5.5.3.tar.gz
cd xmrig-5.5.3
cmake .
make


# Discussion History
## xmrig | 2020-02-02T18:29:17+00:00
Looks like libuv headers and library inconsistency (new headers and old library), Ubuntu 16.04 shipped with libuv 1.8.0 and `uv_os_gethostname` not used because this function added only in libuv 1.12.0 
https://github.com/xmrig/xmrig/blob/master/src/base/kernel/Env.cpp#L137

Please show full cmake output or try fugue out why libuv headers version different than library.
Thank you.

# Action History
- Created by: kio3i0j9024vkoenio | 2020-02-02T18:04:05+00:00
- Closed at: 2020-02-23T23:24:04+00:00
