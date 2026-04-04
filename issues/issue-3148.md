---
title: 'Proposal: Add way to (automatically?) split unspent transactions (UTXOs)'
source_url: https://github.com/monero-project/monero/issues/3148
author: Sheastesx
assignees: []
labels: []
created_at: '2018-01-17T15:28:29+00:00'
updated_at: '2018-10-12T20:32:59+00:00'
type: issue
status: closed
closed_at: '2018-10-12T20:32:59+00:00'
---

# Original Description
As I [didn't get any constructive comments on Reddit](https://www.reddit.com/r/Monero/comments/7qepqi/proposal_add_way_to_automatically_split_utxos/) I'm going to open this on Github so it doesn't get lost.

-----

As can be seen in [this discussion](https://monero.stackexchange.com/questions/7283/will-we-eventually-get-rid-of-locked-and-unlocked-balances) it would be nice to have a way to (maybe automatically) split large UTXOs to (a configurable) amount of smaller outputs. This would not only improve anonymity (?) but also [avoid having to wait for the wallet balance to unlock again](https://monero.stackexchange.com/questions/7283/will-we-eventually-get-rid-of-locked-and-unlocked-balances).

# Discussion History
## moneromooo-monero | 2018-01-17T15:30:19+00:00
Why would it improve anonymity ?


## Sheastesx | 2018-01-17T15:41:30+00:00
I imagine it to be similar to [churning, ie, sending your balance back to yourself](https://www.reddit.com/r/Monero/comments/6rvmj9/what_qualifies_as_a_churn/dl8j0jd/).

It could be implemented as follows. A new config option is added which once enabled will automatically create more change outputs than required. If you have 10 xmr and send 2 xmr to Alice, the remaining 8 xmr are not send back to a single of your addresses as a whole but rather are split to multiple outputs and are send to multiple of your (sub?) addresses. The only downside to this will be an increased transaction fee (because the transaction will be larger). This will be only half as bad with the advent of various techniques such as [Bulletproofs](https://getmonero.org/2017/12/07/Monero-Compatible-Bulletproofs.html).

## moneromooo-monero | 2018-01-17T16:28:04+00:00
How is it different from sending yourself multiple outputs ? Just that it's automated ?

## Sheastesx | 2018-01-17T16:42:11+00:00
Correct, imo if it's not done automatically (even if it opt-in), no one does it because you'll forget to do it. Settings could be labeled with "I want to be able to create more than one transaction per 20 minutes from time to time. This option ensures that at least x (eg, 2) transactions can be made every 20 minutes". It should be simply as real money, I want to spend my xmr without having to think about my wallet structure, __it should just work__.

## dEBRUYNE-1 | 2018-01-17T17:07:18+00:00
>This would not only improve anonymity (?)

It doesn't. If you ever have to recombine those outputs (as inputs) it'll show that they came from the same block (and even transaction) and it'll significantly increase the probability of the input being the real one. 

## moneromooo-monero | 2018-10-12T20:26:41+00:00
The sweep_\* commands now have an optional "outputs=N" setting to control how to split an output.

## moneromooo-monero | 2018-10-12T20:26:45+00:00
+resolved

# Action History
- Created by: Sheastesx | 2018-01-17T15:28:29+00:00
- Closed at: 2018-10-12T20:32:59+00:00
