---
title: no active connection!
source_url: https://github.com/xmrig/xmrig/issues/2700
author: njfamirm
assignees: []
labels: []
created_at: '2021-11-16T19:38:50+00:00'
updated_at: '2021-12-28T09:38:12+00:00'
type: issue
status: closed
closed_at: '2021-12-28T09:38:12+00:00'
---

# Original Description
hi

when i run `xmrig` on my linux

after a while , i have no result!

result
```
 * ABOUT        XMRig/6.15.3 gcc/11.1.0
 * LIBS         libuv/1.42.0 OpenSSL/1.1.1l hwloc/2.5.0
 * HUGE PAGES   supported
 * 1GB PAGES    disabled
 * CPU          AMD Athlon(tm) II X2 250 Processor (1) 64-bit -AES
                L2:2.0 MB L3:0.0 MB 2C/2T NUMA:1
 * MEMORY       3.3/3.8 GB (86%)
 * DONATE       5%
 * ASSEMBLY     auto:none
 * POOL #1      xmrpool.eu:9999 algo auto
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         disabled
[2021-11-16 23:06:26.920] no active connection
[2021-11-16 23:06:28.696] no results yet
```

when i use VPN have this result

```
~  → xmrig
 * ABOUT        XMRig/6.15.3 gcc/11.1.0
 * LIBS         libuv/1.42.0 OpenSSL/1.1.1l hwloc/2.5.0
 * HUGE PAGES   supported
 * 1GB PAGES    disabled
 * CPU          AMD Athlon(tm) II X2 250 Processor (1) 64-bit -AES
                L2:2.0 MB L3:0.0 MB 2C/2T NUMA:1
 * MEMORY       3.3/3.8 GB (85%)
 * DONATE       5%
 * ASSEMBLY     auto:none
 * POOL #1      xmrpool.eu:9999 algo auto
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         disabled
[2021-11-16 23:12:45.661]  net      xmrpool.eu:9999 connect error: "connection refused"
```



config.json file
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
        "mode": "light",
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
        "argon2": [0, 1],
        "astrobwt": [0, 1],
        "cn": [
            [1, 0],
            [1, 1]
        ],
        "cn-heavy": [
            [1, -1]
        ],
        "cn-lite": [
            [1, 0],
            [1, 1]
        ],
        "cn-pico": [
            [2, 0],
            [2, 1]
        ],
        "cn/upx2": [
            [2, 0],
            [2, 1]
        ],
        "rx": [0, 1],
        "rx/wow": [0, 1],
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
        "adl": true
    },
    "cuda": {
        "enabled": false,
        "loader": null,
        "nvml": true
    },
    "log-file": null,
    "donate-level": 5,
    "donate-over-proxy": 1,
    "pools": [
        {
            "algo": null,
            "coin": null,
            "url": "xmrpool.eu:9999",
            "user": "bitcoin:16R8kd8adRHZ6yeJYcPCYLmaZX26Qo4Cmb",
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
```



# Discussion History
# Action History
- Created by: njfamirm | 2021-11-16T19:38:50+00:00
- Closed at: 2021-12-28T09:38:12+00:00
