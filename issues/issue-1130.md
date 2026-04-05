---
title: xmrig-notls what is this process and why is it taking up all my CPU?
source_url: https://github.com/xmrig/xmrig/issues/1130
author: jaekunchoi
assignees: []
labels:
- av
created_at: '2019-08-21T08:39:14+00:00'
updated_at: '2019-12-22T19:22:45+00:00'
type: issue
status: closed
closed_at: '2019-12-22T19:22:45+00:00'
---

# Original Description
I have this process xmrig-notls which is owned by Plesk.

I'm not sure why this is taking up more than 100% of my CPU resources for a few days now.
```
psaadm    20   0  461440   5188    800 S 111.3  0.1  12246:26 xmrig-notls
```

Does anyone know what it is and how I can manage this so it doesn't take up all my resources?

# Discussion History
## qutimqqcom | 2019-08-28T12:08:49+00:00
if the software is not installed by you, use an antivirus

if other read manual

## rjacksix | 2019-09-03T03:46:05+00:00
It is a cryptocurrency miner.  It has probably been dropped on your box by a bot.  Check your crontab for a base64 encoded job that is responsible for persistence.

Hope this helps

Happy hunting

## jangondol | 2019-10-03T12:36:10+00:00
FYI (for those coming here through web search): https://hub.docker.com/_/redis?tab=reviews (see the description of the infection through the official Redis Docker container and info about the fix).

# Action History
- Created by: jaekunchoi | 2019-08-21T08:39:14+00:00
- Closed at: 2019-12-22T19:22:45+00:00
