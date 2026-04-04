---
title: GUI 12.0 missing cmd line box in "Status" window
source_url: https://github.com/monero-project/monero-gui/issues/1278
author: BigslimVdub
assignees: []
labels:
- bug
created_at: '2018-04-06T00:59:17+00:00'
updated_at: '2018-04-27T20:35:52+00:00'
type: issue
status: closed
closed_at: '2018-04-27T20:35:52+00:00'
---

# Original Description
This box was there in 11.* versions but is missing from 12.0. 
It is on aeon rebase 1.7.2 so unsure what happened there unless xmr devs took it out for 12.0? 

![xmr 12_0 missing cmd line box](https://user-images.githubusercontent.com/30030687/38398773-b13f8768-390b-11e8-8021-8d6960ab4dcc.png)
![aeon 1_7_2 cmd line box](https://user-images.githubusercontent.com/30030687/38398789-c40d1ca2-390b-11e8-952e-e9f970b4c97d.png)


# Discussion History
## dEBRUYNE-1 | 2018-04-06T08:41:52+00:00
+bug

## Coded-Dude | 2018-04-06T15:35:12+00:00
The box still exists, and you can interact with it(you should get the windows text/font cursor when you mouse over where the box should be), but for some reason the CMD font is white(or otherwise invisible) unless you highlight it.  I am able to enter commands and get reports/feedback.

![cli_bugjpg](https://user-images.githubusercontent.com/19971145/38430186-281651d0-3986-11e8-84ca-ac257bb9e8b9.jpg)


## BigslimVdub | 2018-04-06T15:42:56+00:00
Completely blank on high Sierra. I do not get the cursor change. I have not tried on windows 10 yet. 

## sanderfoobar | 2018-04-07T19:37:01+00:00
#1292

## jamescanningcooke | 2018-04-10T07:28:37+00:00
It’s there but invisible. Click 

## guifalci | 2018-04-20T17:42:39+00:00
is not there on Mac High Sierra....

# Action History
- Created by: BigslimVdub | 2018-04-06T00:59:17+00:00
- Closed at: 2018-04-27T20:35:52+00:00
