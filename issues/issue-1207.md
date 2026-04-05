---
title: Problem with Opencl on gtx 760
source_url: https://github.com/xmrig/xmrig/issues/1207
author: iEsse
assignees: []
labels:
- bug
- review later
created_at: '2019-09-29T15:23:00+00:00'
updated_at: '2021-04-12T15:54:13+00:00'
type: issue
status: closed
closed_at: '2021-04-12T15:54:13+00:00'
---

# Original Description
Hello, here is the problem with opencl on gtx760, how can i solve it ?
![Безымянный](https://user-images.githubusercontent.com/35467897/65834671-dda63400-e2f6-11e9-86fd-cede39d74271.png)


# Discussion History
## xmrig | 2019-09-29T15:56:58+00:00
Probably should reduce `intensity`, I still no checked OpenCL implementation on NVIDIA hardware, anyway CUDA is coming for it.
Thank you.

## iEsse | 2019-09-30T17:44:45+00:00
Reducing intensity didn't help. Moreover it caused another error, in addition when i set intensity lower then 64 it drops till 56. It all happens on "rx/wow" algo, but only on "cn/gpu" opencl works normally. 
![Безымянный2](https://user-images.githubusercontent.com/35467897/65902369-b8d3be80-e3d3-11e9-976c-abb3b43cdf42.png)


## Spudz76 | 2019-10-29T21:24:38+00:00
You don't have enough memory to run RandomX, it requires >2GB to even begin

## iEsse | 2019-10-30T01:40:41+00:00
> You don't have enough memory to run RandomX, it requires >2GB to even begin

Gtx 760 has 2gb of ram, so it's a bug

## Spudz76 | 2019-11-03T20:20:47+00:00
`>2GB` means more than, like 4GB
2GB == 2048MB which is smaller than the 2080MB minimum before scratchpads, and even then that's without the OS or other stuff reserving some of the memory (never seen a 2GB show 2048MB free even when display is not connected and no GUI running...)
So really 3GB is the minimum probably but I'm not sure there were any 3GB nVidias.

The CUDA version currently in `evo` branch works nicely for me, on 4GB+ card (970GTX), with RandomX algos working fine.
I have not tried the OpenCL-on-nVidia as it has never worked (or if it did it worked badly) with any of the other miners so it didn't seem like worth trying.  I might toss a test at it on my 4GB to see if it works when given enough memory, but doubtful it will be as fast as raw CUDA.

For the new CUDA backend on xmrig (unified) which is in the `evo` branch now, you need to checkout the `xmrig-cuda` project and build from that the so/dll for the unified CUDA backend (different than OpenCL which is fully unified).

# Action History
- Created by: iEsse | 2019-09-29T15:23:00+00:00
- Closed at: 2021-04-12T15:54:13+00:00
