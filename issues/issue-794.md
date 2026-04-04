---
title: Monero Research Lab Meeting - Wed 08 February 2023, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/794
author: Rucknium
assignees: []
labels: []
created_at: '2023-02-08T15:16:22+00:00'
updated_at: '2023-02-12T19:33:44+00:00'
type: issue
status: closed
closed_at: '2023-02-12T19:33:44+00:00'
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

#790 

# Discussion History
## UkoeHB | 2023-02-08T17:30:52+00:00
`[02-08-2023 17:00:25] <UkoeHB> meeting time https://github.com/monero-project/meta/issues/794`
`[02-08-2023 17:00:25] <UkoeHB> 1. greetings`
`[02-08-2023 17:00:25] <UkoeHB> hello`
`[02-08-2023 17:00:59] <Rucknium[m]> Hi`
`[02-08-2023 17:00:59] <rbrunner> Hello`
`[02-08-2023 17:01:02] <one-horse-wagon[> Hello.`
`[02-08-2023 17:02:08] <ofrnxmr[m]> Hi`
`[02-08-2023 17:02:49] <ArticMine[m]> Hi`
`[02-08-2023 17:03:47] <UkoeHB> 2. updates, what's everyone working on?`
`[02-08-2023 17:05:54] <Rucknium[m]> Writing code for OSPEAD. Testing it. `
`[02-08-2023 17:06:40] <ofrnxmr[m]> RavFX has written a guide for using ssd as cache to speedup sync times to HDD`
`[02-08-2023 17:06:40] <ofrnxmr[m]> http://waw7epjul5xeacm4niblpgihdtg3atxyqekrlgz5spynqosdzftnbfad.onion/index.php?article=hdd_sync`
`[02-08-2023 17:06:40] <ofrnxmr[m]> Nanopool had updated their block templates Today, and xmrig pushed an update a few days ago that allows setting the refresh time.`
`[02-08-2023 17:06:40] <ofrnxmr[m]> I believe the majorty of xmr hashrate is now mining efficiently, keeping the tx pool clear `
`[02-08-2023 17:08:34] <one-horse-wagon[> Rucknium[m]: What language did you end up writing it in?`
`[02-08-2023 17:08:49] <UkoeHB> me: I have been designing/implementing a tasking system that could be used in the seraphis wallet engine project (goals being: coherent data/control flow, maximizing responsiveness, maximizing CPU utilization).`
`[02-08-2023 17:08:58] <Rucknium[m]> Thanks to everyone for asking the pools to update their block templates more frequently. In a few weeks I will probably re-run this analysis to measure the speed-up in first tx confirmation: https://rucknium.me/posts/monero-pool-transaction-delay/`
`[02-08-2023 17:10:08] <Rucknium[m]> one-horse-wagon: I'm writing it in R. isthmus is considering helping me write the slow parts in C++, using the R code as a test vector.`
`[02-08-2023 17:11:31] <Rucknium[m]> R has a very good way to wrap C++ called Rcpp`
`[02-08-2023 17:14:07] <UkoeHB> 3. discussion`
`[02-08-2023 17:14:19] <UkoeHB> it looks like there has been some debate on this: https://github.com/monero-project/monero/issues/6668 anyone care to summarize?`
`[02-08-2023 17:15:10] <rbrunner> A real evergreen, that topic`
`[02-08-2023 17:15:26] <rbrunner> Didn't know it flared up again ...`
`[02-08-2023 17:19:33] <rbrunner> Have to read first, in any case`
`[02-08-2023 17:21:46] <Rucknium[m]> I talked with kayabanerve about how to prevent txs from proving that they are the real spend of the output. You can maybe create transferable NFTs if you can prove you are the real spend in the next tx_extra. According to him, you can prove it in 64 bytes, so tx_extra would have to be very small to prevent transferable NFTs I think. And you would lose the ability to have refund addresses in tx_extra if you wanted that.`
`[02-08-2023 17:23:07] <ArticMine[m]> I have to review the tx extra issue `
`[02-08-2023 17:23:17] <ArticMine[m]> ... before l can make any comments `
`[02-08-2023 17:25:46] <UkoeHB> ok well I think we can wrap it up then, I don't have anything more to say today`
`[02-08-2023 17:26:06] <UkoeHB> unless there is something else to discuss ?`
`[02-08-2023 17:27:06] <Rucknium[m]> Unless there are objections, I will explicitly put the tx_extra issue on the agenda for the next MRL meeting.`
`[02-08-2023 17:27:13] <UkoeHB> ok`
`[02-08-2023 17:27:29] <rbrunner> So we have homework this time, reading up the discussion :)`
`[02-08-2023 17:30:09] <UkoeHB> that's all for today, thanks for attending everyone`

# Action History
- Created by: Rucknium | 2023-02-08T15:16:22+00:00
- Closed at: 2023-02-12T19:33:44+00:00
