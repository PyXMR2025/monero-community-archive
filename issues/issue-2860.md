---
title: pause on active new job
source_url: https://github.com/xmrig/xmrig/issues/2860
author: doadin
assignees: []
labels: []
created_at: '2022-01-11T09:51:03+00:00'
updated_at: '2022-12-16T14:11:54+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
**Describe the bug**
Using the "pause-on-active" config option it says its paused but continues to say "new job" as if its requesting work but not executing it.

**To Reproduce**
"pause-on-active": true
start mining

**Expected behavior**
All actions stop when user active.

**Required data**
-
`
[2022-01-11 04:36:19.573]  net      new job from poolurl.com:3333 diff 174379 algo rx/0 height 2534796 (153 tx)
[2022-01-11 04:36:47.356]  net      new job from poolurl.com:3333 diff 174245 algo rx/0 height 2534796 (153 tx)
[2022-01-11 04:36:49.527]  cpu      accepted (1948/0) diff 174245 (50 ms)
[2022-01-11 04:37:05.786]  miner    user active
[2022-01-11 04:37:05.786]  miner    paused, press  r  to resume
[2022-01-11 04:37:12.292]  miner    speed 10s/60s/15m 1208.0 3404.0 3921.7 H/s max 4111.3 H/s
[2022-01-11 04:37:47.513]  net      new job from poolurl.com:3333 diff 174195 algo rx/0 height 2534796 (153 tx)
[2022-01-11 04:38:12.339]  miner    speed 10s/60s/15m n/a n/a 3661.8 H/s max 4111.3 H/s
[2022-01-11 04:38:25.226]  net      new job from poolurl.com:3333 diff 174195 algo rx/0 height 2534797 (26 tx)
[2022-01-11 04:38:47.656]  net      new job from poolurl.com:3333 diff 174061 algo rx/0 height 2534797 (26 tx)
[2022-01-11 04:39:12.386]  miner    speed 10s/60s/15m n/a n/a 3399.8 H/s max 4111.3 H/s
[2022-01-11 04:39:47.746]  net      new job from poolurl.com:3333 diff 173976 algo rx/0 height 2534797 (26 tx)
[2022-01-11 04:40:12.434]  miner    speed 10s/60s/15m n/a n/a 3134.0 H/s max 4111.3 H/s
[2022-01-11 04:40:36.338]  net      new job from poolurl.com:3333 diff 173976 algo rx/0 height 2534798 (2 tx)
[2022-01-11 04:40:47.832]  net      new job from poolurl.com:3333 diff 173836 algo rx/0 height 2534798 (2 tx)
[2022-01-11 04:41:12.482]  miner    speed 10s/60s/15m n/a n/a 2868.1 H/s max 4111.3 H/s
[2022-01-11 04:41:47.895]  net      new job from poolurl.com:3333 diff 173702 algo rx/0 height 2534798 (2 tx)
`
 
```
 "{
    "api": {
    	"id": null,
    	"worker-id": "w"
    },
    "http": {
    	"enabled": true,
    	"host": "0.0.0.0",
    	"port": 8880,
    	"access-token": null,
    	"restricted": true
    },
    "autosave": false,
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
        "numa": false,
        "scratchpad_prefetch_mode": 1
    },
    "cpu": {
        "enabled": true,
        "huge-pages": true,
        "huge-pages-jit": false,
        "hw-aes": null,
        "priority": null,
        "memory-pool": -1,
        "yield": true,
        "max-threads-hint": 100,
        "asm": true,
        "cn": [0, 2, 4, 6],
        "cn/r": [0, 2, 4, 6],
        "cn-heavy": [0, 2],
        "cn-lite": [0, 1, 2, 3, 4, 5, 6, 7],
        "cn-pico": [0, 1, 2, 3, 4, 5, 6, 7],
        "cn/gpu": [0, 1, 2, 3, 4, 5, 6, 7],
        "rx/0": [0, 2, 4, 6],
        "rx/wow": [0, 1, 2, 3, 4, 5, 6, 7],
        "argon2-impl": null,
        "astrobwt-max-size": 550,
        "cn/0": false,
        "cn-lite/0": false,
        "kawpow": false
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
        "cn/0": true,
        "cn-lite/0": true
    },
    "donate-level": 0,
    "donate-over-proxy": null,
    "log-file": null,
    "pools": [
        {
            "algo": "rx/0",
            "coin": null,
            "url": "poolurl.com:3333",
            "user": "supersecret",
            "pass": "w",
            "rig-id": null,
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
    "watch": true,
    "pause-on-battery": false,
    "pause-on-active": true
}"

```
have also tried with pools:keepalive:false
 - OS: Windows 10 21H2 x64

**Additional context**
Add any other context about the problem here.


# Discussion History
## Spudz76 | 2022-01-11T13:47:13+00:00
Correct, pause does not disconnect.  It purely stops mining.

Although I agree I'd rather have it disconnect, too, so that the autodiff doesn't crash to 100 and then flood when unpaused.

## rkraneis | 2022-12-16T13:03:23+00:00
Manually pausing has the same problem. After a while, xmrig even starts complaining itself :laughing: 

![image](https://user-images.githubusercontent.com/1737287/208103703-1033e2ba-d32b-4ded-a585-2702d728e42e.png)

One annoying side effect of the general ignoring-jobs behavior: the pool I use adjusts the difficulty way down (from ~100k to ~10k within 5 minutes). It takes about half an hour until I get jobs with appropriate difficulty (~100k). For longer pauses, I usually kill xmrig now and restart it later :/

## SChernykh | 2022-12-16T14:11:54+00:00
If you use pause feature actively, set fixed difficulty at your pool.

# Action History
- Created by: doadin | 2022-01-11T09:51:03+00:00
