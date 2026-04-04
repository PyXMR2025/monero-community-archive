---
title: 'Cuprate Meeting #51 - Tuesday, 2025-04-15, UTC 18:00'
source_url: https://github.com/monero-project/meta/issues/1185
author: moo900
assignees: []
labels: []
created_at: '2025-04-08T19:05:10+00:00'
updated_at: '2025-04-15T18:55:01+00:00'
type: issue
status: closed
closed_at: '2025-04-15T18:55:01+00:00'
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

Previous meeting: #1181

# Discussion History
## moo900 | 2025-04-15T18:55:00+00:00
## Meeting logs
```
boog900: 1) greetings 
```
```
syntheticbird: Hello
```
```
syntheticbird: Hinto is dead it's over
```
```
hinto: hi
```
```
boog900: 2) Updates
```
```
boog900: Me: working on reversing reorgs to bad chains, also made a new command for broadcasting txs and have broadcasted a tx using cuprated 
```
```
syntheticbird: me: continue on the first transport PR, asked cuprate-docker repository owner if we could upstream their dockerfile, they sad yes
```
```
hinto: me: nothing new, continuing work on the RPC server impl and the testing harness
```
```
boog900: 3) Project: What is next for Cuprate?
```
```
boog900: anything anyone wants to discuss today?
```
```
hinto: boog900: did you see 437? there are some release related questions
```
```
syntheticbird: Regarding fast_sync_hashes.json i'm not against the idea
```
```
m-relay: <N​orrinRadd> Hi All
```
```
m-relay: <N​orrinRadd> I started working on persisting the ban list
```
```
m-relay: <N​orrinRadd> I'm thinking just store it to the same file as the while list and grey list? 
```
```
m-relay: <N​orrinRadd> Just looking at the crate docs to make sure I know how it serializes and deserializes that. 
```
```
boog900: > <@hinto:monero.social> boog900: did you see 437? there are some release related questions

yeah IMO the automation is probably not worth it, the required changes are not that extensive. 

For `fast_sync_hashes.bin` I wouldn't mind making it a JSON file with a build script to keep the current type the same. 
```
```
boog900: > <N​orrinRadd> I'm thinking just store it to the same file as the while list and grey list?

Yeah sounds good 
```
```
boog900: > Just looking at the crate docs to make sure I know how it serializes and deserializes that.

you may find it useful to see what William did here: https://github.com/willco-1/cuprate they got quite far before stopping tbf 
```
```
m-relay: <N​orrinRadd> sounds good 
```
```
m-relay: <N​orrinRadd> "anything anyone wants to discuss today?"
```
```
m-relay: <N​orrinRadd> is there a rough plan on the order of operations for RPC work? 
```
```
hinto: 1. Dummy RPC server (423)
1. Enable endpoints that work now (future PR)
1. Finish testing harness (422)
1. Enable individual endpoints as they are tested (future PRs)
```
```
hinto: speaking of, boog900 Literally Public what should the behavior of disabled endpoints be?
```
```
syntheticbird: Will they be present in the router?
```
```
hinto: we could disable them via the router or return `Default::default()` like https://doc.cuprate.org/cuprate_rpc_interface/struct.RpcHandlerDummy.html
```
```
hinto: I guess disabling it via the router makes more sense
```
```
syntheticbird: you can also just set the endpoints handler to `any(async || { StatusCode::NOT_IMPLEMENTED })`
```
```
syntheticbird: https://docs.rs/http/1.2.0/http/status/struct.StatusCode.html#associatedconstant.NOT_IMPLEMENTED
```
```
syntheticbird: HTTP 501 would make more sense than HTTP 404
```
```
boog900: anything else anyone wants to discuss or we can end here?
```
```
syntheticbird: yes
```
```
syntheticbird: moo's profile picture
```
```
boog900: meetings over
```
```
syntheticbird: thanks
```
```
boog900: Thanks everyone!
```
```
hinto: wait, I'd like to test something
```

# Action History
- Created by: moo900 | 2025-04-08T19:05:10+00:00
- Closed at: 2025-04-15T18:55:01+00:00
