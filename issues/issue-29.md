---
title: MRL To-Do list/roadmap for 2018/2019
source_url: https://github.com/monero-project/research-lab/issues/29
author: b-g-goodell
assignees: []
labels: []
created_at: '2018-05-22T16:03:46+00:00'
updated_at: '2018-10-02T03:45:43+00:00'
type: issue
status: closed
closed_at: '2018-10-02T03:45:43+00:00'
---

# Original Description
This issue to discuss the MRL roadmap as discussed in our meeting on 21 May 2018 (meeting notes can be seen [here](https://github.com/b-g-goodell/research-lab/tree/master/meta/research-meeting-logs)). We hope that the community can help us discuss, amend and modify the following as needed.

1. Technical notes and documentation: We intend on completing some discussions of the following and publishing technical notes on the results of those discussions. Presented in no particular order:
      - ~~Bulletproof Fee Model~~.
      - ~~Multisignatures~~: Recent papers have come out regarding musig's security proofs, so we are reviewing our current material for correctness before seeking publication. See [here](https://eprint.iacr.org/2018/774).
      - Refund transactions/~~dual output addresses~~ (see [here](https://github.com/SarangNoether/research-lab/tree/master/publications/bulletins/in-prog/MRL-XXXX-dlsag)) for payment channel infrastructure (see below).
      - Churn and heuristic linkability, see [here](https://github.com/monero-project/monero/issues/4229#issuecomment-415152036) for a partial discussion, see [here](https://github.com/b-g-goodell/research-lab/wiki/Ring-Signature-Linkability-and-Bipartite-Graphs) for another partial discussion.
      - ~~"Zero to Monero"~~, see [here](https://getmonero.org/library/Zero-to-Monero-1-0-0.pdf) for the current version and for the RingCT report that inspired the expanded version above, see [here](https://github.com/kurtmagnus/Monero-RCT-report)
      - Monero Standards.
      - ~~Curve optimizations and the importance of verification times in cryptocurrency~~ Update: @SarangNoether  and @moneromooo-monero have been killing it with group operation optimizations. We are seeing >= 90% improvement in speed over OpenSSL, and we are removing dependencies on third party libraries as a consequence
      - Failure model effects and analysis: What happens if our PRNG is totally screwed, for example?
      - Time-space trade-offs in cryptocurrency networks and modifying notions of "efficiency" to take verification time into account.



2. Off-chain improvements: We are looking into requisite payment channel infrastructure for Monero. We have also become aware of some advances that enable the following "new technology" investigations at MRL.
      - Improving Monero's privacy by increasing ring sizes and using more efficient ring signatures is not a great long-term approach: sublinear ring signature schemes still take a linear amount of time to verify and often come with bigger keys, so there is a trade-off in space and time. One of the most important areas of investigation at MRL right now involves improvements to signer-ambiguous authentication that will have a net positive effect on the total time to download-and-sync for new nodes.
      - Defining needs for payment channel infrastructure. We need to get a grip on "all that is necessary" to develop lightning-like payment channels. Work on this includes both multisignatures (see above) and refund addresses (see below). Discussions have begun regarding computations in different groups for different currencies, see [here](https://www.reddit.com/r/Monero/comments/89rw7u/any_update_from_the_monero_devs_on_whether_or_not/).
      - Scaling with payment channel infrastructure.
      - Privacy with merge-mined sidechains. We are looking into a model of Monero that allows sidechains with ZCash's ZK-SNARKs. This may allow for improved privacy without sacrificing the approaches used in Monero that do not require a trusted set-up.

3. Literature reviews: This is an always-happening sort of thing, as Sarang and I read more papers, we are going to include short summaries of each and eventually just publish these notes.
      - ~~Multisignature schemes, common pitfalls, recent advancements in multisignature unforgeability proofs.~~ This is included in the "related works" section of the new multisig paper (see above)
      - ZK proofs.
      - Arithmetic circuits.
      - Construction of elliptic curves.
      - Stateless hash-based signatures (esp ring signatures)
      - Large-anon set authentication

3. Libraries for general use: Call this "research infrastructure." It's a lot easier to look into churn if we can easily measure statistics from the Monero blockchain, and it's wiser to model an attack, a PoW change, or a novel consensus mechanism like SPECTRE with a simulation than doing it live. 
      - Transaction graph statistics and visualization: We have some contributors working on a blockchain analysis tool that is optimized for analyzing ring-signature-TXO-based cryptocurrencies. This will be used in our churn analysis above, as well as general privacy investigations.
      - Network simulations: We are working on some code for simulating network evolution over time, both in terms of nodes as well as block propagation. We will be able to use these to test algorithmic changes, or to investigate how population ecology interacts with economic incentives in blockchains. See [here](https://github.com/b-g-goodell/research-lab/tree/master/source-code/Poisson-Graphs).
      - Collision-resistant address visualization for easy checking receiving addresses are correct. See [here](https://github.com/b-g-goodell/research-lab/tree/master/source-code/iseeseashells) for some seashell examples.


# Discussion History
## SarangNoether | 2018-05-23T14:14:57+00:00
I'm finalizing a technical note on a signature scheme that could be used for non-interactive refund transactions, a component of the payment channel infrastructure.

## b-g-goodell | 2018-05-23T14:20:09+00:00
I am also finishing up reading on multisig. High priority.

## b-g-goodell | 2018-05-23T17:38:16+00:00
One question that was brought up once upon a time to me by @fluffypony is a network-activity-dependent  time series model for transaction fees so that we can avoid hard-coding magic numbers for fees when the technology evolves and as exchange rates evolve over time.

## b-g-goodell | 2018-05-28T15:46:06+00:00
Added time-space tradeoff technical note. The idea is to quantify the trade-off between space of a cryptographic scheme with respect to the verification time of that scheme; this leads to a practical trade-off comparison between security and speed/efficiency, a way of learning network characteristics required to support primitives with sufficiently large security parameters. Thing is: many crypto papers talk about the efficiency of their schemes... while they always discuss space requirements and comparisons, they sometimes avoid initial computation time comparisons and almost always avoid verification time comparisons. In our application, verification time is our bottleneck. Want to describe how "efficient" schemes described in the literature can be terribly bad in our set-up.

## b-g-goodell | 2018-08-26T16:34:23+00:00
Finished multisig (link [here](https://eprint.iacr.org/2018/774)), updated the roadmap. I used strikethrough for things that have been accomplished since I last checked this list:
- Bulletproof fee model has been finished, although we have not written up a technical report on this yet. Long story short, transaction "weights" since adding bulletproofs are asymptotically linear in the number of outputs; sticking with the strictly linear terms is sufficient for a large range in "number of outputs," but this needs to be explained and derived in a technical note.
 - Multi-signatures are waiting on an IACR link.
 - Zero to Monero was published on getmonero.org
 - @SarangNoether and @moneromooo-monero have been absolutely murdering our computation times.
 - Bulletproof audit reports are back, some recommended changes are being made, and the results will be published soon(tm)?
 - The dual-output signature scheme first described by Pedro Moreno-Sanchez at Saarlang University and modified/expanded with @SarangNoether combined with the multi-signature scheme will allow for spender-ambiguous cross-chain atomic swaps of confidential assets, which is the next paper MRL is going to push out the door for publication.

## b-g-goodell | 2018-08-28T17:06:34+00:00
https://eprint.iacr.org/2018/774

## b-g-goodell | 2018-10-02T03:45:43+00:00
I'm closing this issue because I have split each individual road map item up into its own issue, so that project-ifying all this is a bit easier, and contributors other than @SarangNoether and I have some place to begin. See issues 32 through 43.

# Action History
- Created by: b-g-goodell | 2018-05-22T16:03:46+00:00
- Closed at: 2018-10-02T03:45:43+00:00
