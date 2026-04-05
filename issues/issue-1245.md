---
title: Hashrate drop on CPU when mining with GPU
source_url: https://github.com/xmrig/xmrig/issues/1245
author: Amf1k
assignees: []
labels:
- bug
created_at: '2019-10-15T10:29:00+00:00'
updated_at: '2021-04-12T15:32:11+00:00'
type: issue
status: closed
closed_at: '2021-04-12T15:32:11+00:00'
---

# Original Description
When launched only on the CPU, the hashrate is ~225 h/s and even less to ~180 h/s
![cpu only](https://user-images.githubusercontent.com/4735986/66823229-403a3980-ef5f-11e9-9fda-2e53ba8e8856.png)

When launched only on the GPU , the hashrate is ~260 h/s
![gpu only](https://user-images.githubusercontent.com/4735986/66823377-8d1e1000-ef5f-11e9-9bcf-001c19e88a50.png)

When starting the CPU and GPU, the hashrate on the CPU is ~120 h/s and drops to ~80 h/s or even less, the hashrate on the GPU is ~260 h/s
![cpu+gpu](https://user-images.githubusercontent.com/4735986/66823764-5694c500-ef60-11e9-9853-ab2cd560f094.png)



# Discussion History
## Amf1k | 2019-10-24T05:47:20+00:00
@xmrig Hey. will there be any corrections?

## ilmerovingio | 2019-10-25T09:28:16+00:00
Same issue on Ryzen Threadripper 1950 and RX580 with CN/R algo and XMRig 4.4.

>  * ABOUT        XMRig/4.4.0-evo gcc/8.3.0
>  * LIBS         libuv/1.24.1 OpenSSL/1.1.1d hwloc/1.11.5
>  * CPU          AMD Ryzen Threadripper 1950X 16-Core Processor (1) x64 AES
>                 L2:8.0 MB L3:32.0 MB 16C/32T NUMA:2
>  * ASSEMBLY     auto:ryzen

>  * OPENCL       #0 AMD Accelerated Parallel Processing/OpenCL 2.1 AMD-APP (2527.3)
>  * OPENCL GPU   #0 41:00.0 Radeon RX 580 Series (Ellesmere) 1340MHz cu:36 mem:3258/4082 MB
> * cpu  use profile  *  (19 threads) scratchpad 2048 KB
> * ocl  use profile  cn/2  (2 threads) scratchpad 2048 KB
> 

When mining CPU alone (limited to 19 threads and XMRig 3.2.x) the hashrate is about 950h/s.  With OpenCL AMD (XMRig 4.4) it drastically drops down to 90h/s.


## xmrig | 2019-10-25T10:59:07+00:00
I unable to reproduce this issue, I checked on Windows 10 (19.9.2 driver) and Ubuntu 18.04 (rocm and recent AMD driver) and didn't notice any hashrate drop.

Try update driver and/or check abnormal CPU usage, for example with one CPU thread or disabled CPU backend.
Thank you.

## ari2asem | 2019-10-26T08:56:52+00:00
i am having the same issue.

cpu only => mining ar around 1000 hashes / s
cpu + gpu mining => cpu mining drops to around 200 hashes (from 1000 to 200)

and, no. no any background task eating my cpu

hardware: asus z10pe-d8 ws (dual socket 2011 v3)
cpu: dual xeon e5-2680v3

using latest nvidia drivers (431.86)
using latest versions of cpu and gpu miners
windows 10, 64bit, version 1903

## xmrig | 2019-10-26T09:40:41+00:00
@ari2asem You mention nvidia drivers, so you got same issue if use external NVIDIA miner?
Thank you.

## ari2asem | 2019-10-26T11:15:02+00:00
@xmrig what do you mean by: "external nvidia miner" ?

i mine with cpu miner and nvidia miner. meaning running 2 miners program together (xmrig-4.4.0-beta.exe and xmrig-nvidia.exe)

if i stop (or pause) nvidia miner, my cpu miner hashrate goes to around 1000 hashes (with 2" xeon e5-2680 v3 cpu's).

if i stop (or pause) cpu miner, my nvidia miner hashrates are the same. so, this is NOT my issue.

my issue begins when i run 2 miners together (xmrig-4.4.0-beta.exe and xmrig-nvidia.exe), dropping hashrate of cpu (xmrig-4.4.0-beta.exe) from 1000 (only cpu mining) to 200 hashes (when also xmrig-nvidia.exe is running)

## Spudz76 | 2019-11-03T21:07:35+00:00
@ari2asem - I run exactly like that also and do not have this issue.  It may dump a few H/s off the CPU side but not a huge difference like you are seeing.

Also this thread is about the unified 4.x xmrig which has OpenCL and CUDA inside the main xmrig along with simultaneous CPU, which is why we assumed you were not running them separate and suggested that.

You could assign some affinities to things so that the CUDA traffic is on a core that is not mining, or on a "fake core" one of the HT ones.  Otherwise it could be awaiting some CUDA work with a blocking method and thus getting in the way (and evicting cache maybe?).  I have always affined my threads manually, which could be why I never saw this problem.  Automatic could be swapping which core is handling things, and making bad decisions, which could also be related to junk BIOS (NUMA definitions wrong).

## Spudz76 | 2019-11-03T21:16:17+00:00
@ari2asem - Another thing, if your CUDA miner is running too low difficulty (wrong pool port, or bad autodiff) then the CPU will be choked with verification of each job the GPU completed.  You don't want more than one or two completions per minute or it definitely will fight with the CPU miner.

## ari2asem | 2019-11-03T23:58:28+00:00
@Spudz76 rigth now running xmrig v4.5.0 with built-in cuda miner, hashrate of totall 4800-4900, combined cpu and gpu (thus cpu and gpu mining at the same time with xmrig 4.5.0)

running only cuda part of xmrig 4.5.0 with 4600 H/s 

running only cpu part of xmrig 4.5.0 with 1100 H/s (30/30 threads according xmrig 4.5.0)

this should give hashrate about 4600+1100=5700. but i get 4800-4900

running on pool of supportxmr, tried ports 3333, 7777 and 9000. all the same result as above. so pool and port are not the reason.

in bios is everything default, nothing tweaked or changed

# Action History
- Created by: Amf1k | 2019-10-15T10:29:00+00:00
- Closed at: 2021-04-12T15:32:11+00:00
