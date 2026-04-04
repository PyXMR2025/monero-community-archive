---
title: 'Cuprate Meeting #86 - Tuesday, 2026-01-20, UTC 18:00'
source_url: https://github.com/monero-project/meta/issues/1327
author: moo900
assignees: []
labels: []
created_at: '2026-01-19T13:56:05+00:00'
updated_at: '2026-01-21T00:08:51+00:00'
type: issue
status: closed
closed_at: '2026-01-20T18:37:29+00:00'
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

Previous meeting: #1320

# Discussion History
## moo900 | 2026-01-20T18:37:28+00:00
## Meeting logs
```
boog900: 1) greetings
```
```
m-relay: <C​indy> hi
```
```
hinto: ehllo
```
```
boog900: 2) updates 
```
```
boog900: Me: I added some proptest's state machine tests to the tapes database, which caught some bugs. I also began the process of removing our database abstraction and moving the txpool over to fjall 
```
```
hinto: me: mostly finished PoWER, I think I'll leave some notes, open for review this week and fix p2p merge conflicts later; maybe the Cuprate version could be opened now since it is just the main crate
```
```
boog900: > Project: What is next for Cuprate?
```
```
boog900: * 3. Project: What is next for Cuprate?
```
```
boog900: hinto: would you be against a 4 GB minimum RAM requirement for Cuprate? 
```
```
boog900: I want to add some dynamic cache settings based on the amount of RAM we are told the system has 
```
```
hinto: I might be remembering wrong but won't it be closer to that for post-FCMP monerod?
```
```
boog900: probably, someone did sync after a few issues with 2 GB on stressnet though IIRC 
```
```
m-relay: <C​indy> i have a question, does the memory requirement include memory overhead from the OS?
```
```
hinto: IIRC the most purchased pi 5 models were 8gb, if we are using that as a benchmark
```
```
hinto: although it does mean the low-cost VPS plans are no longer viable, those usually start at 1/2GB
```
```
boog900: yeah, a 4GB system is the minimum not 4GB allocated to Cuprate, I plan to make the default setting to use 50% of system RAM upto a certain amount for each sub-system. 
```
```
m-relay: <C​indy> i see
```
```
boog900: it wouldn't be a hard minimum but it gives us a lower bound on maximum RAM usage + it sets expectations for people who try lower than 4 GB
```
```
boog900: as I think even now for Cuprate and monerod that is probably too low
```
```
boog900: the hdd ones are now available though :D
```
```
hinto: I've had `cuprated` running well up until now with a 1GB cap btw
```
```
boog900: wow really 👀
```
```
boog900: exceeding what I thought it could do lol 
```
```
boog900: did you sync with 1 GB?
```
```
hinto: although it eats ram if you give it more, seems to peak at 3.5gb, I have it capped at 2gb currently
```
```
boog900: that would be LMDB :)
```
```
hinto: yes
```
```
hinto: 1.3gb resident, 0.7 shared, so possibly other things too
```
```
syntheticbird: Hi
```
```
boog900: Ok that is interesting, I guess no need to agree to 4 GB today we can see how the new database performs on everyones systems first. One of the "problems" with fjall and the tapes is you need to set the cache sizes yourself 
```
```
boog900: you can't rely on the system to eat all the RAM you give it 
```
```
boog900: blessing and a curse as we do get more control over what is cached. 
```
```
boog900: anything anyone else wants to discuss today? 
```
```
hinto: Should I open https://github.com/Cuprate/cuprate/pull/568 for review? or wait until upstream is merged?
```
```
gingeropolous: are peeps mining on it yet?
```
```
boog900: I would wait
```
```
boog900: no and out of every activity you can do on Cuprate that is probably the least recommended. Mining on Cuprate could make chain splits worse if they were to happen. 
```
```
m-relay: <C​indy> i appreciate the modularity of cuprate
```
```
m-relay: <C​indy> i use some parts of it in my own program
```
```
m-relay: <C​indy> i know i said that before :P
```
```
boog900: so this should probably wait for 1.0, at least for any big mining operations 
```
```
boog900: Make sure to let us know when you make it public :) 
```
```
m-relay: <C​indy> i have
```
```
boog900: link?
```
```
m-relay: <C​indy> https://codeberg.org/techmetx11/xmrgift
```
```
boog900: I can't see Cuprate being used :(
```
```
m-relay: <C​indy> i've only tested it on stagenet
```
```
boog900: only monero-oxide 
```
```
m-relay: <C​indy> i remember cuprate using monero-oxide though :o
```
```
m-relay: <C​indy> maybe i misremembered
```
```
syntheticbird: because vikings drink water and I drink water doesn't mean i'm a viking
```
```
m-relay: <C​indy> yeah true
```
```
boog900: FWIW here is cuprate: https://github.com/Cuprate/cuprate

It's basically node parts, rather than monero-oxdie which is wallet/underlying types parts 
```
```
boog900: I think we can end here, thanks everyone!
```
```
hinto: thanks
```
```
boog900: !meeting 
```

# Action History
- Created by: moo900 | 2026-01-19T13:56:05+00:00
- Closed at: 2026-01-20T18:37:29+00:00
