---
title: 'Cuprate Meeting #81 - Tuesday, 2025-12-23, UTC 18:00'
source_url: https://github.com/monero-project/meta/issues/1312
author: moo900
assignees: []
labels: []
created_at: '2025-12-16T18:25:00+00:00'
updated_at: '2025-12-23T18:46:30+00:00'
type: issue
status: closed
closed_at: '2025-12-23T18:46:30+00:00'
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

Previous meeting: #1309

# Discussion History
## moo900 | 2025-12-23T18:46:29+00:00
## Meeting logs
```
boog900: 1) greetings 
```
```
syntheticbird: Hi people
```
```
syntheticbird: syn here
```
```
boog900: 2) updates
```
```
syntheticbird: there was a reference
```
```
boog900: me: I did some work hardening RPC sync, making it more stable etc. Also last week I was reading up on some databases and it made me want to give fjall another go. I spent some time integrating it properly and it performs incredibly well.
```
```
hinto: hello, sorry I'm late, update: still working on PoWER for ZMQ
```
```
boog900: 3) Project: What is next for Cuprate?
```
```
boog900: So the main thing I want to discuss today is how we feel about moving to fjall.

The pros are obvious, it is much faster at syncing for every system. The more storage I/O constrained the better the improvement. My NVMe ssd goes from a little over 2hrs to sync to a little over 1hr. My HDD goes from days to weeks, to 1hr 20 mins.  
```
```
hinto: Are fjall DBs readable from multiple processes?
```
```
boog900: The cons are that it is a less battle tested DB. And I don't think it supports multi-process access yet.
```
```
hinto: How is the memory usage compared to LMDB?
```
```
boog900: yeah I think it does if both are read only, but I am unsure about 1 writer 1 reader
```
```
boog900: it is more, but not crazy amounts more. I don't have exact numbers. You can configure how much memory it uses. 
```
```
boog900: I am going to test a sync on a Pi 4 with a USB HDD soon, we'll see then if it can hold up. 
```
```
boog900: pining sgp_ as using fjall will break the block explorer magic made.
```
```
boog900: pinging*
```
```
hinto: Is there a public working branch? I can add test data as well
```
```
hinto: e.g Pi 5 and M4 Mac mini
```
```
boog900: there is a messy public branch for my testing, I wouldn't recommend you running it though as it is full of todos 
```
```
boog900: you _can_ run it but I literally built it out just to test sync 
```
```
hinto: If we do stick to a single DB I suggest removing the others such that we don't have to maintain them
```
```
hinto: `cuprate-database` traits can then be more tailored to represent whichever DB is chosen
```
```
hinto: (if we keep the traits around instead of directly using the DB)
```
```
boog900: currently I am using fjall directly in cuprate-blockchain 
```
```
sgp_: :'(
```
```
sgp_: Ideally I'd like to read it with a different program but I guess we could migrate to RPC or something if you're set on transitioning
```
```
boog900: yeah it is annoying, I do think the performance gains are worth it though 
```
```
boog900: tbf you would still have access to the tapes database which store most of our data 
```
```
boog900: you would only need to fall back to RPC for some data, like hashes to indexes.
```
```
sgp_: don't skip those because of me then, so long as our thingy can be adapted
```
```
boog900: hinto: do you have any objections at the moment ?
```
```
hinto: No, but it should be tested on a few machines before final merge
```
```
boog900: hinto do you have anything else you want to discuss? 
```
```
sgp_: if one of you has some time to put together a basic gist of how we should use it going forward after the change, that would be great. Otherwise we'll figure it out
```
```
hinto: We can end here
```
```
boog900: I'll do that before we merge it to main
```
```
boog900: thanks everyone!
```
```
boog900: !meeting 
```

# Action History
- Created by: moo900 | 2025-12-16T18:25:00+00:00
- Closed at: 2025-12-23T18:46:30+00:00
