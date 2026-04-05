---
title: L3 Cache is reporting at 50% of total in VM's on Hyper-V
source_url: https://github.com/xmrig/xmrig/issues/3397
author: phatman81
assignees: []
labels: []
created_at: '2024-01-03T01:02:20+00:00'
updated_at: '2024-01-03T16:02:48+00:00'
type: issue
status: closed
closed_at: '2024-01-03T16:02:48+00:00'
---

# Original Description
**Describe the bug**
When running 6.21.0, the L3$ is reporting at 50% lower in a VM than on the physical machine. Performance is also ~66% of the performance of the physical machine. This has been tested to individual NUMA nodes as well.

**To Reproduce**
Launch XMRig on the VM.

**Expected behavior**
All L3$ to be reported correctly and leveraged to the capacity possible.

**Required data**
 - on Physical machine:
![image](https://github.com/xmrig/xmrig/assets/49357589/461536cd-6688-4f5c-b92e-2af921f3b89b)

- on VM:
![image](https://github.com/xmrig/xmrig/assets/49357589/531852e5-792d-4311-b466-b7d0d5a2d12a)


 - OS: Windows Server 2022 adn Windows 10 [VM]

**Additional context**
On the VM, each time a NUMA node is removed from the VM, the L3$ drops accordingly but at still 50% of the correct total.
- on VM [16 cores / 1 NUMA node]:
![image](https://github.com/xmrig/xmrig/assets/49357589/06782b57-ff20-4427-8b9e-7d47ee2b7972)


# Discussion History
## SChernykh | 2024-01-03T08:47:46+00:00
Windows VM supervisor has control over how much cache is allocated to each VM, so it's not an XMRig bug.

## phatman81 | 2024-01-03T15:15:21+00:00
Interesting... Thanks for confirming a suspicion i had but could not otherwise verify.

Regarding the performance; while I expect to lose some performance in a VM, could this account for some of this loss I see currently? To get the best performance, I have to use the '-t 8' argument, as without it it will only use '4 threads' without it [trying to max out a single NUMA node]. The best I can get out of a single NUMA node via VM is:
![image](https://github.com/xmrig/xmrig/assets/49357589/786e7e52-86d3-47f2-beba-2436858b25bf)

This is the physical host to compare [tho this seems to be hasing low as well]:
![image](https://github.com/xmrig/xmrig/assets/49357589/e60f7e31-2deb-4589-a663-45c79739077c)

_NOTE: The two screenshots are two separate machines running like-for-like hardware._ 

## SChernykh | 2024-01-03T15:43:35+00:00
If the VM reports only 8 MB cache, XMRig will use 4 threads (2 MB per thread). 8 threads shouldn't be faster, but it's a VM and the physical CPU has more cache, so anything is possible. Also, when you're running in a VM, MSR mod doesn't work (even if it says that it worked), it will result in some hashrate loss.

## phatman81 | 2024-01-03T16:02:48+00:00
So my issue is “A riddle wrapped in a mystery inside an enigma”. Guess that answers any follow-up questions i may have. :-)
Guess i'll wait for the next OS update and see if anything changes. I'll keep trying different configurations and see what i can max it out with.

Thanks for all your insight!

# Action History
- Created by: phatman81 | 2024-01-03T01:02:20+00:00
- Closed at: 2024-01-03T16:02:48+00:00
