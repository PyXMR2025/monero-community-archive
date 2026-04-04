---
title: Spend balance before unlock
source_url: https://github.com/monero-project/monero/issues/8961
author: nnzo
assignees: []
labels: []
created_at: '2023-07-28T14:17:52+00:00'
updated_at: '2023-08-03T15:47:47+00:00'
type: issue
status: closed
closed_at: '2023-08-03T15:47:47+00:00'
---

# Original Description
I understand that the the 10-confirmation wait for coins to become spendable is a wallet restriction, not a protocol one.

I have some questions that would help me understand this better:
1. How would I send 'unconfirmed' incoming coins through the CLI?
2. Is the `unlock_time` in the `transfer` command changing anything for the external receiver or is it just modifying the 10-confirmation limit for the 'change' coins on the local node?

Thanks in advance for the help :)

# Discussion History
## selsta | 2023-07-28T14:19:01+00:00
> I understand that the the 10-confirmation wait for coins to become spendable is a wallet restriction, not a protocol one.

It's a protocol restriction.

## nnzo | 2023-07-28T15:14:15+00:00
@selsta 

> > I understand that the the 10-confirmation wait for coins to become spendable is a wallet restriction, not a protocol one.
> 
> It's a protocol restriction.

Oh. There is a comment on this Monero StackExchange accepted answer saying the opposite. I suppose it's outdated?

https://monero.stackexchange.com/questions/3262/whats-the-difference-between-balance-and-unlocked-balance

## selsta | 2023-07-28T15:18:09+00:00
Yes, it got changed during one point at a network upgrade.

## nnzo | 2023-07-30T12:24:50+00:00
@selsta 
Ahh, I understand. Is there any way to ignore the spend restriction and queue transactions?
Also, when sending coins to an external address, would it be a good idea to split up all the change coins into different addresses so I don't have to wait the 20 minutes every time? Is there a better way to achieve this?

Say I had a balance of 100 XMR (on one address), and I transferred out 25, that would mean that I would have to wait 20 minuets to be able to use the other 75. Maybe it would be a better idea to have 75 change addresses and send each one of them 1 XMR of 'change', so on the next external transaction also sending 25 XMR I would use up 25 addresses with 1 XMR each and I wouldn't have to wait for the other XMR to become available.

## Wolf54 | 2023-07-30T13:33:13+00:00
@nnzo 
Since this is protocol restriction, I don't think you can go around it at all.

The solution you described has been implemented in a similar way in the ( [Monerujo wallet](https://www.monerujo.io/index.html#about) ). This wallet allows you to generate 10 coins of a given value from your wallet balance which you can spend in rapid succession without waiting the 20 minutes from the first spend.

## selsta | 2023-07-30T13:58:28+00:00
I would recommend this blog post: https://anhdres.medium.com/monerujos-pocketchange-what-it-is-and-how-it-works-8e1ea1f7489e

## nnzo | 2023-07-31T04:41:46+00:00
Thanks @selsta and @Wolf54 this is very helpful information!

My last questions before I get out of your hair are; what is the max amount of change addresses I can provide? Whats the maximum amount of inputs?
Is this stackexchange answer accurate? https://monero.stackexchange.com/questions/11080/how-many-destinations-can-there-be-for-a-single-transaction

> No actual limit, but if the transaction weight exceeds half of the total block weight it will be rejected

Outdated?

> Since bulletproofs, there is also a maximum of 16 outputs per transaction.

Is this enforced in every transaction after the bulletproof update? Or is it optional to construct a bulletproof transaction?

If I did want to split up 100 XMR into lots of 0.1 XMR 'pockets' I would have to send around 62 transactions.

I did find a reddit post from about 4 years ago with comments saying that there is no input limit apart from the transaction weight exceeding half the block size (https://www.reddit.com/r/Monero/comments/e0ypn9/whats_the_maximum_number_of_inputs_and_outputs/)
Does this still apply?

## selsta | 2023-08-01T21:21:08+00:00
What you linked is correct, there is no limit on inputs and a max of 16 outputs per transaction.

> If I did want to split up 100 XMR into lots of 0.1 XMR 'pockets' I would have to send around 62 transactions.

Seems correct.

# Action History
- Created by: nnzo | 2023-07-28T14:17:52+00:00
- Closed at: 2023-08-03T15:47:47+00:00
