---
title: Proposal on how to decouple from Bitcoin and become standalone coin.
source_url: https://github.com/monero-project/meta/issues/1010
author: Kreyren
assignees: []
labels: []
created_at: '2024-05-19T01:58:54+00:00'
updated_at: '2024-05-23T20:06:55+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
As far as i know the thing that prevents Monero from being a standalone coin is the reliability on Bitcoin for:
1. XMR<->FIAT

To manage this i propose to implement a method for atomic swaps in Monero Wallets e.g. https://github.com/monero-project some wallets such as the cake wallet already does this.

2/3. Swaps to other currencies + Ability to buy XMR with FIAT

[Haveno](https://github.com/haveno-dex/haveno) should be the solution to this once it's more established to get funds in the virtual form

Additionally to that [The Monero ATM Project](https://github.com/monero-atm) should address the physical form.

For this to be effective there should be a Monero ATM in every major city in at least the EU and to achieve that we should make a fund to cover or help with the expenses of building the ATM.

---

Additionally to managing dependency on Bitcoin, Monero should be much more practically usable to increase it's ability to generate liquidity.

Monero's privacy is a major feature, but it's insufficient in utility for it to mainly generate liquidity from being a mixer for other crypto.

To manage that if we could get automatic swaps for XMR<->FIAT with management to do that within ~5 sec and software to be able to use e.g. a phone that emulates VISA/Mastercard to be able to use NFC for in-person payments so that it can be a direct replacement for FIAT credit cards.

# Discussion History
## XMRfamily | 2024-05-23T19:41:44+00:00
Your project doesn't really make sense to me how atomic swaps help fiat -xmr

## Kreyren | 2024-05-23T20:06:54+00:00
> Your project doesn't really make sense to me how atomic swaps help fiat -xmr -- @XMRfamily (https://github.com/monero-project/meta/issues/1010#issuecomment-2127897826)

For example in my personal experience using monero in the central EU the main problem is that it's very difficult to get monero and use it.. Basically the options rn are to buy a BTC at the ATM for 5~15% fee and then exchange from BTC to XMR for another fee which can easily eat 30% of the XMR in FIAT value. 

So having the swaps (including for FIAT) integrated in the GUI wallet by spec would manage the risk of overpaying for the fee and made this way easier for general adoption + more XMR ATMs would manage the BTC's scam fees as it doesn't seem to be practically possible to just go to the FIAT ATM with a monero wallet and withdraw money from it.

If we could implement the XMR<->FIAT in a way that takes few seconds that would also enable the e.g. phone's NFC used for in-person checkouts to enable getting rid of the FIAT bank for practical use.



# Action History
- Created by: Kreyren | 2024-05-19T01:58:54+00:00
