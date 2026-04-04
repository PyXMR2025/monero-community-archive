---
title: 'Research meeting: 16 December 2019 @ 17:00 UTC'
source_url: https://github.com/monero-project/meta/issues/419
author: SarangNoether
assignees: []
labels: []
created_at: '2019-12-12T21:00:41+00:00'
updated_at: '2019-12-16T18:28:36+00:00'
type: issue
status: closed
closed_at: '2019-12-16T18:28:36+00:00'
---

# Original Description
Join in for the weekly Monero Research Lab meeting.

**When**: Monday, 16 December 2019 @ 17:00 UTC
**Where**: #monero-research-lab (freenode/matrix)

**Agenda**
1. Greetings

2. Roundtable

3. Questions

4. Action items

# Discussion History
## SarangNoether | 2019-12-16T18:28:35+00:00
    [2019-12-16 11:59:58] <sarang> GREETINGS
    [2019-12-16 12:00:35] <suraeNoether> howdy!
    [2019-12-16 12:02:30] <suraeNoether> suppose we should move onto the roundtable?
    [2019-12-16 12:02:42] <sarang> Might as well
    [2019-12-16 12:02:47] <sarang> Who shall begin?
    [2019-12-16 12:03:23] <suraeNoether> I'm going to ping isthmus
    [2019-12-16 12:03:36] <suraeNoether> in the hopes that he can describe a bit of the data science work he's currently doing
    [2019-12-16 12:03:58] <Isthmus> n3ptune and I have been looking at block rewards
    [2019-12-16 12:04:11] <Isthmus> Lots of funky stuff going on
    [2019-12-16 12:04:17] <sarang> How so?
    [2019-12-16 12:04:46] — Isthmus is digging up figures
    [2019-12-16 12:05:43] <Isthmus> Here's a bad figure, and I'll try to have a nicer one by the end of the meeting
    [2019-12-16 12:05:45] <Isthmus> https://usercontent.irccloud-cdn.com/file/f9F4XDd3/image.png
    [2019-12-16 12:05:49] <Isthmus> x-axis is block height
    [2019-12-16 12:05:56] <Isthmus> y-axis is the total reward claimed by the miner
    [2019-12-16 12:06:00] <Isthmus> (fresh + fees)
    [2019-12-16 12:06:24] <Isthmus> The trend is basically our emission curve (the bottom of the traces)
    [2019-12-16 12:06:44] <Isthmus> The data points above the trend are miners who made good blocks with fees on top of reward
    [2019-12-16 12:06:53] <suraeNoether> exponential decay shape of the graph comes from our emission curve (fees are related to block reward). is the piecewise break from bulletproofs?
    [2019-12-16 12:06:59] <Isthmus> The anomalies below the line are what's interesting
    [2019-12-16 12:07:28] <Isthmus> There's a few distinct events that happened
    [2019-12-16 12:07:38] <Isthmus> For each, we can tell a few things:
    [2019-12-16 12:08:12] <Isthmus> Exactly which blocks were mined by that miner/pool/software
    [2019-12-16 12:08:14] <Isthmus> (linkability)
    [2019-12-16 12:08:28] <Isthmus> And exactly how long it took them to notice that they were making suboptimal blocks, and fix the software
    [2019-12-16 12:09:03] <Isthmus> You can tell a bit more by adding size as the color
    [2019-12-16 12:09:06] <Isthmus> https://usercontent.irccloud-cdn.com/file/HUoctx7I/image.png
    [2019-12-16 12:09:08] <Isthmus> Scale is blue to yellow
    [2019-12-16 12:09:20] <Isthmus> So there I've zoomed into a small section
    [2019-12-16 12:10:31] <Isthmus> Looking at the band from 1225000 to 1275000ish
    [2019-12-16 12:10:58] <Isthmus> It looks like the blocks claiming *less* reward than empty blocks are about the same size as those produced by others
    [2019-12-16 12:11:05] <suraeNoether> that graph is gorgeous bro
    [2019-12-16 12:11:13] <Isthmus> thx :- )
    [2019-12-16 12:11:36] <sarang> Odd behavior
    [2019-12-16 12:11:51] <sarang> The definition of suboptimal, you might say...
    [2019-12-16 12:11:55] <Isthmus> Yeah, because their sizes are about the same as the surrounding blocks, here are two guesses for what might be happening
    [2019-12-16 12:12:24] <Isthmus> Maybe other miners are making high-fee big blocks, and the ones below the trend are the suckers that make big blocks after the mempool has been tapped out for high-fee txns
    [2019-12-16 12:12:51] <Isthmus> But based on how bounded the second (anomalous) trend is, I think it might just be a software bug?
    [2019-12-16 12:13:04] <Isthmus> I just discovered this like 20 hours ago, so I haven't done full exploration
    [2019-12-16 12:13:14] <Isthmus> I'll be able to drill down into the blocks and actually figure out what was going on
    [2019-12-16 12:13:30] <Isthmus> (that's about where it's at right now)
    [2019-12-16 12:14:43] <sarang> It's really interesting to see it mapped out so clearly
    [2019-12-16 12:16:16] <suraeNoether> thanks so much, isthmus; it seems to me like i've read at least one paper about purposely claiming smaller rewards for a variety of game-theoretic reasons...
    [2019-12-16 12:16:20] <suraeNoether> i'm going to try to dig up at least one of htem
    [2019-12-16 12:16:25] ⇐ TheoStorm quit (~TheoStorm@host-p8vu8h.cbn1.zeelandnet.nl): Remote host closed the connection
    [2019-12-16 12:18:06] <suraeNoether> i have so many questions about this
    [2019-12-16 12:18:45] <sarang> It would be good to know which particular software (if it's specific) leads to this, due to how common it appears to be
    [2019-12-16 12:20:01] <sarang> suraeNoether: your roundtable?
    [2019-12-16 12:21:08] <suraeNoether> yeah, sure: Matching. I *think* i'm *one* bug away from getting all the data i want. and I'm talking to Insight Data Science to throw a fellow at the simulation results to help me come up with best-practices recommendation
    [2019-12-16 12:21:59] <suraeNoether> my current bug is silly and strange, in that i'm not adding the number of nodes and edges my software is expecting. initially i thought this was a problem with computing the number of available ring members or something like that, but i'm still trying to figure it out
    [2019-12-16 12:22:47] <sarang> Do you have code ready that can reproduce it?
    [2019-12-16 12:23:14] <suraeNoether> it occurs in a random test in testSimulator.py, not any of my deterministic tests
    [2019-12-16 12:23:33] <suraeNoether> so i'm still hunting down exactly the conditions that lead to the bug, and attempting to isolate it as a new unit test
    [2019-12-16 12:24:10] <suraeNoether> the graph theoretic component is working perfectly, the analysis component exploring parameter space is working perfectly, but the simulator keeps hitting this snag and then we're off to the races
    [2019-12-16 12:24:16] <endogenic> oops, here
    [2019-12-16 12:24:20] <suraeNoether> welcome
    [2019-12-16 12:24:29] <endogenic> suraeNoether: you dont think V could make all those masks by himself even in 20 years though?
    [2019-12-16 12:25:22] <sarang> suraeNoether: is the currently-pushed code the version you're working with?
    [2019-12-16 12:27:03] <suraeNoether> yes, the commit i pushed this morning
    [2019-12-16 12:27:18] <suraeNoether> to matching-buttercup branch
    [2019-12-16 12:28:27] <suraeNoether> so, someone brought up by sidechannel the question about whether i should re-implement the sims in rust in the hopes that the improved explicit references of rust would help find the errors
    [2019-12-16 12:28:57] <sarang> Do you suspect that could be the origin of the errors?
    [2019-12-16 12:29:14] <suraeNoether> i think refactoring the whole codebase is a last-ditch effort for finding the bugs, though
    [2019-12-16 12:29:19] <sarang> If they're simply algorithmic mistakes, switching to Rust might not do anything
    [2019-12-16 12:29:49] <suraeNoether> no; i literally think i'm merely predicting the number of nodes and edges incorrectly based on the total nodeset as opposed to only the nodes that can be spent.
    [2019-12-16 12:30:00] <endogenic> have you tried log statements?
    [2019-12-16 12:30:06] <endogenic> secret weapon
    [2019-12-16 12:30:10] <suraeNoether> and i'm in the midst of tracking that down
    [2019-12-16 12:30:14] <Isthmus> Could you tweak the simulation to be 3 blocks long, 2 transactions per block, with spend pattern & ring member selection algorithm = pull from previous block
    [2019-12-16 12:30:23] <Isthmus> Would the issue persist and be easy to spot by eye?
    [2019-12-16 12:30:38] <sarang> endogenic: your suggestion reminded me of https://xkcd.com/451/ =p
    [2019-12-16 12:31:17] ⇐ Dean_Guss quit (~dean@gateway/tor-sasl/deanguss): Remote host closed the connection
    [2019-12-16 12:31:20] <endogenic> except that i am
    [2019-12-16 12:31:23] <endogenic> :P
    [2019-12-16 12:31:48] <sarang> Nono, the statement about logs!
    [2019-12-16 12:31:56] <sarang> Sorry, digression
    [2019-12-16 12:32:11] <suraeNoether> isthmus unfortunately i believe the problem may be in the ring selection algorithm i have written (which is only uniform at this point), so that would reduce the problem away
    [2019-12-16 12:32:36] <suraeNoether> but i'm attempting something similar next
    [2019-12-16 12:32:45] <suraeNoether> right now, debugger is my friend
    [2019-12-16 12:33:21] <suraeNoether> sarang, how about you?
    [2019-12-16 12:33:27] <endogenic> log statements are nice because you can let the whole thing run
    [2019-12-16 12:33:38] <sarang> Several things to mention
    [2019-12-16 12:33:40] <endogenic> debugger is also nice.
    [2019-12-16 12:34:17] <sarang> I modified the linkability and non-frameability definitions in Triptych, and would like to see if they can be directly used in CLSAG as well
    [2019-12-16 12:34:38] <sarang> I've come around on Backes' definition of linkability
    [2019-12-16 12:34:58] <sarang> I updated the CLSAG linkable anonymity definition, as well as its proof
    [2019-12-16 12:35:27] <sarang> Reviewed a paper by the Zcoin folks on hierarchical Groth commitment proofs
    [2019-12-16 12:35:50] <sarang> Looked over some changes that Zcoin made to fix a problem they had relating to Groth proofs (doesn't apply to Triptych)
    [2019-12-16 12:36:23] <sarang> Worked out some example code for doing inversion via an MPC for use in computing certain linking tag constructions
    [2019-12-16 12:36:43] <sarang> and wrote out some simple draft MPC ideas for RCT3 and Triptych, which for now assume honest-but-curious players
    [2019-12-16 12:37:50] <suraeNoether> nice!
    [2019-12-16 12:37:57] <sarang> The good news on MPC is that it's certainly possible to collaboratively compute the inverse-based key images used in those proving systems
    [2019-12-16 12:38:21] <sarang> The bad news is it requires something akin to Paillier encryption, which leads to some computational overhead
    [2019-12-16 12:39:11] <suraeNoether> hmmm are you looking into the MPC stuff for linking tag constructions due to the constructions and usage of linking tags in Triptych?
    [2019-12-16 12:39:19] <sarang> (note that my example code should _not_ be taken to be a secure Paillier implementation)
    [2019-12-16 12:39:33] <sarang> Yep, the MPC is to handle linking tags in Triptych, RCT3, and Omniring
    [2019-12-16 12:39:55] <sarang> Even though Omniring can use traditional linking tags, even that construction still requires an underlying inversion
    [2019-12-16 12:40:23] <sarang> There are also affine quantities to compute, but those are understood
    [2019-12-16 12:42:12] <suraeNoether> refresh my memory: which, if any, of those 3 require self-sends?
    [2019-12-16 12:42:23] <sarang> None of them
    [2019-12-16 12:42:40] <sarang> DLSAG and Lelantus would require this
    [2019-12-16 12:44:26] <endogenic> LELANTUS
    [2019-12-16 12:44:27] <suraeNoether> okay, so what, in your heart of hearts, are you hoping for from linking tags?
    [2019-12-16 12:45:01] <sarang> The problem, previously, was that it was not clear how to enable multisig support when the linking tags require a secret key inversion
    [2019-12-16 12:45:03] → silur joined (silur@gateway/vpn/nordvpn/silur)
    [2019-12-16 12:45:17] <suraeNoether> aaaaah
    [2019-12-16 12:45:19] <sarang> Now that there's an understood MPC to compute this, it means multisig support is feasible
    [2019-12-16 12:45:25] <suraeNoether> gotcha gotcha
    [2019-12-16 12:45:31] <suraeNoether> you had questions about multisig for me
    [2019-12-16 12:45:38] <sarang> The downside to the MPC is that Paillier can't take advantage of the efficient curve libraries we all know and love
    [2019-12-16 12:45:38] <suraeNoether> we can address them now or after the meeting if you like
    [2019-12-16 12:45:40] <silur> hoi sorry for being late
    [2019-12-16 12:45:46] <Isthmus> holla
    [2019-12-16 12:45:46] <suraeNoether> long time no see silur
    [2019-12-16 12:45:52] <endogenic> whatup silur
    [2019-12-16 12:46:09] <sarang> Paillier requires RSA modulus stuff (but there aren't issues with trusted setup etc.)
    [2019-12-16 12:47:08] <sarang> Encryption and decryption require exponentiation with variable modulus
    [2019-12-16 12:47:36] <sarang> So computationally-constrained devices would need to able to support this
    [2019-12-16 12:47:57] <sarang> s/to able/to be able
    [2019-12-16 12:48:24] <suraeNoether> so are we hoping for an MPC to compute inversion-based key images... such that the MPC is more consistent with the development history of monero/cryptonote? ie based on the DL setting in Ed25519 instead of RSA?
    [2019-12-16 12:48:53] <suraeNoether> or at least, one of the items on our "wish we had" list?
    [2019-12-16 12:49:05] <sarang> Such a thing would be great, but as you pointed out, getting the required homomorphicity would imply a DL break, or some such thing
    [2019-12-16 12:49:12] <silur> can you elaborate on "inversion based key images"?
    [2019-12-16 12:49:23] <silur> or shall I just review it from the log?
    [2019-12-16 12:49:43] <sarang> Key images / linking tags in newer proving systems use the form `(1/x)*U`
    [2019-12-16 12:49:55] <suraeNoether> rather than x*H(X)
    [2019-12-16 12:49:59] <suraeNoether> U is fixed, yes?
    [2019-12-16 12:50:11] <sarang> Here the division is an inverse, `x` is the secret key, and `U` is either globally fixed or depends on the proof statement
    [2019-12-16 12:50:17] <sarang> but it's public
    [2019-12-16 12:50:36] <suraeNoether> uhmmmm wait a moment:
    [2019-12-16 12:50:37] <sarang> It's globally fixed in the more efficient versions of the proving systems
    [2019-12-16 12:50:56] <suraeNoether> my comment had to do with an efficient group-to-scalar map that had any sort of homomorphicity built in
    [2019-12-16 12:51:41] <suraeNoether> oh oh oh
    [2019-12-16 12:51:44] <suraeNoether> i get what you are saying
    [2019-12-16 12:51:55] <sarang> For context: https://github.com/SarangNoether/skunkworks/tree/inverse-mpc
    [2019-12-16 12:52:37] <sarang> The inverse.py script shows how the process works, and the markdown documents describe one possible use for RCT3/Triptych (again, with many assumptions on the players)
    [2019-12-16 12:53:14] <sarang> The encryption homomorphicity is important for the MPC method that Gennaro and Goldfeder introduce
    [2019-12-16 12:54:13] <suraeNoether> so most generally, each person has a secret x_i and there is a function f such that you want to compute f(x_1, ..., x_n)*U with some friends. you were using f(x_1, ..., x_n) = 1/sum(x_i) ?
    [2019-12-16 12:54:26] <suraeNoether> you know what: let's talk about this after the meeting
    [2019-12-16 12:54:33] <sarang> Yeah, better for after meeting
    [2019-12-16 12:55:06] <suraeNoether> so, isthmus, myself, and sarang have all brought the room up to speed. does anyone else want to talk about any monero-related research they are doing?
    [2019-12-16 12:56:05] <silur> can't we somehow exploit the bootle inner-product encryption with a killian randomization here somehow? the killian randomization preserves linear combinations so everything before multiplying with U is the same
    [2019-12-16 12:56:10] <silur> but individual inputs are useless
    [2019-12-16 12:56:36] <silur> and at the last step the same inner-product for the last vector reduces into a Z_p element?
    [2019-12-16 12:56:55] → DeanGuss joined (~dean@gateway/tor-sasl/deanguss)
    [2019-12-16 12:57:40] <sarang> I don't see how to directly apply that to the share derivation in Gennaro
    [2019-12-16 12:57:54] <sarang> The multiplicative-share to additive-share method, I mean
    [2019-12-16 12:58:05] <sarang> (which is the point of their Paillier-based protocol)
    [2019-12-16 12:58:33] <silur> Oh the Genaroo-Goldfeder method IS a hard requirement
    [2019-12-16 12:58:41] <silur> then we can't inded :)
    [2019-12-16 12:58:47] <silur> I wasn't aware it's a must-have
    [2019-12-16 12:59:01] <sarang> Well, we don't _need_ to use Gennaro-Goldfeder
    [2019-12-16 12:59:41] <sarang> but it seems reasonably efficient and useful if you can accept the homomorphicity requirement
    [2019-12-16 13:01:43] <sarang> In the interest of time, let's move to ACTION ITEMS
    [2019-12-16 13:01:55] <sarang> Mine are to continue work on the MPC stuff, get CLSAG definitions ported as necessary (would like to discuss with suraeNoether as well), and get final review on the Triptych draft to get posted to IACR
    [2019-12-16 13:03:05] <silur> triptych? O.o
    [2019-12-16 13:03:13] <sarang> ?
    [2019-12-16 13:03:22] <suraeNoether> mine is to hunt down and kill my final bug, work on the churn report, review the triptych draft (finally) and continue chatting with isthmus about getting a data science fellow working with me on matching/churn
    [2019-12-16 13:03:23] <silur> I was not familiar with that, will look into
    [2019-12-16 13:03:32] <suraeNoether> it's a paper sarang is presently writing
    [2019-12-16 13:03:32] <silur> too much meetings missed :D
    [2019-12-16 13:03:51] <sarang> silur: Triptych is a linkable ring signature construction based on Groth 1-of-many commitment proofs
    [2019-12-16 13:04:05] <silur> <3
    [2019-12-16 13:04:07] <sarang> Preprint draft forthcoming
    [2019-12-16 13:04:22] <sarang> There's a super-efficient version for which I can't reduce soundness to a known hardness assumption
    [2019-12-16 13:04:28] <sarang> If you want to take a look silur, most welcome
    [2019-12-16 13:04:35] <sarang> The less-efficient version does reduce nicely
    [2019-12-16 13:04:54] <silur> yea I'd be more than happy to look into
    [2019-12-16 13:04:57] <sarang> neat
    [2019-12-16 13:05:07] <sarang> OK, I suppose we can formally adjourn and continue discussions as desired


# Action History
- Created by: SarangNoether | 2019-12-12T21:00:41+00:00
- Closed at: 2019-12-16T18:28:36+00:00
