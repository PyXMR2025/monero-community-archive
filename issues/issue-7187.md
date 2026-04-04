---
title: lots and lots of  SYNCHRONIZED OK messages
source_url: https://github.com/monero-project/monero/issues/7187
author: unamefailed
assignees: []
labels: []
created_at: '2020-12-25T12:41:07+00:00'
updated_at: '2021-01-09T01:35:31+00:00'
type: issue
status: closed
closed_at: '2021-01-09T01:35:31+00:00'
---

# Original Description
600+  lines
https://paste.debian.net/1178269/

# Discussion History
## unamefailed | 2020-12-25T13:13:09+00:00
is printing  all the time after reboot

## selsta | 2020-12-25T15:21:47+00:00
You can ignore these messages. Please apply the latest block list while this attack is ongoing: https://gui.xmr.pm/files/block_tor.txt

## moneromooo-monero | 2020-12-26T03:26:39+00:00
https://github.com/monero-project/monero/pull/7189 should fix that, some nodes were claiming data but then only supplying existing but no new actual data.


## BKdilse | 2020-12-28T19:22:47+00:00
I'm also seeing this, along with the 2 blocks ahead on Daemon.
@selsta I've already applied a block last week, I'll try the latest file now.

## BKdilse | 2020-12-28T20:15:10+00:00
@selsta actually I applied https://gui.xmr.pm/files/block.txt
Do I also need https://gui.xmr.pm/files/block_tor.txt ?

## rblaine95 | 2020-12-29T11:15:55+00:00
> 
> 
> @selsta actually I applied https://gui.xmr.pm/files/block.txt
> Do I also need https://gui.xmr.pm/files/block_tor.txt ?

As far as I know, `block_tor.txt` includes all the IPs in `block.txt` but also adds some tor exit nodes

## selsta | 2020-12-30T23:01:19+00:00
v0.17.1.8 is out: https://www.getmonero.org/downloads/

It fixes the current "synchronized ok" spam.

## BKdilse | 2020-12-30T23:31:35+00:00
Thanks, I already compiled the tagged release earlier today, after seeing the 2 block ahead issue coming back due to more dodgy nodes.  Can confirm, it appears to be resolved.

# Action History
- Created by: unamefailed | 2020-12-25T12:41:07+00:00
- Closed at: 2021-01-09T01:35:31+00:00
