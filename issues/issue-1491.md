---
title: 'xmrig 5.5.0 periodical "Rejected share: invalid result"'
source_url: https://github.com/xmrig/xmrig/issues/1491
author: chelmedvedosvin
assignees: []
labels: []
created_at: '2020-01-08T13:05:50+00:00'
updated_at: '2021-04-12T15:03:54+00:00'
type: issue
status: closed
closed_at: '2021-04-12T15:03:54+00:00'
---

# Original Description
I have 64 rigs running on ubuntu with Intel(R) Celeron(R) CPU G3930 @ 2.90GHz and G3900
and 4 from them are producing such error (others work fine).
Screenshot: http://prntscr.com/qktr35
So pool ban my ip because of bad shares. How can I fix this trouble?

# Discussion History
## miner91 | 2020-01-10T10:39:50+00:00
> So pool ban my ip because of bad shares.

Don't use pools that bans your whole network because of couple invalid shares like supporxmr, it's stupid. I talked in the past with admin of supportxmr (m5m400), he told he will turn this off but didn't even increase the limit after which you will get temporarily banned. I use minexmr for couple years and never had a problem, I get couple invalids per day so it's not a big deal but I don't want my whole network to be off because of that for X minutes.

Use minerxmr pool.

>How can I fix this trouble?

First you must trace the source of problem.

Check temps, memory, use xmrig with debugging flag compiled and check the logs.



## chelmedvedosvin | 2020-01-10T12:23:11+00:00
I have created topology xml:
http://prntscr.com/qlrdqk

# Action History
- Created by: chelmedvedosvin | 2020-01-08T13:05:50+00:00
- Closed at: 2021-04-12T15:03:54+00:00
