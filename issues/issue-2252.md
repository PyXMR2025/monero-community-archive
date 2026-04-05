---
title: Using half Thread of AMD Ryzen Threadripper 1950X 16-Core Processor
source_url: https://github.com/xmrig/xmrig/issues/2252
author: ShahramHF
assignees: []
labels:
- question
created_at: '2021-04-09T20:53:53+00:00'
updated_at: '2021-04-12T13:27:59+00:00'
type: issue
status: closed
closed_at: '2021-04-12T13:27:59+00:00'
---

# Original Description
I have AMD Ryzen Threadripper 1950X 16-Core Processor and as you know it has 32 Thread.
xmrig only use half of them. my question is why?! 
Thank you

![image](https://user-images.githubusercontent.com/26859260/114239347-38642580-999b-11eb-9ccc-6f0ab8d7e60b.png)


This is my config file:

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
        "argon2": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31],
        "astrobwt": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31],
        "cn": [
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
        "cn-heavy": [
            [1, 0],
            [1, 2],
            [1, 8],
            [1, 10],
            [1, 16],
            [1, 18],
            [1, 24],
            [1, 26]
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
        "rx": [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],
        "rx/wow": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31],
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
            "coin": null,
            "url": "pool.supportxmr.com:443",
            "user": "My Wallet Address",
            "pass": "Shahramhf.001",
            "rig-id": null,
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

And this is what it done:

![image](https://user-images.githubusercontent.com/26859260/114240187-60a05400-999c-11eb-96f9-4c0e37cebdab.png)



# Discussion History
## SChernykh | 2021-04-09T22:44:50+00:00
2 MB L3 cache per thread is required for RandomX. Also you need to reboot to unlock huge pages and get higher hashrate.

## Spudz76 | 2021-04-10T01:01:55+00:00
So, 32MB cache / 2 = 16 threads doesn't matter you have more cores you have not enough cache for them.  To use all you would need cores * 2 or 64MB cache.

## Lonnegan | 2021-04-10T23:33:16+00:00
If you want to use all your compute resources, you have to use an algo which only takes 1 MB scratchpad per thread, e.g. Wownero.
https://translate.google.de/translate?u=www.planet3dnow.de%2Fcms%2F62151-kryptomining-mit-amd-prozessoren-ein-how-to-fuer-interessierte%2F&sl=de&tl=en&hl=ende&ie=UTF-8

# Action History
- Created by: ShahramHF | 2021-04-09T20:53:53+00:00
- Closed at: 2021-04-12T13:27:59+00:00
