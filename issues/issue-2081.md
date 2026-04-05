---
title: Highly variable hashrate on windows
source_url: https://github.com/xmrig/xmrig/issues/2081
author: seangrant82
assignees: []
labels:
- question
created_at: '2021-02-04T03:48:18+00:00'
updated_at: '2021-04-12T14:17:32+00:00'
type: issue
status: closed
closed_at: '2021-04-12T14:17:32+00:00'
---

# Original Description
**Describe the bug**
Hash rate is not stable and varies wildly (See image over 7hrs)
![image](https://user-images.githubusercontent.com/11846453/106835730-dbc84f80-6665-11eb-842a-8bbabe3cfa76.png)

All other ancillary process are ended

**To Reproduce**
run xmrig over long period of time

**Expected behavior**
I would expect a stable hashrate

**Required data**
 - Miner log as text or screenshot
 - Config file or command line (without wallets):
`xmrig.exe --cuda -o pool.supportxmr.com:443 -k --tls`
 - OS: Windows 10
 - GPU: GTX 970M v2721.14.6140 (CUDA 11)
 - CPU i7-4710 @2.5Ghz





# Discussion History
## SChernykh | 2021-02-04T07:34:38+00:00
Pool-side hashrate is just an estimation of your real hashrate. It depends on how many shares you find. And don't use GPU to mine RandomX, it's very inefficient.

## seangrant82 | 2021-02-05T15:00:09+00:00
@SChernykh thanks for info. I guess i assumed that since xmrig supports gpu it would work for XMR (but I guess the GPU support is for other coins)

Question I have then is when I remove CUDA and only use CPU, why is only 50% of cpu being used? I have 4 cores with 8 logical processors

![image](https://user-images.githubusercontent.com/11846453/107050113-df102800-6798-11eb-8d0b-ccdc34dc0eaf.png)
![image](https://user-images.githubusercontent.com/11846453/107050139-e3d4dc00-6798-11eb-86ad-24e4085b4642.png)
![image](https://user-images.githubusercontent.com/11846453/107050159-e7686300-6798-11eb-9419-cf5dc754eef4.png)




## Lonnegan | 2021-02-05T16:05:45+00:00
Monero mining needs 2 MB scratchpad for each thread. It is important for max performance, that these scratchpads stay in last level cache, otherwise access to slow DRAM would slowdown hashrate.

Your CPU has a last level cache of 6 MB size. So just 3 threads can be started without flooding the cache.

Your CPU is not ideal for Monero mining; too small L3 cache. Perhaps it would be more profitable with your hardware to mine a coin with smaller scratchpad size like Wownero (1 MB => you can start 6 threads) or ArQmA (256 KB => you can use all threads of your CPU). You have to calculate your best profite.

## Spudz76 | 2021-02-05T20:17:10+00:00
Mine to MoneroOcean since they pay XMR regardless which of the algos your equipment actually mines.  Run one xmrig configured for CPU-only and another configured for GPU-only and then they each run whatever's profitable at the moment, while paying XMR auto-changed.  Note there is a fork of xmrig with added features (and algos) for the pool (it won't autoswitch with the mainstream version).

Or yes, you need more ideal equipment for actual RandomX algos (real-cores times 2MB of cache and AES extensions).  6MB only allows for 3 threads regardless if there were 32 cores.  As I understand, the AES-NI extensions only operate on data that is in cache (or it has to be copied in, operated on, and copied back out), as well.

## ghost | 2021-02-08T08:56:56+00:00
It's a bit OT but suggest to use BetterHash. It uses XMRig for CPU and automatically set another Miner for GPU, so it will fix GPU mining on the best miner for your GPU.

## seangrant82 | 2021-02-08T15:37:10+00:00
thanks @Spudz76 and @ScardracS for tips. I will look into both once I hit my min payout on my current pool

# Action History
- Created by: seangrant82 | 2021-02-04T03:48:18+00:00
- Closed at: 2021-04-12T14:17:32+00:00
