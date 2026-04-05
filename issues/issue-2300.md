---
title: 'XMRig 6.12.0  READ ERROR: "end of file"'
source_url: https://github.com/xmrig/xmrig/issues/2300
author: Mcafee-in-trubble
assignees: []
labels:
- question
created_at: '2021-04-22T20:45:26+00:00'
updated_at: '2024-05-09T11:00:54+00:00'
type: issue
status: closed
closed_at: '2021-04-25T08:26:22+00:00'
---

# Original Description
**Describe the bug**

If I change the preset pool (donate.v2.xmrig.com:3333) I get READ ERROR: "end of file"
____________________________________________________________________________________________________________________________________
**To Reproduce**

1). I download xmrig-6.12.0-msvc-win64.zip (I´m on Windows 10 PRO 64bit) from https://github.com/xmrig/xmrig/releases

2). When I extract files the config looks like this = PIC-01

3). I want it to look like this= PIC-02

(It works with my wallet adress and everything else).
____________________________________________________________________________________________________________________________________
**Expected behavior**

4). If I run XMRig.exe right after unziped it works fine. I can put in my wallet address and all, but if i change the pool it give the Read Error: "end of file"...

5). Only way I can get 6.12.0 to work is if i copy/paste the old 6.11 config file into 6.12.0. I shows the new algo rx/arq ( but still I would like it to work "outta the box" ... I have the "Fear-Of-Missing-Out" some better settings or stuff.... 

6). Also when i copy old config file from 6.11 into 6.12 it uses the new algo rx/arq....(it dont do that if i just run the preset pool (donate.v2.xmrig.com:3333)...then it goes for rx/0...maybe thats the request from pool I dont know... just wanted to mention that too.
____________________________________________________________________________________________________________________________________
**Required data**

7). Miner log/screenshot of Read Error: "end of file" = PIC-03

8). A screenshot of XMRig 6.12.0 running with (donate.v2.xmrig.com:3333) pool settings = FILE-01-rar

9). Config file or command line (without wallets) = PIC-02
 
10).OS = Windows 10 PRO 64 build 20H2. Integrated chip GPU HD4000 (Dedicated GPU burned of years ago, but have not been a problem for 6.11.0 XMRig)....guess I miss out of 4-500 h/s (The laptop is +10 years old so the hash is what it is....nothing fancy....)
____________________________________________________________________________________________________________________________________
**Additional context**

The only "fix" I could come up with was copy/paste old 6.11.0 config into 6.12.0 (it finds the new Algo rx/arq but I really want it to work outta the box with no patching of old files....

![PIC-01](https://user-images.githubusercontent.com/83037231/115782198-ae18ba00-a3bb-11eb-93ba-2585c3c14bb9.jpg)

![PIC-02](https://user-images.githubusercontent.com/83037231/115782200-aeb15080-a3bb-11eb-87d9-8c0089f45cd3.jpg)

![PIC-03](https://user-images.githubusercontent.com/83037231/115782202-aeb15080-a3bb-11eb-875b-9db79d5a413b.jpg)

![PIC-04](https://user-images.githubusercontent.com/83037231/115782203-af49e700-a3bb-11eb-8548-26819bccee1a.jpg)

[config.zip](https://github.com/xmrig/xmrig/files/6361123/config.zip)


# Discussion History
## snipeTR | 2021-04-22T20:49:44+00:00
change TLS settings
![image](https://user-images.githubusercontent.com/31975916/115783327-67c85880-a3c5-11eb-8afc-6d110ec55533.png)


## Mcafee-in-trubble | 2021-04-22T21:00:06+00:00
TLS: true, = it works perfect now !!!!!

You FIXED IT!!!!!! Many thx hahahaha I´m gonna be rich !...Diamonds! Fur Coat! Champagne!



## silverscrub | 2021-10-22T06:09:27+00:00
Hey,

I am having the same issue. Already turned the tls options in pools to true but doesnt work.

Error CL_INVALID_OPERATION when calling clGetDeviceInfo, param 0x4037
 * POOL 1   etchash.unmineable.com:13333 algo auto
[2021-10-22 01:05:57.072]  net      etchash.unmineable.com:13333 read error: "end of file"

here's what i get. If the tls is turned to false, then I receive no job request from the server at all




## SChernykh | 2021-10-22T06:12:39+00:00
xmrig doesn't support etchash algorithm.

## silverscrub | 2021-10-22T06:14:08+00:00
what about kawpow?

## Mr-Zer0 | 2021-12-12T09:44:40+00:00
I am facing the same issue.

 net      asia1-etc.ethermine.org:4444 read error: "end of file"

Here is my config.

```json
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
        "argon2": [0, 2, 4, 6, 5, 7],
        "astrobwt": [0, 1, 2, 3, 4, 5, 6, 7],
        "cn": [
            [1, 0],
            [1, 2],
            [1, 4]
        ],
        "cn-heavy": [
            [1, 0],
            [1, 2]
        ],
        "cn-lite": [
            [1, 0],
            [1, 2],
            [1, 4],
            [1, 6],
            [1, 5],
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
        "cn/upx2": [
            [2, 0],
            [2, 1],
            [2, 2],
            [2, 3],
            [2, 4],
            [2, 5],
            [2, 6],
            [2, 7]
        ],
        "ghostrider": [
            [8, 0],
            [8, 2],
            [8, 4]
        ],
        "rx": [0, 2, 4],
        "rx/arq": [0, 1, 2, 3, 4, 5, 6, 7],
        "rx/wow": [0, 2, 4, 6, 5, 7],
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
            "url": "asia1-etc.ethermine.org:4444",
            "user": "0x2076F1bDb316a9436736D23d58D3970231c1cB17",
            "pass": "",
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
        "enabled": true,
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

## fisherbait | 2022-01-23T22:58:36+00:00
I fixed it by running it with `./xmrig -o pool.com:port -u wallet_address -p pass`, dropping the `-k --tls` from the command I got from the xmrig configuration wizzard.

## izzarzn | 2022-08-13T19:28:23+00:00
![Screenshot 2022-08-14 at 12 57 02 AM](https://user-images.githubusercontent.com/65058286/184508039-c2baac68-c778-47c1-a1d8-58adcb34dfa2.png)

I'm facing this issue :
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
        "argon2": [0, 2, 3],
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
            "url": "rx.unmineable.com:13333",
            "user": "MATIC:0x68c5b8CAa86B5E32645A33Fe41AE6d132A889FAc.izzarzn",
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

## SChernykh | 2022-08-14T07:31:16+00:00
Most likely unmineable pool wasn't ready for the Monero fork, so you have to switch to another pool until they fix it.

## flatounet | 2024-05-09T02:40:57+00:00
i got same error here , 
using bat file for config   no error but i have failled MRS MOD ,
when i start exe file i dont have MRS error but : "end of file" ...
post are from 2022 we are 2024 ... 

## SChernykh | 2024-05-09T06:15:03+00:00
> post are from 2022 we are 2024 ...

Time to fix your config in 2024. This is not an XMRig error, you're just connecting to a wrong URL.

## flatounet | 2024-05-09T07:21:16+00:00
witch url ?
it's the config from bat file  and working on bat file ...
executing the exe file got error when i put no information / url ... 

## SChernykh | 2024-05-09T08:42:01+00:00
The URL in your bat file. You're connecting to a wrong port in your pool, or to a pool that doesn't work now or is mining a different coin.

## flatounet | 2024-05-09T10:46:15+00:00
cd /d "%~dp0"
xmrig.exe -o myipv4:18081 -a rx/0 -u myxmrwallet --daemon --cuda
pause

myipv4:18081 is a node accessible from internet - with bat file it working
( same i tryed w localy ip 192.168.1.20 is working to w bat file )
in config json i dont see : rx/0 
i see "pools" algo null , coin null  ;may be have to specify rx/0 here ?
exe have admin right and floder was "exclude" from AV
so np this side, sorry im a 0
( i got i7 127000gf+3090 ( cuda enabled 11.8 12.3 6.21.1 ))

thx for your help 

## SChernykh | 2024-05-09T11:00:20+00:00
You should have `"coin":"monero"` and `"daemon":true` in pool section of config.json. I'm on my phone so typing from memory, so the exact parameters can be different. Better check https://xmrig.com/docs/miner

# Action History
- Created by: Mcafee-in-trubble | 2021-04-22T20:45:26+00:00
- Closed at: 2021-04-25T08:26:22+00:00
