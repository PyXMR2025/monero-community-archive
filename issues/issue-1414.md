---
title: 'Cuprate Meeting #110 - Tuesday, 2026-07-07, UTC 18:00'
source_url: https://github.com/monero-project/meta/issues/1414
author: moo900
assignees: []
labels: []
created_at: '2026-06-30T18:14:59+00:00'
updated_at: '2026-07-07T18:20:32+00:00'
type: issue
status: closed
closed_at: '2026-07-07T18:20:32+00:00'
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

Previous meeting: #1409

# Discussion History
## moo900 | 2026-07-07T18:20:31+00:00
## Meeting logs
```
boog900: 1) greetings
```
```
syntheticbird: Hi
```
```
boog900: 2) updates
```
```
boog900: Me: made the final PR for basic wallet support, once that is merged we just need to do testing 
```
```
boog900: I already know of a few issues I need to fix around limits 
```
```
redsh4de: Hi
```
```
redsh4de: spent a few hrs reviewing the latest PR
```
```
syntheticbird: me: nothing. Following my old message, ETA of 2 weeks before being able to start contributing in "appropriate" conditions. My CCS is still in funding, I'll start with the edits I said on LLM contributions and review.
```
```
boog900: 2) Project: What is next for Cuprate?


```
```
boog900: 3*
```
```
boog900: I think I will try to create a monero-gui binary that uses cuprate instead of monerod 
```
```
syntheticbird: Seems like a shy summer contribution-wise on monero core side
```
```
syntheticbird: thats nice
```
```
syntheticbird: just a PoC or upstream ?
```
```
syntheticbird: or for upstream eventually*
```
```
boog900: No just to allow people to test out cuprate in an easier way 
```
```
boog900: We could make the changes upstream so that it could just be replacing a binary in the GUI build process
```
```
boog900: But I don't plan to do that 
```
```
syntheticbird: I think to enhance our debugging capabilities during test its extremely important that we integrate Firebase and Sentry into this binary and get all the data on a public and unauthenticated database
```
```
syntheticbird: yeah thats sounds like nightmare ngl
```
```
syntheticbird: kind of an ethical issue in providing in core a binary built from another organization
```
```
syntheticbird: imo
```
```
boog900: The GUI is going to require some code changes as it uses some monerod features we don't have fwiw 
```
```
syntheticbird: do you have examples ?
```
```
boog900: > <@boog900:monero.social> Me: made the final PR for basic wallet support, once that is merged we just need to do testing 

Just realized I didn't push the clippy fix will do now
```
```
boog900: > <@syntheticbird:monero.social> do you have examples ?

Using the monerod binary to make ROC requests to a running node

```
```
boog900: RPC*
```
```
syntheticbird: wat
```
```
syntheticbird: why
```
```
syntheticbird: bootstrap node ?
```
```
boog900: No like just to make rpc requests 
```
```
boog900: Anything else to discuss today?
```
```
syntheticbird: nope
```
```
redsh4de: nop
```
```
boog900: Thanks everyone, we can end here 
```
```
boog900: !meeting 
```

# Action History
- Created by: moo900 | 2026-06-30T18:14:59+00:00
- Closed at: 2026-07-07T18:20:32+00:00
