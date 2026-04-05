---
title: static build issue..!!??
source_url: https://github.com/xmrig/xmrig/issues/508
author: Gill1000
assignees: []
labels:
- libuv
created_at: '2018-04-06T16:37:37+00:00'
updated_at: '2018-04-07T03:44:01+00:00'
type: issue
status: closed
closed_at: '2018-04-07T03:44:01+00:00'
---

# Original Description
this is my first lines of cmakelist.

option(WITH_LIBCPUID "Use Libcpuid" ON)
option(WITH_AEON     "CryptoNight-Lite support" ON)
option(WITH_HTTPD    "HTTP REST API" OFF)
option(BUILD_STATIC  "Build static binary" ON)

i want to build static  ..i m using xmrig2.5.2 building by gcc in window8.1
in cmakelist "build static binary" is ON but still i m getting  libwinpthread-1.dill missing.!!

# Discussion History
## xmrig | 2018-04-06T17:25:14+00:00
You trying build with wrong libuv version, please use https://github.com/xmrig/xmrig-deps
Thank you.

## Gill1000 | 2018-04-07T03:43:54+00:00
yes ..you were right ..now its working 
thanks

# Action History
- Created by: Gill1000 | 2018-04-06T16:37:37+00:00
- Closed at: 2018-04-07T03:44:01+00:00
