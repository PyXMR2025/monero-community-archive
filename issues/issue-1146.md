---
title: 'Can''t stop monerod '
source_url: https://github.com/monero-project/monero/issues/1146
author: ghost
assignees: []
labels: []
created_at: '2016-09-28T01:16:34+00:00'
updated_at: '2016-09-29T12:00:38+00:00'
type: issue
status: closed
closed_at: '2016-09-29T12:00:38+00:00'
---

# Original Description
Stopped syncing at 60k blocks, tried to use `monerod exit`, logs showing stop signal sent, not stopping

Will try running with `gdb` tomorrow


# Discussion History
## moneromooo-monero | 2016-09-28T07:18:36+00:00
How much did you wait ? If it's syncing, it'll stop after it's done processing the current 200 blocks.


## ghost | 2016-09-28T11:07:21+00:00
8 minutes. This is the 3rd attempt at resyncing and previous ones flew past these early blocks. 


## moneromooo-monero | 2016-09-28T11:40:36+00:00
Then a "thread apply all bt" will be helpful.


## ghost | 2016-09-28T13:00:32+00:00
Would you mind explaining that a little more?


## moneromooo-monero | 2016-09-28T14:00:37+00:00
When you end up in such a situation again, run gdb like this:
gdb /path/to/monerod `pidof monerod`
Then, in gdb:
thread apply all bt
You will have to press enter to cycle through all pages of the data. When you've gone through all, paste that info here.
It shows what each thread it bitmonerod was doing at the time. There might be a deadlock in some of them.


## ghost | 2016-09-28T15:19:01+00:00
OK thanks, will do. So I can run gdb after the crash?


## ghost | 2016-09-29T12:00:38+00:00
Closing. It now stops....eventually.


# Action History
- Created by: ghost | 2016-09-28T01:16:34+00:00
- Closed at: 2016-09-29T12:00:38+00:00
