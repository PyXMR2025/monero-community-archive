---
title: 'Cuprate Meeting #117 - Tuesday, 2026-08-25, UTC 18:00'
source_url: https://github.com/monero-project/meta/issues/1444
author: moo900
assignees: []
labels: []
created_at: '2026-08-18T18:15:34+00:00'
updated_at: '2026-08-25T18:38:12+00:00'
type: issue
status: closed
closed_at: '2026-08-25T18:38:12+00:00'
---

# Original Description
[Cuprate](https://github.com/Cuprate/cuprate) is an effort to create an alternative Monero node implementation.

Location: [Libera.chat, #cuprate](https://libera.chat/) | [Matrix](https://matrix.to/#/#cuprate:monero.social?via=matrix.org&via=monero.social)

[Join the Monero Matrix server if you don't already have a Matrix account](https://www.getmonero.org/resources/user-guides/join-monero-matrix.html)

Time: 18:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html)

Moderator: @Boog900

Please comment on GitHub in advance of the meeting if you would like to propose a discussion topic.

Main discussion topics:

1. Greetings
2. Updates: What is everyone working on?
3. Project: What is next for Cuprate?
4. Any other business

Previous meeting: #1441

# Discussion History
## moo900 | 2026-08-25T18:38:11+00:00
## Meeting logs
```
boog900: 1) greetings
```
```
redsh4de: hello
```
```
boog900: Matrix is slow 
```
```
boog900: 2) updates 
```
```
boog900: I reviewed the graceful error PRs also made a PR to fix a regression in full verification sync speed. The PR should make us even faster at full verification compared to before the regression
```
```
boog900: I think it is between 10 and 20 % faster
```
```
syntheticbird: hello
```
```
redsh4de: left a comment on it, look 2 me like if a batch contains a invalid block we could lose sync between the cache & db due to the return
```
```
syntheticbird: me: not much. Participated in review earlier last week. Working on the blog and ready for review on RPC PRs.
```
```
boog900: yeah I think that is right, should be easy to just add to the db what we have built up already 
```
```
redsh4de: omg hi
```
```
redsh4de: also worked on a PR to bring us closer to compliance to JSON-RPC 2.0 spec - draft for now as monero isnt compliant with it either so have to check if the strictness can cause problems with wallets
```
```
redsh4de: after the rate limits land we could look into adding batch request support
```
```
boog900: 3) Project: What is next for Cuprate?
```
```
boog900: kayaba has asked for that
```
```
syntheticbird: for serai?
```
```
boog900: wow he showed up just from mentioning it 
```
```
kayabanerve: I would love support for batch requests
```
```
kayabanerve: No, for monero-oxide
```
```
kayabanerve: boog900 @boog900:monero.social: Do you remember what method makes use of it?
```
```
kayabanerve: *would make use of it if it was supported?
```
```
kayabanerve: I think it's JSON fetching of blocks, which is needed for some edge case?
```
```
boog900: yeah it is 
```
```
kayabanerve: Hello, please let us use a single request to fetch blocks (JSON-encoded) over the network, thank you, have a nice day
```
```
boog900: although using JSON to requests blocks is not great so I would rather changes be made to the epee endpoint to allow monero-oxide to use that
```
```
irc_datahoarder: ZMQ-pub would allow p2pool to use it (and do so efficiently), or other alternate notification system for block headers (and/or txs later)
```
```
boog900: yeah we will support ZMQ
```
```
boog900: just need to work on it :)
```
```
boog900: the types are there
```
```
irc_datahoarder: no need for the full ZMQ set (there's some ZMQ for also interacting with monerod) but ZMQ-pub specifically :)
```
```
boog900: did you know they are different to the JSON types in JSON RPC?? :)
```
```
boog900: oh yeah, I think lws uses it IIRC
```
```
datahoarder: but yes. I implemented converters for all of these different types :)
```
```
boog900: does anyone want to discuss anything today?
```
```
boog900: I have made a milestone for preview 2 so we can all track what needs to be done for that
```
```
redsh4de: RPC limits up next? :D
```
```
boog900: yes
```
```
boog900: I have lots of things to review :)
```
```
redsh4de: bountiful cuprate season
```
```
boog900: I will end the meeting here
```
```
boog900: thanks everyone
```
```
syntheticbird: thanks
```
```
boog900: !meeting 
```

# Action History
- Created by: moo900 | 2026-08-18T18:15:34+00:00
- Closed at: 2026-08-25T18:38:12+00:00
