---
title: Remove Extra Coinbase Locktime
source_url: https://github.com/monero-project/research-lab/issues/104
author: UkoeHB
assignees: []
labels: []
created_at: '2022-07-16T20:18:16+00:00'
updated_at: '2025-12-25T08:06:35+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Currently, Monero has two mandatory locktimes for outputs added to the chain.

1. Coinbase outputs cannot be spent until the 60th block after they are created (cryptonote rule, enforced via the `unlock_time` tx field).
2. Non-coinbase outputs cannot be spent until the 10th block after they are added to the chain (monero v12 rule, enforced by consensus).

This issue is to investigate and discuss removing the special coinbase output locktime rule, which has no documented justification that I am aware of. The rule-change probably wouldn't go into effect until Seraphis, where the `unlock_time` feature will likely be removed (see discussion [here](https://github.com/monero-project/research-lab/issues/78)).

Does anyone know if it necessary/useful and why? Let's turn this Chesterton's fence into something meaningful.

# Discussion History
## busyboredom | 2022-07-17T01:46:08+00:00
I've dug up some history and shared it on Matrix, but posting it here too for visibility.

In his initial 2014 bitmonero release forking bytecoin, thankful_for_today made the decision to increase the coinbase unlock time from 10 to 60 while simultaneously decreasing the block time from 2 minutes to 1 minute: https://github.com/monero-project/monero/commit/1a8f5ce89a990e54ec757affff01f27d449640bc#

When asked about it by a confused miner, he said "60 blocks unlock delay. This is much safer." with no further clarification: https://bitcointalk.org/index.php?topic=563821.msg6283927#msg6283927

## UkoeHB | 2022-07-17T16:01:24+00:00
It seems the coinbase lock time idea originated in [Bitcoin](https://bitcoin.stackexchange.com/questions/1991/what-is-the-block-maturation-time) (thanks to @SChernykh for the link). The rationale was to mitigate a situation where a reorg invalidates coinbase outputs and by extension all outputs created by transactions that depend on those coinbase outputs. Bitcoin went out of its way to add this rule because it can impact users interacting with _completely honest funds_, i.e. a reorg that does not double-spend any of the funds in some outputs' tx histories can still invalidate those outputs. There is no mandatory lock time on normal Bitcoin outputs because normal outputs in a reorged Bitcoin tx may not be invalidated if the tx's inputs are not double spent (and aren't part of a tx tree containing double-spent outputs), because those kinds of txs can be re-mined into the reorged chain.

In Monero, a reorg may invalidate a decoy ring member (either its index, or block it completely with a double spend), which would invalidate a normal transaction that's otherwise valid (i.e. because its real inputs are still on-chain). Since it is generally not safe to reference decoys that may be reorged away, it used to be the core wallet's policy to not select tx inputs or decoys from the most recent 10 blocks of the chain. Alternate wallet implementations could select inputs or decoys from that range if desired ([and some did](https://youtu.be/XIrqyxU3k5Q?t=1024)). Since selecting young inputs/decoys can't be a general wallet policy, it is privacy hole that was plugged up by mandating a 10-block lock time on normal outputs in v12 of the protocol. Reorgs invalidating decoy ring members and therefore invalidating honest txs is also a user-expectation problem, in the same way as coinbase outputs being invalidated.

The 10-block normal output lock and 60-block coinbase output lock were therefore implemented to mitigate the same problem - reorgs that invalidate txs without any of the direct participants performing a double spend. This begs the question, is there a reason for the mandatory locktime on those two output types to be different (aside from the conservative argument - don't change what isn't broken)?

## ChristopherKing42 | 2022-08-03T19:55:58+00:00
> Bitcoin went out of its way to add this rule because it can impact users interacting with completely honest funds, i.e. a reorg that does not double-spend any of the funds in some outputs' tx histories can still invalidate those outputs.

Since we are assuming honesty, this could also just be enforced by the wallet instead of at the consensus layer.

## trasherdk | 2022-08-04T08:07:48+00:00
@ChristopherKing42 I'm pretty sure it's the other way around. You should be assuming hostile adversaries everywhere.
Don't trust, verify.

## tevador | 2024-04-05T18:41:41+00:00
With [FCMPs](https://gist.github.com/kayabaNerve/0e1f7719e5797c826b87249f21ab6f86), any reorg deeper than 10 blocks will always permanently invalidate all transactions. Therefore I suggest that the 60-block coinbase lock time be reduced to 10 blocks if/when FCMPs are implemented.

## stianov | 2025-12-01T04:36:53+00:00
Was a consensus ever reached on this through other channels? After FCMPs it seems arbitrary to lock coinbase outputs for longer than any other output.

## spirobel | 2025-12-25T08:06:35+00:00
would also mean we could get rid of timelocks entirely which is a potential footgun when scanning outputs

# Action History
- Created by: UkoeHB | 2022-07-16T20:18:16+00:00
