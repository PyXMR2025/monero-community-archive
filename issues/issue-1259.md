---
title: evo with GPU support integrated
source_url: https://github.com/xmrig/xmrig/issues/1259
author: Spudz76
assignees: []
labels: []
created_at: '2019-11-03T19:41:18+00:00'
updated_at: '2021-04-12T15:31:01+00:00'
type: issue
status: closed
closed_at: '2021-04-12T15:31:01+00:00'
---

# Original Description
Integrated OpenCL/CUDA work well however, seems to lock both to the same coin.

In multimining configurations with profit switching (MoneroOcean in my case), running the same algo on both types of devices is not ideal compared to running separate miners where the GPU can grind on CN/GPU while the CPU grinds on RX/wow and obtain the best effective mining rates.  The CPU would never be very optimal grinding on CN/GPU while the GPU would never be very optimal grinding on RX of any kind (also most of my GPUs are sub-2080MB so wouldn't work anyway), which wastes power toward being partially ineffective.

Are there plans to abandon the separate versions once the backends are unified into main xmrig? And if so to make the unified miner able to funnel differing algos to different backends?

I do enjoy the ability of the cuda-plugin version to be able to hot-switch algos as compared to standalone xmrig-nvidia which can't jump algos (except among families like CN-Heavy it can jump "flavors" thereof, but not when you need a different block/thread per algo, which unified completely fixed).  Relaunching the miner to jump algos tends to crash more often (cold reboot) than if the miner left the GPU initialized and allocated, and only swapped kernels and reformatted its already allocated memory pool.   Also if per-backend pool definition becomes possible, allow each to use a different miner name as well (I use base `hostname` for the cpu miners, and `hostname-nv` for CUDA ones, or `hostname-amd` for OpenCL).

tagging @SChernykh since I think it's your department

Seems like it should work how it does now given a global pool configuration, and then power user types could add a copy of the global pool definition under the "cuda" or "opencl" subsection to define a different one to use for those backend(s).  If no override then it works unified as it does now.  Just unsure if dual active pool is difficult to implement.  And if the separate miners will still be supported and updated just like unified then I can continue to run completely separate processes... but would like to see xmrig-nvidia get the hotswapping (multiple block/thread defs per algo) in that case.

# Discussion History
# Action History
- Created by: Spudz76 | 2019-11-03T19:41:18+00:00
- Closed at: 2021-04-12T15:31:01+00:00
