---
title: Background mining starts from monerod console but not from command line
source_url: https://github.com/monero-project/monero/issues/2209
author: alejandorr
assignees: []
labels: []
created_at: '2017-07-26T14:33:18+00:00'
updated_at: '2017-09-11T17:56:55+00:00'
type: issue
status: closed
closed_at: '2017-09-11T17:56:55+00:00'
---

# Original Description
Last tested with commit ab594cfee94dff87bb7039724563f6177a892b8b

There's different behavior if I try to directly start the daemon with bg mining enabled and if I do it from its console. 

**Case 1** (doesn't work), launching bg mining from command line:
`$ ./monerod --start-mining <realaddr> --mining-threads 6 --bg-mining-enable --bg-mining-ignore-battery`

After initialization, monerod only outputs (despite the battery switch) this message every minute or so:

`2017-07-26 14:22:26.193     7ff1606f6700        ERROR   miner   src/cryptonote_basic/miner.cpp:871      Couldn't find battery/power status file, can't determine if plugged in!`

Idle level is never reported.

**Case 2** (works), launching with fg mining, stopping, and starting bg mining from within the daemon:
`$ ./monerod --start-mining <realaddr> --mining-threads 6`

Daemon starts mining right away (I can check with show_hr). So, I issue from the daemon console:
```
stop_mining
start_mining <realaddr> 6 true true
```
In this case, from the following logs, you can see that mining starts when idle level is reached:
```
2017-07-26 14:29:04.544 [miner 1]       INFO    global  src/cryptonote_basic/miner.cpp:435      background mining is enabled, but not started, waiting until start triggers
2017-07-26 14:29:14.409     7f40d08f4700        ERROR   miner   src/cryptonote_basic/miner.cpp:871      Couldn't find battery/power status file, can't determine if plugged in!
2017-07-26 14:29:14.409     7f40d08f4700        INFO    global  src/cryptonote_basic/miner.cpp:691      idle percentage is 90
2017-07-26 14:29:14.409     7f40d08f4700        INFO    global  src/cryptonote_basic/miner.cpp:694      cpu is 90% idle, idle threshold is 90%, ac power : 1, background mining started, good luck!
2017-07-26 14:29:25.409     7f40d08f4700        ERROR   miner   src/cryptonote_basic/miner.cpp:871      Couldn't find battery/power status file, can't determine if plugged in!
2017-07-26 14:29:25.410     7f40d08f4700        INFO    global  src/cryptonote_basic/miner.cpp:650      idle percentage is 85%, miner percentage is 5%, ac power : 1
```

In summary: bg mining should start when requested from command line when idle level is reached, but it doesn't.

# Discussion History
## alejandorr | 2017-07-26T14:34:10+00:00
Forgot to add: this is on ubuntu 17.04 x64, I observed the same in 16.04.

## moneromooo-monero | 2017-07-31T07:39:36+00:00
https://github.com/monero-project/monero/pull/2232 fixes the battery setting. For the warning, the battery probing was rewritten in https://github.com/monero-project/monero/pull/2147.

## moneromooo-monero | 2017-08-18T16:30:20+00:00
Both are now merged. The error message is still around if the battery/AC state can't be queried, but that's apparently intended, as it  means "assume we're on AC if we fail to determine", from a comment in the source. This might be best changed, not sure.

## alejandorr | 2017-08-31T09:36:48+00:00
I've tried to verify this fix using current head (72b5f37f58754c05627f89fc9e6c1f44d4a3b3ce) but now the node claims to be always busy, even when synchronized. The precise error is given (in red) as:

`Error: Mining did not start -- BUSY`

This is after issuing a `start_mining <addr> 3 true true`

## moneromooo-monero | 2017-08-31T19:23:50+00:00
This works here (testnet, recent master).

Can you share the output of "status" and of "sync_info" (spans may be omitted, if any) ?

## alejandorr | 2017-09-11T17:56:55+00:00
After fetching latest head (commit 02e5dcd2fab07c46b4943028cfabecbba4745b58) it works as expected, and the original issue is also working as it should, so closing. Thanks.

# Action History
- Created by: alejandorr | 2017-07-26T14:33:18+00:00
- Closed at: 2017-09-11T17:56:55+00:00
