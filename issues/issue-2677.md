---
title: 'mining: add OwnBlock as an independent SOLO mining option'
source_url: https://github.com/monero-project/monero-site/issues/2677
author: luisdiegohidalgo
assignees: []
labels: []
created_at: '2026-06-26T19:24:42+00:00'
updated_at: '2026-08-14T22:23:06+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
## Request

Please consider adding OwnBlock to the Monero Mining page as an independent SOLO mining option:

https://www.getmonero.org/get-started/mining/

OwnBlock is intended for miners who want to mine XMR in SOLO mode without running their own Monero node, pool backend, or production stratum infrastructure.

It is not PPLNS, PPS, or shared-reward mining. Each miner mines independently. If a miner finds a block, the reward is paid directly from the coinbase transaction, minus the pool fee.

We believe this model is consistent with the Monero philosophy of reducing unnecessary trust and avoiding custodial miner balances, while giving miners a simpler way to participate in SOLO mining.

This request is only for an informational listing, not an endorsement.

## Service

* Name: OwnBlock
* Website: https://ownblock.io/
* XMR pool: https://xmr.ownblock.io/
* Type: Independent Monero SOLO mining pool
* Algorithm: RandomX
* Fee: 2%
* Mining mode: SOLO only
* Payout model: Direct coinbase payout to the miner who finds the block
* Custody model: No internal miner balance, no minimum payout, no secondary payout from a pool wallet

## Proof of mined blocks

As part of the verification material for mined blocks and the coinbase payout model, OwnBlock provides:

Validation address:

```text
42n8gMGBrgc5UzcDTvtXBtYFfxkUfBGzKN5cMLCPzNJPgLdtbXhDBr3NJCxK9NMHF3BwHfJERS6NsStdyPypxMms2SCPGqo
```

Watch-only view key:

```text
940d3bbd1f111924209a7e7ce85b37b4b66bf40afa86e8940e19b25a87aaa709
```

Public API:

```text
https://api.ownblock.io/xmr/stats
```

These can be used to inspect the published validation address and compare it with the mined block data exposed by the API.

## Suggested wording

If maintainers consider this useful, a short mention could be added near the solo mining / P2Pool section:

> Independent SOLO mining option: OwnBlock provides Monero SOLO mining infrastructure for miners who want to mine in SOLO mode without operating their own node or pool backend. When a miner finds a block, the reward is paid directly from the coinbase transaction, minus the pool fee. OwnBlock does not use PPLNS or PPS and does not custody miner balances. As with all third-party services, miners should do their own research.

## Links

* Website: https://ownblock.io/
* XMR pool: https://xmr.ownblock.io/
* Mining guide: https://xmr.ownblock.io/guide
* FAQ: https://xmr.ownblock.io/faq
* API: https://api.ownblock.io/xmr/stats


# Discussion History
## nahuhh | 2026-06-26T20:48:44+00:00
How are you taking a 2% fee if the payment is directly from the coinbase?

This is only "solo" in that you're not pooling your hash with other users. It's still custodial -- the reward is paid to your pool, which forwards 98% to the users address., correct?

## nahuhh | 2026-06-26T20:58:44+00:00
> for miners who want to mine in SOLO mode without operating their own node or pool backend.

A user can solo-mine to any (trusted) public rpc node. No pool & no fees necessary

```
./xmrig -o node.ip.address:port -u primaryWalletAddress --daemon
```

## luisdiegohidalgo | 2026-06-26T20:59:19+00:00
Thanks for the question. No, that is not correct.

The reward is not first paid to OwnBlock and then forwarded to the miner.

The coinbase transaction itself is built with separate outputs:

* 98% directly to the miner’s Monero address
* 2% directly to the OwnBlock fee address

So OwnBlock never receives or custodies the miner’s 98%, and there is no later payout transaction from a pool wallet.

There is no internal miner balance, no payout threshold, and no “pool receives 100% then sends 98%” flow.

It is “solo” because miners are not sharing rewards or pooling hashrate under PPLNS/PPS. Each miner mines independently, and if that miner finds a block, the miner’s share is paid directly in the coinbase transaction.

The pool only provides the mining infrastructure / stratum endpoint and includes its 2% fee as a separate coinbase output.

For review, here are recent mined blocks:

3704519
3703411
3701977
3701541
3699545
3698315
3698201
3695404
3687802
3683819

You can also validate this using the watch-only view key I provided above.




## luisdiegohidalgo | 2026-06-26T21:03:29+00:00
> > for miners who want to mine in SOLO mode without operating their own node or pool backend.
> 
> A user can solo-mine to any (trusted) public rpc node. No pool & no fees necessary
> 
> ```
> ./xmrig -o node.ip.address:port -u primaryWalletAddress --daemon
> ```

Correct, users can solo-mine directly against their own node or a trusted public RPC node, with no pool and no fee. OwnBlock is not meant to replace that.

The use case here is different: it is for miners who want SOLO mining but prefer a simple stratum endpoint instead of managing the full node/RPC mining setup themselves.

This is especially relevant for users who want to rent hashrate and point it to their mining setup, for example through services like NiceHash. In that case, using a standard pool/stratum endpoint is much simpler than trying to route rented hashrate directly to wallet/RPC solo-mining software.

For a regular user, it is also simpler to run XMRig against a stratum endpoint than to sync and maintain a full or pruned Monero node just to participate in SOLO mining.

## luisdiegohidalgo | 2026-06-26T21:19:43+00:00
Also, OwnBlock data is already available here:

https://blocks.p2pool.observer/proofs

So if you do not want to reconstruct a full watch-only wallet locally, you can also verify the available data through that proof page.

## luisdiegohidalgo | 2026-06-26T21:20:09+00:00
If you have any further questions, I will be happy to answer them.

If you still consider that listing OwnBlock is not viable, even though we believe it is an innovative SOLO mining system that can help the Monero network, we understand.

Please just let us know. In any case, we are grateful that you read our message and took the time to respond.


## luisdiegohidalgo | 2026-08-14T22:23:05+00:00
Hi, just following up on this request. Have you had a chance to review whether OwnBlock would be appropriate to list on the Monero Mining page as an independent SOLO mining option?

As mentioned above, the request is only for an informational listing, not an endorsement. OwnBlock operates as a SOLO-only mining service with direct coinbase payouts and no custodial miner balances.

If you need any additional technical information, verification, or changes to the proposed wording, I'd be happy to provide them.

Thank you for your time and for maintaining the Monero website.

# Action History
- Created by: luisdiegohidalgo | 2026-06-26T19:24:42+00:00
