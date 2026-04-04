---
title: 'Cuprate Meeting #12 - Tuesday, 2024-07-16, UTC 18:00'
source_url: https://github.com/monero-project/meta/issues/1036
author: moo900
assignees: []
labels: []
created_at: '2024-07-09T19:07:32+00:00'
updated_at: '2024-07-16T19:06:19+00:00'
type: issue
status: closed
closed_at: '2024-07-16T19:06:19+00:00'
---

# Original Description
[Cuprate](https://github.com/Cuprate/cuprate) is an effort to create an alternative Monero node implementation.

Location: [Libera.chat, #cuprate](https://libera.chat/) | [Matrix](https://matrix.to/#/#cuprate:monero.social?via=matrix.org&via=monero.social)

> Note that there are currently communication issues with Matrix accounts created on the matrix.org server, consider using a different homeserver to see messages.

[Join the Monero Matrix server if you don't already have a Matrix account](https://www.getmonero.org/resources/user-guides/join-monero-matrix.html)

Time: 18:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html)

Moderator: @Boog900

Please comment on GitHub in advance of the meeting if you would like to propose a discussion topic.

Main discussion topics:

- Greetings
- Updates: What is everyone working on?
- Project: What is next for Cuprate?
- [yamabiiko's CCS](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/479)

- Any other business

Previous meeting with logs: #1033

# Discussion History
## moo900 | 2024-07-16T19:06:19+00:00
## Meeting logs
```
boog900: meeting time! https://github.com/monero-project/meta/issues/1036
```
```
boog900: 1) Greetings 
```
```
yamabiiko: Hi
```
```
hinto: hi
```
```
fluorescent_beige: Hi
```
```
boog900: 2) Updates: What is everyone working on?

```
```
fluorescent_beige: Still the db hotswap (issue 209)
```
```
hinto: me: finishing up custom (de)serialization code for RPC types, will start implementing the RPC interface soon
```
```
boog900: Me: took some days off last week. I spent most of my time working on alt chain handling in the consensus code and planning how the DB tables will look, will hopefully have the consensus changes ready today or tomorrow 
```
```
yamabiiko: Mainly submitted the CCS for ZMQ
```
```
boog900: 3) Project: What is next for Cuprate?
```
```
boog900: - [yamabiiko's CCS](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/479)
```
```
yamabiiko: > <@boog900:monero.social> - [yamabiiko's CCS](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/479)

I'll start ironing out the design, writing playground code and so on while waiting until it will get merged (or not)
```
```
yamabiiko: Not sure how long the decision process can be
```
```
hinto: I have some questions/thoughts for yamabiiko:

1. "I will also write ZMQ user docs for Monero" => what will this be specifically? Documentation PRs for `monero-core` explaining its ZMQ implementation?
1. "Milestones [...] ZMQ documentation" => can you clarify this as well? what types of docs? FWIW I believe end-user crate documentation should be mandatory
1. IMO some preliminary work on ZMQ would increase confidence in this CCS. I think it's okay in its current state as well but there will be expectation to deliver high quality work on time
```
```
yamabiiko: 1. It will be for monero but not about its implementation but it will be akin to the RPC ones, for example there is no docs defining the fields that are sent with the different contexts/events
2. I guess the "extra" documentation would be the one in Cuprate's architecture book
```
```
yamabiiko: 3. I will go forward with this, any ideas of what other preliminary work can be done other than what I suggested?
```
```
boog900: where is (1) planned to go? monero-site _might_ accept a PR adding docs for ZMQ, like the RPC docs they currently have 
```
```
yamabiiko: monero-project/monero's wiki and monero-site, potentially expand the doc file in monerod
```
```
boog900: I would put that in the CCS
```
```
hinto: > documentation

Can you confirm in the CCS that you will write both crate documentation and the ZMQ section in the architecture book? If this means extending the CCS to 3 months I think that would be okay as well.

> preliminary work

Maybe crate layout, how each crate will look, what crates are for what, etc. Not 100% necessary, but I think it would help.
```
```
boog900: > <@yamabiiko:unitoo.it> 3. I will go forward with this, any ideas of what other preliminary work can be done other than what I suggested?

reviewing PRs, adding docs/smaller tests 
```
```
boog900: > <@yamabiiko:unitoo.it> 3. I will go forward with this, any ideas of what other preliminary work can be done other than what I suggested?

 * reviewing PRs, adding docs/smaller tests for other sections 
```
```
yamabiiko: > <@hinto:monero.social> > documentation
> 
> Can you confirm in the CCS that you will write both crate documentation and the ZMQ section in the architecture book? If this means extending the CCS to 3 months I think that would be okay as well.
> 
> > preliminary work
> 
> Maybe crate layout, how each crate will look, what crates are for what, etc. Not 100% necessary, but I think it would help.

Yes
```
```
yamabiiko: I don't expect ZMQ to be as much work as opposed to something like RPC, but I suppose extending it won't hurt given the fact that there will be much to do in Cuprate anyways if I end up being right on time
```
```
hinto: okay thanks - boog900: do you have thoughts on extending to 3 months?
```
```
hinto: I didn't look into the ZMQ issue in detail so I'm not sure what the amount of work is - if you think the amount of work ZMQ + docs will take is < 3 months, now is the time to stack more work on yamabiiko's desk :) 
```
```
boog900: I do want to be careful about promising work for CCSs as it does tie up what other people can work on. yamabiiko would you be willing to extend to 3 months, and add a 3rd milestone that will be claimed for 3 months work and completed ZMQ (as proposed in this CCS), this way _if_ you finish early you can work on whatever is needed 
```
```
boog900: this is what hinto did for their first Cuprate CCS 
```
```
yamabiiko: Yeah I think that is fair and wise. Thought maybe adding some proposed "next things" to work on (not on the milestones) can add value to the CCS
```
```
yamabiiko: * Yeah I think that is fair and wise. Though maybe adding some proposed "next things" to work on (not on the milestones) can add value to the CCS
```
```
boog900: I have been meaning to make a task list/tracking issue for things need for a working binary for a while now, when I do get round to making this you can link to it in the CCS.

Otherwise probably just generic things, closing open issues, documentation, testing and benchmarking 
```
```
boog900: 4) anything else to discuss?
```
```
boog900: fluorescent_beige: how are you getting on with 209
```
```
boog900: anything you want to discuss about that? 
```
```
boog900: anybody else want to discuss anything? or we can end the meeting here 
```
```
boog900: ok lets end here, thanks everyone!
```
```
hinto: thanks
```
```
yamabiiko: Thanks all
```
```
boog900: !meeting 
```

# Action History
- Created by: moo900 | 2024-07-09T19:07:32+00:00
- Closed at: 2024-07-16T19:06:19+00:00
