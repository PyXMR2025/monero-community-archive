---
title: Segmentation fault (core dumped)
source_url: https://github.com/xmrig/xmrig/issues/1727
author: FurryOneLove
assignees: []
labels: []
created_at: '2020-06-10T07:53:02+00:00'
updated_at: '2020-08-19T01:15:33+00:00'
type: issue
status: closed
closed_at: '2020-08-19T01:15:33+00:00'
---

# Original Description
I don’t know what to do!


![9F71899F-3F7F-4359-926E-7455007226AA](https://user-images.githubusercontent.com/35347245/84241680-7b016b00-ab08-11ea-98b2-30fec72964aa.jpeg)


# Discussion History
## downystreet | 2020-06-12T23:14:22+00:00
I'm not sure if you're joking or not but that CPU doesn't have the specs to mine with the randomX dataset. If you seriously wanted to continue to even try to use that processor upping your RAM to 4GB might work or even switching what OS you are using. If you are using an older or obscure version of Linux there may be a kernel conflict. But long story short I don't know why you would want to mine with that CPU unless your are just testing it because you aren't going to be earning much at all.

## Spudz76 | 2020-06-13T22:06:32+00:00
Needs 2082MB free RAM to run RandomX.  You have 2048MB total and barely any free.
Maybe other algos can do better (cn=pico? can fit in cache) but still probably not powerful enough even though they sip watts - the hash per watt ratio is still bad.  Can not earn more than input power cost unless somehow very free power but even then very low payout.  CN-Pico based coins generally don't trade up for much real value compared to other coins.  The scratchpad should be able to fit in cache, and that CPU has 512KB of L1 and that is all (very not much room) and is missing most cool x64 features (cut speed in half a few times even though it's 1.6GHz).

# Action History
- Created by: FurryOneLove | 2020-06-10T07:53:02+00:00
- Closed at: 2020-08-19T01:15:33+00:00
