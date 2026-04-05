---
title: Problem mining RVN using XMRig 6.1.1 for Nvidia GeForce GT 750M
source_url: https://github.com/xmrig/xmrig/issues/2241
author: danigonlinea
assignees: []
labels: []
created_at: '2021-04-07T11:28:32+00:00'
updated_at: '2021-04-12T13:31:25+00:00'
type: issue
status: closed
closed_at: '2021-04-12T13:31:25+00:00'
---

# Original Description
**GPU Info**

- Nvidia GeForce GT 750M
- Version: 425.31

**Context**

I'm trying to mine Ravencoin to check if hashrate can be higher than mining XMR (which is inneficient around 20 H/s) and I wonder, once has been added support for KawPow to give it a try.

For this GPU, _Cuda 10_2_ didn't work but **Cuda 10** yes, using **Xmrig 6.1.1**  so I just replaced the files and start executing it.

**Config File**
I have used the simple [one ](https://github.com/xmrig/xmrig/pull/1694#issuecomment-638310915)

The result is this:

![image](https://user-images.githubusercontent.com/1208620/113858615-384e0500-97a4-11eb-9dd4-8996fbf8c525.png)

Anything I can do? Thanks in advance.



# Discussion History
## SChernykh | 2021-04-07T11:33:07+00:00
Not enough GPU memory for KawPow DAG, you can't mine it with only 2 GB.

## danigonlinea | 2021-04-07T12:04:17+00:00
Thanks for response.

Well, will continue mining XMR but only for CPU. At least, I'm giving him a second life :)

## Spudz76 | 2021-04-09T06:06:54+00:00
CN-Heavy/XHV (Haven) works well on Kepler with lower memory.  Value decent, way more than XMR.  Some pools have multicoin and payout everything in XMR (autochanging).  Then you run one xmrig cpu-only and one cuda-only pointed to same pool and don't have to hassle with different pools or dealing with all different wallets.

This is setup like that with Xeon E5-2620 and GTX970 (XMR equivalent after exchange hashrate shown):
![image](https://user-images.githubusercontent.com/2391234/114135755-f5388280-98c6-11eb-952b-c11c4bc25c3e.png)

## danigonlinea | 2021-04-09T09:39:55+00:00
Thanks for the tip, I have seen is not compatible with Binance which is what I use normally but will try with XHV because I haven't found any useful coin for this GPU and was expecting good results on RVN. 

## danigonlinea | 2021-04-09T17:05:35+00:00
Mining in herominers and having around 60 H/s, that's better than nothing. Thank you.

## Spudz76 | 2021-04-10T01:17:10+00:00
Looks to me like Binance only does bitcoin or eth on their pool, do you mean Bitfinex exchange doesn't handle XMR?
I use kraken to flip my XMR.  You could trade for BTC or ETH there and then send it to your Binance/BItfinex account every now and then?

Otherwise I'm not sure what "compatible with Binance" means.

## danigonlinea | 2021-04-10T13:32:59+00:00
For XHV, what I mean is that I cannot send XHV directly to Binance as it is not traded in this exchange. Exchanges that are compatible with it are Kucoin/Bittnex/Tradeorg/Bkex so I was thinking to:
1. Send XHV to Wallet and then to Kucoin (for example) and start staking them.
2. Send XHV to Wallet and then to Kucoin (for example), converting them to any crypto and send them to Binance (or keeping them in kucoin) and start staking them.


For XMR, my plan is to send them to Binance directly or directly to Trust Wallet. After that start staking them or invest in other cryptos.

Just wanna see the whole process as I'm mining for fun with an old computer I have. Maybe I try Kraken as well, I have read good things in this platform and also allows staking.



# Action History
- Created by: danigonlinea | 2021-04-07T11:28:32+00:00
- Closed at: 2021-04-12T13:31:25+00:00
