---
title: Cuda version and opencl read error
source_url: https://github.com/xmrig/xmrig/issues/3233
author: MatejMagat305
assignees: []
labels: []
created_at: '2023-03-27T09:16:04+00:00'
updated_at: '2025-06-18T22:44:27+00:00'
type: issue
status: closed
closed_at: '2025-06-18T22:44:27+00:00'
---

# Original Description
**Describe the bug**
well I using xmring to mine on cpu and t-rex on graphic card, but I would like suport your project (1%), I was trying to build cuda plugin on linux that give me error at building: 
![Screenshot from 2023-03-27 10-32-32](https://user-images.githubusercontent.com/61238240/227889148-3fdfecb9-afca-43e1-b2ca-aa83ac882c26.png)
then I try openCL and that give me similer error like #2755

![Screenshot from 2023-03-27 11-03-57](https://user-images.githubusercontent.com/61238240/227897355-e0e211e1-8558-4b47-9c00-d490cc060f48.png)


**To Reproduce**
try compile with new nvcc

maybe try to run my config : 
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
        "scratchpad_prefetch_mode": 1
    },
    "cpu": {
        "enabled": false,
        "huge-pages": true,
        "huge-pages-jit": true,
        "hw-aes": null,
        "priority": null,
        "memory-pool": false,
        "yield": true,
        "asm": true,
        "argon2-impl": null,
        "cn-lite/0": false,
        "cn/0": false,
        "rx/arq": "rx/wow",
        "rx/keva": "rx/wow"
    },
    "opencl": {
        "enabled": true,
        "cache": true,
        "loader": null,
        "platform": "NVIDIA",
        "adl": true,
        "cn": [
            {
                "index": 0,
                "intensity": 912,
                "worksize": 8,
                "strided_index": [0, 2],
                "threads": [-1],
                "unroll": 8
            }
        ],
        "cn-heavy": [
            {
                "index": 0,
                "intensity": 304,
                "worksize": 8,
                "strided_index": [0, 2],
                "threads": [-1],
                "unroll": 8
            }
        ],
        "cn-lite": [
            {
                "index": 0,
                "intensity": 1824,
                "worksize": 8,
                "strided_index": [0, 2],
                "threads": [-1],
                "unroll": 8
            }
        ],
        "cn-pico": [
            {
                "index": 0,
                "intensity": 3952,
                "worksize": 8,
                "strided_index": [0, 2],
                "threads": [-1],
                "unroll": 8
            }
        ],
        "cn/2": [
            {
                "index": 0,
                "intensity": 912,
                "worksize": 8,
                "strided_index": [0, 2],
                "threads": [-1],
                "unroll": 8
            }
        ],
        "cn/upx2": [
            {
                "index": 0,
                "intensity": 3952,
                "worksize": 8,
                "strided_index": [0, 2],
                "threads": [-1],
                "unroll": 8
            }
        ],
        "kawpow": [
            {
                "index": 0,
                "intensity": 9961472,
                "worksize": 256,
                "threads": [-1],
                "unroll": 1
            }
        ],
        "rx": [
            {
                "index": 0,
                "intensity": 576,
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
        "enabled": false,
        "loader": null,
        "nvml": true,
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
            "url": "ethash.unmineable.com:3333",
            "user": "LTC:LV7SRSiRmv1jG6DSbsiDVsezLWTZbUzVyk.worker2#tzq1-ebba",
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
    "print-time": 300,
    "health-print-time": 300,
    "dmi": true,
    "syslog": false,
    "tls": {
        "enabled": true,
        "protocols": null,
        "cert": "cert.pem",
        "cert_key": "cert_key.pem",
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
    "watch": false,
    "pause-on-battery": false,
    "pause-on-active": false
}
```
**Expected behavior**
compile

run
**Required data**
 - OS: linux
 - For GPU related issues: cuda 12

**Additional context**
on pictures you can see more ...


what I doing wrong?


# Discussion History
## SChernykh | 2023-03-27T09:20:03+00:00
XMRig doesn't support ETHash, but you can mine KawPow algorithm. As for cuda, try to update cmake - latest versions should be able to find cuda 12 on your machine.

## Spudz76 | 2023-03-31T13:27:37+00:00
Use ` -DWITH_OPENCL=OFF` in the main xmrig build to disable OpenCL so it can't fall back to it when CUDA fails.  OpenCL on nvidia is terrible compared to CUDA.

For the xmrig-cuda build, do not specify `CUDA_LIB`;  and `/usr/local/cuda` is already the default so you also don't need `CUDA_TOOLKIT_ROOT_DIR` either.   You should specify `-DCUDA_ARCH=86` for 3060Ti.

## Spudz76 | 2023-03-31T13:29:23+00:00
Ensure your `/usr/local/cuda` is a link to the correct version of CUDA if you have multiples installed.  Whichever was the last to be installed will take over the link, it does not care if it's older.  So if you installed 12.x and then later also installed 11.2 then 11.2 will be the active version.

## MatejMagat305 | 2023-04-09T13:54:45+00:00
thank, and is available to put "-Ofast" options?

# Action History
- Created by: MatejMagat305 | 2023-03-27T09:16:04+00:00
- Closed at: 2025-06-18T22:44:27+00:00
