---
title: Building on alpine linux resulted in "Could not find OpenSSL" error
source_url: https://github.com/xmrig/xmrig/issues/3416
author: DarkmatterUAE
assignees: []
labels: []
created_at: '2024-02-02T03:33:35+00:00'
updated_at: '2025-06-18T22:16:38+00:00'
type: issue
status: closed
closed_at: '2025-06-18T22:16:38+00:00'
---

# Original Description
**Describe the bug**
Trying to build xmrig on Alpine Linux with openssl-dev package installed resulted in the following error message
```
-- Could NOT find OpenSSL, try to set the path to OpenSSL root folder in the system variable OPENSSL_ROOT_DIR (missing: OPENSSL_CRYPTO_LIBRARY) (found version "3.1.4")
CMake Error at cmake/OpenSSL.cmake:47 (message):
  OpenSSL NOT found: use `-DWITH_TLS=OFF` to build without TLS support
Call Stack (most recent call first):
  CMakeLists.txt:205 (include)
```

**To Reproduce**
Install Alpine Linux v3.19 on a VM or container.
Clone the xmrig source and install all dependencies with `apk add git make cmake libstdc++ gcc g++ libuv-dev openssl-dev hwloc-dev`.
`cmake .. -DBUILD_STATIC=ON -DWITH_OPENCL=OFF -DWITH_CUDA=OFF`

**Expected behavior**
Makefile is generated.

**Required data**
 - OS: Alpine Linux 3.19 amd64


# Discussion History
# Action History
- Created by: DarkmatterUAE | 2024-02-02T03:33:35+00:00
- Closed at: 2025-06-18T22:16:38+00:00
