---
title: monero-wallet-rpc not reporting incoming transactions to account 0
source_url: https://github.com/monero-project/monero/issues/4428
author: woodser
assignees: []
labels: []
created_at: '2018-09-24T13:57:57+00:00'
updated_at: '2018-09-30T22:04:56+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
monero-wallet-rpc is not reporting incoming transactions to account 0 when using the `get_transfers` and `get_bulk_payments` methods, whereas the incoming transactions are reported as expected using the `incoming_transfers` method.  All other accounts work as expected.

The attachments show that `incoming_transfers` reports all 4 incoming transactions to account 0 whereas `get_transfers` and `get_bulk_payments` do not show any.

[monero-wallet-cli.txt](https://github.com/monero-project/monero/files/2411048/monero-wallet-cli.txt) shows the complete transaction sent from [0,0] to 9 subaddresses in the same wallet across [0-2][0-2] using monero-wallet-cli.

The transaction id in question is 409778b3e5abbbeb3b35c9b532001e8b1c84b8743c40728219eeeb95c1c283bf.

[get_transfers.txt](https://github.com/monero-project/monero/files/2411046/get_transfers.txt) shows the monero-wallet-rpc request and response from querying account 0 with `get_transfers`.  No incoming transactions are found.

[incoming_transfers.txt](https://github.com/monero-project/monero/files/2411047/incoming_transfers.txt) shows the monero-wallet-rpc request and response from querying account 0 with `incoming_transfers`.  4 incoming transactions are found which is correct.

[get_bulk_payments.txt](https://github.com/monero-project/monero/files/2411045/get_bulk_payments.txt) shows the monero-wallet-rpc request and response from querying account 0 with `get_bulk_payments`.  6 incoming transactions are found but they are not in account 0.  The account 0 results are omitted.

Environment: Mac OS, Stagenet, v0.12.3.0.

# Discussion History
## woodser | 2018-09-30T22:04:56+00:00
After talking with @moneromooo-monero, it seems the issue is the incoming transactions are being occluded by their outgoing counterpart since funds are sent from and to the same account.

# Action History
- Created by: woodser | 2018-09-24T13:57:57+00:00
