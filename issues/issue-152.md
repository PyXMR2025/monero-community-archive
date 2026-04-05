---
title: linux static compiler
source_url: https://github.com/xmrig/xmrig/issues/152
author: huai201208
assignees: []
labels: []
created_at: '2017-10-13T02:04:45+00:00'
updated_at: '2017-11-05T06:48:07+00:00'
type: issue
status: closed
closed_at: '2017-11-05T06:48:07+00:00'
---

# Original Description
I would like to run under linux xmrig, how can I static compiler?

# Discussion History
## mnik247 | 2017-10-15T08:54:07+00:00
+1
I tried on Ubuntu 16 and can only witn libuv:
cmake .. -DCMAKE_BUILD_TYPE=Release -DUV_LIBRARY=/usr/lib/x86_64-linux-gnu/libuv.a
Try build with:
-DUV_LIBRARY=/usr/lib/x86_64-linux-gnu/libmicrohttpd.a 
Get make ERROR:
/build/libmicrohttpd-FgwLTb/libmicrohttpd-0.9.44+dfsg/src/microhttpd/connection_https.c:157: undefined reference to `gnutls_record_check_pending'
/build/libmicrohttpd-FgwLTb/libmicrohttpd-0.9.44+dfsg/src/microhttpd/connection_https.c:154: undefined reference to `gnutls_bye'
collect2: error: ld returned 1 exit status
CMakeFiles/xmrig.dir/build.make:1137: recipe for target 'xmrig' failed
make[2]: *** [xmrig] Error 1
CMakeFiles/Makefile2:67: recipe for target 'CMakeFiles/xmrig.dir/all' failed
make[1]: *** [CMakeFiles/xmrig.dir/all] Error 2
Makefile:83: recipe for target 'all' failed
make: *** [all] Error 2

And how can I static buid with glibc?


## xmrig | 2017-10-15T09:15:09+00:00
Easy way, build without libmicrohttpd `-DWITH_HTTPD=OFF`
If you need HTTP API you should build custom libmicrohttpd without extra dependencies (TLS, etc).

# Action History
- Created by: huai201208 | 2017-10-13T02:04:45+00:00
- Closed at: 2017-11-05T06:48:07+00:00
