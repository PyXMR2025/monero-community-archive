---
title: 'Research Meeting: 21 January 2019 @ 17:00 UTC'
source_url: https://github.com/monero-project/meta/issues/301
author: SarangNoether
assignees: []
labels: []
created_at: '2019-01-21T14:07:13+00:00'
updated_at: '2019-01-21T19:45:02+00:00'
type: issue
status: closed
closed_at: '2019-01-21T17:45:15+00:00'
---

# Original Description
Join in for the weekly Monero Research Lab meeting.

**When**: Monday, 21 January 2019 @ 17:00 UTC
**Where**: #monero-research-lab (freenode/matrix)

**Agenda**
1. Greetings

2. Ongoing work
a. Payment ID deprecation
b. Block size scaling
c. Transaction size reduction
d. Bulletproofs optimizations

3. New work

4. Questions

# Discussion History
## SamsungGalaxyPlayer | 2019-01-21T19:45:01+00:00
<•sarang> Greetings, everyone
11:02 AM <•suraeNoether> letsdothis.gif
11:02 AM <oneiric_> oneiric o/
11:02 AM <•sarang> I dislike mass pings, but given certain topics, a special ping to sgp_ ArticMine moneromooo knaccc
11:03 AM First, ONGOING WORK
11:03 AM <ArticMine> Hi
11:03 AM — moneromooo looks up
11:03 AM <•sarang> Much discussion about payment ID deprecation has occurred
11:04 AM sgp_ is holding an open meeting to discuss this, on 25 January: https://github.com/monero-project/meta/issues/299
11:05 AM THe current proposal intends to discuss is a deprecation of unencrypted pIDs at next upgrade, followed by a ban on all payment IDs in fall
11:05 AM The main source of contention at this point seems to be whether keeping encrypted pIDs around, whether or not the wallet supports them by default, is necessary or desired
11:06 AM Unless there's something important to talk about regarding this, and its relationship to the upcoming fork, we can table it until sgp_'s meeting
11:07 AM <•suraeNoether> i think it's wise to table the discussion until the meeting
11:07 AM <•sarang> moneromooo has been working on wallet handling of payment IDs, as well as the use of default payment IDs for transaction indistinguishability
11:07 AM ok!
11:07 AM Next is block size scaling
11:07 AM ArticMine recently posted a new proposal \
11:08 AM So the two on the table right now are the dual-median option (presented last time) and ArticMine's new one
11:08 AM <ArticMine> I can go over the details and answer questions
11:08 AM <•sarang> ty ArticMine
11:09 AM Here is the paste on this idea, linked earlier: http://paste.debian.net/hidden/50f142a6/
11:09 AM <lurkinandlearnin> To confirm, the old proposal is this? https://github.com/noncesense-research-lab/Blockchain_big_bang/blob/master/models/Isthmus_Bx_big_bang_model.ipynb
11:09 AM <ArticMine> The key part of  my proposal is to separate the block weight into a long term portion LongTermBlockWeight and the balance
11:10 AM  LongTermBlockWeight - BlockWeight
11:10 AM <•sarang> lurkinandlearnin: look at notebook line [3]
11:11 AM <ArticMine> LongTermBlockWeight does not include the burst potion that can go up to 50x
11:12 AM So the LongTermMedianBlockWeight does not compound at 50x
11:13 AM <•suraeNoether> fwiw for the folks in the audience: one of the reasons block size based on medians is a difficult question is the way medians behave...
11:13 AM most equations that have been proposed here introduce an effective time delay between how max block size is responding to previous block sizes... and it's a difference equation... and introducing time delay to difference equations can introduce very strange behavior like chaos.  (example: https://advancesindifferenceequations.springeropen.com/articles/10.1186/s13662-015-0374-1 )
11:13 AM chaos is bad
11:13 AM so most of these proposals are most easily analyzed with simulations, which provide no guarantee that things won't go crazy. i've been looking into mean-based appraoches instead of median-based approaches; this introduces the possibility that outliers become disproportionately important, but it removes chaos from the equations, so we may be able to design a globally stable approach.
11:13 AM in addition to evaluating articmine's proposal
11:14 AM <ArticMine> This is the key difference with the prior proposal that compounds the LongTermMedianBlockWeight using the entire block
11:14 AM the
11:14 AM <•sarang> Including the simple two-median approach, right ArticMine ?
11:14 AM → rehrar joined (~rehrar@gateway/tor-sasl/rehrar)
11:14 AM <ArticMine> Yes the simple two median approach fails
11:15 AM <•suraeNoether> i'm still not clear on the properties we want out of max block size adjustments
11:15 AM <ArticMine> Since it either compounds the 50x burst (my initial version) or kills the burst over time (smooth's version)
11:15 AM <•sarang> ArticMine: is that paste complete as written?
11:15 AM <•suraeNoether> beyond "ability to go 50x over a slow day to accommodate a christmas day, and to not allow a big bang"
11:15 AM <ArticMine> Yes
11:17 AM <•sarang> Isthmus and I plan to work this in to our existing simulations
11:17 AM His is more complete, but I am doing one for my own education and as a separate check
11:18 AM We shall need to make a decision by freeze time
11:18 AM ArticMine: there are a few subtleties that I'll want to ask you about later
11:19 AM But I also would like to hear the answer to suraeNoether's question
11:19 AM <nioc> nioc_ I did not see any response to smooth's comment.....
11:19 AM you can avoid any sort of consensus issues on *1.4 by making it 1.375 which is adding 3/8
11:20 AM 10:50 PM or some such, but that should be close enough
11:20 AM 10:56 PM overall looks good to me at first reading
11:20 AM 11:02 PM i guess 4/10 is fine too, just slower (but not significant)
11:20 AM <•sarang> that was a rounding issue, I suppose
11:20 AM <moneromooo> If people will fuck up with 1.4, they will fuck up with 1.375.
11:21 AM For interested people, the amp branch has ArticMine's change (untested).
11:21 AM <•suraeNoether> we should just pick a number that can be represented exactly in a computer
11:21 AM <moneromooo> (just the top patch)
11:22 AM Better to pick one that can't. You don't want people to use floating point and think they did it right bevause the number was chosen to make things look right.
11:22 AM <•sarang> branch link: https://github.com/moneromooo-monero/bitmonero/commit/f1ee51c55963d05a78db916d41da7dc5948bb05a
11:22 AM <•suraeNoether> representing 1.4 in a computer is inexact and will cause floating point rounding problems in different pieces of software, but i think 1.375 can be represented in binary exactly and so there is no roundoff problem in that regard...
11:23 AM <•sarang> also, hot dang that was fast moneromooo
11:23 AM <•suraeNoether> one of the things i, personally, would like out of the block size adjustment is this
11:23 AM <ArticMine> smooth's comment would e an improvement if the BlockWeight were a factor of 8 in bytes, but it is not. So in reality it is not a material change
11:23 AM <•suraeNoether> moneromooo: that's a strong argument actually
11:25 AM so, i think block size adjustment can benefit from: forcing the marginal cost of adding an additional transaction in terms of block reward penalty to be greater than the standard fees gained by including that transaction
11:25 AM even if we pick some exotic max_block_size calculation, we should also be changing the block reward penalty this way
11:25 AM <ArticMine> Still I see as an improvement. As per suraeNoether comment above. So we can make the change from 1.4 to 1.375
11:26 AM <•suraeNoether> of course, if the block is nearly full and the block reward is almost zero, adding almost any transaction fees will make up for it
11:26 AM ArticMine: moneromooo just made a strong argument *against* that
11:26 AM so this marginal cost approach will be most effective when block sizes are nowhere near the big bang levels
11:27 AM which is good: providing an incentive to stay reasonable when they are already reasonable
11:28 AM <ArticMine> No When block weight is close to big bang levels LongTermBlockWeight is << BlockWeight
11:29 AM → PauleBert joined (~PauleBert@dslb-188-096-185-204.188.096.pools.vodafone-ip.de)
11:30 AM <•suraeNoether> i'm not talking about your block size proposal; i'm talking about block reward penalty as a function of block size
11:30 AM <lurkinandlearnin> Has any thought been given towards an incentive for miners to create smaller blocks when transaction volume is low? To slow blockchain growth
11:31 AM <•suraeNoether> that's what i was just talking about lurkinandlearnin
11:31 AM <pigeons> lower blockchain growth is probably less important than quicker validation and propogation but the same point applies
11:32 AM <•sarang> lurkinandlearnin: all txns get added eventually if the fee market allows
11:32 AM <•suraeNoether> something isthmus brought up to me: there are only about 150,000 blocks between us and the next hard fork. with the *simple* two-median method will forbid a blowup before the next hard fork.
11:32 AM woops i mean between March and October hard forks
11:33 AM <moneromooo> Yes, starting the penalty before 100% (idea from smooth).
11:33 AM <•suraeNoether> we should consider implementing the simple method *first* and spending time thinking about a more optimal solution, rather than trying to go for broke
11:33 AM <lurkinandlearnin> moneromooo: that sounds like a great idea
11:33 AM <•suraeNoether> moneromooo: yep, smooth had the initial idea of sub-100%-median block penalty; my idea is to make the drop-off nonlinear so that it's more expensive to push block sizes larger in the absence of a healthy fee market
11:33 AM <•sarang> Well, simulations will shortly be done for ArticMine's proposal compared to the current approach and the simple two-median
11:34 AM Presumably the next upgrade will do one of the two options
11:35 AM <•suraeNoether> okay, i don't think we're going to come to any conclusions on this, but it's been a good update
11:35 AM let's move past scaling
11:35 AM <•sarang> Sure thing. We'll talk after simulation data are available
11:35 AM Next is transaction size reduction, for which there is a PR from moneromooo
11:35 AM AFAIK there are no new updates on this otherwise
11:36 AM unless moneromooo you wish to say anything about it?
11:36 AM <moneromooo> I'd just like one of you Noethers to review the code before it goes in.
11:36 AM suraeNoether said he'd have a look.
11:36 AM <•suraeNoether> sarang let's do that *together* tomorrow morning? we can do it over a vidchat since we were going to meet tomorrow anyway
11:37 AM <•sarang> Roger; the math looked correct to me, but I may have neglected to add a comment
11:37 AM ok suraeNoether can do
11:37 AM <•suraeNoether> fun
11:37 AM → mistergo1d joined (~mistergol@185.37.25.30)
11:37 AM <•suraeNoether> as for the semi-final point on the agenda... what's the deal with bulletproofs, anyway? seinfeld.gif
11:37 AM <•sarang> lol
11:37 AM <•suraeNoether> DID YOU GUYS MAKE THINGS FASTER AGAIN
11:38 AM <•sarang> Only a brief update that some BP verifier optimizations didn't make it into the 0.13 release
11:38 AM a very unscientific test on my box resulted in a 64-batch of 2-proofs verifying 60% faster
11:38 AM kudos to moneromooo for continuing to squeeze speed out of those suckers
11:38 AM <lurkinandlearnin> holy smokes
11:39 AM 60% faster than current impl or than pre-BP?
11:39 AM <•sarang> than the 0.13 release code
11:39 AM <•suraeNoether> jeez
11:39 AM <•sarang> that is, 0.13 vs master
11:39 AM as of a few days ago
11:39 AM <•suraeNoether> where did this speedup come from?
11:39 AM <•sarang> Folding in some multiexponentiation operations, as well a host of other voodoo moneromooo can dooo
11:40 AM ⇐ mistergold quit (~mistergol@77.243.30.20) Ping timeout: 240 seconds
11:40 AM <•sarang> So we can brag about the next release making txns smaller and faster again :D
11:40 AM <moneromooo> I did not keep track of which change sped up by how much. I think sarang's single multiexp change is probably the biggest one though.
11:40 AM <•sarang> Let's now discuss NEW WORK
11:40 AM <•suraeNoether> cool!
11:40 AM <•sarang> suraeNoether: your personal updates?
11:41 AM <•suraeNoether> personally, this past week was largely a konferenco administration week for me, contacting speakers and vendors and getting my bank compliant with me
11:41 AM i did research on bulletproofs, linear algebra in cryptography, and our matching paper
11:41 AM <•sarang> I'm sooper excited for this conference
11:41 AM <•suraeNoether> but a lot of my work this week was contacting possible speakers
11:41 AM <•sarang> sounds like we'll have some big names joining us
11:42 AM <•suraeNoether> yes, it's pretty great so far; we are adding more names this week
11:42 AM <•sarang> Any updates on the matching paper suraeNoether ?
11:42 AM <•suraeNoether> my simulations aren't passing unit tests
11:42 AM once they do, i'm making a commit
11:43 AM and then collecting data
11:43 AM so: it's moving forward
11:43 AM <•sarang> excellent
11:43 AM Any questions for suraeNoether ?
11:44 AM OK, I'll go next
11:44 AM <•suraeNoether> oh i had one more thing to bring up
11:44 AM sorry sarang, i don't want to interrupt
11:44 AM <•sarang> np go ahead
11:45 AM <lurkinandlearnin> is there a list of speakers for the conference?
11:45 AM <•suraeNoether> i found all those old Monero Protocol Standards documents I started writing last year, and I'm wondering if folks still want me to compose the v0.1 versions of these rather short text documents into something to put up on our github
11:45 AM <lurkinandlearnin> or not official yet?
11:45 AM <•suraeNoether> lurkinandlearnin: check out konferenco.xyz
11:45 AM the benefit of having the standards instead of a single big zero-to-monero document is this:
11:46 AM we can update each one piecemeal and only update it if something has changed. this reduces overhead work on documentation. and if it's on github, anyone can update them, we don't have to go find kurt magnus or koe
11:46 AM <•sarang> FWIW the ZtM doc is on github and can be PRed
11:46 AM but I see the point about modularity
11:47 AM My pessimistic side worries that updates would fall behind, as they already have on ZtM
11:47 AM <lurkinandlearnin> What aspects of the protocol are covered? Could be something useful to incorporate into the often neglected wiki
11:47 AM as they both sound modular
11:48 AM <•suraeNoether> lurkinandlearnin: essentially similar to the cryptonote standards they released after i reviewed their whitepaper years ago, like this: https://cryptonote.org/cns/cns006.txt
11:48 AM (my whitepaper review would have been moderately better if they wrote those standards before the whitepaper, but hey)
11:48 AM sarang your points are valid
11:48 AM which is why i'm not sure if it's a good idea to devote time to it
11:49 AM <Isthmus> IsthmusCrypto Wiki is a good idea, specs are a good idea. Having experience as a book editor, people making random PRs is a huge nightmare to text style and continuity and often took 4x as long to polish then if SerHack and I had written ourselves.
11:49 AM <•suraeNoether> okay, how about this
11:49 AM <•sarang> Whatever is made available, whether ZtM or wiki or standards, keeping up to date is the most important aspect IMO
11:50 AM I cringe at "text-rendered math" though...
11:50 AM <Isthmus> IsthmusCrypto Maybe we should pick one to be the "reference" documentation and the others follow suite?
11:50 AM <•sarang> Who's responsible for maintenance of each one?
11:50 AM <lurkinandlearnin> Well as long as the version at time of writing is very clear keeping it updated is not so critical
11:50 AM <•suraeNoether> sarang who's responsbile for maintaining anything around here?
11:50 AM <•sarang> lurkinandlearnin: I disagree
11:51 AM <•suraeNoether> how about i just post what i have after making it a little more readable, and if someone wants to run with it they can
11:51 AM <lurkinandlearnin> nice, but not disastrous. If anything having info about how things used to work out there is also useful.
11:51 AM <•suraeNoether> i can post it on my personal github to avoid cluttering the primary\
11:51 AM <•sarang> suraeNoether: I think that'd be useful, to get a better sense of scope of audience
11:51 AM <•suraeNoether> sarang: we can always label them clearly DEPRECATED AND NOT USEFUL. but i think it'd be better to have them out there
11:52 AM <•sarang> good point
11:52 AM <•suraeNoether> okay handing it back to sarang
11:52 AM <•sarang> As long as it's clear what can be considered "closer to canonical"
11:52 AM ⇐ thrmo quit (~thrmo@unaffiliated/thrmo) Quit: Leaving
11:52 AM <•sarang> So I've had some testing and minor optimizations to BPs for the next release, as mentioned earlier
11:53 AM Minor work on simulating block size changes to confirm work by Isthmus on scaling etc.
11:53 AM Recording of new Breaking Monero episodes with sgp_
11:53 AM The usual new lit and project review
11:54 AM and some work on a safe MPC protocol for Bulletproofs for future use
11:54 AM as well as a lot of back-and-forth administrivia on the topics for the Boron upgrade
11:55 AM I am personally in favor of either Boron Betelgeuse or Boron Bellatrix
11:55 AM (as far as names go)
11:55 AM and of course the math for graph matchings, which has been passed back to suraeNoether for simulation data that he is obtaining
11:55 AM <lurkinandlearnin> Betelgeuse will lead to a schism in the community over pronounciation
11:56 AM <•sarang> precisely
11:56 AM It's like the naming of iPhone X... by making it hard to get right, it forces you to think it's better than you are
11:56 AM humbles us all
11:56 AM <lurkinandlearnin> "It gets the people going!"
11:57 AM <•sarang> Any questions for me?
11:57 AM <lurkinandlearnin> what's the next breaking monero topic?
11:57 AM <moneromooo> Hmm... Lightning network things ?
11:58 AM <•sarang> moneromooo: what questions on that?
11:58 AM <Isthmus> IsthmusCrypto "Boron borealis" ?? I think there's a Harry Potter character called Bellatrix, which could get confusing with all the HP-themed MimbleWimble names.
11:58 AM <•sarang> lurkinandlearnin: we have several topics in the lineup, to be arranged
11:59 AM <Isthmus> IsthmusCrypto Also, Breaking Monero = awesome, thanks for all the time going into that series :- D
11:59 AM <moneromooo> Was anything done or thought about recently about anything monero needs for LN or LN style system ?
12:00 PM <•sarang> moneromooo: some of it was an efficient and fungible way to handle protocol aborts, a la noninteractive refunds
12:00 PM that was quietly tabled as several proposals for interactive refunds were thrown around
12:01 PM <moneromooo> Ah yes. It would be nice to see a list of things that are needed in monero as building blocks. In terms of parenthesized AND/OR. I always forget. Or never knew.
12:01 PM <•sarang> That's a good point. Having a well-considered status update will be useful for longer-term planning
12:02 PM Does anyone else have updates to share, before we adjourn?
12:04 PM righto
12:04 PM Thanks to everyone for joining
12:04 PM Our current action items:
12:05 PM (a) simulation data for block size proposals, to make a decision before freeze
12:05 PM (b) final review of transaction size reduction PR
12:05 PM (c) meeting to decide on payment ID deprecation (PLEASE attend or comment on github issue if you have an opinion on this, with justification/data)
12:06 PM — •sarang bangs the gavel

# Action History
- Created by: SarangNoether | 2019-01-21T14:07:13+00:00
- Closed at: 2019-01-21T17:45:15+00:00
