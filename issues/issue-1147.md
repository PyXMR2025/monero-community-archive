---
title: 'Cuprate Meeting #41 - Tuesday, 2025-02-04, UTC 18:00'
source_url: https://github.com/monero-project/meta/issues/1147
author: moo900
assignees: []
labels: []
created_at: '2025-01-28T19:17:18+00:00'
updated_at: '2025-02-04T18:58:18+00:00'
type: issue
status: closed
closed_at: '2025-02-04T18:58:17+00:00'
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
- [cuprated v0.0.1 commit](https://github.com/Cuprate/cuprate/issues/371)
- [Project roadmap for 2025](https://github.com/Cuprate/cuprate/issues/376)

- Any other business

Previous meeting: #1144

# Discussion History
## moo900 | 2025-02-04T18:58:16+00:00
## Meeting logs
```
boog900: meeting time
```
```
boog900: 1) Greetings 
```
```
hinto: hello
```
```
boog900: 2) Updates
```
```
syntheticbird: hi
```
```
boog900: Me: I worked on an initial fast-sync impl, going to be opening a PR soon.
```
```
syntheticbird: Me: Im no more sick
```
```
hinto: me: no code updates other than a few low-priority PRs, mostly spending time on preparing for #371.
```
```
boog900: 3) Project: What is next for Cuprate?

```
```
syntheticbird: hinto: you are planning on releasing the post on thursday?
```
```
hinto: the reddit post, yes, although any day is fine
```
```
boog900: it's ready to be posted now right?
```
```
hinto: Yes. FWIW the point of an update post for me is such that there is a single link/place where that information exists, so it can be posted whenever, although we may as well wait until thursday as it isn't crucial
```
```
boog900: Alright
```
```
boog900: - [cuprated v0.0.1 commit](https://github.com/Cuprate/cuprate/issues/371)
```
```
hinto: I think we can start closing in on the specific commit that will be used for `cuprated v0.0.1` builds.
```
```
hinto: If that commit is in the future, we should layout what work should be done before then 
```
```
hinto: AFAICT it is only `fast-sync`
```
```
syntheticbird: I think too
```
```
boog900: the list of things I want to do first:
- the 174 PR I am working on
- fast sync 
- more `cuprated` commands: fetch tx-pool, maybe peers & download state
```
```
boog900: pop blocks as well 
```
```
hinto: Is there a priority for that list?
```
```
boog900: yeah it's in priority order 
```
```
boog900: top is needed most 
```
```
hinto: Do you think any of them will be ready for inclusion in the release?
```
```
boog900: all of them will be ready very soon, by the end of the month 
```
```
syntheticbird: before 23 february?
```
```
boog900: probably 
```
```
hinto: Ok, going forward I'd like to decide on the release commit ~1 week beforehand such that I can start testing
```
```
hinto: Also I think a backup commit would be good in-case things aren't ready or bugs are found?
```
```
hinto: For now that could be https://github.com/Cuprate/cuprate/commit/7e8e62135c9a814d4157a2927849aadde35cc4a8?
```
```
boog900: yeah sure
```
```
boog900: - [Project roadmap for 2025](https://github.com/Cuprate/cuprate/issues/376)
```
```
boog900: I do think we are being conservative on the 2025 roadmap, probably better than trying to do too much though I guess 
```
```
hinto: I wanted to confirm that the this is more-or-less the 2025 roadmap (i.e. task priority list), I don't think there was official consensus last meeting.
```
```
syntheticbird: I stand on what I said last meeting. I agree with this roadmap
```
```
syntheticbird: no concerns or edits in mind
```
```
boog900: yeah i think it is ok 
```
```
boog900: anything else to discuss? 
```
```
syntheticbird: nope
```
```
boog900: ok I think we can end here, thanks everyone 
```
```
syntheticbird: thanks
```

# Action History
- Created by: moo900 | 2025-01-28T19:17:18+00:00
- Closed at: 2025-02-04T18:58:17+00:00
