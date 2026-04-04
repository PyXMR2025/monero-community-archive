---
title: Wallet RPC `get_transfers` incoming vs outgoing pool transactions
source_url: https://github.com/monero-project/monero/issues/1825
author: amiuhle
assignees: []
labels: []
created_at: '2017-03-01T16:21:47+00:00'
updated_at: '2017-08-07T15:46:33+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
When called with `{"pool": true}`, `get_transfers` will return both incoming and outgoing transactions.

There's no way to tell whether a transaction is incoming or outgoing.

# Discussion History
## moneromooo-monero | 2017-03-01T20:05:42+00:00
If it sends anything out, it's outgoing. If not, it's incoming.

## amiuhle | 2017-03-01T20:54:34+00:00
I'm using this with a view-only wallet and want to be able to identify incoming pool payments, so checking for outgoing transactions doesn't work.

## moneromooo-monero | 2017-03-01T22:30:22+00:00
Then if the wallet does not have the key images, it cannot know, can it ?

## amiuhle | 2017-03-02T09:23:05+00:00
I think checking for incoming payments with a view-only wallet behind `monero-wallet-rpc` is a pretty common use-case. No need to upload a wallet being able to send funds to some publicly available server.

`get_transfers '{"pool":true}'` does this for unconfirmed transactions, however since this will also include outgoing payments, there's the following edge case: While checking for incoming transactions with a given payment id, if someone sends funds with the same payment id from that wallet, this transaction would incorrectly be accepted as a payment.

So, is there any other way to check for unconfirmed payments using wallet-rpc? If not, could we add a flag to the returned `transfer_entry` structure to indicate whether the transaction is incoming or outgoing?

## amiuhle | 2017-03-04T11:39:26+00:00
Sending a notification to @moneromooo-monero 

## moneromooo-monero | 2017-03-04T21:37:59+00:00
A wallet with a view key but no spend key nor key images for the outputs it has does not see outgoing spends. Therefore, it can't tell whether you're spending. Therefore, if it sees something incoming, it can't know whether it's an incoming payment from another wallet, or change.

If you think this is incorrect, please say why you think so.

Also, maybe I'm missing your point, so you might want to try rephrashing what you want to do, with mode details about your setup. Canonical use should work (though it might be buggy right now as it's not used very much I think).

## iamsmooth | 2017-03-06T00:22:38+00:00
A method to address ambiguity over what is change (which currently doesn't exist but would be useful for other reasons) would be to have change go to a different wallet. Therefore no change would ever be received and all received payments would be incoming.

## kenshi84 | 2017-03-06T00:59:01+00:00
Maybe the subaddress scheme in PR #1753 can be helpful for that in the future, since all the changes are received by the original address (index=0) while you use other subaddresses (index!=0) for receiving payments.

## moneromooo-monero | 2017-03-06T09:20:04+00:00
That's a very interesting point kenshi84. This would avoid the premature depletion if one was sending to a different address altogether.

# Action History
- Created by: amiuhle | 2017-03-01T16:21:47+00:00
