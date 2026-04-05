---
title: 'read error: connection reset by peer'
source_url: https://github.com/xmrig/xmrig/issues/2792
author: Aurok85
assignees: []
labels: []
created_at: '2021-12-05T07:10:27+00:00'
updated_at: '2021-12-07T13:59:28+00:00'
type: issue
status: closed
closed_at: '2021-12-07T13:59:28+00:00'
---

# Original Description
First time using xmrig and cpu mining RTM I keep getting an error in command prompt.

![image](https://user-images.githubusercontent.com/95561931/144737262-121ea054-17c9-4335-bf8d-38598f0dac09.png)


# Discussion History
## SChernykh | 2021-12-05T09:39:50+00:00
This pool URL works for me. Can you show your full command line or config.json?

## emilianovilla | 2021-12-05T17:15:57+00:00
Same problem. With Flockpool.

## emilianovilla | 2021-12-05T17:27:27+00:00
![image](https://user-images.githubusercontent.com/19435195/144756814-4014ccab-9c52-4056-a241-bbdb00018e44.png)

## Aurok85 | 2021-12-05T20:05:41+00:00
> This pool URL works for me. Can you show your full command line or config.json?

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
        "argon2": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
        "astrobwt": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
        "cn": [
            [1, 0],
            [1, 1],
            [1, 2],
            [1, 3],
            [1, 4],
            [1, 5],
            [1, 6],
            [1, 7],
            [1, 8],
            [1, 9],
            [1, 10],
            [1, 11],
            [1, 12],
            [1, 13],
            [1, 14],
            [1, 15],
            [1, 16],
            [1, 17],
            [1, 18],
            [1, 19],
            [1, 20],
            [1, 21],
            [1, 22],
            [1, 23]
        ],
        "cn-heavy": [
            [1, 0],
            [1, 2],
            [1, 4],
            [1, 5],
            [1, 6],
            [1, 8],
            [1, 10],
            [1, 11],
            [1, 12],
            [1, 14],
            [1, 16],
            [1, 17],
            [1, 18],
            [1, 20],
            [1, 22],
            [1, 23]
        ],
        "cn-lite": [
            [1, 0],
            [1, 1],
            [1, 2],
            [1, 3],
            [1, 4],
            [1, 5],
            [1, 6],
            [1, 7],
            [1, 8],
            [1, 9],
            [1, 10],
            [1, 11],
            [1, 12],
            [1, 13],
            [1, 14],
            [1, 15],
            [1, 16],
            [1, 17],
            [1, 18],
            [1, 19],
            [1, 20],
            [1, 21],
            [1, 22],
            [1, 23]
        ],
        "cn-pico": [
            [2, 0],
            [2, 1],
            [2, 2],
            [2, 3],
            [2, 4],
            [2, 5],
            [2, 6],
            [2, 7],
            [2, 8],
            [2, 9],
            [2, 10],
            [2, 11],
            [2, 12],
            [2, 13],
            [2, 14],
            [2, 15],
            [2, 16],
            [2, 17],
            [2, 18],
            [2, 19],
            [2, 20],
            [2, 21],
            [2, 22],
            [2, 23]
        ],
        "cn/upx2": [
            [2, 0],
            [2, 1],
            [2, 2],
            [2, 3],
            [2, 4],
            [2, 5],
            [2, 6],
            [2, 7],
            [2, 8],
            [2, 9],
            [2, 10],
            [2, 11],
            [2, 12],
            [2, 13],
            [2, 14],
            [2, 15],
            [2, 16],
            [2, 17],
            [2, 18],
            [2, 19],
            [2, 20],
            [2, 21],
            [2, 22],
            [2, 23]
        ],
        "ghostrider": [
            [8, 0],
            [8, 2],
            [8, 4],
            [8, 6],
            [8, 8],
            [8, 10],
            [8, 12],
            [8, 14],
            [8, 16],
            [8, 18],
            [8, 20],
            [8, 22]
        ],
        "rx": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
        "rx/wow": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
        "cn-lite/0": false,
        "cn/0": false,
        "rx/arq": "rx/wow",
        "rx/keva": "rx/wow"
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
            "algo": "ghostrider",
            "coin": null,
            "url": "raptorna.011data.com:3008",
            "user": "RHfH3Lz2JAun4rr4ioh8ypsfGFBogTkxgg.AurokMiningWS",
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

## Spudz76 | 2021-12-05T21:23:46+00:00
Must be firewall or other blocker.  Works from here, too.

## emilianovilla | 2021-12-05T21:26:12+00:00
> Must be firewall or other blocker. Works from here, too.

Not firewall block.

## Spudz76 | 2021-12-05T22:20:53+00:00
Then ISP.  Use VPN.  Works from here, no firewall, no oppressive ISP.

## SChernykh | 2021-12-05T22:40:11+00:00
@emilianovilla your screenshot is not even from xmrig

## Aurok85 | 2021-12-07T13:59:28+00:00
Finding this reddit post I was able to fix the issue.

Copied from - https://www.reddit.com/r/NiceHash/comments/naoys3/xmrig_read_error_connection_reset_by_peer/

What worked for me was logging into my router and switching on IPv6 setting to passive, then restarting the router, then logging back into my router switching IPv6 off and it worked straight away.

I had read somewhere to switch on IPv6 as a way to solve the error but this only worked for 1 afternoon then the error returned, so I just decided to switch off IPv6 and reset the router and it seems to have solved it instantly.

# Action History
- Created by: Aurok85 | 2021-12-05T07:10:27+00:00
- Closed at: 2021-12-07T13:59:28+00:00
