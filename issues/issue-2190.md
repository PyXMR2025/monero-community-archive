---
title: I can’t receive moneros I’ve sent to my XMR address on Eobot
source_url: https://github.com/monero-project/monero/issues/2190
author: Ignipso
assignees: []
labels:
- invalid
created_at: '2017-07-22T15:56:33+00:00'
updated_at: '2017-08-08T10:42:13+00:00'
type: issue
status: closed
closed_at: '2017-08-08T10:42:13+00:00'
---

# Original Description
I can’t receive moneros I’ve sent to my XMR address on Eobot, hash of transfer:

7172f32f16423bfac5b01eb99158f76b65e35aea1de3b79682f1c505071c8c12

Eobot wrote on my request: «XMR is required to have a "Payment ID" attached when sending coins, otherwise it wont arrive. It's an anonymous coin and we can't track who sent the coins without the payment ID, and some exchanges/websites might not support it, so you need to contact them and ask them to support it».

The problem is, I didn't use payment ID. But probably it’s possible to do something with it…

Then I asked some person from Monero team from their official site — and there was an answer: «The funds were cleared by the Monero network a while back (block 1356806)
https://moneroblocks.info/search/7172f32f16423bfac5b01eb99158f76b65e35aea1de3b79682f1c505071c8c12
so you need to contact the recipient of the funds. If the funds were sent to Eobot or some other Exchange, Wallet Provider, etc., you need to contact their support. One must keep in mind that most Exchanges and Wallet providers will use a common XMR address and assign one or more payment IDs to each account in order to properly credit each account. As a consequence of this, if the payment ID they gave you is not used, it may not be straightforward for them to credit your account with the funds, even though they have the funds somewhere in their system. If the funds were sent to a wallet under your control then it is a matter of setting up the wallet and synchronizing it with the network».

And finally I’m asking somebody of you to help me with advise what to do now — if it is possible to solve my problem. The sum of XMR was probably not so much to mention, but it is not good for me anyway.

# Discussion History
## moneromooo-monero | 2017-07-22T17:51:33+00:00
This is not a bug. If you don't tell the recipient who the monero is from, they won't know.
You can prove you paid someone though, see get_tx_key and check_tx_key. You can give the recipient the tx key you used for a tx, and they can check it matches. There are details for how to do this on monero.stackexchange.com.

## Ignipso | 2017-07-22T21:26:17+00:00
Thank you!

## moneromooo-monero | 2017-08-07T18:15:15+00:00
+invalid

## moneromooo-monero | 2017-08-08T10:40:34+00:00
+resolved

# Action History
- Created by: Ignipso | 2017-07-22T15:56:33+00:00
- Closed at: 2017-08-08T10:42:13+00:00
