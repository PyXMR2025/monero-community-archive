---
title: 'Research meeting: 4 March 2019 @ 17:00 UTC'
source_url: https://github.com/monero-project/meta/issues/309
author: SarangNoether
assignees: []
labels: []
created_at: '2019-03-03T21:52:45+00:00'
updated_at: '2019-03-10T14:44:26+00:00'
type: issue
status: closed
closed_at: '2019-03-04T22:43:31+00:00'
---

# Original Description
Join in for the weekly Monero Research Lab meeting.

**When**: Monday, 4 March 2019 @ 17:00 UTC
**Where**: #monero-research-lab (freenode/matrix)

**Agenda**
1. Greetings

2. Roundtable
a. Sarang: [monthly report](https://www.reddit.com/r/Monero/comments/avdrbs/february_monthly_report_from_sarang_noether/), [Bulletproofs MPC](https://github.com/SarangNoether/research-lab/tree/mpc/source-code/pybullet)
b. Surae
c. SamsungGalaxyPlayer: [public mining selection algorithm](https://github.com/monero-project/monero/issues/5222)
d. Others?

3. Questions

4. Action items

# Discussion History
## SarangNoether | 2019-03-04T22:43:31+00:00
    [2019-03-04 11:55:50] * sarang set the topic to Research meeting NOW: https://github.com/monero-project/meta/issues/309
    [2019-03-04 11:59:14] <sarang> Shall we begin?
    [2019-03-04 11:59:20] <sarang> 1. GREETINGS
    [2019-03-04 11:59:23] <sarang> Hello everyone
    [2019-03-04 11:59:31] <oneiric_> hullo
    [2019-03-04 12:00:18] — needmoney90 waves
    [2019-03-04 12:00:46] — ErCiccione[m] lurks in Italian
    [2019-03-04 12:01:09] <sarang> Let's go over our usual 2. ROUNDTABLE
    [2019-03-04 12:01:20] <sarang> In the spirit of fairness and generosity, I will go first :D
    [2019-03-04 12:01:33] <sarang> I posted my February monthly report (see agenda for link); comments welcome
    [2019-03-04 12:01:57] <sarang> Besides the things listed there, I have initial working code for a Bulletproofs MPC (link in agenda also)
    [2019-03-04 12:02:17] <sarang> moneromooo has been toying around with the idea of a coinjoin-type scheme, for which this MPC would be efficient and useful
    [2019-03-04 12:02:33] <sarang> It still needs a lot of additional testing and work, but the initial code is operational
    [2019-03-04 12:03:10] <sarang> And along with suraeNoether, still making edits and fixes to an upcoming paper in collaboration with other researchers for submission
    [2019-03-04 12:03:34] <sarang> This week I'll be doing some MPC code cleanup and adversarial unit tests
    [2019-03-04 12:03:41] <sarang> Any questions for me on these topics?
    [2019-03-04 12:04:10] <suraeNoether> i have one
    [2019-03-04 12:04:15] <oneiric_> link for repo?
    [2019-03-04 12:04:22] <sarang> Link at the agenda: https://github.com/monero-project/meta/issues/309
    [2019-03-04 12:04:30] <oneiric_> thanks :)
    [2019-03-04 12:04:31] <sarang> the code is in super early stages
    [2019-03-04 12:04:55] <suraeNoether>  the bulletproof coinjoin-style mpc: is this described in any level of detail anywhere outside of the bulletproofs paper? i think i get how bulletproofed MPC works, but if they are intended for use in a coinjoin-style way with Monero, i would like to see an explanation of how
    [2019-03-04 12:05:13] <sarang> Ah good point. The BP paper only described the MPC protocol, and hinted at applications
    [2019-03-04 12:05:34] <sarang> moneromooo has been working on the Monero-specific coinjoin at his "multi" branch
    [2019-03-04 12:06:05] <suraeNoether> has coinjoin ringct been described outside of code?
    [2019-03-04 12:06:15] <sarang> Not that I know of. It's on my list :D
    [2019-03-04 12:06:25] <suraeNoether> got it
    [2019-03-04 12:06:31] <sarang> FWIW having the bulletproofs code refactored to allow for MPC is a good idea anyway
    [2019-03-04 12:06:36] <suraeNoether> agreed
    [2019-03-04 12:06:42] <sarang> It turns the usual multi-output proof into a trivial MPC with one player
    [2019-03-04 12:06:51] <sarang> and of course the verifier is completely unchanged
    [2019-03-04 12:07:03] <suraeNoether> i'm not trying to imply that the MPC work is not important or unrelated to monero; it is both important and related. i just wanted to see what had been written.
    [2019-03-04 12:07:21] <suraeNoether> my update is simple, too.
    [2019-03-04 12:07:31] <suraeNoether> I'm working on my February report right now. i am working on  my funding request for next quarter. sarang and i are both working into our proposals one big change from previous proposals: primarily a pay-up-front clause to prevent MRL researchers from having their paychecks degrade over the funding period.
    [2019-03-04 12:07:32] — sarang passes baton to suraeNoether
    [2019-03-04 12:07:46] <sarang> Ooh good point on the new funding model
    [2019-03-04 12:07:59] <sarang> We discussed this publicly a lot
    [2019-03-04 12:09:06] <suraeNoether> in addition to that, i've passed the proofs-stuff back to our co-authors, who i'm chatting with almost daily on the publication; our deadlines have been pushed back twice now, so i asked for permission to explain what we are working on, and I got a "little bit" of consent, so
    [2019-03-04 12:09:39] <suraeNoether> basically, sarang and i have been working with two authors on formalizing the DLSAG stuff, and i've been working on security proofs while sarang has been working on getting timing results for comparing to vanilla monero ringct
    [2019-03-04 12:09:59] <sarang> Yeah, the paper has specific constructions for payment channels et al.
    [2019-03-04 12:10:08] <suraeNoether> (one of the reasons i wanted a written description of bulletproof coinjoin is to see how well it will mesh with the new scheme
    [2019-03-04 12:10:21] <sarang> Oh interesting. I hadn't thought of that part
    [2019-03-04 12:10:28] <suraeNoether> yeah, long story short: the primitives required in monero for a lightning network
    [2019-03-04 12:10:40] <sarang> The bulletproofs MPC protocol is independent of how the coinjoin signatures are done, FWIW
    [2019-03-04 12:11:11] <suraeNoether> sarang: right, the bulletproofs mpc is merely to securely compute a range proof collaboratively, right, wihtout revealing your hidden values to your cosigners
    [2019-03-04 12:11:20] <sarang> righto
    [2019-03-04 12:11:23] <sarang> But I get your point
    [2019-03-04 12:12:17] <suraeNoether> in addition to that, my plate this week consists of 1) reading about flyclient and making a proposal (if any, even if it is to ignore flyclient), 2) matching simulations are finally moving a little bit after some late night saturday work, and 3) my feb report + next quarter funding request
    [2019-03-04 12:12:23] <suraeNoether> that finishes up my brief roundtable update
    [2019-03-04 12:12:49] <suraeNoether> i would love to hear from anyone else who has done any research this past week. isthmus is always on fire with productivity (poor guy has 3rd degree burns)
    [2019-03-04 12:14:05] <suraeNoether> oh i'm looking at the agenda here and we have sgp_
    [2019-03-04 12:14:17] <suraeNoether> i believe sgp suggested a different input selection algorithm for pools: https://github.com/monero-project/monero/issues/5222
    [2019-03-04 12:14:35] <sgp_> yes, thanks suraeNoether for the link to the Github discussion
    [2019-03-04 12:15:12] <sgp_> this discussion is only around the public POOL selection algorithm, not the selection algorithm for other users
    [2019-03-04 12:15:24] ⇐ thrmo quit (~thrmo@unaffiliated/thrmo): Quit: Leaving
    [2019-03-04 12:16:01] → el00ruobuob joined (~el00ruobu@blabour.fr)
    [2019-03-04 12:16:01] <sgp_> I expect this to be non-controversial and to have no negative impact on any party, but if you feel otherwise, I'd love your comment in the issue
    [2019-03-04 12:16:13] <sgp_> Unless there are any questions, we can keep going
    [2019-03-04 12:16:22] <suraeNoether> some of the thoughts presented in your github discussion reflect some of the thoughts that isthmus has had on the matter with multi-input transactions, so I actually think this discussion is a little more broad than you suspect
    [2019-03-04 12:16:49] <suraeNoether>  but also: since input selection isn't consensus, any pool could *decide* to do this
    [2019-03-04 12:16:56] <sgp_> it could be. this concept as I presented it has been thrown around since early 2018
    [2019-03-04 12:16:57] <moneromooo> I'd like to have a confirmation that it does not harm anything else before I code it up.
    [2019-03-04 12:17:15] <moneromooo> (from sarang and/or surae)
    [2019-03-04 12:17:15] <suraeNoether>  the problem as I see it is that it reduces things in the following way
    [2019-03-04 12:17:23] <sarang> I have looked over it briefly this morning but want to think about it in more detail
    [2019-03-04 12:18:38] <suraeNoether> if we have a ring size N*M, and the average number of outputs per transaction is M, and ring members are selected by transaction instead of by input, there is a strong argument that this reduces the effective ring size to N.
    [2019-03-04 12:18:59] <suraeNoether> the true ring size is N*M, but there are only N transactions included as ring memb ers
    [2019-03-04 12:19:08] <sarang> Right, it's a version of binning
    [2019-03-04 12:19:19] <sarang> and if you can eliminate a bin provably or heuristically, it's a problem
    [2019-03-04 12:19:23] → el00ruobuob_[m] joined (~el00ruobu@blabour.fr)
    [2019-03-04 12:19:49] <sgp_> I argue the typical drawbacks of binning do not apply here, since the public pools make all of the transaction details public anyway
    [2019-03-04 12:20:45] <sgp_> Ring signatures could provide 0 protection and the pools wouldn't be worse off
    [2019-03-04 12:21:11] <suraeNoether> uhm well
    [2019-03-04 12:21:47] ⇐ el00ruobuob quit (~el00ruobu@blabour.fr): Ping timeout: 240 seconds
    [2019-03-04 12:21:48] <suraeNoether> the concern isn't these public pool's privacy
    [2019-03-04 12:21:58] <suraeNoether> it's their behavior negatively impacting the privacy of other participatns in the monero ecosystem
    [2019-03-04 12:22:10] <sgp_> The goal isn't to restore the effective ringsize of the pool rings. It's to preserve the integrity of the pool outputs used in other rings
    [2019-03-04 12:22:17] <sarang> right
    [2019-03-04 12:23:26] <suraeNoether> sgp_: here's my problem, as i see it
    [2019-03-04 12:23:30] <suraeNoether> another problem anyway
    [2019-03-04 12:23:53] <suraeNoether> let's say i am a pool and i have 3 xmr and i want to send 1xmr each to: (1) miner alice and (2) miner bob and (3) myself as change
    [2019-03-04 12:24:23] <suraeNoether> er... 3 outputs
    [2019-03-04 12:24:27] <suraeNoether> assume each output is 1xmr
    [2019-03-04 12:24:30] <sgp_> got it :)
    [2019-03-04 12:24:32] <suraeNoether> under your proposal, i construct 3 separate ring signatues, all of which contain all 3 of these outputs
    [2019-03-04 12:24:40] <suraeNoether> moreover, i'm a public pool
    [2019-03-04 12:24:49] <suraeNoether> anyone will be able to see that all 3 outputs have been spent
    [2019-03-04 12:25:03] <sgp_> wait a sec
    [2019-03-04 12:25:27] <suraeNoether> i have outputs A, B, and C. I want to send A to alice, B to bob, and C to charlie. they all came from the same transaction, so i have to include A, B and C in my rings
    [2019-03-04 12:25:38] <suraeNoether> if i want to send all 3, this guarantees anyone can see they have been spent
    [2019-03-04 12:27:08] <sgp_> this input selection algorithm proposal is meant to handle the change outputs, not the source (eg: coinbase). Those require another more aggressive change
    [2019-03-04 12:27:48] <sgp_> I'm slightly confused by how you are handling these outputs
    [2019-03-04 12:28:10] <sgp_> If you have 3 XMR in output A, you create a transaction to Alice, Bob, yourself with outputs B, C, D
    [2019-03-04 12:28:38] <sgp_> Then you create your next transaction with ring {B, C, D}
    [2019-03-04 12:29:02] <sgp_> to make unclear which of B,C,D is the change output
    [2019-03-04 12:29:44] <suraeNoether> no, that's not what i mean, i misspoke, let me try again really quick
    [2019-03-04 12:29:57] <sgp_> under this current proposal, A is known to be spent still. it doesn't fix that problem
    [2019-03-04 12:31:10] <suraeNoether> ughhhh you know what i need to think about this more, because the pool won't have 3 outputs from a single transaction. it's a pool, so it'll have a bunch of single outputs, each from individual transactions
    [2019-03-04 12:31:22] <suraeNoether> so my example falls apart
    [2019-03-04 12:31:27] <suraeNoether> but i think we should think about it a bit more
    [2019-03-04 12:31:53] <suraeNoether> oh but i suppose it could have a bunch of change transactions
    [2019-03-04 12:32:05] <suraeNoether> okay, i can manufature a problematic exmaple, but let's do it after the meeting
    [2019-03-04 12:32:54] <sarang> roger
    [2019-03-04 12:33:04] <sarang> Does anyone else have research of interest to share?
    [2019-03-04 12:33:08] <sgp_> sure, and I'm not saying this is a perfect solution that defends against all heuristics, but it's an incremental improvement over the status quo in every case I've found so far. doesn't mean there aren't more. move on :)
    [2019-03-04 12:33:30] <sarang> We can also merge this with 3. QUESTIONS from anyone on any research-related topic
    [2019-03-04 12:34:33] <oneiric_> some questions on kdf interaction, but maybe off-topic
    [2019-03-04 12:34:44] <sarang> Fire away; we have time
    [2019-03-04 12:35:22] <oneiric_> so, i2p is considering reddsa from zcash as an offline signing algo
    [2019-03-04 12:36:06] <oneiric_> reddsa has a unique way of generating blinding material 'alpha' to generate new blinded pravte key
    [2019-03-04 12:36:23] <oneiric_> other than that, identical to eddsa
    [2019-03-04 12:36:58] <sarang> OK, I wasn't familiar with this construction
    [2019-03-04 12:37:02] <oneiric_> looking for a link to alpha generation, one moment
    [2019-03-04 12:38:22] <oneiric_> https://geti2p.net/spec/proposals/123-new-netdb-entries#blinding-calculations
    [2019-03-04 12:39:27] <oneiric_> and the proposed red25519: https://geti2p.net/spec/proposals/146-red25519
    [2019-03-04 12:39:34] <suraeNoether> okay
    [2019-03-04 12:40:01] <oneiric_> is there anything obviously dangerous, or gotchas that you can see?
    [2019-03-04 12:40:03] <sarang> So the difference is the deterministic derivation of the private key offset alpha
    [2019-03-04 12:40:26] <oneiric_> sarang yeah that's how i understand it
    [2019-03-04 12:41:11] <sarang> Well if an adversary is able to gain any advantage in determining the hash inputs used to derive alpha, not good
    [2019-03-04 12:41:37] <oneiric_> they have control over the destination, but its hashed
    [2019-03-04 12:41:57] <suraeNoether> oneiric_:  seems like the strength of it relies up on the "secret" input
    [2019-03-04 12:42:48] <suraeNoether> someone who uses an empty secret (or just "0" or a badly selected password or something), then someone could brute force lots of destinations and datetimes and keep them all in a big table and look them up when needed
    [2019-03-04 12:43:33] <oneiric_> oh, yeah that's bad. totally undermines the point of the scheme
    [2019-03-04 12:44:06] <suraeNoether> the next question down is whether they should switch to SHA256 and the answer is "no" because afaik hkdf is basically hmac used as a kdf, and that's what i've been advocating for about a year
    [2019-03-04 12:44:20] <suraeNoether> wow "afaik hkdf hmac kdf"
    [2019-03-04 12:44:21] <oneiric_> what would you suggest as an alternative for alpha generation, or are there checks one could do to prevent bad selection?
    [2019-03-04 12:44:39] <oneiric_> blake2b sane alternative, yeah?
    [2019-03-04 12:45:09] <suraeNoether>  oneiric_ i don't think there is a protection against using crappy randomness
    [2019-03-04 12:45:41] <suraeNoether> the hash function selected isn't a big deal as long as HKDF is correctly implemented as an HMAC, even crappy hash functions can produce indistinguishable results
    [2019-03-04 12:45:48] <suraeNoether>  but let's say you got clever and you said
    [2019-03-04 12:46:22] <suraeNoether> "instead of using secret, let's use HKDF(secret) or SHA256(secret)!" but then you can still be brute forced and you need some salt... which kicks the randomness can down the road to the salt.
    [2019-03-04 12:47:08] <sarang> In the interest of time, let's finish up and move discussion outside of the formal meeting time
    [2019-03-04 12:47:21] <sarang> 4. ACTION ITEMS
    [2019-03-04 12:47:34] <oneiric_> absolutely appreciate both your inputs sarang and suraeNoether
    [2019-03-04 12:47:57] <sarang> I will review sgp_'s proposal in more detail, finish up MPC code and more robust tests, and hopefully get that DLSAG-related paper out the door so we can post publicly
    [2019-03-04 12:48:13] <gingeropolous> so I'm curious on where MRL stands on SPECTRE and, in general, switching from nakamoto-consensus. Was there a write-up from the previous investigation? I'm particularly interested because if monero ever actually achieves a strong decentralized network with many miners, the existing consensus system could make things really unstable. So I guess one possible area of investigation is how capable is nakamoto-consensus in a strong
    [2019-03-04 12:48:13] <gingeropolous> decentralized network? I.e., if we had 3k nodes, all solo mining at 200 h/s, with transactions coming randomly from all the nodes, how well would the network actually function? Would it just be reorging constantly, with broken ring sigs causing txs to drop from existence?
    [2019-03-04 12:48:18] <sarang> Later this month I'll post my next funding request, which as suraeNoether will have upfront payment to hedge against volatility
    [2019-03-04 12:48:33] <gingeropolous> sorry, was waiting for something and hit enter
    [2019-03-04 12:48:36] <sarang> both SPECTRE and PHANTOM have scaling issues
    [2019-03-04 12:48:46] <sarang> and different guarantees
    [2019-03-04 12:48:58] <sarang> there was a proposal to do a sort of hybrid between them, but AFAIK it has not been formally analyzed
    [2019-03-04 12:49:12] <suraeNoether> gingeropolous: spectre is neat for a few reasons but crappy for scaling (although that part is totally mitigatable with const-time spectre). the neat stuff about spectre is that it's robust against partitions of the network
    [2019-03-04 12:49:27] <suraeNoether> in nakamoto consensus, if the network is split into two pieces, both sides continue on and write to their ledgers...
    [2019-03-04 12:49:41] <suraeNoether> but when they re-merge, only the writes on one side of the split ever become final
    [2019-03-04 12:49:48] <suraeNoether>  (except for the non-conflicting ones)
    [2019-03-04 12:50:15] <suraeNoether> in spectre, on the other hand, writes made on both sides of the split have a chance of being merged into the "complete" ledger
    [2019-03-04 12:50:38] <suraeNoether> so in that sense, together with some probability arguments, it's more robust than nakamoto
    [2019-03-04 12:50:45] <sarang> I still remain bullish on an eventual general graph-based consensus mechanism
    [2019-03-04 12:51:29] <suraeNoether> same. as tony arcieraierhal on twitter likes to complain about, the nakamoto consensus isn't actually a very good "solution" to byzantine consensus because of the partitioning property described above.
    [2019-03-04 12:51:55] <suraeNoether> https://en.wikipedia.org/wiki/CAP_theorem : nakamoto scores low on the P in CAP
    [2019-03-04 12:52:36] <sarang> suraeNoether: your action items for this week?
    [2019-03-04 12:52:39] <suraeNoether> spectre sacrifices C for P, i think
    [2019-03-04 12:53:18] <suraeNoether> 1) feb  report. 2) FFS request for next quarter. 3) matching simulations. 4) dlsag paper modifications. 5) reading about flyclient and mmr. i've back-burnered const-time spectre
    [2019-03-04 12:53:56] <suraeNoether> sarang: your action items?
    [2019-03-04 12:53:57] <sarang> Sounds good
    [2019-03-04 12:54:04] <sarang> Any final comments before we formally wrap up?
    [2019-03-04 12:54:11] <sarang> Ah, I already stated mine!
    [2019-03-04 12:54:23] <sarang> I will review sgp_'s proposal in more detail, finish up MPC code and more robust tests, and hopefully get that DLSAG-related paper out the door so we can post publicly
    [2019-03-04 12:54:29] <suraeNoether> oh i see that at the top of the section now
    [2019-03-04 12:55:07] <sarang> OK, thanks to everyone for attending. We are now adjourned!


# Action History
- Created by: SarangNoether | 2019-03-03T21:52:45+00:00
- Closed at: 2019-03-04T22:43:31+00:00
