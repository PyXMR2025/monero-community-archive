---
title: NVML disabled (failed to load NVML)
source_url: https://github.com/xmrig/xmrig/issues/2044
author: spitrip82
assignees: []
labels: []
created_at: '2021-01-17T05:03:22+00:00'
updated_at: '2021-04-12T14:24:06+00:00'
type: issue
status: closed
closed_at: '2021-04-12T14:24:06+00:00'
---

# Original Description
some one can help on this issue ? i am using win10 and i have install CUDA Toolkit 11.2
![Capturar](https://user-images.githubusercontent.com/76714275/104831464-17e76c00-5881-11eb-8684-b5ed2cea5bd0.PNG)


# Discussion History
## xmrig | 2021-01-17T05:36:18+00:00
This error does not affect mining speed (using GPU for RandomX is not the best idea though), but without NVML information about GPU health (clocks, power, temps, fans) is not available. Can you try to find nvml.dll or your C: drive?
Thank you.

## spitrip82 | 2021-01-17T05:38:59+00:00

yes I managed to locate
![2](https://user-images.githubusercontent.com/76714275/104832076-3b60e580-5886-11eb-9f58-1c489473eb6d.PNG)


## xmrig | 2021-01-17T06:40:58+00:00
I unable to reproduce this issue, on almost same software/hardware configuration it just works https://i.imgur.com/qr4Fk8f.png
Thank you.

## spitrip82 | 2021-01-17T06:43:50+00:00
problem fixed ! 
solution : 
config file / edit
 "cuda": { "enabled": false, "loader": null, "nvml": true, "cn/0": false, "cn-lite/0": false


## Pafolo | 2021-01-17T18:05:48+00:00
For anyone that has this issue and is still trying to figure it out search your pc for the nvml.dll file and copy paste that file into your folder with the xmrig.exe

# Action History
- Created by: spitrip82 | 2021-01-17T05:03:22+00:00
- Closed at: 2021-04-12T14:24:06+00:00
