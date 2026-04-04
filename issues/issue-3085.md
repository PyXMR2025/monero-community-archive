---
title: monerod status shows 0 Hashrate while mining
source_url: https://github.com/monero-project/monero/issues/3085
author: quantumproducer
assignees: []
labels: []
created_at: '2018-01-08T14:09:38+00:00'
updated_at: '2018-10-09T11:56:57+00:00'
type: issue
status: closed
closed_at: '2018-10-09T11:56:57+00:00'
---

# Original Description
start_mining <addr>
show_hr
hashrate: 55.0000
status
Height: 1482625/1482625 (100.0%) on mainnet, mining at 0 H/s, net hash 550.67 MH/s, v6, up to date, 8(out)+0(in) connections, uptime 0d 0h 25m 17s


# Discussion History
## quantumproducer | 2018-01-08T14:10:28+00:00
Sometimes status does show a hash rate that's much higher than what show_hr logs. What is status displaying here?
What is net hash?

## wmoreno3 | 2018-03-04T00:44:03+00:00
`root@server:~ # monerod status`
`Height: 1521983/1521983 (100.0%) on mainnet, mining at 44 H/s, net hash 980.46 MH/s, v6, update needed, 8(out)+0(in) connections, uptime 0d 2h 40m 39s`
`root@server:~ # monerod show_hr`
`Hash rate logging is on`

What does mean `update needed` ?

## stoffu | 2018-03-04T02:05:02+00:00
@quantumproducer
This issue was probably fixed by #3243. Please try the latest master.

## wmoreno3 | 2018-03-04T14:16:52+00:00
I saw [#3243](url) but nothing with my doubt,
`#monerod update check`
`#No update available`
I think that `monerod status` tells me that `update needed` but `monerod update check` tells me that not needed. Am I ok?

## stoffu | 2018-03-04T14:26:33+00:00
You need to build the code yourself.

## moneromooo-monero | 2018-10-09T11:46:14+00:00
+resolved

# Action History
- Created by: quantumproducer | 2018-01-08T14:09:38+00:00
- Closed at: 2018-10-09T11:56:57+00:00
