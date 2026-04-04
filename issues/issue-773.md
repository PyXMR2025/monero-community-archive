---
title: Monero Research Lab Meeting - Wed 28 December 2022, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/773
author: Rucknium
assignees: []
labels: []
created_at: '2022-12-24T01:55:48+00:00'
updated_at: '2023-01-03T23:05:46+00:00'
type: issue
status: closed
closed_at: '2023-01-03T23:05:46+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

[Join the Monero Matrix server if you don't already have a Matrix account.](https://forum.monero.space/d/79-how-to-join-the-monero-core-team-matrix-server-web)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20211027T170000&p1=1440)

Main discussion topics:

1. Greetings

2.  Discuss [Jamtis address checksums](https://gist.github.com/tevador/50160d160d24cfc6c52ae02eb3d17024#64-checksum).

3. Improvements to the decoy selection algorithm ( [Decoy Selection Algorithm - Areas to Improve](https://github.com/monero-project/research-lab/issues/86), [Binning PoC](https://github.com/monero-project/research-lab/issues/88), [OSPEAD](https://ccs.getmonero.org/proposals/Rucknium-OSPEAD-Fortifying-Monero-Against-Statistical-Attack.html) ) @j-berman @Rucknium

4. Seraphis. ( [UkoeHB's Seraphis Proof of Concept work](https://ccs.getmonero.org/proposals/seraphis-wallet-poc-2.html), [Seraphis repo](https://github.com/UkoeHB/Seraphis) ).

5. MRL Meta: "Cat herding", i.e. prioritization of research areas and features. Active recruitment of technical talent, MRL structure, funding (@Rucknium & others) [MoneroResearch.info repository of Monero-related research papers](https://moneroresearch.info/), [Reddit discussion](https://www.reddit.com/r/Monero/comments/pkg3d6/the_monero_project_should_actively_recruit/)

6. Any other business

7. Confirm next meeting agenda


Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: UkoeHB

Previous meeting agenda/logs:

#772 

# Discussion History
## UkoeHB | 2022-12-30T15:18:38+00:00
`[12-28-2022 16:59:47] <one-horse-wagon[> Hello.`
`[12-28-2022 17:01:02] <tevador> Hi`
`[12-28-2022 17:01:10] <rbrunner> Hello`
`[12-28-2022 17:01:17] <Rucknium[m]> Meeting time: https://github.com/monero-project/meta/issues/773`
`[12-28-2022 17:01:21] <Rucknium[m]> 1) Greetings`
`[12-28-2022 17:01:22] <isthmus> Hallo`
`[12-28-2022 17:02:07] <one-horse-wagon[> Hello`
`[12-28-2022 17:02:59] <Rucknium[m]> 2) Updates. What is everyone working on?`
`[12-28-2022 17:04:26] <blankpage[m]> Hello`
`[12-28-2022 17:06:16] <tevador> I've been updating the Jamtis specs and finalizing the checksum algorithm. I'm working on new URI schemes for Jamtis (payment URI and wallet export/import URI for the various tiers).`
`[12-28-2022 17:06:44] <Rucknium[m]> Me: Wrote reproducible code for collecting data on p2pool payout outputs: https://github.com/Rucknium/misc-research/tree/main/Monero-p2pool-Output-Stats . My initial calculations were correct. Over the last three months (heights 2721396-2786779), p2pool has found 7% of blocks. 15% of all outputs on the chain during this period were p2pool payout outputs.`
`[12-28-2022 17:08:46] <isthmus> I sent over my first round of OSPEAD review notes to Rucknium. Something like six pages of questions and comments. My impression is very positive! The work is very thorough, the research is well-executed, and I believe the approach proposed will improve the safety of Monero and its users.`
`[12-28-2022 17:08:48] <isthmus> Now poking around at some misc Monero side projects, we’ll see which turn out to be interesting`
`[12-28-2022 17:09:41] <blankpage[m]> 15% seems like a lot of chain bloat `
`[12-28-2022 17:10:31] <blankpage[m]> I suppose this was to be expected with p2pool's tiny payouts`
`[12-28-2022 17:11:02] <rbrunner> Well, at least size-wise the chain does not get bloated because those transactions are still small`
`[12-28-2022 17:11:14] <rbrunner> Have a look at a sample tx that was mentioned last week: https://xmrchain.net/tx/f6c1cfcce9e531d3147f249638233e40a71153f47cac253c45d3f5d1fd06d7dc`
`[12-28-2022 17:11:19] <tevador> coinbase outputs are tiny (under 40 bytes) compared to normal outputs`
`[12-28-2022 17:11:25] <Rucknium[m]> Thanks, isthmus! I am reading through the comments and questions and I will respond soon. Next steps on OSPEAD are: ArticMine sends me his review, I do any necessary modifications to the OSPEAD proposal, then I do initial estimations, then share initial estimates with the committee, then revise.`
`[12-28-2022 17:12:19] <blankpage[m]> Oh I see. So the problem is mostly "what are the impacts of 15% of decoys being from p2pool" rather than chain size`
`[12-28-2022 17:12:40] <rbrunner> That's how I understood it`
`[12-28-2022 17:13:59] <Rucknium[m]> Coinbase tx outputs may be small, but those tiny p2pool payouts have to be consolidated, which implies a full RingCT for each one.`
`[12-28-2022 17:14:04] <rbrunner> And of course how things would look should p2pool get wildly successful :)`
`[12-28-2022 17:15:09] <tevador> There have been suggestions to remove ring signatures from transactions that just consolidate coinbase outputs.`
`[12-28-2022 17:15:13] <Rucknium[m]> IMHO, the main research question is how to handle decoy selection when there are all these p2pool outputs are now being selected for rings.`
`[12-28-2022 17:17:00] <blankpage[m]> Seems to also imply we would hit large majority of outputs (in a given window) being p2pool at p2pool adoption hit 50% (which is itself very desirable)`
`[12-28-2022 17:17:37] <Rucknium[m]> Just a reminder: changing consensus rules on how to construct txs with coinbase inputs would require a hard fork. Changes to the standard decoy selection algorithm to avoid coinbase outputs would not require a hard fork.`
`[12-28-2022 17:20:41] <tevador> After the Seraphis update, coinbase outputs will become significantly larger. Something too keep in mind.`
`[12-28-2022 17:21:11] <rbrunner> What gets added?`
`[12-28-2022 17:21:31] <rbrunner> Just the larger addresses?`
`[12-28-2022 17:21:38] <tevador> One DH pubkey and the encrypted address tag. Total of 50 bytes per output.`
`[12-28-2022 17:23:31] <atomfried[m]> i just wanted to inform you that the firo research team is currently looking into [curve trees](https://eprint.iacr.org/2022/756.pdf)`
`[12-28-2022 17:24:02] <blankpage[m]> I suppose there are two fundamental directions to take:`
`[12-28-2022 17:24:03] <blankpage[m]> 1) Not including coinbase in rings`
`[12-28-2022 17:24:03] <blankpage[m]> 2) changing p2pool in some way so that it does not produce such an overwhelming number of outputs`
`[12-28-2022 17:24:03] <blankpage[m]> The tradeoffs are not clear to me, but it is an interesting problem`
`[12-28-2022 17:24:29] <Rucknium[m]> I should write some calculations on the number of bytes that p2pool adds to the chain as a percentage of total chain bytes.`
`[12-28-2022 17:25:56] <rbrunner> I followed some discussions that included sech1, the author of p2pool, somewhere recently, and got the impression that 2) is quite a tough nut to crack`
`[12-28-2022 17:28:36] <tevador> The p2pool payout consolidation transactions offer practically zero privacy because the ring signatures all contain one member that is a payout to one specific address from the p2pool sidechain.`
`[12-28-2022 17:29:30] <tevador> Those outputs can be marked as spent in practice, so using them as decoys is pointless.`
`[12-28-2022 17:29:30] <Rucknium[m]> I would lean toward (1), but it requires more research. In the abstract, it would reduce the privacy of p2pool miners. Given the very distinctive consolidations of p2pool outputs, I'm not sure it's much of a material reduction in privacy. And mining is pretty private, anyway. The coins have no prior history.`
`[12-28-2022 17:29:45] <isthmus> I'm still working on wrapping my head around the dynamics, variance tradeoffs, etc. Definitely does seem like a tough nut`
`[12-28-2022 17:29:45] <isthmus> Mooo said something a few days ago that I've been wondering about; would it make sense to have different p2p chains for different scale entities (small one for low hashrate high payout rate, and another one for big mining operations with more hashrate and a longer timeframe (not going to drop off the network after 4 hours of mining)`
`[12-28-2022 17:30:33] <Rucknium[m]> isthmus: There is already the main p2pool side chain and p2pool "mini" for low hashrate miners`
`[12-28-2022 17:30:43] <isthmus> 👍`
`[12-28-2022 17:32:16] <rbrunner> Yeah, and making even more seems to be quite easy, basically write a config file and then go look for miners.`
`[12-28-2022 17:32:34] <sech1> each p2pool output has a wallet address attached to it in sidechain data, so using them as decoys is pointless. They will all either use the same address in all inputs, or different random addresses - both cases can be used to eliminate all p2pool decoys`
`[12-28-2022 17:33:10] <sech1> miner consolidation -> all inputs use the same address in decoys, random transaction -> random non-matching addresses`
`[12-28-2022 17:33:33] <sech1> so it makes sense to treat coinbase output differently in all transactions`
`[12-28-2022 17:33:54] <blankpage[m]> It looks like the idea of excluding coinbase tx from rings has been raised before in 2019:`
`[12-28-2022 17:33:54] <blankpage[m]> https://medium.com/@JEhrenhofer/lets-stop-using-coinbase-outputs-da672ca75d43`
`[12-28-2022 17:34:00] <sech1> I often see some transactions not using coinbase decoys at all. It's some modified decoy selection algorithm.`
`[12-28-2022 17:35:05] <isthmus> Woah, really?`
`[12-28-2022 17:35:09] <isthmus> cc: neptune`
`[12-28-2022 17:35:28] <isthmus> That could be interesting to look into`
`[12-28-2022 17:36:00] <sech1> yes, these transactions also avoid selecting old (> 1 year) decoys`
`[12-28-2022 17:36:10] <Rucknium[m]> For a low number of inputs, there is a random chance that no coinbase outputs get included in a tx, right?`
`[12-28-2022 17:36:16] <sech1> someone (probably an exchange or a swap service) is running modified wallet`
`[12-28-2022 17:36:42] <sech1> no, I've seen transactions with dozens of inputs and no coinbase decoys`
`[12-28-2022 17:36:55] <blankpage[m]> Also Justin gave a presentation on the idea:`
`[12-28-2022 17:36:55] <blankpage[m]> https://www.youtube.com/watch?v=Z0P7rWsSGLA`
`[12-28-2022 17:36:55] <blankpage[m]> I guess this was all before p2pool though`
`[12-28-2022 17:37:48] <Rucknium[m]> There is this paper (I haven't read it) Wijaya, D. A., Liu, J. K., Steinfeld, R., & Liu, D. 2021, "Transparency or anonymity leak: Monero mining pools data publication." https://moneroresearch.info/index.php?action=resource_RESOURCEVIEW_CORE&id=37`
`[12-28-2022 17:38:15] <isthmus> @sech1 do you happen to have any of those txns bookmarked? `
`[12-28-2022 17:39:51] <sech1> https://xmrchain.net/tx/2e85d9b813be04abae6e10094e1bef79c1dd43154c2af97ac21bf0fb79f9d0fc`
`[12-28-2022 17:40:25] <sech1> it's even bigger than 100 KB, wallet2 can't create it`
`[12-28-2022 17:40:46] <isthmus> 👀 tyty`
`[12-28-2022 17:40:49] <sech1> https://xmrchain.net/tx/8adc65b0e6f422fe30ff90edec5836cb89adc17387eada48bbcb55bbcc284f44`
`[12-28-2022 17:41:34] <Rucknium[m]> sech1: Wow. Thanks!`
`[12-28-2022 17:43:07] <Rucknium[m]> The MAGIC Monero Fund committee has three seats open for elections. Voter and committee member (self-)nominations close on December 31. Only two people have nominated themselves for committee seats so far. The fund now has about 50,000 USD equivalent, split roughly evenly between XMR and USD: https://github.com/MAGICGrants/Monero-Fund-Elections`
`[12-28-2022 17:43:47] <Rucknium[m]> koe submitted a new Seraphis CCS proposal: https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/369`
`[12-28-2022 17:47:22] <Rucknium[m]> It is great that he is planning to continue Seraphis work. My suggestion would be do the Seraphis paper update first so that the necessary math work can continue on that. We had discussed asking CypherStack to create a road map of what math work needs to be done to guarantee the safety of Seraphis on mainnet. IMHO, we should wait to ask them to create the road map until after koe is done with the paper update.`
`[12-28-2022 17:53:06] <Rucknium[m]> Any more comments? If not, we can end the meeting now.`

# Action History
- Created by: Rucknium | 2022-12-24T01:55:48+00:00
- Closed at: 2023-01-03T23:05:46+00:00
