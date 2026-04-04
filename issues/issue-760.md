---
title: Monero Research Lab Meeting - Wed 30 November 2022
source_url: https://github.com/monero-project/meta/issues/760
author: Rucknium
assignees: []
labels: []
created_at: '2022-11-29T15:02:09+00:00'
updated_at: '2022-12-05T21:27:05+00:00'
type: issue
status: closed
closed_at: '2022-12-05T21:27:05+00:00'
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

#757 

# Discussion History
## UkoeHB | 2022-11-30T18:00:29+00:00
`[11-30-2022 17:00:42] <UkoeHB> meeting time https://github.com/monero-project/meta/issues/760`
`[11-30-2022 17:00:42] <UkoeHB> 1. greetings`
`[11-30-2022 17:00:42] <UkoeHB> hello`
`[11-30-2022 17:00:55] <one-horse-wagon[> Hello.`
`[11-30-2022 17:01:01] <ghostway[m]> Hello`
`[11-30-2022 17:01:03] <rbrunner> Hello`
`[11-30-2022 17:01:40] <vtnerd> hi`
`[11-30-2022 17:02:13] <dangerousfreedom> Hello`
`[11-30-2022 17:03:10] <UkoeHB> 2. updates, what's everyone working on?`
`[11-30-2022 17:03:34] <UkoeHB> me: started my big cleanup/review pass on the seraphis library`
`[11-30-2022 17:03:55] <jberman[m]> hello`
`[11-30-2022 17:04:32] <vtnerd> working on getting my machines together / bp++`
`[11-30-2022 17:04:55] <UkoeHB> vtnerd: does the haskell -> C++ translation seem doable?`
`[11-30-2022 17:05:15] <Rucknium[m]> Hi`
`[11-30-2022 17:05:53] <vtnerd> eh I dunno yet sadly, too focused on IT stuff. I'll message you privately by friday`
`[11-30-2022 17:06:07] <UkoeHB> ok thanks`
`[11-30-2022 17:06:14] <vtnerd> haskell is a bit different, but I should be able to pick up the language`
`[11-30-2022 17:08:17] <UkoeHB> it seems the matrix<->irc bridge is dead`
`[11-30-2022 17:08:37] <UkoeHB> can read along here as an interim solution: https://libera.monerologs.net/monero-research-lab/20221130`
`[11-30-2022 17:08:54] <UkoeHB> nvm that one doesn't see matrix stuff when the bridge is dead..`
`[11-30-2022 17:09:48] <koe000[m]> is the bridge dead?`
`[11-30-2022 17:10:31] <Rucknium[m]> Matrix<>IRC bridge seems laggy. Maybe it's just my Matrix home server.`
`[11-30-2022 17:10:51] <koe000[m]> matrix users can read along here: https://libera.monerologs.net/monero-research-lab/20221130`
`[11-30-2022 17:11:05] <one-horse-wagon[> Shouldn't we all just move to Matrix and be done with it?`
`[11-30-2022 17:12:13] <selsta> one-horse-wagon[: no :D`
`[11-30-2022 17:12:22] <koe000[m]> no`
`[11-30-2022 17:12:27] <selsta> anyway that's not a good topic for the meeting`
`[11-30-2022 17:12:34] <rbrunner> :)`
`[11-30-2022 17:12:35] <UkoeHB> looks like a 3min lag...`
`[11-30-2022 17:12:50] <UkoeHB> and matrix is not reading IRC`
`[11-30-2022 17:13:14] <UkoeHB> going to be a short meeting`
`[11-30-2022 17:13:20] <UkoeHB> 3. discussion, anything to discuss?`
`[11-30-2022 17:13:22] <Rucknium[m]> ghostway was the straw that broke the bridge's back. N+1 Matrix users. ;)`
`[11-30-2022 17:13:22] <plowsof> hi`
`[11-30-2022 17:13:22] <koe000[m]> anyway, do matrix users have any updates to give? looks like IRC is picking up messages 2-3 minutes late`
`[11-30-2022 17:14:15] <plowsof> im waiting on a progress update from the BP++ author (for the new paper)`
`[11-30-2022 17:14:31] <jberman> late update: I've been working through stress testing the pool and doing a final review on 8076, hoping to be done by end of week`
`[11-30-2022 17:14:35] <ghostway[m]> Rucknium[m]: Lol`
`[11-30-2022 17:14:56] <ghostway[m]> No progress on irc as well..`
`[11-30-2022 17:15:50] <ghostway[m]> I can set up monero irc if this is blocking `
`[11-30-2022 17:15:59] <koe000[m]> thanks plowsof`
`[11-30-2022 17:16:13] <Rucknium[m]> No substantial updates. The only feedback I received on the public OSPEAD plan so far was from a Reddit user who asked if OSPEAD tries to account for a possible ongoing flooding a.k.a. black marble attack.`
`[11-30-2022 17:16:14] <Rucknium[m]> The answer is no it does not. But further research on that could happen, outside of the scope of the current OSPEAD CCS.`
`[11-30-2022 17:16:15] <koe000[m]> 1 week sounded pretty ambitious for him, such things always take longer than expected`
`[11-30-2022 17:16:54] <Rucknium[m]> Any feedback can be placed here: https://github.com/monero-project/research-lab/issues/93`
`[11-30-2022 17:18:02] <UkoeHB> does anyone have comments on the account id discussion that starts here: https://gist.github.com/tevador/50160d160d24cfc6c52ae02eb3d17024?permalink_comment_id=4379590#gistcomment-4379590 ?`
`[11-30-2022 17:19:58] <rbrunner> Some sort of meta comment, I asked myself what to do if our two prominent cryptographers have different opinions, and consensus seems elusive`
`[11-30-2022 17:20:55] <rbrunner> But I don't have a good answer. Maybe trying to get comments from kabayanerve, luigi, knaccc as well?`
`[11-30-2022 17:21:31] <jberman> I have a question, can you elaborate on this: "user wallets like the CLI can only support around 6 bits worth of account ids (64) before the UX degrades seriously" -> why do you see this as the case? Seems to be the basis for dividing modes via user mode/automated and I'm not seeing exactly why such division would be desirable`
`[11-30-2022 17:21:42] <jberman> UkoeHB^`
`[11-30-2022 17:21:51] <UkoeHB> so the CLI can support 65k accounts?`
`[11-30-2022 17:21:54] <UkoeHB> how does that UX work?`
`[11-30-2022 17:22:01] <rbrunner> Ah, it's kayabaNerve`
`[11-30-2022 17:24:03] <jberman> I don't believe accounts are paginated when listing them, nor transfers when listing them, but I don't see why the UX *has* to be poor in that circumstance. I.e. why not just have one mode that cleanly handles a large number`
`[11-30-2022 17:24:56] <jberman> So long as there is a mode which supports a large number`
`[11-30-2022 17:25:44] <UkoeHB> My point is the CLI and similar wallets are all manual-interface-oriented. You aren't going to manually manage more than ~64 accounts from the CLI or a phone app, you're going to use a more enterprise-level wallet.`
`[11-30-2022 17:27:16] <UkoeHB> even if the CLI figures out a UX that works, other wallets can't really be expected to all support 'big account set' mode`
`[11-30-2022 17:27:25] <jberman> I follow. Yea, that's fair`
`[11-30-2022 17:27:37] <rbrunner> Sometimes known as "You can't optimize for everything at the same time" :)`
`[11-30-2022 17:27:52] <Rucknium[m]> Maybe the bridge slowdown is retaliation from Matrix.org for slyly bridging #monero`
`[11-30-2022 17:28:33] <ghostway[m]> About the discussion there, why would the ux degrade? You could have names for them and identifiers that map to some bytes`
`[11-30-2022 17:28:37] <rbrunner> Hell, some wallets don't support account *at all* to this day?`
`[11-30-2022 17:29:28] <UkoeHB> rbrunner: right, and that reflects the baseline 'no accounts only indices mode'`
`[11-30-2022 17:29:57] <rbrunner> ghostway[m]: I think a discussion "Is an UX possible" misses the point. Of course it is.`
`[11-30-2022 17:30:40] <rbrunner> The argument was there are (at least) two important groups of users that may use accounts in substantially different ways. At least I see the argument that way.`
`[11-30-2022 17:30:47] <UkoeHB> ghostway[m]: the simplest UX is 'list your accounts and click on the one you want to access' - that because a tedious burden for large numbers of accounts`
`[11-30-2022 17:31:31] <rbrunner> One the one hand you and me with a handful of accounts. On the other side Binance with a 10,000-account wallet, who knows.`
`[11-30-2022 17:31:51] <rbrunner> We don't really need a system that covers both.`
`[11-30-2022 17:32:16] <rbrunner> They won't manage their wallet with the CLI wallet.`
`[11-30-2022 17:33:55] <ghostway[m]> Aha`
`[11-30-2022 17:37:15] <UkoeHB> ghostway[m]: not consensus, but there are some proposals to embed account ids in the jamtis specification`
`[11-30-2022 17:37:29] <UkoeHB> anyway, are there any other topics to discuss today?`
`[11-30-2022 17:38:17] <rbrunner> Maybe now that bridge crashed for good - or is restarting?`
`[11-30-2022 17:39:45] <nioc> rbrunner: what you see is happening in other channels as well`
`[11-30-2022 17:41:21] <tevador> Jamtis address checksum proposal: https://gist.github.com/tevador/50160d160d24cfc6c52ae02eb3d17024?permalink_comment_id=4382275#gistcomment-4382275`
`[11-30-2022 17:43:25] <rbrunner> Can't judge that for lack of knowledge, but I do hope we can use that soon with good confidence. Would be nice to have Jamtis addresses fixed.`
`[11-30-2022 17:43:33] <UkoeHB> I don't really have an opinion on the checksum`
`[11-30-2022 17:45:29] <rbrunner> My question to tevador basically was "Can we trust that particular polynomial" here: https://github.com/seraphis-migration/wallet3/issues/37#issuecomment-1329217733`
`[11-30-2022 17:45:42] <ghostway[m]> Polynomial checksums seem to be having an issue, but I think it's not something that needs to be discussed now when there's no data about it. So my opinion if any, is to have some tests run on it in the background`
`[11-30-2022 17:45:43] <rbrunner> And their answer looks convincing to me.`
`[11-30-2022 17:47:16] <tevador> I'm still planning to run some tests on the "M" constant.`
`[11-30-2022 17:47:24] <rbrunner> Didn't gingeropolous say something about that infrastructure? Maybe we can run those "35 billion polymod evaluations" there :)`
`[11-30-2022 17:47:40] <UkoeHB> tevador: can you document the tests you run so they can be reproduced?`
`[11-30-2022 17:47:54] <Rucknium[m]> Reminder: if we want to do a search for good parameters, gingeropolous maintains a research computing server for us.`
`[11-30-2022 17:48:05] <rbrunner> Yes, that!`
`[11-30-2022 17:48:11] <tevador> Yes, would be great if a more powerful machine was available for that. The generator search took me 3 days with 16 cores.`
`[11-30-2022 17:48:43] <ghostway[m]> Tomorrow I can write polymod in c++/rust, if you want`
`[11-30-2022 17:48:55] <ghostway[m]> Seems like the bridge is working now`
`[11-30-2022 17:48:56] <Rucknium[m]> "64-thread Threadripper CPU" is what the research computing server has`
`[11-30-2022 17:49:04] <tevador> UkoeHB: OK, I'll comment in the wallet3 issue`
`[11-30-2022 17:50:10] <rbrunner> ghostway[m]: What is polymod?`
`[11-30-2022 17:51:04] <ghostway[m]> What is ran in polynomial checksums, polynomial evaluations `
`[11-30-2022 17:51:05] <rbrunner> Er, tevador also mentioned "polymod" ...`
`[11-30-2022 17:51:37] <tevador> polynomial modulo`
`[11-30-2022 17:51:53] <rbrunner> Do we only have that available in some slow language so far then? I am a bit confused.`
`[11-30-2022 17:51:54] <ghostway[m]> https://gist.github.com/tevador/50160d160d24cfc6c52ae02eb3d17024?permalink_comment_id=4382275#gistcomment-4382275 tevador made that`
`[11-30-2022 17:52:35] <tevador> I wrote it in python for testing purposes`
`[11-30-2022 17:52:45] <rbrunner> You mean rewrite this for more speed? https://github.com/sipa/ezbase32`
`[11-30-2022 17:54:15] <tevador> the bitcoin repo has a very well documented C code for the checksum, ours will be very similar except with a degree 8 generator`
`[11-30-2022 17:54:57] <tevador> generator degree = number of checksum characters`
`[11-30-2022 17:55:02] <ghostway[m]> Yes, well seems like it's already implemented, and I started to do it in cuda yesterday, but didn't finish`
`[11-30-2022 17:56:52] <ghostway[m]> But doesn't matter, the machine has a big cpu`
`[11-30-2022 17:59:52] <UkoeHB> ok it's the end of the hour so I'll call it, thanks for attending everyone`

# Action History
- Created by: Rucknium | 2022-11-29T15:02:09+00:00
- Closed at: 2022-12-05T21:27:05+00:00
