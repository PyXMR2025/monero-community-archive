---
title: '[Discussion] Proposal to deprecate the standalone payment ID'
source_url: https://github.com/monero-project/monero/issues/3772
author: SamsungGalaxyPlayer
assignees: []
labels: []
created_at: '2018-05-07T17:13:21+00:00'
updated_at: '2024-02-15T18:13:52+00:00'
type: issue
status: closed
closed_at: '2024-02-15T18:13:52+00:00'
---

# Original Description
**Below is the original text. Please read the other comments for more information:**

Payment IDs are inconvenient, and Monero needs to live with them at the moment. We have addresses, addresses + payment IDs, integrated addresses, and subaddresses. It's confusing and difficult on new users.

Based on some initial community discussion, I recommend that we set some goals for moving away from SPIs. Too many people forget them in their transaction, leading to confusion, larger support requirements, and possibly the loss of funds. Furthermore, there are some privacy concerns. Below are a few steps that can be taken to move away from SPIs in favor of integrated addresses and subaddresses. Fewer means of distinguishing transactions improves privacy.

I recommend the following:

1. Upgrade the Monero FFS to use integrated addresses or subaddresses as soon as possible.

2. Remove support for sending with SPIs by March 2019 (v9 protocol upgrade).

3. Remove support for integrated addresses (using subaddresses instead) by March 2020 (v11 protocol upgrade).

4. Announce intent for these changes to be made as soon as consensus as reached.

Referencing [the 2018/05/06 dev meeting](https://monerobase.com/wiki/DevMeeting_2018-05-06) and @localmonero, who introduced the idea.

# Discussion History
## Starmute | 2018-05-07T18:00:27+00:00
ACK, but I should note it’s not really possible at a lower level than the wallet to distinguish between integrated addresses and short pIDs.

Regardless, we’ll support this decision in Cake Wallet.

## serhack | 2018-05-07T18:07:35+00:00
[Monero Integrations](https://monerointegrations.com) workgroup agrees about the deprecating of Payment ID in favor of integrated addresses and subaddresses.

In the next days, we are going to deprecate payment ID (only [Monero Woocommerce Plugin](https://github.com/monero-integrations/monerowp) affected).

## sneurlax | 2018-05-07T19:51:16+00:00
Concept ACK: one Monero, one anonymity set.  As serhack said, we'll keep up with all changes in monero-integrations

## LocalMonero | 2018-05-08T02:42:45+00:00
Thanks @SamsungGalaxyPlayer for taking the time to open this issue.

One thing I would say, I don't think there's any need to forcefully deprecate integrated addresses, since from the UX perspective there's no difference on the sending side, hence no loss of productivity to the economy as there is with SPIs.

Unless there are privacy/security drawbacks to integrated addresses vs subadresses.

## burnssos | 2018-05-08T06:48:03+00:00
While I understand the concerns about new user Payment ID issues sometimes causing disgruntled experiences, these can be resolved on the UX. 

I believe it is important to maintain the option of the standalone 64-character payment ID field for the valuable, yet uncommon use case - PROOF OF EXISTENCE. 

If a Monero Secret View Key is widely disseminated, it can act as a "notary". The Payment ID field provides an easy method of sharing information or even a file's SHA256 hash. Planning for the future, if the Payment ID field allowed all Base64 characters it would provide additional options.

## johnalanwoods | 2018-05-08T08:54:54+00:00
@burnssos can you elaborate on this a bit more? Is your intention to use paymentID as a method for saving an immutable record?

## burnssos | 2018-05-08T14:49:04+00:00
In my experimentation with Monero over the years, it seems like an easy way to do it. With the secret view key you can see the payment ID. I'd love to test this across the network to confirm my experiences locally.

https://github.com/burnssos/monero-github-shared-viewkey

(It'd be cheaper if we had a Monero fork with Doge-like properties - anyone know any redundant Monero forks created lately to use?)

Multisig wallets could provide more use cases for a "notary" feature as well but needs more testing.

@johnalanwoods - yes. The Payment ID is already used for that purpose - just looking at usage beyond an invoice/account ID.

Simple Example Use Case: Proof of Existence for electronic file.

A billionaire banker and a Monero user agree to a single bet on whether the price of Bitcoin will go below $1000 within 1 year; this physical piece of paper gets signed by both of them. This physical agreement is scanned and both of them get the scanned file. The Monero user wants to ensure further evidence of this agreement's existence. He calculates the SHA256 sum of the scanned file and sends the smallest amount of Monero to a reputable, widely published standard Monero public address which has a widely published secret view key; in his Payment ID he pastes the SHA256 sum of the scanned file. (If all Base64 characters were allowed he could truncate the SHA256 sum and use 20 characters to further link the document to the billionaire banker; or use all 64 characters for a SHA384 sum). Once the transaction is sent, anyone can use the reputable and widely published secret view key to see that SHA256 evidence in the Payment ID for the transaction. The Monero user can prove they were the sender of the transaction using the Prove/Check features in the GUI wallet and has documented the existence of that electronic file as of that tx on-chain.

## sneurlax | 2018-05-08T14:53:09+00:00
Testnet and stagenet are available for cheaper(-than-Mainnet) testing

On Tue, May 8, 2018, 07:49 burnssos <notifications@github.com> wrote:

> In my experimentation with Monero over the years, it seems like an easy
> way to do it. With the secret view key you can see the payment ID. I'd love
> to test this across the network to confirm my experiences locally.
>
> https://github.com/burnssos/monero-github-shared-viewkey
>
> (It'd be cheaper if we had a Monero fork with Doge-like properties -
> anyone know any redundant Monero forks created lately to use?)
>
> Multisig wallets could provide more use cases for a "notary" feature as
> well but needs more testing.
>
> @johnalanwoods <https://github.com/johnalanwoods> - yes. The Payment ID
> is already used for that purpose - just looking at usage beyond an
> invoice/account ID.
>
> Simple Example Use Case: Proof of Existence for electronic file.
>
> A billionaire banker and a Monero user agree to a single bet on whether
> the price of Bitcoin will go below $1000 within 1 year; this physical piece
> of paper gets signed by both of them. This physical agreement is scanned
> and both of them get the scanned file. The Monero user wants to ensure
> further evidence of this agreement's existence. He calculates the SHA256
> sum of the scanned file and sends the smallest amount of Monero to a
> reputable, widely published standard Monero public address which has a
> widely published secret view key; in his Payment ID he pastes the SHA256
> sum of the scanned file. (If all Base64 characters were allowed he could
> truncate the SHA256 sum and use 20 characters to further link the document
> to the billionaire banker; or use all 64 characters for a SHA384 sum). Once
> the transaction is sent, anyone can use the reputable and widely published
> secret view key to see that SHA256 evidence in the Payment ID for the
> transaction. The Monero user can prove they were the sender of the
> transaction using the Prove/Check features in the GUI wallet and has
> documented the existence of that electronic file as of that tx on-chain.
>
> —
> You are receiving this because you commented.
> Reply to this email directly, view it on GitHub
> <https://github.com/monero-project/monero/issues/3772#issuecomment-387428685>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/AD6u2c2-vJ-2DFXMmLOGWoxutoGRUnGMks5twbBsgaJpZM4T1UYu>
> .
>


## phillipsjk | 2018-05-08T15:09:20+00:00
@burnssos A digital notary would probably work better on Bitcoin Cash, using OP_RETURN transactions. The notary can be implicitly identified by the pseudonymous payment address that they use.

The marginal cost for such transactions is around 3mills/kB (dominated by bandwidth costs).

## burnssos | 2018-05-08T16:15:22+00:00
@sneurlax I had been unsuccessful in my attempts to mine testnet coins. Can anyone send some? Testnet xmr coins: A1uf3TSf2UzJZPMWHqZ6Qu4HDeiecVjTM5vFuZZeLD2igtXLbBnV1KKHRsaUTg4iBXdsQsvX5Z8oyDnreqBbpKz3PZumiPo

## janowitz | 2018-05-08T18:21:56+00:00
@burnssos Monero has never had the use case to actually store data beside transactional one and any freely generated data has also a downside when it comes to censorship resistance. We already have seen religious stuff on the Bitcoin blockchain in the past and I don't actually think it should be there. If this method would get major adoption, it might get problematic just storing the blockchain in several jurisdictions.
When talking to Ethereum app developers lately, their main concern seems to be the new GDPR initiative since you have to delete personal user data on his request, but on a blockchain you probably will not be able to do so.

## Starmute | 2018-05-08T18:23:02+00:00
I believe it should still be possible to use the TX_EXTRA field to store data, just not pIDs. It’d make it a bit more roundabout, but I expect it would be the best of both worlds, discouraging legacy pID usage while still allowing limited information storage. It would be prudent to strongly limit this field though.

## burnssos | 2018-05-11T14:47:31+00:00
@phillipsjk As far I know on that BitcoinCash feature OP_RETURN, it reveals everything publicly on the blockchain. I believe the Monero PID (a de facto custom memo field) is significantly different as described below.

@janowitz I don't disagree that Monero has primarily been used only for transaction record keeping of Monero. As to "what is acceptable" on a blockchain should be immaterial if it has paid to be recorded - the blockchain record should be agnostic regardless of what laws any country demand, be they communist, democratic/republic, or EU oligarchy.

I am advocating to keep the potential of future opportunities which may not even be an idea yet. You can easily remove it from the GUI wallet UI and "upgrade" to only use integrated addresses for a large number of users by ignoring the field in the GUI wallet. But eliminating the PID would remove any future potential of alternate use cases not yet formulated.

I believe Monero is greatly undervalued in it's creation of the Spend Proof and its closest real world analogue would be a physical paper receipt for an in-person cash transaction. Someone who possesses the Digital Proof can provide evidence of high proximity to the transaction (i.e. appear as the transmitter), while not providing a signature (another undervalued XMR feature). If I buy something at a store with cash I receive proof I paid for those items with my receipt. If I give the receipt (e.g. Spend Proof) to someone else and they go back with the receipt + items for a store return, the transaction is not questioned and they receive the refund/credit even though they did not pay the store. Additionally, only the store and the receipt-holder (or anyone who directly copies the receipt/store records) have the list of items (e.g. PID) in the transaction because the store transactions are not a public record (e.g. transparent blockchain).

## dnaleor | 2018-05-12T17:19:59+00:00
@burnssos , there is a lesser known variant of proof of existance and you don't need OP_RETURN (for BTC) or paymentIDs (for XMR):

You can just hash your file and use it as a private (spend) key. For monero, then construct the view key based on that spend key (https://xmr.llcoins.net/addresstests.html) and send a very small payment to the address. When you reveal the private (spend) key [or sign a message with it], you prove that you created that transaction based on the hash of the file at a certain point in history.

edit: paymentid's (or any tx_extra use) can be an issue for fungiubility. I would like to see xmr transactions as similar as possible.

## dnaleor | 2018-05-12T17:29:57+00:00
@SamsungGalaxyPlayer I support this, but I guess we can even shorten the roadmap; it's just a user interface change. I agree, exchanges and other services will need to change their deposit systems, but if we don't do it "as fast as possible" I fear we'll need to keep supporting legacy systems because exchanges are lazy when they grow bigger. 

What do you think of this:

1) Upgrade the Monero FFS to use integrated addresses or subaddresses as soon as possible.

2) Remove support for sending with SPIs by **sep 2018** (**v8** protocol upgrade). _most exchanges are already using integrated addresses anyway_ + **rename integrated addresses in the GUI to "Legacy addresses"** + **remove support for generating an integrated address in the GUI** (maybe hide it behind an "legacy button" so individual users will stop using them to receive funds, but can still send funds to integrated addresses)

3) Remove support for integrated addresses (using subaddresses instead) by **March 2019** (**v9** protocol upgrade). _This means that the wallet won't automatically parse an integrated address. It'll always be possible in theory, but if the wallet doesn't do it automatically, it won't happen and exchanges will need to change to subaddresses_ 

Announce intent for these changes to be made as soon as consensus as reached.




## burnssos | 2018-05-12T17:39:07+00:00
@dnaleor Thank you for that, I didn't think of doing that.

@sneurlax (your post is not visible anymore) I don't intend to obstruct this, just offer a prospective which may not have been considered before everyone jumps in head first. With the upcoming launch of bulletproofs, I am looking at additional uses which may be feasible - I was trying to obtain testnet coins for that purpose. I work/learn better with experimentation vs reading the bulletproof paper.

## vtnerd | 2018-05-12T20:56:44+00:00
> @phillipsjk As far I know on that BitcoinCash feature OP_RETURN, it reveals everything publicly on the blockchain. I believe the Monero PID (a de facto custom memo field) is significantly different as described below.

The long-form payment id is not encrypted, and is of fixed length.

## burnssos | 2018-05-15T04:45:22+00:00
For Monero dev of these items, I support @dnaleor timeline. I want to say thanks to everyone for communicating with me on my tangent.

## LocalMonero | 2018-05-17T15:29:14+00:00
@dnaleor what is the purpose of removing support for integrated addresses? From the end-user standpoint the experience of sending to an integrated address or subaddress is the same. Are there any privacy/security implications of having integrated addresses around?

## dnaleor | 2018-05-17T15:38:24+00:00
There are privacy implications when people reuse integrated addresses because the paymentID will be the same. 

Also, it's just in general better to have all transactions look alike. So even if there wasn't reuse of integrated addresses, it would still be visible on chain that this particular transaction was send to an integrated address, which can limit the set of possible receivers to services like exchanges or payment processors who use integrated addresses in stead of subaddresses.

## stoffu | 2018-05-17T23:23:32+00:00
> There are privacy implications when people reuse integrated addresses because the paymentID will be the same.

This isn't true, the short payment ID in an integrated address is encrypted using ECDH, so the same pID will look differently each time.

The latter point is true. Having two kinds of txes, one with pID and the other without pID, could be utilized for analyzing the usage pattern on the blockchain. It's best to make all txes appear as uniform as possible.


## dnaleor | 2018-05-18T01:32:22+00:00
@stoffu Didn't know that, thanks!

But indeed, making every transaction look as similar as possible is important for fungibility.
 
[offtopic: Hence, I'm still a proponent of a fixed 2 output consensus rule and (to a lesser degree) a max 2 input consensus rule]

## wodebutterfly | 2018-05-31T07:52:11+00:00
Payment IDs are super not use-friendly. And it take OKEX almost half a year to get my XMR back as I forget to put the payment ID.

## iamsmooth | 2018-06-15T22:45:53+00:00
There is a (limited?) privacy implication with integrated address since the sender can always tell that base address is the same across transactions/customers even when the payment ID changes. So it is possible to identify all transactions from different customers going to the same exchange.

I don't know whether that matters much in practice, but it is different from subaddresses.


## dnaleor | 2018-08-06T08:29:49+00:00
Let me bump this again as well... Are there any plans to get at least rid of the SPI's in september? As I said before, we just need to disable UX support for it. Exchanges who still use it will be forced to upgrade. But it's not a consensus issue. 

## iamsmooth | 2018-08-08T13:06:59+00:00
I would be against removing it on such short notice. However, I would be in favor of making a change that makes it clear it is deprecated. For example, disable by default and require a non-default e.g.`--enable-deprecated-pid` option. Then removing it later, or further deprecating to a compile-time option (default binaries would not support it).

Non-backward-compatible charges should be made very cautiously and with long and conspicuous notice, but that doesn't mean they shouldn't be made.

## Gingeropolous | 2018-08-08T13:15:16+00:00
> --enable-deprecated-pid

so people would have to use that when loading the GUI? Or just the CLI / RPC wallet? 

Probably the first angle would be getting the service providers to stop using it, so putting it in the CLI / RPC makes the most sense. GUI users would have a hard time dealing with this. 

Yeah, I'd also support this move. 

## dnaleor | 2018-08-08T13:19:32+00:00
> I would be against removing it on such short notice. However, I would be in favor of making a change that makes it clear it is deprecated. 

Fine by me, as long as we're moving towards full deprecation. The longer we keep this stuff around, the harder it'll be to remove it eventually. As I said, in theory it'll always be possible to use paymentID's. It's not a consensus issue. 

## iamsmooth | 2018-08-08T13:22:02+00:00
> so people would have to use that when loading the GUI

Possibly, or it could be an advanced preference type setting, as long as it is off by default.

Alternately the GUI (and possibly CLI) could just generate a warning (for now, with the more intrusive steps to take place later). This can't really be done for the RPC wallet because there is no UI. 

## moneromooo-monero | 2018-08-15T11:21:42+00:00
Interestingly, there is https://github.com/monero-project/monero/pull/4109 which is relevant to this.

## coneiric | 2018-12-21T20:09:37+00:00
I'm in support of this. From what I understand, exchanges could get the same functionality out of subaddresses that they have with SPI, with some retooling to accounting practices (tagging subaddress accounts). It may even be easier to keep track of subaddresses, since the exchange can just tag all subaddresses associated with a given account with that user's info, not requiring the user to manually input a payment ID. Haven't run or worked for an exchange, so I could be wrong here.

I think a final push to draw attention to the issue, getting input from as many affected users/exchanges possible is a good idea.

## SamsungGalaxyPlayer | 2019-01-07T18:23:40+00:00
Update: we are looking to change the timeline somewhat. In the past several Monero Research Lab meeting discussions, it seems like all payment IDs, including unencrypted and encrypted payment IDs, will be disallowed in the **Fall 2019** upgrade. Here is a list of current services that use Monero payment IDs. Please contact them and encourage them to use subaddresses: https://www.irccloud.com/pastebin/Fh9N4WTY/

## bitlamas | 2019-01-07T21:04:28+00:00
> Please contact them and encourage them to use subaddresses

I think it's also a good moment to use the getmonero.org mailing list to preemptively announce the deprecation of the Payments IDs.

## SamsungGalaxyPlayer | 2019-02-28T16:55:22+00:00
After this discussion, several other discussions in #monero-research-lab, #monero-community, and #monero-dev, I created an address update schedule blog post [here](https://repo.getmonero.org/monero-project/monero-site/merge_requests/990).

Luigi commented in the merge request:

> I'm not going to merge [this post] at this time. In particular, I object to this line (and thus the whole MR I guess): "In it, the Monero community made clear its desire to move forward with its recommended timeline." The meeting logs show <20 people in attendance and record a poll, in which 8-ish people voted for 3, while several others dissented with reasons not adequately addressed, including issues from github (related note: a poll in this context is not authoritative).

Luigi feels that there is not enough Monero community support to pursue a September payment ID deprecation timeline. On IRC, he stated that he would like to see other exchanges upgrade first before going forward with this initiative.

I generally disagree for several reasons. The Monero community and Core Team have pursued many updates with a mandatory upgrade timeline even before any services had upgraded at all, including the much-larger RingCT upgrade. In nearly all of the relevant IRC discussions on payment ID deprecation, the community generally agreed that exchanges would not upgrade to subaddresses unless they are explicitly forced to. The other issues Luigi mentioned were discussed countless times in other meeting discussions, to the point that most people are sick about talking about it.

While I acknowledge that not everyone participated in these discussions and have been on board, I feel that we have done an appropriate job to involve many stakeholders. We sent out email notifications with instructions, this Github issue has been open for nearly a year, and IRC meeting conversations spoke about payment IDs in circles throughout December and January. The general consensus from these was that subaddresses do everything that payment IDs do, and that using subaddresses requires similar requirements to using Bitcoin HD wallets. If Luigi and the Core Team would like to receive more feedback on subaddresses, I encourage them to be clear what sort of feedback they are looking for and to create these platforms for discussion if they feel ones I create are inadequate.

I mentioned that the upgrade should be communicated and pursued, forcing exchanges and services to upgrade to the superior system. In the worst-case scenario if no one upgrades by the set timeline, Monero can silently delay the consensus change without any wasted effort. In the best case, we now have a better system. We shouldn't pretend we need to commit to failure at the agreed-upon deadline. We instead commit to evaluate the network at that time and determine if enough people have upgraded to proceed with the change, though the community intends to make the change if the community support is there.

## iamsmooth | 2019-03-01T06:28:22+00:00
> much-larger RingCT upgrade

The RingCT upgrade had little to no impact on terms of APIs and integration with back end software of Monero users.

There is a huge difference between that and breaking integration.

> discussed countless times in other meeting discussion

Meeting discussions are never going to be sufficient to address the serious concerns that arise when it comes to non-backward compatible API changes. Most people using the software and engaged in integration will not be attending the meetings. They won't be reading meeting minutes. They have their own businesses and business-specific problems to focus on.

I'll repeat what I said six months ago:

> Non-backward-compatible charges should be made very cautiously and with long and conspicuous notice, but that doesn't mean they shouldn't be made

The clock on this process has just started with the newly-released option required to enable these functions. When it comes to forced removal, I would ideally like to see a one to two year transition period, possibly more. This is a fairly standard pace when it comes to enterprise software, and even that may be a bit fast. There is no precedent for this in terms of Monero specifically, since nothing done to date has required not only significant API changes but significant _redesign_ of back end software that uses Monero.

If we aren't happy with the pace of voluntary upgrades on the network, we can encourage them with things like a weight/fee penalty that encourage upgrade/migration without hard-breaking anything.

## janowitz | 2019-03-01T10:30:50+00:00
> If we aren't happy with the pace of voluntary upgrades on the network, we can encourage them with things like a weight/fee penalty that encourage upgrade/migration without breaking anything.

This is key in my opinion and we should think about incentives for upgrading.

However, everyone knows that cryptocurrencies and their implementations are alpha, maybe at best beta versions so I think a 1-year schedule for depreciation would be enough, Monero is not a LTS version of its protocol or something similar.

## phillipsjk | 2019-03-01T17:29:47+00:00
I am just lurking, but think a 1 year time-frame is very aggressive, given the the software redisign the previous poster pointed out.

Maybe I am just annoyed because I have been cell-phone shopping; and Google considers 2 years LTS.

On Fri, Mar 01, 2019 at 02:31:03AM -0800, janowitz wrote:
> 
> However, everyone knows that cryptocurrencies and their implementations are alpha, maybe at best beta versions so I think a 1-year schedule for depreciation would be enough, Monero is not a LTS version of its protocol or something similar.


## SamsungGalaxyPlayer | 2019-03-03T19:28:45+00:00
Relevant portion from the dev meeting today, wherein a Kraken representative says that a 6 month timeline for subaddress-only (complete payment ID consensus ban) is generous as long as it is communicated clearly to everyone involved:

```
[2019-03-03 11:32:32] <rehrar> is needmoney90 around? He wanted this meeting and had something to say, as I recall
[2019-03-03 11:35:01] <needmoney90> Hey there
[2019-03-03 11:35:07] <rehrar> ^ this kid
[2019-03-03 11:35:16] <needmoney90> tat: you there?
[2019-03-03 11:35:38] <oneiric_> ...
[2019-03-03 11:36:25] <needmoney90> The kraken Dev was supposed to be here, but I may have missed mentioning it
[2019-03-03 11:36:49] <needmoney90> I believe they were all on board though
[2019-03-03 11:36:53] <needmoney90> After chatting
[2019-03-03 11:36:57] <needmoney90> So it may not be necessary
...
[2019-03-03 11:38:08] <tat> @needmoney90 i am here
[2019-03-03 11:38:25] <needmoney90> Oh perfect
[2019-03-03 11:38:40] <rehrar> ok, ceding the floor again to tat and needmoney90 real fast
[2019-03-03 11:39:11] <moneromooo> (I'll have one more point actually when they're done)
[2019-03-03 11:39:25] <needmoney90> Tat, for the logs, let's talk quickly about the timeline for payment ID deprecation, and Kraken's needs here
[2019-03-03 11:39:26] <rehrar> ok, sure
[2019-03-03 11:39:46] <needmoney90> Difficulty of implementation, how long you feel is reasonable before deprecating, etc
...
[2019-03-03 11:40:38] <needmoney90> We don't want to rush the deprecation, but improving privacy is one of our primary goals, and we cannot wait forever
[2019-03-03 11:41:46] <tat> well, i think going to deprecate them by the fork in october is very reasonable, and informing people about clear decisions 6 month ahead would be great also from a users perspective, to make the transformation as smooth as possible
[2019-03-03 11:42:40] <moneromooo> Is that about short or long ones ?
[2019-03-03 11:43:37] <tat> i will say both, if you guys go for that, either way, 6 month is a good window
[2019-03-03 11:43:54] <sarang> Also please be very clear about wallet deprecation vs something like a consensus ban
[2019-03-03 11:43:58] <rehrar> have you guys toyed with the idea of moving to subaddresses?
[2019-03-03 11:44:10] <sarang> The talk about _how_ to wallet-deprecate in GUI and CLI has also been more contentious than I had expected
[2019-03-03 11:44:36] <rbrunner> There is nothing else to move to, no?
[2019-03-03 11:44:41] <moneromooo> Long ones have been warned about since last fork in the wallet.
[2019-03-03 11:44:49] <moneromooo> So it's deprecated in my book :)
[2019-03-03 11:44:57] <moneromooo> So yes, clear definitions will help.
[2019-03-03 11:45:18] <sgp_> moneromooo: yes, long are "soft" non-consensus deprecated with the 0.14 update. Moreso than before
[2019-03-03 11:46:24] <sarang> Some argued that "deprecated" in GUI should mean "only available via a special flag or crazy advanced option", but others said it should mean "available by a simple toggle on a main page"
[2019-03-03 11:46:38] <sarang> IMO the latter option is not a deprecation at all
[2019-03-03 11:46:53] <sgp_> the latter is what MyMonero and others do
[2019-03-03 11:47:14] <moneromooo> Well, you can't run: firefox --long-payment-id-support so... :)
[2019-03-03 11:48:36] <fluffypony> not yet
[2019-03-03 11:48:49] <needmoney90> When Firefox partnership
[2019-03-03 11:49:08] <sarang> If it's easy to use, then we really haven't deprecated anything
...
[2019-03-03 11:49:15] <sarang> saying "plz don't use" is what we have already
...
[2019-03-03 11:49:50] <sgp_> sarang: I think we should focus on consensus deprecation. The other wallets are mostly out of our control
[2019-03-03 11:50:16] <sarang> I also support (at least temporary) consensus ban, but I know this is not a popular opinion
...
[2019-03-03 11:59:04] <sgp_> tat: can you speak to what the upgrade timeline for you to move to subaddresses looks like?
...
[2019-03-03 12:02:51] <tat> @sgp_ well i can't give you exact numbers, all i can say is that implementing it technically is not that hard, changing the address format has a couple of more processes involved and a 6 month timeline is what i think is very feaasable
...
[2019-03-03 12:04:26] <sgp_> tat: thanks, I really appreciate your perspective
[2019-03-03 12:04:47] <sgp_> Is there any additional documentation you wish was available?
[2019-03-03 12:05:29] <tat> @sgp_ i think you should keep in mind that address format changes are not only problematic for exchanges, you see the fuzz with your own wallets, it's a burden to the user and clear communication and transition is what will make a good change
[2019-03-03 12:06:00] <sgp_> yes, I'm trying to make the communication as clear as possible. I agree that is a hugely important goal
```

## iamsmooth | 2019-03-03T20:38:56+00:00
> wherein a Kraken representative says that a 6 month timeline is generous

That's fine _for them_. It is even quite possible someone else might do it in a week. The necessary time for a non-backwards compatible API change is the maximum necessary for every single API user (including those we don't know about) to learn about the change and make necessary changes to their own software, according to their own business processes and release schedule.

The cost of getting this wrong is not just breaking some systems once (possibly including dropping of Monero support in some marginal cases because the rework is not worth the revenue generated), it is future reluctance to integrate with or support Monero at all because it lacks trust in not aggressively making breaking changes. The most successful APIs almost never introduce non-backwards compatible changes, and when they do it is very carefully and slowly.

If you want to get rid of payment IDs on the network, penalize them with fees. The penalty can ramp up over time and become quite harsh.


# Action History
- Created by: SamsungGalaxyPlayer | 2018-05-07T17:13:21+00:00
- Closed at: 2024-02-15T18:13:52+00:00
