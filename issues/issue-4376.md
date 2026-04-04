---
title: Select the default send address.
source_url: https://github.com/monero-project/monero-gui/issues/4376
author: Uberi-puzo
assignees: []
labels: []
created_at: '2024-11-15T14:50:16+00:00'
updated_at: '2024-11-20T06:42:50+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Situation:

With a bank card, I buy monero at Address1. I have already bought monero from this card and this Address many times, they are already connected.

In some Service, I pay with Address1 (by default, there is no choice), but the money does not reach the Service.

I contact Service support and they ask me for the Transaction Secret Key and the Address from which the payment was made to verify the transaction.

But if I tell them the Address, then I will reveal my Address1, and I will reveal from which card I bought monero, and I will reveal my identity.

I can create Address2.

Address1 and Address2 have a common balance.

I cannot set Address2 as the default for payments. Please add this option.

# Discussion History
## plowsof | 2024-11-15T17:29:05+00:00
Please confirm:

The service has asked you to prove that you sent payment to >their< address because they have not received it?

You are worried that proving this 1 transaction will reveal more details  outside of just this one transaction? 

In my unqualified opinion: (wait for confirmation please) There are only one time use stealth addresses on the Monero blockchain. the details revealed to prove payment of one transaction only reveal information specifically relating to that transaction. 

## Uberi-puzo | 2024-11-17T18:12:24+00:00
At the moment I see:

I received the funds at Address1, then transferred them to Address2 (subaddress).

Then, the payment was made from Address2, the next payment for it from Address1. It looks like the wallet itself chose from which address to send, and sent from Address2.

Then another incoming transaction to Address2, and the next outgoing again from Address2. Then again with Address1.

Then, for some reason, the transaction was executed from Address2, although before that, right before that, there was no incoming transaction on Address2.

## Uberi-puzo | 2024-11-17T19:04:17+00:00
> Please confirm:
> 
> The service has asked you to prove that you sent payment to >their< address because they have not received it?
> 
> You are worried that proving this 1 transaction will reveal more details outside of just this one transaction?
> 
> In my unqualified opinion: (wait for confirmation please) There are only one time use stealth addresses on the Monero blockchain. the details revealed to prove payment of one transaction only reveal information specifically relating to that transaction.

Yes, they are asking to confirm what I sent.

They ask me to give the address from which the funds were sent. This is the address to which I always credit my funds from my bank card.

Specifically, this payment is not important to me.

It is important for me to be able to choose from which address or subaddress to pay each time.

## plowsof | 2024-11-17T20:18:26+00:00
So the question: is it possible to prove to a third party that you both:    

    - Own an address (that do not appear on the blockchain anyway), 
    - and funds where specifically sent FROM this address.  

 To me this seems like it would only work for a transparent chain. How are they going to verify that the address you provided sent the funds?

Your other question seems to be about coin/output control - there is no direct link to your receiving address that you gave someone and the blockchain (one time use stealth addresses) . I will let someone qualified to speak on this answer further, but my understanding is, an output/coin does not belong to a receiving address (like it would on e.g. bitcoin)

## Uberi-puzo | 2024-11-18T12:36:02+00:00
> So the question: is it possible to prove to a third party that you both:
> 
> ```
> - Own an address (that do not appear on the blockchain anyway), 
> - and funds where specifically sent FROM this address.  
> ```
> 
> To me this seems like it would only work for a transparent chain. How are they going to verify that the address you provided sent the funds?
> 
> Your other question seems to be about coin/output control - there is no direct link to your receiving address that you gave someone and the blockchain (one time use stealth addresses) . I will let someone qualified to speak on this answer further, but my understanding is, an output/coin does not belong to a receiving address (like it would on e.g. bitcoin)

They ask me:

1 Send Address (my Address1)
2 Transaction Key

I don't know how they can check.

Regarding the disclosure of identity, if you transfer funds from your personal card to Address1 (you buy monero on the exchanger, and give the exchanger Address1), and then make a purchase by paying with Address1 (by default, there is no choice), and tell someone who transferred monero from Address1, this address, then theoretically, you, through the card-exchanger-Address1 connection, revealed your identity.

## Uberi-puzo | 2024-11-18T12:47:10+00:00
I don't know where I can see this Оne time use stealth address? I only see Address1 in the transaction properties.

## Uberi-puzo | 2024-11-18T12:51:07+00:00
If it is possible to check transactions using the sending address and transaction key, then perhaps we need to automatically generate a new subaddress every time we send?

## selsta | 2024-11-18T12:53:52+00:00
> If it is possible to check transactions using the sending address and transaction key, then perhaps we need to automatically generate a new subaddress every time we send?

I feel there is some misunderstanding.

If you go for example to a blockchain explorer with a sample tx you can see under the "Prove sending" tab that you need the tx private key and the recepient address, not the sending address.

https://xmrchain.net/tx/3f34b2add6ed735f1d017501db98c11a965395b34ff36b9ed455d9f7d8d6a5ab

I don't know why they are asking for your "sending address", but that's not something they can verify.

## Uberi-puzo | 2024-11-18T13:41:48+00:00
> > If it is possible to check transactions using the sending address and transaction key, then perhaps we need to automatically generate a new subaddress every time we send?
> 
> I feel there is some misunderstanding.
> 
> If you go for example to a blockchain explorer with a sample tx you can see under the "Prove sending" tab that you need the tx private key and the recepient address, not the sending address.
> 
> https://xmrchain.net/tx/3f34b2add6ed735f1d017501db98c11a965395b34ff36b9ed455d9f7d8d6a5ab
> 
> I don't know why they are asking for your "sending address", but that's not something they can verify.

They may simply not know how to verify transactions.

I checked it myself, and everything is visible there.

## Uberi-puzo | 2024-11-18T13:42:22+00:00
I'll write to them, and close the ticket, if everything works out, a little later.

Thank you all.

# Action History
- Created by: Uberi-puzo | 2024-11-15T14:50:16+00:00
