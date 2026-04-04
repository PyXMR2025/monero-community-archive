---
title: Proving transactions is incomplete for a specific adversary
source_url: https://github.com/monero-project/research-lab/issues/153
author: kayabaNerve
assignees: []
labels: []
created_at: '2025-11-24T17:54:28+00:00'
updated_at: '2025-11-27T05:42:20+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
For a wallet with one output to spend and an adversary who:

- Knows the wallet's view key
- Is allowed to decide the outputs of a transaction

The adversary may choose outputs whose commitments' masks sum to the spent output's commitment's mask. Due to Monero's balance proof not being zero-knowledge, this will force the pseudo-out to have a re-randomization of 0, which will cause CLSAG's D to equal the identity, which will be rejected by the protocol.

The simplest solution is simply to sample ephemeral randomness as necessary, deriving a distinct set of outputs, for which a collision is negligible. The chance of this occurring with normal operation is absurd and can be dismissed as irrelevant. This is reachable when handed _already-derived_ outputs however.

The best fix would be to use a properly zero-knowledge balance proof, but this doesn't actually improve amount privacy as knowing the outputs (and fee) and all but one input still allows learning the remaining input's amount.


# Discussion History
## kayabaNerve | 2025-11-24T20:17:38+00:00
Re-sampling ephemeral randomness only helps if a destination has a non-identity view key.

In the edge case all destinations have the identity as a view key, there are fifteen possible sum of the outputs' commitments' masks in today's Monero. For an honestly-scanned output to have one of those as its mask is of negligible probability, so it's fine.

## UkoeHB | 2025-11-25T01:17:07+00:00
> The adversary may choose outputs whose commitments' masks sum to the spent output's commitment's mask. Due to Monero's balance proof not being zero-knowledge, this will force the pseudo-out to have a re-randomization of 0, which will cause CLSAG's D to equal the identity, which will be rejected by the protocol.

Can you point out the code line where identity is rejected? I don't off the top of my head recall this being a problem.

## kayabaNerve | 2025-11-25T04:34:30+00:00
https://github.com/monero-project/monero/blob/bba6aa518ba4533859766672cf996f6427b8f1a4/src/ringct/rctSigs.cpp#L897-L898

## UkoeHB | 2025-11-26T22:03:44+00:00
Got it, thanks

## UkoeHB | 2025-11-26T22:20:57+00:00
> The adversary may choose outputs whose commitments' masks sum to the spent output's commitment's mask. Due to Monero's balance proof not being zero-knowledge, this will force the pseudo-out to have a re-randomization of 0, which will cause CLSAG's D to equal the identity, which will be rejected by the protocol.

Took me a bit to refresh. Output commitment masks are pseudo-random, see ZtM2 section 5.3. There is a negligible probability they could choose random outputs that would equal the input. They *could*, however, send the input amount to the same output onetime address (assuming the original was at the same index, and assuming no change output is needed). This would burn the funds, but the tx constructor would panic at the assert you linked before you got that far.

The best solution is to not allow the output-specifier to specify the tx privkey.

## kayabaNerve | 2025-11-26T23:55:04+00:00
Agreed in practice.

To reiterate a theoretical however, an adversary who is only allowed to specify addresses may specify addresses whose view keys are the identity point so the choice of transaction key is irrelevant. That'll force the sum of the outputs to one of fifteen values, corresponding to the fifteen possible choices of the amount of outputs for non-miner transactions today.

That edge case is negligible so long as the sender follows the defined scan process however, which will uniformly distribute the spent output's mask, which has a negligible chance of colliding with those fifteen values. It's only if the sender was given an already-scanned output, fully derived to arbitrary values, that this would be reachable.

This produces the bounds:
- Sender performs the scan procedure
- Sender samples the transaction keys

## UkoeHB | 2025-11-27T05:12:52+00:00
> To reiterate a theoretical however, an adversary who is only allowed to specify addresses may specify addresses whose view keys are the identity point so the choice of transaction key is irrelevant. That'll force the sum of the outputs to one of fifteen values, corresponding to the fifteen possible choices of the amount of outputs for non-miner transactions today.

With the additional restriction that there can be no change output, because the change address would need to be provided by the tx constructor and validated as part of the output set (for any modestly secure framework). And if there is a validation step it begs the question why wouldn't the other output addresses be validated (a naive design might fail to do this, yes), and more generally whether a failure at any step matters (including a panic in tx construction - the bigger problem here being error propagation for UX).

So for bounds:

- Sender performs the scan procedure and selects tx inputs from scanned outputs
  - OR Sender requires there be a change output, even if zero amount, and validates the change address in the final output set.
  - OR Sender validates that output addresses are not in the small order group.
- Sender samples the transaction keys


## kayabaNerve | 2025-11-27T05:23:51+00:00
I'd consider the change output address equivalent to any output address in this discussion. Else, we need the bound the change address has a non-small-order view key (collapsing it to the bound on other outputs' addresses) as the specific criteria for "validates", a statistically-likely side effect of honest sampling.

But yes. This is specific and contrived.

# Action History
- Created by: kayabaNerve | 2025-11-24T17:54:28+00:00
