---
title: Change default log level to avoid exposing public address and txids
source_url: https://github.com/monero-project/monero/issues/1644
author: monerohow
assignees: []
labels: []
created_at: '2017-01-28T14:42:38+00:00'
updated_at: '2017-08-08T12:00:18+00:00'
type: issue
status: closed
closed_at: '2017-08-08T12:00:18+00:00'
---

# Original Description
Request: change default log level for CLI wallet so that no logs are written unless otherwise specified.

Some users don't have encrypted file storage (either because they have unencrypted hard drives, or use unencrypted online backup, or keep their files on company/university storage which other people can inspect, or keep their wallet on an unencrypted flash drive).

For these people, it'd be useful if the CLI wallet did not log to disk by default, so that they can rely completely on the encryption provided by the wallet password. Otherwise, their public address and txids are exposed in the log file if anyone gets access to the location of their wallet.

# Discussion History
## moneromooo-monero | 2017-01-28T15:02:23+00:00
It's a bit of an annoying one, as it requires cleanup of how user output is made. Monero inherits code which makes user output from the internal libraries, and which needs to stay visible on the console. There is no fine grained selection of what goes to the console or log currently, except using console writer classes, but these do not belong to the libs, only to the user level programs.

So this needs doing, but isn't just a trivial change.

## ghost | 2017-01-28T21:37:05+00:00
In the interim you can set --log-level=OFF

## monerohow | 2017-01-28T22:00:34+00:00
Perfect, that's a good solution, thanks.

## moneromooo-monero | 2017-01-29T12:47:51+00:00
<s>You will lose the "transaction sent: txid XXXXXX" messages on the console too, though.</s>

Actually, I'm confused, simplewallet does print a separate message, so the one in wallet2 can be moved to L1.



## moneromooo-monero | 2017-08-08T11:34:31+00:00
+resolved

# Action History
- Created by: monerohow | 2017-01-28T14:42:38+00:00
- Closed at: 2017-08-08T12:00:18+00:00
