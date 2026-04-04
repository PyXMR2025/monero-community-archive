---
title: Should support_flags be included in the handshake?
source_url: https://github.com/monero-project/monero/issues/6272
author: ahook
assignees: []
labels: []
created_at: '2019-12-30T20:11:36+00:00'
updated_at: '2020-01-05T11:45:22+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
When we initiate a connection to a peer, after the handshake is complete, we immediately send a follow-up request just to get the uint32_t support flags (https://github.com/monero-project/monero/blob/5d7ae2d2791c0244a221872a7ac62627abb81896/src/p2p/net_node.inl#L1094).

Would it not make more sense to just include this field in the handshake and avoid the extra network overhead?

# Discussion History
## moneromooo-monero | 2019-12-30T22:37:45+00:00
In general yes, but this should be removed as all nodes support it now.

## ahook | 2019-12-30T22:58:26+00:00
Even better! Could for now simply remove the get_support_flags call (but leave the handler for backwards-compatibility with older nodes) and remove all the checks for fluffy block support.

Then assuming https://github.com/monero-project/monero/pull/6243/commits/896a38343842d363246cb5720d338f9fd21b1446 makes it into master, it would be free network-wise to add an optional field later to the handshake for future use (keeping all the other code that stores/handles/passes around the support_flags field internally).

It's only a minor win, as this is a once-per-connection message, so probably low priority. But I'd be happy to whip up a PR for it.

## ahook | 2019-12-31T00:03:54+00:00
Something along the lines of this: https://github.com/ahook/monero/commit/757c3a67c9e65c5cb09132c395d452a5bf0cef7e

## vtnerd | 2019-12-31T02:54:25+00:00
Since the runtime flag is still available, the p2p flags cannot be removed from the protocol yet.

## moneromooo-monero | 2019-12-31T09:02:12+00:00
I'd OK such a PR (I've only quickly gone through the link)

## ahook | 2019-12-31T21:24:19+00:00
> Since the runtime flag is still available, the p2p flags cannot be removed from the protocol yet.

Assuming you mean the --no-fluffy-blocks runtime flag, from what I can tell, that only affects this one condition: https://github.com/monero-project/monero/blob/5d7ae2d2791c0244a221872a7ac62627abb81896/src/cryptonote_protocol/cryptonote_protocol_handler.inl#L2315. So that flag really just makes it so a node only sends out full blocks, and has no bearing on what the node is able/willing to receive.

The only issue I see is if there happen to be nodes out there who have hardcoded their flags to 0 here: https://github.com/monero-project/monero/blob/2899379791b7542e4eb920b5d9d58cf232806937/src/cryptonote_config.h#L140

Not sure if that's a realistic scenario, or one that should still be supported, since fluffy blocks are pretty well-vetted by now.

## Gingeropolous | 2020-01-05T05:26:52+00:00
> Not sure if that's a realistic scenario, or one that should still be supported, since fluffy blocks are pretty well-vetted by now.

Yes and no. Yes, they have been running as default on the network for a while. No - the network hasn't been seriously attacked or fractured. I can't fathom an attack scenario right now, but I'm really wary of removing the ability of a node to send full blocks to its peers. This is a core function of a node. 

Also, I think the idea of support flags should be maintained - who knows what other wacky things we'll come up with in the future. 

## moneromooo-monero | 2020-01-05T11:45:22+00:00
You can still remove that particular support flag and choose to send full blocks, that is still supported. What would not be is the ability of a peer to say "send me full blocks only".

# Action History
- Created by: ahook | 2019-12-30T20:11:36+00:00
