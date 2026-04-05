---
title: (not bug) Please add aarch64 on ubuntu for L4T and rpi
source_url: https://github.com/xmrig/xmrig/issues/2173
author: leonpano2006
assignees: []
labels: []
created_at: '2021-03-11T19:26:33+00:00'
updated_at: '2021-03-19T21:59:33+00:00'
type: issue
status: closed
closed_at: '2021-03-19T21:59:22+00:00'
---

# Original Description
**Describe the bug**
A clear and concise description of what the bug is.
(Not bug)
**To Reproduce**
Steps to reproduce the behavior.

**Expected behavior**
A clear and concise description of what you expected to happen.

**Required data**
 - Miner log as text or screenshot
 - Config file or command line (without wallets)
 - OS: [e.g. Windows]
 - For GPU related issues: information about GPUs and driver version.

**Additional context**
Add any other context about the problem here.
Please add aarch64 on ubuntu for L4T and rpi

# Discussion History
## benthetechguy | 2021-03-12T04:30:40+00:00
You can easily compile xmrig for aarch64, and I've done so on both my raspberry pi 4 and my nintendo switch (L4T). I don't believe xmrig will be compiled for aarch64 on every release because of the low demand.

## leonpano2006 | 2021-03-12T10:57:14+00:00
> You can easily compile xmrig for aarch64, and I've done so on both my raspberry pi 4 and my nintendo switch (L4T). I don't believe xmrig will be compiled for aarch64 on every release because of the low demand.

I don't have switch 
L4T for jetson nano or jetson Xavier nx or agx 

## benthetechguy | 2021-03-13T03:02:35+00:00
xmrig compiled for aarch64 works on any aarch64 device, so I don't know exactly what you mean.
If you're talking about cuda compatibility, I don't know if xmrig's cuda module will build for arm, but I can try.

## leonpano2006 | 2021-03-13T11:59:07+00:00
yes about cuda compatibility can you test please?

## benthetechguy | 2021-03-15T01:37:23+00:00
I have compiled xmrig for aarch64 with CUDA for you [here](https://github.com/xmrig/xmrig/files/6138232/xmrig-6.10.0-linux-cuda10_2-arm64.tar.gz). Keep in mind that you can always compile this for yourself, it's not very hard. I doubt that xmrig aarch64 cuda will be included in every release because of the low demand, and the dev might not even have an arm machine with an nvidia gpu to compile it with as they are not very common.

## leonpano2006 | 2021-03-15T11:03:41+00:00
> I have compiled xmrig for aarch64 with CUDA for you [here](https://github.com/xmrig/xmrig/files/6138232/xmrig-6.10.0-linux-cuda10_2-arm64.tar.gz). Keep in mind that you can always compile this for yourself, it's not very hard. I doubt that xmrig aarch64 cuda will be included in every release because of the low demand, and the dev might not even have an arm machine with an nvidia gpu to compile it with as they are not very common.

Thank you very much
I have no clue to edit source code
Again thank you a lot

## benthetechguy | 2021-03-15T14:12:47+00:00
You don't need to edit any source code, just follow the [compilation instructions](https://xmrig.com/docs/miner/build/ubuntu), very simple.

## benthetechguy | 2021-03-19T21:05:51+00:00
@xmrig safe to close this probably

## leonpano2006 | 2021-03-19T21:59:33+00:00
> @xmrig safe to close this probably

Closed

# Action History
- Created by: leonpano2006 | 2021-03-11T19:26:33+00:00
- Closed at: 2021-03-19T21:59:22+00:00
