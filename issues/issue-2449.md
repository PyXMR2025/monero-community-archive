---
title: Segmentation fault on Linux monerod
source_url: https://github.com/monero-project/monero/issues/2449
author: celavek
assignees: []
labels: []
created_at: '2017-09-14T22:24:05+00:00'
updated_at: '2018-06-29T19:10:01+00:00'
type: issue
status: closed
closed_at: '2017-09-22T10:12:22+00:00'
---

# Original Description
I get a segmentation fault with the latest release - Monero 'Helium Hydra' (v0.11.0.0-release) on 
Debian Linux. This is the first time I try to synchronize the blockchain and create a wallet. With the current state of the blockchain that I have I consitently get the crash. The logs before the crash look a bit strange to me with confusing output:

> 2017-09-12 20:46:16.601 [P2P7]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:305     [75.88.131.213:57070 INC] Sync data returned a new top block candidate: 1288623 -> 1322390 [Your node is 33767 blocks (46 days) behind] 
SYNCHRONIZATION started
2017-09-12 20:46:16.602 [P2P7]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:305     [37.79.255.43:41287 INC] Sync data returned a new top block candidate: 1288623 -> 1397703 [Your node is 109080 blocks (151 days) behind] 
SYNCHRONIZATION started

first it's 46 days behind then the next line reports 151 days behind?

From the core dump it seems to be crashing during some `boost::asio` operation.
The log is attached but the dump is too big to attach

[monerod_crash.txt](https://github.com/monero-project/monero/files/1304745/monerod_crash.txt)

the stack trace:

[monerod_stacktrace.txt](https://github.com/monero-project/monero/files/1304754/monerod_stacktrace.txt)


I will try to reinitialize the whole thing to see if I still get the crash.


# Discussion History
## moneromooo-monero | 2017-09-15T07:39:10+00:00
Hard to see where it is crashing. Try a debug build, and run with `--log-level 1,blockchain:3`.


## dEBRUYNE-1 | 2017-09-15T14:14:54+00:00
For visibility, I noticed two other people reporting this:

1.

No stack trace (yet).

>I have the latest version downloaded. I resynced from scratch, but got stuck on block 1009840. Closed and re-opened it, and now I get "Segmentation fault (core dumped)".

>I'm using Ubuntu 16.04.

**Source:** https://www.reddit.com/r/Monero/comments/707elm/i_cant_sync_monerod/

---------------------

2. 

Stack trace (old bins): https://paste.fedoraproject.org/paste/WhTPoZoEQNPb2pdLMGABCw

Stack trace (new bins): https://paste.fedoraproject.org/paste/15-XU-Qa50bLaGUFpDWGRg

> Ubuntu 14.04 64bit, monero-v0.11.0.0

>It was dumping the core on first run, so I deleted blockchain and started again. Seemed to stall at 92% so at that point I stopped daemon and upon starting again back to core dumped.

**Source:** https://www.reddit.com/r/Monero/comments/6yprar/mandatory_upgrade_monero_01100_helium_hydra/dn0dr7f/?context=3

## celavek | 2017-09-15T20:33:34+00:00
@moneromooo-monero I think the stack trace I attached gives a *hint* where the crash might be.
I did not build it myself. The binary is the "official release". I will try a debug build and see how that goes.

I initialized the blockchain in a new location from scratch and this time it did not crash.


## moneromooo-monero | 2017-09-20T09:53:47+00:00
Probably fixed by https://github.com/monero-project/monero/pull/2492, as reported in the bug referenced just above.

## moneromooo-monero | 2017-09-22T09:46:05+00:00
+resolved

## celavek | 2017-09-28T22:18:19+00:00
I've seen your comment on the related thread ... and from the commit the fix seems to be related to the call to  __memcmp_sse4_1 () which my backtrace also contained ... 

## Tahutipai | 2017-10-13T23:31:25+00:00
I am experiencing this issue with binaries downloaded from getmonero.org as of 13/oct/2017.  Can anyone please advise how to resolve?

## zzium | 2017-10-17T15:35:09+00:00
Experiencing the exact same issue here. Running same Ubuntu version (17.04) - Also got stuck at block 1288623

Edit: Also running the 0.11.0.0 binaries from getmonero.org downloaded only few days ago

## palexande | 2017-11-16T21:05:10+00:00
Getting the same behaviour.  This is after a hard shutdown of the node. OS:  Linux Mint.

Update:  Was able to fix with "**monerod --db-salvage**"

## muncherelli | 2017-11-16T21:15:11+00:00
Also getting the same error at block 1288623.

v0.11.0.0 binaries from getmonero.org, running on a single core Ubuntu 16.04 VPS with 1GB RAM

```
**********************************************************************
You are now synchronized with the network. You may now start monero-wallet-cli.

Use the "help" command to see the list of available commands.
**********************************************************************
2017-11-16 21:08:31.004 [P2P6]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:305     [84.114.235.113:18080 OUT] Sync data returned a new top block candidate: 1288623 -> 1444455 [Your node is 155832 blocks (216 days) behind]
SYNCHRONIZATION started
Segmentation fault (core dumped)

```

## juliavi | 2018-02-12T11:45:52+00:00
Same error here. Tried restarting multiple times, and starting from scratch multiple times.
--db-salvage didn't help.
I've built the latest package from github, so the fix should have applied.

## andrewvaca | 2018-06-29T19:10:01+00:00
Tahnks @palexande, I was getting **Segmentation fault: 11** after a hard shutdown of the node on macOS, but "**monerod --db-salvage**" did the trick and it's working again.

# Action History
- Created by: celavek | 2017-09-14T22:24:05+00:00
- Closed at: 2017-09-22T10:12:22+00:00
