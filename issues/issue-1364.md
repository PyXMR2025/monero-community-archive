---
title: Multisig support
source_url: https://github.com/monero-project/monero-gui/issues/1364
author: mmitech
assignees: []
labels: []
created_at: '2018-04-30T09:02:02+00:00'
updated_at: '2020-09-27T08:13:58+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Any plans to support multisig?

# Discussion History
## krtschmr | 2018-04-30T14:03:05+00:00
i think that's not the highest priority as the setup is pretty complicated right now. do you have any idea how integration could look like?

## lessless | 2018-09-22T17:53:55+00:00
I guess there should be a new option on the wallet creation (opening, restoration) page with a sequence of steps for N/N and N/M wallets. Maybe on the one screen.
Then transaction sending should also account for additional step to open unsigned transactions (which maybe can be relevant outside of the multisig scope?)

Multisgnatures is a very strong offer and I hope it will get attention it deserves. 

## jonathancross | 2019-04-15T11:53:47+00:00
> Then transaction sending should also account for additional step to open unsigned transactions (which maybe can be relevant outside of the multisig scope?)

@lessless The GUI already handles loading / saving (non-multisig) transactions for signing.

## crocket | 2020-09-27T08:12:32+00:00
Multisig on gui wallet would allow me to trust a random seller on the internet with delivery of physical goods in good conditions.

I'm thinking of making sellers adopt monero. Without multisig, I can't trust them much. Perhaps, does OpenBazaar accept monero?

# Action History
- Created by: mmitech | 2018-04-30T09:02:02+00:00
