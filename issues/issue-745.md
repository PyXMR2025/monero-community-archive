---
title: Monero Research Lab Meeting - Wed 26 October 2022
source_url: https://github.com/monero-project/meta/issues/745
author: Rucknium
assignees: []
labels: []
created_at: '2022-10-21T22:26:52+00:00'
updated_at: '2024-04-02T17:26:32+00:00'
type: issue
status: closed
closed_at: '2022-10-31T20:24:38+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

[Join the Monero Matrix server if you don't already have a Matrix account.](https://forum.monero.space/d/79-how-to-join-the-monero-core-team-matrix-server-web)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20211027T170000&p1=1440)

Main discussion topics:

1. Greetings

2. Improvements to the decoy selection algorithm ( [Decoy Selection Algorithm - Areas to Improve](https://github.com/monero-project/research-lab/issues/86), [Binning PoC](https://github.com/monero-project/research-lab/issues/88), [OSPEAD](https://ccs.getmonero.org/proposals/Rucknium-OSPEAD-Fortifying-Monero-Against-Statistical-Attack.html) ) @j-berman @Rucknium

3. Seraphis. ( [UkoeHB's Seraphis Proof of Concept work](https://ccs.getmonero.org/proposals/seraphis-wallet-poc-2.html), [Seraphis repo](https://github.com/UkoeHB/Seraphis) ).

4. MRL Meta: "Cat herding", i.e. prioritization of research areas and features. Active recruitment of technical talent, MRL structure, funding (@Rucknium & others) [MoneroResearch.info repository of Monero-related research papers](https://moneroresearch.info/), [Reddit discussion](https://www.reddit.com/r/Monero/comments/pkg3d6/the_monero_project_should_actively_recruit/)

5. Any other business

6. Confirm next meeting agenda


Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: UkoeHB

Previous meeting agenda/logs:

#743 

# Discussion History
## UkoeHB | 2022-10-26T18:02:14+00:00
`[10-26-2022 16:59:51] <UkoeHB> meeting time https://github.com/monero-project/meta/issues/745`
`[10-26-2022 16:59:51] <UkoeHB> 1. greetings`
`[10-26-2022 16:59:51] <UkoeHB> hello`
`[10-26-2022 17:00:09] <ArticMine[m]> Hi`
`[10-26-2022 17:00:15] <rbrunner> hello`
`[10-26-2022 17:01:51] <one-horse-wagon[> Hello.`
`[10-26-2022 17:02:25] <Rucknium[m]> Hi`
`[10-26-2022 17:02:36] <jberman[m]> hello`
`[10-26-2022 17:02:43] <plowsof> hi`
`[10-26-2022 17:02:59] <xmrack[m]> Hi`
`[10-26-2022 17:03:49] <UkoeHB> 2. updates, what's everyone working on?`
`[10-26-2022 17:04:58] <UkoeHB> me: did a seraphis walkthrough with some monero devs, working on updating the library to support multisig txs with legacy inputs, after that is the very last library component: coinbase tx type`
`[10-26-2022 17:08:01] <Rucknium[m]> Bringing some R code to production level that measures the out-spends for bitcoin CoinJoins. Not strictly Monero-related, but should help CryptoMorpheus with the moneroj.net charts that compare XMR txs with other "private" cryptocurrency options.`
`[10-26-2022 17:08:17] <jberman[m]> setting up a stress test framework on the pool (with an aim toward getting PR 8076 past the finish line), working on fixing a bug in my re-scanning via scan_tx PR 8566 (good spot by plowsof), submitted a PR 8619 for background sync without the spend key`
`[10-26-2022 17:12:19] <UkoeHB> 3. discussion, any topics on anyone's mind?`
`[10-26-2022 17:14:02] <rbrunner> I have collected a number of issues around the coming Seraphis wallet: https://github.com/seraphis-migration/wallet3/issues`
`[10-26-2022 17:14:17] <rbrunner> Some are closely related to that project, but some are also more general decisions`
`[10-26-2022 17:14:38] <rbrunner> So every Monero dev should find something there to leave their opinion`
`[10-26-2022 17:15:44] <rbrunner> It's a bit lonely there so far, with me writing, and then getting some comments mostly from UkoeHB and dangerousfreedom :)`
`[10-26-2022 17:15:55] <vtnerd> hi`
`[10-26-2022 17:16:43] <vtnerd> fixed d++ bug, and focused on serialization branch, will soon replace zmq serialization stuff, so the patch is pretty big now`
`[10-26-2022 17:17:40] <UkoeHB> yeah migrating to seraphis would/will be a very big project so a bit more attention from monero devs in general would be encouraging`
`[10-26-2022 17:18:05] <Rucknium[m]> vtnerd: May be worth a look: BCH devs are discussing using WebRTC as an alternative node communication port to reduce node communication censorability: https://bitcoincashresearch.org/t/webrtc-websocket-based-p2p-networking-for-bch/928`
`[10-26-2022 17:18:18] <rbrunner> Your walkthrough showed me the size of the task ...`
`[10-26-2022 17:18:32] <UkoeHB> especially considering I don't plan to do a lot of dev work once the seraphis lib is done`
`[10-26-2022 17:19:33] <vtnerd> I have no idea (at a quick glance) why anyone would want to do that for p2p comms`
`[10-26-2022 17:19:46] <jberman[m]> I'm almost there, ready to dive in soon as I finish this slate of tasks`
`[10-26-2022 17:20:04] <vtnerd> I mean, I guess monero nodes running in js-browser thing is interesting, but my goodness`
`[10-26-2022 17:21:36] <UkoeHB> even setting aside seraphis dev, there is an enormous amount of code review necessary`
`[10-26-2022 17:22:19] <rbrunner> That will get interesting, yes. With many thousands of lines of code. Brand new. Dense at times. Promises a lot of fun`
`[10-26-2022 17:23:05] <one-horse-wagon[> rbrunner: Are we going to have the manpower to do it?`
`[10-26-2022 17:23:19] <Rucknium[m]> What skillset is necessary to help push Seraphis forward after UkoeHB is done with his part?`
`[10-26-2022 17:23:23] <UkoeHB> even for me it will probably take 2-3 weeks to do a final cleanup review`
`[10-26-2022 17:23:34] <rbrunner> "it" meaning implementing or reviewing or both?`
`[10-26-2022 17:23:49] <one-horse-wagon[> rbrunner: Both.`
`[10-26-2022 17:24:14] <rbrunner> Frankly, I don't know. I guess nobody knows. But probably not a reason to not try it.`
`[10-26-2022 17:25:21] <rbrunner> and maybe we will be able to invoke "special circumstances" if need be. I don't think somebody said back in 2014, after forking CryptoNote, "let's review everything first", right?`
`[10-26-2022 17:26:35] <Rucknium[m]> If there was a clear job description, then MAGIC could put up a job ad. Just an idea. As it stands, we will have to reach inward, but that's limited. I'm thinking for implementation, not review.`
`[10-26-2022 17:26:43] <UkoeHB> not everything is critical, for example it's probably ok if balance recovery has some minor bugs`
`[10-26-2022 17:27:58] <ArticMine[m]> Defining the Job description then would be helpful.`
`[10-26-2022 17:28:04] <hyc> rbrunner: back in 2014, core team commissioned a full code review and attempt to document APIs`
`[10-26-2022 17:28:07] <rbrunner> I think for the wallet proper we do have the necessary manpower secured. But to get Seraphis running there will be a lot of follow-up jobs.`
`[10-26-2022 17:28:26] <rbrunner> hyc: Color me surprised. Didn't know.`
`[10-26-2022 17:29:07] <vtnerd> a job ad for ... code review?`
`[10-26-2022 17:29:11] <rbrunner> There will be changes and adjustment all over the place. In RPC. In the CLI wallet, in the GUI wallet.`
`[10-26-2022 17:29:29] <vtnerd> I mean its probably best if the existing contributors do it, even if its painful and long process`
`[10-26-2022 17:29:56] <vtnerd> er you said for implementation, so IM not sure what`
`[10-26-2022 17:29:59] <hyc> agreed. people should just sign up for chunks at a time`
`[10-26-2022 17:30:30] <garth> I think it's possible that more Monero devs will give this attention as the switch to Seraphis comes closer. As of now it's still sort of peripheral.`
`[10-26-2022 17:30:55] <one-horse-wagon[> The money is certainly there for however many CCS proposals are needed.`
`[10-26-2022 17:31:03] <rbrunner> That's also my hope. So far it's not much more than a murmur in the background.`
`[10-26-2022 17:31:21] <rbrunner> But once things really are in motion ...`
`[10-26-2022 17:32:35] <rbrunner> Every wallet app dev who wants to use the Seraphis core wallet has to do at least 100 of review. How about this? :)`
`[10-26-2022 17:32:44] <rbrunner> *100 hours`
`[10-26-2022 17:34:16] <Rucknium[m]> AFAIK, our options are: 1) Acquire more resources; 2) Re-allocate existing resources (but we have no bosses); 3) Draw out Seraphis dev/implementation for an extended period of time; 4) Seraphis never reaches mainnet`
`[10-26-2022 17:35:18] <hyc> so the question is whether there's enough devs to complete the implementation?`
`[10-26-2022 17:35:20] <ArticMine[m]> I would suggest a combination of 1 and 2`
`[10-26-2022 17:35:26] <rbrunner> You can sort of mix 1 to 3.`
`[10-26-2022 17:35:52] <rbrunner> Of course not too much of 3 :)`
`[10-26-2022 17:36:24] <hyc> a job ad isn't a bad idea. just like Wolf0 was hired to do an open source miner way back when.`
`[10-26-2022 17:37:03] <UkoeHB> the crypto world probably has more wallet devs than anything else`
`[10-26-2022 17:37:14] <UkoeHB> might be viable`
`[10-26-2022 17:37:54] <rbrunner> Hmm, why not, the Seraphis library is such a nice, mostly self-contained amount of code. Could be reviewed as that. Only problem: It will probably change quite a bit over time.`
`[10-26-2022 17:38:25] <one-horse-wagon[> Wouldn't it be wise to lay out a roadmap of simple steps to the ultimate goal of total implementation.  Then ask for CCS proposals?`
`[10-26-2022 17:39:14] <rbrunner> Er, good idea, but believe me, we are still quite far away for being able to come up with a reasonable roadmap.`
`[10-26-2022 17:39:20] <one-horse-wagon[> s/?/ along the way./`
`[10-26-2022 17:40:02] <UkoeHB> one-horse-wagon[: if you have some vision for a roadmap, that would be a good contribution`
`[10-26-2022 17:40:05] <jberman[m]> Was planning on doing something like this for my next CCS. Past the hours on my current one already, just want to wrap up the tasks that were in there`
`[10-26-2022 17:41:14] <rbrunner> Of course more people thinking and brainstorming about that are a big win. But it will be difficult to look ahead.`
`[10-26-2022 17:41:39] <plowsof> will bulletproofs++ eventually be used in Seraphis? `
`[10-26-2022 17:42:16] <UkoeHB> plowsof: unknown, we still need code and reviews of the paper (which afaik has not been published in a journal yet)`
`[10-26-2022 17:42:37] <one-horse-wagon[> UkoeHB: I'm going to look into that.`
`[10-26-2022 17:43:43] <UkoeHB> one-horse-wagon[: great, glad to hear it :)`
`[10-26-2022 17:44:42] <rbrunner> Do we already know the approximate sizes of Seraphis transactions, compared with current ones?`
`[10-26-2022 17:44:59] <rbrunner> Maybe BP++ will be very welcomed, to counter the size increase`
`[10-26-2022 17:45:21] <UkoeHB> rbrunner: https://github.com/monero-project/research-lab/issues/91#issuecomment-1047191259`
`[10-26-2022 17:45:44] <UkoeHB> there haven't been too many changes since those tests`
`[10-26-2022 17:46:01] <plowsof> asking about bp++ because i want to offer myself for doing any legwork where needed for organising it etc - knowing that it will benefit both the existing monero code base and Seraphis is great`
`[10-26-2022 17:46:42] <UkoeHB> jberman[m]: you want to hand off that task to plowsof ?`
`[10-26-2022 17:47:20] <rbrunner> UkoeHB: Thanks, interesting.`
`[10-26-2022 17:49:19] <jberman[m]> yes I do`
`[10-26-2022 17:49:50] <rbrunner> In those graphs, are we now in the "concise" case?`
`[10-26-2022 17:49:57] <UkoeHB> rbrunner: squashed`
`[10-26-2022 17:50:10] <rbrunner> Ah, ok.`
`[10-26-2022 17:50:34] <UkoeHB> hence, txtype squashed v1 :)`
`[10-26-2022 17:50:57] <rbrunner> Of course. How could I forget. Problably information overload.`
`[10-26-2022 17:51:22] <Rucknium[m]> Looks like if our goal is to "offset" anything by using BP++, it would be in verification time rather than size.`
`[10-26-2022 17:52:14] <UkoeHB> plowsof: ok if you want to organize getting a code proof of concept + paper reviews for bp++ that would be great; jberman[m] and I were thinking to approach Cypher Stack for a quote`
`[10-26-2022 17:53:49] <jberman[m]> +1`
`[10-26-2022 17:54:52] <plowsof> sounds good to me `
`[10-26-2022 17:55:44] <UkoeHB> as a reminder, here is what we know about bp++ https://github.com/monero-project/research-lab/issues/101`
`[10-26-2022 17:56:29] <rbrunner> Hey, that repository link there is new, right?`
`[10-26-2022 17:57:00] <UkoeHB> not that new I think`
`[10-26-2022 17:57:55] <plowsof> there may be some 'community politics' involved with that company which will require some navigation `
`[10-26-2022 17:58:23] <rbrunner> So those are not those mysterious results from ooo's purported implementation?`
`[10-26-2022 17:59:11] <rbrunner> "navigation". May be, yes.`
`[10-26-2022 17:59:34] <UkoeHB> those are the mysterious results yes, the link is older`
`[10-26-2022 17:59:57] <rbrunner> Although, interesting that Stack Wallet from them did not draw any critics, as far as I could see.`
`[10-26-2022 18:00:10] <UkoeHB> plowsof: it's up to you how to go about it, or to look for someone else to work on it`
`[10-26-2022 18:00:12] <plowsof> received very well indeed`
`[10-26-2022 18:00:33] <rbrunner> Maybe the concerned people did not connect the dots ...`
`[10-26-2022 18:01:06] <UkoeHB> trolls lost their momentum or changed direction perhaps`
`[10-26-2022 18:01:17] <UkoeHB> anyway we are at the end of the meeting, thanks for attending everyone`

# Action History
- Created by: Rucknium | 2022-10-21T22:26:52+00:00
- Closed at: 2022-10-31T20:24:38+00:00
