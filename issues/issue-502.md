---
title: 2.6.0 dev fails to compile if building with -DWITH_HTTPD=OFF
source_url: https://github.com/xmrig/xmrig/issues/502
author: plavirudar
assignees: []
labels:
- bug
created_at: '2018-04-05T00:50:40+00:00'
updated_at: '2018-04-06T17:45:34+00:00'
type: issue
status: closed
closed_at: '2018-04-06T17:45:34+00:00'
---

# Original Description
Without that flag, the compile works as expected. 

With the flag, the compile fails with the following error: 

```
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
## JustHoldit | 2018-04-06T16:59:00+00:00
I had the same problem on SUSE linux. It compiles file without -DWITH_HTTPD=OFF


## xmrig | 2018-04-06T17:45:34+00:00
Fixed.

# Action History
- Created by: plavirudar | 2018-04-05T00:50:40+00:00
- Closed at: 2018-04-06T17:45:34+00:00
