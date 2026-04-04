---
title: 'Cuprate Meeting #20 - Tuesday, 2024-09-10, UTC 18:00'
source_url: https://github.com/monero-project/meta/issues/1067
author: moo900
assignees: []
labels: []
created_at: '2024-09-03T19:00:15+00:00'
updated_at: '2024-09-10T19:08:19+00:00'
type: issue
status: closed
closed_at: '2024-09-10T19:08:18+00:00'
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

Previous meeting with logs: #1064

# Discussion History
## moo900 | 2024-09-10T19:08:17+00:00
## Meeting logs
```
boog900: meeting time: https://github.com/monero-project/meta/issues/1067
```
```
boog900: 1) greetings 
```
```
asurar0: Hello
```
```
asurar0: This meeting is free to join by anyone right?
```
```
boog900: yes 
```
```
hinto: hello
```
```
boog900: 2) Updates 
```
```
boog900: Me: I finished the PR adding alt blocks to the DB and have started work on the P2P request handler 
```
```
hinto: me: started working on JSON-RPC handler functions, ported DB docs to https://architecture.cuprate.org
```
```
boog900: 3) Project: What is next for Cuprate?
```
```
hinto: boog900: I don't have anything ready yet but I'm expecting there's going to have to be lots of added request/responses to the DB for RPC, as it is now there's a big lack of data we can actually get
```
```
boog900: Ok yeah I would just be careful as we already have quite a few requests 
```
```
boog900: I'm also going to need to add some for the P2P 
```
```
hinto: RPC also needs access to something like `VerifiedBlockInformation` or something like it, are these request/responses possible: https://github.com/Cuprate/cuprate/pull/272/files#diff-cfc9e4f43383488d656688d434acc5d7dff41165836b838b041d12352c323102R147-R151 ?
```
```
boog900: no, we can't pull `VerifiedBlockInformation` from the DB
```
```
hinto: hmm, ok here's an example of what fields the RPC needs: https://github.com/Cuprate/cuprate/pull/272/files#diff-70eaf57769312968854d8c29d63aa6efea2317b801da97b89048b9b665da6d0f
```
```
hinto: RPC also needs access to P2P state: https://github.com/monero-project/monero/blob/cc73fe71162d564ffda8e549b79a350bca53c454/src/rpc/core_rpc_server.cpp#L2733
```
```
boog900: > <@hinto:monero.social> hmm, ok here's an example of what fields the RPC needs: https://github.com/Cuprate/cuprate/pull/272/files#diff-70eaf57769312968854d8c29d63aa6efea2317b801da97b89048b9b665da6d0f

you should be able to fill most of that in with the `Block` + `BlockExtendedHeader`
```
```
boog900: `pow_hash` would need to be calculated on the fly although IIRC it's not always returned?
```
```
boog900: `reward` would need the previous block's `BlockExtendedHeader`, unless we were to add that field to `BlockExtendedHeader` and have the DB calculate it 
```
```
boog900: same with difficulty 
```
```
boog900: > <@hinto:monero.social> RPC also needs access to P2P state: https://github.com/monero-project/monero/blob/cc73fe71162d564ffda8e549b79a350bca53c454/src/rpc/core_rpc_server.cpp#L2733

this would need to be a TODO
```
```
0xfffc: Hi everyone. My Apologies for being late for the meeting. 
```
```
hinto: I have a feeling I'm overlooking something really obvious but why isn't `pow_hash` stored by the DB for each block?
```
```
boog900: it isn't calculated during fast sync 
```
```
boog900: which is how the vast majority of people sync 
```
```
boog900: we set the field to `[0; 32]` but I have a TODO to change it to an Option 
```
```
hinto: this is ultimately my fault but I would have appreciated a warning that there's lots of unfinished work before handlers can be finished :)
```
```
hinto: it doesn't seem like my milestones can be finished within 3 months
```
```
boog900: I think you will be able to finish it in 3 months
```
```
boog900: I would break it up smaller than you are going now though 
```
```
boog900: Some of the handlers need to use components I am building now 
```
```
boog900: I would recommend doing the easy handlers first like `get_block_count` etc
```
```
hinto: ok, will work the same regardless
```
```
hinto: > <@boog900:monero.social> I would recommend doing the easy handlers first like `get_block_count` etc

already doing this since lots of handlers can't be immediately implemented
```
```
boog900: ah alright I was just going of the PR title 
```
```
hinto: there's also the discussion of RPC calls that will behave slightly differently or won't/can't be supported by `cuprated`
```
```
hinto: I'll create a proposal for next meeting
```
```
asurar0: > <@hinto:monero.social> there's also the discussion of RPC calls that will behave slightly differently or won't/can't be supported by `cuprated`

I apologize for my lack of knowledge, but are you referring to https://github.com/monero-project/monero/issues/9422
```
```
hinto: in that case, I think `cuprated` will implement the new behavior (TBD) and I'll follow up with a `monerod` PR eventually
```
```
boog900: 4) Any other business
```
```
hinto: I'm mostly talking about things like `/update` which is `monerod` specific
```
```
dimalinux: I suspect Cuprate already has enough cooks in the kitchen, but if there are any well defined tasks that need extra help on, let me know. Or if there is feedback on the Cryptonight PR that I didn't address, let me know.
```
```
hinto: I will re-review it but I think actually reviewing the impl would take a while
```
```
boog900: sure, I don't have any good issues to point to at the moment but will keep that in mind, unless hinto has one. I'll also review that PR soon  
```
```
hinto: also there's definitely not enough cooks in the kitchen, at least ones that do large amounts of sustained work 
```
```
hinto: you could takeover https://github.com/Cuprate/cuprate/issues/199, which yamabiiko was planning to do before vanishing from the world
```
```
asurar0: I'm happy to help with your project and assist wherever needed. I've already taken on an issue and would be willing to contribute further in the future.
```
```
boog900: ok I think we can end here 
```
```
boog900: thanks everyone!
```
```
boog900: !meeting 
```

# Action History
- Created by: moo900 | 2024-09-03T19:00:15+00:00
- Closed at: 2024-09-10T19:08:18+00:00
