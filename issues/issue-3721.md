---
title: '`FAILED TO APPLY MSR MOD` even with sudo'
source_url: https://github.com/xmrig/xmrig/issues/3721
author: solomoncyj
assignees: []
labels:
- bug
created_at: '2025-10-14T03:21:16+00:00'
updated_at: '2025-11-26T13:26:52+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
**Describe the bug**
`FAILED TO APPLY MSR MOD` even with sudo on linux

**To Reproduce**
run xmr rig with sudo

**Expected behavior**
msr to be set properly

**Required data**
 - XMRig version : commit 6e4a5a6d94b33d6ed93890126c699b62f9553f50 , 

log:
```
sudo ./xmrig 
[sudo] password for solomoncyj: 
 * ABOUT        XMRig/6.24.0 clang/20.1.8 (built for Linux x86-64, 64 bit)
 * LIBS         libuv/1.51.0 OpenSSL/3.2.4 hwloc/2.12.0
 * HUGE PAGES   supported
 * 1GB PAGES    supported
 * CPU          AMD Ryzen 7 8845HS w/ Radeon 780M Graphics (1) 64-bit AES
                L2:8.0 MB L3:16.0 MB 8C/16T NUMA:1
 * MEMORY       5.2/27.2 GB (19%)
                DIMM_A0: 16 GB DDR5 @ 5600 MHz RMSB3410HA88IBF-5600
                DIMM_B0: 16 GB DDR5 @ 5600 MHz RMSB3410HA88IBF-5600
 * MOTHERBOARD  LENOVO - LNVNB161216
 * DONATE       1%
 * ASSEMBLY     auto:ryzen
 * POOL #1      sg.moneroocean.stream:20004 algo auto
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         disabled
[2025-10-14 11:13:04.101]  net      use pool sg.moneroocean.stream:20004 TLSv1.3 46.250.239.154
[2025-10-14 11:13:04.101]  net      fingerprint (SHA-256): "239daadd5c7d0ac097376c7871f787738826eef1c024729eff870e473b970855"
[2025-10-14 11:13:04.101]  net      new job from sg.moneroocean.stream:20004 diff 40000 algo rx/0 height 3521177 (14 tx)
[2025-10-14 11:13:04.101]  cpu      use argon2 implementation AVX-512F
[2025-10-14 11:13:04.101]  msr      cannot set MSR 0xc0011020 to 0x0004480000000000
[2025-10-14 11:13:04.101]  msr      FAILED TO APPLY MSR MOD, HASHRATE WILL BE LOW
[2025-10-14 11:13:04.101]  randomx  init dataset algo rx/0 (16 threads) seed eda7c5f27497e92d...
[2025-10-14 11:13:04.453]  randomx  allocated 3072 MB (2080+256) huge pages 100% 3/3 +JIT (352 ms)
[2025-10-14 11:13:06.733]  randomx  dataset ready (2280 ms)
[2025-10-14 11:13:06.733]  cpu      use profile  rx  (8 threads) scratchpad 2048 KB
[2025-10-14 11:13:06.737]  cpu      READY threads 8/8 (8) huge pages 100% 8/8 memory 16384 KB (4 ms)
[2025-10-14 11:13:09.171]  net      new job from sg.moneroocean.stream:20004 diff 40000 algo rx/0 height 3521178 (13 tx)
```
 - Config file:
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
        "1gb-pages": true,
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
        "argon2": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
        "cn": [
            [1, 0],
            [1, 2],
            [1, 4],
            [1, 6],
            [1, 8],
            [1, 10],
            [1, 12],
            [1, 14]
        ],
        "cn-heavy": [
            [1, 0],
            [1, 2],
            [1, 4],
            [1, 6]
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
            [1, 15]
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
            [2, 15]
        ],
        "cn/2": [
            [1, 0],
            [1, 2],
            [1, 4],
            [1, 6],
            [1, 8],
            [1, 10],
            [1, 12],
            [1, 14]
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
            [1, 15]
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
            [2, 15]
        ],
        "flex": [0, 2, 4, 6, 8, 10, 12, 14],
        "ghostrider": [
            [8, 0],
            [8, 2],
            [8, 4],
            [8, 6],
            [8, 8],
            [8, 10],
            [8, 12],
            [8, 14]
        ],
        "panthera": [0, 2, 4, 6, 8, 10, 12, 14],
        "rx": [0, 2, 4, 6, 8, 10, 12, 14],
        "rx/wow": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
        "cn-lite/0": false,
        "cn/0": false,
        "rx/xeq": "rx/wow",
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
    "donate-level": 0,
    "donate-over-proxy": 1,
    "pools": [
        {
            "algo": null,
            "coin": null,
            "url": "sg.moneroocean.stream:20004",
            "user": ,
            "pass": "x",
            "rig-id": null,
            "nicehash": false,
            "keepalive": false,
            "enabled": true,
            "tls": true,
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
        "ip_version": 0,
        "ttl": 30
    },
    "user-agent": null,
    "verbose": 0,
    "watch": true,
    "rebench-algo": false,
    "bench-algo-time": 10,
    "algo-min-time": 0,
    "algo-perf": {
        "cn/0": 710.3157894736842,
        "cn/1": 692.6536731634183,
        "cn/2": 692.6536731634183,
        "cn/r": 692.6536731634183,
        "cn/fast": 1385.3073463268365,
        "cn/half": 1385.3073463268365,
        "cn/xao": 692.6536731634183,
        "cn/rto": 692.6536731634183,
        "cn/rwz": 923.5382308845577,
        "cn/zls": 923.5382308845577,
        "cn/double": 346.32683658170913,
        "cn/ccx": 1420.6315789473683,
        "cn-lite/0": 2649.6700659868025,
        "cn-lite/1": 2649.6700659868025,
        "cn-heavy/xhv": 339.962026581393,
        "cn-pico": 18482.351764823517,
        "cn-pico/tlo": 18482.351764823517,
        "cn/gpu": 241.55555555555554,
        "rx/0": 4458.5541445855415,
        "rx/arq": 34327.36726327367,
        "rx/xeq": 34327.36726327367,
        "rx/graft": 4317.1682831716835,
        "rx/sfx": 4458.5541445855415,
        "panthera": 6592.640735926408,
        "argon2/chukwav2": 20636.880328386487,
        "kawpow": -1.0,
        "ghostrider": 1353.6649489956883,
        "flex": 1343.0495632958014
    },
    "pause-on-battery": false,
    "pause-on-active": false,
    "cache_qos":true,
}
```
 - OS: fedora 42, 6.16.10-200
 - For GPU related issues: information about GPUs and driver version.

**Additional context**
Add any other context about the problem here.


# Discussion History
## SChernykh | 2025-10-14T08:58:24+00:00
Can you try to run https://github.com/xmrig/xmrig/blob/master/scripts/randomx_boost.sh (with sudo) and see what error it gives you?

## solomoncyj | 2025-10-14T09:16:06+00:00
```
sudo ./randomx_boost.sh 
Detected Zen3 CPU
wrmsr: pwrite: Operation not permitted
```

## SChernykh | 2025-10-14T10:44:17+00:00
It is disabled in the kernel if you get this error. You can try to disable secure boot in BIOS - it helps sometimes with MSR issues. If it doesn't help, paste here the output of `uname -a`

## SChernykh | 2025-10-14T10:48:25+00:00
Also, can you paste here the output of `grep 'model' /proc/cpuinfo` because the script didn't detect Zen4 for you CPU.

## solomoncyj | 2025-10-15T01:10:40+00:00
```
grep 'model' /proc/cpuinfo
model		: 117
model name	: AMD Ryzen 7 8845HS w/ Radeon 780M Graphics
model		: 117
model name	: AMD Ryzen 7 8845HS w/ Radeon 780M Graphics
model		: 117
model name	: AMD Ryzen 7 8845HS w/ Radeon 780M Graphics
model		: 117
model name	: AMD Ryzen 7 8845HS w/ Radeon 780M Graphics
model		: 117
model name	: AMD Ryzen 7 8845HS w/ Radeon 780M Graphics
model		: 117
model name	: AMD Ryzen 7 8845HS w/ Radeon 780M Graphics
model		: 117
model name	: AMD Ryzen 7 8845HS w/ Radeon 780M Graphics
model		: 117
model name	: AMD Ryzen 7 8845HS w/ Radeon 780M Graphics
model		: 117
model name	: AMD Ryzen 7 8845HS w/ Radeon 780M Graphics
model		: 117
model name	: AMD Ryzen 7 8845HS w/ Radeon 780M Graphics
model		: 117
model name	: AMD Ryzen 7 8845HS w/ Radeon 780M Graphics
model		: 117
model name	: AMD Ryzen 7 8845HS w/ Radeon 780M Graphics
model		: 117
model name	: AMD Ryzen 7 8845HS w/ Radeon 780M Graphics
model		: 117
model name	: AMD Ryzen 7 8845HS w/ Radeon 780M Graphics
model		: 117
model name	: AMD Ryzen 7 8845HS w/ Radeon 780M Graphics
model		: 117
model name	: AMD Ryzen 7 8845HS w/ Radeon 780M Graphics
```

## zepp-fr | 2025-11-26T13:26:51+00:00
On Linux, I am unable to apply MSR mod on Intel CPU either (xmrig version 6.24.0).

# Action History
- Created by: solomoncyj | 2025-10-14T03:21:16+00:00
