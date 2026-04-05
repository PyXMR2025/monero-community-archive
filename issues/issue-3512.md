---
title: Compile Error VS 2019
source_url: https://github.com/xmrig/xmrig/issues/3512
author: doadin
assignees: []
labels: []
created_at: '2024-07-18T09:35:35+00:00'
updated_at: '2024-07-18T13:37:05+00:00'
type: issue
status: closed
closed_at: '2024-07-18T13:37:05+00:00'
---

# Original Description
I have tried compiling using appveyor windows vs 2019 image but I get a couple of errors. Same process but using vs 2017 works fine.

**Describe the bug**
Compile Error

**Required data**
 - XMRig version
 - [v6.21.3](https://github.com/xmrig/xmrig/commit/7897f10c48899842749aa74a32d8405e0fe74af1)
    - Either the exact link to a release you downloaded from https://github.com/xmrig/xmrig/releases
    - Or the exact command lines that you used to build XMRig

  - cmd: if "%APPVEYOR_BUILD_WORKER_IMAGE%"=="Visual Studio 2019" (call "C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\Common7\Tools\VsMSBuildCmd.bat")
  - cmd: if "%APPVEYOR_BUILD_WORKER_IMAGE%"=="Visual Studio 2017" (call "C:\Program Files (x86)\Microsoft Visual Studio\2017\Community\Common7\Tools\VsMSBuildCmd.bat")
  - cmd: cd c:\xmrig
  - cmd: mkdir build
  - cmd: cd build
  - cmd: if "%APPVEYOR_BUILD_WORKER_IMAGE%"=="Visual Studio 2019" (set CMAKE_PREFIX_PATH=c:\xmrig-deps-master\msvc2019\x64\)
  - cmd: if "%APPVEYOR_BUILD_WORKER_IMAGE%"=="Visual Studio 2017" (set CMAKE_PREFIX_PATH=c:\xmrig-deps-master\msvc2017\x64\)
  - cmd: if "%APPVEYOR_BUILD_WORKER_IMAGE%"=="Visual Studio 2019" (cmake .. -G "Visual Studio 16 2019" -A x64 -DXMRIG_DEPS=c:\xmrig-deps-master\msvc2019\x64)
  - cmd: if "%APPVEYOR_BUILD_WORKER_IMAGE%"=="Visual Studio 2017" (cmake .. -G "Visual Studio 15 2017 Win64" -DXMRIG_DEPS=c:\xmrig-deps-master\msvc2017\x64)
  - cmd: msbuild xmrig.sln /p:Configuration=Release -m

**Additional context**
Add any other context about the problem here.

       "C:\xmrig\build\xmrig.sln" (default target) (1) ->
       "C:\xmrig\build\xmrig.vcxproj.metaproj" (default target) (12) ->
       "C:\xmrig\build\xmrig.vcxproj" (default target) (24) ->
       (Link target) -> 
         libuv.lib(process.obj) : error LNK2001: unresolved external symbol __imp_SymSetOptions [C:\xmrig\build\xmrig.vcxproj]
         libuv.lib(process.obj) : error LNK2001: unresolved external symbol __imp_SymGetOptions [C:\xmrig\build\xmrig.vcxproj]
         libuv.lib(process.obj) : error LNK2001: unresolved external symbol MiniDumpWriteDump [C:\xmrig\build\xmrig.vcxproj]
         C:\xmrig\build\Release\xmrig.exe : fatal error LNK1120: 3 unresolved externals [C:\xmrig\build\xmrig.vcxproj]
    145 Warning(s)
    4 Error(s)

Whole build log if needed can be found here: https://ci.appveyor.com/api/buildjobs/cau85i49b1vnxdc8/log


# Discussion History
# Action History
- Created by: doadin | 2024-07-18T09:35:35+00:00
- Closed at: 2024-07-18T13:37:05+00:00
