---
title: xmrig-5.0.0 crash with windows 10 randomx rx/0 ryzen 1700X
source_url: https://github.com/xmrig/xmrig/issues/1297
author: maxfreemax
assignees: []
labels:
- bug
- opcache
created_at: '2019-11-17T07:33:31+00:00'
updated_at: '2020-06-02T14:34:12+00:00'
type: issue
status: closed
closed_at: '2020-06-02T14:34:12+00:00'
---

# Original Description
I try test on randomx, but xmrig 5.0.0 crash after few seconds. 
I have windows 10 and ryzen 1700X

 note , all seem  ok with cn/0 


last screen just before crash
![xmrig](https://user-images.githubusercontent.com/44138963/69004447-aaa21900-0913-11ea-9daf-a0a028c1264b.png)


config.json:
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
    "randomx": {
        "init": -1,
        "numa": false
    },
    "cpu": {
        "enabled": true,
        "huge-pages": true,
        "hw-aes": null,
        "priority": null,
        "memory-pool": false,
        "asm": true,
        "argon2-impl": null,
        "argon2": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
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
            [1, 8],
            [1, 10]
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
        "cn/gpu": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
        "rx": [0, 2, 4, 6, 8, 10, 12, 14],
        "rx/wow": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
        "cn/0": false,
        "cn-lite/0": false,
        "rx/arq": "rx/wow"
    },
    "opencl": {
        "enabled": false,
        "cache": true,
        "loader": null,
        "platform": "AMD",
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
    "donate-level": 5,
    "donate-over-proxy": 1,
    "log-file": null,
    "pools": [
        {
            "algo": "rx/0",
            "coin": null,
            "url": "randomx-benchmark.xmrig.com:7777",
            "user": "BENTCHMARK.TEST",
            "pass": "",
            "rig-id": null,
            "nicehash": false,
            "keepalive": false,
            "enabled": true,
            "tls": false,
            "tls-fingerprint": null,
            "daemon": false,
            "self-select": null
        }
    ],
    "print-time": 60,
    "health-print-time": 60,
    "retries": 5,
    "retry-pause": 5,
    "syslog": false,
    "user-agent": null,
    "watch": true
}

# Discussion History
## ivarsdzalbs | 2019-11-22T13:54:51+00:00
Have exact same problem, can reproduce it on both 1700 and 1700x cpus. 

## SChernykh | 2019-11-25T16:29:53+00:00
Can you try https://github.com/SChernykh/xmrig/tree/ryzen-fix ? Compile it from source and check if it crashes.

## theshadowpeople | 2019-11-25T17:14:56+00:00
It doesn't work too

## SChernykh | 2019-11-25T17:19:43+00:00
We'll keep looking for a workaround then.

## maxfreemax | 2019-11-25T18:12:53+00:00
it crash after 1 minute. (note algo is rx/wow)

![xmrig_wow](https://user-images.githubusercontent.com/44138963/69566415-55bb6e00-0fb7-11ea-85ac-7fef68c58b14.png)



## DiamondLovesYou | 2019-12-01T01:11:14+00:00
@maxfreemax mind trying PR #1348 ?

## Possums | 2019-12-01T01:32:29+00:00
Tried PR #1348, still crashing on Epyc 7551 engineering sample CPU.

## kenshirothefist | 2019-12-01T14:16:51+00:00
Same issue here, can reproduce it on 1700x.

## Samoflan | 2019-12-01T15:34:02+00:00
I am having the issue on my 1700x. Keeps crashing after less then a minute.

## maxfreemax | 2019-12-01T22:04:57+00:00
I have update my bios. no change.
after I have install  this:
https://www.amd.com/en/support/cpu/amd-ryzen-processors/amd-ryzen-7-desktop-processors/amd-ryzen-7-1700x

after multi start of xmrig (v5.0.1) and multi crash, xmrig finish to be stable (actually 12 hours ok at 4200h/s).

after each reboot windows 10, i have to do the same multi start of xmrig(and multi crash) to have a stable xmrig.

i have not try yet proposal  #1348




## xmrig | 2019-12-01T22:24:44+00:00
Disabling opcache in BIOS should fix the issue, please verify https://github.com/xmrig/xmrig/pull/1348#issuecomment-560122919

## maxfreemax | 2019-12-01T23:18:11+00:00
as suggested (proposal #1348) i have disabled opcache (auto --> disabled) on motherboard BIOS
xmrig start with no crash at the first time

thanks.



## kenshirothefist | 2019-12-02T08:02:45+00:00
I can confirm disabling opcache resolves the issue, but then again I only get 4650 H/s (1700X @4.0GHz), therefore I guess there is a 5-10% performance penalty when disabling opcache.

## kenshirothefist | 2019-12-06T20:00:11+00:00
I wouldn't consider this as closed ... disabling opcache is only a (bad) workaround since it significantly impacts performance ...

## maxfreemax | 2019-12-06T22:02:49+00:00
ok i reopen

## kimxilxyong | 2019-12-07T11:18:54+00:00
Opcache disabled did not help. Segfault on 1700x after a few seconds

## tevador | 2019-12-07T13:52:18+00:00
> disabling opcache is only a (bad) workaround since it significantly impacts performance

It's a hardware bug, so I don't think there is a better workaround than this. It seems that AMD has been replacing the faulty processors in some cases: https://www.reddit.com/r/Amd/comments/c3377v/ryzen_1700_segfault_rma/

## xmrig | 2019-12-22T19:37:15+00:00
Try recent version with `"wrmsr": ["0xc0011020:0x0", "0xc0011021:0x60", "0xc0011022:0x510000", "0xc001102b:0x1808cc16"]` more details about MSR https://xmrig.com/docs/miner/randomx-optimization-guide/msr
Thank you.

## SChernykh | 2019-12-30T10:18:49+00:00
@maxfreemax XMRig 5.5.0 has a workaround for 1st gen Ryzen/Threadripper/EPYC crashes, you should be able to mine even with enabled Opcache.

# Action History
- Created by: maxfreemax | 2019-11-17T07:33:31+00:00
- Closed at: 2020-06-02T14:34:12+00:00
