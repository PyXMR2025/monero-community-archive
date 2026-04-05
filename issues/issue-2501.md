---
title: Abort Trap on FreeBSD using 6.13.1(static)
source_url: https://github.com/xmrig/xmrig/issues/2501
author: mircsicz
assignees: []
labels: []
created_at: '2021-07-30T13:03:02+00:00'
updated_at: '2021-07-30T13:04:44+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Hi all,

think I did my homework and google'd before I came here, but only found thinks like this: https://github.com/xmrig/xmrig/issues/1394

But in my case it's not "Abort Trap: 6" but "Abort Trap"

Here's what I run:
```
# /usr/pbi/xmrig-amd64/bin/xmrig --config=/usr/pbi/xmrig-amd64/etc/xmrig/config.json --dry-run
 * ABOUT        XMRig/6.13.1 clang/10.0.0
 * LIBS         libuv/1.41.0 OpenSSL/1.1.1k hwloc/2.4.1
 * HUGE PAGES   supported
 * 1GB PAGES    unavailable
 * CPU          Intel(R) Xeon(R) CPU E5440 @ 2.83GHz (1) 64-bit -AES
                L2:12.0 MB L3:0.0 MB 4C/4T NUMA:1
 * MEMORY       1.8/16.0 GB (11%)
                DIMM_A0: 4 GB DDR2 @ 667 MHz 36HTF51272F667G1D6
                DIMM_A1: 2 GB DDR2 @ 667 MHz 36HTF25672F667D1D4
                DIMM_A2: 2 GB DDR2 @ 667 MHz 72T256520HFD3SB
                DIMM_B0: 4 GB DDR2 @ 667 MHz 36HTF51272F667G1D6
                DIMM_B1: 2 GB DDR2 @ 667 MHz 36HTF25672F667D1D4
                DIMM_B2: 2 GB DDR2 @ 667 MHz 72T256520HFD3SB
 * MOTHERBOARD  Sun Microsystems - SUN FIRE X4150
 * DONATE       1%
 * ASSEMBLY     auto:none
 * POOL #1      pool.minexmr.com:4444 algo auto
 * COMMANDS     hashrate, pause, resume, results, connection
[2021-07-30 15:02:20.909]  config   OK

# /usr/pbi/xmrig-amd64/bin/xmrig --config=/usr/pbi/xmrig-amd64/etc/xmrig/config.json
 * ABOUT        XMRig/6.13.1 clang/10.0.0
 * LIBS         libuv/1.41.0 OpenSSL/1.1.1k hwloc/2.4.1
 * HUGE PAGES   supported
 * 1GB PAGES    unavailable
 * CPU          Intel(R) Xeon(R) CPU E5440 @ 2.83GHz (1) 64-bit -AES
                L2:12.0 MB L3:0.0 MB 4C/4T NUMA:1
 * MEMORY       1.8/16.0 GB (11%)
                DIMM_A0: 4 GB DDR2 @ 667 MHz 36HTF51272F667G1D6
                DIMM_A1: 2 GB DDR2 @ 667 MHz 36HTF25672F667D1D4
                DIMM_A2: 2 GB DDR2 @ 667 MHz 72T256520HFD3SB
                DIMM_B0: 4 GB DDR2 @ 667 MHz 36HTF51272F667G1D6
                DIMM_B1: 2 GB DDR2 @ 667 MHz 36HTF25672F667D1D4
                DIMM_B2: 2 GB DDR2 @ 667 MHz 72T256520HFD3SB
 * MOTHERBOARD  Sun Microsystems - SUN FIRE X4150
 * DONATE       1%
 * ASSEMBLY     auto:none
 * POOL #1      pool.minexmr.com:4444 algo auto
 * COMMANDS     hashrate, pause, resume, results, connection
Abort trap
```

This is
`[root@nas1] ~/mircsicz# freebsd-version
10.3-STABLE

[root@nas1] ~/mircsicz# cat /etc/version
FreeNAS-9.10.2-U6 (561f0d7a1)
`

And yes the machine is kind of ancient... ;-) Not looking for max interest but usage for an old iron which is turned on anyways, as its serving as a local backup target prior to a cloud sync...


# Discussion History
# Action History
- Created by: mircsicz | 2021-07-30T13:03:02+00:00
