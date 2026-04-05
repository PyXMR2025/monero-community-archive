---
title: Error building from cmake files
source_url: https://github.com/xmrig/xmrig/issues/2929
author: echoLOGNAME
assignees: []
labels: []
created_at: '2022-02-08T16:44:45+00:00'
updated_at: '2022-02-08T17:54:03+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
What I did:

1. git clone https://github.com/xmrig/xmrig.git
2. cd xmrig
3. mkdir build
4. cd build
5. cmake ..

It worked until:

```
-- Use ARM_TARGET=8 (aarch64)
CMake Error at /usr/share/cmake-3.16/Modules/FindPackageHandleStandardArgs.cmake:146 (message):
  Could NOT find HWLOC (missing: HWLOC_LIBRARY HWLOC_INCLUDE_DIR)
Call Stack (most recent call first):
  /usr/share/cmake-3.16/Modules/FindPackageHandleStandardArgs.cmake:393 (_FPHSA_FAILURE_MESSAGE)
  cmake/FindHWLOC.cmake:25 (find_package_handle_standard_args)
  src/backend/cpu/cpu.cmake:30 (find_package)
  src/backend/backend.cmake:1 (include)
  CMakeLists.txt:48 (include)


-- Configuring incomplete, errors occurred!
See also "/home/echo/xmrig/build/CMakeFiles/CMakeOutput.log".
See also "/home/echo/xmrig/build/CMakeFiles/CMakeError.log".
```

I was trying this on Ubuntu Focal Fossa on my Chromebook running inside Crouton (a VM on top of Chrome OS).
The issue may be with my VM but I'd like to here some feed back on how I can fix this.
Thanks!

# Discussion History
## Spudz76 | 2022-02-08T17:54:03+00:00
`sudo apt-get install git build-essential cmake libuv1-dev libssl-dev libhwloc-dev`

From [the build docs](https://xmrig.com/docs/miner/build/ubuntu)

# Action History
- Created by: echoLOGNAME | 2022-02-08T16:44:45+00:00
