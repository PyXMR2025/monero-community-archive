---
title: 'Xmrig failed to build "error C7303: <func:#0> AVX512 types (__m512) are not
  currently supported in ARM64EC code" with MSVC on Windows arm64ec'
source_url: https://github.com/xmrig/xmrig/issues/3151
author: YangYang129
assignees: []
labels:
- review later
created_at: '2022-10-31T07:50:19+00:00'
updated_at: '2025-06-16T18:44:30+00:00'
type: issue
status: closed
closed_at: '2025-06-16T18:44:30+00:00'
---

# Original Description
Xmrig failed to build "error C7303: <func:#0> AVX512 types (__m512) are not currently supported in ARM64EC code" with MSVC on Windows arm64ec. It can reproduce on latest version on master branch. Could you please help look at this issue?
**Versions and configuration**
OS: Windows Server 2022 Datacenter
VS: Visual Studio 2019(16.11.20)

**Repro steps:**

1. set VSCMD_SKIP_SENDTELEMETRY=1 & "C:\Program Files (x86)\Microsoft Visual Studio\2019\Enterprise\Common7\Tools\VsDevCmd.bat" -host_arch=amd64 -arch=arm64
2. git clone https://github.com/xmrig/xmrig F:\xmrig
3. cd xmrig
4. mkdir build_arm64ec & cd build_arm64ec 
5. cmake -G "Visual Studio 16 2019" -A ARM64EC -DCMAKE_SYSTEM_VERSION=10.0.22618.0  -DCMAKE_BUILD_TYPE=Release -DXMRIG_DEPS="F:\gitP\xmrig\xmrig-deps-4.1\msvc2019\x64" -DWITH_LIBCPUID=OFF ..
6. msbuild /m /p:Platform=ARM64EC /p:Configuration=Release xmrig.sln /t:Rebuild 

**Error info:**
```
8>LIB : error C7302: <func:#0> AVX types (__m256) are not currently supported in ARM64EC code [F:\xmrig\build_arm64ec\src\3rdparty\argon2\argon2-avx2.vcxproj]
    10>LIB : error C7303: <func:#0> AVX512 types (__m512) are not currently supported in ARM64EC code [F:\xmrig\build_arm64ec\src\3rdparty\argon2\argon2-avx512f.vcxproj]
```

**Error log:**
[xmrig_msbuild.log](https://github.com/xmrig/xmrig/files/9899073/xmrig_msbuild.log)


# Discussion History
## SChernykh | 2022-10-31T08:00:30+00:00
Windows and ARM64? This build configuration has never been tested and is not supported yet. Where did you find it, is it some cloud server?

## YangYang129 | 2022-10-31T08:13:02+00:00
@SChernykh Thanks for your info. We recently work on compiling projects on cross plat X64 -> ARM64.

## xmrig | 2025-06-16T18:44:30+00:00
#3668 

# Action History
- Created by: YangYang129 | 2022-10-31T07:50:19+00:00
- Closed at: 2025-06-16T18:44:30+00:00
