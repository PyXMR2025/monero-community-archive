---
title: Unknown/unsupported algorithm detected, reconnect...login error code:6
source_url: https://github.com/xmrig/xmrig/issues/1613
author: at1921
assignees: []
labels: []
created_at: '2020-03-26T04:02:25+00:00'
updated_at: '2021-04-12T14:59:13+00:00'
type: issue
status: closed
closed_at: '2021-04-12T14:59:13+00:00'
---

# Original Description
**Describe the bug**
A clear and concise description of what the bug is.

**To Reproduce**
Steps to reproduce the behavior.

**Expected behavior**
A clear and concise description of what you expected to happen.

**Required data**
 - Miner log as text or screenshot
 - Config file or command line (without wallets)
 - OS: [e.g. Windows]
 - For GPU related issues: information about GPUs and driver version.

**Additional context**
Add any other context about the problem here.


# Discussion History
## at1921 | 2020-03-26T04:10:21+00:00
I am trying to start mining Monero with my GPU (GeForce GTX 1650 @1560/4001 MHz) and my CPU Intel(R) Core(TM) i7-9750H CPU @ 2.60 GHz) but I can't get it to start mining due to the login error code:6. I am on Windows OS.
It says this: Unknown/unsupported algorithm detected, reconnect [pool.supportxmr.com:3333} login error code: 6
![Image 1](https://user-images.githubusercontent.com/62684283/77609276-e9fdf900-6ef5-11ea-8d0e-b930a53c8c70.png)


This is my current config:
{
    "algo": "cryptonight",
    "api": {
        "port": 0,
        "access-token": null,
        "id": null,
        "worker-id": null,
        "ipv6": false,
        "restricted": true
    },
    "background": false,
    "colors": true,
    "cuda-bfactor": 6,
    "cuda-bsleep": 25,
    "cuda-max-threads": 64,
    "donate-level": 1,
    "log-file": null,
    "pools": [
        {
            "url": "pool.supportxmr.com:3333",
            "user": "44Kx3jhK868NAXSiZGxsFDP7punCLDm2RSdP1dtLvPPgfKvYnSHfzX9RUzeR6o4ra6j8QmcE3fwUeatsW4sLaD5VHHS8EHt",
            "pass": "x",
            "rig-id": null,
            "nicehash": false,
            "keepalive": true,
            "variant": -1,
            "enabled": true,
            "tls": false,
            "tls-fingerprint": null
        }
    ],
    "print-time": 60,
    "retries": 5,
    "retry-pause": 5,
    "threads": [
        {
            "index": 0,
            "threads": 32,
            "blocks": 48,
            "bfactor": 6,
            "bsleep": 25,
            "sync_mode": 3,
            "affine_to_cpu": false
        }
    ],
    "user-agent": null,
    "syslog": false,
    "watch": true
}


## SChernykh | 2020-03-26T13:20:29+00:00
It says "algo": "cryptonight", in your config which is wrong. It's better to generate new config using https://xmrig.com/wizard

## at1921 | 2020-03-26T22:31:40+00:00
I am unfamiliar with this "wizard."  Is there a tutorial on how I can make the config for my setup.

## suanlian1 | 2020-03-27T17:46:22+00:00
set `"algo": null,`

## Lonnegan | 2020-03-30T21:17:46+00:00
> I am trying to start mining Monero with my GPU (GeForce GTX 1650 @1560/4001 MHz) and ...

Don't mine Monero with a GPU. The new Monero algo RandomX is optimized for CPUs, not for GPU. Mine something else with your NVIDIA GPU; BTG or some other non-ASIC Equihash algo.

## at1921 | 2020-03-31T03:45:04+00:00
> > I am trying to start mining Monero with my GPU (GeForce GTX 1650 @1560/4001 MHz) and ...
> 
> Don't mine Monero with a GPU. The new Monero algo RandomX is optimized for CPUs, not for GPU. Mine something else with your NVIDIA GPU; BTG or some other non-ASIC Equihash algo.

Say I were to build my own monero rig, would you recommend how I can go about building one.   I am a complete beginner and I haven't heard of productive CPU mining.  Is there a way you can have more than one CPU mining the monero coin?

## ajtazer | 2020-08-28T15:44:39+00:00
Same Error But My config already has algo=NULL
Also i made my config with WIZARD https://xmrig.com/wizard
MY CONFIG-
`{
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
        "mode": "auto",
        "1gb-pages": false,
        "rdmsr": true,
        "wrmsr": true,
        "cache_qos": false,
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
            [1, 3],
            [1, 4],
            [1, 5],
            [1, 6],
            [1, 7]
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
        "rx": [0, 2, 4, 6],
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
        "adl": true
    },
    "cuda": {
        "enabled": false,
        "loader": null,
        "nvml": true
    },
    "donate-level": 5,
    "donate-over-proxy": 1,
    "log-file": null,
    "pools": [
        {
            "algo": null,
            "coin": "monero",
            "url": "xmrpool.eu:5555",
            "user": "84Mn9Pq4g7fFHaRY9tc9JyfG5B5oRmAR691zsREAb2vbi87XnvfpZiFcWniq76MQMVfSxWgNWZGUU2itGjGDpjumGV2iSjb",
            "pass": "x",
            "rig-id": "test",
            "nicehash": false,
            "keepalive": true,
            "enabled": true,
            "tls": false,
            "tls-fingerprint": null,
            "daemon": false,
            "socks5": null,
            "self-select": null
        }
    ],
    "print-time": 1800,
    "health-print-time": 60,
    "retries": 1,
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
    "watch": true,
    "pause-on-battery": false
}`

# Action History
- Created by: at1921 | 2020-03-26T04:02:25+00:00
- Closed at: 2021-04-12T14:59:13+00:00
