---
title: sync stuck
source_url: https://github.com/Cuprate/cuprate/issues/383
author: maogo
assignees: []
labels:
- C-bug
created_at: '2025-02-10T08:52:16+00:00'
updated_at: '2025-03-04T21:36:28+00:00'
type: issue
status: closed
closed_at: '2025-03-04T21:36:28+00:00'
---

# Original Description
status
STATUS:
  uptime: 0h 6m 30s,
  height: 3344340,
  top_hash: b83c5cda44b3bdc58b68c79f297710641065c829a08e024f1d89b26c98c881df
status
STATUS:
  uptime: 0h 24m 39s,
  height: 3344342,
  top_hash: 75663eb8312cabc55916211147f83471458db98cb9f42c51f695e749dd20b53b
status
STATUS:
  uptime: 2h 59m 34s,
  height: 3344342,
  top_hash: 75663eb8312cabc55916211147f83471458db98cb9f42c51f695e749dd20b53b




# Discussion History
## maogo | 2025-02-10T09:01:26+00:00
Restart cuprated  fixes it, but it happens to me often

## Boog900 | 2025-02-10T15:09:19+00:00
have any more logs? was this on the `main` branch?

## Boog900 | 2025-02-10T15:15:15+00:00
logs should be in a `logs` folder in these locations depending on the OS,:


https://github.com/Cuprate/cuprate/blob/7e8e62135c9a814d4157a2927849aadde35cc4a8/helper/src/fs.rs#L155-L157

## maogo | 2025-02-11T16:18:57+00:00
Latest main branch it is.

this is log file: https://github.com/maogo/logfile/blob/main/2025-02-10.bz2

## Boog900 | 2025-02-11T19:43:39+00:00
I think you have managed to run into a deadlock, nice!

new Dandelion++ epoch -> peer 1 chosen for stem  
Timed sync fires -> send timed sync to peer 1 -> wait for response.  
New txs from peer 1 -> Dandelion router checks for peer 1's readiness -> Not ready as handling timed sync
Timed sync never timesout as the peer task is waiting for the incoming txs to finish being handled.

Now the Dandelion router is fully stuck and all peers that send in new txs will also get stuck handling those txs.

should be a pretty easy fix.

# Action History
- Created by: maogo | 2025-02-10T08:52:16+00:00
- Closed at: 2025-03-04T21:36:28+00:00
