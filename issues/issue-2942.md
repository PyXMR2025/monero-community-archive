---
title: Poor hashrate on AMD Threadripper 1950x 16 core
source_url: https://github.com/xmrig/xmrig/issues/2942
author: karanveersp
assignees: []
labels: []
created_at: '2022-02-21T19:33:57+00:00'
updated_at: '2025-06-20T11:06:50+00:00'
type: issue
status: closed
closed_at: '2025-06-20T11:06:50+00:00'
---

# Original Description
**Describe the bug**
I have two machines, one with a AMD Ryzen 5 and one with a Threadripper 1950x. The Ryzen 5 gets ~5k H/S while the Threadripper is hovering at ~1k H/S. I've set them both up using the same xmrig-v6.16.4-mo1-win64, with auto benchmark. 

**To Reproduce**
Following default instructions, for mining setup on both processors.

**Expected behavior**
I expected the threadripper to be a higher hashrate since its benchmarks on xmrig are closer to 10k H/S.

**Required data**
 
![image](https://user-images.githubusercontent.com/7011511/155016492-76c6bd73-7d85-43d0-8199-4e30efe8b3b3.png)

```
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
        "cn/2": [
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
        "rx": [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],
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
    "donate-over-proxy": 1,
    "pools": [
        {
            "algo": null,
            "coin": null,
            "url": "gulf.moneroocean.stream:10128",
            "user": "WALLET",
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
    "rebench-algo": true,
    "bench-algo-time": 20,
    "algo-min-time": 0,
    "algo-perf": {
        "cn/0": 1177.7253668763103,
        "cn/1": 1014.0486725663717,
        "cn/2": 1014.0486725663717,
        "cn/r": 1014.0486725663717,
        "cn/fast": 2028.0973451327434,
        "cn/half": 2028.0973451327434,
        "cn/xao": 1014.0486725663717,
        "cn/rto": 1014.0486725663717,
        "cn/rwz": 1352.0648967551622,
        "cn/zls": 1352.0648967551622,
        "cn/double": 507.02433628318585,
        "cn/ccx": 2355.4507337526206,
        "cn-lite/0": 2205.769827318788,
        "cn-lite/1": 2205.769827318788,
        "cn-heavy/xhv": 489.18555314084654,
        "cn-pico": 12870.461959381248,
        "cn-pico/tlo": 12870.461959381248,
        "cn/gpu": 105.97045547804677,
        "rx/0": 6945.747029755021,
        "rx/arq": 29007.78947368421,
        "rx/graft": 6386.920407948691,
        "rx/sfx": 6945.747029755021,
        "panthera": 7009.993688196928,
        "argon2/chukwav2": 5608.8692728036995,
        "astrobwt": 1052.199230529271,
        "ghostrider": 1862.4382207578253
    },
    "pause-on-battery": false,
    "pause-on-active": false
}
```
 - OS: Windows

# Discussion History
## Spudz76 | 2022-02-22T02:55:53+00:00
You're getting 6.945KH/s at rx/0 which is the only algorithm on benchmarks.

But apparently cn/r is currently worth more at its 1KH/s speed.

Hashrates do not compare across algorithms.

## Lonnegan | 2022-02-22T11:43:53+00:00
Additionally, this is the site of the original xmrig mining software. You are using the MoneroOcean fork with auto algo switching. So you should post issues here:
https://github.com/MoneroOcean/xmrig/releases

## karanveersp | 2022-02-22T13:18:06+00:00
Oh ok, thanks. I'll post the issue there. I saw that when I use the original xmrig application with the rx/0, the hashrate is 7300 which is much better.
 

## BigslimVdub | 2022-06-29T02:04:54+00:00
For best results on TR platforms use two instances of XMrig with each config calling 8 threads. Total threads will be 16 and with dual or quad-channel ram you will get 10-12kh with good ram and proper cooling. 

ex: 

``"rx": [16, 18, 20, 22, 24, 26, 28, 30],``
and
``"rx": [0, 2, 4, 6, 8, 10, 12, 14],``

also
``"1gb-pages": true,``

and run both as admin then reboot pc and run as admin again. Happy hashing

# Action History
- Created by: karanveersp | 2022-02-21T19:33:57+00:00
- Closed at: 2025-06-20T11:06:50+00:00
