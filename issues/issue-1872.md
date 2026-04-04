---
title: get_bulk_payments hangs occasionally for several seconds
source_url: https://github.com/monero-project/monero/issues/1872
author: arnuschky
assignees: []
labels: []
created_at: '2017-03-16T18:59:58+00:00'
updated_at: '2017-03-25T20:12:52+00:00'
type: issue
status: closed
closed_at: '2017-03-25T20:12:52+00:00'
---

# Original Description
Has anyone encountered this before? Any idea how to trigger this?

I have troubles reproducing this separately, but we're seeing this regularly on our production instance.

Running 0.10.1. (0.10.2 had too many issues.)

Here output from a special logger:
```
[2017-03-16 19:19:28] INFO     before get_bulk_payments
[2017-03-16 19:19:28] INFO     after get_bulk_payments
[2017-03-16 19:19:31] INFO     before get_bulk_payments
[2017-03-16 19:19:31] INFO     after get_bulk_payments
[2017-03-16 19:19:34] INFO     before get_bulk_payments
[2017-03-16 19:19:34] INFO     after get_bulk_payments
[2017-03-16 19:19:37] INFO     before get_bulk_payments
[2017-03-16 19:19:37] INFO     after get_bulk_payments
[2017-03-16 19:19:40] INFO     before get_bulk_payments   <-------
[2017-03-16 19:20:06] INFO     after get_bulk_payments
[2017-03-16 19:20:09] INFO     before get_bulk_payments
[2017-03-16 19:20:09] INFO     after get_bulk_payments
[2017-03-16 19:20:12] INFO     before get_bulk_payments
[2017-03-16 19:20:12] INFO     after get_bulk_payments
[2017-03-16 19:20:15] INFO     before get_bulk_payments
[2017-03-16 19:20:15] INFO     after get_bulk_payments
[2017-03-16 19:20:18] INFO     before get_bulk_payments
[2017-03-16 19:20:18] INFO     after get_bulk_payments
[2017-03-16 19:20:21] INFO     before get_bulk_payments
[2017-03-16 19:20:21] INFO     after get_bulk_payments
[2017-03-16 19:20:24] INFO     before get_bulk_payments
[2017-03-16 19:20:24] INFO     after get_bulk_payments
[2017-03-16 19:20:27] INFO     before get_bulk_payments    <-------
[2017-03-16 19:20:52] INFO     after get_bulk_payments
```

As you can see, `get_bulk_payments` typically completes within a second (as do all other RPC calls), but regularly it hangs for ~30 seconds.

# Discussion History
## moneromooo-monero | 2017-03-17T08:24:17+00:00
Looks more like three seconds, and is probably when the RPC is waiting for the wallet to finish when it's in the middle of refreshing from the daemon.

## arnuschky | 2017-03-17T08:32:19+00:00
You're reading the log wrong. It's 26 seconds in the first case, and 25 seconds in the second case.

Any hints where in the code I can have a look? Looks to me that there's something in that refresh process that's slow, or scales badly with large wallets.

We didn't have this problem before 0.10.1 I think*, so it might be something new.

(* not entirely sure, due to the involved timeouts it's hard to tell...)

## moneromooo-monero | 2017-03-17T17:31:28+00:00
Oh yes, that might seem a bit much for a chain lock...
When it happens, you could run "pstack `pidof monero-wallet-cli`" to see what it's running. Likely waiting for the daemon. If so, "pstack `pidof monerod`".

## arnuschky | 2017-03-18T21:01:59+00:00
Ah, good idea. Will do and report back.

## moneromooo-monero | 2017-03-21T11:05:33+00:00
Should be fixed by https://github.com/monero-project/monero/pull/1903

## arnuschky | 2017-03-21T13:49:04+00:00
Awesome! That was fast. Didn't even manage to debug it in the meantime.. Do you happen to know if this makes in into the new point release?

## moneromooo-monero | 2017-03-21T16:28:56+00:00
It will.

## arnuschky | 2017-03-21T16:54:27+00:00
I'll report back once I've got it to run.

## arnuschky | 2017-03-25T20:12:52+00:00
Works great with 0.10.3! Thanks a lot!

# Action History
- Created by: arnuschky | 2017-03-16T18:59:58+00:00
- Closed at: 2017-03-25T20:12:52+00:00
