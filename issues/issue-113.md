---
title: Porting Utreexo to Monero
source_url: https://github.com/monero-project/research-lab/issues/113
author: jbird186
assignees: []
labels: []
created_at: '2024-01-02T20:17:15+00:00'
updated_at: '2024-04-01T17:00:25+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
[Utreexo](https://github.com/mit-dci/utreexo) allows pruned Bitcoin nodes to be run off of just a few kilobytes of state, rather than gigabytes. The savings with this would be even more extreme on Monero, considering that pruned nodes currently can "only" discard less than 70% of blockchain data.

Since Monero does not reveal which enotes are spent, there would need to be two separate proofs, 1) a non-inclusion proof that the key images do not exist on-chain, and 2) an inclusion proof that the referenced decoys exist on-chain. 

Number 1 should be simple by using a sparse merkle tree or similar, with proof sizes of a couple kilobytes or less per transaction, on average.

Number 2, however, would potentially require proofs on the order of tens of kilobytes for each transaction, even with optimizations from merging separate proofs. Possible, but not very useful. The need for this proof would be eliminated if FCMPs (#100) were to implemented, however, since decoys would be replaced by a small root anyway. Much larger proofs would still be needed for transactions spending old RingCT outputs, but those will quite quickly become rare after Seraphis activates.

I think it's worth exploring the possibility of porting Utreexo (Enote + tree = "Enotree"?) to Monero if FCMPs are included with Seraphis. This would allow users to trade marginally higher bandwidth usage, maybe even 50% or less, for >99.9% lower storage usage. Depending on the implementation, this could also allow light wallet users to easily verify the last N blocks without needing any form of a node, rather than solely relying on PoW.

Somewhat related to #69 and #111.

# Discussion History
## jbird186 | 2024-03-31T04:54:25+00:00
@kayabaNerve I'm starting to look into this concept, and I have a question regarding your FCMP implementation.

If I understand correctly, the state of the enote set could be represented as a sort of merkle root, since that is what the proofs will be checked against, correct? If so, what amount of data is needed to append new enotes to the set (that is, to update the root)?

I would _think_ that you wouldn't need access to the full enote set. Since in a normal merkle tree, optimizations aside, a merkle proof suffices to insert a new leaf, I would hope that the FCMP root would be the same. Unless my understanding of your work is completely off.

Thanks, and sorry to bother you :)

## kayabaNerve | 2024-03-31T09:23:21+00:00
You cannot insert into a Merkle tree with a Merkle tree proof. You need the list of right-most branches. That comment holds here.

Mind if I ask what the interest is for this? Utreexo doesn't reduce the requirements of running a node. It introduces a new class of node which can validate new transactions *when spoonfed the relevant pieces of data from actual nodes* (increasing bandwidth notably). While the argument for Utreexo is the replacement of the blockchain state with an accumulator to better service wallets, this accumulator wouldn't be usable to create TXs under Monero. You'd still need the full blockchain state.

If you have the full blockchain state, you don't need the accumulator to verify old TXs.

Accordingly, this seems completely pointless.

## kayabaNerve | 2024-03-31T09:27:12+00:00
If the goal is solely pruning the blockchain history, then #110 would solve this for the future and the history could be replaced by a meta-proof as well (as proposed for Bitcoin by... ZeroSync?).

## jbird186 | 2024-03-31T16:46:13+00:00
I was being general by saying you need a merkle proof to insert new leaves. In this case, you would have an inclusion proof of the rightmost leaf, allowing you to recompute the rightmost "wall" of the tree. Or, and this is what I was hoping could be done instead, it can be optimized in the style of Utreexo where the client can cache only the rightmost leaves and not need external proofs for adding new outputs. So it sounds like the FCMP tree can be treated as a normal merkle tree?

Utreexo has about 10-15% bandwidth overhead with good caching, and I would hope to get "Enotree" down to at least 25-30% with FCMPs. I don't think your assessment of Utreexo is accurate, since by that standard, Bitcoin pruned nodes also seem to be "spoonfed the relevant pieces of data from actual nodes."

As for the interest, I think effectively eliminating the storage requirement can make a strong argument for this in certain use cases. Here are some that come to mind.

- Fully verifying recent blocks for light wallet users, significantly improving upon the security of SPV clients
- Fully verifying blocks on storage- or I/O-constrained hardware
- Transfer state between devices - for example, do IBD on a desktop computer and use a QR code to transfer the state to a cellphone

## kayabaNerve | 2024-04-01T11:14:29+00:00
The proof for the right-most leaf is a poor indirection for the right-most leaves. It just lets you recalculate them.

Yes, FCMPs are a standard merkle tree.

Bitcoin pruned nodes do not need active spoonfeeding. They maintain the full state, unless Bitcoin pruning has radically diverged from my concept of pruned nodes. They simply don't have the blockchain history and can't be synced from. Utreexo nodes, with each new block, need the relevant pieces of state given to them (with proofs) to avoid even keeping the state around.

With Monero, such a design would also work to avoid keeping the state, except it'd be unusable to service wallets. Wallets *must* be serviced by a node with state. Accordingly, a pruned node does have state, doesn't have the blockchain history, can verify new blocks (without overhead and spoonfeeding), and can service wallets.

Light wallet users should be willing to carry state around if they also want to fully verify blocks IMO. Full verification is extremely computationally expensive (Borromean signatures :vomiting_face:) and state is theoretically just a few hundred MB by my estimate? I personally think it's a really weird device to posit where it can't store a few hundred MB of state, yet does have the computational power to reasonably verify Monero. I do concede such devices do exist however. Why they'd want to be used is a distinct question.

I also do know you specified "recent blocks", but I don't personally think the age of the block should make a difference. Once the claimed TX is at a specific confirmation depth on the best chain, the only additional assumption you make by not verifying the block is that the TX is correct. I'd find it weird to have two confirmation depths, one for assume correct, one for accept payment without assuming correct. If they're the same, no actual benefit is offered.

> Transfer state between devices

You can already do that and then just verify blocks normally. The whole point of Utreexo is so you don't keep/have the state. If you're transferring a state snapshot, and are willing to store the state snapshot, you can verify as a pruned node (pruned as in theory, not as in Monero which has some specific pruning configurations).

Though of course, my opinions on the matter don't prevent, and shouldn't if you still believe in, your work. Happy to answer questions re: FCMPs :)

## jbird186 | 2024-04-01T16:32:50+00:00
My point with pruned nodes is that the way they're given a new block is fundamentally the same as when Utreexo nodes are given a new block, albeit Utreexo needs the proofs. They can both propagate the new block to their peers, but as you said, do not maintain history. I think of the proofs as analogous to SegWit witness data, just not on the consensus-level. Utreexo being the "SegWit nodes" and the rest of the network being "non-SegWit nodes". A pruned node can be queried for the UTXO set, true, but its response cannot necessarily be trusted.

If a post-FCMP node only needs the merkle root and key images for full verification of new Seraphis transactions, then yes, that would probably only take up _at most_ a couple gigabytes. The bigger problem would be verifying then-old RingCT transactions, which would require access to dozens of times more state. The Enotree proofs for these would be large, but would become rare enough (like pre-RCT spends are today) to not be a huge deal. Maybe it would be better to store key images locally, and only rely on Enotree for transactions spending RingCT enotes.

(How many key images have been spent at this point? I would think it would be at least a gigabyte or two's worth)

The goal for this would be to act as a sort of SPV+ client that doesn't blindly trust PoW as much as normal SPV clients. The best chain is by definition the longest _valid_ chain, so SPV clients are _giving up_ this verification, not the other way around. A miner who's lucky or quickly rents more hashpower can easily fool SPV clients, but would find it significantly harder to fool "SPV+" clients. The SPV+ client could check the most recent say 50 or 100 or 200 etc blocks, to have more confidence in the chain tip's validity. Additionally, if it sees a long chainsplit between the attacker and the honest network, it can go back to the fork height and identify which chain is valid.

Thank you for answering my silly questions :)

## kayabaNerve | 2024-04-01T17:00:23+00:00
Those "proofs" are the spoonfeeding I'm referring to. It's trading state storage for bandwidth + additional external work, which of course is its point.

I would not at all call this analogous to SegWit. Non-SegWit nodes can verify new blocks without the SegWit data (as their consensus rules are to follow the best chain, with the unrecognized opcode meaning the TX is valid). They accordingly don't need any additional data. Even if they did have the additional data sent to them, they'd just ignore it.

Under RingCT, the blockchain state can be summarized as the output keys, commitments, and key images. For the current ~90m outputs on-chain (under RingCT, I'm ignoring the cryptonote pools) that's 90,000,000 * 32 * 3 bytes, or ~8.7 GB. If we had that output set under Seraphis, it'd only be * 2 under Grootle (as the output keys and commitments would be squashed). With FCMPs, it's * 1, with the logarithmically sized tree edge.

# Action History
- Created by: jbird186 | 2024-01-02T20:17:15+00:00
