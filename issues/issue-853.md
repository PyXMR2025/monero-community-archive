---
title: Monero Research Lab Meeting - Wed 28 June 2023, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/853
author: Rucknium
assignees: []
labels: []
created_at: '2023-06-24T22:33:42+00:00'
updated_at: '2023-07-05T00:35:21+00:00'
type: issue
status: closed
closed_at: '2023-07-05T00:35:21+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

[Join the Monero Matrix server if you don't already have a Matrix account.](https://forum.monero.space/d/79-how-to-join-the-monero-core-team-matrix-server-web)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20211027T170000&p1=1440)

Main discussion topics:

1. Greetings

2. Discuss: Reducing 10 block lock: https://github.com/monero-project/research-lab/issues/102#issuecomment-1577827259

3. Discuss: [Exploring Trustless zk-SNARKs for Monero's payment protocol](https://github.com/monero-project/research-lab/issues/100). What are the bottlenecks for potential implementation?

4. Improvements to the decoy selection algorithm ( [Decoy Selection Algorithm - Areas to Improve](https://github.com/monero-project/research-lab/issues/86), [Binning PoC](https://github.com/monero-project/research-lab/issues/88), [OSPEAD](https://ccs.getmonero.org/proposals/Rucknium-OSPEAD-Fortifying-Monero-Against-Statistical-Attack.html) ) @j-berman @Rucknium

5. Seraphis. ( [UkoeHB's Seraphis Proof of Concept work](https://ccs.getmonero.org/proposals/seraphis-wallet-poc-2.html), [Seraphis repo](https://github.com/UkoeHB/Seraphis) ).

6. MRL Meta: "Cat herding", i.e. prioritization of research areas and features. Active recruitment of technical talent, MRL structure, funding (@Rucknium & others) [MoneroResearch.info repository of Monero-related research papers](https://moneroresearch.info/), [Reddit discussion](https://www.reddit.com/r/Monero/comments/pkg3d6/the_monero_project_should_actively_recruit/)

7. Any other business

8. Confirm next meeting agenda


Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: UkoeHB

Previous meeting agenda/logs:

#851 

# Discussion History
## UkoeHB | 2023-06-28T17:52:10+00:00
`[06-28-2023 17:00:12] <kayabanerve[m]> 👋`
`[06-28-2023 17:00:20] <UkoeHB> meeting time https://github.com/monero-project/meta/issues/853`
`[06-28-2023 17:00:20] <UkoeHB> 1. greetings`
`[06-28-2023 17:00:20] <UkoeHB> hello`
`[06-28-2023 17:00:22] <sgp[m]> hello`
`[06-28-2023 17:00:22] <vtnerd_> hi`
`[06-28-2023 17:00:29] <rbrunner> Hello`
`[06-28-2023 17:01:46] <jberman[m]> hello`
`[06-28-2023 17:03:05] <UkoeHB> 2. updates, what's everyone working on?`
`[06-28-2023 17:03:44] <kayabanerve[m]> My update is simply my announcement of my work on BP+ + curve trees.`
`[06-28-2023 17:04:42] <vtnerd_> me: p2p encryption. annoying as assumed to get into existing code, but its moving along`
`[06-28-2023 17:05:23] <UkoeHB> me: just did monerokon. In light of kayabanerve[m]'s progress on full-chain membership proofs, I have decided to implement this crypto interface for ed25519 https://github.com/UkoeHB/monero/issues/7 which is a first step to migrating the library to a new curve if necessary. After that I plan to take a 2 month hiatus from Monero work.`
`[06-28-2023 17:06:58] <kayabanerve[m]> I'm unsure if we need such an interface.`
`[06-28-2023 17:07:20] <kayabanerve[m]> My work on BP+ included the range proofs. Accordingly, we could keep Monero's range proofs limited to Ed25519.`
`[06-28-2023 17:07:21] <UkoeHB> the interface makes it easier to swap between curves`
`[06-28-2023 17:07:46] <jberman[m]> Past few weeks I worked a bit on optimization of kayabanerve 's impl + preparing for monerokon + spent some time on monero-serai. Planning to continue with full chain membership impl work, Seraphis wallet work (the production wallet scanner is still a WIP), and some monero-serai work`
`[06-28-2023 17:08:07] <UkoeHB> kayabanerve[m]: the squashed enote model requires commitments and addresses to be on the same curve`
`[06-28-2023 17:08:35] <kayabanerve[m]> Sure, yet if we can commit to a curve swap now, the only proofs which would be variadic would be the range proofs. The fact we have an alt impl of those ready, on each curve, voids their need to be variadic.`
`[06-28-2023 17:08:57] <kayabanerve[m]> ... eh. I have other commentary but none worth doing. I'll drop this, sorry for taking a moment of time away.`
`[06-28-2023 17:11:02] <UkoeHB> using a curve abstraction makes it much easier to do perf comparisons and isolates crypto backend dependencies`
`[06-28-2023 17:11:29] <kayabanerve[m]> And lets us continue development on Ed25519 now while the new curves aren't ready, which is why I realized my commentary was void, yep`
`[06-28-2023 17:12:31] <UkoeHB> 3. discussion, any research topics we should discuss today?`
`[06-28-2023 17:14:13] <kayabanerve[m]> I wanted to inquire what info the developer community wants from me re: my work, and get a commitment to deploying Seraphis under a curve cycle, or at least, get the ball rolling on a commitment.`
`[06-28-2023 17:14:36] <kayabanerve[m]> koe's willingness to abstract the curve sounds like it satisfies my #2 for now.`
`[06-28-2023 17:15:10] <kayabanerve[m]> Though we need someone to actually implement the new curve. Ideally, I think @tevador, yet I'm unsure their availability/willingness.`
`[06-28-2023 17:15:28] <UkoeHB> We either need a C interface for your library (in which case the path to deterministic builds needs to be established) or a migration to C/C++.`
`[06-28-2023 17:16:12] <kayabanerve[m]> Sorry, for my work in total or for the curve impl I technically threw togeher`
`[06-28-2023 17:16:37] <kayabanerve[m]> Eventually, it in total, of course. I'm just unsure the immediate discussion`
`[06-28-2023 17:18:04] <rbrunner> I remember that at one time we had a very lively discussion in the "No Wallet Left Behind" room about interfacing with Rust`
`[06-28-2023 17:18:09] <kayabanerve[m]> Rust can do deterministic builds. I'd prefer to keep the proof in Rust for several reasons, yet the curve and the tree itself would be natural to have in C++. We can rewrite it in C++14, yet it'll reduce the quality (and not just due to my Rust shilling) IMO.`
`[06-28-2023 17:18:12] <rbrunner> which then at one point was dropped`
`[06-28-2023 17:18:26] <rbrunner> Anybody remember why that was so?`
`[06-28-2023 17:18:43] <UkoeHB> The first step is to actually integrate your work so we can evaluate it in context. That requires a C/C++ API for the curve pair and for the membership proof,.`
`[06-28-2023 17:18:53] <rbrunner> Disappointing speed results from the crypto library in Rust that was a candidate?`
`[06-28-2023 17:19:07] <kayabanerve[m]> I do not have a valid implementation of the curve pair. I've tested off of pasta.`
`[06-28-2023 17:19:47] <UkoeHB> even an invalid implementation cannot be used/tested/trialed without a usable API`
`[06-28-2023 17:19:49] <kayabanerve[m]> Hence my prior comment on needing someone to "actually implement" (though shipping pasta wouldn't be the end of the world).`
`[06-28-2023 17:20:13] <kayabanerve[m]> Sure. So immediately, a C++ API to the membership proof. Should be feasible enough.`
`[06-28-2023 17:20:22] <kayabanerve[m]> jberman: Any interest?`
`[06-28-2023 17:21:03] <jberman[m]> Yep, I can take that`
`[06-28-2023 17:21:26] <rbrunner> Does this membership proof interface with the blockchain file?`
`[06-28-2023 17:21:41] <rbrunner> Write into it, read out of it?`
`[06-28-2023 17:21:43] <UkoeHB> rbrunner: no`
`[06-28-2023 17:21:59] <UkoeHB> not directly anyway`
`[06-28-2023 17:22:10] <kayabanerve[m]> It needs the tree root and a series of generators to verify.`
`[06-28-2023 17:22:11] <kayabanerve[m]> To prove, it needs information about the tree.`
`[06-28-2023 17:22:12] <kayabanerve[m]> At the end of a block, we need to append to the tree.`
`[06-28-2023 17:23:24] <rbrunner> So managing the tree will be a quite big new mass of code on the C++ side?`
`[06-28-2023 17:23:54] <kayabanerve[m]> Eh. At end of block, take all new enotes, call append.`
`[06-28-2023 17:24:13] <kayabanerve[m]> Then that outputs a new tree root. We check all proofs specify a valid tree root.`
`[06-28-2023 17:24:27] <kayabanerve[m]> If we re-org, the tree needs to revert, invalidate re-orged out roots, and move on from there.`
`[06-28-2023 17:25:12] <kayabanerve[m]> Ideally, we bind to the tree root in the header (possibly by modifying the TX merkle root to be H(TX merkle root, new tree root)), but that's not necessary. It just makes wallets a bit more secure (as nodes can't provide old tree roots if headers are checked)`
`[06-28-2023 17:25:42] <kayabanerve[m]> The tree itself is a pretty standard merkle tree. I have an impl in Rust to build it, with batched addition. It does need to be DB-backed and support reversions though.`
`[06-28-2023 17:26:34] <kayabanerve[m]> I believe it'd be best to rewrite in C++, the pointers in Rust would be a tad annoying and require being RC'd for safety, but it could go either way.`
`[06-28-2023 17:26:40] <UkoeHB> is your merkle tree hash-based or addition-based?`
`[06-28-2023 17:26:55] <kayabanerve[m]> Hash, yet Pedersen hash.`
`[06-28-2023 17:27:41] <kayabanerve[m]> It isn't Blake2b(elem0, elem1). It's elem0 * G0 + elem1 * G1 + elem2 * G2 + elem3 * G3 for tree width`
`[06-28-2023 17:28:29] <kayabanerve[m]> (instead of each node having 2-children, nodes have a large amount of children for perf reasons)`
`[06-28-2023 17:28:39] <UkoeHB> ok`
`[06-28-2023 17:29:11] <jberman[m]> I can take on implementing the tree in C++ too`
`[06-28-2023 17:29:51] <rbrunner> Looks like you are already booked and busy at least until coming Christmas ...`
`[06-28-2023 17:30:00] <jberman[m]> I'm thinking like Seraphis atm, we could keep everything in memory and first get to constructing and verifying txs all in memory from C++ (interfacing into the rust code). Then move to db work`
`[06-28-2023 17:30:12] <kayabanerve[m]> rbrunner: Would you like to take up the tree? It's only a few hundred lines right now`
`[06-28-2023 17:31:05] <UkoeHB> most of the work is managing merkle tree data flow through the library`
`[06-28-2023 17:31:08] <kayabanerve[m]> We do have a few other developers interested in contributing, and a fully specced out issue board`
`[06-28-2023 17:31:35] <rbrunner> New devs that did not yet work for Monero then?`
`[06-28-2023 17:32:40] <rbrunner> Because this sure starts to sound a bit like "imperial overstretch" to me otherwise ...`
`[06-28-2023 17:32:49] <kayabanerve[m]> (though that doesn't yet cover integration into Monero)`
`[06-28-2023 17:33:50] <kayabanerve[m]> Seraphis can launch without curve trees, solely the curve cycle, as a compromise. I'm not in favor of it, but it's the effective bare minimum and should quash complaints about amount of dev work required.`
`[06-28-2023 17:34:52] <rbrunner> I see. Still this very sexy new work with curve trees, Rust and whatnot seems to have quite a lure.`
`[06-28-2023 17:35:08] <kayabanerve[m]> Though unless curve trees becomes what's blocking Seraphis, I will remain not recommending it. Only once it's shown that Seraphis is held back by CT, and we agree unacceptably long, will I switch. AFAIK, Seraphis itself is in the air on its timeline, lacking academia and auditing. Accordingly... I don't see CT as the issue right now.`
`[06-28-2023 17:35:42] <kayabanerve[m]> (I, of course, expect some delay in moving from Grootle to CT. I just don't think it's years, or a delay worth giving up on launching with CT for. Until we have a quantization showing it is...)`
`[06-28-2023 17:36:59] <UkoeHB> The first milestone is running perf tests in the monero code base for the new proof. After that it will be relatively easy to integrate into seraphis if appropriate.`
`[06-28-2023 17:37:12] <rbrunner> Right now I think in smaller and more immediate terms. jberman is the dev with most experience about the existing Monero codebase right now in the wallet group`
`[06-28-2023 17:37:43] <UkoeHB> And if we don't want to integrate, then there is no 'rewind cost' at that point.`
`[06-28-2023 17:38:50] <UkoeHB> rbrunner: this work is necessary to properly evaluate if seraphis needs to be launched on a new elliptic curve (with or without full-chain proofs at launch)`
`[06-28-2023 17:38:58] <kayabanerve[m]> So immediately, abstracting the curve backend and a C FFI. We also need a proper impl of one of tevador's curve...`
`[06-28-2023 17:38:59] <kayabanerve[m]> s/curve/curves/`
`[06-28-2023 17:39:42] <rbrunner> Like a proof of concept, in a way. Working towards that`
`[06-28-2023 17:39:44] <jberman[m]> Adding to that^ to make the decision that Seraphis should indeed switch to a curve cycle, we'd need the protocol underlying the curve tree work approach fully vetted and understood. So whatever moves us closer toward that direction is the direction to head imo`
`[06-28-2023 17:40:48] <kayabanerve[m]> To be clear`
`[06-28-2023 17:41:11] <kayabanerve[m]> If we do not launch Seraphis with a curve cycle, we will either have to redo the migration, or will permanently have 2x bigger proofs, if not worse.`
`[06-28-2023 17:41:26] <rbrunner> Dev resource allocation will be much fun for years to come :)`
`[06-28-2023 17:41:46] <kayabanerve[m]> tevador has submitted curves with theoretic performance equivalent to Ed25519. I do not understand any proposed future without a curve cycle.`
`[06-28-2023 17:42:15] <kayabanerve[m]> (though to be fair, those 2x bigger proofs would only be under this schema, which is currently the only known one sufficiently performant)`
`[06-28-2023 17:42:44] <kayabanerve[m]> This also ignores all the other benefits of curve cycles which go beyond CT to better fundamental proofs and scaling in general.`
`[06-28-2023 17:43:46] <kayabanerve[m]> If we move to Halo, a discussion for years from now, one reliant on a curve cycle, we could have every proof in a block combined into just one proof at the bottom. Each TX would only be hundreds of bytes on-chain, and verification time would greatly increase.`
`[06-28-2023 17:43:59] <rbrunner> I acknowledge all that, and basically agree. We just can't clone ourselves 5 times to get all the dev capacity that we would ideally need,`
`[06-28-2023 17:44:14] <rbrunner> and that should also go in somewhere into these brainstormings.`
`[06-28-2023 17:44:25] <kayabanerve[m]> I am now officially requesting all devs focus on cloning tech so we can clone ourselves to get all the dev capacity we need /s`
`[06-28-2023 17:44:42] <rbrunner> Yeah :)`
`[06-28-2023 17:44:58] <hyc> just don't forget to turn off the Evil bit in your clones`
`[06-28-2023 17:46:55] <UkoeHB> ok any final comments or topics before we close out the meeting?`
`[06-28-2023 17:48:42] <kayabanerve[m]> I have the path forward I was hoping for :) Thanks`
`[06-28-2023 17:48:47] <sech1> If you want to unleash someone on some unoptimizer C/C++, I could take a look `
`[06-28-2023 17:49:02] <sech1> *unoptimized`
`[06-28-2023 17:51:06] <UkoeHB> I'll call it here, thanks for attending everyone`

# Action History
- Created by: Rucknium | 2023-06-24T22:33:42+00:00
- Closed at: 2023-07-05T00:35:21+00:00
