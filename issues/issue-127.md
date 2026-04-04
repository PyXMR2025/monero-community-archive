---
title: A faster alternative for blockchain consensus
source_url: https://github.com/monero-project/research-lab/issues/127
author: SapphireSpire
assignees: []
labels: []
created_at: '2024-11-07T21:03:22+00:00'
updated_at: '2024-11-26T17:02:17+00:00'
type: issue
status: closed
closed_at: '2024-11-26T17:02:17+00:00'
---

# Original Description
Work is applied to a block hash so that it's highly unlikely to produce a valid hash if it's modified. But this forces work to be done after the block is created, resulting in painfully long delays. The goal is to do the work before a block is created, without leaving the block subject to modification.

Miners create tickets for the opportunity to create a block. A ticket contains the miner's pubkey, a pubkey hash, a nonce, and a payment address. Tickets are added to a ticket pool as they are published. Miners work to improve the difficulty of their pubkey hashes until they meet the minimum difficulty. Every block must have a unique pubkey, so pubkeys can't be reused.

Every block header contains a top ten list of tickets containing the most difficult hashes, and the following block may only be validated by one of these tickets. All of the owners of these tickets are encouraged to create a block for the next position, in case the owners of all the better tickets fail to do so. The one with the best hash counts.

A block's list validates the pubkey of the following block, and everything in the header is included in the signature, which only the miner can produce. Would this not secure the block as well as a block hash with POW?

# Discussion History
## kayabaNerve | 2024-11-21T07:43:05+00:00
It doesn't result in long delays. It isn't 2 minutes to mine a block once you have the template. It's a successfully rolled die to mine a block once you have the template. The 2 minutes is the average time for someone to successfully roll a die since the last time someone did. If a miner makes a new template, they can immediately start rolling dice for it without distinct odds of success (and therefore no delay) than if they continued with the prior template.

Your idea also risks a liveness failure without complicated best-block selection logic which would be a mess. I don't feel a need to go into a detailed pros and cons however given this idea's proposed benefit is inaccurate.

# Action History
- Created by: SapphireSpire | 2024-11-07T21:03:22+00:00
- Closed at: 2024-11-26T17:02:17+00:00
