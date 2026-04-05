---
title: Compile errors whilst building version 4.4.0-beta from source files
source_url: https://github.com/xmrig/xmrig/issues/1255
author: st0f
assignees: []
labels:
- bug
created_at: '2019-10-30T06:46:13+00:00'
updated_at: '2019-10-30T08:55:40+00:00'
type: issue
status: closed
closed_at: '2019-10-30T08:55:09+00:00'
---

# Original Description
I'm getting the following errors whilst building the new version 4.4.0-beta from source.

These are the steps I'm following:

Navigate to the xmrig-4.4.0-beta
mkdir build
cd build
cmake .. -G "Visual Studio 16 2019" -DXMRIG_DEPS="D:\Mining\Mining Software\SourceFiles\XMRIG-DEPS\xmrig-deps\msvc2019\x64"
cmake --build . --config Release

I then get the following errors:

D:\Mining\Mining Software\SourceFiles\XMRIG-CPU\xmrig-4.4.0-beta\src\base\net\stratum\Pool.cpp(249,37): **error C2039: 'to_string': is not a member of 'std' [D:\Mining\Mining Software\SourceFiles\XMRIG-CPU\xmrig-4.4.0-beta\build\xmrig.vcxproj]**

D:\Mining\Mining Software\SourceFiles\XMRIG-CPU\xmrig-4.4.0-beta\src\base\net\stratum\Pool.cpp(249,46): **error C3861: 'to_string': identifier not found [D:\Mining\Mining Software\SourceFiles\XMRIG-CPU\xmrig-4.4.0-beta\build\xmrig.vcxproj]**

D:\Mining\Mining Software\SourceFiles\XMRIG-CPU\xmrig-4.4.0-beta\src\base\net\stratum\Pool.cpp(259,63): **error C2039: 'to_string': is not a member of 'std' [D:\Mining\Mining Software\SourceFiles\XMRIG-CPU\xmrig-4.4.0-beta\build\xmrig.vcxproj]**

D:\Mining\Mining Software\SourceFiles\XMRIG-CPU\xmrig-4.4.0-beta\src\base\net\stratum\Pool.cpp(259,72): **error C3861: 'to_string': identifier not found [D:\Mining\Mining Software\SourceFiles\XMRIG-CPU\xmrig-4.4.0-beta\build\xmrig.vcxproj]**

Im running:

Windows 10
Visual Studio Community 2019
CMake 3.16.0

I can successfully compile version 4.3.1-beta from source using these steps with no issues. Are there further steps to follow for version 4.4?

# Discussion History
## xmrig | 2019-10-30T08:19:23+00:00
Already fixed in evo branch https://github.com/xmrig/xmrig/pull/1253
Thank you.

## st0f | 2019-10-30T08:55:09+00:00
Yep, adding `#include <string>` to Pool.cpp has resolved this issue. 

Thank you! :)

# Action History
- Created by: st0f | 2019-10-30T06:46:13+00:00
- Closed at: 2019-10-30T08:55:09+00:00
