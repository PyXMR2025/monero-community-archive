---
title: asic resistant and compatibility for sumo algo
source_url: https://github.com/xmrig/xmrig/issues/476
author: 2010phenix
assignees:
- xmrig
labels:
- enhancement
created_at: '2018-03-25T13:14:08+00:00'
updated_at: '2018-04-19T14:12:43+00:00'
type: issue
status: closed
closed_at: '2018-04-19T14:12:43+00:00'
---

# Original Description
for few day not have much time.. anyone test already?
link for who registered: https://bitcointalk.org/index.php?topic=1905086.msg33080011#msg33080011

-- cut --
Cryptonight-heavy, Sumokoin's asic resistant algo is finalised and under testing. 
Feel free to test/report and produce patches for miners other than xmr-stak. 
Feedback would be much appreciated.
Exact fork block height and writeup will follow soon
https://github.com/curie-kief/pow_test
-- cut --

and why only xmr-stak....

# Discussion History
## xmrig | 2018-03-25T13:27:45+00:00
fireice-uk just released new version with cryptonight-heavy support, so they just waited when Monero team tags the release. Welcome to PoW war.

## ghost | 2018-03-25T21:30:10+00:00
Who waited for what mate?

## bluemelatonin | 2018-03-25T21:38:09+00:00
I hope that XMRIG will be compatible with sumo after fork. it's planned ?

## ghost | 2018-03-25T21:47:27+00:00
Will it be @xmrig?

## curie-kief | 2018-03-26T01:31:06+00:00
We are not looking to go to war with anyone @xmrig . The reference implementation is public https://github.com/curie-kief/pow_test If you want to implement it and need help, we would be delighted to help you.

## ProfDD | 2018-03-26T02:02:56+00:00
xmrig could also update for SUMO's update? Thanks

## xmrig | 2018-03-26T02:16:27+00:00
I will support it, but can't tell when, I need some time. Some big changes scheduled for v2.6 and I don't like delay it again. Anyway good to know about 4MB scratchpad now, before start implementing other things.

* When is estimated date of the fork?
* Will be nice have test pool like this http://killallasics.moneroworld.com/ before the fork.

Thank you.

## sergneo | 2018-03-26T06:16:43+00:00
@xmrig To test SUMO is better on the pool https://sumokoin.hashvault.pro this is the only quick pool.
on the official sumo tweeter https://twitter.com/sumokoin reference specified https://www.reddit.com/r/sumokoin/comments/83w61w/regarding_cryptonight_asics/

> [–]cryptowarlock[S] 1 очко 2 дня назад 
> 
> the date of the fork is not determined yet. It will be within the following weeks it will be announced once determined. Yes sumo easy miner will be updated


## xmrig | 2018-03-30T15:43:38+00:00
https://github.com/sumoprojects/sumokoin/commit/57daf6365b6c981bf53589bb85cfe0ebcda0eed7 April 4, so disappointing, secretly implement new PoW, not give time for others. 

## ghost | 2018-03-30T15:54:47+00:00
How is the implementation secret? We said it will happen soon (after testing is done). It was clear we will fork soon, since the issue allowed us no bigger delay. We announced the final date today:

Fork Block Height set at 117600 (on abt April 4th). Binaries will be released soon. Following the fork the light Qt GUI wallet will be released featuring remote node connection ability (it is ready for release). Web wallet is expected to be released soon as well. #sumokoin $sumo

## xmrig | 2018-03-30T16:14:05+00:00
Announce of new PoW and xmr-stak 2.3 with fully finished cryptonight-heavy support in same day, okay no secret here, just spontaneously happen. I believe.

## fireice-uk | 2018-03-31T10:10:45+00:00
Secret? Feel free to pull our code if you have implementation troubles and you will be up and running tomorrow.

## xmrig | 2018-03-31T10:13:37+00:00
I will do. Thank you.

## bluemelatonin | 2018-03-31T12:39:47+00:00
@xmrig yes xmr-stak implement cryptonight-heavy , but i love xmrig  and I do not want to change ;-) 

good luck

## sergneo | 2018-04-01T07:51:40+00:00
@xmrig SUMO Testnet pool:
http://92.53.67.18
Testnet wallets:
Sutoe6DuhQJVR2RWKDWtC3YWGaTVeemBZVUYizBirBzK6ecaock4LNyZD6QUYy9Fwvb5MSD6VLFGiHijRhU4AdbzCc2j355X8Yv

## ghost | 2018-04-02T12:31:44+00:00
Sumo's HF is going to happen sooner (block 116520).

Binaries are released (0.3.0.0) and ready to dowbload.

## xmrig | 2018-04-03T11:31:53+00:00
CryptoNight-Heavy added in [dev](https://github.com/xmrig/xmrig/tree/dev) branch. [Full changelog](https://github.com/xmrig/xmrig/blob/dev/CHANGELOG.md#v260-beta1).

* **v2.6.0-beta1** release will be available soon.
* Use `"algo": "cryptonight-heavy",` in config file or `-a cryptonight-heavy` in command line to use new algorithm after the fork happen.
* OpenCL/CUDA miners will be updated later.

## sergneo | 2018-04-03T12:43:31+00:00
@xmrig 
            "variant": -1                    // algorithm PoW variant
what were the options.

## xmrig | 2018-04-03T12:49:14+00:00
About variant https://github.com/xmrig/xmrig/issues/434#issuecomment-372360213
For SUMO this option silency ignored.
Thank you.

## NEK2018 | 2018-04-04T08:07:10+00:00
Please, add graceful reload config support in xmrig-amd.
Thanks for all what you do!

## xmrig | 2018-04-05T19:24:36+00:00
AMD miner now ready too https://github.com/xmrig/xmrig-amd/releases/tag/v2.6.0-beta1

## xmrig | 2018-04-07T17:38:05+00:00
NVIDIA miner is ready https://github.com/xmrig/xmrig-nvidia/releases/tag/v2.6.0-beta1

## sergneo | 2018-04-07T18:19:31+00:00
@xmrig AMD? Nvidia? xmrig-nvidia-2.6.0-beta1-cuda8-win64.zip

## xmrig | 2018-04-07T18:42:10+00:00
Fixed, nvidia of course, thank you.

# Action History
- Created by: 2010phenix | 2018-03-25T13:14:08+00:00
- Closed at: 2018-04-19T14:12:43+00:00
