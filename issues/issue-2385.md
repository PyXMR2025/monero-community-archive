---
title: Error cant create cmkaefiles
source_url: https://github.com/xmrig/xmrig/issues/2385
author: Basha3
assignees: []
labels: []
created_at: '2021-05-16T16:22:30+00:00'
updated_at: '2025-06-16T18:49:32+00:00'
type: issue
status: closed
closed_at: '2025-06-16T18:49:32+00:00'
---

# Original Description
-- Configuring incomplete, errors occurred!
See also "/root/xmrig/build/CMakeFiles/CMakeOutput.log".
root@localhost:~/xmrig/build# apt-get install libhwloc-dev
Reading package lists... Done
Building dependency tree
Reading state information... Done
libhwloc-dev is already the newest version (2.1.0+dfsg-4).
0 upgraded, 0 newly installed, 0 to remove and 0 not upgraded.
root@localhost:~/xmrig/build# cmake ..
CMake Error at /usr/share/cmake-3.16/Modules/FindPackageHandleStandardArgs.cmake:146 (message):
  Could NOT find UV (missing: UV_LIBRARY UV_INCLUDE_DIR)
Call Stack (most recent call first):
  /usr/share/cmake-3.16/Modules/FindPackageHandleStandardArgs.cmake:393 (_FPHSA_FAILURE_MESSAGE)
  cmake/FindUV.cmake:25 (find_package_handle_standard_args)
  CMakeLists.txt:178 (find_package)

# Discussion History
## Spudz76 | 2021-05-17T20:21:32+00:00
Obviously you need libuv-dev, libhwloc-dev, and libssl-dev... or use `bash ./scripts/build_deps.sh` to make supported versions of all three dependencies and then use `-DXMRIG_DEPS=../scripts/deps` to tell it where to find them.

But to build_deps you need to install libtool, autoconf, automake...

# Action History
- Created by: Basha3 | 2021-05-16T16:22:30+00:00
- Closed at: 2025-06-16T18:49:32+00:00
