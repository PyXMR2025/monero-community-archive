---
title: There is no valid actual accepted share （DEROHE）
source_url: https://github.com/xmrig/xmrig/issues/3012
author: q6654282
assignees: []
labels: []
created_at: '2022-04-08T02:56:29+00:00'
updated_at: '2025-06-28T10:41:14+00:00'
type: issue
status: closed
closed_at: '2025-06-28T10:41:14+00:00'
---

# Original Description
Why is there no effective acceptance? derohe

I use DERO miner in 30 Mini blocks every day

There's not one using xmrig

# Discussion History
## q6654282 | 2022-04-08T02:58:53+00:00
[](https://fanyi.baidu.com/###)[](javascript:void(0);)24h did not generate any revenue!

xmrig

## SChernykh | 2022-04-08T05:20:04+00:00
Does xmrig show "0 blocks, 0 miniblocks" in output? If it shows more than 0, all questions go to the Dero network - xmrig works fine.

## q6654282 | 2022-04-08T07:08:29+00:00
![1649401517(1)](https://user-images.githubusercontent.com/4101732/162382633-a5f152e4-ead5-4cb0-881d-de162bd3cfc2.png)
There will never be more than 0. I have a lot of devices! One mini block will be generated in an hour with derominer? But I've been using xmrig for 20 hours! There are no blocks

## SChernykh | 2022-04-08T07:55:51+00:00
What's your hashrate on the device from screenshot? You need to have more than 1 MH/s hashrate to get 1 mini block per hour. You're probably mixing up numbers here.

## q6654282 | 2022-04-08T08:02:08+00:00
The device displays 33000h! But I have 100 such devices! Get Mini blocks with derominer! It's normal!

## q6654282 | 2022-04-08T08:05:18+00:00
![1649405027(1)](https://user-images.githubusercontent.com/4101732/162392790-d490c257-23e8-4fbc-9fb7-5fc0dc6e7e1b.png)
Look at my records. Xmrig hasn't produced more than three in 20 hours

## SChernykh | 2022-04-08T08:24:07+00:00
Dero network is very unstable now, people report that a lot of miniblocks they find don't get credited, and it can change a lot from one day to another. XMRig itself has correct implementation of the algorithm, and it sends all found hashes to Dero daemon. If a single device has 33 kh/s, it will take 2 days on average to find a mini block, so seeing "0 blocks, 0 mini blocks" in xmrig output is normal if you run it only for a few hours. You can try to switch back to dero miner, but I'm 99% sure you'll have the same problem eventually.

## q6654282 | 2022-04-08T08:28:22+00:00
Thank you ~! I try to make time longer! See if there will be a surprise

## Lonnegan | 2022-04-08T09:44:50+00:00
Is there a still working mining calculator left for Dero (HE) somewhere? Many of the old went offline after pools were closed and those which are still left, are showing nonsense, e.g. $120 per day for a Ryzen 7 with 55 kH/s. Quite a mess what's going on at Dero atm.

## SChernykh | 2022-04-08T12:23:54+00:00
@Lonnegan https://benchmark.dero.network/calculator
Ryzen 7 (8-core) should do more than 100 kh/s

## Lonnegan | 2022-04-08T12:41:15+00:00
@SChernykh thank you for the link.

Regarding the Ryzen speed: Well, probably not. It's an old Ryzen 7 2700 "Pinnacle Ridge" with DDR4-2666. AFAIK Dero is quite limited by the memory subsystem incl caches and 1st Zen generation has just 16 MB L3 cache plus the slow memory... A Ryzen 7 5800X with DDR4-3200 dc RAM is well above 100 kH/s, you are right :-)

## SChernykh | 2022-04-08T12:43:39+00:00
astrobwt/v2 fits into 128 KB of memory, all Ryzens can run it with all threads.

## Lonnegan | 2022-04-08T12:49:53+00:00
@SChernykh is that different to AstroBWT/v1? That had 20 MB per thread according to the xmrig algo info site?! That scaled 1 by 1 with the memory bandwidth.

But why then is Zen 1 so much slower than Zen 2/3? The narrow AVX unit?

## SChernykh | 2022-04-08T13:12:57+00:00
Yes, AVX2 is used heavily in the optimized code.

## snipeTR | 2022-04-08T15:33:39+00:00
> Dero network is very unstable now, people report that a lot of miniblocks they find don't get credited, and it can change a lot from one day to another. XMRig itself has correct implementation of the algorithm, and it sends all found hashes to Dero daemon. If a single device has 33 kh/s, it will take 2 days on average to find a mini block, so seeing "0 blocks, 0 mini blocks" in xmrig output is normal if you run it only for a few hours. You can try to switch back to dero miner, but I'm 99% sure you'll have the same problem eventually.

yep unstable mining. I use the same miners with the same hash power. (xmrig) and this is the result. It's really not stable at all.
![image](https://user-images.githubusercontent.com/31975916/162474819-9e6f9a0d-0180-4395-b41b-092c7f5405fe.png)


## akront | 2022-04-15T12:57:27+00:00
> Dero network is very unstable now, people report that a lot of miniblocks they find don't get credited, and it can change a lot from one day to another. XMRig itself has correct implementation of the algorithm, and it sends all found hashes to Dero daemon. If a single device has 33 kh/s, it will take 2 days on average to find a mini block, so seeing "0 blocks, 0 mini blocks" in xmrig output is normal if you run it only for a few hours. You can try to switch back to dero miner, but I'm 99% sure you'll have the same problem eventually.

how unstable ? transactions are supersonic fast, network seems fine, the issue is for the past week mining with 170KH/s using dero mining tool I had around 3-4 mini blocks a day all delivered to wallet fine

since yesterday both xmrig or derominer mine the same blocks but dont deliver to wallet 

something is harvesting the blocks faster or distribution has a problem

I have mined 10 mini blocks with xmrig none delivered to wallet 

## SChernykh | 2022-04-15T13:01:33+00:00
You should understand that if xmrig says "N miniblocks mined", it sent those miniblocks to Dero node that you use and the node said that their PoW hashes were correct. XMRig can't influence what happens next. All responsibility is on the Dero node you use and Dero network as a whole.

## akront | 2022-04-15T13:07:09+00:00
> You should understand that if xmrig says "N miniblocks mined", it sent those miniblocks to Dero node that you use and the node said that their PoW hashes were correct. XMRig can't influence what happens next. All responsibility is on the Dero node you use and Dero network as a whole.

What you saying is correct, what I dont get is what changed on dero network since last week, mining and transactions were fine, today transactions are fast but mining doesn't get credited to wallet anymore, so there is a major issue on dero network mining system, I am still mining and finding blocks lower number than before but no credit to wallet

# Action History
- Created by: q6654282 | 2022-04-08T02:56:29+00:00
- Closed at: 2025-06-28T10:41:14+00:00
