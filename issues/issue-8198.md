---
title: 'Payment never received (similar to issue #8134)'
source_url: https://github.com/monero-project/monero/issues/8198
author: ikseles
assignees: []
labels: []
created_at: '2022-03-01T19:26:46+00:00'
updated_at: '2022-03-01T20:26:04+00:00'
type: issue
status: closed
closed_at: '2022-03-01T20:26:04+00:00'
---

# Original Description
Hello -

I recently was paid for an uncle I found while minding on the mini p2pool.  About 7 days ago I was due to receive a payment for a share I found but never did.  I have included 2 screen shots from the mini p2pool observer that displays my information as well as the transaction information where payment was missed.

<img width="1280" alt="Screen Shot 2022-03-01 at 2 21 46 PM" src="https://user-images.githubusercontent.com/44760353/156235094-059ef05c-72bf-455c-ac75-c9935783db36.png">

<img width="1280" alt="Screen Shot 2022-03-01 at 2 21 28 PM" src="https://user-images.githubusercontent.com/44760353/156235123-acd13fe4-ae16-49fe-9a32-36971de9590d.png">

Thank you in advance for your help!



# Discussion History
## SChernykh | 2022-03-01T19:51:23+00:00
It's p2pool-mini, it doesn't find blocks often enough to pay for every share:
https://github.com/SChernykh/p2pool#how-pplns-works-in-p2pool
> NOTE If P2Pool doesn't have enough hashrate to find Monero blocks faster than every 6 hours on average (~15 MH/s), not all your pool shares will result in a payout. Even if pool hashrate is higher, bad luck can sometimes result in a share going through PPLNS window without a payout. But in the long run it will be compensated by other shares receiving multiple payouts - your payouts will average out to what you'd get with regular pool mining.

# Action History
- Created by: ikseles | 2022-03-01T19:26:46+00:00
- Closed at: 2022-03-01T20:26:04+00:00
