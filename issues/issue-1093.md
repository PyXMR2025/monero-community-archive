---
title: 'Cuprate Meeting #26 - Tuesday, 2024-10-22, UTC 18:00'
source_url: https://github.com/monero-project/meta/issues/1093
author: moo900
assignees: []
labels: []
created_at: '2024-10-15T18:38:28+00:00'
updated_at: '2024-10-22T18:30:18+00:00'
type: issue
status: closed
closed_at: '2024-10-22T18:30:17+00:00'
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

Previous meeting with logs: #1089

# Discussion History
## moo900 | 2024-10-22T18:30:16+00:00
## Meeting logs
```
boog900: 1) greetings 
```
```
0xfffc: Hi everyone 
```
```
boog900: meeting issue: https://github.com/monero-project/meta/issues/1093
```
```
hinto: hello
```
```
boog900: 2) Updates
```
```
boog900: Me: I have done very little work on Cuprate last week, most of my time has been spent on this: https://github.com/Boog900/monero-ban-list 
```
```
boog900: I am back on Cuprate now though
```
```
hinto: me: making criterion benchmarks for all the crates I've written so far
```
```
boog900: 3) Project: What is next for Cuprate?
```
```
syntheticbird: Hello everyone
```
```
syntheticbird: Sorry for the late
```
```
hinto: boog900: will you review #320 soon? that PR is blocking progress on the RPC handlers - I thought about continuing on another branch but the eventual merge conflicts don't seem worth it
```
```
syntheticbird: Update: Working on PR 323 and searching to correct my PR and benchmark proposed lookup algorithm.
```
```
boog900: yep in progress now
```
```
boog900: I just submitted the comments I had already left
```
```
hinto: thanks, also eventually #196 as well would be nice but this is lower priority
```
```
hinto: don't think there will be many conflicts so I'm building all the benchmarks on-top of that PR for now
```
```
hinto: another update: with #321 merged, https://github.com/Cuprate/cuprate/issues/207 is now complete - all of our crates are linted now :)
```
```
hinto: there's still the really strict lints that aren't enabled yet but this is a nice milestone
```
```
boog900: nice, is there anything else anyone wants to discuss?
```
```
syntheticbird: I would appreciate comments on [#315](https://github.com/Cuprate/cuprate/issues/315)
```
```
hinto: does cargo allow you to declare workspace crates like that?
```
```
syntheticbird: > <@hinto:monero.social> does cargo allow you to declare workspace crates like that?

Yes I've use this pattern in another repository
```
```
hinto: seems a lot cleaner than what we do now then
```
```
syntheticbird: Cool. Should I start a PR then?
```
```
boog900: yeah
```
```
syntheticbird: we'll do after lookup table pr
```
```
syntheticbird: will do*
```
```
boog900: alright I think we can end here
```
```
boog900: Thanks everyone
```
```
syntheticbird: thx
```
```
hinto: thanks
```

# Action History
- Created by: moo900 | 2024-10-15T18:38:28+00:00
- Closed at: 2024-10-22T18:30:17+00:00
