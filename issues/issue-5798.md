---
title: 'external/miniupnp: Build fails on SmartOS'
source_url: https://github.com/monero-project/monero/issues/5798
author: kayront
assignees: []
labels: []
created_at: '2019-08-08T07:34:51+00:00'
updated_at: '2019-08-10T14:12:02+00:00'
type: issue
status: closed
closed_at: '2019-08-10T13:46:39+00:00'
---

# Original Description
I'm trying to get monerod to compile on a SunOS system. Compilation right now fails very early on:

```
$ make
[  2%] Built target generate_translations_header
[  2%] Building C object external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-static.dir/minissdpc.c.o
/home/admin/src/monero/external/miniupnp/miniupnpc/minissdpc.c: In function 'ssdpDiscoverDevices':
/home/admin/src/monero/external/miniupnp/miniupnpc/minissdpc.c:673:18: error: storage size of 'ifr' isn't known
     struct ifreq ifr;
                  ^~~
/home/admin/src/monero/external/miniupnp/miniupnpc/minissdpc.c:675:40: error: 'IFNAMSIZ' undeclared (first use in this function); did you mean 'IF_NAMESIZE'?                                                                                
     strncpy(ifr.ifr_name, multicastif, IFNAMSIZ);
                                        ^~~~~~~~
                                        IF_NAMESIZE
/home/admin/src/monero/external/miniupnp/miniupnpc/minissdpc.c:675:40: note: each undeclared identifier is reported only once for each function it appears in                                                                                
/home/admin/src/monero/external/miniupnp/miniupnpc/minissdpc.c:677:8: warning: implicit declaration of function 'ioctl' [-Wimplicit-function-declaration]                                                                                    
     if(ioctl(sudp, SIOCGIFADDR, &ifr, &ifrlen) < 0)
        ^~~~~
In file included from /usr/include/sys/sockio.h:46,
                 from /home/admin/src/monero/external/miniupnp/miniupnpc/minissdpc.c:72:
/home/admin/src/monero/external/miniupnp/miniupnpc/minissdpc.c:677:20: error: invalid application of 'sizeof' to incomplete type 'struct ifreq'                                                                                              
     if(ioctl(sudp, SIOCGIFADDR, &ifr, &ifrlen) < 0)
                    ^~~~~~~~~~~
make[2]: *** [external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-static.dir/build.make:115: external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-static.dir/minissdpc.c.o] Error 1                                                           
make[1]: *** [CMakeFiles/Makefile2:152: external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-static.dir/all] Error 2
make: *** [Makefile:141: all] Error 2
```
I've also tried to compile the original miniupnp***d*** from upstream but it fails with [different errors](https://github.com/miniupnp/miniupnp/issues/391).

miniupnp***c*** from upstream compiled alright:

> ~/src/miniupnp/miniupnpc]$ make
```
/bin/sh updateminiupnpcstrings.sh
Detected OS [SunOS] version [5.11]
MiniUPnPc version [2.1]
setting OS_STRING macro value to SunOS/5.11 in miniupnpcstrings.h.
setting MINIUPNPC_VERSION_STRING macro value to 2.1 in miniupnpcstrings.h.
cc -fPIC -O -Wall -W -Wstrict-prototypes -fno-common -DMINIUPNPC_SET_SOCKET_TIMEOUT -DMINIUPNPC_GET_SRC_ADDR -D_BSD_SOURCE -D_DEFAULT_SOURCE -D_XOPEN_SOURCE=600 -D__EXTENSIONS__ -std=c99   -c -o miniwget.o miniwget.c
cc -fPIC -O -Wall -W -Wstrict-prototypes -fno-common -DMINIUPNPC_SET_SOCKET_TIMEOUT -DMINIUPNPC_GET_SRC_ADDR -D_BSD_SOURCE -D_DEFAULT_SOURCE -D_XOPEN_SOURCE=600 -D__EXTENSIONS__ -std=c99   -c -o minixml.o minixml.c
cc -fPIC -O -Wall -W -Wstrict-prototypes -fno-common -DMINIUPNPC_SET_SOCKET_TIMEOUT -DMINIUPNPC_GET_SRC_ADDR -D_BSD_SOURCE -D_DEFAULT_SOURCE -D_XOPEN_SOURCE=600 -D__EXTENSIONS__ -std=c99   -c -o igd_desc_parse.o igd_desc_parse.c
cc -fPIC -O -Wall -W -Wstrict-prototypes -fno-common -DMINIUPNPC_SET_SOCKET_TIMEOUT -DMINIUPNPC_GET_SRC_ADDR -D_BSD_SOURCE -D_DEFAULT_SOURCE -D_XOPEN_SOURCE=600 -D__EXTENSIONS__ -std=c99   -c -o minisoap.o minisoap.c
cc -fPIC -O -Wall -W -Wstrict-prototypes -fno-common -DMINIUPNPC_SET_SOCKET_TIMEOUT -DMINIUPNPC_GET_SRC_ADDR -D_BSD_SOURCE -D_DEFAULT_SOURCE -D_XOPEN_SOURCE=600 -D__EXTENSIONS__ -std=c99   -c -o miniupnpc.o miniupnpc.c
cc -fPIC -O -Wall -W -Wstrict-prototypes -fno-common -DMINIUPNPC_SET_SOCKET_TIMEOUT -DMINIUPNPC_GET_SRC_ADDR -D_BSD_SOURCE -D_DEFAULT_SOURCE -D_XOPEN_SOURCE=600 -D__EXTENSIONS__ -std=c99   -c -o upnpreplyparse.o upnpreplyparse.c
cc -fPIC -O -Wall -W -Wstrict-prototypes -fno-common -DMINIUPNPC_SET_SOCKET_TIMEOUT -DMINIUPNPC_GET_SRC_ADDR -D_BSD_SOURCE -D_DEFAULT_SOURCE -D_XOPEN_SOURCE=600 -D__EXTENSIONS__ -std=c99   -c -o upnpcommands.o upnpcommands.c
cc -fPIC -O -Wall -W -Wstrict-prototypes -fno-common -DMINIUPNPC_SET_SOCKET_TIMEOUT -DMINIUPNPC_GET_SRC_ADDR -D_BSD_SOURCE -D_DEFAULT_SOURCE -D_XOPEN_SOURCE=600 -D__EXTENSIONS__ -std=c99   -c -o upnperrors.o upnperrors.c
cc -fPIC -O -Wall -W -Wstrict-prototypes -fno-common -DMINIUPNPC_SET_SOCKET_TIMEOUT -DMINIUPNPC_GET_SRC_ADDR -D_BSD_SOURCE -D_DEFAULT_SOURCE -D_XOPEN_SOURCE=600 -D__EXTENSIONS__ -std=c99   -c -o connecthostport.o connecthostport.c
cc -fPIC -O -Wall -W -Wstrict-prototypes -fno-common -DMINIUPNPC_SET_SOCKET_TIMEOUT -DMINIUPNPC_GET_SRC_ADDR -D_BSD_SOURCE -D_DEFAULT_SOURCE -D_XOPEN_SOURCE=600 -D__EXTENSIONS__ -std=c99   -c -o portlistingparse.o portlistingparse.c
cc -fPIC -O -Wall -W -Wstrict-prototypes -fno-common -DMINIUPNPC_SET_SOCKET_TIMEOUT -DMINIUPNPC_GET_SRC_ADDR -D_BSD_SOURCE -D_DEFAULT_SOURCE -D_XOPEN_SOURCE=600 -D__EXTENSIONS__ -std=c99   -c -o receivedata.o receivedata.c
cc -fPIC -O -Wall -W -Wstrict-prototypes -fno-common -DMINIUPNPC_SET_SOCKET_TIMEOUT -DMINIUPNPC_GET_SRC_ADDR -D_BSD_SOURCE -D_DEFAULT_SOURCE -D_XOPEN_SOURCE=600 -D__EXTENSIONS__ -std=c99   -c -o upnpdev.o upnpdev.c
cc -fPIC -O -Wall -W -Wstrict-prototypes -fno-common -DMINIUPNPC_SET_SOCKET_TIMEOUT -DMINIUPNPC_GET_SRC_ADDR -D_BSD_SOURCE -D_DEFAULT_SOURCE -D_XOPEN_SOURCE=600 -D__EXTENSIONS__ -std=c99   -c -o minissdpc.o minissdpc.c
ar crs libminiupnpc.a miniwget.o minixml.o igd_desc_parse.o minisoap.o miniupnpc.o upnpreplyparse.o upnpcommands.o upnperrors.o connecthostport.o portlistingparse.o receivedata.o upnpdev.o minissdpc.o
cc -fPIC -O -Wall -W -Wstrict-prototypes -fno-common -DMINIUPNPC_SET_SOCKET_TIMEOUT -DMINIUPNPC_GET_SRC_ADDR -D_BSD_SOURCE -D_DEFAULT_SOURCE -D_XOPEN_SOURCE=600 -D__EXTENSIONS__ -std=c99   -c -o upnpc.o upnpc.c
cc  -o upnpc-static upnpc.o libminiupnpc.a  -lsocket -lnsl -lresolv
cc -fPIC -O -Wall -W -Wstrict-prototypes -fno-common -DMINIUPNPC_SET_SOCKET_TIMEOUT -DMINIUPNPC_GET_SRC_ADDR -D_BSD_SOURCE -D_DEFAULT_SOURCE -D_XOPEN_SOURCE=600 -D__EXTENSIONS__ -std=c99   -c -o listdevices.o listdevices.c
cc   listdevices.o libminiupnpc.a  -lsocket -lnsl -lresolv -o listdevices
cc -shared  -Wl,-soname,libminiupnpc.so.17 -o libminiupnpc.so miniwget.o minixml.o igd_desc_parse.o minisoap.o miniupnpc.o upnpreplyparse.o upnpcommands.o upnperrors.o connecthostport.o portlistingparse.o receivedata.o upnpdev.o minissdpc.o
cc  -o upnpc-shared upnpc.o libminiupnpc.so  -lsocket -lnsl -lresolv
```



# Discussion History
## thomasvaughan | 2019-08-09T18:26:08+00:00
SmartOS uses pkgsrc as its package manager, so [the pkgsrc Makefile for miniupnpc](http://ftp.netbsd.org/pub/pkgsrc/current/pkgsrc/net/miniupnpc/Makefile) could give you some hints; especially

    CPPFLAGS.SunOS+=	-D__EXTENSIONS__
    LDFLAGS.SunOS+=		-lsocket -lnsl

Do these flags need to be supplied in Monero's `external/CMakeLists.txt`? I'm not fluent in cmake syntax , but perhaps something like

    if(CMAKE_SYSTEM_NAME MATCHES "SunOS")
    	set_property(TARGET libminiupnpc-static APPEND_STRING PROPERTY COMPILE_FLAGS "-D__EXTENSIONS__")
    	set_property(TARGET libminiupnpc-static APPEND_STRING PROPERTY CMAKE_STATIC_LINKER_FLAGS "-lsocket -lnsl")
    endif()


## kayront | 2019-08-10T07:04:09+00:00
It seems you are correct, I commented what I could find in the upstream Makefile about SunOS (sun there) and building the upstream code fails with the same error.

I tried adding your suggestion to external/CmakeLists.txt to no avail.

But definitely to convince it to do that is the right thing.

However it *is* reading the file properly, adding -bogus there makes compilation fail with

> cc: error: unrecognized command line option '-bogus'

Here is what I have at the moment (still failing with the same error)

```
if(CMAKE_SYSTEM_NAME MATCHES "(SunOS|Solaris)")
        set_property(TARGET libminiupnpc-static APPEND_STRING PROPERTY COMPILE_FLAGS "-D__EXTENSIONS__ -std=c99")
        set_property(TARGET libminiupnpc-static APPEND_STRING PROPERTY CMAKE_STATIC_LINKER_FLAGS "-lsocket -lnsl -lresolv")
endif()
```

This seems to mirror the upstream Makefile, which reads:

```
ifneq (, $(findstring sun, $(OS)))
  LDLIBS=-lsocket -lnsl -lresolv
  CFLAGS += -D__EXTENSIONS__
  CFLAGS += -std=c99
endif
```

I've *make clean* in the root dir, external/ and external/miniupnp/miniupnc and nuked the ccache cache - it's still not working.

Bet this is trivial to sort out for someone *actually* familiar with C++.

I'll be happy to apply any solutions and continue trying to build monerod for SunOS.

## thomasvaughan | 2019-08-10T09:57:42+00:00
@kayront When you ran the `updateminiupnpcstrings.sh` shell script, it used some extra compiler options (for example, -D_BSD_SOURCE). Are some/all of those extra options required in `external/CMakeLists.txt`?

## kayront | 2019-08-10T13:46:24+00:00
After experimenting further, this is resolved by having a whitespace after the first " here:  "-D__EXTENSIONS__ -std=c99" and here: 

 "-lsocket -lnsl -lresolv"

```
diff --git a/external/CMakeLists.txt b/external/CMakeLists.txt
index bc4344b3..afc3ffdf 100644
--- a/external/CMakeLists.txt
+++ b/external/CMakeLists.txt
@@ -48,6 +48,10 @@ endif()
 if(CMAKE_SYSTEM_NAME MATCHES "NetBSD")
        set_property(TARGET libminiupnpc-static APPEND_STRING PROPERTY COMPILE_FLAGS " -D_NETBSD_SOURCE")
 endif()
+if(CMAKE_SYSTEM_NAME MATCHES "(SunOS|Solaris)")
+       set_property(TARGET libminiupnpc-static APPEND_STRING PROPERTY COMPILE_FLAGS " -D__EXTENSIONS__ -std=c99")
+       set_property(TARGET libminiupnpc-static APPEND_STRING PROPERTY CMAKE_STATIC_LINKER_FLAGS " -lsocket -lnsl -lresolv")                                                                                                                 
+endif()

 set(UPNP_LIBRARIES "libminiupnpc-static" PARENT_SCOPE)

```

I'll report any further compilation errors, we can close this one. Thanks for the help!

## thomasvaughan | 2019-08-10T14:12:02+00:00
When you write your pull request, you could match the coding style used in other CMakeLists.txt files by putting your additions as an `elseif()` *within* the existing  `if()` ... `endif()`. See #5777 for an example.

# Action History
- Created by: kayront | 2019-08-08T07:34:51+00:00
- Closed at: 2019-08-10T13:46:39+00:00
