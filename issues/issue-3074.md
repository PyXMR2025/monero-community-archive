---
title: Does xmrig support stratum+tcp
source_url: https://github.com/xmrig/xmrig/issues/3074
author: netbie
assignees: []
labels:
- question
created_at: '2022-06-21T01:40:33+00:00'
updated_at: '2022-12-13T14:33:09+00:00'
type: issue
status: closed
closed_at: '2022-12-13T14:33:09+00:00'
---

# Original Description
pool url set "stratum+tcp://prohashing.com:3333"
![error](https://user-images.githubusercontent.com/107898415/174698635-1393b75a-81b8-431b-9062-a3606dd35b04.png)
, run xmrig appear read error: "end of file"

# Discussion History
## netbie | 2022-06-21T02:05:50+00:00
![erro2](https://user-images.githubusercontent.com/107898415/174701229-c04dfc39-1e28-4314-ac2b-72c32eec45b7.png)


## SChernykh | 2022-06-21T05:44:45+00:00
Yes, but it's not required, so you can just use `prohashing.com:3359`. Your configuration error is somewhere else, show your full xmrig command line or config.json

## netbie | 2022-06-21T07:01:49+00:00
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
        "max-threads-hint": 100,
        "asm": true,
        "argon2-impl": null,
        "astrobwt-max-size": 550,
        "astrobwt-avx2": false,
        "cn/0": false,
        "cn-lite/0": false
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
            "algo": null,
            "coin": null,
            "url": "stratum+tcp://prohashing.com:3359",
            "user": "YOUR_WALLET_ADDRESS",
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
    "print-time": 60,
    "health-print-time": 60,
    "dmi": true,
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


## netbie | 2022-06-21T07:06:04+00:00
> Yes, but it's not required, so you can just use `prohashing.com:3359`. Your configuration error is somewhere else, show your full xmrig command line or config.json
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
        "max-threads-hint": 100,
        "asm": true,
        "argon2-impl": null,
        "astrobwt-max-size": 550,
        "astrobwt-avx2": false,
        "cn/0": false,
        "cn-lite/0": false
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
            "algo": null,
            "coin": null,
            "url": "stratum+tcp://prohashing.com:3359",
            "user": "YOUR_WALLET_ADDRESS",
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
    "print-time": 60,
    "health-print-time": 60,
    "dmi": true,
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



YOUR_WALLET_ADDRESS I have filled in my wallet address, other parameters have not changed

## SChernykh | 2022-06-21T07:20:01+00:00
Did you even read their help/getting started page? You need to set a specific password to mine Monero, something like `"pass": "a=randomx,c=monero",`

## netbie | 2022-06-21T07:39:24+00:00
> Did you even read their help/getting started page? You need to set a specific password to mine Monero, something like `"pass": "a=randomx,c=monero",`

![1](https://user-images.githubusercontent.com/107898415/174742692-a47eaab8-8c77-45b1-8f5a-db04031713c4.png)
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
        "argon2": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
        "astrobwt": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
        "astrobwt/v2": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
        "cn": [
            [1, 0],
            [1, 2],
            [1, 4],
            [1, 6],
            [1, 8],
            [1, 10],
            [1, 12],
            [1, 14]
        ],
        "cn-heavy": [
            [1, 0],
            [1, 2],
            [1, 4],
            [1, 6]
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
            [1, 15]
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
            [2, 15]
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
            [2, 15]
        ],
        "ghostrider": [
            [8, 0],
            [8, 2],
            [8, 4],
            [8, 6],
            [8, 8],
            [8, 10],
            [8, 12],
            [8, 14]
        ],
        "rx": [0, 2, 4, 6, 8, 10, 12, 14],
        "rx/wow": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
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
            "algo": null,
            "coin": null,
            "url": "prohashing.com:3359",
            "user": "YOUR_WALLET_ADDRESS",
            "pass": "a=randomx",
            "rig-id": null,
            "nicehash": false,
            "keepalive": false,
            "enabled": true,
            "tls": false,
            "wss": false,
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
still read error end of file

## SChernykh | 2022-06-21T08:05:52+00:00
Try to also set `"algo": "rx/0",`

## netbie | 2022-06-21T08:19:04+00:00
> Try to also set `"algo": "rx/0",`

pools": [
{
"algo": "rx/0",
"coin": null,
"url": "prohashing.com:3359",
"user": "YOUR_WALLET_ADDRESS",
"pass": "a=randomx",
"rig-id": null,
"nicehash": false,
"keepalive": false,
"enabled": true,
"tls": false,
"wss": false,
"tls-fingerprint": null,
"daemon": false,
"socks5": null,
"self-select": null,
"submit-to-origin": false
}
I have tried to close the firewall,still read error end of file,

## netbie | 2022-06-21T08:57:03+00:00
> Try to also set `"algo": "rx/0",`

https://prohashing.com/help/configuring-miners-at-prohashing#configurator-advancedoptions
Did I miss any settings?

## SChernykh | 2022-06-21T10:32:07+00:00
`"algo": "rx/0",` and `"pass":"a=randomx,c=monero,m=pplns",` works for me.

## netbie | 2022-06-21T10:52:20+00:00
> `"algo": "rx/0",` and `"pass":"a=randomx,c=monero,m=pplns",` works for me.

![run](https://user-images.githubusercontent.com/107898415/174782755-930c1078-8120-4065-92d0-bce7945859ef.png)
still read error end of file

## SChernykh | 2022-06-21T11:04:07+00:00
`"user": "YOUR_WALLET_ADDRESS",` you have to put your account name, not a wallet address there. Otherwise I don't know what's wrong, use a normal pool and not this weird one.

## netbie | 2022-06-21T11:29:58+00:00
> "rx/0"

user to geek, it worked, thanks. But I would like to ask how to distribute the cryptocurrency to me without filling in the wallet address

## Spudz76 | 2022-06-22T05:57:36+00:00
How would it know where to send it if you don't give wallet address?

## DeeDeeRanged | 2022-08-18T11:39:56+00:00
> > "rx/0"
> 
> user to geek, it worked, thanks. But I would like to ask how to distribute the cryptocurrency to me without filling in the wallet address

As you have regitered yourself with this pool I suggest login and check account details, probably there is where you entered you MONERO_WALLET address.


# Action History
- Created by: netbie | 2022-06-21T01:40:33+00:00
- Closed at: 2022-12-13T14:33:09+00:00
