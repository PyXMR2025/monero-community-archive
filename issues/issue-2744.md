---
title: Feature request Ghostrider on GPU (OpenCL/Cuda)
source_url: https://github.com/xmrig/xmrig/issues/2744
author: phil2sat
assignees: []
labels: []
created_at: '2021-11-29T02:03:50+00:00'
updated_at: '2021-12-08T09:44:09+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I know all the cons, but on my apu which is rated @25W, it  would be a nice benefit to use the APU for a little bit more hashes.

Actual everything seems fine, but: opencl   disabled (no suitable configuration found)

Thanks for your work

Phil2Sat

# Discussion History
## Lonnegan | 2021-11-29T18:15:21+00:00
If you use your APU's iGPU for mining additionally, however, that will slow down the CPU since they share a TDP budget. Whether that will be faster than just using the CPU?

## phil2sat | 2021-11-29T22:22:04+00:00
We will only know if we prove it, maybe yes, mabe no. 

## Spudz76 | 2021-11-29T23:36:40+00:00
Generally yes, most iGPU architectures share at least the memory bus, and sometimes a chunk of cache, which tend to clash.

If anyone ever makes an iGPU with on-die HBM entirely for it without sharing cache or memory with the CPU cores, then it would be quite viable.

## phil2sat | 2021-11-30T11:08:57+00:00
since the ddr4 specs in xmrig infos and the actual hashrate on my 4700u, there should be plenty of bandwidth available

as far as i remember ddr4 3200 up to 6000H/s

4700u does average 1000H/s
guessing igpu does additional 100h/s

do the math..

And its not only for iGPU's some ppl want to mine on real cards

## nutsnox | 2021-11-30T17:27:14+00:00
IMO This concept makes more sense for discrete GPU than iGPU as iGPU shares resources with the CPU and you could end up with worse performance.

For iGPU I would think that you'd have to pick one or the other to take the work (i.e. depending on what job you get and determining whether iGPU or CPU would be better). I would think that this logic would be really tough to mete out since iGPU performance varies across generations.

## Spudz76 | 2021-11-30T17:29:27+00:00
Pretty pointless splitting hairs, since supporting any GPU also supports iGPUs.  OpenCL is OpenCL...

## phil2sat | 2021-11-30T17:53:37+00:00
Right, its not about implementing a new GPU, i want raptoreum protocol for gpu, since my card is already supported, Vega stays Vega, as long the underlaying parts like kernel, rocm and OpenCl supports it.

Btw Wildrig already supports ghostrider over GPU.

But why have two Miner running if one can do both

## use-dashes-instead | 2021-12-03T00:23:01+00:00
Spudz76 likes to hear himself talk, so don't worry too much about what he has to say

## phil2sat | 2021-12-07T06:40:35+00:00
> Spudz76 likes to hear himself talk, so don't worry too much about what he has to say

pretty sure, yours was the only complete useless and off topic comment here. And what Spudz76 said is nothing more than a fact. 

## use-dashes-instead | 2021-12-07T13:52:15+00:00
> what Spudz76 said is nothing more than a fact.

It's not true, but carry on young trolls, carry on....

## phil2sat | 2021-12-08T09:44:09+00:00
Mhmm, wonder why i can mine Ravencoin Kawpow on my VEGA iGPU at 1.91MH/s while my CPU does average 830H/s using XMRig.

Ah cause its not supported.

For the Speed, it has no Impact on Speed, running two instances, one for CPU and one for iGPU.

Under the line its dubling my crypto income for now.

The only thing i had to do was extra cooling for my laptop.

Request still open, Raptoreum config for GPU

# Action History
- Created by: phil2sat | 2021-11-29T02:03:50+00:00
