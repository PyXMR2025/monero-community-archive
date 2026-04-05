---
title: How to make the compiled executable file smaller?
source_url: https://github.com/xmrig/xmrig/issues/869
author: ttsite
assignees: []
labels:
- question
created_at: '2018-11-04T14:49:23+00:00'
updated_at: '2018-11-05T08:53:48+00:00'
type: issue
status: closed
closed_at: '2018-11-05T06:41:23+00:00'
---

# Original Description
2.8x version of the compiled executable file is much larger than before, can you make the compiled executable file smaller?

# Discussion History
## xmrig | 2018-11-04T14:56:24+00:00
Use builds without SSL/TLS support, `-notls.exe`. 

## ttsite | 2018-11-05T02:20:03+00:00
Will there be any effect on mining if there is no SSL / TLS support? Thank you!

## xmrig | 2018-11-05T06:41:23+00:00
Answered multiple times, without SSL/TLS you can't connect to SSL/TLS ports on pool, all versions before 2.8 not support it.
Thank you.

## ttsite | 2018-11-05T08:53:48+00:00
thanks!!

# Action History
- Created by: ttsite | 2018-11-04T14:49:23+00:00
- Closed at: 2018-11-05T06:41:23+00:00
