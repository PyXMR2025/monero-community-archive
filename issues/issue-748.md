---
title: Monero Research Lab Meeting - Wed 02 November 2022
source_url: https://github.com/monero-project/meta/issues/748
author: Rucknium
assignees: []
labels: []
created_at: '2022-10-31T20:24:27+00:00'
updated_at: '2022-11-08T15:35:42+00:00'
type: issue
status: closed
closed_at: '2022-11-08T15:35:42+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

[Join the Monero Matrix server if you don't already have a Matrix account.](https://forum.monero.space/d/79-how-to-join-the-monero-core-team-matrix-server-web)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20211027T170000&p1=1440)

Main discussion topics:

1. Greetings

2.  Discuss [Jamtis address checksums](https://gist.github.com/tevador/50160d160d24cfc6c52ae02eb3d17024#64-checksum).

3. Improvements to the decoy selection algorithm ( [Decoy Selection Algorithm - Areas to Improve](https://github.com/monero-project/research-lab/issues/86), [Binning PoC](https://github.com/monero-project/research-lab/issues/88), [OSPEAD](https://ccs.getmonero.org/proposals/Rucknium-OSPEAD-Fortifying-Monero-Against-Statistical-Attack.html) ) @j-berman @Rucknium

4. Seraphis. ( [UkoeHB's Seraphis Proof of Concept work](https://ccs.getmonero.org/proposals/seraphis-wallet-poc-2.html), [Seraphis repo](https://github.com/UkoeHB/Seraphis) ).

5. MRL Meta: "Cat herding", i.e. prioritization of research areas and features. Active recruitment of technical talent, MRL structure, funding (@Rucknium & others) [MoneroResearch.info repository of Monero-related research papers](https://moneroresearch.info/), [Reddit discussion](https://www.reddit.com/r/Monero/comments/pkg3d6/the_monero_project_should_actively_recruit/)

6. Any other business

7. Confirm next meeting agenda


Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: UkoeHB

Previous meeting agenda/logs:

#745 

# Discussion History
## UkoeHB | 2022-11-02T18:04:07+00:00
`[11-02-2022 17:00:14] <UkoeHB> meeting time https://github.com/monero-project/meta/issues/748`
`[11-02-2022 17:00:14] <UkoeHB> 1. greetings`
`[11-02-2022 17:00:14] <UkoeHB> hello`
`[11-02-2022 17:00:31] <one-horse-wagon[> Hello`
`[11-02-2022 17:00:32] <dangerousfreedom> Hello`
`[11-02-2022 17:00:36] <font-deny[m]> hello`
`[11-02-2022 17:01:25] <Rucknium[m]> Hi`
`[11-02-2022 17:02:55] <jberman[m]> hello`
`[11-02-2022 17:03:26] <rbrunner> Hi`
`[11-02-2022 17:04:42] <UkoeHB> 2. updates, what has everyone been working on?`
`[11-02-2022 17:05:46] <jberman[m]> me: submitted the final update on my CCS, background sync/scan_tx PR's are ready for review, nearing completion on stress testing the pool, planning to jump into input selection in Seraphis as my first task there`
`[11-02-2022 17:05:56] <UkoeHB> me: working on update seraphis multisig to allow legacy inputs, should have this done within a few days (tm); after that is adding a seraphis coinbase tx type and updating unit tests to use that`
`[11-02-2022 17:06:04] <UkoeHB> on updating*`
`[11-02-2022 17:06:50] <Rucknium[m]> me: working on other projects while waiting for initial OSPEAD review.`
`[11-02-2022 17:06:55] <one-horse-wagon[> I  wrote up a plan for the implementation of Seraphiis and Jamtis and posted it here.  Hopefully, everyone got a chance to look at it.`
`[11-02-2022 17:07:16] <UkoeHB> this is the plan from one-horse-wagon[  https://github.com/seraphis-migration/wallet3/issues/28`
`[11-02-2022 17:07:43] <dangerousfreedom> me: organizing the wallet tiers and the work that should be done to initiate a wallet in legacy and jamtis standards.`
`[11-02-2022 17:08:22] <rbrunner> Looks like that plan, same content as the .odt file`
`[11-02-2022 17:08:44] <rbrunner> Good to have it as an issue, for discussing it`
`[11-02-2022 17:10:21] <UkoeHB> 3. discussion, there are two topics on deck for today: one-horse-wagon['s plan and jamtis checksums https://gist.github.com/tevador/50160d160d24cfc6c52ae02eb3d17024#64-checksum`
`[11-02-2022 17:11:57] <rbrunner> I was late to return home and saw the proposal only a few minutes ago, unfortunately`
`[11-02-2022 17:13:37] <rbrunner> But other may already have formed some opinion?`
`[11-02-2022 17:13:54] <dangerousfreedom> I like the proposal of one-horse-wagon . In my opinion we are already doing it but if I understood you want the wallet development to be something more official/structured ? `
`[11-02-2022 17:15:52] <UkoeHB> Regarding the plan, I'd say the administrator stuff is maybe a bit aggressive. rbrunner is already doing a good job as coordinator. We don't actually know the exact steps that need to be done or what the best order is (this is a matter of ongoing discussion). I think getting a test network up sooner rather than later is a good idea, although I have no idea what's required to get that far (maybe quite a number of `
`[11-02-2022 17:15:52] <UkoeHB> intermediate steps remain).`
`[11-02-2022 17:17:34] <rbrunner> I confess that so far I was running under assumption "As long as nobody complains (e.g. from the Core Team) it's probably ok". But have not problem to contact them, to inform and listen what they think`
`[11-02-2022 17:18:33] <rbrunner> In one point I agree wholeheartedly with one-horse-wagon: The more people fully commit to this gigantic project, the better`
`[11-02-2022 17:18:52] <one-horse-wagon[> The biggest problem I see is the core developers are not onboard yet.  Direction has to come from the very top and right now there is none.`
`[11-02-2022 17:19:22] <rbrunner> Well, we don't now, I would say, we just don't have word yet.`
`[11-02-2022 17:19:48] <plowsof> i'll prod them `
`[11-02-2022 17:20:05] <rbrunner> Gently, I hope?`
`[11-02-2022 17:20:08] <UkoeHB> I can already see the answer: keep at it. lol`
`[11-02-2022 17:20:25] <rbrunner> Yeah, but why not. We do hear damned rarely from them.`
`[11-02-2022 17:20:36] <plowsof> lol`
`[11-02-2022 17:20:36] <dangerousfreedom> I guess so :p`
`[11-02-2022 17:21:44] <UkoeHB> plowsof: do you have an update about BP++?`
`[11-02-2022 17:21:50] <Rucknium[m]> I think the Core Team takes the advice: "That Core Team is best which governs least."`
`[11-02-2022 17:22:25] <plowsof> quarkslab - unavailable until Q2 2023 (said they will come back with quotes and or follow up questions) Kudelski security / CypherStack, i await their reply (after their initial response)`
`[11-02-2022 17:22:37] <rbrunner> Things like that might become important, if people start to feel we just decide over their heads, or even ignore them on purpose, there might be opposition as a result`
`[11-02-2022 17:22:47] <UkoeHB> plowsof: thanks :)`
`[11-02-2022 17:22:52] <rbrunner> and that tends to be a productivity and motivation killer`
`[11-02-2022 17:23:20] <Rucknium[m]> IMHO, I don't think direction needs to come from "the top". According to getmonero.org, "mediation" is a major role of Core. There haven't been major disagreements yet, so Core has not been involved.`
`[11-02-2022 17:24:48] <one-horse-wagon[> Rucknium:Seraphis and Jamtis are a major step for Monero and to hear nothing from the top makes little sense.`
`[11-02-2022 17:25:42] <jberman[m]> who exactly are you waiting to hear from?`
`[11-02-2022 17:26:01] <rbrunner> Hmmm, maybe "the top" is not the top in this matter. Development of Monero is a bit chaotic, if somebody comes forward and implements something, it happens :)`
`[11-02-2022 17:26:10] <UkoeHB> they have generally been quiet about research projects iirc, since they mainly do custodial things like manage the community resources`
`[11-02-2022 17:26:40] <rbrunner> I mean, who ordered that UkoeHB guy to disturb our quit Monero life with something so big? :)`
`[11-02-2022 17:26:45] <rbrunner> *quite`
`[11-02-2022 17:27:08] <rbrunner> We could do CLSAG in peace until we are all old`
`[11-02-2022 17:27:18] <UkoeHB> lol`
`[11-02-2022 17:27:51] <rbrunner> No, after this discussion now, I would like to get at least "comment" from them`
`[11-02-2022 17:28:30] <rbrunner> I know that binaryfate will be affected, because "his" Rino wallet will be affected heavily, as a JavaScript / WASM wallet.`
`[11-02-2022 17:28:56] <Rucknium[m]> A comment from them would be good, yes.`
`[11-02-2022 17:28:57] <rbrunner> Probably much more difficult to adjust than even the wallet2 based apps.`
`[11-02-2022 17:30:28] <one-horse-wagon[> We need more than a comment.  We need for them to get behind the project and pick an administrator and the program seriously underway.  `
`[11-02-2022 17:31:06] <one-horse-wagon[> * administrator and get the program`
`[11-02-2022 17:32:05] <rbrunner> Is there any important difference if people just accept me as administrator by merit, versus the Core Team formally appoints me? Serious question, hopefully not coming over as aggressive.`
`[11-02-2022 17:32:33] <rbrunner> Or just because nobody else steps up ...`
`[11-02-2022 17:33:22] <plowsof> yes people accept you as admin by merit `
`[11-02-2022 17:33:47] <one-horse-wagon[> IMO, you are the perfect guy to run the show.  But you have no power to do anything.  `
`[11-02-2022 17:33:49] <rbrunner> Hmm, yes, but maybe appointing me formally would have solid advantages?`
`[11-02-2022 17:33:58] <dangerousfreedom> I would say that it is even better by merit than if the core team appoints someone that we dont know.`
`[11-02-2022 17:34:22] <rbrunner> Well, I have the power to program and make PRs. I can't merge them, that's true.`
`[11-02-2022 17:34:43] <rbrunner> So of course luigi could stop me dead in my tracks.`
`[11-02-2022 17:35:07] <rbrunner> But to say "I have no power to do anything" sounds a bit strange to me, frankly.`
`[11-02-2022 17:35:10] <one-horse-wagon[> dangerousfreedom: That wouldn't be wise because the job requires a good deal of technical sophistication which rbrunnern7 has.`
`[11-02-2022 17:35:39] <luigi1111w> core is not going to appoint an administrator or arbitrate unless there is fighting/significant issue going on. It seems like the participants are getting along swimmingly so far with rbrunner doing his thing`
`[11-02-2022 17:35:44] <dangerousfreedom> one-horse-wagon[: Thats what I'm saying`
`[11-02-2022 17:36:44] <rbrunner> Thanks, luigi, I try hard to to "my thing" well. No guarantees, however :)`
`[11-02-2022 17:36:57] <one-horse-wagon[> luigi1111w: Why is appointing an administrator a problem?`
`[11-02-2022 17:37:20] <rbrunner> I mean, in a project of this size, there will be conflicts sooner or later, or at least serious disagreements`
`[11-02-2022 17:37:50] <luigi1111w> because core strives to be irrelevant.`
`[11-02-2022 17:37:50] <rbrunner> Even with the best of intentions from all involved parties`
`[11-02-2022 17:39:18] <one-horse-wagon[> luigi1111w: Yea but you guys aren't.  You will decide in the end as to what gets incorporated.`
`[11-02-2022 17:39:44] <luigi1111w> only to the extent there isn't consensus`
`[11-02-2022 17:39:45] <plowsof> we the people assign rbrunner as administrator +1`
`[11-02-2022 17:40:15] <luigi1111w> anyway I don't want to make unilateral statements for core. If input is required we can discuss it`
`[11-02-2022 17:40:50] <rbrunner> How do you personally look at Seraphis?`
`[11-02-2022 17:41:08] <rbrunner> If you are here, a small comment ... :)`
`[11-02-2022 17:41:26] <rbrunner> And Jamtis of course`
`[11-02-2022 17:42:49] <rbrunner> Maybe already returned back to the Olymp.`
`[11-02-2022 17:42:51] <luigi1111w> it's a big change that I don't fully understand / the full implications`
`[11-02-2022 17:44:26] <rbrunner> Well, yes, I think nobody has yet full understanding and overview concerning implications.`
`[11-02-2022 17:46:38] <luigi1111w> so then I have trepidation :)`
`[11-02-2022 17:46:53] <rbrunner> In any case, it would be good for the project to be at least sure that Core has no problem with me.`
`[11-02-2022 17:47:48] <rbrunner> You may give the others a quick call by using whatever you have there for Core, a red telephone maybe?`
`[11-02-2022 17:48:01] <rbrunner> To make sure you are in consensus`
`[11-02-2022 17:50:00] <hyc> dev consensus is really what matters, and it appears that is already a given`
`[11-02-2022 17:50:16] <SerHack> hi`
`[11-02-2022 17:50:19] <hyc> having an "administrator" isn't a bad idea, but that can still be community-chosen`
`[11-02-2022 17:50:41] <hyc> just like during RandomX development, I took over the administrivia, interfacing with the auditor teams, etc`
`[11-02-2022 17:51:29] <rbrunner> Sounds like it, yeah. I am also quite time-limited to do much more, e.g. code, to be honest. But I was frank about that.`
`[11-02-2022 17:51:34] <hyc> a clear delegation of responsibilities is a good thing.`
`[11-02-2022 17:51:59] <hyc> and core doesn't need to get involved unless the devs have unresolvable conflict`
`[11-02-2022 17:53:24] <rbrunner> But is *is* a quite special way to drive a venture the size and importance of Monero further. It worked so far, however.`
`[11-02-2022 17:54:14] <hyc> this is an open source project, developers drive it. that's how open source works.`
`[11-02-2022 17:54:17] <rbrunner> Better than most other coins, I would even say.`
`[11-02-2022 17:55:25] <dangerousfreedom> I dont know if we have any more time but I would like to discuss the new checksum algorithm for Jamtis. Currently we use Keccak but since it was replaced by blake2 in Seraphis I was thinking about using blake2 also. What are the ideas here? I would be fine using blake3 also but I dont think we need to innovate that much.`
`[11-02-2022 17:55:31] <one-horse-wagon[> Can we reach consensus here.  Put rbrunner up as the official administrator?`
`[11-02-2022 17:56:05] <plowsof> +1`
`[11-02-2022 17:56:13] <hyc> no objection here`
`[11-02-2022 17:56:26] <one-horse-wagon[> +1`
`[11-02-2022 17:56:27] <jberman[m]> sgtm`
`[11-02-2022 17:56:30] <hyc> as for keccak vs blake2 - what was the reason for changing it in Seraphis?`
`[11-02-2022 17:56:30] <UkoeHB> dangerousfreedom: I think we should table that until next week. It should be easy enough to switch out the algorithm as needed.`
`[11-02-2022 17:57:00] <Rucknium[m]> IMHO, people who are writing the code are best to ask about an administrator. But if I would vote, I vote yes.`
`[11-02-2022 17:57:00] <hyc> indeed, choice of hash algo is pretty unconstrained`
`[11-02-2022 17:57:18] <UkoeHB> hyc: blake2b is faster and has a keyed hash mode. Also, some of the hash behavior is changing (mainly hash to scalar is now hash to 64 bytes before scalar reducing instead of hash to 32 bytes).`
`[11-02-2022 17:57:42] <UkoeHB> rbrunner: keep at it :p`
`[11-02-2022 17:58:04] <hyc> UkoeHB: makes sense. speed is also why we use blake2b instad of keccak in randomx`
`[11-02-2022 17:58:18] <rbrunner> Looks like it.`
`[11-02-2022 17:58:58] <hyc> keyed hash seems less critical, you can use HMAC on anything if you really want that`
`[11-02-2022 17:59:08] <binaryFate> rbrunner: what does "administrator" mean here?`
`[11-02-2022 17:59:47] <rbrunner> What I basically am already doing: Managing the project "implement a Seraphis / Jamtis core wallet in the Monero codebase"`
`[11-02-2022 18:00:09] <rbrunner> Setting up project infrastructure, for example. Writing issues.`
`[11-02-2022 18:00:27] <rbrunner> Arrange meetings, or at least take part of any, to be informed.`
`[11-02-2022 18:00:41] <binaryFate> sounds good to me`
`[11-02-2022 18:01:00] <UkoeHB> hyc: yeah but at least it's a case of 'one less thing to get right' by using the blake2b interface`
`[11-02-2022 18:01:08] <rbrunner> Later review code, or help to review, merge to some repository`
`[11-02-2022 18:01:24] <rbrunner> a project reposistory`
`[11-02-2022 18:01:46] <hyc> UkoeHB: sure. anyway, blake2b is a good choice for any number of reasons`
`[11-02-2022 18:03:04] <UkoeHB> Ok we are at the end of the hour and seemed to have wrapped up discussion, so I'll call it here. Thanks for attending everyone.`
`[11-02-2022 18:03:11] <one-horse-wagon[> Very good.  Some of the important parts of my suggested plan are accepted.  Congratulations to you rbrunner.`
`[11-02-2022 18:03:18] <rbrunner> Thanks!`

# Action History
- Created by: Rucknium | 2022-10-31T20:24:27+00:00
- Closed at: 2022-11-08T15:35:42+00:00
