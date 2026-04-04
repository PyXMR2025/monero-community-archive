---
title: 'Cuprate Meeting #54 - Tuesday, 2025-05-06, UTC 18:00'
source_url: https://github.com/monero-project/meta/issues/1196
author: moo900
assignees: []
labels: []
created_at: '2025-04-29T19:08:37+00:00'
updated_at: '2025-05-06T18:48:33+00:00'
type: issue
status: closed
closed_at: '2025-05-06T18:48:33+00:00'
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

Previous meeting: #1191

# Discussion History
## moo900 | 2025-05-06T18:48:32+00:00
## Meeting logs
```
boog900: 1) greetings 
```
```
sgp_: Hello
```
```
syntheticbird: Hello
```
```
boog900: 2) updates 
```
```
boog900: Me: finished the recovery from bad reorgs PR 
```
```
boog900: also worked on the tx-pool manager 
```
```
hinto: hello
```
```
hinto: me: preparing `cuprated v0.0.3`
```
```
syntheticbird: Working on send timeout type and Tor Zone definition + cuprated changes for tx relay
```
```
boog900: 3) Project: What is next for Cuprate?
```
```
boog900: anything anyone wants to discuss today?
```
```
hinto: This issue seems to be happening still: https://github.com/Cuprate/cuprate/issues/435#issuecomment-2855497548
```
```
hinto: does 449 fix this? I have it running and it doesn't seem to panic
```
```
boog900: 438 wasn't in `v0.0.2`
```
```
boog900: 438 fixes it 
```
```
hinto: ah, right I forgot about that
```
```
boog900: there is no caller now that does not check that the blocks given are empty 
```
```
boog900: should maybe add a label for when it was fixed 
```
```
boog900: like what release 
```
```
boog900: I don't know how easy that will be to automate 
```
```
hinto: speaking of, `v0.0.3` release is tomorrow, are we ready to tag soon?
```
```
boog900: I think we have anything we need, 455 could be included if ready in time but it's not needed IMO
```
```
hinto: ok, just waiting on 437 then
```
```
boog900: sure, will review after the meeting 
```
```
hinto: this doesn't need to be discussed now although there is a problem with a decision made in RPC a while back that I haven't brought up yet
```
```
hinto: https://github.com/Cuprate/cuprate/blob/d7e6eb785b879a7c67bdb8e02b757be843a2c11a/rpc/json-rpc/README.md?plain=1#L46 this tagging method makes it a difficult to accept partial JSON when deserializing the request
```
```
hinto: Even for methods that have no input, the `params` field is still expected, e.g. this will not be accepted:

json
{"jsonrpc":"2.0","id":"0","method":"sync_info"}


It must be:

json
{"jsonrpc":"2.0","id":"0","method":"sync_info","params":{}}


```
```
hinto: we can merge 423 and probably enable some endpoints although a solution needs to be found before JSON-RPC methods are enabled
```
```
hinto: I will try to find one without resorting to the 2-step deserialization discussed last time
```
```
boog900: hmm that is annoying 
```
```
hinto: I could also run perf tests to see if 2-step deserialization matters in the big picture?
```
```
boog900: sure although IIRC you did some before 
```
```
hinto: from what I remember last time the `async fn json_rpc` handler itself got much slower although I am unsure if it mattered in a larger throughput test
```
```
boog900: Yeah I don't think it will be a lot compared to the time to complete the request 
```
```
boog900: like to fetch the data etc 
```
```
boog900: anything else anyone wants to discuss today?
```
```
syntheticbird: nope
```
```
boog900: ok we can end here 
```
```
boog900: thanks everyone!
```
```
syntheticbird: thanks
```
```
hinto: thanks
```
```
boog900: !meeting 
```

# Action History
- Created by: moo900 | 2025-04-29T19:08:37+00:00
- Closed at: 2025-05-06T18:48:33+00:00
