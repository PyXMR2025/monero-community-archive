---
title: Xmrig build problems
source_url: https://github.com/xmrig/xmrig/issues/894
author: W33v3ly
assignees: []
labels: []
created_at: '2018-12-13T12:16:31+00:00'
updated_at: '2019-08-02T13:05:41+00:00'
type: issue
status: closed
closed_at: '2019-08-02T13:05:41+00:00'
---

# Original Description
Hello today i try built a new xmrig 2.8.3 x86  with Visual Studio 2017 x86  but with that error

![asdasd](https://user-images.githubusercontent.com/28385369/49938120-337d2d00-fed9-11e8-921a-0bf62e7e339f.png)

With Xmrig-2.8.1 i dont have any problems but on 2.8.3 yes any advice? Thx

Inside linker i have this : C:\OpenSSL-Win32\lib\VC\static\libssl32MT.lib;C:\OpenSSL-Win32\lib\VC\static\libcrypto32MT.lib;C:\xmrig-deps\msvc2017\x86\lib\libuv.lib;C:\xmrig-deps\msvc2017\x86\lib\libmicrohttpd.lib;ws2_32.lib;psapi.lib;iphlpapi.lib;userenv.lib;Crypt32.lib;src\3rdparty\libcpuid\Release\cpuid.lib;kernel32.lib;user32.lib;gdi32.lib;winspool.lib;shell32.lib;ole32.lib;oleaut32.lib;uuid.lib;comdlg32.lib;advapi32.lib  


# Discussion History
## DeadManWalkingTO | 2019-03-17T15:16:51+00:00
Please try to build the [latest XMRig version](https://github.com/xmrig/xmrig/releases/latest).
cmake
```
cmake .. -G "Visual Studio 15 2017 Win64" -DXMRIG_DEPS=c:\xmrig-deps\msvc2017\x86 -DWITH_LIBCPUID=OFF
```
Info:
`-DWITH_LIBCPUID=OFF will remove cpuid lib.`

1. Open project in Visual Studio.
2. a. Add new project configuration as Win32.
2.b. Copy settings from: x64.
2.c. Check to create new project platforms.
3. Save all

4.a. Open `\build\xmrig.vcxproj` file with text editor
4b. Replace all machine:x64 with machine:x86.

5. Build ALL_BUILD project.

That's all. The output `.exe` file should be x86.

Does the issue still exist?
Feedback please.
Thank you!

# Action History
- Created by: W33v3ly | 2018-12-13T12:16:31+00:00
- Closed at: 2019-08-02T13:05:41+00:00
