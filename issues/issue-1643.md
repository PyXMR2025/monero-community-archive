---
title: ERROR when try to build
source_url: https://github.com/xmrig/xmrig/issues/1643
author: oiuacc
assignees: []
labels:
- bug
created_at: '2020-04-11T18:09:51+00:00'
updated_at: '2020-08-19T01:25:50+00:00'
type: issue
status: closed
closed_at: '2020-08-19T01:25:50+00:00'
---

# Original Description
**Describe the bug**
ERROR when try to build

**To Reproduce**
build

**Required data**
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
-- WITH_MSR=ON
-- **The ASM_MASM compiler identification is unknown
-- Found assembler: ml
CMake Error: your ASM_MASM compiler: "ml" was not found.   Please set CMAKE_ASM_MASM_COMPILER to a valid compiler path or name.**
-- Found OpenSSL: /usr/lib64/libssl.so;/usr/lib64/libcrypto.so (found version "1.0.2k")
-- The ASM compiler identification is GNU
-- Found assembler: /usr/bin/cc
-- Configuring incomplete, errors occurred!

OS is Centos 7.3 


# Discussion History
## quantflares | 2020-04-11T18:22:01+00:00
same problem, can't solve it

## xmrig | 2020-04-12T13:38:48+00:00
Fixed in dev branch.
Thank you.

## quantflares | 2020-04-12T13:43:08+00:00
How did you fixed exactly?

## xmrig | 2020-04-12T14:05:57+00:00
https://github.com/xmrig/xmrig/commit/87bb1aa4d35903a3870e2d1705e37024abc28af0

# Action History
- Created by: oiuacc | 2020-04-11T18:09:51+00:00
- Closed at: 2020-08-19T01:25:50+00:00
