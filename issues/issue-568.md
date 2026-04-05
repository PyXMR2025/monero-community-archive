---
title: '/lib64/libc.so.6: version `GLIBC_2.14'' not found'
source_url: https://github.com/xmrig/xmrig/issues/568
author: wsm3
assignees: []
labels: []
created_at: '2018-04-20T07:49:04+00:00'
updated_at: '2018-11-05T13:29:02+00:00'
type: issue
status: closed
closed_at: '2018-11-05T13:29:02+00:00'
---

# Original Description
Hello!

I build with 
`cmake .. -DUV_LIBRARY=/usr/lib/x86_64-linux-gnu/libuv.a`
but after run 
`./xmrig: /lib64/libc.so.6: version `GLIBC_2.14' not found (required by ./xmrig)`

It is possible to compile with GLIBC_2.14 static?

# Discussion History
## wsm3 | 2018-04-20T07:57:16+00:00
CMakeLists.txt

`option(WITH_LIBCPUID **"Use Libcpuid" OFF)**
option(WITH_AEON     "CryptoNight-Lite support" ON)
option(WITH_HTTPD    "HTTP REST API" OFF)
option(BUILD_STATIC  "Build static binary" OFF)`

`./xmrig: /lib64/libc.so.6: versionGLIBC_2.14' not found (required by ./xmrig)``




## JKLHJ | 2018-04-21T04:06:44+00:00
![qq 20180421120332](https://user-images.githubusercontent.com/30529699/39080174-18c7e77a-455c-11e8-9888-7a0968149dcb.png)
Yes, I also encountered the same problem, how to statically link libraries? Make it run in any version of GLIBC?

## wsm3 | 2018-04-21T08:26:05+00:00
I decided like this

`cmake .. -DWITH_LIBCPUID=OFF -DUV_LIBRARY=/usr/lib/x86_64-linux-gnu/libuv.so -DBUILD_STATIC=ON`


/usr/lib/x86_64-linux-gnu/libuv.so - is static link


# Action History
- Created by: wsm3 | 2018-04-20T07:49:04+00:00
- Closed at: 2018-11-05T13:29:02+00:00
