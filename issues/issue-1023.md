---
title: Hashrate drops when other threads are running.
source_url: https://github.com/xmrig/xmrig/issues/1023
author: seongung
assignees: []
labels:
- question
created_at: '2019-05-22T01:34:06+00:00'
updated_at: '2019-08-02T11:50:07+00:00'
type: issue
status: closed
closed_at: '2019-08-02T11:50:06+00:00'
---

# Original Description
Xmrig runs with CPU 50% usage.
4 Cores, 8 Threads(logic processors)

It works fine when it runs alone. However, when other processes start to run and
its hashrate drops by 10~20%. (Even though xmrig process takes up 50% cpu consistently)

Does it happen because cores and logic processors don't work seperately and they interfere each other?


# Discussion History
## 2010phenix | 2019-05-23T22:15:24+00:00
other process used L2 \ L3 from CPU too ;)

## Spudz76 | 2019-06-15T17:13:04+00:00
Sometimes, you can set affinity to fence things.  Meaning not only the miner thread affinity but then also entire rest of system processes affinity to the non-mining cores (but not the SMT cores if you're mining on either half of that core)

This worked for me on windows, although not well enough to bother with how clunky setting a base-system-affinity is (needs unofficial tools, and you can only change existing processes not the rules for newly spawned ones, etc) - Linux should be easier to set a global affinity for all processes (that aren't explicitly told to run on the fenced off cores, the miner threads).

# Action History
- Created by: seongung | 2019-05-22T01:34:06+00:00
- Closed at: 2019-08-02T11:50:06+00:00
