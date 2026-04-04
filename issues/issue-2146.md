---
title: Monerod sync stalls when date changes
source_url: https://github.com/monero-project/monero/issues/2146
author: elelel
assignees: []
labels:
- invalid
created_at: '2017-07-04T05:17:07+00:00'
updated_at: '2017-09-21T09:24:23+00:00'
type: issue
status: closed
closed_at: '2017-09-21T09:24:23+00:00'
---

# Original Description
It seems that monerod synchronization stops when the clock goes over 00:00. The last message in the log is like:
```
2017-07-03 23:59:33.947	[P2P6]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1004	[X.X.X.X:28080 OUT]  Synced 1251780/1346393
```

# Discussion History
## moneromooo-monero | 2017-07-04T19:03:19+00:00
That seems pretty unlikely, especially since some people report multi-day sync times.
If you still have that daemon running, please try "set_log 1" and see what you get.
In any case, in another terminal: gdb /path/to/monerod \`pidof monerod\`
Then, in gdb: thread apply all bt
Replace the path as appropriate in the gdb command.

## elelel | 2017-07-04T19:17:27+00:00
Unfortunately I've restarted the server already. It has been working for about a day (syncing from scratch) before that, and has been in the stalled state for about 5 hours after 00:00. It has not been responding to anything, with a CPU thread loaded. Kill it with signal 9. When I restarted it, it continued without a problem.

## moneromooo-monero | 2017-09-21T09:23:43+00:00
Nothing to work on here, so I'll close it. Reopen if you get a trace.

+invalid

# Action History
- Created by: elelel | 2017-07-04T05:17:07+00:00
- Closed at: 2017-09-21T09:24:23+00:00
