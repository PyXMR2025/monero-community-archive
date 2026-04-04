---
title: monero-wallet-rpc JSON RPC interface unusable
source_url: https://github.com/monero-project/monero/issues/5860
author: abyssal0
assignees: []
labels: []
created_at: '2019-08-27T09:44:29+00:00'
updated_at: '2019-08-29T08:56:45+00:00'
type: issue
status: closed
closed_at: '2019-08-29T08:56:45+00:00'
---

# Original Description
The title
After executing the start command:
./bin/monerod
The call to daemon RPC was successful
The call to wallet RPC failed
How can I solve the problem?

# Discussion History
## xiphon | 2019-08-27T10:54:50+00:00
You also have to start the wallet `monero-wallet-rpc`.

## abyssal0 | 2019-08-28T02:07:55+00:00
the option '--rpc-bind-port' is required but missing
I added,but prompt:
This is the RPC monero wallet. It needs to connect to a monero
daemon to work correctly
How can I start the wallet `monero-wallet-rpc` right



## xiphon | 2019-08-28T02:30:30+00:00
Please provide the command you ran and the output

## abyssal0 | 2019-08-28T03:58:05+00:00
command : ./bin/monero-wallet-rpc
output: Failed to parse arguments: the option '--rpc-bind-port' is required but missing
command : /bin/monero-wallet-rpc --rpc-bind-port 18082
output: This is the RPC monero wallet. It needs to connect to a monero
daemon to work correctly.


## xiphon | 2019-08-28T10:40:19+00:00
Something is odd then. There should be another error message. Literally ` Must specify --wallet-file or --generate-from-json or --wallet-dir`

## moneromooo-monero | 2019-08-28T10:57:05+00:00
This is not an error fwiw, someone thought it best to print this at every run. But this is a bug tracker, not a help desk. If there's no bug you can point to, I'll be closing this. For help using monero, try #monero on Freenode.


## abyssal0 | 2019-08-29T01:24:59+00:00
> Something is odd then. There should be another error message. Literally ` Must specify --wallet-file or --generate-from-json or --wallet-dir`

yes,You're right
E Must specify --wallet-file or --generate-from-json or --wallet-dir

# Action History
- Created by: abyssal0 | 2019-08-27T09:44:29+00:00
- Closed at: 2019-08-29T08:56:45+00:00
