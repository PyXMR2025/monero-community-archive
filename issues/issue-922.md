---
title: Problems compiling/running Windows 7/10
source_url: https://github.com/xmrig/xmrig/issues/922
author: sanitariu
assignees: []
labels: []
created_at: '2019-01-28T18:33:36+00:00'
updated_at: '2020-07-28T01:56:37+00:00'
type: issue
status: closed
closed_at: '2019-08-02T12:56:28+00:00'
---

# Original Description
I compiled xmrig for windows using https://github.com/xmrig/xmrig/wiki/Windows-Build
MSYS2 64 bit version.
After running the application it crashes immediately with the following error:
"The application was unable to start correctly (0xc000007b). Click OK to close the application"

How i can fix this ?

# Discussion History
## snipeTR | 2019-01-28T21:44:41+00:00
Run.bat

@echo off
Xmrig.exe
Pause

Save and run


## sanitariu | 2019-01-29T17:34:29+00:00
I tried but it does not work. The same problem.

https://imgur.com/a/7llxNun

## sanitariu | 2019-01-30T11:14:59+00:00
Confirmed latest msys64 can not build static xmrig.
Using the following. Clean build directory.

cmake .. -G "Unix Makefiles" -DXMRIG_DEPS=c:/xmrig-deps/gcc/x64 -DWITH_HTTPD=OFF -DBUILD_STATIC=ON

Binary is built but after running it asks for linwinpthread-1.dll, then later for libstds++-6.dll, libgcc ....

Seems like windows build is broken and need fixes.
I will try manually copy all the files it needs in the current directory.






## sanitariu | 2019-01-30T12:32:44+00:00
I tried manually put all needed files in the same folder and finally after some hours i have again:
"The application was unable to start correctly (0xc000007b). Click OK to close the application"
Anyone can try build this from clean msys64 and latest xmrig git ?

## DeadManWalkingTO | 2019-03-17T16:07:47+00:00
1. Delete old `msys64` folder.
2. Use the `msys2-x86_64-20181211.exe` (clean install).
3. DO NOT UPDATE & DO NOT UPGRADE MSYS.
4. Run:
```
pacman -S mingw-w64-x86_64-gcc
pacman -S make
pacman -S mingw-w64-x86_64-cmake
pacman -S mingw-w64-x86_64-pkg-config
```
5. Download and decompress xmrig-deps.
6. Clone xmrig.
7. Run ```cmake .. -G "Unix Makefiles" -DXMRIG_DEPS=c:/xmrig-deps/gcc/x64```.
8. Run ```make```

Feedback please.
Thank you!

## alterhu2020 | 2020-07-28T01:56:11+00:00
Try to compire with VS2019 not use **msys2** maybe this helps: https://code.pingbook.top/blog/setup/bitcoin-mining-setup.html#windows%E7%BC%96%E8%AF%91%E5%AE%89%E8%A3%85%E8%84%9A%E6%9C%ACxmrig%E9%9B%B6%E6%8A%BD%E6%B0%B4

# Action History
- Created by: sanitariu | 2019-01-28T18:33:36+00:00
- Closed at: 2019-08-02T12:56:28+00:00
