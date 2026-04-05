---
title: ./xmrig  Cannot establish connection to the host.
source_url: https://github.com/xmrig/xmrig/issues/1724
author: Chriszan
assignees: []
labels: []
created_at: '2020-06-08T23:32:43+00:00'
updated_at: '2020-08-19T01:15:51+00:00'
type: issue
status: closed
closed_at: '2020-08-19T01:15:51+00:00'
---

# Original Description
Hello, I am new to ubuntu. I have installed xmrig in a cloud server with ubuntu 18.04. When I run it, I get the Cannot establish connection to the host error.
Can you give me a hand to configure it? It took 3 days and I can't get it. 
I have to configure ip's? I can't find information.
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
    "randomx": {
        "init": -1,
        "mode": "auto",
        "1gb-pages": true,
        "rdmsr": true,
        "wrmsr": true,
        "numa": true
    },
    "cpu": {
        "enabled": true,
        "huge-pages": true,
        "hw-aes": null,
        "priority": null,
        "memory-pool": false,
        "yield": true,
        "asm": true,
        "argon2-impl": null,
        "astrobwt-max-size": 550,
        "astrobwt-avx2": false,
        "argon2": [0, 1, 2, 3, 4, 5, 6, 7],
        "astrobwt": [0, 1, 2, 3, 4, 5, 6, 7],
        "cn": [
            [1, 0],
            [1, 1],
            [1, 2],
            [1, 3],
            [1, 4],
            [1, 5],
            [1, 6],
            [1, 7]
        ],
        "cn-heavy": [
            [1, 0],
            [1, 1],
            [1, 2],
            [1, 3]
        ],
        "cn-lite": [
            [1, 0],
            [1, 1],
            [1, 2],
            [1, 3],
            [1, 4],
            [1, 5],
            [1, 6],
            [1, 7]
        ],
        "cn-pico": [
            [2, 0],
            [2, 1],
            [2, 2],
            [2, 3],
            [2, 4],
            [2, 5],
            [2, 6],
            [2, 7]
        ],
        "rx": [0, 1, 2, 3, 4, 5, 6, 7],
        "rx/wow": [0, 1, 2, 3, 4, 5, 6, 7],
        "cn/0": false,
        "cn-lite/0": false,
        "rx/arq": "rx/wow",
        "rx/keva": "rx/wow"
    },
    "opencl": {
        "enabled": false,
        "cache": true,
        "loader": null,
        "platform": "AMD",
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
            "algo": "rx/0",
            "coin": "monero",
            "url": "xmr-eu1.nanopool.org:14444",
            "user": "My_Wallet",
            "pass": "x",
            "rig-id": null,
            "nicehash": false,
            "keepalive": false,
            "enabled": true,
            "tls": false,
            "tls-fingerprint": null,
            "daemon": false,
            "socks5": null,
            "self-select": null
        }
    ],
    "print-time": 60,
    "health-print-time": 60,
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
    "user-agent": null,
    "verbose": 0,
    "watch": true
}



# Discussion History
## rawbonesfck | 2020-06-09T03:10:15+00:00
"tls": false,

change to true

maybe
"keepalive": false,
change to true as well

## Chriszan | 2020-06-09T10:00:08+00:00
Thanks for you help. Now I receive: sh: 1: ./xmrig: Permission denied. 


## downystreet | 2020-06-09T14:24:23+00:00
You need to run it as root using sudo ./xmrig. This will solve the permission denied problem. Also, you need to put a wallet address in the "user": "My_Wallet", section unless you are using a proxy.

## Chriszan | 2020-06-09T21:27:06+00:00
A lot of thanks for your help. The server is caped. I'm looking for another. 

# Action History
- Created by: Chriszan | 2020-06-08T23:32:43+00:00
- Closed at: 2020-08-19T01:15:51+00:00
