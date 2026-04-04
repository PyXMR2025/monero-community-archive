---
title: 'Cuprate Meeting #94 - Tuesday, 2026-03-17, UTC 18:00'
source_url: https://github.com/monero-project/meta/issues/1351
author: moo900
assignees: []
labels: []
created_at: '2026-03-10T18:43:02+00:00'
updated_at: '2026-03-17T18:33:01+00:00'
type: issue
status: closed
closed_at: '2026-03-17T18:33:01+00:00'
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

Previous meeting: #1348

# Discussion History
## moo900 | 2026-03-17T18:33:00+00:00
## Meeting logs
```
boog900: 1) greetings 
```
```
hinto: hello
```
```
redsh4de: hello
```
```
boog900: 2) updates
```
```
kayabanerve: 👋
```
```
boog900: Me: spent some time reviewing and discussing the new syncer notification system, which also made me find a bug in the tapes DB which I fixed.
```
```
syntheticbird: Hello
```
```
hinto: me: I am getting more serious about a certain side-project and have been working on it a lot recently, hopefully it can be released this year (or at least revealed); back to Cuprate for now though :)
```
```
redsh4de: Me: finished work on the syncer, over the past 2 days worked on making cuprated embeddable for which i submitted a PR. Currently reworking my shutdown branches to depend on the embeddable pattern. looked into options for a cuprate GUi/TUI down the line when cuprate becomes embeddable
```
```
redsh4de: * Me: finished work on the syncer, over the past 2 days worked on making cuprated embeddable for which i submitted a PR. Currently reworking my shutdown branches to depend on the embeddable branch. looked into options for a cuprate GUi/TUI down the line when cuprate becomes embeddable
```
```
boog900: 3) Project: What is next for Cuprate?
```
```
boog900: I plan to PR the current RPC changes I made on the rpc-stage branch before doing any more changes, as I don't really want to dump a massive PR again.
```
```
boog900: speaking of that PR how is the review going hinto, anything you want to discuss on it? 
```
```
hinto: I'm still organizing the comments so not yet
```
```
hinto: also worth noting the new-db branch eventually OOMed on 2GB
```
```
hinto: this was before the recent changes though
```
```
boog900: was that with fast sync?
```
```
hinto: it was the first full verification run
```
```
boog900: oh I thought it completed that
```
```
hinto: current commit + fast sync is currently in progress, will update later
```
```
hinto: it did, although it crashed later on
```
```
boog900: hmmm
```
```
boog900: that's weird 
```
```
boog900: I would have thought sync was the thing that would cause OOMs
```
```
boog900: excluding spam waves 
```
```
hinto: I'd think so too, I'll try to catch logs for the current commit if it happens again
```
```
hinto: is the plan still to merge 587 then release v0.0.9?
```
```
hinto: or perhaps wait for RPC changes?
```
```
boog900: yes I don't think we should wait for RPC 
```
```
boog900: ah ....  I might have found the issue 
```
```
boog900: I think I set fjall to use all the memory on the system I meant to divide by 5.
```
```
boog900: will push a fix 
```
```
boog900: thats the read cache so shouldn't change write speed. 
```
```
hinto: ok, will redo the current run
```
```
boog900: anything else anyone would like to discuss today?
```
```
boog900: I think we can end here
```
```
boog900: thanks everyone!
```
```
boog900: !meeting 
```

# Action History
- Created by: moo900 | 2026-03-10T18:43:02+00:00
- Closed at: 2026-03-17T18:33:01+00:00
