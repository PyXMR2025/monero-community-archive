---
title: monero-wallet-rpc has very dangerous behavior when transferring
source_url: https://github.com/monero-project/monero/issues/5516
author: MoneroKing2000
assignees: []
labels: []
created_at: '2019-05-03T02:27:51+00:00'
updated_at: '2019-05-03T20:55:32+00:00'
type: issue
status: closed
closed_at: '2019-05-03T20:55:31+00:00'
---

# Original Description
Utiliznig monero-wallet-rpc with a remote node (untrusted) exhibits extremely dangerous bavior when transferring. This has been tested with monero integratino PHP client. However, it obviously an issue with the RPC server and not the client.

Upon creating a "transfer" transaction the RPC server returns a 401 not authorized response. Thus, the transfer is marked as failing.

However, this is not true. The transfer has actually succeeded and the funds leave the wallet. Thus, not only has the transfer functionality been broken as a result of returning an error, but it would lead any automated software to believe the funds never left in the first place when in fact they have.

The command is: monero-wallet-rpc --rpc-bind-ip=127.0.0.1 --rpc-bind-port=22113 --daemon-host=node.moneroworld.com:18089 --wallet-dir=/path/to/wallets --rpc-login=user:P248360072 --untrusted-daemon --detach

The daemon logs the spent money, so it is only an error in giving 401 error instead of the actual successful response.

Here is an example of a request that resulted in this 401 error you can observe from the ID field that 30+ other requests successfully completed with no issues, so it is an error specific in the transfer function:

> {"jsonrpc":"2.0","method":"transfer","params":{"destinations":[{"amount":2000000000,"address":"ADDRESS HERE"}],"mixin":11,"get_tx_key":true,"payment_id":"","account_index":0,"subaddr_indices":"","priority":2,"do_not_relay":false},"id":32}

# Discussion History
## moneromooo-monero | 2019-05-03T09:40:24+00:00
This happens with *all* nodes you tried or just one/some ?

If you choose to use a stranger's node rather than your own, there is no way to avoid this. Their software can do whatever it wants. It is your wallet's view of the blockchain. By using a stranger's node, you are abdicating your power to verify what happens on the chain. Use your own if you want more privacy, security, etc.


## Gingeropolous | 2019-05-03T15:15:14+00:00
@moneromooo-monero , 

> This happens with all nodes you tried or just one/some ?

as you prolly know, he indicates using node.moneroworld.com, which picks a random node from some DNS entry thingy. So who knows if its one or some. 

This is probably a useless comment. But I'm feeling productive. 

## moneromooo-monero | 2019-05-03T15:37:57+00:00
You're right, but if you try many times, you'll likely not get the same one all the time, right ? Depending on how the round robin works.
Then if it happens all the time, something's weird. If not, it's probably some jerk being an ass.


## italocoin-project | 2019-05-03T17:51:07+00:00
I've tried and i can't replicate the issue 

## MoneroKing2000 | 2019-05-03T19:17:40+00:00
I have tried at least 30 times, so it is all nodes as each time the nodes would be different on my computer. Considering the transaction succeeds but it returns a 401 my guess is that it is the "get_tx_key" option which according to the documentation is run after the transaction. It would make sense given the transaction completes but the response errors considering. 

I will test a transaction with that value set to false to test it and report back.

## moneromooo-monero | 2019-05-03T20:39:51+00:00
get_tx_key is not a daemon RPC.

## moneromooo-monero | 2019-05-03T20:40:47+00:00
Can you run the wallet with --log-level 2, and post the logs ? If you're worried about leaking private data, you can encrypt the logs with my public key found in the monero tree, utils/gpg_keys

## MoneroKing2000 | 2019-05-03T20:55:31+00:00
The issue has been discovered and it was pretty stupid and not related. It appears curl when it hits a timeout when there is authentication passed returns a 401 header. The transfer command takes far longer than other commands and as a result the timeout was being hit and curl returned a 401 error. Since it was client side the transfer continued to go through of course.

# Action History
- Created by: MoneroKing2000 | 2019-05-03T02:27:51+00:00
- Closed at: 2019-05-03T20:55:31+00:00
