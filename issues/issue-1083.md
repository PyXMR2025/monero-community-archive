---
title: Incompatible/disabled algorithm "cn/0" detected, reconnect
source_url: https://github.com/xmrig/xmrig/issues/1083
author: seanwhe
assignees: []
labels:
- question
created_at: '2019-07-29T13:13:41+00:00'
updated_at: '2019-07-30T02:50:33+00:00'
type: issue
status: closed
closed_at: '2019-07-30T02:50:33+00:00'
---

# Original Description
$ uname -a
Linux sean-work-wks 4.15.0-55-generic #60-Ubuntu SMP Tue Jul 2 18:22:20 UTC 2019 x86_64 x86_64 x86_64 GNU/Linux

````````````````
$ xmrig -V
XMRig 2.99.2-beta
 built on Jul 29 2019 with GCC 7.4.0
 features: 64-bit AES

libuv/1.18.0
OpenSSL/1.1.1
hwloc/1

```````````
When starting from config file
$./xmrig --config=config.json
The following errors are noticed

[2019-07-29 14:59:12.289] [pool.supportxmr.com:5555] Incompatible/disabled algorithm "cn/0" detected, reconnect
[2019-07-29 14:59:12.289] [pool.supportxmr.com:5555] login error code: 6

when the following is present:
``````````````
$ cat config.json 
{
...
	"cn/0": false,
        "cn-lite/0": false
...
   
``````````
Removing the above so that config looks as follows produces no error

``````````
$./xmrig --config=config.json
``````````
$ cat config.json 
{
    "api": {
        "id": null,
        "worker-id": null
    },
    "http": {
        "enabled": true,
        "host": "192.168.1.11",
        "port": 8080,
        "access-token": null,
        "restricted": false
    },
    "autosave": true,
    "background": false,
    "colors": true,
    "randomx": {
        "init": -1,
        "numa": true
    },
    "cpu": {
        "enabled": true,
        "huge-pages": true,
        "hw-aes": null,
        "priority": null,
        "asm": true,
        "cn": [
            0,
            1,
	    2
        ]
    },
    "donate-level": 5,
    "donate-over-proxy": 1,
    "log-file": null,
    "pools": [
        {
            "algo": "cryptonight",
            "url": "pool.supportxmr.com:5555",
            "user": "854sqm2Cm4TB2XgPHWqSPSbnFAe3SMzdEDzZHpukQ8NHBPFropbnkFmEKiZPgwjMFC9PTjaFscR2UU6ZwFCqJzGMUiZVbTM",
            "pass": "wks-jhb-lin-11:user@example.com",
            "rig-id": "wks-jhb-lin-11",
            "nicehash": true,
            "keepalive": true,
            "enabled": true,
            "tls": false,
            "tls-fingerprint": null,
            "daemon": false
        }
    ],
    "print-time": 30,
    "retries": 5,
    "retry-pause": 5,
    "syslog": false,
    "user-agent": "null",
    "watch": true
}
`````````````````````



# Discussion History
## xmrig | 2019-07-29T13:55:31+00:00
Use `"algo": "cn/r",`, `cn/0` disabled by default, because it already dead for CPU/GPU mining.
Thank you.

## looplife55 | 2019-07-29T14:05:35+00:00
seanwhe bro how u upgrade xmrig to latest version in linux. 

## looplife55 | 2019-07-29T14:09:55+00:00
I try all get pull,get fetch,get merge but it still says it's running 2.5.3. The most recent version of XMRig,
I've rebooted the computer and logged out/in. I also tried git fetch and git merge. It tells me I'm using the most recent version.
How do I get XMRig to upgrade to v2.99.0-beta

## seanwhe | 2019-07-29T20:11:40+00:00
> I try all get pull,get fetch,get merge but it still says it's running 2.5.3. The most recent version of XMRig,
> I've rebooted the computer and logged out/in. I also tried git fetch and git merge. It tells me I'm using the most recent version.
> How do I get XMRig to upgrade to v2.99.0-beta

git checkout tags/v2.99.0 -beta

## seanwhe | 2019-07-29T20:13:26+00:00
> Use `"algo": "cn/r",`, `cn/0` disabled by default, because it already dead for CPU/GPU mining.
> Thank you.

Then the config generated when started is inserting but not removing and not updating

## SomethingGettingWrong | 2019-07-29T23:45:16+00:00

![image](https://user-images.githubusercontent.com/36722911/62090040-fdef3f00-b230-11e9-80ac-9eff93dce4d7.png)


same for me in loki running from batch file as follows

@echo off
xmrig.exe -a rx/loki --donate-level 5 -o loki.miner.rocks:5005 -u YOUR_WALLET_ADDRESS -p w=Rig1 -k -o loki.miner.rocks:5007 -u YOUR_WALLET_ADDRESS -p w=Rig1 -k
pause

## SomethingGettingWrong | 2019-07-29T23:48:15+00:00
2.99.1 works 

![image](https://user-images.githubusercontent.com/36722911/62090144-65a58a00-b231-11e9-8802-1d94018dbd1e.png)

with same batch file


## xmrig | 2019-07-30T00:37:36+00:00
Autoconifg for AMD FX CPUs currently broken, please check #1082 
Thank you.

## xmrig | 2019-07-30T02:50:33+00:00
v2.99.3-beta released https://github.com/xmrig/xmrig/releases/tag/v2.99.3-beta

# Action History
- Created by: seanwhe | 2019-07-29T13:13:41+00:00
- Closed at: 2019-07-30T02:50:33+00:00
