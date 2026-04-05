---
title: OpenCL on ARM RPI 4 - OpenCL initialised successfully.
source_url: https://github.com/xmrig/xmrig/issues/2907
author: KodeMunkie
assignees: []
labels: []
created_at: '2022-01-27T20:25:32+00:00'
updated_at: '2022-01-28T20:52:30+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I've recently built [clvk](https://github.com/kpet/clvk) which is an OpenCL wrapper around Vulkan, which seems to work successfully  (at least their simple tests pass), on the RPI 4 8GB  (Raspberry PI OS 64bit), for its Broadcom Videocore 6 SoC GPU.
I'd like to mine Monero (rx/0) using the GPU, this is more or less an academic exercise to see if it can be achieved due to obvious performance issues.

I have modified a couple of xmrig files to allow this non valid OpenCL platform to start ([changes.txt attached here](https://github.com/xmrig/xmrig/files/7953561/changes.txt) as per GPL 3 license).

Aside from some missing/incorrect summary data (see output below) it seems like it may work, however as you can see the pool's response stated that no algorithms are supported which I believe means that the GPU is not registered as supporting rx/0. On other platforms a GPU can be used to mine using rx/0.

Is it possible to enable rx/0 on this ARM/OpenCL implementation and if so how?

Here's my last run

```
WARNING: v3dv is neither a complete nor a conformant Vulkan implementation. Testing use only.
WARNING: lavapipe is not a conformant vulkan implementation, testing use only.
 * ABOUT        XMRig/6.16.2 gcc/10.2.1
 * LIBS         libuv/1.40.0 OpenSSL/1.1.1k hwloc/2.4.1
 * HUGE PAGES   supported
 * 1GB PAGES    unavailable
 * CPU          ARM Cortex-A72 (1) 64-bit -AES
                L2:0.0 MB L3:0.0 MB 4C/4T NUMA:1
 * MEMORY       3.3/7.5 GB (44%)
 * DONATE       0%
 * POOL #1      gulf.moneroocean.stream:10002 algo auto
 * COMMANDS     hashrate, pause, resume, results, connection
 * ADL          disabled (failed to load ADL)
 * OPENCL       #0 (null)/(null)
 * OPENCL GPU   #0 n/a V3D 4.2 0 MHz cu:1 mem:128/512 MB
 * CUDA         disabled
[2022-01-27 20:07:39.443]  net      gulf.moneroocean.stream:10002 error: "algo array must include at least one supported pool algo: []", code: -1
```

# Discussion History
## Spudz76 | 2022-01-27T22:51:50+00:00
512MB of memory with 128MB free will mine approximately nothing.

RandomX needs 2080MB of VRAM, or `dataset_host` mode which will go to system RAM for the dataset accesses (super super super slow).  But then of course you need 2080MB free of system RAM (looks like you do)

So then like in the `opencl->rx` definition:
```
        "rx": [
            {
                "gcn_asm": false,
                "dataset_host": true
            }
        ],
```

And then it might work but 128MB allocatable may still mean it can't do anything.

I'd check the `clvk` code to see if it has dumb limits on VRAM that are less than the hardware actually has and try fixing it there, along with how it doesn't have any platform-name and other serious bugs.

## KodeMunkie | 2022-01-27T23:34:41+00:00
There's definitely a bug/incomplete feature in the vulkan/opencl API somewhere since the PI actually has 256MB allocated for the GPU (and can be set up to 4GB I believe) but still going for the quick win I tried the definition and it didn't change anything - no algos available.

## Spudz76 | 2022-01-27T23:50:48+00:00
Likely some of the other missing information will hurt auto-sizing so it may not generate any definitions.

Does the config.json have anything at all for algorithm definitions?

`cu:1` is likely wrong also, and I'm betting some other useful bit of information that "will always be there" like things that `isValid()` wants aren't there with this very incomplete shim.  Perhaps find the things`isValid()` looks for and see if you can hack the clvk code to set those rather than breaking minimum OpenCL specs and leaving them null.

Another piece that is likely unsupported would be runtime compilation, which is a problem since the kernel code is generated on the fly with your blocks/threads/etc and compiled through OpenCL's runtime compilation.  That would block it from working pretty much regardless of other missing information or filling in manual block/thread settings if it can't auto-size.

## Spudz76 | 2022-01-27T23:52:20+00:00
Is there no native OpenCL implementation for that SoC?  Seems odd.

## KodeMunkie | 2022-01-28T00:37:40+00:00
No native implementation is available for the Videocore 6 - from reading around nobody has had both the skills or motivation.
Although the Vulkan implementation is actually conformant, the vlck project is experimental and as far as I've read in the issue logs as well as being incomplete there are some things that Vulkan doesn't provide that OpenCL needs to, so I assume these will have been stubbed and is what's causing the incorrect memory.

## Pyogenics | 2022-01-28T20:52:30+00:00
I saw some kind of CL lib for the vc4 somewhere, idk where it is as I saw it quite some time ago.

# Action History
- Created by: KodeMunkie | 2022-01-27T20:25:32+00:00
