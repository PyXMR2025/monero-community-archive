---
title: Monero Research Lab Meeting - Wed 12 April 2023, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/825
author: Rucknium
assignees: []
labels: []
created_at: '2023-04-11T16:06:56+00:00'
updated_at: '2023-04-18T19:09:28+00:00'
type: issue
status: closed
closed_at: '2023-04-18T19:09:28+00:00'
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

#822 

# Discussion History
## UkoeHB | 2023-04-12T17:47:54+00:00
`[04-12-2023 16:59:55] <UkoeHB> meeting time https://github.com/monero-project/meta/issues/825`
`[04-12-2023 16:59:55] <UkoeHB> 1. greetings`
`[04-12-2023 16:59:55] <UkoeHB> hello`
`[04-12-2023 17:00:18] <rbrunner> Hello`
`[04-12-2023 17:00:36] <Rucknium[m]> Hi`
`[04-12-2023 17:02:23] <ArticMine[m]> Hi`
`[04-12-2023 17:03:37] <UkoeHB> looking to be a small meeting`
`[04-12-2023 17:03:37] <UkoeHB> 2. updates, what's everyone working on?`
`[04-12-2023 17:05:07] <UkoeHB> me: working on 'implementing seraphis' companion paper to the seraphis abstraction paper`
`[04-12-2023 17:06:10] <ArticMine[m]> I am working on updating the scaling and fee algorithms `
`[04-12-2023 17:06:45] <ArticMine[m]> In advance of my talk at Monerokon `
`[04-12-2023 17:07:10] <Rucknium[m]> Going to post effective ring size analysis for Mordinals and coinbase outputs tomorrow probably. Mordinal minting pretty much ceased on April 2nd. The worst daily effective ring size in the last month (considering Mordinals only) was about 14. As of yesterday, it is already back up to 15.8`
`[04-12-2023 17:07:43] <Rucknium[m]> worst mean effective ring size`
`[04-12-2023 17:08:43] <UkoeHB> did it stop due to the network-layer tx_extra relay constraint?`
`[04-12-2023 17:08:56] <john_r365[m]> @ArticMine - updates, as in, future changes to the fee algorithm? How so?`
`[04-12-2023 17:09:28] <plowsof11> v0.18.2.2 officially released , with the tx_extra limit. looking at my peer list i can see who has/not updated by the error messages when trying to send a tx. 'people seem to be updating' which is nice https://paste.debian.net/1277128/ `
`[04-12-2023 17:10:01] <Rucknium[m]> UkoeHB: I don't think so. I will refer to the cession as "without apparent cause"`
`[04-12-2023 17:10:06] <Rucknium[m]> The cession happened a week before the official release of 0.18.2.2`
`[04-12-2023 17:10:09] <rbrunner> UkoeHB: Mordinals probably stopped because a special fee was introduced`
`[04-12-2023 17:10:41] <UkoeHB> Rucknium[m]: cessation?`
`[04-12-2023 17:10:45] <Rucknium[m]> Er, cession is the wrong word. Means surrender territory.`
`[04-12-2023 17:10:53] <UkoeHB> rbrunner: ah`
`[04-12-2023 17:10:55] <Rucknium[m]> yeah lol`
`[04-12-2023 17:11:26] <Rucknium[m]> Mordinal minters could just use the old software. I'm not sure that's a complete explanation for it.`
`[04-12-2023 17:11:38] <rbrunner> It's almost ironic, as you could get the impression that the Mordinals devs take their NFTs serious, but not the "minters" ...`
`[04-12-2023 17:12:29] <vtnerd__> ive focused on LWS stuff again this past week (sadly)`
`[04-12-2023 17:12:50] <rbrunner> Rucknium[m]: Did you find more than two after April 2? Because only 2 new ones appear in the viewer web app`
`[04-12-2023 17:13:07] <ofrnxmr[m]> they stopped to work on transfers. mordinal devs werent the ones spamming`
`[04-12-2023 17:13:51] <ofrnxmr[m]> the spammers probably updated and got confused. the spam was so low quality for spam and as nfts, that it was just a senseless waste of 5xmr`
`[04-12-2023 17:13:56] <rbrunner> Yes, "transfers" now work. The Monero punks proudly tweeted about their first one`
`[04-12-2023 17:14:03] <UkoeHB> looks like the BP++ CCS is fully funded, so we can look forward to the results of that; plowsof11 what's the timeline look for that work?`
`[04-12-2023 17:14:16] <tevador> here is a 6 blocks old mordinal: https://xmrchain.net/search?value=8da183c297425e9e368d422845a9ddce963186b77c448372142cd6ebacbcfc0a`
`[04-12-2023 17:14:17] <Rucknium[m]> I think there are only two after April 2. My total count is 43083 now. Slightly above the count on the viewer web app I think.`
`[04-12-2023 17:14:56] <ArticMine[m]> 1) Reducing the surge factor for the short term median from 50 to 20 or 16`
`[04-12-2023 17:14:56] <ArticMine[m]> 2) Increasing the growth of the long term median from 1.7 to 2`
`[04-12-2023 17:14:56] <ArticMine[m]> 3) Considering the introduction of a third sanity median of 1,000,000 blocks to cap the long term median to Nielsen's Law of Bandwidth an initial growth  `
`[04-12-2023 17:15:02] <Rucknium[m]> Technically, transfer txs are also black marbles. Do I want to track them? No, but I guess I will have to eventually.`
`[04-12-2023 17:15:16] <ArticMine[m]> This is at protocol level`
`[04-12-2023 17:15:58] <rbrunner> tevador: Just now appears in the viewer app :)`
`[04-12-2023 17:16:11] <ArticMine[m]> Also consider the use of node relay for lower caps than at protocol `
`[04-12-2023 17:16:16] <plowsof11> BP++ CCS: we're still on the hook of the BP++ author : who promises updates for april 14th (no update as of yet)`
`[04-12-2023 17:16:52] <UkoeHB> ok`
`[04-12-2023 17:18:29] <ArticMine[m]> The idea is to have generous limits at protocol with lower limits at node relay `
`[04-12-2023 17:19:46] <xmrack[m]> Hi`
`[04-12-2023 17:20:05] <rbrunner> Is this two-limits system of sorts a new approach?`
`[04-12-2023 17:20:52] <john_r365[m]> Thanks for the update ArticMine - RE 2) Wasn't that a point of contention in Issue 70 discussions? With 2 being the original value, and then 1.7 agreed as a compromise when Justin expressed concern?`
`[04-12-2023 17:21:17] <john_r365[m]> Link to prior discussion: https://github.com/monero-project/research-lab/issues/70#issuecomment-785193630 - or perhaps I'm misunderstanding`
`[04-12-2023 17:21:38] <ArticMine[m]> In reality no because nodes and miners are not obligated to max out scaling`
`[04-12-2023 17:22:42] <ArticMine[m]> It does recognize that node relay can provide more flexibility `
`[04-12-2023 17:23:54] <ArticMine[m]> The protocol changes would introduce a third median to limit the growth of the long term median `
`[04-12-2023 17:24:49] <UkoeHB> is there a security concern? it sounds like overkill from what I remember about the fee design`
`[04-12-2023 17:25:36] <ArticMine[m]> This allows the long term median to be more flexible over the short to medium term while addressing some community concerns `
`[04-12-2023 17:26:18] <UkoeHB> what concerns?`
`[04-12-2023 17:26:31] <ArticMine[m]> UkoeHB: In my view the current situation is good enough, but there is some room for improvement `
`[04-12-2023 17:26:53] <ArticMine[m]> So there is not a security concern `
`[04-12-2023 17:29:09] <UkoeHB> ok, well are there any other topics to discuss today?`
`[04-12-2023 17:29:26] <ArticMine[m]> The main advantage is to allow a faster response of the long term median over a 3  month to a year while tightening the pricing of the growth of the short term median `
`[04-12-2023 17:29:33] <Rucknium[m]> I will include possible mitigations for Mordinals' privacy impact in the post. Here is my list. Any others? These are not necessarily "good" mitigations. Just possible ones:`
`[04-12-2023 17:29:41] <Rucknium[m]> - Exclude coinbases from decoy selection algorithm (in development)`
`[04-12-2023 17:29:41] <Rucknium[m]> - Exclude Mordinals from decoy selection algorithm`
`[04-12-2023 17:29:51] <Rucknium[m]> - Stop transfer of Mordinals by enforcing a decoy selection algorithm (could be transferred with cryptography)`
`[04-12-2023 17:29:51] <Rucknium[m]> - Alter tx_extra rules to make Mordinals less appealing (0.18.2.2 patch)`
`[04-12-2023 17:29:58] <Rucknium[m]> - Raise ring size`
`[04-12-2023 17:30:50] <UkoeHB> ArticMine[m]: at the very least it will be interesting to see your research and proposal`
`[04-12-2023 17:31:27] <john_r365[m]> Yep, looking forward to reading/hearing more on your research ArticMine`
`[04-12-2023 17:31:44] <UkoeHB> Rucknium[m]: seems comprehensive`
`[04-12-2023 17:33:06] <ofrnxmr[m]> Rucknium @rucknium:monero.social: i proposed the same to jeffro and jtgrasie`
`[04-12-2023 17:33:42] <ofrnxmr[m]> (not point 3), but thats where i ended up as well`
`[04-12-2023 17:35:54] <Rucknium[m]> It would be nice for people to try to come up with reasons not to exclude coinbase outputs from the standard decoy selection algorithm. AFAIK, there are no major reasons, but we don't want to overlook anything.`
`[04-12-2023 17:37:14] <Rucknium[m]> As of yesterday, if we only consider coinbase outputs to be black marbles, then average effective ring size is about 14.75`
`[04-12-2023 17:37:40] <Rucknium[m]> That's with the P2Pool payout efficiency upgrade on March 18`
`[04-12-2023 17:37:51] <ofrnxmr[m]> i often, more than id like, have 3-4 coinbase`
`[04-12-2023 17:38:13] <UkoeHB> changing the core wallet decoy selection algorithm just makes it even more difficult to replicate in alternate wallets`
`[04-12-2023 17:38:53] <UkoeHB> you can pretty much guarantee that all wallet implementations will be using different decoy selection algos`
`[04-12-2023 17:39:01] <Rucknium[m]> As of yesterday, the unluckiest 5th percentile is effective ring size 13 (only coinbases as black marbles)`
`[04-12-2023 17:39:05] <ofrnxmr[m]> you can do that now`
`[04-12-2023 17:39:13] <ofrnxmr[m]> im using a different algo than you`
`[04-12-2023 17:39:57] <rbrunner> Yes, but still means that we should increase complexity only after careful deliberation`
`[04-12-2023 17:40:09] <Rucknium[m]> Yeah we should be careful about changing the decoy selection algorithm when not at a hard fork. IMHO, that factor needs more study`
`[04-12-2023 17:40:10] <rbrunner> And weighing trade-offs`
`[04-12-2023 17:41:11] <ofrnxmr[m]> yeah, imo it should be saved for a hf.`
`[04-12-2023 17:45:05] <UkoeHB> hmm can we end the meeting here?`
`[04-12-2023 17:45:37] <ofrnxmr[m]> yes sir. thanks ukoehb`
`[04-12-2023 17:47:10] <UkoeHB> ok thanks for attending everyone`

# Action History
- Created by: Rucknium | 2023-04-11T16:06:56+00:00
- Closed at: 2023-04-18T19:09:28+00:00
