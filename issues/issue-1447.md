---
title: 'Cuprate Meeting #118 - Tuesday, 2026-09-01, UTC 18:00'
source_url: https://github.com/monero-project/meta/issues/1447
author: moo900
assignees: []
labels: []
created_at: '2026-08-25T18:38:11+00:00'
updated_at: '2026-09-01T18:40:24+00:00'
type: issue
status: closed
closed_at: '2026-09-01T18:40:24+00:00'
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

Previous meeting: #1444

# Discussion History
## moo900 | 2026-09-01T18:40:22+00:00
## Meeting logs
```
boog900: 1) greetings 
```
```
redsh4de: hello
```
```
boog900: 2) updates
```
```
boog900: Me: Reviewd some PRs, added a tx interface for our DB. Also today I have been working on removing the lint ignores in cuprated
```
```
redsh4de: not much this week, rebasing older PRs today
```
```
boog900: 3) Project: What is next for Cuprate?
```
```
boog900: The pr I am making today will probably need to be merged fast as it'll conflict with everything in cuprated
```
```
boog900: We should have never had the ignores IMO
```
```
boog900: Oh yeah I have also made some issues this week for things I need to work on 
```
```
boog900: they are things I have just been keeping in my head, I thought it's probably a good idea to get them written down 
```
```
redsh4de: will review it ASAP, today/tomorrow
```
```
boog900: thanks 
```
```
redsh4de: regarding the JSON 2.0 spec compliance PR - there was a point made on the monerod repo about the same issue that monerod doesnt really have anything that benefits from notifications and just puts more strictness on the clients to not forget to pass an id for requests

which is a fair point, but so is the fact that if the RPC is supposed to be a json-rpc 2.0, it is expected to follow its rules
```
```
redsh4de: thoughts/opinions?
```
```
boog900: IMO it does not matter that much 
```
```
boog900: Like I think time would be better spent elsewhere ngl
```
```
syntheticbird: Hi
```
```
syntheticbird: sorry for being late
```
```
syntheticbird: no update on my side
```
```
syntheticbird: I'll address the rebase requet and review on RPC part 2
```
```
redsh4de: yea its just one of the minor points from the PR, most of it is about the errors being returned correctly
```
```
syntheticbird: alright
```
```
boog900: I am very excited for the next release, it's going to have a lot of good changes 
```
```
syntheticbird: same
```
```
boog900: anything else for today?
```
```
redsh4de: not from me
```
```
boog900: I left a comment on 691, I don't know if you saw 
```
```
redsh4de: ah yea
```
```
boog900: I think we can end here
```
```
boog900: thanks everyone
```

# Action History
- Created by: moo900 | 2026-08-25T18:38:11+00:00
- Closed at: 2026-09-01T18:40:24+00:00
