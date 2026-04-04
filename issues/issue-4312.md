---
title: NetBSD 8 amd64 miniupnpc non-build
source_url: https://github.com/monero-project/monero/issues/4312
author: thomasvaughan
assignees: []
labels: []
created_at: '2018-08-29T15:08:05+00:00'
updated_at: '2018-09-01T04:20:04+00:00'
type: issue
status: closed
closed_at: '2018-09-01T04:20:04+00:00'
---

# Original Description
Build fails with this message:

    [  4%] Building C object external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-static.dir/minissdpc.c.o
    /home/t/usr/src/monero/external/miniupnp/miniupnpc/minissdpc.c: In function ‘ssdpDiscoverDevices’:
    /home/t/usr/src/monero/external/miniupnp/miniupnpc/minissdpc.c:673:18: error: storage size of ‘ifr’ isn’t known
         struct ifreq ifr;
                      ^
    /home/t/usr/src/monero/external/miniupnp/miniupnpc/minissdpc.c:675:40: error: ‘IFNAMSIZ’ undeclared (first use in this function)
         strncpy(ifr.ifr_name, multicastif, IFNAMSIZ);
                                            ^
It's not obvious to me whether or not it _should_ be trying to build miniupnpc (or using an installed miniupnpc as in FreeBSD?). There's already a [miniupnc installed through the package management system](http://cdn.netbsd.org/pub/pkgsrc/current/pkgsrc/net/miniupnpc/) (pkgsrc):-

    $ pkg_info -L miniupnpc
    Information for miniupnpc-2.0nb1:
    
    Files:
    /usr/pkg/bin/external-ip
    /usr/pkg/bin/upnpc
    /usr/pkg/include/miniupnpc/igd_desc_parse.h
    /usr/pkg/include/miniupnpc/miniupnpc.h
    /usr/pkg/include/miniupnpc/miniupnpc_declspec.h
    /usr/pkg/include/miniupnpc/miniupnpctypes.h
    /usr/pkg/include/miniupnpc/miniwget.h
    /usr/pkg/include/miniupnpc/portlistingparse.h
    /usr/pkg/include/miniupnpc/upnpcommands.h
    /usr/pkg/include/miniupnpc/upnpdev.h
    /usr/pkg/include/miniupnpc/upnperrors.h
    /usr/pkg/include/miniupnpc/upnpreplyparse.h
    /usr/pkg/lib/libminiupnpc.a
    /usr/pkg/lib/libminiupnpc.so
    /usr/pkg/lib/libminiupnpc.so.16
    /usr/pkg/man/man3/miniupnpc.3
    
The build was started with `make CMAKE_C_FLAGS="-I/usr/pkg/include -L/usr/pkg/lib -Wl,-R/usr/pkg/lib" CMAKE_CXX_FLAGS="-I/usr/pkg/include -L/usr/pkg/lib -Wl,-R/usr/pkg/lib"`, and the pkgsrc system's miniupnc was discovered by the Monero build but not used:-

    -- Found MiniUPnPc: /usr/pkg/include/miniupnpc  
    -- Found miniupnpc API version 16
    -- Using in-tree miniupnpc
   


# Discussion History
## moneromooo-monero | 2018-08-29T16:55:45+00:00
AFAIK, miniupnpc was restricted to the in tree version due to upstream releases being very few/late after security bugs are patched.


## thomasvaughan | 2018-08-29T17:56:35+00:00
This runs without errors:-

`cp -pR external/miniupnp/miniupnpc ./ && cd miniupnpc && gmake`

Running `make` in the copied miniupnpc directory (_i.e._ BSD _make_, not GNU _make_) generates errors,  but they're just down to BSD _make_ not liking GNU makefiles --- _i.e._ different from the "storage size of ‘ifr’ isn't known" error. Using `gmake` rather than `make` in the Monero build doesn't change anything.

## moneromooo-monero | 2018-08-30T13:17:17+00:00
Possibly something to do with defines at build time, such as _GNU_SOURCE etc.

## thomasvaughan | 2018-09-01T04:17:09+00:00
Fixed by adding to external/CMakeLists.txt:-

    if(CMAKE_SYSTEM_NAME MATCHES "NetBSD")
            set_property(TARGET libminiupnpc-static APPEND_STRING PROPERTY COMPILE_FLAGS " -D_NETBSD_SOURCE")
    endif()

Starting the build with BSD `make` is OK.

# Action History
- Created by: thomasvaughan | 2018-08-29T15:08:05+00:00
- Closed at: 2018-09-01T04:20:04+00:00
