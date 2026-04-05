---
title: Xmrig error?
source_url: https://github.com/xmrig/xmrig/issues/2338
author: cozfirto
assignees: []
labels: []
created_at: '2021-05-02T21:58:43+00:00'
updated_at: '2025-06-16T20:34:28+00:00'
type: issue
status: closed
closed_at: '2025-06-16T20:34:28+00:00'
---

# Original Description
Xmrig in termux when i use the command make

root@localhost:~/xmrig/build# make
Scanning dependencies of target ethash
[  1%] Building C object src/3rdparty/libethash/CMakeFiles/ethash.dir/ethash_internal.c.o
cc: error: unrecognized command line option ‘-maes’
make[2]: *** [src/3rdparty/libethash/CMakeFiles/ethash.dir/build.make:63: src/3rdparty/libethash/CMakeFiles/ethash.dir/ethash_internal.c.o] Error 1
make[1]: *** [CMakeFiles/Makefile2:172: src/3rdparty/libethash/CMakeFiles/ethash.dir/all] Error 2
make: *** [Makefile:84: all] Error 2

# Discussion History
## SChernykh | 2021-05-02T22:55:54+00:00
What CPU, OS version, GCC version is this?

## Spudz76 | 2021-05-03T04:10:15+00:00
termux is android shell,

## SChernykh | 2021-05-03T07:30:36+00:00
`-maes` is x86 command line parameter, so cmake doesn't detect that it's ARM CPU for some reason. 

## jhnmchldlsrs | 2022-04-22T04:12:43+00:00
Try adding this to the cmake stuff
`-DARM_TARGET=7`

# Action History
- Created by: cozfirto | 2021-05-02T21:58:43+00:00
- Closed at: 2025-06-16T20:34:28+00:00
