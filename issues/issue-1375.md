---
title: System hangs after 5-10 minutes of XMRig 5.1.0 working
source_url: https://github.com/xmrig/xmrig/issues/1375
author: barmaley997
assignees: []
labels:
- bug
- stability
created_at: '2019-12-03T15:36:54+00:00'
updated_at: '2020-08-31T05:49:00+00:00'
type: issue
status: closed
closed_at: '2020-08-31T05:48:59+00:00'
---

# Original Description
Hello, till renewing mining algorithmg 30th November i have used v4.6.2-beta version of XMRig and all was OK, system was never hang due work of XMRig miner, and moreover - my system was never hangs before due work of XMRig miner by all previous version of XMRig and any others monero miners, but with your new version XMRig 5.1.0 it now always hang system after 5-10 minutes of working miner. So could it be fixed?
CPU - AMD Ryzen 7 1700, 8 Gb memory,   OS Windows 10 1607
I forgot to say - i use XMRig, and always used before, only for CPU mining, without GPU mining

# Discussion History
## FabioFrmg | 2019-12-03T15:46:42+00:00
Same issue here in most of my PCs. 
Waiting a new version. 

## monero101 | 2019-12-03T15:50:35+00:00
> Same issue here in most of my PCs.
> Waiting a new version.

Could you please confirm if the issue is gone with new version here or in your previous post ? And if you had to use [yield](https://github.com/xmrig/xmrig/issues/1365#issuecomment-560966738) option ?

## barmaley997 | 2019-12-03T16:18:50+00:00
> you had to use [yield](https://github.com/xmrig/xmrig/issues/1365#issuecomment-560966738) option ?

So - i need yeld option set to true or to false?

## monero101 | 2019-12-03T16:24:06+00:00
> > you had to use [yield](https://github.com/xmrig/xmrig/issues/1365#issuecomment-560966738) option ?
> 
> So - i need yeld option set to true or to false?

True, it will add some removed call.

## barmaley997 | 2019-12-03T17:00:25+00:00
> True

I`ve tried True but it seems was not help, system still hangs after small time of XMRig work
thats my config.json:

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
    "randomx": {
        "init": -1,
        "numa": true
    },
    "cpu": {
        "enabled": true,
        "huge-pages": true,
        "hw-aes": null,
		"priority": null,
        "memory-pool": false,
		"yield": true,
        "asm": true,
        "argon2-impl": null,
        "argon2": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
        "cn": [
            [1, 0],
            [1, 2],
            [1, 4],
            [1, 6],
            [1, 8],
            [1, 10],
            [1, 12],
            [1, 14]
        ],
        "cn-heavy": [
            [1, 0],
            [1, 2],
            [1, 8],
            [1, 10]
        ],
        "cn-lite": [
            [1, 0],
            [1, 1],
            [1, 2],
            [1, 3],
            [1, 4],
            [1, 5],
            [1, 6],
            [1, 7],
            [1, 8],
            [1, 9],
            [1, 10],
            [1, 11],
            [1, 12],
            [1, 13],
            [1, 14],
            [1, 15]
        ],
        "cn-pico": [
            [2, 0],
            [2, 1],
            [2, 2],
            [2, 3],
            [2, 4],
            [2, 5],
            [2, 6],
            [2, 7],
            [2, 8],
            [2, 9],
            [2, 10],
            [2, 11],
            [2, 12],
            [2, 13],
            [2, 14],
            [2, 15]
        ],
        "cn/gpu": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
        "rx": [0, 2, 4, 6, 8, 10, 12, 14],
        "rx/wow": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
        "cn/0": false,
        "cn-lite/0": false,
        "rx/arq": "rx/wow"
    },
    "opencl": {
        "enabled": false,
        "cache": true,
        "loader": null,
        "platform": "AMD",
        "cn/0": false,
        "cn-lite/0": false
    },
    "cuda": {
        "enabled": false,
        "loader": null,
        "nvml": true,
        "cn/0": false,
        "cn-lite/0": false
    },
    "donate-level": 1,
    "donate-over-proxy": 1,
    "log-file": null,
    "pools": [
        {
            "algo": null,
            "coin": null,
            "url": "pool.hashvault.pro:443",
            "user": "Mywallet",
            "pass": "Mypass",
            "rig-id": null,
            "nicehash": false,
            "keepalive": false,
            "enabled": true,
            "tls": true,
            "tls-fingerprint": null,
            "daemon": false,
            "self-select": null
        }
    ],
    "print-time": 60,
    "health-print-time": 60,
    "retries": 5,
    "retry-pause": 5,
    "syslog": false,
    "user-agent": null,
    "watch": true
}


## barmaley997 | 2019-12-03T17:02:05+00:00
and these strings:

"argon2": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
"cn": [
[1, 0],
[1, 2],
[1, 4],
[1, 6],
[1, 8],
[1, 10],
[1, 12],
[1, 14]
],
"cn-heavy": [
[1, 0],
[1, 2],
[1, 8],
[1, 10]
],
"cn-lite": [
[1, 0],
[1, 1],
[1, 2],
[1, 3],
[1, 4],
[1, 5],
[1, 6],
[1, 7],
[1, 8],
[1, 9],
[1, 10],
[1, 11],
[1, 12],
[1, 13],
[1, 14],
[1, 15]
],
"cn-pico": [
[2, 0],
[2, 1],
[2, 2],
[2, 3],
[2, 4],
[2, 5],
[2, 6],
[2, 7],
[2, 8],
[2, 9],
[2, 10],
[2, 11],
[2, 12],
[2, 13],
[2, 14],
[2, 15]
],
"cn/gpu": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
"rx": [0, 2, 4, 6, 8, 10, 12, 14],
"rx/wow": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],

Miner added by itself, is it right?

## monero101 | 2019-12-03T17:05:13+00:00
did you used the dev branch ? this option has no use i think in current pre-compiled versions.
btw, use pastebin to share configs.

## barmaley997 | 2019-12-03T18:28:08+00:00
> did you used the dev branch ? this option has no use i think in current pre-compiled versions.

I've not compiled frome sources, I've took precompiled binaries  - https://github.com/xmrig/xmrig/releases/download/v5.1.0/xmrig-5.1.0-gcc-win64.zip   and   https://github.com/xmrig/xmrig/releases/download/v5.1.0/xmrig-5.1.0-msvc-win64.zip
So i've changed config.json to as in sources  - https://github.com/xmrig/xmrig/blob/dev/src/config.json
and set "yeld" : true  - and it was not helped - system hangs again, and besides that the miner again added strings that i've posted above
`

`

## 2010phenix | 2019-12-03T20:29:51+00:00
@barmaley997 
"huge-pages": false,
try turn off this one and check....

## FabioFrmg | 2019-12-04T00:09:09+00:00
> > Same issue here in most of my PCs.
> > Waiting a new version.
> 
> Could you please confirm if the issue is gone with new version here or in your previous post ? And if you had to use [yield](https://github.com/xmrig/xmrig/issues/1365#issuecomment-560966738) option ?

Not win with yeld too =( 

## monero101 | 2019-12-04T08:40:45+00:00
5.1.0 is not a dev branch, just wait for 5.1.1 - it will have it set by default or just go back to 5.0.1 for now.

## xmrig | 2019-12-04T10:41:14+00:00
v5.1.1 released https://github.com/xmrig/xmrig/releases/tag/v5.1.1 no changes in config file required, please confirm is this issue fixed or not.
Thank you.

## barmaley997 | 2019-12-04T17:23:39+00:00
> "huge-pages": false,
> try turn off this one and check....


I've tried that and it was not helped also, system still hangs also after small time of XMRig working ((((

## barmaley997 | 2019-12-04T17:25:16+00:00
> v5.1.1 released https://github.com/xmrig/xmrig/releases/tag/v5.1.1 no changes in config file required, please confirm is this issue fixed or not.
> Thank you.


OK, i'll try

## barmaley997 | 2019-12-05T07:49:43+00:00
> v5.1.1 released https://github.com/xmrig/xmrig/releases/tag/v5.1.1 no changes in config file required, please confirm is this issue fixed or not.

I've tried and problem still the same, issue wasn't fixed, but hashrate dropped at 2 times, like when huge page is disabled in previous 5.1.0 version  )))))

## aa-delite | 2019-12-05T12:45:47+00:00
try disabling opcache in BIOS if it exists.
try disabling GPU mining if using (maybe GPU hangs)
try using stress-test like prime95 and temperature monitoring. Maybe CPU hangs.

## BradT7 | 2019-12-12T20:36:41+00:00
Try disabling CPU Virtualization in BIOS if enabled, this recently helped resolve my issue with system hard locks. 

## barmaley997 | 2019-12-23T16:15:39+00:00
> 
> 
> v5.1.1 released https://github.com/xmrig/xmrig/releases/tag/v5.1.1 no changes in config file required, please confirm is this issue fixed or not.
> Thank you.

Hello, sorry for long time silence, so i tried all this advices above, i have disabled opcache, CPU Virtualisation, huge pages, set yield to true, but none of that helped me, GPU mining i not use, and none of new versions helped too, and even when new version  5.4.0  was released i tried it with all the advices above but again nothing was changed - system still was hanged after 5-10 minutes of mining, so i began to try every possibilities that i can:
I have MSI X370 GAMING PLUS motherboard, in UEFI-BIOS in CPU features section it has such
functions:

- Simultaneous Multithreading
- Core C6 State
- Opcache Control
- IOMMU
- Spread Spectrum
- Relaxed EDC throttling
- AMD Cool'n'Quiet
- SVM Mode

So at first i disabled all this options -  set all of them to Disabled
And after that i've loaded to my OS (Windows 10x64 1607)  and started XMRig and i was very wondered after hour of XMRig was worked fine and system was not hanged!
So i made next step - one by one i rebooted computer to UEFI-BIOS and enabled one of these options, in CPU features, and after that booted to OS and watch how XMRig was working.
After such experiment i figured out that all troubles that i had with system hangs by XMRig was in the first two options - Simultaneous Multithreading and Core C6 State - when its was enabled  OS always hangs during XMRig work, not matter other options is enabled or disabled and no matter which settings of XMRig is set - yield and huge pages or other, but if Simultaneous Multithreading and Core C6 State was sets to Disable  XMRig is always works stable and system is not hangs, no matter which other option enabled or disabled or which XMRig settings is set, so i sets Simultaneous Multithreading and Core C6 State to Disable other option to Enable (or Auto if available) and after that XMRig is working OK, but it is very strange - before mining algorithm was updated on 1 december all options in CPU features section of UEFI-BIOS was set to enable and system was never hanged by any of monero miners.
Could you be so please to investigate this cause - why XMRig begins to crash by Simultaneous Multithreading and Core C6 State enabled to fix that so i could enable them in the future? Cause i use my mighty AMD Ryzen not only for monero mining but for many other purposes and i don't want to loose any piece of its power


## BradT7 | 2019-12-24T16:54:50+00:00
Does your Disk go to 100% in Task Manager when your system freezes up? You'll have to have it open beforehand obviously to see, but that is what's happening to me when my system hard locks, I can only move around the mouse and windows that are already opened. I'm only stable on 5.0.1 with reduced threads (6 out of 12). I just posted a new detailed thread about my current issues with v5.x including 5.4 too. 

## xmrig | 2020-08-31T05:48:59+00:00
https://xmrig.com/docs/miner/randomx-stability-troubleshooting-guide

# Action History
- Created by: barmaley997 | 2019-12-03T15:36:54+00:00
- Closed at: 2020-08-31T05:48:59+00:00
