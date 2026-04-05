---
title: Compiling on Android Termux
source_url: https://github.com/xmrig/xmrig/issues/2656
author: LinuxHeki
assignees: []
labels: []
created_at: '2021-10-28T10:01:00+00:00'
updated_at: '2021-10-29T06:53:32+00:00'
type: issue
status: closed
closed_at: '2021-10-29T06:53:32+00:00'
---

# Original Description
**Describe the bug**
When I run make I get an error:

[ 3%] Linking C static library libargon2.a
Error running link command: No such file or directory 
make[2]: *** [src/3rdparty/argon2/CMakeFiles/argon2.dir/build.make:194: src/3rdparty/argon2/libargon2.a] Error 2
make[1]: *** [CMakeFiles/Makefile2:126: src/3rdparty/argon2/CMakeFiles/argon2.dir/all] Error 2
make: *** [Makefile:91: all] Error 2


I also disabled argon2 with cmake

**To Reproduce**
On Termux, git clone, folder build, cmake .. + args, make

**Expected behavior**
It builds xmrig without errors.

**Required data**
 - OS: Android
 - App: Termux

# Discussion History
## LinuxHeki | 2021-10-28T10:03:21+00:00
I tried with AND without `-DWITH_ARGON2=OFF` when I cmake.

## LinuxHeki | 2021-10-28T14:04:08+00:00
I solved it! I followed https://xmrig.com/docs/miner/build/ubuntu Advanched build

## LinuxHeki | 2021-10-28T14:08:43+00:00
Nooooooo! At 100% I get an error:

[  5%] Linking CXX executable xmrig                        ld.lld: error: undefined symbol: uv__pthread_sigmask       >>> referenced by process.c:329 (src/unix/process.c:329)
>>>               libuv_la-process.o:(uv__process_child_init) in archive ../scripts/deps/lib/libuv.a                  >>> referenced by signal.c:160 (src/unix/signal.c:160)     >>>               libuv_la-signal.o:(uv__signal_stop) in archive ../scripts/deps/lib/libuv.a                          >>> referenced by signal.c:160 (src/unix/signal.c:160)     >>>               libuv_la-signal.o:(uv__signal_start) in archive ../scripts/deps/lib/libuv.a
>>> referenced 4 more times
clang-13: error: linker command failed with exit code 1 (use -v to see invocation)
make[2]: *** [CMakeFiles/xmrig.dir/build.make:3767: xmrig] Error 1
make[1]: *** [CMakeFiles/Makefile2:119: CMakeFiles/xmrig.dir/all] Error 2
make: *** [Makefile:91: all] Error 2

## Spudz76 | 2021-10-28T19:07:24+00:00
The one step is wrong unless you corrected it:
```
-DXMRIG_DEPS=../scripts/deps
```

## LinuxHeki | 2021-10-28T21:20:15+00:00
Oh, thanks!

## LinuxHeki | 2021-10-29T06:53:27+00:00
IT WORKED!!! THANKS!!!

# Action History
- Created by: LinuxHeki | 2021-10-28T10:01:00+00:00
- Closed at: 2021-10-29T06:53:32+00:00
