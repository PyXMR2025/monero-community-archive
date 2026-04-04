---
title: CLI wallet disconnects from node when creating transaction
source_url: https://github.com/monero-project/monero/issues/4059
author: dprestegard
assignees: []
labels: []
created_at: '2018-06-27T07:37:31+00:00'
updated_at: '2018-06-27T21:14:24+00:00'
type: issue
status: closed
closed_at: '2018-06-27T21:14:24+00:00'
---

# Original Description
Hello!

I'm on 0.12.2.0 on both node and cli wallet. The node is on Ubuntu, the wallet is on windows.

I'm running the node as follows (on a VM):

`monerod --data-dir $pathToBlockchain --rpc-bind-ip 0.0.0.0 --restricted-rpc --confirm-external-bind --rpc-login $credentials`

I'm running the wallet as follows (locally)

`monero-wallet-cli --daemon-host $nodeIp --daemon-login $credentials`

It connects, I load my wallet, and it shows my balance. I try to transfer some monero, and I get an error like this:

`"Error: Wallet failed to connect to daemon: http://$nodeIp:18081`

I turned off the firewall to be sure, same result. When I curl http://$nodeIp:18081 I get a a 401 Unauthorized Access error.

This used to work, I just haven't sent any monero in awhile.

Switching to the 0.12.1.0 wallet works fine.

# Discussion History
## dprestegard | 2018-06-27T07:42:34+00:00
Verified the issue still occurs using the client from https://build.getmonero.org/builders/monero-static-win64/builds/4766 which looks like a recent master build as far as I can tell.

## dEBRUYNE-1 | 2018-06-27T08:07:58+00:00
That build, most likely, does not include #3962, which supposedly fixes your particular issue. 

## dprestegard | 2018-06-27T08:27:09+00:00
Just switched the node to the latest master build https://build.getmonero.org/builders/monero-static-ubuntu-amd64/builds/4656 and kept the wallet on 0.12.2.0 and it works :)

## dEBRUYNE-1 | 2018-06-27T17:31:23+00:00
@dprestegard - I suppose I can mark this as resolved then? 

## dprestegard | 2018-06-27T21:14:22+00:00
Yep, I suppose so!

# Action History
- Created by: dprestegard | 2018-06-27T07:37:31+00:00
- Closed at: 2018-06-27T21:14:24+00:00
