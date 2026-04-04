---
title: POWER8 mining code
source_url: https://github.com/monero-project/monero/issues/2192
author: yuhong
assignees: []
labels:
- enhancement
created_at: '2017-07-23T03:42:43+00:00'
updated_at: '2018-01-08T12:48:34+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
POWER8 has AES instructions similar to Intel's. It is probably worth putting each architecture including ARM into a separate file.

# Discussion History
## hyc | 2017-07-23T12:52:57+00:00
Who's still buying IBM POWER machines? I can't imagine their H/s/W efficiency is very good, they tend to be pretty monstrous servers.

## ghost | 2017-08-02T11:26:19+00:00
POWER9 is apparently due to be released soon according to Mr. Wikipedia. Actually sounds quite good.

## peronero | 2017-08-09T01:37:11+00:00
I believe there is a push to use POWER in lieu of high-end products from US-based chipmakers in China and other states targeted by export restrictions and sanctions.

https://www.theregister.co.uk/2015/04/10/us_intel_china_ban/
http://wccftech.com/us-government-bans-intel-nvidia-amd-chips-china/
https://www.nytimes.com/2015/10/31/technology/us-tech-giants-may-blur-national-security-boundaries-in-china-deals.html

This is probably a worthwhile issue to tackle but a little tricky I suppose.


## astraleureka-zz | 2017-08-10T14:20:33+00:00
@hyc the new POWER9 stuff has 128MB L3 cache per socket, so it would actually be a great target here ;)

## hyc | 2017-08-10T14:35:50+00:00
IBM won't have POWER9 systems available until late next year. https://www.itjungle.com/2017/07/24/power-neine-conundrum/

I'd say POWER's days of relevance are over. It's targeted at servers only, and the number of deployed servers in the world is tiny compared to the number of workstations/PCs/laptops/phones. 128MB cache sounds good, but only up to 24 cores per chip. For CryptoNight that means most of that on-chip cache isn't even going to be touched. This is a chip designed for multiuser server workloads. Not single-user tasks.

## astraleureka-zz | 2017-08-10T14:44:40+00:00
It's 24 physical cores with 4-way SMT. There's the second iteration of the Talos workstation with POWER9 that claims to be fulfilling in Q4 2017, but the previous rendition was vapourware - we'll see what happens there. 

There's also POWER8 gear available now, and from vendors outside of IBM - check Tyan's single & dual socket offerings for example. It's not as great, but still 96MB L3 and 4-way SMT and multiple AES units per core. 

Unfortunately I don't have anything newer than POWER7 at my disposal, otherwise I would take a whack at this one. 

## nioroso-x3 | 2017-10-31T04:09:14+00:00
Hi,
I made an initial port for POWER8 of the xmr-stak-cpu miner:
https://github.com/nioroso-x3/xmr-stak-power
I hope it's useful!


## dEBRUYNE-1 | 2018-01-08T12:45:29+00:00
+enhancement

# Action History
- Created by: yuhong | 2017-07-23T03:42:43+00:00
