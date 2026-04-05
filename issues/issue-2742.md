---
title: Build failure with Clang-CL and MSVC 2022
source_url: https://github.com/xmrig/xmrig/issues/2742
author: IdrisKalp
assignees: []
labels: []
created_at: '2021-11-28T23:12:32+00:00'
updated_at: '2025-06-12T06:40:01+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Hi. Trying to build 6.16.0 with Clang and MSVC 2022. I'm getting this error during build: 

`E:\xmrig-6.16.0\src\base\io\log\Log.cpp(101,22): error : expected unqualified-id [e:\xmrig-6.16.0\bld\xmrig.vcxproj]`

Is it bug?

# Discussion History
## theAeon | 2021-12-01T07:34:30+00:00
any reason you're using clang? it built fine with msbuild.

## IdrisKalp | 2022-01-07T15:05:35+00:00
> any reason you're using clang? it built fine with msbuild.

I want to try clang's LTO feature and see if there is performance increase

## ahorek | 2022-01-07T18:56:36+00:00
> I want to try clang's LTO feature and see if there is performance increase

on gcc 11 the LTO improvement is within a margin of error, so I don't expect clang will do better.


## MrMarvel | 2025-06-12T06:36:46+00:00
Just got same error
`xmrig\src\base\io\log\Log.cpp(101,22): error : expected unqualified-id`
via
```powershell
cmake .. -T ClangCL -A x64 -DHWLOC_INCLUDE_DIR=D:\TEMP\xmrig\src\3rdparty\hwloc\include -DHWLOC_LIBRARY=D:\TEMP\xmrig\src\3rdparty\hwloc\src -DXMRIG_DEPS="D:\TEMP\xmrig\xmrig-deps\msvc2019\x64"
cmake --build . --config Release
```

## MrMarvel | 2025-06-12T06:37:24+00:00
I think optimization like O3 will make difference.

## SChernykh | 2025-06-12T06:40:01+00:00
MSVC and ClangCL combination is something we never tested and never supported, so don't expect it to work.

# Action History
- Created by: IdrisKalp | 2021-11-28T23:12:32+00:00
