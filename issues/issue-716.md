---
title: config.json new parameters meaining explanation is absent
source_url: https://github.com/xmrig/xmrig/issues/716
author: lisergey
assignees: []
labels:
- question
created_at: '2018-07-10T12:52:30+00:00'
updated_at: '2018-10-10T22:20:12+00:00'
type: issue
status: closed
closed_at: '2018-10-10T22:20:12+00:00'
---

# Original Description
It would be great to update Wiki about all new wonderfull params of config.json, that were added recently.
E.g. `watch: false` or `user-agent: null` - what is their meaning and what they change in behavior.

I've been searching in issues and in wiki - nothing found. I'm no expert to understand from reading the code. Thank you in advance, @xmrig.

# Discussion History
## xmrig | 2018-07-11T19:23:39+00:00
https://github.com/xmrig/xmrig-proxy/issues/119 same as watch feature in proxy, but this feature disabled in miner because reaction to config change not implemented, proxy and miner share same code base.

`user-agent` allow override default miner user agent from `XMRig/<version> ...` to something else.

# Action History
- Created by: lisergey | 2018-07-10T12:52:30+00:00
- Closed at: 2018-10-10T22:20:12+00:00
