---
title: miniupnpc minissdpc ssdpDiscoverDevices errors on DragonFlyBSD 5.2
source_url: https://github.com/monero-project/monero/issues/4583
author: danrmiller
assignees: []
labels: []
created_at: '2018-10-13T21:02:15+00:00'
updated_at: '2019-06-15T17:31:14+00:00'
type: issue
status: closed
closed_at: '2019-06-15T17:31:14+00:00'
---

# Original Description
I don't know if I should raise this in the miniupnp instead. Using miniupnp/monero 6b9b73a

https://build.getmonero.org/builders/monero-static-dragonflybsd-amd64/builds/2670/steps/compile/logs/stdio

```
[  5%] Building C object external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-static.dir/minissdpc.c.o
/home/buildbot/builder/monero-static-dragonflybsd-amd64/build/external/miniupnp/miniupnpc/minissdpc.c: In function 'ssdpDiscoverDevices':
/home/buildbot/builder/monero-static-dragonflybsd-amd64/build/external/miniupnp/miniupnpc/minissdpc.c:673:18: error: storage size of 'ifr' isn't known
     struct ifreq ifr;
                  ^
/home/buildbot/builder/monero-static-dragonflybsd-amd64/build/external/miniupnp/miniupnpc/minissdpc.c:675:40: error: 'IFNAMSIZ' undeclared (first use in this function)
     strncpy(ifr.ifr_name, multicastif, IFNAMSIZ);
                                        ^
/home/buildbot/builder/monero-static-dragonflybsd-amd64/build/external/miniupnp/miniupnpc/minissdpc.c:675:40: note: each undeclared identifier is reported only once for each function it appears in
In file included from /usr/include/sys/ttycom.h:42:0,
                 from /usr/include/sys/ioctl.h:45,
                 from /home/buildbot/builder/monero-static-dragonflybsd-amd64/build/external/miniupnp/miniupnpc/minissdpc.c:70:
/home/buildbot/builder/monero-static-dragonflybsd-amd64/build/external/miniupnp/miniupnpc/minissdpc.c:677:20: error: invalid application of 'sizeof' to incomplete type 'struct ifreq'
     if(ioctl(sudp, SIOCGIFADDR, &ifr, &ifrlen) < 0)
                    ^
gmake[3]: *** [external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-static.dir/build.make:115: external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-static.dir/minissdpc.c.o] Error 1
```

# Discussion History
## moneromooo-monero | 2018-10-17T10:17:17+00:00
Can you add "VERBOSE=1" to the make command line, and check if -D_BSD_SOURCE is included ?

## thomasvaughan | 2018-10-19T23:04:48+00:00
NetBSD had pretty much the same error until  #4326 cured it by adding a -D_NETBSD_SOURCE to external/CMakeLists.txt.

But the fix may become unnecessary if a newer miniupnp is used, if I'm inferring correctly from
http://cvsweb.netbsd.org/bsdweb.cgi/pkgsrc/net/miniupnpc/patches/patch-Makefile.diff?r1=1.2&r2=1.3&f=h

## moneromooo-monero | 2018-10-19T23:25:52+00:00
Monero uses a CMakeLists.txt to build it using cmake, so any patch in the Makefile would be ignored.

## moneromooo-monero | 2019-06-15T10:49:14+00:00
Fixed in https://github.com/monero-project/monero/pull/5616

+resolved

# Action History
- Created by: danrmiller | 2018-10-13T21:02:15+00:00
- Closed at: 2019-06-15T17:31:14+00:00
