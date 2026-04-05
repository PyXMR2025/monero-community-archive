---
title: Build fails with GCC-14
source_url: https://github.com/xmrig/xmrig/issues/3526
author: bgermann
assignees: []
labels: []
created_at: '2024-08-03T20:17:08+00:00'
updated_at: '2024-08-11T15:37:55+00:00'
type: issue
status: closed
closed_at: '2024-08-11T15:37:55+00:00'
---

# Original Description
**Describe the bug**
Building with GCC-14 errors:

```
In file included from /<<PKGBUILDDIR>>/src/base/crypto/Algorithm.cpp:21:
/<<PKGBUILDDIR>>/src/3rdparty/rapidjson/document.h: In member function ‘rapidjson::GenericStringRef<CharType>& rapidjson::GenericStringRef<CharType>::operator=(const rapidjson::GenericStringRef<CharType>&)’:
/<<PKGBUILDDIR>>/src/3rdparty/rapidjson/document.h:319:82: error: assignment of read-only member ‘rapidjson::GenericStringRef<CharType>::length’
  319 |     GenericStringRef& operator=(const GenericStringRef& rhs) { s = rhs.s; length = rhs.length; }
      |                                                                           ~~~~~~~^~~~~~~~~~~~
In file included from /<<PKGBUILDDIR>>/src/base/crypto/Coin.cpp:20:
/<<PKGBUILDDIR>>/src/3rdparty/rapidjson/document.h: In member function ‘rapidjson::GenericStringRef<CharType>& rapidjson::GenericStringRef<CharType>::operator=(const rapidjson::GenericStringRef<CharType>&)’:
/<<PKGBUILDDIR>>/src/3rdparty/rapidjson/document.h:319:82: error: assignment of read-only member ‘rapidjson::GenericStringRef<CharType>::length’
  319 |     GenericStringRef& operator=(const GenericStringRef& rhs) { s = rhs.s; length = rhs.length; }
      |                                                                           ~~~~~~~^~~~~~~~~~~~
[ 20%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/log/backends/FileLog.cpp.o
/usr/bin/c++ -DCL_TARGET_OPENCL_VERSION=200 -DCL_USE_DEPRECATED_OPENCL_1_2_APIS -DHAVE_BUILTIN_CLEAR_CACHE -DHAVE_ROTR -DHAVE_SYSLOG_H -DRAPIDJSON_SSE2 -DUNICODE -DXMRIG_64_BIT -DXMRIG_ALGO_ARGON2 -DXMRIG_ALGO_CN_FEMTO -DXMRIG_ALGO_CN_HEAVY -DXMRIG_ALGO_CN_LITE -DXMRIG_ALGO_CN_PICO -DXMRIG_ALGO_GHOSTRIDER -DXMRIG_ALGO_RANDOMX -DXMRIG_FEATURE_ADL -DXMRIG_FEATURE_API -DXMRIG_FEATURE_ASM -DXMRIG_FEATURE_AVX2 -DXMRIG_FEATURE_BENCHMARK -DXMRIG_FEATURE_CUDA -DXMRIG_FEATURE_DMI -DXMRIG_FEATURE_ENV -DXMRIG_FEATURE_HTTP -DXMRIG_FEATURE_HWLOC -DXMRIG_FEATURE_MSR -DXMRIG_FEATURE_NVML -DXMRIG_FEATURE_OPENCL -DXMRIG_FEATURE_SSE4_1 -DXMRIG_FEATURE_TLS -DXMRIG_FIX_RYZEN -DXMRIG_JSON_SINGLE_LINE_ARRAY -DXMRIG_MINER_PROJECT -DXMRIG_OS_LINUX -DXMRIG_OS_UNIX -DXMRIG_STRICT_OPENCL_CACHE -DXMRIG_VAES -D_FILE_OFFSET_BITS=64 -D_GNU_SOURCE -D__STDC_FORMAT_MACROS -I/<<PKGBUILDDIR>>/src -I/<<PKGBUILDDIR>>/src/3rdparty -g -O2 -ffile-prefix-map=/<<PKGBUILDDIR>>=. -fstack-protector-strong -fstack-clash-protection -Wformat -Werror=format-security -fcf-protection -Wdate-time -D_FORTIFY_SOURCE=2 -Wdate-time -D_FORTIFY_SOURCE=2 -Wall -fexceptions -fno-rtti -Wno-strict-aliasing -Wno-class-memaccess -maes -std=c++11 -MD -MT CMakeFiles/xmrig.dir/src/base/io/log/backends/FileLog.cpp.o -MF CMakeFiles/xmrig.dir/src/base/io/log/backends/FileLog.cpp.o.d -o CMakeFiles/xmrig.dir/src/base/io/log/backends/FileLog.cpp.o -c /<<PKGBUILDDIR>>/src/base/io/log/backends/FileLog.cpp
make[3]: *** [CMakeFiles/xmrig.dir/build.make:121: CMakeFiles/xmrig.dir/src/base/crypto/Coin.cpp.o] Error 1
make[3]: *** Waiting for unfinished jobs....
make[3]: *** [CMakeFiles/xmrig.dir/build.make:107: CMakeFiles/xmrig.dir/src/base/crypto/Algorithm.cpp.o] Error 1
In file included from /<<PKGBUILDDIR>>/src/base/io/json/Json.cpp:20:
/<<PKGBUILDDIR>>/src/3rdparty/rapidjson/document.h: In member function ‘rapidjson::GenericStringRef<CharType>& rapidjson::GenericStringRef<CharType>::operator=(const rapidjson::GenericStringRef<CharType>&)’:
/<<PKGBUILDDIR>>/src/3rdparty/rapidjson/document.h:319:82: error: assignment of read-only member ‘rapidjson::GenericStringRef<CharType>::length’
  319 |     GenericStringRef& operator=(const GenericStringRef& rhs) { s = rhs.s; length = rhs.length; }
      |                                                                           ~~~~~~~^~~~~~~~~~~~
In file included from /<<PKGBUILDDIR>>/src/base/io/json/JsonRequest.cpp:20:
/<<PKGBUILDDIR>>/src/3rdparty/rapidjson/document.h: In member function ‘rapidjson::GenericStringRef<CharType>& rapidjson::GenericStringRef<CharType>::operator=(const rapidjson::GenericStringRef<CharType>&)’:
/<<PKGBUILDDIR>>/src/3rdparty/rapidjson/document.h:319:82: error: assignment of read-only member ‘rapidjson::GenericStringRef<CharType>::length’
  319 |     GenericStringRef& operator=(const GenericStringRef& rhs) { s = rhs.s; length = rhs.length; }
      |                                                                           ~~~~~~~^~~~~~~~~~~~
make[3]: *** [CMakeFiles/xmrig.dir/build.make:233: CMakeFiles/xmrig.dir/src/base/io/json/JsonRequest.cpp.o] Error 1
In file included from /<<PKGBUILDDIR>>/src/base/io/json/JsonChain.h:26,
                 from /<<PKGBUILDDIR>>/src/base/io/json/JsonChain.cpp:19:
/<<PKGBUILDDIR>>/src/3rdparty/rapidjson/document.h: In member function ‘rapidjson::GenericStringRef<CharType>& rapidjson::GenericStringRef<CharType>::operator=(const rapidjson::GenericStringRef<CharType>&)’:
/<<PKGBUILDDIR>>/src/3rdparty/rapidjson/document.h:319:82: error: assignment of read-only member ‘rapidjson::GenericStringRef<CharType>::length’
  319 |     GenericStringRef& operator=(const GenericStringRef& rhs) { s = rhs.s; length = rhs.length; }
      |                                                                           ~~~~~~~^~~~~~~~~~~~
make[3]: *** [CMakeFiles/xmrig.dir/build.make:205: CMakeFiles/xmrig.dir/src/base/io/json/Json.cpp.o] Error 1
```

**To Reproduce**
Install GCC-14 and run a xmrig build.

**Expected behavior**
The build succeeds.

**Required data**
 - XMRig version 6.21.3+dfsg-1 (from Debian)
 - OS: Linux

**Additional context**
This was reported as [Debian bug](https://bugs.debian.org/1075675).

# Discussion History
## bgermann | 2024-08-11T15:37:55+00:00
This was probably a rapidjson issue.

# Action History
- Created by: bgermann | 2024-08-03T20:17:08+00:00
- Closed at: 2024-08-11T15:37:55+00:00
