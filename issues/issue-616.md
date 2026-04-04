---
title: Monero Research Lab Meeting - Wed 06 October 2021 @ 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/616
author: carrington1859
assignees: []
labels: []
created_at: '2021-09-29T22:33:30+00:00'
updated_at: '2021-10-06T18:25:41+00:00'
type: issue
status: closed
closed_at: '2021-10-06T18:25:41+00:00'
---

# Original Description
https://forum.monero.space/d/123-monero-research-lab-meeting-wed-06-october-2021-at-1700-utc

Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

Time:
17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20211006T170000&p1=1440)

Main discussion topics:

1. Greetings

2. Triptych/Lelantus Spark/Seraphis ( [Lelantus Spark](https://eprint.iacr.org/2021/1173) , [Seraphis repo](https://github.com/UkoeHB/Seraphis) & [CCS proposal for a PoC](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/256), [Tripych Multisig](https://github.com/cypherstack/triptych-multisig/blob/main/main.pdf) )

3. Rucknium's OSPEAD discussion ([CCS proposal](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/255) , Reddit discussion [1](https://www.reddit.com/r/Monero/comments/py8ub3/ccs_proposal_ospead_fortifying_monero_against/) & [2](https://www.reddit.com/r/Monero/comments/pyopq0/the_mathematical_nonsense_of_a_possible/)

4. MRL META: Active recruitment of technical talent, MRL structure (@Rucknium & others) [Reddit discussion](https://www.reddit.com/r/Monero/comments/pkg3d6/the_monero_project_should_actively_recruit/)

5. Analysis of July-Aug 2021 tx volume anomaly ( Isthmus / Mitchellpkt ) [Full report](https://mitchellpkt.medium.com/fingerprinting-a-flood-forensic-statistical-analysis-of-the-mid-2021-monero-transaction-volume-a19cbf41ce60) , [Reddit discussion](https://www.reddit.com/r/Monero/comments/pvm634/fingerprinting_a_flood_forensic_statistical/)

6. Improvements to the mixin selection algorithm ( [Decoy Selection Algorithm - Areas to Improve](https://github.com/monero-project/research-lab/issues/86), [JBerman's weekly updates](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/249#note_11480) ) @j-berman @Rucknium

7. [Removing/Fixing/Encrypting monero's timelocks](https://github.com/monero-project/research-lab/issues/78) ) (it also affects [binning](https://github.com/monero-project/research-lab/issues/84))
8. Any other business
9. Confirm next meeting agenda

Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: UkoeHB

Previous meeting agenda/logs: 

https://forum.monero.space/d/114-monero-research-lab-meeting-wed-29-september-2021-at-1700-utc

https://github.com/monero-project/meta/issues/613

# Discussion History
## Rucknium | 2021-10-01T04:54:22+00:00
@carrington1859 Could we add an agenda item about possible disclosure of the OSPEAD methodology? This needs to be hashed out.

Links:

https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/255

https://www.reddit.com/r/Monero/comments/py8ub3/ccs_proposal_ospead_fortifying_monero_against/

https://www.reddit.com/r/Monero/comments/pyopq0/the_mathematical_nonsense_of_a_possible/



## carrington1859 | 2021-10-06T18:25:40+00:00
17:00:17 -UkoeHB> Meeting time: https://github.com/monero-project/meta/issues/616
17:00:21 -UkoeHB> 1. greetings
17:00:22 -UkoeHB> hello
17:00:28 -ArticMine> Hi
17:00:36 -jberman> Hello
17:00:50 -carrington[m]> 👋
17:00:56 -rbrunner> Hoi zäme
17:01:18 -sgp_1> hello
17:03:01 -UkoeHB> We touched all the existing agenda items in recent meetings, so today will be a bit more open ended. We can start with updates. What has everyone been working on?
17:04:40 -jberman> Submitted PR 7993 to decrease the "recent spend window" in the decoy selection algo, submitted a PR to  update openmonero to use the gamma-based decoy selection algo, and started fleshing out a wallet-only binning algorithm that's looking good 
17:06:35 -Rucknium[m]> Working on OSPEAD/Decoy Selection Algorithm. My HackerOne submission is under review by new people, so I won't say much more now. What I will say is that I am extremely optimistic about the research project. It's all coming together 😎
17:07:51 -carrington[m]> Rucknium are you including consideration of binning in your research?
17:07:56 -UkoeHB> My update:
17:07:56 -UkoeHB> 1. submitted a CCS for work on my Seraphis PoC: https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/256
17:07:56 -UkoeHB> 2. I collaborated with sowle at Zano on a large overhaul of their PoS with hidden amounts paper (pushed last night): https://raw.githubusercontent.com/hyle-team/docs/master/PoS/PoS_with_HA/Zano_PoS_HA.pdf. This is a scheme that allows PoS with hidden amounts + ring signatures + sender-recipient anonymity. So, you can stake outputs without revealing any info to anyone.
17:07:56 -UkoeHB> 3. Still working on Seraphis PoC. Recently I coded up Seraphis composition proofs (i.e. for proving ownership/unspentness), and also coded up the ability to do multisig with those proofs. My only uncertainty here is how to add `hwdev` to it... but that's a problem for someone else :).
17:08:06 -ArticMine> I have been reviewing the HackerOne submission ^
17:08:56 -Halver[m]> Hi
17:10:07 -Rucknium[m]> carrington: According to UkoeHB , binning is compatible with my research, or at least the parametric approach (TBD on the nonparametric approach). Examining binning is on my TODO list, but it's a bit far down it.
17:10:54 -sgp_1> Nothing to report from me, just waiting on jberman's binning :)
17:12:13 -UkoeHB> Ok I think it's fine to move on. We can have open discussion about any topic (e.g. any item from the agenda, or updates). Anyone have something they want to discuss?
17:12:28 -selsta> I have something, not sure if it's MRL related.
17:12:41 -UkoeHB> Sure, what's up?
17:12:42 -selsta> This PR is still open and unmerged: https://github.com/monero-project/monero/pull/4159
17:12:59 -selsta> There was a lot of discussion around it in 2018 but it kinda got nowhere. Should we try to get this merged again?
17:13:33 -selsta> ping also moneromooo and hyc (both were involved back then)
17:13:45 -sech1> Is there some problem with current rng?
17:13:53 -sech1> if it works - don't touch :)
17:14:05 -UkoeHB> Yeah, what's the rationale?
17:14:14 -selsta> this issue basically https://github.com/monero-project/monero/issues/1271
17:15:11 -sgp_1> we need these badges again, haha https://cloud.githubusercontent.com/assets/1944293/19835640/d77a7256-9e95-11e6-8674-6e27e93bd9ae.png
17:16:27 -Rucknium[m]> This seems involved. Does this affect every part of the Monero code that uses some randomly-generated bits, or just  a subset?
17:17:46 -sech1> I think it's used everywhere in Monero code
17:17:51 -sech1> tx key generation etc.
17:18:01 -sech1> new wallet generation
17:18:25 -sech1> but the code there is sound, assuming /dev/urandom is not compromised
17:18:49 -UkoeHB> I don't have an opinion... are there people here able to evaluate that issue?
17:19:03 -hyc> the question is whether it's important to move away from the current keccak-based PRNG
17:19:15 -hyc> afaik there's no compelling reason to
17:19:34 -Rucknium[m]> sech1: So something like what happened with Cake wallet won't happen.
17:19:42 -hyc> moving to the Bitcoin PRNG is no longer considered a good idea, anyway
17:19:53 -selsta> yea, this is for libsodium, not bitcoin PRNG
17:20:20 -rbrunner> Didn't Cake Wallet cook up yet another generator?
17:20:27 -Rucknium[m]> urandom could be compromised by a state-level actor, right? That's the threat model, correct?
17:20:35 -Rucknium[m]> Huawei, or whatever that company's name is
17:20:51 -hyc> urandom can be compromised by anyone with write access to /dev
17:20:53 -Rucknium[m]> It's sort of a hardware-level threat, yeah?
17:21:14 -hyc> but anyone who can do that already owns your machine, so ...
17:22:23 -hyc> I suppose the reason to switch then, is the potential ability to use the getrandom() syscall instead of reading a file in /dev
17:23:07 -hyc> not sure this is an MRL conversation. it's not about theoretical goodness or badness of a particulaar PRNG. It's about practical hack attacks.
17:23:20 -hyc> prob can resume in #monero-dev
17:23:32 -selsta> ok we can go to the next topic then
17:24:34 -Rucknium[m]> How about this?: "Active recruitment of technical talent"
17:25:43 -sgp_1> has anyone stepped up to champion this effort?
17:25:46 -UkoeHB> I think it's too vague. If you have specific tasks to recruit for, that would make more sense.
17:25:48 -Rucknium[m]> My little nebulous project is going alright. I continue to get people pining me based on my pinned Reddit post. Most are programmers, though, not researchers per se.
17:26:19 -carrington[m]> Did any research-types come over from #monero-recruitment ?
17:26:27 -Rucknium[m]> I guess there was also recently a suggestion of r/Monero to have a 200k USD DAO to fund research
17:27:35 -Rucknium[m]> We sort of do have some specific tasks: Investigate churning. Understand what's happening on the blockchain data-wise better (i.e. continuation of some threads of ideas from the tx volume anomaly work)
17:28:56 -Rucknium[m]> carrington[m]: I would say that we don't yet have someone with plenty of time who is more research-oriented. But my proposal wasn't to just post something on r/Monero and wait. It was to write Requests For Proposals, etc. 
17:28:56 -Rucknium[m]> I haven't had time to make much progress with it yet. Been busy with decoy selection algorithm work
17:30:14 -Rucknium[m]> Included in my proposal was also, "I don't have time to really spearhead this. I need others to step up."
17:30:38 -carrington[m]> I've been taking a look at the dynamic blocksize system lately. Don't have plenty of time though, and I wouldn't call it "research" at this stage
17:32:02 -rbrunner> I guess the circle of people who is able to successfully recruit in an academic environment is pretty small
17:34:46 -Rucknium[m]> In theory I could spearhead it. It's just other things right now are prioritized. Once things get settled down I can turn back to it. For now, it is sort of floating, in stasis.
17:35:03 -rbrunner> About 2 weeks I and some others chatted with some "-Chamus>" over in #monero-community who wrote they are a successful headhunter, and could get "active talent"
17:35:19 -rbrunner> Didn't convince me personally too much however
17:35:36 -Rucknium[m]> One concrete thing we've got out of it is that some SysAdmins are helping gingeropolous with the (hopefully) forthcoming Research Computing Server
17:35:50 -sgp_1> I can help with the whole process of setting up a fund, but I can't really help with the actual recruiting component
17:37:03 -Rucknium[m]> I am trying to recruit a researcher in particular right now, but not ready to say who it is quite yet.
17:37:13 -Rucknium[m]> More funding options could help, I believe.
17:38:40 -rbrunner> Wasn't that 200k USD DAO idea that was floated not even based on XMR?
17:39:45 -ArticMine> Decentralizing funding sources is a big plus for Monero
17:39:50 -Rucknium[m]> It was DAI-based. I'm not sure how serious or viable it was
17:39:50 -Rucknium[m]> I'm trying to find the post on Reddit. My failure to find it makes me wonder if it has been deleted
17:40:20 -sgp_1> I have no idea where this 200k DAO idea is from, this is the first I'm hearing of it
17:40:56 -rbrunner> I am quite sure it was floated on Reddit, but don't remember details, just finding it strange to fund XMR development and research with DAI
17:41:03 -Rucknium[m]> It was on r/Monero
17:41:23 -rbrunner> And oh all that technical complexity ...
17:41:28 -Rucknium[m]> I commented on the post. Any easy way to search your own comments on Reddit? /:
17:41:55 -rbrunner> Don't think so. Google is sometimes a way.
17:42:02 -kowalabearhugs[m> rucknium[m]: https://www.reddit.com/r/Monero/comments/pw1fxt/proposals_for_a_monero_research_dao/
17:42:17 -Rucknium[m]> rbrunner: Well, many people have said that the instability of XMR value discourages researchers from taking it as payment.
17:42:30 -carrington[m]> I wonder if the bounties.monero.social site could be used for research tasks
17:43:39 -rbrunner> Understood, and good argument, but I really doubt whether something like a DAO running on DAI is the easiest solution for that problem ...
17:43:59 -Rucknium[m]> kowalabearhugs[m]: Ah, so it _was_ deleted. Seemed not very credible to begin with
17:45:38 -Rucknium[m]> carrington[m]: That's an idea. It could also serve as a barometer for what users want to be researched. Many users do churning, but it is not well-studied, for instance, so it is hard to issue recommendations about it.
17:45:55 -hyc> I don't see how a DAO solves the problem of needing formal proof of employment, that surae/sarang talked about
17:46:45 -Rucknium[m]> IRC-Matrix bridge is slow today :(
17:46:56 -ArticMine> One needs an incorporated not for profit
17:47:08 -hyc> yes, exactly.
17:47:25 -Rucknium[m]> hyc: It doesn't, but it would help solve the salary instability issue.
17:47:54 -hyc> Rucknium[m]: then it's only a half-measure. why bother going to all the trouble, for only a partial solution.
17:47:58 -Rucknium[m]> Some people need formal proof of employment. Others don't.
17:48:37 -Rucknium[m]> sgp 's MAGIC is an incorporate nonprofit. The structure is right there, as far as I can tell.
17:48:38 -ArticMine> Some people can work as contractors and accept the exchange risk other cannot
17:49:28 -ArticMine> ... nut the not for profit also has to gain the trust and respect of the donors
17:49:39 -sgp_old> very slow bridge today yeah
17:49:55 -ArticMine> but
17:50:01 -Rucknium[m]> ArticMine: I agree. It's just freelance work, at the end of the day.
17:50:12 -sgp_old> I am still moving forward on the MAGIC Monero Fund, and it's something we should be able to have up and running in a few short months
17:50:22 -rbrunner> I guess we have quite some members in the broader community that will immediately freak out if they only glimpse the word "incorporate" for 1 second
17:50:31 -jberman> Chiming in, I have a code-related topic I'd like to open for discussion too. Not to take away from current topic, but before meeting ends figure it's worth discussing
17:51:38 -ArticMine> MAGIG has done a lot right, but using drop in funding with big names such as GoFundMe is a big turn off to Monero donors
17:51:54 -ArticMine> So is using a VASP to accept donations
17:52:24 -sgp_old> we don't need to, that's just to keep operational costs down. Anyone can send us XMR directly
17:52:32 -Rucknium[m]> jberman: Yes, please chime in
17:52:53 -jberman> A client can possibly construct a ring where the oldest member is from ~10 days ago with some non-negligible probability
17:52:55 -ArticMine> The compliance requirements of a non profit / charity in the US are way less than for a VASP
17:53:04 -jberman> In aggregate, you would expect the oldest ring member to tend to be from ~2 months ago or later
17:53:08 -sgp_old> ArticMine: yeah
17:53:15 -jberman> Do people think it's worth having the client follow the expected aggregate rules? I.e. clients would construct rings where the oldest member is at least 2 months old every time
17:53:32 -jberman> It avoids revealing to someone you received Monero in the last 10 days (versus 60 days), and perhaps could remove that vector for timing analysis (e.g. a tx with tons of inputs and 1 ring is from within the last 10 days may suggest others are likely bounded within a more recent timeframe as well)
17:53:58 -sgp_old> is that not already accounted for with the selection algo, at least on avergae?
17:54:07 -UkoeHB> I think it's a mistake to create any kind of 'Monero inc.', regardless of 'not for profit' or whatever. There is too much inherent conflict of interest, which can't have healthy long term effects (e.g. 10-20 years from now).
17:54:16 -sgp_old> you're asking if we should *force* at least 1 old selection?
17:54:18 -jberman> Ya it's accounted for on average, but not in all cases
17:54:54 -jberman> No forcing to spit out a distribution of ring members that more closely follows the expected distribution, rather than allowing from lots of variance
17:55:25 -Rucknium[m]> UkoeHB: If we don't do something about the research funding situation, there might not be a Monero blockchain in 20 years.
17:55:47 -sgp_old> jberman: I'm still confused about what you're specifically proposing then
17:56:01 -sgp_old> maybe I'm getting caught up in the example
17:56:07 -Rucknium[m]> jberman: "some non-negligible probability" Do you have a specific number?
17:56:14 -jberman> Basically this: https://github.com/monero-project/research-lab/issues/86#issuecomment-933067682
17:56:25 -UkoeHB> jberman: I liked the idea of selecting ring members equi-distant in the probability distribution.
17:56:26 -sgp_old> are you simply asking if we should enforce selection?
17:56:35 -ArticMine> A Monero Inc is not what I mean. One can have many independent option un incorporated and incorporated for funding . The more the better 
17:57:04 -jberman> Rucknium[m] don't have a specific number, but could get it. I was looking at those 194-input tx's and noticed this phenomenon
17:57:14 -UkoeHB> Rucknium[m]: I think that is a non sequitur. There can be research funding without a Monero inc.
17:57:30 -Rucknium[m]> ArticMine: Strong agree. Different strokes for different folks.
17:57:32 -UkoeHB> What ArticMine said ^
17:58:17 -jberman> *felt* like 2 or 3 in 100, but I could definitely quantify it
17:58:32 -jberman> sgp_old yes, basically enforce the distribution in the client
17:58:39 -sgp_old> okay
17:58:49 -sgp_old> yeah, I am interested in doing what is sensible to enforce
17:59:02 -sgp_old> we know some wallets don't follow best practices
17:59:33 -ArticMine> I have serious doubts on consensus enforcement of ring selection
17:59:33 -rbrunner> So basically make the distribution "a little less random" to avoid outliers?
17:59:56 -carrington[m]> Would enforcement of the selection distribution consist of repeatedly rejecting rings which are constructed "wrong"? Because it is not consensus, it seems like that would slow down transaction generation
18:00:05 -sgp_old> I don't see this as making it less random
18:00:08 -Rucknium[m]> It just seems like what you're witnessing may be natural variation due to the gamma distribution (or any distribution, in fact)
18:00:28 -jberman> rbrunner yep
18:00:45 -jberman> I'm not talking about consensus enforcement of ring selection here, it would be wallet-side
18:00:58 -sgp_old> hmm
18:01:08 -ArticMine> If it is wallet side it is fine
18:01:29 -Rucknium[m]> sgp_old: It would "make it less random" in the sense of not following the specified distribution that's already in the code. When you reject certain distributions, you are altering it, in effect.
18:01:30 -sgp_old> I get it now and I'm not sure
18:02:41 -Rucknium[m]> Throwing out sample draws due to some rule makes the distribution dependent on that rule. It is "less random" in that there is some dependency. Lack of dependency can help reduce statistical attack surface.
18:03:27 -Rucknium[m]> I use "dependency" here in the statistical sense. Independent vs dependent.
18:03:53 -rbrunner> So this condenses to "probably not a good idea"? Not sure I understand
18:04:25 -Rucknium[m]> rbrunner: I think it condenses to "needs more study"
18:04:30 -rbrunner> :)
18:05:14 -jberman> Functionally this effect could be achieved via a hypothesis test too Ruck. In certain cases you would expect outliers to be drawn that don't follow the distribution, that would be rejected with a hypothesis test too
18:05:56 -carrington[m]> By saying "at least one output has to be X blocks old" isn't that a very limited kind of binning?
18:07:44 -Rucknium[m]> jberman: I've heard reference to the current algorithm enforcing a certain min or max mean on the age. Is that true? Do you have more details? How many proposed ring members, in proportion, are being rejected based on that rule?
18:08:35 -jberman> I'd say the idea *feels* similar to binning, but isn't really. I'd say binning has a different effect/goal
18:11:02 -jberman> The client performs a sanity check that makes sure the median ring member is not older than ~40% of all outputs
18:11:15 -jberman> >  How many proposed ring members, in proportion, are being rejected based on that rule?
18:11:21 -jberman> I don't know this
18:11:41 -Rucknium[m]> All outputs on the entire blockchain?
18:11:51 -jberman> It's not even exactly that, but ya
18:12:00 -Rucknium[m]> jberman: Let's check that. Especially before adding more rejection rules.
18:12:22 -jberman> it uses the *number* of outputs on the blockchain
18:13:10 -Rucknium[m]> Ah. So a bit weighted more heavily for recent ones, I suppose
18:13:40 -jberman> Yep
18:14:19 -UkoeHB> Ok guys we are past the hour on the meeting, so I will call it here. Should we do next week, same time, again?
18:14:35 -jberman> Sounds good to me :)
18:15:16 -Rucknium[m]> jberman:  I'd say put "Do simulations to determine rejection proportion of current rule" on your TODO list, if I may make such a suggestion 😀
18:15:27 -Rucknium[m]> UkoeHB: I think that is a good idea
18:16:12 -ArticMine> Sure next week same time
18:16:23 -rbrunner> Intense!
18:16:29 -rbrunner> But ok
18:17:02 -jberman> Rucknium[m] Agreed, will do :)  Also will get harder figures for how many rings get constructed that are composed of all outputs -10 days
18:18:25 -jberman> ArticMine I'm also curious, can you share your doubts on consensus enforcement of ring selection? It's a topic I haven't really been pushing as hard on lately, I'm having some second thoughts on it too/continuing to think on it
18:19:42 -ArticMine> It is dependent on changing parameters such as the gamma or replacement
18:20:22 -ArticMine> Consensus is something does not need to change in 50, 100 years etc
18:21:25 -ArticMine> I do not believe that real input distribution will not change with time 
18:22:25 -ArticMine> I like to take the very long term view when talking consensus

# Action History
- Created by: carrington1859 | 2021-09-29T22:33:30+00:00
- Closed at: 2021-10-06T18:25:41+00:00
