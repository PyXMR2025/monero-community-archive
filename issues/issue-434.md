---
title: Monero v7 PoW change status
source_url: https://github.com/xmrig/xmrig/issues/434
author: xmrig
assignees:
- xmrig
labels:
- enhancement
created_at: '2018-03-08T18:28:44+00:00'
updated_at: '2018-08-20T09:30:22+00:00'
type: issue
status: closed
closed_at: '2018-03-29T10:14:05+00:00'
---

# Original Description
Monero will [change PoW](https://getmonero.org/2018/02/11/PoW-change-and-key-reuse.html) on April 6, that means Monero `cryptonight` will not compatible with other `cryptonight` based coins. Also small hashrate drop expected.

**You will require update miners to continue mine Monero.** As soon as version 2.5 released you can update miners don't need do it on April 6, new version fully compatible with current Monero network.

New miner also can be continue use with other `cryptonight` coins without changes, I checked `ETN`, `SUMO` and `ITNS`. If you get compatible issues please report it, also you have 2 ways to disable new algorithm:

1. Use new option `"variant": 0` or `--variant 0` on each pool. Example:
```json
        {
            "url": "YOUR_POOL:3333",
            "user": "YOUR_WALLET",
            "pass": "x",
            "keepalive": true,
            "nicehash": false,
            "variant": 0
        },
```
2. Use [xmrig-proxy](https://github.com/xmrig/xmrig-proxy) to override `variant` option, in proxy config for each pool set `variant` option. This option will be supported in proxy v2.5, this version currently available in [dev](https://github.com/xmrig/xmrig-proxy/tree/dev) branch. Example:
```json
        {
            "url": "YOUR_POOL:3333",
            "user": "YOUR_WALLET",
            "pass": "x",
            "coin": "SUMO",
            "variant": 0
        },
```

####  Current progress:
- [x] Implement changes in [xmrig](https://github.com/xmrig/xmrig/commits/dev).
  - [x] AEON.
- [x] Implement changes in [xmrig-amd](https://github.com/xmrig/xmrig-amd/commits/dev).
  - [x] AEON.
- [x] Implement changes in [xmrig-nvidia](https://github.com/xmrig/xmrig-nvidia/commits/dev).
  - [x] AEON.
- [x] Implement changes in [classic xmrig](https://github.com/xmrig/xmrig/commits/classic) (C version).
- [x] Add new options to https://config.xmrig.com
- [x] Release v2.5
- [x] Proxy release v2.5



# Discussion History
## umiiii | 2018-03-09T03:35:14+00:00
Is that means when I use xmrig and xmrig-proxy v2.5 before March 28 and it will automatically changed its mining strategy when March 28 Monero hard fork come and after that?

## xmrig | 2018-03-09T05:27:07+00:00
That right, xmrig v2.5 will work before and after hard fork without changes, algorithm will change automatically no need do anything. Actually proxy update is not mandatory, old version continue work, but in v2.5 many new features added.
Thank you.

## 2010phenix | 2018-03-09T12:21:47+00:00
and that all be nice.... i think need some love and to classic C miner too ;)

## xmrig | 2018-03-09T12:33:06+00:00
Added classic miner to checklist.
Thank you.

## xmrig | 2018-03-11T14:29:45+00:00
Monero v7 implemented in all miners (in dev branches currently) and in classic C miner (classic branch).

## xmrig | 2018-03-12T07:26:13+00:00
Release delayed, AEON will change PoW too https://github.com/xmrig/xmrig/pull/426
Thank you.

## xmrig | 2018-03-12T15:54:26+00:00
Instead of option `monero` will be added more flexible option `variant`.
Possible values:
 - `-1`  Autodetect, should work fine with Monero, AEON and others coins until their network not updated to v7. Used by default.
- `0` Force use original  `cryptonight` algorithm.
- `1` Force use new Monero v1 PoW.

Please note, this option applied on each pool separately. When use xmrig-proxy, miner can switch between `0` and `1` on each job. 

## tarris034 | 2018-03-13T16:56:52+00:00
How often will the new version check which algo to use ? on every work ? what will be the overhead of this checking procedure ? will it have impact on the hashrate ? 

## xmrig | 2018-03-13T18:44:58+00:00
Depends of miner, on each platform checking is different, but overhead for this is near zero. When use old algorithm hashrate should be same as before. But new algorithm itself is a few % slower.
Thank you.

## jsonnentag | 2018-03-14T00:20:08+00:00
Will mining for MoneroV option be added as well?

## xmrig | 2018-03-14T10:32:28+00:00
I don't know what will be use MoneroV, it they will use new PoW with same version with Monero, anything should work fine.
Thank you.

## xmrig | 2018-03-14T21:41:37+00:00
[GRAFT](https://www.graft.network/) already use v7 network, but original algorithm, so you must use option `"variant": 0` on each GRAFT pool. Algorithm detection will not work with this coin.

Example:
```json
{
    "url": "pool.graft.hashvault.pro:7777",
    "user": "WALLET_ADDRESS",
    "pass": "x",
    "keepalive": true,
    "nicehash": false,
    "variant": 0
},
```

## serisman | 2018-03-14T23:51:25+00:00
Can you build/push a new version of your docker image (https://hub.docker.com/r/xmrig/xmrig/) that contains these changes?

## xmrig | 2018-03-14T23:56:23+00:00
It not my docker image, I'm not related to https://hub.docker.com/r/xmrig/ in any way.
Thank you.

## serisman | 2018-03-14T23:58:24+00:00
Interesting.  Thanks for the reply.  I assumed it was yours based on the name.  I'll look around for a suitable replacement or create one.

## sebseb7 | 2018-03-15T15:21:15+00:00
it there a v7 testpool already?

## xmrig | 2018-03-15T15:23:55+00:00
http://killallasics.moneroworld.com/

## sebseb7 | 2018-03-15T16:22:27+00:00
and is there a testnet with v7 also?

## sterkederk | 2018-03-15T16:58:46+00:00
On testpool mining works, but my hashrate dropped by half? 

## xmrig | 2018-03-15T19:24:57+00:00
@sebseb7 Not sure, latest Monero daemon was use v8 when I last check it, mentioned pool use v7.
@sterkederk Please open separated issue with proper details about your hardware, old and new hashrate.
Thank you.

## oliverw | 2018-03-15T19:30:30+00:00
@xmrig May I ask where you got the information about the necessary changes to the PoW algorithm to support V7?

## xmrig | 2018-03-15T19:34:55+00:00
Reference implementation was submitted by @vtnerd via pull request #426
Thank you.

## oliverw | 2018-03-15T19:41:50+00:00
@xmrig Thanks a lot!

## 2010phenix | 2018-03-15T23:06:54+00:00
@xmrig thx for some love to classic one...
 Implement changes in classic xmrig (C version).

they to have autodetect V7 version already or only first version support from Mar 11?

## xmrig | 2018-03-15T23:16:42+00:00
Since this commit https://github.com/xmrig/xmrig/commit/33944595a2049427a5f19d18e1a475485727d927 V7 supported, autodetect work too.

## guigeddos | 2018-03-16T08:26:38+00:00
@xmrig  Why some of them have 2 CPU. Xmrig can only recognize and read 1 CPU. How to solve this. Stak mining tools can be identified. But xmrig can't recognize it. There are a lot of problems. Is there a way to solve it

## nssy | 2018-03-16T13:16:29+00:00
Works fine for me on the testpool. No noticeable change in Hash Rate. Thanks for patching things up early.

## 2010phenix | 2018-03-16T13:17:34+00:00
@guigeddos i think it can be next to fix... look on https://github.com/xmrig/xmrig/issues/86

@xmrig thx, add by hands in few day and try to check

## guigeddos | 2018-03-16T14:22:08+00:00
![tim 20180316221500](https://user-images.githubusercontent.com/35347058/37525610-4f35c90e-2968-11e8-9fd5-a0d84f6607ed.png)
@xmrig  2.5.0   This is the case? What's the matter

## xmrig | 2018-03-16T17:50:15+00:00
@guigeddos such errors can happen by a lot of reasons, includes troubles with pool. Not issue in this case.
Thank you.

## Sqzsoft | 2018-03-17T03:52:39+00:00
Is that possible to include binary file in the new release for both armv7 and armv8? (rep to 32bit and 64bit)

## xmrig | 2018-03-17T04:00:40+00:00
Binary ARM build is complicated, different platforms and many different hardware especially for ARMv7, build from source for target platform is not too hard.
Thank you.

## xmrig | 2018-03-19T00:07:54+00:00
https://github.com/monero-project/monero/pull/3424 PoW change delayed to around April 6.
Thank you.

## xmrig | 2018-03-29T10:14:05+00:00
I close this issue, use #482 for future details.
Thank you.

## xmrig | 2018-04-03T08:47:28+00:00
If you have plans to mine Monero or other coins in list #482 you should update miner.
Thank you.

## svoutlokk | 2018-05-07T01:14:35+00:00
qual versão do Xmring esta atualizado com a versão cryptonightv7? 

## globeone | 2018-08-19T22:47:12+00:00
The current master is still 2.4 and many pools are demanding 2.5 because of this bug report. would it be possible to please edit the bug report to say 2.4 as this change was already performed in 2.3
![schermafdruk van 2018-08-20 00-46-38](https://user-images.githubusercontent.com/10052587/44313990-90c50e00-a412-11e8-9c39-96d5c83bcc5b.png)


## xmrig | 2018-08-20T09:30:22+00:00
@globeone but current master is v2.6.4 https://github.com/xmrig/xmrig/blob/master/src/version.h#L30
Thank you.

# Action History
- Created by: xmrig | 2018-03-08T18:28:44+00:00
- Closed at: 2018-03-29T10:14:05+00:00
