---
title: Ring member selection enforcement at consensus level
source_url: https://github.com/monero-project/research-lab/issues/87
author: Gingeropolous
assignees: []
labels: []
created_at: '2021-09-23T18:44:03+00:00'
updated_at: '2023-04-16T20:36:44+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
This is a branch from #86 , it feels like it needs its own thread. 

edited to add, it also seems that #84 discusses this concept as well. 

I can copy and paste some important things from there.

One quick idea is for consensus to at least enforce that the entirety of the ring isn't within the last n blocks. 

# Discussion History
## Gingeropolous | 2021-09-29T00:52:13+00:00
So it seems the primary concern that I've seen voiced about this idea is effectively "what if we get it wrong". So, basically, if we lock in some statistical test that all transactions have to pass (and the associated selection algorithm), and it turns out that test ends up not being great and the picking not being great, it would have to be corrected by a hard fork.

I understand this concern, but I kinda want to explore why this is different than enforcing 1 ringsize. Effectively, Monero decided (yes, referring to developers, community, researchers, etc etc as 1 big old "Monero") that it was better to have uniformity of transactions regarding ringsize than to permit users to choose their own ringsize, even though, technically, a user can achieve better privacy by choosing a ringsize of, say, a bajillion. Yes, the fees would be enormous, and yes, it would be the only tx on the chain with an enormous ringsize, but based on the technical properties of a ring signature, a ringsize a bajillion is better than a ringsize of 11. 

## Gingeropolous | 2021-09-29T01:00:23+00:00
Take this in contrast to today. Today, I could feasibly rewrite (well, I couldn't do it, but the pretend gingeropolous that knows how to code could) the wallet such that when I create a transaction, it pulls the 10 decoys from a 20 output window around my output. Because, for some reason, I feel that my privacy is better protected by fuzzing around my actual transaction. afaik, the blockchain would accept such a transaction. 

why?

## j-berman | 2021-09-29T09:14:58+00:00
I'm for validating ring member selection at consensus and generally agree with all the above @Gingeropolous. Here's my attempt at clarifying the primary pro/con from my perspective.

## Primary PRO

Validating at consensus protects users of older wallets using older decoy selection algorithms that can be fingerprinted relatively easily. These older implementations are out in the wild. There are users who have easier-to-guess-link tx's because there is no validation of ring member distribution at consensus. I can demonstrate it with on-chain tx's, but it's simple enough to understand the idea:

- TX 0: User receives output
- TX 1: User uses old wallet to spend output received in TX 0
- TX 2: User uses old wallet to spend change output from TX 1

Depending on how easy it is to fingerprint the ring's selected distribution, it's pretty easy to make a fairly informed link from TX 2 to TX 1 (i.e. guess deduce that a user spent the change output from TX 1). Some older implementations still in use are very easy to fingerprint, such as the one used in the pre-gamma days. I haven't put numbers on the "relative ease"/% of rings fingerprint-able yet (but I could if it would help).

Extending this, if there is some major change to the decoy selection algorithm in the future again without a change to consensus to enforce the newer distribution, then users of older wallets may again be vulnerable to fingerprinting.

Validating at consensus protects users from leaving fingerprints on chain as a result of the above scenario.

## Primary CON

Tweaks to the decoy selection algorithm require a hard fork. This will inevitably make tweaks to the algorithm more challenging to agree on, and would brick wallets that don't update. Compared to ring size bumps, which should just be a change to a magic number, tweaks to the decoy selection algorithm can be much more involved in theory.

Historically, as I understand it, the cadence of changes to the decoy selection algorithm has been slow (once to twice a year, if that?). However, there are a number of potential changes in the pipeline for consideration at the moment:

1. [Patching integer truncation (and reducing the "recent spent" window)](https://github.com/monero-project/monero/pull/7798#issuecomment-917495021)
2. Binning (with at least 4 implementations on the table in ideation stage still)
3. Modifying the distribution estimator i.e. moving beyond the gamma (with at least 2 paths in ideation stage)

Clearly, there are different ideas for what the optimal decoy selection algorithm could look like today, and there are even ideas to iterate toward stronger solutions with a decently strong understanding of what those iterations would look like. Validating at consensus makes *all* changes more difficult to implement, while there is still a concerted effort toward incrementally building to the ideal algorithm.

## Other Cons

I feel the other cons of added complexity/inefficiency/risk of a floating point corner for validating at consensus are decently well addressed in [#86](https://github.com/monero-project/research-lab/issues/86#issuecomment-921805298). But, happy to continue on that/provide benchmarks/more fleshed out code if this is desired. I think there are more ways to tackle the problem in such a way that minimizes complexity/inefficiency/risk, but I hope that comment serves as a solid enough foundation to show that these issues are tackle-able.

## My opinion

I think the decoy selection algorithm should be enforced at consensus. I think a change to the decoy selection algorithm that leaves older wallets vulnerable is probably *worse* than those wallets being bricked. If taking the perspective that privacy can be a matter of life and death + the fact that seeds can be taken from 1 wallet to another if necessary + the fact that not everyone updates their software unless required, then enforcing at consensus seems like the right move to me. Older implementations *should* have their ring signatures rendered "unusable" on the main chain, since they pose a privacy risk to their users.

## A potential compromise

Simply move [something like this](https://github.com/monero-project/monero/blob/6b824c9ed0e5555d614da9cadbb5bb2dbcd6a724/src/cryptonote_core/tx_sanity_check.cpp#L94-L99), or maybe slightly more robust, into consensus. That line checks that the median ring member is roughly younger than 40% of all outputs (not exact). We could add something that makes sure there are at least 2 outputs in the last 1000 blocks, at least 2 outputs older than the last 100 blocks, etc. I think *something* is better than nothing.

EDIT: tidied up language

## Gingeropolous | 2021-09-29T12:29:43+00:00
> Simply move something like this, or maybe slightly more robust, into consensus. That line checks that the median ring member is roughly younger than 40% of all outputs (not exact). We could add something that makes sure there are at least 2 outputs in the last 1000 blocks, at least 2 outputs older than the last 100 blocks, etc. I think something is better than nothing.

100%. I feel this is a good starting point that is relatively simple that can leave room for future improvements. 

## UkoeHB | 2022-12-13T00:27:59+00:00
My general take on this idea is: A) there is no ideal decoy selection algorithm, B) any heuristics-based algorithm would almost necessitate periodic hard forks to adjust it. Reducing the rate of hard forking is an important goal IMO.

## jtgrassie | 2023-04-16T20:36:44+00:00
Non-deterministic decoy selection is a real problem, and if someone can come up with a reasonably good deterministic selection, it would definitely warrant a fork, IMO.

It's worth remembering that privacy is a constant battle and hence network upgrades (hard forks) are always going to be a necessity. Whenever we can improve fungibility / privacy we should do so (this is established for the project and requires network upgrades). 

# Action History
- Created by: Gingeropolous | 2021-09-23T18:44:03+00:00
