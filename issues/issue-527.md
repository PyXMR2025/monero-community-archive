---
title: xmrig fails to link if WITH_HTTPD are set to OFF
source_url: https://github.com/xmrig/xmrig/issues/527
author: passnet
assignees: []
labels: []
created_at: '2018-04-09T09:28:37+00:00'
updated_at: '2018-04-10T06:24:09+00:00'
type: issue
status: closed
closed_at: '2018-04-10T06:24:09+00:00'
---

# Original Description
```
[100%] Linking CXX executable xmrig
CMakeFiles/xmrig.dir/src/api/Api.cpp.o: In function `Api::start(xmrig::Controller*)':
Api.cpp:(.text+0x1d): undefined reference to `ApiRouter::ApiRouter(xmrig::Controller*)'
CMakeFiles/xmrig.dir/src/api/Api.cpp.o: In function `Api::exec(xmrig::HttpRequest const&, xmrig::HttpReply&)':
Api.cpp:(.text+0x7c): undefined reference to `ApiRouter::exec(xmrig::HttpRequest const&, xmrig::HttpReply&)'
Api.cpp:(.text+0x91): undefined reference to `ApiRouter::get(xmrig::HttpRequest const&, xmrig::HttpReply&) const'
CMakeFiles/xmrig.dir/src/api/Api.cpp.o: In function `Api::tick(Hashrate const*)':
Api.cpp:(.text+0xb3): undefined reference to `ApiRouter::tick(Hashrate const*)'
CMakeFiles/xmrig.dir/src/api/Api.cpp.o: In function `Api::tick(NetworkState const&)':
Api.cpp:(.text+0xe3): undefined reference to `ApiRouter::tick(NetworkState const&)'
collect2: error: ld returned 1 exit status
CMakeFiles/xmrig.dir/build.make:1162: recipe for target 'xmrig' failed
make[2]: *** [xmrig] Error 1
CMakeFiles/Makefile2:67: recipe for target 'CMakeFiles/xmrig.dir/all' failed
make[1]: *** [CMakeFiles/xmrig.dir/all] Error 2
Makefile:83: recipe for target 'all' failed
make: *** [all] Error 2

```

# Discussion History
## passnet | 2018-04-10T06:24:09+00:00
Duplicate of #502, sorry.

# Action History
- Created by: passnet | 2018-04-09T09:28:37+00:00
- Closed at: 2018-04-10T06:24:09+00:00
