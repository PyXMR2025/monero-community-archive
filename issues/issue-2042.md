---
title: Why is it only using 16 threads when it knows there are 24?
source_url: https://github.com/xmrig/xmrig/issues/2042
author: dsw-solutions
assignees: []
labels: []
created_at: '2021-01-16T19:19:46+00:00'
updated_at: '2021-01-17T05:55:14+00:00'
type: issue
status: closed
closed_at: '2021-01-17T01:59:32+00:00'
---

# Original Description
 * ABOUT        XMRig/6.7.2 gcc/9.3.0
 * LIBS         libuv/1.34.2 OpenSSL/1.1.1f hwloc/2.1.0
 * HUGE PAGES   supported
 * 1GB PAGES    unavailable
 * CPU          Common KVM processor (2) 64-bit -AES VM
                L2:96.0 MB L3:32.0 MB **24C/24T** NUMA:2
 * MEMORY       4.8/5.8 GB (83%)
 * DONATE       1%
 * ASSEMBLY     auto:none
 * POOL #1      pool.supportxmr.com:443 algo auto
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         disabled
[2021-01-16 19:16:52.291]  net      use pool pool.supportxmr.com:443 TLSv1.2 107.178.104.10
[2021-01-16 19:16:52.291]  net      fingerprint (SHA-256): "69102268332371e7267eb5d5e9c5d7f8e4688bd0a5d9171243f37fa031d94302"
[2021-01-16 19:16:52.291]  net      new job from pool.supportxmr.com:443 diff 50000 algo rx/0 height 2275984
[2021-01-16 19:16:52.291]  cpu      use argon2 implementation SSE2
[2021-01-16 19:16:53.491]  randomx  init datasets algo rx/0 (**24 threads**) seed c16b9816e30cf2bc...
[2021-01-16 19:16:54.071]  randomx  #0 allocated 2080 MB huge pages 100% (580 ms)
[2021-01-16 19:16:54.072]  randomx  #1 allocated 2080 MB huge pages 100% (581 ms)
[2021-01-16 19:16:54.108]  randomx  #0 allocated  256 MB huge pages 100% +JIT (37 ms)
[2021-01-16 19:16:54.108]  randomx  -- allocated 4416 MB huge pages 100% 2208/2208 (618 ms)
[2021-01-16 19:16:56.397]  randomx  #0 dataset ready (2289 ms)
[2021-01-16 19:16:56.648]  randomx  #1 dataset ready (250 ms)
[2021-01-16 19:16:56.648]  cpu      use profile  rx  (16 threads) scratchpad 2048 KB
[2021-01-16 19:16:56.659]  cpu      READY threads **16/16 (16)** huge pages 100% 16/16 memory 32768 KB (12 ms)


# Discussion History
## Lonnegan | 2021-01-16T23:20:29+00:00
xmrig uses only 16 threads, because each RandomX thread has a scratchpad size of 2 MB and your CPU has a last level cache of only 32 MB. So you can run just 16 threads without flooding the cache. Using more means, that the scratchpads won't fit into the cache, the CPU has to access to slow DRAM instead, which makes the hasrates go down.

## xmrig | 2021-01-17T05:25:50+00:00
1. You use virtual machine and it report wrong CPU topology, so auto-config not work properly, you must use [manual configuration](https://github.com/xmrig/xmrig/blob/master/doc/CPU.md). How many threads you should use is unknown, it depends on the host CPU.
2. You should force enable hardware AES support https://github.com/xmrig/xmrig/blob/master/src/config.json#L32 `"hw-aes": true,` likely it will work.

## dsw-solutions | 2021-01-17T05:55:14+00:00
It is a dual E5-2698 v3 system and I setup the VM with 2 sockets with 12 cores on each.

# Action History
- Created by: dsw-solutions | 2021-01-16T19:19:46+00:00
- Closed at: 2021-01-17T01:59:32+00:00
