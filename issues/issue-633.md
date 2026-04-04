---
title: Monero Dev Meeting - Sun 28 November 2021 @ 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/633
author: monerobull
assignees: []
labels: []
created_at: '2021-11-23T15:40:55+00:00'
updated_at: '2021-11-28T19:38:25+00:00'
type: issue
status: closed
closed_at: '2021-11-28T19:38:25+00:00'
---

# Original Description
Location: [Libera.chat, #monero-dev](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-dev:monero.social?via=matrix.org&via=monero.social)

Time:
17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20211128T170000&p1=1440)

Main discussion topics:

1. Greetings

2. Fee changes ( [PR ](https://github.com/monero-project/monero/pull/7819), [Discussion](https://github.com/monero-project/research-lab/issues/70), [Older Discussion](https://github.com/monero-project/monero/issues/5711) )

3. Decoy selection algorithm changes ( [Decoy Selection Algorithm - Areas to Improve](https://github.com/monero-project/research-lab/issues/86), [JBerman's weekly updates](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/249#note_11480) )
 a. Jberman's binning outline
 b. Change to "recent spend window" from 10-60 to 10-20
4. [Ringsize increase](https://github.com/monero-project/research-lab/issues/79)

5. [UkoeHB's multisig refactor](https://github.com/monero-project/monero/pull/7877)

6. [i2p/Tor Network Screen Designs](https://github.com/monero-project/monero-gui/issues/2274)
 a. with idk from the I2p project

7. [Encode restore height as 26th word of the mnemonic seed ](https://github.com/monero-project/monero/issues/6639)(might be better to wait and couple with Seraphis/alternatives?)

8. Removing unlock time ( [Removing/Fixing/Encrypting monero's timelocks](https://github.com/monero-project/research-lab/issues/78) ) (it also affects [binning](https://github.com/monero-project/research-lab/issues/84))
 a. [Community feedback](https://www.reddit.com/r/Monero/comments/q0oiln/proposal_to_remove_timelock_feature/)

9. [Setting date for network upgrade.](https://github.com/monero-project/meta/issues/630)
 a. [Confirm release name for 0.18](https://github.com/monero-project/meta/issues/623)

10. vtnerd's proposals for [E2E of P2P traffic ](https://github.com/monero-project/monero/pull/8028) -[Background](https://github.com/monero-project/monero/issues/7078)

11. Any other business

12. Confirm next meeting agenda

Please comment on GitHub in advance of the meeting if you would like to propose an agenda item (or have it removed).
Logs will be posted here after the meeting.
Meeting chairperson: monerobull

Links to the previous meeting including logs:
[#617](https://github.com/monero-project/meta/issues/617)

# Discussion History
## tevador | 2021-11-23T22:27:20+00:00
Could https://github.com/monero-project/monero/issues/6639 be added to the agenda? There has been some recent development.

## hyc | 2021-11-23T22:41:05+00:00
Seems like with an address format change already looming in the near future (Seraphis) it would be better to only do a  seed format change once, not twice in rapid succession.

## tevador | 2021-11-23T22:46:40+00:00
@UkoeHB will correct me if I'm wrong, but AFAIK Seraphis doesn't affect private keys (and thus the mnemonic seed), only public addresses.

## UkoeHB | 2021-11-23T22:49:52+00:00
Seraphis doesn't require a new mnemonic, although there may be an additional private key (that can be derived from existing private keys or the base entropy).

## carrington1859 | 2021-11-24T00:36:50+00:00
I suspect this is unlikely to be implemented very soon, but it would be good to add vtnerd's proposals for E2E of P2P traffic as a rolling agenda item to get some eyes on it:

[E2E P2P Docs](https://github.com/monero-project/monero/pull/8028) - [Background](https://github.com/monero-project/monero/issues/7078)

## UkoeHB | 2021-11-28T18:37:42+00:00
```
[2021-11-28 16:59:02] <disclosure-bot[m> Greetings. If any meeting participants have a potential conflict of interest, please disclose it now.
[2021-11-28 16:59:17] <monerobull[m]> A what
[2021-11-28 17:00:06] <selsta> hi
[2021-11-28 17:00:12] <hyc> hey
[2021-11-28 17:00:20] <Halver[m]> hi
[2021-11-28 17:00:21] <dont_thread_on_m> o7
[2021-11-28 17:00:30] <tevador> o/
[2021-11-28 17:00:34] <Rucknium[m]> Present
[2021-11-28 17:00:53] <monerobull[m]> Hello, the meeting starts now. Main goal for today is deciding on a fork-date for .18 :)
[2021-11-28 17:01:34] <selsta> I think there is a discussion about it on Github, right?
[2021-11-28 17:02:03] <selsta> https://github.com/monero-project/meta/issues/630
[2021-11-28 17:02:05] <monerobull[m]> Yes, everything should be linked here https://github.com/monero-project/meta/issues/633
[2021-11-28 17:02:43] <tevador> 15th March 2022
[2021-11-28 17:03:00] <selsta> So basically we want to release 1 month before, so 15 Feb 2022
[2021-11-28 17:03:11] <selsta> Code wise everything should be ready in January
[2021-11-28 17:03:27] <selsta> so that we have 1 month for last minute bugs that pop up
[2021-11-28 17:03:45] <selsta> that worked quite well for the last hardforks
[2021-11-28 17:04:03] <monerobull[m]> that seems reasonable for the features that currently are on the list for .18, does anyone have any objections? 
[2021-11-28 17:04:17] <hyc> sounds good
[2021-11-28 17:05:26] <monerobull[m]> We will come back to this point later in case someone joins the discussion late
[2021-11-28 17:05:57] <monerobull[m]> Alright, 2. Fee changes, is there discussing to do on this topic?
[2021-11-28 17:06:25] <selsta> not from my side but maybe others have something to add
[2021-11-28 17:07:37] <monerobull[m]> ok, moving on, Decoy selection algorithm changes
[2021-11-28 17:08:20] <selsta> Rucknium[m] ^
[2021-11-28 17:08:23] <monerobull[m]> jberman: anything on this topic?
[2021-11-28 17:09:38] <Rucknium[m]> I clarified here that decoy selection doesn't need to go into a hard fork. OSPEAD will in fact leverage the discontinuity created by the 11 --> 16 ring size for statistical purposes:
[2021-11-28 17:09:38] <Rucknium[m]> https://github.com/monero-project/meta/issues/630#issuecomment-974480882
[2021-11-28 17:10:15] <jberman[m]> Binning is next up to work on on my end. Planning to spend more time fleshing out parameter selection (e.g. how many blocks per bin). Would be nice to get feedback on the general approach laid out in this issue: https://github.com/monero-project/research-lab/issues/88
[2021-11-28 17:11:14] <Rucknium[m]> I think binning should be vetted by a statisticians before it's implemented in production code. We audit our cryptography. Our statistics should be similarly audited.
[2021-11-28 17:11:17] <jberman[m]> We had discussed in the past targeting to release binning in the hard fork, to maximize chances everyone uses the same algo
[2021-11-28 17:14:11] <monerobull[m]> on the topic of binning, deprecation of timelocks has officially been decided on, correct?
[2021-11-28 17:15:39] <jberman[m]> seems it's fair to say there is a rough consensus to deprecate imo. It's not a strict requirement that it is deprecated for the binning algo proposed though
[2021-11-28 17:16:22] <Rucknium[m]> Another issue is that isthmus found that tens of thousands of rings have an effective ring size of one due to the fact that services or wallets used "cached" outputs as decoys. In fact the current estimate is that 250,000 rings do this.
[2021-11-28 17:16:54] <Rucknium[m]> I discuss the issue here, along with a rough proposed solution:
[2021-11-28 17:16:54] <Rucknium[m]> https://github.com/monero-project/meta/issues/630#issuecomment-980752098
[2021-11-28 17:17:06] <hyc> they used the same set of outputs for multiple txns?
[2021-11-28 17:18:53] <jberman[m]> I recall looking at the tx and seeing many rings using the same subset of outputs, but not the same rings entirely (which isn't possible to do for 250,000 rings)
[2021-11-28 17:19:30] <Rucknium[m]> hyc: hyc:  Yes. So M-1 outputs were all the same. Just the M'th was different, which is clearly the real spend.
[2021-11-28 17:19:58] <Rucknium[m]> In effect, it's a loophole for the consensus rule of having exactly M ring members.
[2021-11-28 17:20:06] <hyc> ugh
[2021-11-28 17:20:09] <Halver[m]> hyc: quote isthmus : 65k ring sigs with effective ring size = 1.
[2021-11-28 17:20:28] <jberman[m]> hash-based collisions wouldn't work as was being discussed earlier, this would be overly burdensome to check for I think
[2021-11-28 17:21:00] <tevador> Yes, this detection of duplicates would be quite difficult to implement.
[2021-11-28 17:21:07] <Rucknium[m]> Halver: isthmus has given me a back-of-the-envelope estimate that the true number may be about 250k, not 65k.
[2021-11-28 17:21:31] <jberman[m]> hash-based collisions wouldn't work because they're not identical rings (bc of the real outputs)
[2021-11-28 17:21:43] <hyc> right so what's the proposed solution? keeping a map of the last N rings?
[2021-11-28 17:23:05] <Rucknium[m]> This was just revealed a few days ago. I'm not sure about how large the computational burdens for any solution may be. This is a delivery of the problem from MRL to -dev. You're welcome :(
[2021-11-28 17:23:45] <hyc> outputs are referenced by an integer index, not their hash
[2021-11-28 17:24:13] <hyc> so the first thing that comes to mind is turning a ring into a bitmap
[2021-11-28 17:24:14] <tevador> It would need a huge hashtable and each new output would add N items into the hashtable where N is the ring size (all possible real spends).
[2021-11-28 17:24:27] <UkoeHB> This can be more-or-less solved with deterministic rings.
[2021-11-28 17:24:39] <tevador> ^this is a better solution
[2021-11-28 17:25:04] <Rucknium[m]> What do you mean by deterministic rings?
[2021-11-28 17:25:32] <UkoeHB> using a public seed to generate rings, instead of inserting private entropy to an rng
[2021-11-28 17:26:35] <hyc> i don't understand how that works to keep the real output hidden
[2021-11-28 17:27:04] <Rucknium[m]> Interesting. And the real spend would be hidden by some sort of hash function that combines the real spend and the public seed, and spits out the set of all ring members?
[2021-11-28 17:27:14] <tevador> the sender of the TX would be able to fix only a single output location (the real spend), the rest woule be random
[2021-11-28 17:27:45] <UkoeHB> You get e.g. 11 pseudo-random numbers from the public seed, randomly select one of them, take the delta between that random selectee and your real output, then rotate all the generated numbers by that offset.
[2021-11-28 17:27:49] <hyc> then you're assuming the internal state of the RNG can't be reversed
[2021-11-28 17:28:38] <tevador> it works even if the RNG can be reversed, see for example: https://github.com/tevador/igamma
[2021-11-28 17:30:08] <Rucknium[m]> UkoeHB:  I don't yet understand the words you are using. I will try to understand how this process cannot be reversed.
[2021-11-28 17:30:40] <UkoeHB> It has already been discussed here: https://github.com/monero-project/research-lab/issues/84
[2021-11-28 17:31:49] <UkoeHB> The point is it solves ring-reuse because if you tie the input seed to tx data, including key images, then seeds are always unique.
[2021-11-28 17:33:32] <UkoeHB> In any case, what's the next agenda item?
[2021-11-28 17:33:54] <monerobull[m]> Ringsize increase, i assume consensus has been reachend
[2021-11-28 17:34:09] <tevador> 16?
[2021-11-28 17:34:14] <monerobull[m]> yes
[2021-11-28 17:34:17] <Rucknium[m]> I see. I will read into it. Deterministic decoy selection is probably too novel to include in this hard fork.
[2021-11-28 17:35:09] <UkoeHB> I think the concerns raised about verification cost increases haven't really been addressed: https://github.com/monero-project/research-lab/issues/79
[2021-11-28 17:35:26] <monerobull[m]> ill remove ringsize increase as an item for the next meeting then 
[2021-11-28 17:36:29] <monerobull[m]> UkoeHB: or maybe i wont just yet
[2021-11-28 17:36:56] <tevador> what is the verification time and tx size cost of ringsize=16?
[2021-11-28 17:36:58] <UkoeHB> Has anyone made any effort to examine the upper bounds of tx throughput of the network?
[2021-11-28 17:37:28] <UkoeHB> This topic was brought up a couple months ago and people said 'wow cool idea', but has anything been done?
[2021-11-28 17:37:33] <Rucknium[m]> Ring size was discussed in -dev. -dev push it to MRL. MRL said, 16, basically. We can re-open the issue for discussion, I guess.
[2021-11-28 17:38:07] <Rucknium[m]> What do you mean by "upper bounds of tx throughput of the network"?
[2021-11-28 17:38:58] <UkoeHB> I mean that literally ?
[2021-11-28 17:39:09] <UkoeHB> How much tx throughput can nodes handle?
[2021-11-28 17:39:16] <Rucknium[m]> mj-xmr with others is working on generating stats about tx characteristics like input and output numbers to map onto UkoeHB 's work on the Seraphis performance tests.
[2021-11-28 17:39:17] <selsta> I assume it will depend on node specs and network speed
[2021-11-28 17:40:09] <UkoeHB> Rucknium[m]: I see, yes that might be the right direction.
[2021-11-28 17:40:35] <rbrunner> Well, can we do anything at all about larger verification costs of ringsize 16? Seems to me we have to just "eat" somewhat longer syncs for enhanced privacy
[2021-11-28 17:40:40] <hyc> should prob benchmark on "typical" PC of 2020 vintage or so. assuming 3-5yr lifetime of most PCs
[2021-11-28 17:41:12] <monerobull[m]> l i7 2600k quad core roughly 400 TPS per core.
[2021-11-28 17:41:43] <monerobull[m]> limiting factor would be bandwidth
[2021-11-28 17:42:09] <UkoeHB> > Seems to me we have to just "eat" somewhat longer syncs for enhanced privacy
[2021-11-28 17:42:09] <UkoeHB> Yes, but it would be useful to know exactly when nodes have to shut down.
[2021-11-28 17:42:09] <Rucknium[m]> rbrunner:  I think if we can eat the cost, we should do so. Privacy threats are increasing every day. I don't think I need to enumerate them here.
[2021-11-28 17:43:09] <rbrunner> Agreed, that why I was wondering what concerns we could probably address, as UkoeHB asked
[2021-11-28 17:43:12] <selsta> We have to live with increased verification anyway once we move to Seraphis
[2021-11-28 17:43:56] <UkoeHB> Sure, but the same problem would arise for Seraphis: what ring size is acceptable, that won't kill the network?
[2021-11-28 17:44:03] <tevador> Also worth noting that CPU speed increases faster than network bandwidth, so verification time is a somewhat smaller problem than tx size.
[2021-11-28 17:45:28] <monerobull[m]> anything to add to this topic?
[2021-11-28 17:46:01] <UkoeHB> I think verification time can also be a problem if synching from scratch. If synching a new copy takes e.g. 1 month, that is a bit concerning.
[2021-11-28 17:46:22] <rbrunner> But we should be very, very far from that, right?
[2021-11-28 17:46:23] <UkoeHB> Revalidating from scratch without checkpoints*
[2021-11-28 17:47:16] <UkoeHB> Ok, but when does that happen? When does that happen after increasing ring size? We are discussing what things look like, without any light.
[2021-11-28 17:48:00] <tevador> I think the initial sync is more I/O bound than CPU bound at the moment
[2021-11-28 17:48:09] <rbrunner> Agreed, it would be nice to hold hard numbers
[2021-11-28 17:49:08] <Rucknium[m]> Who is going to take this on? There's got to be some people in the broader Monero community who love running benchmarks.
[2021-11-28 17:49:09] <ErCiccione> Maybe better postpone the decision for when there will be more concrete numbers? This is something that must not be rushed. Even worth delaying the hard fork if there are doubts IMO
[2021-11-28 17:49:11] <hyc> ... sorry to go offtopic - my gitian build of release-v0.17 failed on Mac, looks like it's missing -std=c++11 build flag
[2021-11-28 17:49:30] <selsta> hyc: will check
[2021-11-28 17:50:01] <selsta> we use c++14 so don't think adding -std=c++11 is correct
[2021-11-28 17:50:21] <hyc> ok, can look into this more after meeting
[2021-11-28 17:50:33] <selsta> also we set the c++ version with cmake so it shouldn't be necessary to set manually
[2021-11-28 17:51:19] <selsta> re verification: the question is, is the slight ring size bump worth the increased verification time without seraphis
[2021-11-28 17:51:21] <monerobull[m]> @idk are you here? 
[2021-11-28 17:53:02] <monerobull[m]> selsta: the ring size bump was short-term to be compatible with binning, no?
[2021-11-28 17:53:34] <crypto_grampy[m]> Would be fun to have a sort of xmrig style benchmarking for monerod that anyone can run/submit processor benchmarks.  Not sure what all the metrics would be
[2021-11-28 17:53:46] <UkoeHB> the sentiment was more like 'seems like a good idea to increase ring size periodically'
[2021-11-28 17:54:11] <jberman[m]> compatibility with binning was 1 reason for going with an even 16, not necessarily for increasing by the exact amount proposed
[2021-11-28 17:54:43] <ErCiccione> FWIW i'm for being more conservative when it comes to ring size increases. We should also keep in mind that Monero's UX is far from great and increasing verification times and size should be considered very carefully
[2021-11-28 17:54:54] <tevador> another option is to increase to 12, which should also support binning
[2021-11-28 17:55:09] <Rucknium[m]> crypto_grampy: That's a great idea. Get the community involved in dev planning decisions by providing data in a decentralized way.
[2021-11-28 17:56:06] <jberman[m]> I think I can take on this research to arrive at throughput limits targeting a specific machine pre-hard fork. I'm kinda putting lots on my plate, and would cede it to someone else who comes along who wants to take it. But if no one else comes along, I'll do it
[2021-11-28 17:56:06] <hyc> if there's no significant improvement in resistance to flooding attacks there's no point
[2021-11-28 17:57:03] <UkoeHB> jberman[m]: I think you should focus on your current stuff. Someone else should take this.
[2021-11-28 17:57:06] <ErCiccione> ^ exactly. If it's a significant improvement, let's see some data. Otherwise a smaller increase (if an increase is necessary at all) would be better IMO
[2021-11-28 17:57:50] <ErCiccione> In any case appears to me that we need more data before being able to take an informed decision (unless i'm missing something)
[2021-11-28 17:58:00] <hyc> definitely, anyone can run benchmarks, no programming skills required. someone else in the community should step up for that
[2021-11-28 17:58:06] <Rucknium[m]> Isn't 11 --> 16 a significant increase to resistance to flooding attacks? It would pretty much kill them, probably?
[2021-11-28 17:58:24] <rbrunner> Hmm, this GitHub issue seems to have lots and lots of number already, no? https://github.com/monero-project/research-lab/issues/79
[2021-11-28 17:58:41] <rbrunner> I think 16 is markedly better
[2021-11-28 17:59:17] <hyc> agreed
[2021-11-28 17:59:27] <hyc> but 11 -> 12 seems quite arbitrary
[2021-11-28 17:59:42] <rbrunner> Otherwise you would think the proposal would be dead for a long time already ...
[2021-11-28 17:59:54] <hyc> and "seems like a good idea to increase ringsize periodically" is just baseless
[2021-11-28 18:00:07] <ErCiccione> not a big fan of the idea as well
[2021-11-28 18:00:43] <monerobull[m]> we already have a decent amount of data suggesting 16 is the most reasonable number
[2021-11-28 18:00:50] <Rucknium[m]> Very back-of-the-envelope: if you want to control 50% of outputs in a one-month period, say, then with the current size of 11 you need to increase tx volume by 5 times, or 500%.  With 16 it would be increasing volume by 8 times, or 800%.
[2021-11-28 18:01:03] <ErCiccione> > Ring size 15/16/17 will mean verification time increases of 36%/45%/55%.
[2021-11-28 18:01:06] <crypto_grampy[m]> Maybe sgp_ @sgp_:matrix.org can speak to it
[2021-11-28 18:01:50] <monerobull[m]> verification only effects initial node setup, right?
[2021-11-28 18:01:58] <ErCiccione> 45% is quite a lot
[2021-11-28 18:02:23] <rbrunner> The cost of doing business in a hostile world?
[2021-11-28 18:02:53] <monerobull[m]> ErCiccione: not if its bottlenecked by download speed 5/95
[2021-11-28 18:03:29] <hyc> right, there's a good possibility most users won't see it because it's hidden by I/O bottlenecks
[2021-11-28 18:04:00] <sgp_> Frankly an increase is necessary for the minimum privacy guarantees. This has been discussed like 1000 times now in MRL, what's up with this discussion now
[2021-11-28 18:04:10] <UkoeHB> It seems knaccc and sgp_ were looking at improving churn effectiveness with larger rings (in MRL issue 79).
[2021-11-28 18:04:47] <sgp_> Churn is only one minor reason, it's not the main reason for me
[2021-11-28 18:05:16] <sgp_> I wouldn't say 11 is "unsafe", but it makes my VERY uneasy
[2021-11-28 18:05:21] <ErCiccione> sgp_: Discussion is always good if doubts arise and the doubt right now it's not much about ring increase or not, but more of how much
[2021-11-28 18:05:24] <sgp_> s/my/me/
[2021-11-28 18:06:25] <monerobull[m]> might suck for raspberry nodes but you shouldnt do that anyways based on the lack of aes
[2021-11-28 18:06:34] <ErCiccione> Also, as you said the increase to 16 would be the largest in Monero's history. Don't think it's crazy to weight the option carefully
[2021-11-28 18:06:37] <hyc> we're past the hour mark, should we move on? 
[2021-11-28 18:06:54] <hyc> sounds like we already have relevant data to answer this question
[2021-11-28 18:06:58] <sgp_> It has been weighted carefully over almost a year of discussion
[2021-11-28 18:07:09] <sgp_> ArticMine wanted ~25
[2021-11-28 18:07:34] <monerobull[m]> we will skip the i2p agenda point for now since idk isnt here
[2021-11-28 18:07:48] <Rucknium[m]> sgp_: Same here. I speak also as someone who has been closely examining the statistical attack surface of Monero's privacy model.
[2021-11-28 18:08:53] <monerobull[m]> encode restore height as 26th word will be skipped since it will most likely wait till seraphis 
[2021-11-28 18:09:03] <monerobull[m]> so we have a lot of time for that
[2021-11-28 18:09:31] <ErCiccione> If 16 is considered a good comproise between security and UX i'm ok with it. I just want to stress the importance of good user experience.
[2021-11-28 18:09:34] <monerobull[m]> lets quickly come back to hardfork date: 15.th March 2022, any objections?
[2021-11-28 18:09:59] <tevador> It doesn't need to wait for Seraphis, but it doesn't need a hardfork, so it can be discussed another time.
[2021-11-28 18:10:29] <sgp_> monerobull[m]: Seems late to me but it is what it is I guess
[2021-11-28 18:10:34] <UkoeHB> My objection is there are still open PRs with insufficient reviews, that have been open for over a month. Setting dates implies they will get reviews... is that really the case?
[2021-11-28 18:11:50] <ErCiccione> setting dates could help pushing people to review.
[2021-11-28 18:11:50] <hyc> is gingeropolous still here? talking about hackathon events to close tickets
[2021-11-28 18:12:27] <ErCiccione> hyc: this is something i've been proposing many times in past before hard fork. Would be a cool idea if somebody could organize something
[2021-11-28 18:12:38] <monerobull[m]> PRs for this fork shouldnt be all that complex, right?
[2021-11-28 18:13:18] <UkoeHB> There is fee PR and multisig PR in limbo.
[2021-11-28 18:13:37] <UkoeHB> BP+ PR, I'm not sure - close?
[2021-11-28 18:14:08] <monerobull[m]> UkoeHB: didnt you just find some bug with multisig?
[2021-11-28 18:14:32] <UkoeHB> Yes there are more issues after this PR.
[2021-11-28 18:14:32] <ErCiccione> multisig doesn't require hard fork rght? In any case we (haveno) need it in soon
[2021-11-28 18:15:11] <ErCiccione> UkoeHB: something new beside what we already discussed?
[2021-11-28 18:16:04] <UkoeHB> I don't remember what we discussed. I believe core is planning to make an announcement to clarify the situation.
[2021-11-28 18:16:16] <ErCiccione> Basically these: https://github.com/haveno-dex/haveno/issues?q=is%3Aissue+is%3Aopen+label%3Aa%3Amonero+label%3Ais%3Abug
[2021-11-28 18:16:26] <ErCiccione> ah ok it's something new then
[2021-11-28 18:16:56] <monerobull[m]> lets quickly close this: https://github.com/monero-project/meta/issues/623
[2021-11-28 18:17:09] <monerobull[m]> Fluorine Fermi was the condorcet winner.
[2021-11-28 18:18:02] <UkoeHB> sgtm
[2021-11-28 18:18:21] <monerobull[m]> ?
[2021-11-28 18:18:33] <UkoeHB> sounds good to me
[2021-11-28 18:18:39] <monerobull[m]> oh ok
[2021-11-28 18:19:18] <monerobull[m]> we need at least somewhat of a consensus, please reply ,:)
[2021-11-28 18:19:18] <hyc> meh. should've required name begin with fl---. imo.
[2021-11-28 18:19:49] <monerobull[m]> oxygen orion doesnt either ;)
[2021-11-28 18:20:43] <hyc> not a lot of choices there. I seem to recall suggesting oxygen ocelot a the closest I could find
[2021-11-28 18:21:01] <Rucknium[m]> Fermi is fine. Flamingo would have been glorious and very meme-able, however.
[2021-11-28 18:22:02] <monerobull[m]> Next one will most likely be Neon Nebula so that will be cool
[2021-11-28 18:23:04] <monerobull[m]> and after that salty sombrero/spider, lots of memeable stuff for the future
[2021-11-28 18:24:04] <monerobull[m]> so we have 1 sgtm, 1 fine and one meh?
[2021-11-28 18:24:24] <hyc> officially meh, yes. ;)
[2021-11-28 18:25:14] <ErCiccione> +1 meh
[2021-11-28 18:25:32] <monerobull[m]> does this count as consensus or whats the plan now?
[2021-11-28 18:26:19] <hyc> prob need a few more people to speak up
[2021-11-28 18:26:56] <jberman[m]> ~ I respect the vote ~
[2021-11-28 18:27:09] <monerobull[m]> ill need to get going soon, i porpose next meeting next week so we can get 2 in before christmas/holidays
[2021-11-28 18:27:14] <hyc> then it sounds like consensus to me
[2021-11-28 18:27:37] <hyc> next meeting should prob be focused on v0.17.3
[2021-11-28 18:27:58] <hyc> presumably we're tagging it in the next day or so
[2021-11-28 18:28:16] <hyc> assuming no other last minute issues
[2021-11-28 18:28:30] <monerobull[m]> monerobull[m]: 5.12, 19.12, 9.01.22 
[2021-11-28 18:29:13] <moneromooo> To increase volume 5 times, you increase by 400%. Yes, I am a bloody pedant.
[2021-11-28 18:30:17] <Rucknium[m]> moneromooo: Yes, true. Thanks for the precision.
[2021-11-28 18:31:21] <monerobull[m]> alright, ill have to leave now, i think we discussed all the pressing issues. Thanks for participating, feel free to keep discussing though.
```

# Action History
- Created by: monerobull | 2021-11-23T15:40:55+00:00
- Closed at: 2021-11-28T19:38:25+00:00
