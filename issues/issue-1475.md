---
title: Building with Clang on Windows
source_url: https://github.com/xmrig/xmrig/issues/1475
author: passnet
assignees: []
labels:
- bug
created_at: '2019-12-31T07:49:43+00:00'
updated_at: '2021-04-12T15:06:18+00:00'
type: issue
status: closed
closed_at: '2021-04-12T15:06:18+00:00'
---

# Original Description
Trying to build xmrig-5.5.0 on Windows/MSYS2-mingw64 with latest CLang:
```
clang version 9.0.0 (https://github.com/msys2/MINGW-packages.git fdafa4d8c4022588676c8ec0985dafaf834258ae)
Target: x86_64-w64-windows-gnu
Thread model: posix
```

Build command: `CC=clang CXX=clang++ cmake . -G "Unix Makefiles" && make -j12`

Fails with following error:

```
[ 11%] Linking CXX executable xmrig.exe
C:\msys64\mingw64\bin\ld: CMakeFiles/xmrig.dir/objects.a(Rx_win.cpp.obj):Rx_win.cpp:(.text+0x1140): multiple definition of `TLS wrapper function for xmrig::Rx::m_mainLoopBounds'; CMakeFiles/xmrig.dir/objects.a(jit_compiler_x86.cpp.obj):jit_compiler_x86.c:(.text+0x1d30): first defined here
```

# Discussion History
## SChernykh | 2019-12-31T09:57:26+00:00
Can you try to compile with https://github.com/xmrig/xmrig/pull/1477 ?

## passnet | 2019-12-31T10:49:56+00:00
Yes, it builds & works now. Thanks!
![Screenshot_20191231_134850](https://user-images.githubusercontent.com/34266118/71619222-66718c00-2bd4-11ea-964f-a9e28d938ec8.png)


## turb1te | 2019-12-31T12:32:49+00:00
@passnet Does Clang give more hashes than gcc/msvc?
@SChernykh Can you tell me how to do this?

## passnet | 2019-12-31T12:43:20+00:00
@martobg10 it used to give me ~1-2% more on old cn/r algo. But that was compared to old gcc-5. Not tested on rx/compared to new gcc yet. Was curious to build & try but not sure when I'll be able to test it now.

You can try building it on your own & test. Just do `git clone https://github.com/xmrig/xmrig && git checkout dev` after use a build command like in my 1st post here. You need to have git, clang-9, clang++-9 packages installed on MSYS2.

## turb1te | 2019-12-31T13:08:30+00:00
Thank you for your answer!
I have a problem:
```
martobg10@DESKTOP-XXXXXXX MINGW64 ~
# git clone https://github.com/xmrig/xmrig && git checkout dev
Cloning into 'xmrig'...
remote: Enumerating objects: 29, done.
remote: Counting objects: 100% (29/29), done.
remote: Compressing objects: 100% (27/27), done.
remote: Total 16197 (delta 9), reused 10 (delta 2), pack-reused 16168
Receiving objects: 100% (16197/16197), 6.12 MiB | 4.66 MiB/s, done.
Resolving deltas: 100% (11892/11892), done.
**fatal: not a git repository (or any of the parent directories): .git**
```


## SChernykh | 2019-12-31T13:10:24+00:00
@martobg10 he forgot to do `cd xmrig` first. Change folder to `xmrig` and then do `git checkout dev`

## turb1te | 2019-12-31T13:30:30+00:00
Thank you! Everything works fine.

## 2010phenix | 2020-01-01T01:46:54+00:00
> Thank you! Everything works fine.

and what we have? any H\s up?

## turb1te | 2020-01-02T07:21:30+00:00
> > Thank you! Everything works fine.
> 
> and what we have? any H\s up?

GCC gives me more hashes than MSVS on Windows 10 OS. For Clang I didn't try.

# Action History
- Created by: passnet | 2019-12-31T07:49:43+00:00
- Closed at: 2021-04-12T15:06:18+00:00
