---
title: Does xmrig support "Ethash4G"?
source_url: https://github.com/xmrig/xmrig/issues/2387
author: Joe23232
assignees: []
labels: []
created_at: '2021-05-17T11:23:27+00:00'
updated_at: '2025-06-16T18:47:21+00:00'
type: issue
status: closed
closed_at: '2025-06-16T18:47:21+00:00'
---

# Original Description
Hi, I wanted to know Does xmrig support "Ethash4G" hashing algorithim for cryptomining as according to [this website](https://whattomine.com/coins?aq_380=1&aq_fury=1&a_fury=true&aq_470=1&aq_480=3&aq_570=0&aq_580=0&aq_vega56=0&aq_vega64=0&aq_5600xt=0&aq_5700=0&aq_5700xt=0&aq_vii=1&aq_67xt=0&aq_68=0&aq_68xt=0&aq_1050Ti=0&aq_10606=0&aq_1070=0&aq_1070Ti=0&aq_1080=0&aq_1080Ti=0&aq_1660=0&aq_1660Ti=0&aq_166s=0&aq_2060=0&aq_2070=0&aq_2080=0&aq_2080Ti=0&aq_3060=0&aq_3060Ti=0&aq_3070=0&aq_3080=0&aq_3090=1&eth=true&factor%5Beth_hr%5D=0.00&factor%5Beth_p%5D=0.00&factor%5Be4g_hr%5D=29.00&factor%5Be4g_p%5D=220.00&factor%5Bzh_hr%5D=32.00&factor%5Bzh_p%5D=240.00&factor%5Bcnh_hr%5D=400.00&factor%5Bcnh_p%5D=120.00&factor%5Bcng_hr%5D=630.00&factor%5Bcng_p%5D=150.00&factor%5Bcnr_hr%5D=0.00&factor%5Bcnr_p%5D=0.00&factor%5Bcnf_hr%5D=900.00&factor%5Bcnf_p%5D=120.00&factor%5Beqa_hr%5D=140.00&factor%5Beqa_p%5D=240.00&factor%5Bcc_hr%5D=0.00&factor%5Bcc_p%5D=0.00&factor%5Bcr29_hr%5D=0.00&factor%5Bcr29_p%5D=0.00&factor%5Bct31_hr%5D=0.40&factor%5Bct31_p%5D=220.00&factor%5Bct32_hr%5D=0.00&factor%5Bct32_p%5D=0.00&factor%5Beqb_hr%5D=16.50&factor%5Beqb_p%5D=160.00&factor%5Brmx_hr%5D=0.00&factor%5Brmx_p%5D=0.00&factor%5Bns_hr%5D=1250.00&factor%5Bns_p%5D=270.00&factor%5Bal_hr%5D=54.00&factor%5Bal_p%5D=200.00&factor%5Bops_hr%5D=0.00&factor%5Bops_p%5D=0.00&factor%5Beqz_hr%5D=23.00&factor%5Beqz_p%5D=240.00&factor%5Bzlh_hr%5D=21.00&factor%5Bzlh_p%5D=240.00&factor%5Bkpw_hr%5D=17.00&factor%5Bkpw_p%5D=300.00&factor%5Bppw_hr%5D=13.50&factor%5Bppw_p%5D=220.00&factor%5Bx25x_hr%5D=1.10&factor%5Bx25x_p%5D=230.00&factor%5Bmtp_hr%5D=0.00&factor%5Bmtp_p%5D=0.00&factor%5Bvh_hr%5D=0.42&factor%5Bvh_p%5D=150.00&factor%5Bcost%5D=0.1&sort=Profitability24&volume=0&revenue=24h&factor%5Bexchanges%5D%5B%5D=&factor%5Bexchanges%5D%5B%5D=binance&factor%5Bexchanges%5D%5B%5D=bitfinex&factor%5Bexchanges%5D%5B%5D=bitforex&factor%5Bexchanges%5D%5B%5D=bittrex&factor%5Bexchanges%5D%5B%5D=dove&factor%5Bexchanges%5D%5B%5D=exmo&factor%5Bexchanges%5D%5B%5D=gate&factor%5Bexchanges%5D%5B%5D=graviex&factor%5Bexchanges%5D%5B%5D=hitbtc&factor%5Bexchanges%5D%5B%5D=hotbit&factor%5Bexchanges%5D%5B%5D=ogre&factor%5Bexchanges%5D%5B%5D=poloniex&factor%5Bexchanges%5D%5B%5D=stex&dataset=Main&commit=Calculate) it seems like it is the fastest hashing algorithim out there?

# Discussion History
## Spudz76 | 2021-05-17T20:14:13+00:00
Cuckaroo does hashing in the Gigahash range.  Hashrates don't mean anything when compared across algorithms so I'm unsure how any of them could be "fastest"...

Also, no, the only Ethash-like algo supported in xmrig is KawPow.

## Joe23232 | 2021-05-19T14:01:34+00:00
Hi @Spudz76 

But then according to this website:

![image](https://user-images.githubusercontent.com/34926497/118825989-7a6b7a00-b8fe-11eb-95a7-135a8ccf82e7.png)


It actually shows Ethash-4G being the fastest though so I kinda don't quite understand. and thanks anyways

## SChernykh | 2021-05-19T14:04:58+00:00
There is no such algorithm and I have no idea what they mean by this. Ethash in 4 GB GPUs running in x16 slot maybe? Anyway, xmrig doesn't support Ethash.

## Joe23232 | 2021-05-19T14:14:29+00:00
What would be the fastest hashing algorithim xmrig supports if you happen to know @SChernykh ?

## SChernykh | 2021-05-19T14:21:52+00:00
This question doesn't make any sense. You must be new in mining. Choose the algorithm that is the most profitable for your hardware, even if it does just 1 hash/second.

## Joe23232 | 2021-05-19T14:23:03+00:00
Which one would be the most profitable on multilple non-gaming hardware?

## SChernykh | 2021-05-19T14:26:11+00:00
I don't know. I depends on the exact model of CPU or GPU. Try https://www.google.com/

## Spudz76 | 2021-05-19T22:25:35+00:00
hash rate is not like miles per hour.

Depends on the algo and how much that algo's coin is worth when you plan on selling/trading it.

Some pools handle all the profit questions for you  and payout XMR for every coin, but I shill for them enough as-is.  You can find them...

## Joe23232 | 2021-05-20T11:21:32+00:00
Which coin (using this software) would you recommend though for multiple
pool mining non-gaming computers?

On Thu, May 20, 2021 at 8:25 AM Tony Butler ***@***.***>
wrote:

> hash rate is not like miles per hour.
>
> Depends on the algo and how much that algo's coin is worth when you plan
> on selling/trading it.
>
> Some pools handle all the profit questions for you and payout XMR for
> every coin, but I shill for them enough as-is. You can find them...
>
> —
> You are receiving this because you authored the thread.
> Reply to this email directly, view it on GitHub
> <https://github.com/xmrig/xmrig/issues/2387#issuecomment-844538412>, or
> unsubscribe
> <https://github.com/notifications/unsubscribe-auth/AIKO7IMI4ADN2HNTNHEOQNLTOQ3G7ANCNFSM45AIIKPQ>
> .
>


## snipeTR | 2021-05-20T11:47:08+00:00
There is no answer to this question. this is personal.
what's your hardware
how much investment money do you have?
how much risk do you want to take?
What is the value of the crypto you want to mine?
how much do you expect it to be worth in the future?
how cold is your city
How much is the energy cost in your city?
How long will you have to pay for it?
https://i.stack.imgur.com/olGrH.gif

## Joe23232 | 2021-05-20T12:41:01+00:00
Ok lets say if the vast majority of PCs will have a standard AMD graphics card (something like ATI or something).

Lets take running expenses out of the equation and lets say it gets very cold in the winter and very hot in the summer.

> What is the value of the crypto you want to mine?

Can you please recommend me a good value of cryptocurrency where there are not many cryptominers out there and it is easy to mine for the following supported: "RandomX, KawPow, CryptoNight and AstroBWT"?

## DeeDeeRanged | 2021-05-30T08:16:12+00:00
As the sreenshot is from whattomine.com it is quite obvious your Fury 4GB doesn't cut it anymore and it is a powerhog with 220W looking at the profitability as you can see from the Rev. $ Profit column. Ethash4G is mining ethash (ethereum) with 4GB GPU's. There are only a few miners supporting ethereum 4GB GPU's. AFAIK PhoenixMiner/TeamRedMiner as they use something like zombie mode and over time it gives diminishing returns. From whattomine charts it looks like Ravencoin (RVN) is the best option, see https://xmrig.com/docs/algorithms for algos supported by xmrig, and if you want something of ethereum only option is then EthereumClassic (ETC)
I have 2 AMD secondhand/used cards a R9 390X 8GB using 162W and a RX 580 8GB using 96W both mining etherueum ethash at 61MH/s total.My apologies if I seem a bit blunt.

# Action History
- Created by: Joe23232 | 2021-05-17T11:23:27+00:00
- Closed at: 2025-06-16T18:47:21+00:00
