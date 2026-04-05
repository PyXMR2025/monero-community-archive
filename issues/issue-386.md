---
title: 'Thread Collapsing '
source_url: https://github.com/xmrig/xmrig/issues/386
author: wesleyvankomen
assignees: []
labels: []
created_at: '2018-02-05T04:11:24+00:00'
updated_at: '2018-02-06T06:44:38+00:00'
type: issue
status: closed
closed_at: '2018-02-06T06:44:38+00:00'
---

# Original Description
I'm having trouble with my Gigabyte Vega 56 Gaming Pro and xmrig. The miner will work great for about an hour or two, but then the two threads specified for the card end up glitching out and merging into one high hash thread and a n/a thread. Not sure if it is the card or the program, but I'm going to test to see if it happens on xmr-stak-amd as well.
<img width="489" alt="screen shot 2018-02-04 at 7 49 00 pm" src="https://user-images.githubusercontent.com/10543162/35788053-812c500e-09e7-11e8-87b2-3baff8062f78.png">
<img width="491" alt="screen shot 2018-02-04 at 8 04 28 pm" src="https://user-images.githubusercontent.com/10543162/35788057-8395c424-09e7-11e8-8a90-dc8476bfe5d6.png">



# Discussion History
## wesleyvankomen | 2018-02-06T06:44:38+00:00
Okay, so reporting back. Same error occurred with xmr-stak but the program just crashed instead of becoming a single thread. Xmrig is actually way better in regards to keeping the mining rig going instead of letting a single card take down the whole operation.

I Iowered the GPU clock rate down from 1408 (~1580 stock) to 1300 and it has been stable for the last hour so far.

The issue is the card and not the software so I will close.

# Action History
- Created by: wesleyvankomen | 2018-02-05T04:11:24+00:00
- Closed at: 2018-02-06T06:44:38+00:00
