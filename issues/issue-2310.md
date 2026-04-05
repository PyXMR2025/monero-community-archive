---
title: 'read error end of file '
source_url: https://github.com/xmrig/xmrig/issues/2310
author: Tawheedop
assignees: []
labels:
- question
created_at: '2021-04-24T23:47:18+00:00'
updated_at: '2023-09-20T19:57:02+00:00'
type: issue
status: closed
closed_at: '2022-04-03T14:40:15+00:00'
---

# Original Description
i am using xmrig and getting this error in loop
in first line:-  error : "A worker name is required to join pool!", code: -1
in second line :- read error: "end of file"
and this in in loop
although i have worker added in config file and tls is true but still getting this error 
pool using rx.unmineable.com:3333
and to start mining
![Screenshot from 2021-04-25 05-15-01](https://user-images.githubusercontent.com/78700500/115975760-40b88500-a585-11eb-8855-162ff34e0e88.png)
 i type 
1:- ./xmrig -o rx.unmineable.com:3333 -u mywalletaddress -p x -k --coin monero -a rx/0

2:- ./xmrig -o rx.unmineable.com:3333 -a rx -k -u DOGE:mywalletaddress.myworkername #myrefferalcode

# Discussion History
## Spudz76 | 2021-04-25T08:10:37+00:00
Likely they mean to use:
```
      --rig-id=ID               rig identifier for pool-side statistics (needs pool support)
```
So then like:
```
./xmrig -o rx.unmineable.com:3333 --rig-id=myworkername -u yourwalletaddress -p x -k
```
Usually the default of coin:auto works fine so I removed those options.

## xmrig | 2021-04-25T08:22:32+00:00
How to specify the worker name is pool specific, but seems documentation on this pool is pretty clear https://www.unmineable.com/coins/XMR and includes an example for XMRig, I just checked it and all works fine. You can't mine DOGE with XMRig anyway. If you plan mine RandomX and Monero you need a Monero wallet address.
Thank you.

## Tawheedop | 2021-04-25T15:09:31+00:00
Well thanks for help but it actually mines XMR with RandomX algo and pay us
in Doge  well i got an idea with your help And somehow i managed to  run it
successfully and Mine Doge but Hashrate is little bit lower anyways
everything is working perfectly

If you could help me with Hashrate that would be great

Thank you



On Sun, 25 Apr, 2021, 1:40 pm Tony Butler, ***@***.***> wrote:

> Likely they mean to use:
>
>       --rig-id=ID               rig identifier for pool-side statistics (needs pool support)
>
> So then like:
>
> ./xmrig -o rx.unmineable.com:3333 --rig-id=myworkername -u yourwalletaddress -p x -k
>
> Usually the default of coin:auto works fine so I removed those options.
>
> —
> You are receiving this because you authored the thread.
> Reply to this email directly, view it on GitHub
> <https://github.com/xmrig/xmrig/issues/2310#issuecomment-826279851>, or
> unsubscribe
> <https://github.com/notifications/unsubscribe-auth/ASYN7VDNYB3FVZHDZZ7A233TKPFATANCNFSM43QUP3ZA>
> .
>


## Tawheedop | 2021-04-25T15:16:51+00:00
thanks for the help now somehow i am mining doge sucessfully on xmrig with unmineable pool  although hashrate is little bit low but everything is working fine thanks a lot 

## xprimate | 2021-05-20T15:10:52+00:00
> thanks for the help now somehow i am mining doge sucessfully on xmrig with unmineable pool although hashrate is little bit low but everything is working fine thanks a lot

Please how where you able to min DOGE on xmrig , I am facing the same error.
Thanks.

## Zeuserous | 2023-03-31T21:45:55+00:00
i think he is able to mine for DOGE because of the stratums algo and the variations of them if you have your stratum set up correctly with the correct algos it wouldn't be hard to mine DOGE  on a multi currency wallet with xmrig 

meaning that if hes mining on xmrig with a multi lingual wallet hes really mining Monero and the multi currency crypto wallet is catching the multiple coins that are mined from pools that dont specify that their multi currency crypto i

i figured this out because i set up cudos upon that all my trials were errors im slowly figuring out the coding of the miners but upon the errors of my trials i noticed that adding different wallets for different currencies while mining for Ethereum that i was catching different coin currencies through unminable stratums algorand eth btc cudos rupee etc etc so thus he didnt do anything but add the wallet and get his straum correctly inputted we even me us of the miners just havnt caught the currencies because we were to inclined in the currencies we actually wanted to mine 

if im wrong i apologize if im right thank god because i dont like talking out my neck but this is the only theory i can come up with because it has happened to me to 

## thom58 | 2023-09-20T17:11:33+00:00
i don know what i am doing wrong 

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
            "algo": "randomx",
            "coin": "monero",
            "url": "hiddedn",
       "user":"43avgazdkBdQAWTsNgPrcxW7T9xyJKNiXeGBTdYAgNX3XaoY4twYh2uFsA1jycag7QFZ3ns9py6BbQScKwePcEFfMGhJQzK",
            "pass": "miner 1",
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

## SChernykh | 2023-09-20T19:57:02+00:00
What error do you get? "end of file" is just a message XMRig prints when the pool disconnects. The actual error happens before it.

# Action History
- Created by: Tawheedop | 2021-04-24T23:47:18+00:00
- Closed at: 2022-04-03T14:40:15+00:00
