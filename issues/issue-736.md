---
title: Monero Research Lab Meeting - Wed 21 September 2022
source_url: https://github.com/monero-project/meta/issues/736
author: Rucknium
assignees: []
labels: []
created_at: '2022-09-18T20:06:44+00:00'
updated_at: '2022-09-24T22:17:58+00:00'
type: issue
status: closed
closed_at: '2022-09-24T22:17:58+00:00'
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

#734 

# Discussion History
## UkoeHB | 2022-09-21T17:36:04+00:00
`[09-21-2022 17:00:02] <UkoeHB> meeting time https://github.com/monero-project/meta/issues/736`
`[09-21-2022 17:00:02] <UkoeHB> 1. greetings`
`[09-21-2022 17:00:02] <UkoeHB> hello`
`[09-21-2022 17:00:28] <one-horse-wagon[> Hello.`
`[09-21-2022 17:00:37] <dangerousfreedom> Hello`
`[09-21-2022 17:03:28] <Rucknium[m]> Hi`
`[09-21-2022 17:05:26] <UkoeHB> hmm low turnout today`
`[09-21-2022 17:05:49] <UkoeHB> well, let's continue`
`[09-21-2022 17:05:51] <UkoeHB> 2. updates`
`[09-21-2022 17:07:57] <UkoeHB> me: wrote the first unit test of a seraphis tx spending legacy enotes, need to add a bunch more unit tests and update tx builders further (multisig will be a bit of work); also plan to write a serialization proof of concept for seraphis txs`
`[09-21-2022 17:08:49] <Rucknium[m]> In a few hours I will send the OSPEAD fully specified estimation plan to the scientific review panel, thus completing Milestone 1 of the CCS. It's about 80 pages. The plan is next week I will release a public version with about half of the content removed (for now).`
`[09-21-2022 17:09:00] <dangerousfreedom> This week I have been studying Seraphis again and opened a CCS (please upvote if you think it is useful). Although I have never contributed officially to Monero, it feels much less scary the tasks I am proposing to do in comparison to the work I did for moneroinflation. I should start getting my first results (or some problems) by next week regarding the audit framework.`
`[09-21-2022 17:10:48] <one-horse-wagon[> Rucknium: I know you are a specialist in advanced statistics and probability.  I have a question about gentian builds on the monero code which are done before a new verison is released.  How many iterations of the checksums would be conclusive that the code is in fact valid?  Keep in mind the code base is quite extensive and just a misplaced letter, or extra space, throws the checksum really askew.`
`[09-21-2022 17:11:31] <Rucknium[m]> Yes, but I'm not a specialist in cryptographically-secure probability.`
`[09-21-2022 17:11:32] <UkoeHB> one-horse-wagon[: do you mean how many people reporting the same checksum?`
`[09-21-2022 17:11:47] <Rucknium[m]> So thanks for the question, but there are probably better people to ask`
`[09-21-2022 17:11:55] <one-horse-wagon[> UkoeHB: yes`
`[09-21-2022 17:12:34] <UkoeHB> presumably only one is needed - one out of the group of people you trust`
`[09-21-2022 17:13:47] <Rucknium[m]> My naive guess is that it is (Pr(Checksum is valid for one run of the compilation))^N, where N is number of people who ran the compilation. Since it is presumably independent and identically distributed.`
`[09-21-2022 17:13:59] <UkoeHB> 3. we can do discussion; it will be a short meeting`
`[09-21-2022 17:14:15] <one-horse-wagon[> UkoeHB: I felt it was very low and one would work, in thinking about it.`
`[09-21-2022 17:15:11] <selsta> the best way is to build your own reproducible builds so that you don't have to trust others`
`[09-21-2022 17:16:02] <Rucknium[m]> dangerousfreedom: Could you explain task (1) in your CCS in more detail? The audit framework. So the goal is that the framework could be passed on to an audit firm or something? Is there a distinction between audit and peer review?`
`[09-21-2022 17:16:13] <one-horse-wagon[> selsta: Absolutely.  But the vast majority of Monero users don't have that capability and are dependent on others.`
`[09-21-2022 17:16:57] <UkoeHB> If someone releases binaries with a checksum that collides with the binaries produced by compiling from source, then no amount of re-confirmations will help you. The checksum only works in this case if you can't do a second preimage attack.`
`[09-21-2022 17:17:04] <jberman[m]> hi sorry I'm late. me: working through a bug from daemon/wallet hf compatibility check + finishing background sync mode + getting quotes on security proofs (and a comprehensive audit) for multisig from veorq and co (email going out today or tomorrow)`
`[09-21-2022 17:17:12] <dangerousfreedom> Rucknium[m]: No, the goal is to generate the proofs that you spend, received or that you have ownership on some inputs/outputs.`
`[09-21-2022 17:17:20] <jberman[m]> After I'm done with the first 2, planning to turn attention toward Seraphis`
`[09-21-2022 17:17:46] <dangerousfreedom> Very much like chapter 8 in ZtM2`
`[09-21-2022 17:18:06] <dangerousfreedom> But for Seraphis and providing code and information`
`[09-21-2022 17:18:50] <Rucknium[m]> So "audit" as in the same thing you did for moneroinflation?`
`[09-21-2022 17:19:51] <UkoeHB> If you concern is checksum-signers are colluding to claim that released binaries are compiled from public source code, then all you need is one checksum signer you trust to corroborate the other signers (or to reach a threshold of signers where you think 'collusion between all these people is very unlikely')`
`[09-21-2022 17:20:46] <dangerousfreedom> Rucknium[m]: No. It will be the code and some explanation regarding how to prove ownership of inputs and outputs.`
`[09-21-2022 17:21:04] <dangerousfreedom> Like the SpendProof that you have in your wallet`
`[09-21-2022 17:21:25] <Rucknium[m]> Ah ok`
`[09-21-2022 17:22:13] <Rucknium[m]> Sounds good...but general question: are we getting closer to formalizing Seraphis for peer review?`
`[09-21-2022 17:22:25] <dangerousfreedom> Koe still didnt do it so there are remaining tasks for me :p`
`[09-21-2022 17:22:39] <UkoeHB> Rucknium[m]: no progress has been made there`
`[09-21-2022 17:22:52] <UkoeHB> I need to update the paper once I am done with all this programming stuff`
`[09-21-2022 17:23:29] <vtnerd> also here - updating my serialization branch/patch to work with json and remove the tons of macro changes on the branch`
`[09-21-2022 17:23:35] <Rucknium[m]> Ok.`
`[09-21-2022 17:23:48] <vtnerd> and I started working on the noise protocol stuff for p2p, the code is a mess but in progress`
`[09-21-2022 17:24:16] <Rucknium[m]> vtnerd: Is there a written specification for the noise protocol?`
`[09-21-2022 17:24:20] <vtnerd> there might be a discussion on which mode to use, because there are some interesting tradeoffs with privacy and whether the protocol even bothers to do authentication`
`[09-21-2022 17:24:23] <vtnerd> yes`
`[09-21-2022 17:24:34] <vtnerd> its been formally verified, etc, and there's a website, pdfs`
`[09-21-2022 17:24:59] <one-horse-wagon[> UkoeHB Good point`
`[09-21-2022 17:25:06] <vtnerd> I also have an open PR of our slightly modified version - some of the mods have to do with backwards compatability (i.e. detecting non-encrypted mode)`
`[09-21-2022 17:25:42] <vtnerd> and some theres an i2p like modification for obscuring the first ephermal key, which isnt strictly necessary but makes fingerprinting slightly harder`
`[09-21-2022 17:25:55] <Rucknium[m]> How do I look up the protocol? Is it just called "noise protocol"?`
`[09-21-2022 17:26:00] <vtnerd> otherwise its whatever noise protocol says`
`[09-21-2022 17:26:21] <vtnerd> noiseprotocol.org`
`[09-21-2022 17:26:45] <Rucknium[m]> Thanks`
`[09-21-2022 17:26:49] <vtnerd> https://github.com/monero-project/monero/pull/8028`
`[09-21-2022 17:32:34] <UkoeHB> discussion about seraphis integration is slowly ramping up, it would be great if people could chime in/participate https://github.com/seraphis-migration/wallet3/issues`
`[09-21-2022 17:33:13] <UkoeHB> https://matrix.to/#/#no-wallet-left-behind:haveno.network`
`[09-21-2022 17:34:57] <UkoeHB> ok I think we can call it here, thanks for attending everyone`

# Action History
- Created by: Rucknium | 2022-09-18T20:06:44+00:00
- Closed at: 2022-09-24T22:17:58+00:00
