---
title: PoW change for Monero/Aeon/Sumokoin and others
source_url: https://github.com/xmrig/xmrig/issues/482
author: xmrig
assignees:
- xmrig
labels:
- META
created_at: '2018-03-29T09:39:36+00:00'
updated_at: '2018-11-05T14:31:32+00:00'
type: issue
status: closed
closed_at: '2018-11-05T14:31:31+00:00'
---

# Original Description
### :heavy_check_mark: Monero
 * **Successfully forked** on **April 6**, block height 1546000.
 * Miners v2.5+ will switch PoW automatically no additional setup or miner restart required.
 * Test pool http://killallasics.moneroworld.com/
 * Previous issue #434 with more Monero related details.

###  :clock5: Aeon
* Estimated date: **April 7**, not fixed yet as I know.
* Miners v2.5+ will switch PoW automatically no additional setup or miner restart required.
* Test pool https://aeonrebase.supportcryptonight.com from [reddit](https://www.reddit.com/r/Aeon/comments/877kmj/aeon_rebase_testnet_pool_pow/)

### :heavy_check_mark: Sumokoin
* **Successfully forked** at block height 116520.
* Sumokoin will use new algorithm named **Cryptonight-Heavy**, currently only CPU and AMD miner (**v2.6.0-beta1**) support it.
* Manual action required, `algo` option should changed to `cryptonight-heavy` and threads count should reduced twice (for CPU miners).
* More details in #476

### :heavy_check_mark: Turtlecoin
* **Successfully forked** on **April 8**, block height 350000.
* Manual action required, `algo` option should changed to `cryptonight-lite`, on each Turtlecoin pool option `variant` should set to `1`.
* Test pool https://trtltest.mine2gether.com/ from https://github.com/fireice-uk/xmr-stak/issues/1227

### :heavy_check_mark: Stellite
 * **Successfully forked** at block height 100800.
* Manual action required, on each Stellite pool option `variant` should set to `1`.
* Test pool https://cryptoknight.cc/v3/ from https://github.com/fireice-uk/xmr-stak/issues/1241

###  :heavy_check_mark: GRAFT
* **Successfully forked** at block height 65110.
* Manual action required now due version conflict https://github.com/xmrig/xmrig/issues/434#issuecomment-373184425
* Manual action required, if you was change `variant` option, on each GRAFT pool option `variant` should set to `1` or `-1`.

### :heavy_check_mark: Haven Protocol
 * **Successfully forked**.
* Manual action required, `algo` option should changed to `cryptonight-heavy` and threads count should reduced twice, only v2.6+ support it.

### :heavy_check_mark: IPBC
* **Successfully forked** on **April 16** at block height 54881.
* Manual action will required, `algo` option should changed to `cryptonight-ipbc`
* Support status: **Pending**.

###  :clock5: Masari
* Estimated date: **[May 1](https://github.com/masari-project/masari/commit/918b3b309b4bd51ced9e33a9e944bbdda503c1fd)**, at block height 170000.
* Manual action required, on each Masari pool option `variant` should set to `1` after the fork.

# Discussion History
## L1LjSHX | 2018-03-29T16:22:40+00:00
cryptonight-heavy?

## L1LjSHX | 2018-03-29T16:31:05+00:00
POW war is started. Thanks Bitmain and baikal...

## 2010phenix | 2018-03-30T10:55:07+00:00
@xmrig for Graft about update: https://www.graft.network/2018/03/27/upcoming-graft-software-release-major-network-update/

## xmrig | 2018-03-30T14:18:01+00:00
@2010phenix thank you, I will update info later, according their github, will be used Monero v7 PoW https://github.com/graft-project/GraftNetwork/pull/100
@esfomeado It just a **new difficulty algorithm**, not a new PoW, this change not directly affect miners.

## sergneo | 2018-04-02T12:10:16+00:00
@xmrig 
Sumokoin
‏ @sumokoin

Due to recent network's hashrate high fluctuations (our best guess is ASICs trying to get their last blocks) stalling the network, we decided to bring the fork's blockheight closer at block **116520**. Binaries will be released shortly.
Thank you

## Zambi9 | 2018-04-05T10:39:50+00:00
What happens if I just continue using version 2.4.4?

## xmrig | 2018-04-05T12:23:43+00:00
You shares will be rejected by pool, you can continue use older versions only for coins which not change PoW yet.

## DuyQuang06 | 2018-04-06T02:51:48+00:00
@xmrig IPBC coin update new Cryptonight "Variant" 

https://ipbc.io/eng/announcements/ipbc-fork-available-in-testnet/

: D

## DrStein99 | 2018-04-06T02:56:14+00:00
Scratchpad to 4k !?!? oh no!

## telebog | 2018-04-06T07:11:10+00:00
I have a Ryzen 1700 Cpu. Tried on Sumokoin and works only on 4 threads ~230 H/s If I configure Json to use 8 Threads it works only with ~130 H/s. Any idea what settings to use to work normally ~500H/s?

## xmrig | 2018-04-06T07:15:09+00:00
@DuyQuang06 Thank you for link.
@DrStein99 Now I'm confused how name this thing, maybe `cryptonight-ipbc` or `cryptonight-v7-jumbo-crazy`, because just `variant` not enough... 4 MB  scratchpad.
@ipbc-dev Reward most crazy PoW change now moved from Sumokoin to you.

## xmrig | 2018-04-06T07:18:57+00:00
@telebog No it not possible, it new `heavy` algorithm.

For reference i7-4770 original hashrate 300 H/s (4 threads) new is 136 H/s (2 threads). New algorithm specially designed to hurt CPUs hashrate. CPU vs GPU balance changed to prefer GPU mining. Scratchpad size is not main reason for such low hashrate, main loop length reduced twice, main reason is thing named `half-step` with additional memory access in main loop. If simple remove this `half-step` for test, hashrate is 237 H/s, but of course it make invalid hashes.

## Sayyiditow | 2018-04-06T17:08:12+00:00
haven protocol did not work for me, i keep getting rejected share, even with @cryptonight-heavy change on config.json. @xmrig 

## ipbc-dev | 2018-04-06T17:09:14+00:00
@xmrig 

Call it cryptonight ultraheavy ? 

We have forked your repo and implemented the new algo, CPU, AMD and Nvidia are working, we are testing and optimizing it, when we are done we can do a pull request.

https://github.com/ipbc-dev/ipbc-miner


## xmrig | 2018-04-06T17:15:37+00:00
@Sayyiditow You should use only version **v2.6.0-beta1** for it, I was checked mine Haven, it works.
@ipbc-dev I think `cryptonight-ipbc` is good, pull request would be nice, please use dev branch for it.
Thank you.

## rhlug | 2018-04-06T20:39:36+00:00

>> Manual action required, algo option should changed to cryptonight-heavy and threads count should reduced twice.

Can intensity be halved and keep same # of threads?

OLD
```
    "threads": [
        { "index": 0,  "intensity": 1920, "worksize": 8, "affine_to_cpu": false },
        { "index": 0,  "intensity": 1600, "worksize": 8, "affine_to_cpu": false },
    ],
```
NEW
```
    "threads": [
        { "index": 0,  "intensity": 960, "worksize": 8, "affine_to_cpu": false },
        { "index": 0,  "intensity": 800, "worksize": 8, "affine_to_cpu": false },
    ],
```

OR is this required?
```
    "threads": [
        { "index": 0,  "intensity": 1920, "worksize": 8, "affine_to_cpu": false },
    ],
```

Or does it matter?


## xmrig | 2018-04-06T21:02:57+00:00
@rhlug it related only to CPU miners and it was written when only CPU version was available, so if you was run 2 threads you should run 2 too, but about `intensity` no need reduce it twice, optimal values should be above 1000 but lesser previous intensity, only experimenting may suggest you now.
Thank you.

## Sajo8 | 2018-04-08T04:13:09+00:00
TurtleCoin has successfully forked on April 8, at block height 350000, please update

## pejuangbitco | 2018-04-08T09:16:04+00:00
how changed algo to cryptonight-heavy? i use cpu

## xmrig | 2018-04-08T17:19:09+00:00
@Sajo811 Thank you I updated info.
@pejuangbitco change [this line](https://github.com/xmrig/xmrig/blob/master/src/config.json#L2) in your config to `"algo": "cryptonight-heavy", ` and use miner v2.6.0-beta1

## Sayyiditow | 2018-04-09T02:28:02+00:00
@ipbc-dev any idea when you will fork?

## 2010phenix | 2018-04-09T16:30:48+00:00
@xmrig Graft add pool for test... and strange, only NVIDIA and AMD miner, link: https://bitcointalk.org/index.php?topic=2115188.msg34305644#msg34305644
-- cut --
The team completed an update to the public testnet. 
A new pool for mining functionality test is available here : http://pooltest.graft.network
-- cut --

## 2010phenix | 2018-04-13T00:37:49+00:00
@xmrig Graft move update date: 
-- cut --
PATCH 1.1.1 HAS BEEN RELEASED – MAJOR NETWORK UPDATE ON BLOCK 65110
We decided to make the major network update sooner in order to minimize the possibility of hashrate attacks. Patch version 1.1.1 is now released and available for download from master. The major network update itself is rescheduled for block height 65110, around April 14th.
-- cut --

## felipe-vvoosh | 2018-04-13T09:17:57+00:00
ETN is doing what? Such a slow team...

## ipbc-dev | 2018-04-13T09:32:28+00:00
@Sayyiditow yes on monday 16.04.2018 at height 54881 (cryptonight light custum version)
more details here:  https://ipbc.io/eng/announcements/ipbc-fork-april-2018/

## xmrig | 2018-04-13T11:45:32+00:00
@ipbc-dev guys are you serious? naturally just one line added in algorithm code.
Hashrate drop is only 10 H/s only because this single line not optimized. (i7-4770 8 threads 1100 H/s on aeon7 vs 1090 H/s on ipbc). But this change makes your algorithm not compatible with exists miners.

## ipbc-dev | 2018-04-13T14:38:50+00:00
@xmrig i am sorry but this "single" line will save our ass when asic's starts to attack aeon.

## xmrig | 2018-04-13T21:57:54+00:00
@ipbc-dev if someone will make ASICs for Aeon in next 6 months, they can implement your XOR just for fun.
@fireice-uk Look at this https://github.com/ipbc-dev/ipbc-miner/blob/master/xmrstak/backend/cpu/crypto/cryptonight_aesni.h#L515

## mcnih | 2018-04-15T02:38:26+00:00
Hai xmrig, is Bytecoin (BCN), Intensecoin and some other coins will fork their algo also?

Thanks.

## ipbc-dev | 2018-04-15T10:21:57+00:00
@xmrig yesterday with new Baikal N on new v7 light.
![image](https://user-images.githubusercontent.com/34477436/38777384-338fa7fa-40a7-11e8-84df-29a0cae68534.jpg)




## xmrig | 2018-04-15T10:30:23+00:00
@ipbc-dev Aeon still not fork to v7.

## ipbc-dev | 2018-04-15T10:45:53+00:00
@xmrig ups sorry my bad, i supposed is already done, just taked a look here https://www.cryptunit.com

## sibero | 2018-04-17T15:02:01+00:00
intensecoin fork to v7 PoW - May 14, 2018 https://intensecoin.com/2018/04/15/april-15th-update/

## felipe-vvoosh | 2018-04-18T08:11:55+00:00
ETN is just playing with the devil now, the network is at 650 MH/s and the fan boys are saying that ASIC miners are fine as the team keeps struggling to fork and become ASIC resistant. It’s a blind trusting.

## marki555 | 2018-04-18T11:00:54+00:00
@sibero That is not accurate. 2 days ago ITNS released new plan for emergency fork in the following few days - https://intensecoin.com/2018/04/16/imminent-hard-fork-and-network-attack/

## 2010phenix | 2018-04-18T17:19:07+00:00
@marki555 yes for now April 21

## cmorsucci | 2018-04-20T10:04:54+00:00
aeon v7 is supported?

## xmrig | 2018-04-22T14:56:43+00:00
Masari will fork too, information updated.

## 2010phenix | 2018-04-26T14:05:51+00:00
almost all coin use or monero v7 clean, or option variant should set to 1
maybe OLD monero change to variant 1 and all other new-NEW-nEW altcoin simple work with autodetect or we can't detect?

## xmrig | 2018-04-26T18:12:31+00:00
`variant` should set to 1, autodetection is useless since all other coins use block version below 7, except GRAFT, but actually good idea change default to `1` sometime later. I think you already saw https://github.com/xmrig/xmrig-proxy/issues/168 it allow pool explicitly inform miner about what exactly algorithm needed.

Now `cryptonight-lite` has 3 possible variants and `cryptonight` will have 3 variants soon, total 7 algorithms now.

## MoneroOcean | 2018-04-26T18:58:01+00:00
Does xmrig already reacts to algo change provided by pool/proxy?

## bobbieltd | 2018-04-26T19:27:05+00:00
@MoneroOcean Under my tests with xmrig 2.6.0 beta 3 / xmrig 2.5.3, xmrig doesn’t change algo.

## 2010phenix | 2018-04-27T13:05:34+00:00
@xmrig Yes for proxy very good and simple idea send variant and algo data and even more, no other solution....
but look on miner, we have already  programmable algo-Terminator )) , demand more and more time for you(with not clarify itself algo Devs) and for ppl who used xmrig..
autodetect all this things(most like new algo fork from monero) solve and save time.

@MoneroOcean us say xmrig detect be in 2.6 stable master (for now only beta)



## randing89 | 2018-04-29T07:17:07+00:00
@xmrig 
Hi 
BBSCoin has been forked to `Cryptonight v7` on height 72500.
Original announcement: https://twitter.com/bbscoin_xyz/status/986098944387072001
Our official pool is: http://pool.bbscoin.xyz/

## 2010phenix | 2018-04-29T11:28:44+00:00
@randing89  Hashrate(Network Hash Rate: 267.77 KH/sec) not to low for IN ?

## mcnih | 2018-04-29T15:21:24+00:00
is ETN going to fork the algo or not? thanks

## cyberghost66 | 2018-04-30T16:20:53+00:00
ETN BLOCKCHAIN UPDATE MAY 30TH
https://electroneum.com/2018/04/25/blockchain-update/
( https://youtu.be/XJVspl2sJWQ )

## bobbieltd | 2018-05-04T22:30:22+00:00
@MoneroOcean 
if (algorithm.isValid()) {
        LOG_ERR("Incompatible algorithm \"%s\" detected, reconnect", algorithm.name());
    }
    else {
        LOG_ERR("Unknown/unsupported algorithm detected, reconnect");
    }

No algorithm switching 😂 only for variant.
@xmrig Do you plan to make algo switch (lite, normal, heavy) in the future ? Scratchpad size issue ?


## Zambi9 | 2018-05-09T05:36:42+00:00
Do I understand correctly, that for Monero we will potentially need to change the miner every 6 months?

## sergneo | 2018-05-09T06:30:34+00:00
   @Zambi9  in the future it is expected that Yes it is necessary

## stoffu | 2018-05-25T01:06:57+00:00
@xmrig Aeon is forking on June 3rd: https://github.com/aeonix/aeon/releases/tag/v0.12.0.0

## QwertyJack | 2018-05-29T23:56:54+00:00
@xmrig Etn is gonna fork these days: [etn update](https://electroneum.com/2018/04/25/blockchain-update/)

## xmrig | 2018-11-05T14:31:31+00:00
Recent information about algorithms/coins https://xmrig.com/docs/supported-currencies this issue not updated for a while, and not actual anymore.

# Action History
- Created by: xmrig | 2018-03-29T09:39:36+00:00
- Closed at: 2018-11-05T14:31:31+00:00
