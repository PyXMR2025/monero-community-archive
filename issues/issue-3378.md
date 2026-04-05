---
title: how do I change difficulty in xmrig from xmrig-proxy
source_url: https://github.com/xmrig/xmrig/issues/3378
author: DARK-DEVIL-66
assignees: []
labels: []
created_at: '2023-12-10T09:51:02+00:00'
updated_at: '2023-12-16T15:00:19+00:00'
type: issue
status: closed
closed_at: '2023-12-16T15:00:19+00:00'
---

# Original Description
i want to set all my miners cpu max is 20% and fixed diff is 120000
i will shared my config.json for xmrig-proxy anything have issue please rewrite for me and thank's


{
    "access-log-file": null,
    "access-password": null,
    "algo-ext": true,
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
    "background": false,
    "bind": [
        {
            "host": "0.0.0.0",
            "port": 8888,
            "tls": true
        },
        {
            "host": "::",
            "port": 8888,
            "tls": true
        }
    ],
    "colors": true,
    "title": true,
    "custom-diff": 0,
    "custom-diff-stats": false,
    "donate-level": 0,
    "log-file": null,
    "mode": "nicehash",
    "pools": [
        {
            "algo": "rx/0",
            "url": "sg.zephyr.herominers.com:1123",
            "user": "ZEPHYR2s5bnTUHNSTKfG9Gc6eC88LFNpEcHjChP2HTi1Wt1pry5XXqBWrLeUUYzzurC22ySZHLwvRgmSAvNcDXsZKm3K9uKBVD33w=120000",
            "pass": "Saba-zephyr",
            "keepalive": true,
            "enabled": true,
            "tls": true
        }
    ],
    "retries": 2,
    "retry-pause": 1,
    "reuse-timeout": 0,
    "tls": {
        "enabled": true,
        "protocols": null,
        "cert": null,
        "cert_key": null,
        "ciphers": null,
        "ciphersuites": null,
        "dhparam": null
    },
    "user-agent": null,
    "syslog": false,
    "verbose": false,
    "watch": true,
    "workers": true
}

# Discussion History
# Action History
- Created by: DARK-DEVIL-66 | 2023-12-10T09:51:02+00:00
- Closed at: 2023-12-16T15:00:19+00:00
