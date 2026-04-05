---
title: 'A compilation error occurs with xmrig 3.1.0 '
source_url: https://github.com/xmrig/xmrig/issues/1128
author: oiuacc
assignees: []
labels:
- bug
created_at: '2019-08-19T15:53:55+00:00'
updated_at: '2019-09-14T13:43:37+00:00'
type: issue
status: closed
closed_at: '2019-08-19T16:13:51+00:00'
---

# Original Description
[root@a9be build]# cmake .. -DCMAKE_BUILD_TYPE=Release -DUV_LIBRARY=/usr/lib64/libuv.a
-- The C compiler identification is GNU 4.8.5
-- The CXX compiler identification is GNU 4.8.5
-- Check for working C compiler: /usr/bin/cc
-- Check for working C compiler: /usr/bin/cc -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working CXX compiler: /usr/bin/c++
-- Check for working CXX compiler: /usr/bin/c++ -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Looking for syslog.h
-- Looking for syslog.h - found
-- Found HWLOC: /usr/lib64/libhwloc.so  
-- Found UV: /usr/lib64/libuv.a  
-- Looking for __builtin___clear_cache
-- Looking for __builtin___clear_cache - found
-- argon2: detecting feature 'sse2'...
-- Performing Test FEATURE_sse2_NOFLAG
-- Performing Test FEATURE_sse2_NOFLAG - Success
-- argon2: feature 'sse2' detected!
-- argon2: detecting feature 'ssse3'...
-- Performing Test FEATURE_ssse3_NOFLAG
-- Performing Test FEATURE_ssse3_NOFLAG - Failed
-- Performing Test FEATURE_ssse3_FLAG
-- Performing Test FEATURE_ssse3_FLAG - Success
-- argon2: feature 'ssse3' detected!
-- argon2: detecting feature 'xop'...
-- Performing Test FEATURE_xop_NOFLAG
-- Performing Test FEATURE_xop_NOFLAG - Failed
-- Performing Test FEATURE_xop_FLAG
-- Performing Test FEATURE_xop_FLAG - Success
-- argon2: feature 'xop' detected!
-- argon2: detecting feature 'avx2'...
-- Performing Test FEATURE_avx2_NOFLAG
-- Performing Test FEATURE_avx2_NOFLAG - Failed
-- Performing Test FEATURE_avx2_FLAG
-- Performing Test FEATURE_avx2_FLAG - Success
-- argon2: feature 'avx2' detected!
-- argon2: detecting feature 'avx512f'...
-- Performing Test FEATURE_avx512f_NOFLAG
-- Performing Test FEATURE_avx512f_NOFLAG - Failed
-- Performing Test FEATURE_avx512f_FLAG
-- Performing Test FEATURE_avx512f_FLAG - Failed
CMake Error at src/3rdparty/argon2/CMakeLists.txt:80 (target_sources):
  Unknown CMake command "target_sources".


-- Configuring incomplete, errors occurred!
See also "/root/xmrig/build/CMakeFiles/CMakeOutput.log".
See also "/root/xmrig/build/CMakeFiles/CMakeError.log".
[root@ecs-a9be build]# make
make: *** No targets specified and no makefile found.  Stop.
[root@a9be build]# 

# Discussion History
## xmrig | 2019-08-19T16:11:37+00:00
Seems you use old cmake without `target_sources` support. You have 2 options:
1. If you don't need Argon2 algorithm support, you can disable it by `cmake .. -DWITH_ARGON2=OFF`.
2. Otherwise you should use newer cmake version.

## oiuacc | 2019-08-19T16:13:46+00:00
thx

## xmrig | 2019-09-14T13:43:21+00:00
cmake issue fixed https://github.com/xmrig/xmrig/commit/179ef31b80f2cc42c948b629689f00e547b483f6

# Action History
- Created by: oiuacc | 2019-08-19T15:53:55+00:00
- Closed at: 2019-08-19T16:13:51+00:00
