---
title: 'Cuprate Meeting #102 - Tuesday, 2026-05-12, UTC 18:00'
source_url: https://github.com/monero-project/meta/issues/1383
author: moo900
assignees: []
labels: []
created_at: '2026-05-05T19:13:21+00:00'
updated_at: '2026-05-12T19:12:26+00:00'
type: issue
status: closed
closed_at: '2026-05-12T19:12:26+00:00'
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

Previous meeting: #1379

# Discussion History
## MarkoPohlo | 2026-05-12T15:36:26+00:00
Guy, our formal methods engineer, would love to update the community with a polished proposal we've been discussing for the past few weeks.

## moo900 | 2026-05-12T19:12:25+00:00
## Meeting logs
```
boog900: 1) greetings
```
```
redsh4de: hi!
```
```
boog900: Sorry for the late start 
```
```
syntheticbird: Hi
```
```
boog900: 2) updates 
```
```
syntheticbird: me: nothing
```
```
redsh4de: me: simplified the KI passing logic a bit, here is the very simplified flow of whats currently PRed
```
```
redsh4de: <image.png>
```
```
boog900: I have made 2 more PRs for the RPC changes, also began working on fcmp tree building. I am working on updating the consensus book as I go.
```
```
redsh4de: also squashed commits for the embeddable library PR into 5 so things are easier to reason about
```
```
boog900: 3) Project: What is next for Cuprate?
```
```
boog900: guy.repta do you have an update  on the fuzzing proposal? 
```
```
gtrepta_rv: Yeah, here it is https://gist.github.com/palinatolmach/04bb23b383c2c499a678997af2adc8b0
```
```
gtrepta_rv: A couple of points. We can probably work with a static Database that's similar to the mocked one that you have in consensus testing. I also don't think we need to fork monero-oxide to fuzz over the transactions, we can fuzz that data independently and then build the structures with it.
```
```
boog900: I think from is technical perspective it looks good, the only thing I want to bring up on that is:

> Initial invalid-transaction generation via patches to monero-oxide

That contradicts what you just said here, was that supposed to be removed? 

```
```
boog900: We will need custom signing functions I would think and I don't think monero-oxide should make making invalid txs easier.

```
```
gtrepta_rv: Yeah, we can clear up some of the details in the document
```
```
gtrepta_rv: Can you tell me more about the challenges for creating invalid txs? Is it hard to keep them well formed, or cover all the possible cases, or...?
```
```
boog900: monero-oxide's API will prevent you from break some rules and its signing functions will never break rules like creating signatures with torsioned KIs
```
```
gtrepta_rv: Hmm. Maybe we could try fuzzing valid transactions, and have a mutation step over the valid binary array that represents the tx? A lot of mutations might not get past the parser but some could make it deeper.
```
```
boog900: that would change the signature hash, so the signature will be invalid.
```
```
gtrepta_rv: I see
```
```
gtrepta_rv: So the signature functions seem to be what's in the way. I'm not familiar enough yet with the api.. If we create our own signatures for invalid transactions can we still build the monero-oxide transactions with all of that information? Does creating a custom signature function for this sound like a lot of work?
```
```
boog900: you may have to turn it to bytes and then read with the monero oxide types, and yes it will probably be a lot of work ngl 
```
```
boog900: I do want to repeat here what I said last meeting too:
```
```
boog900: 
Being completely honest I think this task is too big to do in a short enough time to be
appetising for the community and core who approve CCS proposals.

I don't see them wanting to fund fuzzing work for us, when we are still in alpha and have no users. 


I think the proposal is technically ok, next step would be to post it on the CCS site to get the wider communities view 

```
```
gtrepta_rv: Yes, I was going to bring that up as well. But, if it can be posted regardless and we can see what the response is then it sounds good to me. But, I would like to make sure that we have it properly scoped given the timeline.
```
```
boog900: I think the proposal is there roughly, and it will take a little while to go through anyway
```
```
boog900: the CCS itself is going to be the biggest hurdel for you guys I think 
```
```
boog900: so better to get it started soon so we don't spend too long making it perfect for it to maybe not happen. 
```
```
gtrepta_rv: Ok. Well right now I think the differential harness with valid txs is going to be where we land.
```
```
boog900: yeah, I think that is all that is possible in a month
```
```
gtrepta_rv: I'll get back to our BD people on it, they know more about the proposal process than I do
```
```
boog900: alright sounds good
```
```
boog900: we can end the meeting here 
```
```
boog900: thanks everyone
```
```
gtrepta_rv: thanks
```
```
boog900: !meeting 
```

# Action History
- Created by: moo900 | 2026-05-05T19:13:21+00:00
- Closed at: 2026-05-12T19:12:26+00:00
