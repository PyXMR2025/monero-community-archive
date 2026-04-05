---
title: Get error when starting to mine
source_url: https://github.com/xmrig/xmrig/issues/3550
author: CCMZA78
assignees: []
labels: []
created_at: '2024-09-12T21:44:27+00:00'
updated_at: '2025-06-18T22:05:56+00:00'
type: issue
status: closed
closed_at: '2025-06-18T22:05:56+00:00'
---

# Original Description
**Describe the bug**
I change the URL to unmineable in xmrig config file. See below:

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
        "huge-pages-jit": true,
        "hw-aes": null,
        "priority": 1,
        "memory-pool": true,
        "yield": true,
        "asm": true,
        "argon2-impl": null,
        "argon2": [0, 2, 3],
        "cn": [
            [1, 0],
            [1, 2]
        ],
        "cn-heavy": [
            [1, 0]
        ],
        "cn-lite": [
            [1, 0],
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
            [8, 2]
        ],
        "rx": [0, 2],
        "rx/arq": [0, 1, 2, 3],
        "rx/wow": [0, 2, 3],
        "cn-lite/0": false,
        "cn/0": false
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
    "donate-level": 1,
    "donate-over-proxy": 1,
    "pools": [
        {
            "algo": "rx/0",
            "coin": "ZEPH",
            "url": "rx.unmineable.com:443",
            "user": "walletaddress",
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
        },
        {
            "algo": "rx/0",
            "coin": "ZEPH",
            "url": "rx.unmineable.com:3333",
            "user": "walletaddress",
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
        },
        {
            "algo": "rx/0",
            "coin": "ZEPH",
            "url": "rx.unmineable.com:13333",
            "user": "walletaddress",
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
        },
        {
            "algo": "rx/0",
            "coin": "ZEPH",
            "url": "rx.unmineable.com:80",
            "user": "walletaddress",
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




I have done it before on my Macbook and it worked fine, but now that I am using a Windows 10 laptop I keep getting the below error:

![xmrig error](https://github.com/user-attachments/assets/167f1f9e-b97b-45cb-b8da-271b56f1bbf8)




**To Reproduce**
I start XMrig as follows:

1. I open Command Prompt.

2. I then add "cd and directory where XMRig is" after C:\Users\IamYunique> like this:

C:\Users\IamYunique>cd C:\Users\IamYunique\Downloads\xmrig-6.22.0-msvc-win64\xmrig-6.22.0

3. I then press enter and the below link appears:

C:\Users\IamYunique\Downloads\xmrig-6.22.0-msvc-win64\xmrig-6.22.0>

4. Then I add the words xmrig and press enter after the directory like this:

C:\Users\IamYunique\Downloads\xmrig-6.22.0-msvc-win64\xmrig-6.22.0>xmrig

XMRig runs as per normal but when it mines it gives the errors.

**Expected behavior**
On my Macbook with the same process it mines but it just gave this error

**Required data**
 - XMRig version
  I used versions 6.22.0 and 6.21.1 and it does the same

 - Miner log as text or screenshot
 - 
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
        "huge-pages-jit": true,
        "hw-aes": null,
        "priority": 1,
        "memory-pool": true,
        "yield": true,
        "asm": true,
        "argon2-impl": null,
        "argon2": [0, 2, 3],
        "cn": [
            [1, 0],
            [1, 2]
        ],
        "cn-heavy": [
            [1, 0]
        ],
        "cn-lite": [
            [1, 0],
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
            [8, 2]
        ],
        "rx": [0, 2],
        "rx/arq": [0, 1, 2, 3],
        "rx/wow": [0, 2, 3],
        "cn-lite/0": false,
        "cn/0": false
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
    "donate-level": 1,
    "donate-over-proxy": 1,
    "pools": [
        {
            "algo": "rx/0",
            "coin": "ZEPH",
            "url": "rx.unmineable.com:443",
            "user": "walletaddress",
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
        },
        {
            "algo": "rx/0",
            "coin": "ZEPH",
            "url": "rx.unmineable.com:3333",
            "user": "walletaddress",
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
        },
        {
            "algo": "rx/0",
            "coin": "ZEPH",
            "url": "rx.unmineable.com:13333",
            "user": "walletaddress",
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
        },
        {
            "algo": "rx/0",
            "coin": "ZEPH",
            "url": "rx.unmineable.com:80",
            "user": "walletaddress",
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
 - OS: [e.g. Windows]
 
Windows 10 Pro

 - For GPU related issues: information about GPUs and driver version.

**Additional context**
Add any other context about the problem here.


# Discussion History
## SChernykh | 2024-09-12T21:53:09+00:00
It says on the screenshot what you're doing wrong. You need to provide Monero address, not Zephyr address, and remove `"coin": "ZEPH",` from the config.

# Action History
- Created by: CCMZA78 | 2024-09-12T21:44:27+00:00
- Closed at: 2025-06-18T22:05:56+00:00
