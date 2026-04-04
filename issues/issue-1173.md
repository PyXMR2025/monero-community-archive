---
title: 'Cuprate Meeting #48 - Tuesday, 2025-03-25, UTC 18:00'
source_url: https://github.com/monero-project/meta/issues/1173
author: moo900
assignees: []
labels: []
created_at: '2025-03-18T19:09:04+00:00'
updated_at: '2025-03-25T19:21:12+00:00'
type: issue
status: closed
closed_at: '2025-03-25T19:21:12+00:00'
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
- [Open questions for RPC integration](https://github.com/monero-project/meta/issues/1173#issuecomment-2743428608)

- Any other business

Previous meeting: #1170

# Discussion History
## hinto-janai | 2025-03-21T13:51:25+00:00
### Questions
Some open questions for [RPC integration](https://github.com/Cuprate/cuprate/issues/379).

Q = question
P = problem
B = benefit
M = answer (maybe)
A = answer

**Q.** Considering the path to mainnet FCMP++ is getting closer, is it worth implementing/testing behavior for endpoints that will change?
**P.** If no, `cuprated` will effectively have an incomplete RPC until post-FCMP++, if yes, time will be spent "inefficiently" implementing things that will have to be changed anyway
**B.** Time spent implementing/testing/fixing changed endpoints can be spent more efficiently moving the project forward in [different areas](https://github.com/Cuprate/cuprate/issues/376) e.g. reproducible builds
**A.**

**Q.** Long-term, would it be worth (and supported) to create/maintain a core RPC specification for Monero similar to https://ethereum.org/en/developers/docs/apis/json-rpc?
**P.** This is a large maintenance burden; changes are too large; all following diffs must be enforced to abide by the spec (whether by maintainers or some automation); this level of commitment may be too restrictive for Monero (counter-argument: if solid APIs are never created, people are less willing to build on-top because changing and ill-documented APIs are harder to support); `wallet-rpc` API also exists; there are no maintainers that are willing/incentivized to do this.
**B.** The API can be updated to be more concise/simple; APIs could be categorized into importance/stability, i.e. core/extra, these specs could act as a guide for further changes 
**M.** Cuprate could create/maintain its own core spec (endpoints required by `wallet2`) and could branch from there to create its own APIs https://github.com/Cuprate/cuprate/issues/388 (with all the tradeoffs that that comes with)
**A.**

### Priority ordering for endpoints
The expected priority order for RPC endpoint implementation/testing assuming the answer to the first question is `no`.

1. Required for `wallet2` operation
	- 1a. No expected changes from FCMP++
	- 1b. Signatures for post FCMP++ (inner = `todo!()`)
2. Non-required but frequently used calls
3. All others
4. Fix remaining signatures post-FCMP++

## moo900 | 2025-03-25T19:21:11+00:00
## Meeting logs
```
boog900: meeting time
```
```
boog900: 1) greetings 
```
```
hinto: hello
```
```
syntheticbird: Hello
```
```
boog900: 2) Updates 
```
```
syntheticbird: Me: My CCS got fully funded. Thx to all contributors
```
```
boog900: Me: I worked on tx relay rules + making the config file docs auto generated 
```
```
syntheticbird: * Me: My CCS got fully funded. Thx to all contributors. Will be working on my items starting 1st march
```
```
syntheticbird: * Me: My CCS got fully funded. Thx to all contributors. Will be working on my items starting 1st april
```
```
hinto: me: opened some misc issues/PRs, seems like I will be continuing on RPC stuff soon
```
```
boog900: 3) Project: What is next for Cuprate?

```
```
boog900: - [Open questions for RPC integration](https://github.com/monero-project/meta/issues/1173#issuecomment-2743428608
```
```
boog900:  * - [Open questions for RPC integration](https://github.com/monero-project/meta/issues/1173#issuecomment-2743428608)
```
```
hinto: err actually I was going to ask about #413
```
```
boog900: we can start there if you want
```
```
boog900: IMO with 418 this isn't needed anymore 
```
```
boog900: well the config file at least 
```
```
spirobel: https://github.com/Cuprate/cuprate/pull/418
```
```
spirobel: https://github.com/Cuprate/cuprate/pull/413
```
```
hinto: did you see the comment I left?
```
```
hinto: having a linkable static default config file is desirable, the user-book also uses it currently
```
```
boog900: I did, I think for testing we would probably want to include every possible value so these files aren't suitable and then the user book should generate the config when it is built somehow. 
```
```
boog900: I don't think we need a static config file in the repo 
```
```
hinto: I think the user-book can do something like `./cuprated --generate-config-file > file` and include that
```
```
hinto: how will we test backwards compatibility?
```
```
hinto: not as important now although `v1.0.0` config not working with `v1.0.1` would be embarrassing, this could maybe be figured out later I guess
```
```
boog900: At some point we will need to have config files as test cases but they wont be exposed to users as they should have every option specified 
```
```
boog900: and yeah I don't really want to guarantee backwards compatibility yet 
```
```
hinto: ok, in that case you can remove the relevant files/tests in #418 
```
```
spirobel: i guess in case the name of a config option changes it will just be ignored 
```
```
hinto: #413 is still need for the changelog, any ideas on enforcing the updates? seems like I'll be doing it manually every release
```
```
boog900: > <@spirobel:kernal.eu> i guess in case the name of a config option changes it will just be ignored

we can have serde accept multiple names but only produce one 
```
```
boog900: after 1.0 that's probably what we will do if we ever decide to rename a field 
```
```
boog900: the hard one will be removing an option, we would probably have a transition period where the option is completely hidden but still accepted with a warning printed if it is set.
```
```
boog900: > <@hinto:monero.social> #413 is still need for the changelog, any ideas on enforcing the updates? seems like I'll be doing it manually every release

I think the monero-rs way is good - require every PR to update the changelog 
```
```
boog900: So the default is to update the changelog every PR. If the PR is small/CI related etc, the change log doesn't need to be updated.
```
```
hinto: as merger I think you are responsible for enforcing this on each PR
```
```
hinto: thoughts on a single PR before release collecting all changes at once? saves mental energy when deciding which ones to include / wording  
```
```
boog900: I think it depends on what changelog we decide on, one per crate, just `cuprated` etc. Currently the only changelog is for `cuprated`, right?
```
```
boog900: If we are separating the changelog per crate (even in a single file) then updating on every PR would be best, if we are just doing `cuprated` then a single changelog PR would be best IMO
```
```
hinto: taking time to lay out standards + automating everything would be my approach
```
```
spirobel: regarding the rpc: getblocks.bin seems like a good candidate to start. that will have the most impact. getinfo json could be an easy one to break the ice 
```
```
boog900: > <@hinto:monero.social> taking time to lay out standards + automating everything would be my approach

Yeah, I still don't know what type of changelog I would prefer  
```
```
boog900: > <@spirobel:kernal.eu> regarding the rpc: getblocks.bin seems like a good candidate to start. that will have the most impact. getinfo json could be an easy one to break the ice

we should start with whatever wallet2 uses, not just getblocks.bin IMO
```
```
syntheticbird: I personally prefer a global changelog
```
```
boog900: > Q. Considering the path to mainnet FCMP++ is getting closer, is it worth implementing/testing behavior for endpoints that will change?

hinto AFAIK no endpoints are going to completely change right? 
```
```
boog900: some endpoints may have fields added etc but none completely changed where work would be wasted? 
```
```
syntheticbird: > Q. Long-term, would it be worth (and supported) to create/maintain a core RPC specification for Monero similar to https://ethereum.org/en/developers/docs/apis/json-rpc?

Regarding node RPC specification: https://github.com/SyntheticBird45/monero-open-rpc/blob/main/daemon/openrpc.json 
```
```
syntheticbird: it only include /json_rpc endpoints but could be a start. maybe.
```
```
boog900: I don't really want to maintain RPC docs when getmonero has docs 
```
```
spirobel: maybe something could be generated from the epee macros
```
```
hinto: it depends on the extent of changes made to RPC
```
```
syntheticbird: this was vtnerd original plan
```
```
spirobel: sounds like a good plan
```
```
boog900: I also don't really want to create a new RPC API - IMO that would be a pretty big undertaking.
```
```
hinto: at the very least I think most of the endpoints can be implemented without fear, regardless the testing harness must be created so I can start right now
```
```
syntheticbird: Only if collaborating with Monero on this
```
```
syntheticbird: I would care only*
```
```
boog900: just added 3 years to the timeline with that one sentence 
```
```
syntheticbird: yeah lmao
```
```
spirobel: if getblocks.bin with maxblocks works
```
```
spirobel: 97% done
```
```
syntheticbird: I'm personally not against a new RPC API, and would gladly take the work, but i'm not knowledgeable on the issues people are encountering
```
```
spirobel: some stuff is crazy like banning rpc clients on 500 errors ( which happen when fetching the latest height for getblocks.bin)
```
```
syntheticbird: that is unrelated to the API endpoints
```
```
spirobel: we should propably submit a patch to monerod to remove this behavior 
```
```
hinto: re: standardized/enforced RPC API - the reason I bring it up is because realistically only Cuprate can push for it, I don't expect an opportunity in the future where something like this can be created upstream
```
```
syntheticbird: agree
```
```
spirobel: it is related in so far as it is rpc behavior that shouldnt be carried over. 
```
```
syntheticbird: I mean, making a new RPC API wouldn't change this. What you are describing is RPC server behavior
```
```
spirobel: even returning a 500 error for fetch to the recent block height is weird 
```
```
spirobel: no idea if its good to standardize / enforce this 
```
```
spirobel: because its ugly
```
```
boog900: tbf you are out of range :) chain height vs top height has got me a lot too
```
```
boog900: it was the cause of some of the reorg issues 
```
```
spirobel: the thing is it shouldnt matter. even a too high of a blockheight  shouldnt lead to 500 which indicates an internal server error / malfunctioning node not even speaking of blocking the client after 3 of those 
```
```
spirobel: that would also mean we dont have to check what the current daemon height is before just fetching on a new wallet creation / fresh fetch 
```
```
boog900: For me I wouldn't mind banning behavior that conforming wallets would never do, requesting blocks out of range is invalid. Although the error should be returned so it can be fixed.
```
```
boog900: I would rather be too strict than too lenient   
```
```
spirobel: it makes the whole thing more brittle / is foot gun that makes wallet development harder than it needs to be
```
```
boog900: I would argue allowing partially valid data is a foot gun 
```
```
spirobel: if the fetched height is too high, just return the latest block or no block 
```
```
boog900: we would only be helping people to build broken wallets 
```
```
spirobel: https://github.com/j-berman/monero/blob/b6a029f222abada36c7bc6c65899a4ac969d7dee/src/rpc/core_rpc_server.cpp#L633
```
```
spirobel: no the current behavior is weird. it mixes p2p banning with the local rpc
```
```
spirobel: i think we talked about this before and said  that banning behavior will not be replicated
```
```
syntheticbird: i propose we end the meeting there and people are free to continue talking about rpc ban behavior ?
```
```
spirobel: :D
```
```
spirobel: i need to sleep its 3 am here
```
```
spirobel: but this topic is dear to my heart
```
```
spirobel: you can also take a look at the git blame and how / why this was introduced in the first place 
```
```
boog900: monerod's behavior wont be replicated exactly, and exact decisions on what constitutes a ban is yet to be made. I will say we only officially support "correct" usage, mixing data is very not valid so I wouldn't bet on it not returning an error and possibly a ban.
```
```
boog900: I am happy to support special casing any height above to always return the top block although I would want monerod to have that behavior too 
```
```
boog900: Thanks everyone!
```
```
boog900: (we can end here)
```
```
hinto: thanks
```

# Action History
- Created by: moo900 | 2025-03-18T19:09:04+00:00
- Closed at: 2025-03-25T19:21:12+00:00
