---
title: 'Cuprate Meeting #61 - Tuesday, 2025-06-24, UTC 18:00'
source_url: https://github.com/monero-project/meta/issues/1222
author: moo900
assignees: []
labels: []
created_at: '2025-06-17T18:51:49+00:00'
updated_at: '2025-06-24T19:33:42+00:00'
type: issue
status: closed
closed_at: '2025-06-24T19:33:42+00:00'
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

Previous meeting: #1219

# Discussion History
## moo900 | 2025-06-24T19:33:41+00:00
## Meeting logs
```
boog900: 1) greetings 
```
```
syntheticbird: Hello
```
```
fluorescent_beige: Hello
```
```
sgp_: Hello
```
```
hinto: hi
```
```
boog900: 2) updates 
```
```
syntheticbird: Nothing.
```
```
syntheticbird: review for the Tor pr awaits fixes. Will provide them this evening or tomorrow
```
```
boog900: me: did a bit of work on the address book, should be ready to PR it soon 
```
```
fluorescent_beige: Finishing db hotswap (PR #510)
```
```
hinto: me: also not much, left a small review on 483 and opened 499
```
```
boog900: 3) Project: What is next for Cuprate?
```
```
boog900: bit of a slow week then. Everyone watching monerokon :) 
```
```
boog900: anything to discuss? 
```
```
hinto: boog900: there's a backlog of PRs that you have not commented on, these are stuck if you are the sole merger
```
```
hinto: these need a review or a straight "no" or else they end up compounding in merge conflicts
```
```
boog900: Fair I'll review them, none of them are big PRs, I try stay on top of those. 

I count 3, the rest are waiting on other people 
```
```
boog900: one of them was made by they guy I think is using AI so I didn't want to merge it 
```
```
boog900: * one of them was made by the guy I think is using AI so I didn't want to merge it 
```
```
hinto: there are also issues and bigger questions for the project that are piling up
```
```
boog900: I didn't know there was any issues that needed my immediate interaction  
```
```
hinto: they are mostly medium/long-term decisions that have not been discussed or made yet
```
```
boog900: A lot of stuff has been put to the side as not important for now, like the motto 
```
```
syntheticbird: Feel free to enumerate points you have in mind.
```
```
hinto: - https://github.com/Cuprate/cuprate/issues/467
- https://github.com/Cuprate/cuprate/issues/468
- https://github.com/Cuprate/cuprate/issues/473
```
```
boog900: we discussed all those in a meeting IIRC
```
```
syntheticbird: I don't remember
```
```
boog900: 467 is a tracking issue too 
```
```
hinto: the conditions of a beta release are not clear yet
```
```
boog900: https://github.com/monero-project/meta/issues/1199
```
```
boog900: we discussed that here 
```
```
boog900: > boog900: IMO beta should happen once we hit parity with monerod 
```
```
boog900: > boog900: fair, we could not do ZMQ before beta if that's preferred  
```
```
boog900: so TL/DR once RPC is done
```
```
syntheticbird: boog, stop having a good memory
```
```
syntheticbird: it's detrimental to the project
```
```
syntheticbird: i mean, thx for having a good memory
```
```
syntheticbird: it's very helpful for the project
```
```
hinto: there are safety questions that I cannot take responsibility for
```
```
syntheticbird: safety questions?
```
```
boog900: beta is still not going to be recommended for people to use for anything serious 
```
```
hinto: is the answer to 468: "`cuprated` beta is OK to release without a killswitch and further review"?
```
```
syntheticbird: already provided my answer on the issue
```
```
syntheticbird: > So IMO, the killswitch can be removed at stable or during beta. Probably not at the start of beta, as RPC will bring a lot more users for testing and we would get more chance to catch consensus bugs in this period.
```
```
hinto: I'd also say deciding parameters for https://github.com/Cuprate/cuprate/issues/445 would be good before releasing beta
```
```
boog900: I would be ok with keeping the killswitch for beta 
```
```
boog900: IMO we should try keep the values in line with monerod 
```
```
boog900: I do agree that I don't want really complicated load balancing/shedding in cuprate 
```
```
syntheticbird: well, will end up in my fork ig then
```
```
syntheticbird: so will distributed support too
```
```
syntheticbird: certainly
```
```
syntheticbird: regarding the default I hard stand on what I said:
> - `restricted_request_byte_limit`: 1MB is way too large. There is zero sensible usecase. You can decrease it to 300kB.
```
```
syntheticbird: monerod isn't perfect
```
```
syntheticbird: and for me this relax default is a flaw
```
```
boog900: absolutely but  1mb isn't that huge either  
```
```
boog900: p2p is 100mb 
```
```
syntheticbird: under high load it is
```
```
syntheticbird: for ddos it is
```
```
syntheticbird: I mean you are the first one advocating for removing the unnecessary. 1MB is unnecessary and is never reached in real world scenarios 
```
```
syntheticbird: if someone wanna play at stress testing the node he can rise the limit up
```
```
boog900: I think a DoS is going to come from somewhere else rather than the fact we put the limit at 1mb compared to 300kb 
```
```
boog900: and I would rather be consistent 
```
```
syntheticbird: At the moment cuprate is serializing request/response. 1 request 1 response, only when the response is sent than the next request is read. 1MB is potentially 200% more data to process for the node in a single request. I honestly don't understand what consistency is there here. monerod is in the wrong. 
```
```
syntheticbird: consistency here is making the choice of not making a choice.
```
```
syntheticbird: if this is about user expectancy on default, there are plenty of examples in the config that acknowledge already our stance of RTFM
```
```
syntheticbird: are we ending the meeting btw?
```
```
syntheticbird: we're over the hours
```
```
boog900: we are discussing 
```
```
syntheticbird: alright
```
```
boog900: Individual requests have upper limits on certain params 
```
```
boog900: so it is not always 200% more work 
```
```
syntheticbird: ok
```
```
boog900: my point is this is a user facing thing and I would rather be consistent unless 1MB is really an issue 
```
```
boog900: right now 1 MB is just more data that might have to be processed I can't see 700kb being the saving factor in us not getting DoSed 
```
```
syntheticbird: my point is that default must be sane and stick to reality. We never know when and how exactly we're going to be exploited. Number of software have seen vulnerabilities being exploited because of relaxed defaults.
```
```
syntheticbird: 1MB for me is an issue. It's way over the reality, for what is supposed to be a limit.
```
```
syntheticbird: just taking wrong defaults and waiting for something to happen is a bad mindset honestly. We should be proactive and enforce sanity whenever possible. If it affects user experience then it s worth discussing it. But right now lowering it to 300kB is free.
```
```
boog900: why 300kb?
```
```
boog900: I still think 1MB is low enough, p2p is 100MB 
```
```
syntheticbird: rule of thumbs really. Wallets requests never goes over 50kB. let's allow up to 6x as the maximum allowed until it can be considered malicious.
```
```
syntheticbird: it can be lowered down
```
```
syntheticbird: is this p2p global limit or request limit?
```
```
boog900: max tx size is 150kb, 6x is 900kb which is pretty much 1MB, we got him 😎
```
```
boog900: global, some requests lower it though 
```
```
syntheticbird: lol. very true I was focused on a scanning scenario. tx broadcast are opportunistic. Pretty sure no one is broadcasting 6x transactions in a single call. I'm not even sure this is possible
```
```
m-relay: <p​lowsof> gg 
```
```
hinto: there is also https://github.com/Cuprate/cuprate/issues/473 left to decide, I guess for another time
```
```
boog900: I think if we can show the extra 700kb puts meaningful more load on nodes I would be happy to lower it but until then I think keeping parity is better. It's not like 1MB is really high 
```
```
hinto: FWIW I don't think it is realistic to advertise all of our crates as public with a level of stability/commitment I am thinking
```
```
syntheticbird: Since its never actually reached in real world scenario, it's gonna be hard to demonstrate. It doesn't need to be low, it just need to not be out of touch. I would be happy to show it is in a later time.
```
```
boog900: I have wanted to publish crates, but we are currently prevented by git deps 
```
```
syntheticbird: yeah i'm unsure about that
```
```
boog900: I have tried to make progress on some recently though 
```
```
boog900: we don't have to keep the versions in sync, but we will need to publish them all I think 
```
```
syntheticbird: we can make them public sure, but let's precise that this is a subcrate of project that is dictating changes
```
```
boog900: I think we can discuss more another time, with this being blocked anyway 
```
```
syntheticbird: alright
```
```
boog900: Thanks everyone!
```
```
boog900: !meeting 
```

# Action History
- Created by: moo900 | 2025-06-17T18:51:49+00:00
- Closed at: 2025-06-24T19:33:42+00:00
