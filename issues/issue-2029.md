---
title: Updating --max-threads-hint and --threads while running doesn't change CPU
  usage!
source_url: https://github.com/xmrig/xmrig/issues/2029
author: 88plug
assignees: []
labels:
- question
created_at: '2021-01-08T17:55:02+00:00'
updated_at: '2021-01-10T01:07:04+00:00'
type: issue
status: closed
closed_at: '2021-01-10T01:07:04+00:00'
---

# Original Description
I am trying to update the threads and/or the max-threads-hint while xmrig is running, without a full restart. The changes to the json are detected by xmrig, but the software does not reduce or increase the amount of cores used, even when the value changes in the json. 

Is there a better/any other way to update the cores while running?

# Discussion History
## xmrig | 2021-01-10T01:07:04+00:00
https://github.com/xmrig/xmrig/blob/master/doc/CPU_MAX_USAGE.md
https://github.com/xmrig/xmrig/blob/master/doc/CPU.md

# Action History
- Created by: 88plug | 2021-01-08T17:55:02+00:00
- Closed at: 2021-01-10T01:07:04+00:00
