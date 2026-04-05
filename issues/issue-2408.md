---
title: Mac OS xmrig not working with AMD GPU
source_url: https://github.com/xmrig/xmrig/issues/2408
author: empiresun1
assignees: []
labels: []
created_at: '2021-05-25T04:52:49+00:00'
updated_at: '2025-06-16T18:46:37+00:00'
type: issue
status: closed
closed_at: '2025-06-16T18:46:37+00:00'
---

# Original Description
**Describe the bug**
So I'm VERY new to all this mining, i was using xmrig to randomx mine and it seemed to work but my hashrate is pretty low so I wanted to use my GPU. I have a Razer Core EGPU  setup with a Vega 64 card that i thought would work well but no matter what i try to do i cant get it to start. when i launch it sees the GPUs that i have on my setup but it gives me a bunch of errors and then fails to work. i dont know what the issue could be. 

im attaching both a screenshot of the miner text to see what could be wrong.
![Screen Shot 2021-05-25 at 12 47 25 AM](https://user-images.githubusercontent.com/84761243/119441072-8175fc00-bcf3-11eb-999a-1f70c0293e14.png)


Thank you! 




# Discussion History
## Spudz76 | 2021-05-25T12:41:39+00:00
Patches for all this are in development in [my fork's dev-fixAppleOpenCL branch](https://github.com/Spudz76/xmrig/tree/dev-fixAppleOpenCL) if you can compile and try.  See [macos build howto](https://xmrig.com/docs/miner/build/macos)

See also #2345 where all the action is taking place.

It might just work once you have this test branch running...

## empiresun1 | 2021-05-25T16:07:37+00:00
Thanks! we're making progress! it seems like the config and last compile from you has my EGPU up and running, however for some reason its not looking like its submitting to the pool on unminable even though its running? my CPU load is on there but the GPU is not? not sure why this might be. 
![Screen Shot 2021-05-25 at 12 05 57 PM](https://user-images.githubusercontent.com/84761243/119531295-c892da00-bd51-11eb-8014-01028507384f.png)


## empiresun1 | 2021-05-25T16:48:34+00:00
Also as a side note.... 640000 hash is like 0.64 KH ... isnt that kinda low? my cpu on randomx mines faster then that. lol

## Spudz76 | 2021-05-26T01:58:57+00:00
640KH.  0.64MH.  Hashrate isn't like MPH it's totally incomparable across algos.   But, it is slow for a Vega because Linux gets 19MH...

However I notice yours autoconfigured with only 1024 intensity and mine used 16777216 (same wsize, similar memory usage)

Try manually setting intensity higher.

Also LOL at my fan RPM (Linux driver is a little broken with that)

```
 * OPENCL       #0 AMD Accelerated Parallel Processing/OpenCL 2.1 AMD-APP (3143.9)
 * OPENCL GPU   #0 05:00.0 Radeon Vega Frontier Edition (gfx900) 1600 MHz cu:64 mem:16112/16368 MB
[2021-05-25 19:54:24.578]  opencl   use profile  kawpow  (1 thread) scratchpad 32 KB
|  # | GPU |  BUS ID | INTENSITY | WSIZE | MEMORY | NAME
|  0 |   0 | 05:00.0 |  16777216 |   256 |   2957 | Radeon Vega Frontier Edition (gfx900)
[2021-05-25 19:54:25.318]  opencl   READY threads 1/1 (740 ms)
[2021-05-25 19:54:26.957]  opencl   KawPow program for period 590044 compiled (1638ms)
[2021-05-25 19:54:28.891]  opencl   KawPow program for period 590045 compiled (1934ms)
[2021-05-25 19:54:52.270]  miner    KawPow light cache for epoch 236 calculated (25308ms)
[2021-05-25 19:54:57.297]  opencl   KawPow DAG for epoch 236 calculated (4887ms)
[2021-05-25 19:54:57.386]  opencl   accepted (1/0) diff 342M (56 ms)
[2021-05-25 19:55:02.598]  opencl   KawPow program for period 590046 compiled (5295ms)
[2021-05-25 19:55:08.745]  opencl   accepted (2/0) diff 342M (54 ms)
[2021-05-25 19:55:24.081]  opencl   accepted (3/0) diff 342M (71 ms)
[2021-05-25 19:55:24.416]  opencl   accepted (4/0) diff 342M (52 ms)
[2021-05-25 19:55:28.825]  opencl   #0 05:00.0 194W 70C 134217728RPM 1333/945MHz
[2021-05-25 19:55:28.825]  miner    speed 10s/60s/15m 19.03 19.03 n/a MH/s max 19.04 MH/s
```


## Spudz76 | 2021-05-26T02:01:08+00:00
Also, the job difficulty served to you by unmineable is 4295M and with a hashrate of 0.64MH it could take 111 minutes to hit a result (lol)  They should have some autodiff ports or a way to set a better diff.

Even at 19MH that job diff is high, 3.76 minutes avg between results. Should be around 30 to 60s

## empiresun1 | 2021-05-26T02:09:43+00:00
> Also, the job difficulty served to you by unmineable is 4295M and with a hashrate of 0.64MH it could take 111 minutes to hit a result (lol) They should have some autodiff ports or a way to set a better diff.
> 
> Even at 19MH that job diff is high, 3.76 minutes avg between results. Should be around 30 to 60s

yea i figured out the hashrate thing ... im at 50000 ish intensity now with about an 80% load on the card .... 

someone else said my diff rating was way too high... how would i go about lowering it? 

## empiresun1 | 2021-05-26T02:12:56+00:00
![Screen Shot 2021-05-25 at 10 12 11 PM](https://user-images.githubusercontent.com/84761243/119592337-484a9400-bda6-11eb-9329-e4c1da928205.png)


thats what im running now but i still think with a vega64 it should be much better. no idea how to lower difficulty

## empiresun1 | 2021-11-30T20:37:57+00:00
> Also, the job difficulty served to you by unmineable is 4295M and with a hashrate of 0.64MH it could take 111 minutes to hit a result (lol) They should have some autodiff ports or a way to set a better diff.
> 
> Even at 19MH that job diff is high, 3.76 minutes avg between results. Should be around 30 to 60s

Hey! 

I know its been a bit and you helped me out a ton with getting this running on my Mac with an EGPU... i recently updated my mac and wanted to test my new setup with water cooling but i cant seem to get it to run. Monero seems like a decent choice. 

Any chance you can help me again? thanks! 

# Action History
- Created by: empiresun1 | 2021-05-25T04:52:49+00:00
- Closed at: 2025-06-16T18:46:37+00:00
