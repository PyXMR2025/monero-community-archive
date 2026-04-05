---
title: Issue with using Cuda plugin?
source_url: https://github.com/xmrig/xmrig/issues/3533
author: ComradeOldMajor
assignees: []
labels: []
created_at: '2024-08-15T14:42:14+00:00'
updated_at: '2025-06-16T19:51:18+00:00'
type: issue
status: closed
closed_at: '2025-06-16T19:51:18+00:00'
---

# Original Description
Hello, I have been converting my XMRig to mine Raven-coin with, say as you want this is the platform I would like to use.
 I keep running into an issue with it attempting to open up the files directory for the Cuda Loader.
 I've tried multiple different file locations and I cannot figure it out. 
If it helps anyone, my entirety of XMRIG files are saved onto a flash-drive.
 Here are images showing my problems as well as my code:

![Screenshot 2024-08-15 103147](https://github.com/user-attachments/assets/674a2b12-36b0-4505-8f85-593f49ea3bfb)


Here is my code:

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
        "max-threads-hint": 100,
        "asm": true,
        "argon2-impl": null
    },
    "opencl": {
        "enabled": true,
        "cache": true,
        "loader": null,
        "platform": "INTEL",
        "adl": true,
        "cn": [
            {
                "index": 0,
                "intensity": 256,
                "worksize": 8,
                "strided_index": [0, 2],
                "threads": [1],
                "unroll": 8
            }
        ],
        "cn-heavy": [
            {
                "index": 0,
                "intensity": 256,
                "worksize": 8,
                "strided_index": [0, 2],
                "threads": [-1],
                "unroll": 8
            }
        ],
        "cn-lite": [
            {
                "index": 0,
                "intensity": 512,
                "worksize": 8,
                "strided_index": [0, 2],
                "threads": [-1],
                "unroll": 8
            }
        ],
        "cn-pico": [
            {
                "index": 0,
                "intensity": 512,
                "worksize": 8,
                "strided_index": [0, 2],
                "threads": [-1],
                "unroll": 8
            }
        ],
        "cn/2": [
            {
                "index": 0,
                "intensity": 256,
                "worksize": 8,
                "strided_index": [0, 2],
                "threads": [-1],
                "unroll": 8
            }
        ],
        "cn/upx2": [
            {
                "index": 0,
                "intensity": 512,
                "worksize": 8,
                "strided_index": [0, 2],
                "threads": [-1],
                "unroll": 8
            }
        ],
        "kawpow": [
            {
                "index": 0,
                "intensity": 8388608,
                "worksize": 256,
                "threads": [1],
                "unroll": 1
            }
        ],
        "rx": [
            {
                "index": 0,
                "intensity": 192,
                "worksize": 8,
                "threads": [-1],
                "bfactor": 6,
                "gcn_asm": false,
                "dataset_host": false
            }
        ],
        "rx/arq": [
            {
                "index": 0,
                "intensity": 512,
                "worksize": 8,
                "threads": [-1],
                "bfactor": 6,
                "gcn_asm": false,
                "dataset_host": false
            }
        ],
        "rx/wow": [
            {
                "index": 0,
                "intensity": 448,
                "worksize": 8,
                "threads": [-1],
                "bfactor": 6,
                "gcn_asm": false,
                "dataset_host": false
            }
        ],
        "cn-lite/0": false,
        "cn/0": false
    },
    "cuda": {
        "enabled": true,
        "loader": "E:\Directory\xmrig\config.json",
        "nvml": true
    },
    "log-file": null,
    "donate-level": 1,
    "donate-over-proxy": 0,
    "pools": [
        {
            "algo": "kawpow",
            "coin": "RVN",
            "url": "rvn-us-east1.nanopool.org:10400",
            "user": "Trying to steal from OldMajor are we?",
            "pass": "x",
            "rig-id": null,
            "nicehash": false,
            "keepalive": true,
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

As you may read I have also been messing with OpenCL, which can work but has a problem allocating the threads.
Any advice on that would be good too but I am not too worried about OpenCL

![Screenshot 2024-08-15 101803](https://github.com/user-attachments/assets/27a15189-b6db-428a-b14d-06299dda0c0c)




# Discussion History
## SChernykh | 2024-08-15T19:54:44+00:00
```
"cuda": {
        "enabled": true,
        "loader": "E:\Directory\xmrig\config.json",
        "nvml": true
    },
```
It's wrong, it must be a path to CUDA plugin: https://github.com/xmrig/xmrig-cuda?tab=readme-ov-file#advanced and it must use `/` in the path, not `\`

## ComradeOldMajor | 2024-08-16T00:48:32+00:00
> ```
> "cuda": {
>         "enabled": true,
>         "loader": "E:\Directory\xmrig\config.json",
>         "nvml": true
>     },
> ```
> 
> It's wrong, it must be a path to CUDA plugin: https://github.com/xmrig/xmrig-cuda?tab=readme-ov-file#advanced and it must use `/` in the path, not `\`

I have been able to fix the paths to the .dll for cuda and the back slashes,
 but I seem to be getting an error still >:(

![image_2024-08-15_210939162](https://github.com/user-attachments/assets/1465a8aa-f1db-4f1c-a7b7-01e8eb263fc8)

I am honestly completely lost now 
```
`{
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
        "max-threads-hint": 100,
        "asm": true,
        "argon2-impl": null
    },
    "opencl": {
        "enabled": false,
        "cache": true,
        "loader": null,
        "platform": "INTEL",
        "adl": true,
        "cn": [
            {
                "index": 0,
                "intensity": 256,
                "worksize": 8,
                "strided_index": [0, 2],
                "threads": [1],
                "unroll": 8
            }
        ],
        "cn-heavy": [
            {
                "index": 0,
                "intensity": 256,
                "worksize": 8,
                "strided_index": [0, 2],
                "threads": [-1],
                "unroll": 8
            }
        ],
        "cn-lite": [
            {
                "index": 0,
                "intensity": 512,
                "worksize": 8,
                "strided_index": [0, 2],
                "threads": [-1],
                "unroll": 8
            }
        ],
        "cn-pico": [
            {
                "index": 0,
                "intensity": 512,
                "worksize": 8,
                "strided_index": [0, 2],
                "threads": [-1],
                "unroll": 8
            }
        ],
        "cn/2": [
            {
                "index": 0,
                "intensity": 256,
                "worksize": 8,
                "strided_index": [0, 2],
                "threads": [-1],
                "unroll": 8
            }
        ],
        "cn/upx2": [
            {
                "index": 0,
                "intensity": 512,
                "worksize": 8,
                "strided_index": [0, 2],
                "threads": [-1],
                "unroll": 8
            }
        ],
        "kawpow": [
            {
                "index": 0,
                "intensity": 256,
                "worksize": 256,
                "threads": [-1],
                "unroll": 1
            }
        ],
        "rx": [
            {
                "index": 0,
                "intensity": 192,
                "worksize": 8,
                "threads": [-1],
                "bfactor": 8,
                "gcn_asm": false,
                "dataset_host": false
            }
        ],
        "rx/arq": [
            {
                "index": 0,
                "intensity": 512,
                "worksize": 8,
                "threads": [-1],
                "bfactor": 6,
                "gcn_asm": false,
                "dataset_host": false
            }
        ],
        "rx/wow": [
            {
                "index": 0,
                "intensity": 448,
                "worksize": 8,
                "threads": [-1],
                "bfactor": 6,
                "gcn_asm": false,
                "dataset_host": false
            }
        ],
        "cn-lite/0": false,
        "cn/0": false
    },
    "cuda": {
        "enabled": true,
        "loader": "E:/Directory/xmrig/xmrig-cuda.dll",
        "nvml": true 
    },
    "log-file": null,
    "donate-level": 0,
    "donate-over-proxy": 0,
    "pools": [
        {
            "algo": "kawpow",
            "coin": "RVN",
            "url": "rvn-us-east1.nanopool.org:10400",
            "user": "Changed the wallet after the edit, smh slipped up",
            "pass": "x",
            "rig-id": null,
            "nicehash": false,
            "keepalive": true,
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
`
```

## SChernykh | 2024-08-16T21:44:25+00:00
You have the wrong path to `xmrig-cuda.dll`, XMRig tells you this upon startup ("The specified module could not be found" error).

# Action History
- Created by: ComradeOldMajor | 2024-08-15T14:42:14+00:00
- Closed at: 2025-06-16T19:51:18+00:00
