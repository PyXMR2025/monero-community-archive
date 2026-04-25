---
title: Increased FCMP++ membership proof size, marginally slower 1-input verification
  time
source_url: https://github.com/seraphis-migration/monero/issues/317
author: j-berman
assignees: []
labels: []
created_at: '2026-04-14T15:11:24+00:00'
updated_at: '2026-04-23T00:13:27+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
As a result of [the latest changes implementing Cypher Stack's proposed fix to GBP's](https://github.com/monero-oxide/monero-oxide/commit/8ff1f904bf5018e3be22bbf3da4e186ac2d09e41), FCMP++ tx sizes increased ~17%, and verification times are marginally slower (needs further testing for a completely accurate comparison). See the benchmark results below.

@kayabaNerve notes that there are 2 potential alternative routes to fix the issue Cypher Stack raised:

1) Sample H generators as a challenge.
    - This would leave membership proof sizes untouched from the prior level, but would potentially increase verification times a significant degree. As such, this route is likely unusable.

2) Use an additional BP+ proof.
    - This would leave the membership proof untouched from the prior, but would compose it with an additional BP+ proof (likely up to +2x ~1kb for each Helios and Selene, +verification times likely comparable to batch verification of an additional large range proof).

The latter route appears compelling, however, it would be expected to add at least 2 months to the FCMP++ timeline, would require further back and forth with Cypher Stack/researchers and additional vetting, and adds protocol complexity. We could explore the 2nd alternative route as an additional follow-up hardfork, like the upgrade of BP -> BP+.

Of note, [research into folding many proofs](https://libera.monerologs.net/monero-research-lab/20260401#c665166-c665172) is moving in a positive direction, which if successful, would enable full nodes to prune many membership proofs and replace with a single folded proof. Folding may not be feasibly retroactive, i.e. it may only be feasibly applicable to membership proofs created after the folding scheme is implemented and introduced. @kayabaNerve notes that it may be theoretically possible to fold retroactive proofs, however, it's expected it may be orders of magnitude smaller to have the FCMP itself support folding and fold that directly, and as such, more practical to implement a folding scheme that is not retroactive.

I'm opening this issue to highlight the changes.

## Results

CPU: AMD Ryzen 7950X3D

### New benchmarks with changes applied

Inputs | Outputs | Tx Size (bytes) | Verify (ms) | Membership Proof Size (bytes) | Membership Proof Verify (ms)
|--:|--:|--:|--:|--:|--:|
1 | 2 | 7638 | 37 | 6208 | 31
2 | 2 | 9081 | 57 | 7104 | 50
4 | 2 | 11839 | 95 | 8768 | 87
8 | 2 | 17228 | 171 | 11968 | 162
16 | 2 | 27876 | 326 | 18240 | 314
32 | 2 | 49044 | 657 | 30656 | 644
64 | 2 | 91252 | 1472 | 55360 | 1428
128 | 2 | 175541 | 3264 | 104640 | 3190

### Old benchmarks

Inputs | Outputs | Tx Size (bytes) | Verify (ms) | Membership Proof Size (bytes) | Membership Proof Verify (ms)
|--:|--:|--:|--:|--:|--:|
1 | 2 | 6486 | 35 | 5056 | 28
2 | 2 | 7865 | 56 | 5888 | 48
4 | 2 | 10239 | 93 | 7168 | 84
8 | 2 | 14859 | 167 | 9600 | 154
16 | 2 | 23972 | 337 | 14336 | 308
32 | 2 | 42068 | 640 | 23680 | 613
64 | 2 | 78132 | 1370 | 42240 | 1294
128 | 2 | 150133 | 2960 | 79232 | 2878

### Changes going from Old to New

Inputs | Outputs | Tx Size (bytes) | Verify (ms) | Membership Proof Size (bytes) | Membership Proof Verify (ms)
|--:|--:|--:|--:|--:|--:|
1 | 2 | +18% | +6% | +23% | +11%
2 | 2 | +15% | +2% | +21% | +4%
4 | 2 | +16% | +2% | +22% | +4%
8 | 2 | +16% | +2% | +25% | +5%
16 | 2 | +16% | -3% | +27% | +2%
32 | 2 | +17% | +3% | +29% | +5%
64 | 2 | +17% | +7% | +31% | +10%
128 | 2 | +17% | +10% | +32% | +11%

Source for New benchmarks: (not publicly available yet, will post)
Source for Old benchmarks: https://github.com/j-berman/monero/blob/f94a3989c440efac8339ad7fae3ed935b2b8bc09/tests/unit_tests/fcmp_pp.cpp#L1175

# Discussion History
## tevador | 2026-04-14T16:46:39+00:00
> however, it would be expected to add at least 2 months to the FCMP++ timeline

FWIW, I think the new transaction sizes are acceptable (2/2 is still smaller than RingCT before bulletproofs) and I would prefer not to delay the the FCMP++ hard fork any longer than necessary. An optimization can be rolled out later.

## ACK-J | 2026-04-14T17:20:21+00:00
There is BP+ optimization research in the works, which will hopefully offset some of these increases.
https://donate.magicgrants.org/monero/projects/2026-range-proofs-speedup

## kayabaNerve | 2026-04-14T19:17:29+00:00
I don't believe it'd immediately be directly relevant. The issue with the GBPs as they were is that the commitments could contain terms not used by honest provers but usable by dishonest provers. CS's solution was to double a layout such that these terms may still be present but aren't effective. The two solutions I propose attempt to make it computationally infeasible to have such terms in the first place, allowing preserving the existing layout code.

For the second proposal, composition with a BP+, that'd solely be composing with the BP+ IPA to effect a logarithmic PoK for the opening of the commitment, for which the generators for the BP+ could be solely the generators we expect coefficients to be bound with. That means it'd avoid the overhead of the arithmetic circuit, range proofs which converge into an IPA, solely being the IPA itself. That means, on paper, it'd be even cheaper than a range proof, except for how this would be a much larger IPA than we see effected with Monero's range proofs. While improvements to range proofs may be great, I wouldn't expect those improvements to take the form of a more efficient IPA protocol, the only part used here.

## ArticMine | 2026-04-22T04:55:00+00:00
Updated the scaling definitions to increase TR to 12500 bytes as discussed in https://github.com/monero-project/meta/issues/1371

https://github.com/ArticMine/Monero-Documents/blob/master/MoneroScaling2026-03.odt
https://github.com/ArticMine/Monero-Documents/blob/master/MoneroScaling2026-03.pdf

# Action History
- Created by: j-berman | 2026-04-14T15:11:24+00:00
