---
title: 'Cuprate Meeting #27 - Tuesday, 2024-10-29, UTC 18:00'
source_url: https://github.com/monero-project/meta/issues/1097
author: moo900
assignees: []
labels: []
created_at: '2024-10-22T18:30:17+00:00'
updated_at: '2024-10-29T18:47:38+00:00'
type: issue
status: closed
closed_at: '2024-10-29T18:47:37+00:00'
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
- branch protection

- Any other business

Previous meeting with logs: #1093

# Discussion History
## moo900 | 2024-10-29T18:47:36+00:00
## Meeting logs
```
boog900: 1) Greetings 
```
```
syntheticbird: *hi*
```
```
hinto: hello
```
```
boog900: 2) updates 
```
```
syntheticbird: Me: Wrote a `Bucket` data structure for storing items discriminated into buckets. Will serve for improving the current address book by forcing /16 subnets diversity.
```
```
syntheticbird: Also have been trying to get up to speed around FCMP++
```
```
boog900: Me: I finished up the txpool and the initial `cuprated` config. Today I also worked on adding `cargo hack` to CI and fixing the errors, which is done but my IDE has reformatted some files which I will need to fix.
```
```
boog900: I also did some work on the P2P request handler 
```
```
boog900: that's also pretty much done now 
```
```
hinto: me: not much code writing recently, mostly reviews
```
```
boog900: 3)  Project: What is next for Cuprate?
```
```
syntheticbird: are we in a straight line right now in assembling cuprated up to alpha release ?
```
```
hinto: > <@dimalinux:monero.social> After the latest commit to `main` (`63216aecaead915550be93236faf6aeeebf0e04f`), if I am inside the  top level`types` folder and run `cargo build`, I get a failure. The errors are related to serde serialization. `cargo build` from the top works. I'll try to triage it more tomorrow. My branch has a `zmq/types` folder/crate that uses `HexBytes` from `cuprate-types` and it's getting the same error when building inside the crate after merging main.

dimalinux: lots of our crates have messed up builds if they aren't done in the exact way CI does it (mostly feature related), I made a related issue here: https://github.com/Cuprate/cuprate/issues/325
```
```
hinto: boog900's cargo hack PR will enumerate/fix these I hope
```
```
boog900: > <@syntheticbird:monero.social> are we in a straight line right now in assembling cuprated up to alpha release ?

As long as nothing comes up yes
```
```
hinto: also thanks for continuing to contribute, your PRs are very clean 
```
```
boog900: Is there anything anyone wants to discus? 
```
```
syntheticbird: I would like to talk branch protection
```
```
syntheticbird: we have no rules in place
```
```
boog900: 4) branch protection
```
```
syntheticbird: I think PGP signing commit might be good. Firstly to make people more aware of maintainers and contributors PGP keys (for contact or signing) and so that when people clone the repository from a mirror they can attest authenticity of it.
```
```
boog900: Commits to main are signed by GH btw
```
```
boog900: As we squash merge  
```
```
syntheticbird: Oh I didn't know
```
```
syntheticbird: Then i guess we can just enforce 1 review before merge
```
```
boog900: I would be OK with that 
```
```
hinto: does enforce mean using `CODEOWNERS`? I'd prefer that since I'd like to at least have a chance to see changes to code I wrote before it gets merged
```
```
boog900: It doesn't but we can do that as well if you think it would be helpful 
```
```
hinto: projects with many contributors use some form of it eventually, I don't think we necessarily need it right now but it doesn't hurt adding it either 
```
```
hinto: extreme example: https://github.com/torvalds/linux/blob/master/MAINTAINERS
```
```
hinto: it's like an `Arc<Barrier>` but between code and people
```
```
boog900: 👍
```
```
boog900: Is there anything else anyone wants to discuss?
```
```
boog900: OK I think we can end here 
```
```
boog900: Thanks everyone 
```

# Action History
- Created by: moo900 | 2024-10-22T18:30:17+00:00
- Closed at: 2024-10-29T18:47:37+00:00
