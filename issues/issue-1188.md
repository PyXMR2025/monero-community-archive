---
title: 'Cuprate Meeting #52 - Tuesday, 2025-04-22, UTC 18:00'
source_url: https://github.com/monero-project/meta/issues/1188
author: moo900
assignees: []
labels: []
created_at: '2025-04-15T18:55:00+00:00'
updated_at: '2025-04-22T19:02:02+00:00'
type: issue
status: closed
closed_at: '2025-04-22T19:02:01+00:00'
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

Previous meeting: #1185

# Discussion History
## moo900 | 2025-04-22T19:02:00+00:00
## Meeting logs
```
syntheticbird: monero.social seems laggy today
```
```
boog900: 1) greetings
```
```
syntheticbird: hello
```
```
boog900: > <@syntheticbird:monero.social> monero.social seems laggy today

Yeah
```
```
syntheticbird: We can wait for hinto
```
```
hinto: hello
```
```
boog900: 2) updates 
```
```
syntheticbird: me: finished changes to p2p-core and p2p. actually on p2p-transport trait
```
```
syntheticbird: * me: finished changes to p2p-core and p2p. actually on p2p-transport crate
```
```
boog900: Me still working on reversing bad reorgs, will probably open the PR today 
```
```
hinto: me: I've posted a CCS update: https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/543#note_29699
```
```
syntheticbird: At this rate the reorg code will need a big disclaimer *a la bytemuck in database*
```
```
boog900: 3) Project: What is next for Cuprate?
```
```
syntheticbird: I would have two questions
```
```
syntheticbird: no actually just one
```
```
boog900: Go on ....
```
```
syntheticbird: The current P2P code implement sending timeout within p2p crate (iirc). I would like to move this protection to p2p transort `Tcp` transport implementation, with a 20s write timeout and 30s read timeout
```
```
syntheticbird: `p2p/p2p-core/src/clients/connections.rs#L131`
```
```
boog900: Why do we need a read timeout? This should be handled where it currently is imo
```
```
boog900: For the write timeout that sounds good 
```
```
syntheticbird: In case the peer is solely reading our request but not sending anything
```
```
syntheticbird: sounds good = should we move it?
```
```
syntheticbird: Also one of advantage of passing this into Transport is that it can be configurable. So possibly better stability for high traffic nodes
```
```
boog900: > <@syntheticbird:monero.social> In case the peer is solely reading our request but not sending anything

This is better handled in the connection task like it currently is imo
```
```
boog900: > <@syntheticbird:monero.social> sounds good = should we move it?

Yeah we would be able to use the same type for RPC as well 
```
```
syntheticbird: got it
```
```
syntheticbird: I'll implement it within `cuprate-helper`
```
```
hinto: types shared between RPC and another subsystem should be in: https://doc.cuprate.org/cuprate_types/rpc/index.html
```
```
hinto: I think `cuprate_helper` is mostly for fn/trait, we could also merge these crates together, not sure if it matters too much
```
```
syntheticbird: from what im seeing cuprate-helper is likely more appropriate since it will implement Future trait and some minimal constructor
```
```
boog900: If I am honest I dont really like these crates anyway 
```
```
boog900: I would rather them be removed/their scope be significantly reduced 
```
```
boog900: But long term goal probably not something that I want to deal with now
```
```
hinto: oh my bad, I agree, didn't see the type in question
```
```
hinto: boog900: which crates/modules and how? 
```
```
syntheticbird: im perplex too, how would the types be distributed?
```
```
syntheticbird: * im perplex too, where would these types/fns be distributed?
```
```
syntheticbird: i actually like the helper crate
```
```
syntheticbird: * im perplex too, where would these types/fns be dispatched?
```
```
boog900: The kitchen sink crates, helper and types. I don't like how rpc p2p and database types are all in there which leads to annoying feature flags. 
```
```
boog900: I think we can better structure things/ make other crates to reduce the kitchen sink crates scope. Which should minimize the feature flags 
```
```
boog900: For example these crates were really annoying when trying to get 32 bit support
```
```
syntheticbird: fair enough
```
```
hinto: something like `cuprate-types-{blockchain,p2p,json}` where the modules are in their own crate?
```
```
boog900: That would be a simple solution, this problem isn't urgent though so not worth spending energy on now IMO  
```
```
boog900: Anything else anyone would like to discuss today 
```
```
hinto: for types that are shared across multiple crates like https://github.com/Cuprate/cuprate/blob/main/types/types/src/address_type.rs, would `cuprate-types` still be the appropriate place?
```
```
boog900: > <@hinto:monero.social> for types that are shared across multiple crates like https://github.com/Cuprate/cuprate/blob/main/types/types/src/address_type.rs, would `cuprate-types` still be the appropriate place?

maybe I think it depends, that type for example is just used on a type for the RPC crate in the p2p crate 
```
```
boog900: bit weird layout imo
```
```
boog900: https://github.com/Cuprate/cuprate/blob/474ff9ed6f474789c32436bc560f866164207bbf/p2p/p2p-core/src/types.rs#L29
```
```
syntheticbird: I apologize I have to quit the meeting early. Thanks 👋
```
```
boog900: We could probably structure it better so the P2P returns some info with the types that it uses and then the RPC crate can map them how it wants 
```
```
boog900: cuprated would do the mapping*
```
```
hinto: as I go through each endpoint I will try to clean up the relevant types
```
```
boog900: anything else to discuss today or we can end here 
```
```
boog900: ok we can end here, thanks everyone!
```
```
hinto: thanks
```

# Action History
- Created by: moo900 | 2025-04-15T18:55:00+00:00
- Closed at: 2025-04-22T19:02:01+00:00
