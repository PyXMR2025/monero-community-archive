---
title: a bug when building
source_url: https://github.com/xmrig/xmrig/issues/3590
author: 69gg
assignees: []
labels: []
created_at: '2024-11-23T05:14:16+00:00'
updated_at: '2025-06-16T19:22:10+00:00'
type: issue
status: closed
closed_at: '2025-06-16T19:22:10+00:00'
---

# Original Description
**Describe the bug**
hi guys, i met a bug in the build



**Expected behavior**
[2024-11-23 12:53:00] [100%] Linking CXX executable xmrig
[2024-11-23 12:53:00] /usr/bin/ld: CMakeFiles/xmrig.dir/src/crypto/cn/CnHash.cpp.o: undefined reference to symbol 'fesetround@@GLIBC_2.2.5'
[2024-11-23 12:53:00] /usr/bin/ld: /lib/x86_64-linux-gnu/libm.so.6: error adding symbols: DSO missing from command line
[2024-11-23 12:53:00] collect2: error: ld returned 1 exit status
[2024-11-23 12:53:00] make[2]: *** [CMakeFiles/xmrig.dir/build.make:3886: xmrig] Error 1
[2024-11-23 12:53:00] make[1]: *** [CMakeFiles/Makefile2:182: CMakeFiles/xmrig.dir/all] Error 2
[2024-11-23 12:53:00] make: *** [Makefile:91: all] Error 2
[2024-11-23 12:53:00] The task build Failure!
[2024-11-23 12:53:00] exit status 255

**Required data**
 - XMRig version
    - v6.22.1
 - OS: gitee go(ubuntu x64 20.04)
 - gcc: gcc (Ubuntu 10.3.0-1ubuntu1~20.04) 10.3.0

how can i  fix it? thanks guys


# Discussion History
# Action History
- Created by: 69gg | 2024-11-23T05:14:16+00:00
- Closed at: 2025-06-16T19:22:10+00:00
