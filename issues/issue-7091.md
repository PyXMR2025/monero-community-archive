---
title: Add support for integrated subaddress to monero CLI wallet.
source_url: https://github.com/monero-project/monero/issues/7091
author: crocket
assignees: []
labels: []
created_at: '2020-12-07T11:39:54+00:00'
updated_at: '2021-10-06T02:51:56+00:00'
type: issue
status: closed
closed_at: '2021-10-06T02:51:55+00:00'
---

# Original Description
https://monerodocs.org/public-address/integrated-address/ mentions an integrated address consists of public view key, public spend key, and payment ID.

For now, it seems that integrated addresses are generated only for standard address.

A subaddresses also has public view key and public spend key. An integrated subaddress helps a person assign a subaddress to each business.

Business 1 generates integrated addresses off subaddress 1.
Business 2 generates integrated addresses off subaddress 2.

If each business that I own generates multiple integrated addresses on top of its unique subaddress, tracking companies can't easily link my separate businesses together by just comparing payment addresses. Integrated subaddresses also help avoid computational cost of using subaddresses.

# Discussion History
## moneromooo-monero | 2020-12-07T15:30:33+00:00
It was decided to not do so. Use an account per business, and subaddresses off those accounts.

## crocket | 2020-12-07T22:37:35+00:00
Why was it decided not to do so? https://monerodocs.org/public-address/integrated-address/ still mentions computational cost of using subaddresses. A large e-commerce website may want to avoid using multiple subaddresses that are computationally expensive. Think about walmart and amazon and large cryptocurrency exchanges.

Integrated standard addresses are not useful for people who have more than one business or do mining apart from business.
Using standard address for multiple purposes or multiple identities is no good for privacy.

## moneromooo-monero | 2020-12-07T23:31:19+00:00
I don't remember all maybe, but at least because it would keep the confusion between the full integrated address and the the split address + payment id. Subaddresses don't have much computational cost, assuming you don't use massive amounts of them.

## crocket | 2020-12-08T06:21:49+00:00
> split address

What is this? I never heard.

## moneromooo-monero | 2020-12-08T13:17:13+00:00
An integrated address is your standard address and the payment id stuck together along with some glue, so it looks different when displayed as integrated or displayed separately. This is a continuous source of confusion.

## crocket | 2020-12-08T13:26:22+00:00
It was confusing because the documentation didn't define split address. And, I understood split address intuitively. I just didn't know the name for it.

The UI can make it look obvious.

Base address // xxxxx
Payment ID // xxxx
Base address + Payment ID = Integrated address // xxx

Or, you can show the following tree structure as an advanced viewing option.

Integrated address
|--- Base address
|--- Payment ID

It's quite a simple concept. But, people don't need to see the components of an integrated address by default.

Regular consumers don't even need to know what integrated addresses are in order to send monero to them.

## knaccc | 2020-12-10T02:54:04+00:00
> computational cost of using subaddresses

The computational cost is that a modern CPU can "only" generate thousands of subaddresses per second. What kind of business is exceeding thousands of transactions per second, yet can't afford to run their business on more than one CPU?

Subaddress generation can be GPU accelerated 50x+ if there really is demand and the will to do so.

I've yet to hear a compelling argument that using a library to generate multiple subaddresses (grouping them by account) is significantly more effort than using a library to generate multiple integrated addresses (grouping them by subaddress).

You may need to store the subaddresses you've issued against each customer in a database (instead of just re-using an existing customer ID as the payment ID), but with any payment integration, you're also storing metadata notified to you by that payment integration in your own database.

## crocket | 2020-12-10T03:14:49+00:00
There are also administrative and coding costs of using subaddresses.
It's also cheaper to scan a subaddress than thousands of subaddresses when you need to sync a wallet again.

## selsta | 2020-12-10T03:17:56+00:00
> It's also cheaper to scan a subaddress than thousands of subaddresses when you need to sync a wallet again.

That’s not the case. Subaddresses use a lookup table, there is no speed difference in scanning.

## knaccc | 2020-12-10T03:49:45+00:00
@crocket In case you aren't aware - you don't have to do RPC with a wallet in order to generate subaddresses. You can generate them locally with a library, just like you probably already use a library to generate integrated addresses.

Here are Java and Javascript libraries for generating subaddresses, and more are available for other languages:

https://github.com/knaccc/subaddress-java
https://github.com/knaccc/subaddress-js

## crocket | 2020-12-10T04:07:48+00:00
The fact that subaddress generation requires a private view key isn't ideal.
Bitcoin can derive subaddresses with an extended public key.

There could be wide gaps between subaddresses. Is it okay for there to be huge gaps between subaddresses?
As far as I know, monero wallet may fail to scan past huge gaps. I may be confusing monero with bitcoin.

## knaccc | 2020-12-10T05:12:46+00:00
> There could be wide gaps between subaddresses. Is it okay for there to be huge gaps between subaddresses?

If the gap is more than 200, you need to set a flag on your wallet to "look ahead" more than 200 addresses at a time. You'd want to try and be sequential with your use though, by using a counter to remember the highest subaddress index you've issued so far. 

> The fact that subaddress generation requires a private view key isn't ideal.

I agree it's not ideal. However, if they've compromised the server enough to steal the private view key, they have probably stolen your database credentials too and breached access to much more private information than that.

## crocket | 2020-12-10T06:55:10+00:00
> If the gap is more than 200, you need to set a flag on your wallet to "look ahead" more than 200 addresses at a time. You'd want to try and be sequential with your use though, by using a counter to remember the highest subaddress index you've issued so far.

Administrative and coding and conceptual costs.

> I agree it's not ideal. However, if they've compromised the server enough to steal the private view key, they have probably stolen your database credentials too and breached access to much more private information than that.

Programmers could lose private view keys through mistakes, or they could leak it intentionally against the will of contractors or employers. If merchants didn't want to lose private view key, they better generate 1 million subaddresses within an account and transfer them.

You still want to make sure that there will not be huge gaps between subaddresses.

## knaccc | 2020-12-10T07:21:46+00:00
> Programmers could lose private view keys through mistakes, or they could leak it intentionally 

That is a good point, if you were using a library that did not communicate with a wallet instance. However, if you were listening for incoming payment notifications from a wallet instance, then a wallet instance would be available to ask via RPC to generate subaddresses for you. Then, the private view key would not be visible to the programmer.

> Administrative and coding and conceptual costs

Note that if you were to issue different bitcoin addresses in the same way as you'd issue different subaddresses, the implementation approach and effort would be similar. This does not diminish the fact that integrated addresses would be simpler.

It's certainly not the case that integrated addresses offer no advantages vs generating subaddresses. But we need subaddresses to provide unlinkability, and so the question is whether we are making things too complicated by having integrated addresses in addition to subaddresses. I'm a big fan of simplicity.

## crocket | 2020-12-10T14:04:13+00:00
> But we need subaddresses to provide unlinkability, and so the question is whether we are making things too complicated by having integrated addresses in addition to subaddresses. I'm a big fan of simplicity.

Integrated subaddresses make things simpler for people who own multiple businesses. And, since a business maintains a sustained identity, it doesn't benefit much from using multiple subaddresses.

I don't think integrated subaddresses are too complicated. It's simple enough....
After I read BIP-32, BIP-39, BIP-84, and so on, I know it's simple.

Monero is simple because it is private and doesn't need ugly bitcoin hacks to improve privacy.

I like subaddresses and integrated addresses.

## knaccc | 2020-12-10T16:00:39+00:00
> Integrated subaddresses make things simpler

I strongly disagree that when a developer starts looking at the documentation, it is simpler that they will be be offered the choice of subaddresses vs integrated addresses vs integrated subaddresses. It's obviously much simpler for them to understand what to do next if they are just told to issue subaddresses.

## selsta | 2020-12-10T16:01:47+00:00
Integrated addresses have resulted in a lot of support requests by users, subaddresses are easier to understand for the end user.

## crocket | 2020-12-11T07:12:06+00:00
Why do end users need to understand integrated addresses when they send or receive monero?
They don't need to know anything about integrated addresses to send monero to them.

Support requests don't have to be served by developers. They can be served by videos and articles.
Better documentation pays dividends over time because documentation teaches people while developers sleep.

Monero is still conceptually far simpler than bitcoin. I don't know where you are coming from.
Perhaps, we should provide encrypted data fields in each transaction?
If there is no integrated subaddress, it might be easier to just attach payment ID again.

## crocket | 2020-12-11T11:22:51+00:00
> I strongly disagree that when a developer starts looking at the documentation, it is simpler that they will be be offered the choice of subaddresses vs integrated addresses vs integrated subaddresses. It's obviously much simpler for them to understand what to do next if they are just told to issue subaddresses.

I'm not even a good developer, but I understood the concept quickly. I understood it so quickly that I realized there could be integrated subaddresses even before having any amount of XMR. I understood the possibility of integrated subaddresses even before creating my first monero wallet.

You don't have to use integrated addresses. But, if you learn it, a little bit of time you spent on learning it will pay dividends over time because integrated subaddresses make things easier for development and administration. Designing your payment system carefully so that it doesn't create huge gaps is a lot more difficult than understanding integrated subaddresses.

## knaccc | 2020-12-11T18:42:26+00:00
@crocket I can see that if there were a strong argument for integrated (sub)addresses, that we could get the best of both worlds. We'd prevent regular users from being able to create integrated (sub)addresses (by not implementing the ability to create them in the GUI), and only allow integrated (sub)addresses to be created by developers using the CLI or RPC API. People might be confused when they are given integrated addresses that are many characters longer than regular addresses, but a strong argument for integrated addresses could outweigh that confusion.

Unfortunately, I still don't understand what that strong argument is, and why it's a significant burden to add a row to a database for every subaddress issued. There would simply be a table with an auto-increment column for a subaddress index that would correlate to a user/transaction/shopping basket. You're going to need to use a database anyway, so it's not like subaddresses would be the only reason people would need to use a database at all.

Another privacy advantage of dropping integrated addresses that I should have mentioned before:

With integrated addresses, hosted wallets (MyMonero etc) and exchanges that log users' outgoing transactions will be able to observe whether users are paying the same business multiple times. If, instead, a non-integrated subaddress is issued for each transaction, hosted wallets will not have this visibility on repeat transactions to a vendor. 

An exchange could go to a vendor's web site, see what underyling integrated subaddress was being used to receive payments, and then easily find out which of its users were sending funds to that business.

Is it OK that an exchange or hosted wallet provider can easily tell when users are sending funds to certain well-known destination addresses?

Should users be asked to forgive this privacy leak, so that you don't have to implement an auto-increment counter?

## crocket | 2020-12-12T11:03:13+00:00
> With integrated addresses, hosted wallets (MyMonero etc) and exchanges that log users' outgoing transactions will be able to observe whether users are paying the same business multiple times. If, instead, a non-integrated subaddress is issued for each transaction, hosted wallets will not have this visibility on repeat transactions to a vendor.

If you use a hosted wallet or exchange as your payment wallet, you forfeit a lot of privacy benefits of monero. Subaddresses can help a bit if they are not reused. But, nothing prevents merchants from reusing subaddresses. Even if subaddresses are not reused for a long time, we don't know other ways that online wallets can compromise your privacy. I would not leave my money on online wallets for any longer than it is necessary.

In any case, using online wallets as the main wallet is a form of privacy leak for everyone.

> Should users be asked to forgive this privacy leak, so that you don't have to implement an auto-increment counter?

An auto-increment counter can easily create huge gaps for large websites. Ways to prevent huge gaps can be somewhat complex but still possible.

* Do you know any way to easily prevent address gaps without adding more cognitive burden or make them irrelevant?
* Any way to create subaddresses on the fly without unnecessarily exposing view key to networked services? The less interfaces a view key has to deal with, the better.
* What about allowing only secret view key to extract base address and payment ID from integrated address? This would prevent easy ways to compromise privacy. Asymmetrical encryption is the key here. You use public keys to generate integrated address, but you need secret view key to extract components of integrated addresses. I don't know if this is possible, but it seems like a convenient way to not compromise privacy and not have to worry about address gaps.
  * The idea is to use asymmetrical encryption to protect base address as well as payment ID. A private key of any sort can be used here to make it possible with the least amount of coding.
  * Perhaps, considering integrated subaddress as a subaddress of a subaddress is a good analogy to be made here.

## knaccc | 2020-12-12T17:30:35+00:00
> Do you know any way to easily prevent address gaps

It takes a second of compute time for a wallet to add thousands of subaddresses to the look-ahead lookup table. So if you just set the wallet to look ahead by 50,000 subaddresses, there will be a pause for a few seconds while the wallet pre-computes the lookup table. This is a one-time wait - future wallet restarts will not incur a delay. What kind of gaps were you expecting to see?

> Any way to create subaddresses on the fly without unnecessarily exposing view key to networked services?

Only with the private view key. Also though, how are you going to check for incoming payments, if your service has no connectivity to your wallet instance? You're going to want to immediately confirm to a user when a payment is received, so they aren't anxious that their payment failed to be recognized by your system somehow.

> What about allowing only secret view key to extract base address and payment ID from integrated address?

That's what a subaddress achieves :) Subaddresses were quite challenging to devise. If there were a way of issuing them without needing to create a lookup table, we'd have done it that way.

## crocket | 2020-12-12T23:36:03+00:00
> That's what a subaddress achieves :) Subaddresses were quite challenging to devise. If there were a way of issuing them without needing to create a lookup table, we'd have done it that way.

Subaddresses have two drawbacks.

1. Secret view key is required to generate them
2. Address gaps have to be accounted for. If you migrate, it can be frustrating.

* Use one-time public key to encrypt base addresses in integrated addresses, and use secret view key to decrypt them?
* How about using payment ID to encrypt base address? Since payment ID itself is encrypted inside integrated address, integrated addresses would look opaque to third parties. Integrated subaddress would be like a subaddress of a subaddress without the drawbacks of subaddress. Hashing is irreversible, but encryption is reversible.

## knaccc | 2020-12-13T02:13:56+00:00
> Address gaps have to be accounted for. If you migrate, it can be frustrating.

I'm struggling to understand what kind of migration you might be imagining. You mean if you threw away your database that correlated the subaddress indices you'd issued to customers/shopping baskets/transactions etc? Why would you do that? If you did that and wanted to keep using the same wallet, you could just use a different account in that wallet and start from scratch.

I'm not sure what you mean by "account for address gaps". All you need is a counter that you increment by one every time you issue a subaddress. That's it. If you issue subaddresses that funds never get sent to, that's OK as long as that doesn't happen more than 50,000 times in a row (or whatever you set the lookahead value to).

Re: your suggestions: the cornerstone of the subaddress scheme is that it is vital that the same private view key is used for ECDH on the transaction public key, regardless of the subaddress issued. This is what keeps scanning time constant and prevents scanning time from increasing linearly with the number of subaddresses issued. After examining the subaddress scheme math, if you think you have an idea that preserves the constant scanning time property of subaddresses, it would be interesting to hear. I don't see how any of your suggestions would be compatible with that scanning time constraint.

## crocket | 2020-12-13T04:43:50+00:00
> I don't see how any of your suggestions would be compatible with that scanning time constraint.

It's not a suggestion about blockchain. It could be a wallet-level feature or a node-level feature.
Address encryption can be unwrapped by wallet or node.
As far as I know, multi-sig is also a wallet-level feature.

Blockchain records one-time public key anyway as a stealth address. Why can't we have stealth address for payment as well?

Why can't you allow only secret view key or some sort of encryption key to unwrap integrated address?

I will look into how Pirate Chain tackles address privacy.

> I'm not sure what you mean by "account for address gaps".

There can be algorithms that guarantee there is little or no gap between subaddresses.
Auto-increment counter is not such an algorithm.
My aesthetic sense doesn't like gaps that can make it seem that a wallet lost track of money.

If you compress gaps between subaddresses and reduce the number of subaddresses used, you can reduce scanning time in the long term. If a large website ends up tracking billions or trillions of subaddresses in the future, a wallet may slow down or require a lot of RAM.

If a business or a customer understands the privacy risk, integrated subaddresses can be fine.

> I'm struggling to understand what kind of migration you might be imagining.

You migrate your seed to a new wallet program.

## crocket | 2020-12-13T05:12:23+00:00
Possible solutions

* Make address gaps totally irrelevant whatsoever
* Apply address compression before creating a stealth address for monero blockchain.
  * Billions of subaddresses may be represented by an account address on the blockchain?
* Apply address encryption over integrated subaddresses as a wallet-level or a node-level feature.

## knaccc | 2020-12-13T05:31:42+00:00
> you can reduce scanning time in the long term
> a wallet may slow down or require a lot of RAM

The lookup table requires 32 bytes of storage for every subaddress issued. However, if people were using huge numbers of subaddresses, this would be optimized so that you'd only store the first few bytes of each subaddress in RAM, and only go out to disk on the very rare (1 in 65536 chance per output scanned) occasion that there is a match on those first few bytes. So you'd really only need to dedicate 2GB of RAM to the billion-subaddress lookup table.

The harder part is that the lookup table with a billion subaddresses would take approx. 100 hours to generate, or 2hrs if it were GPU accelerated. This would be a one-time cost, and would be built up in small increments over long periods of time. It would not need to be re-computed if the wallet were restarted. 

A wallet scanning for incoming transactions to a billion subaddresses would require about the same scanning time as if it were scanning for only a single subaddress. 

If you restored your wallet from scratch, you'd need to build the entire table up all at once. So if you really did issue a billion subaddresses, you'd have to A) Wait 100 hours or B) GPU accelerate it or C) Rent an AWS cluster for half an hour

> There can be algorithms that guarantee there is little or no gap between subaddresses

How would you do this? Perhaps you mean that if you issue a subaddress to someone for payment, and they don't use it, then you could re-use it after a period of waiting. I'd advise against that though.

> Apply address encryption over integrated subaddresses as a wallet-level or a node-level feature

Unless you explain exactly how your ideas can work without increasing the scanning time linearly with the number of issued integrated subaddresses, your ideas do not meet the basic criterion necessary to provide a workable solution.

## crocket | 2020-12-13T09:19:19+00:00
> Unless you explain exactly how your ideas can work without increasing the scanning time linearly with the number of issued integrated subaddresses, your ideas do not meet the basic criterion necessary to provide a workable solution.

You don't pre-generate a list of integrated subaddresses. You generate integrated subaddresses on the fly. You don't scan integrated subaddresses on blockchain, either.

> Payment ID in a transaction will be encrypted with a shared secret (one-time random key known only to sender and recipient).

Why can't you use one-time random key to also encrypt base address in an integrated address?
Perhaps, can your personal node decrypt encrypted integrated addresses? If the node has one-time random key, the node can decrypt the address. Think of it as a node-level feature. It doesn't exist on blockchain.

Once monerod decrypts an encrypted integrated address, it discards the one-time random key. You can also keep reusing one pair of asymmetric encryption keys instead of one-time random key in order to reduce burden on nodes. Or, you can change the single encryption key every hour in your personal node in order to not have to try to decrypt an encrypted address with a hundred one-time encryption keys for one hundred pending transactions if you are a large website. Or, your node may maintain a list of encrypted addresses to catch in order to not try to decrypt random encrypted addresses. You utilize a cheap way to catch encrypted integrated addresses with your node.

Only your personal node knows the encrypted address is destined to arrive your wallet.

You get the idea now.

> How would you do this? Perhaps you mean that if you issue a subaddress to someone for payment, and they don't use it, then you could re-use it after a period of waiting. I'd advise against that though.

If a pending payment is canceled, the subaddress used is reserved in a database for later reuse because it was never actually used.
A subaddress is marked used only after it receives one payment.
You don't have to be a genius programmer to make this work, but it can be complex if you are not an experienced programmer.

## knaccc | 2020-12-13T18:25:58+00:00
> If a pending payment is canceled, the subaddress used is reserved in a database for later reuse

This isn't good for privacy, because an exchange can go and create a bunch of shopping baskets and fail to pay, and then note down the subaddresses that the vendor asked for payment to. This would allow the exchange to then see if any of its customers make payment to any of those re-used subaddresses.

I recommend you learn more about the math behind how transactions to subaddresses are constructed so that you can make some more specific and fully explained suggestions. I can't make sense of anything you've suggested.

## crocket | 2020-12-14T01:49:47+00:00
> I recommend you learn more about the math behind how transactions to subaddresses are constructed so that you can make some more specific and fully explained suggestions. I can't make sense of anything you've suggested.

Are you too tired? The concepts I suggested are not difficult to grasp. Try to understand my suggestions after taking a morning shower.

Here's a simple suggestion for one-time address.

You create one-time address for a specific (sub)address or an integrated (sub)address and store the mapping of the one-time address to the actual address in the in-memory look-up table of your full monero node. If someone tries to send monero to your one-time address, nodes look up the address in their own in-memory look-up table. If they can't find it in their look-up table, they pass it to other nodes until your node catches it. Once your node catches it, you remove the one-time address in the temporary look-up table and initiate the transaction with the actual address.

Another suggestion is encrypted integrated address.

You encrypt integrated address and let a customer advertise a transaction with the encrypted integrated (sub)address.
Full nodes try to decrypt the encrypted address with their own encryption keys. If they fail, they pass it to other nodes until your node catches it. If your node decrypts the integrated address, it extracts base address and payment ID and announces a transaction. The encryption key may be re-used for ever or swapped out for another key on a regular basis.

It's a node-level feature. There is some way for a node to check whether it's meant to consume an address passed around by other nodes. I don't know whether this can be implemented as a wallet-level feature.

## knaccc | 2020-12-14T02:20:45+00:00
> If someone tries to send monero to your one-time address

Once you take the time to understand how transactions are created, you'll realize that one-time addresses need to be created by the sender and not the recipient.

If you throw away the normal transaction creation process and just directly write into the transaction a one-time address specified by the recipient, then multiple transactions to the same one-time address will be linkable on the blockchain.

> You encrypt integrated address and let a customer advertise a transaction with the encrypted integrated (sub)address

Encrypt how? If you literally mean just encrypt it using ordinary symmetric or asymmetric encryption, then how does the sender create sensical transactions?

You fundamentally don't understand how transactions are created, which is why your suggestions are nonsensical.

I'm always interested to hear your ideas, but please take the time to learn how the existing Monero transaction creation mechanism works first.


## crocket | 2020-12-14T08:12:47+00:00
> If you throw away the normal transaction creation process and just directly write into the transaction a one-time address specified by the recipient, then multiple transactions to the same one-time address will be linkable on the blockchain.

As I wrote, I'm just a monero beginner. I don't yet know how monero crafts transactions. Where do I start if I want to learn some technical details of transaction?

## jonathancross | 2020-12-14T13:37:29+00:00
> As I wrote, I'm just a monero beginner. I don't yet know how monero crafts transactions. Where do I start if I want to learn some technical details of transaction?

https://web.getmonero.org/library/Zero-to-Monero-2-0-0.pdf

## selsta | 2021-10-06T02:51:55+00:00
Closing as this won't get implemented.

# Action History
- Created by: crocket | 2020-12-07T11:39:54+00:00
- Closed at: 2021-10-06T02:51:55+00:00
