---
title: 'Thread #0 failed with error'
source_url: https://github.com/xmrig/xmrig/issues/2046
author: Pafolo
assignees: []
labels: []
created_at: '2021-01-17T18:03:12+00:00'
updated_at: '2021-04-12T14:23:36+00:00'
type: issue
status: closed
closed_at: '2021-04-12T14:23:36+00:00'
---

# Original Description
I was having issues with it not loading nvml but got that figured out and assumed that issue was what was causing me to have this error pop up.

**"thread #0 failed with error <RandomX_Monero::hash>:37 "no kernel image is available for execution on the device"**

Anyone know how to resolve this?

![Capture](https://user-images.githubusercontent.com/70542624/104851621-c6a89e00-58bb-11eb-93dc-a1163dd898c4.JPG)


# Discussion History
## SChernykh | 2021-01-17T20:30:37+00:00
You could try CUDA 8 plugin `xmrig-cuda-6.5.0-cuda8-win64.zip`. I don't think GTX-660 supports all CUDA 11 features when you start RandomX mining with CUDA 11 plugin.

## Pafolo | 2021-01-17T20:50:12+00:00
I tried cuda 8 and got a different error, tried cuda 9 and it worked. I'm able to go all the way up to 10.2. One issue I have is it doesn't display the GPU wattage.

Do all GPUs get this poor performance? Is there something I can change to make it better? HWinfo says I'm at 100% load.

Also can the temp be changed from C to F?
![Capture](https://user-images.githubusercontent.com/70542624/104855592-3fffbb00-58d3-11eb-8bf7-1546cb879f74.JPG)


## SChernykh | 2021-01-17T20:54:15+00:00
RandomX is designed to be slow on GPUs (basically slow on anything that isn't a CPU) and it uses 2 GB dataset which is more memory than GTX 660 has. So it's very slow.

## Pafolo | 2021-01-17T21:07:27+00:00
The gtx660 is a 2GB card. Am I looking at the wrong info?

## SChernykh | 2021-01-17T21:14:44+00:00
You can't allocate all 2 GB with CUDA and dataset is actually 2080 MB which is more than 2 GB. Also you need a number of 2 MB scratchpads to calculate hashes (320 scratchpads x 2 MB = 640 MB on your screenshot), so 2 GB cards can only run with dataset in system memory which is very slow.

## Pafolo | 2021-01-17T21:38:06+00:00
Does this apply to ALL GPUs or just nvidia models?
If I was to use a 8gb card would I be limited to the same processing power?

## SChernykh | 2021-01-17T21:40:27+00:00
All GPUs are bad at RandomX. You can go to https://whattomine.com/ and see where RandomX is on the list for any GPU.

## Pafolo | 2021-01-17T21:44:50+00:00
Whats the difference between huge-pages and huge-pages-jit? I have them both enabled along with memory pool. I'm just not sure what they do.

## Spudz76 | 2021-01-18T20:29:51+00:00
That original error simply means the cuda-plugin was not compiled with "arch 30" code.  It is impossible with CUDA newer than when they dropped arch30.  Build your own CUDA plugin, using the latest CUDA Toolkit that still supported arch30.  And I would run the LTS nvidia-390 branch not the newer drivers (no point, on old cards). [edit: oops I assume everyone is on Linux - same applies there are no new things for old cards beyond the 390 series of driver / find the windows latest 390.xx]

The list of how CUDA versus arch works out is at: https://github.com/xmrig/xmrig-cuda/blob/master/cmake/CUDA.cmake#L1
arch30 was dropped with CUDA11 (but arch 35 still works, confusing as both are Kepler) so maximum is CUDA10.2
The drivers eventually also drop support usually it works best if you get the CUDA line to match versions (not `10.2/11.2` but `10.2/10.2` or etc by changing the driver to older) - not that it doesn't work but compatibility modes are always imperfect.  Driver series 390.xx had CUDA9.2 max I think so you'd compile with that toolkit to use the older driver.

MoneroOcean lets you mine algos that are good for GPU, but always pays out XMR as if you had been mining RX/0
This way you can run a CPU-only miner which mines what it is good at, and a separate CUDA-only miner that does what it's good at, and then the pool pays out autochanged coin in XMR regardless.  I catch 15.8KH of RX/0 equivalence mining KawPow on Vega64's.  I never bothered benchmarking RX/0 directly but it's definitely nowhere near 15.8KH...

Generally on arch30 or worse, CN/Heavy or CN/GPU work best.  Note CN/GPU was dropped from official here a while back, but using the MoneroOcean fork it continues to exist (because I put it back and maintain it) and it works great.

# Action History
- Created by: Pafolo | 2021-01-17T18:03:12+00:00
- Closed at: 2021-04-12T14:23:36+00:00
