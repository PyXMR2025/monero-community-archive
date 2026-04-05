---
title: Handling situation where AMD GPUs appear as multiple OpenCL platforms
source_url: https://github.com/xmrig/xmrig/issues/1371
author: lss4
assignees: []
labels: []
created_at: '2019-12-03T03:27:48+00:00'
updated_at: '2022-09-12T14:41:21+00:00'
type: issue
status: closed
closed_at: '2021-04-12T15:12:27+00:00'
---

# Original Description
OS: Latest Manjaro
OpenCL: opencl-amd (AUR)
XMRig version: 5.0.0
GPU/Platform 0: FirePro W7100 (Tonga)
GPU/Platform 1: Radeon VII (Vega)

On one of the rig that I intend to dedicate for mining, I've two AMD GPUs (of different generations) installed. However, the two GPUs appear to the system as two different platforms instead of one (the platforms have the same "AMD" name, though), and it seems xmrig can only use one platform at a time when using the configuration file.

Specifying platform as "AMD" will point to the first platform (first card), equivalent to specifying platform as 0, while specifying platform as 1 will correctly point to the second platform (second card). However, I don't know how I can utilize both cards (which means both platforms) in a single instance. I tried specifying "platform" as [0,1] but it does not work and only the first card/platform gets used.

It's not a major issue as I can always make a separate configuration file to utilize the second card/platform on a separate instance, although I really want to use only one instance for everything (CPU and both cards).

This is observed on XMRig 5.0.0. Not sure about 5.1.0, although the PKGBUILD has been updated to 5.1.0 so I can update anytime if needed.

# Discussion History
## RainbowMiner | 2022-09-12T12:30:15+00:00
I know this topic is old, but how has this been solved exactly?

## lss4 | 2022-09-12T14:26:51+00:00
> I know this topic is old, but how has this been solved exactly?

XMR later switched to RandomX which made video cards pretty much irrelevant for this one.

## RainbowMiner | 2022-09-12T14:41:21+00:00
> > I know this topic is old, but how has this been solved exactly?
> 
> XMR later switched to RandomX which made video cards pretty much irrelevant for this one.

Ok, thank you for the prompt reply! So basically nothing has been changed for GPU mining.

# Action History
- Created by: lss4 | 2019-12-03T03:27:48+00:00
- Closed at: 2021-04-12T15:12:27+00:00
