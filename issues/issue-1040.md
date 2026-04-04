---
title: 'Cuprate Meeting #13 - Tuesday, 2024-07-23, UTC 18:00'
source_url: https://github.com/monero-project/meta/issues/1040
author: moo900
assignees: []
labels: []
created_at: '2024-07-16T19:06:19+00:00'
updated_at: '2024-07-23T19:17:51+00:00'
type: issue
status: closed
closed_at: '2024-07-23T19:17:51+00:00'
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

Previous meeting with logs: #1036

# Discussion History
## moo900 | 2024-07-23T19:17:50+00:00
## Meeting logs
```
boog900: there we go :)
```
```
hinto: hello
```
```
boog900: 2) Updates: What is everyone working on?
```
```
boog900: Me: I finished the PR adding alt chain handling to the consensus code and have started work on the tx pool.
```
```
hinto: me: finishing up RPC types, started the RPC interface - only around ~18 days left in my CCS but I'll think I'll be close to finishing on time
```
```
boog900: 3) Project: What is next for Cuprate?
```
```
boog900: hinto: is there anything you want to discuss in this meeting
```
```
hinto: I'd like some input on what I'll be doing next. I've also been thinking I'd like to focus more on project-wide things seeing as we might have more contributors.

Some things I think could/should be done relatively soon:
1. RPC handlers
1. Benchmark setup (such that any contributor can easily add/modify)
1. Documentation and/or re-working some crates (e.g. epee)
```
```
hinto: If I'm honest, I'd like to slow down development a little. I'm not sure how much runway we have as a project but I firmly believe doing things more carefully will be better for the long-term. Releasing a working binary ASAP can be worked in parallel but I would prefer if more time/energy went towards the things that will matter in 5-10+ years.
```
```
hinto: Maybe "slow down development" is bad wording actually, I mean focusing on refining our existing code and spending more time on quality rather than outputting as fast as possible. I still have the energy to work but I think the quality/speed balance is a little too skewed towards speed right now.
```
```
hinto: A counter argument I think is fair is that Cuprate as a project should at least deliver _something_ pretty soon, although if this is the case I think we could focus on the binary even more so
```
```
boog900: I think the days of being able to make a whole CCS solely focused on a single area are coming to an end. The next most important tasks that don't have someone working on them are smaller tasks. It would probably be best to make a CCS for 3 months work with some example stuff that you plan to work on.

RPC handlers would be good. Documentation is another good one. As for other tasks this is another reason I need to make that binary tracking issue :)

> If I'm honest, I'd like to slow down development a little.

From the start my main goal has been to get a working binary out as quickly as possible without compromising the code, so things might not be perfect _now_ however it can be made so in the future, once we have a working binary. Saying this the code is still IMO very good, a huge step up from monerod.

The reason for this was, although support for Cuprate right now is pretty good, it was not so in the past. I think things would look differently now if we did not make as much progress as we did over the past months. 

I don't really want to change trajectory just yet, I do feel a working alpha binary is just round the corner, then I would be happy to take a step back and start working on improving the documentation, testing, etc. 

Although saying that I think the initial alpha binary is only dependent on my planned work now so I would be happy for you to start work on improving code quality on your next CCS.

> although if this is the case I think we could focus on the binary even more so

Too many people working on the binary could lead to contention where people are more dependent on each other, while lots of changes are being made this is something I have tried to avoid. 
```
```
hinto: For the time being I think the current pace is okay as well, just worried about the medium/long-term.

I'll compile a more exact list of things to do for next week's meeting.
```
```
boog900: hinto: I think I am going to split some of the service code out of `cuprate-blockchain`, do you have any opinions on putting this in a separate crate or a feature flag in `cuprate-blockchain` 
```
```
boog900: I am trying to reduce the amount of duplicated code between the blockchain and tx-pool 
```
```
boog900: I plan to split the config and the 2 service types, with a new trait for the inner request handler
```
```
hinto: a separate crate sounds correct in that case
```
```
hinto: the main duplication is the config + threadpool, right?
```
```
hinto: I think formalizing a proposal issue would help here
```
```
boog900: > the main duplication is the config + threadpool, right?
 yeah

> I think formalizing a proposal issue would help here

Probably although that would take time, I think I could do the split pretty quick so I'll just make a PR
```
```
boog900:  * > the main duplication is the config + threadpool, right?

yeah

> I think formalizing a proposal issue would help here

Probably although that would take time, I think I could do the split pretty quick so I'll just make a PR
```
```
boog900: 4) Any other business
```
```
boog900: anything else anyone wants to discuss?
```
```
boog900: ok I think we can end here.
```
```
boog900: thanks hinto 
```
```
hinto: thanks
```
```
boog900: !meeting 
```

# Action History
- Created by: moo900 | 2024-07-16T19:06:19+00:00
- Closed at: 2024-07-23T19:17:51+00:00
