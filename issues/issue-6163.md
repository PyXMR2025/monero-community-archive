---
title: 'Wallet: Distinguish transfers made to a subaddress in a single transaction
  while in txpool'
source_url: https://github.com/monero-project/monero/issues/6163
author: tmoravec
assignees: []
labels: []
created_at: '2019-11-20T15:31:40+00:00'
updated_at: '2020-02-20T03:23:22+00:00'
type: issue
status: closed
closed_at: '2020-02-20T03:23:22+00:00'
---

# Original Description
Imagine we have multiple transfers made to a single subaddress in a single transaction:

    transfer <addr1> <amount1> <addr1> <amount2>

We can distinguish these transfers in `incoming_transfers`. Unfortunately, `incoming_transfers` is not available for txpool transactions because such transactions don't include all info that `incoming_transfers` needs (e.g., global output indices).

The appropriate method for learning about txpool transactions is `get_transfers`. Unfortunately, `get_transfers` doesn't distinguish between multiple outputs aiming to a single subaddress (see https://github.com/monero-project/monero/blob/master/src/wallet/wallet2.cpp#L1779).

To learn about individual outputs in txpool transactions, Moneromooo suggested enhancing the `get_transfers` output with `std::vector<uint64_t> amounts;` in addition to the regular `amount`.

I'll try to implement this.

# Discussion History
## stoffu | 2019-12-05T03:07:11+00:00
What is the use case of this feature? Is it important enough to justify your patch #6190 making changes to the wallet scanning code which is relatively more critical than other parts?

## tmoravec | 2019-12-06T09:42:53+00:00
What's the usecase of several outputs then? If we can do it, the software should be able to distinguish it. It makes little sense to have a feature on the sending side if it's hidden on the receipient side.

## stoffu | 2019-12-09T03:09:29+00:00
In my understanding, the relevant command

    transfer <addr1> <amount1> <addr1> <amount2>

is only useful when you want to split your fewer larger outputs into more smaller outputs by sending funds to yourself. I don't see any other situation where this would be useful.

When you're splitting your outputs, you're the one who initiated the tx, so you have the full knowledge about the tx. Why do you care about being able to see your individual outputs coming to you in that tx in the tx pool?

> It makes little sense to have a feature on the sending side if it's hidden on the receipient side.

"It makes little sense" alone isn't a good enough reason to make changes to the code, especially for sensitive parts which shouldn't receive frequent changes. Any proposed changes must be supported by real demand and use case.


## tmoravec | 2020-01-07T11:31:15+00:00
For instance Minko if you're familiar with that. Minko uses this feature so players can play multiple bets of the same color in a single transaction. But this applies to any automated system where the buyer is to receive a specific piece (physical or digital) from seller for each output. If goods has its own subaddress, in order to buy multiple pieces of the goods in a single transaction, the seller needs to distinguish the outputs.

## arnuschky | 2020-01-07T13:17:38+00:00
Isn't just consistency a good enough reason? I mean, this information is available for confirmed tx through `incoming_transfers`. Making the same functionality available for unconfirmed pool payments seems only consistent to me.

## stoffu | 2020-01-09T09:15:16+00:00
@tmoravec 
> For instance Minko if you're familiar with that. Minko uses this feature so players can play multiple bets of the same color in a single transaction. But this applies to any automated system where the buyer is to receive a specific piece (physical or digital) from seller for each output. If goods has its own subaddress, in order to buy multiple pieces of the goods in a single transaction, the seller needs to distinguish the outputs.

Oh, I never thought of such use cases. Now I'm fine with your proposal.

BTW Minko already seems to be able to distinguish individual incoming outputs in a single unconfirmed tx, indicating that they use some modified version of wallet2 to enable that. It'd be nice if the developer of Minko could share that patch with us. Perhaps @binaryFate knows something?

@arnuschky 
I personally think that every non-trivial code change (such as this one touching wallet2 scanning) should come with tangible benefit such as new use cases or increased performance, because otherwise the commit log could get cluttered unnecessarily and potentially bugs or malicious code could be introduced.


## binaryFate | 2020-01-09T22:02:31+00:00
@stoffu Currently Minko uses some features from https://github.com/moneroexamples/onion-monero-blockchain-explorer additionally to the vanilla daemon (requiring to have both of them running), to be able to distinguish each output and also their respective order. So I'm afraid there is no "nice" or useful patch we can share.

The proposed patch here would be a nice simplification in practice for anyone needing that specific feature -- I did not check the proposed code itself though.  

## stoffu | 2020-01-10T09:02:48+00:00
@binaryFate Thank you for responding.

# Action History
- Created by: tmoravec | 2019-11-20T15:31:40+00:00
- Closed at: 2020-02-20T03:23:22+00:00
