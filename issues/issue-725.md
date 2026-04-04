---
title: Monero Research Lab Meeting - Wed 10 August 2022
source_url: https://github.com/monero-project/meta/issues/725
author: Rucknium
assignees: []
labels: []
created_at: '2022-08-10T06:07:39+00:00'
updated_at: '2022-08-16T15:25:46+00:00'
type: issue
status: closed
closed_at: '2022-08-16T15:25:46+00:00'
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

#724 

# Discussion History
## plowsof | 2022-08-15T06:18:18+00:00
Logs 
```
17:00:24 <UkoeHB> meeting time https://github.com/monero-project/meta/issues/725

17:00:24 <UkoeHB> 1. greetings

17:00:24 <UkoeHB> hello

17:00:55 <dangerousfreedom> Hello

17:00:59 <rbrunner> Hi

17:01:10 <tevador> Hi

17:01:55 <Rucknium[m]> Hi

17:03:38 <jberman[m]> hello

17:04:08 <UkoeHB> 2. updates, what's everyone working on?

17:04:50 <tevador> Published my X25519 code, now I'm back to updating the Jamtis specs.

17:04:54 <UkoeHB> me: finished legacy balance recovery for my seraphis library, started unit testing it

17:05:10 <Rucknium[m]> As mentioned above, an analysis of the evolution of the distribution of spent output
age on BTC, BCH, LTC, and DOGE:

17:05:11 <Rucknium[m]> https://rucknium.me/html/spent-output-age-btc-bch-ltc-doge.html

17:05:24 <Rucknium[m]> Source code here: https://github.com/Rucknium/OSPEAD/tree/main/General-Blockchain-Age-
of-Spent-Outputs

17:05:53 <dangerousfreedom> I have just been reading a lot about the different zero knowledge schemes and I
started scanning the blockchain (BP and so forth) in Rust now.

17:07:40 <jberman[m]> Nothing research related on my end, looking out for things that need doing to make sure
the hard fork goes smooth (pool update, PR review, etc)

17:09:06 <UkoeHB> jberman[m]: btw, it should be possible to hook up the seraphis lib to do balance recovery
with the current chain, with a bit of work; might be an interesting project (which would be a good proof of
concept for a future real wallet)

17:09:44 <UkoeHB> 3. discussion

17:10:08 <jberman[m]> noted :)

17:12:32 <rbrunner> Did anything jump out already from that spent output age evolution that would give hints
how to change something for Monero?

17:12:50 <rbrunner> Or is still early days?

17:13:16 <rbrunner> Looks interesting, in any case.

17:13:18 <tevador> I had a look at Rucknium[m]'s excellent write-up. I'd try to fit some simpler PDF function
as opposed to a very complex one. A shifted Pareto is one option. It's basically a power function. Might be
enough just to fit the general trend.

17:13:25 <Rucknium[m]> So basically it's outlining the final step, which is forecasting.

17:14:12 <Rucknium[m]> We want to get a sense of the variability of other blockchains so we can know what sort
of risk profile we may be facing from the forecast step.

17:15:31 <rbrunner> What was the trend? Was, in your gut feeling, variability high or low?

17:16:57 <Rucknium[m]> tevador: Thanks for the feedback. Right now the general direction I'm heading in is to
test out some mixture distributions to have some flexibility. Basically, combine two or more parametric
distributions. And then _maybe_ add something to account for the 24-hour cycle, like a periodic Laplace
distribution.

17:17:19 <Rucknium[m]> But the final decision is going to be determined by the performance, taking into
account to not overfit

17:18:12 <Rucknium[m]> Unfortunately I do not have the "documentation" published yet, but here is an image of
some distributions fit according to the loss function criteria in what I published above:
https://github.com/Rucknium/OSPEAD/blob/main/images/dry-run/estimate-div-target/estimate-div-target-L_FGT-
flavor-1.png

17:18:37 <Rucknium[m]> ^ This is a "dry run" based on the old Moser et al. (2018) data for demonstration
purposes

17:19:09 <Rucknium[m]> And it displays the ratio so that it's clearer how well the distributions fit

17:19:38 <Rucknium[m]> I am working on the "documentation" for the chart

17:20:08 <Rucknium[m]> rbrunner: Variability in the spent output age distribution for those 4 blockchains was
higher than I expected.

17:20:32 <rbrunner> Ok, interesting

17:21:18 <Rucknium[m]> Which means that the "dynamic risk" for a static Monero decoy selection algorithm would
be higher if Monero's distribution is similarly unstable

17:21:44 <Rucknium[m]> The "S" in OSPEAD stands for Static, so a fully dynamic DSA is pushed off for further
research. But it is important to know the risk rather than ignore it.

17:22:58 <Rucknium[m]> All my ducks are in a row for OSPEAD. "Just" need to write it up, present it to the
review panel, and then do the necessary estimations.

17:28:15 <UkoeHB> hmm, any other questions/comments/topics people want to bring up?

17:28:28 <Rucknium[m]> By the way, a while ago I paused the project to estimate the effect of minexmr's
increased pool fee on their share of hashpower, but I want to go back to it eventually. I have mostly settled
on a model and I was waiting on more data, i.e. more time to pass. The preliminary results suggested very
little effect, if any.

17:28:50 <rbrunner> And now they will close :)

17:29:53 <Rucknium[m]> Yes, but if nanopool takes their role....we may want to put more effort into trying to
resolve the challenges of tevador 's anti-pool proposal.

17:30:10 <Rucknium[m]> So far it doesn't look good: https://miningpoolstats.stream/monero

17:30:28 <Rucknium[m]> Or, anti-centralized pool. Pro-p2pool :)

17:30:48 <dangerousfreedom> UkoeHB: Yes, I would like to help developing the wallet (or what is needed) for
Seraphis so we could have a working full prototype asap. How is the overall project being coordinated and how
exactly I could help?

17:31:46 <rbrunner> Any question concerning Seraphis with the word "exactly" in it is still quite risky ...

17:32:05 <UkoeHB> not too much coordination so far, I'm just trying to finish the library so I can hand it off

17:32:05 <tevador> here are some proposed changes to the Jamtis key hierarchy:
https://gist.github.com/tevador/50160d160d24cfc6c52ae02eb3d17024#gistcomment-4259423

17:32:27 <UkoeHB> yes I still need to look at that (on vacation and focusing on legacy integration)

17:32:43 <dangerousfreedom> Yeah,  I see it is a bit vague now but someday maybe it will be reality :p

17:34:05 <tevador> Also I'd like to remove "certified addresses" from the main specs. It's better to move it
to the future invoice specs. I hope UkoeHB hasn't implemented it yet :P

17:34:12 <UkoeHB> a good starting point is to look at unit tests and get an understanding how the library is
put together

17:34:15 <dangerousfreedom> tevador: Nice. I will start participating on this discussion soon.

17:34:16 <tevador> Becomes a bit more complex with X25519

17:34:29 <UkoeHB> tevador: I only implemented core features

17:34:46 <dangerousfreedom> UkoeHB: Ok!

17:35:05 <UkoeHB> this is what I'm using for unit tests https://github.com/UkoeHB/monero/blob/6272be0845a07c5c
7d9613af4d70f695678efba5/src/seraphis/jamtis_core_utils.h#L60

17:35:48 <tevador> btw, my proposed change has one extra key

17:36:18 <UkoeHB> yeah

17:37:42 <tevador> UkoeHB: are you using Blake2b or Keccak?

17:38:20 <UkoeHB> blake2b https://github.com/UkoeHB/monero/blob/6272be0845a07c5c7d9613af4d70f695678efba5/src/s
eraphis/sp_hash_functions.cpp#L60

17:38:26 <tevador> cool

17:44:42 <UkoeHB> ok I think we can wrap it up here, thanks for attending everyone


```
Automated by [this](https://github.com/plowsof/post-libera-meeting-logs)

# Action History
- Created by: Rucknium | 2022-08-10T06:07:39+00:00
- Closed at: 2022-08-16T15:25:46+00:00
