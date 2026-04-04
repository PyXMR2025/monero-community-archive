---
title: Problem starting monerod
source_url: https://github.com/monero-project/monero/issues/3582
author: Solusan
assignees: []
labels:
- invalid
created_at: '2018-04-08T03:14:19+00:00'
updated_at: '2018-06-20T09:25:10+00:00'
type: issue
status: closed
closed_at: '2018-06-20T09:25:10+00:00'
---

# Original Description
Hi,

I tried to start monerod with this command:

/Users/USER/monero-wallet-gui.app/Contents/MacOS/monerod --rpc-bind-ip 10.10.10.1 --confirm-external-bind --data-ir .

Until now was working fine, now I'm in panic cause i get this message:

```
dyld: lazy symbol binding failed: Symbol not found: _clock_gettime
  Referenced from: /Users/USER/monero-wallet-gui.app/Contents/MacOS/monerod (which was built for Mac OS X 10.12)
  Expected in: /usr/lib/libSystem.B.dylib

dyld: Symbol not found: _clock_gettime
  Referenced from: /Users/USER/monero-wallet-gui.app/Contents/MacOS/monerod (which was built for Mac OS X 10.12)
  Expected in: /usr/lib/libSystem.B.dylib

Trace/BPT trap: 5
```
Does anyone can help me?

Thanks a lot.

# Discussion History
## dEBRUYNE-1 | 2018-04-08T18:40:58+00:00
The GUI v0.12 binaries were updated to resolve this issue. I'd suggest to redownload them from here:

https://github.com/monero-project/monero-gui/releases/tag/v0.12.0.0



## Solusan | 2018-04-09T02:31:25+00:00
@dEBRUYNE-1 After a new installation it works! Thanks for your kindly help :)

## moneromooo-monero | 2018-06-20T08:58:42+00:00
+invalid

# Action History
- Created by: Solusan | 2018-04-08T03:14:19+00:00
- Closed at: 2018-06-20T09:25:10+00:00
