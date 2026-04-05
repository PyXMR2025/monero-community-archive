---
title: GPU mining doesn't show hashrate
source_url: https://github.com/xmrig/xmrig/issues/2166
author: Jolly-Pirate
assignees: []
labels: []
created_at: '2021-03-09T19:16:54+00:00'
updated_at: '2021-03-09T20:09:21+00:00'
type: issue
status: closed
closed_at: '2021-03-09T20:09:21+00:00'
---

# Original Description
CUDA mining doesn't show hashrate.
```
[2021-03-09 14:13:50.979]  net      new job from s3.solopool.org:8010 diff 100001 algo rx/0 height 2313411
[2021-03-09 14:13:50.979]  cpu      use argon2 implementation AVX2
[2021-03-09 14:13:50.982]  msr      register values for "ryzen_17h" preset have been set successfully (3 ms)
[2021-03-09 14:13:50.982]  randomx  init dataset algo rx/0 (16 threads) seed 640effec70686895...
[2021-03-09 14:13:51.169]  randomx  allocated 2336 MB (2080+256) huge pages 100% 1168/1168 +JIT (187 ms)
[2021-03-09 14:13:53.187]  randomx  dataset ready (2018 ms)
[2021-03-09 14:13:53.187]  nvidia   use profile  rx  (2 threads) scratchpad 2048 KB
|  # | GPU |  BUS ID | INTENSITY | THREADS | BLOCKS | BF |  BS | MEMORY | NAME
|  0 |   0 | 0d:00.0 |       832 |      32 |     26 |  0 |   0 |   1664 | GeForce GTX 1650
|  1 |   1 | 07:00.0 |        64 |      32 |      2 |  0 |   0 |    128 | GeForce GT 710
[2021-03-09 14:13:53.824]  nvidia   READY threads 2/2 (637 ms)
[2021-03-09 14:14:53.227]  nvidia   #0 0d:00.0  67W 59C 1980/5000 MHz fan0:29% fan1:29%
[2021-03-09 14:14:53.227]  nvidia   #1 07:00.0   0W 44C
[2021-03-09 14:14:53.227]  miner    speed 10s/60s/15m n/a n/a n/a H/s max n/a H/s
```
Although it's indeed doing work on the GPU.
```
$ nvidia-smi
Tue Mar  9 14:17:25 2021       
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 455.32.00    Driver Version: 455.32.00    CUDA Version: 11.1     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|                               |                      |               MIG M. |
|===============================+======================+======================|
|   0  GeForce GT 710      On   | 00000000:07:00.0 N/A |                  N/A |
| 40%   46C    P0    N/A /  N/A |    155MiB /   981MiB |     N/A      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+
|   1  GeForce GTX 1650    On   | 00000000:0D:00.0 Off |                  N/A |
| 30%   61C    P3    69W / 100W |   3835MiB /  3909MiB |    100%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+
                                                                               
+-----------------------------------------------------------------------------+
| Processes:                                                                  |
|  GPU   GI   CI        PID   Type   Process name                  GPU Memory |
|        ID   ID                                                   Usage      |
|=============================================================================|
|    1   N/A  N/A      1527      G   /usr/lib/xorg/Xorg                  9MiB |
|    1   N/A  N/A      1697      G   /usr/bin/gnome-shell                2MiB |
|    1   N/A  N/A    416515      C   ./xmrig                          3811MiB |
+-----------------------------------------------------------------------------+
```

# Discussion History
## SChernykh | 2021-03-09T19:36:41+00:00
Try different versions of CUDA plugin: https://github.com/xmrig/xmrig-cuda/releases
And try to disable GT 710 (index 1 in config.json) because it's too weak to mine Monero.

## Jolly-Pirate | 2021-03-09T19:44:32+00:00
> Try different versions of CUDA plugin: https://github.com/xmrig/xmrig-cuda/releases
> And try to disable GT 710 (index 1 in config.json) because it's too weak to mine Monero.

Thanks for the quick reply. How do I disable the GT 710? I know it's weak, but I left it in the system after adding the new GTX 1650 that I purchased recently.
I tried with `./xmrig --cuda-devices=0` but it still uses both GPUs.

## SChernykh | 2021-03-09T19:47:58+00:00
Open your config.json, find "cuda" section, then "rx" section in it and remove block with `"index": 1,`

## Jolly-Pirate | 2021-03-09T19:56:00+00:00
> Open your config.json, find "cuda" section, then "rx" section in it and remove block with `"index": 1,`

Great that worked. And it's now showing the hashrate. I was expecting an improvement on GPU, but it's way worse than my CPU!
with GPU alone:
`miner    speed 10s/60s/15m 346.7 n/a n/a H/s max 349.5 H/s`

with CPU 16 threads:
`miner    speed 10s/60s/15m 8697.3 n/a n/a H/s max 8743.6 H/s`

## SChernykh | 2021-03-09T20:02:24+00:00
> I was expecting an improvement on GPU, but it's way worse than my CPU!

Yes, exactly as expected for RandomX mining.

## Jolly-Pirate | 2021-03-09T20:03:18+00:00
> > I was expecting an improvement on GPU, but it's way worse than my CPU!
> 
> Yes, exactly as expected for RandomX mining.

I just read somewhere else that RandomX is very inefficient on GPU. Which begs the question, why even bother writing a CUDA plugin for it!?

# Action History
- Created by: Jolly-Pirate | 2021-03-09T19:16:54+00:00
- Closed at: 2021-03-09T20:09:21+00:00
