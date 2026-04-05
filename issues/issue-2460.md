---
title: Mines via NiceHash
source_url: https://github.com/xmrig/xmrig/issues/2460
author: UnixCro
assignees: []
labels: []
created_at: '2021-06-27T10:36:23+00:00'
updated_at: '2024-01-22T19:22:55+00:00'
type: issue
status: closed
closed_at: '2024-01-22T19:22:55+00:00'
---

# Original Description
Any ideas how I can run NiceHash xmrig without an error message?

```
{
    "api": {
        "id": null,
        "worker-id": null
    },
    "http": {
        "enabled": false,
        "host": "127.0.0.2",
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
        "argon2": [0, 1, 2, 3],
        "astrobwt": [0, 1, 2, 3],
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
        "rx": [0, 1, 2],
        "rx/wow": [0, 1, 2, 3],
        "cn/0": false,
        "cn-lite/0": false,
        "rx/arq": "rx/wow",
        "rx/keva": "rx/wow"
    },
    "opencl": {
        "enabled": false,
        "cache": true,
        "loader": null,
        "cn/0": false,
        "cn-lite/0": false
    },
    "cuda": {
        "enabled": false,
        "loader": null,
        "cn/0": false,
        "cn-lite/0": false
    },
    "log-file": null,
    "donate-level": 1,
    "donate-over-proxy": 1,
    "pools": [
        {
            "algo": null,
            "coin": null,
            "url": "stratum+tcp://randomxmonero.eu-west.nicehash.com:3380",
            "user": "MYBTCADRESS",
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
    "print-time": 60,
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
Message: 

```
[2021-06-27 12:35:48.215]  net      stratum+tcp://randomxmonero.eu-west.nicehash.com:3380 unknown algorithm, make sure you set "algo" or "coin" option
[2021-06-27 12:35:48.216]  net      stratum+tcp://randomxmonero.eu-west.nicehash.com:3380 login error code: 6
```
macOS Big Sur 10.16

# Discussion History
## SChernykh | 2021-06-27T12:56:31+00:00
You don't need `stratum+tcp://` in the pool URL, also set `"algo": "rx/0",`

## UnixCro | 2021-06-27T13:38:34+00:00
Thank you very much @SChernykh. It worked !!



# Action History
- Created by: UnixCro | 2021-06-27T10:36:23+00:00
- Closed at: 2024-01-22T19:22:55+00:00
