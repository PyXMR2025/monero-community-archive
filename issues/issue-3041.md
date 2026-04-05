---
title: Cannot change pause-on-battery configuration without restarting xmrig
source_url: https://github.com/xmrig/xmrig/issues/3041
author: JacksonChen666
assignees: []
labels:
- bug
created_at: '2022-05-05T18:36:24+00:00'
updated_at: '2022-06-23T13:04:13+00:00'
type: issue
status: closed
closed_at: '2022-06-23T13:04:12+00:00'
---

# Original Description
**Describe the bug**
Changing the configuration `pause-on-battery` from `true` to `false` does not apply the changes even if configuration is reloaded

**To Reproduce**
1. Create a new config (or not)
2. Get a computer with a battery (that xmrig can detect of course)
3. Enable `pause-on-battery` in config file and save file
4. Unplug any chargers
5. Start xmrig
6. Disable `pause-on-battery` in config file and save file
7. Try to resume xmrig interactively, it will say that it refuses to resume because of battery power

**Expected behavior**
The change would apply

**Required data**
 - Miner log as text or screenshot
```
[2022-05-05 20:28:25.937]  config   "/Users/jackson/.xmrig.json" was changed, reloading configuration
[2022-05-05 20:28:25.941]  miner    on battery power
[2022-05-05 20:28:25.941]  miner    paused
[2022-05-05 20:28:30.314]  config   "/Users/jackson/.xmrig.json" was changed, reloading configuration
[2022-05-05 20:28:30.361]  net      new job from ******************* diff 50001 algo rx/0 height 2617023 (101 tx)
[2022-05-05 20:28:35.040]  miner    can't resume while on battery power
```
 - Config file or command line (without wallets)
```
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
        "1gb-pages": false,
        "rdmsr": false,
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
        "priority": 1,
        "memory-pool": false,
        "yield": true,
        "argon2-impl": null,
        "astrobwt-max-size": 550,
        "astrobwt-avx2": false,
        "*": {
            "intensity": 1,
            "threads": 8,
            "affinity": -1
        },
        "kawpow": false
    },
    "opencl": {
        "enabled": false,
        "cache": true,
        "loader": null
    },
    "cuda": {
        "enabled": false,
        "loader": null
    },
    "log-file": null,
    "donate-level": 5,
    "donate-over-proxy": 1,
    "pools": [
        {
            "algo": null,
            "coin": null,
            "url": "************",
            "user": "u+50000",
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
    "pause-on-active": 60
}
```
 - OS: macOS (M1 Macbook Pro (not M1 Pro or Max or Ultra))
 - Miner version: 6.17.0

# Discussion History
## SChernykh | 2022-05-05T19:14:43+00:00
#3042 should fix this.

# Action History
- Created by: JacksonChen666 | 2022-05-05T18:36:24+00:00
- Closed at: 2022-06-23T13:04:12+00:00
