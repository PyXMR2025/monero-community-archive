---
title: '[Discussion] Proposal to deprecate integrated addresses'
source_url: https://github.com/monero-project/monero/issues/7889
author: LocalMonero
assignees: []
labels: []
created_at: '2021-08-24T14:22:59+00:00'
updated_at: '2025-02-25T18:24:54+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
A natural progression from #3772

Integrated addresses are a serious problem for entities that batch their outgoing transfers. When a bunch of withdrawals are batched together, they may include no more than one integrated address, since a tx may include no more than one payment ID. This causes unnecessary congestion through artificial scarcity, which probably contributed to the recent events of major exchanges suspending their XMR withdrawals.

There exist subaddresses which may be batched together without limit, and the overwhelming majority of the network already uses them exclusively.

Additionally, eliminating integrated addresses would further increase the homogeneity of the network (improving privacy), reduce blockchain growth as there will no longer be a need to store payment ID data, make the UX simpler due to lesser variations in address types, and make development (both XMR protocol development and ecosystem development) easier due to having to account for less variations.

We recommend the following:

Remove support for integrated addresses (using subaddresses instead) by October 2022 (assuming that's when the v16 protocol upgrade happens).

Announce intent for these changes to be made as soon as consensus as reached.

# Discussion History
## selsta | 2021-08-24T14:25:43+00:00
Theoretically integrated addresses should only be used by services / merchants / exchanges so that for e.g. LocalMonero payouts it should be fine to only allow regular addresses.

For example the GUI can't even generate an integrated address for this reason exact reason (it's not something the end user should use).

## LocalMonero | 2021-08-24T14:30:11+00:00
@selsta the fact that integrated addresses are mostly only used by services/merchants/exchanges only increases the severity of the standing out of these transactions from the general mass of txs and makes it easy for chain analysis to assume that any tx that has a payment ID in it is linked to a service/merchant/exchange/pool.

## selsta | 2021-08-24T14:31:11+00:00
All transactions have an encrypted dummy payment id so on chain there is no difference between regular and integrated address.

## LocalMonero | 2021-08-24T14:34:56+00:00
@selsta the dummy payment ID will no longer be necessary, reducing blockchain growth. Off-chain data will also be homogenized, increasing privacy. This is not taking into account the lack of the integrated-address-imposed bottleneck on transfer batching and the other benefits mentioned in the first comment.

## sethforprivacy | 2021-08-24T18:14:52+00:00
I, for one, am all for this.

Unifying address formats is better for privacy, can reduce complexity of codebases around wallets, and simplifies UX for end-users.

At present, the UX around integrated addresses can be confusing and even outright dangerous, like how the Ledger always displays the underlying address instead of the integrated address, making address verification difficult or impossible depending on the application.

Subaddresses are superior and should be the only allowed alternate to main addresses IMO.

## SamsungGalaxyPlayer | 2021-08-25T02:27:31+00:00
Note on the timeline: if accepted, this would probably be merged with the larger proving system updates. If Monero goes the Seraphis route, for example, that will naturally be a time to revisit address UX since we would need to change the addressing system anyway.

## One-horse-wagon | 2021-08-25T23:10:21+00:00
Since it simplifies the codebase and few, if any people use it, it should be deprecated as requested.  Good idea.

## selsta | 2021-08-25T23:15:05+00:00
> few, if any people use it

How did you come to that conclusion?

## shopglobal | 2021-08-25T23:22:13+00:00
No, I disagree and I believe that deprecating integrated addresses would be
terrible. There's no sound reason to remove the functionality as it
provides a basic function to combine public wallet with payment id. It's
used widely in exchange and wallet configurations. It's good for liquidity
pools. It's got pros and cons against using subaddresses and that adds
value to Monero as a protocol not just XMR

So I vote to keep integrated addresses.

On Wed, Aug 25, 2021, 7:15 PM selsta ***@***.***> wrote:

> few, if any people use it
>
> How did you come to that conclusion?
>
> —
> You are receiving this because you are subscribed to this thread.
> Reply to this email directly, view it on GitHub
> <https://github.com/monero-project/monero/issues/7889#issuecomment-905937777>,
> or unsubscribe
> <https://github.com/notifications/unsubscribe-auth/ADBQBZYJ6EY4477F5ZB5CJTT6V2QXANCNFSM5CW6SAWQ>
> .
> Triage notifications on the go with GitHub Mobile for iOS
> <https://apps.apple.com/app/apple-store/id1477376905?ct=notification-email&mt=8&pt=524675>
> or Android
> <https://play.google.com/store/apps/details?id=com.github.android&utm_campaign=notification-email>
> .
>


## One-horse-wagon | 2021-08-25T23:27:12+00:00
> > few, if any people use it
> 
> How did you come to that conclusion?

I don't have any figures but integrated addresses are seldom mentioned in comparison to sub-addresses.  Therefore, I concluded there isn't much interest.

## LocalMonero | 2021-08-26T00:15:11+00:00
@selsta @One-horse-wagon based on our own withdrawal stats we can attest to integrated addresses being used in less than 10% of the cases.

## selsta | 2021-08-26T00:18:42+00:00
What would be interesting is how many services / exchanges / shops use integrated address vs subaddresses.

@LocalMonero Your number seems to be in regards to end users, which is unsurprisingly low as most wallets don't even allow you to generate an integrated address.

## t-900-a | 2021-08-26T00:56:27+00:00
Few considerations to add to the discussion ....

MyMonero, openMonero, monero-lws do not have support for subaddresses.
By the time integrated addresses are deprecated a lightweight wallet server should have support for subaddresses.

Examples of useful software that utilizes integrated addresses

https://github.com/bitrequest/bitrequest.github.io/issues/2

Example of software that should be using subaddresses, but doesn't

https://github.com/monero-integrations/monerowp/issues/56

A taiga board or other central place could be used to record the various projects & exchanges that need to adopt subaddresses.

## SamsungGalaxyPlayer | 2021-08-26T01:55:30+00:00
We can just have an active user update a table here on github, or update a github project board

## rbrunner7 | 2021-08-26T05:53:52+00:00
Under the assumption that we don't switch to something like Seraphis which brings changes regarding addresses anyway, thus under the assumption that we are free in our decision to leave everything as it is (supporting both integrated addresses and subaddresses versus dropping integrated addresses and continue subaddresses only), I lean towards **keeping** integrated addresses for now, i.e. not yet announce a fixed cut-off date.

When forming this opinion I did not look at details, but tried to look at the "bigger picture". If we remove them I think we lean a little bit too much on the technical side of things where we concentrate on making the coin and its technology better, and ask a little too much from the part of the Monero ecosystem that has a need of "sender identification" in some way.

Or, formulated a little more drastically: It's alright to force the whole ecosystem through frequent hardforks, through changing this, through deprecating that, through introducing this and this new mechanism, and so on, in the intererest of improving technology, privacy, fungibility, performance, etc, - but up to a certain point. In a certain sense a cryptocurrency is also there to **serve** its users and the ecosystem surrounding it, and there stability can be important.

Already now Monero is a much more difficult coin to support for shops, exchanges, etc. than other coins, for various reasons. We should not add still to that difficulty without careful consideration. Worst case a significant part of the overall cryptocurrency universe will find Monero not worth the bother given all those difficulties.


## serhack | 2021-08-26T08:23:17+00:00
I would not consider integrated address as a deprecated feature of Monero. Until we have a better alternative (or a new huge change such as Seraphis), I prefer not to kill that. For my point of view: subaddresses seems fine, but not for all the use cases of adoption. The main difference between a subaddress and an integrated address is who can generate them. Subaddress generation requires to know at least the private view key, while integrated address requires only the public address (or the public subaddress) and a random payment id.

Anyway, for any decision we take, I'll provide all my support to switch subaddress on [monerowp](https://github.com/monero-integrations/monero-wp) and the others payment gateways I've coded. Integrated addresses are helpful for some merchants, and someone even implemented integrated address based on subaddress index. 

@t-900-a: the support of subaddresses for monerowp is experimental and can be found on `subaddress.php`. It's a little bit slow even on servers that are powered by latest hardware. 

## One-horse-wagon | 2021-08-26T12:33:45+00:00
> Already now Monero is a much more difficult coin to support for shops, exchanges, etc. than other coins, for various reasons.

I wouldn't under estimate the ability of people to use Monero.  A market on the dark web for instance, not only uses Monero, but they also want customers to use PGP, which is even more difficult to understand than Monero.  If their numbers are to be believed, they claim to have over 350,000 active users and another 350,000 gawkers.

## LocalMonero | 2021-08-26T12:35:39+00:00
@rbrunner7 For all the reasons mentioned in the OP, integrated addresses are more of an obstacle than a feature. Subaddresses do what integrated addresses do, but better. Most of the ecosystem have already upgraded to them, and those that haven't probably won't upgrade until the protocol is changed. This is the same situation as it was with the separate payment IDs back in 2018.

While serhack is correct that integrated addresses have the advantage of being generated from a public key, one can easily sidestep this problem for subaddresses by pre-generating a bunch of them and storing them and then topping up the database as needed.

In our view, **primarily because this has massive impact on batching outgoing transfers which causes unnecessary extra transactions (congestion) and blockchain bloat** as well as the off-chain privacy leak, this is a band-aid that needs to be ripped off eventually, and the earlier it's done - the better.

## rbrunner7 | 2021-08-26T14:34:50+00:00
> I wouldn't under estimate the ability of people to use Monero. A market on the dark web for instance, not only uses Monero, but they also want customers to use PGP, which is even more difficult to understand than Monero. If their numbers are to be believed, they claim to have over 350,000 active users and another 350,000 gawkers.

Interesting. I was however more referring to technical difficulties, not difficulties in handling. How, for example, a shop plugin for Monero leads to a more complicated setup because `monero-wallet-rpc` has to run somewhere whereas a BTC plugin can directly interface with the Bitcoin blockchain itself because everything is so much simpler technically, or how Monero multisig is currently almost impossibly complex to implement for many environments (I studied this in detail for OpenBazaar).

## Cactii1 | 2021-08-26T17:19:27+00:00
 
> While serhack is correct that integrated addresses have the advantage of being generated from a public key, one can easily sidestep this problem for subaddresses by pre-generating a bunch of them and storing them and then topping up the database as needed.

This makes it more difficult to rotate your wallets. Every time you rotate a wallet you'd have to generate a bunch of new subaddresses and update your database of available addresses. If you want to keep historical information it's much more difficult to keep track of which wallet the subaddresses came from too.

I like integrated addresses, they are very easy to use and implement.  Monero is already very difficult to program for, so why make it even harder?


## busyboredom | 2021-08-26T19:29:42+00:00
Creating a database of pre-generated subaddresses doesn't solve the issue of synchronizing a list of active subadresses between threads in a multi-threaded or actor-based payment processor. Each thread needs up-to-date info on subadresses currently in use, so that two customers are never given the same subaddress at the same time.

With integrated addresses, threads are free to generate a random 64-bit payment ID on the spot without worrying about conflicts. To get the same non-locking system using subaddresses, you'd need to be pulling random subadresses from a database with 2^64 subaddresses in it.

## LocalMonero | 2021-08-26T20:00:37+00:00
> Creating a database of pre-generated subaddresses doesn't solve the issue of synchronizing that database between threads in a multi-threaded or actor-based payment processor. Each thread needs up-to-date info on subadresses currently in use, so that two customers are never given the same subaddress at the same time.
> 
> With integrated addresses, threads are free to generate a random 64-bit payment ID on the spot without worrying about conflicts. To get the same non-locking system using subaddresses, you'd need to be pulling random subadresses from a database with 2^64 subaddresses in it.

@busyboredom That's just a question of adding a uniqueness constraint to the address column in the database that stores the pending payments. Get the next address from the subaddress db if currently selected one is already used.

> This makes it more difficult to rotate your wallets. Every time you rotate a wallet you'd have to generate a bunch of new subaddresses and update your database of available addresses. If you want to keep historical information it's much more difficult to keep track of which wallet the subaddresses came from too.

@Cactii1 If you rotate wallets you may store the subaddress in one column and the base address associated with it in another column of the db to achieve the same effect.

> I like integrated addresses, they are very easy to use and implement. Monero is already very difficult to program for, so why make it even harder?

Because the downsides may outweigh the upsides. Integrated addresses:

- create extra blockchain bloat from the payment ID field;
- create unnecessary bloat and congestion due to inability to batch them, forcing services that process withdrawals to send out more txs than necessary;
- make ecosystem DX worse by having to account for more variations in addresses both when receiving and when sending;
- make core development more complicated;
- make UX worse by causing confusion over the address being much longer than the standard length;
- allow the ability to link different accounts to the same identity, causing an off-chain privacy leak:
**A major point of Monero is making privacy simple by default for the end user.** Integrated addresses stand in opposition to that, both when used by the end user, and when implemented as the default customer differentiation mechanism by services.

---

It's hard to deny that there are some particular use cases where integrated addresses are easier to use. The question is whether those use cases justify the corresponding loss of privacy and increase in bloat and congestion for the network, as well as the increased complexity of the protocol and UX.

## busyboredom | 2021-08-26T20:13:10+00:00
@LocalMonero is there a performant and open-source payment processor using subadresses that you would recommend I look at? Maybe seeing a good existing implementation would put my mind at ease. 

## LocalMonero | 2021-08-26T22:26:35+00:00
> @LocalMonero is there a performant and open-source payment processor using subadresses that you would recommend I look at? Maybe seeing a good existing implementation would put my mind at ease.

Perhaps @sausagenoods and @stnby from @moneropay, an open-source Monero payment processor project that use subaddresses, could offer some input on that.

## One-horse-wagon | 2021-08-26T23:50:06+00:00
Two more points.  Are not integrated addresses distinguishable by looking at the  tx_extra field in the JSON representation of transmission.  If so, it's a potential exploit on the fungibility of Monero.  

And second, the tx_extra field should be deprecated along with integrated addresses at the same time, IMO.  This was extensively discussed previously but I don't believe any decisions were reached?

## selsta | 2021-08-26T23:51:23+00:00
> Are not integrated addresses distinguishable by looking at the tx_extra field in the JSON representation of transmission. If so, it's a potential exploit on the fungibility of Monero.

This was fixed a while ago, see https://github.com/monero-project/monero/issues/7889#issuecomment-904695256

## jeffro256 | 2021-08-27T14:41:58+00:00
A lot of great discussion in this thread. One more point to add:

Integrated addresses can be generated once and used for multiple customers. This allows groups to compile "safelists" and/or certification authorities for merchants' addresses, which I think would help consumers feel safer sending their precious money to long random strings of characters. You can't easily do this with subaddresses.

## LocalMonero | 2021-08-28T14:23:50+00:00
> Integrated addresses can be generated once and used for multiple customers. [...] You can't easily do this with subaddresses.

What makes you say that? You can assign a single subaddress to multiple customers.

## jeffro256 | 2021-08-28T17:29:26+00:00
@LocalMonero  But then the processor has to guess the sender on other information: time of tx, amount, reuse, etc, which is unreliable. Imagine the pain of trying to deal with partial payments/refunds when 1000 other customers are sending to the same subaddress. Alternatively, the processor can have the customer send in a send-proof but that's bad for UI. Integrated addresses work really well for authenticating merchants IMO.

I would be 100% onboard for deprecating integrated addresses if there was a way to generate a zero-knowledge proof that subaddress S is a subaddress of primary address P. Then if customers can trust one address P, they can verify that they are sending to the right place for any subaddress given to them.

## LocalMonero | 2021-08-28T17:33:25+00:00
@jeffro256 there's some confusion here. If you provide a single integrated address to multiple customers you have to guess all the same information that you listed.

What you seem to be saying is that you can provide the customers with a base address and then have them generate the integrated address by themselves, correct? Sounds like creating extra steps instead of just giving them a dedicated subaddress.

## jeffro256 | 2021-08-28T18:18:20+00:00
@LocalMonero Correct me if I'm wrong, but that's where the payment IDs come into play with integrated addresses. You can easily distinguish between senders with a high-entropy encrypted bit string. IMO this is a much stronger solution for differentiating payments than what you can do with subaddresses. You could try to put some special code in the wallets to encode information in the dummy payment ID, but that's sorta hacky. 

## LocalMonero | 2021-08-28T18:23:01+00:00
Integrated addresses = base address + payment ID combined into one address. You generate different payment IDs to differentiate customers, resulting in different integrated addresses.

Just in the same way, you can generate different subaddresses from the same base wallet to differentiate customers. When your wallet processes payments it knows which subaddress received which payment. You differentiate by the receiving subaddress.

## jeffro256 | 2021-08-28T18:49:03+00:00
Sorry, I should have been more specific. Yes, integrated addresses are just a way to encode a base address + a payment ID. But since the base address can remain permanent for the lifetime of a merchant, with only the payment ID changing often, any integrated address can be verified to belong to a certain base address. The same cannot currently be said for  subaddresses, which is a valuable use case IMO. 

## cirocosta | 2021-08-29T01:25:55+00:00
>  _**@jeffro256** [...] any integrated address can be verified to belong to a certain base address.  The same cannot currently be said for subaddresses, [...]_

I don't think that arguments holds - for that proof you're talking about, I believe you'd have to record the payment ID somewhere, right? Well, subaddresses are made out of a major and a minor index, which, as long as stored somehow (just like you would for payment ID), once used will deterministically derive a given subaddress, thus, letting you prove that a subaddress "belongs" to a base address.

## jeffro256 | 2021-08-29T18:51:32+00:00
> You'd have to record the payment ID somewhere, right?

If you've ever sent to an integrated address, you might notice that they are longer than normal addresses. This is because there is a payment ID tacked onto the end of the address. Much like how normal  addresses are just a way to encode (public view key, public spend key), integrated addresses are just a way to encode (public view key, public spend key, payment ID). There is also a field in every tx that stores a payment ID, whether it is used or not (see [this comment](https://github.com/monero-project/monero/issues/7889#issuecomment-904695256)).

> Well, subaddresses are made out of a major and a minor index, which [...] let[s] you prove that a subaddress "belongs" to a base address.

The problem is that a sub address is not just derived from the hash of an index, but also the hash of the private view key. Here is the formula to derive subaddresses:

    Ks,i = Ks + H(kv,i)*G
    Kv,i = kv*Ks

    where i is the subaddress index, 
              Ks,i is the ith public spend key,
              Kv,i is the ith public view key,
              Ks is the base public spend key,
              kv is the base private view key,
              H is a hash function,
              and G is the generator.

As you can see, it in order to deterministically prove that a subaddress belongs to a base address, you would need to divulge the base private view key, which is not ideal for a merchants. However, if there was a way to create a zero-knowledge proof for this scenario, then subaddresses would be easily able to replace integrated addresses in a merchant environment IMO. Until then, I think integrated addresses prove too useful to deprecate. 

## cirocosta | 2021-08-30T12:47:40+00:00
Hey @jeffro256, yes! thanks for pointing that out, totally agree that divulging the private view key is far from ideal - I think I miscommunicated here though.

The point I was going for was just that with a combination of a pool of pre-generated subaddresses (like suggested before in this thread), if it's of one's concern the necessity of proving that a given subaddress is indeed derived out of a given base, one could maintain in their database alongside the subaddress the indices   that were used to get there, which can then, if necessary, be used to do that proof if necessary in a warm/cold way.

If you don't mind me asking, what's your current need when it comes to verifying that an address comes from a particular base? Is it to prove to customers that the subaddresses they're given are based of a particular base address (1), or for the sys admin to make sure nothing is funky with the addresses being handed to the customers (2)? I've been commenting here under the assumption of (2).

Cheers, mate!

## jeffro256 | 2021-08-30T20:37:23+00:00
@cirocosta Thanks for the clarification! Yeah I guess we were sort of misunderstanding. For the purpose of (2), pregenerating a large list of subaddresses would work fine enough for sever-side validation. I was talking more of the first case (i.e. customer protection). Monero transactions are irreversible, and there is no central authority to arbitrate disputes, so it's a great thing that integrated addresses exist and allow customers to self-validate who they are sending to. If a customer messes up the payment ID, (e.g. resending to the same payment ID), as long as the base address is the same, then they know who to talk to about refunds. Also if a merchant is hit with a address-replacement attack, the customer will be able to instantly verify that it happened and prevent transferring funds to an attacker. 

## iamamyth | 2021-08-31T18:43:18+00:00
> I was talking more of the first case (i.e. customer protection). Monero transactions are irreversible, and there is no central authority to arbitrate disputes, so it's a great thing that integrated addresses exist and allow customers to self-validate who they are sending to. If a customer messes up the payment ID, (e.g. resending to the same payment ID), as long as the base address is the same, then they know who to talk to about refunds. Also if a merchant is hit with a address-replacement attack, the customer will be able to instantly verify that it happened and prevent transferring funds to an attacker.

How many users understand what you described regarding address continuity and address replacement attacks? It seems to me the minimum capability bar for every user would be "copy and paste text, triple check it's correct". Anyone capable of following that process, who happens to also understand the threat of address replacement attacks, could likely mitigate such attacks via a secondary communication channel.

How would the mitigation you described provide any likely benefit in a plausible threat model? For a first-time sender who doesn't know the address, the subaddress and integrated are effectively the same. In subsequent cases, the sender needs an address book to know that anything has changed. But, if the sender has an address book, then a change in recipient address would be equally obvious with either addressing format, so the only possible difference here would be the remediation step. If anything, subaddresses would make the user *more* conservative (just don't initiate the transfer without secondary confirmation), which seems a desirable result. The only scenario I can see which subaddresses materially impact would be rotating the recipient's address while keeping the same base address, but why would the recipient do that in the first place? I suppose the options for out of band address confirmation increase with integrated addresses (e.g. ask someone you know who's done business with the merchant to confirm the address), but I suspect few, if any, avail themselves of such options.

## jeffro256 | 2021-08-31T20:12:12+00:00
@iamamyth This is a great point, and this is where we would start geting into the gritty details. Obviously no one is gonna manually inspect the base address of every integrated address they send to because it's such a PITA. And you also have to bootstrap that trust in the first place as you mentioned. In the same way, we don't validate the authenticity of each and every connection to a website we make; we leave that up to HTTPS and certificate authorities. We don't manually filter every outgoing request from our browser for ads and tracking sites; we leave that to adblocks. This client-side authentication of recipients would ideally be done through a seamless automated system, and integrated addresses give us the ability to do that. 

## iamamyth | 2021-08-31T20:58:31+00:00
> This client-side authentication of recipients would ideally be done through a seamless automated system

My point remains: Integrated addresses provide a vanishingly small usable surface for any such automated system, as compared to subaddresses. Is it exactly zero? No, I suppose not. Is it exceedingly close to zero, so as to be inconsequential? In my view, yes. All of which doesn't necessarily mean integrated addresses should be deprecated, there are other tradeoffs to consider, but I think it helps to focus discussion of feature deprecations on actual and near-term likely usages. Put differently, what you've outlined seems like a rounding error in a cost-benefit analysis.

## HoverHalver | 2021-09-16T10:53:30+00:00
> any integrated address can be verified to belong to a certain base address. The same cannot currently be said for subaddresses,

Verifying if a given subaddress belongs to a file of pregenerated subaddresses uses less than 10 lines of code in PHP.


## spirobel | 2021-09-17T05:05:28+00:00
> A natural progression from #3772
> 
> Integrated addresses are a serious problem for entities that batch their outgoing transfers. When a bunch of withdrawals are batched together, they may include no more than one integrated address, since a tx may include no more than one payment ID. This causes unnecessary congestion through artificial scarcity, which probably contributed to the recent events of major exchanges suspending their XMR withdrawals.
> 
> There exist subaddresses which may be batched together without limit, and the overwhelming majority of the network already uses them exclusively.

wouldnt it be possible to ask customers to only withdraw to subaddresses?

## jeffro256 | 2021-09-17T18:44:58+00:00
> Verifying if a given subaddress belongs to a file of pregenerated subaddresses uses less than 10 lines of code in PHP.

See https://github.com/monero-project/monero/issues/7889#issuecomment-908676511


## tevador | 2021-12-29T22:53:03+00:00
FYI, the current proposal for the future Seraphis addressing scheme includes the removal of integrated addresses and encrypted payment IDs.

To compensate for this removal, a new type of wallet is proposed that enables the generation of subaddresses without the private view key.

If a merchant is watching this discussion, we would like to hear feedback on the merchant-related features.

https://gist.github.com/tevador/50160d160d24cfc6c52ae02eb3d17024

 

## SamsungGalaxyPlayer | 2021-12-30T01:21:31+00:00
We need to be able to non-interactively pass at least a short string to a static address for identification for the Thorchain integration to work.

Related: https://gitlab.com/thorchain/thornode/-/issues/919

The issue above says 16 bytes, but it's actually 16 characters (8 bytes).

If Thorchain had their way, they would put the whole string in the tx_extra. This is a compromise to allow those with view keys (the public) to be able to decrypt the 16 character payment ID and compare it to the hashes of the payment requests.

It's extremely important to allow users to non-interactively pass through a reference string of sufficient length.

## rbrunner7 | 2021-12-30T06:26:03+00:00
@SamsungGalaxyPlayer wrote:

> We need to be able to non-interactively pass at least a short string to a static address for identification for the Thorchain integration to work. [...] It's extremely important to allow users to non-interactively pass through a reference string of sufficient length.

My first immediate thoughts when reading this: Did somebody with the necessary knowledge already check whether what Thorchain proposes / wants here is A) a solution for a real problem, B) an appropriate solution for said problem, C) without a simpler alternative, and D) not threatening the privacy of Monero users that don't use and don't care about Thorchain ("Look! There in the Monero blockchain. One of those Monero txs connected with Thorchain use" as a consequence of this would be unfortunate all around).

I am not able to come up with an immediate alternative way to solve the problem to associate a "transaction intent" with the transaction itself as mentioned in the [Thorchain issue](https://gitlab.com/thorchain/thornode/-/issues/919) you link to, but maybe people with better knowledge of Monero's internal workings can have a look.

## SamsungGalaxyPlayer | 2021-12-30T06:31:23+00:00
@rbrunner7 I'm confused, what do you mean by is this a solution to a real problem? This is a real use-case that Cake is investing in heavily since it provides a simple UX like an instant exchanger in a more decentralized manner. It's a valid use-case we wish to support.

The requirement to convey a transaction intent as initiated by the sender is a use-case that payment IDs currently allow for, and I want to make sure that remains.

I'm not clinging to a specific implementation, but this functionality is important and should remain in some reasonable form.

Edit: Firo is planning on encrypting a memo with the amount with Spark, which is an example of a different way of accounting for the same use-case. We don't need to be daft and make it 512 bytes or whatever, but a small memo (like 8 bytes) is quite manageable for the flexibility it allows.

## rbrunner7 | 2021-12-30T06:37:26+00:00
> I'm confused, what do you mean by is this a solution to a real problem?

Agreed, maybe point A) is trivial to answer with "yes, of course", and we can continue already to the probably much harder point B) of mine.

But still, as I said I don't know much about Thorchain, but is it really an absolute "must" that the intent is published **before** the transaction? No way to reverse that? Because if you can do the tx first and the intent second, you could of course trivially include the tx hash in the intent and associate that way.

Maybe that would mean bigger changes in the Thorchain code base, as you would have to do a reverse search to find the intent if you only hold the tx, but perhaps doable. "Thinking outside the box" can sometimes find surprising solutions. And maybe we still could get rid of those problematic payment IDs.

## rbrunner7 | 2021-12-30T06:52:48+00:00
I realized that my proposal to send the tx first and the intent second might be pretty dumb if between intent and tx there has to happen an "offer acceptance" of any sort for the system to work, but I would love to have that argued convincingly by somebody with solid knowledge of how Thorchain works.

## tevador | 2021-12-30T10:36:31+00:00
> We need to be able to non-interactively pass at least a short string to a static address for identification for the Thorchain integration to work.
> 
> Related: https://gitlab.com/thorchain/thornode/-/issues/919
> 
> The issue above says 16 bytes, but it's actually 16 characters (8 bytes).
> 
> If Thorchain had their way, they would put the whole string in the tx_extra. This is a compromise to allow those with view keys (the public) to be able to decrypt the 16 character payment ID and compare it to the hashes of the payment requests.
> 
> It's extremely important to allow users to non-interactively pass through a reference string of sufficient length.

Firstly, there is a big difference between 16 hex characters (64-bit security) and 16 bytes (128-bit security). The former one is insecure as it is feasible to generate two payloads that will hash to the same value. You will need at least 12 bytes to achieve any meaningful security.

Secondly, we should consider if bloating the chain to enable one specific feature not everyone will use is worth it.

I see at least 2 better options:

1. communicate the hash value off-chain or using another blockchain
2. pass the encrypted hash in tx_extra (this will make the transactions somewhat stand out, but at least it won't affect the size for everyone)


## SamsungGalaxyPlayer | 2021-12-30T16:19:08+00:00
I'm happy to use https://github.com/monero-project/monero/pull/6410 instead of a payment ID field for Thorchain if it's added. 16 or 32 bytes is enough it seems.

I specifically wanted to avoid having them dump data in `tx_extra` because of issues like https://github.com/monero-project/monero/issues/6668, but Thorchain will be happy to do this if that's what you all want. I think this is inadvisable since it would make transactions more clearly distinguishable.

## rbrunner7 | 2021-12-30T17:41:54+00:00
Another idea, maybe stupid, but maybe not: Maybe Thorchain could be modified to hand out subaddresses that clients could put both into intents and use for the following Monero transactions?

## One-horse-wagon | 2021-12-30T18:47:03+00:00
I think I missed something because why are we so worried about being accommodating to Thorchain?

## SamsungGalaxyPlayer | 2021-12-30T18:55:05+00:00
@rbrunner7 Thorchain is a semi-decentralized network that only follows commands that are recorded as a verifiable public record, so it's not obvious how this could be achieved. In theory it could be possible for nodes to declare "deposits to this Monero subaddress are for this explicit purpose", but this has other issues.

The ability to include some transaction intent as a sender is an important feature. Thorchain wishes to use this and you can read all about how they do this for other chains [here](https://docs.thorchain.org/developers/transaction-memos), but I highly doubt this will be the only service that uses it. People used payment IDs far before subaddresses existed of course, and even though subaddresses cover a lot of the same use-cases, they don't cover all of them.

## tevador | 2021-12-31T14:22:39+00:00
> The ability to include some transaction intent as a sender is an important feature. Thorchain wishes to use this and you can read all about how they do this for other chains here, but I highly doubt this will be the only service that uses it. People used payment IDs far before subaddresses existed of course, and even though subaddresses cover a lot of the same use-cases, they don't cover all of them.

The encrypted payment ID was never intended for passing arbitrary sender-generated information to the recipient. If you read the [original design notes](https://pastebin.com/bp5RKXuC), it was to be used only with integrated addresses generated by the recipient. This use case can be entirely replaced by subaddresses.

The way I see the Thorchain feature, it is completely orthogonal to payment IDs and addressing schemes. The proper way of passing sender-generated data would be some encrypted memo field like the one proposed in #6410.

## SamsungGalaxyPlayer | 2021-12-31T15:37:08+00:00
In any case, I would like the necessary functionality to be maintained in `tx_extra` in some form, whether it's a free-for-all there (non-ideal) or like #6410.

## gituser | 2022-02-06T17:46:47+00:00
Please don't kill the feature which is working just fine for many many merchants.

Why I don't like subaddresses:
* need to generate separate subaddress for each deposit / invoice - requires knowing key, takes more time comparing to just generating integrated address where you only need to know public key.
* need to accumulate all subaddress balances into one in order to withdraw total amount (takes another tx + fees + time)
* exchanges which suspend XMR deposits (typically Binance) are doing so cause they are already using subaddresses and need to accumulate all those payments from subaddresses into 1 address in order to withdraw big amounts and also due to 10 confirmation utxo lock

Why break monero for thousands of merchants and involve unneeded maintenance there?
It's already a core monero feature used by many.
Leave the integrated addresses as they are, they are working just fine for years without issues.

## selsta | 2022-02-06T17:51:05+00:00
@gituser Regarding point 2 and 3, if you use subaddresses (not accounts) you don't have to anything different than if you would use integrated addresses. No accumulation required.

## gituser | 2022-02-06T19:18:13+00:00
> @gituser Regarding point 2 and 3, if you use subaddresses (not accounts) you don't have to anything different than if you would use integrated addresses. No accumulation required.

Maybe I did it wrong but it was so last time I've tried. Care to share a guide on subaddresses?

Thank you.

## ndorf | 2022-02-06T23:19:24+00:00
Just make sure you're creating subaddresses, and not accounts. That's it.

## CryptoGrampy | 2022-04-04T23:33:46+00:00
With integrated addresses, I can generate unique payment addresses using just a view key/primary address, totally offline, and not have to worry about whether or not an address has ever been used in the associated wallet.  I can instantly create payment unique addresses without ANY scanning or wait time and not have to worry about 1. whether or not an address has been used before and 2. whether or not my wallet will even detect a subaddress payment.  If you generate 'random' subaddresses from an offline generator, you don't know if they've been used before, and it's highly unlikely your Monero GUI wallet at home will see that a payment has been made.  I do *not* think subaddresses 100% cover everything an integrated address does today until I can generate subaddresses offline, and know there won't be collisions and know that my remote wallet I don't have access to on the other side of the world will 100% pick up those payments.  

## Cactii1 | 2022-04-04T23:42:39+00:00
Maybe we should deprecate sub-addresses and only have integrated addresses.

## paulshapiro | 2022-04-04T23:54:28+00:00
Grampy,

It is actually possible for clients to generate subaddresses in an offline and semi-distributed manner presently without collision. i'll publish some work on this imminently. integrated addresses also don't solve certain problems. I think we should just keep both for now personally. 

## CryptoGrampy | 2022-04-04T23:55:42+00:00
I know you can generate them randomly, but a wallet today isn't going to pick up those random subaddress payments at index 1000000 by default.

## paulshapiro | 2022-04-04T23:56:17+00:00
No my solution doesn't require randomness

## Cactii1 | 2022-04-04T23:57:32+00:00
Please share.

## CryptoGrampy | 2022-04-05T00:03:40+00:00
> No my solution doesn't require randomness

So your point of sale (view key wallet A) generating the subaddresses/collecting payment (i.e. say i'm a waiter on the other side of the world) shouldn't need to know *anything* about the spend key wallet (wallet B) (which subaddresses have been used, which index the wallet has stopped tracking subaddresses, etc), and the wallet with the spend key should be able to know of *any* subaddresses that have been used by default.  Wallet A should also not need to track its own or other Wallet A's subaddresses to know if a subaddress has already been used.  

## Cactii1 | 2022-04-05T00:11:04+00:00
> So your point of sale (view key wallet A) generating the subaddresses/collecting payment (i.e. say i'm a waiter on the other side of the world) shouldn't need to know _anything_ about the spend key wallet (wallet B) 

This is a very good point. What if I am a distributor and I have sub-distributors and I want all payments for things to go into my main XMR wallet. With integrated addresses this is possible without my sub-distributor having to have access to my spend keys as it's doable with view-keys. This is similar to how the Monero Integrations Wordpress plugin currently works - the server can generate a payment address without having to give up full control of the wallet.

By removing integrated addresses it'd limit the current functionality. Those calling for this change should consider that after removing Integrated Addresses the functionality of Monero will be more limited.

## paulshapiro | 2022-04-05T00:16:01+00:00
if you say that clients are to track no information about the addresses which have been used then you are by definition, as far as I can tell, stipulating a system that requires random generation instead.  but other than that, it seems to be entirely possible to do what you're asking for with subaddresses and is something that Justin B and I will propose in a second

## CryptoGrampy | 2022-04-05T00:16:20+00:00
> > So your point of sale (view key wallet A) generating the subaddresses/collecting payment (i.e. say i'm a waiter on the other side of the world) shouldn't need to know _anything_ about the spend key wallet (wallet B)
> 
> This is a very good point. What if I am a distributor and I have sub-distributors and I want all payments for things to go into my main XMR wallet. With integrated addresses this is possible without my sub-distributor having to have access to my spend keys as it's doable with view-keys. This is similar to how the Monero Integrations Wordpress plugin currently works - the server can generate a payment address without having to give up full control of the wallet.
> 
> By removing integrated addresses it'd limit the current functionality. Those calling for this change should consider that after removing Integrated Addresses the functionality of Monero will be more limited.

You nailed it. I'm actually currently working on a project that uses this exact method right now for a point of sale app... You will just hit a bookmarked URL with your primary and view key (and a couple other items) as query params, and BOOM.  You instantly have a point of sale app that can receive XMR.  

No need to load up and sync a wallet, no way for someone to steal your funds.  Generate integrated addresses on the fly offline, scan them using xmrchain or your own selfhosted explorer.  Bookmark the URL with your params and you have a simple point of sale anywhere in the world.  

## paulshapiro | 2022-04-05T00:17:02+00:00
By the way, don't get me wrong, I think integrated addresses have their benefits as well as you are describing, why don't they have some problems?

## paulshapiro | 2022-04-05T00:17:11+00:00
but*

## Cactii1 | 2022-04-05T00:25:13+00:00
Sure, they do have problems, they stand out on the blockchain as being different than other txs. Right now that's fixed by giving every tx dummy data if it's not an integrated address. Now getting rid of integrated addresses is only about blockchain bloat.

## CryptoGrampy | 2022-04-05T03:00:43+00:00
> By the way, don't get me wrong, I think integrated addresses have their benefits as well as you are describing, why don't they have some problems?

I'm certainly not super knowledgeable on the pros and cons of these things from the technical aspect.  I've actually always been on team subaddress (especially with the promise of Seraphis/Jamtis tiered address schemes) and never really understood the integrated address argument until I started actually playing around with it.  I just wanted to throw my thoughts out there for the big brain people working on Seraphis / deprecating these addresses to consider.   The comparison between subaddresses and integrated addresses definitely has NASA/USSR simple pencil vs zero gravity highly engineered ball point pen vibes.  

We do really need better simple merchant tools, and it's actually _extremely_ simple to write the client logic to generate random integrated payment ids for the example of a waiter accepting payment for a restaurant owner (or franchise chain) without knowing anything about the franchise owner wallet vs the amount of code required to write a client wallet library with full scanning so that the low tier wallet knows which subaddresses the high tier address has used coupled with the amount of CPU scanning required to look for all of those subaddresses in every wallet tier (waiter needs to be fully up to date to know which subaddresses have been used by other waiter-tier wallets, and full tier wallet has to be scanning through potentially thousands of subaddresses, etc etc).

I think it may be worth taking a stronger look at the total system CPU usage for low / high tier wallets in a multi-tiered payment scenario where there may be hundreds or thousands of payments coming in per day.  From my perspective, the integrated address is already _fully_ ready for dozens of restaurant servers to be accepting thousands of payments into one single base wallet *today* with no collisions, simple and low complexity client code, and very little added CPU burden throughout the spectrum for scanning on both the point of sale client and the spend key wallet at the top tier.  Perhaps it's worth some blue sky ideation into a world where integrated payment addresses are taken to the Jamtis level.  

## busyboredom | 2022-04-05T12:55:16+00:00
One of the improvements in Jamtis is the introduction of an "address tag" into outputs, allowing the subaddress index to be read directly from the output instead of needing to check against a giant matrix of keys: https://gist.github.com/tevador/50160d160d24cfc6c52ae02eb3d17024#53-receiving-an-output

This feature allows vendors to efficiently watch for payments on all subaddresses at once. That'll give subaddresses the simplicity, performance and collision resistance of integrated addresses. 

So knowing that this improvement is in the works, I think we should just wait on depreciating integrated addresses until Jamtis is live. That way we're depreciating it after there's a true drop-in replacement, and not before. 

## CryptoGrampy | 2022-04-05T18:02:12+00:00
Beyond the technical mechanics of subaddress scanning vs integrated, I also think it's important to consider the current wallet UX for managing potentially thousands of subaddresses vs thousands of integrated address payments. Definitely worth discussing with merchants, but I would imagine that managing a thousand integrated payments a day in a wallet is currently much easier to deal with for sweeping/tracking than a thousand subaddresses.  Definitely worth thinking about/getting feedback in this area.

## lukeprofits | 2023-05-16T21:47:41+00:00
My project for automatically paying recurring subscriptions in Monero uses integrated addresses: https://github.com/lukeprofits/Monero_Subscriptions_Wallet/

They seem like a better option than subaddresses, because subaddresses can't be generated without access to the merchants wallet, whereas integrated addresses can be. 

My project is focusing more on accessibility and ease of use for merchants. 

Please don't break my project by depreciating them, unless there is a really good reason. 

## rbrunner7 | 2023-05-17T04:00:36+00:00
@lukeprofits wrote:

> Please don't break my project by depreciating them, unless there is a really good reason.

Of course I can speak strictly for myself only and not for the Monero dev community at large, but from watching things quite closely I am pretty sure you are on the safe side. I really don't think that we can get consensus now to remove the functionality of integrated addresses and eliminate them with a hardfork.

Looking forward, with the switch to Seraphis both subaddresses and integrated address will vanish and get replaced by a single "unified" form of address. The important part for applications like yours: Generating addresses is almost as easy as it is now with integrated addresses. You still need a key, if my understanding is correct, like with subaddresses today, but a key that can do nothing else than generating addresses and that therefore will be no problem for people to hand over, and you don't have to keep track of addresses you already generated.

You can check e.g. [here](https://gist.github.com/tevador/50160d160d24cfc6c52ae02eb3d17024#231-address-generator) for more details. The Jamtis feature in question is called [address generator](https://gist.github.com/tevador/50160d160d24cfc6c52ae02eb3d17024#231-address-generator).

## jeffro256 | 2024-05-06T20:11:10+00:00
Poking this post since there has been a recent update. @tevador has wrote up a [proposal](https://gist.github.com/tevador/d3656a217c0177c160b9b6219d9ebb96) for supporting the Jamtis addressing protocol alongside current legacy addresses (today's integrated addresses included) on the RingCT consensus protocol. Here's a path for how we could *slowly* phase out integrated addresses while giving payment processors ample time to switch to an addressing scheme which gives feature parity (generating arbitrary number of recipient addresses without access to private spend key):

1. Beforehand, agree on rough date J (in chain height) when wallet constructors will start using Jamtis, and date D when we agree to deprecate integrated addresses by
2. On block height J, begin constructing Jamtis + Legacy addressed txs, including 8 bytes for a payment ID in each tx, whether used or not.
3. Wait (D-J) blocks
4. Once we pass block D, all wallet constructors stop adding the 8 byte dummy payment ID to their txs

After this point, we get to shave 8 bytes of each transaction while still supporting all non-integrated addresses and Jamtis addresses. Technically, payment processors would be still able to use integrated addresses without official support as long as the senders' wallets support it and they don't care about fingerprinting their transactions. However, this time, like @rbrunner7 mentioned, payment processors have an actually viable alternative with Jamtis addresses. The Jamtis "PaymentValidator" wallet tier is similar to the current viewkey wallet, except that it can generate addresses and can't see self-send enotes (even better for processor security). And with tevadors RingCT proposal, payment processors get the option of *slowly* phasing out their integrated addresses at their own pace. Seems like a win-win. Pinging @lukeprofits 

P.S: A nice side effect of this proposal unrelated to the OP is that main addresses would be able to use the encrypted address tag space for Janus protection.

## FiatDemise | 2025-02-25T18:24:52+00:00
XMRChat uses integrated addresses. They've worked very well for our use case, and we would like to continue using them. We were advised that we should switch to subaddresses instead. Our lead developer saeedab started looking into it, had some questions, and began a conversation on the Monero Community Workgroup, linked here:

https://matrix.to/#/!WzzKmkfUkXPHFERgvm:matrix.org/$sKIamFscPTodtWBQHJjIeVkTuQsX9Y7I9C2wpZcoXKY?via=cypherstack.com&via=matrix.org&via=monero.social

At the end of that conversation, it looks like integrated addresses will not be deprecated, and that this issue should be closed. Last responses here from linked and quoted:
https://matrix.to/#/!WzzKmkfUkXPHFERgvm:matrix.org/$AVTwkpiVcENk7nKanQ3vHFqS5qzhTvJA_VLSk8E3tXw?via=cypherstack.com&via=matrix.org&via=monero.social

spirobel -
"this proposal is there since forever and will most likely never get implemented. There is no good reason for you to switch to subaddresses. They only make sense for end users that want to use just one wallet but have multiple online identities that they dont want to see connected. So picture someone who sells catnip otc and sometimes receives birthday money from their grandma. They dont want their grandma to know under any circumstances about their OTC catnip trading activity. if grandma were to browse a catnip trading board and see the address she already knows is her grandsons, she knows. That is the reason these addresses are used. For a merchant this makes zero sense. Because they have a website that is known as this one entity. Sharing different subaddresses with different customers doesnt magically split it up, because they all got it from the same known entity. 
...
so the exchange that wants to send non uniform transactions to batch things can just not allow withdrawing to integrated addresses. problem solved"

ofrnxmr - "I dont know of any exchange that allows wd to intg address"

spirobel - "yeah it does not make a ton of sense. this issue should just be closed."



# Action History
- Created by: LocalMonero | 2021-08-24T14:22:59+00:00
