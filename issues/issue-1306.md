---
title: 'Cuprate Meeting #79 - Tuesday, 2025-12-09, UTC 18:00'
source_url: https://github.com/monero-project/meta/issues/1306
author: moo900
assignees: []
labels: []
created_at: '2025-12-02T18:30:31+00:00'
updated_at: '2025-12-09T18:27:26+00:00'
type: issue
status: closed
closed_at: '2025-12-09T18:27:26+00:00'
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

Previous meeting: #1302

# Discussion History
## moo900 | 2025-12-09T18:27:25+00:00
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
boog900: I continued my work on RPC, opened a draft PR for some initial changes, I plan to split it into many PRs once I have basic wallet functionality working on the WIP branch.  
```
```
hinto: me: I've been experimenting [StageX](https://stagex.tools) on smaller repos for reproducible builds, it's been less arcane than Guix so far
```
```
boog900: 3) Project: What is next for Cuprate?
```
```
boog900: is there any examples to see how it will work?
```
```
hinto: tobtoht already started a bit on Monero: https://github.com/monero-project/monero/pull/10223
```
```
hinto: There are other related projects that have already implemented it that I've been looking at as well: https://github.com/nimiq/core-rs-albatross/tree/albatross/build and https://github.com/MystenLabs/sui/tree/main/docker/sui-node-deterministic
```
```
boog900: nice, it will be good to have this for the beta release, whenever that is.
```
```
hinto: I think most of the early problems for Cuprate will be our build code and some of our deps, I haven't checked yet for deeper problems
```
```
boog900: I don't have anything I want to discuss today, hopefully next week I will have more PRs open for the RPC. 
```
```
boog900: hinto if you don't have anything you want to discuss we can end here
```
```
hinto: fyi I'm waiting on tx relay v2 to avoid conflicts for PoWER, so I have time to review now/soon
```
```
hinto: we can end here
```

# Action History
- Created by: moo900 | 2025-12-02T18:30:31+00:00
- Closed at: 2025-12-09T18:27:26+00:00
