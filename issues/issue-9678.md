---
title: 'v0.18.3.4 FTBFS: Arch Linux'
source_url: https://github.com/monero-project/monero/issues/9678
author: Dormouse665
assignees: []
labels:
- reproduction needed
created_at: '2025-01-04T14:06:41+00:00'
updated_at: '2025-04-09T09:51:32+00:00'
type: issue
status: closed
closed_at: '2025-04-09T09:51:32+00:00'
---

# Original Description
```
[dormouse@psappho monero]$ git clean -fxd
Removing build/
[dormouse@psappho monero]$ mkdir build
[dormouse@psappho monero]$ cd build/
[dormouse@psappho build]$ cmake -Wno-dev .. > cmake.log 2>&1
[dormouse@psappho build]$ make -j3 > make.log 2>&1
[dormouse@psappho build]$ git status
HEAD detached at v0.18.3.4
nothing to commit, working tree clean
```
cmake.log:
https://plch.xyz/static/base_app/cmake.log

make.log:
https://plch.xyz/static/base_app/make.log


# Discussion History
## 0xFFFC0000 | 2025-01-04T16:17:23+00:00
This looks like uuid related error. 

I was under impression that we merged a fix [1]. 

This was due to (breaking) update to `boost::uuid` in latest boost. I assume you are using a recent version of boost. 

Let me double check it. 

```
home/dormouse/gits/monero/contrib/epee/include/span.h:165:34: error: static assertion failed: source type may have padding
  165 |     static_assert(!has_padding<T>(), "source type may have padding");
      |                    ~~~~~~~~~~~~~~^~
/home/dormouse/gits/monero/contrib/epee/include/span.h:165:34: note: â! epee::has_padding<boost::uuids::uuid>()â evaluates to false
make[2]: *** [src/rpc/CMakeFiles/obj_rpc.dir/build.make:107: src/rpc/CMakeFiles/obj_rpc.dir/core_rpc_server.cpp.o] Error 1
```


1. https://github.com/monero-project/monero/pull/9462

## Dormouse665 | 2025-01-04T17:00:17+00:00
```
$ pacman -Ss boost
extra/boost 1.86.0-4 [installed]
```

## tankf33der | 2025-01-04T20:03:54+00:00

`Repeated`. Monero is safe. 

```
# cat /etc/os-release
NAME="Arch Linux"
PRETTY_NAME="Arch Linux"
ID=arch
BUILD_ID=rolling
VERSION_ID=20241229.0.293060
ANSI_COLOR="38;2;23;147;209"
HOME_URL="https://archlinux.org/"
DOCUMENTATION_URL="https://wiki.archlinux.org/"
SUPPORT_URL="https://bbs.archlinux.org/"
BUG_REPORT_URL="https://gitlab.archlinux.org/groups/archlinux/-/issues"
PRIVACY_POLICY_URL="https://terms.archlinux.org/docs/privacy-policy/"
LOGO=archlinux-logo
# ./monerod --version
Monero 'Fluorine Fermi' (v0.18.3.4-release)
```

just compiled monero on a freshly installed archlinux.


## Dormouse665 | 2025-01-05T07:39:51+00:00
I found the issue.

If I use the top-level Makefile doing
```
$ cd /path/to/git/repo/
$ make
```
It builds well.

It's only when I run
```
$ cmake /path/to/git/repo
$ make
```
That this occurs.

The correct approach seems to prohibit me from building outside the source tree.
Is there another way to reach such a result?

## Dormouse665 | 2025-01-05T07:42:30+00:00
Don't close yet, I have another failure, I pressed `comment` way too soon.

https://plch.xyz/static/base_app/make2.log

## Dormouse665 | 2025-01-05T07:53:55+00:00
I have disabled threads for this one for better readability.

```
-- Configuring done (10.1s)
-- Generating done (1.0s)
-- Build files have been written to: /home/dormouse/gits/monero/build/Linux/_HEAD_detached_at_v0.18.3.4_/release
make[1]: Entering directory '/home/dormouse/gits/monero/build/Linux/_HEAD_detached_at_v0.18.3.4_/release'
[  2%] Built target generate_translations_header
[  5%] Built target libminiupnpc-static
[  5%] Building C object external/miniupnp/miniupnpc/CMakeFiles/upnpc-static.dir/upnpc.c.o
[  5%] Linking C executable upnpc-static
[  5%] Built target upnpc-static
[  7%] Built target libminiupnpc-shared
[  8%] Building C object external/miniupnp/miniupnpc/CMakeFiles/upnpc-shared.dir/upnpc.c.o
[  8%] Linking C executable upnpc-shared
[  8%] Built target upnpc-shared
[  8%] Building C object external/miniupnp/miniupnpc/CMakeFiles/listdevices.dir/listdevices.c.o
/home/dormouse/gits/monero/external/miniupnp/miniupnpc/listdevices.c: In function ‘add_device’:
/home/dormouse/gits/monero/external/miniupnp/miniupnpc/listdevices.c:60:24: error: implicit declaration of function ‘strdup’; did you mean ‘strcmp’? [-Wimplicit-function-declaration]
   60 |         elt->descURL = strdup(dev->descURL);
      |                        ^~~~~~
      |                        strcmp
/home/dormouse/gits/monero/external/miniupnp/miniupnpc/listdevices.c:60:22: error: assignment to ‘char *’ from ‘int’ makes pointer from integer without a cast [-Wint-conversion]
   60 |         elt->descURL = strdup(dev->descURL);
      |                      ^
make[3]: *** [external/miniupnp/miniupnpc/CMakeFiles/listdevices.dir/build.make:79: external/miniupnp/miniupnpc/CMakeFiles/listdevices.dir/listdevices.c.o] Error 1
make[2]: *** [CMakeFiles/Makefile2:1713: external/miniupnp/miniupnpc/CMakeFiles/listdevices.dir/all] Error 2
make[1]: *** [Makefile:146: all] Error 2
make[1]: Leaving directory '/home/dormouse/gits/monero/build/Linux/_HEAD_detached_at_v0.18.3.4_/release'
make: *** [Makefile:103: release-all] Error 2
```

## tankf33der | 2025-01-05T08:04:40+00:00
@Dormouse665 monero is safe. Please, you have to compile monero according to your chosen distro.
Otherwise the distro will "punish" you.

## Dormouse665 | 2025-01-05T08:17:58+00:00
@tankf33der This looks like an issue in the source tree to me.
```
/home/dormouse/gits/monero/external/miniupnp/miniupnpc/listdevices.c:60:24: error: implicit declaration of function ‘strdup’; did you mean ‘strcmp’? [-Wimplicit-function-declaration]
   60 |         elt->descURL = strdup(dev->descURL);
      |                        ^~~~~~
      |                        strcmp
/home/dormouse/gits/monero/external/miniupnp/miniupnpc/listdevices.c:60:22: error: assignment to ‘char *’ from ‘int’ makes pointer from integer without a cast [-Wint-conversion]
   60 |         elt->descURL = strdup(dev->descURL);
      |                      ^
```

## Dormouse665 | 2025-01-05T08:23:32+00:00
I would welcome to get pointed to such instructions though, as I have not found any special instructions for Arch Linux except for dependency package names.

## tankf33der | 2025-01-05T08:30:45+00:00
> I would welcome to get pointed to such instructions though, as I have not found any special instructions for Arch Linux except for dependency package names.

@Dormouse665 
fuh, finally we get to the heart of the matter. 

You must strictly follow the instructions from this [line](https://gitlab.archlinux.org/archlinux/packaging/packages/monero/-/blob/main/PKGBUILD?ref_type=heads#L69) and below, so as not to rack your brain. The maintainer has already done everything for you.



## Dormouse665 | 2025-01-05T08:48:51+00:00
@tankf33der This will probably come across as a rude note, but it's not intended as such and I would like to genuinely ask:

Why does a downstream developer have to maintain a GCC 13 fix, when GCC 14 has already been released?
```
$ gcc --version
gcc (GCC) 14.2.1 20240910
Copyright (C) 2024 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
```

Thank you for the link, this workaround will at least unblock me on my quest to help with testing xmrchat. :)

## tankf33der | 2025-01-05T08:57:40+00:00
@Dormouse665 They have to respect the users who installed the gcc13 package. 

```
Khaos reigns! (c) "Antichrist" movie
```

## Dormouse665 | 2025-01-05T08:59:02+00:00
@tankf33der Well that's not a very polite answer. I would actually be interested in helping out, possibly with a PR, if there's something blocking it somewhere.

## tankf33der | 2025-01-05T09:24:22+00:00
@Dormouse665
I'm sorry to disappoint you, but I don't see a simple answer to your question within the scope of this PR.


## Dormouse665 | 2025-01-05T09:50:14+00:00
@tankf33der
I don't see any PR around.
I also haven't asked for a simple answer within any scope.

Ping me on Matrix (@dormouse:matrix.org) if you really feel that this issue is not the place to discuss this.

I would like to suggest it is, as this is a FTBFS issue for Arch Linux, and using current release of GCC causes the build to fail on that distro.

## selsta | 2025-02-19T17:38:57+00:00
Please try the latest master / release branch. Multiple build fixes have been merged for newer compilers.

## kpcyrd | 2025-04-09T09:50:48+00:00
I think this is now resolved and can be closed, the new 0.18.4.0 monero release builds with latest boost again:

https://gitlab.archlinux.org/archlinux/packaging/packages/monero/-/blob/f89c75d8344d7dfbeda42b34a2b41d871ed4fad5/PKGBUILD

# Action History
- Created by: Dormouse665 | 2025-01-04T14:06:41+00:00
- Closed at: 2025-04-09T09:51:32+00:00
