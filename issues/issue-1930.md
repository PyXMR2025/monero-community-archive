---
title: Remove unable to open config warning
source_url: https://github.com/xmrig/xmrig/issues/1930
author: Maz4id
assignees: []
labels: []
created_at: '2020-11-05T00:16:01+00:00'
updated_at: '2021-01-03T17:05:46+00:00'
type: issue
status: closed
closed_at: '2020-11-05T09:15:15+00:00'
---

# Original Description
So I'm using 'Systemd' on linux to start xmrig with embedded config on it. It used to work perfectly until the last update. Now when I run xmrig it says:
**[2020-11-05 00:08:21.368] unable to open "/var/tmp/config.json".
[2020-11-05 00:08:21.369] unable to open "/root/.xmrig.json".
[2020-11-05 00:08:21.369] unable to open "/root/.config/xmrig.json".**
Systemd considers this an error and basically, it doesn't start anymore. I just want to know how to remove that message thanks. 

# Discussion History
## xmrig | 2020-11-05T07:36:41+00:00
You can remove this message, by removing this line https://github.com/xmrig/xmrig/blob/master/src/base/io/json/JsonChain.cpp#L84 but it is strange this message was in all previous versions, but just one not 3.
Thank you.

# Action History
- Created by: Maz4id | 2020-11-05T00:16:01+00:00
- Closed at: 2020-11-05T09:15:15+00:00
