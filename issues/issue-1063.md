---
title: simplewallet not showing refresh progress if a refresh is started before daemon
  is ready
source_url: https://github.com/monero-project/monero/issues/1063
author: JollyMort
assignees: []
labels: []
created_at: '2016-09-10T14:51:24+00:00'
updated_at: '2016-09-11T14:51:40+00:00'
type: issue
status: closed
closed_at: '2016-09-11T14:51:40+00:00'
---

# Original Description
As described in the title, I noticed this when hitting refresh on a new wallet in simplewallet before my daemon synced with the network. It just hung there, and later i killed the console.

When re-opening it and hitting refresh, it started from some height, meaning it did scan in the background the first time, but didn't show the status.

Note: monero.win.x64.v0-9-4-0


# Discussion History
## moneromooo-monero | 2016-09-11T13:54:19+00:00
That's by design. If you don't want background refresh, "set auto-refresh 0" in simplewallet.


## JollyMort | 2016-09-11T14:51:40+00:00
The exact steps were:
1. run the deamon, which starts to sync and is catching up with the network
2. meanwhile, open a new command prompt and start simplewallet: simplewallet --restore-deterministic-wallet
3. run "refresh" from simplewallet
4. the cursor moves to next line, and _ blinks, no other indicator like "Starting refresh..." is shown that something is going on
5. after a couple of minutes, I close the window, thus killing simplewallet
6. later, deamon is synced
7. I reopen the wallet, and run refresh
8. it immediately shows the progress, and starts from some block height, indicating that during 4., it was working, but just didn't show the progress

However, as I'm unable to reproduce the issue, I'm closing it.


# Action History
- Created by: JollyMort | 2016-09-10T14:51:24+00:00
- Closed at: 2016-09-11T14:51:40+00:00
