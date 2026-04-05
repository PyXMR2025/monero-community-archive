---
title: i am getting connection error when opening miner. I have pinged the servers
  and that is ok so must be my config? I am quite new to this mining software so I
  am running out of ideas and my research is not finding any help
source_url: https://github.com/xmrig/xmrig/issues/2180
author: mnm279
assignees: []
labels: []
created_at: '2021-03-13T10:47:01+00:00'
updated_at: '2021-04-12T13:58:53+00:00'
type: issue
status: closed
closed_at: '2021-04-12T13:58:53+00:00'
---

# Original Description
**Describe the bug**
A clear and concise description of what the bug is.

**To Reproduce**
Steps to reproduce the behavior.

**Expected behavior**
A clear and concise description of what you expected to happen.

**Required data**
 - Miner log as text or screenshot
 - Config file or command line (without wallets)
 - OS: [e.g. Windows]
 - For GPU related issues: information about GPUs and driver version.

**Additional context**
Add any other context about the problem here.


# Discussion History
## mnm279 | 2021-03-13T10:47:28+00:00
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
            [1, 15]
        ],
        "cn-heavy": [
            [1, 0],
            [1, 2],
            [1, 4],
            [1, 6],
            [1, 8],
            [1, 10],
            [1, 12],
            [1, 14]
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
        "rx": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
        "rx/wow": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
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
            "user": "84WDVV2QmeU1A1gjdFtVdjYZZGqoUB89wCVrTyptAfbwgrayvw6vuUoE4NwxrvbTzsaT8J41d1H1gdFBTV5E7vGM8ujo9CG",
            "pass": null,
            "rig-id": null,
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
    "user-agent": null,
    "verbose": 0,
    "watch": true,
    "pause-on-battery": false,
    "pause-on-active": false
}


## mnm279 | 2021-03-13T10:47:53+00:00
that is my config.json


## mnm279 | 2021-03-13T10:50:09+00:00
os is windows 10 64 bit

![image](https://user-images.githubusercontent.com/72933544/111027715-dd65ff80-83e9-11eb-9203-7aa9df0d6506.png)


## SChernykh | 2021-03-13T10:52:01+00:00
> Port: 9999
 Starting Difficulty: 50000
 Description: SSL for Claymore > 9.7

Why are you trying to connect to Claymore-specific port with XMRig? Use port 7777

## mnm279 | 2021-03-13T10:56:27+00:00
do you mean "url" xmrpoll.eu:9999 to 7777? sorry i am vew to this. it was working yesterday

## mnm279 | 2021-03-13T10:56:57+00:00
*new


## xmrig | 2021-03-13T11:01:53+00:00
It is a network issue, try open http://xmrpool.eu:9999/ and https://xmrpool.eu:9999/ in your browser, if it also timeouts, nothing can be done on the miner side.
Thank you.

## mnm279 | 2021-03-13T11:17:39+00:00
i have four other miners running fine but when i click your links the message reads :"the server xmrpool.eu:9999 is online but is not responding to connection requests." so does that mean my config is ok and there is an issue that cannot be resolved as there is some other issue out of my control?

## mnm279 | 2021-03-13T11:18:54+00:00
rigs running xmr through hiveos seem unaffected. they are running great

## mnm279 | 2021-03-13T12:27:12+00:00
so its not something on my end as everything has been reset and re-configured. is xmrpool.eu having some issues?

## mnm279 | 2021-03-13T13:20:10+00:00
ok so i cant even view my xmrpool.eu wallet earnings either. so the pool must have an issue with something.

## mnm279 | 2021-03-13T13:29:20+00:00
authenticity of data could not be verified. and that is on tor browser. it does not matter how i try to connect with anything. it just wont connect on web or in miner but i can ping them


## mnm279 | 2021-03-13T14:15:23+00:00
all miners now down. you seem to have a big problem at the moment. ill watch pool status pages and wait. thamks for your earlier help. I now know I have not done anything wrong in config at least. hope it is sorted soon.


## Lonnegan | 2021-03-14T00:37:41+00:00
xmrpool.eu doesn't support algo auto detection. You have to change

"coin": null,

to

"coin": "monero",

in your config file, in addition to the port (7777 instead of 9999)

But appart from that, something seems to be wrong with that pool atm:

![xmrpool](https://user-images.githubusercontent.com/60088495/111053658-dbda1d00-8465-11eb-8ca3-e96844a000f2.png)


## DeeDeeRanged | 2021-03-31T02:44:46+00:00
xmrpool.eu does support algo auto automatically see my command line:
sudo ./xmrig --api-worker-id dranged --http-enabled -o xmrpool.eu:9999 -u whatever -k --tls
I don't use a config.

# Action History
- Created by: mnm279 | 2021-03-13T10:47:01+00:00
- Closed at: 2021-04-12T13:58:53+00:00
