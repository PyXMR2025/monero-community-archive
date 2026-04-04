---
title: 'Cuprate Meeting #49 - Tuesday, 2025-04-01, UTC 18:00'
source_url: https://github.com/monero-project/meta/issues/1176
author: moo900
assignees: []
labels: []
created_at: '2025-03-25T19:21:12+00:00'
updated_at: '2025-04-01T19:30:56+00:00'
type: issue
status: closed
closed_at: '2025-04-01T19:30:56+00:00'
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

Previous meeting: #1173

# Discussion History
## moo900 | 2025-04-01T19:30:55+00:00
## Meeting logs
```
boog900: 1) greetings
```
```
syntheticbird: `{ type: "greetings", content: "hello" }`
```
```
hinto: hello
```
```
boog900: 2) updates
```
```
boog900: Me: still working on the tx pool relay rules + making a tx pool manager task 
```
```
syntheticbird: Me: Starting my CCS work today
```
```
hinto: me: still working on a good model for the RPC testing harness
```
```
boog900: 3) Project: What is next for Cuprate?
```
```
hinto: `v0.0.2` release is set for next week, how is the 4-week schedule? would a longer gap be better?
```
```
syntheticbird: right now 4 weeks is good
```
```
syntheticbird: imo
```
```
boog900: I think it's fine we have some fixes that need to go out as well (already merged) 
```
```
hinto: boog900: do you think #418 will be ready by next monday?
```
```
boog900: yes
```
```
boog900: anything else anyone wants to discuss today?
```
```
syntheticbird: nope
```
```
hinto: to confirm, will you be available to review/merge by wednesday after 418? these are required https://github.com/Cuprate/cuprate/milestone/2, there are also a few `fix` PRs I think would be beneficial to merge but optional
```
```
boog900: yeah I will
```
```
hinto: ok, also I left a reply for 422, I'm not sure what a good solution would be there, any thoughts?
```
```
boog900: We already have code to spawn a monerod instance in a test, I also plan to make code that generates random blocks to simulate the blockchain. IMO it makes more sense as an integration test, over testing is better than under testing and the RPC relies on a lot of Cuprate services so probably be best to test it in CI.
```
```
boog900: As for developing you could just comment out the end points you haven't worked on yet  🤷
```
```
hinto: will the simulated blockchain be ready and reliable for both `monerod/cuprated` before 422 is done? this is a tool that I will need relatively soon to generate/assert correct RPC code from real chain data
```
```
boog900: I can prioritize it but probably not. For now I would just use a spawned monerod/cuprated with just the genesis block 
```
```
hinto: I don't think it is realistic to expect anyone to write code that generates matching output to `monerod` (long tail end of odd behavior included) without a testing tool like this
```
```
hinto: if it is just a small set of inputs/outputs + genesis block then I cannot assert `cuprated`'s RPC will match `monerod`'s
```
```
hinto: if it is a repo maintenance problem then I can create this for myself, although I would think the project will need to use it in the future
```
```
hinto: a slightly extreme option here could be to solve the core problem, the RPC API semantics, i.e. make a sane spec and enforce it, instead of copying the current one
```
```
hinto: which is what I would prefer but is probably too much
```
```
boog900: how are you planning to test something like `get_connections`?
```
```
boog900: are we asserting the output matches completely? 
```
```
boog900: i.e identical 
```
```
boog900: even something like `get_block_template` would be hard to check in this case 
```
```
hinto: https://github.com/Cuprate/cuprate/pull/422/files#diff-27e0a59fa526337a8bca072858afb5ec8d854c2c0f9605df2236242dae2e6430R2-R7
```
```
hinto: type + value correctness for most (if not all) fields for most endpoints, particular ones required by `wallet2`
```
```
hinto: there are endpoints where certain fields will need leniency
```
```
boog900: I think for most endpoints you will be able to just use data from the genesis block until the code to generate blocks is made 
```
```
boog900: any endpoints where you can see just having the genesis to be a problem?
```
```
hinto: any post genesis protocol change, or endpoints with multiple schemas post a certain block with a certain input
```
```
boog900: are you planning to test data from every hardfork?
```
```
hinto: do you think integration tests for all the "normal" endpoints + manual testing on the weird ones would be a better usage of time than creating this tester?
```
```
hinto: testing could be as wide as every single block or at key heights
```
```
boog900: We would only be able to create blocks for the current HF, if you wanted to test all we can't do that in CI
```
```
boog900: > <@hinto:monero.social> do you think integration tests for all the "normal" endpoints + manual testing on the weird ones would be a better usage of time than creating this tester?

I think we can hit all endpoints in CI, but if you wanted to est different HFs we can't do that
```
```
boog900: > <@hinto:monero.social> do you think integration tests for all the "normal" endpoints + manual testing on the weird ones would be a better usage of time than creating this tester?

 * I think we can hit all endpoints in CI, but if you wanted to test different HFs we can't do that
```
```
boog900: cuprated is already going to need some changes to enable a regtest mode
```
```
hinto: I will restate attributes I think this tester should have:
- assert input/output of `monerod/cuprated` endpoints (mostly) match in field type and value
- covers a wide set of inputs (all) or at least key ones with known change (e.g. certain heights)
- reusable
```
```
hinto: for example, having a test that asserts `get_block` with all heights from `monerod/cuprated` match in type/value would be assuring
```
```
boog900: ok how about setting up a top level `tests` directory?
```
```
boog900: or `test` if cargo gets angry at that being reserved 
```
```
hinto: that would be fine but it needs access to the full chain
```
```
boog900: I would still like to be able to call it in CI _somehow_, it would be good to make it generic in that sense 
```
```
hinto: > I guess the second could be solved with something like ./cuprate-rpc-compat --monerod-ip $x --cuprated-ip $y, although CI passing now relies on those nodes and cargo test will fail without them, thoughts?
```
```
syntheticbird: im back (i was away), 
- If we can draft up a spec and enforce it then let's do it.
- regarding testing harness testing of all endpoints at all height, imo this is something worth to do outside of CI, just before any release.
```
```
syntheticbird: just proposing yk, if RPC silently break or we create a regression/corner case, i think it's not important on master branch since it will not be recommended for production. We add the RPC harness test as a requirement for release.
```
```
boog900: I think a Rust binary that call all tests in `test`(`s`) and does the required setup would be better than directly calling it, but yeah I agree with the idea.
```
```
syntheticbird: * just proposing yk, if RPC silently break or we create a regression/corner case, i think it's not important on master branch since it will not be recommended for production. We can add the RPC harness test as a requirement for release.
```
```
boog900: > <@syntheticbird:monero.social> just proposing yk, if RPC silently break or we create a regression/corner case, i think it's not important on master branch since it will not be recommended for production. We can add the RPC harness test as a requirement for release.

making more requirements for humans instead of automating it is not ideal IMO
```
```
boog900: especially as this is not too hard to automate 
```
```
syntheticbird: It's just a tradeoff, it's effectively a little annoying for release but it spares us hours wasted in CI on github + verify all possible height
```
```
syntheticbird: unless you meant we can reasonably do all height in CI
```
```
boog900: nah the CI would use a generate chain with just the most recent HF rules 
```
```
boog900:  * nah the CI would use a generated chain with just the most recent HF rules 
```
```
boog900: enough to check all currently valid behavior 
```
```
boog900: anything else to add or we can end here
```
```
syntheticbird: It that is deemed enough, then yeah it make sense.
```
```
syntheticbird: * If that is deemed enough, then yeah it make sense.
```
```
boog900: its enough for CI we don't need to scan the chain all the time IMO
```
```
syntheticbird: i just think overtesting all the real chain data is better, but if the goal was to validate HF/scheme rules then it's enough to put that as a `#[test]`.
```
```
syntheticbird: I think we can end here
```
```
syntheticbird: it's already 20 minutes over the hour, might be worth continuing the discussion off-meeting
```
```
boog900: We can add hardcodded test cases for block data to validated we encode all txs in JSON correctly 
```
```
boog900: I think we already have some as well
```
```
boog900: that should be enough
```
```
hinto: I am noting again that if I don't have access to a tool like this I cannot make assertions on `cuprated` matching `monerod` perfectly
```
```
boog900: I am only talking about CI not for you building FWIW 
```
```
hinto: ok, is 422 separate from CI tests then? do you still want `cuprate-rpc-compat` in the repo?
```
```
syntheticbird: im confused, boog were you talking about hinto's rpc harness test ?
```
```
boog900: I would like to use `cuprate-rpc-compat` in the CI tests 
```
```
syntheticbird: ah alright
```
```
boog900: with nodes on a fake chain generated in CI
```
```
hinto: what about `./cuprate-rpc-compat --ci-light-mode` where only a small subset of inputs are tested?
```
```
boog900: Why can't we test everything?
```
```
syntheticbird: I would like `cuprate-rpc-compat` to support testing the whole chain fwiw
```
```
hinto: I am confused
```
```
syntheticbird: same
```
```
boog900: we are confused 
```
```
syntheticbird: ***our*** confusion
```
```
syntheticbird: CI time
```
```
syntheticbird: testing everything = testing all the height of real chain ?
```
```
syntheticbird: * testing everything = testing all the heights of real chain ?
```
```
boog900: no, it should be generic to handle any chain
```
```
boog900: ask the node for it's height, then scan every block up to the height it told you 
```
```
boog900:  * ask the node for its height, then scan every block up to the height it told you 
```
```
syntheticbird: yeah im fine with this, one can decide to use `cuprate-rpc-compat` to test the real chain if needed, or a fake one for CI
```
```
boog900: for `cuprate-rpc-compat` it doesn't need to do anything apart from not hardcode itself for main chain 
```
```
boog900: all it needs to do is take in a cuprate RPC address & a monerod RPC address 
```
```
boog900: and assume that they are both on the same chain 
```
```
boog900: but maybe not the main chain 
```
```
hinto: ok, I will write some signatures later so we can be more clear on what this thing should be doing
```
```
syntheticbird: so to answer hinto, yes we want `cuprate-rpc-compat` in the repo, ideally chain agnostic. this would invalidate your `--ci-light-mode` idea
```
```
syntheticbird: sgtm
```
```
boog900: ok we can end here 
```
```
boog900: Thanks everyone!
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
- Created by: moo900 | 2025-03-25T19:21:12+00:00
- Closed at: 2025-04-01T19:30:56+00:00
