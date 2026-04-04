---
title: 'Cuprate Meeting #88 - Tuesday, 2026-02-03, UTC 18:00'
source_url: https://github.com/monero-project/meta/issues/1332
author: moo900
assignees: []
labels: []
created_at: '2026-01-27T18:26:39+00:00'
updated_at: '2026-02-03T18:25:57+00:00'
type: issue
status: closed
closed_at: '2026-02-03T18:25:57+00:00'
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

Previous meeting: #1329

# Discussion History
## moo900 | 2026-02-03T18:25:56+00:00
## Meeting logs
```
boog900: 1) greetings 
```
```
hinto: hello
```
```
m-relay: <p​lowsof> 👋
```
```
syntheticbird: hello
```
```
boog900: 2) updates 
```
```
syntheticbird: Me: realized one proptest in the onion_addr.rs was wrongly implemented. `addr in [a-z][2-7]{56}` should be `addr in [[a-z][2-7]]{56}`
```
```
boog900: I had a busy week but I managed to add block popping and alt block handling to the new DB, I will PR it in the next couple of days. 
```
```
hinto: me: posted a CCS update: https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/591#note_34171 - I've opened PoWER for initial review and will be fixing the merge conflicts then start focusing on Cuprate again
```
```
syntheticbird: Nice. I was confused on if it was ready to review or not ngl
```
```
boog900: > Project: What is next for Cuprate?
```
```
boog900: * 3. Project: What is next for Cuprate?
```
```
hinto: to be clear the `seraphis-migration` PR is open, the Cuprate crate and integration will wait until it's merged
```
```
boog900: With the new database done I will be back on the RPC 
```
```
boog900: Wallet catch up is already done and is quick 
```
```
syntheticbird: Did you test multiple simultaneous clients scenario ?
```
```
syntheticbird: or is this with only one wallet?
```
```
boog900: Nope, just one 
```
```
boog900: Although I think that would be even faster 
```
```
syntheticbird: because of cache?
```
```
boog900: Comparing to monerod 
```
```
syntheticbird: ah ok
```
```
boog900: Ah yeah it'll be slower than just 1 most likely, maybe on a HDD it would be quicker though as yeah data could be cached 
```
```
boog900: Does anyone have anything they would like to discuss?
```
```
hinto: I think I'll be continuing on bootstrappable builds and misc stuff
```
```
hinto: not sure if that takes precedence over ZMQ although last time I was going through that code it was boring work :D
```
```
boog900: I would put them at similar levels, ZMQ is only really used for lws and p2pool IIRC
```
```
boog900: And reproducible builds would be needed for a beta release IMO 
```
```
boog900: Anything else to discuss today?
```
```
syntheticbird: i think we're all good
```
```
boog900: OK I'll end it here
```
```
boog900: Thanks everyone
```
```
syntheticbird: Thanks
```

# Action History
- Created by: moo900 | 2026-01-27T18:26:39+00:00
- Closed at: 2026-02-03T18:25:57+00:00
