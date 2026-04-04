---
title: can multi monerod r/w the same lmdb blockchain at the same time with different
  tor ip address？
source_url: https://github.com/monero-project/monero/issues/6137
author: 0xAu
assignees: []
labels: []
created_at: '2019-11-15T01:13:46+00:00'
updated_at: '2020-05-16T16:15:04+00:00'
type: issue
status: closed
closed_at: '2020-05-16T16:15:04+00:00'
---

# Original Description
I have some node run monerod trust each other and want to use the same monero blockchain lmdb file with NFS or other ways，at the same time，every monerod node own different tor ip，can achieve it？ in this way，we can create a lot of full nodes with different tor ip address. （effect is that you know there is many full nodes but you dont know accurate full node number）

# Discussion History
## moneromooo-monero | 2019-11-15T01:17:52+00:00
monerod will not run on NFS, unless some fancy version that has mmap support. Otherwise, a blockchain can be used by more than one monerod at the same time, though I doubt it's tested much.
Note that if two nodes work on the same db, they'll have the same blockchain state at all times, and that can be a way to link two tor peers if they never have some jitter in their update timing (probably requires constant active probing though).

## 0xAu | 2019-11-15T01:35:27+00:00
thanks for reply my preliminary idea，i will do some test by self when 0.15 released.

## hyc | 2019-11-15T03:20:47+00:00
0.15 was already released a few days ago. https://github.com/monero-project/monero/releases/tag/v0.15.0.0

Note: NFS *has* mmap support. But it doesn't guarantee cache coherency, which is what LMDB requires. AFAIK there are no remote filesystems that do.

## moneromooo-monero | 2020-05-16T16:15:04+00:00
No bug here.

# Action History
- Created by: 0xAu | 2019-11-15T01:13:46+00:00
- Closed at: 2020-05-16T16:15:04+00:00
