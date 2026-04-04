---
title: Scale the blockchain with recursive ZK proofs
source_url: https://github.com/monero-project/research-lab/issues/110
author: kayabaNerve
assignees: []
labels: []
created_at: '2023-06-26T19:52:52+00:00'
updated_at: '2023-12-05T14:01:47+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Ideally, the block producer removes all of the range proofs in a block for a single ZK-proof asserting that all commitments in a block had valid range proofs. While we could accomplish this with a pairing curve, curve cycles also have known SNARKs which would allow this. Notably, the Halo proof enables recursive proof composition.

This isn't limited to range proofs, as ideally membership proofs are also so removed. That would notably decrease the on-chain size of full chain membership proofs (a concern being raised in response to #100).

While this is likely a research issue which won't be closed for years, if desirable, then it's important to ensure Seraphis is minimally binding to its proofs. We can go as far as saying the Seraphis TX hash, included in blocks, should solely be the key images and output keys/commitments (the fundamental state transition). Else, we'll have to make such changes at time of actioning this issue, which would require redoing analysis and create yet another TX definition.

If this is done successfully, we could even post-recursive-prove the entire historical Seraphis section of the chain. Unfortunately, this is unlikely since recursively verified proofs require a sublinear proof and expect the embedded proofs to be amenable to such proving. All currently discussed proofs for Seraphis, if Seraphis moves to a curve cycle, would be native to a future sublinear proof (using known techniques), yet none inherently support recursive proving.

# Discussion History
## plowsof | 2023-09-20T19:10:52+00:00
A bounty (albeit vague in its current form) has been created for research in this area https://bounties.monero.social/posts/95 

## kayabaNerve | 2023-12-05T14:01:46+00:00
We actually don't need a recursive proof, nor to burden miners as such.

If we have a pool of 1000 active proofs, someone about to send a transaction can randomly select one. They then produce two sets of TX proofs. One independent, one folded into the existing proof. This lets miners publish the folded proof *without increasing the state size, as we can prune the old proof* OR if it comes into conflict with another transaction (another TX decides to fold into the same proof), they can grow the state as they publish the independent proof.

This doesn't have as clean a path to recursive proofs though. Instead of recursively proving a list of proofs, we'd be recursively proving a list of proofs each of which are already the result of a list of statements which were proven. We'd likely want to:
1) Have archive nodes which archive all independent proofs (likely not feasible)
2) Bound folding depth to a low number such as 8. That way, we'd recursively prove proofs which are 8-folded (and any proofs not yet 8-folded would be artificially padded)

# Action History
- Created by: kayabaNerve | 2023-06-26T19:52:52+00:00
