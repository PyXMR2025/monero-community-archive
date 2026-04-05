---
title: The system freezes after the start of the miner on Mac
source_url: https://github.com/xmrig/xmrig/issues/2528
author: AeShevch
assignees: []
labels: []
created_at: '2021-08-10T21:53:55+00:00'
updated_at: '2021-08-31T02:53:57+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Hello everyone!
I'm trying to run RVN mining on rx570, but the mac freezes immediately after launching xmrig.

macOs 10.14.6 

```
$ ./xmrig --no-cpu --opencl -o rvn.2miners.com:6060 -u RBUYz2dYwqGxTLnKUrcJCujrTgfY23B6W4 -p x -k -a kawpow
[2021-08-10 23:49:30.725] Error CL_INVALID_OPERATION when calling clGetDeviceInfo, param 0x4037
 * ABOUT        XMRig/6.14.0 clang/10.0.0
 * LIBS         libuv/1.41.0 OpenSSL/1.1.1k hwloc/2.4.1
 * HUGE PAGES   supported
 * 1GB PAGES    unavailable
 * CPU          Intel(R) Pentium(R) CPU G620 @ 2.60GHz (1) 64-bit -AES
                L2:0.5 MB L3:3.0 MB 2C/2T NUMA:1
 * MEMORY       6.4/16.0 GB (40%)
                DIMM_A0: 8 GB DDR3 @ 1067 MHz HMT41GU6MFR8C-PB
                DIMM_B0: 8 GB DDR3 @ 1067 MHz HMT41GU6MFR8C-PB
 * MOTHERBOARD  Acidanthera - Mac-42FD25EABCABB274
 * DONATE       1%
 * ASSEMBLY     auto:none
 * POOL #1      rvn.2miners.com:6060 algo kawpow
 * COMMANDS     hashrate, pause, resume, results, connection
[2021-08-10 23:49:30.757] Error CL_INVALID_OPERATION when calling clGetDeviceInfo, param 0x4037
 * OPENCL       #0 Apple/OpenCL 1.2 (Jan  5 2021 21:28:41)
 * OPENCL GPU   #0 n/a AMD Radeon RX 570 Compute Engine 300 MHz cu:32 mem:1024/4096 MB
 * CUDA         disabled
[2021-08-10 23:49:30.866]  net      use pool rvn.2miners.com:6060  51.89.99.172
[2021-08-10 23:49:30.866]  net      new job from rvn.2miners.com:6060 diff 4295M algo kawpow height 1880025
[2021-08-10 23:49:30.867]  opencl   use profile  kawpow  (1 thread) scratchpad 32 KB
|  # | GPU |  BUS ID | INTENSITY | WSIZE | MEMORY | NAME
|  0 |   0 |     n/a |   8388608 |   256 |   3071 | AMD Radeon RX 570 Compute Engine
[2021-08-10 23:49:30.872]  opencl   READY threads 1/1 (6 ms)
[2021-08-10 23:49:31.679]  opencl   KawPow program for period 626675 compiled (807ms)
[2021-08-10 23:49:32.360]  opencl   KawPow program for period 626676 compiled (681ms)
[2021-08-10 23:49:46.095]  net      new job from rvn.2miners.com:6060 diff 4295M algo kawpow height 1880026
[2021-08-10 23:49:46.723]  miner    KawPow light cache for epoch 250 calculated (15044ms)
[2021-08-10 23:49:59.633]  opencl   KawPow DAG for epoch 250 calculated (12781ms)
[2021-08-10 23:50:31.203]  miner    speed 10s/60s/15m n/a n/a n/a MH/s max 4.38 MH/s
```

config.json:
```
{
    "autosave": true,
    "cpu": false,
    "opencl": true,
    "cuda": false,
    "pools": [
        {
            "coin": null,
            "algo": "kawpow",
            "url": "rvn.2miners.com:6060",
            "user": "RBUYz2dYwqGxTLnKUrcJCujrTgfY23B6W4",
            "pass": "x",
            "tls": false,
            "keepalive": true,
            "nicehash": false
        }
    ]
}
```


# Discussion History
## Spudz76 | 2021-08-12T06:27:48+00:00
Hard GPU thrash essentially makes interface unresponsive, is it actual freeze forever, or just not updating the screen...?

Ctrl-C might stop it two minutes later and "unfreeze" and also update the screen as to what happened while it couldn't redraw.

## dg-Nacho | 2021-08-30T23:27:05+00:00
Once the config file is fully made after the start of xmrig, change the intensity in the KAWPOW section to 36864. It is crazy high at the moment. Hopefully you fixed it already.

## Spudz76 | 2021-08-31T02:53:57+00:00
I have a bunch of improvements for Apple OpenCL compatibility ( see #2345 ) I need to collate them as an acceptable PR.

# Action History
- Created by: AeShevch | 2021-08-10T21:53:55+00:00
