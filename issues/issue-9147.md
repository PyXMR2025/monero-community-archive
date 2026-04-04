---
title: 'Proposal: Reduce size of block hashing blobs for PoW validation'
source_url: https://github.com/monero-project/monero/issues/9147
author: jeffro256
assignees: []
labels:
- important
- proposal
- discussion
created_at: '2024-02-01T06:31:20+00:00'
updated_at: '2024-05-12T03:35:05+00:00'
type: issue
status: closed
closed_at: '2024-05-12T03:34:37+00:00'
---

# Original Description
## Background

As of the time of this writing, PoW is checked by RandomX hashing the resultant blob of [`cryptonote::get_block_hashing_blob()`](https://github.com/monero-project/monero/blob/059028a30a8ae9752338a7897329fe8012a310d5/src/cryptonote_basic/cryptonote_format_utils.cpp#L1446). This blob contains the serialized block header + 32 byte merkle tree hash of all transactions in the block + the number of transactions in the block as a `varint`. The resultant blob of `cryptonote::get_block_hashing_blob()` is also hashed to get the block ID, but using the keccak function for speed.

## Proposal

My proposal is to reduce the size of the blob we hash against for PoW by only adding enough bytes to the blob such that the transaction contents of the block are only "bound" (using the cryptographic term loosely here) with at least as much difficulty as the difficulty of the block. Specifically, for each block, we define a new value `rough_diff_bytes = log256ceil(current_difficulty)`. Then, we get the rough tx tree hash: `rough_tx_tree_hash = randomx(<the tx tree>)[:rough_diff_bytes]`, where `string[:n]` means to take the first `n` bytes of `string`. To construct our PoW hashing blob, we concatenate the serialized block header + `rough_tx_tree_hash`. To validate the contents of a block knowing only the PoW hashing blob chain, we can request blocks by the `prev_id` of the block header immediately after it. For the very top block, since there is no following block, we request the top block from a peer node, recompute `rough_tx_tree_hash' = randomx(<the tx tree>)[:rough_diff_bytes]` and check if `rough_tx_tree_hash' =?= rough_tx_tree_hash` for the very top block.

## Trade-off Analysis

### Pro: Reduce data needed to verify PoW by ~37% (28 bytes/block)

Conservatively, let's assume the highest difficulty ever achieved on the Monero blockchain (420 billion) and a low transaction count (1). With our new scheme, `rough_diff_bytes = log256ceil(current_difficulty) = 5`. So instead of serializing the complete 32 merkle tx tree hash (32 bytes) + the number of txs as a varint (1) byte, we just serialize `rough_tx_tree_hash` (5 bytes), and thus save 28 bytes. The typical block header is 43 bytes, so we would save around 28 / (43 + 32 + 1) * 100% = 36.8% total on each downloaded header hashing blob.

### Con: Extra DB space required to cache `rough_tx_tree_hash` (16 bytes/block)

Assuming we don't want to recalculate `rough_tx_tree_hash` each time it is requested, which would entail running RandomX, we need someplace to store it in the database. Realistically, since we assume the difficulty will never rise above 2^128, we would probably store the `rough_tx_tree_hash` as a LE-encoded 128-bit integer in `mdb_block_info_*`.

### Con: One Extra RandomX Call Required before Mining Can Begin

To compute `rough_tx_tree_hash`, we must call RandomX once before we can begin mining which will increase turnover time 
for miners on new block propagation. However, this is a small cost that affects all miners equally, so the effect probably won't be very noticeable.

### Con: Hard Fork and Extra Code Required

This is obviously incompatible with older consensus rules so a hard fork is required. Also, if nodes are actually going to leverage this feature, we would need implement some way retrieve *just* the block header hashing blobs.

## Synergy with @tevador's Fast Partial PoW Proposal

@tevador proposed using an "intermediate hash" to force malicious attackers to expend PoW (in the form of a Blake2B hash) before nodes will execute RandomX in issue #8827. By leveraging the same principal used here (only serializing the amount of entropy required to be at least as hard as the block difficulty), we can actually reduce the intermediate hash size down from 32 bytes to ~5 bytes. If both of these proposals are combined, we can have block header hashing blobs that are ~23 bytes lighter than they currently are **AND** require Blake2B PoW from attackers before clients will expend effort verifying the RandomX. 

These ultra-quick block headers would be excellent for wallets and nodes alike. Nodes will get to toss away bad blocks from peers quicker, retain higher availability, and settle alternative chains faster. It would now be cheaper for wallets to validate block headers directly from the network so they don't have to trust any single node.



# Discussion History
## hyc | 2024-02-01T15:49:57+00:00
> we can actually reduce the intermediate hash size down from 32 bytes to ~5 bytes

Sounds unrealistic to me, since the hash algorithms' block size is 32 bytes.

## jeffro256 | 2024-02-01T17:15:45+00:00
The hash algorithm would remain unmodified, we would simply only include *X* bytes of the RandomX hash result in the header hashing blob, where *X* is the amount of bytes needed to bind the block contents with at least as much as the current difficulty of the block.

In other words, we are downgrading the strength of the bind from industry-standard 128-bit security level to the strength of the block difficulty. 

## vtnerd | 2024-02-04T22:17:32+00:00
I think @hyc was pointing out that with a block of 32-bytes, there isn't going to be much performance improvement in this suggestion.

## jeffro256 | 2024-02-05T21:55:13+00:00
Yes, there would be 0 CPU performance improvement, but if we only save enough bytes from the intermediate hash to bind the contents of the block stronger than its difficulty (~4-5 bytes as of the time of this writing), then we get to save 27 or 28 bytes per header hashing blob while still retaining spam proofness.  

## jeffro256 | 2024-02-05T21:58:10+00:00
Sorry, I guess I jumped ahead a bit since it wouldn't create the same hashes as the current RandomX proposal, it would require a Blake2B hash of this reduced hash, replacing the extra step where we hash the hash of the dataset, but the original proposal also required a hard fork, so this requirement shouldn't be a big deal IMO. 

## iamamyth | 2024-02-05T23:18:48+00:00
Proposals like this make me very uneasy in terms of cost benefit: The history of secure hash algorithms demonstrates fairly conclusively that you want a wide safety margin because things can and do often go wrong. Tevador's original proposal *expands* the safety margin so I don't really see a case for thinking of the two ideas as a single unit; in particular, there's no need to offset the extra header bytes in tevador's proposal (the proposal should stand on its own, and I didn't see much objection to the extra bytes). Linking the proposals creates a lot of downside: What if one has to be undone? I'd rather not condition "reduce DoS vulnerability" on "slightly reduce network traffic".

## jeffro256 | 2024-02-06T01:08:57+00:00
> The history of secure hash algorithms demonstrates fairly conclusively that you want a wide safety margin because things can and do often go wrong

I would tend to agree, except that this problem isn't related to secure hash algorithms in a traditional sense, it's related to PoW. We don't need collision resistance within a security factor so large that no computer we can conceive of could reasonably find one (i.e. the current 128-bit industry standard level), we only need difficulty that is greater than the block difficulty, which should be trivially provable under the current assumptions we use for PoW consensus rules. 

> Tevador's original proposal expands the safety margin

Wrong. It has 0 effect on the "safety margin". If you're talking about resistance to 51% attacks, if the 256-bit intermediate hash *would* cause any extra difficulty to attackers (i.e. finding a collision with the intermediate hash is harder than remining the RandomX PoW, which it should be), then the attacker would simply just remine the RandomX PoW, since that's easier. In that case, we have exactly the same difficulty to perform 51% attacks as before the changes. What @tevador's proposal protects against is forcing any node on the network to run iterations of RandomX at no cost to the remote attacker.

Now you could have a point that we could multiply the current difficulty by a buffer amount, just to be extra sure our rough intermediate hash has a higher difficulty to fake than the current difficulty of the block. For example, instead of `rough_diff_bytes = log256ceil(current_difficulty)`, we could have `rough_diff_bytes = log256ceil(2^7 * current_difficulty)`. 

## iamamyth | 2024-02-06T14:48:28+00:00
> The history of secure hash algorithms demonstrates fairly conclusively that you want a wide safety margin because things can and do often go wrong
>> I would tend to agree, except that this problem isn't related to secure hash algorithms in a traditional sense, it's related to PoW

Except the problem here *does* relate to certain properties of hash algorithms (specifically, bit independence, pre-image resistance), which have been difficult to conclusively analyze in past algorithms. If you think the relevant properties are "trivially provable", then by all means, prove them; your work will no doubt very much be appreciated the next time standards bodies solicit drafts for hashing algorithms.

> Wrong. It has 0 effect on the "safety margin".

I obviously was not referring to the safety margin of the hashing algorithm (which tevador's proposal didn't impact, as it didn't touch the algorithm), but the network as a whole.

## tevador | 2024-05-08T21:29:38+00:00
> `rough_diff_bytes = log256ceil(current_difficulty)`. Then, we get the rough tx tree hash: `rough_tx_tree_hash = randomx(<the tx tree>)[:rough_diff_bytes]`

It should be noted that this is insecure.

With a 40-bit `rough_tx_tree_hash`, finding a collision would only take about 2<sup>20</sup> RandomX hashes. That's just 1 second for an attacker with 1 MH/s, which is a medium-size miner (or a small pool).

The attack works as follows: The malicious miner will first find two sets of transactions (both including their coinbase reward) that have the same `rough_tx_tree_hash`. They then continue mining as usual. Once they find a block, they have effectively found 2 different blocks. They submit block A to one part of the network and block B to another part of the network. This will cause a temporary chain split and a subsequent reorg, which can be used for double-spending. The cost of this attack is negligible because both blocks A and B contain the miner's coinbase reward and the initial collision search only needed 1M hashes.

This vulnerability can be fixed by setting `rough_tx_tree_hash = randomx(<the tx tree>)[:2*rough_diff_bytes]`, doubling the rough hash size from 40 to 80 bits, which makes finding a collision take the same amount of work as mining a block.

However, even with this modification, I would recommend against this change. The main idea of reducing the download size to verify the PoW chain doesn't work because without the ability to verify the `block_id`, you can't actually verify that the list of hashing blobs forms a valid chain (i.e. the `prev_id` of the next block is correct). This could be abused to insert a fake block in the chain with the effort equal to mining a block with the difficulty of the block following the block you want to replace. The light node would "verify" the PoW chain and then use the fake `prev_id` in the replaced block to download a fake block that actually doesn't exist in the chain.

## jeffro256 | 2024-05-12T03:34:35+00:00
Yes everything you said @tevador is correct; we would have to double the size of the buffer to prevent collision attacks. Along with @SChernykh's point that since the hashing blobs overlap for block IDs and PoW, such that `prev_id` can be implied when sent as a compressed chain, I think this issue should be closed. Thanks everyone for the discussion. 

# Action History
- Created by: jeffro256 | 2024-02-01T06:31:20+00:00
- Closed at: 2024-05-12T03:34:37+00:00
