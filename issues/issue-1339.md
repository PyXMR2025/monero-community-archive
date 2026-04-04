---
title: 'Cuprate Meeting #90 - Tuesday, 2026-02-17, UTC 18:00'
source_url: https://github.com/monero-project/meta/issues/1339
author: moo900
assignees: []
labels: []
created_at: '2026-02-10T18:46:10+00:00'
updated_at: '2026-02-17T18:27:01+00:00'
type: issue
status: closed
closed_at: '2026-02-17T18:27:01+00:00'
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

Previous meeting: #1336

# Discussion History
## moo900 | 2026-02-17T18:26:59+00:00
## Meeting logs
```
boog900: 1) greetings
```
```
syntheticbird: Hi
```
```
hinto: hello
```
```
boog900: 2) updates 
```
```
boog900: Me: testing the new DB, did a full verification sync, found some issues which I debugged and fixed
```
```
hinto: me: opened a CCS and am starting to focus on StageX again: https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/643; I think gitian in the interim is unlikely unless there are major integration blocks
```
```
redsh4de: me: finalizing the new syncer logic. debugged the PR over the past few days and hunted for edge cases, will push final commits to the PR soon and remove the draft status
```
```
redsh4de: here is the flowchart m working with locally
```
```
redsh4de: <image.png>
```
```
boog900: redsh4de: the PRs have been great 
```
```
boog900: 3) Project: What is next for Cuprate?
```
```
boog900: I don't have anything I want to discuss today, just trying to get the db finally done :p
```
```
redsh4de: are there any relevant tasks i could explore after the syncer?
```
```
boog900: Some good shutdown logic would be nice 
```
```
boog900: Right now when you stop cuprate it is pretty much a crash.
```
```
boog900: In my experiment branch I did add this, I don't know how easy it will be to port to main vs just restarting it 
```
```
redsh4de: can have a look at the branch, got a commit hash for the shutdown changes?
```
```
redsh4de: risk of data loss?
```
```
boog900: Its in the fjall-wip branch 
```
```
boog900: https://github.com/Cuprate/cuprate/blob/fjall-wip/binaries/cuprated/src/monitor.rs
```
```
boog900: Its a mess as it was just a branch where I was seeing what would work 
```
```
boog900: > <@redsh4de:matrix.org> risk of data loss?

The database is ACID but while changing to the new DB yeah it was an issue. Now the new DB is pretty crash resistance so it isn't an issue again. 
```
```
boog900: But it would still be nice to make sure everything is flushed 
```
```
redsh4de: definitely, will get started on that sometime over the weekend then
```
```
boog900: Anything else to discuss today 
```
```
redsh4de: pushed the final commits for the syncer PR, ready for review
```
```
hinto: nothing from me
```
```
boog900: We can end here 
```
```
boog900: !meeting 
```

# Action History
- Created by: moo900 | 2026-02-10T18:46:10+00:00
- Closed at: 2026-02-17T18:27:01+00:00
