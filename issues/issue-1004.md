---
title: 'Cuprate Meeting #3 - Tuesday, 2024-05-14, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1004
author: Boog900
assignees: []
labels: []
created_at: '2024-05-09T15:53:15+00:00'
updated_at: '2024-05-17T00:15:15+00:00'
type: issue
status: closed
closed_at: '2024-05-17T00:15:15+00:00'
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
- Any other business

Please comment on GitHub in advance of the meeting if you would like to propose a discussion topic.

Previous meeting with logs: #1000

# Discussion History
## Boog900 | 2024-05-17T00:15:03+00:00

Logs:
```
18:00:37 - boog900 (@boog900:monero.social): Meeting time https://github.com/monero-project/meta/issues/1004
18:00:40 - boog900 (@boog900:monero.social): 1) Greetings 
18:00:48 - SyntheticBird: Hi
18:02:08 - hinto (@hinto:monero.social): hello
18:02:28 - boog900 (@boog900:monero.social): 2. Updates: What is everyone working on?
18:03:41 - hinto (@hinto:monero.social): me: fixing CI, boog900: seems like downgrading gcc works
18:04:24 - boog900 (@boog900:monero.social): Me: I have spent the majority of the time last week fixing the issues in the consensus code I mentioned last meeting, should be done now, just need to add more tests  
18:04:32 - boog900 (@boog900:monero.social): <@hinto:monero.social "me: fixing CI, boog900: seems li..."> Thats good, lets hope LMDB/gcc fixes the issues that caused this 
18:04:49 - hinto (@hinto:monero.social): 1 more reason to rewrite `cryptonight/`, using MSVC would be a lot less painful
18:04:57 - boog900 (@boog900:monero.social): 3. Project: What is next for Cuprate?
18:05:21 - SyntheticBird: 2.*
18:05:55 - boog900 (@boog900:monero.social): counting from 0?
18:06:14 - SyntheticBird: 1. Updates
then
1. Project
18:06:21 - SyntheticBird: f*cking markdown
18:06:49 - hinto (@hinto:monero.social): I haven't caught up on RPC yet, boog did you have any more thoughts on it?
18:06:49 - SyntheticBird: you said 1. in greetings, 1. in updates, 1. in project next
18:07:38 - boog900 (@boog900:monero.social): Greetings ?!?
18:07:43 - boog900 (@boog900:monero.social): <@hinto:monero.social "1 more reason to rewrite `crypto..."> true although I don't think that would be an easy task 
18:08:46 - SyntheticBird: <@boog900:monero.social "Greetings ?!?"> Oh nvm its my matrix client that automatically transformed it into 1.
18:10:37 - boog900 (@boog900:monero.social): <@hinto:monero.social "I haven't caught up on RPC yet, ..."> not at the moment 
18:12:51 - boog900 (@boog900:monero.social): My plan, now the consensus code is fixed, is to start working on getting the p2p code ready to test a full sync, I am hoping in a week or 2 it will be ready.
18:13:08 - SyntheticBird: Hinto's CCS is expected to be merged this saturday?
18:14:51 - hinto (@hinto:monero.social): SyntheticBird: you mentioned OpenRPC docs last meeting, are these WIP, is there a link?
18:17:01 - SyntheticBird: Yes. I received some critics I needed to address. (I still didn't addressed them but will). 
repo: https://github.com/SyntheticBird45/monero-open-rpc
18:17:17 - SyntheticBird: The only things lacking are examples
18:18:27 - SyntheticBird: Be aware, this document only treat /json_rpc methods. All methods in other paths are not documented
18:20:38 - SyntheticBird: Monerod issues for reference: https://github.com/monero-project/monero/issues/9186
18:25:46 - hinto (@hinto:monero.social): boog900: thoughts on this? seems like it helps the RPC doc accuracy problem (although only for half the methods)
18:27:04 - SyntheticBird: I was originally writing it for a bounty but when I realized I would have to make 15k lines of high quality JSON to grab 1 XMR I abandon. one of my goal is for the core RPC doc to be complete and merge it into monerod repo
18:30:03 - boog900 (@boog900:monero.social): <@hinto:monero.social "boog900: thoughts on this? seems..."> I'm not sure, are you suggesting we generate this in Cuprate and host separate docs, or use this to test Cuprates methods? 
18:35:59 - hinto (@hinto:monero.social): Oh wait, SyntheticBird do you have to handwrite OpenRPC? Is it not generated?
18:41:58 - hinto (@hinto:monero.social): regardless I think creating an automated system that checks our RPC schema is one of those long-term things we should be doing
18:45:30 - boog900 (@boog900:monero.social): true however I think we would need monerod to adopt a system first, as otherwise we wont have anything to test against 
18:48:07 - SyntheticBird: <@hinto:monero.social "Oh wait, SyntheticBird do you ha..."> Yes. And yes it was painful
18:48:40 - hinto (@hinto:monero.social): right, `monerod` <-> `cuprated` is harder to test, but we can at least test against our own types?
18:50:34 - boog900 (@boog900:monero.social): I don't know what we would test against though? 
18:51:19 - SyntheticBird: There are at the moment no consensus on the RPC. Also OpenRPC test tool is disastreous
18:51:51 - SyntheticBird: It hasn't been updated in 5 years
18:52:44 - hinto (@hinto:monero.social): <@boog900:monero.social "I don't know what we would test ..."> if `cuprated` responds with the object that it should be responding with
18:53:07 - hinto (@hinto:monero.social): again though, getting the reference object type would be manual
18:54:37 - boog900 (@boog900:monero.social): ah ok, yeah
18:59:03 - hinto (@hinto:monero.social): not much to talk about until we start implementing though, I think we can end the meeting :)
19:00:51 - boog900 (@boog900:monero.social): My internet is playing up ... 
19:01:07 - SyntheticBird: Geomagnetic storm hit again
19:01:09 - boog900 (@boog900:monero.social): yep we can end the meeting here, thanks everyone!
19:02:19 - SyntheticBird: Thanks everyone
```

# Action History
- Created by: Boog900 | 2024-05-09T15:53:15+00:00
- Closed at: 2024-05-17T00:15:15+00:00
