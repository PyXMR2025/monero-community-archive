---
title: '" no active pools, stop mining" and read error: "connection timed out"'
source_url: https://github.com/xmrig/xmrig/issues/2745
author: EALG12
assignees: []
labels: []
created_at: '2021-11-29T03:24:22+00:00'
updated_at: '2025-06-20T11:08:25+00:00'
type: issue
status: closed
closed_at: '2025-06-20T11:08:25+00:00'
---

# Original Description
**Describe the bug**
A clear and concise description of what the bug is.
appear the following errors while mining: " no active pools, stop mining" and read error: "connection timed out"


**To Reproduce**
Steps to reproduce the behavior.

**Expected behavior**
A clear and concise description of what you expected to happen.
Do not stop mining.

**Required data**
 - Miner log as text or screenshot
 [2021-11-28 18:39:20.426]  net      new job from rx.unmineable.com:3333 diff 100001 algo rx/0 height 2503491 (47 tx)
[2021-11-28 18:39:36.242]  miner    speed 10s/60s/15m 461.4 462.9 335.8 H/s max 517.3 H/s
[2021-11-28 18:40:36.586]  miner    speed 10s/60s/15m 461.2 462.4 345.1 H/s max 517.3 H/s
[2021-11-28 18:41:36.946]  miner    speed 10s/60s/15m 463.8 460.3 354.5 H/s max 517.3 H/s
[2021-11-28 18:42:02.625]  net      no active pools, stop mining
[2021-11-28 18:42:37.345]  miner    speed 10s/60s/15m n/a 195.3 345.9 H/s max 517.3 H/s
[2021-11-28 18:42:57.743]  net      rx.unmineable.com:3333 connect error: "operation canceled"
[2021-11-28 18:43:22.873]  net      rx.unmineable.com:3333 connect error: "operation canceled"
[2021-11-28 18:43:37.910]  miner    speed 10s/60s/15m n/a n/a 324.0 H/s max 517.3 H/s
[2021-11-28 18:44:18.216]  net      rx.unmineable.com:3333 connect error: "operation canceled"
[2021-11-28 18:44:35.879] no active connection
[2021-11-28 18:44:38.298]  miner    speed 10s/60s/15m n/a n/a 302.2 H/s max 517.3 H/s
[2021-11-28 18:44:38.479] no active connection


[2021-11-28 22:10:32.093]  miner    speed 10s/60s/15m 516.0 478.1 304.8 H/s max 526.3 H/s
[2021-11-28 22:11:30.394]  net      rx.unmineable.com:3333 read error: "connection timed out"
[2021-11-28 22:11:30.394]  net      no active pools, stop mining
[2021-11-28 22:11:32.426]  miner    speed 10s/60s/15m 385.3 456.4 314.3 H/s max 526.3 H/s
[2021-11-28 22:11:36.314]  net      use pool rx.unmineable.com:3333  139.59.164.251
[2021-11-28 22:11:36.314]  net      new job from rx.unmineable.com:3333 diff 100001 algo rx/0 height 2503587 (36 tx)
[2021-11-28 22:11:44.038]  net      new job from rx.unmineable.com:3333 diff 100001 algo rx/0 height 2503588 (43 tx)
[2021-11-28 22:11:51.021]  net      new job from rx.unmineable.com:3333 diff 100001 algo rx/0 height 2503588 (43 tx)
[2021-11-28 22:12:16.911]  net      new job from rx.unmineable.com:3333 diff 100001 algo rx/0 height 2503589 (22 tx)
[2021-11-28 22:12:21.063]  net      new job from rx.unmineable.com:3333 diff 100001 algo rx/0 height 2503589 (22 tx)
[2021-11-28 22:12:32.722]  miner    speed 10s/60s/15m 511.0 455.4 323.6 H/s max 526.3 H/s
[2021-11-28 22:13:01.795]  cpu      accepted (62/0) diff
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
        "argon2": [0, 2, 3],
        "astrobwt": [0, 1, 2, 3],
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
        "cn/0": false,
        "rx/keva": "rx/wow"
    },
    "opencl": {
        "enabled": false,
        "cache": true,
        "loader": null,
        "cn-lite/0": false,
        "cn/0": false
    },
    "cuda": {
        "enabled": false,
        "loader": null,
        "cn-lite/0": false,
        "cn/0": false
    },
    "log-file": null,
    "donate-level": 1,
    "donate-over-proxy": 1,
    "pools": [
        {
            "algo": null,
            "coin": null,
            "url": ,
            "user": ,
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

 - OS: [e.g. Windows]
 MACOSX, cpu
 - For GPU related issues: information about GPUs and driver version.

**Additional context**
Add any other context about the problem here.


# Discussion History
## Spudz76 | 2021-11-29T05:28:07+00:00
Job diff of 100001 is for 3333.366666667H/s minimum.  Pools without autodiff are stupid.

You need job diff ~15780.

It's pretty lucky you even found 62 results.  Most of your work is going unpaid.

# Action History
- Created by: EALG12 | 2021-11-29T03:24:22+00:00
- Closed at: 2025-06-20T11:08:25+00:00
