---
title: RPi xmrig compile
source_url: https://github.com/xmrig/xmrig/issues/3780
author: CooperWaNg-py
assignees: []
labels: []
created_at: '2026-02-06T09:14:52+00:00'
updated_at: '2026-04-13T19:06:59+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
**Describe the bug**
When compiling xmrig on an rpi 0w v1.1 and running make it shows error: cc: error: unrecognized command-line option ‘-maes’
make[2]: *** [src/3rdparty/argon2/CMakeFiles/argon2.dir/build.make:79: src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/argon2.c.o] Error 1
make[1]: *** [CMakeFiles/Makefile2:165: src/3rdparty/argon2/CMakeFiles/argon2.dir/all] Error 2
make: *** [Makefile:91: all] Error 2

**To Reproduce**
Get an RPi 0w v1.1 and then git clone xmrig and then build it.

**Expected behavior**
Xmrig compiles

**Required data**
 - XMRig version
    Newest version
 - Miner log as text or screenshot
 - Config file or command line (without wallets)
 - OS: RPI OS lite 32-bit
 - For GPU related issues: information about GPUs and driver version.

**Additional context**
I've seen other people do it but I can't
on armhf6 architecture


# Discussion History
## im10furry | 2026-04-13T19:06:59+00:00
## Root Cause

The XMRig build system enables AES‑NI acceleration by default, adding the `-maes` compiler flag. However, ARMv6 CPUs (like the one in the Pi Zero W) do not support this flag, causing the compiler to abort.

---

## Solution 1: Disable AES via CMake (Recommended)

Pass the `-DWITH_AES=OFF` flag to CMake to explicitly turn off AES optimisations.

```bash
rm -rf build
mkdir build && cd build
cmake .. -DWITH_AES=OFF
make -j$(nproc)

This prevents the -maes flag from ever being added to the compiler command line.



# Action History
- Created by: CooperWaNg-py | 2026-02-06T09:14:52+00:00
