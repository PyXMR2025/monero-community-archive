---
title: Nodes that don't have the pool loaded can get disconnected from peers when
  missing pool txs exceed 100mb
source_url: https://github.com/seraphis-migration/monero/issues/157
author: j-berman
assignees: []
labels:
- upstream
created_at: '2025-10-09T19:56:37+00:00'
updated_at: '2025-10-11T02:37:22+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Upstream issue.

1) Node A requests tx  pool complement from all connections [here](https://github.com/monero-project/monero/blob/d32b5bfe18e2f5b979fa8dc3a8966c76159ca722/src/cryptonote_protocol/cryptonote_protocol_handler.inl#L2451).
    - Requests all connected and synced peers send pool txs Node A does not have.
    - This gets called on startup, **and after a node gets disconnected from the network [here](https://github.com/monero-project/monero/blob/d32b5bfe18e2f5b979fa8dc3a8966c76159ca722/src/cryptonote_protocol/cryptonote_protocol_handler.inl#L2863-L2864)**.
2) Node B responds with **all** pool txs that Node A does not have [here](https://github.com/monero-project/monero/blob/d32b5bfe18e2f5b979fa8dc3a8966c76159ca722/src/cryptonote_protocol/cryptonote_protocol_handler.inl#L866).
3) (expected but untested) Node A will drop Node B since the packet size exceeds `LEVIN_DEFAULT_MAX_PACKET_SIZE` of 100mb. It would *definitely* exceed the `NOTIFY_NEW_TRANSACTIONS` limit of 128mb as well.

Node B could serve a slice of txs to Node A, and the remaining tx hashes. So long as there are remaining tx hashes, Node A can continue requesting the complement until done. ~~Or this could be solved with https://github.com/monero-project/monero/pull/9933.~~

# Discussion History
## j-berman | 2025-10-10T01:39:25+00:00
TODO: explore sending batches of txs of some max size [here](https://github.com/monero-project/monero/blob/d32b5bfe18e2f5b979fa8dc3a8966c76159ca722/src/cryptonote_protocol/cryptonote_protocol_handler.inl#L872-L881), instead of sending all the txs in one go.

## j-berman | 2025-10-10T21:09:00+00:00
Actually, it appears the txpool complement doesn't even get served. Testing with local nodes, no nodes handling the complement response get past this [if statement](https://github.com/monero-project/monero/blob/d32b5bfe18e2f5b979fa8dc3a8966c76159ca722/src/cryptonote_protocol/cryptonote_protocol_handler.inl#L859-L860). Looks like a distinct issue that nodes are trying to get their pool complement too soon before the handshake fully completes.

Additionally, it looks like nodes can end up trying to relay their entire pool every x minutes because `get_relayable_transactions` can actually return all txs in the pool, not just txs that still need to be relayed. I suspect that is a major culprit of disconnects w/large pool. Tx relay v2 should help with that, but perhaps `get_relayble_transactions` shouldn't even attempt to re-relay every tx hash in the pool. Without additional handling surrounding the packet size limit, and without fixing tx pool complement, that could still be a source of disconnects even with tx relay v2.

## j-berman | 2025-10-11T02:32:44+00:00
> Actually, it appears the txpool complement doesn't even get served. Testing with local nodes...

Assume Node A accepts INC connections, and Node B makes an OUT connection to Node A.

When Node A receives the initial handshake request from Node B in `handle_handshake`, Node A might immediately try to retrieve its tx pool complement from Node B (it requests the complement if it sees that Node A is synced based on Node B's req). But, Node A fires the txpool complement request **before responding to Node B's handshake**, and so Node B ignores the txpool complement request [here](https://github.com/monero-project/monero/blob/d32b5bfe18e2f5b979fa8dc3a8966c76159ca722/src/cryptonote_protocol/cryptonote_protocol_handler.inl#L859-L860), since Node B won't know the connection is ready until Node A responds to the handshake request.

So... nodes that accept incoming connections might have a harder time getting pool tx complements from peers. Note it only runs once until the node disconnects/falls out of sync again.

But, nodes that only make outgoing connections should theoretically be requesting tx pool complements fine, except their connections will close unnecessarily if they are missing too many txs from the pool.

Ways to improve the tx pool complement logic:

1) Serve batches of txs in the response for the complement.
2) Only request tx pool complements from outgoing connections.
    - It should probably *always* run upon completing a handshake and entering normal state with an outgoing connection. It shouldn't only run once.
    - It would probably even be good to do it in the timed sync loop.
3) `handle_notify_get_txpool_complement` should request missing txs from the requester. This could use `NOTIFY_REQUEST_TX_POOL_TXS` from  https://github.com/monero-project/monero/pull/9933 (alternatively nodes could easily just re-request the complement from incoming connections in there, but that's a bit more overhead).

1 is simple. Will submit a PR for that soon. 2 and 3 are a bit trickier. I think 2 and 3 should be done together, and 3 probably makes sense to wait until 9933 is merged.

# Action History
- Created by: j-berman | 2025-10-09T19:56:37+00:00
