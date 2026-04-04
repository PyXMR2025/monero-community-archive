---
title: 'Cuprate Meeting #42 - Tuesday, 2025-02-11, UTC 18:00'
source_url: https://github.com/monero-project/meta/issues/1151
author: moo900
assignees: []
labels: []
created_at: '2025-02-04T18:58:17+00:00'
updated_at: '2025-02-11T19:01:04+00:00'
type: issue
status: closed
closed_at: '2025-02-11T19:01:04+00:00'
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

Previous meeting: #1147

# Discussion History
## moo900 | 2025-02-11T19:01:03+00:00
## Meeting logs
```
boog900: 1) greetings
```
```
syntheticbird: hi
```
```
plowsof: hi
```
```
boog900: 2) updates 
```
```
boog900: me: I opened a new CCS proposal: https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/544, I also worked on cleaning up some of the things I have been working on for fast sync 
```
```
syntheticbird: me: nothing
```
```
boog900: hinto has also opened a CCS: https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/543
```
```
syntheticbird: saw that
```
```
syntheticbird: We can wait 10~20 minutes before jumping to 3.
```
```
syntheticbird: let's see if hinto spawn
```
```
boog900: this poor man was connected to so many proxies: https://github.com/Cuprate/cuprate/issues/383
```
```
syntheticbird: wasn't the ban list hardcoded?
```
```
syntheticbird: or ig he didn't updated
```
```
boog900: only for the fast sync branch 
```
```
syntheticbird: sad
```
```
boog900: I don't know what happened, his node literally died for those hours  
```
```
boog900: the only thing that happened was the syncer checking the node was still synced 
```
```
syntheticbird: weird
```
```
syntheticbird: ig he is away
```
```
syntheticbird: boog900: is there anything you wanna discuss?
```
```
syntheticbird: I don't have any topic in the immediate
```
```
m-relay: <N​orrin> q&a? 
```
```
syntheticbird: feel free to ask Norrin
```
```
m-relay: <N​orrin> I want to build & test
```
```
m-relay: <N​orrin> https://user.cuprate.org/ is bare. main README does not have build instructions. 
```
```
syntheticbird: yes thats because alpha is meant to be release in a few weeks at least
```
```
syntheticbird: so right now isn't the time to test for user
```
```
syntheticbird: but if you really wanna test it absolutely now, just git clone the fast-sync branch and build it with cargo
```
```
boog900: if you want to test now, install latest Rust and run `cargo run -r --bin cuprated` from cuprate's root
```
```
boog900: I wouldn't use fast sync 
```
```
boog900: yet
```
```
syntheticbird: alr
```
```
m-relay: <N​orrin> cool
```
```
boog900: anything else anyone wants to discuss?
```
```
m-relay: <N​orrin> #3
```
```
m-relay: <N​orrin> nvm, i guess that's where you were headed
```
```
boog900: I was just going to end here, without hinto there isn't much to discuss 
```
```
m-relay: <N​orrin> reading the ccs proposal
```
```
boog900: Ok I think we can end here, thanks everyone 
```

# Action History
- Created by: moo900 | 2025-02-04T18:58:17+00:00
- Closed at: 2025-02-11T19:01:04+00:00
