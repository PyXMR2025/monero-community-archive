---
title: 'Research meeting: 22 January 2020 @ 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/430
author: SarangNoether
assignees: []
labels: []
created_at: '2020-01-16T20:48:01+00:00'
updated_at: '2020-01-22T19:33:03+00:00'
type: issue
status: closed
closed_at: '2020-01-22T19:33:03+00:00'
---

# Original Description
Join in for the weekly Monero Research Lab meeting.

**When**: Wednesday, 22 January 2020 @ 18:00 UTC
**Where**: #monero-research-lab (freenode/matrix)

**Agenda**
1. Greetings

2. Roundtable

3. Questions

4. Action items

# Discussion History
## Mitchellpkt | 2020-01-20T23:02:28+00:00
Miscellaneous updates:

## Number of outputs on miner transaction
This is mostly a historical novelty from back in the days of denominated XMR - since RingCT became mandatory at block 1400000 all miner transactions have been 1OTXs. 
![image](https://user-images.githubusercontent.com/21246742/72751133-97aa0000-3b73-11ea-8723-7142b8aa928a.png)

## Miner transaction tx_extra
Wat? Everybody seems to use the miner_tx differently, including some really strange stuff like many blocks with 60 B of null padding(??!) [https://xmrchain.net/tx/7dfcc4e5d8bd772e3373e51d4140052121503d9b4f3cb6587251292bf06ced9a](https://xmrchain.net/tx/7dfcc4e5d8bd772e3373e51d4140052121503d9b4f3cb6587251292bf06ced9a)

There are some good reasons that mining pools use this for differentiating workers and whatnot, but perhaps we could standardize that? Right now everybody has their own ad hoc implementation in the extra field, so it might be safer to provide an actual space for that (perhaps supporting up to 100 billion workers per pool or something big enough that nobody has an excuse to circumvent). I'm not sure exactly what hooks should be built in, but I'm sure we could accommodate if we wanted to. Or even better, can the same technical requirements be accomplished off-chain or by dividing up the nonce range or something? **EDIT: since I posted this, logistics have been developed & discussed in Monero Research Lab**
<img width="814" alt="image" src="https://user-images.githubusercontent.com/21246742/72830799-5a5a7680-3c36-11ea-8b99-d932b667b135.png">
This has implications for privacy of all users. For example, I have a list of blocks mined by the pool that added 60 B null padding to each miner transaction. When this person creates multiple-input transactions to claim the reward, ring signatures offer them no protection. Multi input + miner fingerprint is statistically noisy, so we know when those outputs are really spent, and can rule them out as decoys in other transactions.

To avoid this, it's important that *any* implementation mimics the full hierarchy on any block. For example, if we accommodate {nonce, pool, proxy}, then every miner (including solo mining core software) should put random data in pool & proxy. Otherwise we've just made a fancier way to leave the same fingerprint. :-P

## Altruistic transaction selection
Another mostly historic novelty - altruistic transaction selection by miners who would include many/large transactions in their blocks, incurring a coinbase penalty that is not offset by the added fees. (In other words, they would have had a higher total block payout by mining an empty block.)

![image](https://user-images.githubusercontent.com/21246742/72751184-c031fa00-3b73-11ea-9150-938400080398.png)

![image](https://user-images.githubusercontent.com/21246742/72751248-fe2f1e00-3b73-11ea-9f6b-1cbc5b6daee3.png)


## Mitchellpkt | 2020-01-20T23:16:18+00:00
Oh, and for the encrypted + enforced unlock time, we have to decide on a format. Currently, 3 things are being put in the unlock field:
- Small integers like "12", presumably to be interpreted as height differences, i.e. "unlock in 12 blocks"
- Large integers like "1980000", presumably to be interpreted as block heights
- Very large integers like "1578561720", presumably to be interpreted as unix timestamps

While normally I'd be loathe to bring real world time onto the blockchain, I am inclined towards this approach: encrypted unlock time is a future timestamp recorded in unix seconds, and each ring must include a range proof comparing the unlock time to the oldest or youngest ring member (I haven't fully thought this through).

The minimum lock time of 10 is trivial for any outside observer/miner to enforce by delaying (or rejecting) transactions with rings containing members less than 10 blocks old. This requires no mathematical validation within the transaction.

The encrypted unlock time could actually be defined as `timestamp - 1500000000` to save a bit of space by removing the offset from some of time between 1970 and deployment, but that could be overengineering.

## hyc | 2020-01-21T02:53:33+00:00
Just to note that timestamps should be at least 40 bits or so, 32 bit timestamps roll over 18 years from now. (January 19 2038).

## UkoeHB | 2020-01-22T16:10:33+00:00
iirc the timestamp is a varint, so there are 56 bits available

## SarangNoether | 2020-01-22T19:33:03+00:00
    [2020-01-22 13:01:03] <sarang> GREETINGS
    [2020-01-22 13:02:26] <binaryFate> hi!
    [2020-01-22 13:02:28] <sgp_> hello
    [2020-01-22 13:02:39] <suraeNoether> Hi
    [2020-01-22 13:03:18] → kico joined (~kico@gateway/tor-sasl/kico)
    [2020-01-22 13:03:40] <koe> hiya
    [2020-01-22 13:04:04] <Isthmus> holla
    [2020-01-22 13:04:51] <sarang> Let's move to ROUNDTABLE
    [2020-01-22 13:05:02] <sarang> Isthmus: you posted some data on the agenda; care to discuss?
    [2020-01-22 13:05:14] <sarang> Link to data: https://github.com/monero-project/meta/issues/430#issuecomment-576455137
    [2020-01-22 13:05:28] <Isthmus> Sure
    [2020-01-22 13:05:47] <Isthmus> First, glanced at distribution of number of outputs on miner transactions
    [2020-01-22 13:05:59] <Isthmus> https://usercontent.irccloud-cdn.com/file/OB2UWpjs/image.png
    [2020-01-22 13:06:01] <Isthmus> This is mostly a historical novelty from back in the days of denominated XMR - since RingCT became mandatory at block 1400000 all miner transactions have been 1OTXs.
    [2020-01-22 13:06:12] <Isthmus> *single-output coinbase transactions
    [2020-01-22 13:06:49] <sarang> So that chart is for _all_ miner txns?
    [2020-01-22 13:06:53] <sarang> Throughout all of time?
    [2020-01-22 13:07:08] <Isthmus> From genesis block to last week
    [2020-01-22 13:07:24] <Isthmus> Courtesy of n3ptune's magic database xD
    [2020-01-22 13:07:39] → atoc joined (2fb9c5f1@47.185.197.241)
    [2020-01-22 13:07:56] → JamesNZ joined (~JamesNZ@fedora/JamesNZ)
    [2020-01-22 13:07:56] <Isthmus> Another mostly historic novelty - altruistic transaction selection by miners who would include many/large transactions in their blocks, incurring a coinbase penalty that is not offset by the added fees. (In other words, they would have had a higher total block payout by mining an empty block.)
    [2020-01-22 13:08:01] <Isthmus> https://usercontent.irccloud-cdn.com/file/0pcNROcT/image.png
    [2020-01-22 13:08:15] <Isthmus> color is size, starting at blue = small
    [2020-01-22 13:08:33] <Isthmus> This seems to not be a very common practice these days
    [2020-01-22 13:09:00] <Isthmus> Altruistic mining could be banned at the protocol level, but at the moment I'm not inclined to do so
    [2020-01-22 13:09:17] <koe> more advanced altruism based on suboptimal tx inclusion will involve more intensive analysis, which I provided pseudo code for this week, if that path is chosen
    [2020-01-22 13:09:25] <suraeNoether> Any comparison against partially filled blocks rather than empty blocks?
    [2020-01-22 13:09:39] <Isthmus> @koe yea do you want to jump in
    [2020-01-22 13:09:47] <sarang> Yeah koe please do
    [2020-01-22 13:10:04] — Isthmus has to get off the bus but will be back in 5ish minutes
    [2020-01-22 13:10:11] — Isthmus turns off bunsen burner and puts IRC away
    [2020-01-22 13:10:45] <sarang> koe: if you have a link to the pseudocode can you include it here?
    [2020-01-22 13:11:20] <koe> well this week I: made pseudo code for Isthmus blockchain analysis, deep proofreads of several ZtM chapters, talked with cohcho and jtgrassie about uniformity of coinbase tx
    [2020-01-22 13:12:00] <koe> more or less improved a roadmap of future monero developments: https://justpaste.it/5io6e which we can talk about some items
    [2020-01-22 13:12:26] <koe> latest ztm2 draft, I have honestly been pushing off multisig edits, but not making no progress https://www.pdf-archive.com/2020/01/22/zerotomoneromaster-v1-0-20/zerotomoneromaster-v1-0-20.pdf
    [2020-01-22 13:12:28] <sarang> Enforcement of exact block rewards seems straightforward and a good idea
    [2020-01-22 13:13:19] <koe> pseodo code https://paste.debian.net/1127152/
    [2020-01-22 13:13:39] <sarang> Regarding ZtM, are there topics in progress for which you'd like particular information or assistance?
    [2020-01-22 13:14:23] <koe> currently working on multisig, and have already gone through most documentation available, but there are some things that aren't clear despite documents
    [2020-01-22 13:14:38] <koe> so if anyone knows about multisig, Id like to discuss with them
    [2020-01-22 13:14:51] <koe> otherwise will dive into code base
    [2020-01-22 13:15:22] <suraeNoether> I'm not super familiar with the code base, but I'm familiar with what it's supposed to abstractly represent
    [2020-01-22 13:15:22] <sarang> Thanks koe
    [2020-01-22 13:15:40] <suraeNoether> So if you have questions koe about how things are supposed to work (as compared to how things are currently implemented)
    [2020-01-22 13:15:42] <suraeNoether> Lmk
    [2020-01-22 13:15:51] <koe> ok Ill hit you up
    [2020-01-22 13:16:32] <sarang> Anything else of interest to share koe? You've clearly been busy!
    [2020-01-22 13:18:29] <koe> well there are all the things in the roadmap, in particular enforcing 1 output from coinbase (since Isthmus found literally all coinbase for 4 years have been single output), and possibly enforcing single-type ring membership (only coinbase ring emmbers, only rcttypebulletproof2 ring members) since 99.5% of coinbase are owned by pools who are easy
    [2020-01-22 13:18:29] <koe> to fingerprint
    [2020-01-22 13:19:00] <sarang> Single-type enforcement was brought up a few times by sgp_ in the past as well
    [2020-01-22 13:19:09] <koe> see https://minexmr.com/pools.html where 99.5% of hash is accounted for
    [2020-01-22 13:19:26] <sarang> My concern was that a full segregation of coinbase outputs means certain heuristics are only moved "down chain" by a single hop
    [2020-01-22 13:19:43] <sarang> Meaning there's likely improvement for sure, but perhaps more marginal than desired
    [2020-01-22 13:19:46] → lithiumpt joined (~lithiumpt@152.89.162.252)
    [2020-01-22 13:20:33] <atoc> koe, do you still need proofreading of ZtM or are you good on that?
    [2020-01-22 13:21:02] <suraeNoether> I'm in favor of enforcing single output coonbase txns by consensus. I'm in favor of enforcing block reward. I'm tentaticely in favor of type-restricted rings.
    [2020-01-22 13:21:04] <koe> always need proofreading :)  even after it's published lmao, I've received some good emails that are incorporated in v2
    [2020-01-22 13:21:07] <sgp_> I actually was going to re-introduce the topic again here to keep it on everyone's minds, so nice timing
    [2020-01-22 13:21:27] <sgp_> related: https://medium.com/@JEhrenhofer/lets-stop-using-coinbase-outputs-da672ca75d43
    [2020-01-22 13:21:35] <atoc> koe, I am have some notes that I need to send you.
    [2020-01-22 13:21:43] <atoc> I will try to get them to you soon.
    [2020-01-22 13:21:53] <koe> ill look forward to them :)  (email me)
    [2020-01-22 13:22:16] <moneromooo> Enforcing single output coonbase txns would prevent p2pool.
    [2020-01-22 13:22:46] <atoc> will do :)
    [2020-01-22 13:22:53] <suraeNoether> Atoc, I believe that my mojojo branch is no longer bugging out, although data isn't being written to file how I want. The actual tracing game script I am running will be pushed soon(tm)
    [2020-01-22 13:23:01] <koe> jtgrassie is p2pool your project?
    [2020-01-22 13:23:15] <moneromooo> AFAIK nobody is doing it yet.
    [2020-01-22 13:23:40] <suraeNoether> But simulator is now successfully simulating a monero economy between Alice, Eve, and Bob to model flavors of EABE
    [2020-01-22 13:23:41] <atoc> cool suraeNoether I have been falling a bit behind and will catch up today and get you my thoughts
    [2020-01-22 13:23:50] <atoc> good to know the unit tests are working fine
    [2020-01-22 13:24:01] <atoc> Nice
    [2020-01-22 13:24:01] <suraeNoether> It's all good, I'll still be plugging away
    [2020-01-22 13:24:22] <sarang> Any other questions/comments for koe?
    [2020-01-22 13:24:47] <sgp_> no specific questions, but I have a related topic for mining pools besides coinbase outputs when time allows
    [2020-01-22 13:25:02] <sarang> OK, first, is Isthmus back? He had to step away briefly
    [2020-01-22 13:25:10] — Isthmus gets back
    [2020-01-22 13:25:19] <sarang> Isthmus: care to finish up your data?
    [2020-01-22 13:25:26] <Isthmus> Also, it's not "kicking the can down the road" depending on how you implement it
    [2020-01-22 13:25:28] <sarang> (then we can move to sgp_)
    [2020-01-22 13:25:28] <Isthmus> But yea, moving on
    [2020-01-22 13:25:43] <sarang> Hold on
    [2020-01-22 13:25:43] <Isthmus> Discovered that everybody seems to use the miner_tx differently, including some really strange stuff like many blocks with 60 B of null padding(??!) https://xmrchain.net/tx/7dfcc4e5d8bd772e3373e51d4140052121503d9b4f3cb6587251292bf06ced9a
    [2020-01-22 13:26:22] <sarang> Why would coinbase-only not do this?
    [2020-01-22 13:26:51] <sarang> If you assume the spend patterns would be sufficiently different, I agree
    [2020-01-22 13:27:06] <Isthmus> Uhm, I could get in the weeds with this
    [2020-01-22 13:27:20] <Isthmus> On like 4 levels
    [2020-01-22 13:27:21] <Isthmus> lol
    [2020-01-22 13:27:44] <Isthmus> From an *on chain* perspective, there's two questions we can ask
    [2020-01-22 13:28:20] <Isthmus> 1) Is this ring spending a coinbase
    [2020-01-22 13:28:22] <suraeNoether> \me pulls up lawn chair
    [2020-01-22 13:28:24] <Isthmus> 2) Which coinbase is this ring spending
    [2020-01-22 13:28:30] <Isthmus> #1 is hard to hide
    [2020-01-22 13:28:34] <Isthmus> #2 can be accomplished
    [2020-01-22 13:29:01] — Isthmus clarifies:
    [2020-01-22 13:29:05] <Isthmus> making #2 unanswerable can be accomplished
    [2020-01-22 13:29:10] <Isthmus> I'm an evil exchange
    [2020-01-22 13:29:21] <Isthmus> With current system, I can fingerprint which pools my users belong to
    [2020-01-22 13:29:54] <Isthmus> Aah ha, this person makes monthly deposits that are 4-input transactions each spending from a ring with 62  B null padding, so I know that they have about 3000 H/s attached to minexmr.com
    [2020-01-22 13:30:09] <Isthmus> *each spending from a coinbase whose miner tx_extra has...
    [2020-01-22 13:30:21] <Isthmus> But with coinbase-only txns, we strip the pool-to-user link
    [2020-01-22 13:30:38] <sarang> fair
    [2020-01-22 13:30:49] <Isthmus> Sure, as an exchange I can look at each user, and their average number of coinbases per ring
    [2020-01-22 13:30:58] <Isthmus> And if it's more coinbases per average I could suspect that they're a miner
    [2020-01-22 13:31:08] <Isthmus> But that's about all
    [2020-01-22 13:31:27] <sgp_> while there are some concerns with coinbase-only having only a layer of separation, I think the real benefits are being minimized slightly, especially to non-mining users
    [2020-01-22 13:31:35] <koe> also, coinbase is currently polluting normal tx rings, since a large proportion are identifiably spent/not spent
    [2020-01-22 13:32:12] <sarang> koe: the newer weighted selection algorithm does help this to an extent (relative only to tx weight, nothing else)
    [2020-01-22 13:32:36] <suraeNoether> One thing that is important about privacy is that third parties that have data like this are lawyer magnets. If an exchange couldn't possibly identify their mining user habits, they can't be hacked or subpoenaed to determine one of their customer's hash rates
    [2020-01-22 13:33:08] — Isthmus indicates agreement with last few comments
    [2020-01-22 13:33:39] <Isthmus> In my ideal world, we have 13 ring members and two selection algorithms. Precisely 11 of the members are non-coinbase, selected with current algorithm. Precisely 2 of the members are coinbase(/coinbase-only) that are selected independently.
    [2020-01-22 13:34:10] <sgp_> Isthmus: that would not be good for many reasons :)
    [2020-01-22 13:34:27] <sgp_> notably, you need a set of at least 3
    [2020-01-22 13:34:41] <Isthmus> Oh, I'm not married to the numbers
    [2020-01-22 13:34:47] <Isthmus> Just making an example
    [2020-01-22 13:35:36] <Isthmus> (trying to avoid the misconception that adjusting our coinbase ring member selection algorithm will somehow be zero-sum with the rest of the anonymity set or users)
    [2020-01-22 13:35:46] <nioc> koe: I know that rbrunner (sp) made an implementation of multisig so it might be good to speak with him.  I don't see him online now and haven't seen him for a little while but should still be around
    [2020-01-22 13:37:09] <koe> on the other hand, I wonder if enforced ring types is too much like reacting to how people use it; although the same could be said for many other protocol rules
    [2020-01-22 13:37:09] <sarang> Anyway, I derailed Isthmus's discussion of his other data with this topic...
    [2020-01-22 13:37:40] <Isthmus> Also, let M be the minimum plausible age between any output and it's temporally closest ancestor coinbase
    [2020-01-22 13:37:46] <Isthmus> :- P
    [2020-01-22 13:38:01] <Isthmus> That can either be a plotable feature, or fixed for all transactions at zero
    [2020-01-22 13:38:19] <koe> nioc ok Ill reach out
    [2020-01-22 13:38:58] <Isthmus> I think n3ptune and I may plot this for all outputs just to show the point
    [2020-01-22 13:39:27] <Isthmus> Other two things on the agenda - encrypted unlock time, and tx_extra in coinbases
    [2020-01-22 13:39:36] <Isthmus> I can get into these if people are interested
    [2020-01-22 13:39:38] <sarang> Sure, I saw your information about encrypted locks
    [2020-01-22 13:39:45] <sarang> (I also wish to address timelocks anyway_
    [2020-01-22 13:39:46] <sarang> )
    [2020-01-22 13:39:54] <Isthmus> Cool, lemme copypasta real quick
    [2020-01-22 13:39:56] <Isthmus> Oh, and for the encrypted + enforced unlock time, we have to decide on a format. Currently, 3 things are being put in the unlock field:
    [2020-01-22 13:40:01] <Isthmus> Small integers like "12", presumably to be interpreted as height differences, i.e. "unlock in 12 blocks"
    [2020-01-22 13:40:03] <Isthmus> Large integers like "1980000", presumably to be interpreted as block heights
    [2020-01-22 13:40:05] <Isthmus> Very large integers like "1578561720", presumably to be interpreted as unix timestamps
    [2020-01-22 13:40:08] <Isthmus> While normally I'd be loathe to bring real world time onto the blockchain, I am inclined towards this approach: encrypted unlock time is a future timestamp recorded in unix seconds, and each ring must include a range proof comparing the unlock time to the oldest or youngest ring member (I haven't fully thought this through).
    [2020-01-22 13:40:10] <Isthmus> The minimum lock time of 10 is trivial for any outside observer/miner to enforce by delaying (or rejecting) transactions with rings containing members less than 10 blocks old. This requires no mathematical validation within the transaction.
    [2020-01-22 13:40:12] <Isthmus> The encrypted unlock time could actually be defined as timestamp - 1500000000 to save a bit of space by removing the offset from some of time between 1970 and deployment, but that could be overengineering.
    [2020-01-22 13:40:18] — Isthmus hands the mic to sarang
    [2020-01-22 13:40:38] <sarang> We have a relatively efficient way to do encrypted timelocks, as introduced in DLSAG
    [2020-01-22 13:40:46] <moneromooo> Small integers are block heights. If you put 12 now, it's pointless.
    [2020-01-22 13:40:49] <suraeNoether> I'm 100% in support of encrypted lock times... I know that sarang has done some work into the requirements on that in addition to isthmus
    [2020-01-22 13:40:51] <sarang> The method is described here: https://github.com/SarangNoether/skunkworks/tree/timelock
    [2020-01-22 13:41:20] <sarang> It works as follows: outputs come equipped with a timelock Pedersen commitment (units aren't relevant for this at the moment)
    [2020-01-22 13:41:44] <Isthmus> "<moneromooo> Small integers are block heights. If you put 12 now, it's pointless."  Ahhahahaha that's what everybody is doing. Lemme make a plot real quick
    [2020-01-22 13:41:50] <sarang> Signatures come equipped with an auxiliary plaintext time that's chosen semi-at-random
    [2020-01-22 13:42:03] <sarang> as well as a particular auxiliary commitment
    [2020-01-22 13:42:29] <sarang> There is a range proof constructed using all these values, and CLSAG/MLSAG gets a new set of entries too
    [2020-01-22 13:42:37] → rottensox joined (~rottensox@unaffiliated/rottensox)
    [2020-01-22 13:42:55] <sarang> This maintains signer anonymity, shows the timelock has passed, but does not specifically reveal information about it
    [2020-01-22 13:43:23] <sarang> The cost for CLSAG is 1 new group element; the plaintext timelock is replaced by a plaintext intermediate value
    [2020-01-22 13:43:34] <sarang> and the auxiliary per-signature commitment is 1 new group element
    [2020-01-22 13:43:38] <binaryFate> does this mean the no-locktime transactions will be indistinguishable from locktime ones? Or just that the locktime ones will have an obfuscated time lock?
    [2020-01-22 13:43:48] <sarang> The rangeproofs can be worked into the existing bulletproofs, likely for free due to padding
    [2020-01-22 13:43:56] <Isthmus> Indistinguishable plz
    [2020-01-22 13:43:59] <sarang> Depends on how it's implemented
    [2020-01-22 13:44:32] <suraeNoether> indistinguishable would probably require no-locktime txns to have a dummy encrypted locktime
    [2020-01-22 13:44:38] <sarang> So the cost is 64 extra bytes per signature, and 32 bytes per extra timelocked output
    [2020-01-22 13:44:57] <sarang> Yep, you'd include zero locktime
    [2020-01-22 13:45:07] <sarang> and the rest of the process proceeds the same
    [2020-01-22 13:45:17] <sarang> So this is not free, but it's not terribly expensive either
    [2020-01-22 13:46:12] <sarang> Anyway, this information is to supplement what Isthmus brought up about how timelocks are handled now
    [2020-01-22 13:46:15] <binaryFate> It's completely offtopic but I personally like the idea that we can embed an arbitratry hash in a transaction in a way that is indistinguishable from other txs, for timestamping purposes.
    [2020-01-22 13:46:17] — sarang returns the mic to Isthmus
    [2020-01-22 13:46:33] <binaryFate> Would only be half or a quarter of a hash in that case though
    [2020-01-22 13:46:45] <binaryFate> (using the encrypted time lock field)
    [2020-01-22 13:47:20] <Isthmus> @binaryFate if we add an enforced encrypted memo field, that would be a very good use case
    [2020-01-22 13:47:24] <suraeNoether> binaryFate: well, you could always pick your txn key as the Hp of some message. is that not what you mean?
    [2020-01-22 13:47:54] <binaryFate> it works too, but require you don't lose your local storage.
    [2020-01-22 13:48:34] <suraeNoether> sure. you want to be able to extract the message also, something like that?
    [2020-01-22 13:49:31] <binaryFate> just exhibit the message later on and point out to a past hash in the blockchain that timestamps it, without people taking notice this was a timestamping tx.
    [2020-01-22 13:49:43] <binaryFate> but if you have message you can get hash back, so tx key works perfectly I guess
    [2020-01-22 13:49:50] <suraeNoether> oh neat
    [2020-01-22 13:49:59] <binaryFate> anyway, sorry to derail
    [2020-01-22 13:50:06] <sarang> Isthmus: take it away :)
    [2020-01-22 13:50:24] <Isthmus> Derailing conversation is a key part of research! :- D
    [2020-01-22 13:50:31] <Isthmus> I think that's where 2/3 of our interesting stuff comes from
    [2020-01-22 13:50:40] <suraeNoether> *nod* i prefer these lively research meetings for sure
    [2020-01-22 13:50:52] <Isthmus> Anyways, last topic I had has been discussed significantly since I initially mentioned it. So I'll intro and then duck out of the way
    [2020-01-22 13:50:52] <sarang> You had some notes, Isthmus, on how timestamps are represented
    [2020-01-22 13:50:53] <Isthmus> https://usercontent.irccloud-cdn.com/file/Ovp9yP0j/image.png
    [2020-01-22 13:50:57] <sgp_> I will most likely need to take off, so I'll bring up my other mining pool ring signature proposal (which I mentioned in the past) when I get back
    [2020-01-22 13:51:18] <atoc> @isthmus agreed, it seems that new ideas fluster that way.
    [2020-01-22 13:51:41] <Isthmus> Oh go @sgp_
    [2020-01-22 13:51:51] <sgp_> ah, so very fast
    [2020-01-22 13:52:22] <sgp_> there are special ways we can construct rings for public mining pools to protect the "integrity" of outputs (make it no longer publicly known what transactions they are spent in)
    [2020-01-22 13:52:47] <sgp_> for public mining pools that share transaction histories, it's clear which outputs are change outputs, which are later spent by the pools
    [2020-01-22 13:53:13] <sgp_> to avoid this, public pools can select rings using exclusively decoys that they create as payments to miners
    [2020-01-22 13:53:51] <sgp_> that way, outsiders have no way to distinguish the output from the other outputs given to miners. saves one output per payment, per public pool
    [2020-01-22 13:54:28] <sgp_> this is not a consensus change, but it would require a separate "public pool selection mode" or similar
    [2020-01-22 13:54:37] — Isthmus coughs *could be consensus*
    [2020-01-22 13:55:08] <sgp_> Isthmus: how? payouts won't be from coinbase outputs
    [2020-01-22 13:55:16] — Isthmus re-reads
    [2020-01-22 13:55:37] <Isthmus> Aah, maybe I was thinking of something slightly different
    [2020-01-22 13:55:39] <Isthmus> Carry on :- )
    [2020-01-22 13:55:48] <sgp_> this protects pool change outputs from being known as spent by the pool in specific transactions
    [2020-01-22 13:56:06] <sgp_> that's about it, just wanting to make sure this idea is resurrected, since I introduced it nearly 2 years ago now
    [2020-01-22 13:56:36] <sarang> Thanks sgp_
    [2020-01-22 13:56:43] <sarang> In the interest of time, Isthmus please go ahead!
    [2020-01-22 13:57:55] — Isthmus recaps:
    [2020-01-22 13:58:04] <Isthmus> Everybody seems to use the miner_tx differently, including some really strange stuff like many blocks with 60 B of null padding(??!) https://xmrchain.net/tx/7dfcc4e5d8bd772e3373e51d4140052121503d9b4f3cb6587251292bf06ced9a
    [2020-01-22 13:58:11] <Isthmus> https://usercontent.irccloud-cdn.com/file/tXHruCE0/image.png
    [2020-01-22 13:58:15] <Isthmus>  This has implications for privacy of all users. For example, I have a list of blocks mined by the pool that added 60 B null padding to each miner transaction. When this person creates multiple-input transactions to claim the reward, ring signatures offer them no protection.
    [2020-01-22 13:58:19] <Isthmus> (Multi input + miner fingerprint is statistically noisy, so we know when those outputs are really spent, and can rule them out as decoys in other transactions.)
    [2020-01-22 13:58:29] <Isthmus> To avoid fingerprinting, it's important that any implementation mimics the full hierarchy on any block. For example, if we accommodate {nonce, pool, proxy}, then every miner (including solo mining core software) should put random data in pool & proxy. Otherwise we've just made a fancier way to leave the same fingerprint. :-P
    [2020-01-22 13:58:44] <Isthmus> Anyways, others in this room have made a lot of progress on how to address this, so I'll let them jump in
    [2020-01-22 14:00:30] <sarang> Anyone have anything to add in particular to this?
    [2020-01-22 14:00:59] <suraeNoether> nope, but I have to get going
    [2020-01-22 14:01:08] <sarang> OK, suraeNoether: any brief update before you go?
    [2020-01-22 14:01:12] <sarang> Otherwise, no worries
    [2020-01-22 14:01:13] <koe> sarang is this the encrypted timelock? https://justpaste.it/2754y
    [2020-01-22 14:02:22] <suraeNoether> just that sarang and i have been having some extremely deep discussions about unforgeability in CLSAG and the crappiness of linkability models... we are nearing some very valuable improvements to d-CLSAG as written...
    [2020-01-22 14:02:51] <suraeNoether> i'll let him describe more; i've also gotten my matching simulations (apparently) working correctly on my matching-mojojo branch of mrl-skunkworks
    [2020-01-22 14:02:54] <suraeNoether> other than that, i have to get going
    [2020-01-22 14:02:59] <suraeNoether> sorry :(
    [2020-01-22 14:03:04] <suraeNoether> i'll drop in later today for more of an update
    [2020-01-22 14:03:39] <sarang> koe: you include the auxiliary timestamp in the signature's extra commitment in the model I worked up
    [2020-01-22 14:03:53] <sarang> Isthmus: anything else that you hoped to share?
    [2020-01-22 14:04:06] <sarang> (sorry, trying to ensure everyone gets a chance to finish their presentations)
    [2020-01-22 14:04:59] <Isthmus> Thanks, I'm outta new material
    [2020-01-22 14:05:04] <sarang> OK, thanks Isthmus
    [2020-01-22 14:05:47] <sarang> I worked up some stuff on timelocks (shared earlier), did a blag post with sgp_ relating to supply auditing (to answer questions that often come up), and got into the weeds on security models relating to linkability
    [2020-01-22 14:06:16] <sarang> Linkability meaning the formal definition used in linkable ring signatures, not any particular transaction linking
    [2020-01-22 14:06:34] <sarang> koe: what you have may be algebraically equivalent; I'll take a look shortly
    [2020-01-22 14:06:44] <sarang> OK, did anyone else have something to share that was missed?
    [2020-01-22 14:06:51] <sarang> So many things to discuss today!
    [2020-01-22 14:07:38] <koe> well does anyone have thoughts on enforced sorted TLV format for the extra field? I have spammed up the channel a bit recently, with that topic
    [2020-01-22 14:08:12] <sarang> Can you recap the benefits and tradeoffs briefly, for those who didn't see the earlier discussion?
    [2020-01-22 14:08:20] <moneromooo> If someone wants to stuff some random data in there, it's as visible as now, no ?
    [2020-01-22 14:08:21] <koe> and pursuing coinbase extra field standardization by seeking an inter-pool committe
    [2020-01-22 14:08:35] <sarang> (note that monerologs.net has logs of this and other channels available)
    [2020-01-22 14:08:39] <moneromooo> What's an inter-pool commite ?
    [2020-01-22 14:08:50] <koe> committee between pools
    [2020-01-22 14:08:57] <koe> composed of
    [2020-01-22 14:09:06] <moneromooo> Oh you mean just talk to pool ops ?
    [2020-01-22 14:09:12] <koe> lol yeah
    [2020-01-22 14:09:16] ⇐ atoc quit (2fb9c5f1@47.185.197.241): Remote host closed the connection
    [2020-01-22 14:09:44] <koe> these things are called standardization committees in industry
    [2020-01-22 14:10:02] → atoc joined (2fb9c5f1@47.185.197.241)
    [2020-01-22 14:10:57] ⇐ ferretinjapan quit (ferretinja@gateway/vpn/privateinternetaccess/ferretinjapan): Ping timeout: 268 seconds
    [2020-01-22 14:13:32] <koe> benefits of enforced sorted TLV + guidelines for use: a) makes sure all implementations are using the same essential format for constructing extra fields, since without guidelines or structure each implementation is ad hoc; b) for those who are privacy minded, there will be a clear way to blend in with other like minded implementers (for example,
    [2020-01-22 14:13:33] <koe> who knew that the code base sorts field entries, but at least one live implementation does not?); c) leaves extra field almost as open ended as it is now, so those who choose opt-out privacy (choose to stand out from the crowd) for whatever reason, can still do so trivially
    [2020-01-22 14:14:17] <sarang> In the earlier discussions, were there particular opinions opposed to it?
    [2020-01-22 14:14:23] <sarang> If so, why?
    [2020-01-22 14:15:17] → ferretinjapan joined (ferretinja@gateway/vpn/privateinternetaccess/ferretinjapan)
    [2020-01-22 14:15:59] <koe> tradeoffs: a) it may have limited real impact on transaction indistinguishability, especially among coinbase tx if most pool operators aren't on board; b) implies no stricter enforcement of the field will be pursued (which would directly address questions of indistinguishability; c) so far as coinbase tx go, many pools publish their mined blocks
    [2020-01-22 14:15:59] <koe> (counter argument is Monero development is focused on on-chain, and can't concern too much off-chain activity)
    [2020-01-22 14:16:27] <sarang> Noted; thanks
    [2020-01-22 14:16:45] <sarang> Since you were interested also in the hidden timelock construction, any other thoughts on that as well (from your link above)
    [2020-01-22 14:17:18] <koe> actually I just felt inspired, and wanted to confirm my understanding
    [2020-01-22 14:17:21] <sarang> Keeping in mind that the range proof can be absorbed into the existing one, meaning no effective change in size or verification for that portion of it
    [2020-01-22 14:17:31] <sarang> Your construction appears algebraically equivalent to what I listed
    [2020-01-22 14:17:46] <koe> I dont know enough about CLSAG to make a real judgement
    [2020-01-22 14:17:54] <sarang> The CLSAG part could apply to MLSAG as well
    [2020-01-22 14:18:01] <koe> Perhaps if we knew how much timelock is being used in the wild
    [2020-01-22 14:18:07] <sarang> The only difference is how the commitment to zero is handled in the signature
    [2020-01-22 14:18:37] <sarang> In MLSAG it would be _very_ expensive, but in CLSAG it adds only a single auxiliary linking tag, and makes the verification multiexp a bit more expensive
    [2020-01-22 14:18:54] <koe> oh nice, I was imagining all those extra mlsag scalars
    [2020-01-22 14:18:55] <sarang> If people think it's worth seriously considering, I can get more precise timing estimates on those curve operations
    [2020-01-22 14:19:03] <sarang> Yeah, for CLSAG you don't add scalars
    [2020-01-22 14:19:25] <sarang> It is in no way worth it for MLSAG
    [2020-01-22 14:19:30] <sarang> either in size or extra verification
    [2020-01-22 14:20:05] <sarang> The current CLSAG data has some custom curve-op code for efficiency that wouldn't apply to this new 3-CLSAG timelock construction
    [2020-01-22 14:20:13] <sarang> (the Python code is not suitable for timing, only to see how it works)
    [2020-01-22 14:20:46] <sarang> Anyway
    [2020-01-22 14:20:48] <sarang> We're way over time
    [2020-01-22 14:20:55] <sarang> Anyone have ACTION ITEMS for this week they want to share?
    [2020-01-22 14:21:08] <sarang> (I find action items useful for me, to help prioritize and share those priorities)
    [2020-01-22 14:21:29] ← koe left (4ba8fbe3@75-168-251-227.mpls.qwest.net): 
    [2020-01-22 14:21:30] <atoc> I will continue working with Surae. Hopefully I can share more next week.
    [2020-01-22 14:21:36] → koe joined (4ba8fbe3@75-168-251-227.mpls.qwest.net)
    [2020-01-22 14:21:52] <sarang> I have several... some additional work writing up comparisons of linkability definitions between a few papers, to get some timelock numbers (if it's seen as useful), and some data analysis relating to sublinear protocols
    [2020-01-22 14:22:04] <sarang> Oh, and one additional note... the IEEE S&B conference is coming up later this year
    [2020-01-22 14:22:10] <sarang> https://ieeesb.org/
    [2020-01-22 14:22:22] <sarang> Both suraeNoether and I are on the program committee
    [2020-01-22 14:22:29] <sarang> It's a great event, and is seeking papers
    [2020-01-22 14:22:40] <sarang> If you have some work that could be worth sharing, consider writing it up formally and submitting
    [2020-01-22 14:22:50] <atoc> Ok cool
    [2020-01-22 14:22:54] <sarang> (you should note any conflicts of interest with the program committee if you feel they apply to you)
    [2020-01-22 14:23:24] <sarang> I went to this event a while back, and it had great presentations (but was not streamed)
    [2020-01-22 14:23:32] <sarang> Any other comments, questions, or final remarks before we adjourn?
    [2020-01-22 14:23:44] <sarang> Normally there isn't so much to cover in one meeting; it's a great problem to have :D
    [2020-01-22 14:24:02] <sarang> Going once...
    [2020-01-22 14:24:20] <sarang> going twice...
    [2020-01-22 14:24:29] <koe> I will be focusing on ZtM2 multisig, which may be done by next meeting in which case Ill start in on bulletproofs; and anything else that comes up, perhaps work on updating the fee priority multipliers for surge situations (emails with ArticMine)
    [2020-01-22 14:24:40] <atoc> Last thing, I didn't realize IEE had Security and Privacy on Blockchain. That's pretty cool.
    [2020-01-22 14:24:49] <sarang> I'm happy to help with bulletproofs koe; I have a branch for it in my ZtM repo
    [2020-01-22 14:24:58] <sarang> atoc: it's a great event
    [2020-01-22 14:25:00] <koe> all in good time :)
    [2020-01-22 14:25:08] <sarang> I'm very happy to be asked to be on the committee :)
    [2020-01-22 14:25:26] <sarang> OK, thanks to everyone for attending, even though we went over the usual time
    [2020-01-22 14:25:27] <atoc> Yeah that's awesome!
    [2020-01-22 14:25:32] <sarang> Logs will be posted shortly to the GitHub issue
    [2020-01-22 14:25:38] <atoc> It was good. There was a lot of material.
    [2020-01-22 14:25:38] <sarang> Discussion can of course continue
    [2020-01-22 14:25:52] <sarang> (I just need a stopping point for the posted logs!)


# Action History
- Created by: SarangNoether | 2020-01-16T20:48:01+00:00
- Closed at: 2020-01-22T19:33:03+00:00
