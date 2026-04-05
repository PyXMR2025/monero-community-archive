---
title: rpi4 error on xmrig v.6.7.0
source_url: https://github.com/xmrig/xmrig/issues/1992
author: rlsl
assignees: []
labels: []
created_at: '2020-12-22T01:20:27+00:00'
updated_at: '2021-04-12T14:27:28+00:00'
type: issue
status: closed
closed_at: '2021-04-12T14:27:28+00:00'
---

# Original Description
xmrig does not pass the line in the log that says "cpu ready", so it is not mining, and it does not report any errors, I tested it on my amd notebook and it worked.

compilation: sudo cmake .. -DCMAKE_C_COMPILER=clang-9 -DCMAKE_CXX_COMPILER=clang++-9
run: xmrig --thread=3 --cpu-no-yield --randomx-mode=fast -a cryptonight -o stratum+tcp://xmr.pool.minergate.com:45700 -u xx@x.com -p x --background --log-file=/var/log/xmrig.log --no-color

PS. The previous version v6.6.2 is working perfectly with the same compilation.

----------------------------LOG-----------------------------------------
 * ABOUT        XMRig/6.7.0 clang/9.0.1
 * LIBS         libuv/1.24.1 OpenSSL/1.1.1d hwloc/1.11.12
 * CPU          ARM Cortex-A72 (1) 64-bit -AES
                L2:0.0 MB L3:0.0 MB 4C/4T NUMA:1
 * HUGE PAGES   supported
 * MEMORY       0.2/7.6 GB (3%)
 * DONATE       1%
 * POOL #1      stratum+tcp://xmr.pool.minergate.com:45700 algo cn/0
 * COMMANDS     'h' hashrate, 'p' pause, 'r' resume, 's' results, 'c' connection
 * OPENCL       disabled
 * 1GB PAGES    unavailable
 * CUDA         disabled
[2020-12-21 21:55:42.731]  net      stratum+tcp://xmr.pool.minergate.com:45700 DNS error: "temporary failure"
[2020-12-21 21:55:48.440]  net      stratum+tcp://xmr.pool.minergate.com:45700 DNS error: "temporary failure"
[2020-12-21 21:56:14.467]  net      stratum+tcp://xmr.pool.minergate.com:45700 connect error: "operation canceled"
[2020-12-21 21:56:54.421]  net      stratum+tcp://xmr.pool.minergate.com:45700 connect error: "operation canceled"
[2020-12-21 21:56:59.859]  net      use pool xmr.pool.minergate.com:45700  49.12.80.39
[2020-12-21 21:56:59.860]  net      new job from xmr.pool.minergate.com:45700 diff 1000 algo rx/0 height 2257392
[2020-12-21 21:56:59.860]  cpu      use argon2 implementation default
[2020-12-21 21:57:01.060]  randomx  init dataset algo rx/0 (4 threads) seed fd1813e59eef6d6a...
[2020-12-21 21:57:01.060]  randomx  allocated 2336 MB (2080+256) huge pages 0% 0/1168 +JIT (1 ms)
[2020-12-21 21:57:25.543]  randomx  dataset ready (24483 ms)
[2020-12-21 21:57:25.543]  cpu      use profile  *  (3 threads) scratchpad 2048 KB
[2020-12-21 21:57:25.544]  cpu      READY threads 3/3 (3) huge pages 0% 0/3 memory 6144 KB (1 ms)


# Discussion History
## rlsl | 2021-01-12T03:44:21+00:00
Same error in the new version v6.7.1

## SChernykh | 2021-01-12T08:41:02+00:00
Try another pool, minergate is a known scam. List of Monero pools: https://miningpoolstats.stream/monero

# Action History
- Created by: rlsl | 2020-12-22T01:20:27+00:00
- Closed at: 2021-04-12T14:27:28+00:00
