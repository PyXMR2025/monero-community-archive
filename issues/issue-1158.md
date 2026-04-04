---
title: 'Cuprate Meeting #44 - Tuesday, 2025-02-25, UTC 18:00'
source_url: https://github.com/monero-project/meta/issues/1158
author: moo900
assignees: []
labels: []
created_at: '2025-02-18T19:09:55+00:00'
updated_at: '2025-02-25T19:03:05+00:00'
type: issue
status: closed
closed_at: '2025-02-25T19:03:05+00:00'
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

Previous meeting: #1154

# Discussion History
## moo900 | 2025-02-25T19:03:04+00:00
## Meeting logs
```
boog900: 1) greetings 
```
```
syntheticbird: Hello there
```
```
hinto: hello
```
```
boog900: 2) updates 
```
```
syntheticbird: me: Unfortunately busy, didn't had the time to draft up Tor integration
```
```
boog900: worked on PRing what I have been working on + a couple bug fixes. Mostly done just the fast sync PR now 
```
```
hinto: I have been / am sick.
```
```
syntheticbird: oh no
```
```
syntheticbird: wishing you good healing
```
```
boog900: 3) Project: What is next for Cuprate?
```
```
boog900: Anyone oppose March 6th as release day? 
```
```
syntheticbird: nope
```
```
hinto: I haven't tested anything / worked on release automation / finished the user book.
```
```
syntheticbird: exciting
```
```
boog900: ngl I kinda want to just say fuck it, we should set a date and whatever is ready is ready. 
```
```
boog900: the user book can come later, so can fast sync if I don't get it merge-able in time 
```
```
syntheticbird: ngl I would still like fast-sync to be merged
```
```
syntheticbird: users are going to get confused
```
```
boog900: alpha cuprate's target audience is people in this room 
```
```
syntheticbird: true
```
```
boog900: FWIW I do too and I expect it to be 
```
```
syntheticbird: ok well im not against pushing current "feature state" in release.
```
```
boog900: but I have a feeling the best thing to do if it isn't is just to release without it 
```
```
rottenwheel: Is fast-sync just in its isolated branch on `cuprated` repository currently?
```
```
rottenwheel: Plan is to release `cuprated` "stable" without `fast-sync` and tuck it into its isolated branch for now?
```
```
boog900: yeah but it is not in a state to be merged 
```
```
boog900: it was just a testing branch to get a rough idea on how it will work 
```
```
boog900: plan is for `cuprated` to have fast sync if I get it ready in time
```
```
boog900: if not it will wait for the next release or we delay the release 
```
```
syntheticbird: hinto: whats your opinion?*
```
```
rucknium: Ides of March release date. End Caesar's reign.
```
```
rucknium: (This is a joke)
```
```
syntheticbird: I got the joke
```
```
syntheticbird: 👍️
```
```
rucknium: Did you know "cuprate" is an anagram for "capture"?
```
```
syntheticbird: fire a dictionary to get wtf is an anagram
```
```
syntheticbird: i didn't know. thats a valuable information
```
```
rucknium: Used pretty often in fiction as a big revelation of the villain. Anyway, sorry for offtopic.
```
```
boog900: are ... we ... the baddies?
```
```
syntheticbird: of course
```
```
boog900: anyway while we wait for hinto anyone want to discuss anything else?
```
```
hinto: In my mind even the first release (even if alpha) is still reasonably well prepared, won't crash under relatively normal circumstances, and has some user documentation. I don't want to take responsibility for any user confusion or error nor allow for that situation to occur in the first place, I rather start from the beginning well prepared so that there are already links that provide answers. I also think starting off weak + incremental improvement has a risk of looking bad for a while (where are the docs? how do I do $X? why is this crashing?, $1000_OTHER_COMMON_ISSUES_THAT_MUST_ALL_BE_RESPONDED_TO_INDIVIDUALLY).
```
```
hinto: arguments for premature release: "we can improve incrementally", "alpha is meant for these type of sort-of-broken releases"
```
```
hinto: which I think are fine too, although I think I would rather wait and do it right than not
```
```
syntheticbird: I will favor a balance here. My opinion is that we release once:
- Current fixes are merged
- User book is merged
```
```
boog900: IMHO setting a date for release that we are going to release at no matter what will be beneficial, if 6th is too optimistic then we can pick another date. Although I think we will be ready by the 6th. 

The user docs for release don't have to be that complex 
```
```
boog900: also can be updated as questions come in 
```
```
syntheticbird: I also see 6th as not too optimistic
```
```
syntheticbird: for the second time, sounds fair to me
```
```
hinto: Ok, reminder that I only push back to make sure tradeoffs have been thought of and deemed favorable in a public space, other than that I am ok with anything reasonable
```
```
hinto: although I am not sure if I can commit for the 6th, I am still sick
```
```
rottenwheel: > <@boog900:monero.social> are ... we ... the baddies?

Cuprate is an illuminati CIA Mossad joint operation to overtake the Morono network. 
```
```
rottenwheel: It is widely known. 
```
```
syntheticbird: meds
```
```
syntheticbird: Ok well
```
```
boog900: ok 10th, for some extra days?
```
```
syntheticbird: nah 6th is good
```
```
boog900: 🔥
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
hinto: if it's only the current commit + release automation 6/7th is probably ok
```
```
hinto: (not a commitment)
```
```
boog900: it is not 
```
```
boog900: it's some pending PRs aswell 
```
```
boog900: well still go for 6th I think we can do it 
```

# Action History
- Created by: moo900 | 2025-02-18T19:09:55+00:00
- Closed at: 2025-02-25T19:03:05+00:00
