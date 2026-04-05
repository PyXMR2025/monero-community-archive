---
title: Update build instructions for Fedora 31.
source_url: https://github.com/xmrig/xmrig/issues/1636
author: kotval
assignees: []
labels: []
created_at: '2020-04-07T22:30:51+00:00'
updated_at: '2020-08-28T16:26:45+00:00'
type: issue
status: closed
closed_at: '2020-08-28T16:26:45+00:00'
---

# Original Description
**Describe the bug**
Build Instructions for Fedora are out of date

**To Reproduce**
Attempt to build form source on Fedora 31

**Expected behavior**
Build successfully

**Required data**
 - Miner log as text or screenshot N/A
 - Config file or command line (without wallets) N/A
 - OS: Fedora 31
 - For GPU related issues: information about GPUs and driver version. N/A

**Additional context**
To fix, change "sudo dnf install -y git cmake gcc gcc-c++ libuv-static libstdc++-static libmicrohttpd-devel" to "sudo dnf install -y git cmake gcc gcc-c++ libuv-static libstdc++-static libmicrohttpd-devel openssl-devel hwloc-devel" 


# Discussion History
## xanderificnl | 2020-05-14T05:44:57+00:00
Hi!

I just came with a wiki patch for F32. I didn't check the issue list before creating it, oops.

Anyway, here:

```diff
diff --git a/Fedora-Build.md b/Fedora-Build.md
index 5251409..2aa567b 100644
--- a/Fedora-Build.md
+++ b/Fedora-Build.md
@@ -1,6 +1,7 @@
-## Fedora 25 or 26
+## Fedora >= 25
+
 ```bash
-sudo dnf install -y git cmake gcc gcc-c++ libuv-static libstdc++-static libmicrohttpd-devel
+sudo dnf install -y git cmake gcc gcc-c++ libuv-static libstdc++-static libmicrohttpd-devel hwloc-devel
 git clone https://github.com/xmrig/xmrig.git
 cd xmrig
 mkdir build
@@ -11,4 +12,4 @@ make
 
 ## Additional CMake options
 
-* https://github.com/xmrig/xmrig/wiki/Windows-Build#additional-cmake-options
\ No newline at end of file
+* https://github.com/xmrig/xmrig/wiki/Windows-Build#additional-cmake-options
```

## xmrig | 2020-08-28T16:26:45+00:00
https://xmrig.com/docs/miner/build/fedora

# Action History
- Created by: kotval | 2020-04-07T22:30:51+00:00
- Closed at: 2020-08-28T16:26:45+00:00
