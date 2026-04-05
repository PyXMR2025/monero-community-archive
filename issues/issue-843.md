---
title: CMAKE_MAKE_PROGRAM is not set
source_url: https://github.com/xmrig/xmrig/issues/843
author: prismspecs
assignees: []
labels: []
created_at: '2018-10-24T12:55:22+00:00'
updated_at: '2018-10-24T12:59:53+00:00'
type: issue
status: closed
closed_at: '2018-10-24T12:59:53+00:00'
---

# Original Description
This is clearly a dev environment problem, but I'm curious if there's a quick fix? I got thru the pacman setup but on cmake I get:

```
C:\Users\admin\Desktop\workbench\xmrig\build>cmake .. -G "Unix Makefiles" -DXMRIG_DEPS=c:/xmrig-deps/gcc/x64
CMake Error: CMake was unable to find a build program corresponding to "Unix Makefiles".  CMAKE_MAKE_PROGRAM is not set.  You probably need to select a different build tool.
CMake Error: CMAKE_C_COMPILER not set, after EnableLanguage
CMake Error: CMAKE_CXX_COMPILER not set, after EnableLanguage
-- Configuring incomplete, errors occurred!
See also "C:/Users/admin/Desktop/workbench/xmrig/build/CMakeFiles/CMakeOutput.log".
```

# Discussion History
## prismspecs | 2018-10-24T12:59:53+00:00
Just needed to reinstall MINGw64

# Action History
- Created by: prismspecs | 2018-10-24T12:55:22+00:00
- Closed at: 2018-10-24T12:59:53+00:00
