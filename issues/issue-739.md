---
title: Monero Research Lab Meeting - Wed 05 October 2022
source_url: https://github.com/monero-project/meta/issues/739
author: Rucknium
assignees: []
labels: []
created_at: '2022-10-04T16:12:53+00:00'
updated_at: '2022-10-11T13:51:26+00:00'
type: issue
status: closed
closed_at: '2022-10-11T13:51:26+00:00'
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

#738 

# Discussion History
## UkoeHB | 2022-10-06T17:45:54+00:00
`[10-06-22 16:51:39] <premined_POS> Thankful for being here`
`[10-06-22 16:57:56] <one-horse-wagon[> Hello.`
`[10-06-22 16:59:14] <hyc> hi`
`[10-06-22 17:00:17] <premined_POS> Not very good conection over here sorry 😅`
`[10-06-22 17:01:22] <Rucknium[m]> Hi`
`[10-06-22 17:01:23] <UkoeHB> hi, meeting time`
`[10-06-22 17:01:30] <rbrunner> Hello`
`[10-06-22 17:01:46] <dangerousfreedom> Hello`
`[10-06-22 17:01:52] <UkoeHB> agenda: https://github.com/monero-project/meta/issues/739`
`[10-06-22 17:04:05] <UkoeHB> 2. updates, what's everyone working on?`
`[10-06-22 17:04:21] <vtnerd> hello`
`[10-06-22 17:04:38] <ArticMine[m]> Hi`
`[10-06-22 17:05:58] <Rucknium[m]> Mostly working on non-Monero projects for now. The MAGIC Monero Fund will soon submit its grant application to some research grant databases. Hopefully that catches the attention of some researchers out there.`
`[10-06-22 17:05:58] <dangerousfreedom> First of all thank you very much for your donations! I will do my best to deliver a high quality job as proposed. This week I have been investigating the grootle proofs in seraphis. I have been trying to make a parallel implementation of it in order to better understand how it works, to correct some possible flaws (if I find any) and to facilitate the work of someone else who is going to audit before going to production`
`[10-06-22 17:05:58] <dangerousfreedom> someday.`
`[10-06-22 17:06:11] <UkoeHB> me: have been away from my desk quite a bit the past few weeks, didn't get much done last week; now back full-time to pound out the remaining seraphis library updates (finish unit testing legacy balance recovery for the legacy-seraphis transition, add legacy inputs to multisig, add coinbase tx type)`
`[10-06-22 17:07:33] <UkoeHB> I also owe rbrunner a seraphis serialization poc`
`[10-06-22 17:07:34] <jberman[m]> Hello - finished 8566 (bug fixes for `scan_tx`), next going to finish background sync mode, then likely Seraphis wallet work`
`[10-06-22 17:07:56] <vtnerd> not much has changed since my last update - except I've got two more things to look at, including a fingerprinting issue in p2p protocol`
`[10-06-22 17:07:56] <rbrunner> Yup :)`
`[10-06-22 17:08:24] <vtnerd> and I've still been going through the e2e encryption - may have to drop the noise method I planned due to fingerprinting`
`[10-06-22 17:10:02] <rbrunner> I finally had a closer look at the Seraphis library code. Interesting stuff that will keep me busy a while.`
`[10-06-22 17:10:43] <jberman[m]> I also emailed veorq ~1 week ago re: multisig security proofs but no answer yet. Emailed Inference yesterday (the ones who did the most recent review, and where veorq is also an advisor) and waiting on a response. If no response by next week I'll try to get better contacts`
`[10-06-22 17:11:03] <UkoeHB> 3. discussion`
`[10-06-22 17:13:02] <UkoeHB> well, anything to discuss? otherwise we can call it :)`
`[10-06-22 17:14:11] <jberman[m]> what's the fingerprinting issue vtnerd ?`
`[10-06-22 17:16:10] <dangerousfreedom> I have a general question. Next year, if everything goes well, we will have seraphis working on testnet and I was wondering if we really need a 'paper' of Seraphis to be peer-reviewed? I mean, all the cryptography stuff like grootle proofs (which is the main innovation) has been already very well documented by Tryptich and Groth/Bootle papers. So the remaining 'risk' to be peer reviewed would only be the ingenious work of`
`[10-06-22 17:16:10] <dangerousfreedom> Koe by separating the proofs, which is very ingenious but not so much risky in my opinion. Maybe a paper of 2 pages would do it? What do you think? Should we also have a paper explaining the new way of making membership proofs/ring signatures?`
`[10-06-22 17:17:24] <vtnerd> um, which? the encryption one is with static public key re-use across restarts, and toggling --proxy on/off, etc`
`[10-06-22 17:17:27] <UkoeHB> the seraphis composition proof is a novel scheme`
`[10-06-22 17:18:01] <premined_POS> dangerousfreedom All precautions are good`
`[10-06-22 17:18:08] <vtnerd> the other I'd like to not say much until I review the code, and post a PR`
`[10-06-22 17:18:15] <Rucknium[m]> dangerousfreedom: IMHO, yes, we do need formal peer review.`
`[10-06-22 17:18:35] <Rucknium[m]> ...which is separate from a code audit`
`[10-06-22 17:19:01] <dangerousfreedom> UkoeHB: Yeah, it is new but will follow the general scheme of the previous papers.`
`[10-06-22 17:20:03] <dangerousfreedom> Of course I agree that it is better to have but maybe my question was what if we dont? Does it 'legally' forbids us to use if someone presents a paper or make a patent of it?`
`[10-06-22 17:20:24] <jberman[m]> got it vtnerd :)`
`[10-06-22 17:20:57] <Rucknium[m]> If we don't, and there is a critical error, then the Monero network would probably be destroyed.`
`[10-06-22 17:21:51] <premined_POS> Aviation like redundancy and test are good including trivial scenarios`
`[10-06-22 17:22:19] <UkoeHB> it is standard practice to at least have security proofs for signature schemes`
`[10-06-22 17:23:10] <UkoeHB> full-scale security models for transaction protocols are more '[very] nice to have' but at least historically not standard practice`
`[10-06-22 17:24:06] <dangerousfreedom> Rucknium[m]: Well that doesnt follow, we could have infinite reviews of the code and the theory without publishing a paper. My question was just a theoretical one, I just want to know the implications of formality.`
`[10-06-22 17:24:36] <isthmus> RE your earlier comment dangerousfreedom - I can't speak to international patent law, but I'm somewhat familiar with the relevant US systems. One of the 3 required criteria for a US patent to be awarded is "novelty" and I believe that the existing public work would constitute "prior art" and render it unpatentable.`
`[10-06-22 17:24:46] <Rucknium[m]> Having a paper is the best way to have a review of the math. How would a review of the math work without a paper explaining it?`
`[10-06-22 17:25:26] <premined_POS> I understand the same thing`
`[10-06-22 17:25:34] <premined_POS> isthmus`
`[10-06-22 17:25:42] <dangerousfreedom> isthmus: Okay, I see. Thanks.`
`[10-06-22 17:25:43] <UkoeHB> dangerousfreedom: for example, I would not have found this if sarang hadn't gone through the entire exercise of security modeling to isolate the 'dual DL' assumption https://github.com/UkoeHB/break-dual-target-dl`
`[10-06-22 17:26:04] <Rucknium[m]> If we don't think we have the resources to have a peer review done, then we should figure out how to acquire those resources.`
`[10-06-22 17:26:12] <rbrunner> Maybe I did not follow close enough, but anyway: Where do any "security proofs" for Seraphis currently stand? Done? On your UkoeHB's To Do list? Meant for later paid work?`
`[10-06-22 17:26:58] <UkoeHB> rbrunner: it's in limbo until I get a chance to properly refresh the paper`
`[10-06-22 17:27:22] <rbrunner> Alright, thanks. One step after the other then :)`
`[10-06-22 17:27:46] <UkoeHB> after that we need to find someone to help us`
`[10-06-22 17:28:19] <dangerousfreedom> Thanks for the answers premined_POS and Rucknium `
`[10-06-22 17:28:28] <premined_POS> Need to leave, tank you all for your work`
`[10-06-22 17:30:13] <Rucknium[m]> To be clear, I'm not a cryptographer. But all the hacks and exploits of other protocols and software have made me extremely cautious.`
`[10-06-22 17:31:07] <rbrunner> Yes, and it's brand new and probably bleeding-edge stuff, at least in part.`
`[10-06-22 17:31:19] <Rucknium[m]> Even Monero had a counterfeiting bug, but it was caught and confirmed to be not exploited. It was fortunate that the structure of the exploit permitted the confirmation that it had not been used on mainnet.`
`[10-06-22 17:32:33] <rbrunner> Wil be interesting to see how we fare when looking for help, as UkoeHB said. You don't pick up qualified cryptographers by asking around at the bus stop.`
`[10-06-22 17:32:57] <rbrunner> Maybe one of those grants, who knows?`
`[10-06-22 17:33:16] <dangerousfreedom> I totally agree. I was just curious how formality relates to security of use of the code or idea.`
`[10-06-22 17:41:18] <UkoeHB> looks like we are done with the meeting, I'll call it here; thanks for attending everyone`
`[10-06-22 17:42:38] <one-horse-wagon[> <dangerousfreedom> "I totally agree. I was just..." <- I think rigorous run troughs on testnet are going to show a lot of things that are not foreseeable which can then be addressed.  It should be tested like nothing else like it before.`

# Action History
- Created by: Rucknium | 2022-10-04T16:12:53+00:00
- Closed at: 2022-10-11T13:51:26+00:00
