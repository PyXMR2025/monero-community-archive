---
title: Monero Research Lab Meeting - Wed 15 December 2021 @ 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/640
author: Rucknium
assignees: []
labels: []
created_at: '2021-12-14T14:50:24+00:00'
updated_at: '2021-12-21T15:48:55+00:00'
type: issue
status: closed
closed_at: '2021-12-21T15:48:55+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

[Join the Monero Matrix server if you don't already have a Matrix account.](https://forum.monero.space/d/79-how-to-join-the-monero-core-team-matrix-server-web)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20211027T170000&p1=1440)

Main discussion topics:

1. Greetings

2. Discuss requirements to get [the multisig PR](https://github.com/monero-project/monero/pull/7877) merged.

3. Adaptive CPU regulation for improved mining performance ( maxwellsdemon )

4. Further analysis of July-Aug 2021 tx volume anomaly ( Isthmus / Mitchellpkt - see [these meeting logs](https://github.com/monero-project/meta/issues/621#issuecomment-948953655)) [Previous analysis](https://mitchellpkt.medium.com/fingerprinting-a-flood-forensic-statistical-analysis-of-the-mid-2021-monero-transaction-volume-a19cbf41ce60) with [Reddit discussion](https://www.reddit.com/r/Monero/comments/pvm634/fingerprinting_a_flood_forensic_statistical/)

5. Improvements to the mixin selection algorithm ( [Decoy Selection Algorithm - Areas to Improve](https://github.com/monero-project/research-lab/issues/86), [JBerman's weekly updates](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/249#note_11480), [Binning PoC](https://github.com/monero-project/research-lab/issues/88), [OSPEAD](https://ccs.getmonero.org/proposals/Rucknium-OSPEAD-Fortifying-Monero-Against-Statistical-Attack.html) ) @j-berman @Rucknium

6. Seraphis/Triptych/Lelantus Spark ( [UkoeHB's Seraphis Proof of Concept work](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/256), [Seraphis repo](https://github.com/UkoeHB/Seraphis), [Lelantus Spark](https://eprint.iacr.org/2021/1173) & [Tripych Multisig](https://github.com/cypherstack/triptych-multisig/blob/main/main.pdf) )

7. MRL META: "Cat herding", i.e. prioritization of research areas and features. Active recruitment of technical talent, MRL structure, funding (@Rucknium & others) [Reddit discussion](https://www.reddit.com/r/Monero/comments/pkg3d6/the_monero_project_should_actively_recruit/)

8. Examine sample size and random seed matters in Monero's unit tests. IRC discussion: [monero-dev](https://libera.monerologs.net/monero-dev/20211018#c39593) , [monero-research-lab](https://libera.monerologs.net/monero-research-lab/20211018)

9. Multisig Drijvers attack mitigation [Technical note](https://github.com/UkoeHB/drijvers-multisig-tech-note) , [Haveno bounty](https://github.com/haveno-dex/haveno/issues/103)

10. Any other business

11. Confirm next meeting agenda


Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: UkoeHB

Previous meeting agenda/logs:

#637 

# Discussion History
## UkoeHB | 2021-12-15T22:15:26+00:00
```
[12-15-2021 17:00:57] <UkoeHB> ok, meeting time https://github.com/monero-project/meta/issues/640
[12-15-2021 17:00:57] <UkoeHB> 1. greetings
[12-15-2021 17:00:57] <UkoeHB> hello
[12-15-2021 17:01:22] <Rucknium[m]> Hi!
[12-15-2021 17:01:28] <ArticMine> Hi
[12-15-2021 17:01:32] <rbrunner> Grüezi
[12-15-2021 17:01:55] <sethsimmons> Hi all 🙂
[12-15-2021 17:04:28] <jberman[m]> Howdy
[12-15-2021 17:04:29] <maxwellsdemon[m]> hi
[12-15-2021 17:05:05] <UkoeHB> 2. let's do updates next, what has everyone been working on?
[12-15-2021 17:06:01] <Rucknium[m]> I have mostly been working on BCH projects this past week. Not much to report on Monero.
[12-15-2021 17:06:53] <Rucknium[m]> Dipping my toes into chain analysis, I guess.
[12-15-2021 17:06:58] <UkoeHB> me: I worked on vtnerd's review of my multisig address PR, and discussed wfaressuissia's multisig tx construction PR with him (now available here: https://github.com/monero-project/monero/pull/8114 ).
[12-15-2021 17:07:41] <ArticMine> So is this ready?
[12-15-2021 17:07:46] <jberman[m]> I did a bit more view tag testing to squeeze out optimal gains as per UkoeHB's feedback on the PR, and got back to some decoy selection algo work
[12-15-2021 17:08:11] <mj-xmr[m]> I've been working on making my blockchain analysis simulator widely available: for not only Linux, but also Mac & Windows. Rucknium has reported, that the basic functionality can be executed under his dev OS: Mac. I will need at least half of January, to be able to deliver the remaining pieces of already working code.
[12-15-2021 17:08:36] <jberman[m]> On decoy selection work:
[12-15-2021 17:08:36] <jberman[m]> - I put together a very raw code snippet that demonstrates a way to implement one component of deterministic ring selection, specifically how to map randomly generated values from a seed into the gamma CDF (or any other distribution). It's a bit raw to share at this point I think, but the needle is moving there.
[12-15-2021 17:08:36] <jberman[m]> - Reviewed the PR to stop selecting duplicate outputs across rings when constructing a tx (https://github.com/monero-project/monero/pull/8047)
[12-15-2021 17:08:36] <jberman[m]> - Shared intuition behind a parameter choice for how wide bins should be in wallet side binning (I think the narrower the bins, the more effective the bins at hindering timing analysis, but more prone to someone spamming many locked outputs)
[12-15-2021 17:09:16] <mj-xmr[m]> I'm also working with a friend to write a CCS proposal for her, since she could do a lot of things 1) Cheaper 2) In parallel 
[12-15-2021 17:10:10] <UkoeHB> ArticMine: yes, although reviewers should contact myself, luigi1111, wfaressuissia, or selsta if they want more details about the issues fixed in that PR (they will be disclosed publicly sometime after the PR is merged).
[12-15-2021 17:10:55] <ArticMine> Thanks
[12-15-2021 17:11:10] <rbrunner> I am quite at a loss to see how your PR and 8114 relate, or depend on each other, or whether they solve different problems
[12-15-2021 17:12:21] <maxwellsdemon[m]> im currently trying to log on the web version of this because it will be way easier to communicate:currently on my phone
[12-15-2021 17:12:27] <UkoeHB> rbrunner: they solve different problems. My PR is for making a multisig wallet, this new PR is for making multisig transactions.
[12-15-2021 17:13:17] <rbrunner> I see. Would it make sense then to test 8114 in a similar way that I tested your PR, just to check whether "everything still works"?
[12-15-2021 17:13:18] <maxwellsdemon[m]> im here to get feedback on my idea I proposed two weeks ago, and follow up regarding a signal processing issue to estimate hadh rate
[12-15-2021 17:13:28] <maxwellsdemon[m]> hash*
[12-15-2021 17:14:20] <UkoeHB> rbrunner: yes I think so
[12-15-2021 17:14:31] <rbrunner> Ok, thanks
[12-15-2021 17:14:34] <UkoeHB> maxwellsdemon[m]: can you remind us about your idea? for the logs too
[12-15-2021 17:16:07] <UkoeHB> jberman[m]: does that PR cause issues if the number of available outputs is too low, so cross-ring duplicates are unavoidable?
[12-15-2021 17:16:44] <maxwellsdemon[m]> im back
[12-15-2021 17:16:52] <maxwellsdemon[m]> had to reset my password...
[12-15-2021 17:17:01] <UkoeHB> maxwellsdemon[m]: can you remind us about your idea? for the logs too
[12-15-2021 17:17:51] <maxwellsdemon[m]> sure, the idea was simple: adaptively adjust threadcount while mining to maximize performance metrics, such as CPU/power supply wear and tear or energy management
[12-15-2021 17:18:32] <maxwellsdemon[m]> I got the idea from mining on my laptop, where it quickly rose the temperature of the CPU. I found out pretty quickly it wouldnt be viable unless i regulated the threads using some feedback from the machine
[12-15-2021 17:19:06] <maxwellsdemon[m]> in my case I considered temperature, but power supply draw would also be a consideration - it really comes down to the information available from the sensors that can be installed or utilized on your systenm
[12-15-2021 17:20:09] <maxwellsdemon[m]> Recalling the discussion, it was thought that this would help people who arent "serious" miners, but probably wont be a benefit to people who are more involved unless it can demonstrate improved efficiency
[12-15-2021 17:20:38] <UkoeHB> Is this a project you want to work on?
[12-15-2021 17:20:39] <maxwellsdemon[m]> then it was proposed that I look into improving the estimation scheme to ascertain the network hash rate
[12-15-2021 17:20:54] <mj-xmr[m]> May I suggest giving an option for an abstract external signal? This would be for example the accumulated power in your solar battery.
[12-15-2021 17:21:48] <Rucknium[m]> In my view a main goal of maxwellsdemon 's proposed work would be to increase the hash rate of hobbyist miners. As we move into tail emission next year, squeezing as much hash rate out of honest hobbyist miners will become increasingly important.
[12-15-2021 17:22:08] <merope> maxwellsdemon[m]: (More accurately: improving the difficulty adjustment algorithm)
[12-15-2021 17:24:03] <rbrunner> ... which is quite controversial, because I think many see it as working just well enough to "never touch a running system"
[12-15-2021 17:24:06] <maxwellsdemon[m]> 1) an external signal is viable, but the issue with that is you have to have some kind of uniformity in the hardware so the firmware and software are compatible with the control algos, 2) I doubt it would increase hash rate so much as prevent someone from burning out their machine and maybe save some energy, perhaps increasing the energy efficiency, 3) yes youre correct this was to improve the difficult adjustment
[12-15-2021 17:24:06] <maxwellsdemon[m]> algorithm. My understanding is the current method using a moving window average, which has issues with transient oscillations and delays
[12-15-2021 17:27:21] <mj-xmr[m]> 1) It's as simple for the user as writing a mapping like 80% power -> 40% cores, 40% power -> 20% cores
[12-15-2021 17:27:21] <mj-xmr[m]> 2) It's better to mine on one core all the night, than 2 cores for half the day and 0 cores in the night, as this is not perfectly scallable
[12-15-2021 17:27:21] <mj-xmr[m]> 3) Shameless autopromotion - perhaps my simulator will be of some help, once it's ready. I will take this use case into account.
[12-15-2021 17:28:24] <Rucknium[m]> Well, if it increases the energy efficiency that could bring more hash power anyway since mining would become more economically viable for some hobbyist miners -- electricity cost is a concern, of course.
[12-15-2021 17:29:12] <sethsimmons> I would also consider focusing this work instead on XMRig as it is always the recommendation for someone caring more about mining.
[12-15-2021 17:29:23] <sethsimmons> Or at the very least seeing if the work can be ported to XMRig as well if viable.
[12-15-2021 17:30:07] <maxwellsdemon[m]> my background is in control theory and mathematical modeling, so wherever my skills would be most useful.
[12-15-2021 17:30:58] <mj-xmr[m]> maxwellsdemon[m]: I'm a control engineer as well. Mathematical modeling is my hobby, so I'll ping ya :)
[12-15-2021 17:31:22] <maxwellsdemon[m]> lol nice
[12-15-2021 17:31:22] <Rucknium[m]> Yes, I would assume that maxwellsdemon  's software would be bundled with or connected to xmrig since it's the most widely-used, and I think most efficient miner.
[12-15-2021 17:33:02] <jberman[m]> <UkoeHB> "jberman: does that PR cause..." <- I imagine yes, it would make it more difficult to construct rings when there are fewer outputs available. Perhaps it makes sense to only prevent duplicates across rings when there are sufficient spendable outputs in the chain
[12-15-2021 17:33:12] <merope> Personally, I doubt that reducing the number of threads would actually increase efficiency. If anything, it would lower it, because hashrate is pretty much directly proportional to the number of threads, but the power consumption isn't - because you have the power consumed by the mining itself which is proportional, but also a fixed amount of power consumed by the rest of the system to stay on (motherboard, ram, disk, other stuff)
[12-15-2021 17:34:00] <maxwellsdemon[m]> i see what you mean
[12-15-2021 17:34:08] <merope> So for optimal efficiency, the target is to use as many threads as possible to "spread out" that fixed base power cost
[12-15-2021 17:34:38] <Rucknium[m]> jberman: It would be good to get estimates on this. I could help with that.
[12-15-2021 17:35:00] <jberman[m]> Something high like 10,000 like the sanity check uses when submitting a tx to a node with sanity check enabled might make sense (https://github.com/monero-project/monero/blob/dcba757dd283a3396120f0df90fe746e3ec02292/src/cryptonote_core/tx_sanity_check.cpp#L84)
[12-15-2021 17:35:09] <merope> As for interacting with xmrig, it could be easily done even via some external script that dynamically changes the config file. All you'd have to do then is implement the logic
[12-15-2021 17:35:40] <mj-xmr[m]> merope: Yest for the last part, but desktop PCs are not the only miners out there. This doesn't apply that much for the low powered machines, where the "static cost" is relatively lower.
[12-15-2021 17:35:40] <mj-xmr[m]> Mining is not all that scallable to threads, unfortunately. 
[12-15-2021 17:36:21] <merope> But improving the difficulty adjustment algorithm would be have a much bigger impact on mining and the network as a whole
[12-15-2021 17:36:26] <UkoeHB> jberman[m]: yeah that might work
[12-15-2021 17:37:39] <maxwellsdemon[m]> maybe that is a better problem to focus on then
[12-15-2021 17:37:56] <merope> Making sure that blocks times are more consistent (especially in the case of big hashrate swings) would improve the user experience for the people sending transactions, and would (ideally) make the network less susceptible to hashrate attacks
[12-15-2021 17:38:55] <merope> Of course, such a critical change would be subject to very careful review and testing before being released on mainnet via a hardfork
[12-15-2021 17:39:56] <UkoeHB> Before the meeting runs out, does anyone have questions/comments on other topics? Perhaps from the agenda or otherwise.
[12-15-2021 17:40:31] <maxwellsdemon[m]> i have a reply but i will hold off
[12-15-2021 17:40:52] <Rucknium[m]> Let me point out a key challenge with determining a difficulty adjjustment algorithm: It's not only an engineering challenge. There is also game theory mixed in since player, i.e. miners and malicious entities, can themselves react to any changes in the system.
[12-15-2021 17:41:18] <Rucknium[m]> jberman: 10,000 units of what, exactly?
[12-15-2021 17:41:47] <maxwellsdemon[m]> I think the important thing is to define the problem clearly, define some requirements/goals to solve the problem, and get some data regarding the signals of interest to start designing the estimation scheme
[12-15-2021 17:43:58] <jberman[m]> Rucknium[m]: Spendable outputs in the chain. There are currently 40mn+ spendable RingCT outputs in the chain so wouldn't impact spending RingCT outputs, but some pre-ringCT outputs might have smaller sets (and on the switch to Seraphis, this would be something to consider too)
[12-15-2021 17:43:59] <maxwellsdemon[m]> my thoughts are that we should test the scheme on a model first, de-risk as much as possible in a safe environment, before even thinking about testing on a more realistic platform
[12-15-2021 17:44:53] <jberman[m]> On wallet side binning, my view is starting to shift that it may be challenging to get everyone on board with it for next fork, considering there are fairly subjective parameter choices in the algorithm and it's a fairly significant change to the decoy selection algo as is. It's starting to feel like I should roll up some of the intuition from there into pushing forward on deterministic binning (issue 84), which is the more long
[12-15-2021 17:44:53] <jberman[m]> term direction we're headed anyway. Curious if others have thoughts on that
[12-15-2021 17:45:28] <Rucknium[m]> jberman: Remind me, what happens under your code when the random selection picks a ring member that is a duplicate from another ring in the same tx?
[12-15-2021 17:46:10] <Rucknium[m]> maxwellsdemon: BCH has done some work on an "improved" difficulty adjustment algorithm with ASERT:
[12-15-2021 17:46:33] <Rucknium[m]> https://read.cash/@jtoomim/bch-upgrade-proposal-use-asert-as-the-new-daa-8887b9c1
[12-15-2021 17:46:48] <Rucknium[m]> https://bitcoincashresearch.org/t/asert-before-and-after/312
[12-15-2021 17:48:31] <rbrunner> Also some Monero forks with much smaller hashrates use some different algorithm; but as I said, any change here will be a *tough* sell :)
[12-15-2021 17:49:09] <merope> Though sell to whom? Devs, or the general community?
[12-15-2021 17:49:31] <jberman[m]> Rucknium[m]: In yorha-0x's PR (https://github.com/monero-project/monero/pull/8047), they simply re-select an output when one has already been seen/used in another ring. Which actually now just strikes me as a potential issue in that PR (this comment https://github.com/monero-project/monero/pull/8047#discussion_r769368957 may be applicable to the general case too)
[12-15-2021 17:49:49] <rbrunner> I think mostly the dev community. The general community probably does not care enough.
[12-15-2021 17:50:06] <jberman[m]> Or were you asking about how wallet side binning handles duplicates Rucknium 
[12-15-2021 17:50:35] <UkoeHB> jberman[m]: I think it would be ok for you to shift focus. Ultimately it is your judgement call, since you are the 'project owner' (so to speak).
[12-15-2021 17:50:53] <Rucknium[m]> jberman: Not binning. The duplicate outs issue.
[12-15-2021 17:52:39] <merope> I'd say the DAA is roughly on the same level of "importance" as the transaction protocol, in terms of its critical impact on the system - and there is always interest in making the tx protocol better/safer (with all the review and testing that it comes with). So why would we not apply the same level of scrutiny for other parts of the system?
[12-15-2021 17:53:30] <maxwellsdemon[m]> Rucknium: I read through the links you provided and the glaring concern I have is I dont see and clear mathematical analysis for the scheme they are using. I feel like these write ups are lacking in detail and that concerns me
[12-15-2021 17:53:40] <merope> If someone comes up with a solid, thoroughly reviewed proposal for a better algo, why not adopt it?
[12-15-2021 17:54:23] <maxwellsdemon[m]> For example, just because the signal oscillates doesnt mean that is necessarily wrong. Further, any FIR filter you implement (a moving average is the most simple type) will have oscillations. That is something you cant avoid
[12-15-2021 17:54:35] <jberman[m]> UkoeHB: makes sense, will keep thinking on it
[12-15-2021 17:54:42] <rbrunner> Well, you will have people to agree that it is "better". And there is indeed the "never touch a running system", as I mentioned, to many it works "well enough" now
[12-15-2021 17:55:15] <Rucknium[m]> Some key bits of info needed: In a typical week, what's the difference between the peak and trough of difficulty? The most concerning thing about a DAA would be if it opens the system to a 51% attack more easily by virtue of the fact that it creates a large spread between speak and trough.
[12-15-2021 17:55:36] <rbrunner> Not to discourage anybody, of course. Just to be prepared if walking gets rather stiff :)
[12-15-2021 17:56:03] <UkoeHB> merope: My general understanding is A) the current algorithm doesn't have any fundamental weaknesses, B) there is no one 'championing' algorithm research (surae researched this iirc, but no recommendations for a new algorithm were made).
[12-15-2021 17:56:31] <Rucknium[m]> maxwellsdemon: I'm not saying that their DAA is necessarily a good one. I'm saying that at least they have thought through some of the issues, so maybe something can be learned from what they've done.
[12-15-2021 17:56:40] <atomfried[m]> regarding the DAA, forgive my ignorance, but isnt this "just" controll theory? you have target and need to controll the environment such that the target is met?
[12-15-2021 17:56:40] <atomfried[m]> Isnt this researched already by kybernetics and robotics and so on? shouldnt there already be a perfect controller which solves this?
[12-15-2021 17:57:10] <UkoeHB> atomfried[m]: there is an adversarial dimension not present in normal control theory
[12-15-2021 17:57:19] <merope> ^
[12-15-2021 17:57:26] <rbrunner> Yeah, people who try to topple the robot over :)
[12-15-2021 17:57:29] <atomfried[m]> ahhh i see thank you
[12-15-2021 17:57:43] <Rucknium[m]> atomfried: No, it is not just control theory. It is also game theory, which complicates things quite a bit.
[12-15-2021 17:58:36] <UkoeHB> We are running into the end of the hour. Any last minute questions/comments?
[12-15-2021 17:58:50] <merope> Rucknium: I have a ready made csv of block height and difficulty (and nonces, but you can ignore those). I can send it to you, and I'm sure you have better tools for evaluating the data
[12-15-2021 17:59:50] <Rucknium[m]> endor00: Nice. Please do send it.
[12-15-2021 18:00:38] <Rucknium[m]> rbrunner: A key thing is we don't even have a good idea at this moment of the risk that the current DAA is exposing us to with respect to 51% attacks.
[12-15-2021 18:01:07] <maxwellsdemon[m]> atomfried: control solutions are unique to the system dynamics. Control theory isnt simple except for noncritical applications like home thermostats
[12-15-2021 18:01:33] <Rucknium[m]> So to say that "it's not broken so don't fix it" is not really correct since we don't know if it is broken.
[12-15-2021 18:01:57] <maxwellsdemon[m]> It would be nice if we had a simulator to test the algorithm on first
[12-15-2021 18:02:08] <maxwellsdemon[m]> it is very risky to not take that approach - i wouldnt do it
[12-15-2021 18:02:16] <atomfried[m]> maxwellsdemon[m]: i know that thats why a said "just" lol my uncle is professor in controll theory but i have no understanding of it so i thought i would just ask why all the controll theory cannot be applied to the DAA
[12-15-2021 18:02:20] <ArticMine> I am not clear how the BCH apprach would help here. The problem that BCH has is wild variations in hashrate due to using the same ASICs as BTC
[12-15-2021 18:02:27] <merope> maxwellsdemon: we have test networks that allow us to try this stuff
[12-15-2021 18:02:33] <ArticMine> Monero does not have this issue
[12-15-2021 18:03:53] <merope> We are on the "BTC side" of that issue
[12-15-2021 18:04:03] <Rucknium[m]> A test network isn't good enough since the behavior of the miners would not be the same as on mainnet
[12-15-2021 18:04:41] <merope> But block times can become quite skewed during/after sudden hashrate bursts
[12-15-2021 18:05:28] <Rucknium[m]> ArticMine: Yes, I'm not sure that anything in the BCH approach would help us. It's the only case where I've seen someone take a close look at the DAA, so at least it's good to be aware of it.
[12-15-2021 18:05:38] <maxwellsdemon[m]> We need some type of model, otherwise, in my opinion, whatever solution we come up with is just fancy guessing. We need an understanding of the system dynamics to proceed with a meaningful solution
[12-15-2021 18:05:39] <merope> Especially in the latter phase, when the spike is gone and now the difficulty has to adjust down, but it's taking longer because blocks take longer to show up because the difficulty is still high but the hashrate isn't anymore
[12-15-2021 18:06:25] <Rucknium[m]> maxwellsdemon: Right, right. Building such a model would be part of the task of developing an improved DAA.
[12-15-2021 18:06:55] <maxwellsdemon[m]> Rucknium: I would recommend splitting them because that by itself is a big effort and potentially has many uses
[12-15-2021 18:07:29] <ArticMine> <merope> I know but with BCH trading at ~0.009 BTC and using the same algorithm as BTC this is one stress test on the DAA
[12-15-2021 18:07:29] <bbqcore[m]> UkoeHB: seth mentioned on twitter that seraphis might allow for the removal of the 10 block conf requirement
[12-15-2021 18:07:31] <bbqcore[m]> from what i understood its not possible
[12-15-2021 18:07:32] <bbqcore[m]> can you confirm
[12-15-2021 18:07:57] <atomfried[m]> maxwellsdemon[m]: i am pretty sure that those two things could be nice bachelors or masters thesis for controll theory students...
[12-15-2021 18:08:14] <sethsimmons> Yeah I may have misinterpreted an earlier convo, would also like confirmation.
[12-15-2021 18:08:42] <Rucknium[m]> atomfried[m]: sgp_:  Get MAGIC grants on it lol.
[12-15-2021 18:08:55] <maxwellsdemon[m]> Rucknium: it would be, finished school too early for crypto to be a legitimate academic discussion :(
[12-15-2021 18:09:43] <Rucknium[m]> This is actually mechanism design, with control theory nested within it. It _is_ definitely a complex problem, and for now we have a very rough "heuristic" 
[12-15-2021 18:09:57] <maxwellsdemon[m]> well, if there is a means to get paid regularly (say monthly), I certainly welcome the challenege
[12-15-2021 18:09:59] <atomfried[m]> maxwellsdemon[m]: i think this is actually a nice topic because it applies more to controll theory than to blockchain-crypto-buzzwordy stuff
[12-15-2021 18:09:59] <UkoeHB> no, it is still no
[12-15-2021 18:10:12] <sgp_> yup, MAGIC Grants is here to help :)
[12-15-2021 18:11:12] <bbqcore[m]> UkoeHB: thought so. would tx chaining allow for spending an unconfirmed output once the 10 blocks are mined? allow it to queue until its ready to spend?
[12-15-2021 18:11:57] <UkoeHB> bbqcore[m]: yes you can queue up txs, however the cost is whoever has a queued tx will know the real spends of that tx
[12-15-2021 18:12:17] <bbqcore[m]> UkoeHB: so a non starter privacy wise
[12-15-2021 18:12:24] <bbqcore[m]> 10 block confs remain as is
[12-15-2021 18:12:53] <UkoeHB> yes, it is only useful when dealing with trusted parties (or when the real spend is already known, like in atomic swaps)
[12-15-2021 18:14:19] <bbqcore[m]> UkoeHB: so in theory this could allow a wallet to add auto-splitting of incoming XMR to a set amount of outputs 
[12-15-2021 18:14:54] <UkoeHB> bbqcore[m]: why would you need tx chaining for that?
[12-15-2021 18:15:01] <bbqcore[m]> since it would essentially be a self spend and you would be trust yourself
[12-15-2021 18:15:25] <UkoeHB> when the 10 blocks are over, you still have more work to do to complete your tx (i.e. construct membership proofs)
[12-15-2021 18:15:37] <UkoeHB> btw the meeting is over, thanks for attending everyone
```

## UkoeHB | 2021-12-15T22:15:43+00:00
For next meeting I'd like to focus on Seraphis address schemes and hopefully reach some kind of decision (or get closer, maybe narrow down the choices to 2 or 3).

[Schemes](https://github.com/monero-project/research-lab/issues/92)
[@tevador proposal](https://gist.github.com/tevador/50160d160d24cfc6c52ae02eb3d17024)

# Action History
- Created by: Rucknium | 2021-12-14T14:50:24+00:00
- Closed at: 2021-12-21T15:48:55+00:00
