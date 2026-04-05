---
title: wrong cpu info with xeon e3-1240 under windows
source_url: https://github.com/xmrig/xmrig/issues/113
author: NmxMilk
assignees: []
labels: []
created_at: '2017-09-17T17:44:45+00:00'
updated_at: '2017-10-02T11:54:14+00:00'
type: issue
status: closed
closed_at: '2017-10-02T11:54:14+00:00'
---

# Original Description
First, let me congratulate you on the excellent work your doing and for sharing it!

I was user xmr-stak on my xeon e3-1240 and was getting 270 H/s.
Today i gave xmrig a chance to see if i get better performance but seems difficult to do more than that.

By the way, Xmrig was giving the wrong number of sockets and L2/L3 cache info (all zero in fact).
After investigating with libcpuid, it gives:
  num_cores  : 4
  num_logical: 8
  tot_logical: 4
The CPU is really 8 threads but hyper-threading is disabled under windows.
Taskmanager shows only four logical processors.

The problem seems to come from the fact that your deducing the number of sockets by :  tot_logical/ num_logical.
I suggest adding the following line after line 112 in cpu.cpp:
if (m_sockets == 0) m_sockets = 1; // at least one !

Thanks again

# Discussion History
## xmrig | 2017-10-02T11:54:14+00:00
Closed #86

# Action History
- Created by: NmxMilk | 2017-09-17T17:44:45+00:00
- Closed at: 2017-10-02T11:54:14+00:00
