---
title: bittube / ipbc support?
source_url: https://github.com/xmrig/xmrig/issues/700
author: bananajamma
assignees: []
labels:
- enhancement
created_at: '2018-06-21T22:37:06+00:00'
updated_at: '2018-07-12T05:00:25+00:00'
type: issue
status: closed
closed_at: '2018-07-11T19:17:26+00:00'
---

# Original Description
I stumbled across another cryptonight-based coin, and was wondering if you'd be interested in supporting it.  Currently their fork of xmr-stak has issues, not with the algorithm implementation, but their development/build process which requires not-LTS versions of ubuntu, and has issues with nvidia, and microhttpd.

I love your miner implementation, which is why I'm filing an issue here.  I won't be offended if you reject supporting this.

These are what I think are the meaningful commits:

* Initial implementation of BitTube POW v2 for CPU: https://github.com/ipbc-dev/bittube-miner/commit/835675f7d0c0ea8f059ab9217b2cec931e00829e
* Removed 128bit integer division from POW v2: https://github.com/ipbc-dev/bittube-miner/commit/b4b0091d3649408089ddf69e6acc726d03c81228
* Added OpenCL implementation of BitTube POW v2: https://github.com/ipbc-dev/bittube-miner/commit/0270fd19efea4b1616b3e5fd9ff2f06eac6689a2
* Added missing cryptonight_bittube2 checks: https://github.com/ipbc-dev/bittube-miner/commit/4e37cff71254923046e51c05268cb8b159731c0c

# Discussion History
## reeyon | 2018-06-22T11:20:17+00:00
This upcoming fork objectives are 3 antis..
Anti-fpga, anti-botnet a.k.a anti-cpu, and anti-asic.



## bananajamma | 2018-06-25T00:54:45+00:00
My use case is specifically for GPUs, but I figured getting it in xmrig would be the best way to get it merged into the GPU implementations.  I was not aware of the anti-cpu stance of the project, do you have more information on this?

## reeyon | 2018-06-25T02:23:17+00:00
This fork purpose is going to let GPU benefit from mining by all means.
bittube has added custom tweak for cn-heavy, so that GPU mining on Heavy will have more hashes compare to the ordinary xmr-stak, whereas CPU hashes will more lesser.

https://github.com/ipbc-dev/bittube-miner/commit/5182172f92421f481b13c5caccab99adbf61ea05
<credited to @Imperdin>

Haven is also using Imperdin tweak.(https://github.com/havenprotocol/haven/commit/be8648c318ad7622960e01f674208181219b5c63)






## imperdin | 2018-06-25T02:31:08+00:00
The main idea for the fork was to greatly hinder the current CPUs mining to de-incentive Botnets  
In addition to enable more room for Anti-FPGA measures and in addition to the Heavy 64 unint division

More tweaking to anti FPGAs are work in progress for but now breaking AES-NI and using efficient Heavy code is going to do the trick before dropping the real heavy hitter on FPGAs

Because CPUs are still needed for share verification they could still mine, but not profitably

## xmrig | 2018-06-25T10:13:30+00:00
Okay we got 3rd cn-heavy modification, any ETA when it will be live in mainnet? Anyway I can start work on it not earlier than next week.
@bananajamma Special thanks for information about this fork. Anti-cpu it's feature of cryptonight-heavy itself.

## Mila432 | 2018-06-25T11:26:20+00:00
@xmrig , they said on block 110000 so ~ 4 of July 

## bananajamma | 2018-06-26T01:18:55+00:00
Awesome news, thanks xmrig, and everybody that has contributed information to this issue.

## xmrig | 2018-07-11T19:17:26+00:00
Implemented in v2.6.4

## bananajamma | 2018-07-11T20:25:20+00:00
very much appreciate this!

Any ETA for it getting merged downstream into the AMD and nVidia variants?

## xmrig | 2018-07-11T20:44:48+00:00
Next week I'll start working on GPU versions and plan finish before the end of the month. Right now I have no AMD/NVIDIA GPUs around, but it will be resolved soon. Thank you.

## bananajamma | 2018-07-11T23:08:01+00:00
Thank you, you're awesome.  What's the best way to donate? XMR/BTC address in the README?

## xmrig | 2018-07-12T05:00:25+00:00
Actually donation in miners is ok, but for direct donation XMR/BTC addresses in README ok too.
Thank you.

# Action History
- Created by: bananajamma | 2018-06-21T22:37:06+00:00
- Closed at: 2018-07-11T19:17:26+00:00
