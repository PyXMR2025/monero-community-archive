---
title: Error sending funds to self with integrated subaddress
source_url: https://github.com/monero-project/monero/issues/8380
author: woodser
assignees: []
labels: []
created_at: '2022-06-08T13:50:41+00:00'
updated_at: '2022-06-29T06:46:35+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Currently, wallet2 is able to send funds to external wallets using integrated subaddresses (i.e. integrated addresses derived from subaddresses).

However, sending funds to self with an integrated subaddress throws an error. For example:

`Total received by 52LbSHZbYdaFsu2sZAdVaPBfui3XWD9PqPRMB96BrpziKzYNS1SXJRZBohefSJtk2YB3g7tWYhvzrUCj23sJXBn3V5VAUw2: 0.000000000000, expected 0.225000000000`

This issue requests fixing wallet2 so it can send funds to itself with an integrated subaddress.

# Discussion History
## selsta | 2022-06-08T13:53:18+00:00
We don't want to support any integrated subaddresses at all. This was an intentional decision.

At best I'm for adding code that blocks sending to integrated subaddresses in all cases.

## spirobel | 2022-06-08T14:03:48+00:00
so sad. I really need this feature. If anything we should prohibit sending to primary addresses, as they are the thing that is legacy not subaddresses. 

## SChernykh | 2022-06-08T14:24:47+00:00
If you really need this feature, you should really rethink the design of your software. You can generate billions of subaddresses, so you can uniquely identify each payout. Sure you'll have to keep all the auxiliary data like payment ID somewhere externally, but you can use the subaddress as an ID for all this data.

## spirobel | 2022-06-08T14:32:53+00:00
>If you really need this feature, you should really rethink the design of your software. You can generate billions of subaddresses, so you can uniquely identify each payout. Sure you'll have to keep all the auxiliary data like payment ID somewhere externally, but you can use the subaddress as an ID for all this data.

I thought about this for a long time, but this the only clean way to do it. I want users to login to websites by signing a message with a subaddress. 

I think users should create a new subaddress for each "identity". This is the feature I am currently implementing in my browser wallet. But then I got blocked by this. Because I want the backend to be able to create new clubcards (and other products) for users that used a subaddress to login. The thing is this: if this feature is removed I need to define the concept of identity as "a set of subaddresses" instead of one subaddress in the browserwallet. 

I think this is unclean and can lead to a lot of confusion and possible loss of funds.

## SChernykh | 2022-06-08T14:45:06+00:00
>  I want users to login to websites by signing a message with a subaddress.

How is it related to integrated addresses? You only need a private key to sign any message.

## spirobel | 2022-06-08T15:05:24+00:00
>How is it related to integrated addresses?

I wrote a [short article](https://spirobel.substack.com/p/solving-the-web3-privacy-problem) on this topic. Maybe you can give it a read to understand where I am coming from and how this is related. After you login to the website with a subaddress, the backend will be able to create integrated addresses based on the address you provided.
This means you can sell things on the website in a non custodial fashion. 
I made a [tutorial](https://www.youtube.com/watch?v=9fsdWJo2QFs) before on how to sell things online with Monero. It is not easy for normal people to install their own webserver and configure it just to sell things.
There is currently no easy way to sell things in a non custodial way on a server that you dont host yourself. 
That is what I am trying to improve with this effort. 

## CryptoGrampy | 2022-06-08T17:10:27+00:00
> > I want users to login to websites by signing a message with a subaddress.
> 
> How is it related to integrated addresses? You only need a private key to sign any message.

Verifying signatures currently uses the signers primary address- this is how it's implemented in monero gui; i think (could also be wrong here) that Spirobel would like to be able to (create and) verify a signature using a provided subaddress. This allows users to create accounts at various places using different subaddresses and the various websites that hold these accounts can validate identity using subaddress signature verification rather than all of the websites knowing spirobel's primary address for account verification which is terrible for privacy.

## elibroftw | 2022-06-08T17:35:33+00:00
What you can do for a browser wallet is +1 the seed to create new public addresses that can be used to sign in. That was what I came up with when I was thinking about how to sign in with web3 without keeping track of multiple seeds.  I'm not sure if the subaddress verification signing is feasible which is why I came up with this.

## spirobel | 2022-06-08T17:41:56+00:00
>Verifying signatures currently uses the signers primary address- this is how it's implemented in monero gui;

true. this is specific to how monero gui does it. monero-wallet-rpc does not have this limitation for example. You can also sign with subaddresses if you use it. (It is not in the docs, but it is "officially supported". asked in the dev channel and moneromoo told me about it.)
[More context: (others had the same issue as seen in the reddit thread)](https://twitter.com/spirobel/status/1528978285354360832)

>What you can do for a browser wallet is +1 the seed to create new public addresses that can be used to sign in. 

that is a cumbersome and bad solution. People would have to send transactions to themselves to collect all their funds in one spot. That comes with all sorts of bad implications.
It is also unnecessary, because this
>I'm not sure if the subaddress verification signing is feasible which is why I came up with this.

is not the case as stated earlier.  


## elibroftw | 2022-06-08T17:47:47+00:00
You should've explicitly stated that signing with a subaddress is possible. You're article does not go into the technicalities.
So with the RPC API, would sign({'data': 'my message', 'accountIdx': 0, subaddressIdx: 2}) work (i.e. undocumented feature)?
EDIT: nvm it does work.

## spirobel | 2022-06-08T17:54:30+00:00
>You should've explicitly stated that signing with a subaddress is possible. 

I wrote the article for a semi technical audience. I also didnt intend to write a book. I would much rather write the code than explaining technicalities. But I am currently blocked by this issue. 

Anyway back to the topic:

@woodser  stated in the first post:
>This issue requests fixing wallet2 so it can send funds to itself with an integrated subaddress.

I dont think this is strictly necessary as stated in this comment: https://github.com/monero-ecosystem/monero-javascript/issues/90#issuecomment-1149474885

It is certainly a weird thing that should be investigated, but the pragmatic solution would look like this:
1.decode the integrated address when creating a transaction 2. check if the address belongs to the currently open wallet. 3. if that is the case show an error message and dont createTx.


## Happybara0827 | 2022-06-11T06:07:43+00:00
> 好难过。我真的需要这个功能。如果有的话，我们应该禁止发送到主地址，因为它们是旧地址而不是子地址。

这什么？


## kayabaNerve | 2022-06-29T05:40:39+00:00
The original specification/PR did have integrated subaddresses, yet it was officially removed in 2017, 2 months before being adopted into Monero. Any subaddress which is modified to include a payment ID is non-compliant. If the current Monero generates such invalid addresses in any way, or handles invalid addresses, that should be corrected, as monero-javascript recently did.

These invalid addresses are not recognized by https://xmr.llcoins.net/addresstests.html, the leading site for working with addresses, nor are they supported by a variety of projects in the ecosystem. If everyone had this bug mutually, I'd understand adoptance, but it's an immediate ecosystem fragment and one which further breaks Monero, as Monero will send with a payment ID yet won't work with it while scanning. I'd like to propose creating a new issue, or re-titleing this one, to correct the GUI wallet's/wallet2's behavior here.

## kayabaNerve | 2022-06-29T06:02:55+00:00
I had a comment here which does seem premature about length handling. Will withdraw it for now.

# Action History
- Created by: woodser | 2022-06-08T13:50:41+00:00
