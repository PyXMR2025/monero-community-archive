---
title: 'Cuprate Meeting #40 - Tuesday, 2025-01-28, UTC 18:00'
source_url: https://github.com/monero-project/meta/issues/1144
author: moo900
assignees: []
labels: []
created_at: '2025-01-21T19:10:48+00:00'
updated_at: '2025-01-28T19:17:19+00:00'
type: issue
status: closed
closed_at: '2025-01-28T19:17:19+00:00'
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
- [Project roadmap for 2025](https://github.com/Cuprate/cuprate/issues/376)

- Any other business

Previous meeting: #1140

# Discussion History
## moo900 | 2025-01-28T19:17:18+00:00
## Meeting logs
```
boog900: meeting time: https://github.com/monero-project/meta/issues/1144
```
```
boog900: 1) Greetings 
```
```
syntheticbird: hi
```
```
hinto: hello
```
```
boog900: 2) Updates 
```
```
boog900: Me: I worked on some performance improvements, the DB `SyncMode` and also this: https://github.com/Cuprate/cuprate/issues/174
```
```
boog900: currently working on fast sync 
```
```
syntheticbird: me: posted a reddit post on syncing achievement to check reactions, measure if people forgot about us and also hype them up. I've learned two things: 1. People are excited. 2. I'm really  bad in english.
```
```
hinto: me: test syncing `cuprated`, the VPS in #195 is currently at 2630148 and is on-pace to have a total sync time of ~22 hours. also left some misc review/PRs.
```
```
syntheticbird: 22 hours vs 6.29 days, insane
```
```
boog900: Thats literally only with changing the DB sync mode right? 
```
```
syntheticbird: I think yeah
```
```
boog900: my sync included the 174 changes I made
```
```
hinto: yes, `SyncMode::Async` -> `SyncMode::Fast` in the config
```
```
boog900: nice, I am excited for fast sync 
```
```
syntheticbird: placing bets?
```
```
boog900: 4 hrs
```
```
syntheticbird: 3 hours
```
```
boog900: (we have inside knowledge that the p2p block downloader can download the chain in 2 hrs)
```
```
hinto: for reference, `monerod` with fast-sync is ~15x faster on the VPS, applying that to `cuprated` would make for 2.2 hours
```
```
boog900: 3) Project: What is next for Cuprate?

```
```
hinto: err, less than that actually, closer to 1.5 hours (seems a bit infeasible, probably will hit some bottleneck)
```
```
boog900: if the internet connection is good enough and you have sufficient peers you could probably get below 2 hrs 
```
```
syntheticbird: cuprate with fast sync be like: `cp peer@blockchain .`
```
```
syntheticbird: for what is next with cuprate i think we can directly jump to Project roadmap
```
```
hinto: I want to talk about `SyncMode`: https://doc.cuprate.org/cuprate_database/config/enum.SyncMode.html
```
```
hinto: I think I want to get rid of `Async` as having either `Safe` or `Fast` seems to cover most (all?) usecases
```
```
hinto: it serves no purpose for `redb` as well as `Fast` maps to the same value
```
```
syntheticbird: sgtm
```
```
hinto: Also, ideally I think the `#[default]` should be `FastThenSafe`, but until that is implemented, it is  up for debate whether it should be `Fast` or `Safe`
```
```
boog900: hinto: do you know what `NO_SYNC` and `MAP_ASYNC` together will do?
```
```
hinto: it could also be argued that `Threshold` should be removed due to adding impl complexity and not that much value
```
```
boog900: from LMDB docs it sounds like they do separate things and shouldn't be used together 
```
```
boog900: http://www.lmdb.tech/doc/group__internal.html#ga44d5cd326db2e18f12c59c3eca2c1a3a
```
```
syntheticbird: iirc correctly NO_SYNC is literally not asking the OS to flush maps to disk. MAP_ASYNC is just hinting it should do it. 
```
```
syntheticbird: when NO_SYNC is enabled it's literally at OS good willing to do so
```
```
syntheticbird: on windows that might increase memory usage
```
```
syntheticbird: would need to check to be sure tho
```
```
boog900: so by that explanation the ASYNC flag does nothing 
```
```
boog900: when used with NO_SYNC
```
```
syntheticbird: yes
```
```
syntheticbird: depending on the implementation, i don't know which one overload the other
```
```
syntheticbird: but clearly both together is unsound
```
```
boog900: yeah I believe one of the 2 flags is cancelling the other 
```
```
hinto: I read `mdb.c` last time but still can't make any assertions
```
```
hinto: it's worth noting hyc was the one who combined those flags: https://github.com/monero-project/monero/blame/90359e31fd657251cb357ecba02c4de2442d1b5c/src/blockchain_db/lmdb/db_lmdb.cpp#L1444
```
```
syntheticbird: Maybe for operating system specific behavior
```
```
syntheticbird: like some OS do not support ASYNC so it should resolve to NO_SYNC instead
```
```
boog900: ok yeah we can look into it later, I would be ok with just a `Safe` & `Fast`
```
```
syntheticbird: I also agree default should be FastThenSafe
```
```
hinto: there is still the question of what `cuprated 0.0.1`'s default sync mode be: `Safe` or `Fast`
```
```
boog900: fast
```
```
boog900: too big of a difference 
```
```
syntheticbird: yeah fast
```
```
syntheticbird: Disclaimer tho, with NO_SYNC if the kill switch kicks in in the middle of the sync we can say goodbye to the db
```
```
syntheticbird: FastThenSync should be implemented imo
```
```
syntheticbird: * FastThenSafe should be implemented imo
```
```
hinto: Unless, we were to implement `FastThenSafe` before 0.0.1, an easy but perhaps hacky way to do it would be:
1. Create global `static SYNCED: AtomicBool`
2. Downloader code sets `SYNCED` to true upon sync
3. DB code checks `SYNCED` every so often to switch its sync mode
```
```
syntheticbird: yeah sounds good
```
```
syntheticbird: Zebra isn't shy on using AtomicBool
```
```
syntheticbird: i don't think it's hacky, just not within the codebase habits
```
```
hinto: it could be scoped such that no global is required, i.e. `Arc<AtomicBool>` is passed to only the downloader and DB code 
```
```
hinto: I think there are other parts of the code that would benefit from read access though, e.g. RPC needs it
```
```
syntheticbird: ah yeah right I missed the global static part
```
```
syntheticbird: it's hacky but doable, I don't have any concerns
```
```
boog900: We could just add a parameter to the add block request `syncing` or something 
```
```
boog900:  * We could just add a parameter to the add block request `syncing: bool` or something
```
```
boog900: it's easy to see if a block came from the downloader/a gossip 
```
```
syntheticbird: yes also, it's literally size free because of padding
```
```
hinto: scoped write access would work too:
rust
// downloader code

// can be modified within file
static SYNCED: AtomicBool = /* ... */

// other crates can read
pub fn synced() -> bool {
	SYNCED.load()
}

```
```
syntheticbird: the clear advantage of global variable. It's simple and flexible enough
```
```
syntheticbird: We might want to jump to roadmap for the last 20 minutes
```
```
syntheticbird: this can be discussed later on a draft PR
```
```
boog900: -[Project roadmap for 2025](https://github.com/Cuprate/cuprate/issues/376)
```
```
syntheticbird: I have zero objections on this roadmap fwiw
```
```
hinto: Points that need consensus:
- Beneficiaries are correct and will be prioritized (in that order)
- Considering the above, the laid out 2025 roadmap values will be focused on over others
```
```
hinto: The Q{1,2,3,4} timings can be adjusted, the Q1 alpha `cuprated` goal is only my own, I haven't thought of accurate time estimates yet for the rest
```
```
syntheticbird: Re beneficiaries: The order is good to me. UX for operators can come later on. We would also get better feedback from public node operators than from individual users (without undermining the value of their report obv)
```
```
syntheticbird: does services = businesses ?
```
```
hinto: for the purpose of that list, organization = any larger scale operation of `cuprated` 
```
```
syntheticbird: I'm not sure we can respect ordered priority tho. I can see feedback advantages but developers and individual users might open issue that we find more relevant than organization needs. I don't want them to feel excluded. If you could redefine what you mean by priority just to be sure, that might help
```
```
boog900: yeah I wouldn't like to prioritize any group all the time  
```
```
syntheticbird: or really slightly at most
```
```
boog900: i.e. if exchanges now wanted us to remove dandelion++ should we?
```
```
boog900: no, obviously, but we should make that clear by not prioritizing them
```
```
boog900:  * no, obviously, but we should make that clear by not explicitly prioritizing them
```
```
syntheticbird: Yeah I think explicitly is the keyword. We can responsibly value organization over users or the opposite.
```
```
hinto: FWIW the point of having a loose priority there is to make sure there is no confusion in the future about what current dev power should be going towards, changes that affect organizations can be seen as the most bang-for-buck as it will also affect downstream, but it's not always the reverse case.

Demands from a group that negatively impacts others would/should be contended before consideration.
```
```
hinto: with that said, I don't think it matters too much for now, this can be discussed another time
```
```
boog900: hinto: I think we should bring back the alpha release date by 1 month 
```
```
boog900: February instead of March  
```
```
hinto: I am ok with starting in Feb, although ideally if the CCS process goes smooth then I'd like to buy/rent hardware, setup, and sync test more before the release cycle starts
```
```
hinto: are there other goals that should be in Q1?
```
```
hinto: there are a bunch of smaller more technical ones, those could be listed as well
```
```
hinto: e.g. any `C-bug` or `C-proposal` issue
```
```
boog900: fast-sync, tx-pool relay rules 
```
```
boog900: improving logging/stdin commands 
```
```
hinto: Ok, will update the issue to reflect this meeting
```
```
boog900: anything else anyone wants to discuss?
```
```
boog900: I think we can end here 
```
```
boog900: Thanks everyone
```
```
hinto: thanks
```

# Action History
- Created by: moo900 | 2025-01-21T19:10:48+00:00
- Closed at: 2025-01-28T19:17:19+00:00
