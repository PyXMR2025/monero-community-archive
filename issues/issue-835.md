---
title: 'Feature request: bind multiple RPC ports and selectively control access of
  each'
source_url: https://github.com/monero-project/monero/issues/835
author: Gingeropolous
assignees: []
labels:
- enhancement
created_at: '2016-05-10T02:59:41+00:00'
updated_at: '2019-03-21T14:17:46+00:00'
type: issue
status: closed
closed_at: '2019-03-21T14:17:46+00:00'
---

# Original Description
Would be cool to bind multiple RPC ports to bitmonerod, and be able to lock down one of them using the --restricted-rpc flag.

So when launching, flag would be

`--rpc-restricted-port 18085 --rpc-bind-port 18081`


# Discussion History
## jonathancross | 2017-09-19T22:38:39+00:00
This would be very useful for those who want to monitor from localhost (`monerod status`, `monerod stop_daemon`, etc), but restrict remote connections.

## Timo614 | 2017-11-16T16:14:14+00:00
I have this working here at the moment: https://github.com/Timo614/monero/tree/bind-multiple-rpc-ports

I'm going to spend a bit more time with it before putting up a pull request as I'm not sure if my approach is ideal but in the branch the logic adds the argument `--rpc-restricted-bind-port` to create a restricted RPC port
https://github.com/Timo614/monero/commit/30bce81fda9c8a082bed258067ac0ea5d697f5dd was able to confirm that both reply to unrestricted calls (such as `/getinfo`) while the restricted port cannot handle the restricted calls (`/get_peer_list`).

## moneromooo-monero | 2019-03-21T14:14:06+00:00
+resolved

# Action History
- Created by: Gingeropolous | 2016-05-10T02:59:41+00:00
- Closed at: 2019-03-21T14:17:46+00:00
