---
title: Solo mining not working
source_url: https://github.com/monero-project/monero-gui/issues/501
author: ghost
assignees: []
labels: []
created_at: '2017-02-27T21:16:33+00:00'
updated_at: '2017-03-03T12:31:45+00:00'
type: issue
status: closed
closed_at: '2017-03-03T12:31:45+00:00'
---

# Original Description
Shows 0 h/s. Daemon viewer shows it is trying to "smart mine". Probably related to: https://github.com/monero-project/monero/issues/1810

Edit: I'm on OSX 10.12.3

# Discussion History
## ghost | 2017-02-27T21:19:30+00:00
Strange. I stopped the daemon, changed the log level, restarted the daemon, and restarted the miner. This time it didn't smart mine, but it mined like normal, and I got 35 h/s. So perhaps smart mining is the only problem, though I don't understand why smart mining would begin when the daemon auto-starts vs. normal mining is enabled when I start the daemon manually.

## moneromooo-monero | 2017-02-27T23:56:30+00:00
Probably because the GUI does not set the new smart mining options when calling the RPC, so they get set to random values, which the daemon reads and acts upon. There might be a number of RPCs with added fields which might need filling...

## ghost | 2017-02-28T01:54:25+00:00
@Jaqueeee Perhaps we can just forbid the GUI from smart mining, and this issue will be solved?

## Jaqueeee | 2017-03-02T13:11:16+00:00
@xmr-eric @medusadigital Mining works for me with #1827

## ghost | 2017-03-02T18:03:49+00:00
@Jaqueeee Added #1827 and it works now

# Action History
- Created by: ghost | 2017-02-27T21:16:33+00:00
- Closed at: 2017-03-03T12:31:45+00:00
