---
title: make debug fails on FreeBSD i386
source_url: https://github.com/monero-project/monero/issues/4119
author: marmulak
assignees: []
labels: []
created_at: '2018-07-09T15:39:52+00:00'
updated_at: '2018-12-20T14:27:42+00:00'
type: issue
status: closed
closed_at: '2018-12-20T14:27:42+00:00'
---

# Original Description
CPU: Intel(R) Atom(TM) CPU N270   @ 1.60GHz (1596.03-MHz 686-class CPU)
OS version: FreeBSD 11.2-RELEASE #0 r335510: Fri Jun 22 04:09:26 UTC 2018     root@releng2.nyi.freebsd.org:/usr/obj/usr/src/sys/GENERIC
System architecture: i386

Build log: http://paste.debian.net/hidden/e9a02625/

I accidentally encountered this error when attempting to solve another issue I was having to get Monero to build on this system. Monero now builds and runs, but debug cannot build due to wallet2.cpp.o being (probably) too large for the linker to handle. Talked to some devs about it, apparently a similar issue had been encountered on 32-bit Windows.

I hope to get this working so I can file some good crash reports. ;)

# Discussion History
## moneromooo-monero | 2018-09-12T09:56:35+00:00
Any luck ? :)

# Action History
- Created by: marmulak | 2018-07-09T15:39:52+00:00
- Closed at: 2018-12-20T14:27:42+00:00
