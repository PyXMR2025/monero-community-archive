---
title: '"Illegal instruction" error running on ARMv7 rev2'
source_url: https://github.com/xmrig/xmrig/issues/322
author: dserodio
assignees: []
labels:
- wontfix
- arm
created_at: '2018-01-05T16:41:52+00:00'
updated_at: '2019-02-03T17:24:27+00:00'
type: issue
status: closed
closed_at: '2019-02-03T17:24:27+00:00'
---

# Original Description
This is similar to #230 but on ARMv7 (Scaleway C1 server), distro is Ubuntu 16.04, kernel 4.10.8:

    $ ./xmrig
    Illegal instruction

I tried the fix mentioned in #230, but it did'nt work:

    $ ./xmrig --av 3
    Illegal instruction

    $ cat /proc/cpuinfo
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

Thanks

# Discussion History
## xmrig | 2018-01-06T15:36:38+00:00
ARM without NEON instructions not supported. #230 relevant only for ARMv8 (and other ARMv7) without hardware AES support.
Thank you.

## italomaia | 2018-01-10T01:09:49+00:00
Workaround?

## xmrig | 2018-01-10T06:15:10+00:00
No workaround at this moment.
Thank you.

# Action History
- Created by: dserodio | 2018-01-05T16:41:52+00:00
- Closed at: 2019-02-03T17:24:27+00:00
