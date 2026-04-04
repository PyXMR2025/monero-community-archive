---
title: Add scripting to Monero via the specification of R1CS circuits
source_url: https://github.com/monero-project/research-lab/issues/116
author: kayabaNerve
assignees: []
labels: []
created_at: '2024-01-18T18:00:40+00:00'
updated_at: '2024-04-29T03:45:49+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I'll start by saying I don't support this, due to the privacy (and performance) concerns around it.

If Monero outputs specified an R1CS program, an opaque collection of numbers, then outputs could only be spent given a sufficient ZK proof that all conditions are specified. If Monero was to change the ZK proof it used to evaluate the R1CS, all prior outputs would remain spendable. It's only that we couldn't move to a proof which doesn't support R1CS (or whatever circuit description chosen). This would enable Bulletproofs/Bulletproofs+/Bulletproofs++/Halo/Nova/more now, yet prevent us from accessing the Plonk family without a converter (which probably could be trivially done, albeit inefficiently).

This would enable ZK rollups on Monero, not bind us to a proof within Monero, and support complex wallet descriptors.

# Discussion History
## chaserene | 2024-01-20T12:49:15+00:00
how opaque is an R1CS program? is it transparent enough for an outside observer to infer something about the content of the program?

would this mean all enotes would be R1CS programs, or only the ones with scripting?

I see layer 2's, especially rollups (and obviously I prefer ZK to optimistic), as a very important future direction for Monero. however, I also hold that they are acceptable only if the required changes on layer 1 don't meaningfully reduce the privacy of layer 1 transactions, or there are no changes required at all. (I conjecture that's possible, but that's a separate conversation.)

## kayabaNerve | 2024-01-20T23:54:19+00:00
It's a series of scalars. You'd be able to see the expected mathematical relations of the proof without issue.

Evaluating what those mathematical relations do is a much more difficult problem, yet not one inherently private.

Your question about if all enotes would use this is partially left to the privacy discussion. Due to the computational load of proof production/verification, ideally no, standard enotes wouldn't be R1CS specified.

## chaserene | 2024-01-26T01:07:16+00:00
I would then side with you that this is a no-go in terms of privacy at minimum, but potentially also in terms of performance.

## kayabaNerve | 2024-01-26T03:02:04+00:00
I don't believe the privacy of the program is an issue in the slightest.

Yes, the programs would be transparent. The arguments they're evaluated with would be ZK, and the programs can be written such that they show *which* program they are yet *not* how they're configured.

The concern is that any output using a program is outside of the privacy pool. While that may be an inevitability with scaling (any scaling solution would use a distinct privacy pool), it's not one I care to answer today.

## chaserene | 2024-01-30T01:14:41+00:00
I see: so the script would be transparent, but what it's used for would be private, and who uses it would be somewhat-private (limited by the privacy of the graph of the transaction rings, unless full-chain membership proofs are achieved).

> any scaling solution would use a distinct privacy pool

not if it were built with scriptless scripts, i.e. using the signature algorithm's algebraic property to essentially execute programs with it.

Andrew Poelstra formalized this and has shown that it works with Schnorr signatures, of which Monero's EdDSA is a variant. there are a couple of papers that describe how payment channel(network)s can be built on such a foundation.

it's a longer shot for rollup validation because the scriptless scripts known/developed so far aren't expressive enough, and it's an underresearched area, but something like this would be very much in line with Monero's focus on privacy.

## kayabaNerve | 2024-01-30T03:05:55+00:00
1) Monero doesn't use EdDSA.
2) Any scaling solution having a distinct privacy pool holds true. Within a payment channel, your counterparty is a known, consistent entity. If a rollup of a series of TXs were to be executed, the privacy of TXs would be dependent on the rollup (non-existent, or its own privacy solution) distinct from the Monero base layer. Scriptless scripts hide a program is being executed, it doesn't offer the program the same privacy properties as the underlying network.
3) We presumably can have programs revealed at time of spent and the output embedding the program be hidden via a FCMP.

## kayabaNerve | 2024-01-31T00:11:39+00:00
This was discussed in Zcash 7y ago.

https://github.com/zcash/zcash/issues/2425

Due to their use of Groth16, they would've had a fixed program length (which is opaque), fixed verification time, and they achieved randomization so you can't distinguish between a Sapling proof and between a full program proof (achieving full privacy on the L1).

They didn't move forward with it as the tooling was no where near at a matching level. With the context of now, it'd have allowed full ZK rollups, including EVMs, yet over the underlying blockchain.

While I can't propose Groth16 here, as achieving the same guarantees would require a Monero circuit program premised on Groth16, it does point to the end goal use case and question about modern SNARKs which achieve similar enough properties (based on pairing curves/class groups/the discrete log problem). Unfortunately, the current discussion of moving to a curve cycle isn't directly amenable with currently known techniques, and I'm unsure an evolution of such 'perfection' is possible without a trusted setup.

## chaserene | 2024-02-01T01:43:16+00:00
1. indeed it doesn't use EdDSA. I seriously misunderstood something about the current proving scheme. now I read up on scriptless efforts that may be compatible with CLSAG and [found](https://eprint.iacr.org/2022/744) some [hints](https://eprint.iacr.org/2020/1441) that the [algebraic](https://ieeexplore.ieee.org/abstract/document/10371398) properties are [there](https://eprint.iacr.org/2020/1613).
2. I used "privacy pool" in the sense whether the related enotes created on L1 form a separate pool from regular enotes. executing a scriptless script that e.g. opens a payment channel or validates a rollup proof wouldn't leave a trace on the L1 that distinguishes that transaction from regular ones. I view whatever an L2 counterparty needs to know/publish/etc as (ephemeral) side-channel information, and the transaction model they use as a detail that the L1's scripting capability should not concern itself with. (the latter is presuming that R1CS circuits are expressive enough for general computation, which I understand [they are](https://learn.0xparc.org/materials/circom/additional-learning-resources/r1cs%20explainer/#context-what-is-r1cs-and-how-does-it-fit-in).)
3. interesting. FCMP seems to improve a lot on the viability of this in terms of privacy. do I understand correctly that, in this scheme, a script enote would be initially created from regular one(s) (basically pop out of nowhere), and transactions spending from that script would have the constrained anonymity set of every previous enote that spent from the same script? and once *those* enotes are spent, they are back in the regular anonymity set?
4. any guess about the order-of-magnitude costs of an R1CS enote (size, verification time), presuming the best available proof system?

## kayabaNerve | 2024-02-02T06:12:03+00:00
1. While CLSAGs presumably can have adaptor signatures performed over them, it's still fundamentally a minor detail over the discussion here.
2. It's not about you personally, so please do not take it personally, yet I have no interest in spending the several hours of effort to discuss and explain this literalized at this time. While your questions are the right questions to open this discussion and move this forward, I do not believe the end result is within the feasibility of Monero for multiple years so I don't personally care to invest so much time right now.

## kayabaNerve | 2024-02-16T04:44:31+00:00
https://gist.github.com/kayabaNerve/7336bf7d95176deaa9c2807690e8c47e

I did end up spending multiple hours literalizing this for distinct reasons. Given those distinct reasons have run their life, I post this now here.

## amano-kenji | 2024-04-28T16:09:14+00:00
If you are trying to save storage space, this cannot be just pruned.

## kayabaNerve | 2024-04-28T23:13:47+00:00
Mind providing more context?

The outputs would not increase in size under the ZeroExec proposal, and the input proofs would be as prunable as our current input proofs. For the data layer, we could inherit behavior from Ethereum and only guarantee data publication and availability for a limited time (as done by its blob space).

This also reduces on-chain load by enabling L2s.

I'm not inherently sure what your commentary on pruning then is.

## amano-kenji | 2024-04-29T03:05:48+00:00
I don't know details. I was just stating my perspective as a beginner.

> availability for a limited time

That's good. If it had to be available for ever, no pruning is possible.

## kayabaNerve | 2024-04-29T03:45:48+00:00
If you don't know details, please don't make statements ("this cannot be just pruned") yet ask questions ("how does this impact pruning?").

# Action History
- Created by: kayabaNerve | 2024-01-18T18:00:40+00:00
