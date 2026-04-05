---
title: How to compile xmrig with clang on windows
source_url: https://github.com/xmrig/xmrig/issues/3317
author: makalamaba
assignees: []
labels: []
created_at: '2023-08-13T13:08:37+00:00'
updated_at: '2024-11-22T09:16:26+00:00'
type: issue
status: closed
closed_at: '2024-11-22T09:16:26+00:00'
---

# Original Description
I compile xmrig with clang which produces a lot of errors

Step1:
Install vs2019 and clang12
![Snipaste_2023-08-13_16-56-29](https://github.com/xmrig/xmrig/assets/142157372/4ffbb30d-f07a-44ee-b4cb-1a94acc4f796)

Step 2:
download xmrig-6.20.0 and xmrig-deps-4.1
![image](https://github.com/xmrig/xmrig/assets/142157372/fd2d87be-48d3-4f45-8d2f-9034abe3219c)

Step 3:
cmake .. -G "Visual Studio 16 2019" -DXMRIG_DEPS=c:/xmrig-deps-4.1/msvc2019/x64
![image](https://github.com/xmrig/xmrig/assets/142157372/d853bf6e-d01e-4162-b554-fbde7b413631)

Step 4:
Modify the "Platform Toolset" set to "LLVM(clang-cl)"
![image](https://github.com/xmrig/xmrig/assets/142157372/6eca44c9-e800-429b-9e15-21e8be13cc74)

Step 5:
compile and error
![image](https://github.com/xmrig/xmrig/assets/142157372/ad8d2360-1d3c-4181-b512-a824db52c763)




what should I do？


# Discussion History
## SChernykh | 2023-08-13T13:35:53+00:00
clang compilation is not supported on Windows. You can build XMRig on Windows using standard Visual Studio compiler, or using MSYS2: https://xmrig.com/docs/miner/build/windows

You could try running cmake with clang option:
`cmake .. -G "Visual Studio 16 2019" -DXMRIG_DEPS=C:\xmrig-deps\msvc2019\x64 -T ClangCL`
But it doesn't recognize dependencies because they were prepared for Visual Studio compiler.

P.S. Theoretically, you could install clang in MSYS2 and try to build it there. But why are you trying to use clang on Windows? It will not give you better hashrate.

## makalamaba | 2023-08-13T15:28:01+00:00
> clang compilation is not supported on Windows. You can build XMRig on Windows using standard Visual Studio compiler, or using MSYS2: https://xmrig.com/docs/miner/build/windows
> 
> You could try running cmake with clang option: `cmake .. -G "Visual Studio 16 2019" -DXMRIG_DEPS=C:\xmrig-deps\msvc2019\x64 -T ClangCL` But it doesn't recognize dependencies because they were prepared for Visual Studio compiler.
> 
> P.S. Theoretically, you could install clang in MSYS2 and try to build it there. But why are you trying to use clang on Windows? It will not give you better hashrate.

Thanks for your suggestion.But it still fails to compile on msys2

```
cmake .. -G "Unix Makefiles" -DXMRIG_DEPS=c://xmrig-deps-4.1/gcc/x64
make -j8
```
![image](https://github.com/xmrig/xmrig/assets/142157372/6ba1d8b4-95bf-4044-b485-c14776e60418)
![image](https://github.com/xmrig/xmrig/assets/142157372/da23370a-9266-4910-8df3-42723a0fbef2)


## makalamaba | 2023-08-13T15:37:59+00:00
If I specify the compiler as gcc, it works fine.
cmake .. -G "Unix Makefiles" -DXMRIG_DEPS=c://xmrig-deps-4.1/gcc/x64 -DCMAKE_C_COMPILER=gcc -DCMAKE_CXX_COMPILER=g++


The tools I installed are as follows
```
pacman -S mingw-w64-x86_64-gcc git make
pacman -S mingw-w64-clang-x86_64-toolchain
```

## SChernykh | 2023-08-13T15:56:16+00:00
```
#ifdef __GNUC__
#   include <fcntl.h>
#   include <sys/stat.h>
#   include <ext/stdio_filebuf.h>
#endif
```
This code is directly incompatible with clang on Windows, because `stdio_filebuf.h` is a GCC-only extension. So you can't compile it with clang on Windows unless source code is fixed first. As I told before, this is not a supported configuration.

# Action History
- Created by: makalamaba | 2023-08-13T13:08:37+00:00
- Closed at: 2024-11-22T09:16:26+00:00
