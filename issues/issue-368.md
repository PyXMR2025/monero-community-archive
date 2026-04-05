---
title: '[Windows] Compile 32bit version with visual studio 2015 and CMake ?'
source_url: https://github.com/xmrig/xmrig/issues/368
author: ondradus
assignees: []
labels: []
created_at: '2018-01-28T10:54:45+00:00'
updated_at: '2019-06-13T22:35:48+00:00'
type: issue
status: closed
closed_at: '2018-01-28T14:25:40+00:00'
---

# Original Description
Hello!
Ive been trying to compile xmrig with  VS2015 as Win32 application.
I can compile 64 bit (Win64) version with VS2015/2017 fine but cant compile 32 bit version (Win32).
However, i strictly need to compile it as 32 bit in vs 2015.

Here is my batch build file ` "%PROGRAMFILES%\CMake\bin\cmake" .. -G "Visual Studio 14 2015 Win32" -DUV_INCLUDE_DIR="C:\xmrig-deps-v2_1\msvc2015\libuv\x86\include" -DUV_LIBRARY="C:\xmrig-deps-v2_1\msvc2015\libuv\x86\lib\libuv.lib" -DMHD_INCLUDE_DIR="C:\xmrig-deps-v2_1\msvc2015\libmicrohttpd\x86\include" -DMHD_LIBRARY="C:\xmrig-deps-v2_1\msvc2015\libmicrohttpd\x86\lib\libmicrohttpd.lib"`

CMake gives me this error: `CMake Error: Could not create named generator Visual Studio 14 2015 Win32`.

Am I missing some VS tools or something like that ? Does anyone know how to approach this ? 

Thank you!

# Discussion History
## metalurgus | 2018-01-28T13:37:47+00:00
have you tried `Visual Studio 14 2015 Win64` instead of `Visual Studio 14 2015 Win32`? AFAIK it is not a target platform


## ondradus | 2018-01-28T14:10:17+00:00
thanks but i have stated that i need to compile it specifically as Win32...not win64. i need a 32bit version of xmirg.

## metalurgus | 2018-01-28T14:11:58+00:00
`Win64` does not mean what you will get as an output. It is something else. You will get 32 bit binary as an output using `Visual Studio 14 2015 Win64`

## ondradus | 2018-01-28T14:24:34+00:00
thanks for clarifying.  I've compiled it with the settings you stated  and tried to run it in my Windows 7 32bit virtual machine. It didn't give any runtime library errors, however it said that the binary can't be executed.

I solved this issue by compiling via mingw32 and gcc. Now it runs everywhere ☺

## metalurgus | 2018-01-28T14:30:55+00:00
I have just build 32 bit version:
I had to remove CPUID lib support for it to build 32 bit. Was unable to make it build as 32 bit. 
Steps:

Cmake command (you called it a batch build file):

`cmake .. -G "Visual Studio 15 2017 Win64" -DUV_INCLUDE_DIR="c:\xmrig\msvc2017\libuv\x86\include" -DUV_LIBRARY="c:\xmrig\msvc2017\libuv\x86\lib\libuv.lib" -DMHD_INCLUDE_DIR="c:\xmrig\msvc2017\libmicrohttpd\x86\include" -DMHD_LIBRARY="c:\xmrig\msvc2017\libmicrohttpd\x86\lib\libmicrohttpd.lib" -DWITH_LIBCPUID=OFF`

`-DWITH_LIBCPUID=OFF` will remove cpuid lib.

Open generated project in the visual studio
Add new project configuration as `Win32`, ccopy settings from: x64, check to create new project platforms. 
Save all

Open 
`\build\xmrig.vcxproj` filewith any text editor, and replace all accurances of `machine:x64` with `machine:x86`. 

In visual studio choose to Reload this file (didn't try `Reload solution`, I think it might break something)

Finally build ALL_BUILD project. Now it should build just fine, output .exe should be x86.

But you did right to build it with mingw32 - it is easier, and cpuid lib works

## noname29 | 2019-06-13T22:35:48+00:00
How did you compile it as 32 bit? Can yuou please show the steps? I need it compiled as a dll and 32 bits. I was able to compile it as a dll with visual studio 2017 but I am running into problems as I try it for 32 bits. Can you give me some tips ?

# Action History
- Created by: ondradus | 2018-01-28T10:54:45+00:00
- Closed at: 2018-01-28T14:25:40+00:00
