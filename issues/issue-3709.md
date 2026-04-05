---
title: OpenCL don't accept any jobs at all on m1 Mac, but new jobs just keep coming
source_url: https://github.com/xmrig/xmrig/issues/3709
author: leeleeleeW
assignees: []
labels: []
created_at: '2025-09-18T11:46:29+00:00'
updated_at: '2025-11-16T07:05:30+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
**Describe the bug**
OpenCL don't accept any jobs at all on m1 Mac, but new jobs just keep coming

**To Reproduce**
I've been mining on m1 Mac with XMRig for Ravencoin using kawpow algorithm for a long time, but no one single has ever been accepted by OpenCL, only new jobs keep coming
**Expected behavior**
A clear and concise description of what you expected to happen.
just make it to accept jobs normally
**Required data**
 - XMRig version
    - latest version 6.24.0 from https://github.com/xmrig/xmrig/releases

 - Miner log as text or screenshot
 - Config file or command line (without wallets)
   config.json as below:
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
        "wrmsr": false,
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
        "argon2-impl": null,
        "argon2": [0, 1, 2, 3, 4, 5, 6, 7],
        "cn": [0, 1, 2, 3, 4, 5, 6, 7],
        "cn-heavy": [0, 1, 2, 3, 4, 5, 6, 7],
        "cn-lite": [0, 1, 2, 3, 4, 5, 6, 7],
        "cn-pico": [0, 1, 2, 3, 4, 5, 6, 7],
        "cn/upx2": [0, 1, 2, 3, 4, 5, 6, 7],
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
        "enabled": true,
        "huge-pages": true,
        "cache": true,
        "loader": null,
        "platform": "APPLE",
        "cn": [
            {
                "index": 0,
                "intensity": 384,
                "worksize": 8,
                "strided_index": [0, 2],
                "threads": [-1],
                "unroll": 8
            }
        ],
        "cn-heavy": [
            {
                "index": 0,
                "intensity": 192,
                "worksize": 8,
                "strided_index": [0, 2],
                "threads": [-1],
                "unroll": 8
            }
        ],
        "cn-lite": [
            {
                "index": 0,
                "intensity": 832,
                "worksize": 8,
                "strided_index": [0, 2],
                "threads": [-1],
                "unroll": 8
            }
        ],
        "cn-pico": [
            {
                "index": 0,
                "intensity": 1984,
                "worksize": 8,
                "strided_index": [0, 2],
                "threads": [-1],
                "unroll": 8
            }
        ],
        "cn/2": [
            {
                "index": 0,
                "intensity": 384,
                "worksize": 8,
                "strided_index": [0, 2],
                "threads": [-1],
                "unroll": 8
            }
        ],
        "cn/upx2": [
            {
                "index": 0,
                "intensity": 1984,
                "worksize": 8,
                "strided_index": [0, 2],
                "threads": [-1],
                "unroll": 8
            }
        ],
        "kawpow": [
            {
                "index": 0,
                "intensity": 6291456,
                "worksize": 256,
                "threads": 7,
                "unroll": 8
               
            }
        ],
        "rx": [
            {
                "index": 0,
                "intensity": 128,
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
        "cn-lite/0": false,
        "cn/0": false
    },
    "log-file": null,
    "donate-level": 1,
    "donate-over-proxy": null,
    "pools": [
        {
            "algo": "kawpow",
            "coin": "RVN",
            "url": "asia.ravenminer.com:3838",
            "user": "wallet address",
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
        "ip_version": 0,
        "ttl": 30
    },
    "user-agent": null,
    "verbose": 0,
    "watch": true,
    "pause-on-battery": false,
    "pause-on-active": false
}

also, screenshots

![Image](https://github.com/user-attachments/assets/c89a1031-7f3b-4930-928b-4d3f95a33263)

![Image](https://github.com/user-attachments/assets/1f6b4956-4ef8-488d-ab53-a90eb2718df2)

![Image](https://github.com/user-attachments/assets/c591758b-0a83-48eb-b7bc-310a40790ccd)

 - OS: Mac M1 air
 - For GPU related issues: information about GPUs and driver version.

**Additional context**
It just keeps mining without any jobs accepted!

# Discussion History
## leeleeleeW | 2025-09-18T11:47:19+00:00
please help advise solutions !

## HumbleDeer | 2025-11-16T07:05:30+00:00
Does the memory actually get allocated beyond just the light dag cache? 


# Action History
- Created by: leeleeleeW | 2025-09-18T11:46:29+00:00
