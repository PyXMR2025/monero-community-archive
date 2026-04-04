---
title: (simplewallet) Terrible user experience on slow networks (high packet loss)
source_url: https://github.com/monero-project/monero/issues/3172
author: xmr-karnal
assignees: []
labels: []
created_at: '2018-01-22T16:04:57+00:00'
updated_at: '2018-01-24T01:06:49+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Terminal input constantly hangs, presumably because some network activity is blocking processing of user input.

When everything is fine with the network this is barely noticeable, but when there is packet loss, as in my case now, using simplewallet becomes a very frustrating experience - commands hang without any visible explanation, and worse, even after the prompt comes back, input is not working for a very long time (half a minute in some cases here).

Would it be possible to decouple network processing (just a guess, but it seems like the most logical one) from terminal input somehow?

# Discussion History
## xmr-karnal | 2018-01-22T16:06:27+00:00
Furthermore, there are some minor inconsistencies here and there, for instance right now the yellow prompt shows (no daemon), and yet on another tmux pane I can see a neverending stream of TCP packets  on port 18081 (the wallet *is* catching up)

## moneromooo-monero | 2018-01-22T16:15:29+00:00
simplewallet is supposed to refresh in the background. When such a hang happens, get an all thread stack trace (pstack or gdb), and paste to fpaste.org or pastebin.mozilla.org. Do this a few times if possible.

## moneromooo-monero | 2018-01-22T16:18:00+00:00
As for the "(no daemon)", it's simply the wallet timing out. Maybe asking for fewer blocks at once might just be enough for this case. If you build your own, I can give you a small patch to try.

## moneromooo-monero | 2018-01-22T16:27:43+00:00
Trivial, in fact:
src/cryptonote_config.h:#define COMMAND_RPC_GET_BLOCKS_FAST_MAX_COUNT           1000
Replace by, say, 10.

## xmr-karnal | 2018-01-23T14:35:13+00:00
Just some further observations:

Example1:

```
Wallet password:
Opened 2/2 multisig wallet: ...
**********************************************************************
Use the "help" command to see the list of available commands.
Use "help <command>" to see a command's documentation.
**********************************************************************
Warning: using an untrusted daemon at blabla.onion:18081, privacy will be lessened
Error: wallet failed to connect to daemon: blabla.onion:18081. Daemon either is not started or wrong port was passed. Please make sure daemon is running or change the daemon address using the 'set_daemon' command.
Error: wallet failed to connect to daemon: blabla.onion:18081. Daemon either is not started or wrong port was passed. Please make sure daemon is running or change the daemon address using the 'set_daemon' command.
Background refresh thread started
Height xxxx, txid <>, ??.000000000000, idx ?/0
```

Observations: Immediately after claiming that the connection failed, a background refresh begins and (very slowly) starts working. This is happening frequently, and I wonder how it is possible that the initial connection fails so often, but then immediately after the background refresh thread succeeds.

Example2:

```
Warning: using an untrusted daemon at blabla.onion:18081, privacy will be lessened
Error: wallet failed to connect to daemon: blabla.onion:18081. Daemon either is not started or wrong port was passed. Please make sure daemon is running or change the daemon address using the 'set_daemon' command.
Starting refresh...
Height X / Y
```

Observations: Here we see the initial connection failing, and then oblivious to this fact, the refresh starts working right away, as if the connection did succeed (which according to tcpdump it did, data was being exchanged even as the wallet claims the connection to have failed).



And a few other random observations:

1. *account* commands appear to hit the network, even when it seems unnecessary to do so: for instance, right after finishing the refresh (which took close to 1 hour, i'm on a terrible network), I type account to locate the information I need, and **the prompt hangs for 7 minutes as TCP packets to port 18081 are being exchanged** -- it just finished refreshing, shouldn't the information be cached locally?
This happens with 'account', 'account switch', etc.

Example3:

Terminal input is completely blocked, (enter) doesn't work, typing a command doesn't work, and tcpdump actually shows no data being exchanged at this moment (likely because the TCP connection to monerod died in the mean time) -- this should not hang user input.


## xmr-karnal | 2018-01-23T14:39:26+00:00
As for the suggestion to lower *COMMAND_RPC_GET_BLOCKS_FAST_MAX_COUNT* and recompiling, wouldn't it make more sense if the wallet determines whether the daemon is connected or not based on whether a TCP connection is established and active?




## moneromooo-monero | 2018-01-23T23:09:32+00:00
I don't see why account commands would need the network.

I'm not sure offhand whether considering an established connectoin to be "connected" is a good idea.

## stoffu | 2018-01-24T01:06:49+00:00
I also have the same thought as @moneromooo-monero. Does the hang happen only and consistently with the `account` command?

# Action History
- Created by: xmr-karnal | 2018-01-22T16:04:57+00:00
