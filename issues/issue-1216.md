---
title: 'Cuprate Meeting #59 - Tuesday, 2025-06-10, UTC 18:00'
source_url: https://github.com/monero-project/meta/issues/1216
author: moo900
assignees: []
labels: []
created_at: '2025-06-03T18:58:57+00:00'
updated_at: '2025-06-10T18:56:18+00:00'
type: issue
status: closed
closed_at: '2025-06-10T18:56:18+00:00'
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

Previous meeting: #1212

# Discussion History
## moo900 | 2025-06-10T18:56:17+00:00
## Meeting logs
```
boog900: 1) greetings 
```
```
syntheticbird: Hi
```
```
syntheticbird: well seems like i'm not the only one late
```
```
boog900: 2) updates 
```
```
boog900: me: I worked on changing how the tx-pool is kept in sync with the blockchain, removing the need for a RWLock. It's ready but waiting on 483
```
```
syntheticbird: Me: Successfully integrated Arti into Cuprate. We're capable of connecting to onion nodes, run an onion service within cuprate for inbound and use Arti for anonymizing outgoing clearnet connections. I'm also finishing up the changes on dandelion for broadcasting tx over Tor (thx to boog900 for helping me with this)
```
```
syntheticbird: I saw that PR, mind explaining it briefly? 
```
```
boog900: the context cache and blockchain DB are separate 
```
```
boog900: you run into a problem if you need data from both and the blockchain updates between getting the data 
```
```
fluorescent_beige: I'm preparing my talk for monerokon, not directly cuprate related but I want to ask you about one thing. Will open a WIP PR for #209 and finish it asap too
```
```
boog900: I think hinto may have started that in 503
```
```
syntheticbird: https://github.com/Cuprate/cuprate/pull/503
```
```
fluorescent_beige: Ok
```
```
boog900: 3) Project: What is next for Cuprate?
```
```
boog900: anything to discuss while we wait for hinto?
```
```
hinto: hello, sorry for being late
```
```
hinto: update: CCS milestone https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/543#note_30251, working on wallet sync support for RPC and planning other various things
```
```
hinto: fluorescent_beige: I did start testing DB hotswap in 503, I can close it if work is being done
```
```
hinto: also, I don't think our CI properly covers redb currently
```
```
fluorescent_beige: > <@hinto:monero.social> fluorescent_beige: I did start testing DB hotswap in 503, I can close it if work is being done

I dragged it for so long that I can't really complain if I was unassigned. Idk how much work you put in it, if you want to close yours or if I should drop my work on it instead, I'm fine with both.
```
```
hinto: I have not done much, although I do believe I could get it done relatively quickly
```
```
fluorescent_beige: Let's say I try to get done until next week, and otherwise you'll take over?
```
```
hinto: sure, I'd mention that there is also `redb-memory`, so 3 hotswappable backends to support 
```
```
fluorescent_beige: Yes, I noticed.
```
```
hinto: the code is in `Env::open` @ `storage/database/src/backend/redb/env.rs`
```
```
hinto: it is just an `if cfg!(feature = "redb-memory")`, it could be replaced with something like:

rust
enum Backend {
	Heed,
	Redb,
	RedbMemory,
}

let end = match backend {
	/*...*/
}


```
```
hinto: `let env`*
```
```
fluorescent_beige: So you don't want to follow the idea to swap the backend upstream in the blockchain/txpool init() functions anymore?
```
```
hinto: I think that can stay the same, the `Config` in `cuprate_blockchain::open` will be passed down eventually to the  redb `Env::open` where it will branch again
```
```
hinto: so maybe `Config` should have a `backend: Backend` field
```
```
hinto: maybe calling it `Lmdb` not `Heed` would be better for end-users btw
```
```
fluorescent_beige: Yes, that's how I was doing it. But our plan was to have different DatabaseReadHandle and DatabaseWriteHandle initializations based on which back end we have. So the database hotswap PR would touch the blockchain and txpool modules too.
```
```
hinto: is the plan still runtime hotswap? i.e. edit `Cuprated.toml` to use a different backend?
```
```
fluorescent_beige: My understanding was hotswap means at runtime. I. e. one build of cuprate can be run with different backends via config or command line option.
```
```
syntheticbird: For me HOTswap at RUNTIME, means literally changing the db on the fly at runtime
```
```
syntheticbird: not changing at bootime
```
```
fluorescent_beige: So an already running node throws away its database and starts to sync anew with a different one?
```
```
boog900: no
```
```
syntheticbird: no
```
```
boog900: the DB should be configurable without a recompile, so at boot-time  
```
```
syntheticbird: like thats what I understand when I read it, but I understand that it really just mean "change the db in config instead of recompiling cuprate"
```
```
syntheticbird: bad naming
```
```
fluorescent_beige: Let's call it lukewarmswap then?
```
```
syntheticbird: sounds good
```
```
syntheticbird: We should have just named this PR: "Support for multiple database backend" but then I feel like a dejavu
```
```
syntheticbird: * We should have just named this PR: "Support for multiple database backend through config" but then I feel like a dejavu
```
```
syntheticbird: im polluting a bit sry
```
```
boog900: the database crate still becomes hot-swappable 
```
```
hinto: a draft PR would clarify things, although if the plan is the same as before then seems OK
```
```
fluorescent_beige: OK I'll make a draft PR
```
```
boog900: anything else to discuss today? 
```
```
syntheticbird: not from my end
```
```
boog900: ok I think we can end here
```
```
boog900: thanks everyone!
```
```
syntheticbird: thx
```
```
hinto: thanks
```
```
boog900: !meeting 
```

# Action History
- Created by: moo900 | 2025-06-03T18:58:57+00:00
- Closed at: 2025-06-10T18:56:18+00:00
