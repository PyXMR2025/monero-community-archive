---
title: Integrate UsethlessMiner for CPU-based KAPOW and ETHHASH mining
source_url: https://github.com/xmrig/xmrig/issues/2877
author: hilga007
assignees: []
labels: []
created_at: '2022-01-19T08:39:45+00:00'
updated_at: '2022-03-04T13:40:38+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
**Describe the bug**
Feature request: Integrate https://github.com/Chainfire/UselethMiner to utilize CPU to mine ETHHASH and KAPOW. 

**To Reproduce**
n/a

**Expected behavior**
Be able to compile xmrig with usethlessminer backend for cpu mining of KAPOW and ETHHASH

**Required data**
source: **https://github.com/Chainfire/UselethMiner**
**Additional context**
Geth would be another route, but useleth seems to be fastest. Making note of this to work on pull request and fiddling around if there is time. 


# Discussion History
## Spudz76 | 2022-01-19T15:34:12+00:00
But what for, five hashes per second?

## hilga007 | 2022-01-21T02:42:37+00:00
> But what for, five hashes per second?

It seems a 7700HQ gets about 1.1MH/s which is about what a Vega 3 iGPU gets with OpenCL or an M1+GPU7 gets with OpenCL (both around 1.5H/s). The 2nd gen Trheadripper looks unpleasant: however Apple Silicon performance far surpasses other miner's performance (including my fav, XMRig) when it comes to Apple Silicon (even beating W/H for a 1080 ti...). Ryzen 3000, 5000, Intel Core 10th-12th gens have not been benchmarked though due to process and arch changes are viable mining canditates. Again: the largest gains are with Apple Silicon which could see an idle MacBook Pro or Mac mini churning out the h/s. 

This table is ripped from their info man: 



CPU | Threads | MT | Watt | MH | W/MH | Notes
-- | -- | -- | -- | -- | -- | --
TR 2950x | 16 | 4x2933 | 115 | 6.1 | 18.9 | 1
i7-7700HQ | 4 | 2x2400 | 9 | 1.1 | 8.2 | 2
AS M1 | 8 | 8x4266 | 14 | 4.0 | 3.5 | 3
AS M1 Max CPU | 10 | 8x6400 | 40 | 10.4 | 3.8 | 4
AS M1 Max GPU | - | 8x6400 | 24 | 10.3 | 2.3 | 4
AS M1 Max CPU+GPU | 10 | 8x6400 | 62 | 20.0 | 3.4 | 4
GKE Xeon | 2 | - | - | 0.6 | - | 5
1080 ti | - | - | 180 | 32.0 | 5.6 | 6

---- 

Regarding Apple Silicon: I have compiled via xterm after installing OpenCL headers. I haven't gotten around to trying the OpenCL --> Vulkan --> MoltenVK --> Metal wrappers yet. Its "on the radar." 

That being said: it looks like the bulk of the work has been handled already by uthelessminer which doesn't look so useless afterall, but instead would expand upon the portfolio XMRig offers. 

- Massive KAPOW performance improvements on AS M1/Max/Pro/etcblah + CPU mining on other platforms? **check**
- Gateway to metal-based rx/0, etc mining on Apple Silicon and/or CPU+GPU hybrid mining to make up for the loss of huge pages? **check**
- Gateway to Vulkan-based cross-platform GPU mining for rx/0 and kapow? **check**
- Gateway for someone to script out dynamic GPU/CPU/OpenCL/Metal/Vulkan, etc blah changes for algorithms depending on device-specific hashing per watt vs exchange rate performance? Yup. 

Side note 1: I first switched to xmrig in 2018? 2019? Something like that... anyway I switched due to frustrations with GPU mining support on other clients after the monero fork and xmrig took care of those issues. Strongly ++ greatly approve of everyone setting their devfees higher for the work being done here. 

Side note 2: Heck when compiling with CUDA 11.6 toolkit on Ubuntu 22.04 with kernel 5.16.1 and nvidia 510.x driver: CUDA mining performance outpaces that of trex on the same system. Uber-impressive. 

**Rant Conclusion:** XMRig has been a limited-scope yet multi-purpose miner that seeks to serve its users through unmatched CPU mining performance (especially when compiled with native compiler e.g. AOCC on Ryzen) as well as offering OpenCL and CUDA mining of our favorite algorithms ++ KAPOW. Adding in "utheless" functionality would allow xmrig to further expand its dynamic portability and unmatched performance whilst remaining in-scope of its now-core algorithms. 

**Rant Conclusion's Conclusion:** Diversifying hardware mining capability for the key algorithms enables an even broader range of hardware to be utilized to maximum potential resulting in more of those delicious, delicious hashes. 

Example Use Case:

- Ryzen 5600X + RTX 2080 
- Core i9-9900S Engineering Sample + Integrated HD (640?) 
- Athlon 3000G + Vega 3 iGPU
- MacBook Air Core i7-55xxU + Intel HD 6000 GPU
- Intel NUC Atom Z4xxx + Intel HD ??
- Intel Compute Stick 
- Raspberry Pi 3
- Raspberry Pi 4
- VIA "Isiah" 8-Core + Nvidia 1050 ti 
- Intel Pentium G4200 + Radeon R9 290X 
- MacBook Air M1 
- (Mac mini pending M1 Max or "M2" gen)
 
In this case there are plenty of compute resources here that, if balanced correctly manually and eventually (manually) automated could result in the perfect fine-tuning for automatic mining on CPU and GPU resources of all available algorithms based on h/W and active exchange rate.

This level of granularity and control to maximize profitability of all available compute resources is within the realm of reason thanks to the amazing dev team here, and the availability of a parallel open source project to enhance, not detract from, the one here. 




## risner | 2022-03-04T13:40:38+00:00
> **Required data** source: **https://github.com/Chainfire/UselethMiner** **Additional context** Geth would be another route, but useleth seems to be fastest. Making note of this to work on pull request and fiddling around if there is time.

No code right? So how would xmrig integrate innovations? Decompile the binary?

# Action History
- Created by: hilga007 | 2022-01-19T08:39:45+00:00
