---
title: Cannot build on Windows 8.1
source_url: https://github.com/monero-project/monero-gui/issues/823
author: jklepatch
assignees: []
labels:
- resolved
created_at: '2017-08-17T06:55:55+00:00'
updated_at: '2018-07-17T14:18:31+00:00'
type: issue
status: closed
closed_at: '2018-07-17T14:18:31+00:00'
---

# Original Description
I tried to compile tag monero-core for tag `v.0.10.3.1`

Failed at `./build.sh` step:
```
The C compiler "C:/msys64/mingw64/bin/gcc.exe" is not able to compile a simple test program.
```

Details:
```
HEAD is now at c9063c0b... Merge pull request #1930
You are currently on commit 4ca35af
The most recent tag was at 4ca35af
You are building a tagged release
D       include/INode.h
D       include/IWallet.h
Switched to and reset branch 'release'
libwallet_merged.a not found - Building libwallet
Building libwallet release
cleaning up existing monero build dir, libs and includes
~/monero-core/monero/build/release ~/monero-core ~/monero-core
Configuring build for MINGW32..
-- The C compiler identification is unknown
-- The CXX compiler identification is unknown
-- Check for working C compiler: C:/msys64/mingw64/bin/gcc.exe
-- Check for working C compiler: C:/msys64/mingw64/bin/gcc.exe -- broken
CMake Error at C:/msys64/mingw32/share/cmake-3.9/Modules/CMakeTestCCompiler.cmake:51 (message):
  The C compiler "C:/msys64/mingw64/bin/gcc.exe" is not able to compile a
  simple test program.

  It fails with the following output:

   Change Dir: C:/msys64/home/win8/monero-core/monero/build/release/CMakeFiles/CMakeTmp



  Run Build Command:"C:/msys64/usr/bin/make.exe" "cmTC_6b1b3/fast"
```

I am bit confused about the `-mingw32`  / `mingw64` flag when launching `msys2_shell.cmd`.   Instructions for windows points to the README of the daemon, which mention the `-mingw64` flag. But part of the instruction for windows on monero-core mention the `-mingw32` flag.

* I first tried to compile with a combo of  `-mingw64` flag first then switched to `-mingw32` when monero-core mention it
* Then I tried to compile by using `-mingw32` flag for all instructions, but it didnt work either.


# Discussion History
## jklepatch | 2017-08-21T07:08:58+00:00
I fixed the above errors by re-installing the whole mingw/msys2 environment and re-installing all dependencies with -mingw32 flag.

However I stumbled accross linker errors for boost. Fixed with this PR:
https://github.com/monero-project/monero-core/pull/828

## sanderfoobar | 2018-07-17T13:54:58+00:00
+resolved

# Action History
- Created by: jklepatch | 2017-08-17T06:55:55+00:00
- Closed at: 2018-07-17T14:18:31+00:00
