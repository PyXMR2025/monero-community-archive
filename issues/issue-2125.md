---
title: -maes flag need remova on arm devices
source_url: https://github.com/xmrig/xmrig/issues/2125
author: fgsoftware1
assignees: []
labels: []
created_at: '2021-02-22T04:54:12+00:00'
updated_at: '2021-04-12T14:11:00+00:00'
type: issue
status: closed
closed_at: '2021-04-12T14:11:00+00:00'
---

# Original Description
**Describe the bug**
make command fails due to flag -maes flag -maes is only supported by x86

**To Reproduce**
run make on arm devices

**Expected behavior**
A clear and concise description of what you expected to happen.

**Required data**
 - Miner log as text or screenshot
 - Config file or command line (without wallets)
 - OS: ubuntu
 - For GPU related issues: information about GPUs and driver version.

**Additional context**

error: unrecognized command line option '-maes'; did you mean '-mapcs'?
src/3rdparty/argon2/CMakeFiles/argon2.dir/build.make:62: recipe for target 'src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/argon2.c.o' failed
make[2]: *** [src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/argon2.c.o] Error 1
CMakeFiles/Makefile2:123: recipe for target 'src/3rdparty/argon2/CMakeFiles/argon2.dir/all' failed
make[1]: *** [src/3rdparty/argon2/CMakeFiles/argon2.dir/all] Error 2
Makefile:83: recipe for target 'all' failed
make: *** [all] Error 2

# Discussion History
## SChernykh | 2021-02-22T07:21:45+00:00
XMRig compiles fine on all my ARM devices. Note that you need to compile it for ARMv8 or ARMv7l and use recent GCC/clang compiler.

## SChernykh | 2021-02-22T07:22:22+00:00
ARMv6 and older architectures are not supported.

## fgsoftware1 | 2021-02-22T15:42:08+00:00
I try build on armv8l

## SChernykh | 2021-02-22T15:46:55+00:00
-maes flag is not used on armv8/armv7, see https://github.com/xmrig/xmrig/blob/master/cmake/flags.cmake#L25
Maybe your cmake doesn't work properly.

## fgsoftware1 | 2021-02-22T20:42:58+00:00
> -maes flag is not used on armv8/armv7, see https://github.com/xmrig/xmrig/blob/master/cmake/flags.cmake#L25
> Maybe your cmake doesn't work properly.

src/3rdparty/argon2/CMakeFiles/argon2.dir/build.make:62

Makefile:83: recipe for target 'all' failed

# Action History
- Created by: fgsoftware1 | 2021-02-22T04:54:12+00:00
- Closed at: 2021-04-12T14:11:00+00:00
