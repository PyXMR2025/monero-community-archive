---
title: error compiling FileLog.cpp
source_url: https://github.com/xmrig/xmrig/issues/64
author: prismspecs
assignees: []
labels: []
created_at: '2017-08-18T23:35:45+00:00'
updated_at: '2017-10-02T12:02:27+00:00'
type: issue
status: closed
closed_at: '2017-10-02T12:02:27+00:00'
---

# Original Description
```
1>------ Build started: Project: xmrig, Configuration: Debug x64 ------
1>FileLog.cpp
1>C:\Users\dagobah\Downloads\xmrig\src\log\FileLog.cpp(37): error C2065: 'O_CREAT': undeclared identifier
1>C:\Users\dagobah\Downloads\xmrig\src\log\FileLog.cpp(37): error C2065: 'O_APPEND': undeclared identifier
1>C:\Users\dagobah\Downloads\xmrig\src\log\FileLog.cpp(37): error C2065: 'O_WRONLY': undeclared identifier
1>C:\Users\dagobah\Downloads\xmrig\src\log\FileLog.cpp(37): error C2660: 'uv_fs_open': function does not take 5 arguments
1>C:\Users\dagobah\Downloads\xmrig\src\log\FileLog.cpp(91): warning C4267: 'argument': conversion from 'size_t' to 'unsigned int', possible loss of data
1>Done building project "xmrig.vcxproj" -- FAILED.
2>------ Skipped Build: Project: ALL_BUILD, Configuration: Debug x64 ------
2>Project not selected to build for this solution configuration 
========== Build: 0 succeeded, 1 failed, 3 up-to-date, 1 skipped ==========

```

# Discussion History
## NmxMilk | 2017-08-19T10:20:28+00:00
Hello,
You should provide context information (paltform, compiler version, etc.) and steps to reproduce your problem !
At first glance, this seems to be due to missing include files (man open under linux) :
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>

The error concerning uv_fs_open may indicate you're using the wrong version of libuv.
Hope this helps
Cheers

## xmrig | 2017-08-19T11:06:34+00:00
According #65 issue you try use mingw library, you should use **libuv.lib** not **libuv.a**.
Now you can use prebuilt libuv https://github.com/xmrig/xmrig-deps/releases I receive a lot of questions about where find libuv.
Also you need change Debug build to Release.
Thank you.

## prismspecs | 2017-08-21T18:03:43+00:00
Thank you. So with the pre built uvlib, I should re-create the build folder and then execute the cmake line in command line, referencing these files rather than program files/uvlib/ etc?

## xmrig | 2017-08-21T18:07:44+00:00
Right.

## prismspecs | 2017-08-21T19:31:47+00:00
Alright, getting closer! Now I've got:

```
4>App.obj : MSIL .netmodule or module compiled with /GL found; restarting link with /LTCG; add /LTCG to the link command line to improve linker performance
4>App.obj : error LNK2001: unresolved external symbol "public: __cdecl FileLog::FileLog(char const *)" (??0FileLog@@QEAA@PEBD@Z)
4>C:\Users\dagobah\Downloads\xmrig\build\Release\xmrig.exe : fatal error LNK1120: 1 unresolved externals
4>Done building project "xmrig.vcxproj" -- FAILED.
```


## xmrig | 2017-08-22T08:34:35+00:00
It's pretty strange maybe you deleted FileLog.cpp from project?

## prismspecs | 2017-08-22T17:02:36+00:00
Hmm no, FileLog.cpp is still there.
Here is the entire output if it's helpful:

```
1>------ Build started: Project: xmrig, Configuration: Release x64 ------
1>App.obj : MSIL .netmodule or module compiled with /GL found; restarting link with /LTCG; add /LTCG to the link command line to improve linker performance
1>App.obj : error LNK2001: unresolved external symbol "public: __cdecl FileLog::FileLog(char const *)" (??0FileLog@@QEAA@PEBD@Z)
1>C:\Users\dagobah\Downloads\xmrig\build\Release\xmrig.exe : fatal error LNK1120: 1 unresolved externals
1>Done building project "xmrig.vcxproj" -- FAILED.
2>------ Skipped Build: Project: ALL_BUILD, Configuration: Release x64 ------
2>Project not selected to build for this solution configuration 
```

# Action History
- Created by: prismspecs | 2017-08-18T23:35:45+00:00
- Closed at: 2017-10-02T12:02:27+00:00
