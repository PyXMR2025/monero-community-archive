---
title: 'discussion: remove output blackballing'
source_url: https://github.com/monero-project/monero/issues/8756
author: tobtoht
assignees: []
labels:
- discussion
created_at: '2023-03-03T00:30:44+00:00'
updated_at: '2024-02-28T13:59:37+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
#### Context

From https://monero-blackball.github.io/monero-blackball-site/

> This tool can be used to avoid including outputs that are known to be spent in other transactions. If you exclude these known-spent outputs, other higher-quality outputs can be included in your ring signatures, thus improving your privacy.

Once imported, blackballed outputs are stored in the shared ringdb.

#### Why remove blackballing?

Output blackballing has been "unnecessary" for over 4 years: https://old.reddit.com/r/Monero/comments/9rml9j/generating_and_importing_an_output_spent/

> This is a quick PSA to say that generating and importing a spent output (blackball) list is unnecessary with Monero's new, larger ringsize. It was also unnecessary with Monero's ringsize 7.

Removing output blackballing would eliminate ~2.2k lines of code (https://github.com/tobtoht/monero/commit/906f9c840d7f968a91dd296133962c225ee02a86), remove `monero-blockhain-mark-spent-outputs` (9.6 MB) from release archives, and slightly simplify decoy selection code. It is also one less thing to worry about during the seraphis transition.

# Discussion History
## SamsungGalaxyPlayer | 2023-03-03T01:00:43+00:00
This was a really interesting project at the time, but I have to agree. There's no expected future for this, and no further support is needed.

## Gingeropolous | 2023-03-17T11:37:44+00:00
output blackballing might still be useful if the chain gets filled with nfts

## Gingeropolous | 2023-08-26T16:40:57+00:00
so should this issue be closed?

## selsta | 2023-08-26T17:02:02+00:00
It has been removed from the GUI but not yet from the CLI. I would keep it open until there is consensus on if we should remove it or keep it.

## Rucknium | 2024-02-28T13:59:36+00:00
Vijayakumaran (2023) notes bugs when using the blackball tool with forked blockchains:

> The Monero reference implementation includes a tool for identifying spent outputs using the techniques described above [6]. It implements the cascade attack, finds transactions which cause the ring attack characterized by Wijaya et al. [22], attempts to identify closed sets, and performs the cross-chain analysis proposed by Wijaya et al. [24] and Hinteregger et al. [13]. It is included in every Monero release as an executable with the name monero- blockchain-mark-spent-outputs. It is informally called the “blackball tool” in the Monero community as the set of spent outputs represent a blacklist which should be avoided when sampling mixins. To perform cross-chain analysis, the tool takes the LMDB database files of all chains as input.

> We noticed two issues with the Monero blackball tool with regard to cross-chain analysis. Firstly, the tool is not able to read the LMDB database of MoneroV [3] due to a discrepancy in the transaction formats in the main Monero code and the MoneroV code. This discrepancy did not affect our analysis as we used the JSON-RPC interface of the MoneroV client [3] to extract the transaction data. Secondly, and more seriously, the tool only uses an integer index to uniquely identify an output across chains and not the output public key.

> Outputs in a single Monero chain are partitioned by their amounts (with RingCT outputs having dummy amount zero) and are assigned increasing indices in the order of their appearance on the chain. This means that outputs which appear in two different chains after a fork can have the same index even though they have different public keys. Consequently, the cross-chain analysis performed by the blackball tool has errors. To be fair, the tool outputs error messages during its execution when it encounters disjoint transaction rings for the same key image. The presence of code for generating these error messages suggests that the blackball tool developers are aware of this issue. To avoid such errors, we used the public keys of the outputs as their unique identifier in our cross-chain analysis.

Vijayakumaran's code may have a fix: https://github.com/avras/cryptonote-analysis

Reference:

Vijayakumaran, S. (2023), "Analysis of CryptoNote transaction graphs using the Dulmage-Mendelsohn decomposition." Paper presented at 5th Conference on Advances in Financial Technologies (AFT 2023).  https://eprint.iacr.org/2021/760

# Action History
- Created by: tobtoht | 2023-03-03T00:30:44+00:00
