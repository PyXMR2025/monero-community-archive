---
title: 'xmrig 6.19.2 "FAILED: CMakeFiles/xmrig.dir/src/backend/opencl/kernels/rx/HashAesKernel.cpp.o"
  if OpenCL is installed system-wide on FreeBSD'
source_url: https://github.com/xmrig/xmrig/issues/3250
author: PaddyMac
assignees: []
labels: []
created_at: '2023-04-16T15:16:06+00:00'
updated_at: '2025-06-18T22:41:45+00:00'
type: issue
status: closed
closed_at: '2025-06-18T22:41:45+00:00'
---

# Original Description
The title pretty much summarizes the issue. I don't know if this issue affects other systems such as Linux, as I haven't tested that, but I can only successfully compile xmrig if I remove the OpenCL package from my system before compiling xmrig. So clearly xmrig's build system is confused and pollutes the build environment with a combination of the system and bundled versions of OpenCL if there is a system installation of OpenCL.

# Discussion History
# Action History
- Created by: PaddyMac | 2023-04-16T15:16:06+00:00
- Closed at: 2025-06-18T22:41:45+00:00
