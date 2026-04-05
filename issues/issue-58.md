---
title: Can't compile x64 in VS 2017
source_url: https://github.com/xmrig/xmrig/issues/58
author: Leo1906
assignees: []
labels: []
created_at: '2017-08-11T09:52:59+00:00'
updated_at: '2017-08-12T06:36:26+00:00'
type: issue
status: closed
closed_at: '2017-08-12T06:36:26+00:00'
---

# Original Description
I have no problem compiling the project in x86 (different project file, created with cmake and VS 2017 (32 Bit) compiler).
But as soon as it gets to x64 it fails. I build libuv correctly and gave the correct path when using cmake. When trying to build the release in Visual Studio I get 44 errors saying:

C:\Users\root\Downloads\xmrig-master\build\Release\xmrig.exe : fatal error LNK1120: 44 nicht aufgel÷ste Externe Symbole

or 

App.obj : error LNK2001: Nicht aufgel÷stes externes Symbol "uv_signal_start".

That means that it can't find the libuv, right? Or where's the error?
But why does it work for 32 bit application and not for 64 bit?

Only XMRig can't be build. The rest of the project can be build without any problem.
How do I fix this error?

Thanks a lot! :)

# Discussion History
## xmrig | 2017-08-11T16:23:42+00:00
Looks like you point cmake to wrong libuv version, maybe 32bit. You need 2 libuv one for 64bit one for 32bit.
Thank you.

## Leo1906 | 2017-08-11T17:02:09+00:00
Yeah of course I compiled libuv for x64 and for x32. For building the x64 XMRig I pointed to libuv (x64). Do I need to point to x32 as well?

## xmrig | 2017-08-11T17:09:45+00:00
64bit build required 64bit libuv
How do you build libuv? Did you use `vcbuild.bat`? If yes was you add `x64` param?

This error mean linker not found suitable symbols, wrong lib/arch. CMake check only existence of .lib file.

## Leo1906 | 2017-08-12T06:32:29+00:00
I thought I did so .. I have done everything aggain from scratch now and it works! :)
Thanks for your help :)

# Action History
- Created by: Leo1906 | 2017-08-11T09:52:59+00:00
- Closed at: 2017-08-12T06:36:26+00:00
