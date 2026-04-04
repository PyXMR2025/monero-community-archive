---
title: 'Cuprate Meeting #77 - Tuesday, 2025-11-25, UTC 18:00'
source_url: https://github.com/monero-project/meta/issues/1298
author: moo900
assignees: []
labels: []
created_at: '2025-11-18T18:40:37+00:00'
updated_at: '2025-11-25T19:01:48+00:00'
type: issue
status: closed
closed_at: '2025-11-25T19:01:48+00:00'
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

Previous meeting: #1295

# Discussion History
## moo900 | 2025-11-25T19:01:47+00:00
## Meeting logs
```
boog900: 1. greetings
```
```
hinto: hello
```
```
boog900: 2. Updates 
```
```
boog900: me: I have been working on FCMP tree building still, trying to make sure it is as efficient as possible. Also added shutdown code to cuprated, as with database split across 2 systems it is a bit more fragile. 
```
```
hinto: me: preparing `cuprated v0.0.8` and finishing up on PoWER tests to match C++/Rust output
```
```
boog900: current tree building is pretty much a background task and is only interacted with when needed, which is different to how monerod currently does it.
```
```
boog900: 3) Project: What is next for Cuprate?
```
```
boog900: I intend to review the 0.0.8 PR today
```
```
boog900: I juts need to check the hashes 
```
```
hinto: It assumes 562 is included as well
```
```
hinto: The killswitch for 0.0.7 activates tomorrow so hopefully we can release today?
```
```
boog900: yeah sure 
```
```
boog900: how do you feel about the linear tape DB? I haven't marked it as ready for review yet but they is quite a bit of unsafe in there.
```
```
boog900: also atomics 
```
```
boog900: I tried to add a loom test but loom doesn't like memory maps IIRC 
```
```
boog900: also Miri doesn't like memory maps 
```
```
boog900: I have thought about putting it in its own repo?
```
```
hinto: AFAIC if there is sufficient usage and testing then go wild
```
```
boog900: nice, is this something you have experience in for the review?

If not then no worries
```
```
hinto: both the memory map and atomic usage don't seem too complicated
```
```
rucknium: boog900: Do you have a rough estimate of how much database "overhead" there is in `monerod`'s database? In the scaling discussion, it would be good to know how much padding needs to be added to the FCMP tx size numbers.
```
```
boog900: ah thats good then, I should be able to mark it ready for review soon
```
```
boog900: here as the raw table sizes as of a couple weeks ago:

boog900: 
4.0K	./lock.mdb
21G	./data.mdb
11G	./rct_outputs.tape
18G	./prunable/stripe2.tape
17G	./prunable/stripe1.tape
18G	./prunable/stripe6.tape
18G	./prunable/stripe3.tape
18G	./prunable/stripe7.tape
18G	./prunable/stripe5.tape
18G	./prunable/stripe8.tape
18G	./prunable/stripe4.tape
139G	./prunable
27G	./pruned.tape
196G	.


The `stripeX.tape`s store the prunable part of all txs in the different pruning strips, `pruned.tape` stores block headers, miner txs, the pruned blobs and the prunable hashes (32 bytes) for each tx.
```
```
boog900: so we can just sum `pruned.tape` and the `stripeX.tape` for an estimate of the size of all the tx/block blobs in the DB, which comes to 170 GB
```
```
rucknium: Thanks! Is it reasonable to say "monerod's database is X GB, cuprate's is Y GB. We should pad FCMP tx sizes by (X/Y - 1)%"?
```
```
rucknium: What is the status of cuprate's RPC? If I can, I would like to make a cuprate-compatible version of https://stressnetnode1.moneronet.info/ for beta stressnet. These are the calls that I use: get_info, get_transaction_pool_stats, get_last_block_header, get_fee_estimate, get_connections, get_bans
```
```
rucknium: I don't necessarily have to have all those RPC methods available.
```
```
boog900: hmm, honestly I am not sure if it'll work out like that, it all depends on how LMDB deals with the values. Smaller values _should_ lead to less wasted space (I would think) and by just using the total DB sizes you are including all database tables, some of which have small values. 
```
```
boog900: LMDB database size highly depends on it reclaiming old pages too, you can get a database huge by just holding open a read tx while monerod is syncing 
```
```
hinto: This would be cleaner although you'll have to setup CI to be as strict as Cuprate/cuprate and maintain it over time
```
```
hinto: Rucknium: here's a list of the currently activated endpoints: https://user.cuprate.org/rpc.html
```
```
hinto: many of those are actually practically ready but the focus is on endpoints required by wallet2 for now, unless boog900 wants to change that :)
```
```
boog900: your best bet would probably be to note this and as a best effort you can make a calculation like that as an example? 
```
```
rucknium: hinto: Thanks. Everything I need is available 😁
```
```
boog900: I think I would like to do this, for now, I think it will be easier to make changes to it especially as I am using it across multiple branches right now 
```
```
hinto: boog900: perhaps we could enable certain "incomplete" endpoints for now, lots of them are not since misc fields aren't available / don't make sense for `cuprated` e.g. `get_info`: https://github.com/Cuprate/cuprate/blob/a9ef306bdbfee3b2ff11f11f3553cc645471dc57/binaries/cuprated/src/rpc/handlers/json_rpc.rs#L452
```
```
rucknium: Wait. I think I misread the table
```
```
rucknium: 😅
```
```
boog900: I have a branch in waiting for wallet sync support 
```
```
boog900: I'll PR that at some point 
```
```
boog900: I wanted to make the changes to the DB first though
```
```
boog900: `get_info` is needed for wallet sync so I exposed it on that branch 
```
```
boog900: `get_connections` would be the only one I am unsure if we could support quickly 
```
```
boog900: anything else for today? 
```
```
boog900: ok I think we can end here, thanks everyone!
```

# Action History
- Created by: moo900 | 2025-11-18T18:40:37+00:00
- Closed at: 2025-11-25T19:01:48+00:00
