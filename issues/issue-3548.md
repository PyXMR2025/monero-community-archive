---
title: selected OpenCL platform NOT found
source_url: https://github.com/xmrig/xmrig/issues/3548
author: MBecke36
assignees: []
labels: []
created_at: '2024-09-08T22:40:58+00:00'
updated_at: '2025-06-18T22:05:16+00:00'
type: issue
status: closed
closed_at: '2025-06-18T22:05:16+00:00'
---

# Original Description
After installation, this error occurs:
"selected OpenCL platform NOT found"
opencl was reinstalled.
with "lspci" this is found:
03:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Ellesm ere [Radeon RX 470/480/570/570X/580/580X/590] (rev cf)

**To Reproduce**
Steps to reproduce the behavior.

How can I fix the error so that I can mine with the card?

**Required data**
 - XMRig 6.22.0
    1. sudo apt install git build-essential cmake automake libtool autoconf
2. git clone https://github.com/xmrig/xmrig.git
3. mkdir xmrig/build && cd xmrig/scripts
4. ./build_deps.sh && cd ../build
5. cmake .. -DXMRIG_DEPS=scripts/deps
6. make -j$(nproc)
7. 

 - Miner log as text or screenshot:
genius@MinerRig:~$ ./xmrig/build/xmrig
[2024-09-09 00:24:54.333] Error UNKNOWN_ERROR when calling clGetPlatformIDs for number of platforms.
[2024-09-09 00:24:54.333] No OpenCL platform found.
 * ABOUT        XMRig/6.22.0 gcc/11.4.0 (built for Linux x86-64, 64 bit)
 * LIBS         libuv/1.48.0 OpenSSL/3.0.14 hwloc/2.10.0
 * HUGE PAGES   supported
 * 1GB PAGES    unavailable
 * CPU           (1) 64-bit -AES
                L2:0.5 MB L3:0.0 MB 1C/1T NUMA:1
 * MEMORY       1.1/7.7 GB (15%)
 * DONATE       1%
 * ASSEMBLY     auto:none
 * POOL #1      xmr.kryptex.network:7777 coin Monero
 * COMMANDS     hashrate, pause, resume, results, connection
[2024-09-09 00:24:54.338] Error UNKNOWN_ERROR when calling clGetPlatformIDs for number of platforms.
[2024-09-09 00:24:54.338] No OpenCL platform found.
 * OPENCL       disabled (selected OpenCL platform NOT found)
 * CUDA         disabled
[2024-09-09 00:24:54.466]  net      use pool xmr.kryptex.network:7777  157.90.32.66
[2024-09-09 00:24:54.466]  net      new job from xmr.kryptex.network:7777 diff 400015 algo rx/0 height 3233262 (1 tx)
[2024-09-09 00:24:54.466]  cpu      use argon2 implementation SSE2
[2024-09-09 00:24:55.667]  randomx  init dataset algo rx/0 (1 threads) seed 36b6fa94ae6af2ea...
[2024-09-09 00:24:55.668]  randomx  allocated 2336 MB (2080+256) huge pages 0% 0/1168 +JIT (0 ms)
[2024-09-09 00:25:59.937]  randomx  dataset ready (64268 ms)
[2024-09-09 00:25:59.937]  cpu      use profile  rx  (1 thread) scratchpad 2048 KB
[2024-09-09 00:25:59.938] Error UNKNOWN_ERROR when calling clGetPlatformIDs for number of platforms.
[2024-09-09 00:25:59.938] No OpenCL platform found.
 * OPENCL       disabled (selected OpenCL platform NOT found)
[2024-09-09 00:25:59.938]  cpu      READY threads 1/1 (1) huge pages 0% 0/1 memory 2048 KB (1 ms)
 

 - Config file or command line (without wallets)
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
        "max-threads-hint": 100,
        "asm": true,
        "argon2-impl": null,
        "cn/0": false,
        "cn-lite/0": false
    },
    "opencl": {
        "enabled": true,
        "cache": true,
        "loader": null,
        "platform": 3,
        "adl": true,
        "cn/0": false,
        "cn-lite/0": false
    },
    "cuda": {
        "enabled": false,
        "loader": null,
        "nvml": true,
        "cn/0": false,
        "cn-lite/0": false
    },
    "donate-level": 1,
    "donate-over-proxy": 1,
    "log-file": null,
    "pools": [
        {
            "algo": null,
            "coin": "xmr",
            "url": "xmr.kryptex.network:7777",
            "user": "XXXXXXXXXXXXX/Miner",
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
    "print-time": 60,
    "health-print-time": 60,
    "dmi": true,
    "retries": 5,
    "retry-pause": 5,
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


 - OS: Ubuntu 22.04.04
 - For GPU related issues: information about GPUs and driver version.
 - 03:00.0 VGA compatible controller [0300]: Advanced Micro Devices, Inc. [AMD/ATI] Ellesmere [Radeon RX 470/480/570/570X/580/580X/590] [1002:67df] (rev cf)
        Subsystem: Micro-Star International Co., Ltd. [MSI] Ellesmere [Radeon RX 470/480/570/570X/580/580X/590] [1462:3414]
        Kernel driver in use: amdgpu
        Kernel modules: amdgpu


**Additional context**
Add any other context about the problem here.


# Discussion History
# Action History
- Created by: MBecke36 | 2024-09-08T22:40:58+00:00
- Closed at: 2025-06-18T22:05:16+00:00
