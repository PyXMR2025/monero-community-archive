---
title: 'Cuprate Meeting #114 - Tuesday, 2026-08-04, UTC 18:00'
source_url: https://github.com/monero-project/meta/issues/1432
author: moo900
assignees: []
labels: []
created_at: '2026-07-28T18:38:58+00:00'
updated_at: '2026-08-04T18:31:35+00:00'
type: issue
status: closed
closed_at: '2026-08-04T18:31:35+00:00'
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

Previous meeting: #1428

# Discussion History
## moo900 | 2026-08-04T18:31:34+00:00
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
boog900: We put out a new release!
```
```
redsh4de: 🎉
```
```
boog900: 3) Project: What is next for Cuprate?
```
```
boog900: My next CCS will be focused on getting Cuprate ready for FCMP++ with the RPC and tx relay changes too
```
```
redsh4de: working on expanding build targets - currently, FreeBSD and OpenBSD are pretty much a go, working on riscv support at the moment
```
```
boog900: do you have a riscv to test with?
```
```
redsh4de: plan is to rely on qemu for now
```
```
redsh4de: tested freebsd & openbsd on 15.1 and 7.9 respectively
```
```
redsh4de: after im finished with this probably taking a break, the burnout stage's creeping in
```
```
syntheticbird: mental health is important
```
```
boog900: nothing worse for the mental health than fighting CI 
```
```
syntheticbird: lmao
```
```
redsh4de: waiting hours for yet another undiscovered roadblock will do it
```
```
redsh4de: :P
```
```
boog900: anything else to discuss today?
```
```
syntheticbird: Just a word
```
```
syntheticbird: to say that reception on Reddit is good regarding latest release
```
```
syntheticbird: 6k views and 100% upvote ratio
```
```
redsh4de: would be good if @monero retweets too to get more eyes on it
```
```
syntheticbird: very true. on X side it was kinda invisible because of the coldcard event
```
```
syntheticbird: tho some people with influence liked (but not shared)
```
```
boog900: I was saying to syntheticbird we should put out a sped up video of both syncing side by side
```
```
boog900: that way people can _see_ the diff in speed 
```
```
syntheticbird: I am currently installing OBS
```
```
boog900: exciting 
```
```
syntheticbird: I also said to boog that pruning support is currently the biggest blocker for enthusiasts to try Cuprate
```
```
syntheticbird: We tend to forget how important pruning is for most local node users
```
```
boog900: hopefully that should be ready soon :)
```
```
syntheticbird: so TheRedHell ongoing work is welcome
```
```
boog900: a pruned DB should be ~80GB
```
```
syntheticbird: STOP BEING SYNCHRONIZED WITH ME ITS SCARY
```
```
syntheticbird: whats monerod current ?
```
```
boog900: over 100 IIRC
```
```
syntheticbird: cuprate keeps winning
```
```
boog900: that's the tapes 
```
```
boog900: anything else for today? 
```
```
theredhell: hi
```
```
boog900: 👋
```
```
syntheticbird: literally the world leader group chat video with finland answering with a hi at the very end
```
```
theredhell: I would say I'm maybe 60-70% done, I can maybe also make a draft pr and you can start reviewing already
```
```
theredhell: Am I not supposed to be in this meeting? 😅
```
```
syntheticbird: we aren't in a hurry, you can take the time to be done before opening PR, if you want
```
```
boog900: no harm in opening one though
```
```
syntheticbird: no no anyone is welcome, i am just joking around
```
```
theredhell: I won't be able to work much until next week though
```
```
boog900: that's fine, we aren't in a rush for the next release 
```
```
boog900: I think we can end here
```
```
boog900: Thanks everyone
```
```
syntheticbird: BOOG IS HOLDING ME HOSTAGE IN THEIR BASEMENT HELP
```
```
redsh4de: thank you
```
```
boog900: bro 
```
```
syntheticbird: thank you
```
```
theredhell: thanks
```
```
boog900: moans at me to let them say thanks just to do that 😆
```
```
boog900: !meeting 
```

# Action History
- Created by: moo900 | 2026-07-28T18:38:58+00:00
- Closed at: 2026-08-04T18:31:35+00:00
