---
title: Monero Research Lab Meeting - Wed 30 March 2022 @ 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/682
author: Rucknium
assignees: []
labels: []
created_at: '2022-03-29T14:14:46+00:00'
updated_at: '2022-04-04T18:17:28+00:00'
type: issue
status: closed
closed_at: '2022-04-04T18:17:28+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

[Join the Monero Matrix server if you don't already have a Matrix account.](https://forum.monero.space/d/79-how-to-join-the-monero-core-team-matrix-server-web)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20211027T170000&p1=1440)

Main discussion topics:

1. Greetings

2. Fee policy and dynamic block size discussion for upcoming hard fork: https://github.com/monero-project/meta/issues/630 ; https://github.com/monero-project/monero/pull/7819 ; https://github.com/monero-project/research-lab/issues/70

3. Revisit @tevador 's idea to record account indices in the tx, to improve robustness of output recovery: https://libera.monerologs.net/monero-research-lab/20211230 . Additional reading: https://gist.github.com/tevador/50160d160d24cfc6c52ae02eb3d17024#gistcomment-4025357

4. Focus on Seraphis address schemes and hopefully reach some kind of decision (or get closer, maybe narrow down the choices to 2 or 3). [Schemes](https://github.com/monero-project/research-lab/issues/92) [@tevador proposal](https://gist.github.com/tevador/50160d160d24cfc6c52ae02eb3d17024)

5. Adaptive CPU regulation for improved mining performance ( maxwellsdemon )

6. Further analysis of July-Aug 2021 tx volume anomaly ( Isthmus / Mitchellpkt - see [these meeting logs](https://github.com/monero-project/meta/issues/621#issuecomment-948953655)) [Previous analysis](https://mitchellpkt.medium.com/fingerprinting-a-flood-forensic-statistical-analysis-of-the-mid-2021-monero-transaction-volume-a19cbf41ce60) with [Reddit discussion](https://www.reddit.com/r/Monero/comments/pvm634/fingerprinting_a_flood_forensic_statistical/)

7. Improvements to the mixin selection algorithm ( [Decoy Selection Algorithm - Areas to Improve](https://github.com/monero-project/research-lab/issues/86), [JBerman's weekly updates](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/249#note_11480), [Binning PoC](https://github.com/monero-project/research-lab/issues/88), [OSPEAD](https://ccs.getmonero.org/proposals/Rucknium-OSPEAD-Fortifying-Monero-Against-Statistical-Attack.html) ) @j-berman @Rucknium

8. Seraphis/Triptych/Lelantus Spark ( [UkoeHB's Seraphis Proof of Concept work](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/256), [Seraphis repo](https://github.com/UkoeHB/Seraphis), [Lelantus Spark](https://eprint.iacr.org/2021/1173) & [Tripych Multisig](https://github.com/cypherstack/triptych-multisig/blob/main/main.pdf) )

9. MRL META: "Cat herding", i.e. prioritization of research areas and features. Active recruitment of technical talent, MRL structure, funding (@Rucknium & others) [Reddit discussion](https://www.reddit.com/r/Monero/comments/pkg3d6/the_monero_project_should_actively_recruit/)

10. Examine sample size and random seed matters in Monero's unit tests. IRC discussion: [monero-dev](https://libera.monerologs.net/monero-dev/20211018#c39593) , [monero-research-lab](https://libera.monerologs.net/monero-research-lab/20211018)

11. Multisig Drijvers attack mitigation [Technical note](https://github.com/UkoeHB/drijvers-multisig-tech-note) , [Haveno bounty](https://github.com/haveno-dex/haveno/issues/103)

12. Any other business

13. Confirm next meeting agenda


Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: UkoeHB

Previous meeting agenda/logs:

#677 

# Discussion History
## UkoeHB | 2022-03-30T17:52:39+00:00
```
[03-30-2022 17:00:22] <UkoeHB> meeting time https://github.com/monero-project/meta/issues/682
[03-30-2022 17:00:22] <UkoeHB> 1. greetings
[03-30-2022 17:00:22] <UkoeHB> hello
[03-30-2022 17:00:30] <Rucknium[m]> Hi
[03-30-2022 17:00:35] <dangerousfreedom> Hi!
[03-30-2022 17:00:44] <reeemuru[m]> yoroshiku!
[03-30-2022 17:00:52] <jberman[m]> howdy
[03-30-2022 17:01:22] <rbrunner> Hello
[03-30-2022 17:02:47] <SerHack> Hi
[03-30-2022 17:03:10] <UkoeHB> 2. updates, what is everyone working on?
[03-30-2022 17:04:50] <dangerousfreedom> I think I understand MLSAG signatures now :) I will soon start writing about it. Can I use some of your phrases in ZtM, Koe ?
[03-30-2022 17:05:15] <UkoeHB> go for it
[03-30-2022 17:05:44] <reeemuru[m]> I'm currently looking through xmr-ack's current work to see what kind tx fee analysis I can contribute
[03-30-2022 17:06:09] <xmr-ack[m]> hi
[03-30-2022 17:06:14] <reeemuru[m]> should have something neat to share in a couple weeks
[03-30-2022 17:06:35] <Rucknium[m]> My effort to uncover nonstandard Decoy Selection Algorithms (DSAs) by partitioning transactions by `unlock_time`, `tx_extra`, etc. has been bearing fruit. Not ready to share publicly yet. I think we should seriously consider enforcement of a standard DSA at the node rebroadcast-level in the hard fork after this upcoming one.
[03-30-2022 17:07:31] <Rucknium[m]> Eventually I hope to understand UkoeHB 's "deterministic" ring member selection proposal here:
[03-30-2022 17:07:31] <Rucknium[m]> https://github.com/monero-project/research-lab/issues/84
[03-30-2022 17:08:57] <UkoeHB> me: Still plugging away at seraphis multisig tx builders. I've been thinking about some software design ideas like correct by construction and validating preconditions. Multisig tx builders have this problem where a malicious participant could provide a malformed piece during a tx building ceremony that doesn't cause a failure until the final step. Trying to duplicate all tx semantic rules into custom semantic checkers 
[03-30-2022 17:08:57] <UkoeHB> isn't robust/easy, and isn't easy to extend to match hard fork rule changes.
[03-30-2022 17:09:11] <Rucknium[m]> I am also reading a bunch of statistical methodology papers.
[03-30-2022 17:10:06] <xmr-ack[m]> Me: I'm currently processing a preliminary dataset using gingeropolous server in hopes to start heavily focusing on feature engineering and also writing up my progress report for MAGIC 
[03-30-2022 17:13:25] <jberman[m]> Me: on a "background sync mode" where the client uses just the view key to scan for incoming tx's that can be enabled/disabled, I was unsure (and am now more sure) how to proceed in a way that makes the feature most useful for a mobile wallet in practice. I believe upon enabling the mode, wiping the spend key from memory would be a tangible security improvement if e.g. a user has been idle for a long time. Can see my thoughts
[03-30-2022 17:13:25] <jberman[m]> here: https://github.com/m2049r/xmrwallet/issues/785#issuecomment-1067482984
[03-30-2022 17:13:53] <jberman[m]> Maybe more -dev than -research-lab not sure
[03-30-2022 17:15:52] <jberman[m]> I've also spent some time studying the multisig stuff again. I hope to eventually be able to provide a valuable review on this work some day in the near future and fully understand the attacks it is mitigating, though I'm still a ways off in my training. So I'm studying it more in my free time to try to "get there". I will probably get back over to reviewing other PR's (like rbrunner 's reducing trips to daemon PR) today
[03-30-2022 17:16:17] <rbrunner> Hurray :)
[03-30-2022 17:16:39] <UkoeHB> 3. discussion, any topics to discuss, questions, comments?
[03-30-2022 17:16:53] <kayabanerve[m]> I do have a question I was curious about
[03-30-2022 17:18:18] <kayabanerve[m]> With Seraphis, which is a massive change which will require new keys already, why not take advantage of the breakage and move to Ristretto?
[03-30-2022 17:19:20] <UkoeHB> Our entire crypto library is geared to ed25519, it would be a massive undertaking to implement an entire new library.
[03-30-2022 17:19:52] <rbrunner> and we would have to keep the "old" one anyway. We would carry around two libraries, right?
[03-30-2022 17:20:26] <kayabanerve[m]> Do you mean from an optimization standpoint regarding the various types with various properties? Or from an existence standpoint? Because it wouldn't be an entire new library vs just changing the frombytes and tobytes functions
[03-30-2022 17:21:03] <kayabanerve[m]> rbrunner: And because of this, adding new from/to bytes functions
[03-30-2022 17:22:19] <rbrunner> Was just thinking that "taking advantage of the breakage" is relative if you basically double the crypto code ...
[03-30-2022 17:22:22] <kayabanerve[m]> I do understand not wanting to add extreme levels of technical debt. I just, immediately, don't actually believe it has any significant level of debt as it's functionally an encoder/decoder over Ed25519 and not actually a new curve
[03-30-2022 17:23:25] <rbrunner> The win would be some speedup, I guess as a (still) crypto noob?
[03-30-2022 17:23:56] <kayabanerve[m]> rbrunner: Thankfully not the case. I think the main issue post-impl would be the existing rct::key type would have to be deprecated for seraphis::key as rct::key is already encoded and uses the existing encoding functions. It's just a slight annoyance
[03-30-2022 17:25:19] <SerHack> Is maxwellsdemon here? 
[03-30-2022 17:26:02] <kayabanerve[m]> Ristretto removes torsion and guarantees canonical encodings at all times. It prevents two Ed25519 libraries from disagreeing on signatures if a signature isn't normal because everything must be normal. While Monero doesn't use traditional signatures, already bans torsion and canonicity, and isn't really looking for a multi node future, I just personally believe canonicity may be one of the most important things in
[03-30-2022 17:26:02] <kayabanerve[m]> cryptocurrency and that ristretto is the way to do it for ed25519
[03-30-2022 17:27:06] <kayabanerve[m]> Sightly faster equality checks, sightly slower encode/decode IIRC. It's basically just those pair of functions over an Ed25519 lib and we'd still keep all the Ed25519 arithmetic and point types.
[03-30-2022 17:27:17] <UkoeHB> I personally don't have the time/bandwidth to implement Ristretto. If someone can present a fully-featured library of manageable size that interfaces with the existing Ed25519 ops, then I would consider converting the existing seraphis library to use that.
[03-30-2022 17:27:35] <kayabanerve[m]> It also voids the need to multiply by 8 and I think I saw an issue saying small scalar multiplication wasn't optimized.
[03-30-2022 17:27:54] <kayabanerve[m]> UkoeHB: Got it. Completely understandable. Thanks for the heads up
[03-30-2022 17:28:46] <wernervasquez[m]> Ristretto requires that group elements only be constructed by decode and from_uniform_bytes. So, hash to point would need updating as well
[03-30-2022 17:29:13] <UkoeHB> iirc the dalek ristretto library has a hash to point algorithm
[03-30-2022 17:29:26] <rbrunner> Yeah, we have tons of code to implement and rework for Seraphis anyway, I am already dizzy thinking who will do all that, maybe moving even more is a luxury we simply can't afford ...
[03-30-2022 17:30:07] <wernervasquez[m]> If I have time (haha) I plan on writing my implementation to be ablr to use both
[03-30-2022 17:30:16] <rbrunner> as nice as it would probably be
[03-30-2022 17:30:34] <kayabanerve[m]> Ristretto specifies Elligator 2 as THE hash to curve algorithm 
[03-30-2022 17:30:54] <wernervasquez[m]> I am not an optimize coder so there wont be a perfect comparison
[03-30-2022 17:31:15] <kayabanerve[m]> While I think it'd be great for XMR to standardize on a modern hTC it should be possible to preserve the existing one and its benefits
[03-30-2022 17:33:21] <kayabanerve[m]> rbrunner: I'll probably step up here when I have a moment and given how people use wallet2 all the time, this will hopefully have minimal impact on wallets. For tooling, they'll need to update as they already did, but there is R for C/C++, JS, Rust, Zig...
[03-30-2022 17:34:02] <rbrunner> Maybe we will replace wallet2, just saying :)
[03-30-2022 17:34:10] <kayabanerve[m]> And I'm actually not sure if the existing hTC has benefits over Elligator. It just should be technically possible to keep it
[03-30-2022 17:34:26] <kayabanerve[m]> I can't wait for wallet4 personally
[03-30-2022 17:34:53] <rbrunner> :)
[03-30-2022 17:35:09] <rbrunner> Is there anything useful / sensible to discuss in this forum regarding hardfork preparation, and as preparation of Saturday's dev meeting?
[03-30-2022 17:35:20] <moneromooo> mul8 does three doublings. It's fast AFAIK.
[03-30-2022 17:35:54] <kayabanerve[m]> Got it. That may just be other small scalars then or I may be confusing my issues. Thanks for reminding me of mul8 :)
[03-30-2022 17:36:11] <UkoeHB> yeah ristretto would probably only give us on the order of 1% performance gains
[03-30-2022 17:37:04] <UkoeHB> variable base scalar multiplication is the main expense we pay for everything
[03-30-2022 17:37:39] <moneromooo> AIUI, the benefit of ristretto is ensuring we never forget to ensure points are in the expected subgroup (or whatever the correct term is).
[03-30-2022 17:37:55] <UkoeHB> right
[03-30-2022 17:38:07] <UkoeHB> rbrunner: don't think so
[03-30-2022 17:38:23] <rbrunner> Alright, thanks
[03-30-2022 17:40:27] <UkoeHB> anything else people want to discuss?
[03-30-2022 17:41:31] <Rucknium[m]> I would find it helpful if someone(s) could help convert the C++ code for old Monero decoy selection algorithms to mathematical expressions. jberman is working on the current one. My hypothesis is that some nonstandard wallets are using the older decoy selection algorithms.
[03-30-2022 17:42:10] <Rucknium[m]> I can see the historical empirical distributions here:
[03-30-2022 17:42:10] <Rucknium[m]> https://www.monero.observer/rucknium-shares-visualizations-monero-ring-member-age-distribution/
[03-30-2022 17:42:46] <Rucknium[m]> But having the mathematical expressions for them would be a big improvement since it is tough to work with the empirical estimate. And it's less precise.
[03-30-2022 17:43:14] <moneromooo> Old as in, the triangular one ?
[03-30-2022 17:43:19] <moneromooo> Or earlier ?
[03-30-2022 17:43:52] <Rucknium[m]> It was uniform and then triangular at one point, I believe.
[03-30-2022 17:44:15] <moneromooo> Yes. Then uniform with an exception for recent outs, I forget the details.
[03-30-2022 17:45:15] <Rucknium[m]> I think triangular is a priority, and then any earlier ones are a lesser priority.
[03-30-2022 17:45:20] <moneromooo> I think I saw a mathematical version of the triangular pick, but I have no idea where. IIRC smooth made that change, he might know.
[03-30-2022 17:46:19] <wernervasquez[m]> Rucknium[m]: I think dr_overdose may be capable of that. May be worth asking if he can and would. He seemed to be interested in contributing.
[03-30-2022 17:47:17] <Rucknium[m]> wernervasquez: Sounds great. I will reach out.
[03-30-2022 17:51:20] <UkoeHB> Ok I think we are at the end of the meeting. Thanks for attending everyone
```

# Action History
- Created by: Rucknium | 2022-03-29T14:14:46+00:00
- Closed at: 2022-04-04T18:17:28+00:00
