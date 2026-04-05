---
title: 'DNS error: "resource busy or locked"'
source_url: https://github.com/xmrig/xmrig/issues/1509
author: snowdream
assignees: []
labels: []
created_at: '2020-01-22T06:05:35+00:00'
updated_at: '2020-02-10T04:15:37+00:00'
type: issue
status: closed
closed_at: '2020-02-10T04:15:37+00:00'
---

# Original Description
**Describe the bug**
DNS error: "resource busy or locked"

**To Reproduce**
Steps to reproduce the behavior.

**Expected behavior**
use xmrig in docker https://hub.docker.com/repository/docker/snowdream/xmr

```bash
docker run --restart=always --network host -d -v /etc/xmrig/config.json:/etc/xmrig/config.json --name xmr snowdream/xmr
```
**Required data**
 - Miner log as text or screenshot
 - Config file or command line (without wallets)
 - OS: [e.g. Windows]
 - For GPU related issues: information about GPUs and driver version.
```bash
 /usr/bin/xmrig -c /etc/xmrig/config.json
 * ABOUT        C3XMRig/5.4.0-c3 gcc/7.4.0
 * LIBS         libuv/1.18.0 OpenSSL/1.1.1 hwloc/2.0.4
 * HUGE PAGES   supported
 * 1GB PAGES    disabled
 * CPU          Intel(R) Xeon(R) Gold 61xx CPU (1) x64 AES
                L2:4.0 MB L3:0.0 MB 1C/1T NUMA:1
 * MEMORY       1.5/1.8 GB (83%)
 * DONATE       0%
 * ASSEMBLY     auto:intel
 * POOL #1      mine.c3pool.com:13333 algo auto
 * COMMANDS     hashrate, pause, resume
 * OPENCL       disabled
 * CUDA         disabled
[2020-01-22 05:51:02.811] >>>>> STARTING ALGO PERFORMANCE CALIBRATION (with 10 seconds round)
[2020-01-22 05:51:03.138]  cpu  use argon2 implementation AVX2
[2020-01-22 05:51:03.138]  cpu  use profile  argon2  (1 thread) scratchpad 512 KB
[2020-01-22 05:51:03.139]  cpu  READY threads 1/1 (1) huge pages 100% 1/1 memory 512 KB (2 ms)
[2020-01-22 05:51:03.344]  ===> Starting benchmark of argon2/chukwa algo
[2020-01-22 05:51:13.351]  ===> argon2/chukwa hasrate: 1461.976685
[2020-01-22 05:51:13.351]  cpu  stopped (1 ms)
[2020-01-22 05:51:13.352]  msr  msr kernel module is not available
[2020-01-22 05:51:13.352]  rx   init dataset algo rx/0 (1 threads) seed 0000000000000000...
[2020-01-22 05:51:13.352]  rx   not enough memory for RandomX dataset
[2020-01-22 05:51:13.413]  rx   failed to allocate RandomX dataset, switching to slow mode (60 ms)
[2020-01-22 05:51:14.300]  rx   dataset ready (887 ms)
[2020-01-22 05:51:14.300]  cpu  use profile  rx  (1 thread) scratchpad 2048 KB
[2020-01-22 05:51:14.301]  cpu  READY threads 1/1 (1) huge pages 100% 1/1 memory 2048 KB (1 ms)
[2020-01-22 05:51:14.499]  ===> Starting benchmark of rx/0 algo
[2020-01-22 05:51:24.575]  ===> rx/0 hasrate: 45.851528
[2020-01-22 05:51:24.576]  cpu  stopped (1 ms)
[2020-01-22 05:51:24.576]  rx   init dataset algo rx/wow (1 threads) seed 0000000000000000...
[2020-01-22 05:51:24.576]  rx   dataset ready (0 ms)
[2020-01-22 05:51:24.576]  cpu  use profile  rx/wow  (1 thread) scratchpad 1024 KB
[2020-01-22 05:51:24.576]  cpu  READY threads 1/1 (1) huge pages 100% 1/1 memory 1024 KB (0 ms)
[2020-01-22 05:51:24.633]  ===> Starting benchmark of rx/wow algo
[2020-01-22 05:51:34.643]  ===> rx/wow hasrate: 51.048950
[2020-01-22 05:51:34.644]  cpu  stopped (1 ms)
[2020-01-22 05:51:34.644]  rx   init dataset algo defyx (1 threads) seed 0000000000000000...
[2020-01-22 05:51:34.644]  rx   dataset ready (0 ms)
[2020-01-22 05:51:34.644]  cpu  use profile  defyx  (1 thread) scratchpad 256 KB
[2020-01-22 05:51:34.644]  cpu  READY threads 1/1 (1) huge pages 100% 1/1 memory 256 KB (0 ms)
[2020-01-22 05:51:34.666]  ===> Starting benchmark of defyx algo
[2020-01-22 05:51:44.690]  ===> defyx hasrate: 243.016769
[2020-01-22 05:51:44.691]  cpu  stopped (0 ms)
[2020-01-22 05:51:44.691]  rx   init dataset algo rx/arq (1 threads) seed 0000000000000000...
[2020-01-22 05:51:44.691]  rx   dataset ready (0 ms)
[2020-01-22 05:51:44.691]  cpu  use profile  rx/wow  (1 thread) scratchpad 256 KB
[2020-01-22 05:51:44.691]  cpu  READY threads 1/1 (1) huge pages 100% 1/1 memory 256 KB (1 ms)
[2020-01-22 05:51:44.716]  ===> Starting benchmark of rx/arq algo
[2020-01-22 05:51:54.736]  ===> rx/arq hasrate: 197.005981
[2020-01-22 05:51:54.736]  cpu  stopped (0 ms)
[2020-01-22 05:51:54.736]  cpu  use profile  cn  (1 thread) scratchpad 2048 KB
[2020-01-22 05:51:55.414]  cpu  READY threads 1/1 (1) huge pages 100% 1/1 memory 2048 KB (678 ms)
[2020-01-22 05:51:55.558]  ===> Starting benchmark of cn/r algo
[2020-01-22 05:52:03.063] speed 10s/60s/15m n/a n/a n/a H/s max n/a H/s
[2020-01-22 05:52:05.670]  ===> cn/r hasrate: 35.996834
[2020-01-22 05:52:06.881]  ===> Starting benchmark of cn/gpu algo
[2020-01-22 05:52:18.176]  ===> cn/gpu hasrate: 4.338202
[2020-01-22 05:52:18.177]  cpu  stopped (0 ms)
[2020-01-22 05:52:18.177]  cpu  use profile  cn-lite  (1 thread) scratchpad 1024 KB
[2020-01-22 05:52:18.193]  cpu  READY threads 1/1 (1) huge pages 100% 1/1 memory 1024 KB (17 ms)
[2020-01-22 05:52:18.315]  ===> Starting benchmark of cn-lite/1 algo
[2020-01-22 05:52:28.332]  ===> cn-lite/1 hasrate: 127.882599
[2020-01-22 05:52:28.333]  cpu  stopped (1 ms)
[2020-01-22 05:52:28.333]  cpu  use profile  cn-heavy  (1 thread) scratchpad 4096 KB
[2020-01-22 05:52:28.421]  cpu  READY threads 1/1 (1) huge pages 100% 2/2 memory 4096 KB (88 ms)
[2020-01-22 05:52:28.554]  ===> Starting benchmark of cn-heavy/tube algo
[2020-01-22 05:52:38.605]  ===> cn-heavy/tube hasrate: 31.340166
[2020-01-22 05:52:38.608]  cpu  stopped (4 ms)
[2020-01-22 05:52:38.608]  cpu  use profile  cn-pico  (1 thread) scratchpad 256 KB
[2020-01-22 05:52:38.611]  cpu  READY threads 1/1 (2) huge pages 100% 1/1 memory 512 KB (2 ms)
[2020-01-22 05:52:38.630]  ===> Starting benchmark of cn-pico algo
[2020-01-22 05:52:48.645]  ===> cn-pico hasrate: 835.946106
[2020-01-22 05:52:48.646] configuration saved to: "/etc/xmrig/config.json"
[2020-01-22 05:52:48.646] [mine.c3pool.com:13333] DNS error: "resource busy or locked"
[2020-01-22 05:52:54.023] [mine.c3pool.com:13333] DNS error: "resource busy or locked"
[2020-01-22 05:52:59.025] [mine.c3pool.com:13333] DNS error: "resource busy or locked"
[2020-01-22 05:53:03.237] speed 10s/60s/15m n/a n/a n/a H/s max 925.4 H/s
[2020-01-22 05:53:04.026] [mine.c3pool.com:13333] DNS error: "resource busy or locked"
[2020-01-22 05:53:09.028] [mine.c3pool.com:13333] DNS error: "resource busy or locked"
[2020-01-22 05:54:03.289] speed 10s/60s/15m n/a n/a n/a H/s max 925.4 H/s
[2020-01-22 05:55:03.342] speed 10s/60s/15m n/a n/a n/a H/s max 925.4 H/s
[2020-01-22 05:56:03.404] speed 10s/60s/15m n/a n/a n/a H/s max 925.4 H/s
[2020-01-22 05:57:03.462] speed 10s/60s/15m n/a n/a n/a H/s max 925.4 H/s
[2020-01-22 05:58:03.524] speed 10s/60s/15m n/a n/a n/a H/s max 925.4 H/s
[2020-01-22 05:59:03.587] speed 10s/60s/15m n/a n/a n/a H/s max 925.4 H/s
[2020-01-22 06:00:03.648] speed 10s/60s/15m n/a n/a n/a H/s max 925.4 H/s
[2020-01-22 06:01:03.689] speed 10s/60s/15m n/a n/a n/a H/s max 925.4 H/s
[2020-01-22 06:02:03.728] speed 10s/60s/15m n/a n/a n/a H/s max 925.4 H/s
[2020-01-22 06:02:26.724] Ctrl+C received, exiting
[2020-01-22 06:02:26.903]  cpu  stopped (
```

**Additional context**
Add any other context about the problem here.


# Discussion History
## Spudz76 | 2020-01-27T20:54:37+00:00
Probably related to [this](https://github.com/moby/moby/issues/23910)

Docker doesn't honor your `/etc/resolv.conf` if it has 127.x anything (such as any recent distro with `systemd-resolved` on `127.0.0.53`) and will use `8.8.8.8` which could be blocked elsewhere.

Same link above has hacks to make it work, if your situation is similar.  And some tests to find out what Docker is actually doing.

## snowdream | 2020-02-10T04:15:37+00:00
Thank you,i will check it.

# Action History
- Created by: snowdream | 2020-01-22T06:05:35+00:00
- Closed at: 2020-02-10T04:15:37+00:00
