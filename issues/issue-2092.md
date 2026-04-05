---
title: 'Task Manager doens''t show RAM used for xmrig '
source_url: https://github.com/xmrig/xmrig/issues/2092
author: ghost
assignees: []
labels:
- question
created_at: '2021-02-09T21:51:52+00:00'
updated_at: '2021-04-12T14:16:35+00:00'
type: issue
status: closed
closed_at: '2021-04-12T14:16:35+00:00'
---

# Original Description
I have just downloaded and tested newest xmrig and I realized that my task manager doesn't show RAM usage for xmrig process, it shows just 10MB but mining is working with this same hashrate like on xmrig 6.5.3, 6.5.3 version normally shows RAM usage in Task Manager

# Discussion History
## SChernykh | 2021-02-09T23:49:45+00:00
Windows task manager doesn't show huge pages allocations for some reason. If you run xmrig without huge pages it'll show more than 2 GB used.

# Action History
- Created by: ghost | 2021-02-09T21:51:52+00:00
- Closed at: 2021-04-12T14:16:35+00:00
