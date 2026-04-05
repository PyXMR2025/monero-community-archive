---
title: Huge Pages available but not enabled.
source_url: https://github.com/xmrig/xmrig/issues/677
author: ganapathy-mani
assignees: []
labels:
- question
created_at: '2018-06-04T17:42:06+00:00'
updated_at: '2018-06-17T17:54:56+00:00'
type: issue
status: closed
closed_at: '2018-06-17T17:54:56+00:00'
---

# Original Description
I am using windows 10. I compiled and built XMRig miner but the huge pages are available and there is no enable next to the available. 

I started xmrig as an admin. Rebooted the computer after first start. 

![capture](https://user-images.githubusercontent.com/7914346/40932658-eb8785b8-67e3-11e8-8eb1-fb3cc3e78832.PNG)


# Discussion History
## rtau | 2018-06-05T01:11:01+00:00
Update: It should be a line start with "READY" like below, which "12/12" indicates the hugepages allocated/needed.

    READY (CPU) threads 6(6) huge pages 12/12  100% memory 24.0 MB

From  2.6, the hugepages are allocated by each thread, thus it's not a simple yes/no toggle. Take a look on the statistics line then you'll find something like "2/2", which indicates both threads have hugepages enabled.

## xmrig | 2018-06-05T02:04:12+00:00
#614 

# Action History
- Created by: ganapathy-mani | 2018-06-04T17:42:06+00:00
- Closed at: 2018-06-17T17:54:56+00:00
