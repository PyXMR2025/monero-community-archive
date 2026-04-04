---
title: 'Research meeting: 9 September 2019 @ 17:00 UTC'
source_url: https://github.com/monero-project/meta/issues/389
author: SarangNoether
assignees: []
labels: []
created_at: '2019-09-06T21:17:54+00:00'
updated_at: '2019-09-09T17:55:58+00:00'
type: issue
status: closed
closed_at: '2019-09-09T17:55:58+00:00'
---

# Original Description
Join in for the weekly Monero Research Lab meeting.

**When**: Monday, 9 September 2019 @ 17:00 UTC
**Where**: #monero-research-lab (freenode/matrix)

**Agenda**
1. Greetings

2. Roundtable
a. Sarang: [IACR 944 protocols](https://github.com/SarangNoether/skunkworks/tree/944-ipa-nozk/ipa-nozk), [RandomRun's LRS idea](https://github.com/monero-project/research-lab/issues/56), paper revisions
b. Surae
c. Others?

3. General questions

4. Action items

# Discussion History
## SarangNoether | 2019-09-09T17:55:58+00:00
    [2019-09-09 12:58:49] <sarang> GREETINGS
    [2019-09-09 12:58:52] <suraeNoether> howdy!
    [2019-09-09 12:59:25] <ArticMine> Hi
    [2019-09-09 12:59:31] <xmrmatterbridge> <worriedrise> Hello
    [2019-09-09 13:00:08] <sarang> For our ROUNDTABLE, I can go first
    [2019-09-09 13:00:41] <sarang> A meta-note is that my next funding request needs feedback to determine if/when it should be opened: https://repo.getmonero.org/monero-project/ccs-proposals/merge_requests/96
    [2019-09-09 13:01:14] <sarang> Aside from that, I've been working on inner-product proofs from IACR 944, which I know kenshamir[m] has also been working on
    [2019-09-09 13:01:31] <sarang> Some neat efficiency things going on with those: https://github.com/SarangNoether/skunkworks/tree/944-ipa-nozk/ipa-nozk
    [2019-09-09 13:01:47] <sarang> I've received plenty of edits/feedback to get the CLSAG paper submitted by its deadline
    [2019-09-09 13:02:06] <suraeNoether> *thumbs up for clsag*
    [2019-09-09 13:02:38] <sarang> And our friend RandomRun had a neat idea for applying a Groth proving system to transactions, detailed in a GitHub issue: https://github.com/monero-project/research-lab/issues/56
    [2019-09-09 13:03:08] <suraeNoether> that proving system is also the basis for bootle's sublinear ring signatures, which was the basis for RTRS once upon a time
    [2019-09-09 13:03:14] <sarang> The sizes are pretty big, but it may be possible to use some tricks from another paper to shrink them down
    [2019-09-09 13:03:17] <suraeNoether> it's a strong foundational paper
    [2019-09-09 13:03:25] <sarang> Yeah, it's used in Lelantus too
    [2019-09-09 13:04:19] <sarang> That's my two cents so far
    [2019-09-09 13:04:21] <sarang> suraeNoether: ?
    [2019-09-09 13:04:51] <mikerah> Hello
    [2019-09-09 13:05:13] <suraeNoether> my updates involve 1) matching, 2) proof of knowledge of signatures, and 3) looking at omniring as a general proving system for various uses
    [2019-09-09 13:05:28] <suraeNoether> re: 1) i've made a bunch of local commits that i'll be squashing and pushing in a day or so
    [2019-09-09 13:05:46] <suraeNoether> re: 2) i've identified a few of the foundational papers i'll be using to make my argument
    [2019-09-09 13:05:57] <suraeNoether> re: 3) is a lot of reading and asking sarang questions
    [2019-09-09 13:07:09] <sarang> neat
    [2019-09-09 13:07:22] <sarang> Before we do questions and discussion, any other interesting work to share?
    [2019-09-09 13:07:24] <suraeNoether> that's pretty much it so far; i have a stack of papers i've annihilated in the past few weeks, ranging from BOLT to bilinear pairings papers, but a lot of it has been background reading
    [2019-09-09 13:08:53] <sarang> All right, we can also do QUESTIONS now
    [2019-09-09 13:09:13] <sarang> suraeNoether: sounded from earlier like the PoKoS would likely require pairing operations?
    [2019-09-09 13:09:59] <mikerah> I have a question. A few weeks back, I came on here asking about minimal smart contracts. I'm still doing some thinking about this. It doesn't seem like monero has any form of storage. Is this correct?
    [2019-09-09 13:10:15] <sarang> What do you mean by storage?
    [2019-09-09 13:10:18] <suraeNoether> yeah, all the foundational stuff i've found ranges from "easy" to "moderate" in the pairings setting, but has zero solutions at all for the DL setting. so i'm looking sort of into how to solve some of these problems in the DL setting. If i make progress on that front, it'd be of independent interest to the larger research community *AND* it would allow for some weeeeird stuff in Monero
    [2019-09-09 13:11:28] ⇐ midnightmagic quit (~midnightm@unaffiliated/midnightmagic): Ping timeout: 264 seconds
    [2019-09-09 13:12:01] <kenshamir[m]> suraeNoether: I was reading the bulletin and saw this issue: "Tech note/MRL bulletin on placing STARKs inside bulletproofs"
    [2019-09-09 13:12:02] <kenshamir[m]> Is there anymore information regarding this?
    [2019-09-09 13:12:11] <kenshamir[m]> Issue: 43
    [2019-09-09 13:12:43] <mikerah> @kenshamir: How would fitting a STARK inside a bulletproof work? I can see the opposite working, though.
    [2019-09-09 13:13:04] <suraeNoether> kenshamir[m]: I wanted to write a technical note re: that topic, or i want someone else to write it. i'm interested in the details behind placing a Sapling-style statement inside of a bulletproof. this is work that the zcash folks have done already, apparently, but i want a formal write-up. it's a common idea a lot of folks have, so it'd be nice to have a document to point to re: efficiency etc
    [2019-09-09 13:13:35] <sarang> AFAIK the zcash-related work was simply estimating sizes/times based on circuit complexity
    [2019-09-09 13:13:38] <suraeNoether> mikerah: a bulletproof can prove statements about inner products about vectors. so you can take a Sapling-style statement and formalize it in a bulletproof
    [2019-09-09 13:13:52] <suraeNoether> sarang: indeedily do, neighborino, that's my recollection as well
    [2019-09-09 13:14:02] <sarang> Well, bulletproofs can prove things about circuits natively :)
    [2019-09-09 13:14:19] <sarang> The range proofs that are commonly used are a less general application
    [2019-09-09 13:14:23] <suraeNoether> *nod*
    [2019-09-09 13:14:24] <sarang> (but are more efficient)
    [2019-09-09 13:14:32] <mikerah> @sarang: storage as in extra space in a transaction that one can take advantage of for random stuff. Bitcoin blocks have extra space that people have used in the past to store messages. In Ethereum, there's calldata.
    [2019-09-09 13:14:40] <mikerah> *extra space in a block
    [2019-09-09 13:14:49] <sarang> There's an arbitrary data field that's also used to store certain transaction information and payment IDs
    [2019-09-09 13:14:59] <sarang> tx_extra
    [2019-09-09 13:15:03] <suraeNoether> we have tx_extra, but storing anything but uniform random data in it can lead to de-anonymization
    [2019-09-09 13:15:09] <sarang> aye
    [2019-09-09 13:15:25] <sarang> (or if not uniform random, "typical" data)
    [2019-09-09 13:15:32] <suraeNoether> yeah
    [2019-09-09 13:15:37] <suraeNoether> i should caveat that
    [2019-09-09 13:15:43] <sarang> There have been ideas in the past for things like return addresses etc
    [2019-09-09 13:15:44] <suraeNoether> if any data is stored in tx_extra, it should be encrypted
    [2019-09-09 13:17:04] <mikerah> I see. I will continue thinking about this see if I can come up with something, eventually
    [2019-09-09 13:17:10] <ArticMine> This begs the question how does one enforce encryption for tx_extra?
    [2019-09-09 13:18:24] <sarang> should != must
    [2019-09-09 13:19:01] <Inge-> What is the length limitation of tx_extra?
    [2019-09-09 13:20:49] <xmrmatterbridge> <worriedrise> Have you looked into dual outputs for Lelantus? Maybe if instead using the hash of the signing key, it took the hash of two signing keys S = Hs(P||Q), then also perhaps the commitments for the timelock could be stored in triple commitment? I haven't thought much about it though.
    [2019-09-09 13:21:35] <sarang> Inge-: AFAIK there is no hard cap (aside from any block-specific limits etc.)
    [2019-09-09 13:22:23] <sarang> worriedrise: interesting, but why a triple commitment?
    [2019-09-09 13:22:37] <sarang> That commitment could be stored as a standard Pedersen commitment along with the new outputs, could it not?
    [2019-09-09 13:24:21] <xmrmatterbridge> <worriedrise> It could indeed. It would be one more point to store is all
    [2019-09-09 13:24:35] <suraeNoether> "This begs the question how does one enforce encryption for tx_extra?" <-- add a tx_extra_valid field, change tx_extra to a pair of group elements, use switch commitments in tx_extra and in tx_extra_valid store a proof of knowledge of the opener of the commitment. if you stash plaintext in tx_extra, you won't be able to open it as a commitment... that'd be one way. but i don't think enforcing it is
    [2019-09-09 13:24:35] <suraeNoether> necessarily a good idea...
    [2019-09-09 13:24:39] <suraeNoether> ArticMine: ^
    [2019-09-09 13:26:47] <ArticMine> There is a possible attack vector if unencrypted data in tx_extra is enforced or an incentive is provided. This came up in the payment id discussion
    [2019-09-09 13:27:26] <suraeNoether> *nod* but enforcing that stuff in tx_extra "looks uniform" can only go so far before head-meets-brick-wall
    [2019-09-09 13:27:31] <kenshamir[m]> Reading a bit slow; sarang For rangeproofs, are you looking to switch out the inner product argument being used currently in bulletproofs for the one being used in 944?
    [2019-09-09 13:27:58] <sarang> Oh, I was just tooling around with it
    [2019-09-09 13:29:07] <kenshamir[m]> For the record, I think previously I mentioned 944 modifying bulletproofs inner product proof, but bulletproofs is an inner product argument also
    [2019-09-09 13:29:15] <kenshamir[m]> Oh right
    [2019-09-09 13:29:19] <sarang> ?
    [2019-09-09 13:30:07] <kenshamir[m]> <sarang "?"> In case I said it in a previous monero meeting, not sure
    [2019-09-09 13:30:08] <sarang> Yeah, I was playing around with the algebra needed to get the 944 IPA playing nicely with the optimized verification in BP
    [2019-09-09 13:30:10] <sarang> righto
    [2019-09-09 13:31:18] <sarang> It sounds like the 944 authors did implementations of the BP range proofs with both inner product arguments, and claimed a fairly substantial speedup, if I'm reading correctly
    [2019-09-09 13:31:31] <sarang> A much bigger speedup than I'd expect
    [2019-09-09 13:32:04] <ArticMine> suraeNoether Right one can enforce encryption but one cannot prevent out of bounds publication of the decryption key
    [2019-09-09 13:32:24] <kenshamir[m]> <sarang "It sounds like the 944 authors d"> Yep, I am trying to verify this against Dalek's implementation, but I have paused as something in the paper does not make sense to me at the moment
    [2019-09-09 13:32:38] <sarang> kenshamir[m]: what's that?
    [2019-09-09 13:32:50] <kenshamir[m]> Hopefully, I can get an asnwer on it and benchmark against Dalek's optimised implementation
    [2019-09-09 13:33:09] <kenshamir[m]> <sarang "kenshamir: what's that?"> The \Gamma_{i} that is mentioned multiple times
    [2019-09-09 13:33:20] <kenshamir[m]> Which is of size n-2 x n-2
    [2019-09-09 13:33:23] <sarang> I assume, for example, that the 944 authors didn't unroll the IPA recursion in verification
    [2019-09-09 13:33:26] <kenshamir[m]> Only holds on quadratic equation
    [2019-09-09 13:33:52] <kenshamir[m]> I originally thought that it would hold n-2 quadratic equations
    [2019-09-09 13:33:54] <sarang> Why would this be important for the underlying non-zk IPA?
    [2019-09-09 13:34:21] <kenshamir[m]> <sarang "I assume, for example, that the "> Yep, I will need to implement your code in order to make the benchmarks fair because Dalek's code does this
    [2019-09-09 13:34:46] <sarang> My suspicion is that the unrolled recursion wipes out almost all of the speedup
    [2019-09-09 13:35:07] <sarang> Since most of the optimizations appear to be in scalar operations only
    [2019-09-09 13:35:46] <kenshamir[m]> <sarang "Why would this be important for "> It does not make sense to me that a matrice only holds one equation, unless there is something I have misunderstand
    [2019-09-09 13:36:19] <sarang> But this doesn't affect any uses of _only_ the underlying non-zk IPA, correct?
    [2019-09-09 13:36:44] <sarang> So you don't mean that misunderstanding is a holdup for testing of the IPA for rangeproofs alone?
    [2019-09-09 13:36:47] <kenshamir[m]> <sarang "My suspicion is that the unrolle"> Plus Dalek use a batch_invert function for Scalars, so this may absolutely be the case
    [2019-09-09 13:37:03] <sarang> Yeah, we also batch the inversions
    [2019-09-09 13:37:21] <sarang> so it's really just a single inversion and some scalar-scalar multiplications (which are essentially free)
    [2019-09-09 13:37:52] <kenshamir[m]> <sarang "So you don't mean that misunders"> I implemented the code using dense matrices, which is really in-efficient. I think there will be a big difference if we can store n-2 equations in one matrice, versus storing n-2 matrices of size `n-2 x n-2`
    [2019-09-09 13:38:29] <sarang> Right, but if you're only testing a swap of the inner product argument in the bulletproofs rangeproof, you don't need any of the "higher-level" protocols
    [2019-09-09 13:38:38] <sarang> the non-zk IPA stands on its own
    [2019-09-09 13:38:53] <kenshamir[m]> <sarang "Right, but if you're only testin"> Oh right, I get what you mean
    [2019-09-09 13:38:57] <sarang> This is what I assume that table at the end of 944 was doing
    [2019-09-09 13:39:01] <sarang> For the general applications, totally
    [2019-09-09 13:39:08] <sarang> I think we're on the same page :D
    [2019-09-09 13:39:19] ⇐ xmrmatterbridge quit (~xmrmatter@lists.getmonero.org): Remote host closed the connection
    [2019-09-09 13:39:37] → xmrmatterbridge joined (~xmrmatter@lists.getmonero.org)
    [2019-09-09 13:39:37] <kenshamir[m]> I was thinking of benchmarking 944 rangeproof vs bulletproofs. But you are correct, in that we also need to benchmark 944s IPA_Nozk vs bulletproofs IPA
    [2019-09-09 13:39:57] <sarang> The paper seems to have both
    [2019-09-09 13:40:13] <sarang> Perhaps the latter benchmarks were only in the extended 944 paper (I'd have to check)
    [2019-09-09 13:40:13] ⇐ glv quit (~glv@2a01:e34:ed03:c7d0:c1ab:c05d:9d2f:9025): Remote host closed the connection
    [2019-09-09 13:40:16] <sarang> but no matter reallly
    [2019-09-09 13:40:47] <sarang> AFAICT the last timing table is just swapping the non-zk IPA
    [2019-09-09 13:40:47] <kenshamir[m]> Yeah it had both, the benchmarks show that they are basically the same once bulletproofs uses  IPA_NoZK
    [2019-09-09 13:40:54] <kenshamir[m]> Yeah
    [2019-09-09 13:41:12] <sarang> Although the speedup was still impressive from just IPA_NoZK (hence wanting to know if unrolling makes it irrelevant)
    [2019-09-09 13:41:30] <sarang> something like ~30% IIRC?
    [2019-09-09 13:41:37] <sarang> which seems absurd
    [2019-09-09 13:41:46] <kenshamir[m]> Yeah, it was in that ballpark
    [2019-09-09 13:41:57] <sarang> Still, worth a shot anyway to confirm :)
    [2019-09-09 13:42:08] <sarang> Probably will be worth writing to the authors to note this
    [2019-09-09 13:42:19] <kenshamir[m]> I will also test the normal IPA_NOZK without multi-exp versus bulletproofs with multiexp
    [2019-09-09 13:42:24] <sarang> I'll send them my unrolling algorithm too, to provide better benchmarks
    [2019-09-09 13:42:50] <sarang> Multiexp will be huge, of course, in any of the applications
    [2019-09-09 13:43:11] <sarang> when the size gets large
    [2019-09-09 13:43:30] <kenshamir[m]> They used a generic library too, so this could play a role in the benchmarks
    [2019-09-09 13:43:37] <kenshamir[m]> Not sure how/if though
    [2019-09-09 13:43:46] <kenshamir[m]> <sarang "when the size gets large"> Yep
    [2019-09-09 13:43:47] <sarang> Yeah, but that shouldn't matter, ideally, if they did parallel implementations
    [2019-09-09 13:44:03] <sarang> But hey, that's part of the point of a preprint, I suppose
    [2019-09-09 13:44:07] <sarang> Get feedback and additional info!
    [2019-09-09 13:44:21] ⇐ midipoet quit (uid316937@gateway/web/irccloud.com/x-gndbtjglwddmunnt): Quit: Connection closed for inactivity
    [2019-09-09 13:44:27] <sarang> Perhaps we can collaborate on feedback to the authors, kenshamir[m] 
    [2019-09-09 13:44:33] <sarang> once we have numbers on this stuff
    [2019-09-09 13:44:45] <sarang> I think it would be useful in their paper to note these things
    [2019-09-09 13:44:50] <kenshamir[m]> <sarang "Perhaps we can collaborate on fe"> Yep that would be great
    [2019-09-09 13:45:02] <sarang> awesome
    [2019-09-09 13:45:05] ⇐ xmrmatterbridge quit (~xmrmatter@lists.getmonero.org): Remote host closed the connection
    [2019-09-09 13:45:10] ⇐ wow-discord quit (~wow-disco@104.248.17.142): Remote host closed the connection
    [2019-09-09 13:45:13] <kenshamir[m]> Yeah, because this was one of the more important contributions of the paper
    [2019-09-09 13:45:21] <sarang> for sure
    [2019-09-09 13:45:23] <kenshamir[m]> The proof system was also great
    [2019-09-09 13:45:36] → wow-discord joined (~wow-disco@104.248.17.142)
    [2019-09-09 13:45:36] → xmrmatterbridge joined (~xmrmatter@lists.getmonero.org)
    [2019-09-09 13:45:41] ⇐ xmrmatterbridge quit (~xmrmatter@lists.getmonero.org): Remote host closed the connection
    [2019-09-09 13:45:42] <sarang> 10/10 would verify?
    [2019-09-09 13:45:44] <sarang> =p
    [2019-09-09 13:46:33] <kenshamir[m]> :D
    [2019-09-09 13:46:49] <sarang> In the interest of time, are there other questions?
    [2019-09-09 13:48:18] <sarang> OK!
    [2019-09-09 13:48:22] <sarang> On to ACTION ITEMS before we close
    [2019-09-09 13:48:51] → xmrmatterbridge joined (~xmrmatter@lists.getmonero.org)
    [2019-09-09 13:48:55] <sarang> I'll be continuing several things: proving systems, benchmarks, paper submission
    [2019-09-09 13:49:10] ⇐ xmrmatterbridge quit (~xmrmatter@lists.getmonero.org): Remote host closed the connection
    [2019-09-09 13:49:14] <sarang> Feel free to comment on the proposed funding request, to determine if it should be opened
    [2019-09-09 13:49:22] <sarang> suraeNoether: your action items?
    [2019-09-09 13:49:52] <suraeNoether> ah, yes, sorry about that: squashing a bunch of commits for matching, to whip thring signatures into shape for the FC conference, and to start putting my ideas on POKOS down
    [2019-09-09 13:50:07] <suraeNoether> but mainly matching, because that is so close to giving good results
    [2019-09-09 13:51:08] <sarang> Awesome! Any other action items to share before we close?
    [2019-09-09 13:51:20] <suraeNoether> just that i love all of you
    [2019-09-09 13:51:27] → xmrmatterbridge joined (~xmrmatter@lists.getmonero.org)
    [2019-09-09 13:51:32] <suraeNoether> be sure to comment on sarang's proposal request/comment period
    [2019-09-09 13:51:41] ⇐ xmrmatterbridge quit (~xmrmatter@lists.getmonero.org): Remote host closed the connection
    [2019-09-09 13:51:49] <kenshamir[m]> 😳
    [2019-09-09 13:52:50] <sarang> Aw shucks
    [2019-09-09 13:53:03] <sarang> Thanks to everyone for participating! Logs will be posted to GitHub shortly


# Action History
- Created by: SarangNoether | 2019-09-06T21:17:54+00:00
- Closed at: 2019-09-09T17:55:58+00:00
