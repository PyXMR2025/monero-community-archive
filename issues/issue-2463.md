---
title: System crash & parameter malfunction
source_url: https://github.com/xmrig/xmrig/issues/2463
author: UnixCro
assignees: []
labels: []
created_at: '2021-06-28T21:05:22+00:00'
updated_at: '2021-07-01T16:50:21+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Hi,

First of all, before I ask a question and report a bug, I would like to thank you for this great program. In my opinion it is the best miner you can get for the Mac right now. All other miners just cause trouble and trouble and don't love to work. XMRig doesn't know anything like that. That's why I think it's totally justified that a donation takes place there when mining.

So we come to my question. Is it possible to mine with my Radeon Pro 570 on my iMac  `Ethereum` and not inefficient `Monero`?

If I use the `--opencl` parameter with `-a rx/0` my system crashes immediately. I don't know what XMRig is doing, but with this command I have to restart my computer immediately. Can't I somehow get a very low level through the command center?

Why does XMRig not use 400% with a 4 core processor but always only 300% even if the parameter `--cpu-max-threads-hint=100` has been entered?

I found this command. But I get an error message. Any ideas?
```
xmrig --no-cpu --opencl -o kawpow.eu-west.nicehash.com:3385 -a kawpow -u MY_NICEHASH_BTC_ADRESS -p x

[2021-06-28 23:14:06.116]  opencl   error CL_INVALID_GLOBAL_OFFSET when calling clEnqueueNDRangeKernel for kernel progpow_search
[2021-06-28 23:14:06.116]  opencl   thread #0 failed with error CL_INVALID_GLOBAL_OFFSET
```
macOS Big Sur 10.16 Radeon Pro 570 4gb i5 7500

Thank you for your efforts

# Discussion History
## Lonnegan | 2021-06-28T22:11:27+00:00
Your i5 processor has 6 MB of last level cache. RandomX needs 2 MB scratchpad size per thread. That's why xmrig starts 3 threads to reach best performance.

xmrig comes from the Cryptonight scene, so it does not support ETH. You'll have to use another mining software to mine ETH. Besides your RX 570 has only 4 GB RAM. That's not enough anymore for ETH. You need a graphic card with at least 6 GB RAM for ETH.

## Spudz76 | 2021-06-28T22:56:26+00:00
It would mine other supported algos, such as KawPow as it is attempting, except you have to run unreleased code from [my fork, branch fixAppleOpenCL](https://github.com/Spudz76/xmrig/tree/dev-fixAppleOpenCL) until it is finalized into an acceptable master-line patch.  I do not have a public MoneroOcean fork version with those patches included (yet) which would be important for earning XMR out of non-RandomX algorithms.

But for actual Ethereum you'd need to find another miner app, which hopefully supports Apple OpenCL.  Most "AMD" miners are written for the AMD drivers and can use AMD extensions and AMD GCN assembly code, while Apple has wedged their generic OpenCL layer in between and do not support any of that (it will run slower than the identical GPU in a Linux/Windows OS).  And of course you have to have >4GB of VRAM which I guess you may not.  There is an ethash-2GB and a coin or two based on that, which would work, but are not particularly valuable in comparison (and not supported by MoneroOcean either).  KawPow is essentially very much like Ethash also (uses DAG) but with more like 2.5GB of VRAM required, and is supported by xmrig + my patch.

It may still choke out responsiveness of the GUI while mining since there is no support in OpenCL for sleeping between jobs (like there is in CUDA backend).  You may be confusing a completely unresponsive GUI as crashed?  It's just mining so hard there is no time to update the screen more likely.  If you CTRL+C to bust out of the miner does it ever come back (~2 minutes)?  It should also just crash itself out after generating the DAG (which may take a short while).  The normal master/dev branches all crash as soon as they try to actually mine (due to attempting to use AMD extensions that aren't there).

## UnixCro | 2021-06-29T07:10:27+00:00
First of all, thank you very much for the quick and helpful answers @Lonnegan and @Spudz76 

@Lonnegan your contribution really helped me. Now I realized why it only takes 300% due to the low L3 cache. I thought my CPU was defective or something. 

As I can see, almost all of my questions were answered cleanly. I also noticed that `Ethereum` is not working due to the Cryptonight scene, but it could be made to work via detours. Due to my low graphics memory, it would have no added value either way, because I still remember when I started the NiceHash Miner on Macs with Windows and an AMD GPU a benchmarked the individual algorithms always selected the `KawPow` algorithm. I think this is the most efficient for AMD GPUs. The question remains, however, how exactly do I get XMRig to run.

As already described above, I always get an error message. I'll post the entire XMRig issue:


```
xmrig --no-cpu --opencl -o stratum+tcp://kawpow.eu-west.nicehash.com:3385 -a kawpow -u  MY_NICEHASH_BTC_ADRESS -p x 

[2021-06-29 08:52:19.201] Error CL_INVALID_OPERATION when calling clGetDeviceInfo, param 0x4037
 * ABOUT        XMRig/6.12.2 clang/10.0.0
 * LIBS         libuv/1.41.0 OpenSSL/1.1.1k hwloc/2.4.1
 * HUGE PAGES   supported
 * 1GB PAGES    unavailable
 * CPU          Intel(R) Core(TM) i5-7500 CPU @ 3.40GHz (1) 64-bit AES
                L2:1.0 MB L3:6.0 MB 4C/4T NUMA:1
 * MEMORY       7.4/16.0 GB (46%)
                DIMM0: 4 GB DDR4 @ 2400 MHz 0x344154463531323634485A2D3247334232202020
                DIMM1: 4 GB DDR4 @ 2400 MHz 0x344154463531323634485A2D3247334232202020
                DIMM0: 4 GB DDR4 @ 2400 MHz 0x344154463531323634485A2D3247334232202020
                DIMM1: 4 GB DDR4 @ 2400 MHz 0x344154463531323634485A2D3247334232202020
 * MOTHERBOARD  Apple Inc. - Mac-BE088AF8C5EB4FA2
 * DONATE       10%
 * ASSEMBLY     auto:intel
 * POOL # 1      stratum+tcp://kawpow.eu-west.nicehash.com:3385 algo kawpow
 * COMMANDS     hashrate, pause, resume, results, connection
[2021-06-29 08:52:19.206] Error CL_INVALID_OPERATION when calling clGetDeviceInfo, param 0x4037
 * OPENCL       #0 Apple/OpenCL 1.2 (May  8 2021 03:14:28)
 * OPENCL GPU   #0 n/a AMD Radeon Pro 570 Compute Engine 1000 MHz cu:28 mem:1024/4096 MB
 * CUDA         disabled
[2021-06-29 08:52:19.290]  net      use pool kawpow.eu-west.nicehash.com:3385  172.65.226.105
[2021-06-29 08:52:19.291]  net      new job from kawpow.eu-west.nicehash.com:3385 diff 350M algo kawpow height 1819054
[2021-06-29 08:52:19.291]  opencl   use profile  kawpow  (1 thread) scratchpad 32 KB
|  # | GPU |  BUS ID | INTENSITY | WSIZE | MEMORY | NAME
|  0 |   0 |     n/a |   7340032 |   256 |   3006 | AMD Radeon Pro 570 Compute Engine
[2021-06-29 08:52:19.292]  opencl   READY threads 1/1 (2 ms)
[2021-06-29 08:52:19.295]  opencl   KawPow program for period 606351 compiled (3ms)
[2021-06-29 08:52:19.297]  opencl   KawPow program for period 606352 compiled (2ms)
[2021-06-29 08:52:26.039]  miner    KawPow light cache for epoch 242 calculated (6744ms)
[2021-06-29 08:52:26.052]  opencl   KawPow DAG for epoch 242 calculated (4ms)
[2021-06-29 08:52:26.780]  opencl   error CL_INVALID_GLOBAL_OFFSET when calling clEnqueueNDRangeKernel for kernel progpow_search
[2021-06-29 08:52:26.780]  opencl   thread #0 failed with error CL_INVALID_GLOBAL_OFFSET
[2021-06-29 08:52:34.119]  net      new job from kawpow.eu-west.nicehash.com:3385 diff 350M algo kawpow height 1819055
```

Even if it is indicated that there is a new job and is allegedly mined, this is not true and no hashrate is displayed. 

<br>

> @Spudz76  You may be confusing a completely unresponsive GUI as crashed? It's just mining so hard there is no time to update the screen more likely. If you CTRL+C to bust out of the miner does it ever come back (~2 minutes)?

I can fade in the command. As soon as I entered that and a few seconds after that, the entire screen froze. Nothing worked anymore. Exiting with the control buttons was also unfortunately unsuccessful. I then had to restart the computer because there was nothing else to do.

```
xmrig --no-cpu --opencl -o stratum+tcp://randomxmonero.eu-west.nicehash.com:3380 -a rx/0 -u MY_NICEHASH_BTC_ADRESS -p x 
```

This whatsoever command freezes my Mac. As I noticed, it doesn't matter whether you leave `--no-cpu` on or not. It comes out the same.


## SChernykh | 2021-06-29T07:19:45+00:00
I found this description of the error you get:
> `CL_INVALID_GLOBAL_OFFSET` if the value specified in global_work_size + the corresponding values in global_work_offset for any dimensions is greater than the sizeof(size_t) for the device on which the kernel execution will be enqueued.

I don't see how it can happen looking at the code. `global_work_offset+global_work_size` always fits in 32 bits there, so probably it's a driver bug again. OpenCL support on Mac is very bad.



## Spudz76 | 2021-06-30T18:16:04+00:00
The fork and branch I linked will work you need to checkout and compile it.  It removes all the assumptions that AMD extensions work on AMD devices.

## UnixCro | 2021-06-30T18:20:13+00:00
@Spudz76 I honestly don't know how to run your code. I am redirected to a page where the same xmrig file is in the readme file at release. If I download your source code directly from the repository, I don't know what to do afterwards. Can you help me with that? 

## Spudz76 | 2021-07-01T15:13:24+00:00
https://xmrig.com/docs/miner/build

Same directions except you clone my branch instead of xmrig mainstream, and `git checkout dev-fixAppleOpenCL`

## UnixCro | 2021-07-01T16:36:37+00:00
I also saw it on your previous link and it was the one here: (https://github.com/Spudz76/xmrig/tree/dev-fixAppleOpenCL)
Since the above, so the one here (https://xmrig.com/docs/miner/build), brings me to the completely normal side of xmrig that I want to compile something. And I always avoid it when something has to be compiled. Because it just causes trouble. 

I then changed to the directory with `cd` and then, as you mentioned, entered the command `git checkout dev-fixAppleOpenCL` Output:

```
Branch 'dev-fixAppleOpenCL' set up to track remote branch 'dev-fixAppleOpenCL' from 'origin'.
Switched to a new branch 'dev-fixAppleOpenCL'
```
Even if I now run the correct XMRig program, I get the same error message. I would like XMRig to simply take note of this error message and publish a new program that does not contain this error message. 

By the way, to the developers . Even in the hope that a specially made miner could possibly solve this problem remained unsuccessful. Since the `XMRig-AMD` miner cannot even be run on the[ macOS operating systems](https://github.com/xmrig/xmrig-amd/issues/303). 

Greeting
UnixCro

# Action History
- Created by: UnixCro | 2021-06-28T21:05:22+00:00
