---
title: Fresh computer with cmake and msys64
source_url: https://github.com/xmrig/xmrig/issues/863
author: liminalsoundscapes
assignees: []
labels: []
created_at: '2018-11-01T13:28:12+00:00'
updated_at: '2018-11-01T14:15:46+00:00'
type: issue
status: closed
closed_at: '2018-11-01T14:15:46+00:00'
---

# Original Description
Hi!

I get the xmrig to compile nicely on visual studio 2017 but i wish to try to compile it using the other compiler, however this is a fresh installed computer, no development tools was installed prior.

I install latest CMake and MSYS2 64 bit

i follow the build instructions and do create the build folder

> cmake .. -G "Unix Makefiles" -DWITH_HTTPD=OFF -DXMRIG_DEPS="c:/xmrig-deps/gcc/x64/"
> 
> C:\msys64\usr\bin\make
> pause

```
C:\source\xmrig-master\build>cmake .. -G "Unix Makefiles" -DWITH_HTTPD=OFF -DXMRIG_DEPS="c:/xmrig-deps/gcc/x64/"
CMake Error: CMake was unable to find a build program corresponding to "Unix Makefiles".  CMAKE_MAKE_PROGRAM is not set.  You probably need to select a different build tool.
CMake Error: CMAKE_C_COMPILER not set, after EnableLanguage
CMake Error: CMAKE_CXX_COMPILER not set, after EnableLanguage
-- Configuring incomplete, errors occurred!
See also "C:/source/xmrig-master/build/CMakeFiles/CMakeOutput.log".

C:\source\xmrig-master\build>C:\msys64\usr\bin\make
make: *** No targets specified and no makefile found.  Stop.

C:\source\xmrig-master\build>pause
Press any key to continue . . .
```

the output log reads: The system is: Windows - 10.0.17134 - AMD64

would appreciate some pointers in the right direction

# Discussion History
# Action History
- Created by: liminalsoundscapes | 2018-11-01T13:28:12+00:00
- Closed at: 2018-11-01T14:15:46+00:00
