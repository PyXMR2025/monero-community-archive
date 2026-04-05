---
title: New algo for Graft, CN Waltz. Support?
source_url: https://github.com/xmrig/xmrig/issues/923
author: pikomule
assignees: []
labels:
- enhancement
- algo
created_at: '2019-01-29T21:02:31+00:00'
updated_at: '2019-03-05T12:24:17+00:00'
type: issue
status: closed
closed_at: '2019-03-05T12:24:17+00:00'
---

# Original Description
CryptoNight Waltz custom POW is ready for testing:

Seeds:
54.208.86.27:28880
54.144.192.6:28880
35.175.164.180:28880
Recent HF Height: 261100

https://github.com/graft-project/GraftNetwork/tree/test/cn_waltz_test

# Discussion History
## xmrig | 2019-01-30T04:12:19+00:00
Just another variation of changing iteration count, the third such change in the last few weeks. Little boring.
Thank you.

## xmrig | 2019-02-03T16:52:33+00:00
@zelerius @graft-project please explain current situation, looks like both coins will use same algorithm (cn/2 with 393216 iterations) https://github.com/fireice-uk/xmr-stak/pull/2196

So thank you for suggested name for the algorithm, but little name conflict here.

## ghost | 2019-02-03T22:07:05+00:00
This is very rare or just a coincidence...

We have done several tests months ago and we want to change the iterations in the next hard fork in order to avoid merged mining. We have everything ready, for that reason, we have made several PR for example 
https://github.com/fireice-uk/xmr-stak/pull/2196 and https://github.com/MoneroOcean/node-cryptonight-hashing/pull/21

Our intention is calling this little variation as **cryptonight_zlx** but this situation changes everything... we have identified several pools where people mine Graft and Zelerius at the same time, for example, this one https://webgrft.semipool.com/#/blockauxs This is exactly what we want to avoid.

## bobbieltd | 2019-02-04T09:24:01+00:00
It is not coincidence but it is fate ;). 
(Graft + Zelerius + semiPOOL) = destiny 🐥
Using same algos will have better support and less burden on mining softwares (xmrig, xmr-stak, ...)
If Zelerius dev does not like merged mining, you can look at BBSCoin codes to disable it.

## SomethingGettingWrong | 2019-02-04T13:49:38+00:00
Yes its on the testnet but just the other day on the Graft mining channel they
 discussing a different algo.  So graft dev's need to chime in. 

## ghost | 2019-02-04T17:18:52+00:00
Ok, thank you. Then we are waiting for a response from Graft dev's. If they use this number of iterations we will use other custom variation of CN. 

## EDDragonWolf | 2019-02-04T19:00:23+00:00
@xmrig 
We have learned about Zelerius and their changes a day ago and found the latter quite surprising. 

Waltz landed in our main repository 7 days ago (https://github.com/graft-project/GraftNetwork/pull/216). The current variant was based on CNv8, is not final, we're still weighing our options for CNv8, CNv0, Heavy, etc.

We'd call it a new hashing algorithm but rather a CryptoNight tweak. It was named Waltz because this tweak used 3/4 iteration of original CryptoNight and waltz dance has 3/4 time signature.

## ghost | 2019-02-04T19:36:09+00:00
Sorry but we have done private test months ago and our changes were published 7 days ago on github, as you can see here https://github.com/zelerius/Zelerius-Network/commit/8e3527fac13319e90559076a34283e6df0f7c33d For that reason we have the code for xmr-stak and node-cryptonight-hashing as Zelerius said in his last comment. Our intention is to make a hard fork with our custom variation of CNv8 but if Graft network wants the same variation of this algorithm, then we will make a different variation of CNv8. Please tell us your intention. **Does Graft network want to include our variation?**



## SomethingGettingWrong | 2019-02-04T20:24:33+00:00
![new bitmap image](https://user-images.githubusercontent.com/36722911/52235019-9612f980-2888-11e9-93b9-b62868c410b3.png)


## ghost | 2019-02-04T20:35:38+00:00
Please tell us your intention 

## SomethingGettingWrong | 2019-02-04T20:52:53+00:00
Honestly I planned on using a 3/4 iteration change but I felt that your coin would be merge mined with mine and I didn't want to devalue it since obviously my coin would be the parent coin.  So I'm trying to figure out which one of you guys need the algo more then me since you cant merge mine all 3 of us together.  

Edit: I named my algo Waltzerius


## ghost | 2019-02-04T21:27:56+00:00
Honestly, I don't understand your comments. This is very simple if Graft uses our variant then Zelerius will not use it, it's all yours. We will create another different variant for Zelerius network.

You have two options: include our variant in your network or don't include it and keep cloning Monero which always is fine for Graft

Please, tell us your intention.

## anartz | 2019-02-04T21:50:43+00:00
be honest man of GRAFT coin, stop this foolishness...quite sad this kind of comments from a "serious" dev...LMAO

## fireice-uk | 2019-02-04T22:00:31+00:00
> Just another variation of changing iteration count, the third such change in the last few weeks. Little boring.

@xmrig I get why they do it, just **try** to modify something here so that it is supported both on SSE2 and ARMs https://github.com/monero-project/monero/blob/master/src/crypto/slow-hash.c I tend to swap the code out altogether for my jobs for something more competently written ;)

## ghost | 2019-02-04T22:36:25+00:00
@fireice-uk Yes it is quite complicated ;)

## SomethingGettingWrong | 2019-02-04T22:55:38+00:00
lol Im not a graft dev. I'm saying you guys are fighting over a simple iteration change. but then you said you don't want it if they use it. The graft dev has not replied back yet. I have no idea what they are going to do. If you use an iteration change make sure other projects have not done this. Iteration changes are apparently the property of the first person to discover them.

## ghost | 2019-02-05T06:45:25+00:00
I’m not fighting over iteration change I’m just waiting for a response from Graft dev’s for that reason we want to give the change to them if they want use it. I’m waiting for a simple response from them

## psychocrypt | 2019-02-05T21:53:16+00:00
@xmrig my answer to the new hobby to change the number of iteration is [this WIP PR](https://github.com/fireice-uk/xmr-stak/pull/2209). It will allow the use to mine a modification of an original POW algorithm with modified iterations without the need to update the miner.
`cn_half` will be `cryptonight_monero_v8:0x00040000:0x00200000:0x1FFFF0`

## xmrig | 2019-02-06T08:42:02+00:00
@psychocrypt It's crazy I think I will not add same thing, but if it not break performance who knows. Also take look to this code https://github.com/xmrig/xmrig/blob/master/src/workers/CpuThread.cpp#L111 introduced via #905 It allow change ASM code on fly too.
Thank you.

## jagerman | 2019-02-14T03:45:33+00:00
@nilhcraiv - I understand why you wouldn't want merge mining, but wouldn't it be simpler to just modify the blockchain to not accept merge-mined blocks?

## jagerman | 2019-02-14T03:53:20+00:00
> It was named Waltz because this tweak used 3/4 iteration of original CryptoNight and waltz dance has 3/4 time signature.

Given that it actually cuts from 0x80000 to 0x60000 iterations, I feel a 6/8 time signature is more appropriate.  So maybe it should be called CN-double-jig?  Or CN-Hallelujah?

## ghost | 2019-02-14T06:47:08+00:00
The initial idea was to temporarily avoid Nicehash. The merged mined represents a low percentage, in the future, we will also eliminate it.

Finally, we are going to fork over the next few weeks with 0x60000 iterations. For now, no currency is using it, then we have called it ZLS. Honestly, the name does not matter to us but we will call it ZLS for this reason. It is a minimal change, fight for the name does not make sense :) Thank you

## xmrig | 2019-03-05T12:24:17+00:00
I close this issue both Zelerius variant and Graft/Waltz (the new one) is added to dev branch.
Thank you.

# Action History
- Created by: pikomule | 2019-01-29T21:02:31+00:00
- Closed at: 2019-03-05T12:24:17+00:00
