---
title: 'Community Workgroup Meeting: Sunday 13th February 2022 16:00 UTC'
source_url: https://github.com/monero-project/meta/issues/663
author: carrington1859
assignees: []
labels: []
created_at: '2022-02-09T10:42:38+00:00'
updated_at: '2022-03-19T04:45:37+00:00'
type: issue
status: closed
closed_at: '2022-03-19T04:45:37+00:00'
---

# Original Description
Location: [Libera.chat, #monero-community](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-community:monero.social?via=matrix.org&via=monero.social)

[Instructions for joining the monero.social Matrix server.](https://forum.monero.space/d/79-how-to-join-the-monero-core-team-matrix-server-web)

Time
16:00 UTC [Check your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20220213T160000&p1=1440)

Moderator: Carrington

Please reach out in advance of the meeting if you would like to propose an agenda item.

Proposed Meeting Items:

1) Introduction
2) Greetings
3) Community highlights
News: [Monero Observer](https://www.monero.observer/) - [Monero Moon](https://johnfoss.medium.com/) - [Monero Revuo](https://localmonero.co/revuo)
4) [CCS updates](https://ccs.getmonero.org/)
a. [Monero Afghanistan Expansion Strategy by spirobel](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/282)
b. [mj part time coding 2022-03](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/283)
c. [j-berman full-time 3 months part 2](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/285)
d. ['Work in Progress' projects discussion](https://ccs.getmonero.org/work-in-progress/)
5) Workgroup reports
a. Dev workgroup
b. Localization workgroup
c. Outreach workgroup
d. Events workgroup
e. Website workgroup
f. Policy workgroup
g. Research workgroup
6) Open ideas time
7) Confirm next meeting date/time

[Previous meeting including logs](https://github.com/monero-project/meta/issues/653)

Meeting logs will be posted here afterwards.

# Discussion History
## carrington1859 | 2022-02-13T17:39:15+00:00
```
16:00:38 <carrington[m]> Meeting time!
16:00:46 <carrington[m]> https://github.com/monero-project/meta/issues/663
16:01:32 <plowsof[m]> Hi
16:01:37 <bbqcore[m]> yo
16:01:39 <netrik182> hi
16:01:43 <carrington[m]> 1. Introduction
16:01:51 <carrington[m]> Hello and welcome to this regularly scheduled community meeting. This is an opportunity to discuss recent event in Monero, crowdfunding proposals and updates as well as any other relevant topics which people want to talk about. It is an open meeting so feel free contribute. We will try to stick to the agenda on the github issue.
16:01:54 <Rucknium[m]> Hi
16:02:03 <carrington[m]> 2. Greetings
16:02:15 <plowsof[m]> Hi 😁
16:02:57 <carrington[m]> Hello. Matrix seems to be running very slow for me still.
16:03:16 <netrik182> yeah, bridge seems slow
16:03:22 <carrington[m]> 3. Community highlights
16:03:30 <hansams[m]1> carrington[m]: Participating first time. Hi!
16:03:46 <carrington[m]> As far as community highlights I think the biggest news is that all the PRs for the upcoming network upgrade are submitted and it looks like most of the issues raised at the last dev meeting have been resolved.
16:03:46 <carrington[m]> https://github.com/monero-project/meta/issues/655
16:03:46 <netrik182> welcome hansams :)
16:05:14 <carrington[m]> You can try refreshing this log link to see messages quicker :
16:05:14 <carrington[m]> https://libera.monerologs.net/monero-community/20220213
16:05:21 <carrington[m]> Are there any other recent news items people would like to discuss? The best way to keep up with news in the Monero community is to follow on of the community news sources listed in the github issue or to join in with monero communities on Matrix/IRC, Reddit, Twitter etc.
16:06:21 <plowsof[m]> I was pleased to see monermoo pick up coding again the other day and release something to reduce unsigned transaction file size by 40+% , @bbqcore knows more about it
16:06:47 <plowsof[m]> https://github.com/monero-project/monero/pull/8179
16:07:00 <bbqcore[m]> yeah, i've been talking to Andy at AirGap about making a QR standard for monero offline txs
16:07:26 <bbqcore[m]> moneromooo has pushed a PR that addresses the data size bottleneck - which was the biggest obstacle to making QR codes possible
16:07:46 <carrington[m]> From what I gather, this makes it more feasible to do some clever stuff with QR codes?
16:08:06 <bbqcore[m]>  now we just need to test and gather data size from different wallets - if anyone has experience doing offline txs and wants to help test so we can get feedback that would be great
16:08:37 <carrington[m]> Very cool. It would be nice if this could be implemented in Sidekick from Monerujo
16:08:51 <bbqcore[m]> carrington[m]: monero output export data is usually too big to fit in QR, even animated ones
16:09:00 <bbqcore[m]> youd have to scan for like 2-3 minute
16:09:22 <bbqcore[m]> this PR really reduces the size and would improve the qr UX
16:09:33 <carrington[m]> And it looks like Sidekick has been getting an uptick in donations
16:09:33 <carrington[m]> https://funding.monerujo.app/
16:10:01 <bbqcore[m]> yeah. great time for offline monero txs
16:10:38 <bbqcore[m]> carrington[m]: agreed, the standard needs to be made first. the team at AirGap is really interested in making this happen
16:10:38 <bigbklynballs[m]> bbqcore[m]: 40% smaller blob can be represented by qr code, but 40% larger can't be ?
16:10:39 <bigbklynballs[m]> wtf ?
16:10:55 <bigbklynballs[m]> only 40% and no problem ?
16:11:09 <bbqcore[m]> come again
16:11:15 <carrington[m]> Which brings us onto 
16:11:15 <carrington[m]> 4. CCS/fundraising updates
16:12:04 <plowsof[m]> - 99% smaller in some tests 👀 
16:12:20 <carrington[m]> a. Monero Afghanistan Expansion Strategy by spirobel 
16:12:29 <bbqcore[m]> plowsof[m]: yeah we need more eyes on this thing
16:12:32 <carrington[m]> https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/282
16:12:36 <bbqcore[m]> test it in a bunch of wallets
16:13:27 <bigbklynballs[m]> bbqcore[m]: tx representation in the same between all wallets, what do you suggest to test ?
16:13:40 <bigbklynballs[m]> s/in/is/
16:14:26 <bbqcore[m]> > <@bigbklynballs[m]:libera.chat> > <@bbqcore[m]:libera.chat> test it in a bunch of wallets
16:14:26 <bbqcore[m]> > 
16:14:26 <bbqcore[m]> >  * tx representation is the same between all wallets, what do you suggest to test ?
16:14:26 <bbqcore[m]> were looking at the size of "outputs" export file
16:14:45 <hansams[m]1> carrington[m]: Is there any other expansions in other countries/cities/regions or is Afghanistan the forst focused one?
16:15:04 <bbqcore[m]> every wallet is unique and size can vary depending on usage
16:15:05 <hansams[m]1> s/forst/first/
16:15:10 <selsta> carrington[m]: feels quite unclear what the scope of this ccs is
16:15:18 <carrington[m]> It looks like spirobel  isn't around, but people can comment on the issue on gitlab. I don't think there has been a reddit post for this proposal, so that would be a good idea to get more eyes on it.
16:16:49 <carrington[m]> Yes I agree the deliverables are a little vague.
16:18:18 <nioc> ii seems that they are doing a study to see what is actually feasible
16:18:22 <carrington[m]> Actually they made this reddit post with a similar topic
16:18:22 <carrington[m]> https://www.reddit.com/r/Monero/comments/s3w15c/increase_adoption_of_monero_in_afghanistan_and/
16:18:31 <netrik182> it looks like a research paper, yes
16:18:34 <nioc> with someone who is there
16:18:47 <nioc> no idea where spirobel[m] is located
16:19:10 <bbqcore[m]> tora bora
16:19:35 <nioc> *someone on the ground who is greatly affected by recent events 
16:19:45 <carrington[m]> Well anyways if people could leave a comment there it would be appreciated.
16:20:08 <carrington[m]> b. mj part time coding 2022-03
16:20:09 <carrington[m]> https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/283
16:20:18 <bigbklynballs[m]> The first question is how people in that country are earning money right now
16:20:22 <carrington[m]> mj-xmr[m] mj-xmr 
16:20:41 <mj-xmr[m]> Hi. Thanks for pinging.
16:20:42 <selsta> I would like a comment from Rucknium[m] on why tsqsim is preferred to existing open source projects.
16:20:44 <bigbklynballs[m]> And why monero can be better than that way 
16:20:51 <mj-xmr[m]> Give me a minute to read...
16:21:00 <carrington[m]> jberman 
16:21:23 <nioc> bigbklynballs[m]: half the country was recently prevented from working 
16:21:59 <bigbklynballs[m]> nioc: external sanctions or internal restrictions by new govt ?
16:22:13 <nioc> new gov, Taliban 
16:22:28 <bigbklynballs[m]> It would be hard to compete with guys with guns
16:22:31 <bigbklynballs[m]> then
16:22:49 <nioc> usually is
16:23:32 <bigbklynballs[m]> In that case people will prefer anything that reduces risk to be killed and monero via electronic device isn't the safest solution
16:24:48 <selsta> mj-xmr[m]: we need monero developers and funding someone almost full time for an external tool doesn't make much sense in my opinion :/
16:25:09 <carrington[m]> There is also a related reddit post
16:25:09 <carrington[m]> https://www.reddit.com/r/Monero/comments/shq9ia/mjs_ccs_proposal_for_march_2022/
16:25:10 <selsta> unless Rucknium[m] can explain why his research wouldn't be possible otherwise with existing tools
16:26:41 <hansams[m]1> bigbklynballs[m]: I am not suggesting at all that it is comparable, but as a principle you are referring to any government in the world. The problem exists no matter the country. In Europe they just use other measures: restrictions, fines, imprisonment etc. That is why I was asking, if this Afghanistan initiative is a pilot or there are others in other countries. There might be similarities and good practices.
16:27:29 <mj-xmr[m]> <selsta> "I would like a comment from..." <- He has made a comment already, since such a question was asked. I can't find it, so I'll paraphrase:
16:27:30 <mj-xmr[m]> He said that he could perform this already with existing tools, but he preferred to be in close contact with somebody who has experience with a time series analysis, in order to quickly respond to required changes. This was commented some 4 months ago.
16:27:30 <hansams[m]1> * The problem (guys with guns) exists no, * In Europe/US/Canada they, * imprisonment etc. And finally they bring out guns. That is
16:27:31 <mj-xmr[m]> Lately I've reviewed his document, and OSPEAD requires about 50 thousand iterations in a single data portion to find an optimal setting, so I personally think that a tool, that focuses on speed of execution would speed up the research. All the other tools serve more as discovery tools, rather than robustness check tools.
16:28:26 <carrington[m]> hansams[m]:  as far as I'm aware there are no targeted Monero outreach proposals like that one, and none have ever been funded by the CCS
16:28:56 <mj-xmr[m]> selsta: Unless the tool is finished. Then I'm more free for the internal development.
16:29:02 <selsta> mj-xmr[m]: yes, I think it was fine for the last CCS to port the tool but continuing to work full time on it for months now just isn't a good way to spend dev focus on my opinion
16:29:13 <mj-xmr[m]> mj-xmr[m]: But still, the decision is yours.
16:29:28 <selsta> in your last CCS it sounded like the tool is already coded and you would just port it
16:30:19 <selsta> so I was surprised that you want to continue focus on it for 3 months
16:31:30 <mj-xmr[m]> Yes and this happened. But still, these were just 3 months. Is this a lot for such a tool, you think?
16:31:31 <mj-xmr[m]> One could work with the tool already somehow. This was my goal. But quite a few features can still be ported. I could tell more about them, if there's such a need.
16:32:25 <selsta> If we want to fund someone for months to work on a tool there have to be clear benefits on using it over existing tools. That's why I wanted a comment from Rucknium[m].
16:32:33 <mj-xmr[m]> Otherwise, here's the development plan:
16:32:33 <mj-xmr[m]> https://github.com/mj-xmr/tsqsim/wiki
16:32:33 <mj-xmr[m]> There are some new requests from Ruck.
16:32:49 <bigbklynballs[m]> > <@mj-xmr[m]:libera.chat> Otherwise, here's the development plan:
16:32:49 <bigbklynballs[m]> > https://github.com/mj-xmr/tsqsim/wiki
16:32:49 <bigbklynballs[m]> > There are some new requests from Ruck.
16:32:49 <bigbklynballs[m]> What's the final goal of this ?
16:32:57 <bigbklynballs[m]> The tool for ... ?
16:34:49 <mj-xmr[m]> Initially it was meant to predict the expected number of transactions in a given time step (for OSPEAD - decoy algo), but after various discussions, many people have found other uses of the tool for predicting also other values than the transaction numbers. Examples include: Seraphis CPU drainage and input for adaptive mining.
16:35:13 <carrington[m]> It would be beneficial is there was someone else who has reviewed your work in depth who could comment on the need for this proposal. Although I realize it is difficult to get reviewers.
16:36:23 <bigbklynballs[m]> mj-xmr[m]: machine learning model that predicts number of transactions, and your tool is for training such model or evaluation of such model ?
16:36:40 <mj-xmr[m]> @carrington I think too, that Rucknium would be the best person to comment. Let's maybe give him some time and comment under the proposal, when he finds time?
16:37:03 <netrik182> +1 for mj-xmr suggestion ^
16:37:50 <bigbklynballs[m]> mj-xmr[m]: What does it mean "Seraphis CPU drainage" ?
16:38:21 <mj-xmr[m]> > <@bigbklynballs[m]:libera.chat> > <@mj-xmr[m]:libera.chat> Initially it was meant to predict the expected number of transactions in a given time step (for OSPEAD - decoy algo), but after various discussions, many people have found other uses of the tool for predicting also other values than the transaction numbers. Examples include: Seraphis CPU drainage and input for adaptive mining.
16:38:21 <mj-xmr[m]> > 
16:38:21 <mj-xmr[m]> > machine learning model that predicts number of transactions, and your tool is for training such model or evaluation of such model ?
16:38:21 <mj-xmr[m]> Preferably classical TSA (AR/MA, ARIMA, SARIMA, etc.) for simplicity. Coding ML can be left for a plugin dev. The tool serves as both training tool and evaluation of the model via Walk Forward Validation (or Optimization)
16:39:03 <carrington[m]> Yes the gitlab comments have only been available for a week so there is plenty of time
16:39:34 <carrington[m]> c. j-berman full-time 3 months part 2
16:39:34 <carrington[m]> https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/285
16:39:41 <selsta> support ^
16:39:56 <mj-xmr[m]> > <@bigbklynballs[m]:libera.chat> > <@mj-xmr[m]:libera.chat> Initially it was meant to predict the expected number of transactions in a given time step (for OSPEAD - decoy algo), but after various discussions, many people have found other uses of the tool for predicting also other values than the transaction... (full message at https://libera.ems.host/_matrix/media/r0/download/libera.chat/58d25c8ac35f03c9a1d9f41e9664c3ee5e70f1c3)
16:40:51 <carrington[m]> https://www.reddit.com/r/Monero/comments/skjtjd/jberman_final_ccs_update_feedback_welcome/
16:41:55 <Rucknium[m]> (Collecting my thoughts on this) I will say that my own pace on OSPEAD and related matters hasn't kept up with mj-xmr  's pace on developing tsqsim, since I have not yet arrived at the computational time series portion of the work.
16:42:00 <carrington[m]> It looks like jberman[m] is not around right now, but this CCS proposal was also only made recently
16:42:26 <netrik182> I support jberman's proposal
16:42:32 <bigbklynballs[m]> > <@mj-xmr[m]:libera.chat> > <@bigbklynballs[m]:libera.chat> > <@mj-xmr[m]:libera.chat> Initially it was meant to predict the expected number of transactions in a given time step (for OSPEAD - decoy algo), but after various discussions, many people have found other uses of the tool for predicting also... (full message at https://libera.ems.host/_matrix/media/r0/download/libera.chat/8690795fa763b253dcc791070a41fb3663bcee23)
16:42:38 <netrik182> will left a comment on gitlab
16:42:55 <Rucknium[m]> I had to carry out some BCH work that I had committed to before OSPEAD ( See https://read.cash/@Rucknium/update-on-cashfusion-red-team-phase-one-flipstarter-4dc6e95f if you are curious on that at all. )
16:43:55 <bigbklynballs[m]> > <@mj-xmr[m]:libera.chat> > <@bigbklynballs[m]:libera.chat> > <@mj-xmr[m]:libera.chat> Initially it was meant to predict the expected number of transactions in a given time step (for OSPEAD - decoy algo), but after various discussions, many people have found other uses of the tool for predicting also... (full message at https://libera.ems.host/_matrix/media/r0/download/libera.chat/74836f18ba6618e9a26db89f9a17423b7e679936)
16:44:26 <mj-xmr[m]> > <@bigbklynballs[m]:libera.chat> > <@mj-xmr[m]:libera.chat> > <@bigbklynballs[m]:libera.chat> > <@mj-xmr[m]:libera.chat> Initially it was meant to predict the expected number of transactions in a given time step (for OSPEAD - decoy algo), but after various discussions, many people have found other uses of the... (full message at https://libera.ems.host/_matrix/media/r0/download/libera.chat/0b61f23d8ee30444ea072185510666a6de2039ec)
16:44:38 <Rucknium[m]> Also for a while I have been struggling with some strange behavior in my "dry run" of OSPEAD that seemed "simple" since it _sort of_ involved the order in which to apply logarithms, but I believe in the last few days I have resolved the problem, or at least found an alternative route.
16:46:38 <bigbklynballs[m]> > <@mj-xmr[m]:libera.chat> > <@bigbklynballs[m]:libera.chat> > <@mj-xmr[m]:libera.chat> > <@bigbklynballs[m]:libera.chat> > <@mj-xmr[m]:libera.chat> Initially it was meant to predict the expected number of transactions in a given time step (for OSPEAD - decoy algo), but after various discussions, many... (full message at https://libera.ems.host/_matrix/media/r0/download/libera.chat/530c7863958027d5edda250c8b669286c9b0f5b1)
16:47:04 <Rucknium[m]> It's true that as formulated today, OSPEAD is computationally expensive. Many time series techniques are written by statisticians, not programmers, and are therefore slow. So a fast C++ implementation of things may be important to make it viable.
16:47:04 <carrington[m]> Thanks for the update Rucknium . 
16:47:06 <mj-xmr[m]> > <@bigbklynballs[m]:libera.chat> > <@mj-xmr[m]:libera.chat> > <@bigbklynballs[m]:libera.chat> > <@mj-xmr[m]:libera.chat> Initially it was meant to predict the expected number of transactions in a given time step (for OSPEAD - decoy algo), but after various discussions, many people have found other uses of the... (full message at https://libera.ems.host/_matrix/media/r0/download/libera.chat/5fd8a1cf392d45ff474854eef4d3dddeae7b54d9)
16:47:35 <mj-xmr[m]> > <@bigbklynballs[m]:libera.chat> > <@mj-xmr[m]:libera.chat> > <@bigbklynballs[m]:libera.chat> > <@mj-xmr[m]:libera.chat> > <@bigbklynballs[m]:libera.chat> > <@mj-xmr[m]:libera.chat> Initially it was meant to predict the expected number of transactions in a given time step (for OSPEAD - decoy algo), but after... (full message at https://libera.ems.host/_matrix/media/r0/download/libera.chat/0493076b88a4c8c98b4fd7a32d575265b562cd78)
16:47:50 <nioc> may be
16:47:55 <bigbklynballs[m]> rucknium[m]: Any example of inefficient code written by statistician ?
16:48:51 <mj-xmr[m]> nioc: May be important, but will surely be faster, if this is of any value.
16:49:31 <Rucknium[m]> Anyway, ideally I would be more advanced in my OSPEAD work so that I could catch up with mj-xmr  's place that he is at with tsqsim. I think with the logarithm issue mostly resolved, and therefore imminent public release of (part of) the OSPEAD technical specification, I may be there shortly.
16:50:32 <mj-xmr[m]> I'm not 100% ready with my tool either. It's good but not great yet.
16:50:33 <nioc> value would be cloning jberman :D
16:51:06 <mj-xmr[m]> "I'm sorry. I'm not Neo."
16:51:09 <Rucknium[m]> bigbklynballs[m]: I'm not sure since I haven't been able to delve into things. Broadly, poorly optimized statistical code written in a slow language can be tens or hundreds of times slower than well optimized statistical code written in a fast language.
16:51:21 <selsta> are there some benchmarks that comapare your tool to existing tools mj-xmr[m] ?
16:51:25 <carrington[m]> Well perhaps it makes more sense for mj's proposal to be delayed for some amount of time? Until OSPEAD has progressed a bit further
16:52:47 <bigbklynballs[m]> rucknium[m]: Do you know only slow languages ?
16:53:07 <mj-xmr[m]> selsta: I'm sure that it beats other ones, if not on the face value, then surely due to its parallelism (including network parallelism), so I didn't need it, but I can prepare some.
16:53:48 <mj-xmr[m]> > <@bigbklynballs[m]:libera.chat> > <@rucknium[m]:libera.chat> bigbklynballs[m]: I'm not sure since I haven't been able to delve into things. Broadly, poorly optimized statistical code written in a slow language can be tens or hundreds of times slower than well optimized statistical code written in a fast language.
16:53:48 <mj-xmr[m]> > 
16:53:49 <mj-xmr[m]> > Do you know only slow languages ?
16:53:49 <mj-xmr[m]> This is quite rude. Please give me a tool you want me to benchmark, so we can talk on some level.
16:54:52 <carrington[m]> I.e. I mean increase the "expiration date" on the CCS proposal
16:55:14 <mj-xmr[m]> carrington[m]: I'd be fine with this.
16:55:36 <carrington[m]> But again that proposal has only been up a week so maybe it is too early to make decision like that
16:57:20 <carrington[m]> In case people were not aware, since the last meeting there was also a large proposal for funding the Haveno dex which was ultimately withdrawn after lots of discussion on reddit and gitlab
16:57:48 <mj-xmr[m]> I'd love to know until the end of the month. 
16:57:49 <mj-xmr[m]> In the case that it should be delayed, shall I prepare an alternative one (in the way like selsta proposed)? If so, I'd like to start the alternative one in March anyway.
16:58:41 <carrington[m]> https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/284
16:58:42 <Rucknium[m]> bigbklynballs[m]: I mostly know R, which is generally a slow language. An experienced R programmer can avoid some issues that slow R down, but that only gets you so far.
16:59:30 <carrington[m]> On the agenda there is also 
16:59:30 <carrington[m]> d. 'Work in Progress' projects discussion
16:59:30 <carrington[m]> https://ccs.getmonero.org/work-in-progress/
17:00:33 <netrik182> I'd say to prepare a new one, yes mj-xmr
17:01:23 <msvb-web> Do we have a meeting now?
17:01:38 <netrik182> so you don't have to wait until Rucknium catchs up
17:02:03 <netrik182> started 1h ago msvb-web
17:02:04 <mj-xmr[m]> carrington: my https://ccs.getmonero.org/proposals/mj-part-time-2021-q4.html is complete with 3 reports. Just not paid yet. 
17:02:05 <mj-xmr[m]> The https://ccs.getmonero.org/proposals/mj-compil-time-reduction.html is scheduled for funds redistribution.
17:02:22 <plowsof[m]> After several months of inactivity, xmrSale has an update https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/246
17:02:22 <plowsof[m]> I was a bit upset with the 'anonymouse team' for this update, claiming that something was impossible but we already have a few examples of it. BusyBoredom the creator of AcceptXMR has offered to help them. (which does the thing they claim is impossible) 
17:03:06 <plowsof[m]> But at least theyre alive 👍️
17:05:25 <hansams[m]1> > <@carrington[m]:libera.chat> On the agenda there is also... (full message at https://libera.ems.host/_matrix/media/r0/download/libera.chat/cc9966b1a364b2ab5c088e212b1f30cf85374a36)
17:05:27 <carrington[m]> Keeping up with in-progress CCS work seems to be getting more difficult with the high number of projects in that category
17:06:59 <carrington[m]> Several of the CCS proposals are nontechnical, so it would be immensely helpful if anyone can take the time to verify their work or lend a hand.
17:07:25 <plowsof[m]> I also took a look at this 2~ year old proposal in limbo https://ccs.getmonero.org/proposals/36c3.html
17:08:23 <plowsof[m]> and made a suggestion to 'pay out' some of the funds to the volunteers involved. ajs_ attended , and is owed funds from it for some expenses + to pay off his ticket) 
17:08:52 <plowsof[m]> there was budget for volunteer expenses so Ajs is saying 50 euro per day * 5 = 250 (food / drink etc). + 30 euros to fully pay for his ticket. 290 is 1.0562639 percent of the google docs price of 27,455.26.  1.0562639 % of 560 xmr is 5.91507784xmr to be awarded to Ajs. Who wishes it to be donated to monerokon
17:09:18 <selsta> do we know if these funds were paid out or not in the first place?
17:09:28 <selsta> maybe it simply didn't get written into the ccs system
17:09:47 <plowsof[m]> ajs_: also has fund left over from xmr.radio and i quote "If is 5.915 XMR and there is a little over 17 XMR left from the Monero FM CCS, luigi1111 luigi1111_ would it be possible to reallocate these funds (~22.92 XMR) towards MoneroKon's CCS?"
17:09:57 <plowsof[m]> selsta: Diego said the funds have never been paid out
17:10:01 <netrik182> IIRC luigui was going to roll those fund to general fund
17:10:12 <selsta> plowsof[m]: it says 280 were paid out
17:10:18 <selsta> the remaining haven't?
17:10:18 <netrik182> then it could be used to fund monerokon if core sees fit
17:10:27 <plowsof[m]> The community donated for volunteer expenses and those volunteers where never paid
17:10:34 <plowsof[m]> let that sink in
17:11:00 <plowsof[m]> Ajs out of the kindness of his heart wishes for his funds to be donated to monerokon 
17:11:18 <carrington[m]> That is very generous of them. It would be good if you each could drop a comment in the gitlab to make the situation clear.
17:11:30 <carrington[m]> Anyway we are over the usual 1 hour, so I need to point out that I won't be available in 2 weeks to help with the meeting. If someone could volunteer to chair a meeting then it would be appreciated.
17:11:32 <hansams[m]1> carrington[m]: OK. Will look into the projects. Somehow it would be helpful to use some kind of tagging in the projects to make it more clear what it is all about.
17:11:50 <netrik182> this was discussed over #monero-events carrington
17:12:44 <plowsof[m]> selsta: i see.. we nee d clarification on this 
17:13:12 <selsta> lol luigi probably has no idea himself
17:13:35 <plowsof[m]> according to Diego Salazar  there was no payout 🤷
17:14:39 <nioc> up until the time that Diego was still working for core
17:14:54 <plowsof[m]> Ajs never received a cent for expenses (5 day/night food / tickets) (along with the other volunteers)
17:15:09 <nioc> but very much doubt anything has happened since then 
17:15:22 <carrington[m]> Thanks everyone for attending the meeting! Ending it here for the purposes of logs. 
17:15:27 <nioc> ty
17:15:33 <netrik182> thanks carrington
17:15:45 <plowsof[m]> thanks carrington 
17:16:12 <carrington[m]> hansams[m]: usually there are not so many all running at once
17:17:32 <carrington[m]> Reminder that there is a meeting in  #monero-events:monero.social  in around 45 minutes for Monerokon 2022 planning 
17:17:32 <plowsof[m]> SerHack: work in progress has taken a back seat as he is busy with mastering monero 2
17:17:34 <hansams[m]1> General question by newbie like me. So, the disussions are carried out in IRC channels, Reddit, Twitter? So, if there is nothing which catches eye, then it does not happen or exist in the community? Ot there are other, like dedicated work groups and discussions?
17:17:55 <carrington[m]> https://github.com/monero-project/meta/issues/661
17:19:03 <netrik182> also everyone is welcome to ask questions about the translation workgroup since we didn't get that far during the meeting
17:19:07 <nioc> hansams[m]1: this keeps an overview of many channels https://www.monero.observer/
17:19:35 <netrik182> my brief report is that there a new PR for monero gui waiting to be merged
17:20:06 <netrik182> and I'm trying to make screenshot context work on weblate
17:20:08 <carrington[m]> Looking forward to another edition of Mastering Monero!
17:20:20 <netrik182> still getting 404 erros when uploading them
17:20:51 <netrik182> s/there are/there is
17:21:26 <carrington[m]> Yes sorry we seemed to run out of time but I have to end the "meeting logs" somewhere. Discussion can of course carry on.
17:22:26 <netrik182> no need to apologize 
17:22:45 <netrik182> i'm always around 
17:25:27 <plowsof[m]> thanks netrik182 
17:31:28 <hansams[m]1> Thanks for the meeting. I am still getting use to all of it and learning and trying to get trough all this technical lingo (at leas to understand, what is important for me as non-techie to understand what not), but hopefully will be actively involved in close future. 
```

# Action History
- Created by: carrington1859 | 2022-02-09T10:42:38+00:00
- Closed at: 2022-03-19T04:45:37+00:00
