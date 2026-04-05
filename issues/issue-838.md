---
title: cannot build on VC2015, Win10
source_url: https://github.com/xmrig/xmrig/issues/838
author: cloudszhang1979
assignees: []
labels:
- question
created_at: '2018-10-23T04:06:09+00:00'
updated_at: '2018-10-25T02:41:39+00:00'
type: issue
status: closed
closed_at: '2018-10-25T02:41:39+00:00'
---

# Original Description
it seems like ws2def.h is conflict with winsock.h. But I don't know which file includes this two headers.
version is xmrig-2.8.1.

error message is :
3>  Client.cpp
3>C:\Program Files (x86)\Windows Kits\8.1\Include\shared\ws2def.h(100): warning C4005: 'AF_IPX': macro redefinition
3>  C:\Program Files (x86)\Windows Kits\8.1\Include\um\winsock.h(452): note: see previous definition of 'AF_IPX'
3>C:\Program Files (x86)\Windows Kits\8.1\Include\shared\ws2def.h(140): warning C4005: 'AF_MAX': macro redefinition
3>  C:\Program Files (x86)\Windows Kits\8.1\Include\um\winsock.h(471): note: see previous definition of 'AF_MAX'
3>C:\Program Files (x86)\Windows Kits\8.1\Include\shared\ws2def.h(177): warning C4005: 'SO_DONTLINGER': macro redefinition
3>  C:\Program Files (x86)\Windows Kits\8.1\Include\um\winsock.h(394): note: see previous definition of 'SO_DONTLINGER'
3>C:\Program Files (x86)\Windows Kits\8.1\Include\shared\ws2def.h(221): error C2011: 'sockaddr': 'struct' type redefinition
3>  C:\Program Files (x86)\Windows Kits\8.1\Include\um\winsock.h(1002): note: see declaration of 'sockaddr'
3>C:\Program Files (x86)\Windows Kits\8.1\Include\shared\ws2def.h(421): error C2059: syntax error: 'constant'
3>C:\Program Files (x86)\Windows Kits\8.1\Include\shared\ws2def.h(421): error C3805: 'constant': unexpected token, expected either '}' or a ','

# Discussion History
## xmrig | 2018-10-24T02:59:15+00:00
Something very wrong with your Visual Studio installation, did you modify the source or build custom libraries for example libuv?
Thank you.

## cloudszhang1979 | 2018-10-24T04:03:35+00:00
> Something very wrong with your Visual Studio installation, did you modify the source or build custom libraries for example libuv?
> Thank you.

Thank you verymuch.
I use the libuv and microhttpd from https://github.com/xmrig/xmrig-deps/releases
I didn't modify the source, and use CMake GUI to generate solution and project files.

if it is the problem of environment, I can try to build the project on another PC again now. Thank you.

## cloudszhang1979 | 2018-10-25T02:41:17+00:00
when disable the build options of "With Httpd", "With TLS" in CMake GUI, It can generate a good project file.
Thanks.

# Action History
- Created by: cloudszhang1979 | 2018-10-23T04:06:09+00:00
- Closed at: 2018-10-25T02:41:39+00:00
