---
title: Catalogue of Monero decoy selection algorithms
source_url: https://github.com/monero-project/research-lab/issues/99
author: Rucknium
assignees: []
labels: []
created_at: '2022-03-16T17:43:08+00:00'
updated_at: '2022-11-02T23:10:08+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Monero wallet developers are free to choose decoys for ring signatures almost any way they wish. Currently, the "standard" Decoy Selection Algorithm of the official GUI wallet uses a log-gamma distribution with shape parameter 19.28 and scale 1/1.61. To assess the impact of nonstandard Decoy Selection Algorithms on Monero user privacy, it is important to collect information about how wallets are choosing decoys.

Collection of this information is meant to be a collaborative effort. If you know what decoy selection method any of these wallets use, please comment with a link to the code that implements the wallet's Decoy Selection Algorithm. Many wallets will simply incorporate the Monero GUI wallet's Decoy Selection Algorithm. If wallets are not open source, reaching out to the wallet developers would be beneficial. Any leads of nonstandard Decoy Selection Algorithms used by centralized exchanges or other services would also be helpful. I am mostly interested in what wallets have been using over the past two years.


| Wallet | Decoy Selection Algorithm | Source |
| --- | --- | --- | 
| Monero GUI | Standard | [■](https://github.com/monero-project/monero/blob/master/src/wallet/wallet2.cpp) |
| Feather | Standard | [■](https://github.com/feather-wallet/monero/tree/v0.17.2.3_1-feather) | 
| Cake | Standard | [■](https://github.com/cake-tech/cake_wallet/blob/main/cw_monero/ios/Classes/monero_api.cpp#L13) | 
| Monerujo | Standard | [■](https://github.com/m2049r/monero/tree/release-v0.17.3.0-monerujo) | 
| MyMonero | `monero-lws` | [■](https://github.com/monero-project/research-lab/issues/99#issuecomment-1074822142) | 
| Edge | `monero-lws` | [■](https://github.com/monero-project/research-lab/issues/99#issuecomment-1074822142) | 
| Exodus | unknown |  | 
| ZelCore| `monero-lws` | [■](https://github.com/monero-project/research-lab/issues/99#issuecomment-1074822142) | 
| Guarda | unknown |  | 
| Exa | unknown |  | 
| WooKey | unknown |  | 
| Atomic | unknown |  | 




# Discussion History
## tobtoht | 2022-03-16T21:48:19+00:00
Feather Wallet 1.0.1 (current) uses wallet2 (v0.17.2.3).

https://github.com/feather-wallet/monero/tree/v0.17.2.3_1-feather


## SamsungGalaxyPlayer | 2022-03-17T12:50:44+00:00
Cake Wallet and Monero.com use wallet2.

https://github.com/cake-tech/cake_wallet/blob/main/cw_monero/ios/Classes/monero_api.cpp#L13

## m2049r | 2022-03-21T19:22:12+00:00
monerujo uses wallet2 through wallet2_api.h

https://github.com/m2049r/monero/tree/release-v0.17.3.0-monerujo

## devinpearson | 2022-03-22T07:23:11+00:00
For the light wallets listed there, MyMonero, Edge and Zelcore. decoys are selected on the light wallet server. 
All 3 wallets by default use the MyMonero servers and decoy selection is the same algorithm found in monero-lws. https://github.com/vtnerd/monero-lws/blob/develop/src/util/random_outputs.cpp

## Rucknium | 2022-03-22T08:55:29+00:00
@devinpearson Thank you! Do you have a source for the statement that Edge and Zelcore use the monero-lws method? Is it based on your personal communication with the Edge and Zelcore dev teams?

## devinpearson | 2022-03-22T09:02:09+00:00
@Rucknium you can confirm with them but they use our libraries. Which handles the decoy selection as part of the sending process. They would need to run their own light wallet compliant server and modify the libraries  to change this behaviour.

## kayabaNerve | 2022-11-02T23:10:08+00:00
monero-serai uses a Rust implementation of the monero-lws algorithm post-patch to resolve differences with wallet2.

# Action History
- Created by: Rucknium | 2022-03-16T17:43:08+00:00
