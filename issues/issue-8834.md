---
title: Consider enabling --sync-pruned-blocks by default for pruned nodes
source_url: https://github.com/monero-project/monero/issues/8834
author: jbird186
assignees: []
labels:
- low priority
- proposal
created_at: '2023-05-02T05:32:27+00:00'
updated_at: '2024-02-19T05:21:33+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
**TLDR**: Not enabling --sync-pruned-blocks is strictly unnecessary and wasteful.



The `--sync-pruned-blocks` flag, added in #5915, allows a pruned node to skip downloading the full content of certain blocks, when they would otherwise be pruned locally. This flag appears to be largely forgotten about, as I've seen little mention of it at all.

This should be enabled by default when running a pruned node, eg with `--prune-blockchain` set. Normally, pruned nodes must download the entire blockchain, despite the fact that they are going to discard roughly 2/3 of it after. This adds unnecessary strain to not only the syncing node's connection, but to the network as a whole. Since that 2/3 goes to waste anyway, there seems to be no reason to not have this flag set by default. It does not change the trust model either, since nodes already trust old blocks to be valid.

Edit: 
To clarify, the prunable data that I'm referring to is **not**, in fact, used for validation in most cases. By default, monerod only validates relatively recent transactions, and any transactions covered by a checkpoint are presumed to be valid. If a user chooses to disable fast-sync, then the prunable data would still have to be downloaded and validated. Otherwise, it's total dead weight on the node and the network as a whole.

# Discussion History
## tevador | 2023-05-02T18:52:47+00:00
Full nodes must download the whole blockchain in order to verify it. There is currently no way around that (perhaps in the future there can be a more efficient way based on zero knowledge proofs).

Nodes run with `--sync-pruned-blocks` are not full nodes. They only verify PoW and delegate the blockchain validation to miners. Therefore I don't think it should be the default option.

## jbird186 | 2023-05-02T20:10:47+00:00
@tevador  Nodes don't actually fully verify the entire history, AFAIU.

https://github.com/monero-project/monero/blob/a2e8d1d4271df1591786b8d92516455488ee82fd/src/cryptonote_core/cryptonote_core.cpp#L899-L903

## tevador | 2023-05-02T21:04:16+00:00
If verification is skipped for checkpointed blocks, that is unfortunate and should be fixed ASAP. The default should be full verification of the blockchain. There can be an option to skip downloading and verifying pruned blocks for people who are OK with that.

Running a pruned node is orthogonal to full verification. I think most people run pruned nodes due to storage limitations rather than bandwidth or CPU constraints.

## jbird186 | 2023-05-02T22:00:54+00:00
@tevador The core point in this request is that when both fast sync and pruning are enabled simultaneously, `--sync-pruned-blocks` should also be enabled by default, as it's a free massive optimization yet very few people seem to know about it. As it stands, right now, fast sync is enabled by default, meaning that this flag should be automatically enabled when pruning. Something similar to #3191 should be done with `--sync-pruned-blocks`.

If you believe that fast sync should not be enabled by default, then that's a separate discussion, not within the scope of this issue. I disagree that fast sync should be disabled, but either way, can we agree that this flag should be enabled when fast-syncing (default or not) + pruning?

> most people run pruned nodes due to storage limitations rather than bandwidth or CPU constraints

Maybe, but IBD does demand a lot of bandwidth, and that will only become even more true over time as the chain continues to grow. Data caps are also an issue. There's a massive amount of waste without this flag, not just for the node being synced but also for the network as a whole, which has to waste time feeding it unused data.

## tevador | 2023-05-02T22:12:13+00:00
> when both fast sync and pruning are enabled simultaneously, --sync-pruned-blocks should also be enabled by default

Yes, I agree. Downloading data to be discarded without being verified is just a waste of bandwidth.

> that's a separate discussion, not within the scope of this issue

I disagree with this. I think that fast sync being enabled by default might be a mistake that should be rectified first rather than being cemented in with the change you are proposing.

## jbird186 | 2023-05-03T02:25:05+00:00
@tevador I don't see how this cements fast syncing. It would simply be activated when fast sync and pruning are both enabled, and maybe `--no-sync-pruned-blocks` could be added too if one wishes to explicitly disable it. This would not be affected if fast syncing were to be disabled by default, as instead one would just have to explicitly set  `--fast-sync`.

## DeeDeeRanged | 2023-05-10T07:14:42+00:00
At the moment I have in my monerod.conf --prune-blockchain and not --sync-pruned-blocks and/or --fast-sync. From the --help I can see --fast-block-sync arg (=1) but there is no --fast-sync mentioned.
Would anyone be so kind to enlighten me?


## tevador | 2023-05-10T07:36:32+00:00
`--fast-sync` is a hypothetical command which does not exist. Fast sync is on by default but can be disabled with `--fast-block-sync 0`. `--sync-pruned-blocks` doesn't work if fast sync is disabled.

## DeeDeeRanged | 2023-05-10T10:03:36+00:00
> `--fast-sync` is a hypothetical command which does not exist. Fast sync is on by default but can be disabled with `--fast-block-sync 0`. `--sync-pruned-blocks` doesn't work if fast sync is disabled.

Thanks. I have added sync-pruned-blocks=1 to my config file :)

## DaWe35 | 2024-02-18T09:11:58+00:00
I agree with this proposal, makes sense. However in the comments I can only see confusion.

`fast-block-sync` is on by default, because most users don't want to verify the whole blockchains. The question of this is not in scope with this PR.

As @tevador wrote, pruned clients are not full nodes, therefore it is unnecessary to download the whole blockchain,` --sync-pruned-blocks` should be on by default. Not sure how @tevador got to the opposite conclusion, I carefully read all your words and it does not make sense, but please correct me if I'm wrong.

## DaWe35 | 2024-02-18T09:19:40+00:00
> @tevador I don't see how this cements fast syncing. It would simply be activated when fast sync and pruning are both enabled, and maybe `--no-sync-pruned-blocks` could be added too if one wishes to explicitly disable it. This would not be affected if fast syncing were to be disabled by default, as instead one would just have to explicitly set `--fast-sync`.

The amount of flags we have is already confusing, I don't think adding more makes the situation better. I had to write a [gist about syncing](https://gist.github.com/DaWe35/aaa0d1a99be4a6fb0977fb7df7ddb702), it is so complicated.
I also don't understand why we have `--sync-pruned-blocks` option, why it is not automatically default for pruned clients (as you proposed), and off for full nodes. So instead of adding one more flag, I'd remove `--sync-pruned-blocks` after it is automatically turned on for pruned nodes 🤣

# Action History
- Created by: jbird186 | 2023-05-02T05:32:27+00:00
