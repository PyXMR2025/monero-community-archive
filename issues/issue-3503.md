---
title: Unable to compile xmrig in 64x MSYS2 , Windows .
source_url: https://github.com/xmrig/xmrig/issues/3503
author: kamlendras
assignees: []
labels: []
created_at: '2024-06-28T14:06:38+00:00'
updated_at: '2025-06-18T22:11:10+00:00'
type: issue
status: closed
closed_at: '2025-06-18T22:11:10+00:00'
---

# Original Description
**Describe the bug**
I read https://xmrig.com/docs/miner/build/windows . 


![compile_error](https://github.com/xmrig/xmrig/assets/96082996/cdc3a206-ca1c-48cd-8f58-73b4d0f269a4)

```
kamle@hello UCRT64 ~/xmrig/build
$ "c:\Program Files\CMake\bin\cmake.exe" .. -G "Unix Makefiles" -DXMRIG_DEPS=c:/xmrig-deps/gcc/x64
-- The C compiler identification is unknown
-- The CXX compiler identification is unknown
CMake Error at CMakeLists.txt:2 (project):
  No CMAKE_C_COMPILER could be found.

  Tell CMake where to find the compiler by setting either the environment
  variable "CC" or the CMake cache entry CMAKE_C_COMPILER to the full path to
  the compiler, or to the compiler name if it is in the PATH.


CMake Error at CMakeLists.txt:2 (project):
  No CMAKE_CXX_COMPILER could be found.

  Tell CMake where to find the compiler by setting either the environment
  variable "CXX" or the CMake cache entry CMAKE_CXX_COMPILER to the full path
  to the compiler, or to the compiler name if it is in the PATH.


-- Configuring incomplete, errors occurred!
```

**To Reproduce**
```
1. pacman -S mingw-w64-x86_64-gcc git make
2. git clone https://github.com/xmrig/xmrig.git
3. mkdir xmrig/build && cd xmrig/build
4. "c:\Program Files\CMake\bin\cmake.exe" .. -G "Unix Makefiles" -DXMRIG_DEPS=c:/xmrig-deps/gcc/x64
```

**Expected behavior**
It should compile

**Required data**
 - XMRig v6.21.3
```
1. pacman -S mingw-w64-x86_64-gcc git make
2. git clone https://github.com/xmrig/xmrig.git
3. mkdir xmrig/build && cd xmrig/build
4. "c:\Program Files\CMake\bin\cmake.exe" .. -G "Unix Makefiles" -DXMRIG_DEPS=c:/xmrig-deps/gcc/x64
```
 - OS: [Windows]
 



# Discussion History
## SChernykh | 2024-06-28T15:41:38+00:00
Try this instead:
```
pacman -S git mingw-w64-x86_64-toolchain make mingw-w64-x86_64-cmake
git clone https://github.com/xmrig/xmrig.git
mkdir xmrig/build && cd xmrig/build
cmake .. -G "Unix Makefiles" -DXMRIG_DEPS=c:/xmrig-deps/gcc/x64
make -j$(nproc)
```

## kamlendras | 2024-06-28T16:15:14+00:00
> Try this instead:
> 
> ```
> pacman -S git mingw-w64-x86_64-toolchain make mingw-w64-x86_64-cmake
> git clone https://github.com/xmrig/xmrig.git
> mkdir xmrig/build && cd xmrig/build
> cmake .. -G "Unix Makefiles" -DXMRIG_DEPS=c:/xmrig-deps/gcc/x64
> make -j$(nproc)
> ```
```
kamle@hello UCRT64 ~/xmrig/build
$ cmake .. -G "Unix Makefiles" -DXMRIG_DEPS=c:/xmrig-deps/gcc/x64
-bash: cmake: command not found
```
i do have installed cmake

If i replace `cmake` with `"c:\Program Files\CMake\bin\cmake.exe"` I get the same error 
```
kamle@hello UCRT64 ~/xmrig/build
$ "c:\Program Files\CMake\bin\cmake.exe" .. -G "Unix Makefiles" -DXMRIG_DEPS=c:/xmrig-deps/gcc/x64
-- The C compiler identification is unknown
-- The CXX compiler identification is unknown
CMake Error at CMakeLists.txt:2 (project):
  No CMAKE_C_COMPILER could be found.

  Tell CMake where to find the compiler by setting either the environment
  variable "CC" or the CMake cache entry CMAKE_C_COMPILER to the full path to
  the compiler, or to the compiler name if it is in the PATH.


CMake Error at CMakeLists.txt:2 (project):
  No CMAKE_CXX_COMPILER could be found.

  Tell CMake where to find the compiler by setting either the environment
  variable "CXX" or the CMake cache entry CMAKE_CXX_COMPILER to the full path
  to the compiler, or to the compiler name if it is in the PATH.


-- Configuring incomplete, errors occurred!

```

## SChernykh | 2024-06-28T16:20:25+00:00
Did you run `pacman -S git mingw-w64-x86_64-toolchain make mingw-w64-x86_64-cmake` ? cmake must be installed from within msys2.

## kamlendras | 2024-06-28T16:31:04+00:00
> cmake .. -G "Unix Makefiles" -DXMRIG_DEPS=c:/xmrig-deps/gcc/x64

I installed cmake via msys2 
![err2](https://github.com/xmrig/xmrig/assets/96082996/7d50c3d3-f0b2-4ec5-a00c-f81cda79cad8)


## SChernykh | 2024-06-28T16:33:00+00:00
It can't find GCC compiler. Did you also install `mingw-w64-x86_64-toolchain`? Why do I have to repeat everything twice?

## kamlendras | 2024-06-28T16:34:25+00:00
> mingw-w64-x86_64-toolchain

yes, i have installed `mingw-w64-x86_64-toolchain`

## SChernykh | 2024-06-28T16:38:55+00:00
Then something is broken in your msys2 installation. If you run `gcc --version`, what does it print?

## kamlendras | 2024-06-28T16:39:34+00:00
> Then something is broken in your msys2 installation. If you run `gcc --version`, what does it print?

```
kamle@hello UCRT64 ~/xmrig/build
$ gcc --version
-bash: gcc: command not found
```

## SChernykh | 2024-06-28T16:43:57+00:00
If by this point you tried to install both `mingw-w64-x86_64-gcc` and `mingw-w64-x86_64-toolchain`, GCC must've been there 100%. I'd recommend to make a fresh install of MSYS2, something is broken in your current install.

# Action History
- Created by: kamlendras | 2024-06-28T14:06:38+00:00
- Closed at: 2025-06-18T22:11:10+00:00
