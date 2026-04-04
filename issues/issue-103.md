---
title: Remove the burning bug as a class of attack with a modified shared key definition
source_url: https://github.com/monero-project/research-lab/issues/103
author: kayabaNerve
assignees: []
labels: []
created_at: '2022-05-19T23:32:08+00:00'
updated_at: '2022-05-20T23:06:42+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Currently, shared keys are defined as `Hs(8raG || o)`, with output keys being defined as `shared_key G + B`. By reusing a `r` value, it is possible to create multiple outputs with the same output key, and therefore the same key image, effectively burning the funds. Wallets must maintain a contextual state accordingly of all one time keys they have ever seen, and if any are shared, prioritize the higher value one.

Not only does this complicate wallets, it also makes higher level protocols (which operate with their own wallet) more complicated, and increases requirements on them in order to be secure.

In order to solve this on the protocol level, shared keys must contain an element which is guaranteed to only be usable once. By including the transaction's first key image, we offer that guarantee, and make it impossible to legitimately generate the same output key multiple times on a single chain. For miner transactions, which do not have key images, the proposed unique element is the previous block's hash. With Seraphis, the unique element would be the linkability tag.

The new formulation would accordingly be: `Hs(unique_element || 8raG || o)` (with the caveat Seraphis doesn't include `o` already and still would not).

Wallets, when scanning an individual TX, must also now receive this unique element. This adds 32 bytes to a minimal representation and should not change security parameters for light wallets. Whereas they could already be lied to about Rs, unless they do a merkle proof up to the block header, they can now also be lied to about key images, unless they do a merkle proof up to the block header. Scanning miner transactions with SPV proofs now must also grab the block header, for the previous block hash, which they already do (as it's SPV).

Since this is not feasible to include in the upcoming hard fork, as I'm unfortunately only now considering the problem, this would be for the hard fork after. If the hard fork after is Seraphis, this turns this into a Seraphis design discussion instead of a fork change discussion. This is incompatible with the suggested TX construction flow established under 4.8 of the current Seraphis paper, and better solutions may be available for it specifically.

Having discussed this with koe, his initial suggestion regarding Seraphis was two-fold.

1) Output keys in transactions remain `K_i = Hs(8raG)G + B`, yet output keys are saved as `K_i + Hs({R, K, C}_0, .., {R, K, C}_n, extra)G`. This guarantees for a given set of one time keys, recipients, amounts, and extra, unique enotes will be generated. It does not alone prevent someone from sending the same amount of funds to the same amount of people multiple times, still requiring full context as an isolate.

2) Monero enforces unique output keys as saved to disk. This cannot currently be done with K alone, as it'd enable people sending 1 Moneroj in advance of an agreed upon K, burning it and DoSing a protocol. With the offset  binding C, this is locked to specific amounts, preventing such DoSs. A similar scheme could also be applied to RingCT.

I was against this as TXs having one K yet saving another seemed frustrating, yet as long as the RPC offers both (or the original K in the calculated offset, which would be more valuable)... it's *fine*. The reason my suggestion was not koe's preference was it breaks down the modularity Seraphis offers, and would prevent isolated enotes/collaborative TX building. I proposed a workaround for the latter (creating a multisig, presigning escape routes, then funding until it's ready at which point the protocol would achieve its collaboration), which was accepted.

I personally prefer koe's suggestion for Seraphis, as it maintains modularity and can remove context when paired with a protocol enforcement of unique K values, yet don't prefer it when discussing RingCT which doesn't have this modularity. koe currently prefers the linkability tag based solution for Seraphis, as it drops the most convoluted parts of Seraphis which already offer minimal benefit while simultaneously being a dead simple, complete solution.

Regarding feasibility, my proposed solution can be done completely by wallets so long as they agree on criteria on when to use it (BP+ usage, a flag in extra, Seraphis...). Currently, entire Monero TXs can be done as a 2-round multisig protocol, and that's unchanged with this suggested edit (if a seeded RNG variant of BPs is available). The reason I use that criteria to judge the impact of this is due to the complexities with a group protocol, on how/when data is created, so acknowledging it doesn't increase communication rounds signifies it's not overtly breaking to flow. Unfortunately, I am unable to comment on the current wallet2 codebase, though koe believes, while requiring notable refactoring, this does simplify Seraphis.

The latter solution is completely outside of transaction handling, solely affecting node's saving to disk and calculating the key spent with, and is the most trivial to implement regarding wallets.

It should be noted this fixes a griefing attack against any exchange/protocol which receives funds to a singular address they publish with a view key, distinguishing users by data encoded in extra (so either legacy integrated addresses with published view keys or a custom design, one of which I'm currently working on). The view key enables crafting matching, successfully decodeable, outputs. The attacker will receive X and the actual user will receive Y - X according to the Monero wallet daemon, if the attacker can ensure their TX is included in the block first. This leads to the attacker only paying marginal TX fees while actual users burn funds, without meaning to, and get credited less funds (or nothing) accordingly. When partnered with a miner with sufficient hash power, it'd be possible to only successfully burn some of the time yet never lose money attempting to burn.

Said custom protocols may be able to adopt this change locally, without affecting the Monero protocol as a whole, and then the legacy integrated address case should be dismissable. This does mean this should not be an immediate priority for Monero, while remaining a valuable long term discussion. Custom protocols may alternatively include a Schnorr proof of knowledge of `r` in extra, signing over the first used key image to prevent reuse, therefore NOT modifying internal definitions of shared keys/masks while still preventing this from being a possible grief.

# Discussion History
## kayabaNerve | 2022-05-20T01:46:23+00:00
To provide a more specific specification, with mild differences from the above:

Shared secret transcripts are to be prefixed with `uniqueness`, an element guaranteed to be unique for a given chain by the Monero protocol. This value is calculated based on an initial value `u`. The initial value for miner transactions is the height specified in their sole inputs encoded as a VarInt. For regular transactions, the initial value is `{KI}`, being the key images of the transaction with these outputs, in their sorted form. 

`uniqueness = H("domain_separator" || u)`

## UkoeHB | 2022-05-20T23:04:14+00:00
Without a fix for this issue, payment validators must maintain a full record of transactions received to their main wallet. Moreover, any 'tx engineering' protocol such as multisig, atomic swaps, etc., must take into account the possibility of this issue cropping up. The issue also implies the possibility of race conditions around tx submission. All of this adds up to a violation of the principle of least astonishment.

While the issue has never really affected Monero users (just like the Janus attack, as far as anyone knows), it is better to find a solution for the sake of protocol health and robustness. As far as Seraphis goes, the cost to fix it (by baking input context into the sender-receiver secret, e.g. key images for normal txs or block height for coinbase txs) would be easy collaborative funding (collaborative funding would still be possible I think, but would require more rounds of communication, closer to the TxTangle protocol discussed in ZtM2; complex enough that I won't try to support it any more with my Seraphis wallet PoC), and isolated enotes. The former is mostly a 'nice-to-have', while the latter has only hypothetical benefits (no known off-chain protocol could use it, moreover any such protocol would need to deal with this issue - perhaps making the protocol infeasible anyway). Tx chaining, the primary new 'tx engineering' feature of Seraphis, would not be affected.


# Action History
- Created by: kayabaNerve | 2022-05-19T23:32:08+00:00
