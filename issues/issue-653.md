---
title: Performance regression 0.9.0->0.9.1
source_url: https://github.com/monero-project/monero/issues/653
author: iamsmooth
assignees: []
labels: []
created_at: '2016-02-10T12:06:52+00:00'
updated_at: '2016-02-11T18:53:52+00:00'
type: issue
status: closed
closed_at: '2016-02-11T18:53:52+00:00'
---

# Original Description
Reported by equipoise on bitcointalk

https://bitcointalk.org/index.php?topic=583449.msg13836518#msg13836518

> > My blockchain got corrupted when the electricity stopped. I resynced from scratch and it took about 24 hours. Previously I resynced from scratch a few times on the same machine on the same USB3 external hdd and on the same internet connection for 1-3 hours (it was on bitmonerod 0.9.0 tagged and before tagged, not 0.9.1). What could be the issue with the slow sync this time? 
> 
> I'm not sure I'm understanding. Are you using the same version as before?
> What CPU do you have?

I'm using 0.9.1 now. Previous times I was using 0.9.0 tagged and previous version (0.9.0 before tagged). Windows 7 64x. Mobile Core I7 (4 cores, 8 logical cores, 6 MB cash, with AES-NI).


# Discussion History
## iamsmooth | 2016-02-11T18:53:51+00:00
Reported resolved by using a higher nblocks-per-sync

https://bitcointalk.org/index.php?topic=583449.msg13851403#msg13851403


# Action History
- Created by: iamsmooth | 2016-02-10T12:06:52+00:00
- Closed at: 2016-02-11T18:53:52+00:00
