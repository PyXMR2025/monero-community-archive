---
title: 'Cuprate Meeting #91 - Tuesday, 2026-02-24, UTC 18:00'
source_url: https://github.com/monero-project/meta/issues/1342
author: moo900
assignees: []
labels: []
created_at: '2026-02-17T18:27:00+00:00'
updated_at: '2026-02-24T18:48:42+00:00'
type: issue
status: closed
closed_at: '2026-02-24T18:48:42+00:00'
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

Previous meeting: #1339

# Discussion History
## moo900 | 2026-02-24T18:48:41+00:00
## Meeting logs
```
boog900: 1) greetings
```
```
hinto: hello
```
```
boog900: 2) updates
```
```
boog900: Me: testing the new db and fixing the issues I ran into 
```
```
boog900: A txpool issue was particularly annoying this debug 
```
```
boog900: To*
```
```
hinto: me: took/taking a break from Cuprate for now and have been working on another related project
```
```
boog900: 3) Project: What is next for Cuprate?
```
```
boog900: Are you able to reveal the related project :)
```
```
hinto: perhaps, eventually, maybe
```
```
hinto: I can say that it uses Cuprate and monero-oxide :)
```
```
hinto: was this OOM behavior happening with the old DB? IIRC I had the current cuprated running on a Pi 5 with a 2GB systemd limit
```
```
boog900: No clue I don't think anyone was crazy enough to sync on a system like that 
```
```
boog900: The new db does use more ram though 
```
```
hinto: should Cuprate be prioritizing speed over resource footprint?
```
```
boog900: Up to a point 
```
```
hinto: if we have a belief of who should be node operators in the future then we can focus on one of the qualities moreso
```
```
hinto: if disk/memory prices keep spiking perhaps we'll all be priced out sooner than later :D
```
```
m-relay: <s​elsta> I have a question, afaik LMDB was always chosen for read speed and not the write speed, so we knew that initial sync would be slower in favour of faster reads later. How is that with the new DB system chosen by Cuprate?
```
```
boog900: IMO 2 GB is already below the minimum amount of RAM for a monero node
```
```
boog900: The fact we can fast sync and probably can full verify sync shows the DB doesn't use crazy amounts of RAM not that 2 GB is fine for cuprated 
```
```
boog900: Like itll only take a bit of spam to OOM a node with 2 GB on the old DB 
```
```
boog900: Selsta: the tapes DB is faster than LMDB for random reads. The tapes db is used for RCT outputs so for that we should be more efficient. For pre rct it would be slower however in my tests this doesn't actually slow it down at all. Presumably lookups make up a much smaller proportion of the time compared to the other things that need to be done during verification.
```
```
boog900: I did a full verification sync in under 15 hrs with the new DB 
```
```
m-relay: <s​elsta> really impressive and shows that there are still a lot of possible performance gains also in monerod
```
```
boog900: Anything else to discuss today?
```
```
boog900: Ah I don't think I answered why fjall was chosen 
```
```
boog900: It was chosen as its underlying "format" is a LSM, which is much better at writes than LMDB. Plus its in  rust 
```
```
boog900: We could have gone with rocksDB 
```
```
syntheticbird: no
```
```
syntheticbird: rocksDb is dogshit
```
```
boog900: Lol
```
```
boog900: Yeah its also doesn't have a good reputation
```
```
boog900: I'll end here 
```
```
boog900: Thanks everyone
```

# Action History
- Created by: moo900 | 2026-02-17T18:27:00+00:00
- Closed at: 2026-02-24T18:48:42+00:00
