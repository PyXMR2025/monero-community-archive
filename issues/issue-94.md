---
title: Open Research Questions
source_url: https://github.com/monero-project/research-lab/issues/94
author: Rucknium
assignees: []
labels: []
created_at: '2021-11-18T20:25:24+00:00'
updated_at: '2025-06-23T18:53:28+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
This is an effort to construct a list of open research question relevant to Monero, as discussed in a [recent MRL meeting](https://github.com/monero-project/meta/issues/627). The purpose of this list is to:

1. Prioritize MRL efforts
2. Inform external researchers of key Monero questions
3. Maybe serve as a basis for Request For Proposal-style grantmaking in the future

This effort was in part inspired by a [similar list put together by Grin](https://grin.mw/open-research-problems).

Cat = Category. The categories are Privacy, Scaling, Decentralization, and User experience.
Imp = Impact, a subjective 1-10 measure of how important resolving the question is for Monero's goals.
Dif = Difficulty, a subjective 1-10 measure of how difficult resolving the question may be.

A collection of Monero-related research papers is available at [MoneroResearch.info](https://moneroresearch.info/).

This list is a work in progress. Please give feedback below, including additional questions that should be added.


| Question | Cat | Imp | Dif | Work in Progress | Links |
| --- | --- | --- | --- | --- | --- |
| Increase ring size | P,S | 8   | 8   | Seraphis; Triptych |  #91; #92   |
| Decoy selection algorithm (DSA) that closely matches the real spend age distribution | P   | 8   | 6   | OSPEAD; Dynamic; Nonparametric |   #93; #86  |
| Advisability and feasibility of enforcement of DSA at the node and/or consensus level | P,D | 6   | 4   |     |  #87   |
| Advisability and implementation of binning for the DSA | P   | 6   | 4   | @j-berman 's implementation | #84; #88 |
| Decoy selection when transitioning transaction types | P   | 6   | 5   | | [■](https://github.com/monero-project/research-lab/issues/94#issuecomment-1098385712) |
| Advisability of churning and churning best practices | P,S,U | 7   | 5   |     |     |
| Defend against the Overseer Attack | P   | 7   | 9   |     | [■](https://www.zfnd.org/blog/blockchain-privacy/#overseer) |
| Defend against the Flashlight/Poisoned Outputs/EAE/EABE Attack | P   | 7   | 9   |     | [■](https://www.zfnd.org/blog/blockchain-privacy/#flashlight); [■](https://www.monerooutreach.org/breaking-monero/poisoned-outputs.html); [■](https://github.com/monero-project/monero/issues/1673#issuecomment-312968452) |
| Defend against the Tainted Dust Attack | P   | 7   | 9   |     | [■](https://www.zfnd.org/blog/blockchain-privacy/#dust) |
| Cross-ring output collisions: implications and solutions | P   | 2   | 3   |     | [■](https://github.com/monero-project/monero/pull/8047) |
| Faster syncing of non-custodial wallets | S,U | 7   | 8   | View Tags | #73; [■](https://github.com/monero-project/monero/pull/8061) |
| Reducing or eliminating 10 block lock with acceptable drawbacks | S,U | 9   | 7   |     | #85; #95; #102; [■](https://github.com/monero-project/monero/issues/5810); [■](https://raw.githubusercontent.com/noncesense-research-lab/lock_time_framework/master/writeup/lock_time_framework.pdf) |
| Increase mining decentralization | S,D | 7   | 7   | [p2pool](https://github.com/SChernykh/p2pool); [SolOptXMR](https://ccs.getmonero.org/proposals/soloptxmr-mj-endor-2022.html) |     |
| Determine if miners increasing block size is incentive-compatible from a game theory perspective | S,D | 5   | 6   | |   [■](https://academic.oup.com/restud/article/88/6/3011/6169547);  [■](https://www.ndss-symposium.org/ndss-paper/squirrl-automating-attack-analysis-on-blockchain-incentive-mechanisms-with-deep-reinforcement-learning/);  [■](https://link.springer.com/chapter/10.1007/978-3-662-54970-4_30); [■](https://www.sciencedirect.com/science/article/pii/S2405959522000443)   |
| Payment channels | S,U | 6   | 7   |  [Grease](https://github.com/grease-xmr/grease)   | [■](https://eprint.iacr.org/2022/117); [■](https://eprint.iacr.org/2021/1445); [■](https://eprint.iacr.org/2020/1441); [■](https://eprint.iacr.org/2022/744); [■](https://ieeexplore.ieee.org/abstract/document/10371398)   |
| Layer 2 solutions | P,S,D,U | 8   | 9   |     |     |
| Atomic swaps with every coin ever | D,U | 8   | 8   | BTC; [ETH](https://github.com/noot/atomic-swap); [BCH](https://bitcoincashresearch.org/t/monero-bch-atomic-swaps/545) |  [■](https://eprint.iacr.org/2020/1126); [■](https://arxiv.org/abs/2101.12332); [■](https://eprint.iacr.org/2022/1650); [■](https://eprint.iacr.org/2021/1612); [■](https://arxiv.org/abs/2211.13335)  |
| Pruning of spent outputs | S,D | 7   | 8   |  |   #69 https://github.com/zcash/zcash/issues/4946  |
| Private, untraceable transactions without ring signatures, but with acceptable tradeoffs | P   | 10  | 10  |  [FCMP](https://web.getmonero.org/2024/04/27/fcmps.html)   |  [■](https://eprint.iacr.org/2020/499); #100  |
| Post-quantum Security & Privacy | P   | 9  | 10  |     |  [■](https://eprint.iacr.org/2020/499); [■](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/142#note_10181); [■](https://gist.github.com/tevador/23a84444df2419dd658cba804bf57f1a); #105  |


# Discussion History
## LocalMonero | 2022-01-04T01:13:28+00:00
@Rucknium can we bump the importance of the 10-block-lock problem up to 9? The inability to spend unconfirmed coins is a massive pain point in Monero for a large number of reasons, ranging from basic consumer needs like buying two cups off coffee in the span of less than 20 minutes to enterprise applications like multisignature non-custodial service optimizations, so it seems more important than layer 2 solutions or swaps.

## Rucknium | 2022-01-04T01:20:24+00:00
@LocalMonero Sure. Done.

## ChristopherKing42 | 2022-01-11T15:24:23+00:00
Suggestion: use polling to estimate user experience impact. Although for the other categories I think the Monero research lab are the experts, user experience is more subjective. For example, polling could be advertised on Reddit, on IRC, or even in popular wallets. It would be completely optional, of course. As part of the polling, we could also ask how heavy of a Monero user someone is, how tech savvy they are, etc... to see how it correlates to the questions.

## ChristopherKing42 | 2022-01-11T20:09:19+00:00
@LocalMonero 

> for a large number of reasons, ranging from basic consumer needs like buying two cups off coffee in the span of less than 20 minutes to enterprise applications like multisignature non-custodial service optimizations, so it seems more important than layer 2 solutions or swaps.

I don't understand. It seems that layer 2 solutions would also solve that and any other problems caused by the 10 block limit, so it would be strictly less impactful.

## endorxmr | 2022-04-03T14:58:25+00:00
A followup question related to the DSA: what are (if any) the side-effects of hardforks/changes in the transaction protocol on the DSA, both in the short term (the initial transactions happening right after a fork) and in the long term (a very old output being upgraded to a newer format)?

## Rucknium | 2022-04-13T18:48:45+00:00
@endorxmr : If the transaction format changes completely, like it will with Seraphis, then yes there are tricky issues around decoy selection. I'm not sure of all the details, but yes there will be a discontinuity and yes we will have to figure out how to deal with it so as to maximally protect user privacy. @UkoeHB , could you clarify this point?


## UkoeHB | 2022-04-13T19:03:59+00:00
@Rucknium After the hardfork, new transactions spending new outputs will only be able to use new outputs as ring members. 'Transition' transactions will spend old outputs and create new outputs. Those txs will only use old outputs for ring members.

## UkoeHB | 2022-04-18T16:44:53+00:00
@Rucknium Another information leak is 'when a tx is constructed'. This has two vectors: decoy selection (solvable with seraphis where you can defer making membership proofs until right before tx submission), fee granularity (see [this analysis](https://github.com/Mitchellpkt/fees_data_and_design/blob/main/monero_fee_analysis.ipynb); mitigate-able by discretizing fees).

Fees can also lead to [tx fingerprinting](https://www.youtube.com/watch?v=XIrqyxU3k5Q), which is also mitigated with discretization.

## HardenedSteel | 2023-02-27T12:47:17+00:00
Should we add these to the roadmap page?

## chaserene | 2023-05-04T00:48:22+00:00
@Rucknium inspired by the latest MRL meeting, could you add "Post-quantum cryptography"? and here's a would-be (to-be?) MRL paper as related resource:

[Corbo, Krawiec-Thayer, Goodell: Evaluating cryptocurrency security and privacy in a post-quantum world](https://raw.githubusercontent.com/insight-decentralized-consensus-lab/post-quantum-monero/master/writeups/technical_note.pdf)

and what do you think about renaming "Private, untraceable transactions without ring signatures, but with acceptable tradeoffs" to "Global anonymity set with acceptable tradeoffs"? IMHO it describes the goal better.

and a resource for payment channels:

[Sui, Liu, Yu, Qin: MoNet: A Fast Payment Channel Network for Scriptless Cryptocurrency Monero](https://eprint.iacr.org/2022/744)

## chaserene | 2023-05-04T01:57:32+00:00
also this merge request to the post-quantum MRL paper's CCS, and especially this comment:

https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/142#note_10181

**edit**: and these as well:

[koe: Implementing Seraphis (section 8.7, Forward secrecy against DLP-solver)](https://github.com/UkoeHB/Seraphis/tree/master/implementing_seraphis) (obviously the section may change in the future because the paper is a draft as of now)

[tevador: Zero-cost post-quantum mitigations for Seraphis](https://gist.github.com/tevador/23a84444df2419dd658cba804bf57f1a)

**edit2**:

[tevador: Consider Switch commitments for future supply security (#105)](https://github.com/monero-project/research-lab/issues/105)

# Action History
- Created by: Rucknium | 2021-11-18T20:25:24+00:00
