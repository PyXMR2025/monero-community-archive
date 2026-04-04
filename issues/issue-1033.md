---
title: 'Cuprate Meeting #11 - Tuesday, 2024-07-09, UTC 18:00'
source_url: https://github.com/monero-project/meta/issues/1033
author: moo900
assignees: []
labels: []
created_at: '2024-07-02T18:58:52+00:00'
updated_at: '2024-07-09T19:07:33+00:00'
type: issue
status: closed
closed_at: '2024-07-09T19:07:33+00:00'
---

# Original Description
[Cuprate](https://github.com/Cuprate/cuprate) is an effort to create an alternative Monero node implementation.

Location: [Libera.chat, #cuprate](https://libera.chat/) | [Matrix](https://matrix.to/#/#cuprate:monero.social?via=matrix.org&via=monero.social)

> Note that there are currently communication issues with Matrix accounts created on the matrix.org server, consider using a different homeserver to see messages.

[Join the Monero Matrix server if you don't already have a Matrix account](https://www.getmonero.org/resources/user-guides/join-monero-matrix.html)

Time: 18:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html)

Moderator: @Boog900

Please comment on GitHub in advance of the meeting if you would like to propose a discussion topic.

Main discussion topics:

- Greetings
- Updates: What is everyone working on?
- Project: What is next for Cuprate?
- How to handle binary blobs in JSON?

- Any other business

Previous meeting with logs: #1029

# Discussion History
## moo900 | 2024-07-09T19:07:32+00:00
## Meeting logs
```
boog900: meeting time: https://github.com/monero-project/meta/issues/1033
```
```
boog900: 1. Greetings 
```
```
yamabiiko: Hi
```
```
hinto: hi
```
```
boog900: 2. Updates
```
```
boog900: Me: I started work on handling alt-blocks. I also spent the last few days working on documenting the P2P protocol. Hopefully I'll have that finished by tomorrow and can claim the last milestone of my last CCS  
```
```
hinto: me: finished porting all RPC types, the resulting discrepancies list: https://github.com/Cuprate/cuprate/issues/159
```
```
yamabiiko: Went a bit deeper with how ZMQ is implemented in monerod, imo there is not much to add to the current design proposal apart from expanding on the `NotifierService`
```
```
yamabiiko:  * Went a bit deeper with how ZMQ is implemented in monerod, imo there is not much to add to the current design proposal apart from expanding on the `NotifierService`
```
```
syntheticbird: me: No update, despite my my statement at last meeting, I haven't been able to work this week.
```
```
syntheticbird:  * me: No update, despite my statement at last meeting, I haven't been able to work this week.
```
```
fluorescent_beige: I started working on issue #209, make database backends swappable at runtime. So far we just discussed different approaches, will try to plan + implement until next week
```
```
boog900: Lets move onto: 

3. Project: What is next for Cuprate?
```
```
boog900: I did want to make a decision on this: `How to handle binary blobs in JSON?`
```
```
boog900: I think the only practical option is to have custom functions that manually write out these types, seen as there are only 2 types like this I don't think it's too bad 
```
```
boog900: and we just forget about trying to deserialize them 
```
```
hinto: agreed, I'd also like to push to replace these with either full JSON or full binary endpoints/methods eventually
```
```
hinto: does anyone have a clue as to why these even exist? Why not go full JSON or binary? Mixing them in this manner is the worst of both worlds and breaks JSON spec
```
```
syntheticbird: probably because the packet is large, 4kb from one of my test, compressed
```
```
syntheticbird: they didn't wanted to make http compression so ended up compressing the json infos and pushing it into the struct
```
```
boog900: The responses I was getting from the endpoint I was testing was not that large 
```
```
syntheticbird: > <@boog900:monero.social> The responses I was getting from the endpoint I was testing was not that large

weird. hold on i'll check that rq
```
```
boog900: I think it is an efficiency thing, but realistically the gains are not worth it, encoding the bytes as hex would be significantly better for not too much overhead 
```
```
yamabiiko: > <@yamabiiko:unitoo.it> Went a bit deeper with how ZMQ is implemented in monerod, imo there is not much to add to the current design proposal apart from expanding on the `NotifierService`

Speaking of which, any thoughts/remarks on a general notification service for cuprate? 
```
```
syntheticbird: > <@syntheticbird:monero.social> weird. hold on i'll check that rq

nvm deleted the folder. Your point is still right. It's not worth it
```
```
syntheticbird: > <@yamabiiko:unitoo.it> Speaking of which, any thoughts/remarks on a general notification service for cuprate?

I haven't followed. A notification service for who? client? over zmq? http endpoint?
```
```
boog900: > <@yamabiiko:unitoo.it> Speaking of which, any thoughts/remarks on a general notification service for cuprate?

IMO the `NotifierService` API should not be zmq specific, however I don't think it should be used to send messages to Cuprate components.

So currently the `NotifierService` will only send messages to ZMQ however in the future, it _could_ do more.
```
```
yamabiiko: ZMQ pub/sub is used to notify clients for changes to the chain and new txpool transaction
```
```
boog900: does anyone else have anything they want to discuss here?
```
```
syntheticbird: has moo900 been fixed ?
```
```
yamabiiko: Why does moo have 200+ sessions?
```
```
hinto: boog900: lints :)
```
```
hinto: yamabiiko: hmm some implementation detail of `matrix-sdk` I assume
```
```
boog900: I forgot :(
```
```
hinto: !add 133
```
```
moo: [133] added to queue (priority: Medium)
```
```
hinto: timer has started
```
```
hinto: just a reminder: merging that does nothing until crates opt in
```
```
boog900: I will look over it today
```
```
boog900: 4. Any other business

```
```
hinto: maybe we could discuss a fix for https://github.com/Cuprate/cuprate/issues/149?
```
```
hinto: the most practical and easiest option I see is just mapping `SyncMode::{Async,Fast}` to the same `redb::Eventual` at https://github.com/Cuprate/cuprate/blob/0622237d19e655fa68b3814c4e3d2ac5b3f71fb8/storage/cuprate-blockchain/src/backend/redb/env.rs#L60-L61
```
```
boog900: yeah I think that's the best option
```
```
hinto: it isn't quite the same semantically as LMDB leaving it up to whenever the OS feels like it but the only other option I see is creating custom logic that syncs every `x` seconds, blocks, etc
```
```
boog900: Using fast sync we should be able to batch add blocks to the DB with a single tx so I don't think there will enough difference to justify it 
```
```
boog900: I am excited to test our fast sync performance 
```
```
boog900: anything else to discuss or can we end here?
```
```
hinto: yamabiiko: do you have any timeline for work on ZMQ?
```
```
yamabiiko: I am planning to apply for a CCS this week, however I don't expect that it'd take more than 1/1.5 months so was looking for other tasks as well aside from documenting
```
```
yamabiiko: Side note: when is the architecture book going to be started ?
```
```
boog900: soon™️
```
```
hinto: I haven't written any RPC stuff for it yet, the DB section still needs porting
```
```
hinto: I haven't upstreamed my repo (`cuprate-architecture`) into Cuprate yet because things will change and there's going to be a lot of diff noise
```
```
hinto: boog900: if you're okay with this I could upstream it
```
```
boog900: yeah I am, I will probably start writing the P2P sections soon 
```
```
boog900: > <@yamabiiko:unitoo.it> I am planning to apply for a CCS this week, however I don't expect that it'd take more than 1/1.5 months so was looking for other tasks as well aside from documenting

as for other tasks right now I am not sure what will need to be done in ~2 months  
```
```
boog900: It will be good to start with a smaller proposal as well IMO, you could always include that if you finish early you will work on whatever is needed  
```
```
yamabiiko: Yeah just wasn't sure about a "generic" 3rd milestone
```
```
hinto: > <@boog900:monero.social> yeah I am, I will probably start writing the P2P sections soon

okay, this would be nice - I assumed I'd have to write the entire book
```
```
boog900: Ok I think we can end here. Thanks everyone!
```
```
hinto: thanks
```
```
boog900: !meeting 
```

# Action History
- Created by: moo900 | 2024-07-02T18:58:52+00:00
- Closed at: 2024-07-09T19:07:33+00:00
