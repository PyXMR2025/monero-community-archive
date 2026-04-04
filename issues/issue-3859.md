---
title: Compiling from release tarball fails due to miniupnpc-static
source_url: https://github.com/monero-project/monero/issues/3859
author: sammy007
assignees: []
labels: []
created_at: '2018-05-25T11:20:17+00:00'
updated_at: '2018-11-07T14:49:25+00:00'
type: issue
status: closed
closed_at: '2018-11-07T14:49:25+00:00'
---

# Original Description
```
-- Found MiniUPnPc: /usr/include/miniupnpc
-- Found miniupnpc API version 10
-- Using in-tree miniupnpc
CMake Error at external/CMakeLists.txt:42 (add_subdirectory):
  add_subdirectory given source "miniupnp/miniupnpc" which is not an existing
  directory.


CMake Error at external/CMakeLists.txt:44 (set_property):
  set_property could not find TARGET libminiupnpc-static.  Perhaps it has not
  yet been created.


CMake Error at external/CMakeLists.txt:48 (set_property):
  set_property could not find TARGET libminiupnpc-static.  Perhaps it has not
  yet been created.
```

Happened with 0.12.1.0 point release.

```
dpkg -l| grep upnpc
ii  libminiupnpc-dev                       1.9.20140610-2ubuntu2.16.04.2              amd64        UPnP IGD client lightweight library development files
ii  libminiupnpc10:amd64                   1.9.20140610-2ubuntu2.16.04.2              amd64        UPnP IGD client lightweight library
ii  miniupnpc                              1.9.20140610-2ubuntu2.16.04.2              amd64        UPnP IGD client lightweight library client
```

Ubuntu 16.04.

# Discussion History
## sammy007 | 2018-05-25T11:22:02+00:00
I understand that github's stupid tarball releases does not contain submodules, but why not fallback to miniupnpc from the system?

## moneromooo-monero | 2018-05-25T11:23:47+00:00
AFAIK, because there are security bugs which aren't released.

## sammy007 | 2018-05-25T11:24:14+00:00
Just tested v0.12.0.0 and it compiles with system libraries, seems broken in this new point release or is there any special reason for it?

## sammy007 | 2018-05-25T11:26:06+00:00
@moneromooo-monero ah. Imo makes sense to get rid of auto tarballs then since they are poorly implemented.

## hyc | 2018-05-25T15:31:32+00:00
and on older OSs the static libs aren't compiled -fPIC, so they can't be used anyway.

## anonimal | 2018-05-25T20:55:17+00:00
>why not fallback to miniupnpc from the system?

See https://github.com/monero-project/monero/issues/3862#issuecomment-392183195, and just do a recursive git clone / check out tag. The repo is a development repo so git should be easily attainable. If people don't want to do development then they can simply use the release binaries.

>Imo makes sense to get rid of auto tarballs then since they are poorly implemented.

Yes. There should be a github/github ticket somewhere for this.

## ilovezfs | 2018-05-26T00:05:12+00:00
The automatically available tarballs are just a thin wrapper around the `git archive` command. They cannot be disabled. If you want the submodules available in a source tarball, a separate source release tarball can be manually uploaded to the release in the GUI, which is pretty common. For example, see

https://github.com/zyedidia/micro/releases/tag/v1.4.0
and the attached
https://github.com/zyedidia/micro/releases/download/v1.4.0/micro-1.4.0-src.tar.gz

It's also perfectly valid to expect people to use the Git clone, although a complete source tarball can help with preventing issues such as the current one and is a nice convenience.

## moneromooo-monero | 2018-10-25T10:06:37+00:00
Fixed in 0.13.0.4 



## moneromooo-monero | 2018-11-07T14:24:27+00:00
+resolved

# Action History
- Created by: sammy007 | 2018-05-25T11:20:17+00:00
- Closed at: 2018-11-07T14:49:25+00:00
