---
title: OpenCL failed on APPLE M1
source_url: https://github.com/xmrig/xmrig/issues/2012
author: noatte
assignees: []
labels:
- wontfix
- opencl
created_at: '2020-12-28T17:28:03+00:00'
updated_at: '2021-04-12T14:26:02+00:00'
type: issue
status: closed
closed_at: '2021-04-12T14:26:02+00:00'
---

# Original Description
Hello,
Whatever it's cpu + gpu or just gpu (with OpenCL) I get the following error :

![Capture d’écran 2020-12-28 à 18 17 03](https://user-images.githubusercontent.com/49617162/103231989-9794b180-4939-11eb-935e-1e01212c43d3.png)

here's my command : ./xmrig --no-cpu --opencl -o xmrpool.eu:9999 -u 4(...) -k --tls

I'm on macOS 11.1 (Mac mini)


# Discussion History
## noatte | 2021-02-04T14:34:26+00:00
Hello,
does someone know how to fix this ? I am still experiencing the issue (with cpu or no-cpu)

## Spudz76 | 2021-02-05T20:39:02+00:00
RandomX is not a GPU algorithm on purpose by design, even if it worked you would be losing (unless you are somehow on "free" electricity).  But time is never free, and other algos would rake in more profit over that fixed amount of time, even if you are stealing the watts.  So there is really no reason to run RandomX algo family on GPUs.

It is supported just for proof of concept mostly, and designed for Vega56/64/VII (if it works at all on any other type of chip, it's a bonus).  Also of note, whichever OS version you have has removed real OpenCL and is using the CL->Metal conversion layer which of course can't handle all OpenCL code properly (was probably tested with Tensorflow and called it good).  Some final version of OSX had the last real OpenCL but that version probably also doesn't have a M1 version so you're pretty stuck.

Similar to if KawPow were supported on CPU, there would also be no point in actually using it (hash per watt terrible).

## Spudz76 | 2021-02-05T20:46:31+00:00
Look into MoneroOcean if you want to be paid XMR for mining whatever algos your hardware is best at doing (auto-changed).
Then you run one xmrig set for CPU-only and a separate one configured for GPU-only and they run different algos, but the pool outputs only XMR to you (no hassle of managing 15 different coins).  The effective "XMR-equivalent" hashrate after exchange will be much higher than the native rates.  Note there is a fork with added features for that pool, important to making it autoswitch properly, and at least two additional algos that are not in mainstream.

RandomX may not be best on the M1 itself either.  But if it can mine some other half-as-valuable coin but gets four times the rate you're still ahead.

## Spudz76 | 2021-02-05T20:49:05+00:00
Also other simpler algos probably do work through the CL2Metal layer.  Like Haven or normal cryptonight types (not CN-R, probably).  It would be neat if you could test them all and let us know which ones work and which don't.

## kakadais | 2021-03-30T03:02:09+00:00
I think the question is not the efficiency of OpenCL. Maybe he could get some free power or just of curious. I agree and I want to know why xmrig is not working with any algorithm for any reason. Any Idea-?

## Spudz76 | 2021-03-30T22:12:01+00:00
MacOS eliminated OpenCL, and you wonder why OpenCL doesn't work?

There are no Metal-native miners since it would only work on MacOS.

cl2metal does not work for miner kernels and Apple probably wants it that way.

## kakadais | 2021-03-31T11:57:37+00:00
It seems that the confusion comes from the GPU info on xmrig process.
![image](https://user-images.githubusercontent.com/5265343/113140593-e992ef00-9228-11eb-8061-030869965f0e.png)

So there's no way to use M1 GPU to process xmrig hashing even the performance wouldn't be good enough or something?


## Spudz76 | 2021-04-01T19:18:27+00:00
Don't know, nobody on dev team has an M1.  Or as far as I know any other Apple.

Looks like it's only allowing 1GB per allocation which will force lower intensity even if it did realtime-compile properly.  Perhaps there is a similar setting to AMD's "GPU_MAX_ALLOC_PERCENT" environment variable somewhere, find it.  Or, since it's Apple, there is no setting for that.


# Action History
- Created by: noatte | 2020-12-28T17:28:03+00:00
- Closed at: 2021-04-12T14:26:02+00:00
