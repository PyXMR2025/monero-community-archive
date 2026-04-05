---
title: Dual CPU Xeon E5630 mines on 8 cores only
source_url: https://github.com/xmrig/xmrig/issues/2148
author: hdwitch
assignees: []
labels:
- question
created_at: '2021-03-01T21:55:27+00:00'
updated_at: '2021-03-03T10:25:31+00:00'
type: issue
status: closed
closed_at: '2021-03-03T10:25:31+00:00'
---

# Original Description
Hi, 

I run xmrrig on a Linux (Deb10) machine with dual Xeon E5630 CPU (16 cores together). However i see only 8 threads running, the hashrate is around ~2100H/s and in htop is see the other CPU idling. What should i change to make xmrig use the 2nd CPU ? Thanks !

![Screenshot_2021-03-01_22-51-10](https://user-images.githubusercontent.com/79876604/109564310-2dd38800-7ae1-11eb-9bb2-66e743bd3237.png)

![Screenshot_2021-03-01_22-53-15](https://user-images.githubusercontent.com/79876604/109564322-3330d280-7ae1-11eb-85f7-477bd508d667.png)


# Discussion History
## SChernykh | 2021-03-01T22:42:49+00:00
It is using both CPUs. You're limited by L2 cache per CPU core, so adding more threads will not increase hashrate. You can try to edit config.json manually and check yourself - find `"rx": [0, 1, 2, 3, 4, 5, 6, 7],` and add threads there.

## hdwitch | 2021-03-02T13:00:27+00:00
Thanks for replying. I think I got confused by /proc/cpuinfo output which shows 16 logical cores (2xCPU x4 Physical Cores x2 Threads).

So if I understand it correctly I have 24MB L2 memory for 16 logical cores. Shouldn't xmrig run on 12 cores if it needs 2MB L2 memory per core ? 

When I run xmrig as is, i get a hashrate around 2100H/s. When I add "threads": 20, to the xmrig.json file i get a higher hashrate: 

`speed 10s/60s/15m 2418.6 2401.6 2401.4 H/s max 2442.6 H/s
`
However this value doesnt make any sense to me, why is "Threads":  20 working better as compared to when I change the "rx" and add threads there ? 

I still see the second CPU idling (cores 0-7 are 100%, cores 8-15 are having no load) in default setting. When i add "Threads": 20, i see one additional core from the second CPU have an occasional load..

Can you advise me on the best setting to utilize max CPU power ? 

## xmrig | 2021-03-02T13:35:56+00:00
1. You are limited by L2 cache, unlike previous algorithms RandomX also requires 256 KB of L2 cache.
2. `"threads": 20,` is not a valid config option and ignored, you must edit the `rx` array.
3. Use command `lscpu` to view relations between cores and sockets. You will see that the miner uses both CPUs.
4. Occasional load happens due to other tasks running, you must run the miner on an idle system to get high and stable results.


## hdwitch | 2021-03-02T13:55:11+00:00
1. Thanks a lot for the answer. I now see that 2048KB L2 Cache / 256 = 8.

2. If I remove "threads": 20 from my config, the hashrate falls to ~2100H/s, when i add it it raises up to ~2400H/s. Do you have any idea why ? See my config below.

```json
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
    "threads": 20,
    "randomx": {
        "init": -1,
        "init-avx2": -1,
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
        "memory-pool": false,
        "yield": true,
        "asm": true,
        "argon2-impl": null,
        "astrobwt-max-size": 550,
        "astrobwt-avx2": false,
        "argon2": [0, 8, 1, 9, 2, 10, 3, 11, 4, 12, 5, 13, 6, 14, 7, 15],
        "astrobwt": [0, 8, 1, 9, 2, 10, 3, 11, 4, 12, 5, 13, 6, 14, 7, 15],
        "cn": [
            [1, 0],
            [1, 1],
            [1, 2],
            [1, 3],
            [1, 10],
            [1, 11],
            [1, 4],
            [1, 5],
            [1, 6],
            [1, 7],
            [1, 14],
            [1, 15]
        ],
        "cn-heavy": [
            [1, 0],
            [1, 1],
            [1, 2],
            [1, 4],
            [1, 5],
            [1, 6]
        ],
        "cn-lite": [
            [1, 0],
            [1, 8],
            [1, 1],
            [1, 9],
            [1, 2],
            [1, 10],
            [1, 3],
            [1, 11],
            [1, 4],
            [1, 12],
            [1, 5],
            [1, 13],
            [1, 6],
            [1, 14],
            [1, 7],
            [1, 15]
        ],
        "cn-pico": [
            [2, 0],
            [2, 8],
            [2, 1],
            [2, 9],
            [2, 2],
            [2, 10],
            [2, 3],
            [2, 11],
            [2, 4],
            [2, 12],
            [2, 5],
            [2, 13],
            [2, 6],
            [2, 14],
            [2, 7],
            [2, 15]
        ],
        "rx": [0, 1, 2, 3, 4, 5, 6, 7],
        "rx/wow": [0, 8, 1, 9, 2, 10, 3, 11, 4, 12, 5, 13, 6, 14, 7, 15],
        "cn/0": false,
        "cn-lite/0": false,
        "rx/arq": "rx/wow",
        "rx/keva": "rx/wow"
    },
    "opencl": {
        "enabled": false,
        "cache": true,
        "loader": null,
        "platform": "AMD",
        "adl": true
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
            "algo": null,
            "coin": "monero",
            "url": "xmrpool.eu:9999",
            "user": "[redacted]",
            "pass": "x",
            "rig-id": "[redacted]",
            "nicehash": false,
            "keepalive": true,
            "enabled": true,
            "tls": true,
            "tls-fingerprint": null,
            "daemon": false,
            "socks5": null,
            "self-select": null,
            "submit-to-origin": false
        }
    ],
    "retries": 1,
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
    "user-agent": null,
    "verbose": 0,
    "watch": true,
    "pause-on-battery": false,
    "pause-on-active": false
}

## xmrig | 2021-03-02T14:08:30+00:00
Please show full miner log for both cases with pressed `h` at the end to view hashrate.
Thank you.


## hdwitch | 2021-03-02T14:28:10+00:00
After I removed "threads": 20 the hashrate didnt change. I'm sorry for the confusion, and all the questions. This issue can be closed. Thanks a lot !

# Action History
- Created by: hdwitch | 2021-03-01T21:55:27+00:00
- Closed at: 2021-03-03T10:25:31+00:00
