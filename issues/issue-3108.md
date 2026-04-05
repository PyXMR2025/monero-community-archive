---
title: 'Build Failed on assembling cryptonight on Windows '
source_url: https://github.com/xmrig/xmrig/issues/3108
author: jamesorgan
assignees: []
labels: []
created_at: '2022-08-16T19:55:45+00:00'
updated_at: '2022-08-17T16:19:47+00:00'
type: issue
status: closed
closed_at: '2022-08-17T16:19:47+00:00'
---

# Original Description
**Describe the bug**
A clear and concise description of what the bug is.

**To Reproduce**
Follow the https://xmrig.com/docs/miner/build/windows using Visual Studio 2019
cmake .. -G "Visual Studio 16 2019" -A x64 -DXMRIG_DEPS=c:\xmrig-deps\msvc2019\x64
cmake --build . --config Release

**Required data**
 - Cmake output
 Microsoft (R) Build Engine version 16.11.2+f32259642 for .NET Framework
Copyright (C) Microsoft Corporation. All rights reserved.

Build started 16/08/2022 20:15:05.
Project "C:\xmrig\build\ALL_BUILD.vcxproj" on node 1 (default targets).
Project "C:\xmrig\build\ALL_BUILD.vcxproj" (1) is building "C:\xmrig\build\ZERO_CHECK.proj" (2) on node 1 (default targets).
Build:
Skipping target "Build" because all output files are up-to-date with respect to the input files.
Done Building Project "C:\xmrig\build\ZERO_CHECK.proj" (default targets).
Project "C:\xmrig\build\ALL_BUILD.vcxproj" (1) is building "C:\xmrig\build\src\3rdparty\argon2\argon2.vcxproj" (3) on node 1 (default targets).
Project "C:\xmrig\build\src\3rdparty\argon2\argon2.vcxproj" (3) is building "C:\xmrig\build\src\3rdparty\argon2\argon2-avx2.vcxproj" (4) on node 1 (default targets).
InitializeBuildStatus:
  Creating "argon2-avx2.dir\Release\argon2-avx2.tlog\unsuccessfulbuild" because "AlwaysCreate" was specified.
CustomBuild:
  All outputs are up-to-date.
ClCompile:
  All outputs are up-to-date.
Lib:
  All outputs are up-to-date.
  argon2-avx2.vcxproj -> C:\xmrig\build\src\3rdparty\argon2\Release\argon2-avx2.lib
FinalizeBuildStatus:
  Deleting file "argon2-avx2.dir\Release\argon2-avx2.tlog\unsuccessfulbuild".
  Touching "argon2-avx2.dir\Release\argon2-avx2.tlog\argon2-avx2.lastbuildstate".
Done Building Project "C:\xmrig\build\src\3rdparty\argon2\argon2-avx2.vcxproj" (default targets).
Project "C:\xmrig\build\src\3rdparty\argon2\argon2.vcxproj" (3) is building "C:\xmrig\build\src\3rdparty\argon2\argon2-avx512f.vcxproj" (5) on node 1 (default targets).
InitializeBuildStatus:
  Creating "argon2-avx512f.dir\Release\argon2-avx512f.tlog\unsuccessfulbuild" because "AlwaysCreate" was specified.
CustomBuild:
  All outputs are up-to-date.
ClCompile:
  All outputs are up-to-date.
Lib:
  All outputs are up-to-date.
  argon2-avx512f.vcxproj -> C:\xmrig\build\src\3rdparty\argon2\Release\argon2-avx512f.lib
FinalizeBuildStatus:
  Deleting file "argon2-avx512f.dir\Release\argon2-avx512f.tlog\unsuccessfulbuild".
  Touching "argon2-avx512f.dir\Release\argon2-avx512f.tlog\argon2-avx512f.lastbuildstate".
Done Building Project "C:\xmrig\build\src\3rdparty\argon2\argon2-avx512f.vcxproj" (default targets).
Project "C:\xmrig\build\src\3rdparty\argon2\argon2.vcxproj" (3) is building "C:\xmrig\build\src\3rdparty\argon2\argon2-sse2.vcxproj" (6) on node 1 (default targets).
InitializeBuildStatus:
  Creating "argon2-sse2.dir\Release\argon2-sse2.tlog\unsuccessfulbuild" because "AlwaysCreate" was specified.
CustomBuild:
  All outputs are up-to-date.
ClCompile:
  All outputs are up-to-date.
Lib:
  All outputs are up-to-date.
  argon2-sse2.vcxproj -> C:\xmrig\build\src\3rdparty\argon2\Release\argon2-sse2.lib
FinalizeBuildStatus:
  Deleting file "argon2-sse2.dir\Release\argon2-sse2.tlog\unsuccessfulbuild".
  Touching "argon2-sse2.dir\Release\argon2-sse2.tlog\argon2-sse2.lastbuildstate".
Done Building Project "C:\xmrig\build\src\3rdparty\argon2\argon2-sse2.vcxproj" (default targets).
Project "C:\xmrig\build\src\3rdparty\argon2\argon2.vcxproj" (3) is building "C:\xmrig\build\src\3rdparty\argon2\argon2-ssse3.vcxproj" (7) on node 1 (default targets).
InitializeBuildStatus:
  Creating "argon2-ssse3.dir\Release\argon2-ssse3.tlog\unsuccessfulbuild" because "AlwaysCreate" was specified.
CustomBuild:
  All outputs are up-to-date.
ClCompile:
  All outputs are up-to-date.
Lib:
  All outputs are up-to-date.
  argon2-ssse3.vcxproj -> C:\xmrig\build\src\3rdparty\argon2\Release\argon2-ssse3.lib
FinalizeBuildStatus:
  Deleting file "argon2-ssse3.dir\Release\argon2-ssse3.tlog\unsuccessfulbuild".
  Touching "argon2-ssse3.dir\Release\argon2-ssse3.tlog\argon2-ssse3.lastbuildstate".
Done Building Project "C:\xmrig\build\src\3rdparty\argon2\argon2-ssse3.vcxproj" (default targets).
Project "C:\xmrig\build\src\3rdparty\argon2\argon2.vcxproj" (3) is building "C:\xmrig\build\src\3rdparty\argon2\argon2-xop.vcxproj" (8) on node 1 (default targets).
InitializeBuildStatus:
  Creating "argon2-xop.dir\Release\argon2-xop.tlog\unsuccessfulbuild" because "AlwaysCreate" was specified.
CustomBuild:
  All outputs are up-to-date.
ClCompile:
  All outputs are up-to-date.
Lib:
  All outputs are up-to-date.
  argon2-xop.vcxproj -> C:\xmrig\build\src\3rdparty\argon2\Release\argon2-xop.lib
FinalizeBuildStatus:
  Deleting file "argon2-xop.dir\Release\argon2-xop.tlog\unsuccessfulbuild".
  Touching "argon2-xop.dir\Release\argon2-xop.tlog\argon2-xop.lastbuildstate".
Done Building Project "C:\xmrig\build\src\3rdparty\argon2\argon2-xop.vcxproj" (default targets).
InitializeBuildStatus:
  Creating "argon2.dir\Release\argon2.tlog\unsuccessfulbuild" because "AlwaysCreate" was specified.
CustomBuild:
  All outputs are up-to-date.
ClCompile:
  All outputs are up-to-date.
Lib:
  All outputs are up-to-date.
  argon2.vcxproj -> C:\xmrig\build\src\3rdparty\argon2\Release\argon2.lib
FinalizeBuildStatus:
  Deleting file "argon2.dir\Release\argon2.tlog\unsuccessfulbuild".
  Touching "argon2.dir\Release\argon2.tlog\argon2.lastbuildstate".
Done Building Project "C:\xmrig\build\src\3rdparty\argon2\argon2.vcxproj" (default targets).
Project "C:\xmrig\build\ALL_BUILD.vcxproj" (1) is building "C:\xmrig\build\src\crypto\ghostrider\ghostrider.vcxproj" (9) on node 1 (default targets).
InitializeBuildStatus:
  Creating "ghostrider.dir\Release\ghostrider.tlog\unsuccessfulbuild" because "AlwaysCreate" was specified.
CustomBuild:
  All outputs are up-to-date.
ClCompile:
  All outputs are up-to-date.
  All outputs are up-to-date.
Lib:
  All outputs are up-to-date.
  ghostrider.vcxproj -> C:\xmrig\build\src\crypto\ghostrider\Release\ghostrider.lib
FinalizeBuildStatus:
  Deleting file "ghostrider.dir\Release\ghostrider.tlog\unsuccessfulbuild".
  Touching "ghostrider.dir\Release\ghostrider.tlog\ghostrider.lastbuildstate".
Done Building Project "C:\xmrig\build\src\crypto\ghostrider\ghostrider.vcxproj" (default targets).
Project "C:\xmrig\build\ALL_BUILD.vcxproj" (1) is building "C:\xmrig\build\src\3rdparty\hwloc\hwloc.vcxproj" (10) on node 1 (default targets).
InitializeBuildStatus:
  Creating "hwloc.dir\Release\hwloc.tlog\unsuccessfulbuild" because "AlwaysCreate" was specified.
CustomBuild:
  All outputs are up-to-date.
ClCompile:
  All outputs are up-to-date.
Lib:
  All outputs are up-to-date.
  hwloc.vcxproj -> C:\xmrig\build\src\3rdparty\hwloc\Release\hwloc.lib
FinalizeBuildStatus:
  Deleting file "hwloc.dir\Release\hwloc.tlog\unsuccessfulbuild".
  Touching "hwloc.dir\Release\hwloc.tlog\hwloc.lastbuildstate".
Done Building Project "C:\xmrig\build\src\3rdparty\hwloc\hwloc.vcxproj" (default targets).
Project "C:\xmrig\build\ALL_BUILD.vcxproj" (1) is building "C:\xmrig\build\xmrig.vcxproj" (11) on node 1 (default targets).
Project "C:\xmrig\build\xmrig.vcxproj" (11) is building "C:\xmrig\build\xmrig-asm.vcxproj" (12) on node 1 (default targets).
InitializeBuildStatus:
  Touching "xmrig-asm.dir\Release\xmrig-asm.tlog\unsuccessfulbuild".
CustomBuild:
  All outputs are up-to-date.
_MASM:
Skipping target "_MASM" because all output files are up-to-date with respect to the input files.
_MASM:
  Assembling C:\xmrig\src\crypto\cn\asm\CryptonightR_template.asm...
  cmd.exe /C "C:\Users\------\AppData\Local\Temp\tmp3caa03a81b1047b3bdfe96fc2ac7a42f.cmd"
  ml64.exe /c /nologo /Zi /Fo"xmrig-asm.dir\Release\CryptonightR_template.obj" /D"WIN32" /D"_WINDOWS" /D"NDEBUG" /D"XMRIG_64_BIT" /D"RAPIDJSON_SSE2" /D"XMRIG_FEATURE_SSE4_1" /D"XMRIG_OS_WIN" /D"XMRIG_FEATURE_HTTP" /D"XMRIG_FEATURE_API" /D"XMRIG_FEATURE_ENV" /D"XMRIG_FEATURE_BENCHMARK" /D"XMRIG_FEATURE_HWLOC" /D"XMRIG_VAES" /D"XMRIG_MINER_PROJECT" /D"XMRIG_JSON_SINGLE_LINE_ARRAY" /D"__STDC_FORMAT_MACROS" /D"UNICODE" /D"_FILE_OFFSET_BITS=64" /D"_CRT_SECURE_NO_WARNINGS" /D"_CRT_NONSTDC_NO_WARNINGS" /D"NOMINMAX" /D"HAVE_ROTR" /D"XMRIG_ALGO_RANDOMX" /D"XMRIG_FEATURE_MSR" /D"XMRIG_FIX_RYZEN" /D"XMRIG_ALGO_ARGON2" /D"XMRIG_ALGO_GHOSTRIDER" /D"XMRIG_FEATURE_TLS" /D"XMRIG_FEATURE_ASM" /D"XMRIG_ALGO_CN_LITE" /D"XMRIG_ALGO_CN_HEAVY" /D"XMRIG_ALGO_CN_PICO" /D"XMRIG_ALGO_CN_FEMTO" /D"XMRIG_FEATURE_DMI" /D"CMAKE_INTDIR="Release"" /I "C:\xmrig\src\3rdparty\hwloc\include" /I "C:\xmrig-deps\msvc2019\x64\include" /I "C:\xmrig\src" /I "C:\xmrig\src\3rdparty" /W3 /errorReport:prompt  /TaC:\xmrig\src\crypto\cn\asm\CryptonightR_template.asm
  The system cannot find the path specified.
C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\MSBuild\Microsoft\VC\v160\BuildCustomizations\masm.targets(70,5): error MSB3721: The command "ml64.exe /c /nologo /Zi /Fo"xmrig-asm.dir\Release\CryptonightR_template.obj" /D"WIN32" /D"_WINDOWS" /D"NDEBUG" /D"XMRIG_64_BIT" /D"RAPIDJSON_SSE2" /D"XMRIG_FEATURE_SSE4_1" /D"XMRIG_OS_WIN" /D"XMRIG_FEATURE_HTTP" /D"XMRIG_FEATURE_API" /D"XMRIG_FEATURE_ENV" /D"XMRIG_FEATURE_BENCHMARK" /D"XMRIG_FEATURE_HWLOC" /D"XMRIG_VAES" /D"XMRIG_MINER_PROJECT" /D"XMRIG_JSON_SINGLE_LINE_ARRAY" /D"__STDC_FORMAT_MACROS" /D"UNICODE" /D"_FILE_OFFSET_BITS=64" /D"_CRT_SECURE_NO_WARNINGS" /D"_CRT_NONSTDC_NO_WARNINGS" /D"NOMINMAX" /D"HAVE_ROTR" /D"XMRIG_ALGO_RANDOMX" /D"XMRIG_FEATURE_MSR" /D"XMRIG_FIX_RYZEN" /D"XMRIG_ALGO_ARGON2" /D"XMRIG_ALGO_GHOSTRIDER" /D"XMRIG_FEATURE_TLS" /D"XMRIG_FEATURE_ASM" /D"XMRIG_ALGO_CN_LITE" /D"XMRIG_ALGO_CN_HEAVY" /D"XMRIG_ALGO_CN_PICO" /D"XMRIG_ALGO_CN_FEMTO" /D"XMRIG_FEATURE_DMI" /D"CMAKE_INTDIR="Release"" /I "C:\xmrig\src\3rdparty\hwloc\include" /I "C:\xmrig-deps\msvc2019\x64\include" /I "C:\xmrig\src" /I "C:\xmrig\src\3rdparty" /W3 /errorReport:prompt  /TaC:\xmrig\src\crypto\cn\asm\CryptonightR_template.asm" exited with code 1. [C:\xmrig\build\xmrig-asm.vcxproj]
Done Building Project "C:\xmrig\build\xmrig-asm.vcxproj" (default targets) -- FAILED.
Done Building Project "C:\xmrig\build\xmrig.vcxproj" (default targets) -- FAILED.
Done Building Project "C:\xmrig\build\ALL_BUILD.vcxproj" (default targets) -- FAILED.

Build FAILED.

"C:\xmrig\build\ALL_BUILD.vcxproj" (default target) (1) ->
"C:\xmrig\build\xmrig.vcxproj" (default target) (11) ->
"C:\xmrig\build\xmrig-asm.vcxproj" (default target) (12) ->
(_MASM target) ->
  C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\MSBuild\Microsoft\VC\v160\BuildCustomizations\masm.targets(70,5): error MSB3721: The command "ml64.exe /c /nologo /Zi /Fo"xmrig-asm.dir\Release\CryptonightR_template.obj" /D"WIN32" /D"_WINDOWS" /D"NDEBUG" /D"XMRIG_64_BIT" /D"RAPIDJSON_SSE2" /D"XMRIG_FEATURE_SSE4_1" /D"XMRIG_OS_WIN" /D"XMRIG_FEATURE_HTTP" /D"XMRIG_FEATURE_API" /D"XMRIG_FEATURE_ENV" /D"XMRIG_FEATURE_BENCHMARK" /D"XMRIG_FEATURE_HWLOC" /D"XMRIG_VAES" /D"XMRIG_MINER_PROJECT" /D"XMRIG_JSON_SINGLE_LINE_ARRAY" /D"__STDC_FORMAT_MACROS" /D"UNICODE" /D"_FILE_OFFSET_BITS=64" /D"_CRT_SECURE_NO_WARNINGS" /D"_CRT_NONSTDC_NO_WARNINGS" /D"NOMINMAX" /D"HAVE_ROTR" /D"XMRIG_ALGO_RANDOMX" /D"XMRIG_FEATURE_MSR" /D"XMRIG_FIX_RYZEN" /D"XMRIG_ALGO_ARGON2" /D"XMRIG_ALGO_GHOSTRIDER" /D"XMRIG_FEATURE_TLS" /D"XMRIG_FEATURE_ASM" /D"XMRIG_ALGO_CN_LITE" /D"XMRIG_ALGO_CN_HEAVY" /D"XMRIG_ALGO_CN_PICO" /D"XMRIG_ALGO_CN_FEMTO" /D"XMRIG_FEATURE_DMI" /D"CMAKE_INTDIR="Release"" /I "C:\xmrig\src\3rdparty\hwloc\include" /I "C:\xmrig-deps\msvc2019\x64\include" /I "C:\xmrig\src" /I "C:\xmrig\src\3rdparty" /W3 /errorReport:prompt  /TaC:\xmrig\src\crypto\cn\asm\CryptonightR_template.asm" exited with code 1. [C:\xmrig\build\xmrig-asm.vcxproj]

    0 Warning(s)
    1 Error(s)

Time Elapsed 00:00:01.51

**Additional context**
Add any other context about the problem here.


# Discussion History
## SChernykh | 2022-08-16T19:57:50+00:00
> The system cannot find the path specified.

It looks like you don't have `ml64.exe`. Fix your Visual Studio installation.

## jamesorgan | 2022-08-16T21:05:00+00:00
I had to use the x64 Native Tools Command Prompt. I was using git bash prompt.

## jamesorgan | 2022-08-16T21:05:52+00:00
Do you know if you can build from inside Visual Studio?

## SChernykh | 2022-08-17T05:19:41+00:00
```
cmake --build . --config Release
```
This line is wrong. You have to build the generated .sln file - either from Visual Studio directly, or using MSBuild from Visual Studio command line.

# Action History
- Created by: jamesorgan | 2022-08-16T19:55:45+00:00
- Closed at: 2022-08-17T16:19:47+00:00
