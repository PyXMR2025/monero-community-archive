---
title: Monero Mining how to limit CPU  thread usage?
source_url: https://github.com/xmrig/xmrig/issues/3027
author: Luk8-8
assignees: []
labels: []
created_at: '2022-04-17T09:34:59+00:00'
updated_at: '2025-06-20T11:05:29+00:00'
type: issue
status: closed
closed_at: '2025-06-20T11:05:29+00:00'
---

# Original Description
Hi, i need to limit CPU usage from 32 to 30 thread on my  Ryzen 5950X

it was straigh forward on .bat file, since i started using moneroocean i don't know where to put request in json file

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
        "init-avx2": 0,
        "mode": "auto",
        "1gb-pages": false,
        "rdmsr": true,
        "wrmsr": true,
        "cache_qos": false,
        "numa": true,
        "scratchpad_prefetch_mode": 1
    },
    "cpu": {
        "enabled": true,
        "huge-pages": true,
        "huge-pages-jit": false,
        "hw-aes": null,
        "priority": null,
        "memory-pool": true,
        "yield": true,
        "asm": true,
        "argon2-impl": null,
        "astrobwt-max-size": 550,
        "astrobwt-avx2": false,
        "argon2": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31],
        "astrobwt": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31],
        "cn": [
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
            [1, 15],
            [1, 16],
            [1, 17],
            [1, 18],
            [1, 19],
            [1, 20],
            [1, 21],
            [1, 22],
            [1, 23],
            [1, 24],
            [1, 25],
            [1, 26],
            [1, 27],
            [1, 28],
            [1, 29],
            [1, 30],
            [1, 31]
        ],
        "cn-heavy": [
            [1, 0],
            [1, 2],
            [1, 4],
            [1, 6],
            [1, 8],
            [1, 10],
            [1, 12],
            [1, 14],
            [1, 16],
            [1, 18],
            [1, 20],
            [1, 22],
            [1, 24],
            [1, 26],
            [1, 28],
            [1, 30]
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
            [1, 15],
            [1, 16],
            [1, 17],
            [1, 18],
            [1, 19],
            [1, 20],
            [1, 21],
            [1, 22],
            [1, 23],
            [1, 24],
            [1, 25],
            [1, 26],
            [1, 27],
            [1, 28],
            [1, 29],
            [1, 30],
            [1, 31]
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
            [2, 15],
            [2, 16],
            [2, 17],
            [2, 18],
            [2, 19],
            [2, 20],
            [2, 21],
            [2, 22],
            [2, 23],
            [2, 24],
            [2, 25],
            [2, 26],
            [2, 27],
            [2, 28],
            [2, 29],
            [2, 30],
            [2, 31]
        ],
        "cn/2": [
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
            [1, 15],
            [1, 16],
            [1, 17],
            [1, 18],
            [1, 19],
            [1, 20],
            [1, 21],
            [1, 22],
            [1, 23],
            [1, 24],
            [1, 25],
            [1, 26],
            [1, 27],
            [1, 28],
            [1, 29],
            [1, 30],
            [1, 31]
        ],
        "cn/gpu": [
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
            [1, 15],
            [1, 16],
            [1, 17],
            [1, 18],
            [1, 19],
            [1, 20],
            [1, 21],
            [1, 22],
            [1, 23],
            [1, 24],
            [1, 25],
            [1, 26],
            [1, 27],
            [1, 28],
            [1, 29],
            [1, 30],
            [1, 31]
        ],
        "cn/upx2": [
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
            [2, 15],
            [2, 16],
            [2, 17],
            [2, 18],
            [2, 19],
            [2, 20],
            [2, 21],
            [2, 22],
            [2, 23],
            [2, 24],
            [2, 25],
            [2, 26],
            [2, 27],
            [2, 28],
            [2, 29],
            [2, 30],
            [2, 31]
        ],
        "ghostrider": [
            [8, 0],
            [8, 2],
            [8, 4],
            [8, 6],
            [8, 8],
            [8, 10],
            [8, 12],
            [8, 14],
            [8, 16],
            [8, 18],
            [8, 20],
            [8, 22],
            [8, 24],
            [8, 26],
            [8, 28],
            [8, 30]
        ],
        "panthera": [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],
        "rx": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31],
        "rx/wow": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31],
        "cn-lite/0": false,
        "cn/0": false,
        "rx/arq": "rx/wow",
        "rx/keva": "rx/wow"
    },
    "opencl": {
        "enabled": false,
        "cache": true,
        "loader": null,
        "platform": "AMD",
        "adl": true,
        "cn-lite/0": false,
        "cn/0": false,
        "panthera": false
    },
    "cuda": {
        "enabled": false,
        "loader": null,
        "nvml": true,
        "astrobwt": false,
        "cn-lite/0": false,
        "cn/0": false,
        "panthera": false
    },
    "log-file": null,
    "donate-level": 0,
    "donate-over-proxy": 0,
    "pools": [
        {
            "algo": null,
            "coin": null,
            "url": "gulf.moneroocean.stream:10128",
            "user": "431pA8dDk6nR8E6G78JSchLZMj4vUTdJLENtErbBSBhzSZ7k5WoHH5iQLAPHuyPSUuV42cxo4hVizZLxu7hbTAtcHB34RH1.Luk3090",
            "pass": "x",
            "rig-id": null,
            "nicehash": false,
            "keepalive": true,
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
    "rebench-algo": false,
    "bench-algo-time": 20,
    "algo-min-time": 0,
    "algo-perf": {
        "cn/0": 1721.3719445056156,
        "cn/1": 1457.142857142857,
        "cn/2": 1457.142857142857,
        "cn/r": 1457.142857142857,
        "cn/fast": 2914.285714285714,
        "cn/half": 2914.285714285714,
        "cn/xao": 1457.142857142857,
        "cn/rto": 1457.142857142857,
        "cn/rwz": 1942.8571428571427,
        "cn/zls": 1942.8571428571427,
        "cn/double": 728.5714285714286,
        "cn/ccx": 3442.743889011231,
        "cn-lite/0": 4046.0628695922815,
        "cn-lite/1": 4046.0628695922815,
        "cn-heavy/xhv": 1003.9543057996485,
        "cn-pico": 27562.17126025668,
        "cn-pico/tlo": 27562.17126025668,
        "cn/gpu": 312.28920741989884,
        "rx/0": 11348.626749447543,
        "rx/arq": 51912.10526315789,
        "rx/graft": 11054.936974789916,
        "rx/sfx": 11348.626749447543,
        "panthera": 12535.838332807072,
        "argon2/chukwav2": 25294.854256550563,
        "astrobwt": 1143.1366155852625,
        "ghostrider": 2823.9631336405528
    },
    "pause-on-battery": false,
    "pause-on-active": false
}



# Discussion History
## NVMDSTEVil | 2022-04-17T10:20:56+00:00
Your config.json may have deleted the value "max-threads-hint": due to using a bat/cmd file.  This is a "bug" with XMRIG.  It usually exists in the CPU options between yield and asm. If you change the percentage from 100 to 94 it should remove 2 threads, though since Monero Ocean is a profit switching pool i'm not sure it will affect all algorithms used.

    "cpu": {
        "enabled": true,
        "huge-pages": true,
        "huge-pages-jit": true,
        "hw-aes": null,
        "priority": null,
        "memory-pool": true,
        "yield": false,
        "max-threads-hint": 100,
        "asm": true,
        "argon2-impl": null,
        "astrobwt-max-size": 550,
        "astrobwt-avx2": false,
        "cn/0": false,
        "cn-lite/0": false
    },

## Spudz76 | 2022-04-17T15:16:47+00:00
In the CPU section of config.json, remove all thread definitions, save.

Run once with `--cpu-max-threads-hint=93` and then note the resulting config.json has definitions in it again, but less threads.  This will cap all available algorithms to 30 threads max.  94 would use 31 because it always rounds upward.

The threads hint does not do anything once there are existing thread definitions, so to make it operable again you must remove the definitions so that it triggers auto-sizing again (with the hint set).

## Spudz76 | 2022-04-17T15:18:09+00:00
And then for most accurate heatseeking, clear the algo-perf section and re-run the benchmarks on the new limited thread profiles.

## NVMDSTEVil | 2022-04-17T19:41:30+00:00
> In the CPU section of config.json, remove all thread definitions, save.
> 
> Run once with `--cpu-max-threads-hint=93` and then note the resulting config.json has definitions in it again, but less threads. This will cap all available algorithms to 30 threads max. 94 would use 31 because it always rounds upward.
> 
> The threads hint does not do anything once there are existing thread definitions, so to make it operable again you must remove the definitions so that it triggers auto-sizing again (with the hint set).

A lot of work instead of not deleting the value from the config.json file.

## Spudz76 | 2022-04-17T20:01:08+00:00
THAT. STILL. WOULD. NOT. HELP. (and is intended behavior)

## snipeTR | 2022-04-17T23:02:41+00:00
> THAT. STILL. WOULD. NOT. HELP. (and is intended behavior)

because: low intelligence, he satisfies himself by trying to prove himself to people he doesn't know :I

## NVMDSTEVil | 2022-04-18T00:35:30+00:00
> > THAT. STILL. WOULD. NOT. HELP. (and is intended behavior)
> 
> because: low intelligence, he satisfies himself by trying to prove himself to people he doesn't know :I

Keep up the attacks, really positive way to boost your image.

## Luk8-8 | 2022-04-18T08:34:36+00:00
Thank you for your reply in this matter
I did changed value "max-threads-hint": 100, to 94 and 90, but cpu is still load in 100%
Also on XMR start screen it shows there is 32 thread in use so this wont work for some reason

Where should i put this command ? --cpu-max-threads-hint=93

Thank you in advance



## Spudz76 | 2022-04-18T11:11:12+00:00
You must remove all existing profiles from the config.json

and then use that hint option the very next time you run xmrig, so that autoconfiguration of threads takes it into account while regenerating the deleted profiles.

If there are already profiles, then autoconfig doesn't run, and autoconfig is the only thing that reads the hint.

## christophediprima | 2023-01-04T09:36:30+00:00
Would it be possible to change that behavior?

I am not using the CLI but https://github.com/XMRig-for-Android/xmrig-for-android

And you need to provide a config.json you want to run. 

## Spudz76 | 2023-01-04T17:58:56+00:00
No, xmrig modifying existing profiles should never happen, in case you hand-designed your own.  So then you hand-remove the profiles to re-enable autoconfiguration.  Simple and won't nuke anything that you didn't nuke yourself with an editor.

## pazhosch | 2023-11-01T04:24:31+00:00
I use the "rx" parameter for that. Ryzen 5800 (8 physical cores: 0-1, 2-3,... 14-15), originally it was:

> "rx": [0, 2, 4, 6, 8, 10, 12, 14]

but I've changed it to: 

> "rx": [2, 4, 6, 8, 10, 12, 14]

System Monitor now shows that these and only these cores are 100% loaded, my hashrate is about the same as with 8 threads (decreases significantly with 6 threads), while I'm just happy to know I always have one free physical core for myself :-D Worked in Windows too

# Action History
- Created by: Luk8-8 | 2022-04-17T09:34:59+00:00
- Closed at: 2025-06-20T11:05:29+00:00
