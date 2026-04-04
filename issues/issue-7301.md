---
title: tx-notify seems not working
source_url: https://github.com/monero-project/monero/issues/7301
author: netwarp
assignees: []
labels: []
created_at: '2021-01-09T13:08:03+00:00'
updated_at: '2021-01-09T14:46:31+00:00'
type: issue
status: closed
closed_at: '2021-01-09T14:46:31+00:00'
---

# Original Description
I would like to be notified on each transaction incoming in my wallet.
In a first terminal, I run 
`monerod --stagenet --block-notify "/bin/echo %s" `
In this one everything works.

In a second terminal, I run:
`monero-wallet-rpc --stagenet --rpc-bind-ip=127.0.0.1 --rpc-bind-port=18089 --disable-rpc-login --log-level=3 --wallet-file=sn1 --prompt-for-password --tx-notify "/bin/echo %s"`
or 
`monero-wallet-rpc --stagenet --rpc-bind-ip=127.0.0.1 --rpc-bind-port=18089 --disable-rpc-login --log-level=3 --wallet-file=sn1 --prompt-for-password --tx-notify "node /home/me/notify.js"`

No one of those scripts is working.
What can I do to run a script when the pool detects a new transaction ?
Thanks


# Discussion History
## netwarp | 2021-01-09T14:46:31+00:00
Got it.
I change --log-level=3 by log-level=0 and it's work.

# Action History
- Created by: netwarp | 2021-01-09T13:08:03+00:00
- Closed at: 2021-01-09T14:46:31+00:00
