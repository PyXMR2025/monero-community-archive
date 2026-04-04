---
title: Monero Research Lab Meeting - Wed 17 August 2022
source_url: https://github.com/monero-project/meta/issues/726
author: Rucknium
assignees: []
labels: []
created_at: '2022-08-16T15:25:36+00:00'
updated_at: '2022-08-23T19:43:58+00:00'
type: issue
status: closed
closed_at: '2022-08-23T19:43:58+00:00'
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

#725 

# Discussion History
## UkoeHB | 2022-08-17T18:03:17+00:00
`[08-17-2022 17:00:04] <UkoeHB> meeting time https://github.com/monero-project/meta/issues/726`
`[08-17-2022 17:00:04] <UkoeHB> 1. greetings`
`[08-17-2022 17:00:04] <UkoeHB> hello`
`[08-17-2022 17:00:55] <rbrunner> hi`
`[08-17-2022 17:01:02] <one-horse-wagon[> Hello to everyone.`
`[08-17-2022 17:02:43] <Rucknium[m]> Hi`
`[08-17-2022 17:02:55] <tevador> Hi`
`[08-17-2022 17:04:38] <UkoeHB> 2. updates, what's everyone working on? looks like low turnout so might be a short meeting`
`[08-17-2022 17:05:57] <Rucknium[m]> me: OSPEAD work`
`[08-17-2022 17:06:42] <Rucknium[m]> In my CCS proposal I said "The upcoming hard fork, which does not yet have a fixed date, will include an increase in the ring size. The discontinuity that the hard fork creates can be leveraged to better understand how ring signatures work in pratcice [sic] on the Monero blockchain. Therefore, some of the research work will occur after the hard fork."`
`[08-17-2022 17:06:49] <UkoeHB> me: finished unit testing legacy balance recovery with my seraphis lib, still on vacation until sept so working slowly, will probably make a new CCS next week`
`[08-17-2022 17:07:49] <Rucknium[m]> Judging by the crash in on-chain transaction volume and the number of wallets that were not ready for the hard fork, we can safely say that the expected discontinuity has been achieved! 🎉🎉🎉🎉🎉`
`[08-17-2022 17:09:10] <UkoeHB> I discovered that legacy balance recovery is 4-10x more work than seraphis balance recovery due to A) the key image import workflow for view-only wallets, B) the possibility of duplicate onetime addresses that needs to be handled.`
`[08-17-2022 17:10:06] <tevador> I'm waiting for feedback on some Jamtis changes. In the meantime, I'm planning to implement a deterministic binning strategy as an alternative to UkoeHB's current code.`
`[08-17-2022 17:10:19] <tevador> Some recent discussion happened here: https://github.com/monero-project/research-lab/issues/84 also tangentially related to time locks.`
`[08-17-2022 17:10:59] <jberman[m]> been working on hard fork monitoring/cold wallet stuff. I think the crash in volume is primarily from the light wallet ecosystem (MyMonero, Exodus, Guarda, Edge, not sure of others), though it seems some people are still having sporadic issues in other wallets`
`[08-17-2022 17:11:31] <UkoeHB> tevador: yeah I'll get there... tbh pretty worn out on making changes after a year of continuous development`
`[08-17-2022 17:12:19] <Rucknium[m]> If anyone wants the empirical probability mass functions of the BTC&BCH&LTC&DOGE spent output age for each week since 2015, it is here: https://rucknium.me/data/weekly-spent-output-age-empirical-pmfs.tar.xz`
`[08-17-2022 17:12:57] <tevador> ^ I'm planning to use this.`
`[08-17-2022 17:13:33] <Rucknium[m]> tevador: Could you explain more?`
`[08-17-2022 17:16:28] <tevador> From the datasets you collected, predicting the real spend-age distribution seems impossible. So I want to try a different empirical strategy.`
`[08-17-2022 17:16:39] <tevador> Not fully fleshed out yet.`
`[08-17-2022 17:16:59] <Rucknium[m]> Ok sounds good.`
`[08-17-2022 17:18:29] <one-horse-wagon[> I thought the hard fork went very well.  The issues seemed to be minor and came from those that did not update the software beforehand.  `
`[08-17-2022 17:20:13] <Rucknium[m]> Do we want to discuss possible research priorities for the next hard fork, whenever it is? In other words, research on things that could only be realistically implemented in a hard fork?`
`[08-17-2022 17:22:01] <UkoeHB> sure we can move on`
`[08-17-2022 17:22:03] <UkoeHB> 3. discussion`
`[08-17-2022 17:23:53] <UkoeHB> idk what priorities there are for next hardfork, maybe improving the defaul decoy selection algorithm?`
`[08-17-2022 17:25:28] <rbrunner> Does that need a hardfork however?`
`[08-17-2022 17:25:29] <Rucknium[m]> Priorities could be: (1) Seraphis, obviously (2) nlocktime removal (or not) (3) 10 block lock removal (4) making p2pool much more attractive than centralized pool mining  (5) Fee discretization and its implications (6) Possible enforcement of a decoy selection algorithm (7) tx_extra issues`
`[08-17-2022 17:25:43] <UkoeHB> perhaps BP++ will gain enough steam to be implemented`
`[08-17-2022 17:26:05] <Rucknium[m]> No, decoy selection does not need a hard fork. It is "best" to be implemented in a hard fork, but not necessary`
`[08-17-2022 17:26:25] <Rucknium[m]> jberman updated the decoy selection algorithm twice last year without a hard fork`
`[08-17-2022 17:27:04] <rbrunner> Interesting, wasn't even aware`
`[08-17-2022 17:27:26] <Rucknium[m]> "Best" as in it is 25% better to implement a new DSA at a hard fork ;)`
`[08-17-2022 17:27:28] <UkoeHB> a large-scale overhaul should probably coincide with a hard fork for better adoption (which has privacy impacts)`
`[08-17-2022 17:28:04] <Rucknium[m]> But much better to implement one ASAP as soon as we have a well-supported improved one.`
`[08-17-2022 17:29:50] <Rucknium[m]> I think the privacy impacts of a poor DSA occur as we speak. Yes, there will be some issues with transaction non-uniformity as people update their wallet software, but that was also the case for jberman's fixes last year.`
`[08-17-2022 17:30:59] <tevador> btw, the removal of the current lock time field would also simplify decoy selection`
`[08-17-2022 17:32:59] <UkoeHB> tevador: really? you still need to keep track of historical locked outputs`
`[08-17-2022 17:33:14] <UkoeHB> it only has an impact for seraphis where we get a clean slate`
`[08-17-2022 17:36:04] <one-horse-wagon[> How much of a demand is there to get rid of the 10 block lockout?`
`[08-17-2022 17:37:39] <Rucknium[m]> Pretty high demand. Haveno wants it gone or reduced. So does LocalMonero. Users also probably want it gone`
`[08-17-2022 17:38:41] <Rucknium[m]> I would assume it would simplify things for Serai. kayabanerve , is that right?`
`[08-17-2022 17:38:46] <ErCiccione> yeah it's probably the biggest hit for Monero's UX`
`[08-17-2022 17:42:00] <ErCiccione> as far as i understood we also never got close to the current limit of 10 and the reasoning behind choosing exactly 10 is unclear. At least to me`
`[08-17-2022 17:42:29] <ErCiccione> good to know an hard fork is not needed btw`
`[08-17-2022 17:43:28] <Rucknium[m]> A hard fork is needed to change the 10 block lock AFAIK. A HF is not needed for decoy selection changes.`
`[08-17-2022 17:44:02] <UkoeHB> Historically all known reorgs have been 2 or 3 blocks deep. Making the lock 10 blocks means there is a good safety factor in case of network instability that enables deeper reorgs.`
`[08-17-2022 17:46:51] <jberman[m]> Fwiw the changes I made to the algo wouldn’t result in definitively identifiable pools of decoy selection algos, except for the one where if the change wasn’t made, 99% of rings would be compromised (the integer truncation one)`
`[08-17-2022 17:47:14] <jberman[m]> I think a change to the algo that would result in identifiable pools without a HF needs a very high bar to pass`
`[08-17-2022 17:47:47] <rbrunner> would *not* result I guess?`
`[08-17-2022 17:48:09] <Rucknium[m]> We need to define "identifiable" precisely at some point`
`[08-17-2022 17:48:14] <Rucknium[m]> In terms of probabilities`
`[08-17-2022 17:48:39] <jberman[m]> Well both need a very high bar to pass. But I did mean what was written`
`[08-17-2022 17:48:59] <rbrunner> Ah, yes, now I understand`
`[08-17-2022 17:49:14] <rbrunner> We should not do something like that lightly`
`[08-17-2022 17:49:28] <jberman[m]> Also sorry to derail, but I think the most critical next significant step we need to take post hard fork is getting security proofs for multisig/a more comprehensive audit completed with the aim moving it out of experimental. I think it’s worth reaching out to veorq for that`
`[08-17-2022 17:51:11] <UkoeHB> that would be nice to have`
`[08-17-2022 17:51:35] <one-horse-wagon[> UkoeHB: The 10 block lockout has served Monero well and I don't see how you can lower or eliminate it without risking major problems?`
`[08-17-2022 17:54:03] <isthmus> Haha it is kind of a "Chesterton's Fence" situation`
`[08-17-2022 17:54:25] <UkoeHB> one-horse-wagon[: isthmus this is the rationale https://github.com/monero-project/research-lab/issues/104#issuecomment-1186552665`
`[08-17-2022 17:54:38] <Rucknium[m]> So what would be the next concrete steps for multisig? The MAGIC Monero Fund could put in some funds, possibly.`
`[08-17-2022 17:55:07] <isthmus> A while back I tried to formulate a framework for approaching a potential reduction of the lock time, I dunno if it is helpful`
`[08-17-2022 17:55:08] <isthmus> https://raw.githubusercontent.com/noncesense-research-lab/lock_time_framework/master/writeup/lock_time_framework.pdf`
`[08-17-2022 17:55:41] <isthmus> I do not believe #2 to be correct anymore, based on subsequent work by hasu showing that lock time is not a strong mechanism against 51% attacks`
`[08-17-2022 17:57:14] <isthmus> Specifically this work: https://uncommoncore.co/wp-content/uploads/2019/10/A-model-for-Bitcoins-security-and-the-declining-block-subsidy-v1.02.pdf`
`[08-17-2022 17:58:08] <isthmus> Not all aspects apply to Monero (because the paper treats BTC mining as specialized-purpose equipment and RandomX is for general-purpose equipment, meaning that the switching costs are not the same). But much of it is very applicable`
`[08-17-2022 17:58:10] * isthmus ends ramble`
`[08-17-2022 17:58:10] <Rucknium[m]> isthmus: Is it OK if I link that here?:`
`[08-17-2022 17:58:11] <Rucknium[m]> https://github.com/monero-project/research-lab/issues/94`
`[08-17-2022 17:58:15] <isthmus> Yep`
`[08-17-2022 18:02:22] <UkoeHB> ok we are at the end of the hour so I'll call it here, thanks for attending everyone`

# Action History
- Created by: Rucknium | 2022-08-16T15:25:36+00:00
- Closed at: 2022-08-23T19:43:58+00:00
