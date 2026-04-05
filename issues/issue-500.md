---
title: version 2.5.x stellite Low diffficulty share error
source_url: https://github.com/xmrig/xmrig/issues/500
author: exceler55
assignees: []
labels: []
created_at: '2018-04-04T22:04:43+00:00'
updated_at: '2018-04-05T10:10:24+00:00'
type: issue
status: closed
closed_at: '2018-04-05T10:10:24+00:00'
---

# Original Description
Hi, 
I set "variant" as 1 for Stellite, but the program returns the error "Low difficulty share" rejected. 
What's wrong? 

# Discussion History
## pikomule | 2018-04-05T06:40:31+00:00
only change "-1" for "1"

## pikomule | 2018-04-05T06:41:34+00:00
2.6.0 beta 1 ok for stellite

## xmrig | 2018-04-05T08:00:17+00:00
Both 2.5 and 2.6 should work fine for stellite.
@exceler55 `variant` is not global option, it applied for each pool separately. 

## exceler55 | 2018-04-05T10:10:24+00:00
Ah, I understand. It works fine. 
Sorry and thank you.


# Action History
- Created by: exceler55 | 2018-04-04T22:04:43+00:00
- Closed at: 2018-04-05T10:10:24+00:00
