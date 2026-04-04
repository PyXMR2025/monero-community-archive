---
title: 'Research meeting: 1 April 2020 @ 17:00 UTC'
source_url: https://github.com/monero-project/meta/issues/451
author: SarangNoether
assignees: []
labels: []
created_at: '2020-03-27T15:15:43+00:00'
updated_at: '2020-04-01T18:06:01+00:00'
type: issue
status: closed
closed_at: '2020-04-01T18:06:01+00:00'
---

# Original Description
Join in for the weekly Monero Research Lab meeting.

**When**: Wednesday, 1 April 2020 @ 17:00 UTC
**Where**: #monero-research-lab (freenode/matrix)

**Agenda**
1. Greetings

2. Roundtable

3. Questions

4. Action items

# Discussion History
## Mitchellpkt | 2020-04-01T17:06:01+00:00
<img width="951" alt="image" src="https://user-images.githubusercontent.com/21246742/78165574-c14f9500-7408-11ea-8ae5-7d695b4321d3.png">


## SarangNoether | 2020-04-01T18:06:01+00:00
    [2020-04-01 12:58:50] <sarang> GREETINGS
    [2020-04-01 12:59:01] <ArticMine> Hi
    [2020-04-01 13:00:19] — sarang will wait a few moments
    [2020-04-01 13:00:19] → adhux0x0f0x3f-- joined (~adhux0x0f@gateway/tor-sasl/adhux0x0f0x3f)
    [2020-04-01 13:00:50] ⇐ rubdos quit (~rubdos@77.109.103.196): Remote host closed the connection
    [2020-04-01 13:02:23] ⇐ adhux0x0f0x3f quit (~adhux0x0f@gateway/tor-sasl/adhux0x0f0x3f): Ping timeout: 240 seconds
    [2020-04-01 13:02:39] <Isthmus> Heya
    [2020-04-01 13:02:48] <Isthmus> Sorry I fell asleep last week
    [2020-04-01 13:02:57] <sarang> I'm feeling a bit under the weather today, so I'll try to keep things short and sweet if possible
    [2020-04-01 13:03:01] <sarang> No problem Isthmus
    [2020-04-01 13:03:06] <sarang> Let's move on to ROUNDTABLE
    [2020-04-01 13:03:16] <sarang> My list is short but hopefully interesting
    [2020-04-01 13:03:26] <sarang> The CLSAG preprint has been revised and updated on the IACR archive
    [2020-04-01 13:03:38] <sarang> Link: https://eprint.iacr.org/2019/654
    [2020-04-01 13:03:47] <sarang> New security model and proofs
    [2020-04-01 13:04:06] <UkoeHB_> Oh hi forgot about this :p
    [2020-04-01 13:04:20] <sarang> Alongside this, the code has been updated to make it easier to include trezor/ledger support
    [2020-04-01 13:04:50] → atoc joined (2fb9e984@47.185.233.132)
    [2020-04-01 13:04:58] <sarang> Plumbing for device support: https://github.com/SarangNoether/monero/commit/94a7daad0f53074a28dbfb39c0ed1d68d5c40e86
    [2020-04-01 13:05:16] <sarang> Support for ledger, courtesy of cslashm: https://github.com/SarangNoether/monero/pull/1
    [2020-04-01 13:06:03] <sarang> Smaller items are proofreading for UkoeHB_'s Zero to Monero update, and finalizing a PR for hash function domain separation, along with the usual literature review
    [2020-04-01 13:06:18] <sarang> Does anyone have particular questions, or otherwise have research of interest to share?
    [2020-04-01 13:07:15] <sarang> I see that Isthmus has just added to the agenda issue
    [2020-04-01 13:07:28] <Isthmus> https://user-images.githubusercontent.com/21246742/78165574-c14f9500-7408-11ea-8ae5-7d695b4321d3.png
    [2020-04-01 13:08:17] <Isthmus> n3ptune and I have been exploring tx_extra some more
    [2020-04-01 13:08:28] <sarang> neat
    [2020-04-01 13:08:33] <Isthmus> A few months ago @UkoeHB_ suggested that the *ordering* of tags might leak some information
    [2020-04-01 13:08:39] <Isthmus> This intuition turned out to be correct
    [2020-04-01 13:09:03] → rubdos joined (~rubdos@77.109.103.196)
    [2020-04-01 13:09:33] <n3ptune> link to the issue: https://github.com/monero-project/research-lab/issues/61
    [2020-04-01 13:10:04] <Isthmus> If we look at tx_extra in the wild since 1978433 (v12) we see 8 different ways that tags are assembled
    [2020-04-01 13:11:05] <sarang> Enforcing an ordering and certain fields makes sense for uniformity; I wonder what the added time complexity would be for parsing overall
    [2020-04-01 13:11:43] <sarang> This also ties in with an idea for Janus mitigation, which would enforce a per-transaction Janus transaction key and per-output tx pubkeys
    [2020-04-01 13:11:58] <Isthmus> +1
    [2020-04-01 13:12:11] <sarang> And, FWIW, there was a PR yesterday from moneromooo with an idea for an encrypted-memo-type addition to extra: https://github.com/monero-project/monero/pull/6410
    [2020-04-01 13:12:16] <sarang> (I have concerns about that one)
    [2020-04-01 13:13:28] <Isthmus> I would support encrypted memo if *length* and *inclusion* enforced in protocol. :- )
    [2020-04-01 13:14:00] <Isthmus> Zcash has a 512 byte encrypted memo on all z2z transactions, and people are having a lot of fun with it
    [2020-04-01 13:14:21] <Isthmus> (mostly whimsical fun at the moment, but I expect fun applications to follow)
    [2020-04-01 13:14:22] <sarang> Of course, this seems to overlap in functionality somewhat with encrypted pIDs
    [2020-04-01 13:14:40] <Isthmus> Oh yea, could just roll the PID into the memo
    [2020-04-01 13:14:55] <sarang> But yes, I agree that if included, length should be enforced for uniformity
    [2020-04-01 13:15:03] <Isthmus> Would it be per txn or per output?
    [2020-04-01 13:15:10] <UkoeHB_> Im a bit skeptical about scope creep, since Monero is money, not random messages
    [2020-04-01 13:15:11] <ArticMine> and kept small
    [2020-04-01 13:15:26] <UkoeHB_> or email
    [2020-04-01 13:16:06] <ArticMine> or a replacement for twitter
    [2020-04-01 13:16:44] <sarang> AIUI that PR requires a single non-change output
    [2020-04-01 13:16:50] <sarang> at least from my initial read of the code
    [2020-04-01 13:17:45] <sarang> Its use in Zcash is per-output, I believe
    [2020-04-01 13:18:11] <ArticMine> Can we actually do away with this messaging entirely?
    [2020-04-01 13:18:19] <sarang> ?
    [2020-04-01 13:18:21] <UkoeHB_> Isthmus's research indicates that even though the extra field is technically open ended, in practice people arent implementing random things
    [2020-04-01 13:18:43] <UkoeHB_> supporting random messages with core code would directly lead to more random things in the chain
    [2020-04-01 13:18:54] <Isthmus> Wait can we clarify "random"
    [2020-04-01 13:19:01] → netrik182[m] joined (netrik182m@gateway/shell/matrix.org/x-tgaxdzxchqwtakgj)
    [2020-04-01 13:19:03] <Isthmus> Do we mean a fixed tag that supports arbitrary payload
    [2020-04-01 13:19:03] <UkoeHB_> non-standard
    [2020-04-01 13:20:05] <UkoeHB_> I guess 'memo field' implies to me 'any random message you feel like'
    [2020-04-01 13:20:37] <Isthmus> Ideally encrypted
    [2020-04-01 13:20:51] <sarang> To clarify, this PR uses chacha to encrypt with the DH shared secret, including padding as needed to hit certain size resolution
    [2020-04-01 13:20:54] ⇐ rubdos quit (~rubdos@77.109.103.196): Remote host closed the connection
    [2020-04-01 13:20:58] <atoc> what are pros of including memo field?
    [2020-04-01 13:21:10] <sarang> but it's not possible to enforce that the data are actually encrypted
    [2020-04-01 13:21:31] <UkoeHB_> does chacha index each chunk in some way (so no two chunks are likely to be the same)?
    [2020-04-01 13:21:36] <ArticMine> That is my question
    [2020-04-01 13:21:39] <sarang> I think the goal was to enable encrypted recipient data as desired, to reduce the likelihood of non-standard inclusion of data in extra
    [2020-04-01 13:21:58] <sarang> UkoeHB_: the chunks are appended before passing to chacha
    [2020-04-01 13:22:14] <sarang> If I'm reading the PR correctly, the chunking is just to enforce size resolution
    [2020-04-01 13:22:23] <Isthmus> From a technical/statistical info leak standpoint, we should either have *no* messages, or an encrypted message on *every* transactions. Which option we choose is partially a UX/design conversation.
    [2020-04-01 13:22:47] <sarang> And at that point, you basically have a larger pID setup
    [2020-04-01 13:22:56] <Isthmus> Yea
    [2020-04-01 13:23:05] <sarang> Which was part of my concern
    [2020-04-01 13:23:11] <Isthmus> Is there no way to mathematically verify that a field is encrypted?
    [2020-04-01 13:23:47] <sarang> Not for the network AFAIK
    [2020-04-01 13:23:58] <sarang> Nor is it possible in Zcash either
    [2020-04-01 13:24:16] <sarang> It is possible to assure the _recipient_ that if they can decrypt properly, the data were encrypted as expected
    [2020-04-01 13:24:17] → rubdos joined (~rubdos@77.109.103.196)
    [2020-04-01 13:24:30] <Isthmus> Ohhh yea that's how that works
    [2020-04-01 13:24:41] <sarang> But otherwise, it's just uniformly distributed data
    [2020-04-01 13:25:14] <UkoeHB_> I think that encryption or not isn't a concern, since implementers should want to harmonize with other implementations. The core impl would encrypt, so others would too
    [2020-04-01 13:25:17] <ArticMine> All of this begs the question do we need this memo filed and even extra
    [2020-04-01 13:25:23] <sarang> So the worst case in Zcash is that you throw a bunch of unencrypted junk into a tx that gets accepted by the network, but that the recipient won't properly decrypt
    [2020-04-01 13:25:50] <Isthmus> " All of this begs the question do we need this memo filed and even extra" < I would be very happy to do away with both
    [2020-04-01 13:26:04] <UkoeHB_> ArticMine: I think ultimately the extra field is useful when/if hard forks are no longer feasible.
    [2020-04-01 13:26:27] <sarang> At the very least, enforcing ordering as UkoeHB_ listed in their issue would help a lot of this
    [2020-04-01 13:26:41] <sarang> certainly not all cases though
    [2020-04-01 13:26:51] <UkoeHB_> Imagine if Janus attack wasn't discovered until after hard forks stopped happening. We'd be in Bitcoin's situation of absolute chaos
    [2020-04-01 13:27:39] <UkoeHB_> (i.e. if no extra field for wiggle room)
    [2020-04-01 13:27:40] <ArticMine> How would extra help
    [2020-04-01 13:27:54] <Isthmus> Geez, if that happened I think the issue is ossification
    [2020-04-01 13:28:17] <UkoeHB_> wallets can implement janus mitigation on their own, since it's technically unverifiable anyway
    [2020-04-01 13:29:06] <Isthmus> I'd like to proactively avoid a situation like that by keeping an agile codebase, not having an anything-goes tx_extra field
    [2020-04-01 13:31:06] <Isthmus> Anyways, lots of different pros & cons to consider for each possibility
    [2020-04-01 13:35:00] <sarang> The question at this point, I think, is to decide whether doing order enforcement (e.g. TLV) is something that a develop wishes to take on
    [2020-04-01 13:35:25] <sarang> Which ties in to whether enforcement of a consistent Janus mitigation is desirable (I think yes, it is)
    [2020-04-01 13:35:30] <UkoeHB_> After next gen tx protocol gets implemented, I imagine the stuff that can go in a hard fork will drop off quite a bit. Rather than losing the ability to make hard forks, we might just run out of hard forks to make. Once the expectation of making periodic hard forks fades away, subsequent hard forks will become much more difficult (also the case if adoption rises concurrently).
    [2020-04-01 13:35:55] <sarang> Network upgrades also have the probable advantage of encouraging client upgrades
    [2020-04-01 13:36:08] <Isthmus> Yeah "we might just run out of hard forks to make" is a different situation from encountering an issue (e.g. Janus) and not forking
    [2020-04-01 13:36:10] <sarang> which provide other non-consensus fixes and benefits
    [2020-04-01 13:36:40] <Isthmus> Regardless, let's separate the metadata question (should we enforce ordered TLV) from feature questions (should we have a memo field)
    [2020-04-01 13:37:20] <sarang> Well, TLV enforcement has a big effect on non-standard data, since it requires a stated type
    [2020-04-01 13:37:33] — Isthmus views this as a good thing
    [2020-04-01 13:37:35] <UkoeHB_> I did make pseudo code for enforced sorted TLV, about 200lines
    [2020-04-01 13:37:36] <sarang> yes
    [2020-04-01 13:37:52] <sarang> But I mean that the features and the layout enforcement are closely intertwined here
    [2020-04-01 13:38:02] <UkoeHB_> Current code already mostly does sorted tlv by default
    [2020-04-01 13:38:38] <UkoeHB_> So all that needs to change is in tx validation
    [2020-04-01 13:38:47] <Isthmus> 👍
    [2020-04-01 13:39:01] <atoc> nice
    [2020-04-01 13:39:15] <sarang> OK, so I think what should be brought up in -dev is a well-considered position for 3 things related to extra
    [2020-04-01 13:39:25] <sarang> 1. Decision on TLV enforcement, and responsibility for implementation
    [2020-04-01 13:39:25] <atoc> koe, what's your github
    [2020-04-01 13:39:38] <sarang> 2. Decision on Janus mitigation, and implementation
    [2020-04-01 13:39:49] <sarang> 3. Musings on the new encrypted-memo idea
    [2020-04-01 13:40:13] <UkoeHB_> atoc https://github.com/monero-project/research-lab/issues/61
    [2020-04-01 13:40:48] <sarang> My position is 1: yes, 2: yes, 3: not unless enforced uniformly (and then it runs up against ePIDs)
    [2020-04-01 13:41:04] <Isthmus> 1: agree, 2: agree, 3: agree
    [2020-04-01 13:41:28] <sarang> Anyway, good things to consider here
    [2020-04-01 13:41:29] <gingeropolous> is the janus mitigation the thing with the subaddresses?
    [2020-04-01 13:41:32] <sarang> Yes
    [2020-04-01 13:41:49] <UkoeHB_> Janus https://github.com/monero-project/research-lab/issues/62
    [2020-04-01 13:41:53] <sarang> Enforcing a mitigation has the added advantage of making the number of tx pubkeys uniform
    [2020-04-01 13:42:03] <Isthmus> !!!
    [2020-04-01 13:42:04] <Isthmus> yesplz
    [2020-04-01 13:42:33] <gingeropolous> ima just throw it out there to play devils advocate, dunno if its been stated before. What about reverting to not having subaddresses?
    [2020-04-01 13:42:38] <sarang> So you have one Janus-specific tx pubkey per transaction, and a separate additional pubkey per output
    [2020-04-01 13:42:51] <fuwa> is it possible to replace tx extra completely with memo, so you don't need to sort anything
    [2020-04-01 13:43:07] <sarang> You'd need to remove all non-recipient-specific data from memo
    [2020-04-01 13:43:18] <sarang> Which IIRC moneromooo said would be a significant engineering effort
    [2020-04-01 13:43:54] <sarang> Extra isn't an inherent problem if uniformity is reasonably enforced
    [2020-04-01 13:44:06] <Isthmus> Oh, I was wondering something actually
    [2020-04-01 13:44:24] <Isthmus> Suppose we decide that each transaction should contain X, Y, and Z
    [2020-04-01 13:44:47] <UkoeHB_> gingeropolous: then Janus would no longer be a problem. That's about it afaik
    [2020-04-01 13:44:58] <Isthmus> What's the performance difference between having 3 separate fields versus having 1 field with 3 enforced objects
    [2020-04-01 13:45:31] <sarang> That's a good question, and I'm not sure
    [2020-04-01 13:46:15] <gingeropolous> right. so i guess the underlying question is whether subaddresses are worth it.
    [2020-04-01 13:46:34] <sarang> The scanning benefit is huge for large sets of addresses
    [2020-04-01 13:46:56] <sarang> Hash lookups are much faster than doing multiple scans of all transactions per address
    [2020-04-01 13:47:14] <sarang> and Janus checks are only needed for transactions that are already identified as being destined for you
    [2020-04-01 13:47:22] <sarang> (and those checks are quite fast anyway)
    [2020-04-01 13:47:46] <sarang> Also note that MLSAG -> CLSAG drops average tx size by 600 bytes already
    [2020-04-01 13:48:03] <sarang> s/average/typical
    [2020-04-01 13:48:42] <ArticMine> Like 2 in 2 out
    [2020-04-01 13:49:07] <sarang> Yes, a 2-2 tx drops already from ~2.5 kB to ~1.9 kB
    [2020-04-01 13:49:29] <sarang> So Janus mitigation adds something like about 64 bytes back in
    [2020-04-01 13:49:37] <sarang> (more for multi-output)
    [2020-04-01 13:49:53] <sarang> Meaning there's already plenty of wiggle room
    [2020-04-01 13:50:15] <gingeropolous> well here's hoping its the last mitigation for subaddresses.
    [2020-04-01 13:50:17] <atoc> that's a pretty good drop
    [2020-04-01 13:52:18] <ArticMine> We can increase the ring size
    [2020-04-01 13:52:43] <UkoeHB_> meeting is getting toward the end, so Ill add my update here: ztm2 should be ready to publish this weekend, I'm finishing up my last proofreading atm
    [2020-04-01 13:53:08] <sarang> UkoeHB_: great!
    [2020-04-01 13:53:12] <UkoeHB_> might take a bit for getmonero to update though, so we will see when I post about it
    [2020-04-01 13:53:13] <atoc> koe - i sent you an email but to reiterate it's looking really good
    [2020-04-01 13:53:26] <UkoeHB_> yeah saw that :)
    [2020-04-01 13:53:27] <sarang> Since the hour is indeed almost up, does anyone else wish to share any topics of interest?
    [2020-04-01 13:53:43] <Isthmus> https://www.reddit.com/r/Monero/comments/fnhm6u/maam_monero_ask_anything_monday_march_23_2020/flbbt45?utm_source=share&utm_medium=web2x
    [2020-04-01 13:53:45] <Isthmus> ^ thoughts?
    [2020-04-01 13:54:19] <Isthmus> I'm looking for projects for Fellows to work on, wondering if that seems like a good candidate
    [2020-04-01 13:55:26] <sarang> That sounds like a question for -dev or -gui TBH!
    [2020-04-01 13:55:31] <Isthmus> I could also have one of the software engineers implement ordered TLV if -dev wants somebody else to tackle it
    [2020-04-01 13:55:38] <Isthmus> Oh yea, good point
    [2020-04-01 13:56:17] <Isthmus> Any wish list projects for MRL? I have 2 software engineers, 1 mathematician, and some data scientists that are open to working on Monero stuff
    [2020-04-01 13:56:30] <atoc> Isthmus this seems good. i am willing to help but probably can't commit too much atm
    [2020-04-01 13:56:31] <sarang> Isthmus: perhaps pop over to -dev after meeting and let the channel know that a Fellow might be able to tackle TLV
    [2020-04-01 13:56:34] <sarang> see what the responses are
    [2020-04-01 13:56:57] <sarang> I bet moneromooo will have better knowledge of the effects that parsing would have on performance overall
    [2020-04-01 13:57:06] <UkoeHB_> well this never got much traction but Im still a fan https://github.com/monero-project/research-lab/issues/59 could be a lot of work idk
    [2020-04-01 13:57:40] <sarang> Isthmus: I know this important PR needed review... https://github.com/monero-project/supercop/pull/3
    [2020-04-01 13:58:21] <sarang> and if any Fellows have sufficient interest, the new CLSAG security model in the paper could use some eyes
    [2020-04-01 13:58:39] — Isthmus takes notes
    [2020-04-01 13:59:10] <sarang> Anyway, let's start to wrap up
    [2020-04-01 13:59:16] <ArticMine> I'll cover the fee, penalty and median proposal in the next meeting. By then I'll have most of this finalized
    [2020-04-01 13:59:16] <sarang> Any ACTION ITEMS to share?
    [2020-04-01 13:59:21] <sarang> Great ArticMine
    [2020-04-01 13:59:56] <atoc> @sarang i'll probably ping you tomorrow to go over some zkp ideas for atomic swap
    [2020-04-01 14:00:11] <sarang> I'll be doing some work on an older preprint, reviewing some ideas in a draft preprint that were sent to me by another researcher, and returning to some Triptych code
    [2020-04-01 14:00:13] <UkoeHB_> there are two other big projects: fully-formed audit functionality, and extensive updates to multisig; mentioned those to TheCharlatan but they really are beasts I expect
    [2020-04-01 14:00:24] <atoc> i have some resources i'd like to share
    [2020-04-01 14:00:25] <sarang> for sure
    [2020-04-01 14:00:43] <Isthmus> We can close up the meeting, but I'm curious later if anybody has speculation around what's going on with https://xmrchain.net/search?value=f6cff1edd1a7861ed13d494dd4ae7c4a7f42b5c3bf91457310d2166722c1316f
    [2020-04-01 14:00:55] <Isthmus> It has an unknown tag type, and the length is recorded incorrectly
    [2020-04-01 14:01:30] <UkoeHB_> are you sure it's a length and not a value byte?
    [2020-04-01 14:02:00] <Isthmus> Not sure, that's why I'm asking
    [2020-04-01 14:02:23] <sarang> All right, let's go ahead and adjourn for timing purposes, but discussions can of course continue
    [2020-04-01 14:02:27] <sarang> Thanks to everyone for attending!
    [2020-04-01 14:02:33] <sarang> Logs posted shortly on the GitHub agenda issue


# Action History
- Created by: SarangNoether | 2020-03-27T15:15:43+00:00
- Closed at: 2020-04-01T18:06:01+00:00
