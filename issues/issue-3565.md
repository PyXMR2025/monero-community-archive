---
title: Will 'unspent_outputs' json rpc be implemented?
source_url: https://github.com/monero-project/monero/issues/3565
author: egonson
assignees: []
labels:
- invalid
created_at: '2018-04-06T03:23:31+00:00'
updated_at: '2018-10-01T14:32:14+00:00'
type: issue
status: closed
closed_at: '2018-05-18T09:01:09+00:00'
---

# Original Description
I need 'unspent_outputs' json rpc method to manage outputs (consolidating, dividing...).
I saw wallet-cli supports that command.
I must know when i should sweep the changes. To do so, I need the method to list all unspent outputs in program.
Or is there any other method?

# Discussion History
## moneromooo-monero | 2018-04-11T09:57:36+00:00
You're looking for "incoming_transfers", with the "available" transfer type.

## moneromooo-monero | 2018-05-18T08:37:35+00:00
+invalid

## gituser | 2018-10-01T14:32:14+00:00
I've just stumbled across same issue that there is no `unspent_outputs` equivalent for RPC.

And, no `incoming_transfers` with `available` transfer_type isn't solving the issue, because it will not show you block number and number of keys in that block number, instead it will show you some internal `global_index` instead.

I've looked into the code and it uses some internal flag `m_spent` here from RPC `get_transfers` method instead in the `unspent_outputs`: https://github.com/monero-project/monero/blob/master/src/simplewallet/simplewallet.cpp#L6881

I wasn't able to reproduce fully cli method `unspent_outputs` via RPC call `incoming_transfers` or `get_transfers` to get similar output.

Maybe you could just add block number into the output of `incoming_transfers` ?

# Action History
- Created by: egonson | 2018-04-06T03:23:31+00:00
- Closed at: 2018-05-18T09:01:09+00:00
