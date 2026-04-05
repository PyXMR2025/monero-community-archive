---
title: Compiling errors on W10 x64 Msys2
source_url: https://github.com/xmrig/xmrig/issues/2373
author: netomx
assignees: []
labels: []
created_at: '2021-05-14T07:07:43+00:00'
updated_at: '2022-01-11T10:44:10+00:00'
type: issue
status: closed
closed_at: '2021-05-15T20:57:51+00:00'
---

# Original Description
`ernes@LAPTOP-QEOIDSG4 MSYS ~/xmrig/build
$ "c:\Program Files\CMake\bin\cmake.exe" .. -G "Unix Makefiles" -DXMRIG_DEPS=c:/xmrig-deps/gcc/x64
-- WITH_MSR=ON
-- argon2: detecting feature 'sse2'...
-- argon2: feature 'sse2' detected!
-- argon2: detecting feature 'ssse3'...
-- argon2: feature 'ssse3' detected!
-- argon2: detecting feature 'xop'...
-- argon2: feature 'xop' detected!
-- argon2: detecting feature 'avx2'...
-- argon2: feature 'avx2' detected!
-- argon2: detecting feature 'avx512f'...
-- argon2: feature 'avx512f' detected!
-- Configuring done
-- Generating done
-- Build files have been written to: C:/msys64/home/ernes/xmrig/build

ernes@LAPTOP-QEOIDSG4 MSYS ~/xmrig/build
$ make
Scanning dependencies of target xmrig-asm
[  2%] Built target xmrig-asm
Consolidate compiler generated dependencies of target argon2-avx512f
[  3%] Built target argon2-avx512f
Consolidate compiler generated dependencies of target argon2-ssse3
[  4%] Built target argon2-ssse3
Consolidate compiler generated dependencies of target argon2-sse2
[  5%] Built target argon2-sse2
Consolidate compiler generated dependencies of target argon2-avx2
[  5%] Built target argon2-avx2
Consolidate compiler generated dependencies of target argon2-xop
[  5%] Built target argon2-xop
Consolidate compiler generated dependencies of target argon2
[  8%] Built target argon2
Consolidate compiler generated dependencies of target ethash
[ 10%] Built target ethash
Scanning dependencies of target xmrig
Consolidate compiler generated dependencies of target xmrig
[ 10%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/log/backends/ConsoleLog.cpp.obj
C:/msys64/home/ernes/xmrig/src/base/io/log/backends/ConsoleLog.cpp: In constructor ‘xmrig::ConsoleLog::ConsoleLog(const xmrig::Title&)’:
C:/msys64/home/ernes/xmrig/src/base/io/log/backends/ConsoleLog.cpp:49:5: error: ‘HANDLE’ was not declared in this scope; did you mean ‘UV_HANDLE’?
   49 |     HANDLE handle = GetStdHandle(STD_INPUT_HANDLE);
      |     ^~~~~~
      |     UV_HANDLE
C:/msys64/home/ernes/xmrig/src/base/io/log/backends/ConsoleLog.cpp:50:9: error: ‘handle’ was not declared in this scope
   50 |     if (handle != INVALID_HANDLE_VALUE) {
      |         ^~~~~~
C:/msys64/home/ernes/xmrig/src/base/io/log/backends/ConsoleLog.cpp:50:19: error: ‘INVALID_HANDLE_VALUE’ was not declared in this scope
   50 |     if (handle != INVALID_HANDLE_VALUE) {
      |                   ^~~~~~~~~~~~~~~~~~~~
C:/msys64/home/ernes/xmrig/src/base/io/log/backends/ConsoleLog.cpp:51:9: error: ‘DWORD’ was not declared in this scope
   51 |         DWORD mode = 0;
      |         ^~~~~
C:/msys64/home/ernes/xmrig/src/base/io/log/backends/ConsoleLog.cpp:52:37: error: ‘mode’ was not declared in this scope; did you mean ‘mode_t’?
   52 |         if (GetConsoleMode(handle, &mode)) {
      |                                     ^~~~
      |                                     mode_t
C:/msys64/home/ernes/xmrig/src/base/io/log/backends/ConsoleLog.cpp:52:13: error: ‘GetConsoleMode’ was not declared in this scope
   52 |         if (GetConsoleMode(handle, &mode)) {
      |             ^~~~~~~~~~~~~~
C:/msys64/home/ernes/xmrig/src/base/io/log/backends/ConsoleLog.cpp:53:21: error: ‘ENABLE_QUICK_EDIT_MODE’ was not declared in this scope
   53 |            mode &= ~ENABLE_QUICK_EDIT_MODE;
      |                     ^~~~~~~~~~~~~~~~~~~~~~
C:/msys64/home/ernes/xmrig/src/base/io/log/backends/ConsoleLog.cpp:54:42: error: ‘ENABLE_EXTENDED_FLAGS’ was not declared in this scope
   54 |            SetConsoleMode(handle, mode | ENABLE_EXTENDED_FLAGS);
      |                                          ^~~~~~~~~~~~~~~~~~~~~
C:/msys64/home/ernes/xmrig/src/base/io/log/backends/ConsoleLog.cpp:54:12: error: ‘SetConsoleMode’ was not declared in this scope
   54 |            SetConsoleMode(handle, mode | ENABLE_EXTENDED_FLAGS);
      |            ^~~~~~~~~~~~~~
C:/msys64/home/ernes/xmrig/src/base/io/log/backends/ConsoleLog.cpp:59:9: error: ‘SetConsoleTitleA’ was not declared in this scope
   59 |         SetConsoleTitleA(title.value());
      |         ^~~~~~~~~~~~~~~~
make[2]: *** [CMakeFiles/xmrig.dir/build.make:272: CMakeFiles/xmrig.dir/src/base/io/log/backends/ConsoleLog.cpp.obj] Error 1
make[1]: *** [CMakeFiles/Makefile2:163: CMakeFiles/xmrig.dir/all] Error 2
make: *** [Makefile:91: all] Error 2

`

# Discussion History
## netomx | 2021-05-15T20:57:51+00:00
Compiled using chocolatey and it worked.

## PatrykMis | 2022-01-11T10:42:58+00:00
I had similar issues. Follow carefully this guide: https://xmrig.com/docs/miner/build/windows

Make sure after updating MSYS you've switched your environment to MinGW64. Building with MSYS isn't possible but with MinGW64 it builds fine, even using GCC 11+.

I wouldn't recommend building with chocolatey as it's not an official way, uses old compilers and can cause problems (looking at different guides posted on the Internet).

# Action History
- Created by: netomx | 2021-05-14T07:07:43+00:00
- Closed at: 2021-05-15T20:57:51+00:00
