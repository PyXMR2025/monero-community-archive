---
title: Can i change my diff and the algo?
source_url: https://github.com/xmrig/xmrig/issues/2960
author: Noeleth
assignees: []
labels: []
created_at: '2022-03-09T15:18:41+00:00'
updated_at: '2025-06-20T11:06:38+00:00'
type: issue
status: closed
closed_at: '2025-06-20T11:06:38+00:00'
---

# Original Description
hi, is posible change the diff? manually i think i cant. i just mining or starting mining monero xmr, i dont know is for the pool of unmineable or what.
is posible to change the algorithm? or is auto? changing the pool? i dnt know if the pool gave me this diff, or is the algorithm.

this is my json:

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
        "huge-pages-jit": true,
        "hw-aes": null,
        "priority": 5,
        "memory-pool": false,
        "yield": true,
        "asm": true,
        "argon2-impl": null,
        "astrobwt-max-size": 1000,
        "astrobwt-avx2": false,
        "argon2": [0, 2, 4, 6, 5, 7],
        "astrobwt": [0, 1, 2, 3, 4, 5, 6, 7],
        "cn": [
            [1, 0],
            [1, 2],
            [1, 4]
        ],
        "cn-heavy": [
            [1, 0],
            [1, 2]
        ],
        "cn-lite": [
            [1, 0],
            [1, 2],
            [1, 4],
            [1, 6],
            [1, 5],
            [1, 7]
        ],
        "cn-pico": [
            [2, 0],
            [2, 1],
            [2, 2],
            [2, 3],
            [2, 4],
            [2, 5],
            [2, 6],
            [2, 7]
        ],
        "cn/upx2": [
            [2, 0],
            [2, 1],
            [2, 2],
            [2, 3],
            [2, 4],
            [2, 5],
            [2, 6],
            [2, 7]
        ],
        "ghostrider": [
            [8, 0],
            [8, 2],
            [8, 4]
        ],
        "rx": [0, 2, 4],
        "rx/arq": [0, 1, 2, 3, 4, 5, 6, 7],
        "rx/wow": [0, 2, 4, 6, 5, 7],
        "cn-lite/0": false,
        "cn/0": false,
        "rx/keva": "rx/wow"
    },
    "opencl": {
        "enabled": false,
        "cache": true,
        "loader": null,
        "platform": "AMD",
        "adl": true,
        "cn-lite/0": false,
        "cn/0": false
    },
    "cuda": {
        "enabled": false,
        "loader": null,
        "nvml": true,
        "astrobwt": [
            {
                "index": 0,
                "threads": 32,
                "blocks": 5,
                "bfactor": 8,
                "bsleep": 25,
                "affinity": -1
            }
        ],
        "cn": [
            {
                "index": 0,
                "threads": 44,
                "blocks": 15,
                "bfactor": 8,
                "bsleep": 25,
                "affinity": -1
            }
        ],
        "cn-heavy": [
            {
                "index": 0,
                "threads": 22,
                "blocks": 15,
                "bfactor": 8,
                "bsleep": 25,
                "affinity": -1
            }
        ],
        "cn-lite": [
            {
                "index": 0,
                "threads": 88,
                "blocks": 15,
                "bfactor": 8,
                "bsleep": 25,
                "affinity": -1
            }
        ],
        "cn-pico": [
            {
                "index": 0,
                "threads": 4,
                "blocks": 40,
                "bfactor": 8,
                "bsleep": 25,
                "affinity": -1
            }
        ],
        "cn/2": [
            {
                "index": 0,
                "threads": 4,
                "blocks": 40,
                "bfactor": 8,
                "bsleep": 25,
                "affinity": -1
            }
        ],
        "cn/upx2": [
            {
                "index": 0,
                "threads": 4,
                "blocks": 40,
                "bfactor": 8,
                "bsleep": 25,
                "affinity": -1
            }
        ],
        "kawpow": [
            {
                "index": 0,
                "threads": 256,
                "blocks": 10240,
                "bfactor": 8,
                "bsleep": 25,
                "affinity": -1
            }
        ],
        "rx": [
            {
                "index": 0,
                "threads": 32,
                "blocks": 10,
                "bfactor": 8,
                "bsleep": 25,
                "affinity": -1,
                "dataset_host": false
            }
        ],
        "cn-lite/0": false,
        "cn/0": false
    },
    "log-file": null,
    "donate-level": 1,
    "donate-over-proxy": 1,
    "pools": [
        {
            "algo": null,
            "coin": null,
            "url": "rx.unmineable.com:3333",
            "user": "XMR:87DutJKDeuBNqbkqTKNQEf76V4SKsU1wP3njJhPSu9hC7UwwG7JqTZC6BR1j94SH7Rafp5WvvGZ7dihxfDRYGJUd6VuFDSt.NOEL",
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

And my lapt:
![Captura de pantalla (52)](https://user-images.githubusercontent.com/100553798/157470789-7ce3929d-984e-469d-ad12-7264a11c0ea9.png)

i dont know if i need a new json file.... help me please.

thnks for all your works.



# Discussion History
## Spudz76 | 2022-03-09T15:30:38+00:00
Other algos on Unmineable are on other endpoints.  `rx.unmineable.com` serves RandomX (rx/0) so that will always be that algo.

[For custom diff](https://twitter.com/un_mineable/status/1364788602627108866?s=20&t=FgAU52b3j3pVAlXT1RtnTw) you add `+54000` on the end of the `user` field, so
```
"user": "XMR:87DutJKDeuBNqbkqTKNQEf76V4SKsU1wP3njJhPSu9hC7UwwG7JqTZC6BR1j94SH7Rafp5WvvGZ7dihxfDRYGJUd6VuFDSt.NOEL+54000",
```

Because 1800 * 30 = 54000

## Noeleth | 2022-03-10T15:17:52+00:00
yes it canged to 54000, thanks, i have another dougth, in mi cuda nvidia i have 32 threads like you see in the pic, its posible the grafic card work more or this grafic is obsolet?

![Captura de pantalla (53)](https://user-images.githubusercontent.com/100553798/157692791-f468a815-5905-4ed3-bc0b-eee94aee4e86.png)
![Captura de pantalla (54)](https://user-images.githubusercontent.com/100553798/157692799-7ba40e13-a406-43a6-9434-aec06bc19693.png)


## Spudz76 | 2022-03-10T16:30:47+00:00
No that's about all you get from a GPU with RandomX, it's intentionally bad at it because it's a "CPU-only" algorithm.

So the 83H/s is costing hundreds of watts.

If you want XMR payment from GPU use MoneroOcean.  It will help your CPU earn more too since it's an Intel.

## Noeleth | 2022-03-11T07:52:59+00:00
Im going to try the moneroOcean pool and see what happen, so, i see in moneroOcean there are a guide to config a miner, but at the final of the article are another guide to reddit that say how to config the miner. Is a guide of 3yrs old, i think somethings have changed. 

## Spudz76 | 2022-03-11T18:00:19+00:00
Standard setup is to get the MO fork of everything: [xmrig](https://github.com/MoneroOcean/xmrig/) and [xmrig-cuda](https://github.com/MoneroOcean/xmrig-cuda/)

Then setup one folder with just xmrig and set for cpu-only.  And then another folder with xmrig and xmrig-cuda and set for cuda-only.  Then run both at the same time.  Give them different rig names so they show up as separate devices in the dashboard. 
 This way they can choose different algorithms, because they are completely different talents at different algorithms and running both backends in the same xmrig locks algorithm to the same one (very not optimal).

First run of either will benchmark all algorithms.

# Action History
- Created by: Noeleth | 2022-03-09T15:18:41+00:00
- Closed at: 2025-06-20T11:06:38+00:00
