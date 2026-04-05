---
title: How work it
source_url: https://github.com/xmrig/xmrig/issues/3502
author: Mohammad-Abbasi2559
assignees: []
labels: []
created_at: '2024-06-27T11:38:37+00:00'
updated_at: '2025-06-18T22:11:25+00:00'
type: issue
status: closed
closed_at: '2025-06-18T22:11:25+00:00'
---

# Original Description
Hello
How to **view mined amount**
and **transfer it**
Thank you

# Discussion History
## im10furry | 2024-08-01T06:07:48+00:00
You can used c3pool
The web is :c3pool.org

## randommamm | 2024-08-27T15:09:24+00:00
Hi, 

I know it maybe a stupid question. I run the script and I updated my wallet address in the config. It is running on my GPU from the morning. When I go to the website c3pool.org and add my wallet address it shows 0. 

I am new to this world of mining, can you let me know what is the issue? or what to expect?
One more question, Is the GPU is getting the max memory and core?
## Example of the logs

```sh
 nvidia   #0 01:00.0  14W 47C 139/405 MHz fan0:0%
 nvidia   #0 01:00.0  14W 47C 139/405 MHz fan0:0%
 nvidia   #0 01:00.0  14W 47C 139/405 MHz fan0:0%
 nvidia   #0 01:00.0  13W 47C 139/405 MHz fan0:0%
 nvidia   #0 01:00.0  17W 47C 139/405 MHz fan0:0%
 nvidia   #0 01:00.0  13W 47C 139/405 MHz fan0:0%
 nvidia   #0 01:00.0  19W 47C 139/405 MHz fan0:0%
 nvidia   #0 01:00.0  13W 46C 139/405 MHz fan0:0%
 nvidia   #0 01:00.0  14W 47C 139/405 MHz fan0:0%
 nvidia   #0 01:00.0  64W 51C 1569/5005 MHz fan0:0%
 nvidia   #0 01:00.0  15W 48C 139/405 MHz fan0:0%
 nvidia   #0 01:00.0  15W 49C 139/405 MHz fan0:0%
 nvidia   #0 01:00.0  16W 48C 151/405 MHz fan0:0%
 nvidia   #0 01:00.0  15W 48C 139/405 MHz fan0:0%
 nvidia   #0 01:00.0  15W 48C 139/405 MHz fan0:0%
```
## Config.json
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
        "enabled": false,
        "huge-pages": true,
        "huge-pages-jit": false,
        "hw-aes": null,
        "priority": null,
        "memory-pool": false,
        "yield": true,
        "asm": true,
        "argon2-impl": null,
        "argon2": [0, 1, 2, 3, 4, 5, 6, 7],
        "cn": [
            [1, 0],
            [1, 1],
            [1, 2],
            [1, 3],
            [1, 4],
            [1, 5],
            [1, 6],
            [1, 7]
        ],
        "cn-heavy": [
            [1, 0],
            [1, 1],
            [1, 2],
            [1, 3],
            [1, 4],
            [1, 5],
            [1, 6],
            [1, 7]
        ],
        "cn-lite": [
            [1, 0],
            [1, 1],
            [1, 2],
            [1, 3],
            [1, 4],
            [1, 5],
            [1, 6],
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
            [8, 1],
            [8, 2],
            [8, 3],
            [8, 4],
            [8, 5],
            [8, 6],
            [8, 7]
        ],
        "rx": [0, 1, 2, 3, 4, 5, 6, 7],
        "rx/wow": [0, 1, 2, 3, 4, 5, 6, 7],
        "cn-lite/0": false,
        "cn/0": false,
        "rx/arq": "rx/wow"
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
        "enabled": true,
        "loader": "C:/Users/MY_USER/Downloads/xmrig-6.22.0-msvc-win64/xmrig-cuda.dll",
        "nvml": true
    },
    "log-file": null,
    "donate-level": 1,
    "donate-over-proxy": 1,
    "pools": [
        {
            "algo": null,
            "coin": "monero",
            "url": "donate.v2.xmrig.com:3333",
            "user": "MY_MONERO_WALLET_ADDRESS",
            "pass": "x",
            "rig-id": null,
            "nicehash": false,
            "keepalive": false,
            "enabled": true,
            "tls": false,
            "sni": false,
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
```

## SChernykh | 2024-08-27T15:58:04+00:00
You forgot to change pool url in the config.

## randommamm | 2024-08-27T16:32:45+00:00
Thanks, what should be the pool url? I don’t know how to set it or change it. Is there any difference?

# Action History
- Created by: Mohammad-Abbasi2559 | 2024-06-27T11:38:37+00:00
- Closed at: 2025-06-18T22:11:25+00:00
