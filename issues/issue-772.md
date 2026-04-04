---
title: Monero Research Lab Meeting - Wed 21 December 2022, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/772
author: Rucknium
assignees: []
labels: []
created_at: '2022-12-20T16:41:52+00:00'
updated_at: '2023-01-05T14:34:55+00:00'
type: issue
status: closed
closed_at: '2022-12-24T01:55:59+00:00'
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

#768 

# Discussion History
## UkoeHB | 2022-12-21T17:51:53+00:00
`[12-21-2022 17:01:30] <UkoeHB> meeting time`
`[12-21-2022 17:01:35] <UkoeHB> https://github.com/monero-project/meta/issues/772`
`[12-21-2022 17:01:41] <UkoeHB> 1. greetings`
`[12-21-2022 17:01:42] <UkoeHB> hello`
`[12-21-2022 17:01:46] <Rucknium[m]> Hi`
`[12-21-2022 17:01:55] <rbrunner> Hello`
`[12-21-2022 17:02:03] <ofrnxmr[m]> Hello`
`[12-21-2022 17:02:20] <vtnerd> hi`
`[12-21-2022 17:04:25] <UkoeHB> 2. updates, what's everyone working on?`
`[12-21-2022 17:05:04] <Rucknium[m]> Collecting mempool and found block broadcast time for analysis of mining pools' block template update policies. Some analysis of p2pool payout outputs.`
`[12-21-2022 17:06:06] <vtnerd> no real tangible updates since last week unfortunately - working on (other stuff) and bp++`
`[12-21-2022 17:07:02] <tevador> Hi. Jamtis checksum + updating the specs.`
`[12-21-2022 17:08:07] <isthmus> I read the OSPEAD doc again and started drafting up thoughts / questions. Converting from my own shorthand into comments shortly.`
`[12-21-2022 17:08:33] <Rucknium[m]> Thanks, isthmus.`
`[12-21-2022 17:08:59] <jberman[m]> Submitted a PR to rbrunner 's PR to optimize pool processing (https://github.com/rbrunner7/monero/pull/4) + been going through balance recovery in the Seraphis lib`
`[12-21-2022 17:09:24] <UkoeHB> me: continued cleanup of the seraphis library. I decided to move all member functions out of C-style structs for a more clean/consistent environment (and to discourage adding member functions in the future).`
`[12-21-2022 17:09:50] <rbrunner> Yeah, things get so complex that now PR's need PR's :) Thanks jberman[m]`
`[12-21-2022 17:12:05] <UkoeHB> 3. discussion`
`[12-21-2022 17:13:35] <UkoeHB> This seraphis design overview basically got no attention - everyone should read it though because this is what monero will get if nothing changes. https://gist.github.com/UkoeHB/f508a6ad973fbf85195403057e87449e`
`[12-21-2022 17:14:29] <rbrunner> Not sure there was a lack of attention, I just think that it's not that controversial now`
`[12-21-2022 17:14:44] <Rucknium[m]> I read it and gave comments/questions :P`
`[12-21-2022 17:15:19] <rbrunner> I read it and was impressed how much will really change, it only becomes clear if you heap it all in one place.`
`[12-21-2022 17:15:31] <rbrunner> And not merely change of course, but improve`
`[12-21-2022 17:16:26] <rbrunner> By the way, is there already support in the library for transaction chaining? I guess so, given how modular it is`
`[12-21-2022 17:17:08] <UkoeHB> Rucknium[m]: yes I'm grateful :)`
`[12-21-2022 17:17:28] <Rucknium[m]> Another question in my mind is how much of the structure would have to change if many years from now we eliminate ring signatures and have an "accumulator model". In other words, how future-proof is the modular Seraphis structure?`
`[12-21-2022 17:17:39] <UkoeHB> rbrunner: more or less, I didn't put a lot of effort into the mock offchain scanning stuff so it may or may not work`
`[12-21-2022 17:17:49] <UkoeHB> the offchain mockups may or may not work *`
`[12-21-2022 17:18:37] <rbrunner> Ok, it will be hard work to support it "higher up" in wallets anyway, probably not the first thing to implement`
`[12-21-2022 17:18:48] <UkoeHB> Rucknium[m]: it depends on the accumulator model. If they are plug-and-play, doing the same thing as grootle proofs, then it should be easy enough`
`[12-21-2022 17:20:00] <isthmus> Amazing work @UkoeHB `
`[12-21-2022 17:20:00] <isthmus> /me is very happy about the transaction uniformity improvements`
`[12-21-2022 17:20:18] <UkoeHB> thanks isthmus `
`[12-21-2022 17:22:25] <UkoeHB> hmm are there any other topics to discuss today?`
`[12-21-2022 17:23:47] <UkoeHB> In the seraphis migration workgroup meeting on monday it was basically decided that no additional changes to the jamtis spec are needed to support accounts. Does anyone feel like weighing in today?`
`[12-21-2022 17:24:26] <vtnerd> its still handled by the blowfish technique .. ?`
`[12-21-2022 17:24:57] <tevador> twofish`
`[12-21-2022 17:25:27] <vtnerd> I guess I could just read, but my last reading of the spec looked like it was a bit rough because it involved a block cipher in the design too, but it solved lots of existing problems`
`[12-21-2022 17:25:44] <tevador> yes, it uses a block cipher`
`[12-21-2022 17:26:09] <vtnerd> ah right the upgrade sorry, but I think it was probably worth the change`
`[12-21-2022 17:26:11] <tevador> I'm in the process of updating the specs to match UkoeHB's library`
`[12-21-2022 17:26:14] <vtnerd> it makes accounts more seamless`
`[12-21-2022 17:26:38] <UkoeHB> vtnerd: the 'mac' thing was renamed to 'address tag hint' and uses blake2b now`
`[12-21-2022 17:27:10] <UkoeHB> the address index is still ciphered with twofish`
`[12-21-2022 17:27:19] <vtnerd> ok will scan the comment and proposed changes again`
`[12-21-2022 17:29:05] <Rucknium[m]> Some preliminary numbers on p2pool payout outputs: They account for about 15% of all outputs on the chain if my calculations are correct. Implications: larger storage needs (but coinbase outputs are lighter than most tx outputs); and some potential privacy issues with decoy selection since each ring will have two p2pool outputs on average.`
`[12-21-2022 17:29:32] <Rucknium[m]> The Monero Meet discussion encouraged me to run the numbers`
`[12-21-2022 17:30:06] <Rucknium[m]> This is with p2pool finding about 7% of all blocks`
`[12-21-2022 17:30:10] <rbrunner> That's a bit surprising, given that not yet too many people mine there`
`[12-21-2022 17:30:18] <tevador> on the other hand, it makes all transfers plausibly use freshly minted coins`
`[12-21-2022 17:30:59] <Rucknium[m]> It's more "possible" than "plausible" IMHO`
`[12-21-2022 17:31:40] <Rucknium[m]> p2pool payout consolidations would probably be distinct on the chain.`
`[12-21-2022 17:31:46] <tevador> yes, possibly*`
`[12-21-2022 17:32:52] <Rucknium[m]> And then the addresses being mined to are transparent, which can lead to deeper analysis of what txs may be p2pool payout consolidations`
`[12-21-2022 17:33:30] <rbrunner> What do you mean with "consolidation"? E.g. payout only after I participated on x blocks, x>1?`
`[12-21-2022 17:33:50] <UkoeHB> wow 15%`
`[12-21-2022 17:33:53] <Rucknium[m]> The average number of p2pool payout outputs per found block is about 150. the mini chain tends to have higher numbers of outputs.`
`[12-21-2022 17:35:22] <Rucknium[m]> Consolidation: If I am a p2pool miner, I would want to consolidate the very small payouts. I doubt that an individual p2pool output would be enough to pay for a good or service or be something to send to an exchange, etc.`
`[12-21-2022 17:36:20] <isthmus> High frequency of miner outputs in rings has benefits`
`[12-21-2022 17:36:22] <isthmus> https://usercontent.irccloud-cdn.com/file/lVoXxbJv/image.png`
`[12-21-2022 17:36:45] <isthmus> Nice if most or all rings have Y_{hops}(t) = 0 `
`[12-21-2022 17:37:13] <isthmus> Sorry this is a very old doc`
`[12-21-2022 17:37:31] <Rucknium[m]> This p2pool coinbase has small amounts per output, for example: https://xmrchain.net/tx/f6c1cfcce9e531d3147f249638233e40a71153f47cac253c45d3f5d1fd06d7dc`
`[12-21-2022 17:37:31] <UkoeHB> only nice if the hops can't be ignored due to identifiable consolidations`
`[12-21-2022 17:38:25] <isthmus> https://usercontent.irccloud-cdn.com/file/fujH5bfH/image.png`
`[12-21-2022 17:40:06] <rbrunner> At least those transactions are still small`
`[12-21-2022 17:40:39] <rbrunner> Almost Bitcoin like :)`
`[12-21-2022 17:40:45] <Rucknium[m]> Also, if I'm an adversary receiving a user's payment (or I have cleartext view into that payment), the amount could easily exceed the possible amount of the sum of the cleartext p2pool payouts in the corresponding history.`
`[12-21-2022 17:41:00] <isthmus> 🤔`
`[12-21-2022 17:43:10] <Rucknium[m]> Let's analyze single-hop: If sum(max(p2pool outputs in each ring)) > value_of_surveilled_tx_output, then you can rule out the p2pool outputs, (used as inputs) as a whole.`
`[12-21-2022 17:43:15] <Rucknium[m]> Or should I say enotes`
`[12-21-2022 17:44:43] <Rucknium[m]> If the target tx has a single input, then in this scenario the p2pool ring members could be ruled out completely.`
`[12-21-2022 17:49:27] <isthmus> Gotta run, catch y'all later`
`[12-21-2022 17:51:10] <UkoeHB> seems like we are at the end of the meeting, so let's wrap it up here; thanks for attending everyone`

# Action History
- Created by: Rucknium | 2022-12-20T16:41:52+00:00
- Closed at: 2022-12-24T01:55:59+00:00
