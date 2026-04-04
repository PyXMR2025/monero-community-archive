---
title: 'Cuprate Meeting #16 - Tuesday, 2024-08-13, UTC 18:00'
source_url: https://github.com/monero-project/meta/issues/1051
author: moo900
assignees: []
labels: []
created_at: '2024-08-06T19:06:33+00:00'
updated_at: '2024-08-13T19:44:09+00:00'
type: issue
status: closed
closed_at: '2024-08-13T19:44:09+00:00'
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

Previous meeting with logs: #1047

# Discussion History
## moo900 | 2024-08-13T19:44:08+00:00
## Meeting logs
```
boog900: 2) updates 
```
```
fluorescent_beige: I'm fixing the massive merge conflicts in my PR for issue #209, probably I'll just make a new branch and redo my changes there. Hope I can wrap it up quickly then
```
```
hinto: me: no updates, I think I will return from break within a couple days
```
```
boog900: Me: I completed the initial tx-pool PR and have began work on improving the dandelion pool efficiency.   
```
```
hinto: fluorescent_beige: looks bad... I think this was due to https://github.com/Cuprate/cuprate/pull/237
```
```
fluorescent_beige: > <@hinto:monero.social> fluorescent_beige: looks bad... I think this was due to https://github.com/Cuprate/cuprate/pull/237

Yes, I'll just rewrite.
```
```
boog900: 3) Project: What is next for Cuprate?
```
```
hinto: boog900: did you have any concrete thoughts on where the RPC handlers should be defined? IIRC you wanted them in `cuprated`
```
```
boog900: I think they would probably have to go in `cuprated`
```
```
hinto: Is there a reason why they can't be in a separate `cuprate-rpc-handler` crate that pulls in the necessary deps?
```
```
boog900: it will need access to pretty much all services, some of which will be defined in `cuprated` 
```
```
hinto: but practically speaking, `cuprated` doesn't exist yet so how that would this work, where would code be written?
```
```
hinto: maybe in a separate crate for the meanwhile? the services it needs access to can be `let resp = todo!()` then filled in when 'moved' into the binary?
```
```
boog900: right now you would only be able to complete the endpoints that don't require the services yet to be made.

```
```
boog900: you could still be able to work in `cuprated`, but if you would rather work in a separate crate for now that's fine by me
```
```
hinto: do you have a `binaries/cuprated` ready to be merged soon? I could put code there
```
```
hinto: it could just be a skeleton as well
```
```
boog900: Yeah I did start working on it for the P2P syncer but closed the PR as I wanted to clean it up. I'll reopen it without the syncer and just the skeleton.
```
```
boog900: I am thinking of creating a bounty for the creation of a Rust lib to interact with monerod's DB, which would conform to our DB `tower::Service` interface.

This would be useful for 2 projects I have in mind, one is a RPC server that uses monerod's DB and our RPC server. The other is a monerod fast syncer that uses our P2P and fast sync crate.

hinto do you think this is a good idea? 
```
```
boog900: It would give our Rust lib use cases apart from Cuprate
```
```
boog900:  * It would give our Rust crates use cases apart from Cuprate
```
```
hinto: what is the purpose of the 1st? to have a faster RPC server on-top of `monerod`'s DB?
```
```
hinto: the purpose of the 2nd is to sync `monerod` faster than `monerod` itself can?
```
```
boog900: monerod doesn't handle RPC traffic well 
```
```
boog900: > <@hinto:monero.social> the purpose of the 2nd is to sync `monerod` faster than `monerod` itself can?

yes
```
```
hinto: when `monerod` grabs an exclusive write lock for the DB, how is the Rust RPC side supposed to know not to read?
```
```
boog900: LMDB should handle that right?
```
```
boog900: IIRC the restriction on re-sizing is only at a process level right? multiple process are ok with one resizing 
```
```
hinto: http://www.lmdb.tech/doc/group__mdb.html#gaa2506ec8dab3d969b0e609cd82e619e5
```
```
hinto: while a resize occurs, no transactions must exist, i.e. if `monerod` is resizing, Rust RPC should _not_ be opening a read tx, how is it supposed to know?
```
```
boog900: > It may be called at later times if no transactions are active **in this process**. Note that the library does not check for this condition, the caller must ensure it explicitly.
```
```
boog900: > If the mapsize is increased by another process, and data has grown beyond the range of the current mapsize, mdb_txn_begin() will return MDB_MAP_RESIZED. This function may be called with a size of zero to adopt the new size.
```
```
hinto: oh I see
```
```
boog900: > <@boog900:monero.social> > If the mapsize is increased by another process, and data has grown beyond the range of the current mapsize, mdb_txn_begin() will return MDB_MAP_RESIZED. This function may be called with a size of zero to adopt the new size.

do we handle this btw?
```
```
hinto: was wondering how block explorers worked without segfaulting all the time
```
```
hinto: > <@boog900:monero.social> do we handle this btw?

probably not as well as we could: https://github.com/Cuprate/cuprate/blob/59adf6dcf8a1adfbfbf05583866f6c5b0d85b374/storage/service/src/service/write.rs#L129-L130
```
```
hinto: it will resize, but IIRC the default is to add a fixed amount of bytes, so if process resized way below it wouldn't be enough
```
```
hinto: then again, I'm pretty sure `monerod` would freak out if you started touching `data.mdb`
```
```
boog900: yeah I was just thinking we probably don't need to handle this as no one should be writing to our DB 
```
```
boog900: do you think this is a good idea?
```
```
boog900: (the bounty)
```
```
hinto: so basically the goal is an alternative RPC server? `monerod` does everything _but_ RPC?
```
```
boog900: also gives Cuprate's crates more use cases 
```
```
boog900: but yes 
```
```
boog900: that and the fast syncer, the bounty would just be for monerod's DB in our Service interface 
```
```
hinto: it does sound good, but is it worth building more on-top the current DB/RPC interfaces when a hardfork is around the corner?
```
```
boog900: the next HF is probably at least 6 months away, more than likely more, I think we will have enough warning
```
```
hinto: IMO I would focus resources towards parts that won't change, then focus on the ideas after the hardfork
```
```
boog900: tbf this is a bounty which will hopefully attract some new people 
```
```
boog900: I think waiting for the HF would be a mistake as we haven't even got a solid date yet 
```
```
hinto: If the goal is delivering middleware binaries then I think we would be the most suited to write it, both in speed and correctness
```
```
hinto: If the goal is to deliver `cuprated` ASAP (I think this is the case), then I think it's a bit of a distraction since`cuprated` is a better overall solution to any node problems
```
```
hinto: If the goal is to attract people then sure, although there's other things that could be worked on too right?
```
```
syntheticbird: From a user perspective, cuprated should come before middleware binaries
```
```
syntheticbird: a unified solution let people generate bug reports and performance data that are then beneficials for the middleware binaries
```
```
syntheticbird: that are most likely never going to be used by simple users
```
```
boog900: The thing is a 1.0 `cuprated` binary is still some time away IMO.

These tools are a way for people to use Cuprate while still relying on monerod for the important stuff
```
```
boog900: like block/tx validation 
```
```
boog900: > <@hinto:monero.social> If the goal is delivering middleware binaries then I think we would be the most suited to write it, both in speed and correctness

true although this bounty would just be for the DB interface 
```
```
boog900: and it actually solves a problem that I know cake + others were having issues with during the spam 
```
```
syntheticbird: > <@boog900:monero.social> and it actually solves a problem that I know cake + others were having issues with during the spam 

they are craving for single consensus parallel rpc
```
```
syntheticbird: afaik
```
```
syntheticbird: so it would be a little like monerod in proxy mode?
```
```
hinto: hmm I think it's a balance between cost / delivery speed / correctness
```
```
hinto: boog900: we would be able to create this RPC server better and faster than a bounty, although it "costs" time/energy away from `cuprated`
```
```
hinto: reversely, a bounty would allow us to focus more on `cuprated`, but then the RPC server would most likely be delivered slower
```
```
hinto: I'm ok with it if you think it's a good tradeoff, I just hope it doesn't take away too much from `cuprated`
```
```
boog900: I think it's worth a go, IMO I don't think it will take much away from `cuprated` 
```
```
boog900: It would be delivered slower than if we were to work on the server now, however it could still be delivered quicker than us working on cuprated and then moving to the RPC server 
```
```
boog900: I do understand your point about correctness, however I still think we should try it and see how it goes 
```
```
boog900: I'll write it out soon
```
```
boog900: 4) Any other business
```
```
syntheticbird: can moo have a profile picture ?
```
```
moo: no
```
```
boog900: moo has spoken
```
```
boog900: ok I think we can end here 
```
```
boog900: thanks everyone!
```
```
hinto: thanks
```
```
syntheticbird: thanks
```
```
boog900: !meeting 
```

# Action History
- Created by: moo900 | 2024-08-06T19:06:33+00:00
- Closed at: 2024-08-13T19:44:09+00:00
