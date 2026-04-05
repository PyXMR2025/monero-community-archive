---
title: CPU consumption of OpenCL vs CUDA
source_url: https://github.com/xmrig/xmrig/issues/2294
author: clflush
assignees: []
labels: []
created_at: '2021-04-21T06:20:59+00:00'
updated_at: '2021-04-24T13:56:45+00:00'
type: issue
status: closed
closed_at: '2021-04-24T13:56:45+00:00'
---

# Original Description
Hi, I am mining XMR on 2 Xeon machines. On these 2 machines, I had to put in GPUs, one with 750Ti, the other with RX550. Since they are there, I thought might as well mine Astrobwt. That was when I noticed a significant randomx hashrate dropping when i started the xmrig opencl mining (no-cpu option), which is not happening on the machine mining Astrobwt using xmrig cuda. Any ideas why it is like that?

# Discussion History
## clflush | 2021-04-22T01:53:23+00:00
Further testing (with MoneroOcean and its modified algo switching xmrig) showed that mining using AMD GPU, regardless of the algo, will take away RandomX hashrates. I suspect something similar for Nvidia too but the effect is less obvious. I wonder if it is the devices itself or is the mining code's issue? 

If it is the devices, I would just switch out my AMD with Nvidia. If it is the code, would it be fixable?

## Spudz76 | 2021-04-23T06:12:22+00:00
You can set the affinity of the GPU handler thread to stay on a cpu/core that is not mining.  Otherwise it jumps around or parks wherever it likes, whenever it likes.

Linux or Windows?  Sometimes the Windows drivers freak out when there is also an Intel iGPU and driver.  DDU to the ground and install only the AMD driver.  Possibly also use the option in DDU to block automatic driver installation through Windows Update (or it will put the Intel driver back).  I have never noticed any problem dual-wield with Linux.

## clflush | 2021-04-23T07:25:20+00:00
> You can set the affinity of the GPU handler thread to stay on a cpu/core that is not mining. Otherwise it jumps around or parks wherever it likes, whenever it likes.
> 
> Linux or Windows? Sometimes the Windows drivers freak out when there is also an Intel iGPU and driver. DDU to the ground and install only the AMD driver. Possibly also use the option in DDU to block automatic driver installation through Windows Update (or it will put the Intel driver back). I have never noticed any problem dual-wield with Linux.

Hey thanks! Will try to set the affinity. 
Linux.

## clflush | 2021-04-23T14:17:14+00:00
hey, Just want to give a quick update on my test. So setting affinity works!! 

And I verified that xmrig opencl is consuming cpu compared to xmrig cuda, the latter being almost negligible. Verified on 4 different machines, 2 cuda and 2 opencl.

## Spudz76 | 2021-04-23T19:03:57+00:00
CPU mining is sensitive to being cache-evicted as most of its speed happens by loading cache once and then operating on it with ultra low latency.  Other tasks step in on that core and interrupt the miner forcing it to reload cache again.

I have never bothered to set affinity, maybe I should.  Sometimes mining actually uses all cores so there is nowhere to park the GPU-xfer thread.  But usually there is at least a "fakecore" from HT that doesn't help mining (on most algos)...

## clflush | 2021-04-24T13:56:45+00:00
Thanks for your suggestion. Prob true for Ryzen, with less cores but large L2 (yes, not L3). Intel, on the other hand, because of L2, cannot make full use of all the cores. Its almost like RandomX was targeted for Ryzen. 

In any case, if a Ryzen user whom setting affinity did not help, can re-open the case. 

# Action History
- Created by: clflush | 2021-04-21T06:20:59+00:00
- Closed at: 2021-04-24T13:56:45+00:00
