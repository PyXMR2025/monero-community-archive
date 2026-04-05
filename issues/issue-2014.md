---
title: mining cn-heavy / xhv at 128 core
source_url: https://github.com/xmrig/xmrig/issues/2014
author: Tom68-cz
assignees: []
labels: []
created_at: '2020-12-29T22:43:42+00:00'
updated_at: '2020-12-30T16:30:11+00:00'
type: issue
status: closed
closed_at: '2020-12-30T16:30:11+00:00'
---

# Original Description
I have a 128 thread processor. When I want a mining cn-heavy / xhv processor it runs only 64 threads and is minig 5500 H / s. If I reset mining in config to 120 threads, mining is only 2200 H / s. All threads run 4000 Mhz in both cases. I have 64 Gb of RAM. Does anyone know why this is so?


# Discussion History
## Lonnegan | 2020-12-30T13:03:08+00:00
CN Heavy uses 4 MB scratchpad size per thread. Do you have enough last level cache to run 120 or 128 threads without flooding the cache? What's your CPU?

## Tom68-cz | 2020-12-30T13:09:56+00:00
Threadriper 3990x

## Tom68-cz | 2020-12-30T13:14:44+00:00
Ok I get it. Is there a way to fix it?

## Lonnegan | 2020-12-30T13:15:32+00:00
Your cpu has 256 MB last level cache. 4 MB for each thread makes 64 threads. So running 64 threads gives you the best performance in CN heavy, because it can mine without accessing the slow DRAM.

If you want to use all your logical cores, you have to mine a coin with 2 MB scratchpad size, for example Monero. Monero should give you around 60000 H/s with your cpu.

You can check here...
https://www.cryptunit.com/
...what gives you more profit, 5500 H/s in Haven or 60000 H/s in Monero (algo = RX).

## Tom68-cz | 2020-12-30T16:30:11+00:00
thank you

# Action History
- Created by: Tom68-cz | 2020-12-29T22:43:42+00:00
- Closed at: 2020-12-30T16:30:11+00:00
