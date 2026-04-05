---
title: "  Could NOT find UV (missing: UV_LIBRARY UV_INCLUDE_DIR)\t"
source_url: https://github.com/xmrig/xmrig/issues/1236
author: wcsmomo
assignees: []
labels:
- question
created_at: '2019-10-12T10:34:27+00:00'
updated_at: '2022-04-13T01:52:01+00:00'
type: issue
status: closed
closed_at: '2019-11-15T07:23:05+00:00'
---

# Original Description
I made a mistake when using vs 2019 to connect GitHub to import xmrig projects:



CMake Error at E:/Program Files (x86)/Microsoft Visual Studio/2019/Community/Common7/IDE/Common Extensions/Microsoft/CMake/CMake/share/cmake-3.15/Modules/FindPackageHandleStandard Args.cmake:137 (message):

Can NOT find UV (missing: UV_LIBRARY UV_INCLUDE_DIR) E:/Program Files (x86)/Microsoft Visual Studio/2019/Community/Common 7/IDE/Common Extensions/Microsoft/CMake/share/cmake-3.15/Modules/FindPackage Args.cmake 137

# Discussion History
## Spudz76 | 2019-11-03T21:38:45+00:00
Windows external deps are in the [xmrig-deps](https://github.com/xmrig/xmrig-deps/) project

You checkout that tree and then provide CMake definition:
`XMRIG_DEPS=C:\src\xmrig-deps\msvc2019\x64`
...but of course using your actual pathspec for where `xmrig-deps` is checked out, and then it should find everything.

I have never used the builtin VS cmake much less the VS IDE (just the build tools, CMake from their site, and a cmd shell) unsure how to add that define to its CMake properties so hopefully you can find it.

My shell cmd for building is:
`cmake -G "Visual Studio 16 2019" -DCMAKE_BUILD_TYPE=Release -DXMRIG_DEPS=C:\src\xmrig-deps\msvc2019\x64 -DCMAKE_VERBOSE_MAKEFILE=ON -DWITH_OPENCL=OFF -DWITH_CUDA=OFF -DWITH_ARGON2=OFF ..`

## NineWoranop | 2021-03-28T02:47:15+00:00
I also try to search this answer. I discover that. If you do the [steps](https://xmrig.com/docs/miner/build/windows) for compile code with Visual Studio 19. You will already got the generated solution and project. You need to use those projects. Not need to create your own project.

## navasquillo | 2021-04-25T12:44:18+00:00
Hello,
I'll do the same steps as [but](https://xmrig.com/docs/miner/build/windows) except install Git because I had installed. My question is, is the steps correct?

## navasquillo | 2021-04-25T12:49:41+00:00
The error is is related with CMake

-- Selecting Windows SDK version 10.0.19041.0 to target Windows 10.0.19042.
CMake Error at C:/Program Files/CMake/share/cmake-3.20/Modules/FindPackageHandleStandardArgs.cmake:230 (message):
  Could NOT find UV (missing: UV_LIBRARY UV_INCLUDE_DIR)
Call Stack (most recent call first):
  C:/Program Files/CMake/share/cmake-3.20/Modules/FindPackageHandleStandardArgs.cmake:594 (_FPHSA_FAILURE_MESSAGE)
  cmake/FindUV.cmake:25 (find_package_handle_standard_args)
  CMakeLists.txt:178 (find_package)


## Spudz76 | 2021-04-25T13:21:56+00:00
If you missed downloading and unpacking (or, git clone) the [xmrig-deps](https://github.com/xmrig/xmrig-deps), and the `-DXMRIG_DEPS=c:\xmrig-deps\msvc2019\x64` piece for cmake (or where your xmrig-deps folder is), it will be unable to find multiple things.

## Fooughhy | 2021-05-05T19:43:03+00:00
I'm having this issue aswell. 
CMake version 3.20.2
MSVC version 19.28.29914.0

Structure is:
C:\Mining\xmrig
C:\Mining\xmrig-deps
Running `cmake .. -G "Visual Studio 16 2019" -A x64 -DXMRIG_DEPS=c:\Mining\xmrig-deps\msvc2019\x64` give the same output as @navasquillo.


## Spudz76 | 2021-05-06T04:57:57+00:00
I use:
`cmake -G "Visual Studio 16 2019" -DCMAKE_BUILD_TYPE=Release -DXMRIG_DEPS=D:\src\xmrig-deps\msvc2019\x64 -DCMAKE_VERBOSE_MAKEFILE=ON -DWITH_OPENCL=OFF -DWITH_ADL=OFF -DWITH_CUDA=OFF -DWITH_NVML=OFF -DWITH_KAWPOW=OFF ..`
and it works, followed by:
`cmake --build . --config Release`
and it builds

## Fooughhy | 2021-05-06T15:26:31+00:00
Thank you! That seems to have worked. Wonder which parameter fixed it 🤔 

## Spudz76 | 2021-05-07T18:35:49+00:00
Dunno, I've used the same build bat file for years and it always works.  Maybe specifying the build type helps.  Or, don't specify architecture (`-A x64`) which only matters if you have more than just VS-x64 installed.

## navasquillo | 2021-05-07T22:03:37+00:00
I cannot compile.
My structure:
C:/xmrig
C:/xmrig-deps
(both cloned from github)
![imagen](https://user-images.githubusercontent.com/61295506/117512831-aac32800-af90-11eb-9425-368631f61284.png)
I've create C:/xmrig/build
Using the Git Bash I pasted the command cmake -G "Visual Studio 16 2019" -DCMAKE_BUILD_TYPE=Release -DXMRIG_DEPS=D:\src\xmrig-deps\msvc2019\x64 -DCMAKE_VERBOSE_MAKEFILE=ON -DWITH_OPENCL=OFF -DWITH_ADL=OFF -DWITH_CUDA=OFF -DWITH_NVML=OFF -DWITH_KAWPOW=OFF ..

and... error!!!

-- Selecting Windows SDK version 10.0.19041.0 to target Windows 10.0.19042.
CMake Error at C:/Program Files/CMake/share/cmake-3.20/Modules/FindPackageHandleStandardArgs.cmake:230 (message):
  Could NOT find UV (missing: UV_LIBRARY UV_INCLUDE_DIR)
Call Stack (most recent call first):
  C:/Program Files/CMake/share/cmake-3.20/Modules/FindPackageHandleStandardArgs.cmake:594 (_FPHSA_FAILURE_MESSAGE)
  cmake/FindUV.cmake:25 (find_package_handle_standard_args)
  CMakeLists.txt:178 (find_package)

![imagen](https://user-images.githubusercontent.com/61295506/117513024-11484600-af91-11eb-9e49-ad6c0a813403.png)



## Spudz76 | 2021-05-08T22:03:33+00:00
BASH doesn't accept backslash, change to `\\` or `/` in paths.

Or use CMD.EXE like normal.

## dday9 | 2021-05-16T05:37:18+00:00
@Spudz76 - I spent about an hour until I realized that my issue was related to the backslash. Once I changed it, it worked. For those of you who want to have a step-by-step guide of what I did after installing cmake and Git BASH:

1. Open up Git BASH
2. Change the directory to C (if necessary) by running: `cd C:/`
3. Clone the XMRig dependencies project ([repo link](https://github.com/xmrig/xmrig-deps)) by running: `git clone https://github.com/xmrig/xmrig-deps.git`
4. Clone the XMRig project ([repo link](https://github.com/xmrig/xmrig)) by running: `git clone https://github.com/xmrig/xmrig.git`
5. Make the "build" directory by running: `mkdir build`
6. Change the directory to the "build" directory by running: `cd build`
7. Compile the project by using the Visual Studio 2019 compiler by running: `cmake -G "Visual Studio 16 2019" -DCMAKE_BUILD_TYPE=Release -DXMRIG_DEPS=C:/xmrig-deps/msvc2019/x64 -DCMAKE_VERBOSE_MAKEFILE=ON -DWITH_OPENCL=OFF -DWITH_ADL=OFF -DWITH_CUDA=OFF -DWITH_NVML=OFF -DWITH_KAWPOW=OFF ..`
8. Build the project by running: `cmake --build . --config Release`

Hopefully this clears it up for someone else who ran into the same issue I did.

## Spudz76 | 2021-05-16T08:40:34+00:00
I believe CMake in general accepts `/` regardless of shell type, so it may be best practice to always use `/`

## vladkras | 2021-11-03T20:04:56+00:00
on macos this error was fixed with
`brew install libuv `

## Spudz76 | 2021-11-04T00:29:01+00:00
Except now you're using whatever (probably older) version of libuv that comes from homebrew, defeating the purpose of using the bundled deps.

## TomerGamerTV | 2022-03-26T12:45:08+00:00
> I use: `cmake -G "Visual Studio 16 2019" -DCMAKE_BUILD_TYPE=Release -DXMRIG_DEPS=D:\src\xmrig-deps\msvc2019\x64 -DCMAKE_VERBOSE_MAKEFILE=ON -DWITH_OPENCL=OFF -DWITH_ADL=OFF -DWITH_CUDA=OFF -DWITH_NVML=OFF -DWITH_KAWPOW=OFF ..` and it works, followed by: `cmake --build . --config Release` and it builds

guys remember to change from "D:\scr\xmrig-deps" to your own folder or it wont work!

## aiden3c | 2022-04-13T01:52:01+00:00
> BASH doesn't accept backslash, change to `\\` or `/` in paths.
> 
> Or use CMD.EXE like normal.

Completely fixed it for me. Thank you!

# Action History
- Created by: wcsmomo | 2019-10-12T10:34:27+00:00
- Closed at: 2019-11-15T07:23:05+00:00
