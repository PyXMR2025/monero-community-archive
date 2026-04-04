---
title: 'ARM: build fails due to ld segfaulting on checkpoints.dat'
source_url: https://github.com/monero-project/monero/issues/974
author: radfish
assignees: []
labels: []
created_at: '2016-08-21T04:27:14+00:00'
updated_at: '2016-08-23T14:55:44+00:00'
type: issue
status: closed
closed_at: '2016-08-23T14:55:44+00:00'
---

# Original Description
```
cd /home/redfish/bitmonero-git/src/bitmonero/build/src/daemon && cd /home/redfish/bitmonero-git/src/bitmonero/src/daemon && cp ../blocks/checkpoints.dat blocks.dat && /usr/bin/ld -r -b binary -o /home/redfish/bitmonero-git/src/bitmonero/build/src/daemon/blocksdat.o blocks.dat && rm -f blocks.dat
```

The ld command segfaults even for the empty testnet_blocks.dat

The ld command succeeds on x86 (32bit). Sounds like an ld bug. Filing here, just for visibility:

```
$ touch foo.dat
$ /usr/bin/ld -r -b binary -o /tmp/foo.o foo.dat
Segmentation fault (core dumped)
```

GDB on ld:

```
(gdb) bt
#0  0xb6f2ca94 in ?? () from /usr/lib/libbfd-2.27.so
#1  0xb6f66ad0 in bfd_elf_final_link () from /usr/lib/libbfd-2.27.so
```


# Discussion History
## radfish | 2016-08-21T07:02:23+00:00
Workaround: use ld.gold instead of ld: `cmake -DCMAKE_LINKER=/usr/bin/ld.gold`

Sidenote: This CMAKE_LINKER var seems to affect only the linker invocations in the custom commands that deal with checkpoints.dat; all the rest is still linked with ld. So, the workaround has a minimal impact.

I will leave this issue open for a little while for visibility, then will close.


## ghost | 2016-08-21T11:00:29+00:00
Which ARM architecture?


## radfish | 2016-08-21T15:45:45+00:00
armv7h

$ ld --version
GNU ld (GNU Binutils) 2.27

$ uname -a
Linux bmsyncarm 4.4.8-std-1 #1 SMP Mon Apr 25 17:18:53 UTC 2016 armv7l
GNU/Linux

ld from binutils 2.27-1 from Arch Linux ARM distro.
Build details:
https://raw.githubusercontent.com/archlinuxarm/PKGBUILDs/master/core/binutils/PKGBUILD
Patch applied:
https://raw.githubusercontent.com/archlinuxarm/PKGBUILDs/master/core/binutils/binutils-e9c1bdad.patch


## radfish | 2016-08-23T14:55:44+00:00
They patched it, should make it into next binutils release I guess:
http://lists.gnu.org/archive/html/bug-binutils/2016-08/msg00165.html


# Action History
- Created by: radfish | 2016-08-21T04:27:14+00:00
- Closed at: 2016-08-23T14:55:44+00:00
