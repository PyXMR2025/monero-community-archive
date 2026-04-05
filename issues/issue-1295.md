---
title: I opened it.  -DWITH_EMBEDDED_CONFIG=ON  But why it didn't work
source_url: https://github.com/xmrig/xmrig/issues/1295
author: axsoftshi
assignees: []
labels: []
created_at: '2019-11-16T20:30:08+00:00'
updated_at: '2019-11-16T20:42:41+00:00'
type: issue
status: closed
closed_at: '2019-11-16T20:42:41+00:00'
---

# Original Description
[100%] Built target xmrig-notls
localhost:~/xmrig/build# ./xmrig-notls 
[2019-11-16 20:28:02.944] unable to open "/root/xmrig/build/config.json".
localhost:~/xmrig/build# ldd xmrig-notls 
        /lib/ld-musl-x86_64.so.1 (0x7f41abfee000)
localhost:~/xmrig/build# cmake .. -DWITH_EMBEDDED_CONFIG=ON -DWITH_TLS=OFF -DWITH_CN_G
PU=OFF -DUV_INCLUDE_DIR=/root/libuv-1.33.1/include -DBUILD_STATIC=ON -DUV_LIBRARY=/roo
t/libuv-1.33.1/build/libuv_a.a -DHWLOC_INCLUDE_DIR=~/hwloc-2.0.4/include/ -DHWLOC_LIBR
ARY=~/hwloc-2.0.4/hwloc/.libs/libhwloc.a


# Discussion History
## axsoftshi | 2019-11-16T20:30:44+00:00
@xmrig 

## axsoftshi | 2019-11-16T20:33:15+00:00
@xmrig alpine linux

# Action History
- Created by: axsoftshi | 2019-11-16T20:30:08+00:00
- Closed at: 2019-11-16T20:42:41+00:00
