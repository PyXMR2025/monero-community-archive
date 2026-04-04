---
title: Monero Research Lab Meeting - Wed 25 January 2023, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/786
author: Rucknium
assignees: []
labels: []
created_at: '2023-01-24T16:08:18+00:00'
updated_at: '2023-02-12T19:31:24+00:00'
type: issue
status: closed
closed_at: '2023-02-12T19:31:24+00:00'
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

#782

# Discussion History
## UkoeHB | 2023-01-25T17:38:55+00:00
`[01-25-2023 17:00:08] <UkoeHB> meeting time https://github.com/monero-project/meta/issues/786`
`[01-25-2023 17:00:08] <UkoeHB> 1. greetings`
`[01-25-2023 17:00:08] <UkoeHB> hello`
`[01-25-2023 17:00:24] <ArticMine[m]> Hi`
`[01-25-2023 17:00:28] <rbrunner> hello`
`[01-25-2023 17:00:39] <dangerousfreedom> Hello`
`[01-25-2023 17:00:40] <vtnerd> hi`
`[01-25-2023 17:00:51] <shalit[m]> hello`
`[01-25-2023 17:01:27] <Rucknium[m]> Hi`
`[01-25-2023 17:03:12] <UkoeHB> 2. updates, what's everyone working on?`
`[01-25-2023 17:04:29] <Rucknium[m]> Released my analysis of mining pools delaying tx confirmations: https://www.reddit.com/r/Monero/comments/10gapp9/centralized_mining_pools_are_delaying_monero/ . Already HashVault, MoneroOcean, and SupportXMR have started updating their block templates more frequently, according to the pool operators and sech1.`
`[01-25-2023 17:04:58] <shalit[m]> UkoeHB: I'm currently looking for a task`
`[01-25-2023 17:05:33] <Rucknium[m]> With P2Pool, which already had a frequent update policy, about 60% of Monero's blocks are now being mined with frequent template updates, decreasing the time to first tx confirmation.`
`[01-25-2023 17:06:03] <blankpage[m]> Hello`
`[01-25-2023 17:06:24] <Rucknium[m]> I'm working on understanding the computational complexity issues of OSPEAD.`
`[01-25-2023 17:06:26] <rbrunner> shalit[m]: Would you have time for a chat with me on Matrix in about 2 hours time? We could look at it`
`[01-25-2023 17:06:45] <blankpage[m]> Fantastic news on the template updates. Very strange that this hadn't been noticed earlier. Any idea how long this has been an issue?`
`[01-25-2023 17:06:56] <UkoeHB> me: finished my cleanup/review pass on the seraphis library (took almost 2 months wow - over 50k lines is a lot)`
`[01-25-2023 17:07:22] <UkoeHB> right now doing some finishing touches related to practical enote store handling`
`[01-25-2023 17:07:55] <shalit[m]> rbrunner: yeap, sounds good, so in 19:00 UTC?`
`[01-25-2023 17:08:08] <Rucknium[m]> blankpage: I don't know how long it's been an issue. Possibly since the beginning of Monero.`
`[01-25-2023 17:08:45] <dangerousfreedom> I will probably finish the work on the knowledge proofs this week (at least a first functional version with basically all the functionalities that we have today and a bit more) but it will probably change a bit when we go to testnet as the integration with the wallet and new bugs may appear. I would like to thank Koe also for always taking the time for reviewing it thoroughly.`
`[01-25-2023 17:09:03] <ArticMine[m]> I have been working on my OSPEAD review. It is now at the point of completing the verite up. `
`[01-25-2023 17:09:03] <ArticMine[m]> I have provided Rucknium with timelines and preliminary results. `
`[01-25-2023 17:09:59] <vtnerd> Im still working on bp++ implementation, mainly comparing the paper and the c code (not haskell code), hopefully something more tangible next week (this is definitely dragging too long, sorry)`
`[01-25-2023 17:10:31] <Rucknium[m]> Someone on Reddit suggested checking these repos and creating GitHub issues to change the default block template update time: https://github.com/oliverw/miningcore , https://github.com/zone117x/node-open-mining-portal`
`[01-25-2023 17:10:40] <UkoeHB> thanks vtnerd`
`[01-25-2023 17:10:54] <Rucknium[m]> Thank you, ArticMine !`
`[01-25-2023 17:12:46] <UkoeHB> 3. discussion`
`[01-25-2023 17:16:06] <UkoeHB> any topics anyone had in mind? on my end, these PRs could use more review https://github.com/monero-project/monero/pulls/UkoeHB`
`[01-25-2023 17:18:24] <Rucknium[m]> In "Avoid selecting coinbase outputs as decoys" https://github.com/monero-project/research-lab/issues/109 I say that this would be a wallet-level change. Now I am not sure if that's totally correct. Would monerod need to change what it sends to wallet software, i.e. exclude coinbase outputs from get_outs RPC call?`
`[01-25-2023 17:20:24] <UkoeHB> I'm not familiar with exactly how wallet2 does it.. but probably yes`
`[01-25-2023 17:21:32] <ArticMine[m]> This would require a separate call for coinbase outputs `
`[01-25-2023 17:21:49] <rbrunner> Same here. But as it's only one software package, I don't think it would matter too much exactly where one changes code`
`[01-25-2023 17:21:58] <Rucknium[m]> Probably a good question for jberman , too`
`[01-25-2023 17:23:50] <Rucknium[m]> It could matter because a old-version wallet software could connect with a new-version remote node (or vice versa) and then...? And if I'm an old version wallet that wants to spend my coinbase output (from P2Pool, let's say), and I don't see my owned output in the reply from monerod remote node, what would I do?`
`[01-25-2023 17:24:24] <Rucknium[m]> This is if the change would happen outside of a hard fork boundary.`
`[01-25-2023 17:26:05] <rbrunner> The RPC interface is somewhat flexible regarding compatibility, I think you could add something to the RPC answer of `get_outs` that tells the wallet what to expect`
`[01-25-2023 17:26:24] <rbrunner> and then react accordingly`
`[01-25-2023 17:27:05] <rbrunner> (the new wallet would find out whether it talks to a new or an old daemon)`
`[01-25-2023 17:30:25] <Rucknium[m]> Ok. I'm not sure of the next steps with this idea. I guess we can leave it open for a while longer and see if any arguments to the contrary surface. I've described the privacy risks of the status quo.`
`[01-25-2023 17:32:18] <ArticMine[m]> It would have to be implemented only at the wallet level unless it is done with a hard fork`
`[01-25-2023 17:33:13] <UkoeHB> it increases the complexity of making txs which basically increases dependency on the core wallet implementation`
`[01-25-2023 17:34:31] <UkoeHB> not that there are many txs being made with anything else, but it's still a cot`
`[01-25-2023 17:34:32] <UkoeHB> cost`
`[01-25-2023 17:36:22] <UkoeHB> anything else to bring up? otherwise we can end the meeting early`
`[01-25-2023 17:38:10] <UkoeHB> ok I'll call it here, thanks for attending everyone`

# Action History
- Created by: Rucknium | 2023-01-24T16:08:18+00:00
- Closed at: 2023-02-12T19:31:24+00:00
