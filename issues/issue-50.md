---
title: rpc save command causes wallet timeout
source_url: https://github.com/monero-project/monero/issues/50
author: ghost
assignees: []
labels: []
created_at: '2014-06-21T17:11:57+00:00'
updated_at: '2014-08-21T09:17:14+00:00'
type: issue
status: closed
closed_at: '2014-08-21T09:17:14+00:00'
---

# Original Description
Currently the RPC save blockchain command communicates to the daemon and waits for a response; however, because blockchain storage at the daemon takes a long time, the wallet always timesout waiting for the RPC to respond and freezes the wallet.

Proper wallet behaviour for save blockchain functionality should prevent the wallet from timing out while it waits for the daemon to complete saving the blockchain.


# Discussion History
## Neozaru | 2014-06-22T20:36:13+00:00
The daemon should indeed respond as soon as the request is accepted, a not after the blockchain storage is completed. This method was implemented when the blockchain storage took less than 2 secs.
I don't know if the best thing to do is to change the behavior of this RPC call, or to disable it completely from the Wallet : This is not the role of the Wallet to send directives to the daemon, and the blockchain storage will be migrated to a more efficient system (database)


## Jojatekok | 2014-06-30T07:53:00+00:00
Storing the blockchain should not overwrite the whole file, but should append to it (like in a DB, as @Neozaru mentioned above). Thus, even **automatic async savestates** could be allowed each 'n' blocks/minutes _(with a new command-line argument --autosave [arg])._


## fluffypony | 2014-08-21T09:17:14+00:00
Fixed in rpcwallet, although a more thorough fix will be with the move to BlockchainDB


# Action History
- Created by: ghost | 2014-06-21T17:11:57+00:00
- Closed at: 2014-08-21T09:17:14+00:00
