---
title: Sync data returned a new top block....
source_url: https://github.com/monero-project/monero/issues/3945
author: jwm1969
assignees: []
labels: []
created_at: '2018-06-06T12:40:09+00:00'
updated_at: '2018-06-06T13:40:27+00:00'
type: issue
status: closed
closed_at: '2018-06-06T13:40:27+00:00'
---

# Original Description
When I start monerod, i get this at the end:

2018-06-06 12:31:41.541	[P2P8]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1583	
**********************************************************************
You are now synchronized with the network. You may now start monero-wallet-cli.

Use the "help" command to see the list of available commands.
**********************************************************************
2018-06-06 12:32:02.566	[P2P1]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:310	[113.210.179.21:51461 INC] Sync data returned a new top block candidate: 1589058 -> 1589601 [Your node is 543 blocks (0 days) behind] 
SYNCHRONIZATION started
status
Height: 1589060/1589060 (100.0%) on mainnet, not mining, net hash 393.03 MH/s, v7, up to date, 0(out)+5(in) connections, uptime 0d 0h 5m 53s

It says my node is 543 blocks behind but never updates... what is strange is that if I look at the monero block explorer, it looks like the Height returned from status is up to date.

I apologize if this is a duplicate issue, just point me in right direction, my search did not show this exact issue.


# Discussion History
## moneromooo-monero | 2018-06-06T13:37:23+00:00
That's normal. What makes you think there's a bug ? Is your daemon stuck somewhere for a long time ?



## jwm1969 | 2018-06-06T13:40:27+00:00
nope, sorry, thought "SYNCHRONIZATION started" meant it was trying to catch up; it just means its running... ok got it, I will close issue.  Thanks.

# Action History
- Created by: jwm1969 | 2018-06-06T12:40:09+00:00
- Closed at: 2018-06-06T13:40:27+00:00
