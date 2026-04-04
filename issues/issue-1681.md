---
title: Daemon not writing exit message on quit
source_url: https://github.com/monero-project/monero/issues/1681
author: ghost
assignees: []
labels:
- invalid
created_at: '2017-02-05T11:01:40+00:00'
updated_at: '2017-10-03T21:24:23+00:00'
type: issue
status: closed
closed_at: '2017-10-03T21:24:23+00:00'
---

# Original Description
So I recently had #1628 merged which should give a clear 'Daemon stopped successfully' message on the command line upon exit. 

However, this never seems to appear :(

Can anyone explain why? `scoped_message_writer.h` has been included appropriately.

# Discussion History
## moneromooo-monero | 2017-02-05T11:14:30+00:00
You mean, you didn't actually try it before PR ?

## moneromooo-monero | 2017-02-05T11:16:39+00:00
Anyway, adding lots of redundant messages which appear regardless of log level is not really wanted in the first place.

## ghost | 2017-02-05T11:55:55+00:00
Well it kinda seemed obvious that it would work - the correct header was included, the same exact code worked elsewhere in the codebase, it was a very small change without potential to break anything, and it compiled correctly. It just didn't work (which I admit I didn't check before submitting).

The idea wasn't to write to the log but to provide positive feedback to a user on the command line that the daemon had terminated so that they wouldn't then have to run `top` or `less ~/.bitmonero/monero.log` after `monerod exit` in order to check it had terminated correctly.

We already tell users that we're `Forking to background...` why not have a corresponding termination message?

## moneromooo-monero | 2017-02-05T15:06:01+00:00
Ooooh, this is supposed to be the daemonized process printing this ?
If so, it explains why it doesn't print anything. stdin/out/err are closed.

## ghost | 2017-02-05T22:15:25+00:00
Aaaah. Bugger. 

Can you think of any simple way to let the user know when the daemon has successfully terminated without checking the logs?

## moneromooo-monero | 2017-02-05T22:39:17+00:00
Yes, check the PID does not run anymore.

## moneromooo-monero | 2017-02-05T22:39:59+00:00
But really, the best way is to ensure the RPC waits till the end (or close enough).

## moneromooo-monero | 2017-08-08T11:33:47+00:00
I think best way to do this would be to get the calling daemon to wait. Posibly by adding a "wait" boolean to the RPC call, which would cause the receiving daemon to wait till most of the CN layers are down (not sure how much it can wait before blocking though). Otherwise, by having the calling daemon check for when the other process dies. Not sure the effort/gain is good though.

## moneromooo-monero | 2017-10-03T21:18:32+00:00
It's a daemon. Daemons are discreet creatures. They keep their logs to... logs. We'll keep it typical.

+invalid


# Action History
- Created by: ghost | 2017-02-05T11:01:40+00:00
- Closed at: 2017-10-03T21:24:23+00:00
