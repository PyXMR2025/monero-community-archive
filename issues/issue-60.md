---
title: FreeBSD super pages support
source_url: https://github.com/xmrig/xmrig/issues/60
author: vcambur
assignees: []
labels:
- help wanted
created_at: '2017-08-15T07:50:06+00:00'
updated_at: '2017-10-22T20:26:14+00:00'
type: issue
status: closed
closed_at: '2017-10-22T20:26:14+00:00'
---

# Original Description
Hi,

Is it possible to add super pages support for FreeBSD (similar to huge pages in Linux) ?
Will there be any benefit ?
Currently without some hacks xmrig won't even compile on FreeBSD

Thanks again for your hard work

# Discussion History
## xmrig | 2017-08-15T22:31:45+00:00
Sorry I has zero knowledge about FreeBSD, pull request with fixed build are welcome. If you make short tutorial how build miner on FreeBSD I appreciate that, will try make it. Thank you.

## lisergey | 2017-08-28T14:25:52+00:00
I've tried to compile XMRig on FreeBSD 11.1 with no luck.
But it runs with linux_base-c7 compaitibilty emulator with minor bugs, like refusing to run background if no-root, and ignoring kill signal.
I'd like to help with testing on FreeBSD.

## vcambur | 2017-08-28T14:48:38+00:00
I was able to compile with gcc5 after some tweaks and hacks regarding huge pages and cpu affinity (I have no real knowledge of FreeBSD internals). 
I want to try to compile with gcc7 and need to find some time to make it go on github..



## lisergey | 2017-10-02T13:06:19+00:00
Hello @vcambur !
any progress on how-to?
How can I help you with it?

## vcambur | 2017-10-19T11:59:59+00:00
Hi,

patch agains master for FreeBSD (tested on 10.3-RELEASE both with clang and gcc7) attached.
to apply after git clone or unzip, cd to xmrig directory and do
`patch -p1 < fbsd-xmrig.txt`
then (per wiki)
`mkdir build`
`cd build`
(for clang)
`cmake -DUV_LIBRARY=/usr/local/lib/libuv.a -DMHD_LIBRARY=/usr/local/lib/libmicrohttpd.a ..`
(for gcc7)
`cmake -DUV_LIBRARY=/usr/local/lib/libuv.a -DMHD_LIBRARY=/usr/local/lib/libmicrohttpd.a -DCMAKE_C_COMPILER=gcc7 -DCMAKE_CXX_COMPILER=g++7 ..`

@xmrig, can you please review the patch
[fbsd-xmrig.txt](https://github.com/xmrig/xmrig/files/1398218/fbsd-xmrig.txt)

![zz](https://user-images.githubusercontent.com/10867337/31770000-91036dea-b4de-11e7-8c38-a8a7e6c2788c.png)


## xmrig | 2017-10-19T13:17:52+00:00
Better if you make this path via pull request, your name also will be appear in commit history.
Anyway thank you, I will check it tomorrow.

# Action History
- Created by: vcambur | 2017-08-15T07:50:06+00:00
- Closed at: 2017-10-22T20:26:14+00:00
