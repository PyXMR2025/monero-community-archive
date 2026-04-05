---
title: Idle/dynamic mining
source_url: https://github.com/xmrig/xmrig/issues/432
author: wilburforce666
assignees: []
labels:
- duplicate
created_at: '2018-03-07T19:12:49+00:00'
updated_at: '2018-03-14T23:18:17+00:00'
type: issue
status: closed
closed_at: '2018-03-14T23:18:17+00:00'
---

# Original Description
Does this support idle/dynamic mining?

# Discussion History
## wilburforce666 | 2018-03-07T19:14:56+00:00
If so how?

## dunklesToast | 2018-03-08T18:27:14+00:00
What do you mean with this?
That the Miner pauses when you use your PC and continues when you do not use it or the CPU has many resources free? If you mean that take a look at #141 

## wilburforce666 | 2018-03-08T23:26:11+00:00
Yes that is what I mean. That task schudele thing that was linked. How could I implement it into a silent miner?

## CthulhuVRN | 2018-03-09T15:51:55+00:00
@wilburforce666 why don't use task priority? Linux has `nice`, Windows has `start`. Give the lower priority to miner, and that's a deal.

## xmrig | 2018-03-14T23:18:17+00:00
Duplicate #141

# Action History
- Created by: wilburforce666 | 2018-03-07T19:12:49+00:00
- Closed at: 2018-03-14T23:18:17+00:00
