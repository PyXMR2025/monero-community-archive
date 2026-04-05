---
title: Not running GhostRider Algo on Linux VMs
source_url: https://github.com/xmrig/xmrig/issues/2777
author: ghost
assignees: []
labels: []
created_at: '2021-12-03T03:50:21+00:00'
updated_at: '2021-12-03T08:50:46+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
**Describe the bug**
Running the xmrig command with `-a gr` will receive a `Segmentation fault` error immediately after mining starts.

**To Reproduce**
Simply create an KVM virtualized server w/ Ubuntu 20.04 and run the latest linux-static compiled xmrig.

**Expected behavior**
Should work as any other algorithm works, combining working algos should work fine.

**Required data**
```
root@ubuntu:~# virt-what
kvm
root@ubuntu:~# ./xmrig_4 -a gr -o raptoreumemporium.com:3008 -u [wallet here]
 * ABOUT        XMRig/6.16.2 gcc/9.3.0
 * LIBS         libuv/1.42.0 OpenSSL/1.1.1l hwloc/2.5.0
 * HUGE PAGES   supported
 * 1GB PAGES    disabled
 * CPU          AMD EPYC 7K62 48-Core Processor (1) 64-bit AES VM
                L2:4.0 MB L3:16.0 MB 1C/1T NUMA:1
 * MEMORY       0.7/1.9 GB (35%)
                DIMM 0: 2 GB RAM @ 0 MHz DIMM 0
 * MOTHERBOARD  Tencent Cloud - CVM
 * DONATE       1%
 * ASSEMBLY     auto:ryzen
 * POOL #1      raptoreumemporium.com:3008 algo ghostrider
 * COMMANDS     hashrate, pause, resume, results, connection
[2021-12-03 11:44:51.071]  net      use pool raptoreumemporium.com:3008  172.14.53.224
[2021-12-03 11:44:51.071]  net      new job from raptoreumemporium.com:3008 diff
 6554 algo ghostrider height 197423
[2021-12-03 11:44:51.072]  msr      cannot read MSR 0xc0011020
[2021-12-03 11:44:51.072]  msr      FAILED TO APPLY MSR MOD, HASHRATE WILL BE LOW
Segmentation fault
```

**Additional context**
Maybe nothing else.
If needed I'll try to dump memory log out.


# Discussion History
## SChernykh | 2021-12-03T07:27:51+00:00
Can you check if version 6.16.0 works?

## ghost | 2021-12-03T08:50:46+00:00
> Can you check if version 6.16.0 works?

nope it still crashes...

# Action History
- Created by: ghost | 2021-12-03T03:50:21+00:00
