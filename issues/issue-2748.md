---
title: GhostRider algorithm cause RTX3060 on windows 470.05 driver go back to LHR
  mode
source_url: https://github.com/xmrig/xmrig/issues/2748
author: jcstudio-jeff-chen
assignees: []
labels: []
created_at: '2021-11-29T13:20:34+00:00'
updated_at: '2021-11-30T05:10:18+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
**Describe the bug**
Xmrig running GhostRider algorithm on Windows 10 causes RTX 3060 originally fully unlocked with Nvidia 470.05 driver go back to LHR mode. Every 10-30 minutes, the Ethash hashrate of RTX 3060 dropped from 48mh/s to 24mh/s and slowly goes back. This only happened when I use Xmrig to mine Raptoreum, Cpuminer doesn't have this problem.

**To Reproduce**
Motherboard: Gigabyte x570s Gaming X
CPU: Ryzen 5950X
GPU: RTX 3060 version 1 which can be unlocked with 470.05 driver.
OS: Windows 10
Ethereum miner: Gminer 2.71

Use Xmrig to mine Raptoreum and mine Ethereum at the same time, within 1 hour, you will see this bug.

**Expected behavior**
Mining Raptoreum should not cause RTX 3060 go to LHR mode.

**Required data**
I don't think log is required since xmrig itself functions normally, it just causes other program to function abnormally.

 - Config file or command line (without wallets)
 xmrig -a gr -o pool address -u wallet

 - OS: [e.g. Windows]
 Windows 10

 - For GPU related issues: information about GPUs and driver version.
NVidia driver 470.05

**Additional context**
Add any other context about the problem here.


# Discussion History
## SChernykh | 2021-11-29T13:32:04+00:00
Try to add `--cpu-priority 0` to xmrig command line.

## Spudz76 | 2021-11-29T16:14:17+00:00
Also changing all threads to `-1` allegedly helps with the Windows Process Scheduler, sometimes it doesn't like literal core index.

## jcstudio-jeff-chen | 2021-11-30T02:36:57+00:00
--cpu-priority 0 solved the problem thanks.
Also just a small thought. If I am gaming while CPU mining and now we know CPU mining can trigger LHR, therefore reduce GPU's performance. Is this considered a malfunction of the GPU? Like a proof of LHR can affect normal use too.

## Spudz76 | 2021-11-30T05:10:18+00:00
No, it probably just threw off the timing of how LHR cheats work.

Unless the game uses CUDA which it doesn't, the mining locker won't do anything.

# Action History
- Created by: jcstudio-jeff-chen | 2021-11-29T13:20:34+00:00
