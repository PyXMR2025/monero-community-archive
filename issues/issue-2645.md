---
title: '[MSVC][/std:c++latest] Build error error C2445: result type of conditional
  expression is ambiguous'
source_url: https://github.com/xmrig/xmrig/issues/2645
author: QuellaZhang
assignees: []
labels: []
created_at: '2021-10-25T07:35:33+00:00'
updated_at: '2021-10-26T10:22:37+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Hello,

We build xmrig latest source code f7aa5e7 on MSVC with /std:c++latest, found the following error, can you help look? Looks like error C2440 are third-party lib errors, but error C2445 comes from xmrig.

**Repro steps:**

1. open VS2019 x64 tools command
2. git clone --recursive https://github.com/xmrig/xmrig F:\gitP\xmrig\xmrig
3. set _CL_= /std:c++latest
4. mkdir F:\gitP\xmrig\xmrig\build_amd64
5. cd F:\gitP\xmrig\xmrig\build_amd64
6. cmake -G "Visual Studio 16 2019" -A x64 -DCMAKE_SYSTEM_VERSION=10.0.18362.0 -DXMRIG_DEPS="F:\gitP\xmrig\xmrig-deps-4.1\msvc2019\x64" -DWITH_LIBCPUID=OFF ..
7. msbuild /m /p:Platform=x64 /p:Configuration=Release xmrig.sln /t:Rebuild

**Build log:** [Xmrig_build.log](https://github.com/xmrig/xmrig/files/7408109/Xmrig_build.log)

**Error info:**
F:\gitP\xmrig\xmrig\src\3rdparty\getopt/getopt.h(514,16): error C2440: '=': cannot convert from 'const char [1]' to 'char *'
F:\gitP\xmrig\xmrig\src\3rdparty\getopt/getopt.h(546,16): error C2440: '=': cannot convert from 'const char [1]' to 'char *'
F:\gitP\xmrig\xmrig\src\3rdparty\getopt/getopt.h(573,16): error C2440: '=': cannot convert from 'const char [1]' to 'char *'
F:\gitP\xmrig\xmrig\src\3rdparty\getopt/getopt.h(582,15): error C2440: '=': cannot convert from 'const char [1]' to 'char *'
F:\gitP\xmrig\xmrig\src\3rdparty\getopt/getopt.h(594,17): error C2440: '=': cannot convert from 'const char [1]' to 'char *'
F:\gitP\xmrig\xmrig\src\3rdparty\getopt/getopt.h(602,15): error C2440: '=': cannot convert from 'const char [1]' to 'char *'
F:\gitP\xmrig\xmrig\src\base\kernel\Process.cpp(155,71): error C2445: result type of conditional expression is ambiguous: types 'const char [1]' and 'xmrig::String' can be converted to multiple common types

# Discussion History
## SChernykh | 2021-10-25T08:22:26+00:00
https://github.com/xmrig/xmrig/pull/2646 should fix this.

## QuellaZhang | 2021-10-26T10:22:37+00:00
@SChernykh Thanks for the quick fix!

# Action History
- Created by: QuellaZhang | 2021-10-25T07:35:33+00:00
