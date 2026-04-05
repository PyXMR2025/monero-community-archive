---
title: run as administrator doesnt work
source_url: https://github.com/xmrig/xmrig/issues/3418
author: susgirl446
assignees: []
labels: []
created_at: '2024-02-07T07:11:03+00:00'
updated_at: '2024-02-11T11:16:37+00:00'
type: issue
status: closed
closed_at: '2024-02-11T11:16:36+00:00'
---

# Original Description
**Describe the bug**
Rightclick the exe > Run As Admin doesnt work (it cant apply MSR mod)

**To Reproduce**
Right click the executable > Run as admin (win 11)

**Expected behavior**
it should apply MSR mod 

**Required data**
 - miner log:
 
![image](https://github.com/xmrig/xmrig/assets/129160115/f409b156-1ad6-4bc6-8b2d-227d4312fa85)

 - Config file or command line (without wallets)
 - {
```
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
        "argon2": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
        "cn": [
            [1, 0],
            [1, 2],
            [1, 4],
            [1, 5],
            [1, 6],
            [1, 7],
            [1, 8],
            [1, 9]
        ],
        "cn-heavy": [
            [1, 0],
            [1, 2],
            [1, 4]
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
            [1, 11]
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
            [2, 11]
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
            [2, 11]
        ],
        "ghostrider": [
            [8, 0],
            [8, 2]
        ],
        "rx": [0, 2, 4, 5, 6, 7, 8, 9, 10],
        "rx/wow": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
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
    "donate-level": 0,
    "donate-over-proxy": 0,
    "pools": [
        {
            "algo": null,
            "coin": null,
            "url": "pool.supportxmr.com:5555",
            "user": "my wallet is here",
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
    "verbose": 1,
    "watch": true,
    "pause-on-battery": false,
    "pause-on-active": false
}
```
 - OS: windows 11 latest update
 - For GPU related issues: i use cpu

**Additional context**
video showing the bug
https://youtu.be/GriuJYG8DTM

# Discussion History
## geekwilliams | 2024-02-07T07:41:20+00:00
Please disable Secure Boot and try again 

## susgirl446 | 2024-02-07T08:08:46+00:00
> Please disable Secure Boot and try again

whats secure boot?


## geekwilliams | 2024-02-07T08:13:28+00:00
Secure Boot is a method of security your motherboard uses to verify that the bootloader for the Operating system has not been tampered with. With some Intel processor/motherboard combos, Secure Boot also disallows the use of MSR Mods, giving you the issue you're experiencing.  For details on how to disable Secure Boot, you'll need to get the manual for your motherboard, and follow its guide, or you could just search google for it

## susgirl446 | 2024-02-07T13:22:33+00:00
so i now disabled secure boot but msr mod still doesnt work

## SChernykh | 2024-02-07T18:40:51+00:00
Disable core isolation and memory integrity in Windows.

## susgirl446 | 2024-02-08T07:08:31+00:00
where is core isolation?
![image](https://github.com/xmrig/xmrig/assets/129160115/f9b0401d-9547-4aff-894c-95fbb873a581)


## susgirl446 | 2024-02-08T12:26:55+00:00
ok it worked now but can i execute it as admin in a batch script?

## geekwilliams | 2024-02-08T17:03:46+00:00
Right click and run the batch script as administrator 

## susgirl446 | 2024-02-09T16:07:13+00:00
ok. one last question, how can i setup a fallback pool that xmrig connects to when the main pool goes down

## geekwilliams | 2024-02-09T17:29:18+00:00
In the "pools" array of the config, put a comma after the }, then add another set of brackets {} then add the backup pool information in between those brackets. Make sure you follow json formatting rules 

## susgirl446 | 2024-02-11T11:16:36+00:00
thanks for helping

# Action History
- Created by: susgirl446 | 2024-02-07T07:11:03+00:00
- Closed at: 2024-02-11T11:16:36+00:00
