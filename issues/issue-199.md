---
title: ZMQ Pub/Sub design proposal
source_url: https://github.com/Cuprate/cuprate/issues/199
author: Boog900
assignees: []
labels:
- C-proposal
- A-zmq
created_at: '2024-06-27T19:20:06+00:00'
updated_at: '2024-09-25T12:43:39+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
## What

The proposal covers integrating [`monerod`'s ZMQ Pub/Sub system](https://github.com/monero-project/monero/blob/master/docs/ZMQ.md#zmq-pubsub), it does not cover the seperate ZMQ RPC system.

## How

`monerod` uses ZMQ `XPUB` sockets to allow clients to filter the data they do not need and so `monerod` only has to create data that has active subscribers for.

This means we can't use the `zeromq` crate (the ZMQ Rust rewrite) as it does not yet support XPUB sockets, so we will have to use the `zmq` crate (Rust bindings). 

### Message types

The message types from Monero will need to be defined, this should be done in its own crate `cuprate-zmq-types` in `zmq/types`.

[This file](https://github.com/monero-project/monero/blame/master/src/rpc/zmq_pub.cpp) contains some of these types.

### Filtering

As described in [monerod's ZMQ docs](https://github.com/monero-project/monero/blob/master/docs/ZMQ.md#zmq-pubsub) filtering is done on multiple levels, format, context, and event.

`zmq` will handle routing the messages to the right clients, however we need a way to keep track of the amount of subscribers for each type so we know if we actually need to send a certain message or not.

This will be done by a `Subscribers` struct which will look something like this:

```rust
struct Subscribers {
    numb_subscribers: BTreeMap<MessageType, u64>,
}

#[derive(Clone, Copy, Debug, Eq, PartialEq, Ord, PartialOrd)]
enum MessageType {
    // The order of these variants must not change

    JsonMinimalChainMain,
    JsonMinimalTxPoolAdd,

    JsonFullChainMain,
    JsonFullTxPoolAdd,
    JsonFullMinerData,
}

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
enum Filter {
    All,

    JsonMinimal,
    JsonMinimalChainMain,
    JsonMinimalTxPoolAdd,

    JsonFull,
    JsonFullChainMain,
    JsonFullTxPoolAdd,
    JsonFullMinerData,
}

// by implementing `RangeBounds<MessageType>` it allows us to do `.range(Filter::XX)` on a btree
// tests should be added to make sure every Filter returns the correct range. 

impl RangeBounds<MessageType> for Filter {
    fn start_bound(&self) -> Bound<&MessageType> {
        match self {
            Filter::All => Unbounded,
            Filter::JsonMinimal => Unbounded,
            Filter::JsonMinimalChainMain => Included(&MessageType::JsonMinimalChainMain),
            Filter::JsonMinimalTxPoolAdd => Included(&MessageType::JsonMinimalTxPoolAdd),
            Filter::JsonFull => Included(&MessageType::JsonFullChainMain),
            Filter::JsonFullChainMain => Included(&MessageType::JsonFullChainMain),
            Filter::JsonFullTxPoolAdd => Included(&MessageType::JsonMinimalTxPoolAdd),
            Filter::JsonFullMinerData => Included(&MessageType::JsonFullMinerData)
        }
    }

    fn end_bound(&self) -> Bound<&MessageType> {
        match self {
            Filter::All => Unbounded,
            Filter::JsonMinimal => Excluded(&MessageType::JsonFullChainMain),
            Filter::JsonMinimalChainMain => Included(&MessageType::JsonMinimalChainMain),
            Filter::JsonMinimalTxPoolAdd => Included(&MessageType::JsonMinimalTxPoolAdd),
            Filter::JsonFull => Unbounded,
            Filter::JsonFullChainMain => Included(&MessageType::JsonFullChainMain),
            Filter::JsonFullTxPoolAdd => Included(&MessageType::JsonMinimalTxPoolAdd),
            Filter::JsonFullMinerData => Included(&MessageType::JsonFullMinerData)
        }
    }
}
```
I wrote a little more than just example code there to check this idea actually works. 

`Filter` then needs a method to create it from a string, see the Monero zmq docs for what strings are needed, an empty string and the string "json" should return `Filter::All`.

`Subscribers` will need a method to add subscribers from a `Filter` by adding one to every integer in that range. It will also need a method to see if there are subscribers for a certain `MessageType`. On creation `Subscribers` should be filled with every `MessageType`.

The `Subscribers` struct will be defined in a new crate `cuprate-zmq-pubsub` in `zmq/pubsub`. `MessageType` and `Filter` should be in `cuprate-zmq-types`.

### Pub/Sub Server

The zmq server pub/sub will be defined in the `cuprate-zmq-pubsub`. It will start 2 sockets, the `XPUB` socket that will listen for inbound connections and a `PAIR` socket that Cuprate can send messages to broadcast down, this is the same method monerod uses.

Cuprate will then use the [poll](https://docs.rs/zmq/latest/zmq/fn.poll.html) method with both socket's poll items: https://docs.rs/zmq/latest/zmq/struct.Socket.html#method.as_poll_item.

A message from the `XPUB` socket will be an update to a subscription, either a new one or an unsubscribe and a message down the `PAIR` socket will be a message from the rest of Cuprate. 

### NotifierService

The notifier service will be whats given to the rest of Cuprate, its request type will be the new event to send notifications about and it should have no response.

The NotifierService internally will use the other end of the `PAIR` socket to send requests to the Pub/Sub server.

The request enum for this service should be defined in the `cuprated` binary and the imlmentation of the service should be in `cuprate-zmq-pubsub`.

(We could use atomic bools for if a certain message type is needed to avoid needlessly sending messages down the PAIR socket.)



# Discussion History
## dimalinux | 2024-09-24T05:28:36+00:00
I wrote some code to grab samples of the different ZMQ messages that are subscribable on monerod's `--zmq-pub` port and stored them in a gist:
https://gist.github.com/dimalinux/50cc09956618f4322520246b5ec132dc

What is the next step for this issue? Do you want a `cuprate-zmq-types` crate with 5 top-level message types? Is the goal that the types will serialize to 100% identical JSON with what `monerod` generates? Looking through that JSON output, there are a lot of obsolete fields that could potentially be eliminated given that this API doesn't return information from old blocks.

## Boog900 | 2024-09-25T12:43:37+00:00
> Do you want a cuprate-zmq-types crate with 5 top-level message types

Yeah that would be a good place to start, and yes identical output. Although some of the fields are obsolete some users could still be relying on then being present so, for now at least, I would include them.

The block/tx JSON output looks the same as it would appear in the JSON RPC, @hinto-janai it might be a good idea to define the JSON encoding for txs/blocks in cuprate-helper or even another crate as it would probably be useful for monero-oxide related crates as well.

# Action History
- Created by: Boog900 | 2024-06-27T19:20:06+00:00
