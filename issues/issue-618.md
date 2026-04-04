---
title: Monero Research Lab Meeting - Wed 13 October 2021 @ 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/618
author: carrington1859
assignees: []
labels: []
created_at: '2021-10-10T09:19:16+00:00'
updated_at: '2021-10-18T10:06:14+00:00'
type: issue
status: closed
closed_at: '2021-10-18T10:06:14+00:00'
---

# Original Description
https://forum.monero.space/d/139-monero-research-lab-meeting-wed-13-october-2021-at-1700-utc

Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

Time:
17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20211013T170000&p1=1440)

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

https://forum.monero.space/d/123-monero-research-lab-meeting-wed-06-october-2021-at-1700-utc

https://github.com/monero-project/meta/issues/616

# Discussion History
## UkoeHB | 2021-10-13T18:01:09+00:00
```
[10-13-2021 17:00:41] <UkoeHB> meeting time (https://github.com/monero-project/meta/issues/618)
[10-13-2021 17:00:43] <UkoeHB> 1. greetings
[10-13-2021 17:00:44] <UkoeHB> hello
[10-13-2021 17:00:57] <ArticMine> Hi
[10-13-2021 17:01:04] <rbrunner> Hello
[10-13-2021 17:01:10] <wfaressuissia> Hello
[10-13-2021 17:01:25] <Rucknium[m]> Reporting in.
[10-13-2021 17:01:42] <jberman[m]> Hello :)
[10-13-2021 17:03:50] <hxr404> hey there 👋
[10-13-2021 17:04:06] <UkoeHB> Today again will be ~open-ended. We can start with updates.
[10-13-2021 17:04:06] <UkoeHB> 2. what has everyone been working on lately?
[10-13-2021 17:05:39] <jberman[m]> Been working on the wallet-side binning implementation, should have a fairly fleshed out PoC ready for review today. I was writing up an overview of it yesterday and found a couple tweaks I want to make to make it stronger
[10-13-2021 17:06:29] <UkoeHB> me: I have continued to work on my Seraphis PoC. Today I was reminded how I suck at bit fiddling (this is broken https://github.com/UkoeHB/monero/blob/ace6c889a29838dde8494a82e21336bed6336314/src/mock_tx/mock_sp_core.cpp#L163).
[10-13-2021 17:07:12] <Rucknium[m]> (1) I have more or less finished writing out the mathematics of OSPEAD as a numerical optimization problem.
[10-13-2021 17:07:12] <Rucknium[m]> (2) Light recruiting efforts for MRL.
[10-13-2021 17:07:12] <Rucknium[m]> (3) An idea was floated to have a GUI interface for simulation of p2pool payouts. I may do it.
[10-13-2021 17:07:48] <Rucknium[m]> (4) Begun work on reproducing the Moser et al. (2018) analysis. jberman is helping with that.
[10-13-2021 17:10:10] <UkoeHB> Well I think we can move on. If anyone else has updates, feel free to drop them in as you want.
[10-13-2021 17:10:10] <UkoeHB> 3. discussion; any questions/comments/thoughts about anything on the agenda or the above updates or anything else? :)
[10-13-2021 17:11:06] <neptune> Re: transaction unlock_time, I have posted on-chain stats from the previous year (Oct 2020 - Oct 2021) to the GitHub issue: https://github.com/monero-project/research-lab/issues/78#issuecomment-941840213
[10-13-2021 17:11:11] <neptune> In the previous year, the timestamp lock was still not used, and block height locks only made up ~11% of usage otherwise. Most usage took place in unlock_time values < 15, which don't lock anything.
[10-13-2021 17:13:01] <UkoeHB> I want to bring up the multisig address generation refactor: https://github.com/monero-project/monero/pull/7877. This fixes serious problems with multisig address generation, but there doesn't seem to be anyone willing/able to review it... If things continue I may have to recommend disabling multisig completely until it is reviewed. Call to action: is there anyone out there who can dive in, learn how multisig works/is supposed to 
[10-13-2021 17:13:01] <UkoeHB> work, and review the PR?
[10-13-2021 17:13:34] <Rucknium[m]> neptune: Nice! Thank you. In #monero-space:monero.social there was some discussion about how a certain DNM likes time locks.
[10-13-2021 17:14:38] <rbrunner> "have to recommend disabling multisig completely until it is reviewed" Are the problems that bad with the current code?
[10-13-2021 17:14:43] <carrington[m]> rbrunner? They worked on multisig stuff in the past
[10-13-2021 17:14:44] <Rucknium[m]> UkoeHB: I suppose coinstudent2048[m] would be a good candidate.
[10-13-2021 17:15:20] <rbrunner> Yes! But only as a user. Did not have a clue when I tried to read up on the theory in UkoeHB's book :)
[10-13-2021 17:15:39] <Rucknium[m]> Maybe someone could set up a bounty for the PR review using http://bounties.monero.social/ ?
[10-13-2021 17:15:41] <UkoeHB> rbrunner: yes there is little or no protection against key cancellation or address hostage attacks during key gen
[10-13-2021 17:16:18] <neptune> Rucknium[m]: well, if they were referring to using unlock_time, they aren't currently using the timestamp mode.
[10-13-2021 17:17:01] <rbrunner> Yes, the idea of a bounty also crossed my mind. Maybe that would get the people who implemented the current full M/N multisig on board for a review
[10-13-2021 17:18:10] <rbrunner> Hmm, maybe has the problem to attract people that only pretend to review ... how would you notice that?
[10-13-2021 17:18:11] <carrington[m]> Seems difficult for some anon to prove they have reviewed a PR to the extent that they deserve a bounties payout
[10-13-2021 17:18:49] <Rucknium[m]> neptune: "We will probably soon limit XMR transactions to a certain max value because we are primarily a multisig market and as long as the monero developer don't come up with a decent multisig solution and locktime transaction support we wont favor XMR over BTC" <- That's what the DNM rep said
[10-13-2021 17:19:47] <Rucknium[m]> carrington[m]: I don't think we need an anon. Someone known to the community, but who might need a bit of an incentive to tackle the task.
[10-13-2021 17:19:52] <carrington[m]> The use of locktime in that instance is referring to the bitcoin type, I think
[10-13-2021 17:23:09] <neptune> My opinion otherwise from all the data (previous year and TheCharlatan's study) is that we would be safe to "remove support for" the timestamp locks (unlock_time > CRYPTONOTE_MAX_BLOCK_NUMBER) and for invalid values (unlock_time < block_height). I only see the block height lock as having any contention, since it is used, just rarely. We could just let it be still, and fix the others.
[10-13-2021 17:23:22] <ErCiccione> Haveno is willing to contribute to move things forward, but setting a bounty for a review doesn't sound optimal to me. Unless the reviewer is known
[10-13-2021 17:24:38] <rbrunner> That's a circle of maybe 5 people ...
[10-13-2021 17:24:57] <ErCiccione> Is the problem that we don't find reviewer because it's tricky to review the crypto? If that's the case maybe luigi1111 could take a look 
[10-13-2021 17:25:38] <ErCiccione> yeah but assuring that the reviewer has done a good job would be tricky if the person is unknown or unwilling to provide references.
[10-13-2021 17:26:32] <Rucknium[m]> Could we get isthmus 's company to review it? That may get expensive though. Or Cypher Stack?
[10-13-2021 17:28:13] <rbrunner> Expensive may still better than no multisig
[10-13-2021 17:28:24] <UkoeHB> imo the crypto isn't that crazy; most of it is algorithmic/protocol logic
[10-13-2021 17:28:25] <h4sh3d> UkoeHB: how long do you estimate the work for reviewing 7877?
[10-13-2021 17:28:40] <ErCiccione> This would be the first time that we don't have somebody able to review a pr in-house btw
[10-13-2021 17:28:41] <atomfried[m]> rucknium[m]: why not ask both?
[10-13-2021 17:28:58] <moneromooo> I'll review the code (as in, not the crypto). I was mostly afk today but I'll try to do it soon. luigi for the cypto would be ideal... stoffu also if you can interest them.
[10-13-2021 17:28:58] <ErCiccione> I'm not willing to work with cypherstack fyi
[10-13-2021 17:29:13] <UkoeHB> h4sh3d: maybe a week or two 
[10-13-2021 17:29:52] <UkoeHB> assuming you start out not know how it is supposed to work
[10-13-2021 17:29:59] <ErCiccione> sounds great thanks mooo
[10-13-2021 17:30:06] <Rucknium[m]> erciccione[m]: isthmus may be looking at a no-bid contract then ;)
[10-13-2021 17:33:35] <Rucknium[m]> UkoeHB: Is your Seraphis PoC CCS proposal ready to move to the "Funding required" stage?
[10-13-2021 17:34:01] <UkoeHB> Sure, it has been from the beginning
[10-13-2021 17:34:07] <h4sh3d> I take some time next week to do a review, but it's great if luigi can do it too
[10-13-2021 17:34:20] <UkoeHB> h4sh3d: great! thank you :)
[10-13-2021 17:35:46] * h4sh3d have to go sorry, cia
[10-13-2021 17:36:10] <rbrunner> Ah, regarding timelock: There was a post on Reddit, as decided here, to get feedback. IMHO nothing really surprising surfaced there.
[10-13-2021 17:36:12] <Rucknium[m]> A pointed question: Don't we have a fairly centralized personnel situation with both the CCS and GitHub maintainer being the same person? No offense at all intended to luigi, but it doesn't feel quite right.
[10-13-2021 17:36:35] <coinstudent2048[> I can't C++ and I don't know secure implementation practice. Sorry :(
[10-13-2021 17:37:18] <Rucknium[m]> The criteria for moving a CCS forward seems to be when luigi thinks that it is ready. Or maybe the criteria is written somewhere.
[10-13-2021 17:37:50] <fluffypony> that's pretty much how loose consensus works
[10-13-2021 17:37:53] <fluffypony> :-P
[10-13-2021 17:38:05] <fluffypony> https://en.wikipedia.org/wiki/Rough_consensus
[10-13-2021 17:38:19] <ErCiccione> Luigi considers feedback from the community, but at the end yes, it's at discretion of core
[10-13-2021 17:39:07] <carrington[m]> I think you are correct rucknium[m] about the centralization issue . It only became this way when snipa stopped being the lead maintainer
[10-13-2021 17:39:25] <ErCiccione> snipa was lead maintainer for a very short time
[10-13-2021 17:39:51] <UkoeHB> I think meta questions like that can be discussed in #monero-community. Does anyone else have research topics to discuss today? Otherwise we can end early.
[10-13-2021 17:41:30] <wfaressuissia> UkoeHB: can you mention explicitly minimum set of docs that describe math behind prev and new multisig ?
[10-13-2021 17:41:32] <UkoeHB> rbrunner: thank you for mentioning the reddit post; it seems there were a few ideas about use-cases (https://github.com/monero-project/research-lab/issues/78#issuecomment-935599960)
[10-13-2021 17:42:02] <wfaressuissia> prev (before your PR), new (after your PR)
[10-13-2021 17:43:48] <Rucknium[m]> UkoeHB: I have a topic: How do we fund researchers? I am making efforts to recruit, and things would be easier if the funding situation were clearer.
[10-13-2021 17:43:49] <UkoeHB> wfaressuissia: https://web.getmonero.org/resources/research-lab/pubs/MRL-0009.pdf and https://web.getmonero.org/library/Zero-to-Monero-2-0-0.pdf chapter 9; there are also a bunch of undocumented input-validation steps (i.e. there is nothing like an ietf protocol draft spec)
[10-13-2021 17:45:46] <UkoeHB> The existing code does not check that messages from other participants A) are from other participants (not rigorously anyway), B) contain the expected contents.
[10-13-2021 17:48:27] <UkoeHB> The main fundamental change between before/after is adding aggregation coefficients to the key-merge step (from the MRL paper). Other parts of the core algo are the same (aside from rigorous message validation).
[10-13-2021 17:53:47] <coinstudent2048[> Like does the existing code not check if EC points are not in the main subgroup?
[10-13-2021 17:54:55] <UkoeHB> No, it does not check that there is proper overlap between key shares recommended by different participants.
[10-13-2021 17:56:12] <UkoeHB> We are getting to the hour mark now. Should we meet again next week, same time? The discussion topics have slowed down the past couple meetings.
[10-13-2021 17:58:41] <coinstudent2048[> Hmm... I am not available this time period most of the time, but there seems to be questions and possible updates still, like rucknium[m]'s last, and (now) multisig review.
[10-13-2021 17:59:16] <UkoeHB> Ok fine with me. Let's meet again next week same time. Thank you for attending everyone.
```

# Action History
- Created by: carrington1859 | 2021-10-10T09:19:16+00:00
- Closed at: 2021-10-18T10:06:14+00:00
