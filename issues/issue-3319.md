---
title: 'OpenCL disabled '
source_url: https://github.com/xmrig/xmrig/issues/3319
author: mkkc
assignees: []
labels: []
created_at: '2023-08-19T16:05:17+00:00'
updated_at: '2025-06-18T22:39:58+00:00'
type: issue
status: closed
closed_at: '2025-06-18T22:39:58+00:00'
---

# Original Description
Hi, I want to enable OPENCL on my Intel server but xmrig allways shows this feature as disabled. Can someone help me please ?

lof file
 * ABOUT        XMRig/6.20.0 gcc/9.4.0
 * LIBS         libuv/1.44.2 OpenSSL/1.1.1s hwloc/2.9.0
 * HUGE PAGES   supported
 * 1GB PAGES    disabled
 * CPU          Intel(R) Core(TM) i5-7400 CPU @ 3.00GHz (1) 64-bit AES
                L2:1.0 MB L3:6.0 MB 4C/4T NUMA:1
 * MEMORY       1.3/7.7 GB (17%)
 * DONATE       1%
 * ASSEMBLY     auto:intel
 * POOL #1      xmr-us-west1.nanopool.org:14433 coin Monero
kelo@xerces:~$ sudo less -X /home/kelo/xmrig-6.20.0/xmrig.log
 * ABOUT        XMRig/6.20.0 gcc/9.4.0
 * LIBS         libuv/1.44.2 OpenSSL/1.1.1s hwloc/2.9.0
 * HUGE PAGES   supported
 * 1GB PAGES    disabled
 * CPU          Intel(R) Core(TM) i5-7400 CPU @ 3.00GHz (1) 64-bit AES
                L2:1.0 MB L3:6.0 MB 4C/4T NUMA:1
 * MEMORY       1.3/7.7 GB (17%)
 * DONATE       1%
 * ASSEMBLY     auto:intel
 * POOL #1      xmr-us-west1.nanopool.org:14433 coin Monero
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         disabled

OS                                              Ubuntu Server 22.04
 Platform Name                                   Intel(R) OpenCL Graphics
 Device Name                                     Intel(R) HD Graphics 630
 Device Vendor                                   Intel(R) Corporation
 Device Vendor ID                                0x8086
 Device Version                                  OpenCL 3.0 NEO
 Device Numeric Version                          0xc00000 (3.0.0)
 Driver Version                                  23.22.26516.18
 Device OpenCL C Version                         OpenCL C 1.2

command line
 sudo /home/kelo/xmrig-6.20.0/xmrig --opencl-devices 0 --opencl-loader libOpenCL.so --opencl-platform=Imagination -c -B --syslog /home/kelo/xmrig-6.20.0/config.json


config.json
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
        "argon2": [0, 1, 2, 3],
        "cn": [
            [1, 0],
            [1, 1],
            [1, 2]
        ],
        "cn-heavy": [
            [1, 0],
            [1, 1]
        ],
        "cn-lite": [
            [1, 0],
            [1, 1],
            [1, 2],
            [1, 3]
        ],
        "cn-pico": [
            [2, 0],
            [2, 1],
            [2, 2],
            [2, 3]
        ],
        "cn/upx2": [
            [2, 0],
            [2, 1],
            [2, 2],
            [2, 3]
        ],
        "ghostrider": [
            [8, 0],
            [8, 1],
            [8, 2]
        ],
        "rx": [0, 1, 2],
        "rx/wow": [0, 1, 2, 3],
        "cn-lite/0": false,
        "cn/0": false,
        "rx/arq": "rx/wow",
        "rx/keva": "rx/wow"
    },
    "opencl": {
        "enabled": true,
        "cache": true,
        "loader": null,
        "platform": "Intel",
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
            "url": "theurl",
            "user": "myaddress",
            "pass": null,
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
Thanks in advance!

# Discussion History
## SChernykh | 2023-08-19T16:11:20+00:00
You shouldn't mix command line arguments and config.json. Try to only use config.json.

## mkkc | 2023-08-19T16:55:48+00:00
Thanks, your advice helped me to figure out my issue. Running sudo ./xmrig it shows me NVRM: No NVIDIA gpu found,  xmrig enable OPENCL and dectects Intel HD GRAPHICS 630, then opencl gpu #0 compiling... free()...invalida pointer Aborted and xmrig ends.

# Action History
- Created by: mkkc | 2023-08-19T16:05:17+00:00
- Closed at: 2025-06-18T22:39:58+00:00
