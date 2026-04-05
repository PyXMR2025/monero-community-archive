---
title: Xmrig 6.15.2 Kawpow error
source_url: https://github.com/xmrig/xmrig/issues/2663
author: Chowdary1999
assignees: []
labels: []
created_at: '2021-10-31T21:33:23+00:00'
updated_at: '2025-06-20T11:10:26+00:00'
type: issue
status: closed
closed_at: '2025-06-20T11:10:26+00:00'
---

# Original Description
 error CL_INVALID_GLOBAL_OFFSET when calling clEnqueueNDRangeKernel for kernel progpow_search
thread #0 failed with error CL_INVALID_GLOBAL_OFFSET

Device : Apple MacBook Pro
Software version :  macOS Monterey Version 12.0
Procesor : 2.3 GHz Dual-Core Intel Core i5
E-gpu connected : AMD Radeon RX580
Open CL version : 1.2
<img width="920" alt="Screen Shot 2021-11-01 at 8 25 41 am" src="https://user-images.githubusercontent.com/51407838/139601900-795a044d-5063-41b3-a842-7699f61633f9.png">

<img width="696" alt="Screen Shot 2021-11-01 at 8 26 04 am" src="https://user-images.githubusercontent.com/51407838/139601901-c355de47-1f96-4c40-958e-e0b90e113612.png">

{
    "api": {
        "id": null,
        "worker-id": null
    },
    "http": {
        "enabled": false,
        "host": "127.0.0.1",
        "port": 0,
        "access-token": null,
        "restricted": true
    },
    "autosave": true,
    "background": false,
    "colors": true,
    "title": true,
    "randomx": {
        "init": -1,
        "init-avx2": -1,
        "mode": "auto",
        "1gb-pages": false,
        "rdmsr": true,
        "wrmsr": false,
        "cache_qos": false,
        "numa": true,
        "scratchpad_prefetch_mode": 1
    },
    "cpu": {
        "enabled": false,
        "huge-pages": true,
        "huge-pages-jit": false,
        "hw-aes": null,
        "priority": null,
        "memory-pool": false,
        "yield": true,
        "max-threads-hint": 100,
        "asm": true,
        "argon2-impl": null,
        "astrobwt-max-size": 550,
        "astrobwt-avx2": false,
        "cn-lite/0": false,
        "cn/0": false
    },
    "opencl": {
        "enabled": true,
        "cache": true,
        "loader": null,
        "astrobwt": [
            {
                "index": 0,
                "intensity": 64,
                "threads": [-1, -1]
            },
            {
                "index": 1,
                "intensity": 256,
                "threads": [-1, -1]
            }
        ],
        "cn": [
            {
                "index": 1,
                "intensity": 864,
                "worksize": 8,
                "strided_index": [1, 2],
                "threads": [-1, -1],
                "unroll": 8
            }
        ],
        "cn-heavy": [
            {
                "index": 1,
                "intensity": 288,
                "worksize": 8,
                "strided_index": [1, 2],
                "threads": [-1, -1],
                "unroll": 8
            }
        ],
        "cn-lite": [
            {
                "index": 1,
                "intensity": 1728,
                "worksize": 8,
                "strided_index": [1, 2],
                "threads": [-1, -1],
                "unroll": 8
            }
        ],
        "cn-pico": [
            {
                "index": 0,
                "intensity": 768,
                "worksize": 8,
                "strided_index": [0, 2],
                "threads": [-1],
                "unroll": 8
            },
            {
                "index": 1,
                "intensity": 1728,
                "worksize": 8,
                "strided_index": [2, 2],
                "threads": [-1, -1],
                "unroll": 8
            }
        ],
        "cn/2": [
            {
                "index": 1,
                "intensity": 864,
                "worksize": 8,
                "strided_index": [2, 2],
                "threads": [-1, -1],
                "unroll": 8
            }
        ],
        "cn/upx2": [
            {
                "index": 0,
                "intensity": 768,
                "worksize": 8,
                "strided_index": [0, 2],
                "threads": [-1],
                "unroll": 8
            },
            {
                "index": 1,
                "intensity": 1728,
                "worksize": 8,
                "strided_index": [2, 2],
                "threads": [-1, -1],
                "unroll": 8
            }
        ],
        "kawpow": [
            {
                "index": 1,
                "intensity": 9437184,
                "worksize": 256,
                "threads": [-1]
            }
        ],
        "rx": [
            {
                "index": 0,
                "intensity": 320,
                "worksize": 8,
                "threads": [-1],
                "bfactor": 6,
                "gcn_asm": false,
                "dataset_host": true
            },
            {
                "index": 1,
                "intensity": 576,
                "worksize": 8,
                "threads": [-1, -1],
                "bfactor": 6,
                "gcn_asm": false,
                "dataset_host": false
            }
        ],
        "rx/arq": [
            {
                "index": 0,
                "intensity": 768,
                "worksize": 8,
                "threads": [-1],
                "bfactor": 6,
                "gcn_asm": false,
                "dataset_host": true
            },
            {
                "index": 1,
                "intensity": 576,
                "worksize": 8,
                "threads": [-1, -1],
                "bfactor": 6,
                "gcn_asm": false,
                "dataset_host": false
            }
        ],
        "rx/wow": [
            {
                "index": 0,
                "intensity": 704,
                "worksize": 8,
                "threads": [-1],
                "bfactor": 6,
                "gcn_asm": false,
                "dataset_host": true
            },
            {
                "index": 1,
                "intensity": 576,
                "worksize": 8,
                "threads": [-1, -1],
                "bfactor": 6,
                "gcn_asm": false,
                "dataset_host": false
            }
        ],
        "cn-lite/0": false,
        "cn/0": false
    },
    "cuda": {
        "enabled": false,
        "loader": null,
        "cn-lite/0": false,
        "cn/0": false
    },
    "log-file": null,
    "donate-level": 1,
    "donate-over-proxy": 1,
    "pools": [
        {
            "algo": "kawpow",
            "coin": null,
            "url": "kp.unmineable.com:3333",
            "user": xxxxxx,
            "pass": "x",
            "rig-id": null,
            "nicehash": false,
            "keepalive": false,
            "enabled": true,
            "tls": false,
            "tls-fingerprint": null,
            "daemon": false,
            "socks5": null,
            "self-select": null,
            "submit-to-origin": false
        }
    ],
    "retries": 5,
    "retry-pause": 5,
    "print-time": 60,
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
## Spudz76 | 2021-10-31T22:15:20+00:00
Master branch will not (yet) work.

Dev branch contains all my patches which fix this.  Build from `dev` branch, or await next `master` release so the pre-builds contain the fixes.

## Chowdary1999 | 2021-10-31T22:19:09+00:00
is there any specific link for that repo, seems like when ever I tried to build from the dev branches and look for the docs, it takes me to the current release page https://github.com/xmrig/xmrig/releases

## Spudz76 | 2021-10-31T22:26:50+00:00
You just checkout the repo like normal which will give you the `master` branch by default. Like `cd /usr/src/ && git clone https://github.com/xmrig/xmrig.git`

Then `cd /usr/src/xmrig/ && git checkout dev` and you've got the `dev` branch code.  Build as normal from there.

## Chowdary1999 | 2021-10-31T22:28:12+00:00
Thanks for that, Will try that now

## Chowdary1999 | 2021-11-01T02:01:49+00:00
<img width="982" alt="Screen Shot 2021-11-01 at 12 59 12 pm" src="https://user-images.githubusercontent.com/51407838/139611399-36796ee5-06da-4ed5-a14d-e357c4dce9dc.png">
Yep just built from the dev branch, but still the same error

## hogboon | 2022-01-07T14:13:03+00:00
Same CL_INVALID_GLOBAL_OFFSET error here on a new Mac mini 2018 I bought few days ago to take advantage of TB3 ports. I've tried dev branch, same error. 

dev-fixAppleOpenCL of @Spudz76 no longer exists... 

## Spudz76 | 2022-01-08T00:23:36+00:00
Because that branch was merged.  Must be a new bug.

## hogboon | 2022-01-10T15:15:03+00:00
@Chowdary1999 can I ask if you found some solution in the meanwhile? Thanks 

## Chowdary1999 | 2022-01-10T21:11:13+00:00
I mean, looks like the XMrig cannot compile for the macbooks with lower than i7 multithreaded processors, i have tested this out on multiple laptops and I found that it is having issues with allocation of the thread memory for any i5 macbook. 

I5 13” MacbookPro - Doesn’t Work
I5 15” MacbookPro - Doesn’t Work
I7 13” MacbookPro - Works
I7 16” MacbookPro - Works
I9 16” MacbookPro - Works

So I’ve decided to use my i9 16” MBP for mining. This is very frustrating so hopefully XMrig fixes the issues in the future releases.

Lemme know if u guys found any solution for this.

> On 11 Jan 2022, at 2:15 am, hogboon ***@***.***> wrote:
> 
> ﻿
> @Chowdary1999 can I ask if you found some solution in the meanwhile? Thanks
> 
> —
> Reply to this email directly, view it on GitHub, or unsubscribe.
> Triage notifications on the go with GitHub Mobile for iOS or Android. 
> You are receiving this because you were mentioned.


## hogboon | 2022-01-10T21:15:06+00:00
I3 2018 MacMini - Doesn't Work..... 

## Chowdary1999 | 2022-01-10T21:19:06+00:00
Yeah wouldn’t be surprised, like I mentioned any processor lower than i7  is having this issue. Hopefully xmrig responds.


> On 11 Jan 2022, at 8:15 am, hogboon ***@***.***> wrote:
> 
> ﻿
> I3 2018 MacMini - Doesn't Work.....
> 
> —
> Reply to this email directly, view it on GitHub, or unsubscribe.
> Triage notifications on the go with GitHub Mobile for iOS or Android. 
> You are receiving this because you were mentioned.


## Spudz76 | 2022-01-10T21:23:13+00:00
Are those all on the same 12.0?

## hogboon | 2022-01-10T21:28:09+00:00
On Mac Pro 2013 with 12.0 it works. Not on i3 Mini 2018 with 12.0 (or 11.0 downgrading).  

## Chowdary1999 | 2022-01-11T01:05:54+00:00
Whats ur processor on mac pro ? Is it dual core or octa core 

With Regards 
HEMANTH KUMAR VEJANDLA


> On 11 Jan 2022, at 8:28 am, hogboon ***@***.***> wrote:
> 
> ﻿
> On Mac Pro 2013 with 12.0 it works. Not on i3 Mini 2018 with 12.0 (or 11.0 downgrading).
> 
> —
> Reply to this email directly, view it on GitHub, or unsubscribe.
> Triage notifications on the go with GitHub Mobile for iOS or Android. 
> You are receiving this because you were mentioned.


## hogboon | 2022-01-11T08:33:55+00:00
4-Core originally, upgraded to 12-core recently. 

Have you ever tried to GPU mine with xmrig with an algo different than kawpow? 

## Chowdary1999 | 2022-01-11T20:47:26+00:00
Yeah coz ur processor is not dual core it will definitely work.

Yes I tried random x but no luck in using ethash or etchash



> On 11 Jan 2022, at 7:34 pm, hogboon ***@***.***> wrote:
> 
> ﻿
> 4-Core originally, upgraded to 12-core recently.
> 
> Have you ever tried to GPU mine with xmrig with an algo different than kawpow?
> 
> —
> Reply to this email directly, view it on GitHub, or unsubscribe.
> Triage notifications on the go with GitHub Mobile for iOS or Android. 
> You are receiving this because you were mentioned.


## hogboon | 2022-01-11T21:14:11+00:00
Ok you are mining on unMineable, and you need kawpow if you (we) are on Intel Mac. I was asking if you ever tried some other algorithm supported by xmrig on OpenCL with other pools: reading from the config.json: astrobwt, cn, cn-heavy cn-lite etc etc. 
I've tried with no luck. But I'm a newbie. 

Anyway, I think that @Spudz76 is doing his magic now. We must have a little patience. 

## Spudz76 | 2022-01-11T22:52:26+00:00
Nah, I'm not doing anything, since I don't have any of these platforms.

Fixing OpenCL the other time simply removed the AMD-specific stuff when it's not AMD-platform (but is AMD-device).  And then it only happened to work everywhere, luck more so, simply from following specs better.

This feels more like real internal breakage in Apple OpenCL, perhaps only with OS 12.x and more than two cores.  None of which (cpu core count) has anything to do with how xmrig inits OpenCL at all.  Therefore why I suspect it's deeper within the abandoned Apple OpenCL which they have no problems breaking since it was supposed to be nonexistent by 12.x

## Chowdary1999 | 2022-01-11T23:09:41+00:00
The problem is that although i tried to downgrade the os and try to run with previous versions of opencl its still blocked on the dual core processors, which is not very understandable on the intention of apple for doing that.

> On 12 Jan 2022, at 9:52 am, Tony Butler ***@***.***> wrote:
> 
> ﻿
> Nah, I'm not doing anything, since I don't have any of these platforms.
> 
> Fixing OpenCL the other time simply removed the AMD-specific stuff when it's not AMD-platform (but is AMD-device). And then it only happened to work everywhere, luck more so, simply from following specs better.
> 
> This feels more like real internal breakage in Apple OpenCL, perhaps only with OS 12.x and more than two cores. None of which (cpu core count) has anything to do with how xmrig inits OpenCL at all. Therefore why I suspect it's deeper within the abandoned Apple OpenCL which they have no problems breaking since it was supposed to be nonexistent by 12.x
> 
> —
> Reply to this email directly, view it on GitHub, or unsubscribe.
> Triage notifications on the go with GitHub Mobile for iOS or Android. 
> You are receiving this because you were mentioned.


## Spudz76 | 2022-01-12T00:14:27+00:00
Okay so it's not related to something new, that's a good information point.

I still never went much deeper than getting the kernels to pass realtime compilation which it seems like is still successful, just the actual communication with the kernel after that is broken.  Suprising it generated the dataset fine also, and then fails.

Could be attempting to setup multiple pipes automatically, does forcing affinity to a single core help?  xmrig doesn't benefit from multipipe anyway since the nonce feed and result feed are not using heavy transfers, but if the OpenCL Platform decides to setup multipipe anyway and then that doesn't work for some reason with "too many cores" then affinity might cause it to only use a single pipe since "there are no other cores (for you)".

## Chowdary1999 | 2022-01-12T00:19:21+00:00
I guess that might help


> On 12 Jan 2022, at 11:14 am, Tony Butler ***@***.***> wrote:
> 
> ﻿
> Okay so it's not related to something new, that's a good information point.
> 
> I still never went much deeper than getting the kernels to pass realtime compilation which it seems like is still successful, just the actual communication with the kernel after that is broken. Suprising it generated the dataset fine also, and then fails.
> 
> Could be attempting to setup multiple pipes automatically, does forcing affinity to a single core help? xmrig doesn't benefit from multipipe anyway since the nonce feed and result feed are not using heavy transfers, but if the OpenCL Platform decides to setup multipipe anyway and then that doesn't work for some reason with "too many cores" then affinity might cause it to only use a single pipe since "there are no other cores (for you)".
> 
> —
> Reply to this email directly, view it on GitHub, or unsubscribe.
> Triage notifications on the go with GitHub Mobile for iOS or Android. 
> You are receiving this because you were mentioned.


# Action History
- Created by: Chowdary1999 | 2021-10-31T21:33:23+00:00
- Closed at: 2025-06-20T11:10:26+00:00
