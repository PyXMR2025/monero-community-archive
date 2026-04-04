---
title: 'Wallet Warnings: Unsupported Format & Expected tx(es) got 0'
source_url: https://github.com/monero-project/monero/issues/3137
author: gaylordbendylover
assignees: []
labels: []
created_at: '2018-01-16T14:35:00+00:00'
updated_at: '2018-07-19T22:16:57+00:00'
type: issue
status: closed
closed_at: '2018-07-19T22:16:57+00:00'
---

# Original Description
i run a pool and the wallet rpc connection output throws a couple warnings:

1. Transaction extra has unsupported format: <......>

2. Expected 2 tx(es), got 0

What do these mean?  (Are we getting blocks but not actually receiving them for some reason?)



# Discussion History
## moneromooo-monero | 2018-01-16T15:02:29+00:00
The first one is inconsequential. The second one seems to be a bug. Please repro with --log-level 2 on the wallet and --log-level 0,daemon.rpc:DEBUG on monerod, and paste the relevant log portions on fpaste.org or pastebin.mozilla.org.

## gaylordbendylover | 2018-01-17T00:24:35+00:00
Thanks for the reply moneromooo-monero.  see my logs here:

debug_monerod:
https://paste.fedoraproject.org/paste/oXWlwsGKdJGVGxiQmQv1EA

debug_wallet:
https://paste.fedoraproject.org/paste/8vpaLASS5PqeBm~UrdzcmQ

lmk what you think, and if you would like to see any of my other logs.


## moneromooo-monero | 2018-01-17T00:58:48+00:00
The wallet is running with default logs on that paste.

## moneromooo-monero | 2018-01-17T01:02:02+00:00
Also, in the wallet log, you will see lines with:

Found new pool tx: ....

shortly before the "Expected..." message. When one or more is not found, do this in monerod:

print_tx HASH

with HASH being the tx hash mentioned on that line, and report whether it's found or not, and, if found, whether in the txpool or the blockchain (that'll be the first line of that command's output)..


## gaylordbendylover | 2018-01-17T01:19:45+00:00
running again with proper debug level.  will output shortly.  in the meantime, there are several lines that say:

asking for 4 transactions
Got 1 and OK

does this mean that 3 weren't found?

## gaylordbendylover | 2018-01-17T01:39:44+00:00
wallet out:
https://paste.fedoraproject.org/paste/r9a0Rox6OwoGIzcMyXNktQ

monerod out:
https://paste.fedoraproject.org/paste/VgZz4JGTQkv2pTkdlQ1fQA

## moneromooo-monero | 2018-01-17T10:25:23+00:00
This has the right log levels, but you need to wait till the bug happens for the log to show anything useful.

and no, Got 1 and OK doesn't mean 3 aren't found.

## gaylordbendylover | 2018-01-17T22:30:20+00:00
sorry to take so long to get back with you.  (day job dutys)

4 sets of logs from wallet:
https://paste.fedoraproject.org/paste/qQeraRP4QTQocSEtIhPlAg

pasting preceding hashes in monerod show they are found on the blockchain


## moneromooo-monero | 2018-01-17T22:55:31+00:00
This is the wrong log level again, but one message in that log tells me you're running old code, and that's probably fixed since (0c57df9770024e73718a518b10700d5fcf8ba594).

## moneromooo-monero | 2018-07-19T21:58:24+00:00
I'll call that fixed, reopen if the "expected 2, got 0" happens again (and send logs as requested if so).

+resolved

# Action History
- Created by: gaylordbendylover | 2018-01-16T14:35:00+00:00
- Closed at: 2018-07-19T22:16:57+00:00
