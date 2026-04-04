---
title: '[Idea] Sidechain with unspendable outputs after a year'
source_url: https://github.com/monero-project/research-lab/issues/81
author: SamsungGalaxyPlayer
assignees: []
labels: []
created_at: '2021-01-27T15:45:42+00:00'
updated_at: '2021-01-27T18:02:14+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Adding this here mostly for reference and to get some gears moving. This is certainly not a fleshed out proposal or anything remotely close.

We worry about blockchain efficiency since transaction sizes and verification grows forever. What if it didn't grow forever.

Introducing... a Monero sidechain that prevents the spending of funds a year after they are created.

Basically, all outputs older than a certain block height can be totally forgotten by nodes. Any new transactions that reference these old outputs will be tossed.

Advantages:
* Transactions can be huge
* Transactions can take forever to verify
* Transactions can be cheap
* Accounts for most user behavior (spending within a few days)

Disadvantages:
* Funds can be destroyed if a user if forgetful
* Possibly lower user adoption/anonymity than Monero natively

Unknowns:
* How to swap into and out of this asset
* Everything else

# Discussion History
## jedigras | 2021-01-27T18:01:15+00:00
there are a bunch of problems with this, but mainly, if you are doing this for convenience but trying to maintain privacy, it may not work.

your ring signature transaction input pool is going to be mighty small...

if you don't care about sidechain privacy, then just wait until 2 way atomic swaps work with other chains... 

my $0.02

## tevador | 2021-01-27T18:02:14+00:00
> Basically, all outputs older than a certain block height can be totally forgotten by nodes

That's not entirely true. Historical transactions are needed for chain verification. Otherwise you can't convince new nodes joining the network that there are no counterfeit/stolen coins.

# Action History
- Created by: SamsungGalaxyPlayer | 2021-01-27T15:45:42+00:00
