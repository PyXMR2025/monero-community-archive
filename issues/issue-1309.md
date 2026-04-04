---
title: 'Cuprate Meeting #80 - Tuesday, 2025-12-16, UTC 18:00'
source_url: https://github.com/monero-project/meta/issues/1309
author: moo900
assignees: []
labels: []
created_at: '2025-12-09T18:27:25+00:00'
updated_at: '2025-12-16T18:25:01+00:00'
type: issue
status: closed
closed_at: '2025-12-16T18:25:01+00:00'
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

Previous meeting: #1306

# Discussion History
## moo900 | 2025-12-16T18:25:00+00:00
## Meeting logs
```
boog900: 1) greetings
```
```
syntheticbird: Goodbye
```
```
syntheticbird: Good morning
```
```
hinto: hello
```
```
boog900: 2) updates
```
```
boog900: Me: I spent some time investigating an issue with wallet sync, turns out axum drops connections after responding if you don't read the whole request.
```
```
boog900: Wallet syncing is otherwise going good, ran into another issue today that looks to be on the cli side but it seems to be rare. 
```
```
syntheticbird: if it doesn't read the whole request? You mean client reading response, or server reading request
```
```
boog900: server handling request. If we don't decode the JSON for example, axum will respond but after responding will drop the connection. 
```
```
hinto: me: started attempting Guix and StageX on more complicated repos including `Cuprate/cuprate` and stopped at dep compile issues, moved onto working on ZMQ related code for PoWER
```
```
syntheticbird: Why would we not decode the JSON
```
```
syntheticbird: what's a situation where we wouldn't process the request and still respond somehow
```
```
boog900: becuase on one request we didn't need it.
```
```
boog900: the request was the  txpool hashes "bin" request, so we didn't need any of the pay for RPC data which is the only data in the request so I just didn't read it.
```
```
boog900: which then meant we would respond to the txpool hashes bin request fine but then disconnect after, which was hard to debug as to me all requests were fine. 
```
```
boog900: 3) Project: What is next for Cuprate?
```
```
hinto: RPC payments may stay with us forever, it's unused and clutters code yet it's too harmless to get consensus/review to remove
```
```
hinto: 1 thing to add onto the bucket list of the fabled monerod RPC/P2P rewrite
```
```
syntheticbird: wait until 50%+ of nodes are cuprate, you'll see how quick the consensus on removing it will be
```
```
boog900: Cuprate doesn't support it 
```
```
syntheticbird: i know and it's good
```
```
boog900: it just has the fields in its types 
```
```
syntheticbird: but it could be removed from the specs altogether
```
```
boog900: Anything else anyone wants to discuss today? 
```
```
boog900: We can end here, thanks everyone!
```
```
syntheticbird: I just bought a chessboard
```
```
boog900: !meeting 
```

# Action History
- Created by: moo900 | 2025-12-09T18:27:25+00:00
- Closed at: 2025-12-16T18:25:01+00:00
