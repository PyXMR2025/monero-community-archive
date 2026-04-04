---
title: 'Cuprate Meeting #87 - Tuesday, 2026-01-27, UTC 18:00'
source_url: https://github.com/monero-project/meta/issues/1329
author: moo900
assignees: []
labels: []
created_at: '2026-01-20T18:37:28+00:00'
updated_at: '2026-01-27T18:26:40+00:00'
type: issue
status: closed
closed_at: '2026-01-27T18:26:40+00:00'
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

Previous meeting: #1327

# Discussion History
## moo900 | 2026-01-27T18:26:38+00:00
## Meeting logs
```
boog900: 1) greetings
```
```
kayabanerve: 👋
```
```
boog900: Quiet meeting today
```
```
boog900: 2) updates
```
```
m-relay: <p​lowsof> 👋
```
```
boog900: Me: I removed the underlying database abstraction crate and moved our tx pool over to fjall. This will allow us to have concurrent tx pool write operations although I have kept it single writer for now. 
```
```
boog900: I have also joined the txpool database to the blockchain one. Fjall is more of a heavy database than LMDB so having 2 instances is wasteful. 
```
```
boog900: I still need to work on popping blocks and alt blocks and updating tests but I don't expect that will take too long, then I can PR the new DB. 
```
```
boog900: 3) Any other business
```
```
boog900: Does anyone have anything they would like to discuss?  
```
```
m-relay: <p​lowsof> thanks for sharing your update 💪
```
```
boog900: Thanks for joining the meeting :) 
```
```
boog900: I'll end it here 
```
```
boog900: !meeting 
```

# Action History
- Created by: moo900 | 2026-01-20T18:37:28+00:00
- Closed at: 2026-01-27T18:26:40+00:00
