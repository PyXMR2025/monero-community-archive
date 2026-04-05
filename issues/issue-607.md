---
title: donation not working
source_url: https://github.com/xmrig/xmrig/issues/607
author: focaeppe
assignees: []
labels:
- bug
created_at: '2018-05-06T10:04:41+00:00'
updated_at: '2018-05-06T19:44:25+00:00'
type: issue
status: closed
closed_at: '2018-05-06T19:44:25+00:00'
---

# Original Description
Hello,
![2018-05-06_23-57-29](https://user-images.githubusercontent.com/34982607/39672163-38e5c5f2-5125-11e8-9646-113474f7dcc6.jpg)
levels 99% donation don't start
donation is 97%  doesnt donating after 6 min.


# Discussion History
## dunklesToast | 2018-05-06T17:05:54+00:00
I think the donation system got some randomization some versions ago so it takes some time for it to start. What happens, if you wait ~10 min?

## Gill1000 | 2018-05-06T18:04:01+00:00
Check #519

## xmrig | 2018-05-06T19:13:18+00:00
It really epic bug, so v2.6.1 is donation free, because algorithm validation broken for donations.
Thank you.

## xmrig | 2018-05-06T19:44:25+00:00
I make release v2.6.2 with the fix.
Start time is randomized, but only +/- 50%, so for level 99% it from 30 to 90 seconds, for 97% it from 1.5 minutes to 4.5 minutes.
Thank you.

# Action History
- Created by: focaeppe | 2018-05-06T10:04:41+00:00
- Closed at: 2018-05-06T19:44:25+00:00
