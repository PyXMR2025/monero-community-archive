---
title: Again seeing high CPU load on mainnet
source_url: https://github.com/monero-project/monero/issues/4835
author: arnuschky
assignees: []
labels: []
created_at: '2018-11-11T13:28:06+00:00'
updated_at: '2018-11-13T07:35:46+00:00'
type: issue
status: closed
closed_at: '2018-11-13T07:35:46+00:00'
---

# Original Description
We're again experiencing high CPU load on all our mainnet instances. Seems to be coming in spikes:

![image](https://user-images.githubusercontent.com/179920/48313503-db8f9580-e5bd-11e8-87d7-300b5701e496.png)

Present since ~Friday, worse today. Anyone else seeing this?

Related: #4618  (we're running the patched version, so this isn't the problem)

# Discussion History
## moneromooo-monero | 2018-11-11T14:02:04+00:00
Same info needed :) perf top output and a few stack traces in the culprits.


## dEBRUYNE-1 | 2018-11-11T16:05:41+00:00
>worse today

Note that there have been a lot of transactions today with a huge amount of inputs (i.e. >100).

## arnuschky | 2018-11-12T10:12:24+00:00
Ah that's the kind of info I was hoping for. Was too lazy to start tracing immediately. ;)

Admittedly I should have had a look in the pool first. I'll verify that this is the cause; if not I'll trace. 

## moneromooo-monero | 2018-11-12T10:56:19+00:00
Not really. If you only look at the data if there's no tx load, then those slow bits won't get fixed :)

## arnuschky | 2018-11-13T07:35:46+00:00
Spikes are gone, so it must have been the transactions @dEBRUYNE-1 mentioned. Closing this. Thanks everyone.

# Action History
- Created by: arnuschky | 2018-11-11T13:28:06+00:00
- Closed at: 2018-11-13T07:35:46+00:00
