---
title: Monero Research Lab Meeting - Wed 15 March 2023, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/811
author: Rucknium
assignees: []
labels: []
created_at: '2023-03-14T17:10:13+00:00'
updated_at: '2023-03-22T00:27:20+00:00'
type: issue
status: closed
closed_at: '2023-03-22T00:27:20+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

[Join the Monero Matrix server if you don't already have a Matrix account.](https://forum.monero.space/d/79-how-to-join-the-monero-core-team-matrix-server-web)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20211027T170000&p1=1440)

Main discussion topics:

1. Greetings

2. Discuss: [Consider removing the tx_extra field](https://github.com/monero-project/monero/issues/6668).

3. Discuss: [Exploring Trustless zk-SNARKs for Monero's payment protocol](https://github.com/monero-project/research-lab/issues/100).

4. Improvements to the decoy selection algorithm ( [Decoy Selection Algorithm - Areas to Improve](https://github.com/monero-project/research-lab/issues/86), [Binning PoC](https://github.com/monero-project/research-lab/issues/88), [OSPEAD](https://ccs.getmonero.org/proposals/Rucknium-OSPEAD-Fortifying-Monero-Against-Statistical-Attack.html) ) @j-berman @Rucknium

5. Seraphis. ( [UkoeHB's Seraphis Proof of Concept work](https://ccs.getmonero.org/proposals/seraphis-wallet-poc-2.html), [Seraphis repo](https://github.com/UkoeHB/Seraphis) ).

6. MRL Meta: "Cat herding", i.e. prioritization of research areas and features. Active recruitment of technical talent, MRL structure, funding (@Rucknium & others) [MoneroResearch.info repository of Monero-related research papers](https://moneroresearch.info/), [Reddit discussion](https://www.reddit.com/r/Monero/comments/pkg3d6/the_monero_project_should_actively_recruit/)

7. Any other business

8. Confirm next meeting agenda


Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: UkoeHB

Previous meeting agenda/logs:

#808 

# Discussion History
## ajs-xmr | 2023-03-15T08:54:32+00:00
@Rucknium Approaching Monerokon presentation submission deadline (3rd April 2023 @ 00:00 UTC) - https://apply.monerokon.com

## UkoeHB | 2023-03-15T23:14:48+00:00
`[03-15-2023 16:59:52] <UkoeHB> meeting time https://github.com/monero-project/meta/issues/811 hopefully the matrix bridge works`
`[03-15-2023 16:59:52] <UkoeHB> 1. greetings`
`[03-15-2023 16:59:52] <UkoeHB> hello`
`[03-15-2023 17:00:08] <shalit[m]> hello`
`[03-15-2023 17:00:17] <rbrunner> Hello`
`[03-15-2023 17:00:20] <dangerousfreedom> Hello`
`[03-15-2023 17:00:20] <ArticMine[m]> Hello `
`[03-15-2023 17:01:14] <Rucknium[m]> Hi`
`[03-15-2023 17:01:14] <hgfrtdhbgff[m]> Hi!`
`[03-15-2023 17:02:13] <UkoeHB> 2. updates, what's everyone working on?`
`[03-15-2023 17:02:29] <heinrich[m]> hi`
`[03-15-2023 17:03:53] <hgfrtdhbgff[m]> I am looking into the discussions happening in "Consider removing the tx_extra field" (issue #6668). I have to say it's a really long one `
`[03-15-2023 17:05:01] <Rucknium[m]> Due to the power of (research) persuasion, the average waiting time to first transaction confirmation has fallen by a full minute in the last two months: https://www.reddit.com/r/Monero/comments/11nu4aj/monero_transaction_confirmations_are_now_60/ . Thanks to DataHoarder, sech1, ofrnxmr, xmrack, plowsof, and gingeropolous for helping the research process and/or contacting mining pools.`
`[03-15-2023 17:05:17] <UkoeHB> me: merged and updated ghostway[m]'s block id checkpoint cache to be used in enote stores, then jberman[m] sucked me into some deeper design optimizations for balance recovery`
`[03-15-2023 17:06:35] <xmrack[m]> Hi`
`[03-15-2023 17:06:48] <UkoeHB> Rucknium[m]: good work, quite an achievement`
`[03-15-2023 17:07:13] <Rucknium[m]> Thanks :)`
`[03-15-2023 17:07:42] <ArticMine[m]> Yes very good work `
`[03-15-2023 17:08:10] <hgfrtdhbgff[m]> Yes, that's amazing`
`[03-15-2023 17:08:17] <rbrunner> Somebody should calculate how many waiting years were wasted over the history of Monero :)`
`[03-15-2023 17:08:21] <plowsof11> good work Rucknium! Lovera also joined the effort in contacting pools`
`[03-15-2023 17:09:12] <dangerousfreedom> Awesome Rucknium !`
`[03-15-2023 17:09:44] <ArticMine[m]> rbrunner: The time savings will become apparent when Monero scales to it true potential `
`[03-15-2023 17:10:00] <ArticMine[m]> Hard to calculate now`
`[03-15-2023 17:10:49] <rbrunner> Right. Transactions now confirm in Rucknium time.`
`[03-15-2023 17:13:00] <UkoeHB> 3. discussion, today we return to the tx_extra topic`
`[03-15-2023 17:13:24] <UkoeHB> as a reminder, this is the choice matrix:`
`[03-15-2023 17:13:24] <UkoeHB> A) [remove tx extra]: tx utility flexibility tied to hardfork (or steganography)`
`[03-15-2023 17:13:24] <UkoeHB> B) [keep tx extra in some optimized form]: uniformity and scaling trade-offs depending on the solution`
`[03-15-2023 17:13:24] <UkoeHB>     1) leave as unlimited-size TLV field`
`[03-15-2023 17:13:24] <UkoeHB>     2) mandate maximum tx extra size (e.g. anything in 0 - 1000 bytes) (option: encrypted by default)`
`[03-15-2023 17:13:25] <UkoeHB>     3) mandate optional fixed-length tx extra size + encrypt by default`
`[03-15-2023 17:13:25] <UkoeHB>     4) mandate fixed-length tx extra for all txs + encrypt by default`
`[03-15-2023 17:13:26] <UkoeHB>     5) other`
`[03-15-2023 17:14:30] <ArticMine[m]> Can we narrow this down to A and B3`
`[03-15-2023 17:15:50] <hgfrtdhbgff[m]> I still against removing tx_extra field. Size limit/increase pricing for people trying to dump things inside this field sounds good.`
`[03-15-2023 17:15:51] <hgfrtdhbgff[m]> (Basically choose B) `
`[03-15-2023 17:16:10] <rbrunner> Ok for me to narrow down thus, I still stand at the same point regarding this.`
`[03-15-2023 17:16:14] <UkoeHB> To start the discussion, let's do a temperature check of the room. Let's have a period of 4 minutes where the only message people should post is in this format: LETTER [rating 0-5, 0 is abstain, 1 is strongly oppose, 5 is strong desire], for choices A and B3. If you have a strong opinion about something else, you may post that as well.`
`[03-15-2023 17:16:16] <UkoeHB> Starting now`
`[03-15-2023 17:16:40] <UkoeHB> me: A[2], B3[5]`
`[03-15-2023 17:16:50] <ArticMine[m]> Is there any support for B1, B2, B4 or B5?`
`[03-15-2023 17:17:27] <rbrunner> A[2], B3[4]`
`[03-15-2023 17:17:30] <hgfrtdhbgff[m]> B2`
`[03-15-2023 17:17:37] <hgfrtdhbgff[m]>  * B[2]`
`[03-15-2023 17:17:45] <ArticMine[m]> Me oppose anything other than A or B3`
`[03-15-2023 17:17:57] <UkoeHB> please follow the format`
`[03-15-2023 17:18:07] <hgfrtdhbgff[m]>  * B[2] / B[3]`
`[03-15-2023 17:18:45] <hgfrtdhbgff[m]> Could we create a poll to simplify this?`
`[03-15-2023 17:18:51] <ofrnxmr[m]> A[5] (keep for coinbase)`
`[03-15-2023 17:19:01] <tevador> A[4],B3[3]`
`[03-15-2023 17:19:20] <Rucknium[m]> A[4], B3[3]`
`[03-15-2023 17:20:44] <xmrack[m]> A[3], B3[3]`
`[03-15-2023 17:20:44] <ArticMine[m]> A[3] B3[4]`
`[03-15-2023 17:21:08] <UkoeHB> A decidedly inconclusive poll`
`[03-15-2023 17:21:21] <BawdyAnarchist[m> A[2], B3[5] (altho I'm not sure if my opinion is relevant. I'm just a pleb🫠)`
`[03-15-2023 17:21:24] <Alex|LocalMonero> A`
`[03-15-2023 17:21:46] <cryptogrampy[m]> A[5]`
`[03-15-2023 17:21:56] <Alex|LocalMonero> A[5]`
`[03-15-2023 17:22:28] <Alex|LocalMonero> B3[1]`
`[03-15-2023 17:25:29] <UkoeHB> Anyone feel like BRIEFLY summarizing the case for A?`
`[03-15-2023 17:27:27] <rbrunner> I think of it simply as "No tx_extra, impossible to have any problems with it", fwiw`
`[03-15-2023 17:27:47] <ofrnxmr[m]> Still supports merge mining / p2pool etc. Doesn't incentivize other, unproven or malicious purposes`
`[03-15-2023 17:29:25] <BawdyAnarchist[m> It's the simplest solution, and hypothetically the theoretical best for transaction uniformity. Steg, while possible, seems a bit unwieldy, costly, and unlikely to be commonly used.`
`[03-15-2023 17:30:30] <UkoeHB> The case for B3 is: reduces the chance of needing future hard forks to support arbitrary non-core functionality/innovations. Removing the tx_extra is an implicit commitment to perpetual future hard forks, which I view as a critical long-term weakness.`
`[03-15-2023 17:31:44] <hgfrtdhbgff[m]>  * A[1] / B[4]`
`[03-15-2023 17:31:49] <rbrunner> Aka "painting yourself into a corner"`
`[03-15-2023 17:31:50] <Alex|LocalMonero> (Some) of the case for A:... (full message at <https://libera.ems.host/_matrix/media/v3/download/libera.chat/d96ac1fba811d1d5baa0a98e565669ae7dbf7e0e>)`
`[03-15-2023 17:32:01] <ofrnxmr[m]> What would prevent us from adding it back? `
`[03-15-2023 17:32:01] <ofrnxmr[m]> Id like it removed sooner than later. And we can revisit when we do Seraphis (or another) hard fork. `
`[03-15-2023 17:32:51] <rbrunner> The same thing that prevents its removal for almost 3 years already? Split dev community.`
`[03-15-2023 17:32:55] <UkoeHB> ofrnxmr[m]: it's much easier to move to e.g. B3 then to A at a later date than from A to B3`
`[03-15-2023 17:33:42] <rbrunner> And no accepted decision process yet beyond "loose consensus" ...`
`[03-15-2023 17:33:44] <UkoeHB> from that standpoint alone, it is the more conservative choice`
`[03-15-2023 17:33:44] <ofrnxmr[m]> A would move data from Txextra to dedicated fields > wouldnt that be preferable to just leaving it in Txextra?`
`[03-15-2023 17:33:58] <UkoeHB> B3 is the more conservative approach*`
`[03-15-2023 17:34:52] <BawdyAnarchist[m> B3 does follow the principle of: When in doubt, make the least adjustment necessary.`
`[03-15-2023 17:35:15] <UkoeHB> ofrnxmr[m]: not everything that makes sense to go in a tx should go in a tx. Subaddresses were an experimental feature not enforced by consensus, as a prime example. They are being formalized in jamtis after what, 6-8 years of experimentation and experience?`
`[03-15-2023 17:35:44] <ofrnxmr[m]> Agreed it is the more conservative approach. But being making compromises or concessions doesnt necessarily make sense when the damage from removing it = "use monero how you thought I was last week".`
`[03-15-2023 17:35:44] <ofrnxmr[m]> Leaving doors unlocked, or bridges down, just leads to abuse (see mrl logs on chain)`
`[03-15-2023 17:35:47] <ArticMine[m]> The case for A is that there is no application now outside of merged mining in coinbase. This discussion does not apply to coinbase. `
`[03-15-2023 17:36:11] <UkoeHB> not everything that makes sense to go in a tx should go in the consensus-enforced structure of a tx.*`
`[03-15-2023 17:36:38] <ArticMine[m]> The case for B3 is to allow for some protocol flexibility outside of hard dorks`
`[03-15-2023 17:36:46] <Alex|LocalMonero> <UkoeHB> "The case for B3 is: reduces..." <- Have you ever tried developing an enterprise application for Bitcoin? It's a nightmare of libraries and applications that are often mutually incompatible. Someone implements one BIP, someone else thinks that BIP is a scam and ideologically rejects it. Every wallet/app becomes its own little application island that requires all other users have to use the same wallet/app to get`
`[03-15-2023 17:36:46] <Alex|LocalMonero> the benefits. This is not good, this is awful. I feel like there's a case of dev blindness. Just because something makes life more exciting for a dev doesn't mean it will lead to more actual usage. Code is read much more that it is written, therefore it's more important for code to be readable that for a coder to write a one-liner that encompasses 15 different ideas. Similarly, protocols are implemented more than they are`
`[03-15-2023 17:36:46] <Alex|LocalMonero> extended. It's much more important for the application builders to have less complexity to deal with than for a protocol dev to have more soft forking capability`
`[03-15-2023 17:38:21] <Alex|LocalMonero> As a business that utilizes both Bitcoin and Monero, I can tell you that it's much easier to develop for Monero than for Bitcoin because there isn't a million soft forks that our devs need to deal with on a constant basis.`
`[03-15-2023 17:38:35] <rbrunner> A [1] from about the insinuation that "dev blindness" could be a major factor for those voting for B3`
`[03-15-2023 17:38:41] <rbrunner> *from me`
`[03-15-2023 17:40:56] <UkoeHB> Alex|LocalMonero: that is a risk yes, but at the same time the tx_extra has not led to bifurcation of wallets after 8 years so it's not immediately clear that is a priority issue here`
`[03-15-2023 17:41:06] <ofrnxmr[m]> Communitues looking into tx extra, bar kaya and thorchain, are mostly looking into nfts, chat apps, and other stuff that I dont need in my blockchain storage devices `
`[03-15-2023 17:41:07] <ofrnxmr[m]> Wownero has Txextra 👍 `
`[03-15-2023 17:41:36] <hgfrtdhbgff[m]> For me the choose B:... (full message at <https://libera.ems.host/_matrix/media/v3/download/libera.chat/08714f04e32957f3cda3867bb1a80ccaa4d14811>)`
`[03-15-2023 17:42:23] <rbrunner> NFTs and chat apps? Now it gets a bit funny.`
`[03-15-2023 17:42:29] <ArticMine[m]> Alex|LocalMonero: This is a very valid point. The reason for Bitcoin's problems with multiple soft forks is a fundamental design flaw in Bitcoin that is not present in Monero  `
`[03-15-2023 17:42:36] <hgfrtdhbgff[m]>  * For me the choose B:... (full message at <https://libera.ems.host/_matrix/media/v3/download/libera.chat/2057ca0fbe52b1caaa529ed63b6365e8b43c535f>)`
`[03-15-2023 17:42:40] <ofrnxmr[m]> Exchanges can put your username in Txextra `
`[03-15-2023 17:43:14] <rbrunner> Yes. Do they? Today? We have tx_extra now, lest somebody forgets.`
`[03-15-2023 17:43:26] <ArticMine[m]> Bitcoin cannot hard fork because it cannot face this flaw`
`[03-15-2023 17:45:14] <rbrunner> And do people really think that if we go for B3 now, but come under a large-scale attack by somebody using it, we won't be able to react somehow?`
`[03-15-2023 17:45:29] <ArticMine[m]> Regardless of the decision between A and B3 I do not see Monero having Bitcoin's problems `
`[03-15-2023 17:45:29] <ofrnxmr[m]> React by doing A? `
`[03-15-2023 17:45:50] <rbrunner> Yes, of course, depending on the severity of the attack. I am not stupid.`
`[03-15-2023 17:46:05] <Alex|LocalMonero> <UkoeHB> "Alex | LocalMonero | AgoraDesk..." <- Yeah, mass adoption is saving us from that issue, *for now*.`
`[03-15-2023 17:46:21] <ofrnxmr[m]> ^`
`[03-15-2023 17:46:34] <ArticMine[m]> One can raise the fee on tx extra transactions via node relay to respond to such an attack `
`[03-15-2023 17:46:37] <rbrunner> Everything is *for now*, no?`
`[03-15-2023 17:47:03] <Alex|LocalMonero> Which is why tx_extra needs to be removed rbrunner `
`[03-15-2023 17:47:16] <ofrnxmr[m]> And for now, there are no uses nor anything on the horizon that needs it `
`[03-15-2023 17:47:32] <hgfrtdhbgff[m]> Do support`
`[03-15-2023 17:47:35] <rbrunner> Sadly kayabanerve is not here to contradict you`
`[03-15-2023 17:47:40] <bit_thanos[m]> ofrnxmr`
`[03-15-2023 17:47:40] <bit_thanos[m]> Exchanges can put your username in Txextra `
`[03-15-2023 17:47:44] <UkoeHB> removing tx_extra doesn't prevent attacks, since the same kinds of attacks can be trivially done with steganography\`
`[03-15-2023 17:47:46] <ofrnxmr[m]> Kaya doesnt need Txextra.`
`[03-15-2023 17:47:59] <ofrnxmr[m]> Its just a convenience `
`[03-15-2023 17:48:01] <kayabanerve[m]> Yes and no.`
`[03-15-2023 17:48:14] <kayabanerve[m]> I don't need it because of steganography. I do need it to be on-chain to ensure atomicity.`
`[03-15-2023 17:48:23] <kayabanerve[m]> There's a loss of funds risk without on-chain data encoding.`
`[03-15-2023 17:48:39] <kayabanerve[m]> *within my model which cannot be resolved without placing data on Monero in any model AFAICT`
`[03-15-2023 17:49:00] <bit_thanos[m]> Putting username in txextra is alone against keeping it`
`[03-15-2023 17:49:13] <kayabanerve[m]> Sending Monero, with no instructions on what to do with the Monero,, and no way to send it back, means the sender loses it. That requires some flow ensuring the Monero funds come with the data.`
`[03-15-2023 17:49:14] <BawdyAnarchist[m> But tx_extra will be encrypted`
`[03-15-2023 17:49:34] <kayabanerve[m]> I have an issue fully covering this discussion. While I do not need TX extra, I want to clarify it's only due to steganography tha's true.`
`[03-15-2023 17:49:53] <rbrunner> That "putting username into tx_extra" seems to impress.`
`[03-15-2023 17:49:57] <ofrnxmr[m]> Right 👍 @kaya`
`[03-15-2023 17:50:40] <kayabanerve[m]> https://github.com/serai-dex/serai/issues/253`
`[03-15-2023 17:50:43] <rbrunner> And because of stego everybody will wade through fake outputs. That's fun.`
`[03-15-2023 17:50:53] <ArticMine[m]> BawdyAnarchist[m: It can be encrypted to allow the recipient to read it `
`[03-15-2023 17:51:25] <rbrunner> Instead of tx_extra that they can simply ingnore.`
`[03-15-2023 17:51:33] <Rucknium[m]> BawdyAnarchist: Enforcing "encryption" on tx_extra would not be easy.`
`[03-15-2023 17:51:33] <ofrnxmr[m]> It could already be encrypted. We already know they use funky ring members etc`
`[03-15-2023 17:51:33] <kayabanerve[m]> This is a complete issue, on my end, discussing the lack of any data encoding. Please note the atomicity section specifically.`
`[03-15-2023 17:51:38] <Alex|LocalMonero> rbrunner: Having 0.01% extra outputs is better than having a loosy-goosy blockchain`
`[03-15-2023 17:51:55] <rbrunner> :)`
`[03-15-2023 17:53:14] <kayabanerve[m]> I estimate +4 outputs per TX. TC does thousands of BTC TXs a day AFAIK.`
`[03-15-2023 17:53:31] <rbrunner> kayabanerve: Did you read in the backlog about the opinion poll? Where would you stand regarding A versus B3? That 0..5 story.`
`[03-15-2023 17:53:57] <kayabanerve[m]> Sorry, I literally just got here. I'll read up no`
`[03-15-2023 17:54:00] <kayabanerve[m]> *now`
`[03-15-2023 17:54:28] <ofrnxmr[m]> TC wont integrate monero til im 1063 year old. And they "promised" not to abuse tx extra `
`[03-15-2023 17:54:43] <ofrnxmr[m]> Sounds reliable.`
`[03-15-2023 17:54:44] <rbrunner> TC being Thorchain?`
`[03-15-2023 17:54:51] <ofrnxmr[m]> Yes sir`
`[03-15-2023 17:55:03] <BawdyAnarchist[m> Removing tx_extra kind of ensures that some people will use steg, doesn't it? Which harms the weakest part of XMR privacy - the # of ring members.`
`[03-15-2023 17:55:05] <kayabanerve[m]> B2 is my preference, yet B3/B4 would also be fine. I think A is stupid yet I'll survive.`
`[03-15-2023 17:55:29] <ArticMine[m]> ... but someone else may fork TC`
`[03-15-2023 17:55:31] <kayabanerve[m]> Which I say as a real world user while I also legitimately expect to be a significant real-world TX driver in the future.`
`[03-15-2023 17:55:46] <ofrnxmr[m]> Kaya ^ ArticMine @ArticMine:libera.chat:  serai works like thorchain `
`[03-15-2023 17:56:07] <kayabanerve[m]> Yes, I did mean THORChain. Specifically, I'm interested in: If Serai matches TC' BTC swap count, with XMR, then that may be thousands of 'poison' outputs a day without TX extra`
`[03-15-2023 17:56:30] <Alex|LocalMonero> Why is it a poison output if it's just a transaction?`
`[03-15-2023 17:56:32] <kayabanerve[m]> The larger issue is we publish our entire wallet info, so the TX extra privacy issue is irrelevant.`
`[03-15-2023 17:57:00] <kayabanerve[m]> Without TX extra though, we're now putting forth more bad outputs, assuming we haven't moved to a full chain membership proof yet`
`[03-15-2023 17:57:02] <kayabanerve[m]> Alex | LocalMonero | AgoraDesk: Globally increased scan time + invalid decoy`
`[03-15-2023 17:57:30] <rbrunner> Yeah, but will outsiders be able to determine they are invalid?`
`[03-15-2023 17:57:35] <kayabanerve[m]> ... immediately defeatable decoy`
`[03-15-2023 17:57:41] <kayabanerve[m]> rbrunner: We publish view keys and all TX data.`
`[03-15-2023 17:57:51] <ofrnxmr[m]> Either way ^ `
`[03-15-2023 17:57:55] <kayabanerve[m]> That's not a TX extra issue, that's an accountability issue.`
`[03-15-2023 17:57:59] <Alex|LocalMonero> kayabanerve: and how exactly does having tx_extra prevent a malicious actor from poisoning everyone's decoys in the same way?`
`[03-15-2023 17:58:13] <Alex|LocalMonero> Aren't you conflating two separate issues?`
`[03-15-2023 17:58:14] <ofrnxmr[m]> It doesnt`
`[03-15-2023 17:58:25] <kayabanerve[m]> Except instead of poisoning the one output to us, and noting the other output in the TX is a Serai user, we're now discussing poisoning 5 outputs and fingerprinting a sixth.`
`[03-15-2023 17:58:36] <kayabanerve[m]> Alex | LocalMonero | AgoraDesk: It makes the issue 5x worse if I don't have TX extra.`
`[03-15-2023 17:58:59] <Alex|LocalMonero> Bro I'm not worried about Serai poisoning, I'm worried about an actual malicious actor poisoning the chain.`
`[03-15-2023 17:59:02] <ofrnxmr[m]> Which is counterproductive to doing it`
`[03-15-2023 17:59:19] <Alex|LocalMonero> Your DEX won't have any impact compared to a determined attacker.`
`[03-15-2023 17:59:41] <ofrnxmr[m]> "Use xmr for private swaps that hurt privacy"`
`[03-15-2023 17:59:43] <kayabanerve[m]> Since TC has had 25k TXs today, if I assume they're all swaps, and BTC (tied for the largest pool) is just 20%... we're discussing 20k publicly revealed outputs if TX extra isn't available.`
`[03-15-2023 17:59:52] <kayabanerve[m]> Without a full chain membership proof, that could be extremely damaging.`
`[03-15-2023 18:00:14] <ofrnxmr[m]> Haveno and bisq dont use Txextra, right?`
`[03-15-2023 18:00:17] <kayabanerve[m]> *If Serai has that same usage as TC has accomplished with BTC`
`[03-15-2023 18:00:29] <Alex|LocalMonero> If`
`[03-15-2023 18:00:30] <ofrnxmr[m]> Off topic, sorry`
`[03-15-2023 18:00:30] <kayabanerve[m]> No. They also don't publish view keys of participants.`
`[03-15-2023 18:00:56] <kayabanerve[m]> Alex | LocalMonero | AgoraDesk: Sure, if. I generally bet on myself and I don't feel this is a totally out of this world estimation.`
`[03-15-2023 18:01:12] <kayabanerve[m]> I think it's decently sane and should be noted.`
`[03-15-2023 18:01:27] <LyzaL> would an attacker abusing tx extra to poison outputs be like, effectively a normal flood attack, except the data for bad decoys becomes public?`
`[03-15-2023 18:01:50] <rbrunner> A really good DEX could become a success. If people doubt that, that would be strange.`
`[03-15-2023 18:01:51] <kayabanerve[m]> The theoretical model is the actor keeps it to themselves/chosen accomplices, but yes.`
`[03-15-2023 18:02:14] <kayabanerve[m]> I cited the real world numbers of an comparable product.`
`[03-15-2023 18:02:17] <UkoeHB> It's past the hour and y'all are getting into the weeds so I'll call it here. The meeting is over but you may continue the discussion.`
`[03-15-2023 18:02:26] <ofrnxmr[m]> Thank you Koe`
`[03-15-2023 18:02:33] <rbrunner> +1`
`[03-15-2023 18:03:15] <ArticMine[m]> Thank you Joe. The meeting has made progress on tx extra `
`[03-15-2023 18:03:31] <Alex|LocalMonero> Thanks UkoeHB `

# Action History
- Created by: Rucknium | 2023-03-14T17:10:13+00:00
- Closed at: 2023-03-22T00:27:20+00:00
