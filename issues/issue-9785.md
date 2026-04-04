---
title: Default priority has no mapping in get_fee_estimate
source_url: https://github.com/monero-project/monero/issues/9785
author: woodser
assignees: []
labels: []
created_at: '2025-02-08T15:39:31+00:00'
updated_at: '2025-02-16T05:20:42+00:00'
type: issue
status: closed
closed_at: '2025-02-16T05:20:42+00:00'
---

# Original Description
Currently there is no mapping from `default` transaction priority to the fee estimates provided by [`get_fee_estimate`](https://docs.getmonero.org/rpc-library/monerod-rpc/#get_fee_estimate).

This prevents third parties from verifying that a transaction was generated with `default` priority. The best they can do is verify that a transaction was generated with `uimportant` priority.

This issue requests providing a such a mapping.

One way it could be done is by adding a new RPC call to monero-wallet-rpc. For example, `get_default_fee_priority()`, which returns 0-3, corresponding to unimportant, normal, elevated, and extra elevated.

Alternatively, the daemon could calculate and provide the mapping, but this would be a bigger change.

# Discussion History
## iamamyth | 2025-02-10T00:33:54+00:00
I'm a bit confused as to who these "third parties" would be, as anyone relying on get_fee_estimate could easily be fooled by the new endpoint, too, as they'd don't have a "trusted" daemon. Or, if someone trusts the daemon, but not the client connecting to it, they can't ever confirm the client used the right daemon. Who does this help?

## iamamyth | 2025-02-10T00:39:09+00:00
Is the goal here to just help the client pick the right fee? If so, I'm not sure why you wouldn't add a field to the existing response, except, I suppose, the priorities and the default may have different change frequencies, but I suspect most clients will just call the endpoints in a pair, so splitting them makes net more work for the daemon.

## woodser | 2025-02-10T11:45:08+00:00
> I'm a bit confused as to who these "third parties" would be, as anyone relying on get_fee_estimate could easily be fooled by the new endpoint, too, as they'd don't have a "trusted" daemon. Or, if someone trusts the daemon, but not the client connecting to it, they can't ever confirm the client used the right daemon. Who does this help?

In our use case, peers submit signed transactions to an arbitrator for verification. For example, peers submit a "penalty" transaction which the arbitrator may broadcast if they misbehave during trade initialization. They also submit signed transactions to move funds to a shared multisig wallet.

The goal is for the arbitrator to verify that the peers used an appropriate mining fee at current congestion levels, to ensure protocol reliability.

Therefore, peers should use the "default" fee priority, to adjust to current congestion levels, and the arbitrator needs to be able to verify that the fee meets the current default level as well.

The problem is that the arbitrator has no way of knowing what the default fee level currently is, because it's not provided from their trusted daemon via `get_fee_estimate` or their own internal wallet.

## iamamyth | 2025-02-10T17:07:39+00:00
Based on your description, it seems my earlier suspicion would be correct:

> I suspect most clients will just call the endpoints in a pair, so splitting them makes net more work for the daemon.

Can you confirm that would be your usage pattern? If so, I think you should just add the default priority to the existing endpoint, for the reasons laid on in my earlier comment.

## woodser | 2025-02-10T17:34:14+00:00
> I think you should just add the default priority to the existing endpoint

What existing endpoint?

## iamamyth | 2025-02-10T17:41:08+00:00
`get_fee_estimate` (the only one discussed in this issue).

## woodser | 2025-02-10T17:55:37+00:00
The priority adjustment code is currently part of wallet2 / monero-wallet-rpc. It would be a much bigger change to move this logic to the daemon and refactor the wallet to use it, than to extend monero-wallet-rpc with an additional call to expose this functionality. If the daemon did support such functionality, we could deprecate this function or refactor it to use the daemon.

## woodser | 2025-02-10T18:39:16+00:00
But yes I will use the result of get_default_fee_priority to get the index in get_fee_estimate.

## iamamyth | 2025-02-10T19:13:31+00:00
> It would be a much bigger change to move this logic to the daemon and refactor the wallet to use it, than to extend monero-wallet-rpc with an additional call to expose this functionality

Yes, that's fine.

# Action History
- Created by: woodser | 2025-02-08T15:39:31+00:00
- Closed at: 2025-02-16T05:20:42+00:00
