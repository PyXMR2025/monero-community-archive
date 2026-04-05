---
title: '"Illegal instruction" error on ARMv7'
source_url: https://github.com/xmrig/xmrig/issues/246
author: razza-guhl
assignees:
- xmrig
labels:
- bug
- enhancement
- wontfix
- arm
created_at: '2017-12-07T22:53:59+00:00'
updated_at: '2019-04-18T12:38:09+00:00'
type: issue
status: closed
closed_at: '2018-09-22T05:22:16+00:00'
---

# Original Description
I'm getting Illegal instruction error on ARMv7 machine

```
root@machine:~/xmrig/build# ./xmrig
Illegal instruction
```
Source was compiled on machine (described here: https://github.com/xmrig/xmrig/wiki/Ubuntu-Build)

Using --av=3 did not work.

This is the output of "cat /proc/cpuinfo"
                                   
```
processor       : 0
model name      : ARMv7 Processor rev 2 (v7l)
BogoMIPS        : 50.00
Features        : half thumb fastmult vfp edsp thumbee vfpv3 tls idiva idivt vfpd32 lpae
CPU implementer : 0x56
CPU architecture: 7
CPU variant     : 0x2
CPU part        : 0x584
CPU revision    : 2

processor       : 1
model name      : ARMv7 Processor rev 2 (v7l)
BogoMIPS        : 50.00
Features        : half thumb fastmult vfp edsp thumbee vfpv3 tls idiva idivt vfpd32 lpae
CPU implementer : 0x56
CPU architecture: 7
CPU variant     : 0x2
CPU part        : 0x584
CPU revision    : 2

processor       : 2
model name      : ARMv7 Processor rev 2 (v7l)
BogoMIPS        : 50.00
Features        : half thumb fastmult vfp edsp thumbee vfpv3 tls idiva idivt vfpd32 lpae
CPU implementer : 0x56
CPU architecture: 7
CPU variant     : 0x2
CPU part        : 0x584
CPU revision    : 2

processor       : 3
model name      : ARMv7 Processor rev 2 (v7l)
BogoMIPS        : 50.00
Features        : half thumb fastmult vfp edsp thumbee vfpv3 tls idiva idivt vfpd32 lpae
CPU implementer : 0x56
CPU architecture: 7
CPU variant     : 0x2
CPU part        : 0x584
CPU revision    : 2

Hardware        : Marvell Armada 370/XP (Device Tree)
Revision        : 0000
Serial          : 0000000000000000
```

# Discussion History
## xmrig | 2017-12-11T10:37:13+00:00
CPU must support neon instructions. This requirement may changed in future, I have plans to add/replace software aes implementation.
Thank you.

## gtimeg77 | 2017-12-13T15:27:55+00:00
not needing neon definitely wanted/needed

## sam0x17 | 2018-01-07T08:59:30+00:00
Likewise needed for me :+1: 

## gvieri | 2018-01-18T17:47:17+00:00
I am getting the same trouble... 

## xmrig | 2018-09-22T05:22:16+00:00
ARM CPUs without NEON will be not supported.
Thank you.

# Action History
- Created by: razza-guhl | 2017-12-07T22:53:59+00:00
- Closed at: 2018-09-22T05:22:16+00:00
