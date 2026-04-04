---
title: 'Research meeting: 18 March 2019 @ 17:00 UTC'
source_url: https://github.com/monero-project/meta/issues/319
author: SarangNoether
assignees: []
labels: []
created_at: '2019-03-16T19:16:31+00:00'
updated_at: '2019-03-18T18:10:39+00:00'
type: issue
status: closed
closed_at: '2019-03-18T18:10:39+00:00'
---

# Original Description
Join in for the weekly Monero Research Lab meeting.

**When**: Monday, 18 March 2019 @ 17:00 UTC
**Where**: #monero-research-lab (freenode/matrix)

**Agenda**
1. Greetings

2. Roundtable
a. Sarang: [output selection](https://github.com/SarangNoether/skunkworks/tree/outputs/outputs), [Bulletproofs MPC](https://github.com/SarangNoether/skunkworks/tree/pybullet-mpc/pybullet) security model, [Lelantus](https://lelantus.io/lelantus.pdf), DLSAG paper, [funding request](https://ccs.getmonero.org/proposals/sarang-2019-q2.html)
b. Surae: graph matching paper, SPECTRE
c. Others?
d. Discussion: [shorter MLSAGs](https://github.com/monero-project/research-lab/issues/52)

3. Questions

4. Action items

# Discussion History
## SarangNoether | 2019-03-18T18:10:39+00:00
    [2019-03-18 12:58:14] * sarang set the topic to Research meeting NOW: https://github.com/monero-project/meta/issues/319
    [2019-03-18 12:58:22] <sarang> OK, let's begin presently; agenda in topic
    [2019-03-18 12:58:48] <xmrmatterbridge> <worriedrise> Thanks :) I hope it is all secure. I/we still need to work on the security proofs
    [2019-03-18 12:59:34] <sarang> 1. GREETINGS
    [2019-03-18 12:59:35] <sarang> Hello all
    [2019-03-18 13:00:01] <suraeNoether> greetings!
    [2019-03-18 13:00:12] <xmrmatterbridge> <worriedrise> Hello
    [2019-03-18 13:00:17] <xmrmatterbridge> <oneiric> hidere
    [2019-03-18 13:00:45] <suraeNoether> worriedrise: i'm pretty sure i can prove that it's an interaction-free instantiation of thring signatures without much effort at all. i spent about an hour working on that proof this weekend, but i haven't uploaded it anywhere yet
    [2019-03-18 13:00:55] <sarang> Let's discuss it shortly per the agenda
    [2019-03-18 13:01:10] <sarang> Since it should warrant plenty of discussion
    [2019-03-18 13:01:13] → el00ruobuob_[m] joined (~el00ruobu@blabour.fr)
    [2019-03-18 13:01:18] <sarang> 2. ROUNDTABLE
    [2019-03-18 13:01:27] <xmrmatterbridge> <worriedrise> I am looking forward to seeing it
    [2019-03-18 13:02:01] <sarang> We have been discussing output selection quite a bit, and should prepare to make a recommendation for the next point release
    [2019-03-18 13:02:41] <sarang> The output age distribution for selections made by the different options are reasonably close to each other under usual chain conditions
    [2019-03-18 13:02:49] <sarang> At this point I'm going to recommend the output-lineup method
    [2019-03-18 13:02:52] <sarang> Any thoughts on this?
    [2019-03-18 13:03:21] <suraeNoether> for now, i favor the lineup method, until we have established a better alternative, or better metrics for analysis
    [2019-03-18 13:03:40] <xmrmatterbridge> <worriedrise> I am fine with that
    [2019-03-18 13:03:50] <sarang> Neat
    [2019-03-18 13:04:04] <moneromooo> For the output lineup method, the parameters (assuming you still use a gamma) are going to be very different.
    [2019-03-18 13:04:36] <sarang> They use the same 2-day mean, but with an average output age determined by the chain (or some portion thereof)
    [2019-03-18 13:04:37] <moneromooo> And they depend on how many outputs there are in the blocks. That seems to be fundamentally wrong to me, even though it seems to work in practice...
    [2019-03-18 13:05:00] <moneromooo> I feels like overfitting/
    [2019-03-18 13:05:12] <sarang> I don't know a better approach that meets our needs
    [2019-03-18 13:05:27] <sarang> The point is they use averaging to smooth out density fluctuations
    [2019-03-18 13:05:28] <suraeNoether> whatever method we end up selecting, we will have to re-estimate our selection parameters, since the distribution technically won't be gamma, for sure
    [2019-03-18 13:05:45] <suraeNoether> the sensitivity to blockchain density is actually a feature not a bug imho
    [2019-03-18 13:05:59] <sarang> Under the famine condition, for example, the averaging means that older outputs are favored more than the 2-day mean would currently do
    [2019-03-18 13:06:04] <moneromooo> I had expected gamma to stay.
    [2019-03-18 13:06:05] ⇐ cardboardoranges quit (~cardboard@65.112.8.199): Quit: cardboardoranges
    [2019-03-18 13:06:12] <sarang> The exp-gamma selection would stya
    [2019-03-18 13:06:29] <sarang> but the parameters use an average output age
    [2019-03-18 13:07:15] <suraeNoether> to sarang's point about famine: real-life spend-time distributions are very much sensitive to blockchain density and vice versa. a famine condition as sarang describes is "what happens if people start spending less and less, or with greater intervals of time between spends?" the answer *should* be that older outputs appear in ring signatures more often
    [2019-03-18 13:07:48] <sarang> I invite people to play around with the algorithms and chain conditions with my simulation code
    [2019-03-18 13:08:15] <suraeNoether> to moo's point: we are still trying to approximate a gamma distribution in terms of the age of one of the next outputs to be confirmed on-chain.
    [2019-03-18 13:08:56] <xmrmatterbridge> <worriedrise> Is anyone looking into the metrics of how many times an output is used in a ring? That should give us soe good insights
    [2019-03-18 13:09:18] <suraeNoether> but either way, we should probably run our own analysis on spend-times and see if the parameters reported in the monerolink paper are sitll reasonable
    [2019-03-18 13:09:22] <sarang> IIRC the statistical average tends toward the fixed ringsize
    [2019-03-18 13:10:17] <sarang> At any rate, if people want to do more analysis, now is the time so we have a solid scheme ready for next release
    [2019-03-18 13:10:59] <sarang> Otherwise: there's working bulletproofs MPC test code now, but the security guarantees depend heavily on the number of rounds and the presence or absence of player precommitments to their values to avoid cancellations
    [2019-03-18 13:11:36] <suraeNoether> worriedrise and sarang: the average number of uses per key with a fixed ring size of R and N total ring signatures is <= R. Why? assume each ring signature has R members, and there are N ring signatures in total. There are at least N keys (one for each ring signature) so the average number of uses per key is total number of uses (N*R) divided by total number of keys (there are N or more of these). So the
    [2019-03-18 13:11:37] <suraeNoether> average uses per key is at most R.
    [2019-03-18 13:11:45] → cardboardoranges joined (~cardboard@65.112.8.199)
    [2019-03-18 13:11:59] <suraeNoether> gratz on working bulletproofs MPC; to be precise you mean "bulletproofed range proof MPCs" correct? not arbitrary bulletproofed statements?
    [2019-03-18 13:12:16] <sarang> range proofs
    [2019-03-18 13:12:19] <suraeNoether> neat
    [2019-03-18 13:12:22] <sarang> but the idea extends to general proofs
    [2019-03-18 13:12:31] <xmrmatterbridge> <worriedrise> Average, yes. But the question is are there rings being over/under-selected?
    [2019-03-18 13:12:37] <sarang> for sure
    [2019-03-18 13:12:59] <xmrmatterbridge> <worriedrise> And how bad is the problem
    [2019-03-18 13:13:00] <suraeNoether> so sarang you've been reading more on lelantus?
    [2019-03-18 13:13:14] <sarang> Yes, and playing around with some of the schemes they use
    [2019-03-18 13:13:24] <sarang> Modifications to BPs and a Groth sigma protocol
    [2019-03-18 13:13:31] <sarang> Nothing to report except that
    [2019-03-18 13:13:43] <sarang> My funding request is open for funding now, and is about 1/3 complete!
    [2019-03-18 13:13:57] <suraeNoether> do you have plans or ideas on how to assess scaling of the lelantus ringct versus ours?
    [2019-03-18 13:14:31] <sarang> Yes, more careful op counts and a better understanding of how to handle commitments in the Groth protocol
    [2019-03-18 13:15:15] <sarang> it's still very pie-in-the-sky at this point
    [2019-03-18 13:15:28] <suraeNoether> okay; need anything from me in your reading about it?
    [2019-03-18 13:15:29] <sarang> suraeNoether: your updates?
    [2019-03-18 13:15:36] <sarang> not at this point
    [2019-03-18 13:16:28] <suraeNoether> okay, so my work this past week has revolved primarily around simulations for my matching code, which i want to describe briefly
    [2019-03-18 13:17:04] <suraeNoether> basically, i'm trying to simulate a blockchain under "realistic enough" circumstances and embed within this simulation some abnormal behavior that an analyzer may be interested in seeking out with machine learning or something like that
    [2019-03-18 13:17:26] <suraeNoether> for example, if we want to model the classic EABE controlled purchase weekly of some illicit stuff, this would correspond to embedding a periodic signal into this blockchain
    [2019-03-18 13:18:01] <suraeNoether> for another example, what if a specific vendor is merely impatient and spends more rapidly than other vendors? drawing from an exponential distribution instead of a gamma, or something along those lines
    [2019-03-18 13:18:31] <suraeNoether> the goal is for my matching algorithm to try  to find this embedded signal and see how good it is at this task, both in terms of false positives and false negatives
    [2019-03-18 13:19:17] <suraeNoether> this can be loosely compared to the methods used in monerolink for testing those approaches, with a major exception: the goal here is to estimate the power of the statistical test over a wide range of hypotheses, while all the "background noise" is behaving *just as one would expect with our wallet distributions.*
    [2019-03-18 13:20:26] <suraeNoether> so i want to sit down with sarang later today to discuss output selection simulation methods. after all, if we suspect we'll be implementing one of four different schemes, it makes sense to implement these in the simulations and test their performance... but it's very easy to go overboard with such tests and over-engineering a big experiment
    [2019-03-18 13:20:52] <suraeNoether> i want to come up with a very precise set of tests to get to the heart of what we want to test and what information we need in order to make informed decisions and move forward
    [2019-03-18 13:21:31] <suraeNoether> on teh plus side, we are ending up with a pretty rigorous simulation suite for simulating monero blockchains.
    [2019-03-18 13:22:00] <sarang> nice
    [2019-03-18 13:22:19] <xmrmatterbridge> <worriedrise> Could we keep track of a counter to keep track of how outputs may be over/under-selected, as I mentioned before?
    [2019-03-18 13:22:31] <suraeNoether> my other updates involve dlsag security stuff and reading about generalizations of the keccak sponge construction to the family of parazoa hash functions. but those are less interesting: the first paper is nearing completion, and the second is pie-in-the-sky
    [2019-03-18 13:22:39] <xmrmatterbridge> <worriedrise> I believe this may be a good goal
    [2019-03-18 13:22:41] <moneromooo> I think you can do that with one of the tools in src/blockchain_utilities
    [2019-03-18 13:23:02] <sarang> worriedrise: how would this data affect your opinion on output selection?
    [2019-03-18 13:23:43] <xmrmatterbridge> <worriedrise> If we can find certain outputs that are consistently being under selected, that is more likely to be the true soender
    [2019-03-18 13:23:46] <xmrmatterbridge> <worriedrise> spender
    [2019-03-18 13:23:55] <xmrmatterbridge> <worriedrise> And conversely
    [2019-03-18 13:24:32] <xmrmatterbridge> <worriedrise> I believe that might be already happening with the approach of choosing uniformly on small blocks, not just to coinbase outputs
    [2019-03-18 13:25:08] <sarang> We're certainly seeing outputs being selected with improper weighting based on block size, no doubt
    [2019-03-18 13:25:19] <xmrmatterbridge> <worriedrise> Coinbase outputs are just easy to spot, which is why people noticed them
    [2019-03-18 13:25:21] <sarang> The numbers for output-lineup are much better on that
    [2019-03-18 13:25:27] <sarang> My sim tool can provide those numbers
    [2019-03-18 13:25:46] <suraeNoether> so, that's an interesting heuristic, actually, worriedrise, but i'm not too worried about it for the following reason
    [2019-03-18 13:25:47] <sarang> e.g. how often are outputs in blocks of size X selected relative to their occurrence on the chain
    [2019-03-18 13:25:54] ⇐ cardboardoranges quit (~cardboard@65.112.8.199): Quit: cardboardoranges
    [2019-03-18 13:25:59] <xmrmatterbridge> <worriedrise> Yes, but we should check if further methods don't do that as well inadvertently
    [2019-03-18 13:26:18] <sarang> What do you mean? We can check those numbers for all the proposed methods
    [2019-03-18 13:26:36] <sarang> just run the sim tool, choosing your preferred selection method and preferred chain density condition
    [2019-03-18 13:26:39] <sarang> (including the real chain)
    [2019-03-18 13:26:46] <xmrmatterbridge> <worriedrise> I believe we can. I was not sure we were
    [2019-03-18 13:26:50] <sarang> Ah ok
    [2019-03-18 13:26:58] ⇐ TheoStorm quit (~TheoStorm@host-g4sn8hj.cbn1.zeelandnet.nl): Quit: Leaving
    [2019-03-18 13:26:59] <sarang> I added that functionality a week or two ago to the tool
    [2019-03-18 13:27:09] <sarang> Feel free to run it if you want to play around with the results
    [2019-03-18 13:27:11] <sarang> (link in agenda)
    [2019-03-18 13:27:21] <xmrmatterbridge> <worriedrise> Thanks. I hadn't seen it
    [2019-03-18 13:27:24] <sarang> np
    [2019-03-18 13:27:34] <suraeNoether> so, basically my primary lack of concern comes from variance
    [2019-03-18 13:27:44] <xmrmatterbridge> <worriedrise> How about for the actual blockchain, do we have that data?
    [2019-03-18 13:27:52] <suraeNoether> if average ring use is <= 11 when we have a fixed ring size 11, the variance in use per output is going to be *huge* compared to 11
    [2019-03-18 13:28:25] → cardboardoranges joined (~cardboard@65.112.8.199)
    [2019-03-18 13:28:29] <sarang> worriedrise: that data meaning...
    [2019-03-18 13:28:32] <suraeNoether> the power of that heuristic would be absolutely awful
    [2019-03-18 13:28:41] <sarang> The chain density, or the frequency of selections based on poor weighting?
    [2019-03-18 13:28:50] <xmrmatterbridge> <worriedrise> Agreed. But we can see the problem with coinbase outputs. Maybe looking at the data we can see it with other outputs too
    [2019-03-18 13:29:39] <xmrmatterbridge> <worriedrise> The data of outputs use in the actual blockchain. Maybe you have that already
    [2019-03-18 13:29:56] <xmrmatterbridge> <worriedrise> Not just for the simulations
    [2019-03-18 13:30:18] <sarang> I don't have data for how frequently outputs from small blocks are overselected
    [2019-03-18 13:30:36] <sarang> I have data for how the current selection scheme performs under simulated selections from the actual chain
    [2019-03-18 13:31:11] <xmrmatterbridge> <worriedrise> That should be good enough for now. I am still curious though :)
    [2019-03-18 13:31:16] <suraeNoether> we can chase heuristics all day long; let's move along for now
    [2019-03-18 13:31:17] <suraeNoether> yeah
    [2019-03-18 13:31:24] <xmrmatterbridge> <worriedrise> Okay
    [2019-03-18 13:31:39] <suraeNoether> worriedrise: nothing stopping you from compiling some data and taking a gander and seeing if any conclusions can be drawn
    [2019-03-18 13:31:47] <suraeNoether> i'm in favor of more data, generally
    [2019-03-18 13:31:50] ⇐ cardboardoranges quit (~cardboard@65.112.8.199): Client Quit
    [2019-03-18 13:32:27] <xmrmatterbridge> <worriedrise> I don't know how to do that, but I will look into it and see what I can do.
    [2019-03-18 13:32:51] <sarang> suraeNoether: anything else to report from your update?
    [2019-03-18 13:33:12] <suraeNoether> nothing to report yet, although I suspect a draft of the matching paper is incoming some time this week (but i said that last week too)
    [2019-03-18 13:33:23] <sarang> righto
    [2019-03-18 13:33:48] <sarang> worriedrise/randomrun had an idea for making MLSAGs shorter: https://github.com/monero-project/research-lab/issues/52
    [2019-03-18 13:34:09] <sarang> This has grown into an idea for general MLSAGs that applies a kind of key aggregation
    [2019-03-18 13:34:26] <sarang> Care to comment or discuss worriedrise?
    [2019-03-18 13:34:49] <xmrmatterbridge> <worriedrise> Sure
    [2019-03-18 13:35:23] <xmrmatterbridge> <worriedrise> That is just something that seemed reasonable, but I have no security proofs at this time
    [2019-03-18 13:35:41] <suraeNoether> for simple ringct transactions, the approach uses a Musig-style key aggregation with LSAG signatures to construct a RingCT, instead of using MLSAG signatures to construct RingCT. The overall size of the signatures are smaller, although verification time takes as much time (roughly) as previously.
    [2019-03-18 13:35:45] <xmrmatterbridge> <worriedrise> The idea is to use a hashed linear combination to aggregate keys
    [2019-03-18 13:35:59] <xmrmatterbridge> <worriedrise> into a single signing key
    [2019-03-18 13:36:08] <xmrmatterbridge> <worriedrise> Linkability is harder
    [2019-03-18 13:36:12] <sarang> right
    [2019-03-18 13:36:19] <sarang> at worst, it would require a new image format
    [2019-03-18 13:36:26] <sarang> at best, a second image-style point, correct?
    [2019-03-18 13:36:38] <suraeNoether> the unforgeability proof because of the structure of this, essentially boils down to a very similar proof to the proof of security for the thring signatures paper (https://eprint.iacr.org/2018/774.pdf)
    [2019-03-18 13:36:50] <suraeNoether> linkability *is* harder
    [2019-03-18 13:36:51] <xmrmatterbridge> <worriedrise> Correct, but that may work well with the previous one
    [2019-03-18 13:36:57] <suraeNoether> *nod*
    [2019-03-18 13:37:24] <xmrmatterbridge> <worriedrise> Have you been able to write down how that would work, without changing the key image?
    [2019-03-18 13:37:37] <sarang> You mean the general form?
    [2019-03-18 13:37:45] <sarang> I have not
    [2019-03-18 13:37:52] <xmrmatterbridge> <worriedrise> I would love to see that bc it would work for DLSAGs s well
    [2019-03-18 13:37:58] <sarang> The specific initial form would work with the existing key image, by adding the second point as you mentioned in the post
    [2019-03-18 13:38:00] <xmrmatterbridge> <worriedrise> I see
    [2019-03-18 13:38:20] <sarang> But I have only just started examining the scheme in detail today!
    [2019-03-18 13:38:24] <xmrmatterbridge> <worriedrise> Yes, but just for aggregating the amount component
    [2019-03-18 13:38:59] <xmrmatterbridge> <worriedrise> It seems to me that we need different sets of constants for different key images, as it stands
    [2019-03-18 13:39:17] <xmrmatterbridge> <worriedrise> But with the change to the key image, they all aggregate together
    [2019-03-18 13:39:37] <xmrmatterbridge> <worriedrise> The problem is that that doesn't work for DLSAGs as they are right now
    [2019-03-18 13:39:37] <sarang> right
    [2019-03-18 13:39:56] <xmrmatterbridge> <worriedrise> Since their key images are not defined over a common point
    [2019-03-18 13:40:06] <xmrmatterbridge> <worriedrise> I am trying to see a way
    [2019-03-18 13:40:17] <xmrmatterbridge> <worriedrise> Would love suggestions :)
    [2019-03-18 13:40:27] <sarang> It is a very clever idea regardless
    [2019-03-18 13:40:36] <xmrmatterbridge> <worriedrise> Thanks
    [2019-03-18 13:40:50] <sarang> Once this meeting is over, I will be continuing to review it
    [2019-03-18 13:40:58] <xmrmatterbridge> <worriedrise> It still looks too good to be true. Please double chack that carefully
    [2019-03-18 13:41:40] <xmrmatterbridge> <worriedrise> Great
    [2019-03-18 13:42:01] <sarang> Any questions for worriedrise on this?
    [2019-03-18 13:42:11] → crCr62U0 joined (~crCr62U0@gateway/tor-sasl/crcr62u0)
    [2019-03-18 13:42:12] <sarang> We will certainly continue to keep investigating it
    [2019-03-18 13:43:04] <suraeNoether> Brief update on Konferenco: we are beginning to purchase travel tickets for speakers
    [2019-03-18 13:43:12] <suraeNoether> tickets to the konferenco will be on sale soon(tm)
    [2019-03-18 13:43:33] <sarang> very excited!
    [2019-03-18 13:43:33] <suraeNoether> if anyone wants to submit an abstract, please don't hesitate! konferenco.xyz
    [2019-03-18 13:43:43] <suraeNoether> we have a great lineup of speakers, and we need more!
    [2019-03-18 13:44:01] <sarang> Perhaps we can convince worriedrise/randomrun :D
    [2019-03-18 13:44:04] <xmrmatterbridge> <worriedrise> I saw you will be in NY in May too
    [2019-03-18 13:44:20] <xmrmatterbridge> <worriedrise> Another conference
    [2019-03-18 13:44:22] <h4sh3d[m]> What kind of speaker are you looking for?
    [2019-03-18 13:44:26] <suraeNoether> we are having more speakers added later today, by the way; i believe we may have someone from the human rights foundation and/or an activist working in venezuela to come speak, and we are having the executive director at coincenter, Jerry Brito, come speak, too
    [2019-03-18 13:44:50] <suraeNoether> h4sh3d[m]: any technical content related to monero or privacy enhancing technologies in general are welcome
    [2019-03-18 13:45:16] <suraeNoether> we are having some speakers on the social impacts of these technologies too; scholarly work only, no ICOs, a gathering of intelleckshuals
    [2019-03-18 13:45:33] <suraeNoether> basically: if you have an idea for an abstract, you may as well submit it
    [2019-03-18 13:45:50] ⇐ iDunk quit (~iDunk@unaffiliated/idunk): Read error: Connection reset by peer
    [2019-03-18 13:45:57] <suraeNoether> worriedrise: i will be at MCC yes
    [2019-03-18 13:46:12] <sarang> lucky suraeNoether !
    [2019-03-18 13:46:27] <suraeNoether> i have a feeling i'll be put to work organizing. :P
    [2019-03-18 13:46:43] <xmrmatterbridge> <worriedrise> Since we are talking about other technologies, what do you think of the idea of having monero addresses as Bitmessage addresses, as I proposed
    [2019-03-18 13:46:58] <xmrmatterbridge> <worriedrise> https://github.com/monero-project/research-lab/issues/51
    [2019-03-18 13:47:18] <xmrmatterbridge> <worriedrise> I saw that there is an issue with the order of encryption and authentication
    [2019-03-18 13:47:21] <sarang> Seems clever if used correctly!
    [2019-03-18 13:47:25] <xmrmatterbridge> <worriedrise> But assuming we get over that
    [2019-03-18 13:47:37] <xmrmatterbridge> <worriedrise> Thank
    [2019-03-18 13:47:52] <suraeNoether> yeah, it shouldnt' be too rough, i just haven't sat down and thought about it yet
    [2019-03-18 13:48:15] <xmrmatterbridge> <worriedrise> Would you care to explain what the problem is
    [2019-03-18 13:48:20] <suraeNoether> the easy way to fix it is with a tailored key structure
    [2019-03-18 13:48:23] <suraeNoether> okay, so basically
    [2019-03-18 13:49:11] <suraeNoether> when you are encrypting and authenticating, you don't want to authenticate-and-then-encrypt, followed by verification-then-decryption
    [2019-03-18 13:49:32] <suraeNoether> er.. followed by decryption-then-verification i mean
    [2019-03-18 13:49:33] <sarang> (swap the latter version)
    [2019-03-18 13:49:35] <sarang> yeah
    [2019-03-18 13:49:44] <suraeNoether> this is a bad way to do things because you end up decrypting something without knowing who it came from
    [2019-03-18 13:50:09] <suraeNoether> if, on the other hand, the ciphertext is signed by the authenticating key, you know whoever signed it approves of the ciphertext
    [2019-03-18 13:50:17] <suraeNoether> so first you check the signature, then you decrypt
    [2019-03-18 13:50:30] <nioc> no idea if it has any relevance but I believe it was rbrunner that was using bitmessage for his multisig scheme (MMS)
    [2019-03-18 13:50:42] <xmrmatterbridge> <worriedrise> What is wrong with not knowing who it came from?
    [2019-03-18 13:50:56] → iDunk joined (~iDunk@unaffiliated/idunk)
    [2019-03-18 13:51:08] <xmrmatterbridge> <worriedrise> Can't you stablish that later?
    [2019-03-18 13:51:16] <xmrmatterbridge> <worriedrise> Once you see the key?
    [2019-03-18 13:51:34] <suraeNoether> well, here's an example
    [2019-03-18 13:51:43] <sarang> You wouldn't know if the encrypted message had been altered
    [2019-03-18 13:51:48] <suraeNoether> of why the implementation is dangerous
    [2019-03-18 13:53:08] <xmrmatterbridge> <worriedrise> I would know that is was signed by the accompanying key. Are you saying I wouldn't know if the key was switched?
    [2019-03-18 13:54:11] <suraeNoether> the extreme and silly example is "what if an app developer decrypts the ciphertext and starts executing it as code while checking in parallel that the signature is valid? then you are running arbitrary code without knowledge of what's in it or whatever." and this seems like it has an easy fix, right, is that the developer should be doing things in the other order...
    [2019-03-18 13:54:16] <xmrmatterbridge> <worriedrise> At first contact, I would just have to take wahtever key it was given, but from that point on, I would know whether further messges are signed by the same person
    [2019-03-18 13:54:28] <suraeNoether> but actually, the answer is no, the encrypt/decrypt should be going in the other order so a bad developer can't make that mistake
    [2019-03-18 13:54:38] <suraeNoether> this is using a silly but very malicious example
    [2019-03-18 13:54:56] <suraeNoether> there are more harmless examples like sarang's mention that you don't know if the ciphertext is actually going to decrypt to the intended plaintext.
    [2019-03-18 13:55:07] <suraeNoether> and to be frank, that's the root of the problem
    [2019-03-18 13:55:22] <moneromooo> What is an app developer fails to check for signature check fail and starts executing the ciphertext as code ?
    [2019-03-18 13:56:05] <suraeNoether> ciphertext is indistinguishable from white noise, so their code would do nothing with high probability :D
    [2019-03-18 13:56:07] <sarang> what a ride that would be
    [2019-03-18 13:56:17] <moneromooo> The ciphertext is under attacker control.
    [2019-03-18 13:56:18] <suraeNoether> https://link.springer.com/chapter/10.1007/3-540-44448-3_41 worriedrise this paper is pretty seminal in the area
    [2019-03-18 13:56:27] <xmrmatterbridge> <worriedrise> I see. I have to think more about that one. I wonder how that problem is handled in Bitmessage currently
    [2019-03-18 13:56:46] <suraeNoether> moneromooo: ah yeah, that's true, but at that point your developer is merely executing random code it's received from an extra party
    [2019-03-18 13:56:56] <moneromooo> That was what you assumed too :)
    [2019-03-18 13:57:22] <sarang> In the interest of time, let's review action items and then continue further discussion
    [2019-03-18 13:57:57] <sarang> I will keep talking with suraeNoether about output selection if he has additional thoughts/concerns, will review the MLSAG change in detail, and continue toying around with Lelantus
    [2019-03-18 13:58:04] <sarang> and watch my funding request =p
    [2019-03-18 13:58:07] <suraeNoether> hm moneromooo no, in my example, the developer decrypts first :D
    [2019-03-18 13:58:27] <sarang> suraeNoether: your action items for the week?
    [2019-03-18 13:58:56] <suraeNoether> 1) funding request, 2) monthly report for last month, 3) simulations, 4) dlsag security, 5) reduced mlsag security
    [2019-03-18 13:59:07] <suraeNoether> oh and fun reading on parazoa
    [2019-03-18 13:59:27] <sarang> Neato
    [2019-03-18 13:59:35] <sarang> Any final questions or remarks before we formally adjourn?
    [2019-03-18 13:59:56] <sarang> Thanks for joining us worriedrise today
    [2019-03-18 14:00:12] <xmrmatterbridge> <worriedrise> My pleasure. Thnks for having me
    [2019-03-18 14:01:04] <sarang> Thanks to everyone for attending. We are now adjourned!
    [2019-03-18 14:01:19] * sarang set the topic to Research meeting Mondays @ 17:00 UTC

# Action History
- Created by: SarangNoether | 2019-03-16T19:16:31+00:00
- Closed at: 2019-03-18T18:10:39+00:00
