---
title: Stuck on "Loading blockchain from folder /home/user/.bitmonero/lmdb ..."
source_url: https://github.com/monero-project/monero/issues/8146
author: ghost
assignees: []
labels: []
created_at: '2022-01-18T04:51:04+00:00'
updated_at: '2022-01-18T06:07:07+00:00'
type: issue
status: closed
closed_at: '2022-01-18T06:07:07+00:00'
---

# Original Description
I ran out of space on my main HDD, so I moved data.mdb to an external drive and created a symlink to it:
```
 ~/.bitmonero/lmdb ls -l
total 8
lrwxrwxrwx 1 conner conner   76 Jan 17 22:37 data.mdb -> '/media/conner/BFAB-3292/Conner/storage/Archive/Monero Database/lmdb/data.mdb'
-rw-r--r-- 1 conner conner 8192 Jan 17 22:42 lock.mdb
 ~/.bitmonero/lmdb 
```

Now when I run:
```
2022-01-18 04:49:25.735	I Monero 'Oxygen Orion' (v0.17.3.0-release)
2022-01-18 04:49:25.735	I Initializing cryptonote protocol...
2022-01-18 04:49:25.735	I Cryptonote protocol initialized OK
2022-01-18 04:49:25.736	I Initializing core...
2022-01-18 04:49:25.737	I Loading blockchain from folder /home/conner/.bitmonero/lmdb ...
```
`monerod` gets stuck on that last line.

# Discussion History
## ghost | 2022-01-18T06:07:04+00:00
Wasn't stuck, loglevel 4 reveals it had to reinitialize a bunch of stuff

# Action History
- Created by: ghost | 2022-01-18T04:51:04+00:00
- Closed at: 2022-01-18T06:07:07+00:00
