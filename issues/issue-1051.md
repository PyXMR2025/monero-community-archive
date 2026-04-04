---
title: A couple of implementation questions
source_url: https://github.com/monero-project/monero/issues/1051
author: Crypto2
assignees: []
labels: []
created_at: '2016-09-04T23:59:30+00:00'
updated_at: '2016-12-15T17:33:09+00:00'
type: issue
status: closed
closed_at: '2016-12-15T17:33:09+00:00'
---

# Original Description
Hi, I'm implementing Monero in a system processing payments and user deposits. 
1. From the docs so far I plan on having a single simplewallet and each payment will have it's own payment ID as well as user deposits will be identified by payment ID using integrated addresses. Is this the best practice for a system with thousands of users?
2. Part of handling incoming payments is uniquely identifying them, in Bitcoin for example in a particular transaction there can only be one output to any given address so you can uniquely identify by txid and address. In Monero are transactions the same way? ie. If you see a payment with tx_hash X is that guaranteed to be the only payment with that tx_hash in your wallet or would you uniquely identify by block_height and tx_hash?
3. Looking at the source of the get_bulk_payments RPC call, if you leave out the 'payment_ids' param it returns all your incoming payments, correct?


# Discussion History
## moneromooo-monero | 2016-09-11T14:14:02+00:00
1. Yes. Note that all wallets do not support sending to integrated addresses, so you may want to have a fallback using full size payment ids.
2. I'm not sure exactly what you're saying here. Only one transaction will have the same hash (within cryptographically small probability). You can uniquely identify a tx from its txid (which is its hash). That transaction will have several outputs (0 to N, a subset of which will be to you).
3. Yes.

You may also want to check out the newer "get_transfers" RPC call, which is a bit nicer to use IMHO.


## Crypto2 | 2016-09-17T07:27:40+00:00
Hi, thanks for the answers.

On 2) what I mean is can there can be more than one payment to my address in one transaction (a single tx_hash.) Since there is no sub-identifier that would be pretty confusing since the only difference would be the amount (and then you could have a case of two with the same amount.) Just as an example in Bitcoin they disallow that in the transaction checking code so there can't be two outputs to the same address in a single transaction, I don't know if XMR is similar.

I don't see a 'get_transfers' API call in the docs and RPC says the method isn't found. I see 'incoming_transfers' but it doesn't include payment IDs so it doesn't look like it's much use.


## moneromooo-monero | 2016-09-18T09:13:01+00:00
You can have any number of outputs to your address in a single tx. In fact, this is the common case, due to the splitting by denominations. So if you receive 435 monero in a tx, you will in fact receive three outputs: 400, 30, and 5.

incoming_transfers shows at the output level, so you'll see those three. show_transfers (which is fairly new, so you may need to update to git version, but there'll be new binaries in the next few days otherwise) shows at the payment level, so you'll see just one payment of 435.


# Action History
- Created by: Crypto2 | 2016-09-04T23:59:30+00:00
- Closed at: 2016-12-15T17:33:09+00:00
