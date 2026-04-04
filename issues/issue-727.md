---
title: Monero Research Lab Meeting - Wed 24 August 2022
source_url: https://github.com/monero-project/meta/issues/727
author: Rucknium
assignees: []
labels: []
created_at: '2022-08-23T19:43:45+00:00'
updated_at: '2022-08-29T23:13:40+00:00'
type: issue
status: closed
closed_at: '2022-08-29T23:13:40+00:00'
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

#726 

# Discussion History
## UkoeHB | 2022-08-24T18:06:15+00:00
`[08-24-2022 17:00:02] <UkoeHB> meeting time https://github.com/monero-project/meta/issues/727`
`[08-24-2022 17:00:02] <UkoeHB> 1. greetings`
`[08-24-2022 17:00:02] <UkoeHB> hello`
`[08-24-2022 17:00:37] <xmrack[m]> Hi`
`[08-24-2022 17:00:54] <Rucknium[m]> Hi`
`[08-24-2022 17:01:01] <rbrunner> Hello`
`[08-24-2022 17:03:57] <UkoeHB> looks like a low-turnout day, might be a short meeting`
`[08-24-2022 17:04:06] <UkoeHB> 2. updates, what's everyone working on?`
`[08-24-2022 17:04:44] <xmrack[m]> I’m finishing up my final report for the magic grant which will be released Sept 1.`
`[08-24-2022 17:05:40] <selsta> ooo123ooo1234567 posted an update on bulletproofs++ verification speed and it looks really promising for monero: https://github.com/monero-project/research-lab/issues/101`
`[08-24-2022 17:05:43] <UkoeHB> me: closed my previous ccs and opened a new one https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/338; started integrating tevador's mx25519 library into seraphis_lib to hopefully speed up the find-received scanning step (should have a performance test ready next week)`
`[08-24-2022 17:06:08] <selsta> though I don't know what his plans are with the code now`
`[08-24-2022 17:06:46] <Rucknium[m]> OSPEAD work. Some research into possible methods to probabilistically classify on-chain transactions by their decoy selection algorithms, which would decrease effective transaction uniformity.`
`[08-24-2022 17:07:46] <UkoeHB> selsta: an almost 3x speedup seems too good to be true, looking forward to the code if/when it becomes available`
`[08-24-2022 17:08:22] <selsta> UkoeHB: what part of the transaction verification is the bulletproof part? how would that translate to transaction verification?`
`[08-24-2022 17:08:47] <UkoeHB> iirc it's around half of the cost`
`[08-24-2022 17:09:35] <jberman[m]> me: I've been focused on wrapping up hard fork issues, atm specifically on more cleanly handling the case when an updated client connects to an older daemon and vice versa`
`[08-24-2022 17:10:28] <jberman[m]> I said last week I'd have a plan for moving forward with multisig to get it out of experimental but have been prioritizing the above. Will share my thoughts on it`
`[08-24-2022 17:10:34] <UkoeHB> ah looks like the batched verification isn't much faster in that test run`
`[08-24-2022 17:12:37] <UkoeHB> the speedup in proof construction would be a big win, making bps is really slow`
`[08-24-2022 17:14:21] <UkoeHB> 3. discussion, anything to discuss?`
`[08-24-2022 17:16:01] <UkoeHB> jberman[m]: ?`
`[08-24-2022 17:16:12] <jberman[m]> Preliminary plan of action on moving multisig forward:`
`[08-24-2022 17:16:33] <jberman[m]> Open discussion with veorq with UkoeHB  involved if willing, explain we'd like to get security proofs written for multisig and that our goal is to arrive at a well-vetted and safe multisig implementation that we are confident is no longer experimental. Will work together with veorq/koe to try to help explain the code so the security proofs can cover the entire multisig protocol`
`[08-24-2022 17:16:55] <jberman[m]> In that discussion, we'd discuss cost and time to completion estimates. Once we have a working framework established that is mutually agreeable toward achieving the above objective, would then look to funding`
`[08-24-2022 17:18:30] <Rucknium[m]> Sounds good to me`
`[08-24-2022 17:18:44] <UkoeHB> works for me`
`[08-24-2022 17:18:56] <selsta> would these security proofs also apply to seraphis multisig later?`
`[08-24-2022 17:19:37] <UkoeHB> not directly, because there is a new proof structure`
`[08-24-2022 17:20:14] <UkoeHB> the new proof is basically a schnorr signature though, so existing multisig security proofs should be easy enough to adapt`
`[08-24-2022 17:21:46] <selsta> ok, so we don't start with 0 again`
`[08-24-2022 17:22:40] <rbrunner> So all multisig wallets need to get "dissolved" before the Seraphis hardfork?`
`[08-24-2022 17:22:57] <UkoeHB> rbrunner: no, I have a migration strategy`
`[08-24-2022 17:23:11] <rbrunner> Oh, surprising`
`[08-24-2022 17:23:14] <UkoeHB> multisig groups just need to do one extra ceremony to migrate`
`[08-24-2022 17:26:04] <Rucknium[m]> jberman, at the last meeting you said "I think a change to the algo that would result in identifiable pools without a HF needs a very high bar to pass" I think it's possible to reduce the question to direct probability calculations, i.e. probability of correct guess of the real spend with current DSA vs. probability of guessing the real spend based on a probabilistic classification of the DSA that a given transaction is using in`
`[08-24-2022 17:26:04] <Rucknium[m]> a partial migration scenario.`
`[08-24-2022 17:26:19] <Rucknium[m]> Is such a comparison what you had in mind for the criterion?`
`[08-24-2022 17:27:28] <UkoeHB> rbrunner: https://github.com/UkoeHB/monero/blob/c822c7a90b18dfe5fa6c2f4661da85749f40bdb4/tests/unit_tests/seraphis_multisig.cpp#L144 this is account migration`
`[08-24-2022 17:28:06] <rbrunner> Thanks, interesting`
`[08-24-2022 17:28:27] <UkoeHB> oh, and you'd need to update legacy multisig accounts so they can do aggregation-style signing on legacy enotes`
`[08-24-2022 17:28:35] <UkoeHB> that's on my TODO`
`[08-24-2022 17:31:12] <Rucknium[m]> I have found a few candidate methods to classify on-chain rings by their DSA. xmrack may have additional ideas.`
`[08-24-2022 17:32:50] <jberman[m]> If we have a high proportion of rings where the probability it's constructed by old DSA diverges largely from the new DSA, that would be a no-go imo`
`[08-24-2022 17:35:07] <Rucknium[m]> No-go until a hard fork, I assume?`
`[08-24-2022 17:36:13] <jberman[m]> right. unless we're certain there is some glaring issue that must be fixed`
`[08-24-2022 17:39:17] <Rucknium[m]> There is a glaring issue. The question you pose, which you're right to pose, is if the cure is worse than the disease. Anyway, I think it's probably possible to get a clear, fairly precise answer on that.`
`[08-24-2022 17:41:18] <jberman[m]> sgtm`
`[08-24-2022 17:43:11] <Rucknium[m]> I'm probably going to need more funding for that analysis though 😅`
`[08-24-2022 17:47:21] <UkoeHB> are there any other topics anyone would like to discuss? questions?`
`[08-24-2022 17:49:24] <UkoeHB> ok I'll call it here, thanks for attending everyone`
`[08-24-2022 17:53:02] <UkoeHB> selsta: there aren't many google hits for bp++, do you think we should hit up bunz's team and possibly some others to review the paper?`
`[08-24-2022 17:56:00] <Rucknium[m]> We could also ask the paper's author if he has submitted it for publication anywhere.`
`[08-24-2022 17:57:09] <selsta> it would be great if ooo123ooo1234567 could clarify his plans on how to continue with bulletproofs++ now, he did say he spent time on checking security but i don't know what that entails`
`[08-24-2022 17:59:15] <Rucknium[m]> kayabanerve: Want to email the BP++ author and ask if it is under review anywhere?`
`[08-24-2022 17:59:31] <selsta> otherwise we can either try to contact the paper author or like you suggested someone who was involved with Bulletproofs`

# Action History
- Created by: Rucknium | 2022-08-23T19:43:45+00:00
- Closed at: 2022-08-29T23:13:40+00:00
