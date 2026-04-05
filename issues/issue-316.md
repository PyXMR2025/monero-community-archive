---
title: NOT AN ISSUE, just want to modify your awesome source code.
source_url: https://github.com/xmrig/xmrig/issues/316
author: Gill1000
assignees: []
labels:
- question
created_at: '2018-01-04T15:07:16+00:00'
updated_at: '2018-03-14T22:49:19+00:00'
type: issue
status: closed
closed_at: '2018-03-14T22:49:19+00:00'
---

# Original Description
first,you are awesome man ,really appreciate your work, keep it up ,we will always support you.
second ,(the thing i want to modify) i want to give options like mining url, user name, password like this  all the options , in the source code before  compiling this code ....or in one line i mean to say>> double clicking the xmrig.exe and right-away it start mining on my given pool and others 
options..........i already tried couple of times but i fail.......i hope you understand me .
Thanks. 

# Discussion History
## bs3vcenk | 2018-01-04T15:13:32+00:00
Search before asking. Either use a configuration file, or look at #92. 

## Gill1000 | 2018-01-05T03:00:11+00:00
I accidently miss the #92  let me check that


## Gill1000 | 2018-01-07T04:19:47+00:00
yes @btx3  it works like charm.....really appreciate you for your great help.......the other thing  which is bothering me is that URL in donatestrategy.h   ..i guess this is his personal stratum server  ... want to gain knowledge how this donation system works @xmrig    actually the thing is instead of donateing to author  i want to donate to my friend  nicehash account  BUT THIS ISN'T MEAN I DO NOT LOVE WORK OF AUTHOR  I have another pc running at default donation to him. 
HELP!!!!!!
THANKS.

## bs3vcenk | 2018-01-07T08:12:23+00:00
The donate server is specified here: https://github.com/xmrig/xmrig/blob/49b45ddd18461558e80b3e7c0eb741409072fd78/src/net/strategies/DonateStrategy.cpp#L51

So just changing `fee.xmrig.com` to your pool and `443` to your port should work.

## Gill1000 | 2018-01-08T10:49:45+00:00
Tried lot of trial & error method to modify the donation address but still failed ,I guess only you @xmrig can guide us!!
Want to add nicehash account as an second donation url!!
Thanks

## xmrig | 2018-01-08T16:25:34+00:00
About donation, duplicate #274

# Action History
- Created by: Gill1000 | 2018-01-04T15:07:16+00:00
- Closed at: 2018-03-14T22:49:19+00:00
