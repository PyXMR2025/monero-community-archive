---
title: Better UX for transactions that are stuck as pending
source_url: https://github.com/monero-project/monero/issues/5745
author: tobtoht
assignees: []
labels: []
created_at: '2019-07-09T13:23:12+00:00'
updated_at: '2019-07-09T14:47:00+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
A common issue lately is remote nodes failing to relay transactions to the network, leaving them stuck as pending until they get cleared from the node pool.
To resolve this in a timely matter the user has to switch to a different remote node and use `rescan_spent`. This is not only bad UX, but it can also result in an unexpected loss of funds if the transaction does end up getting relayed.

Does the CLI store the raw transaction so that it can be manually submitted to a transaction pusher in case this happens?
I looked briefly at the code, but it appears that the raw transaction is only stored when the `--do-not-relay` flag is used. Perhaps a `--save-tx-to-file` flag can be added that would relay + save?
Or, would it make more sense to (temporarily) store the (pending) transaction blob in the wallet cache?

A wallet command could be added to show the raw transaction, for example: `get_raw_tx <txid>`. The output can then be submitted to a tx pusher.

Or, perhaps `submit_transfer` could be extended to allow `submit_transfer <daemon_address> <txid>` to submit the transaction to a different daemon.

A more robust solution could be to have the CLI automatically submit the transaction to multiple (user-specified) daemons.

# Discussion History
## moneromooo-monero | 2019-07-09T13:38:53+00:00
Keeping the entire tx till mined seems like a good idea. Along with a submit TXID command.

A better solution is to not rely on a stranger doing your work for you though.


## tobtoht | 2019-07-09T14:39:34+00:00
>A better solution is to not rely on a stranger doing your work for you though.

While I agree, running a local node cannot realistically be expected of all users in all environments.

Besides, having the option to quickly relay transactions to the network through a different node is also beneficial for users that are connected to their local node if it unexpectedly happens to experience relaying issues.

## moneromooo-monero | 2019-07-09T14:47:00+00:00
The daemon can already do it (relay command).

# Action History
- Created by: tobtoht | 2019-07-09T13:23:12+00:00
