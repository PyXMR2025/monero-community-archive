---
title: Unable to mine MSR
source_url: https://github.com/xmrig/xmrig/issues/692
author: gnock
assignees: []
labels:
- enhancement
created_at: '2018-06-12T22:45:53+00:00'
updated_at: '2018-06-22T22:36:01+00:00'
type: issue
status: closed
closed_at: '2018-06-22T15:05:25+00:00'
---

# Original Description
Hi,

I was going to submit a PR to add support for the Masari variant, but i saw you did. I gave it a run and wasn't able to mine (test pool:testnet.masaricoin.com, already on the variant, accept even invalid address).

I tracked the problem to the worker not selecting the right variant (falling back to VARIANT_1).
Looking more closely at the code, pool.setAlgo is never called (only way i found to set the variant).
One solution is to modify CommonConfig.cpp (function finalize) and replace 

`pool.adjust(m_algorithm.algo());`
by
`pool.setAlgo(m_algorithm);
pool.adjust(m_algorithm.algo());`

Not sure it's the way you would have done it but it works.

If you need more info i can provide some.

Xmrig-proxy (with xmrig patched as above) works


# Discussion History
## xmrig | 2018-06-13T03:25:58+00:00
It works as expected, because `variant` is not global option and specified separately for each pool.
So config should looks like (only key options):
```json
{
  "algo": "cryptonight",
  "pools": [
        {
            "url": "testnet.masaricoin.com:3333",
            "variant": "msr"
        }
  ]
}
```
or command line: `xmrig.exe -a cn --url testnet.masaricoin.com:3333 --variant msr`

Also please take look to [extended job object](https://github.com/xmrig/xmrig-proxy/blob/master/doc/STRATUM_EXT.md#12-extended-job-object) part of mining algorithm negotiation, if pool adds `"algo":"cn/msr",` to each job object, variant on miner side become optional.
Thank you.

## gnock | 2018-06-13T11:04:58+00:00
Hi,

Effectively with --variant it works, i couldn't make it work yesterday, weird.
If you write `-a cn/msr` it doesn't. Is it the expected behaviour ? 

Eithercase, sorry for the inconvenience

## xmrig | 2018-06-14T11:46:38+00:00
Yes it is expected behavior, but you are right it's good to allow user specify global variant if per pool variant option not specified or set to automatic. I will fix it soon.
Thank you.

## xmrig | 2018-06-14T16:51:05+00:00
Next version will support syntax like: `xmrig.exe -a cn/msr --url testnet.masaricoin.com:3333`
Thank you.

## DrStein99 | 2018-06-22T12:12:35+00:00
I was mining version 2.6.2, received:

`rejected (0/1) diff 21000 "Low difficulty share" (147 ms)`

all over the place.  Just upgraded to version "2.6.4-dev".  Still the same thing - I have zero accepted shares and all rejects.  Here's my pool config:

`{       
 "url": "masari.superpools.net:5555",
"user": "myWalletAddress.21000",
 "pass": "x",
 "variant": "msr"
  },`

Is there something else I need to set somewhere else ?  is the "algo": "cryptonight", or should that be different too?


## gnock | 2018-06-22T15:05:25+00:00
I think this discussion should continue on the discord of Masari (https://discord.gg/eSb9ZdM).
Also, the admin of superpools he had no time to handle the pool anymore, so maybe use another pool. There is a list (unofficial) at masaripools.org

# Action History
- Created by: gnock | 2018-06-12T22:45:53+00:00
- Closed at: 2018-06-22T15:05:25+00:00
