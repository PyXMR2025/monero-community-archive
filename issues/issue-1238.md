---
title: 'Cuprate Meeting #65 - Tuesday, 2025-07-22, UTC 18:00'
source_url: https://github.com/monero-project/meta/issues/1238
author: moo900
assignees: []
labels: []
created_at: '2025-07-15T18:42:51+00:00'
updated_at: '2025-07-22T18:47:42+00:00'
type: issue
status: closed
closed_at: '2025-07-22T18:47:42+00:00'
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

Previous meeting: #1234

# Discussion History
## moo900 | 2025-07-22T18:47:41+00:00
## Meeting logs
```
boog900: 1) greetings 
```
```
syntheticbird: moooooooooo!
```
```
boog900: 2) updates
```
```
boog900: Me: I have been taking it slow with Cuprate, will be back full time from now though. I have opened a draft PR with some changes I made a while ago for the network scanner. 
```
```
syntheticbird: Me: Addressed recent review on #509.
```
```
boog900: 3) Project: What is next for Cuprate?
```
```
syntheticbird: monerod has received a PR for fuzz of rpc endpoints
```
```
syntheticbird: any plans on our side for that
```
```
syntheticbird: cargo fuzz is a great infra
```
```
boog900: we already have fuzzing set up 
```
```
boog900: pretty limited currently though 
```
```
boog900: hinto: 
```
```
syntheticbird: yeah think it's just the parser right
```
```
boog900: a couple others too 
```
```
syntheticbird: i see that
```
```
boog900: the next release will probably have a breaking change for the tx-poll DB 
```
```
boog900: * the next release will probably have a breaking change for the tx-pool DB 
```
```
boog900: currently I just exit with a message to delete the DB, do we think this is the best way?
```
```
syntheticbird: with a message to delete the dB ?
```
```
syntheticbird: im not sure to understand
```
```
boog900: https://github.com/Cuprate/cuprate/blob/txpool-manager2/storage/txpool/src/free.rs#L98
```
```
syntheticbird: Oh
```
```
syntheticbird: This is the txpool. It's ephemeral by itself, you could probably delete it
```
```
syntheticbird: * This is the txpool. It's ephemeral by itself, you could probably replace it automatically on startup
```
```
boog900: true I would rather be too conservative though 
```
```
syntheticbird: im fine with both approach
```
```
boog900: anything else to discuss today?
```
```
syntheticbird: not from me
```
```
boog900: I think we can end here then 
```
```
boog900: Thanks SyntheticBovinae
```
```
boog900: !meeting 
```

# Action History
- Created by: moo900 | 2025-07-15T18:42:51+00:00
- Closed at: 2025-07-22T18:47:42+00:00
