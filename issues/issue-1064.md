---
title: 'Cuprate Meeting #19 - Tuesday, 2024-09-03, UTC 18:00'
source_url: https://github.com/monero-project/meta/issues/1064
author: moo900
assignees: []
labels: []
created_at: '2024-08-27T18:51:11+00:00'
updated_at: '2024-09-03T19:00:15+00:00'
type: issue
status: closed
closed_at: '2024-09-03T19:00:15+00:00'
---

# Original Description
[Cuprate](https://github.com/Cuprate/cuprate) is an effort to create an alternative Monero node implementation.

Location: [Libera.chat, #cuprate](https://libera.chat/) | [Matrix](https://matrix.to/#/#cuprate:monero.social?via=matrix.org&via=monero.social)

[Join the Monero Matrix server if you don't already have a Matrix account](https://www.getmonero.org/resources/user-guides/join-monero-matrix.html)

Time: 18:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html)

Moderator: @Boog900

Please comment on GitHub in advance of the meeting if you would like to propose a discussion topic.

Main discussion topics:

- Greetings
- Updates: What is everyone working on?
- Project: What is next for Cuprate?
- Any other business

Previous meeting with logs: #1059

# Discussion History
## moo900 | 2024-09-03T19:00:14+00:00
## Meeting logs
```
hinto: hello
```
```
syntheticbird: Hi github
```
```
boog900: 2) Updates 
```
```
boog900: Me: I have been working on adding alt blocks to the DB, I have done some things slightly differently than the issue which I will have to update. I'll hopefully have that PR ready soon 
```
```
boog900: Then I'll get back to work on the blockchain manager 
```
```
hinto: me: starting on RPC handlers, all the mappings/signatures are probably done: https://github.com/Cuprate/cuprate/pull/262
```
```
boog900: 3. Project: What is next for Cuprate?
```
```
hinto: boog900: I think I'll be doing what you said here https://github.com/Cuprate/cuprate/issues/106#issuecomment-2141023700 and splitting `cuprate_rpc_interface::RpcHandler` into 3 `tower::Service`s, one for each enum type
```
```
hinto: the `RpcRequest/RpcResponse` type that exists has 300+ byte differences in some variants, which is a bit too much IMO
```
```
syntheticbird: 300 byte stack-wise?
```
```
hinto: I thought about making `RpcHandler` just be a `tower::Service<$($ALL_REQUEST_TYPES)*>` but that may be too unwieldy? we wouldn't have to deal with enums though
```
```
hinto: > <@syntheticbird:monero.social> 300 byte stack-wise?

yes
```
```
syntheticbird: > <@hinto:monero.social> I thought about making `RpcHandler` just be a `tower::Service<$($ALL_REQUEST_TYPES)*>` but that may be too unwieldy? we wouldn't have to deal with enums though

That way could permit better optimization or easier check routines at the price of code duplication.
```
```
boog900: > <@hinto:monero.social> boog900: I think I'll be doing what you said here https://github.com/Cuprate/cuprate/issues/106#issuecomment-2141023700 and splitting `cuprate_rpc_interface::RpcHandler` into 3 `tower::Service`s, one for each enum type

yeah that sounds ok to me
```
```
boog900: > <@hinto:monero.social> I thought about making `RpcHandler` just be a `tower::Service<$($ALL_REQUEST_TYPES)*>` but that may be too unwieldy? we wouldn't have to deal with enums though

I don't know if I understand, a Service per request type? 
```
```
hinto: yes, definitely would be automated with a macro though
```
```
boog900: because that API looks like it would need one of every request to call the service 
```
```
boog900: with the duplication where it is 
```
```
boog900: > <@hinto:monero.social> yes, definitely would be automated with a macro though

ah ok the only problem with this would be we wouldn't have middle where that could act over multiple request 
```
```
boog900: > <@hinto:monero.social> yes, definitely would be automated with a macro though

 * ah ok a problem with this would be we wouldn't have middle where that could act over multiple request
```
```
hinto: what middleware were you thinking? we can apply `.layer()` to the `axum::Router` directly which would affect all routes
```
```
boog900: Nothing in mind just wanted to mention 
```
```
hinto: do you think it's worth replacing the `enum`s and doing macro stuff with `tower::Service`?
```
```
boog900: IMO no, I don't think the enums are that bad + it makes the API harder to use 
```
```
syntheticbird: all i know is that I hate monerod macro based rpc map
```
```
syntheticbird: as long as we don't end up like that its fine
```
```
syntheticbird: * as long as we don't end up in this level of macros its fine
```
```
hinto: the alternative would be mapping everything by hand though
```
```
hinto: there's already a bunch of macro maps sorry :D https://github.com/Cuprate/cuprate/blob/main/rpc/interface/src/router_builder.rs#L139-L186
```
```
syntheticbird: > <@hinto:monero.social> there's already a bunch of macro maps sorry :D https://github.com/Cuprate/cuprate/blob/main/rpc/interface/src/router_builder.rs#L139-L186

terrifying
```
```
syntheticbird: but at least its tabbed
```
```
boog900: > <@hinto:monero.social> the alternative would be mapping everything by hand though

We would still need to indicate the type and the respective functions in the macro right?
```
```
boog900: so surly the amount of repetition saved would not be that high
```
```
hinto: the inner body would have to be repeated for every fn?
```
```
hinto: https://github.com/Cuprate/cuprate/blob/main/rpc/interface/src/route/other.rs#L77-L95
```
```
boog900: I'm talking about the inner request service handlers not the current macros 
```
```
hinto: oh yeah they're just a bunch of functions https://github.com/Cuprate/cuprate/pull/262/files#diff-6bc35ce624aad008e6a4081162d6edd5a5cb85bf9eb9ce42e4cd4f757b2b397d
```
```
boog900: I don't mind macro-ing the inner request handler functions if you think that would be helpful, I just don't really want 100+ services 
```
```
hinto: is 3 `tower::Service`s ok then? `trait RpcHandler: Service<JsonRpcRequest> + Service<BinRequest> + Service<OtherRequest>`
```
```
syntheticbird: Deal!
```
```
boog900: yeah that's fine 
```
```
hinto: another thing: what `Future` did you want cuprated's `RpcHandler` to return? `InfallibleOneshotReceiver`?
```
```
hinto: surely we can do a pool system so we don't have to allocate a new `Arc` per RPC request?
```
```
hinto: infact we should probably do that with the DB too?
```
```
syntheticbird: > <@hinto:monero.social> surely we can do a pool system so we don't have to allocate a new `Arc` per RPC request?

isn't this like a requirement for shared state in axum?
```
```
boog900: cloning Arcs does not allocate AFAIK
```
```
syntheticbird: yes it just increase the counter *atomically*. It can cause mayhem for the cpu scheduler under high-parallelism
```
```
boog900: it's just an atomic increment pointing to the same heap data 
```
```
syntheticbird: but that's unnoticeable until you go over 20 threads
```
```
boog900: > <@hinto:monero.social> another thing: what `Future` did you want cuprated's `RpcHandler` to return? `InfallibleOneshotReceiver`?

`BoxFuture` would be the easiest 
```
```
boog900: And the cheapest thing currently possible I think, `InfallibleOneshotReceiver` would be more expensive here.
```
```
hinto: what about a pool system? i.e. `call()` returns a handle you `await` on _for_ the channel but not the channel itself
```
```
hinto: the channels are allocated upfront at once, i.e `ConnectionPool::new(1000)`
```
```
hinto: essentially a reader slot table
```
```
syntheticbird: honestly i would like to benchmark this but otherwise it sounds good to me
```
```
hinto: FYI this isn't some new proposal from me, this is usually referred as a DB connection pool in other non-embedded DB impls
```
```
hinto: https://docs.rs/sqlx/latest/sqlx/pool/
```
```
syntheticbird: that must be what I used with Postgresql crate then
```
```
syntheticbird: yeah i see
```
```
syntheticbird: Sacrificing memory-efficiency to limit allocations/deallocations. This is sound.
```
```
boog900: I would think the cost of allocation wouldn't be that high compared to the total cost of the call 
```
```
boog900: so it's dependent on how complicated this is to implement IMO 
```
```
hinto: ok we can always do perf stuff later, will use `BoxFuture` for now then
```
```
boog900: That would be my recommendation 
```
```
boog900: I think there are probably lots of places we could do things slightly more efficiently  
```
```
boog900: 4. Any other business
```
```
syntheticbird: can we please try to convince moo to have a profile picture
```
```
boog900: moo is already on life support 
```
```
boog900: a pfp might end them 
```
```
syntheticbird: ok that's fair
```
```
hinto: boog900: did you have any thoughts on what a new `get_txpool_backlog/get_output_distribution` API should look like?
```
```
boog900: do we need a new API, I thought we were just changing the data format 
```
```
syntheticbird: > <@hinto:monero.social> boog900: did you have any thoughts on what a new `get_txpool_backlog/get_output_distribution` API should look like?

is this the actual NWLB discussion?
```
```
hinto: yes but which data format?
```
```
syntheticbird: json + hex?
```
```
hinto: my choice was to do full JSON + full binary version, no hex
```
```
boog900: > <@hinto:monero.social> my choice was to do full JSON + full binary version, no hex

yeah I think I agree with this
```
```
boog900: If we already have the `bin` endpoint no need for hex in JSON as well 
```
```
boog900: anything else anyone wants to discuss?
```
```
syntheticbird: I think we can end here
```
```
boog900: Thanks everyone!
```
```
syntheticbird: thanks
```

# Action History
- Created by: moo900 | 2024-08-27T18:51:11+00:00
- Closed at: 2024-09-03T19:00:15+00:00
