---
title: Mining on NVIDIA Tesla K80
source_url: https://github.com/xmrig/xmrig/issues/2426
author: radimkohout
assignees: []
labels: []
created_at: '2021-06-06T10:12:13+00:00'
updated_at: '2021-10-08T20:23:24+00:00'
type: issue
status: closed
closed_at: '2021-06-07T19:21:13+00:00'
---

# Original Description
Hello,
I've compiled your cuda plugin(https://github.com/xmrig/xmrig-cuda) for my Debian VM with Tesla K80 GPU. I've installed drivers for the GPU and nvidia-detect can see it... But the xmrig writes "No GPU found". Where is the problem?

# Discussion History
## Spudz76 | 2021-06-06T18:07:11+00:00
what does `nvidia-smi` say

which CUDA Toolkit version did you compile against?

## Spudz76 | 2021-06-06T18:09:09+00:00
Also you may need cmake option `-DCUDA_ARCH=37` for it to build the perfect kernels.

## Spudz76 | 2021-06-06T18:15:16+00:00
And capability 3.7 was deprecated in v11.0 so it could be broken or abandoned in subsequent versions (will be gone in v12)

I might use CUDA Toolkit 10.2 for it / there are no new features or gains by using newer really (for mining, for Kepler).  It should run against whatever driver (are you on 460.80?) but there is a listing [here](https://docs.nvidia.com/deploy/cuda-compatibility/index.html#binary-compatibility__table-toolkit-driver) that tells which minimum driver for each Toolkit.

## radimkohout | 2021-06-07T19:21:13+00:00
I've installed incorrect drivers. I've found that by running the nvidia-smi command... Now everything works...

## Spudz76 | 2021-06-08T00:33:04+00:00
It seemed like the current driver should have still worked according to readme's but yes the alternative is the nvidia-390 series which is still maintained to compile on current kernels.  It works even for Pascal series.

## ributmaestro | 2021-10-07T21:34:55+00:00
> I've installed incorrect drivers. I've found that by running the nvidia-smi command... Now everything works...

hello can you teach how to make the xmrig-cuda on tesla k80?

## Spudz76 | 2021-10-08T20:22:07+00:00
Obtain CUDA Toolkit 10.2

Build according to instructions except also add `-DCUDA_ARCH=37` to the cmake command so it doesn't waste time building kernels for GPUs you don't have.

Copy result dll/so to xmrig run folder, enable cuda backend, should detect...

## Spudz76 | 2021-10-08T20:23:24+00:00
Or for windows, download the precompiled binary for cuda10.2, versions for 11.x might not work with K80

# Action History
- Created by: radimkohout | 2021-06-06T10:12:13+00:00
- Closed at: 2021-06-07T19:21:13+00:00
