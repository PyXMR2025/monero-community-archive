---
title: 'Cuprate Meeting #4 - Tuesday, 2024-05-21, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1009
author: Boog900
assignees: []
labels: []
created_at: '2024-05-17T00:05:49+00:00'
updated_at: '2024-05-25T00:34:33+00:00'
type: issue
status: closed
closed_at: '2024-05-25T00:34:33+00:00'
---

# Original Description
[Cuprate](https://github.com/Cuprate/cuprate) is an effort to create an alternative Monero node implementation.

Location: [Libera.chat, #cuprate](https://libera.chat/) | [Matrix](https://matrix.to/#/#cuprate:monero.social?via=matrix.org&via=monero.social)

> Note that there are currently communication issues with Matrix accounts created on the matrix.org server, consider using a different homeserver to see messages.

[Join the Monero Matrix server if you don't already have a Matrix account](https://www.getmonero.org/resources/user-guides/join-monero-matrix.html)

Time: 18:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html)

Moderator: boog900

Main discussion topics:
- Greetings
- Updates: What is everyone working on?
- Project: What is next for Cuprate?
   - Integrating FCMP++ into Cuprate
- Any other business

Please comment on GitHub in advance of the meeting if you would like to propose a discussion topic.

Previous meeting with logs: #1004

# Discussion History
## hinto-janai | 2024-05-19T13:28:25+00:00
I'd like to discuss: Integrating FCMP++ into Cuprate.

- The estimated timeline for FCMP++ implementation is 6-12 months IIRC; assuming Cuprate has an alpha binary ready at this point, should integrating FCMP++ be considered relatively soon?
- Node-related work (section 6):
    * The tree (section 6.1)
    * `grow` & `trim` algorithms (section 6.1.1, 6.1.2)
    * Initialization & normal operation (section 6.2.1, 6.2.2)
    * Transaction verification (section 6.7)
    * RPC (section 6.9)
    * [Key image migration](https://libera.monerologs.net/monero-research-lab/20240508#c374339-c374381) (or none if this is implemented before release)

Regarding tree storage: the current draft for `monerod` is 2 additional tables, one being a multimap table similar to outputs.

Relevant links:
- [FCMP++ Paper](https://github.com/kayabaNerve/fcmp-ringct/blob/221e8c0e155d5fe526080c6e56c6418e0433177d/fcmp%2B%2B.pdf)
- [FCMP++ Gist](https://gist.github.com/kayabaNerve/0e1f7719e5797c826b87249f21ab6f86)
- [Draft database tables by jberman](https://gist.github.com/kayabaNerve/0e1f7719e5797c826b87249f21ab6f86?permalink_comment_id=5054800#gistcomment-5054800)

## Boog900 | 2024-05-25T00:34:11+00:00
logs:

```
18:00:26 - boog900 (@boog900:monero.social): Meeting time! https://github.com/monero-project/meta/issues/1009
18:00:34 - boog900 (@boog900:monero.social): 1) Greetings
18:02:50 - m-relay: <p​lowsof> Hi
18:04:16 - hinto (@hinto:monero.social): hello
18:05:43 - boog900 (@boog900:monero.social): SyntheticBird said they might not be able to make today so lets move on to:
18:05:45 - boog900 (@boog900:monero.social): Updates: What is everyone working on?
18:06:19 - yamabiiko: Hi
18:06:51 - hinto (@hinto:monero.social): me: created a discussion for workspace lints: https://github.com/Cuprate/cuprate/issues/131
18:07:09 - boog900 (@boog900:monero.social): I spent the last week splitting up the big `Peer Set` PR into a few smaller PRs and adding tests.
18:07:52 - boog900 (@boog900:monero.social): I also created a proposal to significantly reduce node bandwidth usage: https://github.com/monero-project/monero/issues/9334
18:08:16 - yamabiiko: Not much to update on from my side - I'll be able to spend more time on the project from June
18:08:45 - boog900 (@boog900:monero.social): 3) Project: What is next for Cuprate? 
18:08:53 - boog900 (@boog900:monero.social): hinto: you wanted to discuss FCMPs in Cuprate 
18:09:26 - SyntheticBird: Hi, sorry for being late
18:10:11 - hinto (@hinto:monero.social): Yup, since Cuprate may have a binary ready by the time FCMP++ is callable, would it make sense to start moving that up in priority? Over things like ZMQ 
18:10:54 - SyntheticBird: What is ZMQ used for already? afaik only mining
18:11:21 - hinto (@hinto:monero.social): There's lots of internals we won't have to migrate if have FCMP++ in mind from the very start, i.e. database stuff
18:11:38 - hinto (@hinto:monero.social): *if we have
18:12:46 - boog900 (@boog900:monero.social): <@syntheticbird:monero.social "What is ZMQ used for already? af..."> it's another interface like RPC, but yeah P2pool is the only major user I know 
18:13:38 - hinto (@hinto:monero.social): Relevant changes needed for the database: https://gist.github.com/kayabaNerve/0e1f7719e5797c826b87249f21ab6f86?permalink_comment_id=5054800#gistcomment-5054800 
18:15:29 - hinto (@hinto:monero.social): AFAICT the changes are relatively straightforward but I'm wondering if there is a danger in implementing too early
18:16:31 - hinto (@hinto:monero.social): i.e. the longer we wait the more time audits/impl in monerod can reveal changes we also need to make
18:18:51 - SyntheticBird: Early generalization or abstractions might be beneficial. I don't think we should worry about implementation this early
18:19:29 - hinto (@hinto:monero.social): the reverse is that if FCMP++ comes out with no changes needed on our end, implementing code now with it in mind would probably be cheaper in the long run
18:23:34 - boog900 (@boog900:monero.social): IMHO I think it's too early to start working on FCMPs in Cuprate. We are pretty dependent on how monerod does things like tx encoding/ RPC interface so we would have to wait for the changes to be made there first or be pretty confidant in their current plan.
18:23:35 - SyntheticBird: Best case scenario would be to work on getting cuprate stable and at the same time importing FCMP++ codebase
18:23:57 - SyntheticBird: but we don't have this kind of devpower and none of us is familiar yet with it
18:24:20 - boog900 (@boog900:monero.social): And although we could bump it up in priority, I think there would be less people willing to work on FCMPs than ZMQ
18:26:15 - boog900 (@boog900:monero.social): I think our current design puts us in a much better position than monerod for integration aswell, it should be easier 
18:26:38 - SyntheticBird: FCMP being a rust library is also a pro, no need to worry about FFI
18:28:35 - boog900 (@boog900:monero.social): kayabanerve: are you planning to update monero-serai for FCMPs (I would guess so just want to make sure)
18:34:17 - hinto (@hinto:monero.social): boog900: did you want to do any of the integration? It seems like it touches mostly DB/RPC
18:35:30 - SyntheticBird: Changes to consensus might become clearer over time
18:35:36 - boog900 (@boog900:monero.social): Yeah I am happy to do the integration when the time comes 
18:35:54 - boog900 (@boog900:monero.social):  I am not saying we should prioritize things like ZMQ over FCMPs, just that it depends on timings
18:38:25 - boog900 (@boog900:monero.social): any thing else to discuss?
18:39:35 - hinto (@hinto:monero.social): I did want to discuss the integration but seems like that's for another time 
18:40:21 - hinto (@hinto:monero.social): feedback would be appreciated here on the `Lints (hot)` section: https://github.com/Cuprate/cuprate/issues/131
18:40:51 - hinto (@hinto:monero.social): turns out we can add workspace lints and it affects nothing since crates must opt in
18:43:35 - boog900 (@boog900:monero.social): If thats all I think we can end the meeting here, thanks everyone!
18:45:35 - SyntheticBird: thanks

```

# Action History
- Created by: Boog900 | 2024-05-17T00:05:49+00:00
- Closed at: 2024-05-25T00:34:33+00:00
