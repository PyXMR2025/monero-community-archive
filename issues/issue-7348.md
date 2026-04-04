---
title: Monerod keeps growing the database file regardless of the number of free pages
source_url: https://github.com/monero-project/monero/issues/7348
author: tevador
assignees: []
labels: []
created_at: '2021-01-24T23:59:49+00:00'
updated_at: '2021-02-20T23:28:04+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
My database has over 40 GB of empty space in it:

```
> ./mdb_stat -eff ~/.bitmonero/lmdb/
...
  Free pages: 10990719
Status of Main DB
  Tree depth: 1
  Branch pages: 0
  Leaf pages: 1
  Overflow pages: 0
  Entries: 18
```

4 KB pages * 11M > 40 GB

Yet monerod keeps insisting on growing the database file:

```
2021-01-24 20:42:31.640 D DB map size:     163662839808
2021-01-24 20:42:31.640 D Space used:      148498677760
2021-01-24 20:42:31.640 D Space remaining: 15164162048
2021-01-24 20:42:31.640 D Size threshold:  0
2021-01-24 20:42:31.640 D Percent used: 90.7345  Percent threshold: 90.0000
2021-01-24 20:42:31.640 I Threshold met (percent-based)
2021-01-24 20:42:31.640 E !! WARNING: Insufficient free space to extend database !!: 167 MB available, 1024 MB needed
```

I only noticed this issue because I ran out of disk space.

# Discussion History
## ruderod | 2021-02-20T06:20:02+00:00
https://symas.com/understanding-lmdb-database-file-sizes-and-memory-utilization/
i read it.  still not sure why it would have 40 gig of free entries.  monero blockchain changes that much?

## hyc | 2021-02-20T22:41:30+00:00
Mine has only 1037 free pages. You must be running something that's keeping long-lived read transactions, like that block explorer or something.

## tevador | 2021-02-20T23:11:02+00:00
Yes, but why does monerod keep growing the db file when there is clearly enough free space? This happens even when the block explorer is not running. Can't monerod see the empty space?

BTW I had to delete the whole blockchain and resync from scratch to reclaim those 40 GB.

## hyc | 2021-02-20T23:28:04+00:00
monerod doesn't know about the empty space. There is currently no LMDB API call that returns it as a count. The mdb_stat command has to count it up itself. I suppose this is a glaring omission from the API.

# Action History
- Created by: tevador | 2021-01-24T23:59:49+00:00
