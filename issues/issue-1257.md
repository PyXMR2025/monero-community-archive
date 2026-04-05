---
title: OPENSSL_CRYPTO_LIBRARY OPENSSL_INCLUDE_DIR
source_url: https://github.com/xmrig/xmrig/issues/1257
author: Conan-Wolf
assignees: []
labels: []
created_at: '2019-11-02T04:10:31+00:00'
updated_at: '2020-02-10T06:26:39+00:00'
type: issue
status: closed
closed_at: '2019-11-02T18:16:40+00:00'
---

# Original Description
how can i fix OPENSSL_CRYPTO_LIBRARY OPENSSL_INCLUDE_DIR?
this is happening when i am doing cmake

``-- Use ARM_TARGET=7 (armv7l)
-- Found HWLOC: /usr/lib/arm-linux-gnueabihf/libhwloc.so
-- Found UV: /usr/lib/arm-linux-gnueabihf/libuv.a
-- Looking for __builtin___clear_cache
-- Looking for __builtin___clear_cache - found
-- Could NOT find OpenSSL, try to set the path to OpenSSL root folder in the system variable OPENSSL_ROOT_DIR (missing: OPENSSL_CRYPTO_LIBRARY OPENSSL_INCLUDE_DIR)
CMake Error at cmake/OpenSSL.cmake:21 (message):
  OpenSSL NOT found: use `-DWITH_TLS=OFF` to build without TLS support
Call Stack (most recent call first):
  CMakeLists.txt:160 (include)
``
do note i am newer to linux 

# Discussion History
## Conan-Wolf | 2019-11-02T18:16:53+00:00
solved it myself

## GayathriBabu98 | 2020-02-10T06:26:39+00:00
same error i have...please help me how to solve it??

# Action History
- Created by: Conan-Wolf | 2019-11-02T04:10:31+00:00
- Closed at: 2019-11-02T18:16:40+00:00
