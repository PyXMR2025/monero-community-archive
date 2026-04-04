---
title: 'wallet-cli: unable connect monero-wallet-cli to v0.12.2.0 daemon'
source_url: https://github.com/monero-project/monero/issues/3930
author: coneiric
assignees: []
labels: []
created_at: '2018-06-05T04:35:17+00:00'
updated_at: '2018-06-05T16:15:34+00:00'
type: issue
status: closed
closed_at: '2018-06-05T16:15:34+00:00'
---

# Original Description
After successfully building, migrating database, and syncing with peers, `monero-wallet-cli` gives the following error:
```
Error: wallet failed to connect to daemon: http://localhost:18081. Daemon either is not started or wrong port was passed. Please make sure daemon is running or change the daemon address using the 'set_daemon' command.
```
Error occurs with old and newly created wallets. Looking through the logs, some potentially relevant errors: [https://pastebin.mozilla.org/9086988](https://pastebin.mozilla.org/9086988)

# Discussion History
## moneromooo-monero | 2018-06-05T10:45:16+00:00
That DB error is unrelated.

I assume you can reach the daemon via telnet from where you're running the wallet. If not, fix it.
Then run the dameon with --log-level 2, and post the log excerpt when you run the wallet.

## coneiric | 2018-06-05T16:15:34+00:00
> I assume you can reach the daemon via telnet from where you're running the wallet

Awesome, that worked! Apologies for the non-issue, and thanks for the help.

# Action History
- Created by: coneiric | 2018-06-05T04:35:17+00:00
- Closed at: 2018-06-05T16:15:34+00:00
