---
title: 'Cuprate Meeting #100 - Tuesday, 2026-04-28, UTC 18:00'
source_url: https://github.com/monero-project/meta/issues/1376
author: moo900
assignees: []
labels: []
created_at: '2026-04-21T19:05:47+00:00'
updated_at: '2026-04-28T18:59:23+00:00'
type: issue
status: closed
closed_at: '2026-04-28T18:59:23+00:00'
---

# Original Description
[Cuprate](https://github.com/Cuprate/cuprate) is an effort to create an alternative Monero node implementation.

Location: [Libera.chat, #cuprate](https://libera.chat/) | [Matrix](https://matrix.to/#/#cuprate:monero.social?via=matrix.org&via=monero.social)

[Join the Monero Matrix server if you don't already have a Matrix account](https://www.getmonero.org/resources/user-guides/join-monero-matrix.html)

Time: 18:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html)

Moderator: @Boog900

Please comment on GitHub in advance of the meeting if you would like to propose a discussion topic.

Main discussion topics:

1. Greetings
2. Updates: What is everyone working on?
3. Project: What is next for Cuprate?
4. Any other business

Previous meeting: #1370

# Discussion History
## MarkoPohlo | 2026-04-27T18:51:52+00:00
Would like to propose an agenda item for tomorrow, around a potential, Cuprate-specific CCS proposal to get a temperature check as to its value proposition.

In short, the proposal would revolve around expanding the fuzzing test suite to cover the consensus-critical surface, setting it up with OSS-Fuzz for continuous coverage, and setting up differential fuzzing against monerod to catch any divergences in how the two implementations validate blocks and transactions.

If there's a different space to get that initial feedback, please let me know. Happy to chat more about specifics/scoping!





## Boog900 | 2026-04-27T21:36:03+00:00
Yeah we can discuss that in the meeting.

## moo900 | 2026-04-28T18:59:22+00:00
## Meeting logs
```
boog900: 1) greetings 
```
```
m-relay: <M​arkoPohlo> hey everyone
```
```
redsh4de: hello
```
```
boog900: Hi! 
```
```
syntheticbird: Hi
```
```
boog900: 2) updates
```
```
boog900: Me: I have begun splitting up the RPC changes I have done to PR them. I started with updating monero-oxide which is open now. With hinto gone I don't know if I should wait for
reviews anymore or should I just merge?
```
```
boog900: SyntheticBird: what do you think?
```
```
syntheticbird: me: pushed a fix for onion address proptest. Currently looking at improving supply chain security
```
```
syntheticbird: better wait for at least a review, may it be me or external. I took a look at reviewing monero-oxide PR, I can review it today.
```
```
syntheticbird: s/ a / one /
```
```
redsh4de: me: worked on some nits for the graceful shutdown PRs
```
```
boog900: yeah that one is easy, it's the bigger ones I worry about 
```
```
boog900: relying on volunteers to review my work could become a bottleneck, but I guess we can deal with it when that happens. 
```
```
syntheticbird: i concur with that.
```
```
boog900: 3) Project: What is next for Cuprate?
```
```
boog900: MarkoPohlo: had a proposal they would like to discuss today
```
```
m-relay: <M​arkoPohlo> Yup, let me collect my thoughts, one sec.
```
```
boog900: sure
```
```
m-relay: <M​arkoPohlo> So, we (Runtime Verification) have been looking into Cuprate and the Monero fuzzing landscape, and wanted to check if there would be interest in extending Cuprate's existing fuzzing to consensus rules and setting up differential fuzzing against monerod? Based our experience it's a very effective way to surface divergences, this would add structured
```
```
m-relay: <M​arkoPohlo> fuzzing where it matters most.
```
```
m-relay: <M​arkoPohlo> If getting CCS funding at this time is a challenge, we could scope out an exploratory 1 month-only deliverable to at least get structured cargo-fuzz targets over consensus rules wired into CI (plus the beginning of a grammar that's reusable for FCMP++ when that lands).
```
```
m-relay: <M​arkoPohlo> Or, start with building out a grammar for FCMP++ blocks/transactions and a specification alongside it, so it can be used for fuzzing both monerod and Cuprate, and can also guide the development of Cuprate. Just wanted a temperature check today tbh, we can scope out something specific if this truly aligns with a clear value-add for the Monero
```
```
m-relay: <M​arkoPohlo> community around Cuprate.
```
```
boog900: Having a tool to fuzz cuprated against monerod is something I do think would be quite beneficial to have before a 1.0. I do worry that this is not a small job though and the fact that a lot is still changing at the moment with cuprated. Although our consensus has and probably will stay static for now.

We would want to have tx signing and block creation, both invalid and valid forms. Maybe we could reduce the scope by only doing currently enfoced rules/TXs. monero-oxide can be used for a lot of valid tx creation, which could help with an initial version.

```
```
boog900: FCMP++ has not even got TX types done in Rust yet FWIW
```
```
syntheticbird: I would personally find this work interesting. However the development of Cuprate is pretty detached from the consensus decisions of the Monero project, we and other members are following along the meetings and respecting consensus decision on many matters, but the authoritative specification is the monerod source code. There are no formal consensus specifications. I'm not hopeful on how maintaining this fuzzing target would look like. I'm also confused what you mean by grammar here, if this is a framework for consensus rules that would require you to redo the work of digging up meetings, reading the source code etc... The risks of consensus divergence with your work would be the exact same as Cuprate. For it to be robust, this framework maintenance would need to be incorporated into monerod development. I'm enumerating my concerns, but again I find it interesting.
```
```
boog900: we are a bit behind the C++ daemon there
```
```
boog900: I don't want to discourage this type of work, but IMHO I do think now may be a bit early for it.
```
```
syntheticbird: Yeah I think its clear that the final objective is ideal but the work is very heavy.
```
```
jbabb: Comparing Cuprate to monerod has been fruitful in the past, I'd recommend it and I would be interested in looking into any sort of fuzzing harness.  Even if the results find that Cuprate and monerod match, showing some meaningful work with reproducible findings can be helpful for CCS purposes, but it won't guarantee funding and could end up being work you do for free.  But like others have mentioned, it'd be interesting and if you do find differences it'd be even more interesting
```
```
m-relay: <M​arkoPohlo> Boog, that's exactly what we had in mind for the much scoped-down deliverable that can be built upon in the future - only doing currently enfoced rules/TXs . As far as maintenance, if monerod changes, the harness just catches new divergences, it doesn't need to be updated to match a spec. And by grammar I mean a structured input generator for the
```
```
m-relay: <M​arkoPohlo> fuzzer: something that produces syntactically valid blocks and transactions to feed into both cuprated and monerod, so the fuzzer explores interesting code paths instead of getting stuck on deserialization. But appreciate the feedback!
```
```
boog900: would the fuzzer attempt to sign txs validly? 
```
```
boog900: I know that's what fuzzing is, but for consensus we would need to make sure some rules that will pretty much never be satisfied by fully random data are not holding us back from finding issues in other rules.

```
```
m-relay: <M​arkoPohlo> Also, from what I understand monerod has a fuzzing harness setup by Ada Logic, and it's likely that we can adapt it for differential fuzzing against Cuprate, which makes diff fuzzing not too difficult of a next step.
```
```
m-relay: <M​arkoPohlo> Yea, the fuzzer would need to produce validly signed transactions to get past signature checks and actually exercise the consensus rules underneath. That's where monero-oxide helps, I believe.
```
```
boog900: yeah ok nice we are on the same page.
```
```
m-relay: <M​arkoPohlo> And, basically that's why we need grammar/structured input data - so we supply well-formed inputs and get to the actual validation code, and not just blast random data that gets rejected every time.
```
```
boog900: You may need custom ones from monero-oxide to hit some consensus rules. Like torsioned key images, as monero-oxide wont allow you to sign txs with them.
```
```
m-relay: <M​arkoPohlo> But since this is a deep topic and we only have so my time here - would the Cuprate contributors feel that this topic warrants a CCS proposal that is heavily-informed by your feedback, focuses more on an exploratory stage work with specific deliverables that can be built upon in the future, and the funding of which would be more "digestible" than
```
```
m-relay: <M​arkoPohlo> the full-fledged proposal?
```
```
m-relay: <M​arkoPohlo> We're more than happy to bring our lead engineers to chat with the community on this btw.
```
```
boog900: I do think I could support a 1-month reduced proposal
```
```
boog900: It would depend on the specifics of the CCS proposal though, the deliverables and cost.
```
```
boog900: SyntheticBird: what do you think 
```
```
boog900: and redsh4de if you want to give an opinion
```
```
syntheticbird: same as you. I think a reduction warrant a CCS proposal.
```
```
m-relay: <M​arkoPohlo> Would you rather we prioritize that proposal around getting a working differential harness on tx verification (even if narrow), or broader cargo-fuzz coverage over consensus rules without the monerod comparison? I want to make sure we're building what's most useful/high impact to the core contributors atm, not just what's easiest to scope for us.
```
```
redsh4de: Makes sense to me, it would definitely be a value add imo
```
```
boog900: I think the differential harness, building txs on a fake chain and giving them to monerod and cuprated would be best.
```
```
m-relay: <M​arkoPohlo> Thank you everyone for your feedback, we'll get our main fuzzing engineer's opinion as a reality check on doing that in 1 month and I'll stop by next meeting to share an update. Cheers!
```
```
boog900: nice, thank you!
```
```
syntheticbird: Thanks for coming by
```
```
boog900: I think I will end the meeting here
```
```
boog900: thanks everyone!
```
```
syntheticbird: thanks
```

# Action History
- Created by: moo900 | 2026-04-21T19:05:47+00:00
- Closed at: 2026-04-28T18:59:23+00:00
