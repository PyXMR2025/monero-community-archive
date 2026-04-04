---
title: 'Cuprate Meeting #32 - Tuesday, 2024-12-03, UTC 18:00'
source_url: https://github.com/monero-project/meta/issues/1115
author: moo900
assignees: []
labels: []
created_at: '2024-11-26T19:08:43+00:00'
updated_at: '2024-12-03T19:03:06+00:00'
type: issue
status: closed
closed_at: '2024-12-03T19:03:05+00:00'
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

Previous meeting with logs: #1111

# Discussion History
## moo900 | 2024-12-03T19:03:05+00:00
## Meeting logs
```
boog900: meeting time: https://github.com/monero-project/meta/issues/1115
```
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
boog900: Me: I fixed `get_range` in upstream `heed` however I have been struggling to get it working with our abstraction layer. 
```
```
hinto: me: mostly finished reviews, working on https://github.com/Cuprate/benches, will start on binary/other RPC handlers soon
```
```
boog900: I know a hacky way to get it working, but to get it working in a nice way will require more changes in `heed` - I am planning to make an issue there
```
```
boog900: 3) Project: What is next for Cuprate?
```
```
boog900: anything anyone wants to discuss today?
```
```
hinto: Is this because 1) it's a hard abstraction problem, 2) `cuprate_database` makes it hard, or 3) `heed` makes it hard?
```
```
syntheticbird: hello
```
```
syntheticbird: sorry for being late
```
```
syntheticbird: no update
```
```
boog900: 2 & 3. The problem is that `heed` use certain concrete types to change the comparison function used on a DB. This comparison type shows in the struct signature as a generic which then makes each DB with a different comparison function a different type.

It is now hard to map a comparison function choice made by a type impl'ing our `Key` to either heed's special types (default or integer) or the custom comparison function. 
```
```
boog900: if the comparison function didn't show in the database signature we would be fine or if heed didn't use special concrete types we would be fine.
```
```
boog900: or if specialization was stabilized we would (probably) be fine
```
```
boog900: We got around this before by just not setting the comparison function when opening the database only when creating the database. LMDB remembers the choice and heed gives us a database with a default comparison function.
```
```
boog900: However the `range` functions use the comparison function in `heed`, which means they don't work when you do this.
```
```
hinto: The solutions short-term seem to be:

1. Turning `get_range` -> `for r in range { get(r) }`
1. Adding a hacky `get_range` to `cuprate_database`
1. Hard-coding some comparator fns for certain tables?

which do you think would be better until this is fixed? (considering these choices will eventually have to be fixed long-term)

```
```
hinto: Or would solving this now correctly be better?
```
```
boog900: I think we go with 2 and hope `heed` accepts removing the comparator from the signature 
```
```
hinto: btw this just finished running, here's some examples of benchmark data/visuals:

- All benches: https://benches.hinto.rs/moo/criterion/38541db/report/
- `cuprate_cryptonight`: https://benches.hinto.rs/moo/criterion/38541db/cuprate_cryptonight/report/index.html
- Data: https://github.com/Cuprate/benches/tree/main/data/moo/criterion/38541db
```
```
hinto: GH pages for this is pretty nice although I think repo limits will be an issue, that 1 run alone is 43MB.
```
```
syntheticbird: Could there be in long-term future automated report in case of performance regression ?
```
```
syntheticbird: I don't think its a good idea but I wonder if it would be easily possible
```
```
boog900: > <@hinto:monero.social> GH pages for this is pretty nice although I think repo limits will be an issue, that 1 run alone is 43MB.

what is the limit, if you know?
```
```
syntheticbird:  * I don't think its a good idea but I wonder if it would be easily possible with Actions
```
```
hinto: https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github#repository-size-limits

> We recommend repositories remain small, ideally less than 1 GB, and less than 5 GB is strongly recommended.
```
```
hinto: ~23 more of those benchmarks will go past 1GB
```
```
boog900: is there an automatic way to purge old data?
```
```
boog900: keeping 20 past runs is probably enough 
```
```
hinto: if we're storing in git, we can remove + rebase. I think force pushing this would mark them for eventual removal on GH's side, not 100% sure what they do here though
```
```
hinto: I'm hoarding every single run locally
```
```
boog900: does anyone have anything else they want to discuss?
```
```
syntheticbird: ^

```
```
syntheticbird: Forget the Actions, but what about automated performance test in the future, when internal API is settled
```
```
hinto: I agree, having some automation here would be nice. Not sure what the best way to do it would be though.
```
```
syntheticbird: I brought it up but I'm skeptical, maybe I don't know enough about it but I wonder how we will decide that n% variations in benchmark can simply be ignored
```
```
syntheticbird: for me it sounds like these ignore rules would be on a case per case basis
```
```
hinto: I proposed before that we could make moo automate this on the GH side but it may be easier to introduce an off-the-shelf bot
```
```
hinto: yes, stuff are benchmarks are heuristics
```
```
hinto: stuf like*
```
```
boog900: anything else or we can end here?
```
```
syntheticbird: I think we re good
```
```
boog900: ok thanks everyone!
```
```
boog900: !meeting 
```

# Action History
- Created by: moo900 | 2024-11-26T19:08:43+00:00
- Closed at: 2024-12-03T19:03:05+00:00
