---
title: 'Error: Mining did not start -- BUSY'
source_url: https://github.com/monero-project/monero/issues/6413
author: IvRRimum
assignees: []
labels: []
created_at: '2020-04-01T14:34:43+00:00'
updated_at: '2020-04-09T18:43:25+00:00'
type: issue
status: closed
closed_at: '2020-04-09T18:43:25+00:00'
---

# Original Description
Works fine when i run `./monerod --offline`, but as soon as it tries to sync(which i don't actually need it to), i can't start the miner.

# Discussion History
## IvRRimum | 2020-04-01T14:35:42+00:00
I keep digging in the code and can't figure out with what it is BUSY with. I only want monero to sync with peers i define or not sync at all.

## sumogr | 2020-04-01T15:24:42+00:00
1. you cant mine on your daemon while its syncing hence the busy message. Wait for it to completely sync
2. you cant mine on your daemon when your daemon is offline
3. To connect exclusively to peers you want,  run `./monerod --p2p-bind-ip 127.0.0.1 --add-exclusive-node <peer ip>:<port> `(repeat that last flag as many times as needed)

## moneromooo-monero | 2020-04-01T15:44:35+00:00
Not a bug, it's supposed to do that.

+invalid


# Action History
- Created by: IvRRimum | 2020-04-01T14:34:43+00:00
- Closed at: 2020-04-09T18:43:25+00:00
