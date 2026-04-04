---
title: ' Cuprate Meeting #5 - Tuesday, 2024-05-28, 18:00 UTC '
source_url: https://github.com/monero-project/meta/issues/1014
author: Boog900
assignees: []
labels: []
created_at: '2024-05-25T00:44:47+00:00'
updated_at: '2024-05-29T20:14:25+00:00'
type: issue
status: closed
closed_at: '2024-05-29T20:14:25+00:00'
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

Previous meeting with logs: #1009



# Discussion History
## Boog900 | 2024-05-29T20:14:25+00:00
```
18:01:03 - boog900 (@boog900:monero.social): Meeting time https://github.com/monero-project/meta/issues/1014
18:01:07 - boog900 (@boog900:monero.social): 1) Greetings 
18:02:22 - hinto (@hinto:monero.social): hello
18:03:24 - m-relay: <p​lowsof> hi
18:03:40 - boog900 (@boog900:monero.social): Hi, lets move to 2) updates
18:04:14 - boog900 (@boog900:monero.social): hinto:  CCS was moved to funding 🎉
18:05:25 - hinto (@hinto:monero.social): me: working on a the initial design draft for RPC, and worked on mostly repo/CI related stuff last week
18:06:38 - boog900 (@boog900:monero.social): Me: I've been working on the block downloader, I decided to re-write the prototype one in the peer-set PR. I also did some final work on the consensus PR, I think it's ready for review now 
18:07:33 - boog900 (@boog900:monero.social): I think we can move onto: 
18:07:47 - boog900 (@boog900:monero.social): 3) Project: What is next for Cuprate?
18:09:00 - boog900 (@boog900:monero.social): I did want to bring up the binary name again (https://github.com/Cuprate/cuprate/pull/42) I have changed my mind and think I prefer `cuprate-node` rather than `cuprated`
18:10:11 - boog900 (@boog900:monero.social): hinto: do you have a preference? 
18:11:04 - boog900 (@boog900:monero.social): (or anyone else in the meeting)
18:11:57 - hinto (@hinto:monero.social): I am okay with `cuprated` or `cuprate-{node,daemon}` - the d suffix has history behind it (and I think I prefer it) but maybe it makes sense for Cuprate naming to be more 'modern'
18:14:43 - hinto (@hinto:monero.social): `cuprate` is also tempting but it will get confusing if we ever create another binary 
18:16:49 - hinto (@hinto:monero.social): I wanted to discuss our root directories: I was going to adjust our label CI and thought we might as well create the skeleton too (`rpc/`, `zmq/`, etc)
18:17:53 - hinto (@hinto:monero.social): boog900: what root directories do you foresee in the future?
18:18:39 - boog900 (@boog900:monero.social): yep, I guess well have to wait for SyntheticBird to be the deciding vote, unless anyone else wants to chime in
18:19:23 - m-relay: <p​lowsof> reg cuprated, history seems to be 'name of coin + d' so theres room for change if required 
18:24:06 - boog900 (@boog900:monero.social): <@hinto:monero.social "boog900: what root directories d..."> `rpc`, `zmq` and `binaries` unless we were to put each binary as it's own root directory
18:24:32 - boog900 (@boog900:monero.social): just off the top of my head ^
18:25:13 - boog900 (@boog900:monero.social): I would want a separate directory for binaries as then it will be easy to isolate the AGPL code  
18:25:32 - hinto (@hinto:monero.social): If we were to move our books in-tree, would it be `books/{protocol, architecture}/`?
18:26:16 - boog900 (@boog900:monero.social): ah yeah, so `books` as well 
18:29:52 - hinto (@hinto:monero.social): what about `benchmarks/` or `benches/`? Or should these be per crate i.e. `database/benchmarks/` - we could still detect this with the label CI
18:34:48 - boog900 (@boog900:monero.social): I think I would prefer them to be together so + `benches` 
18:36:19 - hinto (@hinto:monero.social): last naming question: what should the separated `storage/` crates be called? https://github.com/Cuprate/cuprate/pull/138
18:36:50 - hinto (@hinto:monero.social): currently I have `cuprate-database/` which is our high-level service API, then `key-value/` as a non-Monero related database abstraction
18:38:38 - boog900 (@boog900:monero.social): when the txpool comes is that going to be another directory?
18:39:28 - hinto (@hinto:monero.social): I was thinking `storage/cuprate-{txpool,transaction-pool}`
18:42:16 - boog900 (@boog900:monero.social): I would do `key-value` ->`cuprate-database`, `cuprate-database` -> `cuprate-blockchain` and `cuprate-{txpool,transaction-pool}`

So the 3 crates would be: `cuprate-database`, `cuprate-blockchain` and `cuprate-{txpool,transaction-pool}`
18:44:36 - hinto (@hinto:monero.social): is the `cuprate-` naming okay for `key-value`? it has 0 connection with Monero/Cuprate
18:45:11 - hinto (@hinto:monero.social): do you have a preference for `cuprate-txpool` or `cuprate-transaction-pool`?
18:48:06 - boog900 (@boog900:monero.social): <@hinto:monero.social "is the `cuprate-` naming okay fo..."> I think so
18:48:15 - boog900 (@boog900:monero.social): <@hinto:monero.social "do you have a preference for `cu..."> `cuprate-txpool`
18:50:30 - boog900 (@boog900:monero.social): I don't mind if you would rather not have the cuprate name there though 
18:51:57 - hinto (@hinto:monero.social): I don't mind either way but there's crates like `async-buffer` so I was thinking non-Monero related stuff followed a no prefix/suffix naming scheme
18:55:18 - boog900 (@boog900:monero.social): The crate naming scheme so far has been pretty loose tbf
18:56:00 - boog900 (@boog900:monero.social): You are right though that is roughly how I have been doing it
18:56:36 - hinto (@hinto:monero.social): okay - will open a PR formalizing it in `CONTRIBUTING.md`
18:57:11 - boog900 (@boog900:monero.social): thanks!
18:57:30 - boog900 (@boog900:monero.social): 4) Any other business
19:00:18 - boog900 (@boog900:monero.social): hinto: would you mind if I took over the Cuprate binary PR/ started it from scratch, some things like the syncer should be put in there IMO as they don't really make sense in the P2P crates 
19:01:42 - boog900 (@boog900:monero.social): It's going to be pretty bare bones for now, just enough to start everything up
19:03:14 - hinto (@hinto:monero.social): sure, I think you should close the old PR and open a new one
19:06:11 - boog900 (@boog900:monero.social): Yep alright, anything else people want to discuss or we can end here 
19:08:59 - boog900 (@boog900:monero.social): ok we can end here, thanks everyone!
```

# Action History
- Created by: Boog900 | 2024-05-25T00:44:47+00:00
- Closed at: 2024-05-29T20:14:25+00:00
