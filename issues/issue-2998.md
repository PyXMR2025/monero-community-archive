---
title: 'Feature Request: panthera algo'
source_url: https://github.com/xmrig/xmrig/issues/2998
author: Tohelo101
assignees: []
labels:
- question
- wontfix
created_at: '2022-04-03T05:07:56+00:00'
updated_at: '2022-07-18T05:44:43+00:00'
type: issue
status: closed
closed_at: '2022-04-03T06:40:56+00:00'
---

# Original Description
Hello could be possible to add panthera algo in xmrig ?

# Discussion History
## xmrig | 2022-04-03T06:40:56+00:00
You can use third party fork for this algorithm https://github.com/MoneroOcean/xmrig
Thank you.

## benthetechguy | 2022-07-17T06:58:22+00:00
@xmrig @SChernykh, is there a specific reason why panthera support can't be upstreamed into XMRig proper? I've found it to be the most profitable algorithm on many of my devices.

## SChernykh | 2022-07-17T07:25:03+00:00
Because it doesn't work when compiled with MSVC, all shares are invalid.

## benthetechguy | 2022-07-18T05:44:43+00:00
Just tested by compiling with both MSVC and gcc. It doesn't just occur when compiled with MSVC, but running on Windows in general. I've reported the bug to them.

# Action History
- Created by: Tohelo101 | 2022-04-03T05:07:56+00:00
- Closed at: 2022-04-03T06:40:56+00:00
