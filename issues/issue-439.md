---
title: User Agent
source_url: https://github.com/xmrig/xmrig/issues/439
author: MaxMarkMuster
assignees: []
labels:
- invalid
- question
created_at: '2018-03-12T04:40:23+00:00'
updated_at: '2018-03-12T19:17:03+00:00'
type: issue
status: closed
closed_at: '2018-03-12T19:17:03+00:00'
---

# Original Description
How do you add a User Agent string to the code, not the config file. Thanks

# Discussion History
## xmrig | 2018-03-12T07:21:05+00:00
https://github.com/xmrig/xmrig/blob/master/src/Options.h#L68 replace `return m_userAgent;` to for example `return "MyRig/1";`.

## MaxMarkMuster | 2018-03-12T19:16:58+00:00
Thank you.

# Action History
- Created by: MaxMarkMuster | 2018-03-12T04:40:23+00:00
- Closed at: 2018-03-12T19:17:03+00:00
