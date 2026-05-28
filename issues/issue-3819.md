---
title: '[MSVC] Failed to build xmrig on arm64ec with error LNK2001: unresolved external
  symbol "struct RandomX_ConfigurationBase RandomX_CurrentConfig"'
source_url: https://github.com/xmrig/xmrig/issues/3819
author: KarenHuang2016
assignees: []
labels:
- arm
created_at: '2026-05-25T08:06:32+00:00'
updated_at: '2026-05-26T07:50:01+00:00'
type: issue
status: closed
closed_at: '2026-05-26T07:45:04+00:00'
---

# Original Description
**Describe the bug**
The MSVC team regularly builds popular open-source projects, including yours, with development versions of the build tools in order to find and fix regressions in the compiler and libraries before they can ship and cause trouble for the world. This also allows us to provide advance notice of breaking changes, which is the case here.

xmrig failed to build on **arm64ec** with  error LNK2001: unresolved external symbol "struct RandomX_ConfigurationBase RandomX_CurrentConfig" (?RandomX_CurrentConfig@@3URandomX_ConfigurationBase@@A) (EC Symbol) with MSVC on Windows. Could you help take a look? Thanks in advance.


**To Reproduce**

1. Open a CMD.
2. "C:\Program Files\Microsoft Visual Studio\2022\Enterprise\Common7\Tools\VsDevCmd.bat" -host_arch=amd64 -arch=arm64 -winsdk=10.0.26100.0
3. git clone https://github.com/xmrig/xmrig C:\gitP\xmrig\xmrig
4. Download https://github.com/xmrig/xmrig-deps/archive/refs/tags/v4.1.zip and unzip it to C:\gitP\xmrig\xmrig.
5. cd C:\gitP\xmrig\xmrig
6. mkdir build_arm64ec && cd build_arm64ec
7. cmake -G "Visual Studio 17 2022" -A ARM64EC -DCMAKE_SYSTEM_VERSION=10.0.26100.0 -DXMRIG_DEPS='C:\gitP\xmrig\xmrig\xmrig-deps-4.1\msvc2019\x64' -DWITH_LIBCPUID=OFF ..
8. msbuild /m /p:Platform=ARM64EC /p:Configuration=Release xmrig.sln /t:Rebuild

**Error info:**
CpuWorker.obj : error LNK2001: unresolved external symbol "struct RandomX_ConfigurationBase RandomX_CurrentConfig" (?RandomX_CurrentConfig@@3URandomX_ConfigurationBase@@A) (EC Symbol) [C:\gitP\xmrig\xmrig\build_arm64ec\xmrig.vcxproj]
         C:\gitP\xmrig\xmrig\build_arm64ec\Release\xmrig.exe : fatal error LNK1120: 1 unresolved externals [C:\gitP\xmrig\xmrig\build_arm64ec\xmrig.vcxproj]

**build log file:** 

[Build (23).log](https://github.com/user-attachments/files/28211920/Build.23.log)


# Discussion History
## SChernykh | 2026-05-25T08:15:36+00:00
@KarenHuang2016 can you try this patch? I don't have an arm64ec Windows system to test it on.
```
diff --git a/src/crypto/randomx/randomx.h b/src/crypto/randomx/randomx.h
index 51998e29..4b23b37d 100644
--- a/src/crypto/randomx/randomx.h
+++ b/src/crypto/randomx/randomx.h
@@ -163,7 +163,7 @@ extern RandomX_ConfigurationGraft RandomX_GraftConfig;
 extern RandomX_ConfigurationSafex RandomX_SafexConfig;
 extern RandomX_ConfigurationYada RandomX_YadaConfig;
 
-extern RandomX_ConfigurationBase RandomX_CurrentConfig;
+alignas(64) extern RandomX_ConfigurationBase RandomX_CurrentConfig;
 
 template<typename T>
 void randomx_apply_config(const T& config)

```

## xmrig | 2026-05-25T09:12:41+00:00
Native ARM with MSVC for Windows is not supported; for native builds, you must use MSYS2 with clang.
arm64ec has never been tested and, as a result, is not supported either.

## KarenHuang2016 | 2026-05-26T07:45:00+00:00
@SChernykh The error LNK2001 is still reported after applied the patch. As @xmrig mentioned arm64ec is not support with MSVC on Windows, we will stop testing it. 

# Action History
- Created by: KarenHuang2016 | 2026-05-25T08:06:32+00:00
- Closed at: 2026-05-26T07:45:04+00:00
