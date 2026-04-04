---
title: 'Cuprate Meeting #30 - Tuesday, 2024-11-19, UTC 18:00'
source_url: https://github.com/monero-project/meta/issues/1108
author: moo900
assignees: []
labels: []
created_at: '2024-11-12T18:38:24+00:00'
updated_at: '2024-11-19T20:14:42+00:00'
type: issue
status: closed
closed_at: '2024-11-19T20:03:51+00:00'
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

Previous meeting with logs: #1104

# Discussion History
## moo900 | 2024-11-19T20:03:51+00:00
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
spirobel:  [======··············] 
```
```
boog900: Me: I continued working on integrating fast-sync but I have decided to put that on hold for a bit as it was more complicated than expected. Instead I have been working on binary startup.
```
```
hinto: me: Have been reviewing https://github.com/Cuprate/cuprate/pull/308 for the past couple days to make sure everything looks correct, should be ready for review by end of week. Also planning to review https://github.com/Cuprate/cuprate/pull/304 today.
```
```
boog900: 3) Project: What is next for Cuprate?
```
```
hinto: boog900: does #344 need #304?
```
```
boog900: yep and #303
```
```
hinto: are there other things that could be worked on? I think the merge conflicts (if any) may be a bit painful
```
```
hinto: there's #196, #330, #333 that need review and #337 can be changed/merged
```
```
boog900: > <@hinto:monero.social> are there other things that could be worked on? I think the merge conflicts (if any) may be a bit painful

the amount of code just in 344 is actually pretty small, I have finished the main part, and am currently syncing `cuprated`. I only really need to clean it up a bit.
```
```
boog900: I did want to discuss command parsing in `cuprated`, in 344 I used `clap`, so to change log level you would give the command `set_log -l debug`
```
```
boog900: Does anyone have anything against using clap here?
```
```
boog900: > <@hinto:monero.social> there's #196, #330, #333 that need review and #337 can be changed/merged

Yeah I'll start working through these.
```
```
boog900: ```
2024-11-19T18:20:59.626888Z  INFO Handling batch to main chain height: 1583713
2024-11-19T18:21:00.455366Z  INFO Handling batch to main chain height: 1583734
2024-11-19T18:21:02.363217Z  INFO Handling batch to main chain height: 1583755
```
```
hinto: command parsing at runtime via stdin?
```
```
boog900: yes
```
```
m-relay: <p​lowsof> noticed this in -dev regarding an LMDB fix upstream which might be useful for cuprate https://libera.monerologs.net/monero-dev/20241119#c461466
```
```
hinto: took a brief look at the stdin impl in #344, seems ok
```
```
boog900: > <@m-relay:monero.social> <p​lowsof> noticed this in -dev regarding an LMDB fix upstream which might be useful for cuprate https://libera.monerologs.net/monero-dev/20241119#c461466

We don't use encryption so I don't think that applies to us but thank you for letting us know.
```
```
m-relay: <p​lowsof> 👍
```
```
boog900: anything else anyone wants to discuss?
```
```
hinto: re: discussion - for long-lasting impl decisions I would prefer if short proposals/documents/specs were made before code, both to narrow the ideas and make it clearer for review what is intended
```
```
hinto: I think there are a few adhoc impl decisions that have been made (from me as well) that could have benefited from deeper/longer discussion although I guess this is a time tradeoff
```
```
boog900: Yeah this is true, also the backlog of docs/book pages I need to write is getting pretty large. I'll keep it in mind for the future. These last couple months I have felt like a working binary has been very close and then something keeps coming up. I think now we are literally touching distance (I am running a draft `cuprated` right now) when this is merged I plan to work more on all the jobs that have been semi-neglected up until this point, improving API/docs/testing etc. 
```
```
boog900: There are still somethings missing, like handling bad alt chains that have enough cumulative difficulty will make us crash but for an alpha version I am ok with it.
```
```
hinto: There's a risk going too far to the perfection extreme where there is no deadline in sight, although I'm more worried about the project going to the other extreme (get it working asap and never touch it again), which I think is more common. In general though I think the project is progressing at a good rate, but I think we should be aware of this\ and stay somewhere in the middle.
```
```
kayabanerve: FYI, monero-serai is expected to have a 4 month code freeze (starting from ~now). I don't love that and plan to start on a derivative.
```
```
spirobel: > <@boog900:monero.social> anything else anyone wants to discuss?

i was wondering if we can merge this: https://github.com/Cuprate/cuprate/pull/334 and something about epee varint sizes ...
```
```
kayabanerve: Also, I have a Q. Has any thoughts been given to TX types which don't deserialize and validate, solely deserialize? Maybe using borrows internally over a bytestream/something like the bytes crate?
```
```
hinto: kayabanerve: would that be an opportunity to start a new repo for the library in `monero-oxide`?
```
```
kayabanerve: One immediate such idea would be making Transaction generic to the point type as point decompressions/compressions are extremely expensive.
```
```
kayabanerve: hinto: Undecided. I think it should be

Fork
Patch
Use patched version
Get audit results
Fix audit issues
Re-patch audited lib

And I'd like to resolve with a git history of 

Current
Audit fixes
Additional patches
```
```
hinto: spirobel: what/how many types are you using and what is your timeline for when they are needed? If the answer is not many + soon then I think it'll be worth re-implementing the types used and using `cuprate-epee-encoding` directly
```
```
kayabanerve: We could clone Serai into monero-oxide, create a branch there, then downscope/patch? Fix audit issues on Serai, have monero-oxide re-pull from Serai, then redo downscope/patch?
```
```
kayabanerve: Or we use Serai's next branch which already made minor tweaks to monero-serai because I made some tweaks to its dependencies.
```
```
kayabanerve: Feel free to comment a preference
```
```
boog900: > <@kayabanerve:matrix.org> Also, I have a Q. Has any thoughts been given to TX types which don't deserialize and validate, solely deserialize? Maybe using borrows internally over a bytestream/something like the bytes crate?

I have defiantly thought about it, at the time I thought it would be too complicated to implement outside of monero-serai, we would need to re-impl tx (de)serialization and I didn't think the added complexity would be appreciated in monero-serai. 
```
```
boog900: I decided having a tx type with cached data would be a better approach: https://github.com/Cuprate/cuprate/issues/191
```
```
kayabanerve: I think it's an optimization. If consumers are at the point they want optimizations, I'd support them if we can do them to standards.
```
```
kayabanerve: Making a Transaction<Pruned = NotPruned, Deserialization = Full> and introducing Deserialization = Minimal sounds amenable if y'all are at such a level.
```
```
kayabanerve: Caching hashes should be a fraction of the work compared to the EC ops. If you fetch TXs from the DB, and don't immediately send out the raw bytes but instead deser, do any partial accesses/reser, then that should be a nontrivial percent

```
```
kayabanerve: Just wanted to open the discussion. We can kick it to an issue
```
```
boog900: hashing requires EC ops though, through the serialization.
```
```
kayabanerve: Yes that's why I'm suggesting Deserialization = Minimal to remove the EC ops
```
```
kayabanerve: Then hashing is just a hash
```
```
spirobel: > <@hinto:monero.social> spirobel: what/how many types are you using and what is your timeline for when they are needed? If the answer is not many + soon then I think it'll be worth re-implementing the types used and using `cuprate-epee-encoding` directly

the types are in the grayzone between wallet and node. would be good to share them between nodes and wallets.
```
```
boog900: > <@spirobel:kernal.eu> i was wondering if we can merge this: https://github.com/Cuprate/cuprate/pull/334 and something about epee varint sizes ...

I'll try get it done soon, what is your question on epee varints?
```
```
hinto: spirobel: they will be eventually but it will be a while before I can setup rigorous testing across all types to make sure they really work everywhere - is it only `get_blocks.bin` that is needed for now?
```
```
spirobel: > <@hinto:monero.social> spirobel: they will be eventually but it will be a while before I can setup rigorous testing across all types to make sure they really work everywhere - is it only `get_blocks.bin` that is needed for now?

yes that is what is needed currently. I already got it working splendidly by patching this function https://github.com/Cuprate/cuprate/blob/b6c4adc83a199886d6f932c1321857fb8a535af5/rpc/types/src/bin.rs#L298 by using the types as a client we can make sure it meets the expectations that exist elsewhere 
```
```
hinto: ok thanks, will submit a PR soon
```
```
spirobel: > <@boog900:monero.social> I'll try get it done soon, what is your question on epee varints?

i was wondering how big it needs to be to prevent overflows in any case. serai also has a function to parse it https://github.com/serai-dex/serai/blob/dc1b8dfccd68b7c2eb4359a1e37b55ce5e4453b5/networks/monero/rpc/src/lib.rs#L824 or should the resulting type be dependent on the respective epee type that is being deserialized ?
```
```
boog900: a `u64` can hold the max value although it is often used for container sizes which need to be `usize`
```
```
kayabanerve: I fucking hate that piece of Serai code D:
```
```
spirobel: > <@boog900:monero.social> a `u64` can hold the max value although it is often used for container sizes which need to be `usize`

this is the place where we get the possible max size from, right? https://github.com/monero-project/monero/blame/893916ad091a92e765ce3241b94e706ad012b62a/src/common/varint.h#L69 https://github.com/monero-project/monero/commit/a70bf86037575ecb1bb2c8b1103deeb2fd1c0ae5#diff-1ebe2484093489afe3be3a0d2ebf8eb048670929bccc8379e721730e9f4de0a3L62 
```
```
spirobel: > <@kayabanerve:matrix.org> I fucking hate that piece of Serai code D:

first time I see kaya use language haha 
```
```
boog900: That is the other varint format 
```
```
boog900: Monero has 2
```
```
kayabanerve: I swear a lot, I just try not to swear in code or as much in a professional context
```
```
kayabanerve: There's probably a few MRL meetings I've sworn during but I'm unsure if you'll find "fuck" there
```
```
kayabanerve: I just truly hate Serai's half-baked single-use domain-specific epee fn
```
```
boog900: https://github.com/monero-project/monero/blob/893916ad091a92e765ce3241b94e706ad012b62a/contrib/epee/include/storages/portable_storage_from_bin.h#L238
```
```
kayabanerve: But we either have this, validated for a sjngle RPC response, or need validation of the entire undocumented protocol and an entire lib for it
```
```
kayabanerve: I stand by my limited scoping, I just still hate it
```
```
boog900: !meeting 
```

# Action History
- Created by: moo900 | 2024-11-12T18:38:24+00:00
- Closed at: 2024-11-19T20:03:51+00:00
