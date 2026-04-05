---
title: 'thread #0 failed with error <randomx_prepare>:45 "out of memory"'
source_url: https://github.com/xmrig/xmrig/issues/1693
author: Blacksheep70
assignees: []
labels:
- CUDA
created_at: '2020-05-25T21:48:10+00:00'
updated_at: '2021-04-12T14:56:17+00:00'
type: issue
status: closed
closed_at: '2021-04-12T14:56:17+00:00'
---

# Original Description
**Describe the bug**
When using xmrig with CUDA on a RTX 2080 Super error ` thread #0 failed with error <randomx_prepare>:45 "out of memory"` occur

**To Reproduce**
Use a RTX 2080 Super with 8GB
Run `xmrig.exe --donate-level <N> --no-cpu --cuda --cuda-loader=<full qualified path to xmrig-cuda.dll> --cuda-devices=<ID> -o <URL>:<PORT> -u <WALLET> -k --tls -p`

**Expected behavior**
Correct detection of available GPU memory
Not running into  `thread #0 failed with error <randomx_prepare>:45 "out of memory"`

**Required data**
Log:
```
 * ABOUT        XMRig/5.11.2 MSVC/2019
 * LIBS         libuv/1.38.0 OpenSSL/1.1.1g hwloc/2.2.0
 * HUGE PAGES   permission granted
 * 1GB PAGES    unavailable
 * CPU          Intel(R) Core(TM) i9-9900K CPU @ 3.60GHz (1) x64 AES
                L2:2.0 MB L3:16.0 MB 8C/16T NUMA:1
 * MEMORY       7.1/31.9 GB (22%)
 * DONATE       5%
 * ASSEMBLY     auto:intel
 * POOL #1      pool.supportxmr.com:443 algo auto
 * COMMANDS     hashrate, pause, resume
 * OPENCL       disabled
 * CUDA         10.1/10.2/3.0.0
 * NVML         10.441.66/441.66 press e for health report
 * CUDA GPU     #0 01:00.0 GeForce RTX 2080 SUPER 1830/7751 MHz smx:48 arch:75 mem:6695/8192 MB
[2020-05-25 23:25:28.779]  net  use pool pool.supportxmr.com:443 TLSv1.2 94.23.23.52
[2020-05-25 23:25:28.779]  net  fingerprint (SHA-256): "b90d9xxxxx57b4003xxxxxxxxxxxxxxx0c733cc4xxxxxxxxxxxxd1442e"
[2020-05-25 23:25:28.780]  net  new job from pool.supportxmr.com:443 diff 50000 algo rx/0 height 2106378
[2020-05-25 23:25:28.780]  cpu  use argon2 implementation AVX2
[2020-05-25 23:25:28.781]  msr  service WinRing0_1_2_0 is already exists
[2020-05-25 23:25:28.812]  msr  register values for "intel" preset has been set successfully (32 ms)
[2020-05-25 23:25:28.813]  rx   init dataset algo rx/0 (16 threads) seed 63aabd0407a961c1...
[2020-05-25 23:25:28.817]  rx   allocated 2336 MB (2080+256) huge pages 100% 1168/1168 +JIT (3 ms)
[2020-05-25 23:25:30.508]  rx   dataset ready (1692 ms)
[2020-05-25 23:25:30.508]  nv   use profile  rx  (1 thread) scratchpad 2048 KB
|  # | GPU |  BUS ID |    I |   T |   B | BF |  BS |  MEM | NAME
|  0 |   0 | 01:00.0 | 2240 |  32 |  70 |  6 |  25 | 4480 | GeForce RTX 2080 SUPER
[2020-05-25 23:25:30.729]  nv   READY threads 1/1 (220 ms)
[2020-05-25 23:25:31.231]  nv   thread #0 failed with error <randomx_prepare>:45 "out of memory"
```
OS: Running on Win 10
CUDA drivers: 10.2.89

**Additional context**
Looks like only 4 GB are detected:

`|  0 |   0 | 01:00.0 | 2240 |  32 |  70 |  6 |  25 | 4480 | GeForce RTX 2080 SUPER`

Task manager shows for GPU 0 7,7 GB used of available 8 GB while the GPU is bored

<img width="516" alt="Unbenannt" src="https://user-images.githubusercontent.com/8124924/82844786-19bf8200-9ee2-11ea-8a69-62b01d5c1343.PNG">





# Discussion History
# Action History
- Created by: Blacksheep70 | 2020-05-25T21:48:10+00:00
- Closed at: 2021-04-12T14:56:17+00:00
