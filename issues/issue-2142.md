---
title: 'connect error: "operation canceled"'
source_url: https://github.com/xmrig/xmrig/issues/2142
author: xmaresalizm31
assignees: []
labels: []
created_at: '2021-03-01T04:58:37+00:00'
updated_at: '2021-04-12T14:09:03+00:00'
type: issue
status: closed
closed_at: '2021-04-12T14:09:03+00:00'
---

# Original Description
Hello; i have a problem
I get this error when I try to mine with xmrig on my remote desktop, which I connect to with ssh. please help.

error: stratum+tcp://randomxmonero.eu-west.nicehash.com:3380 connect error: "operation canceled"

config.json


{
    "api": {
        "id": null,
        "worker-id": null
    },
    "http": {
        "enabled": false,
        "host": "127.0.0.1",
        "port": 3380,
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
{
    "api": {
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
        "argon2": [0, 4, 1, 5, 2, 6, 3, 7],
        "astrobwt": [0, 4, 1, 5, 2, 6, 3, 7],
        "cn": [
            [1, 0],
            [1, 4],
            [1, 1],
            [1, 5],
            [1, 2],
            [1, 6],
            [1, 3],
            [1, 7]
        ],
        "cn-heavy": [
            [1, 0],
            [1, 4],
            [1, 1],
            [1, 5],


    },
    "opencl": {
        "enabled": false,
        "cache": true,
        "loader": null,
        "platform": "NVİDİA",
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
    "log-file": null,
    "donate-level": 1,
    "donate-over-proxy": 1,
    "pools": [
        {
            "algo": null,
            "coin": null,
            "url": "stratum+tcp://randomxmonero.eu-west.nicehash.com:3380",
            "user": "8C2NVSiYcTCLgAF8WhzvTzBMpyENAY1ifdwBdAXKGQLLDtUNxD3NqzJdLDNuxRFPZgiuEE4Rdui1YErdH8uBYZxq27Kovga",
            "pass": "x",
            "rig-id": null,
            "nicehash": true,
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
    "user-agent": null,
    "verbose": 0,
    "watch": true,
    "pause-on-battery": false,


# Discussion History
# Action History
- Created by: xmaresalizm31 | 2021-03-01T04:58:37+00:00
- Closed at: 2021-04-12T14:09:03+00:00
