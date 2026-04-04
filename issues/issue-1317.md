---
title: 'Cuprate Meeting #83 - Tuesday, 2026-01-06, UTC 18:00'
source_url: https://github.com/monero-project/meta/issues/1317
author: moo900
assignees: []
labels: []
created_at: '2025-12-23T20:54:59+00:00'
updated_at: '2026-01-06T18:24:17+00:00'
type: issue
status: closed
closed_at: '2026-01-06T18:24:17+00:00'
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

Previous meeting: #1316

# Discussion History
## moo900 | 2026-01-06T18:24:16+00:00
## Meeting logs
```
boog900: 1)greetings
```
```
hinto: hello hello
```
```
boog900: 2) updates
```
```
m-relay: <p​lowsof> 👋
```
```
boog900: Me: Continuing my work on the tapes database, I am in the process of moving away from memory maps and chnaging the way we synchronize access. 

The current method for synchronization wont allow cross process access, however last meeting I said it would. 
```
```
boog900: * Me: Continuing my work on the tapes database, I am in the process of moving away from memory maps and chnaging the way we synchronize access. 

The new method for synchronization wont allow cross process access, however last meeting I said it would. 
```
```
boog900: I have thought about it and I just don't think cross process access is necessary 
```
```
boog900: and not having it makes it so much simpler. 
```
```
hinto: me: continuing work on PoWER; another thing came up over the holidays I think is worth mentioning to this group although I'll announce it when the time is right (if it ever is)
```
```
boog900: secret hinto project 👀
```
```
hinto: IMO this is fine although in practice it means it will be one of us creating external programs that access the DB  
```
```
hinto: either that or the API becomes polished for easy public use (unlikely, I think)
```
```
boog900: it means that you can't read the DB while Cuprate is running so any data you want you'll need to go through RPC or integrate directly into the node. 
```
```
boog900: https://github.com/Cuprate/cuprate/issues/516
```
```
hinto: reminder that 516 is an opportunity to create "The API Spec v2" that starts from scratch without being held back by RPC and monerod-isms
```
```
hinto: (which a potential websocket interface could be built on-top of)
```
```
kayabanerve: I would love support for batch JSON-RPC requests.
```
```
boog900: tbf we can just expose the DB handle directly 
```
```
kayabanerve: That could even be done on top of the current Monero RPC though.
```
```
boog900: 3) Project: What is next for Cuprate?
```
```
boog900: I'll keep it in mind but just getting RPC working at all is the current target :)
```
```
boog900: I don't plan to spend much more time on the database then I'll split if from the RPC changes and PR it.
```
```
boog900: * I don't plan to spend much more time on the database then I'll split it from the RPC changes and PR it.
```
```
boog900: I don't have anything else I want to discuss today.
```
```
boog900: hinto: do you have anything you would like to discuss? 
```
```
hinto: nope, back to work
```
```
boog900: thanks everyone.
```
```
boog900: !meeting 
```

# Action History
- Created by: moo900 | 2025-12-23T20:54:59+00:00
- Closed at: 2026-01-06T18:24:17+00:00
