---
title: 'Research meeting: 11 March 2020 @ 17:00 UTC'
source_url: https://github.com/monero-project/meta/issues/445
author: SarangNoether
assignees: []
labels: []
created_at: '2020-03-05T13:01:49+00:00'
updated_at: '2020-03-12T02:09:49+00:00'
type: issue
status: closed
closed_at: '2020-03-12T02:09:49+00:00'
---

# Original Description
Join in for the weekly Monero Research Lab meeting.

**When**: Wednesday, 11 March 2020 @ 17:00 UTC
**Where**: #monero-research-lab (freenode/matrix)

**Agenda**
1. Greetings

2. Roundtable

3. Questions

4. Action items

# Discussion History
## SarangNoether | 2020-03-12T02:09:49+00:00
    [2020-03-11 12:59:44] <sarang> OK, let's begin the meeting!
    [2020-03-11 12:59:56] <sarang> Agenda is here: https://github.com/monero-project/meta/issues/445
    [2020-03-11 13:00:03] <sarang> Logs will be posted there after the meeting
    [2020-03-11 13:00:09] <suraeNoether> good morning
    [2020-03-11 13:00:11] <sarang> First on the list, GREETINGS
    [2020-03-11 13:00:13] <sarang> hi
    [2020-03-11 13:00:59] — selsta lurking for CLSAG updates
    [2020-03-11 13:01:03] <sarang> Note that because of a recent time change for the United States and elsewhere, these meetings will take place at 17:00 UTC instead of 18:00 UTC
    [2020-03-11 13:01:12] <ArticMine> hi
    [2020-03-11 13:01:21] — sarang will wait a few moments for folks to arrive
    [2020-03-11 13:02:05] <Isthmus> heya sarang and artic
    [2020-03-11 13:02:12] — Isthmus puts on lab coat and goggles
    [2020-03-11 13:02:53] <sarang> I suppose we can move on to ROUNDTABLE
    [2020-03-11 13:02:58] <sarang> Who wishes to share research topics of interest?
    [2020-03-11 13:03:15] <vtnerd> hi
    [2020-03-11 13:03:37] <UkoeHB_> Hi
    [2020-03-11 13:03:43] <suraeNoether> well
    [2020-03-11 13:03:55] <suraeNoether> i want to give a brief two-part update
    [2020-03-11 13:03:58] <sarang> Go ahead suraeNoether!
    [2020-03-11 13:05:15] <suraeNoether> firstly, personally: i'm going to have to take a break from monero for a few weeks while i get this medical stuff figured out. importantly: i'm not stopping work. I just don't know how much time i can actually contribute practically.
    [2020-03-11 13:05:57] <sarang> Oof, sorry to hear this. I hope everything goes well for you suraeNoether
    [2020-03-11 13:06:46] <ArticMine> sorry to hear this. I hope all goes well
    [2020-03-11 13:07:29] <suraeNoether> secondly: my research into matching is a hydra where fixing one bug is revealing handfuls of more bugs, and i'm getting super frustrated with it. this is particularly important work for a few reasons, but for right now i don't anticipate movement any time soon. one of the reasons that this has become so frustrating to me is that certain threats to monero that are going to become more likely over the
    [2020-03-11 13:07:30] <suraeNoether> next several years to be presenting themselves that make the answers that lie within this work *lower priority* than other things. i mean this very specifically in the following sense
    [2020-03-11 13:08:15] ⇐ kl_ quit (uid344501@gateway/web/irccloud.com/x-vsgxpnnigobzpawe): Quit: Connection closed for inactivity
    [2020-03-11 13:08:18] <suraeNoether> everyone should know that our anonymity reduces to something like the one-more decisional diffie hellman problem, and our unforgeability reduces to something like one-more discrete logarithm
    [2020-03-11 13:08:44] <suraeNoether> both of these are known to not be hard for quantum adversaries, and while quantum computers are not yet practical...
    [2020-03-11 13:09:25] <suraeNoether> it doesn't matter what ring size we use if china goes "manhattan project" on quantum computers and turns their resulting computing power on de-anonymizing privacy coins in secret.
    [2020-03-11 13:10:07] <suraeNoether> my work on matching would give us answers to questions like "how large should ring sizes be *assuming the underlying problem that our anonymity rests upon is hard to solve*" but we know that this problem is only going to be hard over the short term
    [2020-03-11 13:10:12] <sarang> FWIW such a "quantum adversary" could wreak havoc on basically the entire global internet
    [2020-03-11 13:10:32] <suraeNoether> indeed ^ but that's in fact exactly all the more reason to become resistant to a quantum adversary sooner rather than later
    [2020-03-11 13:10:56] <UkoeHB_> How realistic is a quantum adversary?
    [2020-03-11 13:10:57] <ArticMine> ^ I agree
    [2020-03-11 13:11:04] <suraeNoether> if it takes 3 years to migrate to a quantum-secure system, and we hope something like clsag or triptych has a 3 year shelf life, then we should be looking at what will be practical 6 years from now
    [2020-03-11 13:11:15] <sarang> In the shorter term, understanding the effects of ring size on matching-type analysis is useful for knowing how large to make ring size for a next-gen protocol
    [2020-03-11 13:11:22] <Isthmus> Uhm
    [2020-03-11 13:11:43] <Isthmus> Would an adversary with a quantum computer break ring signatures or just decrypt the transactions?
    [2020-03-11 13:12:01] <suraeNoether> both: they can compute the discrete log of every one-time key and then they just own all of monero
    [2020-03-11 13:12:10] <Isthmus> Yeah, I'd just do that.
    [2020-03-11 13:12:15] <suraeNoether> yeah
    [2020-03-11 13:12:17] <suraeNoether> so like
    [2020-03-11 13:12:25] <sarang> Once you have key discrete logs, you can check key images
    [2020-03-11 13:12:31] <suraeNoether> matching: important. investigating quantum-secure schemes: higher priority, even over a relatively short 3-year term
    [2020-03-11 13:12:54] <suraeNoether> so every time i kill a bug in my matching code, i become more painfully aware: i'm fighting the wrong hydra
    [2020-03-11 13:13:20] <sarang> I still think it's very valuable
    [2020-03-11 13:13:20] <Isthmus> Yeah, we've been doing some quantum vs crypto experiments at Insight lately
    [2020-03-11 13:13:24] <suraeNoether> long story short, i'm prsently working on a summary-of-knowledge of quantum-resistant RingCT-type protocols, 3 of which have been proposed in the past 3 years
    [2020-03-11 13:13:29] <sarang> Otherwise, "bigger rings are better" is a qualitative statement
    [2020-03-11 13:13:38] <suraeNoether> just for community education reasons
    [2020-03-11 13:13:41] <suraeNoether> sarang: absolutely agreed
    [2020-03-11 13:14:13] <sarang> My recent work on Triptych-2 and chain simulations shows, as expected, that ring size has a large effect on verification complexity
    [2020-03-11 13:14:22] <UkoeHB_> Can you also evaluate how realistic a quantum adversary is? I recall general skepticism of them ever materializing
    [2020-03-11 13:14:36] <sarang> So choosing the smallest rings that do the job is important
    [2020-03-11 13:14:53] <suraeNoether> UkoeHB_: yeah, so basically here's a qualitative answer to that question
    [2020-03-11 13:15:08] <Isthmus> We're already working on 5 [actual] qbits
    [2020-03-11 13:15:21] <Isthmus> (Insight working on IBM equipment)
    [2020-03-11 13:15:30] <Isthmus> Expecting this to scale in the next few years
    [2020-03-11 13:15:31] <suraeNoether> you may recall the sensationalist headlines a few months ago: https://www.eurekalert.org/pub_releases/2020-02/aps-teo022720.php
    [2020-03-11 13:15:42] <suraeNoether> quantum supremacy is probably a bad term but
    [2020-03-11 13:15:59] <suraeNoether> before these researchers did what they did, the *fastest way to figure out what a quantum computer can do* would be to *simulate it on a classical computer*
    [2020-03-11 13:16:15] <sarang> Quantum supremacy is a poor metric for usefulness IMO
    [2020-03-11 13:16:25] <sarang> Such problems are typically highly contrived
    [2020-03-11 13:16:29] <suraeNoether> because of these guys' work, that is no longer the case: there now exist quantum computers that cannot be simulated more quickly than they can operate. this is a critical benchmark for scaling quantum
    [2020-03-11 13:16:33] <Isthmus> @surae should I just loop in my quantum/crypto engineer for a few weeks, so you can focus on the matching hydra?
    [2020-03-11 13:16:50] <Isthmus> They're already looking into the schemes, and would probably be happy to work on Monero
    [2020-03-11 13:17:34] <suraeNoether> google's bristlecone has 72 qubits running
    [2020-03-11 13:17:44] <suraeNoether> isthmus: let's set up a call for later this week
    [2020-03-11 13:17:55] <vtnerd> well I have to say it ... quantum computers are BS, they just spin hyperbole but go nowhere. There was a discussion about this on metzdowd
    [2020-03-11 13:18:38] <Isthmus> Given retroactive denonymization doesn't really matter if they're 5 or 15 years off, we gotta hustle to protect Monero users in 2020
    [2020-03-11 13:18:49] <suraeNoether> do you mean like computers based on quantum principles will never work, vtnerd? can you clarify?
    [2020-03-11 13:18:56] → Osiris1 joined (Michael_@unaffiliated/osiris1)
    [2020-03-11 13:18:59] <suraeNoether> isthmus ^ bingo
    [2020-03-11 13:19:21] <vtnerd> someone discussed the progress made on metzdowd. Its been very little over 25+ years
    [2020-03-11 13:19:46] <vtnerd> the researchers have alwasy been just on the edge of making it a reality
    [2020-03-11 13:20:39] <suraeNoether> okay well
    [2020-03-11 13:20:50] <suraeNoether> the researchers into QC i've spoken with disagree
    [2020-03-11 13:20:55] <suraeNoether> and that's an appeal to authority
    [2020-03-11 13:21:09] <vtnerd> admitedly this isn't my expertise, but theres time tradeoffs investigating these QC resitistent systems
    [2020-03-11 13:21:55] <suraeNoether> but i think it's absolutely silly to say that very little progress has occurred over 25 years, and it's even sillier to assume that no progress will be made ala cold fusion, and i think it's even sillier to propose that we, say, avoid quantum-secure implementations rather than looking into the costs and benefits and time horizons of implementing them
    [2020-03-11 13:22:28] <vtnerd> and the one thing thats bizarre, is when someone builds a QC system, we basically ahve to reboot on general purpose computing projects, no? Like one year out are they even cracking crypto?
    [2020-03-11 13:23:05] <suraeNoether> well, i don't want to take more time on this: my update is that i have to step back from monero for awhile, and i'm looking into RLWE-based ring signatures
    [2020-03-11 13:23:14] <Isthmus> Y'all know the tech cycle. Many-year winters leads to the most exciting explosions. AI, crypto, quantum... the pattern repeats
    [2020-03-11 13:23:18] <suraeNoether> i'll still be presenting at meetings and coming by and stuff
    [2020-03-11 13:24:11] <suraeNoether> for folks who are interested, the wikipedia article on the timeline of quantum computing has lots of good info
    [2020-03-11 13:24:57] <sarang> OK thanks suraeNoether
    [2020-03-11 13:25:02] <sarang> I have a few things to share
    [2020-03-11 13:25:05] <sarang> First, CLSAG
    [2020-03-11 13:25:15] <sarang> I've completed review of suraeNoether's security model updates
    [2020-03-11 13:25:23] <sarang> suraeNoether: I've left several Overleaf review comments for you
    [2020-03-11 13:26:09] <sarang> Along with that, I migrated some recent CLSAG verification optimization code to moneromooo's branch, along with relevant unit and performance tests
    [2020-03-11 13:26:20] <sarang> Saves about 5% on verification, which seemed worth it
    [2020-03-11 13:27:09] <sarang> Relating to Triptych: I made a minor update to the original Triptych-1 preprint for readability, but also completed the Triptych-2 preprint
    [2020-03-11 13:27:29] <sarang> Here is a link to the Triptych-2 preprint on Overleaf: https://www.overleaf.com/read/ynfkhykjfvrd
    [2020-03-11 13:27:53] <sarang> I'd appreciate any review on it prior to posting to the IACR archive
    [2020-03-11 13:28:27] <sarang> Unrelated to these, I've been catching up with literature review
    [2020-03-11 13:28:46] <sarang> and, as a program committee member for the IEEE S&B conference, I'm reviewing submissions
    [2020-03-11 13:28:52] <suraeNoether> i'll take a look at your comments and read through triptych 2: electric bugaloo
    [2020-03-11 13:29:00] <sarang> Thanks suraeNoether
    [2020-03-11 13:29:05] <sarang> IMO the CLSAG review is top priority
    [2020-03-11 13:29:15] <selsta> Did you contact Teserakt?
    [2020-03-11 13:29:38] <sarang> I'd like to wait on confirming a schedule until we have this paper done
    [2020-03-11 13:29:53] <sarang> Otherwise we risk losing the availability again due to delays
    [2020-03-11 13:30:33] ⇐ nsh quit (~lol@wikipedia/nsh): Max SendQ exceeded
    [2020-03-11 13:30:48] <sarang> Anyone who wants to review the CLSAG optimizations can see this branch: https://github.com/SarangNoether/monero/commits/clsag-mooo
    [2020-03-11 13:31:34] <sarang> Finally, my funding proposal needs feedback on GitLab before it's decided whether to open it: https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/131
    [2020-03-11 13:31:39] <sarang> That's all for me today
    [2020-03-11 13:31:47] <sarang> Does anyone else wish to present, or have questions?
    [2020-03-11 13:34:24] <suraeNoether> i propose that we fund sarang
    [2020-03-11 13:34:33] <suraeNoether> but no
    [2020-03-11 13:34:36] <suraeNoether> no questions
    [2020-03-11 13:34:40] → grubles joined (~blockhash@unaffiliated/grubles)
    [2020-03-11 13:34:48] <Isthmus> I propose that we fund surae
    [2020-03-11 13:34:48] <sarang> Heh, then leave a reaction or comment on gitlab!
    [2020-03-11 13:34:54] <Isthmus> I've been wrestling with a weird conundrum
    [2020-03-11 13:35:27] <sarang> Go on
    [2020-03-11 13:35:28] <Isthmus> I'm thinking about modifying my wallet to only select decoys from transactions generated by the core wallet
    [2020-03-11 13:35:47] <Isthmus> But then that in and of itself becomes a subtle heuristic
    [2020-03-11 13:35:49] <sarang> Ah, so using fingerprinting to pick the most "standard" decoys?
    [2020-03-11 13:36:05] <Isthmus> Not "most"
    [2020-03-11 13:36:12] <Isthmus> Something either looks like the core wallet, or provably isn't
    [2020-03-11 13:36:14] <sarang> Heh, yeah, it kicks the fingerprinting can slightly down the road
    [2020-03-11 13:36:56] <Isthmus> I guess if almost everybody used only outputs generated by the core wallet, then it wouldn't be a heuristic to fingerprint me
    [2020-03-11 13:37:16] <Isthmus> *outputs that cannot be proven to have not originated from the core wallet
    [2020-03-11 13:37:18] <Isthmus> ^ to be very specific
    [2020-03-11 13:37:36] <sarang> got it
    [2020-03-11 13:38:05] <Isthmus> Eh, I dunno. Don't really have a solution. It was just funny that I worked on it for a it before realizing that it becomes its own heuristic xD
    [2020-03-11 13:38:25] <Isthmus> Anyways, nothing much from me. I've had about 20 minutes per week for Monero lately
    [2020-03-11 13:38:37] <Isthmus> But in May, we're gonna have some long talks and clean house
    [2020-03-11 13:39:04] <sarang> ?
    [2020-03-11 13:40:02] <Isthmus> Have 7 heuristics that have now partitioned out upwards of 20 different implementations.
    [2020-03-11 13:40:11] <Isthmus> Most of which I've shared in MRL already
    [2020-03-11 13:40:22] <UkoeHB_> 20 sounds like a lot
    [2020-03-11 13:40:29] <UkoeHB_> monero is really doing well if there are 20
    [2020-03-11 13:40:38] <Isthmus> That's unfiltered for time.
    [2020-03-11 13:40:49] <Isthmus> Going to clean it to recent blocks and see what's in the wild *now*
    [2020-03-11 13:41:01] <sarang> So some might be updates to the same implementations?
    [2020-03-11 13:41:02] <Isthmus> It's at least 3 right now,
    [2020-03-11 13:41:36] <Isthmus> Yeah, that's why I'm not really sweating the 20
    [2020-03-11 13:41:52] <Isthmus> I think it's 3-5 in current era
    [2020-03-11 13:42:19] <Isthmus> Which is pleasantly(?) surprising
    [2020-03-11 13:43:05] <Isthmus> But yea, with absolutely no time to work on it now, hard to put together a full writeup
    [2020-03-11 13:43:15] <Isthmus> But will definitely circle back in the next 2 months
    [2020-03-11 13:43:19] → nsh joined (~lol@wikipedia/nsh)
    [2020-03-11 13:44:01] <sarang> Sounds good!
    [2020-03-11 13:44:07] <sarang> Anyone else wish to share any research?
    [2020-03-11 13:44:50] <UkoeHB_> hi, ztm2 proofreading draft is updated (with feedback from sarang about bulletproofs, and also the clawback formula regarding tx weights) https://www.pdf-archive.com/2020/03/11/zerotomoneromaster-v1-1-1/zerotomoneromaster-v1-1-1.pdf
    [2020-03-11 13:45:02] <UkoeHB_> 2 more weeks for proofreading
    [2020-03-11 13:46:25] <sarang> Good feedback so far overall?
    [2020-03-11 13:46:27] <UkoeHB_> also, looked into next-gen tx key image generation for multisig (sarang has a solution for it), and it seems like inversion key images wont greatly disrupt multisig transaction flows (especially escrowed markets, which is a big deal)
    [2020-03-11 13:46:32] <UkoeHB_> Not much feedback so far
    [2020-03-11 13:47:41] <UkoeHB_> But it's 152 pages so not surprising
    [2020-03-11 13:48:24] <UkoeHB_> that's all from me
    [2020-03-11 13:48:38] <sarang> OK, let's move on to ACTION ITEMS for the next week or so
    [2020-03-11 13:48:51] <sarang> I'll await final word on my CLSAG review notes
    [2020-03-11 13:48:54] <UkoeHB_> wondering if ArticMine has progress on fees
    [2020-03-11 13:49:14] <sarang> Continue working on Triptych
    [2020-03-11 13:49:57] <Isthmus> Why did it switch from 02 to 20?
    [2020-03-11 13:50:00] <Isthmus> oops
    [2020-03-11 13:50:02] <ArticMine> Yes I do
    [2020-03-11 13:50:03] <Isthmus> ignore that
    [2020-03-11 13:50:51] <sarang> Go ahead ArticMine!
    [2020-03-11 13:51:13] <ArticMine> I am looking at making the penalty free one also dynamic and using the long term median to control it
    [2020-03-11 13:52:14] <ArticMine> Also slowing down the fall in the long term median to match the constraint on the rise
    [2020-03-11 13:52:58] <sgp_> just got caught up
    [2020-03-11 13:53:10] <ArticMine> So it does not go from say 3000000 bytes 300000 bytes in one shot
    [2020-03-11 13:54:17] <ArticMine> The new dynamic penalty free one would track the long term median at say 20 - 25% of the long term median
    [2020-03-11 13:55:02] <Isthmus> Ooh interesting
    [2020-03-11 13:55:20] <ArticMine> This will provide predictable fee over time
    [2020-03-11 13:56:34] <sarang> Will you have a specific proposal for this, intended for a network upgrade?
    [2020-03-11 13:56:51] <ArticMine> The models I am looking at is a sharp drop, followed by a fiat banking crisis that creates a very sharp rise
    [2020-03-11 13:56:52] <ArticMine> Yes
    [2020-03-11 13:57:27] <sarang> OK, any final thoughts or topics before we wrap up this hour?
    [2020-03-11 13:58:07] <suraeNoether> be kind to each other
    [2020-03-11 13:58:11] <suraeNoether> just be excellent
    [2020-03-11 13:58:12] <suraeNoether> you animals
    [2020-03-11 13:59:19] <sarang> All right, thanks to everyone for attending. Adjourned!


# Action History
- Created by: SarangNoether | 2020-03-05T13:01:49+00:00
- Closed at: 2020-03-12T02:09:49+00:00
