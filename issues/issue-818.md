---
title: Monero Research Lab Meeting - Wed 29 March 2023, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/818
author: Rucknium
assignees: []
labels: []
created_at: '2023-03-28T21:17:19+00:00'
updated_at: '2023-04-11T23:51:16+00:00'
type: issue
status: closed
closed_at: '2023-04-11T23:51:16+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

[Join the Monero Matrix server if you don't already have a Matrix account.](https://forum.monero.space/d/79-how-to-join-the-monero-core-team-matrix-server-web)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20211027T170000&p1=1440)

Main discussion topics:

1. Greetings

2. Discussion with paper author(s): ["Range Proofs with Constant Size and Trustless Setup"](https://link.springer.com/chapter/10.1007/978-3-031-28694-0_28) 

3. Discuss: [Consider removing the tx_extra field](https://github.com/monero-project/monero/issues/6668).

4. Discuss: [Exploring Trustless zk-SNARKs for Monero's payment protocol](https://github.com/monero-project/research-lab/issues/100).

5. Improvements to the decoy selection algorithm ( [Decoy Selection Algorithm - Areas to Improve](https://github.com/monero-project/research-lab/issues/86), [Binning PoC](https://github.com/monero-project/research-lab/issues/88), [OSPEAD](https://ccs.getmonero.org/proposals/Rucknium-OSPEAD-Fortifying-Monero-Against-Statistical-Attack.html) ) @j-berman @Rucknium

6. Seraphis. ( [UkoeHB's Seraphis Proof of Concept work](https://ccs.getmonero.org/proposals/seraphis-wallet-poc-2.html), [Seraphis repo](https://github.com/UkoeHB/Seraphis) ).

7. MRL Meta: "Cat herding", i.e. prioritization of research areas and features. Active recruitment of technical talent, MRL structure, funding (@Rucknium & others) [MoneroResearch.info repository of Monero-related research papers](https://moneroresearch.info/), [Reddit discussion](https://www.reddit.com/r/Monero/comments/pkg3d6/the_monero_project_should_actively_recruit/)

8. Any other business

9. Confirm next meeting agenda


Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: UkoeHB

Previous meeting agenda/logs:

#815 

# Discussion History
## UkoeHB | 2023-04-05T17:01:07+00:00
`[03-29-2023 17:00:03] <UkoeHB> meeting time https://github.com/monero-project/meta/issues/818`
`[03-29-2023 17:00:04] <UkoeHB> 1. greetings`
`[03-29-2023 17:00:04] <UkoeHB> hello`
`[03-29-2023 17:00:09] <vtnerd__> hi`
`[03-29-2023 17:00:32] <ArticMine[m]> Hi I have to leave early today `
`[03-29-2023 17:00:37] <rbrunner> Hello`
`[03-29-2023 17:01:07] <kayabanerve[m]> Hello`
`[03-29-2023 17:02:01] <xmrack[m]> Hey`
`[03-29-2023 17:02:24] <hinto[m]> hi`
`[03-29-2023 17:02:57] <UkoeHB> 2. updates, what's everyone working on?`
`[03-29-2023 17:05:56] <xmrack[m]> The authors of the paper “Range Proofs with Constant Size and Trustless Setup" are here leonardo.mostarda emsczkp to discuss their paper and answer any questions we may have`
`[03-29-2023 17:06:25] <xmrack[m]> https://link.springer.com/chapter/10.1007/978-3-031-28694-0_28`
`[03-29-2023 17:06:45] <leonardomostarda> Hi nice to meet you all `
`[03-29-2023 17:06:53] <emsczkp[m]> Hi`
`[03-29-2023 17:07:42] <emsczkp[m]> we are the authors of the range paper proof paper`
`[03-29-2023 17:08:11] <Rucknium> I am monitoring Mordinals. The mint rate has seemed to slow down over the past 48 hours. As of about 24 hours ago, total number of Mordinal txs were 24,222. Sum of Mordinal tx sizes was 202 Megabytes. Total fees to mint Mordinals was 4.05 XMR.`
`[03-29-2023 17:09:17] <rbrunner> Good to have you on watch :) Interesting numbers.`
`[03-29-2023 17:09:35] <xmrack[m]> Thanks for coming emsczkp and leonardo.mostarda! `
`[03-29-2023 17:10:11] <leonardomostarda> xmrack[m]: You are welcome we are happy to clarify any doubts `
`[03-29-2023 17:10:55] <emsczkp[m]> xmrack[m]: is it just chat or some kind of videocall ?`
`[03-29-2023 17:11:19] <rbrunner> Old school chat only`
`[03-29-2023 17:11:45] <blankpage[m]> It is worth mentioning that the monero community has recently raised approx 130 XMR towards peer review/audit of bulletproofs++`
`[03-29-2023 17:11:45] <blankpage[m]> https://ccs.getmonero.org/proposals/bulletproofs-pp-peer-review.html`
`[03-29-2023 17:12:11] <rbrunner> Oh, that's filled already?`
`[03-29-2023 17:12:18] <leonardomostarda> great!!`
`[03-29-2023 17:12:24] <ofrnxmr[m]> 1.x xmr away`
`[03-29-2023 17:12:32] <blankpage[m]> 128.67 of 130`
`[03-29-2023 17:13:09] <ofrnxmr[m]> leonardo.mostarda:  we are not committed to bp++, and is why we have invited you here today. Would like to hear more about your solutions `
`[03-29-2023 17:13:13] <UkoeHB> re: the constant size range proof, is there a comprehensive security analysis in the works?`
`[03-29-2023 17:14:35] <xmrack[m]> The paper compares propf sizes with bulletproofs. I’d be curious to see how it compares to BP++`
`[03-29-2023 17:18:32] <leonardomostarda> <ofrnxmr[m]> "leonardo.mostarda:  we are not..." <- Our work is at preliminary stage. Our work seems to be sound and correct  the deep analysis is ongoing work in progress. However we were inspired by other works which have been proved`
`[03-29-2023 17:19:24] <plowsof11> bp++ author aims to have a new draft ready for April 14th, which is going to be re-looked at by CypherStack. adjusting the scope/price (as it will come with missing security proofs according to the author) `
`[03-29-2023 17:19:59] <AaronFeickert[m]> The paper seems to jump from security properties of the Halo2 design to conclusions about range proof security. Do you intend to extent the security proofs to cover this?`
`[03-29-2023 17:20:29] <AaronFeickert[m]> On an initial read of the paper, it was not immediately clear if/why this jump should be valid`
`[03-29-2023 17:20:45] <UkoeHB> leonardomostarda: do you have an estimate of the relative performance for proving/verification compared to BP? e.g. as a function of crypto operations`
`[03-29-2023 17:20:52] <leonardomostarda> <xmrack[m]> "The paper compares propf sizes..." <- We do not know BP+ but we can compare our approach with it.`
`[03-29-2023 17:21:17] <AaronFeickert[m]> That is, if the Halo2 construction is sound and ZK, and if the original BP paper relied on certain IPP properties (like WEE), do these necessarily play nicely together?`
`[03-29-2023 17:21:19] <rbrunner> It's already BP double plus :)`
`[03-29-2023 17:22:25] <AaronFeickert[m]> s/extent/extend`
`[03-29-2023 17:26:13] <emsczkp[m]> <AaronFeickert[m]> "The paper seems to jump from..." <- Yes, exactly. This is our ongoing work, we now have assumed the IPA argument relation of Halo as secure in our design. However, we need to prove the whole range proof when the new IPA relation is integrated.`
`[03-29-2023 17:27:39] <xmrack[m]> Context for BP++ https://moneroresearch.info/index.php?action=resource_RESOURCEVIEW_CORE&id=83&browserTabID=`
`[03-29-2023 17:27:58] <blankpage[m]> Incidentally you might be interested in presenting your work at https://monerokon.com/ in Prague 23rd-25th June`
`[03-29-2023 17:30:24] <xmrack[m]> The last sentence of the conclusion states "As future work, we will validate our approach in real case studies involving streams of sensor data" What do you mean by this?`
`[03-29-2023 17:32:58] <leonardomostarda> blankpage[m]: Nice we are very interested. We will submit.`
`[03-29-2023 17:33:20] <isthmus> Hi, sorry I’m late. Thanks so much emsczkp and leonardomostarda for taking the time to join us. `
`[03-29-2023 17:33:20] <isthmus> I’m on a call that is taking most of my attention, so apologies in advance if I’m not very responsive. Will try to catch up.`
`[03-29-2023 17:38:33] <emsczkp[m]> <AaronFeickert[m]> "That is, if the Halo2 constructi..." <- Referring to Halo and BP, they share the same security properties (WEE, HVZK) and hardness assumptions. I think they can play nicely together.`
`[03-29-2023 17:41:24] <UkoeHB> hmm are there any other topics to discuss, otherwise we can end it early? I'm not feeling great today`
`[03-29-2023 17:41:38] <leonardomostarda> <xmrack[m]> "The last sentence of the..." <- We are trying to develop private multi transfer payments in an IoT scenario. This involves a continuos stream of sensor data. `
`[03-29-2023 17:43:47] <leonardomostarda> <isthmus> "I’m on a call that is taking..." <- Thanks your interest `
`[03-29-2023 17:46:12] <xmrack[m]> <emsczkp[m]> "Yes, exactly. This is our..." <- Do you have any rough timelines for your ongoing work? Or is it too early to say. `
`[03-29-2023 17:48:02] <emsczkp[m]> Yes, this work has high priority since is part of my PhD`
`[03-29-2023 17:48:57] <AaronFeickert[m]> You're of course free not to say, but did the reviewers have any particular notes on the security model or analysis?`
`[03-29-2023 17:55:03] <ceetee[m]> <leonardomostarda> "Nice we are very interested..." <- if you have event specific questions you're welcome to join us in #monero-events:monero.social `
`[03-29-2023 17:55:32] <leonardomostarda> <AaronFeickert[m]> "You're of course free not to say..." <- The paper was published in a workshop. The number of pages were very very limited. We could not write a lot. A reviewer was asking about validation.`
`[03-29-2023 17:56:02] <AaronFeickert[m]> Yeah, page limits can be pretty brutal :/`
`[03-29-2023 17:58:22] <leonardomostarda> Anyway, we are very happy to collaborate with anyone interested in completing the work with the needed proofs. `
`[03-29-2023 17:59:47] <AaronFeickert[m]> Can you remind me if the construction supports efficient batch verification? I don't have the paper handy`
`[03-29-2023 18:00:12] <AaronFeickert[m]> And unfortunately don't recall if this was the case`
`[03-29-2023 18:01:00] <AaronFeickert[m]> BP and BP+ verify linearly-ish, but shared generators mean pretty big savings in batch`
`[03-29-2023 18:01:41] <UkoeHB> ah, are there any plans to publish the paper outside springer? the paywall makes things difficult outside academia`
`[03-29-2023 18:02:22] <AaronFeickert[m]> Yeah, posting the submission version (if allowed) to ePrint would be great`
`[03-29-2023 18:02:35] <AaronFeickert[m]> I'd be very surprised if you weren't allowed`
`[03-29-2023 18:03:22] <emsczkp[m]> AaronFeickert[m]: Yes the work support batch verification and aggregation of range values. In fact the evaluation shows a constant proof size when the number of range values increase.`
`[03-29-2023 18:03:37] <AaronFeickert[m]> Nice`
`[03-29-2023 18:03:54] <AaronFeickert[m]> I'll need to review the details on this later`
`[03-29-2023 18:09:01] <emsczkp[m]> <AaronFeickert[m]> "Yeah, posting the submission..." <- yes by extending the work we could publish on a different journal`
`[03-29-2023 18:10:11] <AaronFeickert[m]> Oh I just meant posting the original preprint to the archive for open access`
`[03-29-2023 18:10:53] <AaronFeickert[m]> Great way to get extra eyes on it`
`[03-29-2023 18:12:00] <emsczkp[m]> yes for the preprint is fine, there should't be any problems`
`[03-29-2023 18:15:28] <UkoeHB> we are well past the hour, so in case anyone was wondering the meeting is over`
`[03-29-2023 18:15:40] <UkoeHB> next week we will return to the tx_extra discussion`
`[03-29-2023 18:15:53] <UkoeHB> thanks for attending everyone`
`[03-29-2023 18:17:36] <emsczkp[m]> thanks for inviting us to the meeting, should we join next week ?`
`[03-29-2023 18:18:33] <xmrack[m]> leonardo.mostarda: emsczkp Thanks again for coming. You're free to come any week you'd like :) but don't feel obligated. This room is open 24/7 to discuss Monero related research.`
`[03-29-2023 18:19:36] <leonardomostarda> Thanks, for sure we keep you updated with the progress of our work.`

# Action History
- Created by: Rucknium | 2023-03-28T21:17:19+00:00
- Closed at: 2023-04-11T23:51:16+00:00
