---
title: Monero Research Lab Meeting - Wed 26 January 2022 @ 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/654
author: Rucknium
assignees: []
labels: []
created_at: '2022-01-24T01:58:14+00:00'
updated_at: '2022-01-27T01:12:45+00:00'
type: issue
status: closed
closed_at: '2022-01-27T01:12:45+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

[Join the Monero Matrix server if you don't already have a Matrix account.](https://forum.monero.space/d/79-how-to-join-the-monero-core-team-matrix-server-web)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20211027T170000&p1=1440)

Main discussion topics:

1. Greetings

2. Revisit @tevador 's idea to record account indices in the tx, to improve robustness of output recovery: https://libera.monerologs.net/monero-research-lab/20211230 . Additional reading: https://gist.github.com/tevador/50160d160d24cfc6c52ae02eb3d17024#gistcomment-4025357

3. Focus on Seraphis address schemes and hopefully reach some kind of decision (or get closer, maybe narrow down the choices to 2 or 3). [Schemes](https://github.com/monero-project/research-lab/issues/92) [@tevador proposal](https://gist.github.com/tevador/50160d160d24cfc6c52ae02eb3d17024)

4. Adaptive CPU regulation for improved mining performance ( maxwellsdemon )

5. Further analysis of July-Aug 2021 tx volume anomaly ( Isthmus / Mitchellpkt - see [these meeting logs](https://github.com/monero-project/meta/issues/621#issuecomment-948953655)) [Previous analysis](https://mitchellpkt.medium.com/fingerprinting-a-flood-forensic-statistical-analysis-of-the-mid-2021-monero-transaction-volume-a19cbf41ce60) with [Reddit discussion](https://www.reddit.com/r/Monero/comments/pvm634/fingerprinting_a_flood_forensic_statistical/)

6. Improvements to the mixin selection algorithm ( [Decoy Selection Algorithm - Areas to Improve](https://github.com/monero-project/research-lab/issues/86), [JBerman's weekly updates](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/249#note_11480), [Binning PoC](https://github.com/monero-project/research-lab/issues/88), [OSPEAD](https://ccs.getmonero.org/proposals/Rucknium-OSPEAD-Fortifying-Monero-Against-Statistical-Attack.html) ) @j-berman @Rucknium

7. Seraphis/Triptych/Lelantus Spark ( [UkoeHB's Seraphis Proof of Concept work](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/256), [Seraphis repo](https://github.com/UkoeHB/Seraphis), [Lelantus Spark](https://eprint.iacr.org/2021/1173) & [Tripych Multisig](https://github.com/cypherstack/triptych-multisig/blob/main/main.pdf) )

8. MRL META: "Cat herding", i.e. prioritization of research areas and features. Active recruitment of technical talent, MRL structure, funding (@Rucknium & others) [Reddit discussion](https://www.reddit.com/r/Monero/comments/pkg3d6/the_monero_project_should_actively_recruit/)

9. Examine sample size and random seed matters in Monero's unit tests. IRC discussion: [monero-dev](https://libera.monerologs.net/monero-dev/20211018#c39593) , [monero-research-lab](https://libera.monerologs.net/monero-research-lab/20211018)

10. Multisig Drijvers attack mitigation [Technical note](https://github.com/UkoeHB/drijvers-multisig-tech-note) , [Haveno bounty](https://github.com/haveno-dex/haveno/issues/103)

11. Any other business

12. Confirm next meeting agenda


Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: UkoeHB

Previous meeting agenda/logs:

#651 

# Discussion History
## UkoeHB | 2022-01-26T17:58:43+00:00
```
[01-26-2022 17:03:17] <UkoeHB> whoops, meeting time https://github.com/monero-project/meta/issues/654
[01-26-2022 17:03:23] <UkoeHB> 1. greetings
[01-26-2022 17:03:23] <UkoeHB> hello
[01-26-2022 17:03:28] <Fungibility> Salutations.
[01-26-2022 17:03:33] <rbrunner> Hi there
[01-26-2022 17:03:44] <Rucknium[m]1> Hi
[01-26-2022 17:04:27] <jberman[m]> hello :)
[01-26-2022 17:05:16] <dangerousfreedom> Hello
[01-26-2022 17:05:20] <h4sh3d> Hi
[01-26-2022 17:05:44] <dangerousfreedom> Excited to be on my first meeting. Hope you guys solve a lot of things haha
[01-26-2022 17:06:02] <UkoeHB> 2. I suppose we can do updates; what has everyone been working on?
[01-26-2022 17:06:25] <UkoeHB> the big topic today is probably https://github.com/monero-project/monero/issues/8157, but we can get to that in a few minutes
[01-26-2022 17:07:09] <rbrunner> Yeah, that was what I was busy with ...
[01-26-2022 17:07:24] <UkoeHB> me: I finally resumed coding my PoC, right now I am in the middle of implementing core jamtis components.
[01-26-2022 17:10:49] <jberman[m]> Been working on updating view tag code thanks to rbrunner 's review. He caught some good stuff
[01-26-2022 17:10:58] <Rucknium[m]1> me: Recruiting work. And the MAGIC Monero Fund had its first meeting earlier this week. We will do weekly meetings initially.
[01-26-2022 17:12:02] <UkoeHB> btw good news: this PR is on track to being merged https://github.com/monero-project/monero/pull/8052 , this comment might be interesting to some: https://github.com/monero-project/monero/pull/8052#discussion_r791165516
[01-26-2022 17:13:33] <UkoeHB> compared to the past, we are right now pretty low on new research ideas (a lot of things being implemented: seraphis + jamtis + semantic reforms, view tags)
[01-26-2022 17:15:00] <UkoeHB> should we move on to rbrunner's post?
[01-26-2022 17:15:50] <UkoeHB> Personally, I have a huge amount of code to write still, so that will be my main focus for the next month or two.
[01-26-2022 17:17:14] <rbrunner> From experience with IT projects I expect any project as I described it to be a marathon, certainly not a sprint
[01-26-2022 17:17:36] <rbrunner> I think if really takes off it will take the whole year, basically
[01-26-2022 17:18:05] <rbrunner> Consensus takes time.
[01-26-2022 17:19:14] <rbrunner> By the way, I also made a post on Reddit, for more visibility: https://old.reddit.com/r/Monero/comments/sczdrk/no_wallet_left_behind_make_sure_our_wallets/
[01-26-2022 17:19:15] <jberman[m]> I want to call attention to a specific thing rbrunner  pointed out in my view tag PR ​that I'm still looking into: I introduced a serialization change that could cause issues for users before the hard fork, specifically to the struct `tx_construction_data`, which is used when passing around unsigned tx's. I'm trying to understand its full ramifications, but I don't really see a way around it at this point
[01-26-2022 17:19:30] <jberman[m]> https://github.com/monero-project/monero/pull/8061#discussion_r789891757
[01-26-2022 17:19:58] <rbrunner> I had no time yet to answer, but I am hopeful it's a complete non-issue, thanks to the hardfork
[01-26-2022 17:20:19] <rbrunner> Thankfully
[01-26-2022 17:20:43] <UkoeHB> do hardforks typically invalidate stuff in files?
[01-26-2022 17:21:19] <rbrunner> Indirectly. I think every possible transaction in the old serialization format that this breaks is invalid anyway: Too small a ring
[01-26-2022 17:21:26] <rbrunner> wrong proofs, not BP1
[01-26-2022 17:21:29] <rbrunner> *BP+
[01-26-2022 17:21:59] <rbrunner> Nobody will blame poor jberman[m] :)
[01-26-2022 17:22:45] <rbrunner> I will look closer at this anyway. Stay tuned. Anyway, the review is nearing it's close, from my point of view.
[01-26-2022 17:22:45] <UkoeHB> makes sense; contractually, it makes sense to always start fresh for 'partial txs' when crossing a hardfork boundary
[01-26-2022 17:23:49] <jberman[m]> the issue in this case is that it could cause issues for users who upgrade software before the hard fork (i.e. introduce incompatibility across software even before the fork height). 
[01-26-2022 17:23:49] <jberman[m]> I think it's worth keeping in mind something like that view tag issue in the context of this larger wallet transition. We want to avoid breaking changes like this when making updates in the future, and this proposed major rewrite toward a wallet3-like variant keeping stuff like this in mind I think would actually *reduce* the plausibility for future breaking changes, even if it causes pain in the shorter term to people who built
[01-26-2022 17:23:49] <jberman[m]> around wallet2
[01-26-2022 17:24:55] <rbrunner> Ah, right, it will start to serialize that way before the hardfork already ... hmmm ...
[01-26-2022 17:25:31] <UkoeHB> imo one problem we have is munging old formats with each update, instead of having separate, versioned structures
[01-26-2022 17:25:52] <UkoeHB> if you had to add a new 'v15' structure, that would be way easier to deal with
[01-26-2022 17:26:10] <UkoeHB> or v16, whatever we are on
[01-26-2022 17:26:24] <rbrunner> Yeah, one can dream :) Such things certainly are to be discussed for something like "wallet3". At least there.
[01-26-2022 17:27:10] <rbrunner> However such versions can heighten the pain on the implementation side
[01-26-2022 17:27:26] <rbrunner> the Monero side I mean
[01-26-2022 17:27:32] <jberman[m]> agreed UkoeHB , some structures use this versioning scheme with `VERSION_FIELD` which I think makes sense to add in this one so long as we have this opportunity
[01-26-2022 17:31:15] <jberman[m]> anyway, I don't think this is something that needs a lot of discussion in this meeting, more investigative dev grunt work is needed I think. just wanted to highlight it and point out its relevance to the larger change. fine with omving on
[01-26-2022 17:31:44] <UkoeHB> thanks jberman[m] 
[01-26-2022 17:31:57] <rbrunner> The reactions to my post have been mixed so far, especially of course on Reddit. But so far nobody with weight spoke out against it, in the way of "no need", or "does not make sense", IMHO
[01-26-2022 17:33:18] <rbrunner> I guess in any case I will go on and try to speak directly with some key people, e.g. wallet devs
[01-26-2022 17:33:25] <ArticMine[m]> I see it as strengthening Monero
[01-26-2022 17:34:41] <Fungibility> Hopefully some interested parties can split the work in smaller chunks. Albeit I share the concern and importance of getting the ball rolling as soon as possible, the tone may somewhat make developers and researchers dubious of jumping in, since for outsiders, it might look like way too much to undertake with no substantial cues in. rbrunner
[01-26-2022 17:35:08] <Fungibility> Touching base with wallet devs is a good first step. Appreciate you making the post all the way.
[01-26-2022 17:35:23] <rbrunner> Thanks
[01-26-2022 17:36:01] <rbrunner> Will be interesting to get them to look so far ahead.
[01-26-2022 17:36:42] <rbrunner> For outsiders it looks different in quite fascinating ways, as can be seen by the comments on Reddit.
[01-26-2022 17:36:45] <Fungibility> I think I shared the post with m2049r from Monerujo yesterday. :)
[01-26-2022 17:36:56] <rbrunner> Nice
[01-26-2022 17:38:15] <rbrunner> By the way, what's the current think, will Tevador code anything for that Seraphis wallet PoC, or is that your show only, UkoeHB?
[01-26-2022 17:38:23] <Rucknium[m]1> Is there precedent? Has another chain done a forced address format upgrade? (Or course BTC has had optional address format upgrades.)
[01-26-2022 17:38:51] <UkoeHB> I believe tevador is writing test vectors and stuff in python. All the core PoC will be me though
[01-26-2022 17:39:24] <rbrunner> Ok, simplifies discussions as soon as results are visible :)
[01-26-2022 17:39:56] <rbrunner> I never heard of such an address update, but maybe that does not mean much.
[01-26-2022 17:40:16] <rbrunner> And I think that particular aspect is one of the easier ones, in the grand scheme of things.
[01-26-2022 17:40:29] <rbrunner> Still needs a good migration strategy, of course
[01-26-2022 17:41:12] <rbrunner> As does wallet file migration, and many other things
[01-26-2022 17:42:46] <Rucknium[m]1> I guess Zcash has made obsolete some of its shielded pools, so that's a bit of a precedent I suppose.
[01-26-2022 17:43:33] <rbrunner> Anyway, I am afraid we won't be able to look much to precedents to see "how it's done"
[01-26-2022 17:43:46] <rbrunner> or how it's not done of course :)
[01-26-2022 17:43:46] <ArticMine[m]> It does need a good migration strategy which why raising this is very important
[01-26-2022 17:44:49] <rbrunner> This is something even I as a "crypto noob" can probably research
[01-26-2022 17:46:40] <UkoeHB> well, I appreciate your effort rbrunner :) otherwise all my research and code might stagnate and die lol
[01-26-2022 17:47:08] <rbrunner> You are welcome. We will avoid that, would be a terrible pity
[01-26-2022 17:47:27] <jberman[m]> +1
[01-26-2022 17:49:05] <UkoeHB> before the meeting ends, does anyone have any comments/questions about any topic?
[01-26-2022 17:50:40] <Fungibility> Reminder: dev meeting on Saturday, 1700 UTC. #monero-dev https://github.com/monero-project/meta/issues/652
[01-26-2022 17:51:19] <UkoeHB> ah thanks
[01-26-2022 17:51:21] <rbrunner> Right. Make that hardfork happen.
[01-26-2022 17:51:36] <Fungibility> ...only if more people push it along. ;-)
[01-26-2022 17:51:49] <rbrunner> Review, review, review :)
[01-26-2022 17:51:52] <h4sh3d> sorry for being quite unresponsive lately UkoeHB. I've started the review of #7877, more changes than I remembered.
[01-26-2022 17:51:54] <Fungibility> UkoeHB: Same day, same time for next MRL meeting, correct?
[01-26-2022 17:53:50] <UkoeHB> oh sweet thanks h4sh3d 
[01-26-2022 17:54:27] <UkoeHB> yes Fungibility 
[01-26-2022 17:57:32] <UkoeHB> we seem to be done, so I'll call the meeting here; thanks for attending everyone
```

# Action History
- Created by: Rucknium | 2022-01-24T01:58:14+00:00
- Closed at: 2022-01-27T01:12:45+00:00
