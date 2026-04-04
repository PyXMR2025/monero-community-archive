---
title: 'Cuprate Meeting #21 - Tuesday, 2024-09-17, UTC 18:00'
source_url: https://github.com/monero-project/meta/issues/1071
author: moo900
assignees: []
labels: []
created_at: '2024-09-10T19:08:17+00:00'
updated_at: '2024-09-17T18:54:59+00:00'
type: issue
status: closed
closed_at: '2024-09-17T18:54:59+00:00'
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
- logging: https://github.com/Cuprate/cuprate/issues/163

- Any other business

Previous meeting with logs: #1067

# Discussion History
## moo900 | 2024-09-17T18:54:58+00:00
## Meeting logs
```
boog900: meeting time: https://github.com/monero-project/meta/issues/1071
```
```
boog900: 1) Greetings 
```
```
hinto: hello
```
```
boog900: 2) updates 
```
```
hinto: me: working on a new `cuprate_constants` crate which will close https://github.com/Cuprate/cuprate/issues/189 - seems like a good opportunity to do this now as the RPC has some `const`s
```
```
boog900: Me: I continued work on the block manager, I managed to leave it running for a day fully synced, verifying new blocks with no issues.

I also started work on the txpool in `cuprated`, however I realized it is going to require some changes to the P2P client pool, which is what I am currently working on. 
```
```
boog900: 3) Project: What is next for Cuprate?

```
```
hinto: I think I'll be adding required service message types for RPC, then cutting up https://github.com/Cuprate/cuprate/pull/272 into smaller PRs for the next couple weeks
```
```
hinto: boog900: have you looked at this issue yet?: https://github.com/Cuprate/cuprate/issues/278
```
```
boog900: > <@hinto:monero.social> boog900: have you looked at this issue yet?: https://github.com/Cuprate/cuprate/issues/278

I skimmed it, for `get_connections` we do store the `peer_id` however we don't have a `connection_id`
```
```
boog900: also we wont have a bad blocks/transactions cache 
```
```
hinto: I'll make an architecture book PR to track these, maybe it'll be easier to settle different semantics there
```
```
boog900: - [Logging](Cuprate/cuprate#163)
```
```
boog900: I don't know what happened with that link: https://github.com/Cuprate/cuprate/issues/163
```
```
boog900: I'll aim to create some rough guidelines that we can discuss next meeting but as a start, I think any state changes to the blockchain DB should be an `info` level log, i.e. any new block 
```
```
boog900: This is more verbose than monerod though and hinto I remember you mentioning that we should aim to roughly emit a similar amount of logs 
```
```
hinto: I do remember saying something about logs but it's been so long I forget what I said and why I said it
```
```
kayabanerve: Logs aren't real and if you just keep ignoring them they aren't an issue /s
```
```
kayabanerve: I'd personally advocate for info logs on any state changes which are non-trivial and occur greater than every 5s
```
```
kayabanerve: A new block sounds more than fine to be info, especially if logs are topic'd such that you can opt in/out (as the context here)
```
```
boog900: I think instead of making guidelines I am just going to make a document of what is logged above the `trace` level.
```
```
boog900: I think trying to make guidelines is just going to turn into that anyway 
```
```
syntheticbird: > <@boog900:monero.social> I think instead of making guidelines I am just going to make a document of what is logged above the `trace` level.

Yes. that's the way
```
```
hinto: it would be worth looking at other projects and see how they handle logging before doing anything
```
```
hinto: was there a specific deadline you wanted logs to be "ready"? or could we just be loose with them until a public release + a giant "fix logging" PR
```
```
hinto: simple logging is mostly easy to modify so it wouldn't be too bad unlike "temporary" code that turns into infrastructure that can' 
```
```
hinto:  * simple logging is mostly easy to modify so it wouldn't be too bad unlike "temporary" code that turns into infrastructure that can't be touched for 10 years
```
```
syntheticbird: > <@hinto:monero.social> was there a specific deadline you wanted logs to be "ready"? or could we just be loose with them until a public release + a giant "fix logging" PR

I think no one on earth want to make a +33000 fix logging PR near release and say to everyone just wait next week we need to fix logs.
```
```
syntheticbird: The +33000 part is the most important.
```
```
syntheticbird: At least you should shard the work into important sections (db, p2p, rpc).
```
```
boog900: I do think an initial binary is pretty close, so hopefully by then 
```
```
boog900: The current log situation is really bad 
```
```
hinto: note: I have not written a single log line :)
```
```
boog900: Yeah we have some sections doing too much and some doing nothing 
```
```
syntheticbird: > <@boog900:monero.social> Yeah we have some sections doing too much and some doing nothing

I would gladly take the nothing
```
```
boog900: Not if you are trying to test a sync :p
```
```
boog900: 4) Any other business

```
```
boog900: anything else anyone wants to discuss in this meeting?
```
```
boog900: ok I think we can end here 
```
```
boog900: Thanks everyone!
```
```
hinto: thanks
```
```
boog900: !meeting 
```

# Action History
- Created by: moo900 | 2024-09-10T19:08:17+00:00
- Closed at: 2024-09-17T18:54:59+00:00
