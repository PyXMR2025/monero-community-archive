---
title: Fatal error when building project
source_url: https://github.com/xmrig/xmrig/issues/101
author: Valke88
assignees: []
labels:
- bug
created_at: '2017-09-08T09:56:10+00:00'
updated_at: '2017-09-11T19:45:30+00:00'
type: issue
status: closed
closed_at: '2017-09-11T19:45:30+00:00'
---

# Original Description
Hi,

I get a fatal error while compiling:


> 4>App.obj : MSIL .netmodule or module compiled with /GL found; restarting link with /LTCG; add /LTCG to the link command line to improve linker performance
> 4>LINK : fatal error C1047: The object or library file 'C:\libuv-msvc2017-x64\lib\libuv.lib' was created with an older compiler than other objects; rebuild old objects and libraries
> 4>LINK : fatal error LNK1257: code generation failed
> 4>Done building project "xmrig.vcxproj" -- FAILED.
> 5>------ Skipped Build: Project: ALL_BUILD, Configuration: Release x64 ------
> 5>Project not selected to build for this solution configuration 
> ========== Build: 3 succeeded, 1 failed, 0 up-to-date, 1 skipped ==========


It does work when i use the libuv from https://dist.libuv.org/dist/
But then libuv.dll is missing when i open xmrig.exe after compiling.

Any solutions?

Regards, Valke


# Discussion History
## xmrig | 2017-09-08T10:13:13+00:00
I build this library with Visual Studio 2017 version 15.2 you probably run version 15.3.
There 2 options:
* Build own libuv https://github.com/libuv/libuv#windows
* Just wait I will update, own msvc installation and rebuild & upload new libuv build later today.

## Valke88 | 2017-09-08T11:09:55+00:00
Thanks mate

## xmrig | 2017-09-08T13:41:26+00:00
I updated dependencies https://github.com/xmrig/xmrig-deps/releases/tag/v2
Thank you.

# Action History
- Created by: Valke88 | 2017-09-08T09:56:10+00:00
- Closed at: 2017-09-11T19:45:30+00:00
