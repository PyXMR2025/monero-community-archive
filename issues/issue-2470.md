---
title: 'xmrig not working on Linux '
source_url: https://github.com/xmrig/xmrig/issues/2470
author: TimyIsCool
assignees: []
labels: []
created_at: '2021-07-03T23:06:29+00:00'
updated_at: '2021-07-04T20:08:06+00:00'
type: issue
status: closed
closed_at: '2021-07-04T20:08:06+00:00'
---

# Original Description
if i try running xmrig i get this error 
![image](https://user-images.githubusercontent.com/74112751/124368721-ac8d2d00-dc5b-11eb-9f1c-1010e2924859.png)


# Discussion History
## ghost | 2021-07-04T16:01:54+00:00
Syntax is missing in config.json just recheck configuration.

## TimyIsCool | 2021-07-04T16:14:02+00:00
ok im using the config wisard on the site 

This is my config

{
    "autosave": true,
    "cpu": true,
    "opencl": false,
    "cuda": false,
    "pools": [
        {
            "url": "xmrpool.eu:9999",
            "user": "42rrP8MT5mXAY4HRhH7ojv1jMtWe1wdDD4QjRnJyQ5ViPtSYHf1CzNNERD49b6p4yLdB8kveRzoVvbqFn5oebbFPEpHygjR",
            "keepalive": true,
            "tls": true
        }
    ]
}

## SChernykh | 2021-07-04T16:22:32+00:00
If you downloaded xmrig binary from github, it won't work on Raspberry Pi. You need to build it yourself.

## TimyIsCool | 2021-07-04T16:24:02+00:00
> If you downloaded xmrig binary from github, it won't work on Raspberry Pi. You need to build it yourself.

ok, will update you on how it goes


## ghost | 2021-07-04T16:31:07+00:00
Confirm  particular ssl stratum wont work in xmrig and it's only works on clayminer

SSL/TLS Mining
Claymore miner > 9.7 enabled SSL mining. Using SSL mining allows to lower dev fee from 2.5% to 2%.
xmrpool.eu has a special port 9999 for Claymore SSL miners.
If you want to mine using Claymore with lower fee (2%) configure it to use: -o ssl://xmrpool.eu:9999 

You can try it on port 443 instead of 9999

Or try on different pool :)

## TimyIsCool | 2021-07-04T16:59:43+00:00
![image](https://user-images.githubusercontent.com/74112751/124393262-903bcf80-dcf1-11eb-9f64-da2922a3be6d.png)
what do i do with the xmrig.json

## TimyIsCool | 2021-07-04T17:04:48+00:00
ok fixed it but i got this 
![image](https://user-images.githubusercontent.com/74112751/124393401-40113d00-dcf2-11eb-8387-b8e2bd39786e.png)
i have 1gb on my pi, how do i configure gpu mem on ubuntu server 21.04.1

## TimyIsCool | 2021-07-04T18:03:29+00:00
> In my cases I just playing around CPU not in GPU cause it won't support GPU acceleration

ok but how do i fix the bus error?

## ghost | 2021-07-04T18:04:52+00:00
> > In my cases I just playing around CPU not in GPU cause it won't support GPU acceleration
> 
> ok but how do i fix the bus error?

It's like you not enough memory and try set threads to 1 should be working 

## TimyIsCool | 2021-07-04T18:05:11+00:00
will try now


## TimyIsCool | 2021-07-04T18:05:44+00:00
> will try now

how do i do that again?


## ghost | 2021-07-04T18:09:54+00:00
> > will try now
> 
> how do i do that again?

Find rx/0 in configuration and from 0,1,2,3 just set 0

## TimyIsCool | 2021-07-04T18:20:19+00:00
can u change what to change for me cuz i cant get it to work

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
        "argon2-impl": null,
        "astrobwt-max-size": 550,
        "astrobwt-avx2": false,
        "argon2": [0, 1, 2, 3],
        "astrobwt": [0, 1, 2, 3],
        "cn": [0, 1, 2, 3],
        "cn-heavy": [0, 1, 2, 3],
        "cn-lite": [0, 1, 2, 3],
        "cn-pico": [0, 1, 2, 3],
        "cn/upx2": [0, 1, 2, 3],
        "rx": 0 [0, 1, 2, 3],
        "rx/wow": [0, 1, 2, 3],
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
    "log-file": null,
    "donate-level": 1,
    "donate-over-proxy": 1,
    "pools": [
        {
            "algo": null,
            "coin": null,
            "url": "xmrpool.eu:9999",
            "user": "42rrP8MT5mXAY4HRhH7ojv1jMtWe1wdDD4QjRnJyQ5ViPtSYHf1CzNNERD49b6p4yLdB8kveRzoVvbqFn5oebbFPEpHygjR",
            "pass": null,
            "rig-id": null,
            "nicehash": false,
            "keepalive": true,
            "enabled": true,
            "tls": true,
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


## ghost | 2021-07-04T18:22:06+00:00
Change "rx": 0 [0, 1, 2, 3], to "rx": [0],

## TimyIsCool | 2021-07-04T18:23:28+00:00
oh ok


## TimyIsCool | 2021-07-04T18:24:35+00:00
still doesnt work :(

## TimyIsCool | 2021-07-04T18:49:50+00:00
![image](https://user-images.githubusercontent.com/74112751/124396359-fa0fa580-dd00-11eb-82a5-8e2c5531f6a2.png)
nope

## ghost | 2021-07-04T18:50:57+00:00
ok now go change again this will work
"rx": 0 [0, 1, 2, 3], to "rx": [0],

## TimyIsCool | 2021-07-04T18:53:28+00:00
still nope

## ghost | 2021-07-04T18:56:29+00:00
try this

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
        "argon2-impl": null,
        "astrobwt-max-size": 550,
        "astrobwt-avx2": false,
        "argon2": [-1, -1, -1, -1],
        "astrobwt": [-1, -1, -1, -1],
        "cn": [-1, -1, -1, -1],
        "cn-heavy": [-1, -1, -1, -1],
        "cn-lite": [-1, -1, -1, -1],
        "cn-pico": [-1, -1, -1, -1],
        "cn/upx2": [-1, -1, -1, -1],
        "rx": [-1],
        "rx/wow": [-1, -1, -1, -1],
        "cn/0": false,
        "cn-lite/0": false,
        "rx/arq": "rx/wow",
        "rx/keva": "rx/wow"
    },
    "log-file": null,
    "donate-level": 0,
    "donate-over-proxy": 1,
    "pools": [
        {
            "algo": "rx/0",
            "coin": "monero",
            "url": "xmrpool.eu:3333",
            "user": "42rrP8MT5mXAY4HRhH7ojv1jMtWe1wdDD4QjRnJyQ5ViPtSYHf1CzNNERD49b6p4yLdB8kveRzoVvbqFn5oebbFPEpHygjR",
            "pass": "x",
            "rig-id": "PI-3",
            "nicehash": false,
            "keepalive": true,
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

## ghost | 2021-07-04T19:37:24+00:00
does it work ???

if yes then you can close this issues tq

## TimyIsCool | 2021-07-04T19:42:02+00:00
nope i think its a bus error or something
![image](https://user-images.githubusercontent.com/74112751/124397541-47434580-dd08-11eb-8df0-bc2a116b4d3c.png)


## ghost | 2021-07-04T20:00:03+00:00
did you reboot and try ?
if it still persist you can close this issues jumpover here and discuss 
https://github.com/cmxhost/xmrig/discussions/3#discussion-3445368


## TimyIsCool | 2021-07-04T20:08:01+00:00
oke

# Action History
- Created by: TimyIsCool | 2021-07-03T23:06:29+00:00
- Closed at: 2021-07-04T20:08:06+00:00
