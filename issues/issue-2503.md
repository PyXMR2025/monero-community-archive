---
title: 'kawpow algo error: thread #0 failed with error CL_OUT_OF_HOST_MEMORY'
source_url: https://github.com/xmrig/xmrig/issues/2503
author: redwineforgaea
assignees: []
labels: []
created_at: '2021-07-31T00:29:26+00:00'
updated_at: '2025-06-20T11:11:34+00:00'
type: issue
status: closed
closed_at: '2025-06-20T11:11:34+00:00'
---

# Original Description
although this is an error, for months, I have been trying to get xmrig to work with my amdgpu.
I finally got it running with manjaro, and huge pages!
I can use xmrig with both cpu and OpenCL/AMD with RandomX, without any errors, if I include the "export variables"
I have an older laptop with a hybrid AMD R5 M335.
I have everything working properly, and all programs can access the amd, even without DRI_PRIME=1
I have 2 other miners working, and can access  AMD/OpenCL - phoenixminer, and nanominer.
I have nanominer accessing the AMD/OpenCL and mining RVN with the kawpow algo.

I HAVE to use these variables in order to get the miners to work with AMD:
export GPU_FORCE_64BIT_PTR=1
export GPU_USE_SYNC_OBJECTS=1
export GPU_MAX_ALLOC_PERCENT=100
export GPU_SINGLE_ALLOC_PERCENT=100
export GPU_MAX_HEAP_SIZE=100

Since I can use XMRIG with OpenCL and RandomX, I'm suspicious I have the kawpow algo setup wrongly.
BUT, I can't find any google info or ??? on how to work with that algo and AMD. Could it have anything with slowly building the DAG file? I found a few examples of the algo variables for kawpow, but none helped me. Thank you for any help! 

$ lspci:
01:00.0 Display controller: Advanced Micro Devices, Inc. [AMD/ATI] Sun XT [Radeon HD 8670A/8670M/8690M / R5 M330 / M430 / Radeon 520 Mobile] (rev 81)

-------------------------------------------

$ glxinfo | egrep -i 'device|memory'
    Device: Mesa Intel(R) HD Graphics 520 (SKL GT2) (0x1916)
    Video memory: 3072MB
    Unified memory: yes
    GL_AMD_performance_monitor, GL_AMD_pinned_memory, 
    GL_AMD_pinned_memory, GL_AMD_query_buffer_object, 

---------------------------------------------
config.json:
{
    "api": {
        "id": null,
        "worker-id": null
    },
    "http": {
        "enabled": true,
        "host": "127.0.0.1",
        "port": 8080,
        "access-token": null,
        "restricted": true
    },
    "autosave": true,
    "background": false,
    "colors": true,
    "title": true,
    "randomx": {
        "init": -1,
        "init-avx2": 1,
        "mode": "auto",
        "1gb-pages": false,
        "rdmsr": true,
        "wrmsr": true,
        "cache_qos": false,
        "numa": true,
        "scratchpad_prefetch_mode": 1
    },
    "cpu": {
        "enabled": false,
        "huge-pages": true,
        "huge-pages-jit": true,
        "hw-aes": null,
        "priority": 2,
        "memory-pool": true,
        "yield": false,
        "asm": true,
        "argon2-impl": null,
        "astrobwt-max-size": 550,
        "astrobwt-avx2": false,
        "argon2": [0, 1, 2, 3],
        "astrobwt": [0, 1, 2, 3],
        "cn": [
            [1, 0],
            [1, 2]
        ],
        "cn-heavy": [
            [1, 0]
        ],
        "cn-lite": [
            [1, 0],
            [1, 1],
            [1, 2],
            [1, 3]
        ],
        "cn-pico": [
            [2, 0],
            [2, 1],
            [2, 2],
            [2, 3]
        ],
        "cn/upx2": [
            [2, 0],
            [2, 1],
            [2, 2],
            [2, 3]
        ],
        "rx": {
    	  "intensity": 1,
          "threads": 2,
          "affinity": -1
	},
        "rx/wow": [0, 1, 2, 3],
        "cn/0": false,
        "cn-lite/0": false,
        "rx/arq": "rx/wow",
        "rx/keva": "rx/wow"
    },
    "opencl": {
        "enabled": true,
        "cache": true,
        "loader": null,
        "platform": "AMD",
        "adl": true,
        "astrobwt": [
            {
                "index": 0,
                "intensity": 128,
                "threads": [-1, -1]
            }
        ],
        "cn": [
            {
                "index": 0,
                "intensity": 496,
                "worksize": 8,
                "strided_index": [1, 2],
                "threads": [-1, -1],
                "unroll": 8
            }
        ],
        "cn-heavy": [
            {
                "index": 0,
                "intensity": 176,
                "worksize": 8,
                "strided_index": [1, 2],
                "threads": [-1, -1],
                "unroll": 8
            }
        ],
        "cn-lite": [
            {
                "index": 0,
                "intensity": 1000,
                "worksize": 8,
                "strided_index": [1, 2],
                "threads": [-1, -1],
                "unroll": 8
            }
        ],
        "cn-pico": [
            {
                "index": 0,
                "intensity": 1000,
                "worksize": 8,
                "strided_index": [2, 2],
                "threads": [-1, -1],
                "unroll": 8
            }
        ],
        "cn/2": [
            {
                "index": 0,
                "intensity": 496,
                "worksize": 8,
                "strided_index": [2, 2],
                "threads": [-1, -1],
                "unroll": 8
            }
        ],
        "cn/upx2": [
            {
                "index": 0,
                "intensity": 1310720,
                "worksize": 256,
                "threads": [-1],
                "unroll" : 8
            }
        ],
        "kawpow": [
            {
                "index": 0,
                "intensity": 1,
                "worksize": 256,
                "threads": [1],
		"unroll": 8
            }
        ],
        "rx": [
            {
                "index": 0,
                "intensity": 64,
                "worksize": 8,
                "threads": [0, 2],
                "bfactor": 6,
                "gcn_asm": false,
                "dataset_host": false
            }
        ],
        "cn/0": false,
        "cn-lite/0": false
    },
    "cuda": {
        "enabled": false,
        "loader": null,
        "nvml": true
    },
    "log-file": null,
    "donate-level": 1,
    "donate-over-proxy": 1,
    "pools": [
        {
            "algo": "kawpow",
            "coin": "rvn",
            "url": "xxx.xxx.com:6600",
            "user": "xxx",
            "pass": null,
            "rig-id": "xxx",
            "nicehash": false,
            "keepalive": false,
            "enabled": true,
            "tls": false,
            "daemon": false,
            "socks5": null,
            "self-select": null,
            "submit-to-origin": false
        }
    ],
    "retries": 5,
    "retry-pause": 5,
    "print-time": 60,
    "health-print-time": 60,
    "dmi": true,
    "syslog": false,
    "tls": {
        "enabled": false,
        "protocols": null,
        "cert": null,
        "cert_key": null,
        "ciphers": null,
        "ciphersuites": null,
        "dhparam": null
    },
    "dns": {
        "ipv6": false,
        "ttl": 30
    },
    "user-agent": null,
    "verbose": 0,
    "watch": true,
    "pause-on-battery": false,
    "pause-on-active": false
}


# Discussion History
## redwineforgaea | 2021-07-31T00:34:51+00:00
--------------------------------------

$ sudo ./xmrig -c /home/will/Miner/config.json 
 * ABOUT        XMRig/6.13.1 gcc/11.1.0
 * LIBS         libuv/1.42.0 OpenSSL/1.1.1k hwloc/2.5.0
 * HUGE PAGES   supported
 * 1GB PAGES    disabled
 * CPU          Intel(R) Core(TM) i7-6500U CPU @ 2.50GHz (1) 64-bit AES
                L2:0.5 MB L3:4.0 MB 2C/4T NUMA:1
 * MEMORY       6.0/7.7 GB (79%)
                DIMM A: 4 GB DDR3 @ 1600 MHz HMT451S6BFR8A-PB  
                DIMM B: 4 GB DDR3 @ 1600 MHz HMT451S6BFR8A-PB  
 * MOTHERBOARD  Dell Inc. - 05NVNV
 * DONATE       1%
 * ASSEMBLY     auto:intel
 * POOL #1      us1.xxx.com:6600 coin ravencoin
 * COMMANDS     hashrate, pause, resume, results, connection
 * HTTP API     127.0.0.1:8080 
 * ADL          press e for health report
 * OPENCL       #0 AMD Accelerated Parallel Processing/OpenCL 2.1 AMD-APP (3224.4)
 * OPENCL GPU   #0 01:00.0 AMD Radeon (TM) R5 M335 (Hainan) 750 MHz cu:5 mem:3072/3072 MB
 * CUDA         disabled
[2021-07-30 16:31:48.584]  net      use pool us1.xxx.com:6600  52.224.9.152
[2021-07-30 16:31:49.538]  net      new job from us1.xxx.com:6600 diff 431M algo kawpow height 1864457
[2021-07-30 16:31:49.538]  opencl   use profile  kawpow  (1 thread) scratchpad 32 KB
|  # | GPU |  BUS ID | INTENSITY | WSIZE | MEMORY | NAME
|  0 |   0 | 01:00.0 |   1310720 |   256 |   3054 | AMD Radeon (TM) R5 M335 (Hainan)
[2021-07-30 16:31:49.539]  opencl   error CL_OUT_OF_HOST_MEMORY when calling clCreateCommandQueueWithProperties
[2021-07-30 16:31:49.539]  opencl   thread #0 failed with error CL_OUT_OF_HOST_MEMORY
[2021-07-30 16:31:49.539]  opencl   thread #0 self-test failed
[2021-07-30 16:31:49.539]  opencl   disabled (failed to start threads)
[2021-07-30 16:32:07.831]  net      new job from us1.xxx.com:6600 diff 431M algo kawpow height 1864457
[2021-07-30 16:32:14.419]  net      new job from us1.xxx.com:6600 diff 431M algo kawpow height 1864458
[2021-07-30 16:32:45.688]  signal   Ctrl+C received, exiting
[2021-07-30 16:32:45.688]  opencl   stopped (0 ms)


## redwineforgaea | 2021-07-31T00:48:11+00:00
OH MY! well. i got it working. I created a basic config, and it started to work!

I can at least tell you, that xmrig is such an awesome miner!
I didn't want to use any other  miner but xmrig.
and now that it has kawpow support. i'm very happy.
thank you!


## redwineforgaea | 2021-08-02T04:20:07+00:00
Well, i have spent a day trying to get some shares from xmrig, but no luck.
I can mine and get shares via nanominer, but honestly i'm hoping i can get it to work with xmrig instead.
I finally have xmrig running on several computers, using the linux hugepages. so it makes sense to me, to use it for my older amd gpu. 
the  share difficulty = 431 MH, epoch 249 (3015 MB).
So it would take at least for me, an hour and a half to start getting  them, and then i do, but only with nanominer.

is there anything i can do in xmrig to improve my changes of getting  shares?
I use these variables in a script:
export GPU_FORCE_64BIT_PTR=1
export GPU_USE_SYNC_OBJECTS=1
export GPU_MAX_ALLOC_PERCENT=100
export GPU_SINGLE_ALLOC_PERCENT=100
export GPU_MAX_HEAP_SIZE=100

thank you!

## redwineforgaea | 2021-08-02T04:20:32+00:00
ugh. have to reopen the case... sorry. my bad.

## SChernykh | 2021-08-02T07:39:37+00:00
```
Video memory: 3072MB
epoch 249 (3015 MB)
```
I think this is the main reason. Other miners probably use a tiny bit less memory, but they will stop mining in a couple of weeks too.

## redwineforgaea | 2021-08-02T11:35:51+00:00
i actually have 4.098g of memory, and its on linux. that's why i went to linux from windows. 

## Spudz76 | 2021-08-02T20:02:17+00:00
No, GPU memory, not system memory.  Entire DAG thing which is 3015MB must fit into 3072MB total provided by GPU.  If you are using Xorg rather than shell-only then definitely there is more than 57MB of VRAM already used for graphics, so there is no room for 3015MB thus the no memory error.  OUT_OF_HOST_MEMORY doesn't mean only system memory rather the GPU didn't have enough so the system memory mapping with VRAM backing could not be allocated.

## redwineforgaea | 2021-08-02T20:49:01+00:00
I agree with you. This is what i read too. BUT... my AMD, R5 M335 is a Discrete GPU, and the system uses the primary Intel HD, as its display. So the XFCE uses that card. The Discrete AMD has nothing accessing it. That's  why you try and use the  miner with the DRI_PRIME=1 to get the software to dedicate to that GPU. since that's the case, there is 4.078G of memory available. See what I mean now? other wise, what you say IS correct.

## SChernykh | 2021-08-02T22:00:40+00:00
This GPU has only 2 GB memory: https://www.techpowerup.com/gpu-specs/radeon-r5-m335.c2692
```
Memory Size 2 GB
```

## redwineforgaea | 2021-08-02T23:36:54+00:00
no, look closer please. 
read the whole page... down at the bottom, you will see:` Dell R5 M335 4 GB`
https://www.techpowerup.com/gpu-specs/dell-r5-m335-4-gb.b5409

This is my Laptop. lol!
Now, what's interesting, is that i'm also trying to use xmrig, which now has kowpow as well, and IT can access almost all of the 4G of memory I have: `4062M / 4091M VRAM  99.29%` (info via radeontop).

BUT, xmrig, for some reason, CAN'T send shares up to the pool. I have just changed to a pool, with a lower difficulty, so its a wait and see. 
But, i'd also like to see if nanominer can do something with extra timings, or something to grab all of the ram.
thank you.

## redwineforgaea | 2021-08-03T05:31:17+00:00
I have been running xmrig on a new pool, with a small Diff of 167M,
and i'm getting this error: 

`[2021-08-03 01:19:02.679]  opencl   GPU #0 COMPUTE ERROR`

I get it about once every few minutes. but as far as I can see, xmrig still accesses the gpu, and there's no shut down.
how do I go about trying to see what the error could be?

thank you!

## redwineforgaea | 2021-08-06T20:37:14+00:00
Ok, so from what i can see, xmrig starts off creating the 3G DAG that is needed kawpow, but then it goes and grabs almost all of the 4G of GPU memory, when it only needs the 3G for the DAG. why would it grab all of the gpu memory when it needs just 3G?
I still get that error: opencl GPU #0 COMPUTE ERROR

## DeeDeeRanged | 2021-08-20T10:03:36+00:00
Try kawpow with gminer to see if it does the same. By the way kawpow is very power hungry way more than mining etheash or whatever. So make sure you laptop has enough cooling.

## Deep0310 | 2021-08-20T10:08:36+00:00
Oke
Please i just needed your team stop send message to me

Pada tanggal Jum, 20 Agt 2021 17.03, DeeDeeRanged ***@***.***>
menulis:

> Try kawpow with gminer to see if it does the same. By the way kawpow is
> very power hungry way more than mining etheash or whatever. So make sure
> you laptop has enough cooling.
>
> —
> You are receiving this because you are subscribed to this thread.
> Reply to this email directly, view it on GitHub
> <https://github.com/xmrig/xmrig/issues/2503#issuecomment-902583232>, or
> unsubscribe
> <https://github.com/notifications/unsubscribe-auth/AU22PXXT7S672M27MGF2FCLT5YSAXANCNFSM5BJN2G5A>
> .
> Triage notifications on the go with GitHub Mobile for iOS
> <https://apps.apple.com/app/apple-store/id1477376905?ct=notification-email&mt=8&pt=524675>
> or Android
> <https://play.google.com/store/apps/details?id=com.github.android&utm_campaign=notification-email>
> .
>


## Deep0310 | 2021-08-20T10:11:42+00:00
I'm not have laptop i just have phone
Yesterday i'm login github with handphone

Pada tanggal Jum, 20 Agt 2021 17.03, DeeDeeRanged ***@***.***>
menulis:

> Try kawpow with gminer to see if it does the same. By the way kawpow is
> very power hungry way more than mining etheash or whatever. So make sure
> you laptop has enough cooling.
>
> —
> You are receiving this because you are subscribed to this thread.
> Reply to this email directly, view it on GitHub
> <https://github.com/xmrig/xmrig/issues/2503#issuecomment-902583232>, or
> unsubscribe
> <https://github.com/notifications/unsubscribe-auth/AU22PXXT7S672M27MGF2FCLT5YSAXANCNFSM5BJN2G5A>
> .
> Triage notifications on the go with GitHub Mobile for iOS
> <https://apps.apple.com/app/apple-store/id1477376905?ct=notification-email&mt=8&pt=524675>
> or Android
> <https://play.google.com/store/apps/details?id=com.github.android&utm_campaign=notification-email>
> .
>


## DeeDeeRanged | 2021-08-20T10:49:56+00:00
If you do not want anymore messages close this issue.

## hammadmallick | 2021-11-03T12:54:45+00:00
hello, id like to contact you regarding a similar issue, can you give me your email id or any means of communication you prefer. 


## redwineforgaea | 2021-11-03T15:06:58+00:00
hi there. its ***@***.***

On Wed, Nov 3, 2021 at 8:54 AM hammadmallick ***@***.***>
wrote:

> hello, id like to contact you regarding a similar issue, can you give me
> your email id or any means of communication you prefer.
>
> —
> You are receiving this because you modified the open/close state.
> Reply to this email directly, view it on GitHub
> <https://github.com/xmrig/xmrig/issues/2503#issuecomment-959004214>, or
> unsubscribe
> <https://github.com/notifications/unsubscribe-auth/AB7LI7CV25PXECWNVSQPHULUKEWKBANCNFSM5BJN2G5A>
> .
>


## hammadmallick | 2021-11-03T15:33:13+00:00
![image](https://user-images.githubusercontent.com/75981093/140091500-697f0c8e-06ec-4b5d-b273-3c1dfe702c03.png)

github is censoring your email kindly share email in a different format or on telegram. makk.9696242 @ gmail . com 

## redwineforgaea | 2021-11-03T15:42:24+00:00
how about this: https://twitter.com/technobuddha

On Wed, Nov 3, 2021 at 11:33 AM hammadmallick ***@***.***>
wrote:

> [image: image]
> <https://user-images.githubusercontent.com/75981093/140091500-697f0c8e-06ec-4b5d-b273-3c1dfe702c03.png>
>
> github is censoring your email kindly share email in a different format or
> on telegram. makk.9696242 @ gmail . com
>
> —
> You are receiving this because you modified the open/close state.
> Reply to this email directly, view it on GitHub
> <https://github.com/xmrig/xmrig/issues/2503#issuecomment-959463178>, or
> unsubscribe
> <https://github.com/notifications/unsubscribe-auth/AB7LI7AGQ3TU7BG7XBQRPRTUKFI4JANCNFSM5BJN2G5A>
> .
>


## hammadmallick | 2021-11-09T11:08:14+00:00
messaging you on Twitter is disabled. 


## hammadmallick | 2021-11-09T11:10:06+00:00
https://twitter.com/HammadZ60907338 this is me, please send me a message or anything else


# Action History
- Created by: redwineforgaea | 2021-07-31T00:29:26+00:00
- Closed at: 2025-06-20T11:11:34+00:00
