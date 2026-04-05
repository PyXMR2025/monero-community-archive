---
title: uptime is reset, but stats appear to keep
source_url: https://github.com/xmrig/xmrig/issues/712
author: DrStein99
assignees: []
labels:
- review later
created_at: '2018-07-02T16:15:12+00:00'
updated_at: '2019-08-02T13:12:59+00:00'
type: issue
status: closed
closed_at: '2019-08-02T13:12:59+00:00'
---

# Original Description
 The UPTIME appears to get reset on a connection fail, yet the hash total  and other stats save.  This throws off my stat-keeping.  Once the rig is up for and have accumulated stats, then the uptime zero's out, makes a big mess.  I am trying analyze my performance on any calculation of per-hour uptime.

Is there any solutions outside of me modifying the code myself?  I figure I would ask since it is possible I am overlooking a simple solution, and welcome to entertain replies for advice please.

# Discussion History
## xmrig | 2019-08-02T13:12:59+00:00
Recent versions also provide global uptime in API.
Thank you

# Action History
- Created by: DrStein99 | 2018-07-02T16:15:12+00:00
- Closed at: 2019-08-02T13:12:59+00:00
