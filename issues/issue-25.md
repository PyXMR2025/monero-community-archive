---
title: Enable huge pages on OSX
source_url: https://github.com/xmrig/xmrig/issues/25
author: kurakin-oleksandr
assignees: []
labels: []
created_at: '2017-07-03T09:53:22+00:00'
updated_at: '2018-01-31T11:51:18+00:00'
type: issue
status: closed
closed_at: '2017-07-03T10:23:20+00:00'
---

# Original Description
When I run miner huge pages support sometimes is enabled, sometimes - not.
Would be good to have instructions how to activate it on OSX

# Discussion History
## xmrig | 2017-07-03T10:17:42+00:00
If hugepages disabled it means allocation failed and used failback, There many reasons why it can happen, memory fragmentation, system load, other applications, ... Only after reboot there is a maximum chance of getting hugepages. Longer system works less chance. Unfortunately there is no guaranteed way to get them.

## kurakin-oleksandr | 2017-07-03T10:23:18+00:00
Thanks!

## iexa | 2018-01-31T11:51:18+00:00
how much memory does it try to allocate with hugepages anyway?

# Action History
- Created by: kurakin-oleksandr | 2017-07-03T09:53:22+00:00
- Closed at: 2017-07-03T10:23:20+00:00
