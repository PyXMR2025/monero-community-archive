---
title: X5675 CPU Support on rx/arq
source_url: https://github.com/xmrig/xmrig/issues/1268
author: BKdilse
assignees: []
labels: []
created_at: '2019-11-09T11:23:51+00:00'
updated_at: '2019-11-09T11:47:07+00:00'
type: issue
status: closed
closed_at: '2019-11-09T11:47:07+00:00'
---

# Original Description
Hi,

Having a problem getting this working, and wanted to confirm if the X5675 CPU is supported, or whether something else is wrong?

Here is the output from the Miner:

` * ABOUT        XMRig/4.5.0-beta gcc/5.4.0
 * LIBS         libuv/1.31.0 OpenSSL/1.1.1c hwloc/2.0.4
 * CPU          Intel(R) Xeon(R) CPU X5675 @ 3.07GHz (24) x64 AES
                L2:6.0 MB L3:288.0 MB 24C/24T NUMA:2
 * DONATE       5%
 * ASSEMBLY     auto:intel
 * POOL #1      arq.pool.gntl.co.uk:7777 coin arqma
 * COMMANDS     hashrate, pause, resume
 * OPENCL       disabled
 * CUDA         disabled
[2019-11-09 11:20:03.345]  net  use pool arq.pool.gntl.co.uk:7777  x.x.x.x
[2019-11-09 11:20:03.346]  net  new job from arq.pool.gntl.co.uk:7777 diff 25000 algo rx/arq
[2019-11-09 11:20:03.346]  rx   init datasets algo rx/arq (24 threads) seed 19a4fa4705a9788a...
[2019-11-09 11:20:03.346]  rx   #1 allocated 2080 MB huge pages   0% (0 ms)
[2019-11-09 11:20:03.346]  rx   #0 allocated 2080 MB huge pages   0% (1 ms)
[2019-11-09 11:20:03.347]  rx   #0 allocated  256 MB huge pages   0% +JIT (0 ms)
[2019-11-09 11:20:03.347]  rx   -- allocated 4416 MB huge pages   0% 0/2208 (1 ms)
[2019-11-09 11:20:03.807]  net  new job from arq.pool.gntl.co.uk:7777 diff 25000 algo rx/arq
[2019-11-09 11:20:15.752]  rx   #0 dataset ready (12371 ms)
[2019-11-09 11:20:59.363]  net  new job from arq.pool.gntl.co.uk:7777 diff 13158 algo rx/arq
Killed
`

# Discussion History
## xmrig | 2019-11-09T11:42:20+00:00
You use virtual machine, not physical server and this machine has no enough memory for 2 datasets, try disable NUMA support in config https://github.com/xmrig/xmrig/blob/beta/src/config.json#L19
Thank you.

## BKdilse | 2019-11-09T11:47:07+00:00
Sorry, my fault, not enough RAM.  Thanks for the quick response :)

# Action History
- Created by: BKdilse | 2019-11-09T11:23:51+00:00
- Closed at: 2019-11-09T11:47:07+00:00
