---
title: deleted
source_url: https://github.com/xmrig/xmrig/issues/1513
author: Bilaboz
assignees: []
labels:
- question
created_at: '2020-01-23T23:44:39+00:00'
updated_at: '2020-08-28T16:42:09+00:00'
type: issue
status: closed
closed_at: '2020-08-28T16:42:09+00:00'
---

# Original Description
deleted

# Discussion History
## Spudz76 | 2020-01-27T20:42:02+00:00
Edit config file, there is no override from command line.
What cpu, generally threads are capped by cache size.  Regardless if a CPU has 80 cores, if there are not 2MB per core then you can only use up to cacheMB/2 threads.  So I'm guessing you have one of those 6-core 4MB cache ones where 66% of the cores can't be used.

# Action History
- Created by: Bilaboz | 2020-01-23T23:44:39+00:00
- Closed at: 2020-08-28T16:42:09+00:00
