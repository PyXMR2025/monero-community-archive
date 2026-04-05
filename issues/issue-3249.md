---
title: 'How to connect to the pool '
source_url: https://github.com/xmrig/xmrig/issues/3249
author: gif12
assignees: []
labels: []
created_at: '2023-04-13T19:23:20+00:00'
updated_at: '2025-06-18T22:42:52+00:00'
type: issue
status: closed
closed_at: '2025-06-18T22:42:52+00:00'
---

# Original Description
How to connect to the pool and which is the best?

And if we have a cpu with 16 cores from the Intel brand, if it is constantly active, can we estimate how much it earns per month?


# Discussion History
## Spudz76 | 2023-04-14T01:43:51+00:00
Find your exact CPU model at the [benchmarks site](https://xmrig.com/benchmark?vendor=intel) for speeds, then plug speed into an earnings calculator (most pools have one, or some price index sites also do, the pool ones might account for their fee schedule though).

I only know about Monero/XMR pools, although xmrig could mine quite a few various other coins.

MoneroOcean has a fork that can hop algorithms to whichever one earns the most XMR at all times, and tests all the hashrates on your actual rig for the supported algorithms, and pays XMR regardless which actual blockchain is being mined.  Depending what CPU model and the RAM situation it might earn more that way than straight RX/0.  There is a minimum balance and fees reduce the more you stack before withdrawing.  I have been using them for years.

If it's actually good at RX/0 then P2Pool is best for no fees and no balances but you get a bursty stream of dust payments, but over longer time scales luck runs or lags average out.  Extra software to setup since it's decentralized/p2p and there is no "pool" and no balances.

Do not use any pool that doesn't have autodiff or requestable-diff or at worst a low-diff port.  Whatever your hashrate is times 30 should be the diff (so you catch a result about every 30 seconds).  Lots of the busiest pools only go low enough for multiple kilohash rates they don't really want to bother with slower miners, watch out for that or you won't find results in time and won't earn anything.

## gif12 | 2023-04-14T06:25:23+00:00
Thanks for the help

Can you tell me your total hashrate and income?
It helps me to calculate my income better

# Action History
- Created by: gif12 | 2023-04-13T19:23:20+00:00
- Closed at: 2025-06-18T22:42:52+00:00
