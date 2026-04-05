---
title: Connection refused when using XMRig 6.15.2 in Windows 10
source_url: https://github.com/xmrig/xmrig/issues/2647
author: MarshalSeb
assignees: []
labels: []
created_at: '2021-10-25T17:55:16+00:00'
updated_at: '2021-10-25T21:01:19+00:00'
type: issue
status: closed
closed_at: '2021-10-25T21:01:19+00:00'
---

# Original Description
Dear XMRig,

I have recently tried to setup XMRig for solo-mining (using 127.0.0.1:18081 as my url/port), however I keep getting a connection issue saying "connect error: connection refused". What do I need to do to get it to work?

Here is my config.json file for my settings:
{
    "api": {
        "id": null,
        "worker-id": null
    },
    "http": {
        "enabled": false,
        "host": "127.0.0.1",
        "port": 18081,
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
        "enabled": false,
        "huge-pages": true,
        "huge-pages-jit": false,
        "hw-aes": null,
        "priority": null,
        "memory-pool": false,
        "yield": true,
        "max-threads-hint": 100,
        "asm": true,
        "argon2-impl": null,
        "astrobwt-max-size": 550,
        "astrobwt-avx2": false
    },
    "opencl": {
        "enabled": false,
        "cache": true,
        "loader": null,
        "platform": "AMD",
        "adl": true
    },
    "cuda": {
        "enabled": true,
        "loader": null,
        "nvml": true,
        "astrobwt": [
            {
                "index": 0,
                "threads": 32,
                "blocks": 8,
                "bfactor": 6,
                "bsleep": 25,
                "affinity": -1
            }
        ],
        "cn": [
            {
                "index": 0,
                "threads": 34,
                "blocks": 72,
                "bfactor": 6,
                "bsleep": 25,
                "affinity": -1
            }
        ],
        "cn-heavy": [
            {
                "index": 0,
                "threads": 16,
                "blocks": 72,
                "bfactor": 6,
                "bsleep": 25,
                "affinity": -1
            }
        ],
        "cn-lite": [
            {
                "index": 0,
                "threads": 68,
                "blocks": 72,
                "bfactor": 6,
                "bsleep": 25,
                "affinity": -1
            }
        ],
        "cn-pico": [
            {
                "index": 0,
                "threads": 128,
                "blocks": 72,
                "bfactor": 6,
                "bsleep": 25,
                "affinity": -1
            }
        ],
        "cn/2": [
            {
                "index": 0,
                "threads": 34,
                "blocks": 72,
                "bfactor": 6,
                "bsleep": 25,
                "affinity": -1
            }
        ],
        "cn/upx2": [
            {
                "index": 0,
                "threads": 128,
                "blocks": 72,
                "bfactor": 6,
                "bsleep": 25,
                "affinity": -1
            }
        ],
        "kawpow": [
            {
                "index": 0,
                "threads": 256,
                "blocks": 49152,
                "bfactor": 6,
                "bsleep": 25,
                "affinity": -1
            }
        ],
        "rx": [
            {
                "index": 0,
                "threads": 32,
                "blocks": 46,
                "bfactor": 6,
                "bsleep": 25,
                "affinity": -1,
                "dataset_host": false
            }
        ],
        "rx/arq": [
            {
                "index": 0,
                "threads": 32,
                "blocks": 48,
                "bfactor": 6,
                "bsleep": 25,
                "affinity": -1,
                "dataset_host": false
            }
        ],
        "rx/keva": [
            {
                "index": 0,
                "threads": 32,
                "blocks": 48,
                "bfactor": 6,
                "bsleep": 25,
                "affinity": -1,
                "dataset_host": false
            }
        ],
        "rx/wow": [
            {
                "index": 0,
                "threads": 32,
                "blocks": 48,
                "bfactor": 6,
                "bsleep": 25,
                "affinity": -1,
                "dataset_host": false
            }
        ],
        "cn-lite/0": false,
        "cn/0": false
    },
    "log-file": null,
    "donate-level": 3,
    "donate-over-proxy": 1,
    "pools": [
        {
            "algo": null,
            "coin": "XMR",
            "url": "127.0.0.1:18081",
            "user": "_My wallet address_",
            "enabled": true,
            "tls": false,
            "tls-fingerprint": null,
            "daemon": true,
            "socks5": null,
            "daemon-poll-interval": 1000,
            "daemon-zmq-port": -1
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

# Discussion History
## Spudz76 | 2021-10-25T19:11:28+00:00
Is your daemon running?  Otherwise it's firewall related.

## MarshalSeb | 2021-10-25T19:13:02+00:00
Could be firewall related. I've been fighting with my firewall the whole time, but so far no luck. Do you think port forwarding will fix the issue?

## Spudz76 | 2021-10-25T19:21:27+00:00
No, `127.*.*.*` stays inside your local computer it has nothing to do with any router anywhere.

So windows firewall, or various anti-garbageware apps will block the port for both the miner and the daemon since most people don't want either one (Potentially Unwanted list).  So you may have to add both folders to exceptions somewhere.

## MarshalSeb | 2021-10-25T20:50:46+00:00
Thanks! I'll give it a try! Modern Antivirus has a myriad of ways to block any strange internet traffic, so it'll be a long haul to get it fixed!

# Action History
- Created by: MarshalSeb | 2021-10-25T17:55:16+00:00
- Closed at: 2021-10-25T21:01:19+00:00
