---
title: Daemon Stop at here
source_url: https://github.com/monero-project/monero/issues/3440
author: jinglics
assignees: []
labels: []
created_at: '2018-03-19T09:07:11+00:00'
updated_at: '2018-05-16T11:48:59+00:00'
type: issue
status: closed
closed_at: '2018-05-16T11:48:59+00:00'
---

# Original Description
Now is hundreds of blocks delay.

![screenshot from 2018-03-19 17-05-54](https://user-images.githubusercontent.com/3910258/37586603-d9309b9e-2b97-11e8-87d1-e00a06205328.png)


# Discussion History
## jinglics | 2018-03-19T09:08:04+00:00
I use Helium Hydra, Point Release 1

## moneromooo-monero | 2018-03-19T09:37:53+00:00
Restart monerod with `--log-level 1` to see whether blocks are being rejected, and why.
The update warning is not related to this as we've not forked yet.

## gituser | 2018-03-22T02:18:35+00:00
I had the same issue - restart helped for me. I'll look into logs later and report back.

## moneromooo-monero | 2018-05-16T10:58:16+00:00
All known sync bugs are now fixed in release-0.12. Reopen if it happens again with it.

+resolved


# Action History
- Created by: jinglics | 2018-03-19T09:07:11+00:00
- Closed at: 2018-05-16T11:48:59+00:00
