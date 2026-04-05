---
title: Monero. Solo mining. Zeros in the results row.
source_url: https://github.com/xmrig/xmrig/issues/2415
author: RunesReader
assignees: []
labels: []
created_at: '2021-05-30T13:00:20+00:00'
updated_at: '2021-06-01T07:37:07+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Hello!
I set up solo mining for Monero coins.
Is it ok, when I see **zeros** in the Results row **_all the time_**?

Thank you in advance!
![Screenshot 2021-05-30 at 15 49 40](https://user-images.githubusercontent.com/12240504/120105030-fddb6580-c15f-11eb-812d-f6fbb623059e.png)


# Discussion History
## SChernykh | 2021-05-30T13:26:40+00:00
When solo mining, each accepted result = mined block, so it will be rare. You can check on testnet if it's working correctly, testnet difficulty is much lower.

## RunesReader | 2021-05-30T14:30:53+00:00
@SChernykh Thank you for quick response! I will try testnet.

## toy1111 | 2021-05-31T17:54:50+00:00
Hi - you should join a mining pool for Monero. There are a number of options like miningpoolhub.com and others. These payout based on your hashrate contribution not on how many blocks you actually solve. Solo mining with a low hashrate will take a very long time to be lucky to solve a block. Based on your hashrate and the total network hashrate you would expect to solve a block once every 6 years.

## RunesReader | 2021-06-01T07:12:23+00:00
@toynn I was mining Monero in the pool. I had about 0.01 Monero per month. So it might not be interesting at all. But solo mining is like a gambling :))

## Lonnegan | 2021-06-01T07:18:02+00:00
> @toynn I was mining Monero in the pool. I had about 0.01 Monero per month. So it might not be interesting at all. But solo mining is is like gambling :))

Yes, but with such a low hashrate you have, it's a hopeless gamble. Using a calculator tool, you can see, that with just 1,6 kH/s the probability to find a block for yourself is at each 6.5 years with the current difficulty! Ok, probability doesn't mean, that it will take so long. You might find one tomorrow; or just in 20 years.

With such a slow device I'd mine on a PPS pool, where you get paid for each share you return to the pool, regardless if it found a block in that peroid or not. PPS pools are e.g. hashcity or hellominer.

## RunesReader | 2021-06-01T07:37:07+00:00
@Lonnegan Yes, you are right. But for now I use my free laptop for mining only as a start point in mining world. I am just trying to understand all these stuffs. Thank you for response!

# Action History
- Created by: RunesReader | 2021-05-30T13:00:20+00:00
