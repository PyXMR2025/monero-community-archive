---
title: Archiving historic nullifiers with mutator sets
source_url: https://github.com/monero-project/research-lab/issues/111
author: narodnik
assignees: []
labels: []
created_at: '2023-10-17T08:12:48+00:00'
updated_at: '2023-11-03T13:31:00+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
With #100, then Monero now has an infinitely growing nullifier set.

However it's possible to put a bound on this using merkle trees. Basically all coins belong to a large batch, call this index k. When spending the coin, we create an unlinkable nullifier and also reveal the batch index k.

All nullifiers for previous windows except the current active one are put in a merkle tree (a merkle mountain range to be precise). When spending, we have to show our nullifier isn't in the batch. An efficient way of doing this is using bloom filters instead of just storing the ordered nullifiers in the tree.

Then anyone else with coins in that batch, will update their set of nullifiers (the bloom filter) with the newly added nullifier. Users without coins in that batch don't need to keep track of those nullifiers.

This decreases privacy since the batch k that a nullifier belongs to is public, but the batch can be sufficiently large enough that it still provides practical strong anonymity while ensuring the nullifier set isn't unbounded. For example a batch could be for 2 years worth of coins.

[Mutator Sets and their Application to Scalable Privacy](https://eprint.iacr.org/2023/1208) by Alan Szepieniec .et al

# Discussion History
## kayabaNerve | 2023-11-03T13:31:00+00:00
To start, Monero already has an infinitely growing set of nullifiers/linking tags/key images.

I am against ever segregating Monero's privacy set, along with making old outputs unspendable (not proposed here, yet another potential 'solution')

One possibility may be the following:

1) We define a sparse merkle tree (or bloom filter, if that actually would work here which I'd have to check) to store the last year's linking tags
2) We define a list of all the SMT roots
3) Users prove their linking tag isn't present in *any* of the SMTs

This reduces node's storage of the set of linking tags (which is part of the state and not prunable) to the last year's worth. This does require wallets to create *several* proofs (which could be folded with an IVC like Nova to effectively be one proof) *and* have access to a node with the full set still in state to get the necessary proving data.

I don't believe this is a worthwhile trade-off, as I'm not personally too concerned about this state growth aspect, yet it's good to start accumulating ideas and noting options.

# Action History
- Created by: narodnik | 2023-10-17T08:12:48+00:00
