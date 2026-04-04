---
title: miniupnpc not static upnpDiscover change
source_url: https://github.com/monero-project/monero/issues/480
author: perl5577
assignees: []
labels: []
created_at: '2015-11-06T21:09:37+00:00'
updated_at: '2017-08-12T14:06:12+00:00'
type: issue
status: closed
closed_at: '2017-08-12T14:06:12+00:00'
---

# Original Description
/build/bitmonero-git/src/bitmonero/src/p2p/net_node.inl:446:69: error: too few arguments to function 'UPNPDev\* upnpDiscover(int, const char_, const char_, int, int, unsigned char, int_)'
   UPNPDev_ deviceList = upnpDiscover(1000, NULL, NULL, 0, 0, &result);
                                                                     ^
In file included from /build/bitmonero-git/src/bitmonero/src/p2p/net_node.inl:58:0,
                 from /build/bitmonero-git/src/bitmonero/src/p2p/net_node.h:288,
                 from /build/bitmonero-git/src/bitmonero/src/rpc/core_rpc_server.h:39,
                 from /build/bitmonero-git/src/bitmonero/src/rpc/core_rpc_server.cpp:35:

Change format for upnpDiscover if MINIUPNPC_API_VERSION >= 14
https://github.com/bitcoin/bitcoin/commit/9f3e48e5219a09b5ddfd6883d1f0498910eff4b6.patch

From
upnpDiscover(int delay, const char \* multicastif,
             const char \* minissdpdsock, int sameport,
             int ipv6,
             int \* error)

To
upnpDiscover(int delay, const char \* multicastif,
             const char \* minissdpdsock, int localport,
             int ipv6, unsigned char ttl,
             int \* error)

Sorry , I am not competent for code change in CMake and .inl


# Discussion History
## warptangent | 2015-11-08T13:26:51+00:00
Addressed in #422.


## perl5577 | 2015-11-11T13:34:48+00:00
Work perfectly :)
I can submited PKGBUILD to AUR archlinux ans close issues
https://aur.archlinux.org/packages/bitmonero-git


## ghost | 2016-09-15T19:58:23+00:00
Hi @perl5577 is this still an issue for you or can this be closed?


## moneromooo-monero | 2017-08-12T14:03:39+00:00
+resolved

# Action History
- Created by: perl5577 | 2015-11-06T21:09:37+00:00
- Closed at: 2017-08-12T14:06:12+00:00
