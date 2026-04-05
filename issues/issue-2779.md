---
title: How to Fix this DNS Error '  No Addrees'
source_url: https://github.com/xmrig/xmrig/issues/2779
author: besskyy
assignees: []
labels:
- bug
created_at: '2021-12-03T07:40:51+00:00'
updated_at: '2025-06-16T20:25:20+00:00'
type: issue
status: closed
closed_at: '2025-06-16T20:25:20+00:00'
---

# Original Description
![IMG_20211203_083349](https://user-images.githubusercontent.com/95467778/144563933-5739b760-1686-41df-9c18-1e754937b197.jpg)


# Discussion History
## kazmek | 2021-12-07T00:31:53+00:00
Either the URL is wrong or try using a different DNS resolver. You can change it on your NIC or router. If your router was provided by your ISP, chances are you are using their DNS server. It could be being blocked since it's a mining site. I use PiHole as my DNS and one of the lists I pulled in blocked many of the mining pools. I have to manually whitelist stuff. That could be a source of problems for you too.

## Spudz76 | 2021-12-07T01:59:47+00:00
You have a space at the beginning of the hostname in the `url`

# Action History
- Created by: besskyy | 2021-12-03T07:40:51+00:00
- Closed at: 2025-06-16T20:25:20+00:00
