---
title: Affinity xmrig or system problem
source_url: https://github.com/xmrig/xmrig/issues/3268
author: dawidmosk
assignees: []
labels:
- question
created_at: '2023-05-14T12:00:23+00:00'
updated_at: '2023-06-07T14:55:02+00:00'
type: issue
status: closed
closed_at: '2023-06-07T14:55:02+00:00'
---

# Original Description
I know system affinity is more important like program but how it work in real life? Which option is more stable/real/correct? For example
1. cpu 8 cores, xmrig using 2,3,4,5,6,7 and system affinity 2,3,4,5,6,7 expected used: 2,3,4,5,6,7 
2. cpu 8 cores, xmrig using 0,1,2,3,4,5,6,7 and system affinity 2,3,4,5,6,7 expected used: 2,3,4,5,6,7 
3. cpu 8 cores, xmrig using 2,3,4,5,6,7 and system affinity 0,1,2,3,4,5,6,7 expected used: 2,3,4,5,6,7 
We talking about win10+. On option 3 notitied using 100% ?!?!



# Discussion History
## SChernykh | 2023-05-15T07:32:52+00:00
> On option 3 notitied using 100% ?!?!

100% for xmrig or the whole system? xmrig can't use 100% if it's not running all 8 threads. The best option is to leave it to xmrig to auto configure.

## dawidmosk | 2023-05-15T08:49:09+00:00
> 100% for xmrig or the whole system? **xmrig can't use 100% if it's not running all 8 threads**. The best option is to leave it to xmrig to auto configure.

Yes, but not always working correct settings (depends hardware drivers/machine) - that's why my question. Yes, not 100% because some % is for system. System is hanging because priority i to not everything.

Maybe another way: if i choice option 3 it will always work and get free - low usage - 0,1 cores?




## SChernykh | 2023-05-15T09:23:47+00:00
Option 3 should always leave cores 0,1 unused by XMRig. If they're still used, it's some other program or system itself.

# Action History
- Created by: dawidmosk | 2023-05-14T12:00:23+00:00
- Closed at: 2023-06-07T14:55:02+00:00
