---
title: ERROR C1007 unrecognized flag '-Ot' in 'p2' project xmrig file LINK
source_url: https://github.com/xmrig/xmrig/issues/630
author: felixmoure
assignees: []
labels: []
created_at: '2018-05-15T02:47:04+00:00'
updated_at: '2018-12-06T07:33:04+00:00'
type: issue
status: closed
closed_at: '2018-05-30T09:15:37+00:00'
---

# Original Description
i get LINK 1257 code generation failed. i cloned a few minutes ago, i use xmrig-deps no cmake errors still cant compile debug or release . any clues? 
forgot to say, Visual Studio 2017.

# Discussion History
## xmrig | 2018-05-15T02:55:14+00:00
Please provide all possible information.

1. Version of Visual Studio.
2. cmake command line used to create solution file.
3. cmake output from step 2.
4. Any other useful information.

Thank you.

## felixmoure | 2018-05-15T03:14:22+00:00
cmake .. -G "Visual Studio 15 2017" -DXMRIG_DEPS=c:\xmrig-deps\msvc2017\x86

C:\Users\noseque11\Desktop\xmr1\xmrig-master\build>cmake .. -G "Visual Studio 15 2017" -DXMRIG_DEPS=c:\xmrig-deps\msvc2017\x86
-- The C compiler identification is MSVC 19.13.26131.1
-- The CXX compiler identification is MSVC 19.13.26131.1
-- Check for working C compiler: C:/Program Files (x86)/Microsoft Visual Studio/2017/Community/VC/Tools/MSVC/14.13.26128/bin/Hostx86/x86/cl.exe
-- Check for working C compiler: C:/Program Files (x86)/Microsoft Visual Studio/2017/Community/VC/Tools/MSVC/14.13.26128/bin/Hostx86/x86/cl.exe -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working CXX compiler: C:/Program Files (x86)/Microsoft Visual Studio/2017/Community/VC/Tools/MSVC/14.13.26128/bin/Hostx86/x86/cl.exe
-- Check for working CXX compiler: C:/Program Files (x86)/Microsoft Visual Studio/2017/Community/VC/Tools/MSVC/14.13.26128/bin/Hostx86/x86/cl.exe -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Found UV: C:/xmrig-deps/msvc2017/x86/lib/libuv.lib
-- Looking for syslog.h
-- Looking for syslog.h - not found
-- Found MHD: C:/xmrig-deps/msvc2017/x86/lib/libmicrohttpd.lib
-- Configuring done
-- Generating done
-- Build files have been written to: C:/Users/noseque11/Desktop/xmr1/xmrig-master/build

version 15.7.1 Visual Studio 2017

## xmrig | 2018-05-15T04:20:02+00:00
Did you update xmrig-deps to recent version v3.1? previous versions not compatible with MSVC 15.7.
If yes it might local issue, I checked build all compiled fine.
Thank you.

## felixmoure | 2018-05-16T00:48:47+00:00
super flustrated,  I just downloaded 3.1 deps and cmake again but cant get it to compile same error. 👎 
where can I edit VS compiler settings I cant find the -Ot flag enyware. Everyday I hate more visual studio and fall in love with command line compilers 💯 

## ShannonZ | 2018-05-16T02:48:27+00:00
Using VS2015 instead.

## felixmoure | 2018-05-17T01:16:49+00:00
wanted to let u know it was a local issue. unistalled every sdk /compiler/libraries i had in the system unistalled visual studio, reinstalled visual studio and cmake. After long hours it now compiles fine with visual studio 2017 and 3.1 deps. thank u for the support. i think this issue can be marked as resolved as it wasn't a code error but it might help other who had same issue. 

## BumbrT | 2018-05-24T22:07:16+00:00
I got the same error. Updated Visual Studio to the latest version and it disappeared.

## ShannonZ | 2018-05-28T02:47:11+00:00
“Ot”  is Optimization level. Just disable it


## aleshem | 2018-12-06T07:33:03+00:00
This happened to me after visual studio automatically upgraded. I use Matlab 2015b with Microsoft Visual C++ 2017 
I changed the following things in the .vcxproj project file and now Mex compiles:
1. For each configuration:
    <PlatformToolset>v141</PlatformToolset> 
    changed to
    <PlatformToolset>v120</PlatformToolset>

2. <Project DefaultTargets="Build" ToolsVersion="15.0" xmlns="http://schemas.microsoft.com/developer/msbuild/2003">
    changed to
    <Project DefaultTargets="Build" ToolsVersion="12.0" xmlns="http://schemas.microsoft.com/developer/msbuild/2003">

3. Delete the following line (in PropertyGroup) <WindowsTargetPlatformVersion>10.0.17134.0</WindowsTargetPlatformVersion>

# Action History
- Created by: felixmoure | 2018-05-15T02:47:04+00:00
- Closed at: 2018-05-30T09:15:37+00:00
