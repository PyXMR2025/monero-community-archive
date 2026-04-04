---
title: Something like bitcoin's nLockTime
source_url: https://github.com/monero-project/monero/issues/1184
author: ChristopherKing42
assignees: []
labels: []
created_at: '2016-10-05T18:40:01+00:00'
updated_at: '2019-09-16T08:14:29+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Currently Monero has [a feature](https://getmonero.org/knowledge-base/moneropedia/unlocktime) by which you can publish a transaction to the block chain, and the funds become locked. This is similar to bitcoin's nLockTime, but it has some important differences.

Namely, if I sign a transaction with nLockTime, the funds can still be spent if another transaction is signed before the transaction becomes unlocked.

This has some important consequences. nLockTime is what is required for payment channels, in particular. How a unidirectional payment channel works is that Alice and Bob open a 2 of 2 multisig wallet, and set up an nLockTime transaction to send the funds back to Alice after, say, a week (this escape transaction is signed before Alice signs the transaction sending Monero to the multisig wallet). Then to send funds, you sign a transaction from Alice to Bob. Bob can accept the funds before a block is mined, since he knows Alice can't double spend the funds (since she would need his signature). They also update Alice's escape transaction each time. This transaction is necessary so that if Bob disappears, Alice can get her Monero back.

nLockTime also allows for agents to trustlessly buy and sell information. For example, a security researcher could sell a security exploit to a company, anonymously, and with no chance of either party defrauding each other.

It works similarly to [this](https://bitcoincore.org/en/2016/02/26/zero-knowledge-contingent-payments-announcement/). Again, Alice and Bob set up a multisig wallet. Bob set ups a transaction spending from him to the multisig wallet and an escape transcation (with nLockTime) sending from the multisig wallet to himself. Alice and Bob sign the escape transaction, and then Bob signs and publishes the transaction putting funds into the multisig wallet. Then Alice creates a transaction sending from the multisig wallet to herself (call it T). Let Z=H(T). She uses K=H(0|T) to encrypt the information P, resulting in cipher-text C. She then sends Bob Z, K, and P, and a proof that there is a T' (which turns out to be T) such that Z=H(T'), K=H(0|T'), C decrypted with K is the information that Bob is seeking. Bob signs T ([he only need to know Z to do this](http://monero.stackexchange.com/questions/1583/when-you-sign-a-monero-transaction-are-you-signing-a-hash)). Alice then also signs it, and publishes it to the blockchain. Bob then calculates K=H(0|T), and decrypts the cipher text C to get P, which according to the proof Alice made will satisfy the conditions set forth by Bob.

This means, for example, that pay to hash won't be necessary to implement, since Bob could pay Alice for X such that Y = H(X).

It is technically possible to implement nLockTime now (without protocol change), but it is a little clunky. You have to put a negligible amount of Monero in a time lock transaction, and then sign a transaction spending it and the funds you want to nLockTime. This won't be publishable until the other transaction is unlocked, but it is a little clunky, requiring a couple of transactions (and data must be published to the blockchain).

Implementing this at the protocol level would be simple, on the other hand (although I do suggest naming it something better. Maybe call the current feature "unlock_time", and the new feature "publishable_time").


# Discussion History
## iamsmooth | 2016-10-06T05:15:19+00:00
I'm not a huge fan of the nLockTime concept in general. The existence of the feature implies a commitment to support old signed transactions and transaction formats forever, the existence and structure of which can't be known. The means no transaction format or feature, whether ever used or not, can ever be changed or removed. Locking on outputs implies only continuing to support outputs that exist on the blockchain, which is a much narrower requirement.

Some sort of restricted version with a maximum time interval between the outputs being spent and the publishable time would probably be sufficient for most conceptions of payment channels but avoid the implied indeterminate commitment. I have not worked out the details of this.


## ChristopherKing42 | 2016-10-06T05:20:18+00:00
I don't think you need to go that far. nLockTime contracts are usually only
for short amounts of time. Disallowing transactions that are out of date
should be fine for most applications, as long as you make it apparent in
the documentation.

On Thu, Oct 6, 2016, 1:15 AM iamsmooth notifications@github.com wrote:

> I'm not a huge fan of the nLockTime concept in general. The existence of
> the feature implies a commitment to support old signed transactions and
> transaction formats forever, the existence and structure of which can't be
> known. The means no transaction format or feature, whether ever used or
> not, can ever be changed or removed. Locking on outputs implies only
> continuing to support outputs that exist on the blockchain, which is a much
> narrower requirement.
> 
> —
> You are receiving this because you authored the thread.
> Reply to this email directly, view it on GitHub
> https://github.com/monero-project/monero/issues/1184#issuecomment-251868977,
> or mute the thread
> https://github.com/notifications/unsubscribe-auth/AIVoEpyf5i-NGfHDSh1LPl8gtQ8c0FAWks5qxIPrgaJpZM4KPJWw
> .


## iamsmooth | 2016-10-06T06:56:04+00:00
@ChristopherKing42 I edited the comment after the email you got adding something similar to what you suggested, so we agree on that.


## CameronRuggles | 2018-08-26T21:10:50+00:00
https://github.com/monero-project/monero/issues/3139#issuecomment-362108451

In the comment I linked, it says: "If they [monero] upgraded their ring-input to be a bulletproof or-gate thing, then they could also impose a CSV style timelock in it."

Considering that we'll be getting bulletproofs soon, will this mean that we can have a CSV style timelock fairly soon, and use that for atomic swaps, an a lightning network? Or does our current bulletproof scheme not allow for this and it is still an opened ended issue on how to implement atomic swaps and LN?



## lacksfish | 2019-09-16T08:14:29+00:00
CSV would mean locking funds to a certain output, with no way of spending them for the locked time period. On the other hand, nLockTime (on Bitcoin) allows for a low sequence number to be set on the input - so that the funds could be re-spent elsewhere before the locktime is reached.

# Action History
- Created by: ChristopherKing42 | 2016-10-05T18:40:01+00:00
