---
title: xmrig does not dye if network is down
source_url: https://github.com/xmrig/xmrig/issues/2553
author: gaga9999
assignees: []
labels: []
created_at: '2021-08-23T08:43:42+00:00'
updated_at: '2025-06-16T20:50:26+00:00'
type: issue
status: closed
closed_at: '2025-06-16T20:50:26+00:00'
---

# Original Description
is that intended or not, i dont know, it dies if one starts it without parameters, but it does not quit when network is down. an option would be fine for those who run it on watchdog and receive notfivications. exit would be a trigger for an alarm.

# Discussion History
## Spudz76 | 2021-08-23T17:55:29+00:00
No, because then you lose your memory allocations, and it's better to leave it running until the network comes back, it doesn't "do" anything but try to reconnect during the no-network phase.

## gaga9999 | 2021-08-23T21:25:41+00:00
ok got it, recoverable error = keeps running forever.

## Spudz76 | 2021-08-24T00:52:37+00:00
That is a better way to describe it, yes.

# Action History
- Created by: gaga9999 | 2021-08-23T08:43:42+00:00
- Closed at: 2025-06-16T20:50:26+00:00
