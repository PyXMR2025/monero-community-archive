---
title: 'Cuprate Meeting #93 - Tuesday, 2026-03-10, UTC 18:00'
source_url: https://github.com/monero-project/meta/issues/1348
author: moo900
assignees: []
labels: []
created_at: '2026-03-03T18:27:57+00:00'
updated_at: '2026-03-10T18:43:03+00:00'
type: issue
status: closed
closed_at: '2026-03-10T18:43:03+00:00'
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

Previous meeting: #1345

# Discussion History
## moo900 | 2026-03-10T18:43:01+00:00
## Meeting logs
```
boog900: 1) greetings 
```
```
hinto: hello
```
```
boog900: 2) updates 
```
```
boog900: Me: ported the wip RPC changes to the new db branch, on the RPC stage branch. Also found and fixed a bug in the tapes 
```
```
hinto: me: testing new DB changes
```
```
hinto: It synced <24hr with max 2GB, no OOMs and has been stable - this is full verification fyi, IIRC it took ~4 days with old cuprated although I'll be testing it again
```
```
sbt: meow
```
```
boog900: Wow 
```
```
boog900: That's crazy 
```
```
boog900: How many threads? 
```
```
hinto: 🎉
```
```
hinto: 6
```
```
boog900: I didn't realize how much it would improve full verification sync 
```
```
hinto: I wonder if I could get away with 1GB...
```
```
boog900: I would try fast sync first 
```
```
hinto: although we still don't have numbers on memory usage of a public `cuprated` getting hit with a bunch of RPC requests
```
```
hinto: I assume OOMs will occur there
```
```
boog900: Yeah with 2GBs. Although we could and will add a rate limit to prevent this.
```
```
boog900: 3) Project: What is next for Cuprate?
```
```
boog900: I'll be opening a CCS soon to work on RPC 
```
```
boog900: Current numbers are with cuprate a local wallet can fully sync in under 23 minutes, with monerod it was over an hour. 
```
```
hinto: do you plan on making any large changes to the existing RPC system?
```
```
boog900: No not really 
```
```
boog900: Just filling in what's already there 
```
```
boog900: > <@boog900:monero.social> Current numbers are with cuprate a local wallet can fully sync in under 23 minutes, with monerod it was over an hour. 

This can be self tested with the RPC stage branch too 
```
```
boog900: Also we will no longer have 0xFFC working on RPC, they closed their CCS 
```
```
jbabb: I have been cleaning up and cherrypicking old work forward, porting it from the original monero-serai to monero-wallet.  here's an example:
```
```
jbabb: https://github.com/sneurlax/cuprate/tree/feat/regtest
```
```
jbabb: idk if this is going to be useful for or suitable in mainline cuprate but I am using it to test monero wallet development and multisig stuff using something very similar to this. but the older code is called cuprate-simnet and is pretty dirty, I didn't want to show that yet, personal project stuff
```
```
jbabb: anyways that included some very very minor mostly-mock rpc stuff. what all's needed for rpc?
```
```
jbabb: and should I update this by merging new-db into it or is it just a dead end tech demo at this point?
```
```
jbabb: this is an example of the point: https://github.com/Cuprate/cuprate/compare/main...sneurlax:cuprate:feat/regtest#diff-0fae4dcac8928774cbb0c9feac8a6173077c2f66624cf2574984dd3aae75ceb9
```
```
jbabb: motivation: I was doing some Alice, Bob, and Charlie multisig experiments and needed something quicker than stagenet for testing
```
```
jbabb: finally, I wonder if the RPC work lines up with this because ideally we could control this regtest node over RPC and that's where I was going to go with it next
```
```
boog900: hmm is that code filling in monero-oxide's RPC traits with our DB backend?
```
```
jbabb: yes lol
```
```
boog900: ah nice kayaba has been asking me to do something like that 
```
```
jbabb: I considered it just a hack to get what I wanted
```
```
boog900: it wont help with the real RPC sadly though 
```
```
jbabb: can I find out about RPC work needed via https://github.com/Cuprate/cuprate/issues?q=is%3Aissue%20state%3Aopen%20rpc ?
```
```
boog900: As our DB currently only allows 1 process to access it, I don't know if it will be usable in a real world project ngl 
```
```
boog900: but it is still cool 
```
```
jbabb: does that apply to new-db, too?
```
```
jbabb: I had merged that in and resolved conflicts enough for it to run last night but need to clean it up before pushing
```
```
jbabb: then I wondered if I even needed to do that--that is, if it should even be PRed at all (I think no, not in this state, anyways)
```
```
boog900: the old DB alllows multi-process access, the new one (on the new-db branch) does not.
```
```
hinto: current (LMDB) allows multi-process access, redb and new-db (fjall) both do not
```
```
hinto: off by 1 second
```
```
boog900: I think if you impl the traits for the tower::Service DB interface it could be useful  
```
```
boog900: as that will be exposed when people embed cuprated
```
```
jbabb: it was useful just personally for playing with a new p2pool-rs and some sharechain work in addition to testing multisig tx flows but idk what a "real" cuprate regtest mode would look like or enable
```
```
jbabb: would such a mode or some end-to-end tests enabled by that be helpful at all or is everything else needed more important?
```
```
jbabb: * would such a mode or some end-to-end tests enabled by that be helpful at all or is everything else that's* needed more important atm?
```
```
boog900: it would be helpful, especially for the people already using monerod in regtest mode. I think it should work in the same way to monerod.
```
```
boog900: I have already thought of making a kind of tx fuzzer and testing them against both nodes, that sort of mode will be needed I think 
```
```
boog900: anything else to discuss today?
```
```
boog900: I think we can end here, thanks everyone!
```

# Action History
- Created by: moo900 | 2026-03-03T18:27:57+00:00
- Closed at: 2026-03-10T18:43:03+00:00
