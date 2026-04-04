---
title: 'Research meeting: 11 March 2019 @ 17:00 UTC'
source_url: https://github.com/monero-project/meta/issues/314
author: SarangNoether
assignees: []
labels: []
created_at: '2019-03-10T14:45:00+00:00'
updated_at: '2019-03-11T18:02:05+00:00'
type: issue
status: closed
closed_at: '2019-03-11T18:02:05+00:00'
---

# Original Description
Join in for the weekly Monero Research Lab meeting.

**When**: Monday, 11 March 2019 @ 17:00 UTC
**Where**: #monero-research-lab (freenode/matrix)

**Agenda**
1. Greetings

2. Network upgrade

3. Next point release
a. [Output selection](https://github.com/SarangNoether/skunkworks/tree/outputs/outputs)
b. [Bulletproofs optimizations](https://github.com/monero-project/monero/blob/master/src/ringct/bulletproofs.cc)

4. Roundtable
a. Sarang
b. Surae
c. Others?

5. Questions

6. Action items

# Discussion History
## SarangNoether | 2019-03-11T18:02:05+00:00
    [2019-03-11 12:56:39] <sarang> Our meeting begins presently
    [2019-03-11 12:56:50] * sarang set the topic to Research meeting NOW: https://github.com/monero-project/meta/issues/314
    [2019-03-11 12:58:30] <sarang> Let's go ahead and get started. Agenda is here: https://github.com/monero-project/meta/issues/314
    [2019-03-11 12:58:36] <suraeNoether> howdy everyone
    [2019-03-11 12:58:38] <sarang> 1. GREETINGS
    [2019-03-11 12:58:43] <sarang> hi
    [2019-03-11 12:58:49] <MRL-discord> <Isthmus> Hello! Biking, in soon.
    [2019-03-11 12:58:55] <parasew[m]> hello!
    [2019-03-11 12:59:51] <sarang> Let's recap 2. NETWORK UPGRADE
    [2019-03-11 13:00:03] <sarang> Kudos to everyone for a successful first upgrade
    [2019-03-11 13:00:26] <sarang> I don't recall when the second was slated to occur, since block arrival was stunted
    [2019-03-11 13:00:42] <sarang> Any thoughts on the upgrade after the fact?
    [2019-03-11 13:01:26] <xmrmatterbridge> <rehrar> Hi
    [2019-03-11 13:01:57] <sarang> I believe it was dEBRUYNE who wanted an upcoming meeting specifically to talk more deeply about the future of PoW
    [2019-03-11 13:01:58] <parasew[m]> anyone monitored the "old chain"? if there have been this large amount of asics on there, and not turned off it should be visible
    [2019-03-11 13:02:24] <sarang> I believe sgp_ ran some blackball numbers on it
    [2019-03-11 13:02:38] <sarang> and found essentially nothing of interest
    [2019-03-11 13:02:49] <sarang> but as far as hashrate, I am not sure
    [2019-03-11 13:03:05] <sgp_> yeah, no chain reactions so far, very few known spent outputs through reused key images
    [2019-03-11 13:03:13] <sgp_> impact on network privacy so far is essentially 0
    [2019-03-11 13:03:26] <sarang> sgp_: were the key image reuse numbers for only v9 and v10?
    [2019-03-11 13:03:28] — sgp_ disappears for the rest of the meeting
    [2019-03-11 13:03:36] <sgp_> yes, just those two
    [2019-03-11 13:03:41] <sarang> great, thanks
    [2019-03-11 13:04:04] <sarang> Relating to this, we can also introduce 3. NEXT POINT RELEASE
    [2019-03-11 13:04:20] <sarang> Not all desired non-consensus changes made it in to this release, so Sometime Soon (tm) will be a point release
    [2019-03-11 13:04:33] <sarang> BP optimizations will be one nice addition
    [2019-03-11 13:04:50] <sarang> I would like output selection to also be included... we talked about it at length at an earlier meeting
    [2019-03-11 13:04:59] <dEBRUYNE> sarang: Correct. It's a topic with a lot of depth that requires an extensive discussion imo
    [2019-03-11 13:05:32] <sarang> suraeNoether: do you have a current recommendation for output selection?
    [2019-03-11 13:06:11] <suraeNoether> i'm running into problems testing the matching code, based on this problem too
    [2019-03-11 13:06:21] <sarang> Here is a discussion of the different algorithms: https://github.com/monero-project/meta/issues/307#issuecomment-466514757
    [2019-03-11 13:06:43] <suraeNoether> iirc the output lineup method performs quite well
    [2019-03-11 13:06:57] <sarang> I prefer it among the others that were tested
    [2019-03-11 13:07:21] <sarang> But it's a change that deserves more than two thumbs-up :)
    [2019-03-11 13:07:29] <suraeNoether> there is no optimal solution, but some solutions are better than others and the output lineup method is more reasonable than the other proposals, and i have no new proposals to make (yet)
    [2019-03-11 13:08:02] <sarang> I updated the sim code (link in agenda) to examine the output weighting in more details
    [2019-03-11 13:08:25] <sarang> Hopefully the BP optimizations are less contenious
    [2019-03-11 13:08:44] <suraeNoether> uhm i think i have one possible proposal that i want to chat about with you by side channel to hash out some details
    [2019-03-11 13:08:55] <sarang> sure
    [2019-03-11 13:09:11] <sarang> We should have a formal recommendation before whatever date is set for the point release code freeze
    [2019-03-11 13:09:27] — needmoney90 shuffles in
    [2019-03-11 13:09:50] <sarang> Anything else relating to the point upgrade that ought to be discussed?
    [2019-03-11 13:09:55] <sarang> ping moneromooo perhaps
    [2019-03-11 13:10:58] <xmrmatterbridge> <rehrar> I just want timelines. Nothing to say on content.
    [2019-03-11 13:12:31] <moneromooo> hi
    [2019-03-11 13:12:40] <moneromooo> What's the question ? :)
    [2019-03-11 13:13:24] <moneromooo> I don't know about any date. Depends when we get all the stuff on master ready really.
    [2019-03-11 13:13:28] <sarang> Anything relating to the next point release you'd like us to discuss?
    [2019-03-11 13:13:40] <moneromooo> None that come to mind right now.
    [2019-03-11 13:13:46] <sarang> ty
    [2019-03-11 13:13:58] <sarang> In that case, let's move to 4. ROUNDTABLE
    [2019-03-11 13:14:04] <sarang> suraeNoether: care to go first?
    [2019-03-11 13:14:29] ⇐ rex4539 quit (~rex4539@ppp-2-84-160-62.home.otenet.gr): Ping timeout: 268 seconds
    [2019-03-11 13:14:50] <sarang> OK, I can go first instead
    [2019-03-11 13:14:57] <suraeNoether> ok
    [2019-03-11 13:15:01] <sarang> aha, go ehead
    [2019-03-11 13:15:07] <suraeNoether> heh
    [2019-03-11 13:15:08] — sarang steps aside
    [2019-03-11 13:15:26] <suraeNoether> Well, my simulations for the matching code are to the point where i'm running a matching on some test data now to generate a confusion matrix.
    [2019-03-11 13:15:40] <suraeNoether> i'm also editing the manuscript describing the whole process
    [2019-03-11 13:16:06] <suraeNoether> one of the problems i'm running into is actually simulating our output selection in part because it's not clear which direction we are going yet
    [2019-03-11 13:16:31] <suraeNoether> and it occurred to me that this could help inform our choice of output selection by seeing if one of these possibilities makes matching easier or harder
    [2019-03-11 13:17:00] <sarang> IMO matching expect spend with proper weighting seems optimal enough from a purely timing perspective
    [2019-03-11 13:17:12] <sarang> (leaving out questions of binning etc)
    [2019-03-11 13:17:30] <suraeNoether> when i say easy or hard i don't mean in terms of time, because as we've seen matching is essentially super duper fast
    [2019-03-11 13:17:38] <suraeNoether> i mean in terms of false negative and false positive rates
    [2019-03-11 13:17:52] <suraeNoether> but you are 100% on that
    [2019-03-11 13:18:49] <sarang> aw shucks
    [2019-03-11 13:19:01] <suraeNoether> i'm working on a variety of other side things but i'm shooting for this matching paper to be complete and published some time in the next 2 months
    [2019-03-11 13:19:10] <sarang> Excellent
    [2019-03-11 13:19:18] <suraeNoether> if we get more speakers for the konferenco, then i won't be speaking, but otherwise i will probably be presenting on this at the konferenco
    [2019-03-11 13:19:28] → LuisM joined (5e3d3263@gateway/web/freenode/ip.94.61.50.99)
    [2019-03-11 13:19:50] <sarang> Neat; anything else of interest to share?
    [2019-03-11 13:20:00] <suraeNoether> that's all i have today, thanks!
    [2019-03-11 13:20:05] <sarang> Righto
    [2019-03-11 13:20:07] <sarang> I have a few things
    [2019-03-11 13:20:07] <xmrmatterbridge> <learninandlurkin> The line up is looking great btw! Fantastic effort for a first konferenco
    [2019-03-11 13:20:12] <suraeNoether> catching up on lots of reaidng in algebraic geometry :D
    [2019-03-11 13:20:17] <sarang> First, my next FFS/CCS will be posted soon
    [2019-03-11 13:20:37] <sarang> As was discussed here, in -community, and elsewhere, the request will be for immediate payout
    [2019-03-11 13:20:57] <sarang> This means both donors and I know the actual value of the donations
    [2019-03-11 13:21:04] <sarang> Since this is a big change, any questions or comments on it?
    [2019-03-11 13:21:16] <sarang> (presumably suraeNoether will be doing the same arrangement)
    [2019-03-11 13:21:26] <suraeNoether> i'm in support of this, and i will indeed be mimicking this
    [2019-03-11 13:21:41] <sarang> Folks who do not trust us to run with the money should, of course, not donate
    [2019-03-11 13:21:49] <sarang> But my hope is that our records have shown we're good for it :D
    [2019-03-11 13:21:54] <binaryFate> happy we came to that solution eventually, hopefully will be better for your guys
    [2019-03-11 13:22:09] <sarang> Thanks to binaryFate and others for agreeing to this change
    [2019-03-11 13:22:15] <binaryFate> yes the idea is that donors being careful should discourage randomers to do the same
    [2019-03-11 13:22:27] <sarang> The CCS posting will _very_ clearly state the arrangement, so there is no confusion
    [2019-03-11 13:22:40] <binaryFate> If you figure out the markdown
    [2019-03-11 13:22:50] <sarang> Yes indeed
    [2019-03-11 13:23:05] <moneromooo> Technically, it's within the existing rules as stated: one milestone, which consists of "sarang starts working" :)
    [2019-03-11 13:23:18] <sarang> Second, the paper that suraeNoether and I have been collaborating with external researchers on (DLSAG et al.) is in final review now
    [2019-03-11 13:23:35] <sarang> We've been asked not to share it before it's released as a preprint, as a courtesy to all authors
    [2019-03-11 13:23:48] <suraeNoether> *nod*
    [2019-03-11 13:24:12] <sarang> It has some great details on useful constructions that I'm sure we'll discuss at length after the preprint goes to IACR
    [2019-03-11 13:24:22] <sarang> it'll be submitted for a conference as well
    [2019-03-11 13:24:37] <sarang> Third, I wrote up some additional tests and code for Bulletproofs MPC
    [2019-03-11 13:24:42] <dEBRUYNE> sarang: How does this work if the proposal is not fully funded yet when your period starts?
    [2019-03-11 13:24:58] → msvb-mob joined (~msvb-lab@monero/hardware/michael)
    [2019-03-11 13:25:06] <sarang> Two options: either the bulk is paid out and it stays open until filled
    [2019-03-11 13:25:13] <sarang> or it all sits there until fully funded
    [2019-03-11 13:25:20] → Febo joined (Febo@89-212-17-205.static.t-2.net)
    [2019-03-11 13:25:28] <sarang> I prefer the first, but am open to discussion
    [2019-03-11 13:26:12] <sarang> Regarding Bulletproofs MPC, real_or_random had some great thoughts on this before the meeting (but I won't put him on the spot)
    [2019-03-11 13:26:13] <suraeNoether> i imagine that the important part is laying out which way it goes in the proposal
    [2019-03-11 13:26:29] <sarang> the question has to do with what a malicious player can do
    [2019-03-11 13:27:33] <sarang> We chatted about the fact that an evil player could try to pull what amounts to a cancellation of partial proof elements, effectively setting the inputs to the hash that generates a F-S challenge
    [2019-03-11 13:27:55] <sarang> I couldn't find a way that this could be used as an exploit, aside from obviously generated an invalid proof
    [2019-03-11 13:28:18] <sarang> but the security proofs for BPs do require that F-S challenges are uniform
    [2019-03-11 13:28:31] <sarang> I had neglected that point when I had thought about this earlier
    [2019-03-11 13:30:49] ⇐ silur quit (~silur@185.236.201.131): Quit: leaving
    [2019-03-11 13:30:55] <sarang> My strong suspicion is that proof elements are still uniformly distributed in the presence of a dishonest challenge due to the prover's randomness, and that you still get zk in this case (but not provably)
    [2019-03-11 13:31:20] <sarang> Moral: if we do anything in the future that requires/desires this scheme, these things would need to be considered
    [2019-03-11 13:31:26] <sarang> Any questions/comments relating to this?
    [2019-03-11 13:32:46] <sarang> allrightythen
    [2019-03-11 13:32:53] ← msvb-mob left (~msvb-lab@monero/hardware/michael): "Leaving"
    [2019-03-11 13:33:00] <suraeNoether> i think we should continue to ponder it and write something up formally about the BP MPC schemes
    [2019-03-11 13:33:14] <sarang> Well that's the thing... there's really nothing to write formally
    [2019-03-11 13:33:45] <sarang> You can probably solve all the theoretical woes by having all players commit to their proof elements before multicasting them
    [2019-03-11 13:34:10] <sarang> then an honest prover is guaranteed uniform F-S challenges
    [2019-03-11 13:34:21] <xmrmatterbridge> <learninandlurkin> Sorry but I'm a little out of the loop here. What exactly are BP MPC for? something to do with multisig with BP?
    [2019-03-11 13:34:34] <suraeNoether> it's nice to think about collectively computing BP range proofs, but I'm still v curious about the coinjoin approach that we are considering on the larger scale.
    [2019-03-11 13:34:37] <sarang> Ideally, untrusted parties could generate single BPs for outputs
    [2019-03-11 13:34:45] <suraeNoether>  after all, it's hard to even think about threat models unless we know how these things will be used in practice
    [2019-03-11 13:34:57] <sarang> Sure, this is all pie-in-the-sky right now
    [2019-03-11 13:35:07] <suraeNoether> learninandlurkin: collaborating with friends to compute a range proof for a coinjoin style transaction, so that the participants don't reveal their amounts to each other
    [2019-03-11 13:35:27] <sarang> But yes, the threat model would be very different depending on how the rounds go
    [2019-03-11 13:35:46] <sarang> Finally, suraeNoether had shown me this a while back: https://lelantus.io/lelantus.pdf
    [2019-03-11 13:35:56] <suraeNoether> agreed on the commit-and-reveal; expensive but usually does the trick to ensure participants can't be rewound inappropriately
    [2019-03-11 13:36:00] <sarang> An interesting application of some of the fundamentals behind Bulletproofs and the old StringCT scheme
    [2019-03-11 13:36:14] <xmrmatterbridge> <learninandlurkin> So... allowing multi-input transactions where each user doesn't know the amounts of the other inputs? Sounds useful
    [2019-03-11 13:36:41] <suraeNoether> learninandlurkin hence our interest in nailing down threat models *nod*
    [2019-03-11 13:37:03] <sarang> I've been playing around with some of the math in that paper to see what nuggets could be extracted
    [2019-03-11 13:37:52] <suraeNoether> oh i had a brief thing to point out: isthmus and n3ptune at noncesense-research-lab answered one of my requests and we now have a complete empirical distribution of number of inputs and outputs per transaction
    [2019-03-11 13:38:00] <suraeNoether> forgot to mention this:
    [2019-03-11 13:38:42] <sarang> Neato, where is this distribution to be found?
    [2019-03-11 13:38:46] <suraeNoether> https://github.com/noncesense-research-lab/tx_in_out_distribution
    [2019-03-11 13:39:00] <suraeNoether> the data surprised me
    [2019-03-11 13:39:08] <dEBRUYNE> <sarang> I prefer the first, but am open to discussion <= I'd be OK with the first, but perhaps it would be most convenient to use a rounded number
    [2019-03-11 13:39:14] <dEBRUYNE> e.g. if 211 XMR is funded, pay out 200
    [2019-03-11 13:39:20] <sarang> You won't believe what's in tx_distribution_in.csv!
    [2019-03-11 13:39:45] <dEBRUYNE> Mebbe malware
    [2019-03-11 13:39:46] <dEBRUYNE> :P
    [2019-03-11 13:39:55] <suraeNoether> super heavy tails for one thing, and a rootkit for another
    [2019-03-11 13:40:34] <sarang> dEBRUYNE: perhaps a full payout at date X, and then a second payout at either date Y or completion, whichever comes first
    [2019-03-11 13:40:39] <binaryFate> <sarang> I prefer the first, but am open to discussion <-- donors will have no incentive to fund in time, it will drag till the end of the period
    [2019-03-11 13:40:56] <sarang> binaryFate: how would you do it?
    [2019-03-11 13:41:19] <binaryFate> I like the incentive to donors of you proposing something and getting to work on it only if funded
    [2019-03-11 13:41:19] <xmrmatterbridge> <learninandlurkin> I imagine coinjoining going on would really complicate output selection. Or is there some idea where they work off each other to get rid of heuristics?
    [2019-03-11 13:42:08] <sarang> Depends on how timely it is
    [2019-03-11 13:42:09] ⇐ iDunk quit (~iDunk@unaffiliated/idunk): Read error: Connection reset by peer
    [2019-03-11 13:42:21] <suraeNoether> learningandlurkin coinjoin brings a whole new nightmare to the party. does everyone bring their own mix-ins? certainly nothing is to stop a malicious party from coinjoining with a bunch of badly selected mix-ins
    [2019-03-11 13:42:45] <moneromooo> A ring is one person only. Fake output selection is untouched.
    [2019-03-11 13:42:47] <sarang> Well each input signs with its own ring
    [2019-03-11 13:42:53] <sarang> ^
    [2019-03-11 13:43:00] <moneromooo> That person makes their own ring, yes. Otherwise others would know which is the real out.
    [2019-03-11 13:43:18] <sarang> The benefit is breaking the assumption of one-party control of outputs and the link to the input rings
    [2019-03-11 13:43:56] <binaryFate> What about simple attack of using the same 10 decoys as one of the other participants?
    [2019-03-11 13:44:01] → msvb-mob joined (~msvb-lab@monero/hardware/michael)
    [2019-03-11 13:44:22] <suraeNoether> ^
    [2019-03-11 13:44:28] <msvb-mob> Is parasew, nevvton, or txmr in the channel?
    [2019-03-11 13:44:43] <binaryFate> mmm you don't know which are decoys, nevermind ^^
    [2019-03-11 13:45:12] <sarang> If this moves forward, hopefully we can determine the necessary practical security for BPs
    [2019-03-11 13:45:23] <sarang> If we can't aggregate, they'd have to be separate for each output
    [2019-03-11 13:45:33] <suraeNoether> my beard is getting very thoroughly stroked this morning. much to think about...
    [2019-03-11 13:46:18] <sarang> I believe we'd get practical security without player commitments, but not provable
    [2019-03-11 13:47:23] <sarang> Anyway: does anyone else wish to share interesting research before we close?
    [2019-03-11 13:47:37] → iDunk joined (~iDunk@unaffiliated/idunk)
    [2019-03-11 13:47:57] <xmrmatterbridge> <learninandlurkin> Yes it sounds like the interplay between coinjoin and ringsigs will require some diagrams for me to ever understand. Could get complicated.
    [2019-03-11 13:48:08] <suraeNoether> i think you would want a commit-and-reveal stage for everyone to see the ring members to prevent malicious ring intersection in the coinjoin
    [2019-03-11 13:48:32] <sarang> MoneroCoinJoin: an easy 14-round process!
    [2019-03-11 13:48:51] <suraeNoether> isthmus and i have been chatting about methods of extracting the true spend-time distribution from the monero blockchain without knowing exactly which outputs have been spent
    [2019-03-11 13:49:04] <suraeNoether> that's a very nascent conversation, though I think it'll end up being a very straightforward project
    [2019-03-11 13:49:36] <sarang> Discussions in #noncesense-research-lab I presume?
    [2019-03-11 13:50:04] <xmrmatterbridge> <learninandlurkin> so, truish spend-time distribution
    [2019-03-11 13:51:20] <binaryFate> Are there regular meetings on this or just continuous discussion? I had been working on this at some point and have some code around aiming to graphically show the real spend distribution
    [2019-03-11 13:52:01] <sarang> I've seen a few informal conversations in #noncesense-research-lab but didn't know if suraeNoether had something more formal
    [2019-03-11 13:52:07] <suraeNoether> binaryFate: ah, no, this has been a casual conversation by side channel, but there is clearly interest
    [2019-03-11 13:52:19] <suraeNoether> i'll start blabbing about it in here more publicly
    [2019-03-11 13:52:30] <sarang> In the interest of time, let's review 6. ACTION ITEMS and then close to continue discussion afterword
    [2019-03-11 13:52:35] <binaryFate> Ok don't hesitate to ping me on this
    [2019-03-11 13:53:19] <sarang> I will be posting my CCS request soon, tidying up the output selection stuff for a recommendation, getting the DLSAG application paper reviewed and out the door, and playing around with that Lelantus paper when/if I get a chance
    [2019-03-11 13:53:21] <sarang> suraeNoether: ?
    [2019-03-11 13:54:31] <suraeNoether> CCS request, working on simulations and measurable numbers for matching, and looking into using our matching code to answer questions about output selection
    [2019-03-11 13:54:56] <sarang> excellent
    [2019-03-11 13:54:59] <suraeNoether> also casual github maintenance
    [2019-03-11 13:55:07] <sarang> Any final questions or remarks before we adjourn?
    [2019-03-11 13:55:37] <xmrmatterbridge> <learninandlurkin> once you guys have made a recommendation for output selection
    [2019-03-11 13:55:55] <xmrmatterbridge> <learninandlurkin> and it gets implemented, what's the next big focus?
    [2019-03-11 13:56:25] <sarang> There will be much to consider in the realm of refund and payment channels
    [2019-03-11 13:56:47] <xmrmatterbridge> <learninandlurkin> Ooh yes the refund ideas from a while back were really interesting
    [2019-03-11 13:56:54] <sarang> and some aspects of output selection, like linking spends across rings in txns, is not solved yet
    [2019-03-11 13:57:06] <xmrmatterbridge> <learninandlurkin> Seems like a logical next area of research
    [2019-03-11 13:57:19] <sarang> and if coinjoin works out, there will be a lot to consider with that
    [2019-03-11 13:57:41] <sarang> Also transaction relay and network-level anonymity stuff that's still in progress
    [2019-03-11 13:57:59] <sarang> To quote the Simpsons: "like the cleaning of a house... IT NEVER ENDS"
    [2019-03-11 13:58:12] <sarang> But on that note, our meeting does end
    [2019-03-11 13:58:23] <sarang> Thanks to everyone for attending. We're adjourned; let the conversations continue
    [2019-03-11 13:58:36] * sarang set the topic to Research meeting Monday @ 17:00 UTC

# Action History
- Created by: SarangNoether | 2019-03-10T14:45:00+00:00
- Closed at: 2019-03-11T18:02:05+00:00
