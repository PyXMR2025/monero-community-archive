---
title: 'Cuprate Meeting #120 - Tuesday, 2026-09-15, UTC 18:00'
source_url: https://github.com/monero-project/meta/issues/1455
author: moo900
assignees: []
labels: []
created_at: '2026-09-08T19:15:21+00:00'
updated_at: '2026-09-15T18:22:55+00:00'
type: issue
status: closed
closed_at: '2026-09-15T18:22:55+00:00'
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

Previous meeting: #1450

# Discussion History
## moo900 | 2026-09-15T18:22:54+00:00
## Meeting logs
```
boog900: 1) greetings
```
```
boog900: solo meeting today
```
```
boog900: my update is I finished pruning and started on the FCMP tree
```
```
boog900: almost finished with a basic version 
```
```
syntheticbird: Hi
```
```
boog900: I have a feeling it is going to be a lot better than what monerod has :)
```
```
boog900: ah no solo meeting 
```
```
syntheticbird: me: working on cuprate website and a blog post, addressed review on rpc hardening PR
```
```
syntheticbird: yeah sry I'm late
```
```
syntheticbird: better in what way ?
```
```
syntheticbird: performance?
```
```
boog900: mainly UX but also probably performance
```
```
boog900: it works in the background, monerod's does not 
```
```
boog900: When the first FCMP release is made monerod will build the full tree before doing anything else, we just build the outputs layer 
```
```
boog900: * When the first FCMP release is first run monerod will build the full tree before doing anything else, we just build the outputs layer 
```
```
boog900: then start the tree builder in the background 
```
```
syntheticbird: nice
```
```
boog900: also when adding blocks we just let it add the new outputs in the background monerod will wait for them to be added 
```
```
boog900: 3) Project: What is next for Cuprate?
```
```
syntheticbird: could you merge 684 so I can rebase pt.3
```
```
boog900: sure
```
```
syntheticbird: thx
```
```
boog900: done
```
```
syntheticbird: a thousand thx
```
```
boog900: anything to discuss today?
```
```
syntheticbird: I'll try to find time to review docker image pr this week
```
```
syntheticbird: so next release public node operator can use the docker file to deploy
```
```
boog900: I don't expect next release before october FWIW 
```
```
syntheticbird: yeah the pace greatly reduced
```
```
boog900: the PRs have not lol 
```
```
syntheticbird: lmao
```
```
syntheticbird: true
```
```
boog900: we have made some big changes since last release 
```
```
syntheticbird: pruning is the biggest without a doubt
```
```
syntheticbird: i've nothing else to discuss
```
```
boog900: yeah also a load of stability stuff 
```
```
boog900: the next release will be a much more secure node 
```
```
boog900: we can end here
```
```
boog900: !meeting 
```

# Action History
- Created by: moo900 | 2026-09-08T19:15:21+00:00
- Closed at: 2026-09-15T18:22:55+00:00
