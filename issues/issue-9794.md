---
title: seed node instability. restarts constantly
source_url: https://github.com/monero-project/monero/issues/9794
author: Gingeropolous
assignees: []
labels:
- more info needed
created_at: '2025-02-10T01:40:23+00:00'
updated_at: '2025-06-25T03:56:47+00:00'
type: issue
status: closed
closed_at: '2025-06-25T03:56:47+00:00'
---

# Original Description
so my seed node has been really unstable. monerod keeps restarting. on master, and on release, and on release binaries. I managed to get gdb running on a debug monerod (master). 

I'm leaning towards this being a hardware problem, but I've attached the gdb logs and the monerod logs.

[gdb_log.txt](https://github.com/user-attachments/files/18727181/gdb_log.txt)
[10klog_log.txt](https://github.com/user-attachments/files/18727180/10klog_log.txt)

# Discussion History
## Gingeropolous | 2025-02-10T01:41:09+00:00
i think this is captured in the gdb log, but this is what first crashes out:

0x00007ffff1130107 in mdb_page_search_root (mc=0x7fc3acd1e6e8, key=0x7fc3bfffc090, flags=0) at /home/mondaemon/monero/external/db_drivers/liblmdb/mdb.c:6385

## Gingeropolous | 2025-02-10T01:45:56+00:00
yeah here it is again:

Thread 14 "monerod" received signal SIGBUS, Bus error.
[Switching to Thread 0x7fc3edffa640 (LWP 743673)]
0x00007ffff1130107 in mdb_page_search_root (mc=0x7fc3c88ded18, key=0x7fc3edff7090, flags=0) at /home/mondaemon/monero/external/db_drivers/liblmdb/mdb.c:6385
6385            while (IS_BRANCH(mp)) {


## selsta | 2025-02-10T10:16:30+00:00
I would do a resync and if the issue continues to happen it might be a hardware issue.

## Gingeropolous | 2025-02-21T11:48:19+00:00
update - I'm running release branch with the 2 for 1 database thing, and it is still synchronizing. Has been synchronizing for days. The box this node is on has a secondary HDD, so I'm synchronizing to that. 

## Gingeropolous | 2025-06-25T03:56:47+00:00
hardware issue. syncd and has continued to run on a secondary HDD for a while now. 

# Action History
- Created by: Gingeropolous | 2025-02-10T01:40:23+00:00
- Closed at: 2025-06-25T03:56:47+00:00
