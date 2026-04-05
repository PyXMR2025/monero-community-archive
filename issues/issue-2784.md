---
title: Xmrig 6.16 testing Gtx645 geforce for cuda
source_url: https://github.com/xmrig/xmrig/issues/2784
author: MRvykyng
assignees: []
labels: []
created_at: '2021-12-03T16:59:58+00:00'
updated_at: '2021-12-04T02:56:09+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I have a dell 3610 E5-1620 v2 desktop. It runs cpu random x at about  2300/hs
I have an older GeForce gtx 645 graphics card that I would like to test cuda/xmrig with.
All info I have on the gpu indicates it is cuda enabled. I have installed the video card, enabled cuda in the Jason.config, and tried various versions of cuda. Currently I have cuda 8.0 installed for the older card.
When I run xmrig,- cuda remains disabled??
I know this card will not hash well, but for learning and testing purposes, my goal is to get xmrig to identify the gpu and run cuda,
![D41BCCF8-A171-46E5-AAEF-D7E0713B3819](https://user-images.githubusercontent.com/94088700/144641874-b02042f6-fb13-4a7d-8c5e-a67083059450.jpeg)

Any assistance with tweaking to recognize the gpu in xmrig would be helpful

thanx

# Discussion History
## MRvykyng | 2021-12-03T17:03:47+00:00
A bit more info
![8B6BF4FD-1B4E-4E2E-9E56-23A6354A8150](https://user-images.githubusercontent.com/94088700/144642908-a745ac26-ef27-4061-9c2b-e1aef8a4a675.jpeg)
![B5FEE9DE-90F9-4958-BA35-9648CA6CAA8F](https://user-images.githubusercontent.com/94088700/144642914-20849dcb-1b58-458a-a49b-4c0dda305563.jpeg)


## Spudz76 | 2021-12-03T17:58:36+00:00
Kepler does not work with newer CUDA runtime, use between 9.1 and 10.2 (such as [xmrig-cuda-6.15.1-cuda10_2-win64.zip](https://github.com/xmrig/xmrig-cuda/releases/download/v6.15.1/xmrig-cuda-6.15.1-cuda10_2-win64.zip)).

However -- `nvidia-smi` command will show in the upper right corner which CUDA runtime your driver includes.  You also have to be at that version, or below.

## MRvykyng | 2021-12-03T18:58:54+00:00
This is what I have in my control panel showing cuda version
![Cuda_ControlPanel](https://user-images.githubusercontent.com/94088700/144657506-800042a8-fafa-4274-8f55-e633313235f4.jpg)
I however am unable to locate or execute nvidia-smi??

## Spudz76 | 2021-12-03T19:50:26+00:00
That is not anything to do with the driver bundled CUDA which is what it runs against.

When it's not in your PATH for some reason, it is located at `C:\Program Files\NVIDIA Corporation\NVSMI\nvidia-smi.exe`

## MRvykyng | 2021-12-03T20:24:34+00:00
Wow....you are spectacular, and bang on!! It is there
so I have pulled up cmd prompt, and browsed to the file location, and when i hit run, I get a very brief "dos window flash", but it does not open.... no information screen? I also tried to run as administrator, but am only getting a brief flash, no matter what method I try to execute 

## Spudz76 | 2021-12-03T20:49:29+00:00
Run `cmd.exe`

`cd \Program Files\NVIDIA Corporation\NVSMI\`

`nvidia-smi`

## MRvykyng | 2021-12-03T21:06:47+00:00

![nvidia-smi error](https://user-images.githubusercontent.com/94088700/144672859-0f9848f1-38d5-4fc1-9bf8-1b94afa629db.jpg)

thanx for your patience

## MRvykyng | 2021-12-03T23:28:51+00:00
well, after researching my error, I found my driver for the GTX645 was not installed properly. I updated to nvidia driver- ver 471.12  Now when I run nvidia-smi I get these results.
incompatible
![nvidia-smi result](https://user-images.githubusercontent.com/94088700/144685248-a287cdf3-833c-4010-9661-5f4719867788.jpg)


## Spudz76 | 2021-12-03T23:31:40+00:00
It should work now then, with the xmrig-cuda 10.2 build I linked earlier (drop dll in xmrig folder)

## MRvykyng | 2021-12-04T00:02:50+00:00
when I try to run xmrig as an adminstrator from the "pool mine example" -cuda is still disabled ??  
![PoolMineStartupScreen](https://user-images.githubusercontent.com/94088700/144687656-9a5700a2-befb-4b18-8d3c-375dff9d971e.jpg)


when i run xmrig directly as an administrator- all looks good
![StartupScreen](https://user-images.githubusercontent.com/94088700/144687289-7b7198a9-f6f0-45c7-97ee-8bb5b3a15730.jpg)

Running from POOL_MINE_EXAMPLE does not load cuda??


 * ABOUT        XMRig/6.16.2 gcc/10.1.0
 * LIBS         libuv/1.42.0 OpenSSL/1.1.1l hwloc/2.5.0
 * HUGE PAGES   permission granted
 * 1GB PAGES    unavailable
 * CPU          Intel(R) Xeon(R) CPU E5-1620 v2 @ 3.70GHz (1) 64-bit AES
                L2:1.0 MB L3:10.0 MB 4C/8T NUMA:1
 * MEMORY       2.8/15.9 GB (17%)
                DIMM1: 4 GB DDR3 @ 1333 MHz HMT451R7AFR8C-RD
                DIMM5: <empty>
                DIMM3: 4 GB DDR3 @ 1333 MHz HMT451R7AFR8C-RD
                DIMM7: <empty>
                DIMM2: 4 GB DDR3 @ 1333 MHz HMT351R7BFR8A-H9
                DIMM6: <empty>
                DIMM4: 4 GB DDR3 @ 1333 MHz HMT351R7BFR8A-H9
                DIMM8: <empty>
 * MOTHERBOARD  Dell Inc. - 09M8Y8
 * DONATE       1%
 * ASSEMBLY     auto:intel
 * POOL #1      rx-us.unmineable.com:3333 algo auto
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         10.2/11.4/6.15.1
 * NVML         11.472.12/472.12 press e for health report
 * CUDA GPU     #0 03:00.0 NVIDIA GeForce GTX 645 0/0 MHz smx:3 arch:30 mem:816/1024 MB
[2021-12-03 15:53:28.367]  net      use pool rx-us.unmineable.com:3333  139.59.164.251
[2021-12-03 15:53:28.367]  net      new job from rx-us.unmineable.com:3333 diff 100001 algo rx/0 height 2507077 (52 tx)
[2021-12-03 15:53:28.367]  cpu      use argon2 implementation SSSE3
[2021-12-03 15:53:28.555]  msr      register values for "intel" preset have been set successfully (184 ms)
[2021-12-03 15:53:28.555]  randomx  init dataset algo rx/0 (8 threads) seed 5ab039574d1c5b6c...
[2021-12-03 15:53:28.555]  randomx  allocated 2336 MB (2080+256) huge pages 100% 1168/1168 +JIT (0 ms)
[2021-12-03 15:53:33.170]  randomx  dataset ready (4610 ms)
[2021-12-03 15:53:33.170]  cpu      use profile  rx  (4 threads) scratchpad 2048 KB
[2021-12-03 15:53:33.170]  nvidia   use profile  rx  (1 thread) scratchpad 2048 KB
|  # | GPU |  BUS ID | INTENSITY | THREADS | BLOCKS | BF |  BS | MEMORY | NAME
|  0 |   0 | 03:00.0 |       192 |      32 |      6 |  8 |  25 |    384 | NVIDIA GeForce GTX 645
[2021-12-03 15:53:33.201]  cpu      READY threads 4/4 (4) huge pages 100% 4/4 memory 8192 KB (22 ms)
[2021-12-03 15:53:33.326]  nvidia   READY threads 1/1 (148 ms)
[2021-12-03 15:54:01.841]  net      new job from rx-us.unmineable.com:3333 diff 100001 algo rx/0 height 2507077 (52 tx)
[2021-12-03 15:54:08.533]  cpu      accepted (1/0) diff 100001 (244 ms)
[2021-12-03 15:54:10.981]  cpu      accepted (2/0) diff 100001 (245 ms)
[2021-12-03 15:54:16.882]  net      new job from rx-us.unmineable.com:3333 diff 100001 algo rx/0 height 2507077 (52 tx)
[2021-12-03 15:54:30.305]  cpu      accepted (3/0) diff 100001 (307 ms)
[2021-12-03 15:54:34.386]  nvidia   #0 03:00.0   0W  0C
[2021-12-03 15:54:34.386]  miner    speed 10s/60s/15m 2170.5 2204.9 n/a H/s max 2290.6 H/s
[2021-12-03 15:54:45.787]  cpu      accepted (4/0) diff 100001 (271 ms)
[2021-12-03 15:54:55.080]  cpu      accepted (5/0) diff 100001 (266 ms)
[2021-12-03 15:55:16.978]  net      new job from rx-us.unmineable.com:3333 diff 100001 algo rx/0 height 2507077 (52 tx)
[2021-12-03 15:55:25.099]  net      new job from rx-us.unmineable.com:3333 diff 100001 algo rx/0 height 2507077 (88 tx)
[2021-12-03 15:55:35.675]  nvidia   #0 03:00.0   0W  0C
[2021-12-03 15:55:35.675]  miner    speed 10s/60s/15m 1869.6 2201.1 n/a H/s max 2290.6 H/s
[2021-12-03 15:55:38.666]  cpu      accepted (6/0) diff 100001 (292 ms)
[2021-12-03 15:55:54.848]  net      new job from rx-us.unmineable.com:3333 diff 100001 algo rx/0 height 2507077 (88 tx)
[2021-12-03 15:56:02.158]  net      new job from rx-us.unmineable.com:3333 diff 100001 algo rx/0 height 2507077 (88 tx)
[2021-12-03 15:56:06.023]  cpu      accepted (7/0) diff 100001 (249 ms)
[2021-12-03 15:56:17.141]  net      new job from rx-us.unmineable.com:3333 diff 100001 algo rx/0 height 2507077 (88 tx)
[2021-12-03 15:56:32.270]  cpu      accepted (8/0) diff 100001 (260 ms)
[2021-12-03 15:56:36.663]  nvidia   #0 03:00.0   0W  0C
[2021-12-03 15:56:36.663]  miner    speed 10s/60s/15m 2131.8 1994.2 n/a H/s max 2290.6 H/s
[2021-12-03 15:56:38.803]  cpu      accepted (9/0) diff 100001 (263 ms)
[2021-12-03 15:56:42.771]  cpu      accepted (10/0) diff 100001 (245 ms)
[2021-12-03 15:56:44.261]  net      new job from rx-us.unmineable.com:3333 diff 100001 algo rx/0 height 2507078 (28 tx)
[2021-12-03 15:56:46.964]  net      new job from rx-us.unmineable.com:3333 diff 100001 algo rx/0 height 2507078 (28 tx)
[2021-12-03 15:57:01.953]  net      new job from rx-us.unmineable.com:3333 diff 100001 algo rx/0 height 2507078 (28 tx)
[2021-12-03 15:57:12.586]  cpu      accepted (11/0) diff 100001 (247 ms)
[2021-12-03 15:57:15.435]  net      new job from rx-us.unmineable.com:3333 diff 100001 algo rx/0 height 2507079 (15 tx)
[2021-12-03 15:57:16.918]  net      new job from rx-us.unmineable.com:3333 diff 100001 algo rx/0 height 2507079 (15 tx)
[2021-12-03 15:57:30.672]  cpu      accepted (12/0) diff 100001 (248 ms)
[2021-12-03 15:57:31.959]  net      new job from rx-us.unmineable.com:3333 diff 100001 algo rx/0 height 2507079 (15 tx)
[2021-12-03 15:57:37.579]  nvidia   #0 03:00.0   0W  0C
[2021-12-03 15:57:37.579]  miner    speed 10s/60s/15m 2260.2 2227.4 n/a H/s max 2290.6 H/s
[2021-12-03 15:57:46.954]  net      new job from rx-us.unmineable.com:3333 diff 100001 algo rx/0 height 2507079 (15 tx)
[2021-12-03 15:57:49.920]  cpu      accepted (13/0) diff 100001 (253 ms)
[2021-12-03 15:58:01.934]  net      new job from rx-us.unmineable.com:3333 diff 100001 algo rx/0 height 2507079 (15 tx)
[2021-12-03 15:58:32.003]  net      new job from rx-us.unmineable.com:3333 diff 100001 algo rx/0 height 2507079 (15 tx)
[2021-12-03 15:58:38.470]  nvidia   #0 03:00.0   0W  0C



## MRvykyng | 2021-12-04T00:25:34+00:00
now that my GPU is recognized- is it doing anything?
![xmrigCPU_GPUresults](https://user-images.githubusercontent.com/94088700/144688919-f9558f95-d989-41ba-af24-2ee11941a9de.jpg)

thanx


## Spudz76 | 2021-12-04T01:18:46+00:00
Generally RandomX isn't for GPUs anyway, especially ones with less than 4GB.

You could try to force it to work by checking config.json for the "rx" profile in the "cuda" section.  It should look something like:
```
        "rx": [
            {
                "index": 0,
                "threads": 32,
                "blocks": 6,
                "bfactor": 8,
                "bsleep": 25,
                "affinity": -1,
                "dataset_host": true
            }   
        ],  
```

So that `dataset_host` item has to be `true` when you don't have more than 3GB of VRAM (yours is 1GB).  But then along with the GPU being slow to begin with, every memory access to the dataset has to go across the PCIe bus which is even slower (compared to VRAM).  And it may still not work I don't think I have bothered testing on a Fermi/Kepler.

You'd get much better results using an autoexchange pool like MoneroOcean.  Then the GPU can do something else like cn-heavy/xhv or cn-gpu which it is good at (still slow) and be paid the value of that in XMR.  And likely the CPU would profit more processing some other algo, both pointed at MoneroOcean results in a stream of XMR just like any other pool even though it's mining other coins in reality.  And the profit chases the current pricing so they will hop to other types.  If rx/0 is actually the top profit then it will mine that (usually isn't, on my older stuff).

## MRvykyng | 2021-12-04T02:56:09+00:00
hey, did I tell you that you are SPECTACULAR!!!!
And patient!!   This has been great getting knowledge, and tackling challenges, for this old-newbie. 
The settings in config.jason are same as your example....
I wasn't expecting miracles, but thought I could get a few hashes out the back end on this ol' card.....hoping it might crank out a bit since its just sitting there 
But more importantly was the problem solving,...... 
Its been a while since playing with dos, and config files and such,
and windows 10/11 has made navigating for this windows XP/ 7 era-dude, very interesting     lol
Still a bit unclear why cuda is disabled when running "pool_mine_example" command as administrator?
As I said, im kinda getting my toes wet, and set up with shiba-inu on the unmineable pool was where I found the best(least complicated) info to start mining shiba. 
 I will research moneroocean, for sure!!
You have been absolutely stellar!!!    and haven't steered me wrong yet
Cheers!!!!

# Action History
- Created by: MRvykyng | 2021-12-03T16:59:58+00:00
