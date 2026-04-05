---
title: 'Feature Request: CN/UPX'
source_url: https://github.com/xmrig/xmrig/issues/2274
author: Lonnegan
assignees: []
labels:
- enhancement
- algo
created_at: '2021-04-17T00:25:45+00:00'
updated_at: '2022-07-17T06:55:06+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Hi,

is there the possibility to support CN/UPX officially? The coin goes thru the roof atm and there is only an old non-opensource variant of xmrig available for UPX. But I know, that you can do this miles better :) According to the coin developers they use a CN/lite-v1 variant, so perhaps it's just a little adjustment for you!

# Discussion History
## SChernykh | 2021-04-17T13:07:56+00:00
https://github.com/xmrig/xmrig/pull/2276
https://github.com/xmrig/xmrig-cuda/pull/95

## SChernykh | 2021-04-17T13:16:24+00:00
Bonus: MSVC version for Windows is faster than other miners by 3-4% on Ryzen CPUs.

## SChernykh | 2021-04-17T18:02:27+00:00
Update: https://github.com/xmrig/xmrig/pull/2278 - GCC version is a bit faster than MSVC now. This code is now the fastest on Zen3 with big margin (**7.8%** faster than SRBMiner, **15.7%** faster than XMRigCC on my **Ryzen 5 5600X**).

## Lonnegan | 2021-04-17T21:28:07+00:00
I am looking forward to the release so I can test it myself :)

## Lonnegan | 2021-04-17T22:15:05+00:00
I see you've made an extra asm for Zen3. Is the reason just because you have one ;) or are there specific things on Zen3 to make the effort?

And a second question: is UPX really a variant of cn/lite? Im asking this because cn/lite years ago worked very well on week CPUs with big caches (like AMD Bulldozer) doing Dual-Share or low-power-mode or what ever it was called in the past. With a scratchpad size of just 128 KB there would fit multiples (16) shares into the L2 cache of one Bulldozer module! :o :D 

## SChernykh | 2021-04-17T22:22:06+00:00
No, I just discovered that compiler generated code runs faster on Zen3 so I took it as is. I haven't started optimizing it specifically for Zen3 yet. That said, Zen3 has +18% IPC on this algo compared to Zen2.

UPX is a variant of Cryptonight V2 with smaller scratchpad and fewer iterations.

## Spudz76 | 2021-04-20T11:02:30+00:00
It is referred to as a cn/femto so yes it's like cn/lite, except even smaller than cn/pico by half again.  Should work nice for low-cache but fast-core.

I have good rates on an old Phenom-II X6 1035T which does pretty bad on everything else, haha:
```
        "cn/0": 34.06581852591736,
        "cn/1": 45.74613524029866,
        "cn/2": 45.74613524029866,
        "cn/r": 45.74613524029866,
        "cn/fast": 91.49227048059733,
        "cn/half": 91.49227048059733,
        "cn/xao": 45.74613524029866,
        "cn/rto": 45.74613524029866,
        "cn/rwz": 60.99484698706488,
        "cn/zls": 60.99484698706488,
        "cn/double": 22.87306762014933,
        "cn-lite/1": 203.38270826767519,
        "cn-heavy/xhv": 18.168452005881119,
        "cn-pico": 648.5236944415257,
        "cn-pico/tlo": 648.5236944415257,
        "cn/ccx": 68.13163705183472,
        "cn/upx2": 1820.4750893420224,
        "cn/gpu": 13.954464379393558,
        "rx/0": 501.73665929902116,
        "rx/wow": 1213.8503572929804,
        "rx/arq": 4923.8295633876909,
        "rx/sfx": 501.73665929902116,
        "argon2/chukwav2": 1222.210548434545,
        "astrobwt": 157.24789915966387,
        "panthera": 1244.8250499106862
```

## xmrig | 2021-04-20T14:43:42+00:00
[v6.12.0](https://github.com/xmrig/xmrig/releases/tag/v6.12.0) released.

## Shai0Hulud | 2021-04-20T16:13:41+00:00
> Update: #2278 - GCC version is a bit faster than MSVC now. This code is now the fastest on Zen3 with big margin (**7.8%** faster than SRBMiner, **15.7%** faster than XMRigCC on my **Ryzen 5 5600X**).

Ha, I was hoping it's also faster on Zen 2^^

GCC is exactly as fast as XMRigCC. Which is more than okay.

Thanx for all your work guys!

EDIT: You mentioned zen3 option, I guess for asm option? Is there documentation what options are possible? Is there one for Ryzen Zen 2 CPUs for example?

## SChernykh | 2021-04-20T16:19:42+00:00
> You mentioned zen3 option, I guess for asm option? Is there documentation what options are possible? Is there one for Ryzen Zen 2 CPUs for example?

`"asm":true,` in config.json should be enough to automatically detect the best code for your CPU. Currently there's a dedicated code for Zen3 and a single version for all other CPUs.

## benthetechguy | 2022-07-17T06:55:05+00:00
> there is only an old non-opensource variant of xmrig available for UPX

XMRig is licensed under GPLv3. Failure to provide source code for a fork of XMRig is a violation of its license.

# Action History
- Created by: Lonnegan | 2021-04-17T00:25:45+00:00
