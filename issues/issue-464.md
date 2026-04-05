---
title: Can I modify the number of threads or maximum CPU usage without exiting?
source_url: https://github.com/xmrig/xmrig/issues/464
author: webees
assignees:
- xmrig
labels:
- enhancement
created_at: '2018-03-20T07:26:40+00:00'
updated_at: '2019-03-12T02:12:43+00:00'
type: issue
status: closed
closed_at: '2019-03-12T02:12:43+00:00'
---

# Original Description
Hi, I hope the program will modify the number of threads during operation. Now I can only exit the program and reset the thread number and run. Thank you for your efforts. My Internet cafe running this software, but it should not affect the normal use of the computer, so i need to dynamically adjust the number of threads.

I tried App::close() and then recreated the thread to run, but it always went wrong.

# Discussion History
## xmrig | 2018-03-20T09:41:57+00:00
Dynamic config reload will be added in next release v2.6 if not something big like recent Monero PoW change happen again.
Thank you.

## jvds123 | 2018-03-25T10:32:43+00:00
love the idea, was just about to ask about the same but on max-cpu-usage
tumbs up

# Action History
- Created by: webees | 2018-03-20T07:26:40+00:00
- Closed at: 2019-03-12T02:12:43+00:00
