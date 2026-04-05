---
title: ' XMRig 6.8.1 nvidia   disabled (no suitable configuration found)'
source_url: https://github.com/xmrig/xmrig/issues/2099
author: you-die
assignees: []
labels: []
created_at: '2021-02-12T17:51:52+00:00'
updated_at: '2022-03-19T23:29:50+00:00'
type: issue
status: closed
closed_at: '2021-04-12T14:15:28+00:00'
---

# Original Description
Hi,

I can't figure out how to configure gpu options. Still have this message :
nvidia disabled (no suitable configuration found)

Maybe you can help ? I can't find lot of documentation around theses conf.

Here is the log :

 * ABOUT        XMRig/6.8.1 gcc/10.2.0
 * LIBS         libuv/1.40.0 OpenSSL/1.1.1i hwloc/2.4.0
 * HUGE PAGES   permission granted
 * 1GB PAGES    unavailable
 * CPU          Intel(R) Core(TM) i5-5200U CPU @ 2.20GHz (1) 64-bit AES
                L2:0.5 MB L3:3.0 MB 2C/4T NUMA:1
 * MEMORY       3.9/7.9 GB (49%)
                DIMM_A0: 4 GB DDR3 @ 1600 MHz HMT451S6AFR8A-PB
                DIMM_B0: 4 GB DDR3 @ 1600 MHz
 * MOTHERBOARD  ASUSTeK COMPUTER INC. - X455LDB
 * DONATE       1%
 * ASSEMBLY     auto:intel
 * POOL #1      pool.hashvault.pro:3333 algo auto
 * COMMANDS     hashrate, pause, resume, results, connection
[2021-02-13 00:28:34.175]  config   configuration saved to: "D:\ETH Mining setup\xmrig-6.8.1-gcc-win64\sample\xmrig-6.8.1\config.json"
 * OPENCL       disabled
 * CUDA         8.0/9.1/6.5.0
 * NVML         9.388.73/388.73 press e for health report
 * CUDA GPU     #0 04:00.0 GeForce 820M 1250/900 MHz smx:2 arch:21 mem:1687/2048 MB
[2021-02-13 00:28:34.380]  net      use pool pool.hashvault.pro:3333  131.153.76.130
[2021-02-13 00:28:34.380]  net      new job from pool.hashvault.pro:3333 diff 72000 algo rx/0 height 2295343
[2021-02-13 00:28:34.381]  cpu      use argon2 implementation AVX2
[2021-02-13 00:28:34.528]  msr      register values for "intel" preset have been set successfully (147 ms)
[2021-02-13 00:28:34.528]  randomx  init dataset algo rx/0 (4 threads) seed d4668d8487123de2...
[2021-02-13 00:28:34.612]  randomx  allocated 2336 MB (2080+256) huge pages 0% 0/1168 +JIT (83 ms)
[2021-02-13 00:28:50.022]  randomx  dataset ready (15409 ms)
[2021-02-13 00:28:50.022]  cpu      use profile  rx  (2 threads) scratchpad 2048 KB
[2021-02-13 00:28:50.024]  nvidia   disabled (no suitable configuration found)
[2021-02-13 00:28:50.251]  cpu      READY threads 2/2 (2) huge pages 0% 0/2 memory 4096 KB (227 ms)
[2021-02-13 00:29:50.184]  nvidia   #0 04:00.0   0W 91C fan0:0%
[2021-02-13 00:29:50.184]  miner    speed 10s/60s/15m 288.5 n/a n/a H/s max 310.2 H/s
[2021-02-13 00:30:00.315]  net      new job from pool.hashvault.pro:3333 diff 37241 algo rx/0 height 2295343
[2021-02-13 00:30:00.316]  nvidia   disabled (no suitable configuration found)
[2021-02-13 00:30:01.273]  net      new job from pool.hashvault.pro:3333 diff 37241 algo rx/0 height 2295343
[2021-02-13 00:30:01.274]  **nvidia   disabled (no suitable configuration found)**

# Discussion History
## Lonnegan | 2021-02-16T14:28:46+00:00
First of all, RandomX is a CPU only algo. It doesn't make sense to mine a RandomX coin like Monero via GPU. Even the fastest GPUs in the world are slower here than modern CPUs. That was the design goal for RandomX and it has been reached.

Secondly, in your special case your GPU is so slow, that it cannot contribute anything useful to your mining power, even if you'd mine a GPU algo. Simply don't use it and save the energy :)

If you want to use it despite of all warnings ;) mine Monero only on the CPU and try to mine something like Haven or BTG on your GPU. Ethereum, Ethereum Classic and Ravencoin isn't possible anymore because the VRAM is too small for that, but Haven or BTG or Turtlecoin could still be possible perhaps. The first two coins are supported by xmrig, as well. :D But you have to use a second instance with a different config.json and start it in addition to your Monero instance of xmrig.

## Spudz76 | 2021-02-17T03:06:12+00:00
RandomX, AstroBWT, and KawPow do not work with CUDA below 9

Fermi core (arch 20, 21) do not work with CUDA above 8

Therefore, you can't use any of those three algo families on your arch 21 GPU

Also RandomX on GPUs is a pointless waste of watts even if it did work.

Best two algos for Fermi are CN-Heavy or CN-GPU (but you need MoneroOcean fork to get CN-GPU back)

## hotheadhacker | 2021-08-06T18:08:34+00:00
you need to disable cpu mining

## floppy69 | 2022-03-19T23:29:50+00:00
> you need to disable cpu mining

thanks for the hint !

Works well on centos 7 with Cuda 8 and XMRig/6.16.4

# Action History
- Created by: you-die | 2021-02-12T17:51:52+00:00
- Closed at: 2021-04-12T14:15:28+00:00
