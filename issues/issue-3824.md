---
title: Monero bockchain import batch increase
source_url: https://github.com/monero-project/monero/issues/3824
author: ph4r05
assignees: []
labels: []
created_at: '2018-05-17T19:06:11+00:00'
updated_at: '2018-06-16T20:13:44+00:00'
type: issue
status: closed
closed_at: '2018-05-18T10:46:30+00:00'
---

# Original Description
Hi,

I was experimenting a bit with starting a full node from scratch using blockchain import from downloaded `blockchain.raw`.

I noticed the main bottleneck is the DB commit. The default batch size value is set to 100, which took around 20 seconds to commit on older hardware (2.2 GHz, 5 GB RAM, HDD, in virtualbox). With the current height of 1.5M it would take 3.5 days to do the full sync. I've set the `batch-size` to 10000 which takes around 180 seconds to commit. With this, I achieved 12x speed improvement, in total full sync in 7 hours (maybe for a price of higher RAM usage?).

It would be nice to test if these observations generalize on different HW configurations and if it is so, increase a default value a bit or mention this in the manual. Having the more full nodes running is the better so making initial sync less painful is of high importance.


# Discussion History
## moneromooo-monero | 2018-05-18T10:20:08+00:00
Feel free to rope people in testing this with a variety of hardware (CPU, network, and especially SSD/HDD).

## ph4r05 | 2018-05-18T10:46:30+00:00
I was thinking about increasing batch size from 100 to 1000. But for now it is at least googable, so closing the issue. 

## hyc | 2018-05-19T04:36:50+00:00
Increasing the batch size certainly increases the RAM requirement. In this case it may cause a system with not enough RAM to start swapping, which would be self-defeating.

## mmortal03 | 2018-06-16T00:01:53+00:00
@hyc , would a potential workaround to the following bug be to decrease the batch-size substantially?
https://github.com/monero-project/monero/issues/2732

## hyc | 2018-06-16T06:36:46+00:00
No, there's no evidence that the amount of private memory is excessive in that ticket.

## mmortal03 | 2018-06-16T20:13:44+00:00
@hyc , maybe I'm misunderstanding you, but I can provide more detailed evidence of it happening on Windows if you need it. I'll comment over on that ticket in more depth, but I've done some testing overnight, and lowering the batch-size to, say, 100, while it definitely doesn't solve the overall issue (I may have a workaround for that), still causes it to use a little less system RAM before it hits the maximum amount, after which it starts swapping to disk. My testing shows that *anything* you can do to prolong it from swapping to disk is crucial when importing the chain from scratch.

# Action History
- Created by: ph4r05 | 2018-05-17T19:06:11+00:00
- Closed at: 2018-05-18T10:46:30+00:00
