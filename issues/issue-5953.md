---
title: '[Request] add transaction decoding to wallet-rpc'
source_url: https://github.com/monero-project/monero/issues/5953
author: mirathewhite
assignees: []
labels:
- invalid
created_at: '2019-10-02T16:45:33+00:00'
updated_at: '2019-10-10T13:51:45+00:00'
type: issue
status: closed
closed_at: '2019-10-10T12:49:46+00:00'
---

# Original Description
It would be very helpful to be able to validate transactions signed in cold storage prior to broadcast.  (Basically, a last minute sanity check in the view wallet).  

Input: a signed transaction hex,
Output: recipient address, tx amount, and fee.  Alternatively, the meta-data that the daemon-rpc returns for get_transactions.

# Discussion History
## moneromooo-monero | 2019-10-02T16:49:51+00:00
Do you know about describe_transfer, and does it not fit your needs ?

## mirathewhite | 2019-10-03T13:35:54+00:00
Yes!  Thank you @moneromooo-monero. Do you know when `describe_transfer` will be added to monero-wallet-rpc?  The current wallet documentation does not mention this function. https://web.getmonero.org/resources/developer-guides/wallet-rpc.html

## moneromooo-monero | 2019-10-03T13:41:16+00:00
It was added in the past. Is it not working ?

## jtgrassie | 2019-10-08T05:58:59+00:00
@mirathewhite it's just not documented in the guide. `describe_transfer` takes a string parameter of either `unsigned_txset` or `multisig_txset`.

## moneromooo-monero | 2019-10-10T12:47:54+00:00
Already exists. I think someone is paid to update the docs from time to time so it'll get there.

+invalid


## erciccione | 2019-10-10T13:48:28+00:00
> I think someone is paid to update the docs from time to time so it'll get there.

AFAIK currently nobody is paid or have an open CCS proposal for that. An update of the dev guides is very needed tho, so if somebody wants to take care of that, please do. I would also totally support a CCS with that goal. 

If you find other important stuff is missing in the docs, plese open an issue [on gitlab](https://repo.getmonero.org/monero-project/monero-site) or let us know somehow, so we can keep track of what needs to be updated. In the meantime i [opened an issue](https://repo.getmonero.org/monero-project/monero-site/issues/1002) about this one.

# Action History
- Created by: mirathewhite | 2019-10-02T16:45:33+00:00
- Closed at: 2019-10-10T12:49:46+00:00
