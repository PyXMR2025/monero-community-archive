---
title: moneo mining
source_url: https://github.com/xmrig/xmrig/issues/3298
author: pitester12
assignees: []
labels: []
created_at: '2023-07-12T22:31:37+00:00'
updated_at: '2025-06-18T22:40:43+00:00'
type: issue
status: closed
closed_at: '2025-06-18T22:40:43+00:00'
---

# Original Description
/xmrig -o 172.0.0.1:3333 --tls -o 127.0.0.1:18081 -u 453ottx4pLWCUxj8c592PS2gTwGQZdh45gjW3PgzotJobi8srydhm5A93ZKKp9Cdp7De5DXC1hFXd252HMvGrJTg7VRxW8H --coin monero --daemon --tls -o pool.supportxmr.com:443 -u 453ottx4pLWCUxj8c592PS2gTwGQZdh45gjW3PgzotJobi8srydhm5A93ZKKp9Cdp7De5DXC1hFXd252HMvGrJTg7VRxW8H -k --tls -p pitester
 * ABOUT        XMRig/6.20.0 gcc/12.2.0
 * LIBS         libuv/1.44.2 OpenSSL/3.0.9 hwloc/2.9.0
 * HUGE PAGES   supported
 * 1GB PAGES    unavailable
 * CPU          ARM Cortex-A72 (1) 64-bit -AES
                L2:1.0 MB L3:0.0 MB 4C/4T NUMA:1
 * MEMORY       1.8/7.6 GB (23%)
 * DONATE       1%
 * POOL #1      172.0.0.1:3333 algo auto
 * POOL #2      127.0.0.1:18081 coin Monero
 * POOL #3      pool.supportxmr.com:443 algo auto
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         disabled
[2023-07-12 18:25:45.694]  net      172.0.0.1:3333 172.0.0.1 connect error: "operation canceled"
[2023-07-12 18:26:10.727]  net      172.0.0.1:3333 172.0.0.1 connect error: "operation canceled"
[2023-07-12 18:26:35.755]  net      172.0.0.1:3333 172.0.0.1 connect error: "operation canceled"
[2023-07-12 18:27:00.784]  net      172.0.0.1:3333 172.0.0.1 connect error: "operation canceled"

i am an inexperienced xmrig miner, and i am in need of assistance with this error
this also happens;
 ./xmrig --donate-level 5 --api-worker-id 172.0.0.1 --http-host 0.0.0.0 --http-port 55689 -o 127.0.0.1:18081 -u 453ottx4pLWCUxj8c592PS2gTwGQZdh45gjW3PgzotJobi8srydhm5A93ZKKp9Cdp7De5DXC1hFXd252HMvGrJTg7VRxW8H --coin monero --daemon --tls -o xmr-us-east1.nanopool.org:14433 -u 453ottx4pLWCUxj8c592PS2gTwGQZdh45gjW3PgzotJobi8srydhm5A93ZKKp9Cdp7De5DXC1hFXd252HMvGrJTg7VRxW8H --tls --coin monero
 * ABOUT        XMRig/6.20.0 gcc/12.2.0
 * LIBS         libuv/1.44.2 OpenSSL/3.0.9 hwloc/2.9.0
 * HUGE PAGES   supported
 * 1GB PAGES    unavailable
 * CPU          ARM Cortex-A72 (1) 64-bit -AES
                L2:1.0 MB L3:0.0 MB 4C/4T NUMA:1
 * MEMORY       1.8/7.6 GB (24%)
 * DONATE       5%
 * POOL #1      127.0.0.1:18081 coin Monero
 * POOL #2      xmr-us-east1.nanopool.org:14433 coin Monero
 * COMMANDS     hashrate, pause, resume, results, connection
 * HTTP API     0.0.0.0:55689 
 * OPENCL       disabled
 * CUDA         disabled
[2023-07-12 18:29:26.193]  net      127.0.0.1:18081 connect error: "connection refused"
[2023-07-12 18:29:31.194]  net      127.0.0.1:18081 connect error: "connection refused"
[2023-07-12 18:29:36.195]  net      127.0.0.1:18081 connect error: "connection refused"
[2023-07-12 18:29:41.197]  net      127.0.0.1:18081 connect error: "connection refused"
[2023-07-12 18:29:46.199]  net      127.0.0.1:18081 connect error: "connection refused"
[2023-07-12 18:29:46.637]  net      use pool xmr-us-east1.nanopool.org:14433 TLSv1.3 142.44.242.100
[2023-07-12 18:29:46.637]  net      fingerprint (SHA-256): "c38886efdee542ebd99801b75c75d3498d97978bbcdec07c7271cb19729e014f"
[2023-07-12 18:29:46.637]  net      new job from xmr-us-east1.nanopool.org:14433 diff 480045 algo rx/0 height 2928411 (60 tx)
[2023-07-12 18:29:46.637]  cpu      use argon2 implementation default
[2023-07-12 18:29:47.839]  randomx  init dataset algo rx/0 (4 threads) seed bcd911cbc3776ed5...
[2023-07-12 18:29:47.840]  randomx  allocated 2336 MB (2080+256) huge pages 0% 0/1168 +JIT (0 ms)
[2023-07-12 18:29:48.935]  net      new job from xmr-us-east1.nanopool.org:14433 diff 480045 algo rx/0 height 2928411 (62 tx)
[2023-07-12 18:29:59.143]  net      new job from xmr-us-east1.nanopool.org:14433 diff 480045 algo rx/0 height 2928411 (64 tx)
[2023-07-12 18:30:09.384]  net      new job from xmr-us-east1.nanopool.org:14433 diff 480045 algo rx/0 height 2928411 (72 tx)
[2023-07-12 18:30:19.420]  net      new job from xmr-us-east1.nanopool.org:14433 diff 480045 algo rx/0 height 2928411 (78 tx)
[2023-07-12 18:30:25.625]  randomx  dataset ready (37785 ms)
[2023-07-12 18:30:25.625]  cpu      use profile  rx  (4 threads) scratchpad 2048 KB
[2023-07-12 18:30:25.627]  cpu      READY threads 4/4 (4) huge pages 0% 0/4 memory 8192 KB (2 ms)
[2023-07-12 18:30:29.457]  net      new job from xmr-us-east1.nanopool.org:14433 diff 480045 algo rx/0 height 2928411 (80 tx)
[2023-07-12 18:30:39.192]  net      new job from xmr-us-east1.nanopool.org:14433 diff 480045 algo rx/0 height 2928411 (82 tx)


it says it is mining but i check my monero wallet and it says 0.00000000


# Discussion History
## SChernykh | 2023-07-13T09:14:11+00:00
```
-o 172.0.0.1:3333
```
It's `-o 127.0.0.1:3333` (not 172), and it will only work if you set up p2pool correctly. Where did you take the command line from? It's better to use command line from pool_mine_example.cmd or solo_mine_example.cmd:
https://github.com/xmrig/xmrig/blob/master/scripts/pool_mine_example.cmd

## pitester12 | 2023-07-13T12:13:12+00:00
I am running kali linux not windows but thanks

## pitester12 | 2023-07-14T15:34:20+00:00
Ok

# Action History
- Created by: pitester12 | 2023-07-12T22:31:37+00:00
- Closed at: 2025-06-18T22:40:43+00:00
