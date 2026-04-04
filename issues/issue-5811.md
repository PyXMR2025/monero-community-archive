---
title: wallet2 does not fully sync transactions in the pool
source_url: https://github.com/monero-project/monero/issues/5811
author: woodser
assignees: []
labels: []
created_at: '2019-08-14T22:06:59+00:00'
updated_at: '2019-08-19T23:16:59+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
To recreate this issue:

1. Open a wallet with available funds
2. Create a transaction using the wallet but do not relay it
3. Relay the transaction directly to daemon RPC and not through the wallet
3. Sync / refresh the wallet

Now wallet2 `get_unconfirmed_payments()` will report the incoming transfer, but the wallet's balance and unlocked balance are unchanged.  Creating a new transaction with the same request will double spend outputs which are known to be spent in the pool.

Here is a [test](https://github.com/monero-ecosystem/monero-java/blob/3fe667583b6240cebe1235f40dd943b7a4da0a9a/src/test/java/test/TestMoneroWalletCommon.java#L1945) which illustrates the issue.


# Discussion History
## moneromooo-monero | 2019-08-19T15:32:52+00:00
That's why there is a wallet RPC for it. Otherwise it behaves like a normal incoming tx. Those also don't change your balance: they're not mined.

## woodser | 2019-08-19T19:04:20+00:00
@moneromooo-monero Why should unconfirmed funds not be included in the balance?

If we don't count transactions that are not mined in the balance, then we can never accomplish the user experience of having 5 XMR, sending 1, then seeing 4 remaining minus the fee.  This is a significant user experience issue that is worthwhile to resolve if it's feasible without putting the user at risk, IMO.

The only added risk I'm aware of is that the user will misplace trust in a balance which includes unconfirmed funds which are more susceptible to being double spent.  That is true, but:

1) The API already returns unconfirmed transfers which the UI can flag.  The same could be done for the balance, allowing the UI to flag the balance as including unconfirmed funds.  Otherwise, there is a discrepancy between their transaction history and their balance, and the incorrect balance must either be accepted or masked by the application using local data.
2) Even if the transaction confirms, it may still be invalidated by a re-org, so risk and functionality of being invalidated already exists.  Is the added risk of including unconfirmed funds unacceptably higher than single confirmation funds?

IMO the added risk I described is minimal compared to the improved user experience, especially considering that the vast majority of transactions are not double spend attempts.  Therefore, I think it's better to include unconfirmed funds in the balance, exclude them from the unlocked balance as is already done, and let the UI warn the user about low confirmations than to provide an incorrect balance from the Core wallet.

Thoughts?

Related to #5809

## moneromooo-monero | 2019-08-19T23:16:07+00:00
I don't really disagree with your view over what's best/ideal from a user's point of view. A number of things are really aribtrary decisions among plausible ways to do things.

I'm open to someone writing parallel wallet tx scanner, which simplewallet could plug into instead of the existing one. You've already complained about several similar things (especially the tx-to-same-account thing), and I'm scared to break something by changing this when it's not to fix bugs, so if there was such a parallel, opt-in scanner, it could be tested over time, and then possibly made the default once it's shown to be solid. Similar to how there were two tx creation algorithms at one point. Then you can switch the semantics to whatever you think is the best.


## moneromooo-monero | 2019-08-19T23:16:58+00:00
Oh, and put this new scanner in another file than wallet2.cpp :P

# Action History
- Created by: woodser | 2019-08-14T22:06:59+00:00
