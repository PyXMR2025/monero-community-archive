---
title: Lucky transactions (51% attack mitigation)
source_url: https://github.com/monero-project/research-lab/issues/145
author: tevador
assignees: []
labels: []
created_at: '2025-09-14T22:24:32+00:00'
updated_at: '2025-09-24T09:07:12+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
This is another proposal to bolster chain security against 51% attacks. I'm not very convinced that this should be implemented, but I think it can be discussed as an alternative to the finality layer proposal.

A finality layer marks blocks as finalized. Such blocks can never be replaced, they are cemented in the chain forever. It's the ultimate protection from 51% attacks.

However, this comes at a cost. Finality layers must be Byzantine fault tolerant (BFT), so they need a complex P2P protocol. An attacker controlling at least 1/3 of the stake can stall the finality layer or cause a permanent chain split (i.e. two parts of the network will finalize different blocks).

The following table shows the properties of some of the proposed soft-forking mitigation strategies:

| Strategy | stops 51% attack | stops selfish mining | can stall/split | impl. complexity | decentralized |
|---------------------|-----------------------|-----------|-----------|------|----|
| [DNS checkpoints](https://github.com/monero-project/monero/issues/10064) | Yes | No\* | Yes | Low | No |
| [PoS finality layer](https://github.com/monero-project/research-lab/issues/135) | Yes |  No\* | Yes | High | Yes |
| [Publish or Perish](https://github.com/monero-project/research-lab/issues/144) | No | Yes | No | Medium | Yes |
| **Lucky transactions** | Yes\*\* | No\* | No | Medium | Yes |

\* Cannot stop reorgs of depth  1.

\*\* With assumptions (see the Security section below).

## Lucky transactions

Intuitively, given two alternative chains, the "correct" chain should be the one where the majority of the economic value takes place.

However, "economic value" cannot be defined simply as the transaction volume because miners can create their own fake transactions at virtually no cost.

Instead, we define "economic value" in terms of "lucky transactions", which cannot be easily spoofed.

Assuming `H(...)` is a hash function and `||` is the concatenation operator, a transaction spending an output created at height `input_height` with a key image `key_image` and amount `amount` is "lucky" if:

``` 
H(checkpoint_hash || key_image) < target * amount * (checkpoint_height - input_height)
```
(Eqn. 1) 

Here `checkpoint_hash` is the hash of a recent block with a height of `checkpoint_height` and `target` is a dynamically adjusted value so that the blockchain contains on average 1 lucky transaction per block. 

The above formula basically says that a transaction has a higher chance of being "lucky" if it spends an old output or an output with a high amount.

The minimum relay fee doesn't apply to lucky transactions.

### Verification

If a transaction is lucky, the sender includes a special field in tx_extra that contains:

1. The index of the lucky input.
2. `checkpoint_hash` and `checkpoint_height`
3. `amount` and `blinding_factor` of the input pseudo-commitment.

This is only about 80 bytes of data.

Before selecting the decoys, the sender calculates:

```
anchor_height = checkpoint_height - H(checkpoint_hash || key_image) / (target * amount)
```
(Eqn. 2)

Ring members are selected from heights below `anchor_height`. Note that by Eqn. 1, `anchor_height > input_height`, so the ring can always include the lucky input.

To verify that a transaction included in the blockchain at height `height` is lucky, any chain observer does the following:

1. Check that `height - checkpoint_height <= K`, where `K` is a parameter (the maximum checkpoint age).
2. Check that the `checkpoint_hash` matches the block at height `checkpoint_height`.
3. Check that `H(checkpoint_hash || key_image) < target * amount * (checkpoint_height - newest_ring_member_height)`.
4. Check that `input_commitment = amount * H + blinding_factor * G`.

### Fork choice

A new chain weight formula is used for the fork choice rule that replaces the "longest chain" rule. A block at height `height` has the following weight:

```
block_weight = (included_lucky_diff + current_lucky_diff / M) * pow_diff
```
(Eqn. 3)

Here `included_lucky_diff` is the sum of the difficulties of the valid lucky transactions included in the block, `current_lucky_diff` is the difficulty of a lucky transaction at `height` (calculated using the difficulty adjustment formula), `pow_diff` is the standard Proof of Work difficulty at `height` and `M` is a parameter.

Eqn. 3 basically says that a chain with lucky transactions has approximately (M+1)-times higher weight than the same chain without lucky transactions.

The canonical chain is the chain with the highest total weight.

### Incentives

Miners have an incentive to include lucky transactions because they increase the weight of their blocks.

Users have an incentive to submit lucky transactions because they can be sent with a zero fee, they take priority over all non-lucky transactions and reduce the chance of their transaction being invalidated by a fork.

Lucky transactions can be "mined" by checking Eqn. 1 for each of the user's unspent outputs everytime a new block is published. However, there is no reward for that. It can be done altrustically to support the chain, as the cost is nearly zero (just a couple of hashes). Wallets could have an option to mine lucky transactions in the background.

### Privacy

A lucky transaction leaks the amount spent in one of the inputs and also leaks the minimum age of the input. However, the identity of the spent input is still protected with a ring signature.

### Security

With the recommended parameters of `K = 3` and `M = 3`, lucky transactions can commit to one of the previous 3 blocks and a block without lucky transactions has about 1/4 of the weight of a block with 1 lucky transaction.

The new fork choice rule makes 51% attacks harder under the assumption that the majority of lucky transactions come from honest users.

The table below lists the required combinations of lucky transactions and hashrate as a percentage of the total to attack the chain. An attacker without any lucky transactions would need >80% of the network hashrate to overtake the honest chain (this applies to relatively short reorgs where the difficulty adjustment can be ignored).

| Lucky transactions | Hashrate needed |
|--------------------|-----------------|
|       0%           |  >80%           |
|      33%           |  >60%           |
|      50%           |  >50%           |
|      67%           |  >40%           |
|     100%           |  >20%           |


# Discussion History
## kayabaNerve | 2025-09-14T23:14:46+00:00
At ~3 TPS, isn't this proposing that every second, we get `3 * hashes_per_transaction` in a secondary PoW algorithm? Wouldn't that be trivial for a hostile actor to independently replicate? If a user was willing to perform a large amount of hashes, wouldn't it better for them to directly contribute to Monero's PoW?

## tevador | 2025-09-15T06:54:28+00:00
No.

By Eqn. 1, you can see that for each unspent output, you need to calculate 1 hash per block. Let's assume there are 12 million unspent outputs and all Monero holders are actively mining lucky transactions. That would amount to 100 000 hashes per second. If we assume that `H(...)` is RandomX (in practice, there is no need to use a slow hash function), that's 100 kH/s compared to 4 GH/s that miners do for PoW. That's a completely negligible number of hashes that would have no impact on PoW security.

## kayabaNerve | 2025-09-15T07:12:06+00:00
That was partially my point though. A malicious adversary can easily organize an additional 100 KHs. How is crowdsourcing PoW in this manner superior to crowdsourcing via p2pool? Why is one insignificant and one significant?

## tevador | 2025-09-15T07:56:39+00:00
Of course, an adversary can easily calculate 100 000 hashes per second, but that's not very useful by itself.

1. You cannot calculate hashes on behalf of other users because you don't know their key images.
2. Even if you somehow knew everyone's key images, you still cannot submit any lucky transactions, unless you also have access to everyone's spend keys.

Basically, an adversary cannot outperform the honest majority of users unless he owns more XMR than all active honest users combined.

## kayabaNerve | 2025-09-15T08:04:56+00:00
Premising on share of outputs, especially when we prior had a rather notable spam attack, seems problematic but I do hear the distinction.

## tevador | 2025-09-15T08:23:29+00:00
Spamming outputs also won't help much.

Someone who owns 1 million outputs of 0.001 XMR each has about the same chance of finding a lucky transaction as someone with 1 output of 1000 XMR (assuming similar age of outputs).

## kayabaNerve | 2025-09-15T08:28:44+00:00
Sorry, I'm up quite late and missed the `amount` incorporation. I'll think on it again tomorrow. Thank you for your patience.  

## SChernykh | 2025-09-15T10:54:36+00:00
Realistically, only the pool's hot wallets would participate in the "lucky transaction" mining. People aren't going to risk their cold wallets for this. As I understand, you need to run an active hot wallet for this, with large amounts in it?

## SChernykh | 2025-09-15T10:57:36+00:00
> target is a dynamically adjusted value so that the blockchain contains on average 1 lucky transaction per block.

How would you dynamically adjust it, if every mined lucky transaction changes the chances of that specific miner because their input height will update? Dynamic adjustment algorithm assumes there is a rather stable "mining power", but here it reduces with every lucky tx mined.

P.S. On the other hand, it increases with every block mined, so these two factors might cancel each other out. It will need real-life testing.

## SChernykh | 2025-09-15T11:02:18+00:00
```
block_weight = (included_lucky_diff + current_lucky_diff / M) * pow_diff
```
Do I get it right, blocks without lucky transactions have no weight at all? Is it a design choice?

## lnchan | 2025-09-15T12:16:36+00:00
How should the `amount` in the transaction scale compared to `checkpoint_height - input_height`? Having enough Monero seems to give a lot of power compared to having old coins, which show a commitment to using the network.

I also presume the `amount` unit isn't piconeros.

~~Also, is the `amount` variable sufficiently useful to the interest of strengthening a specific chain? I'm not quite certain it helps to serves the purpose well.~~

EDIT: Nevermind, with the case of spam attacks, this is relevant.

## tevador | 2025-09-15T13:10:26+00:00
> As I understand, you need to run an active hot wallet for this, with large amounts in it?

Yes, for "mining", the wallet must be open and able to spend. However, the idea is that lucky transactions will be submitted mostly opportunistically when you are sending funds anyways.

> How would you dynamically adjust it, if every mined lucky transaction changes the chances of that specific miner because their input height will update? Dynamic adjustment algorithm assumes there is a rather stable "mining power", but here it reduces with every lucky tx mined.

The chance decreases for that specific "miner", but increases for everyone else as more blocks are added. I think this could be analyzed on a transparent chain like Bitcoin, where you can see how many "coin-blocks" are spent per day on average (i.e. for each spent input, you multiply the amount and the age). It's likely that this will be a relatively stable number.

> Do I get it right, blocks without lucky transactions have no weight at all? Is it a design choice?

No. A block with no lucky transactions has `block_weight = current_lucky_diff / M * pow_diff`, where `current_lucky_diff` is the difficulty a lucky transaction would need to meet. Maybe the notation is a bit confusing.

Assuming a steady state where difficulty doesn't change, a block with no lucky transactions will have `1/(M+1)` of the average weight, or 25% of the average weight if `M=3`.



> How should the `amount` in the transaction scale compared to `checkpoint_height - input_height`? Having enough Monero seems to give a lot of power compared to having old coins, which show a commitment to using the network.
> 
> I also presume the `amount` unit isn't piconeros.
> 

Since they are multiplied together, there is no need for scaling. `amount` can be in arbitrary units. If we wanted to disqualify dust transactions, we could use millineros.

## SChernykh | 2025-09-15T13:13:46+00:00
> transactions will be submitted mostly opportunistically when you are sending funds anyways.

So all end user wallets must support this for it to be efficient. Especially exchange and pool wallets because they move larger amounts regularly.

## taoeffect | 2025-09-18T16:43:20+00:00
It's not very clear to me from the description, is my understanding correct in that the reason this improves on the status quo is because it forces miners to stick to chains that have economic activity going on? In other words, this proposal doesn't actually stop 51% attacks, but it prevents certain types of behavior during a 51% attack (e.g. mining empty blocks or blocks with few economically-meaningful txns in them)?

A 51% attack could still occur, for example, by mining blocks in such a way that the forks can be created by selecting certain combinations of transactions (e.g. one block with 2 "minor" lucky txns, and another with 1 but a "big" one), and these forks would be limited in size. Is that right?

Re privacy:

> A lucky transaction leaks the amount spent in one of the inputs and also leaks the minimum age of the input. However, the identity of the spent input is still protected with a ring signature.

Has anyone done an in-depth analysis of how this would affect Monero's overall privacy?

Should this proposal wait to be deployed only after FCMP++ is deployed?

## DNAKentang | 2025-09-19T05:53:17+00:00
> Should this proposal wait to be deployed only after FCMP++ is deployed?

FCMP++ will take more time to implement i think, it's been there since alot of month but not yet implemented if i not wrong
so now the focus i think on the way monero act to ppl like qubic 

## tevador | 2025-09-19T20:10:48+00:00
> I didn't see this spelled out very clearly in the proposal, so is my understanding correct in that the reason this improves on the status quo is because it forces miners to stick to chains that have economic activity going on? In other words, this proposal doesn't actually stop 51% attacks, but it prevents certain types of behavior during a 51% attack (e.g. mining empty blocks or blocks with few economically-meaningful txns in them)?

It does stop 51% attacks in the sense that an attacker with <80% of the network hashrate won't be able to overtake the honest chain without additional resources.

The table below shows the resources the attacker needs in order to successfully attack the chain. "Coin-age rate" (for lack of a better term) is roughly the expected rate of lucky transactions, which is based on the rate of spending outputs weighted by `amount * coin_age`.

| Coin-age rate      | Hashrate  |
|--------------------|-----------------|
|       0%           |  >80%           |
|      33%           |  >60%           |
|      50%           |  >50%           |
|      67%           |  >40%           |
|     100%           |  >20%           |

The attacker would either need a supermajority of the overall hashrate or would need to collude with a significant amount of coin holders to execute the attack.

> A 51% attack could still occur, for example, by mining blocks in such a way that the forks can be created by selecting certain combinations of transactions

Lucky transactions submitted to the network by honest users cannot be used by the attacker because they commit to the honest blocks, not the attacker's blocks. The attacker would need to control a large amount of XMR as well as a large number of CPUs.

## chaserene | 2025-09-22T03:04:10+00:00
this is a very smart proposal because it introduces a new scarce resource to influence fork choice. that seems to be a requirement for tackling 51% attacks in Nakamoto consensus.

as an aside, what you call "coin-age rate" is known in on-chain financial analytics as "[coin days destroyed](https://www.coingecko.com/learn/coin-days-destroyed-cdd)." lucky transactions can be seen as a way to decide which coin day destroying event should be revealed.

the major/only downside I see is that lucky transactions lose (some) amount privacy.

I've been wondering, and saw @jonathancross propose it elsewhere, if it would be worth obfuscating the amount and proving it's greater than or equal to certain discretized amounts, e.g. integer powers of 10. this it would leak less information.

as a caveat, it would also mean "mining" lucky transactions (with e.g. 10^n XMR sized enotes) would yield more "luck" per capital on average than with organic transactions. a luck-mining attacker could gain advantage over honest users if the honest side had only organic lucky transactions, so there would be some implicit requirement for honest users to mine too. however, I don't think that's unreasonable to expect. there is the indirect benefit of a higher coin price if the chain is secure against 51% attacks. the more XMR someone holds, the greater the incentive would be to mine.

regarding hot wallet risk, could FCMP++'s [transaction chaining](https://raw.githubusercontent.com/kayabaNerve/fcmp-plus-plus-paper/6f01fd3296b17f90b5c97c738cc3320e3369ad49/fcmp%2B%2B.pdf#page=16) or a similar approach mitigate it by allowing the pre-signing of lucky transaction candidates?

## tevador | 2025-09-23T05:16:05+00:00
> I've been wondering, and saw [@jonathancross](https://github.com/jonathancross) propose it elsewhere, if it would be worth obfuscating the amount and proving it's greater than or equal to certain discretized amounts, e.g. integer powers of 10. this it would leak less information.

Yes, this is a possibility. It would require the discretized amount and one ~600 byte bulletproof per lucky transaction (instead of the transparent amount + blinding factor). It's a tradeoff.

> regarding hot wallet risk, could FCMP++'s [transaction chaining](https://raw.githubusercontent.com/kayabaNerve/fcmp-plus-plus-paper/6f01fd3296b17f90b5c97c738cc3320e3369ad49/fcmp%2B%2B.pdf#page=16) or a similar approach mitigate it by allowing the pre-signing of lucky transaction candidates?

Lucky transactions cannot be presigned because they commit to a recent block id. 

It can be seen as a good thing because it proves it's really the owner of the funds who voted for the checkpoint and not some proxy. Allowing presigned transactions would enable risk-free rental of lucky transactions (in a way similar to hashrate rental, which is detrimental to network security).

## binarybaron | 2025-09-24T08:28:50+00:00
> Allowing presigned transactions would enable risk-free rental of lucky transactions (in a way similar to hashrate rental, which is detrimental to network security).

If this means we'd have to disallow pre-signing for all transactions (even non-lucky ones), I'd be strongly against it.

## tevador | 2025-09-24T09:07:12+00:00
> If this means we'd have to disallow pre-signing for all transactions (even non-lucky ones), I'd be strongly against it.

No, it does not mean we should not allow presigning for ordinary transactions. But it means that the contents of tx_extra need to be presigned, so it can't be changed later.

# Action History
- Created by: tevador | 2025-09-14T22:24:32+00:00
