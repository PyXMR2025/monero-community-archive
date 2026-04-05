---
title: CPU config (argon2/chukwa) ignore intensity
source_url: https://github.com/xmrig/xmrig/issues/1153
author: qutimqqcom
assignees: []
labels: []
created_at: '2019-08-31T11:21:20+00:00'
updated_at: '2019-09-01T19:52:57+00:00'
type: issue
status: closed
closed_at: '2019-09-01T19:52:57+00:00'
---

# Original Description
"argon2/chukwa":{"intensity": 4,"threads": 4,"affinity": -1}
set   intensity   from 0 to 8 ,  no changes


 * ABOUT        XMRig/3.1.1 gcc/7.4.1
 * LIBS         libuv/1.30.1 hwloc/1.11.8rc2-git
 * CPU          Intel(R) Core(TM) i7-4790 CPU @ 3.60GHz (1) x64 AES
                L2:1.0 MB L3:8.0 MB 4C/8T NUMA:1
 * DONATE       5%
 * ASSEMBLY     auto:intel
 * POOL #1      Pool.TRTL.CryptoPool.Space:3333 algo auto
 * COMMANDS     hashrate, pause, resume
[2019-08-31 14:14:38.355] use pool Pool.TRTL.CryptoPool.Space:3333  199.247.10.186
[2019-08-31 14:14:38.356] new job from Pool.TRTL.CryptoPool.Space:3333 diff 50000 algo argon2/chukwa height 1804065
[2019-08-31 14:14:38.610]  cpu  use argon2 implementation AVX2
[2019-08-31 14:14:38.610]  cpu  use profile  argon2/chukwa  (**4 threads**) scratchpad 512 KB
[2019-08-31 14:14:38.612]  cpu  READY threads **4(4) huge pages 4/4 100**% memory 2048 KB (2 ms)
[2019-08-31 14:14:44.313] accepted (1/0) diff 50000 (77 ms)
[2019-08-31 14:14:50.397] accepted (2/0) diff 50000 (77 ms)


# Discussion History
## xmrig | 2019-08-31T11:30:34+00:00
This algorithm not support this option, same as RandomX and cn/gpu.
Thank you.

# Action History
- Created by: qutimqqcom | 2019-08-31T11:21:20+00:00
- Closed at: 2019-09-01T19:52:57+00:00
