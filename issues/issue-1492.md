---
title: Strange behavior of the "threads" parameter on a dual-processor computer
source_url: https://github.com/xmrig/xmrig/issues/1492
author: timk74
assignees: []
labels:
- question
created_at: '2020-01-09T01:05:43+00:00'
updated_at: '2020-02-01T09:25:18+00:00'
type: issue
status: closed
closed_at: '2020-02-01T09:25:18+00:00'
---

# Original Description
**Config.json**
```
{
  "pools": [
    {
      "coin": "monero",
      "url": "xmr-eu1.nanopool.org:14433",
      "tls": true,
      "user": "",
      "pass": "x"
    }
  ],
  "watch": false,
  "autosave": false,
  "cuda": {"enabled": false},
  "opencl": {"enabled": false},
  "randomx": {"init": 1},
  "cpu": {"*": {"threads": 0}}
}
```

**Output (threads: 0):**
```
 * ABOUT        XMRig/5.5.0 MSVC/2019
 * LIBS         libuv/1.34.0 OpenSSL/1.1.1d hwloc/2.1.0
 * HUGE PAGES   permission granted
 * 1GB PAGES    unavailable
 * CPU          Intel(R) Xeon(R) Silver 4110 CPU @ 2.10GHz (2) x64 AES
                L2:16.0 MB L3:22.0 MB 16C/32T NUMA:2
 * MEMORY       2.2/63.7 GB (3%)
 * DONATE       5%
 * ASSEMBLY     auto:intel
 * POOL #1      xmr-eu1.nanopool.org:14433 coin monero
 * COMMANDS     'h' hashrate, 'p' pause, 'r' resume
[2020-01-09 10:42:41.343]  net  use pool xmr-eu1.nanopool.org:14433 TLSv1.2 51.15.65.182
[2020-01-09 10:42:41.345]  net  fingerprint (SHA-256): "c38886efdee542ebd99801b75c75d3498d97978bbcdec07c7271cb19729e014f"
[2020-01-09 10:42:41.345]  net  new job from xmr-eu1.nanopool.org:14433 diff 480045 algo rx/0 height 2007111
[2020-01-09 10:42:41.413]  msr  register values for "intel" preset has been set successfully (67 ms)
[2020-01-09 10:42:41.413]  rx   init datasets algo rx/0 (1 threads) seed 777ae6a98aeff256...
[2020-01-09 10:42:41.437]  rx   #1 allocated 2080 MB huge pages 100% (23 ms)
[2020-01-09 10:42:41.473]  rx   #0 allocated 2080 MB huge pages 100% (59 ms)
[2020-01-09 10:42:41.479]  rx   #0 allocated  256 MB huge pages 100% +JIT (5 ms)
[2020-01-09 10:42:41.480]  rx   -- allocated 4416 MB huge pages 100% 2208/2208 (66 ms)
[2020-01-09 10:42:49.575]  net  new job from xmr-eu1.nanopool.org:14433 diff 480045 algo rx/0 height 2007111
[2020-01-09 10:43:27.047]  rx   #0 dataset ready (45567 ms)
[2020-01-09 10:43:27.550]  rx   #1 dataset ready (502 ms)
[2020-01-09 10:43:27.550]  cpu  use profile  rx  (16 threads) scratchpad 2048 KB
[2020-01-09 10:43:28.021]  cpu  READY threads 16/16 (16) huge pages 100% 16/16 memory 32768 KB (470 ms)
[2020-01-09 10:43:42.249]  net  new job from xmr-eu1.nanopool.org:14433 diff 480045 algo rx/0 height 2007112
[2020-01-09 10:44:03.441]  net  new job from xmr-eu1.nanopool.org:14433 diff 480045 algo rx/0 height 2007113
[2020-01-09 10:44:10.894]  cpu  accepted (1/0) diff 480045 (192 ms)
[2020-01-09 10:44:18.354]  cpu  accepted (2/0) diff 480045 (186 ms)
[2020-01-09 10:44:29.254] speed 10s/60s/15m 7473.6 7473.8 n/a H/s max 7477.7 H/s
```
Now we begin to change the threads parameter and we see that from 1 to 8 the hashrate is growing as expected. With a further increase to 16, the hash rate drops to 2455, although with an automatic configuration with 16 threads it reaches 7473:

```
0  7473
1  436
2  1181
4  1696
6  2974
8  3125
10 3179
12 2764
14 2631
16 2455
```


# Discussion History
## xmrig | 2020-01-09T01:38:02+00:00
Threads it not just a number, it more complicated thing, automatic configuration use 8 threads per one physical CPU (16 total) and properly assign it to physical cores and it best for your system.

By using threads as number without CPU affinity all messed up, threads may created anywhere, even on one physical CPU and multiple dataset not work as expected, threads as number works OK only on single socket/single NUMA (UMA) hardware. If you still like change threads count you should edit generated `rx` profile.

By using `"randomx": {"init": 1},` you just increase dataset initialization time from few seconds to 45 seconds.
Thank you.

## timk74 | 2020-01-09T03:27:31+00:00
Ok. I just assumed that the threads are distributed among the cores more smarter :)

> By using `"randomx": {"init": 1},` you just increase dataset initialization time from few seconds to 45 seconds.

I use init:1 to reduce the load at startup. I think the initialization time is not important here.


# Action History
- Created by: timk74 | 2020-01-09T01:05:43+00:00
- Closed at: 2020-02-01T09:25:18+00:00
