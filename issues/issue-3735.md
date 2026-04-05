---
title: Unable to Reduce GPU Utilization (Always 100% Load on CUDA Backend
source_url: https://github.com/xmrig/xmrig/issues/3735
author: emreemrelan0-gif
assignees: []
labels:
- bug
- kawpow
created_at: '2025-11-19T00:09:54+00:00'
updated_at: '2025-11-20T23:24:26+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
No matter what CUDA configuration I use, the GPU always stays at 100% utilization according to:
nvidia-smi --query-gpu=utilization.gpu --format=csv
Task Manager (GPU 3D)

I successfully reduced the hashrate from 18 MH/s to 6 MH/s, but the GPU load still reports 100% even at very low clocks, blocks, threads, bfactor, and bsleep.

What I Tried
1. Power limit / locked clocks
nvidia-smi -lgc 600,600
nvidia-smi -pl 70

Clocks and power reduce correctly, but utilization stays 100%.

2. Tweaking CUDA settings in JSON
"threads": [
  {
    "index": 0,
    "threads": 64,
    "blocks": 8,
    "bfactor": 8,
    "bsleep": 4000
  }
]

Hashrate drops but utilization remains 100%.

I want to limit the GPU load below 100%, similar to how CPU mining supports --cpu-max-threads-hint or throttling via sleep.

My goals:

Reduce load (e.g., 30–50% GPU utilization)

Avoid constant 100% GPU usage

Make the GPU available for normal desktop usage while mining lightly

Actual Behavior

Hashrate decreases when tweaking blocks/threads/bfactor/bsleep

GPU utilization always stays at 100%

Windows Task Manager and NVML both confirm 100% usage

GPU is always fully occupied regardless of intensity


I'm trying to mine KawPow at low intensity with XMRig GPU, but the miner forces the GPU to 100% utilization even when hashrate is intentionally reduced. I need a way to mine at partial utilization.

Any clarification or guidance would be greatly appreciated.


# Discussion History
## SChernykh | 2025-11-19T17:20:39+00:00
bsleep should control it (it's a sleep interval between iterations, in microseconds), but as far as I can see, xmrig-cuda doesn't use it for KawPow, it's only used when mining Cryptonight.

## SChernykh | 2025-11-19T18:02:48+00:00
https://github.com/xmrig/xmrig-cuda/pull/215 fixes this.

## SChernykh | 2025-11-19T18:04:45+00:00
You can build xmrig-cuda plugin yourself from the dev branch once it's merged, or you can wait for the next xmrig-cuda plugin release. To achieve what you want (30-50% GPU load), set `bsleep` to 10000-50000, and then reduce `blocks` gradually until you get the needed load %.

## emreemrelan0-gif | 2025-11-19T18:32:00+00:00
> [xmrig/xmrig-cuda#215](https://github.com/xmrig/xmrig-cuda/pull/215) fixes this.

Thank you so much!


## emreemrelan0-gif | 2025-11-19T20:45:44+00:00
> You can build xmrig-cuda plugin yourself from the dev branch once it's merged, or you can wait for the next xmrig-cuda plugin release. To achieve what you want (30-50% GPU load), set `bsleep` to 10000-50000, and then reduce `blocks` gradually until you get the needed load %.

[2025-11-20 00:43:12.645]  miner    speed 10s/60s/15m n/a n/a n/a H/s max n/a H/s
[2025-11-20 00:43:14.004] no results yet
[2025-11-20 00:43:14.780] no results yet
[2025-11-20 00:43:14.900] no results yet
[2025-11-20 00:43:15.585]  nvidia   #0 01:00.0  66W 50C 1935/6801 MHz fan0:35% fan1:35%
[2025-11-20 00:43:16.314]  nvidia   #0 01:00.0  67W 50C 1935/6801 MHz fan0:35% fan1:35%
[2025-11-20 00:43:16.425]  nvidia   #0 01:00.0  67W 50C 1935/6801 MHz fan0:35% fan1:35%
[2025-11-20 00:43:16.525]  nvidia   #0 01:00.0  67W 50C 1935/6801 MHz fan0:35% fan1:35%
[2025-11-20 00:43:16.656]  nvidia   #0 01:00.0  67W 50C 1935/6801 MHz fan0:35% fan1:35%
[2025-11-20 00:43:17.316] no results yet
[2025-11-20 00:43:17.432] no results yet
[2025-11-20 00:43:19.228] no results yet
[2025-11-20 00:43:36.796] no results yet
[2025-11-20 00:43:48.732] no results yet
[2025-11-20 00:43:53.316] no results yet

What could be causing this? Its been doing this for about an hour now and not mining.

## kkaze5348-ops | 2025-11-19T20:48:33+00:00
<img width="840" height="79" alt="Image" src="https://github.com/user-attachments/assets/ac0215ff-3678-4849-8219-2842ed617734" />

## emreemrelan0-gif | 2025-11-19T21:13:57+00:00
> You can build xmrig-cuda plugin yourself from the dev branch once it's merged, or you can wait for the next xmrig-cuda plugin release. To achieve what you want (30-50% GPU load), set `bsleep` to 10000-50000, and then reduce `blocks` gradually until you get the needed load %.

<img width="367" height="147" alt="Image" src="https://github.com/user-attachments/assets/4a715553-44b1-481f-8566-d8815baf0bd4" />
For a second I thought it worked, but it sometimes spikes to 100% usage and then throttles.
<img width="348" height="103" alt="Image" src="https://github.com/user-attachments/assets/0f42d5c4-7adc-49b6-b53e-ff42c4b18ede" />

## SChernykh | 2025-11-20T08:57:07+00:00
> > You can build xmrig-cuda plugin yourself from the dev branch once it's merged, or you can wait for the next xmrig-cuda plugin release. To achieve what you want (30-50% GPU load), set `bsleep` to 10000-50000, and then reduce `blocks` gradually until you get the needed load %.
> 
> [2025-11-20 00:43:12.645] miner speed 10s/60s/15m n/a n/a n/a H/s max n/a H/s [2025-11-20 00:43:14.004] no results yet [2025-11-20 00:43:14.780] no results yet [2025-11-20 00:43:14.900] no results yet [2025-11-20 00:43:15.585] nvidia #0 01:00.0 66W 50C 1935/6801 MHz fan0:35% fan1:35% [2025-11-20 00:43:16.314] nvidia #0 01:00.0 67W 50C 1935/6801 MHz fan0:35% fan1:35% [2025-11-20 00:43:16.425] nvidia #0 01:00.0 67W 50C 1935/6801 MHz fan0:35% fan1:35% [2025-11-20 00:43:16.525] nvidia #0 01:00.0 67W 50C 1935/6801 MHz fan0:35% fan1:35% [2025-11-20 00:43:16.656] nvidia #0 01:00.0 67W 50C 1935/6801 MHz fan0:35% fan1:35% [2025-11-20 00:43:17.316] no results yet [2025-11-20 00:43:17.432] no results yet [2025-11-20 00:43:19.228] no results yet [2025-11-20 00:43:36.796] no results yet [2025-11-20 00:43:48.732] no results yet [2025-11-20 00:43:53.316] no results yet
> 
> What could be causing this? Its been doing this for about an hour now and not mining.

I tested it on my system and it worked normally. Maybe you put too high bsleep value. 10-50k worked for me, but maybe you need to try lower values first.

## emreemrelan0-gif | 2025-11-20T17:11:19+00:00
> I tested it on my system and it worked normally. Maybe you put too high bsleep value. 10-50k worked for me, but maybe you need to try lower values first.

Where did you test it? On Windows 11 25H2 it isn’t working. In Task Manager the GPU utilization shows 100%, while nvidia-smi reports much lower usage.

## SChernykh | 2025-11-20T21:17:27+00:00
I checked GPU load in GPU-Z utility, not in the task manager.

## emreemrelan0-gif | 2025-11-20T21:25:25+00:00
> I checked GPU load in GPU-Z utility, not in the task manager.

Could you check the GPU usage in Task Manager on your Windows system?
Also, do you have any idea why Task Manager, Process Explorer, or System Informer all show 100% GPU usage?

## SChernykh | 2025-11-20T21:31:56+00:00
I don't know, but GPU-Z is a more reliable source because it's a specialized utility.

## emreemrelan0-gif | 2025-11-20T23:23:18+00:00
> I don't know, but GPU-Z is a more reliable source because it's a specialized utility.

In most cases, the miner console crashes or freezes before the DAG size is calculated. However, when the DAG size is successfully calculated, the miner runs without issues.
Do you know why? (thats really annoying)

# Action History
- Created by: emreemrelan0-gif | 2025-11-19T00:09:54+00:00
