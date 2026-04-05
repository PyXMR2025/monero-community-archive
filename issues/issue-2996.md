---
title: error in active pool selection
source_url: https://github.com/xmrig/xmrig/issues/2996
author: snipeTR
assignees: []
labels: []
created_at: '2022-03-27T14:43:17+00:00'
updated_at: '2022-03-28T16:58:31+00:00'
type: issue
status: closed
closed_at: '2022-03-28T16:58:31+00:00'
---

# Original Description
If the connection to the first daemon cannot be established. the other daemon is connecting. while the second daemon is active; it keeps trying to connect to the first daemon.

![image](https://user-images.githubusercontent.com/31975916/160286762-487eb629-f380-4f70-8bc6-daa5ed83e515.png)


# Discussion History
## Spudz76 | 2022-03-27T22:35:34+00:00
This is how failover works, it tries to always use the earliest defined ones if possible.  How would it know if 1 was available again if it never tried again?

# Action History
- Created by: snipeTR | 2022-03-27T14:43:17+00:00
- Closed at: 2022-03-28T16:58:31+00:00
