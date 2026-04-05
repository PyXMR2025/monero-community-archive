---
title: Feature Request - Support Stellite's algorithm change from CryptonightV1 to
  a slightly modified variant
source_url: https://github.com/xmrig/xmrig/issues/581
author: stellitedev
assignees: []
labels:
- enhancement
created_at: '2018-04-23T13:33:02+00:00'
updated_at: '2018-05-05T06:45:48+00:00'
type: issue
status: closed
closed_at: '2018-05-05T06:45:48+00:00'
---

# Original Description
# Summary  

After forking to V7 without the presence of nicehash our network was stable, now since that V7 works for all block versions on it we're making a small change to the V7 variant.  

# Details 
You can see the simple modification we've done in [this](https://github.com/stellitecoin/Stellite/tree/V4) branch on our main repo   

# Testing the new variant  
For convenience we have already set up a testnet pool [here](https://testxtl.anypool.net/#), you can use the following address for testing purposes.  

```
Se3EkZfYDpXhaVqyBnAkkjfM1D3RWKeEECMJtAMjCuDE1qaQyEVUqcpXg6b49fCFSeKUD7Xvtzp5nFNPrFrFBVCG1C91AmN8d 
```

Hope you take our request into consideration soon as we plan to implement this onto our mainnet as soon as possible and a good amount of our miners are fond of your miners.  Thank you.

# Discussion History
## xmrig | 2018-04-26T07:21:41+00:00
I will add it as algorithm `cryptonight` variant `xtl` or `cryptonight/xtl`, if you have better name for variant, now is good time for suggestion, but please note numeric variants is reserved for Monero.
Thank you.

## stellitedev | 2018-04-26T09:25:14+00:00
cryptonight_xtl, sounds well and good

## bobbieltd | 2018-04-26T10:29:45+00:00
I hope xmrig will support both syntaxes : algo cryptonight variant xtl and algo crypronight-xtl no variant like IPBC.

## xmrig | 2018-04-26T11:29:26+00:00
@stellitedev Would be nice if Stellite pools will support [extended job object](https://github.com/xmrig/xmrig-proxy/blob/dev/doc/STRATUM_EXT.md#12-extended-job-object) on each job object should added one field `"algo":"cn/xtl"`. Miner will use this hint to set proper variant automatically.
Thank you.

## ahmyi | 2018-04-26T16:18:00+00:00
 https://testnet.xtlpool.com has added the extended job object. This test pool is also using the cryptonight xtl variant changes

## xmrig | 2018-04-26T17:54:15+00:00
I added Stellite support in feature-algo branch https://github.com/xmrig/xmrig/commit/3df99fbcedb0d736e7c16e51b5d988e92518fe6d for CPU miner.
It will be included in next CPU miner/proxy release after all in **Wave 1** will done https://github.com/xmrig/xmrig-proxy/issues/168
GPU miners will be updated later.

@ahmyi just `algo` enough, no need send `variant`. Thank you.

## ahmyi | 2018-04-27T00:26:44+00:00
@xmrig noted. I have made the changes to the pool removing the variant and will test from given branch...

## ahmyi | 2018-04-27T00:40:03+00:00
The new miner looks awesome btw..kudos..shows the correct algo when mining to stratum+tcp://testnet.xtlpool.com:3333 
![image](https://user-images.githubusercontent.com/630603/39338630-84e188dc-49f6-11e8-8e3a-561a53b15df4.png)



## xmrig | 2018-04-27T08:15:11+00:00
My bad, I missed that `table` changed too, but now I'm confused, because `testxtl.anypool.net:3333` successfully accept wrong shares ![image](https://i.imgur.com/ZmGZztm.png) 

## xmrig | 2018-04-27T09:08:15+00:00
@stellitedev Please provide reference hashes, preferably for these 5 inputs https://github.com/xmrig/xmrig/blob/feature-algo/src/crypto/CryptoNight_test.h#L29 but other hashed is ok too. Also look like your changes in table has no effect, so @ahmyi something not ok with your pool.

## hayzamjs | 2018-05-01T13:18:13+00:00
Our team has added a few tests for the second variant in [this](https://github.com/stellitecoin/Stellite/commit/b4710260a9dd746d06617b315aa9d001efe9f783) commit, and one more thing, we hope there will be a way to manually specify the cn/xtl variant for the pools that don't have the auto detect feature too?

## xmrig | 2018-05-03T15:25:14+00:00
Thank you for test hashes. Of course variant can set manually, I added documentation how it works https://github.com/xmrig/xmrig/blob/dev/doc/ALGORITHMS.md
Also I added block version check, so variant `xtl` will work after new version of miner released. No need change it after the fork.

# Action History
- Created by: stellitedev | 2018-04-23T13:33:02+00:00
- Closed at: 2018-05-05T06:45:48+00:00
