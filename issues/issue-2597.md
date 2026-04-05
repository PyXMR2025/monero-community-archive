---
title: Building with Visual Studio 2015 fails.
source_url: https://github.com/xmrig/xmrig/issues/2597
author: RCECoder
assignees: []
labels: []
created_at: '2021-09-22T17:02:44+00:00'
updated_at: '2025-06-16T20:48:54+00:00'
type: issue
status: closed
closed_at: '2025-06-16T20:48:54+00:00'
---

# Original Description
Is 2015 no longer supported?

```

$ cmake .. -G "Visual Studio 14 2015" -A x64 -DXMRIG_DEPS="c:\xmrig-deps\msvc2015\x64"
-- Selecting Windows SDK version  to target Windows 10.0.18363.
-- Found UV: C:/xmrig-deps/msvc2015/x64/lib/libuv.lib
-- The ASM_MASM compiler identification is MSVC
-- Found assembler: C:/Program Files (x86)/Microsoft Visual Studio 14.0/VC/bin/x86_amd64/ml64.exe
-- WITH_MSR=ON
-- Found OpenSSL: C:/xmrig-deps/msvc2015/x64/lib/libcrypto.lib (found version "1.1.1c")
-- Configuring done
-- Generating done
-- Build files have been written to: C:/Users/Crim/Desktop/xmrig-master/Build



$ cmake --build . --config Release
Microsoft (R) Build Engine version 14.0.25420.1
Copyright (C) Microsoft Corporation. All rights reserved.

  Checking Build System
  Building Custom Rule C:/Users/Crim/Desktop/xmrig-master/src/3rdparty/argon2/CMakeLists.txt
  argon2-avx2.c
  LINK : MSIL .netmodule or module compiled with /GL found; restarting link with /LTCG; add /LTCG to the link command line to improve linker performance
  argon2-avx2.vcxproj -> C:\Users\Crim\Desktop\xmrig-master\Build\src\3rdparty\argon2\Release\argon2-avx2.lib
  Building Custom Rule C:/Users/Crim/Desktop/xmrig-master/src/3rdparty/argon2/CMakeLists.txt
cl : Command line warning D9002: ignoring unknown option '/arch:AVX512F' [C:\Users\Crim\Desktop\xmrig-master\Build\src\3rdparty\argon2\argon2-avx512f.vcxproj]
  argon2-avx512f.c
C:\Users\Crim\Desktop\xmrig-master\src\3rdparty\argon2\arch\x86_64\lib\argon2-avx512f.c(15): error C2061: syntax error: identifier 'f' [C:\Users\Crim\Desktop\xmrig-master\B
uild\src\3rdparty\argon2\argon2-avx512f.vcxproj]
C:\Users\Crim\Desktop\xmrig-master\src\3rdparty\argon2\arch\x86_64\lib\argon2-avx512f.c(15): error C2059: syntax error: ';' [C:\Users\Crim\Desktop\xmrig-master\Build\src\3r
dparty\argon2\argon2-avx512f.vcxproj]
C:\Users\Crim\Desktop\xmrig-master\src\3rdparty\argon2\arch\x86_64\lib\argon2-avx512f.c(15): error C2146: syntax error: missing ')' before identifier 'x' [C:\Users\Crim\Des
ktop\xmrig-master\Build\src\3rdparty\argon2\argon2-avx512f.vcxproj]
C:\Users\Crim\Desktop\xmrig-master\src\3rdparty\argon2\arch\x86_64\lib\argon2-avx512f.c(15): error C2061: syntax error: identifier 'x' [C:\Users\Crim\Desktop\xmrig-master\B
uild\src\3rdparty\argon2\argon2-avx512f.vcxproj]
C:\Users\Crim\Desktop\xmrig-master\src\3rdparty\argon2\arch\x86_64\lib\argon2-avx512f.c(15): error C2059: syntax error: ',' [C:\Users\Crim\Desktop\xmrig-master\Build\src\3r
dparty\argon2\argon2-avx512f.vcxproj]
C:\Users\Crim\Desktop\xmrig-master\src\3rdparty\argon2\arch\x86_64\lib\argon2-avx512f.c(15): error C2059: syntax error: ')' [C:\Users\Crim\Desktop\xmrig-master\Build\src\3r
dparty\argon2\argon2-avx512f.vcxproj]
C:\Users\Crim\Desktop\xmrig-master\src\3rdparty\argon2\arch\x86_64\lib\argon2-avx512f.c(153): error C2143: syntax error: missing ')' before '*' [C:\Users\Crim\Desktop\xmrig
-master\Build\src\3rdparty\argon2\argon2-avx512f.vcxproj]
C:\Users\Crim\Desktop\xmrig-master\src\3rdparty\argon2\arch\x86_64\lib\argon2-avx512f.c(153): error C2143: syntax error: missing '{' before '*' [C:\Users\Crim\Desktop\xmrig
-master\Build\src\3rdparty\argon2\argon2-avx512f.vcxproj]
C:\Users\Crim\Desktop\xmrig-master\src\3rdparty\argon2\arch\x86_64\lib\argon2-avx512f.c(153): error C2371: 'block': redefinition; different basic types [C:\Users\Crim\Deskt
op\xmrig-master\Build\src\3rdparty\argon2\argon2-avx512f.vcxproj]
  C:\Users\Crim\Desktop\xmrig-master\src\3rdparty\argon2\lib\core.h(54): note: see declaration of 'block'
C:\Users\Crim\Desktop\xmrig-master\src\3rdparty\argon2\arch\x86_64\lib\argon2-avx512f.c(153): warning C4228: nonstandard extension used: qualifiers after comma in declarat
or list are ignored [C:\Users\Crim\Desktop\xmrig-master\Build\src\3rdparty\argon2\argon2-avx512f.vcxproj]
C:\Users\Crim\Desktop\xmrig-master\src\3rdparty\argon2\arch\x86_64\lib\argon2-avx512f.c(153): error C2143: syntax error: missing ';' before '*' [C:\Users\Crim\Desktop\xmrig
-master\Build\src\3rdparty\argon2\argon2-avx512f.vcxproj]
C:\Users\Crim\Desktop\xmrig-master\src\3rdparty\argon2\arch\x86_64\lib\argon2-avx512f.c(154): error C2059: syntax error: 'type' [C:\Users\Crim\Desktop\xmrig-master\Build\sr
c\3rdparty\argon2\argon2-avx512f.vcxproj]
C:\Users\Crim\Desktop\xmrig-master\src\3rdparty\argon2\arch\x86_64\lib\argon2-avx512f.c(154): error C2059: syntax error: ')' [C:\Users\Crim\Desktop\xmrig-master\Build\src\3
rdparty\argon2\argon2-avx512f.vcxproj]
C:\Users\Crim\Desktop\xmrig-master\src\3rdparty\argon2\arch\x86_64\lib\argon2-avx512f.c(195): error C2065: '__m512i': undeclared identifier [C:\Users\Crim\Desktop\xmrig-mas
ter\Build\src\3rdparty\argon2\argon2-avx512f.vcxproj]
C:\Users\Crim\Desktop\xmrig-master\src\3rdparty\argon2\arch\x86_64\lib\argon2-avx512f.c(195): error C2146: syntax error: missing ';' before identifier 'zero_block' [C:\Use
rs\Crim\Desktop\xmrig-master\Build\src\3rdparty\argon2\argon2-avx512f.vcxproj]
C:\Users\Crim\Desktop\xmrig-master\src\3rdparty\argon2\arch\x86_64\lib\argon2-avx512f.c(195): error C2065: 'zero_block': undeclared identifier [C:\Users\Crim\Desktop\xmrig-
master\Build\src\3rdparty\argon2\argon2-avx512f.vcxproj]
C:\Users\Crim\Desktop\xmrig-master\src\3rdparty\argon2\arch\x86_64\lib\argon2-avx512f.c(195): error C2109: subscript requires array or pointer type [C:\Users\Crim\Desktop\x
mrig-master\Build\src\3rdparty\argon2\argon2-avx512f.vcxproj]
C:\Users\Crim\Desktop\xmrig-master\src\3rdparty\argon2\arch\x86_64\lib\argon2-avx512f.c(196): error C2065: '__m512i': undeclared identifier [C:\Users\Crim\Desktop\xmrig-mas
ter\Build\src\3rdparty\argon2\argon2-avx512f.vcxproj]
C:\Users\Crim\Desktop\xmrig-master\src\3rdparty\argon2\arch\x86_64\lib\argon2-avx512f.c(196): error C2146: syntax error: missing ';' before identifier 'zero2_block' [C:\Us
ers\Crim\Desktop\xmrig-master\Build\src\3rdparty\argon2\argon2-avx512f.vcxproj]
C:\Users\Crim\Desktop\xmrig-master\src\3rdparty\argon2\arch\x86_64\lib\argon2-avx512f.c(196): error C2065: 'zero2_block': undeclared identifier [C:\Users\Crim\Desktop\xmrig
-master\Build\src\3rdparty\argon2\argon2-avx512f.vcxproj]
C:\Users\Crim\Desktop\xmrig-master\src\3rdparty\argon2\arch\x86_64\lib\argon2-avx512f.c(196): error C2109: subscript requires array or pointer type [C:\Users\Crim\Desktop\x
mrig-master\Build\src\3rdparty\argon2\argon2-avx512f.vcxproj]
C:\Users\Crim\Desktop\xmrig-master\src\3rdparty\argon2\arch\x86_64\lib\argon2-avx512f.c(198): error C2065: 'zero_block': undeclared identifier [C:\Users\Crim\Desktop\xmrig-
master\Build\src\3rdparty\argon2\argon2-avx512f.vcxproj]
C:\Users\Crim\Desktop\xmrig-master\src\3rdparty\argon2\arch\x86_64\lib\argon2-avx512f.c(198): warning C4022: 'memset': pointer mismatch for actual parameter 1 [C:\Users\TO
W\Desktop\xmrig-master\Build\src\3rdparty\argon2\argon2-avx512f.vcxproj]
C:\Users\Crim\Desktop\xmrig-master\src\3rdparty\argon2\arch\x86_64\lib\argon2-avx512f.c(199): error C2065: 'zero2_block': undeclared identifier [C:\Users\Crim\Desktop\xmrig
-master\Build\src\3rdparty\argon2\argon2-avx512f.vcxproj]
C:\Users\Crim\Desktop\xmrig-master\src\3rdparty\argon2\arch\x86_64\lib\argon2-avx512f.c(199): warning C4022: 'memset': pointer mismatch for actual parameter 1 [C:\Users\TO
W\Desktop\xmrig-master\Build\src\3rdparty\argon2\argon2-avx512f.vcxproj]
C:\Users\Crim\Desktop\xmrig-master\src\3rdparty\argon2\arch\x86_64\lib\argon2-avx512f.c(205): warning C4013: 'fill_block' undefined; assuming extern returning int [C:\User
s\Crim\Desktop\xmrig-master\Build\src\3rdparty\argon2\argon2-avx512f.vcxproj]
C:\Users\Crim\Desktop\xmrig-master\src\3rdparty\argon2\arch\x86_64\lib\argon2-avx512f.c(205): error C2065: 'zero_block': undeclared identifier [C:\Users\Crim\Desktop\xmrig-
master\Build\src\3rdparty\argon2\argon2-avx512f.vcxproj]
C:\Users\Crim\Desktop\xmrig-master\src\3rdparty\argon2\arch\x86_64\lib\argon2-avx512f.c(208): error C2065: 'zero2_block': undeclared identifier [C:\Users\Crim\Desktop\xmrig
-master\Build\src\3rdparty\argon2\argon2-avx512f.vcxproj]
C:\Users\Crim\Desktop\xmrig-master\src\3rdparty\argon2\arch\x86_64\lib\argon2-avx512f.c(218): error C2065: '__m512i': undeclared identifier [C:\Users\Crim\Desktop\xmrig-mas
ter\Build\src\3rdparty\argon2\argon2-avx512f.vcxproj]
C:\Users\Crim\Desktop\xmrig-master\src\3rdparty\argon2\arch\x86_64\lib\argon2-avx512f.c(218): error C2146: syntax error: missing ';' before identifier 'state' [C:\Users\TO
W\Desktop\xmrig-master\Build\src\3rdparty\argon2\argon2-avx512f.vcxproj]
C:\Users\Crim\Desktop\xmrig-master\src\3rdparty\argon2\arch\x86_64\lib\argon2-avx512f.c(218): error C2065: 'state': undeclared identifier [C:\Users\Crim\Desktop\xmrig-maste
r\Build\src\3rdparty\argon2\argon2-avx512f.vcxproj]
C:\Users\Crim\Desktop\xmrig-master\src\3rdparty\argon2\arch\x86_64\lib\argon2-avx512f.c(218): error C2109: subscript requires array or pointer type [C:\Users\Crim\Desktop\x
mrig-master\Build\src\3rdparty\argon2\argon2-avx512f.vcxproj]
C:\Users\Crim\Desktop\xmrig-master\src\3rdparty\argon2\arch\x86_64\lib\argon2-avx512f.c(263): error C2065: 'state': undeclared identifier [C:\Users\Crim\Desktop\xmrig-maste
r\Build\src\3rdparty\argon2\argon2-avx512f.vcxproj]
C:\Users\Crim\Desktop\xmrig-master\src\3rdparty\argon2\arch\x86_64\lib\argon2-avx512f.c(263): warning C4022: 'memcpy': pointer mismatch for actual parameter 1 [C:\Users\TO
W\Desktop\xmrig-master\Build\src\3rdparty\argon2\argon2-avx512f.vcxproj]
C:\Users\Crim\Desktop\xmrig-master\src\3rdparty\argon2\arch\x86_64\lib\argon2-avx512f.c(304): error C2065: 'state': undeclared identifier [C:\Users\Crim\Desktop\xmrig-maste
r\Build\src\3rdparty\argon2\argon2-avx512f.vcxproj]
C:\Users\Crim\Desktop\xmrig-master\src\3rdparty\argon2\arch\x86_64\lib\argon2-avx512f.c(306): error C2065: 'state': undeclared identifier [C:\Users\Crim\Desktop\xmrig-maste
r\Build\src\3rdparty\argon2\argon2-avx512f.vcxproj]
  Building Custom Rule C:/Users/Crim/Desktop/xmrig-master/src/3rdparty/argon2/CMakeLists.txt
  argon2-sse2.c
  LINK : MSIL .netmodule or module compiled with /GL found; restarting link with /LTCG; add /LTCG to the link command line to improve linker performance
  argon2-sse2.vcxproj -> C:\Users\Crim\Desktop\xmrig-master\Build\src\3rdparty\argon2\Release\argon2-sse2.lib
  Building Custom Rule C:/Users/Crim/Desktop/xmrig-master/src/3rdparty/argon2/CMakeLists.txt
cl : Command line warning D9002: ignoring unknown option '/arch:SSSE3' [C:\Users\Crim\Desktop\xmrig-master\Build\src\3rdparty\argon2\argon2-ssse3.vcxproj]
  argon2-ssse3.c
  LINK : MSIL .netmodule or module compiled with /GL found; restarting link with /LTCG; add /LTCG to the link command line to improve linker performance
  argon2-ssse3.vcxproj -> C:\Users\Crim\Desktop\xmrig-master\Build\src\3rdparty\argon2\Release\argon2-ssse3.lib
  Building Custom Rule C:/Users/Crim/Desktop/xmrig-master/src/3rdparty/argon2/CMakeLists.txt
  argon2-xop.c
  LINK : MSIL .netmodule or module compiled with /GL found; restarting link with /LTCG; add /LTCG to the link command line to improve linker performance
  argon2-xop.vcxproj -> C:\Users\Crim\Desktop\xmrig-master\Build\src\3rdparty\argon2\Release\argon2-xop.lib
  Building Custom Rule C:/Users/Crim/Desktop/xmrig-master/src/3rdparty/libethash/CMakeLists.txt
  ethash_internal.c
C:\Users\Crim\Desktop\xmrig-master\src\3rdparty\libethash\ethash_internal.c(157): warning C4244: 'return': conversion from 'uint64_t' to 'uint32_t', possible loss of data
[C:\Users\Crim\Desktop\xmrig-master\Build\src\3rdparty\libethash\ethash.vcxproj]
C:\Users\Crim\Desktop\xmrig-master\src\3rdparty\libethash\ethash_internal.c(156): warning C4244: 'initializing': conversion from 'uint64_t' to 'const uint32_t', possible l
oss of data [C:\Users\Crim\Desktop\xmrig-master\Build\src\3rdparty\libethash\ethash.vcxproj]
C:\Users\Crim\Desktop\xmrig-master\src\3rdparty\libethash\ethash_internal.c(205): warning C4133: 'function': incompatible types - from 'const node *' to 'const char *' [C:
\Users\Crim\Desktop\xmrig-master\Build\src\3rdparty\libethash\ethash.vcxproj]
C:\Users\Crim\Desktop\xmrig-master\src\3rdparty\libethash\ethash_internal.c(337): warning C4028: formal parameter 3 different from declaration [C:\Users\Crim\Desktop\xmrig-
master\Build\src\3rdparty\libethash\ethash.vcxproj]
  keccakf800.c
  LINK : MSIL .netmodule or module compiled with /GL found; restarting link with /LTCG; add /LTCG to the link command line to improve linker performance
  ethash.vcxproj -> C:\Users\Crim\Desktop\xmrig-master\Build\src\3rdparty\libethash\Release\ethash.lib
  Building Custom Rule C:/Users/Crim/Desktop/xmrig-master/src/3rdparty/hwloc/CMakeLists.txt
  base64.c
  bind.c
  bitmap.c
  components.c
  diff.c
  distances.c
  misc.c
  pci-common.c
  shmem.c
  topology.c
  topology-noos.c
  topology-synthetic.c
  topology-windows.c
C:\Users\Crim\Desktop\xmrig-master\src\3rdparty\hwloc\src\topology-windows.c(1029): warning C4996: 'GetVersionExA': was declared deprecated [C:\Users\Crim\Desktop\xmrig-mas
ter\Build\src\3rdparty\hwloc\hwloc.vcxproj]
  C:\Program Files (x86)\Windows Kits\8.1\Include\um\sysinfoapi.h(433): note: see declaration of 'GetVersionExA'
  topology-x86.c
  topology-xml.c
C:\Users\Crim\Desktop\xmrig-master\src\3rdparty\hwloc\src\topology-xml.c(246): warning C4244: '=': conversion from 'unsigned long' to 'unsigned char', possible loss of dat
a [C:\Users\Crim\Desktop\xmrig-master\Build\src\3rdparty\hwloc\hwloc.vcxproj]
  topology-xml-nolibxml.c
  traversal.c
  memattrs.c
  cpukinds.c
C:\Users\Crim\Desktop\xmrig-master\src\3rdparty\hwloc\src\cpukinds.c(448): warning C4244: 'return': conversion from 'const hwloc_uint64_t' to 'int', possible loss of data
[C:\Users\Crim\Desktop\xmrig-master\Build\src\3rdparty\hwloc\hwloc.vcxproj]
  Generating Code...
  hwloc.vcxproj -> C:\Users\Crim\Desktop\xmrig-master\Build\src\3rdparty\hwloc\Release\hwloc.lib
  Building Custom Rule C:/Users/Crim/Desktop/xmrig-master/CMakeLists.txt
  Assembling C:\Users\Crim\Desktop\xmrig-master\src\crypto\cn\asm\win64\cn_main_loop.asm...
  Assembling C:\Users\Crim\Desktop\xmrig-master\src\crypto\cn\asm\win64\CryptonightR_template.asm...
  xmrig-asm.vcxproj -> C:\Users\Crim\Desktop\xmrig-master\Build\Release\xmrig-asm.lib
```

# Discussion History
## SChernykh | 2021-09-22T17:38:05+00:00
https://docs.microsoft.com/en-us/cpp/build/reference/arch-x64?view=msvc-160
> Limited support for /arch:AVX512 was added in Visual Studio 2017, and expanded in Visual Studio 2019.

## RCECoder | 2021-09-22T17:51:08+00:00
@SChernykh That is what I thought.
Do you think it is possible to build x86 with VS 2019?

# Action History
- Created by: RCECoder | 2021-09-22T17:02:44+00:00
- Closed at: 2025-06-16T20:48:54+00:00
