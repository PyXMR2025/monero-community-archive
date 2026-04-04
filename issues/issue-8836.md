---
title: Monerod is not a full node by default
source_url: https://github.com/monero-project/monero/issues/8836
author: tevador
assignees: []
labels:
- question
- proposal
created_at: '2023-05-03T19:48:07+00:00'
updated_at: '2025-09-13T17:40:40+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
~~It seems that Monero likely hasn't had any actual full nodes since 2017: https://github.com/monero-project/monero/pull/2225~~

Monerod will skip tx verification for checkpointed blocks:

https://github.com/monero-project/monero/blob/a2e8d1d4271df1591786b8d92516455488ee82fd/src/cryptonote_core/cryptonote_core.cpp#L899-L903

This means that most (if not all) new users actually trust the dev team to embed the correct hashes into the release binary.

~~AFAICS the only way to make a full node is to manually edit CMakeLists.txt here and build your own binary. There should at least be a command line option to force full verification.~~

There is a command line option to disable fast sync, but preferably it should be the other way around, i.e. having `--fast-sync` option to enable this feature.

I think the fact that full verification is skipped is not widely known. For example, running with `--prune-blockchain` will needlessly download unpruned transactions *to be discarded without verification*. There is a related issue to avoid downloading the useless data here: https://github.com/monero-project/monero/issues/8834

However, I think it's quite important to allow users to select each of the 4 options as follows:

1. By default, monerod will be an unpruned full node.
2. When run with `--fast-sync`, the result will be an unpruned node that skips the verification of checkpointed blocks (current default).
3. When run with `--prune-blockchain`, the result will be a pruned full node.
4. When run with both `--fast-sync` and `--prune-blockchain`, the result will be a pruned node that skips the verification of checkpointed blocks. This should be equivalent to the current option of `--sync-pruned-blocks` as it can save both CPU and network bandwidth.



# Discussion History
## selsta | 2023-05-03T20:36:19+00:00
> There should at least be a command line option to force full verification

There is `./monerod --fast-block-sync 0`

## tevador | 2023-05-03T21:03:37+00:00
> `--fast-block-sync 0`

Thanks. So I guess the remaining point of this issue is to invert the default value of that option or at least make it more widely known that verification is skipped, for example by printing a warning when running monerod and the current height is below the latest checkpoint.


## iamamyth | 2023-05-03T21:55:47+00:00
Anyone running a pre-built binary places quite a bit of trust in its contents (the flag itself could have no effect, or the opposite effect of the documentation, etc). Noting the operating mode as an info at startup seems fine, but making it a WARN likely will produce unhelpful support requests (the default fast-sync behavior responds to user demands to make sync faster for old blocks; if fast-sync remains the default, you'd have a default WARN, which I consider a design error).

## tevador | 2023-05-03T22:07:34+00:00
An INFO-level message printed at startup should be enough as a "warning".

## jbird186 | 2023-05-03T22:50:15+00:00
>It seems that Monero likely hasn't had any actual full nodes since 2017

FWIW, Monero has had fast syncing in some form since the very beginning. 

https://github.com/monero-project/monero/blob/1a8f5ce89a990e54ec757affff01f27d449640bc/src/cryptonote_core/blockchain_storage.cpp#L1367-L1368

Bitcoin also does something similar to this,

https://github.com/bitcoin/bitcoin/blob/aebcd18c654a1706954a9e2c9cbfe97dfe531357/src/kernel/chainparams.cpp#L107

Fast sync is pretty standard, so it's not as if there's some sneaky trick being pulled on Monero to centralize control.

## jtgrassie | 2023-05-08T18:10:29+00:00
> Fast sync is pretty standard...

I tend to agree but also support an info message at startup notifying the user as to what options are in use. 

Thus I'd advocate for default unpruned & fast-sync (e.g. the current default), and a message stating those options are in effect.

## DaWe35 | 2024-02-18T08:54:38+00:00
I think this issue should be marked as invalid, since the title of and the first paragraph is not true.

The question about defaults should be a discussion somewhere else, but honestly, I don't think making `fast-block-sync` is a bad idea. Most users don't need a full-node and advanced users will find the way.
The only problem I see is the inconsistency in defaults: if we want mass-user-friendly defaults, why pruning is not on? I feel like either should be on or off.

Another problem is the lack of documentation. It is hard to find guides about running a full node, and seeing this inconsistency in default values, I can fully understand why everyone is confused. I wrote a new gist to help you understand how to properly sync a monerod client:
[Monerod sync modes
](https://gist.github.com/DaWe35/aaa0d1a99be4a6fb0977fb7df7ddb702)

## Gingeropolous | 2024-02-20T03:50:02+00:00
> Most users don't need a full-node and advanced users will find the way.

ehh... I think the core software that builds and maintains the monero network should, by default, be doing everything in such a way to make sure the network works as best it can. 

as it stands, the network is essentially dependent on the hashes (because fast sync is on by default)... which, as it currently exists is within the code itself (i think), so it's sorta like if you trust the current release, then you should trust the hashes.

~~I think it would be a different issue if the hashes we were dependent on were getting fetched from some centralized server or something. I know there is a DNS checkpoint system, but I don't know if thats active, and i think its more for emergencies afaik.~~

I think i was conflating the embedded hashes that come with the pre-built binaries and the checkpoints that are in the sourcecode somewhere. 

but yeah in general I think the primary software that builds the network should be doing full verify by default. If the GUI wants to come with a preset mod that enables fast sync and prune by default for "simple mode", then yeah. 

## BigslimVdub | 2024-03-20T02:36:04+00:00
> > There should at least be a command line option to force full verification
> 
> There is `./monerod --fast-block-sync 0`

Why not ask the cli user on initial sync “The default sync method is fast sync which does not verify 100% of the blocks from block 0. Do you want to fully sync the blockchain? This process will slow down the initial sync because it will verify every block including checkpoints.” 

Obviously an end user opting for cli is typically not a beginner user and most likely has the intent to run a full node and or personal node and wants a fully verified blockchain. GUI wallet should be fine with fast sync/pruned since most gui users use remote node anyway.

The question is, will full syncs put additional load on seed nodes due to verification of additional blocks and one reason fast sync/pruning was enabled? Nobody wants spamming.

# Action History
- Created by: tevador | 2023-05-03T19:48:07+00:00
