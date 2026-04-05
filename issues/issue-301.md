---
title: 'New wiki page: FreeBSD Build'
source_url: https://github.com/xmrig/xmrig/issues/301
author: z3dm4n
assignees: []
labels: []
created_at: '2017-12-28T09:57:22+00:00'
updated_at: '2018-05-09T12:34:20+00:00'
type: issue
status: closed
closed_at: '2018-01-01T14:19:21+00:00'
---

# Original Description
## FreeBSD 11
There are 2 different ways of installing XMRig on FreeBSD 11.

### 1. Installation via the ports collection:
```
cd /usr/ports/net-p2p/xmrig && make install clean
```
*or*
```
cd /usr/ports/ports-mgmt/portmaster && make install clean
portmaster net-p2p/xmrig
```

### 2. Using binary packages and building XMRig from source:

Using Clang:
```
pkg install git clang38 cmake libuv libmicrohttpd
git clone https://github.com/xmrig/xmrig.git
cd xmrig
mkdir build
cd build
cmake ..
make
```
*or*

Using GCC:
```
pkg install git gcc7 cmake libuv libmicrohttpd
git clone https://github.com/xmrig/xmrig.git
cd xmrig
mkdir build
cd build
cmake -DCMAKE_C_COMPILER=gcc7 -DCMAKE_CXX_COMPILER=g++7 ..
make
```

## Additional CMake options

* `-DWITH_LIBCPUID=OFF` Disable libcpuid. Auto configuration of CPU after this will be very limited.
* `-DWITH_AEON=OFF` Disable CryptoNight-Lite support.
* `-DWITH_HTTPD=OFF` Build without built-in httpd and API.
* `-DUV_LIBRARY=/usr/local/lib/libuv.a` Use static libuv version.
* `-DMHD_LIBRARY=/usr/local/lib/libmicrohttpd.a` Use static libmicrohttpd version.

# Discussion History
## xmrig | 2018-01-01T14:19:21+00:00
Thank you, I added the page https://github.com/xmrig/xmrig/wiki/FreeBSD-Build

## lisergey | 2018-05-09T10:08:35+00:00
@xmrig, cmake/FindUV.cmake is using static linking of libuv by default.
with
```
diff --git a/cmake/FindUV.cmake b/cmake/FindUV.cmake
index ba59d1d..6335de9 100644
--- a/cmake/FindUV.cmake
+++ b/cmake/FindUV.cmake
@@ -10,13 +10,13 @@ find_path(UV_INCLUDE_DIR NAMES uv.h)
 
 find_library(
     UV_LIBRARY
-    NAMES libuv.a uv libuv
+    NAMES libuv.so libuv.a uv libuv
     PATHS "${XMRIG_DEPS}" ENV "XMRIG_DEPS"
     PATH_SUFFIXES "lib"
     NO_DEFAULT_PATH
 )
 
-find_library(UV_LIBRARY NAMES libuv.a uv libuv)
+find_library(UV_LIBRARY NAMES libuv.so libuv.a uv libuv)
 
 set(UV_LIBRARIES ${UV_LIBRARY})
 set(UV_INCLUDE_DIRS ${UV_INCLUDE_DIR})

```
the build was successful:
```
ldd build/xmrig|grep libuv
        libuv.so.1 => /usr/local/lib/libuv.so.1 (0x80088e000)
```


# Action History
- Created by: z3dm4n | 2017-12-28T09:57:22+00:00
- Closed at: 2018-01-01T14:19:21+00:00
