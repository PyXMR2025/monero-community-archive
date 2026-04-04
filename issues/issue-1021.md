---
title: ' Cuprate Meeting #7 - Tuesday, 2024-06-11, 18:00 UTC '
source_url: https://github.com/monero-project/meta/issues/1021
author: Boog900
assignees: []
labels: []
created_at: '2024-06-09T23:01:40+00:00'
updated_at: '2024-06-18T00:14:06+00:00'
type: issue
status: closed
closed_at: '2024-06-18T00:14:05+00:00'
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

Previous meeting with logs: #1017

# Discussion History
## Boog900 | 2024-06-18T00:14:05+00:00
logs:

```
18:00:37 - boog900 (@boog900:monero.social): Meeting time: https://github.com/monero-project/meta/issues/1021
18:00:45 - boog900 (@boog900:monero.social): 1) Greetings 
18:01:14 - SyntheticBird: Hi
18:02:36 - m-relay: <p​lowsof> Hi
18:02:49 - boog900 (@boog900:monero.social): 2. Updates 
18:02:52 - hinto (@hinto:monero.social): hello
18:03:16 - yamabiiko: Hi
18:04:15 - boog900 (@boog900:monero.social): Me: I am very close to finishing the block downloader, will hopefully have that ready tonight 
18:04:45 - hinto (@hinto:monero.social): me: no updates, expecting to continue straightforward work on rpc porting and the architecture book
18:04:52 - SyntheticBird: Me: Been testing some syncing related commits and building cuprate's new website
18:05:48 - yamabiiko: No updates from me as well, except that I plan to start actively contributing later this month
18:08:43 - boog900 (@boog900:monero.social): Also I was contacted by a hackathon team at moneroKon who wanted to work on Cuprate, they worked on implementing fast sync and managed to implement one of the requests, they said they will work on completing it    
18:09:34 - boog900 (@boog900:monero.social): lets move onto:
18:09:40 - boog900 (@boog900:monero.social): 3. Project: What is next for Cuprate?
18:10:33 - SyntheticBird: I would like to ask if ZMQ is necessary for testnet release
18:11:07 - boog900 (@boog900:monero.social): <@syntheticbird:monero.social "I would like to ask if ZMQ is ne..."> IMO no
18:12:28 - SyntheticBird: The roadmap is fast-sync, RPC, then binary
18:12:47 - SyntheticBird: I will use my newly migrated VM to build the fully verified database for building fast-sync table
18:12:57 - hinto (@hinto:monero.social): boog900: re: replacing `enum Key` with `Cow<str>` in `json-rpc`: serde can't always pass a ref into data due to https://github.com/serde-rs/json/issues/742#issuecomment-772446812
18:13:59 - hinto (@hinto:monero.social): I rather not use `Cow<str>` here since it means a `String` will be allocated each time it happens
18:14:49 - hinto (@hinto:monero.social): would be bad if you could DoS a Cuprate node/client by sending a bunch of extra key fields with escaped/unicode characters
18:15:04 - boog900 (@boog900:monero.social): The string will have to be allocated anyway even with `Key`.... right?
18:16:12 - boog900 (@boog900:monero.social): Otherwise how would the reference to the string be made? 
18:16:41 - hinto (@hinto:monero.social): `Key` (u8) gets allocated on the stack, and the field gets ignored in the current impl, it's a visitor so no allocation AFAICT
18:17:07 - boog900 (@boog900:monero.social): it has to be deserialized first though 
18:17:51 - boog900 (@boog900:monero.social): https://github.com/hinto-janai/cuprate/blob/007c9adac735654a9f5bceb06fd13374aed8d729/rpc/json-rpc/src/response.rs#L250
18:18:53 - hinto (@hinto:monero.social): isn't that visiting key fields in the original JSON?
18:19:42 - boog900 (@boog900:monero.social): <@hinto:monero.social "boog900: re: replacing `enum Key..."> you can't make `&str` references into the original JSON because of this issue I thought 
18:21:13 - hinto (@hinto:monero.social): outside of the `'de` lifetime I believe
18:21:50 - hinto (@hinto:monero.social): I think the `&str` `visit_str` has access to is just the raw JSON so it can include backslashes
18:24:42 - hinto (@hinto:monero.social): AFAICT the macro serde impl needs `Cow<str>` instead of `&str` since it might need to allocate, when we manually impl we get to decide 
18:25:32 - hinto (@hinto:monero.social): none of the fields we're looking for contain weird characters so I don't think we need to allocate 
18:38:02 - boog900 (@boog900:monero.social): are you sure this is the case?
18:38:50 - boog900 (@boog900:monero.social): I tried looking at `serde_json` but can't find the right section, it'll take too much time
18:39:34 - boog900 (@boog900:monero.social): if `&str` includes extra chars then the `str` wouldn't be equivalent to the fields name right? 
18:42:03 - hinto (@hinto:monero.social): I'll find more assertive docs to link to later
18:43:27 - hinto (@hinto:monero.social): I believe the `&str` in `visit_str` is raw, i.e. if the field was `\nhello` then the `&str == r#""\nhello""#`
18:44:18 - hinto (@hinto:monero.social): in which point macro serde would see that and allocate
18:44:35 - hinto (@hinto:monero.social): here's another impl: https://docs.rs/jsonrpsee-types/0.23.1/src/jsonrpsee_types/response.rs.html#183-230
18:46:34 - boog900 (@boog900:monero.social): alright
18:47:01 - boog900 (@boog900:monero.social): anything else people want to discuss?
18:47:54 - SyntheticBird: Not that I can think of
18:48:47 - boog900 (@boog900:monero.social): oh wait 
18:48:58 - boog900 (@boog900:monero.social): I think I found the section 
18:50:23 - boog900 (@boog900:monero.social): it seems `serde_json` keeps an allocated `String` scratch pad 
18:51:09 - boog900 (@boog900:monero.social): https://github.com/serde-rs/json/blob/24d868f4e9be428afa1c744f8218a32660a1e0bf/src/de.rs#L1527
18:54:14 - boog900 (@boog900:monero.social): if no one has anything else they want to discuss I think we can end the meeting here
18:56:19 - boog900 (@boog900:monero.social): Thanks everyone 
18:56:38 - SyntheticBird: Thanks
18:57:42 - hinto (@hinto:monero.social): thanks
```

# Action History
- Created by: Boog900 | 2024-06-09T23:01:40+00:00
- Closed at: 2024-06-18T00:14:05+00:00
