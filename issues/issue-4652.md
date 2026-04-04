---
title: Why is mixin even and total signatures odd?
source_url: https://github.com/monero-project/monero/issues/4652
author: ChloeMackey
assignees: []
labels:
- invalid
created_at: '2018-10-18T18:52:23+00:00'
updated_at: '2018-10-19T08:57:02+00:00'
type: issue
status: closed
closed_at: '2018-10-19T08:57:02+00:00'
---

# Original Description
Sorry if this has been answered before. I must be confused, If half of the mixen is from 1.8 days and the other half is after 1.8 days, wouldn't it be trivial to half your security by looking at which group is higher, the pre 1.8 days vs post 1.8 days group? Today, the mixen is 10 so total signatures 11, that means if i make a transaction after a day, 6 of my total sig will be pre 1.8 days and 5 would be post 1.8 days.

# Discussion History
## ChloeMackey | 2018-10-18T19:28:50+00:00
Is what I'm talking about a legacy problem and we have since switched to a gamma distribution decoy picking? https://github.com/monero-project/monero/blob/master/src/wallet/wallet2.cpp#L6996

## SamsungGalaxyPlayer | 2018-10-18T19:35:05+00:00
Yes

## ChloeMackey | 2018-10-18T19:35:16+00:00
Answered my own question, looks like we switched to gamma distribution.

"Furthermore, Monero has redesigned their GUI settings, implemented a faster wallet refresh and gamma distribution for ring selection"

https://blocklr.com/news/monero-xmr-hard-fork/ 

## ChloeMackey | 2018-10-18T19:35:40+00:00
Thanks!

## moneromooo-monero | 2018-10-18T20:06:48+00:00
The code allocated the right amount depending on the age of the real output:

      if (td.m_global_output_index >= num_outs - num_recent_outs && recent_outputs_count > 0)
        --recent_outputs_count; // if the real out is recent, pick one less recent fake out


## moneromooo-monero | 2018-10-18T20:07:28+00:00
Also, "whole chain" can pick in the last 1.8 days too.

## ChloeMackey | 2018-10-18T20:44:19+00:00
Thank you, how did we get the gamma parameters? https://github.com/monero-project/monero/blob/master/src/wallet/wallet2.cpp#L6779

## moneromooo-monero | 2018-10-18T20:51:42+00:00
They are from a paper from Miller et al, I don't have a link right now.

## ChloeMackey | 2018-10-18T21:52:49+00:00
https://arxiv.org/pdf/1704.04299/ this guy?

## moneromooo-monero | 2018-10-18T22:32:32+00:00
That's the one (well, a previous version) - fig 11.


## moneromooo-monero | 2018-10-19T08:45:09+00:00
+invalid

# Action History
- Created by: ChloeMackey | 2018-10-18T18:52:23+00:00
- Closed at: 2018-10-19T08:57:02+00:00
