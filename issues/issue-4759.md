---
title: Enter password (output received) ？？？
source_url: https://github.com/monero-project/monero/issues/4759
author: wwaayyaa
assignees: []
labels:
- invalid
created_at: '2018-10-30T03:28:23+00:00'
updated_at: '2018-10-30T10:09:10+00:00'
type: issue
status: closed
closed_at: '2018-10-30T10:09:10+00:00'
---

# Original Description
`./monero-wallet-cli --shared-ringdb-dir=/work/wallets/xmr/.shared-ringdb --trusted-daemon --daemon-address IP:PORT --password PASSWORD
2018-10-30 03:09:06,246 INFO  [default] Page size: 4096
This is the command line monero wallet. It needs to connect to a monero
daemon to work correctly.
WARNING: Do not reuse your Monero keys on another fork, UNLESS this fork has key reuse mitigations built in. Doing so will harm your privacy.

Monero 'Beryllium Bullet' (v0.13.0.2-release)
Logging to ./monero-wallet-cli.log
Specify wallet file name (e.g., MyWallet). If the wallet doesn't exist, it will be created.
Wallet file name (or Ctrl-C to quit): 4DS****wallet
Wallet and key files found, loading...
Opened wallet: 491GyZY********************VTp2H
**********************************************************************
Use the "help" command to see the list of available commands.
Use "help <command>" to see a command's documentation.
**********************************************************************
Starting refresh...
**Enter password (output received):**    // <- Why is this line appearing?
`

It makes me very upset，It sometimes appears, sometimes not, I don't know the rules of his appearance.
And I'm using "expect" packet, it broke my plan。

Is there any way to turn off this feature?


# Discussion History
## hyc | 2018-10-30T05:17:43+00:00
If you're automating/scripting, you should probably be using monero-wallet-rpc instead. Parsing -cli output is always going to be unreliable.

## moneromooo-monero | 2018-10-30T10:07:51+00:00
Also, set ask-password to 0 or 1, not 2.
Anyway, not a bug.

+invalid

# Action History
- Created by: wwaayyaa | 2018-10-30T03:28:23+00:00
- Closed at: 2018-10-30T10:09:10+00:00
