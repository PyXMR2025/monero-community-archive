---
title: Latest master code doesn't connect to testnet
source_url: https://github.com/monero-project/monero/issues/3018
author: emesik
assignees: []
labels: []
created_at: '2017-12-27T23:20:01+00:00'
updated_at: '2018-01-07T00:00:20+00:00'
type: issue
status: closed
closed_at: '2018-01-07T00:00:20+00:00'
---

# Original Description
I compiled the code from master (tip at 270236e) and it fails to connect to testnet. I launch it without any fancy command line settings, just `--testnet --log-level 2`. The log contains numerous *handshake failure* messages but nothing that could hint me what the exact reason is.

I submit an example log file.
[monerod.log.txt](https://github.com/monero-project/monero/files/1590037/monerod.log.txt)





# Discussion History
## moneromooo-monero | 2018-01-01T15:44:50+00:00
Is that still the case ? If so, try adding: --add-exclusive-node 5.9.100.248:28080


## emesik | 2018-01-05T00:58:09+00:00
It didn't help, the daemon complained about a block having invalid version for its height.

I'm downloading the blockchain again. Will post an update then.

## moneromooo-monero | 2018-01-05T12:08:22+00:00
Ah, you might have synced with a v6 daemon past the v7 height, as we did not have much notice for poeple to update.

## emesik | 2018-01-07T00:00:20+00:00
It works now with the node address you provided. Thanks.

# Action History
- Created by: emesik | 2017-12-27T23:20:01+00:00
- Closed at: 2018-01-07T00:00:20+00:00
