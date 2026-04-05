---
title: Xmrig failed to build with many errors with MSVC on windows arm64
source_url: https://github.com/xmrig/xmrig/issues/2943
author: spacelg
assignees: []
labels: []
created_at: '2022-02-22T08:53:28+00:00'
updated_at: '2022-02-22T08:53:28+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Hi All,

**Environment:**
VS 2019 + Windows Server 2019

Xmrig failed to build with many errors with MSVC on windows arm64. It can be reproduced on latest version 4f5f9bd on master branch.  Could you please help look at this issue?  Does Xmrig support windows arm64? 

**Repro steps:**
1. vcpkg.exe install --recurse libuv openssl hwloc --triplet arm64-windows --clean-after-build
2. git clone https://github.com/xmrig/xmrig F:\gitP\xmrig\xmrig
3. cd F:\gitP\xmrig\xmrig && mkdir build_arm64
4. "C:\Program Files (x86)\Microsoft Visual Studio\2019\Enterprise\Common7\Tools\VsDevCmd.bat" -host_arch=amd64 -arch=arm64
5. cmake -G "Visual Studio 16 2019" -DCMAKE_SYSTEM_NAME=Windows -DCMAKE_SYSTEM_PROCESSOR=aarch64 -A arm64 -DCMAKE_SYSTEM_VERSION=10.0.18362.0 -DXMRIG_DEPS="F:\gitP\microsoft\vcpkg\installed\arm64-windows" -DWITH_LIBCPUID=OFF ..
6. msbuild /m /p:Platform=arm64 /p:Configuration=Release xmrig.sln /t:Rebuild

ARM64_build_log: 
[build_arm64.zip](https://github.com/xmrig/xmrig/files/8115045/build_arm64.zip)

**Error info:**
12>F:\gitP\xmrig\xmrig\src\3rdparty\argon2\arch\x86_64\lib\argon2-sse2.c(20,16): error C2061: syntax error: identifier 'f' [F:\gitP\xmrig\xmrig\build_arm64\src\3rdparty\argon2\argon2-sse2.vcxproj]
    12>F:\gitP\xmrig\xmrig\src\3rdparty\argon2\arch\x86_64\lib\argon2-sse2.c(20,16): error C2059: syntax error: ';' [F:\gitP\xmrig\xmrig\build_arm64\src\3rdparty\argon2\argon2-sse2.vcxproj]
    12>F:\gitP\xmrig\xmrig\src\3rdparty\argon2\arch\x86_64\lib\argon2-sse2.c(20,26): error C2146: syntax error: missing ')' before identifier 'x' [F:\gitP\xmrig\xmrig\build_arm64\src\3rdparty\argon2\argon2-sse2.vcxproj]
    12>F:\gitP\xmrig\xmrig\src\3rdparty\argon2\arch\x86_64\lib\argon2-sse2.c(20,26): error C2061: syntax error: identifier 'x' [F:\gitP\xmrig\xmrig\build_arm64\src\3rdparty\argon2\argon2-sse2.vcxproj]
    12>F:\gitP\xmrig\xmrig\src\3rdparty\argon2\arch\x86_64\lib\argon2-sse2.c(20,27): error C2059: syntax error: ',' [F:\gitP\xmrig\xmrig\build_arm64\src\3rdparty\argon2\argon2-sse2.vcxproj]
    12>F:\gitP\xmrig\xmrig\src\3rdparty\argon2\arch\x86_64\lib\argon2-sse2.c(20,38): error C2059: syntax error: ')' [F:\gitP\xmrig\xmrig\build_arm64\src\3rdparty\argon2\argon2-sse2.vcxproj]
    12>F:\gitP\xmrig\xmrig\src\3rdparty\argon2\arch\x86_64\lib\argon2-template-128.h(11,32): error C2143: syntax error: missing ')' before '*' [F:\gitP\xmrig\xmrig\build_arm64\src\3rdparty\argon2\argon2-sse2.vcxproj]
    12>F:\gitP\xmrig\xmrig\src\3rdparty\argon2\arch\x86_64\lib\argon2-template-128.h(11,32): error C2143: syntax error: missing '{' before '*' [F:\gitP\xmrig\xmrig\build_arm64\src\3rdparty\argon2\argon2-sse2.vcxproj]
    12>F:\gitP\xmrig\xmrig\src\3rdparty\argon2\arch\x86_64\lib\argon2-template-128.h(11,42): error C2371: 'block': redefinition; different basic types [F:\gitP\xmrig\xmrig\build_arm64\src\3rdparty\argon2\argon2-sse2.vcxproj]
       F:\gitP\xmrig\xmrig\src\3rdparty\argon2\lib\core.h(54): message : see declaration of 'block' [F:\gitP\xmrig\xmrig\build_arm64\src\3rdparty\argon2\argon2-sse2.vcxproj]
    12>F:\gitP\xmrig\xmrig\src\3rdparty\argon2\arch\x86_64\lib\argon2-template-128.h(11,48): warning C4228: nonstandard extension used: qualifiers after comma in declarator list are ignored [F:\gitP\xmrig\xmrig\build_arm64\src\3rdparty\argon2\argon2-sse2.vcxproj]
    12>F:\gitP\xmrig\xmrig\src\3rdparty\argon2\arch\x86_64\lib\argon2-template-128.h(11,48): error C2143: syntax error: missing ';' before '*' [F:\gitP\xmrig\xmrig\build_arm64\src\3rdparty\argon2\argon2-sse2.vcxproj]
    12>F:\gitP\xmrig\xmrig\src\3rdparty\argon2\arch\x86_64\lib\argon2-template-128.h(11,60): error C2371: 'block': redefinition; different basic types [F:\gitP\xmrig\xmrig\build_arm64\src\3rdparty\argon2\argon2-sse2.vcxproj]
       F:\gitP\xmrig\xmrig\src\3rdparty\argon2\lib\core.h(54): message : see declaration of 'block' [F:\gitP\xmrig\xmrig\build_arm64\src\3rdparty\argon2\argon2-sse2.vcxproj]
    12>F:\gitP\xmrig\xmrig\src\3rdparty\argon2\arch\x86_64\lib\argon2-template-128.h(11,66): error C2143: syntax error: missing ';' before '*' [F:\gitP\xmrig\xmrig\build_arm64\src\3rdparty\argon2\argon2-sse2.vcxproj]
    12>F:\gitP\xmrig\xmrig\src\3rdparty\argon2\arch\x86_64\lib\argon2-template-128.h(12,28): error C2059: syntax error: 'type' [F:\gitP\xmrig\xmrig\build_arm64\src\3rdparty\argon2\argon2-sse2.vcxproj]
    12>F:\gitP\xmrig\xmrig\src\3rdparty\argon2\arch\x86_64\lib\argon2-template-128.h(12,36): error C2059: syntax error: ')' [F:\gitP\xmrig\xmrig\build_arm64\src\3rdparty\argon2\argon2-sse2.vcxproj]
    12>F:\gitP\xmrig\xmrig\src\3rdparty\argon2\arch\x86_64\lib\argon2-template-128.h(52,13): error C2065: '__m128i': undeclared identifier [F:\gitP\xmrig\xmrig\build_arm64\src\3rdparty\argon2\argon2-sse2.vcxproj]
    12>F:\gitP\xmrig\xmrig\src\3rdparty\argon2\arch\x86_64\lib\argon2-template-128.h(52,13): error C2146: syntax error: missing ';' before identifier 'zero_block' [F:\gitP\xmrig\xmrig\build_arm64\src\3rdparty\argon2\argon2-sse2.vcxproj]
    12>F:\gitP\xmrig\xmrig\src\3rdparty\argon2\arch\x86_64\lib\argon2-template-128.h(52,23): error C2065: 'zero_block': undeclared identifier [F:\gitP\xmrig\xmrig\build_arm64\src\3rdparty\argon2\argon2-sse2.vcxproj]
    12>F:\gitP\xmrig\xmrig\src\3rdparty\argon2\arch\x86_64\lib\argon2-template-128.h(52,46): error C2109: subscript requires array or pointer type [F:\gitP\xmrig\xmrig\build_arm64\src\3rdparty\argon2\argon2-sse2.vcxproj]
    12>F:\gitP\xmrig\xmrig\src\3rdparty\argon2\arch\x86_64\lib\argon2-template-128.h(53,13): error C2065: '__m128i': undeclared identifier [F:\gitP\xmrig\xmrig\build_arm64\src\3rdparty\argon2\argon2-sse2.vcxproj]
    12>F:\gitP\xmrig\xmrig\src\3rdparty\argon2\arch\x86_64\lib\argon2-template-128.h(53,13): error C2146: syntax error: missing ';' before identifier 'zero2_block' [F:\gitP\xmrig\xmrig\build_arm64\src\3rdparty\argon2\argon2-sse2.vcxproj]
    12>F:\gitP\xmrig\xmrig\src\3rdparty\argon2\arch\x86_64\lib\argon2-template-128.h(53,24): error C2065: 'zero2_block': undeclared identifier [F:\gitP\xmrig\xmrig\build_arm64\src\3rdparty\argon2\argon2-sse2.vcxproj]
    12>F:\gitP\xmrig\xmrig\src\3rdparty\argon2\arch\x86_64\lib\argon2-template-128.h(53,47): error C2109: subscript requires array or pointer type [F:\gitP\xmrig\xmrig\build_arm64\src\3rdparty\argon2\argon2-sse2.vcxproj]
    12>F:\gitP\xmrig\xmrig\src\3rdparty\argon2\arch\x86_64\lib\argon2-template-128.h(55,22): error C2065: 'zero_block': undeclared identifier [F:\gitP\xmrig\xmrig\build_arm64\src\3rdparty\argon2\argon2-sse2.vcxproj]
    12>F:\gitP\xmrig\xmrig\src\3rdparty\argon2\arch\x86_64\lib\argon2-template-128.h(55,12): warning C4022: 'memset': pointer mismatch for actual parameter 1 [F:\gitP\xmrig\xmrig\build_arm64\src\3rdparty\argon2\argon2-sse2.vcxproj]
    12>F:\gitP\xmrig\xmrig\src\3rdparty\argon2\arch\x86_64\lib\argon2-template-128.h(55,44): error C2065: 'zero_block': undeclared identifier [F:\gitP\xmrig\xmrig\build_arm64\src\3rdparty\argon2\argon2-sse2.vcxproj]
    12>F:\gitP\xmrig\xmrig\src\3rdparty\argon2\arch\x86_64\lib\argon2-template-128.h(56,23): error C2065: 'zero2_block': undeclared identifier [F:\gitP\xmrig\xmrig\build_arm64\src\3rdparty\argon2\argon2-sse2.vcxproj]
    12>F:\gitP\xmrig\xmrig\src\3rdparty\argon2\arch\x86_64\lib\argon2-template-128.h(56,12): warning C4022: 'memset': pointer mismatch for actual parameter 1 [F:\gitP\xmrig\xmrig\build_arm64\src\3rdparty\argon2\argon2-sse2.vcxproj]
    12>F:\gitP\xmrig\xmrig\src\3rdparty\argon2\arch\x86_64\lib\argon2-template-128.h(56,46): error C2065: 'zero2_block': undeclared identifier [F:\gitP\xmrig\xmrig\build_arm64\src\3rdparty\argon2\argon2-sse2.vcxproj]
    12>F:\gitP\xmrig\xmrig\src\3rdparty\argon2\arch\x86_64\lib\argon2-template-128.h(62,15): warning C4013: 'fill_block' undefined; assuming extern returning int [F:\gitP\xmrig\xmrig\build_arm64\src\3rdparty\argon2\argon2-sse2.vcxproj]
    12>F:\gitP\xmrig\xmrig\src\3rdparty\argon2\arch\x86_64\lib\argon2-template-128.h(62,26): error C2065: 'zero_block': undeclared identifier [F:\gitP\xmrig\xmrig\build_arm64\src\3rdparty\argon2\argon2-sse2.vcxproj]
    12>F:\gitP\xmrig\xmrig\src\3rdparty\argon2\arch\x86_64\lib\argon2-template-128.h(65,27): error C2065: 'zero2_block': undeclared identifier [F:\gitP\xmrig\xmrig\build_arm64\src\3rdparty\argon2\argon2-sse2.vcxproj]
    12>F:\gitP\xmrig\xmrig\src\3rdparty\argon2\arch\x86_64\lib\argon2-template-128.h(76,13): error C2065: '__m128i': undeclared identifier [F:\gitP\xmrig\xmrig\build_arm64\src\3rdparty\argon2\argon2-sse2.vcxproj]
    12>F:\gitP\xmrig\xmrig\src\3rdparty\argon2\arch\x86_64\lib\argon2-template-128.h(76,13): error C2146: syntax error: missing ';' before identifier 'state' [F:\gitP\xmrig\xmrig\build_arm64\src\3rdparty\argon2\argon2-sse2.vcxproj]
    12>F:\gitP\xmrig\xmrig\src\3rdparty\argon2\arch\x86_64\lib\argon2-template-128.h(76,18): error C2065: 'state': undeclared identifier [F:\gitP\xmrig\xmrig\build_arm64\src\3rdparty\argon2\argon2-sse2.vcxproj]
    12>F:\gitP\xmrig\xmrig\src\3rdparty\argon2\arch\x86_64\lib\argon2-template-128.h(76,41): error C2109: subscript requires array or pointer type [F:\gitP\xmrig\xmrig\build_arm64\src\3rdparty\argon2\argon2-sse2.vcxproj]
    12>F:\gitP\xmrig\xmrig\src\3rdparty\argon2\arch\x86_64\lib\argon2-template-128.h(121,17): error C2065: 'state': undeclared identifier [F:\gitP\xmrig\xmrig\build_arm64\src\3rdparty\argon2\argon2-sse2.vcxproj]
    12>F:\gitP\xmrig\xmrig\src\3rdparty\argon2\arch\x86_64\lib\argon2-template-128.h(121,12): warning C4022: 'memcpy': pointer mismatch for actual parameter 1 [F:\gitP\xmrig\xmrig\build_arm64\src\3rdparty\argon2\argon2-sse2.vcxproj]
    12>F:\gitP\xmrig\xmrig\src\3rdparty\argon2\arch\x86_64\lib\argon2-template-128.h(162,29): error C2065: 'state': undeclared identifier [F:\gitP\xmrig\xmrig\build_arm64\src\3rdparty\argon2\argon2-sse2.vcxproj]
    12>F:\gitP\xmrig\xmrig\src\3rdparty\argon2\arch\x86_64\lib\argon2-template-128.h(164,29): error C2065: 'state': undeclared identifier [F:\gitP\xmrig\xmrig\build_arm64\src\3rdparty\argon2\argon2-sse2.vcxproj]
    10>F:\gitP\xmrig\xmrig\src\3rdparty\argon2\arch\x86_64\lib\argon2-avx512f.c(15,16): error C2061: syntax error: identifier 'f' [F:\gitP\xmrig\xmrig\build_arm64\src\3rdparty\argon2\argon2-avx512f.vcxproj]
    10>F:\gitP\xmrig\xmrig\src\3rdparty\argon2\arch\x86_64\lib\argon2-avx512f.c(15,16): error C2059: syntax error: ';' [F:\gitP\xmrig\xmrig\build_arm64\src\3rdparty\argon2\argon2-avx512f.vcxproj]
    10>F:\gitP\xmrig\xmrig\src\3rdparty\argon2\arch\x86_64\lib\argon2-avx512f.c(15,26): error C2146: syntax error: missing ')' before identifier 'x' [F:\gitP\xmrig\xmrig\build_arm64\src\3rdparty\argon2\argon2-avx512f.vcxproj]
    10>F:\gitP\xmrig\xmrig\src\3rdparty\argon2\arch\x86_64\lib\argon2-avx512f.c(15,26): error C2061: syntax error: identifier 'x' [F:\gitP\xmrig\xmrig\build_arm64\src\3rdparty\argon2\argon2-avx512f.vcxproj]
    10>F:\gitP\xmrig\xmrig\src\3rdparty\argon2\arch\x86_64\lib\argon2-avx512f.c(15,27): error C2059: syntax error: ',' [F:\gitP\xmrig\xmrig\build_arm64\src\3rdparty\argon2\argon2-avx512f.vcxproj]
    10>F:\gitP\xmrig\xmrig\src\3rdparty\argon2\arch\x86_64\lib\argon2-avx512f.c(15,38): error C2059: syntax error: ')' [F:\gitP\xmrig\xmrig\build_arm64\src\3rdparty\argon2\argon2-avx512f.vcxproj]
    10>F:\gitP\xmrig\xmrig\src\3rdparty\argon2\arch\x86_64\lib\argon2-avx512f.c(153,32): error C2143: syntax error: missing ')' before '*' [F:\gitP\xmrig\xmrig\build_arm64\src\3rdparty\argon2\argon2-avx512f.vcxproj]
    10>F:\gitP\xmrig\xmrig\src\3rdparty\argon2\arch\x86_64\lib\argon2-avx512f.c(153,32): error C2143: syntax error: missing '{' before '*' [F:\gitP\xmrig\xmrig\build_arm64\src\3rdparty\argon2\argon2-avx512f.vcxproj]
    10>F:\gitP\xmrig\xmrig\src\3rdparty\argon2\arch\x86_64\lib\argon2-avx512f.c(153,42): error C2371: 'block': redefinition; different basic types [F:\gitP\xmrig\xmrig\build_arm64\src\3rdparty\argon2\argon2-avx512f.vcxproj]


# Discussion History
# Action History
- Created by: spacelg | 2022-02-22T08:53:28+00:00
