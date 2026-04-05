---
title: 'compile issue '
source_url: https://github.com/xmrig/xmrig/issues/2251
author: zhekafun
assignees: []
labels:
- question
created_at: '2021-04-09T08:33:42+00:00'
updated_at: '2025-03-16T13:59:15+00:00'
type: issue
status: closed
closed_at: '2021-04-12T13:28:51+00:00'
---

# Original Description
cmake optios

cmake .. -G "Unix Makefiles" -DWITH_CUDA=OFF -DWITH_NVML=OFF -DWITH_CN_LITE=OFF -DWITH_ARGON2=OFF -DWITH_ADL=OFF -DWITH_OPENCL=OFF -DWITH_CN_HEAVY=OFF -DWITH_CN_PICO=OFF -DWITH_ASTROBWT=OFF -DWITH_KAWPOW=OFF -DXMRIG_DEPS=c:/xmrig-deps-master/gcc/x64

result
[ 69%] Building C object CMakeFiles/xmrig.dir/src/crypto/cn/c_blake256.c.o
/home/zheko/xmrig/src/crypto/common/VirtualMemory_unix.cpp: In static member function ‘static void* xmrig::VirtualMemory::allocateExecutableMemory(size_t, bool)’:
/home/zheko/xmrig/src/crypto/common/VirtualMemory_unix.cpp:148:109: error: ‘MAP_POPULATE’ was not declared in this scope; did you mean ‘MAP_PRIVATE’?
  148 |         mem = mmap(0, align(size), PROT_READ | PROT_WRITE | SECURE_PROT_EXEC, MAP_PRIVATE | MAP_ANONYMOUS | MAP_POPULATE | hugePagesFlag(hugePageSize()), -1, 0);
      |                                                                                                             ^~~~~~~~~~~~
      |                                                                                                             MAP_PRIVATE
/home/zheko/xmrig/src/crypto/common/VirtualMemory_unix.cpp: In static member function ‘static void* xmrig::VirtualMemory::allocateLargePagesMemory(size_t)’:
/home/zheko/xmrig/src/crypto/common/VirtualMemory_unix.cpp:168:85: error: ‘MAP_HUGETLB’ was not declared in this scope; did you mean ‘MAP_HUGE_MASK’?
  168 |     void *mem = mmap(0, size, PROT_READ | PROT_WRITE, MAP_PRIVATE | MAP_ANONYMOUS | MAP_HUGETLB | MAP_POPULATE | hugePagesFlag(hugePageSize()), 0, 0);
      |                                                                                     ^~~~~~~~~~~
      |                                                                                     MAP_HUGE_MASK
/home/zheko/xmrig/src/crypto/common/VirtualMemory_unix.cpp:168:99: error: ‘MAP_POPULATE’ was not declared in this scope; did you mean ‘MAP_PRIVATE’?
  168 |     void *mem = mmap(0, size, PROT_READ | PROT_WRITE, MAP_PRIVATE | MAP_ANONYMOUS | MAP_HUGETLB | MAP_POPULATE | hugePagesFlag(hugePageSize()), 0, 0);
      |                                                                                                   ^~~~~~~~~~~~
      |                                                                                                   MAP_PRIVATE
make[2]: *** [CMakeFiles/xmrig.dir/build.make:1356: CMakeFiles/xmrig.dir/src/crypto/common/VirtualMemory_unix.cpp.o] Error 1
make[2]: *** Waiting for unfinished jobs....
make[1]: *** [CMakeFiles/Makefile2:133: CMakeFiles/xmrig.dir/all] Error 2
make: *** [Makefile:103: all] Error 2


# Discussion History
## SChernykh | 2021-04-09T08:37:49+00:00
```
1. pacman -S mingw-w64-x86_64-gcc git make
2. git clone https://github.com/xmrig/xmrig.git
3. mkdir xmrig/build && cd xmrig/build
4. "c:\Program Files\CMake\bin\cmake.exe" .. -G "Unix Makefiles" -DXMRIG_DEPS=c:/xmrig-deps/gcc/x64
5. make -j$(nproc)
```
Step 4 uses cmake you have to install separately. The one in msys64 doesn't work with xmrig.

## snipeTR | 2021-04-09T09:04:12+00:00
Why msys64 cmake doesn't work with xmrig.

## xmrig | 2021-04-09T11:00:37+00:00
@snipeTR It works, but not always, so the safest option is use external cmake. I didn't really investigate what exactly was wrong with msys64 cmake.
Thank you.

## Spudz76 | 2021-04-10T01:26:06+00:00
I've never gotten it to work, same error.  It seems to think it's on Linux, probably because the compiler isn't defining any of the Windows OS defines.  Seems there was some flag to get it to act like it's Windows.  At some point they changed the default so Linux code would more likely just work out-of-the-box without knowing about windows at all (the primary use of msys64 is to run simple Linux code without porting).  But VirtualMemory things are very very different.  I may have been trying to compile under cygwin64 but same issue, it thought it was Linux.

Easy enough to just install VS2019 Build Tools which is how I solved the problem, haha.

## greatwolf | 2025-03-16T13:45:37+00:00
I actually ran into this similar issue myself. I did manage to get it to build though.

There are a couple of subtle things to note in the build setup:

 - Make sure you are using the 64-bit version of the toolchain eg. `mingw-w64-x86_64-gcc` + `msys2_shell.cmd -mingw64`. I found that if I use the 32-bit version `mingw-w64-i686-gcc` + `msys2_shell.cmd -mingw32` then the build will fail at some point with the OP's errors about stuff like `MAP_POPULATE` not being declared.
 - `mingw-w64-x86_64-cmake` appears to work for me. Note, msys2 `pacman` has a couple cmake variants like `msys/cmake`, `clangarm64/mingw-w64-clang-aarch64-cmake`, `mingw64/mingw-w64-x86_64-cmake` etc. Make sure to use `mingw-w64-x86_64-cmake` one. The main different far as I can tell is msys version has some generators missing eg. `MinGW Makefiles` being one -- likely assuming a true *nix environment rather than Windows. That might be the reason why sometimes cmake feels unreliable.
 - Make sure `-DXMRIG_DEPS=...` is an absolute path rather than relative. CMake does not like relative paths to the dependences.

I'll just leave the build instructions I used here for future visitors.

Start a msys2 terminal session with:

    msys2_shell.cmd -mingw64

Setup and build with the following:

```
pacman -S mingw-w64-x86_64-cmake mingw-w64-x86_64-gcc git make

git clone https://github.com/xmrig/xmrig.git
cd xmrig

git clone https://github.com/xmrig/xmrig-deps.git

cmake -B ./build -G "Unix Makefiles" -DXMRIG_DEPS=$(pwd)/xmrig-deps/gcc/x64/
cmake --build ./build

# or to see full build commands
# cmake --build ./build --verbose 
```

# Action History
- Created by: zhekafun | 2021-04-09T08:33:42+00:00
- Closed at: 2021-04-12T13:28:51+00:00
