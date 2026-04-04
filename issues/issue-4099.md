---
title: Unauthorized Access Monero RPC
source_url: https://github.com/monero-project/monero/issues/4099
author: 5-digits
assignees: []
labels:
- invalid
created_at: '2018-07-05T16:21:10+00:00'
updated_at: '2018-09-04T23:16:55+00:00'
type: issue
status: closed
closed_at: '2018-09-04T23:16:55+00:00'
---

# Original Description
I Configured the monero rpc with the command with the following command lines:

1/ First I run the monero daemon : [ ./monerod --testnet --rpc-bind-ip=x.x.x.x --rpc-bind-port=28081 --rpc- login user:password --confirm-external-bind](url)

2/Then I configured the monero-rpc : [ ./monero-wallet-rpc --wallet-file testwallet --password test --rpc-bind- port 28082 --rpc-bind-ip=x.x.x.x --daemon-address x.x.x.x.x:28081 - -testnet --daemon-login user:password --log-level 4 --confirm-external-bind
] (credit to Wejden )

Result : The RPC server Connetc Succefully but when request any like ( getheight ), it return an "Unauthorized Access" . 


# Discussion History
## moneromooo-monero | 2018-07-05T18:30:27+00:00
Are you sure you're authenticating (digest HTTP auth) ?

## 5-digits | 2018-07-06T08:38:38+00:00
For sure i'm authenticating 

## moneromooo-monero | 2018-07-06T09:04:11+00:00
You're saying monero-wallet-rpc can connect to monerod, but RPC actually fails, right ?
monero-wallet-rpc logs should include the HTTP data sent to the daemon. Find it, and post it.

## moneromooo-monero | 2018-08-15T11:15:17+00:00
If no further comment, I'll be assuming you didn't auth correctly and close.

## moneromooo-monero | 2018-09-04T23:02:33+00:00
Closing then. Please reopen if you have further info.

+invalid

# Action History
- Created by: 5-digits | 2018-07-05T16:21:10+00:00
- Closed at: 2018-09-04T23:16:55+00:00
