---
title: Monero Research Lab Meeting - Wed 29 September 2021 @ 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/613
author: carrington1859
assignees: []
labels: []
created_at: '2021-09-22T18:12:42+00:00'
updated_at: '2021-09-29T22:41:31+00:00'
type: issue
status: closed
closed_at: '2021-09-29T22:41:31+00:00'
---

# Original Description
https://forum.monero.space/d/114-monero-research-lab-meeting-wed-29-september-2021-at-1700-utc

Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

Time:
17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20210929T170000&p1=1440)

Main discussion topics:

1. Greetings

2. Analysis of July-Aug 2021 tx volume anomaly ( Isthmus / Mitchellpkt ) [Full report](https://mitchellpkt.medium.com/fingerprinting-a-flood-forensic-statistical-analysis-of-the-mid-2021-monero-transaction-volume-a19cbf41ce60) , [Reddit discussion](https://www.reddit.com/r/Monero/comments/pvm634/fingerprinting_a_flood_forensic_statistical/)
3. MRL META: Active recruitment of technical talent, MRL structure (@Rucknium & others) [Reddit discussion](https://www.reddit.com/r/Monero/comments/pkg3d6/the_monero_project_should_actively_recruit/)
4. Improvements to the mixin selection algorithm ( [Decoy Selection Algorithm - Areas to Improve](https://github.com/monero-project/research-lab/issues/86), [JBerman's recent update](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/249#note_11480) ) @j-berman @Rucknium
5. Triptych vs. alternatives ( [Lelantus Spark](https://eprint.iacr.org/2021/1173) , [Seraphis](https://github.com/UkoeHB/Seraphis) , [Tripych Multisig](https://github.com/cypherstack/triptych-multisig/blob/main/main.pdf) )
6. Removing/fixing/encrypting unlock time ( [Removing/Fixing/Encrypting monero's timelocks](https://github.com/monero-project/research-lab/issues/78) ) (it also affects [binning](https://github.com/monero-project/research-lab/issues/84))
7. Any other business
8. Confirm next meeting agenda

Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: UkoeHB

Previous meeting agenda/logs: 

https://forum.monero.space/d/110-monero-research-lab-meeting-wed-22-september-2021-at-1700-utc

https://github.com/monero-project/meta/issues/611

# Discussion History
## UkoeHB | 2021-09-29T18:03:37+00:00
```
[2021-09-29 17:00:03] <UkoeHB> hi guys, MRL meeting starts now: https://github.com/monero-project/meta/issues/613
[2021-09-29 17:00:08] <UkoeHB> 1. greetings
[2021-09-29 17:00:09] <UkoeHB> hello
[2021-09-29 17:00:20] <vtnerd_> Hi
[2021-09-29 17:00:26] <janowitz> Hello
[2021-09-29 17:00:33] <rbrunner> Hi there
[2021-09-29 17:00:36] <jberman> hello
[2021-09-29 17:00:47] <Rucknium[m]> Hi
[2021-09-29 17:01:41] <tobtoht> hello
[2021-09-29 17:02:06] <binaryFate> hello, lurking
[2021-09-29 17:02:47] <UkoeHB> Like last time, we will skip general updates in favor of agenda items.
[2021-09-29 17:02:47] <UkoeHB> 2. Analysis of July-Aug 2021 tx volume anomaly; big thanks to Isthmus for writing an interesting report (https://mitchellpkt.medium.com/fingerprinting-a-flood-forensic-statistical-analysis-of-the-mid-2021-monero-transaction-volume-a19cbf41ce60) and to everyone who helped put that together.
[2021-09-29 17:03:22] <abberant[m]> hey
[2021-09-29 17:04:10] <gingeropolous> hi
[2021-09-29 17:04:28] <Rucknium[m]> I have 6 actionable implications of the research, but I want any question about the results to appear first
[2021-09-29 17:05:01] <janowitz> Great insights in your report, isthmus!
[2021-09-29 17:05:03] <UkoeHB> My take on the tx volume anomaly is that yes, such a thing can happen and isn't 'unexpected' in the sense that we expected it couldn't happen. The dynamic block and fee algorithms are designed to resist spam when blocks are larger than the minimum penalty free zone. However, this is a good opportunity to review our expectations there.
[2021-09-29 17:06:17] <UkoeHB> It is worth noting that this spam event did not really push into the dynamic block range.
[2021-09-29 17:06:37] <UkoeHB> Did the spammer avoid doing so, or was that a coincidence?
[2021-09-29 17:07:29] <Rucknium[m]> That's a good question. I am somewhat ignorant about the exact parameters of the current fee policy
[2021-09-29 17:08:10] <gingeropolous> i don't think its possible to know if they avoided it or if it was coincidence. 
[2021-09-29 17:08:50] <Rucknium[m]> Well, was their peak just barely below the penalty area? If so, that may indicate some sort of deliberate avoidance
[2021-09-29 17:09:13] <M030AAAYAD> hello
[2021-09-29 17:09:29] <UkoeHB> Yeah I think there was a period of time when blocks filled the penalty free zone consistently.
[2021-09-29 17:09:33] <Rucknium[m]> My list of actionable implications:... (full message at https://libera.ems.host/_matrix/media/r0/download/libera.chat/daa0f1e1985f970069053a4e175c62d7ebdad9f6)
[2021-09-29 17:09:53] <teedles[m]> Hello hello
[2021-09-29 17:11:16] <M030AAAYAD> I wonder if they just queued up a bunch of transactions with a low fee and were happy with them just sitting in the mempool for a while
[2021-09-29 17:11:20] <gingeropolous> one thing i ponder is if its worth getting rid of the penalty free zone, and if that would help antiflood
[2021-09-29 17:11:22] <M030AAAYAD> any chance we have mempool stats?
[2021-09-29 17:11:31] <M030AAAYAD> not super important, just curiosu
[2021-09-29 17:12:28] <Rucknium[m]> sgp_: I was wondering the same. We didn't use them in our analysis, but mempool stats could augment our analysis. I think some websites collect mempool data.
[2021-09-29 17:12:32] <teedles[m]> how are y'all doing today
[2021-09-29 17:12:44] <jberman> I recall watching the mempool consistently empty and fill up while this was going on, but that's more anecdotal
[2021-09-29 17:13:18] <UkoeHB> Rucknium[m]: 
[2021-09-29 17:13:18] <UkoeHB> 1. I doubt this can be accelerated beyond showing up in #monero-dev and getting the ball rolling if it is meandering (current plan seems some time this winter? lol)
[2021-09-29 17:13:18] <UkoeHB> 2. I have some estimate in ZtM2 section 7.3.4 footnote 32
[2021-09-29 17:13:18] <UkoeHB> 3. no comment (anyone can implement what they want :) )
[2021-09-29 17:13:18] <UkoeHB> 4. no comment (exploring things requires no opinion)
[2021-09-29 17:13:18] <UkoeHB> 5. dito
[2021-09-29 17:13:18] <UkoeHB> 6. dito
[2021-09-29 17:13:41] <janowitz> I have somehow monitored the mempool frequently, but never seen more like 300 tx in it
[2021-09-29 17:14:34] <rbrunner> I wonder how a counter-attack could probably look ...
[2021-09-29 17:14:43] <UkoeHB> gingeropolous: I think the original idea for min penalty free zone is to avoid friction when there is low tx volume, where tx volume fluctuations can have large relative magnitude.
[2021-09-29 17:15:00] <gingeropolous> right. it was like training wheels. there is consistent tx activity now
[2021-09-29 17:15:07] <Rucknium[m]> Based on the ring member age analysis I did, I think the entity somewhat staggered their transactions. Like, if it was balls-to-the-wall, then we would be seeing more ring members from the 10th most recent block. instead, it was more spread out over blocks #10-15 
[2021-09-29 17:15:32] <M030AAAYAD> having someone take on #3 would be a cool task
[2021-09-29 17:16:06] <gingeropolous> yeah a monero network monitor would be neat. 
[2021-09-29 17:16:54] <Rucknium[m]> rbrunner: I imagine that someone could write a script with an easy UI and let Monero community members have it. Then if a real flood attack is detected, initiate decentralized flood counter-attack. This is a last resort, though, since it would bloat the blockchain. Miners would be very happy, though
[2021-09-29 17:17:24] <Rucknium[m]> I think isthmus is particular is in a good position to do #3. Maybe he could submit a CCS
[2021-09-29 17:17:43] <rbrunner> Ah, you mean if we suspect the flood is there as an attempt to deanonymize. Makes sense.
[2021-09-29 17:17:55] <UkoeHB> I think Rucknium[m] has some good action items on the topic of tx spam. Does anyone else have action items to pursue? We can give this topic a few more minutes.
[2021-09-29 17:18:04] <jberman> Am I understanding right that the coming update to the dynamic fee algo still wouldn't have increased the cost to spam in this particular case?
[2021-09-29 17:18:30] <gingeropolous> it seems the fact is that the monero network can be flooded. we know this. ringsigs need other txs on the blockchain to work, so penalizing blockchain usage isn't great. 
[2021-09-29 17:18:31] <atomfried[m]> Rucknium[m]: couldnt this encourage miners to perform flood attacks?
[2021-09-29 17:18:31] <M030AAAYAD> best thing to do at the moment is just make a "wish list", starting with the basic stuff you want a v1 of the tool to have
[2021-09-29 17:18:32] <Rucknium[m]> Yeah, have a Monero Defense Corps waiting in the wings. Also, the existence of a counterattack capability itself could deter a flood attack. It is like nuclear mutually assured destruction.
[2021-09-29 17:18:34] <UkoeHB> jberman: fee update increases minimum fee by 5x, unless I am misremembering (ArticMine ?)
[2021-09-29 17:18:46] <M030AAAYAD> start with the ez stuff
[2021-09-29 17:19:10] <teedles[m]> Rucknium[m]: Monero Armed Forces 😎
[2021-09-29 17:19:13] <jberman> UkoeHB got it so it would've cost ~$5k instead of ~$1k
[2021-09-29 17:19:14] <M030AAAYAD> UkoeHB: 4x
[2021-09-29 17:19:27] <gingeropolous> oh woopty doo
[2021-09-29 17:20:16] <M030AAAYAD> yeah obviously a government could just spam if they wanted to
[2021-09-29 17:20:28] <M030AAAYAD> but in practice poisoned outputs are more effective
[2021-09-29 17:20:46] <jberman> On Rucknium[m]'s [2] (Conduct calculations for costliness of a "real" flood attack and de-anonymization probability), would probably make sense to incorporate the fee change into this
[2021-09-29 17:21:07] <crypto_grampy[m]> > <@rucknium:monero.social> My list of actionable implications:... (full message at https://libera.ems.host/_matrix/media/r0/download/libera.chat/1c1064f4a18059ae873e8f199978659bce663329)
[2021-09-29 17:21:10] <crypto_grampy[m]> 😎😎😎
[2021-09-29 17:21:12] <teedles[m]> M030AAAYAD: speaking of that there's prolly someone part of a government readin dis rn 👀
[2021-09-29 17:21:30] <UkoeHB> ok let's move on to...
[2021-09-29 17:21:30] <UkoeHB> 3. MRL META: Active recruitment of technical talent, MRL structure; this is Rucknium[m]'s agenda item.
[2021-09-29 17:21:34] <ArticMine> Yes the minimum node relay fee goes up 5x in the penalty free zone'
[2021-09-29 17:21:43] <UkoeHB> thanks ArticMine 
[2021-09-29 17:22:47] <Rucknium[m]> On agenda item #3: It seems that some balls are getting dropped on important MRL activities. Or, rather, it is not anyone's specific responsibility to ensure that certain key tasks get done, like:
[2021-09-29 17:23:36] <Rucknium[m]> Ensure that we are aware of all Monero-related academic publications and see how they can be useful. And also when outside entities do work for MRL, what is the mechanism to make sure the work gets done?
[2021-09-29 17:24:20] <Rucknium[m]> Moser et al. (2018) "An Empirical Analysis of Traceability in the Monero Blockchain" alone now has 84 citations.  I think we are missing important papers. I've started to go through them myself
[2021-09-29 17:24:38] <M030AAAYAD> on the last question, that would fall under the scope of the specific funding platform (eg: CCS or MAGIC)
[2021-09-29 17:25:08] <Rucknium[m]> How does CCS know that a task has been satisfactorily completed, though?
[2021-09-29 17:25:25] <Rucknium[m]> CCS is not necessarily in a great position to know that
[2021-09-29 17:25:48] <Rucknium[m]> I am thinking spedifically of the confusion over Cypher Stack's Triptych work.
[2021-09-29 17:26:42] <M030AAAYAD> You would have to ask luigi I suppose, but that proposal is effectively stalled indefinitely because we don't need more research there
[2021-09-29 17:27:05] <gingeropolous> oh? 
[2021-09-29 17:27:45] <M030AAAYAD> yeah unless you want to have the remaining funds go to something that we won't use
[2021-09-29 17:28:00] <Rucknium[m]> Anyway, mostly I want to throw a maybe somewhat controversial idea into the ring, and let it simmer for a week or so. The idea is not new, in fact. Maybe it would be good for MRL to have a lab manager or director to ensure that certain key tasks get done. 
[2021-09-29 17:28:01] <gingeropolous> so research into triptych multisig is complete, and it was deemed too complex, and we're waiting on seraphis etc?
[2021-09-29 17:28:16] <Rucknium[m]> This idea was brought up in the comments here:
[2021-09-29 17:28:16] <Rucknium[m]> https://www.reddit.com/r/Monero/comments/n2njsk/how_to_increase_the_number_of_cryptographers_and/
[2021-09-29 17:28:16] <UkoeHB> That is an interesting question - what happens to funds in funded proposals that get stalled/canceled?
[2021-09-29 17:28:32] <Rucknium[m]> gingeropolous: See, this is the confusion I'm talking about
[2021-09-29 17:28:36] <tobtoht> UkoeHB: general fund iirc
[2021-09-29 17:28:43] <gingeropolous> in general the core team would gobble up the funds and ridistribute as they see fit
[2021-09-29 17:28:51] <UkoeHB> Makes sense, thanks
[2021-09-29 17:28:56] <M030AAAYAD> not sure re: director/manager title, but in the past it was nice to have full-time people where part of their responsibilities was keeping up-to-date on the latest papers
[2021-09-29 17:29:32] <binaryFate> <UkoeHB> That is an interesting question - what happens to funds in funded proposals that get stalled/canceled? <-- they are moved to general fund
[2021-09-29 17:29:33] <rbrunner> Yes, that was a well established part of work then
[2021-09-29 17:29:51] <rbrunner> judging from sarang's reports
[2021-09-29 17:30:25] <M030AAAYAD> yeah sarang's reports would always include the papers he reviewed that period
[2021-09-29 17:30:32] <atomfried[m]> is there currently any cryptographer hired or working on seraphis? i know of coinstudent2048 and UkoeHB could the triptych multisig CCS just be used for seraphis research?
[2021-09-29 17:31:25] <UkoeHB> atomfried[m]: it is only coinstudent2048[ and I as volunteers right now
[2021-09-29 17:31:43] <binaryFate> Given the amount we currently have in the general fund and the speed with which quality CCS proposals are funded, funding in general is IMO not an issue at all to support some MRL "positions", manager or other
[2021-09-29 17:32:56] <gingeropolous> UkoeHB, would u have the bandwidth to take on funded work for seraphis?
[2021-09-29 17:33:31] <Rucknium[m]> Another point that's on my mind: If we go to institutions seeking collaboration, we would receive a better response if the cold-call email went something like, "Hi, I'm Director of MRL". Rather than "Hi, I'm with MRL."
[2021-09-29 17:33:31] <gingeropolous> personally, i dunno about the manager idea. if there are things like keeping up on articles, perhaps we just make that a default piece of any ccs funded MRL work
[2021-09-29 17:33:34] <UkoeHB> I am already working on it full time, but if you want to pay me I won't complain :)
[2021-09-29 17:33:58] <gingeropolous> what i mean is that will a bucket of monero make the work go faster ? because thats how that works, righT? :)
[2021-09-29 17:34:15] <UkoeHB> No not faster
[2021-09-29 17:34:25] <utxobr[m]> <crypto_grampy[m]> "> <@rucknium:monero.social> My..." <- i'd super be up for helping - it's "conferences & releases season" now @ fiat job, so, kinda strapped 😅 
[2021-09-29 17:34:56] <rbrunner> I am sure sooner or later some temptations will show up for UkoeHB where payment could make the difference pro Monero
[2021-09-29 17:35:01] <Rucknium[m]> IMHO, paying people for essential work establishes a good precedent, regardless of if it is "needed" in any particular case.
[2021-09-29 17:35:19] <rbrunner> In a positive sense, of course.
[2021-09-29 17:35:54] <UkoeHB> rbrunner: I already plan to do other stuff once there is nothing more to do re:Seraphis. But until then I am here full time.
[2021-09-29 17:36:36] <rbrunner> Which could be quite some time if Monero really switches to that, I suspect
[2021-09-29 17:37:00] <UkoeHB> Perhaps
[2021-09-29 17:37:09] <rbrunner> Or is the work on "theory" usually quite limited?
[2021-09-29 17:37:10] <Rucknium[m]> UkoeHB: Are you considering submitting a CCS proposal? I think it would be much welcomed.
[2021-09-29 17:37:29] <M030AAAYAD> maybe we can just start using the term "committee" loosely. eg: "Hi I'm Justin, a member of the Monero Research Lab funding committee", etc
[2021-09-29 17:37:45] <M030AAAYAD> means nothing but should be enough to get in the door lol
[2021-09-29 17:38:10] <UkoeHB> I wasn't planning on it - I was hoping it would be done already, but I really misjudged the time required.
[2021-09-29 17:38:14] <rbrunner> This looks like a classic case of "Shut up and take my money" :)
[2021-09-29 17:38:24] <gingeropolous> lol.
[2021-09-29 17:38:32] <Rucknium[m]> sgp_: Maybe "board"? But that sounds pretty formal and may need some sort of decision.
[2021-09-29 17:38:44] <gingeropolous> IMO, this MRL structure conversation can go on forever. 
[2021-09-29 17:39:22] <gingeropolous> if you have a vision, make it happen, and ask for forgiveness not permission.
[2021-09-29 17:39:43] <UkoeHB> rbrunner: the theory is good already imo (aside from adding security model/proofs), but implementing the core parts requires a lot of time. I do have a bit of scope creep on exactly how far I want to go with my PoC.
[2021-09-29 17:40:07] <Rucknium[m]> gingeropolous: Establishing something like a manager or director kind of requires permission, though.
[2021-09-29 17:40:42] <tobtoht> (are messages from sgp_ not relayed to irc or just me?)
[2021-09-29 17:40:50] <gingeropolous> they come through as M030AAAYAD 
[2021-09-29 17:40:59] <tobtoht> ginger: ty
[2021-09-29 17:41:08] <Rucknium[m]> UkoeHB: Seraphis etc. can't die at PoC stage, though. What are the plans for getting it to a production stage?
[2021-09-29 17:41:53] <UkoeHB> Well, once there is a PoC then other coders could pull it across the finish line. However, I am thinking to have a PoC 95% production ready.
[2021-09-29 17:42:02] <gingeropolous> ^
[2021-09-29 17:42:40] <M030AAAYAD> I'm okay with people choosing any title here tbh, so long as there is some reference that they need to talk with others for a final decision, lol
[2021-09-29 17:42:49] <rbrunner> With multisig within reach because much simpler than with Triptych?
[2021-09-29 17:43:14] <UkoeHB> rbrunner: yeah I started on it today, should require only a few hundred lines at most
[2021-09-29 17:43:17] <UkoeHB> the core parts anyway
[2021-09-29 17:43:26] <rbrunner> Wow
[2021-09-29 17:43:31] <M030AAAYAD> UkoeHB: will you do formal proofs for Seraphis?
[2021-09-29 17:43:44] <UkoeHB> sgp_: coinstudent2048[ is helping me with that
[2021-09-29 17:43:58] <M030AAAYAD> oh nice
[2021-09-29 17:44:20] <M030AAAYAD> is there a conference submission deadline you are hoping to hit?
[2021-09-29 17:44:33] <UkoeHB> no I won't do a conference; formatting is way too PITA
[2021-09-29 17:44:41] <gingeropolous> nice
[2021-09-29 17:45:25] <UkoeHB> Plus my writing style is yucky to the people on those committees :p
[2021-09-29 17:45:40] <Rucknium[m]> IMHO, we'll need academic peer review, at the very least, for any new signature scheme for Monero. But UkoeHB doesn't have to do that part, of course.
[2021-09-29 17:46:18] <Rucknium[m]> Should we move to the next agenda item? We have 15 mins remaining
[2021-09-29 17:46:53] <rbrunner> So if all goes well there will soon be a time for a first round of reviews / audits already?
[2021-09-29 17:47:01] <ArticMine> So we find a collaborator(s) to assist with the presentation / peer review part
[2021-09-29 17:47:08] <gingeropolous> is 15 mins enough time for "Improvements to the mixin selection algorithm ( Decoy Selection Algorithm - Areas to Improve, JBerman's recent update ) @j-berman @Rucknium"
[2021-09-29 17:47:33] <UkoeHB> Sure. The remaining items have already been covered in other meetings, so we don't have to do them in order. Let's do open discussion. Here are the other items
[2021-09-29 17:47:33] <UkoeHB> 4. Improvements to the mixin selection algorithmTriptych vs. alternatives ( Lelantus Spark , Seraphis , Tripych Multisig )
[2021-09-29 17:47:33] <UkoeHB> Removing/fixing/encrypting unlock time
[2021-09-29 17:47:38] <Rucknium[m]> gingeropolous: Well, we can start the discussion at least. I think so, yes
[2021-09-29 17:47:38] <UkoeHB> whoops
[2021-09-29 17:47:53] <UkoeHB> 4. Improvements to the mixin selection algorithm
[2021-09-29 17:47:53] <UkoeHB> 5. Triptych vs. alternatives ( Lelantus Spark , Seraphis , Tripych Multisig )
[2021-09-29 17:47:53] <UkoeHB> 6. Removing/fixing/encrypting unlock time
[2021-09-29 17:48:37] <jberman> On improvements, rehashing these are the 4 areas to improve
[2021-09-29 17:48:41] <Rucknium[m]> I have now (finally) submitted my CCS proposal for OSPEAD here:
[2021-09-29 17:48:41] <Rucknium[m]> https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/255
[2021-09-29 17:48:49] <jberman> 1. Integer truncation in the wallet (e.g.: `3 / 2 = 1`)
[2021-09-29 17:48:49] <jberman> 2. Binning
[2021-09-29 17:48:50] <jberman> 3. Modifying the distribution estimator (@Rucknium spearheading this)
[2021-09-29 17:48:50] <jberman> 4. Validating correct algo used at consenus
[2021-09-29 17:48:58] <UkoeHB> > So if all goes well there will soon be a time for a first round of reviews / audits already?
[2021-09-29 17:48:58] <UkoeHB> Idk how soon, since I need my PoC for the efficiency section, but my PoC still needs a bunch of work.
[2021-09-29 17:49:02] <zkao> Rucknium[m]: the issue is that incremental improvements that are needed for a running project like this are harder to publish because they're typically no breakthroughs, just incremental
[2021-09-29 17:49:07] <Rucknium[m]> The formatting is not visible for some reason, so you can read it here:
[2021-09-29 17:49:07] <Rucknium[m]> https://repo.getmonero.org/monero-project/ccs-proposals/-/blob/c2cb28f099eeb87cd07cbc0697bda924dc552248/Rucknium-OSPEAD-Fortifying-Monero-Against-Statistical-Attack.md
[2021-09-29 17:50:21] <M030AAAYAD> I don't think we have time for them in this meeting (since I don't want to derail it), but I certainly have reservations with this given 1) I have no idea what it is since I haven't seen the report, and 2) not sharing the reasoning behind the implementation publicly is probably going to do more harm than good imo
[2021-09-29 17:51:24] <Rucknium[m]> sgp_: I can check with the Vulnerability Response Process (i.e. moneromooo ) if it is OK to share the document with you specifically.
[2021-09-29 17:51:38] <Rucknium[m]> I don't agree on (2)
[2021-09-29 17:51:50] <M030AAAYAD> Rucknium: thank you, I would appreciate that for context if they allow
[2021-09-29 17:52:29] <rottenstonks> nice Rucknium[m]; taking a cursory glance at your proposal. happy to see it regardless.
[2021-09-29 17:52:37] <gingeropolous> i don't understand how we can implement things in a FOSS and also keep them secret. are u hoping to keep the rationale for selecting paramters secret?
[2021-09-29 17:53:18] <wfaressuissia> someone will just reverse what you've done it will be public anyway, not a problem 
[2021-09-29 17:53:25] <rottenstonks> i can see why it should be kept hushy hushy, but i also agree there should be some peer-review within some trusted parties in the community, my two cents.
[2021-09-29 17:53:25] <rbrunner> How long-range would that be, by the way? Would things from this carry over to Seraphis nicely? Or is there urgent if still-secret need for rapid action?
[2021-09-29 17:53:27] <Rucknium[m]> gingeropolous: Basically, yes, at this point. later we could release. However, once it is released, we cannot un-release it. So I am erring on the side of caution.
[2021-09-29 17:53:43] <Rucknium[m]> wfaressuissia[m]: No, that is not how statistics work
[2021-09-29 17:54:34] <Rucknium[m]> rbrunner: OSPEAD is unrelated to any of Monero's cryptography. It is pretty modular. It can even be compatible with the ring binning idea, according to UkoeHB 
[2021-09-29 17:54:46] <Rucknium[m]> Since it just produces a new probability distribution function
[2021-09-29 17:55:02] <rbrunner> Nice to hear
[2021-09-29 17:55:38] <Rucknium[m]> rbrunner: But in general, OSPEAD may be obsolete within a year as I work on a nonparametric approach. Nonparametrics is much harder, though, so it will take time.
[2021-09-29 17:56:13] <Rucknium[m]> But it's worth it to have many months of the OSPEAD-derived mixin (or decoy) selection algorithm
[2021-09-29 17:56:19] <rbrunner> And a jump up in complexity, I guess.
[2021-09-29 17:57:13] <Rucknium[m]> Yes, nonparametrics will increase the complexity in terms of the research as well as the implementation in the code. OSPEAD does not increase the implementation complexity.
[2021-09-29 17:57:15] <gingeropolous> and the OSPEAD-derived decoy will even be effective in the current ringsize?
[2021-09-29 17:57:25] <john_r365> Rucknium: if a Chain Analysis firm has simultaneously understood the same vulnerability as you have - how "at risk" is privacy on the network currently?
[2021-09-29 17:58:11] <Rucknium[m]> gingeropolous: Yes. How much exactly, I am not sure yet. But my intuition, as I state in my CCS, is a reduction in attack vulnerability from OSPEAD of 70-90%
[2021-09-29 17:58:40] <rottenstonks> nice...
[2021-09-29 17:58:51] <Rucknium[m]> john_r365: There are diverse view on that, even among people who have seen my attack. Let me get the link from the #monero-dev:monero.social logs....
[2021-09-29 17:59:38] <ArticMine> <jberman> 1. Integer truncation in the wallet (e.g.: `3 / 2 = 1`) <--- This could cause problems with the minimum fee. We need to round up rather than down so 3/2 = 2 not 1
[2021-09-29 17:59:48] <UkoeHB> Ok everyone, we are nigh on the 1800 mark for today's meeting. Since there continues to be a lot to discuss, let's schedule another meeting next week at the same time (1700 UTC Wednesday).
[2021-09-29 17:59:54] <Rucknium[m]> Starts here, roughly:
[2021-09-29 17:59:54] <Rucknium[m]> https://libera.monerologs.net/monero-dev/20210925#c31869
[2021-09-29 18:00:15] <john_r365> Rucknium: will read, thank you :)
[2021-09-29 18:00:23] <tobtoht> Has someone who has read the document submitted to the VRP commented on its severity?
[2021-09-29 18:00:25] <UkoeHB> ArticMine: the rounding isn't related to fees
[2021-09-29 18:00:42] <jberman> It's only in a line related to decoy selection algo
[2021-09-29 18:00:50] <ArticMine> ah ok
[2021-09-29 18:01:02] <Rucknium[m]> tobtoht: Yes, see the log I just posted. moneromooo commented as well at isthmus 
[2021-09-29 18:01:13] <UkoeHB> Let's end the meeting here (for logging purposes). Thanks all for attending.
```

# Action History
- Created by: carrington1859 | 2021-09-22T18:12:42+00:00
- Closed at: 2021-09-29T22:41:31+00:00
