---
title: 'donate.v2.xmrig.com:3333 DNS error: "no such file or directory"'
source_url: https://github.com/xmrig/xmrig/issues/3442
author: ac615223s5
assignees: []
labels: []
created_at: '2024-03-13T05:58:40+00:00'
updated_at: '2025-02-23T10:53:00+00:00'
type: issue
status: closed
closed_at: '2024-03-15T06:32:46+00:00'
---

# Original Description
**Describe the bug**
A clear and concise description of what the bug is.

**To Reproduce**
xmrig.exe

**Expected behavior**
A clear and concise description of what you expected to happen.

**Required data**
[2024-03-13 01:57:28.223]  net      donate.v2.xmrig.com:3333 DNS error: "no such file or directory"


**Additional context**
Add any other context about the problem here.


# Discussion History
## SChernykh | 2024-03-14T07:51:22+00:00
Use OpenDNS servers instead of your regular DNS from your internet provider.

## Pythdevver | 2024-03-15T07:12:40+00:00
Try to ping some other server with cmd.exe, maybe it's an accident network failure.

## itscz-org | 2025-02-23T10:52:20+00:00
I just had the same issue with an older and the newest release. "nslookup pool.domain" just worked fine in CMD. However, i tried to disable my piHole and yes, that helped. Seems there are some other lookups beside the pool address that are blocked and the log info is just wrong. Maybe this can be improved. Hope that info helps.

# Action History
- Created by: ac615223s5 | 2024-03-13T05:58:40+00:00
- Closed at: 2024-03-15T06:32:46+00:00
