---
title: 'Cuprate Meeting #45 - Tuesday, 2025-03-04, UTC 18:00'
source_url: https://github.com/monero-project/meta/issues/1161
author: moo900
assignees: []
labels: []
created_at: '2025-02-25T19:03:04+00:00'
updated_at: '2025-03-04T19:20:18+00:00'
type: issue
status: closed
closed_at: '2025-03-04T19:20:18+00:00'
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
- anti-Kewbit Code of Conduct?

- Any other business

Previous meeting: #1158

# Discussion History
## moo900 | 2025-03-04T19:20:17+00:00
## Meeting logs
```
boog900: 1) Greetings 
```
```
hinto: hello
```
```
boog900: 2) updates 
```
```
boog900: I have been working on getting all the PRs for the release ready mostly there just need to do a few things for fast-sync
```
```
hinto: me: I am still sick but am doing much better now. I've been mostly out of the loop for the past few weeks so I'll be starting to catch up today - I think I'll be starting work on stuff too.
```
```
boog900: 2) Project: What is next for Cuprate?

```
```
boog900: all the PRs needed on my end for the release are open. 385 can probably be merged now the rest build on 382 which would be the thing most needing review.
```
```
hinto: I think I can commit to a release cycle starting this friday, if not then very likely next friday - I think it's mostly figuring out what can be left out / done manually and what needs to be done /automated for future releases
```
```
hinto: boog900: are you still for releasing soon?
```
```
boog900: yes
```
```
hinto: ok, 382 and 385 are the only PRs needed before a theoretical release then?
```
```
hinto: i.e. the commit will be post 382+385 merge
```
```
boog900: no ... 382, 384, 386, 389 + 385  
```
```
boog900: 384 is pretty small, 386 should also be an easy review. 382 and 389 are semi-big 
```
```
boog900: 385 has enough review and is pretty simple I am happy to merge now if you are 
```
```
boog900: 382, 384, 386, 389 all build of off the last 
```
```
hinto: I am less confident about getting those all merged before this friday
```
```
syntheticbird: Hello there, sorry for being late
```
```
hinto: if they are absolutely required for a release then can until they are merged? 
```
```
hinto: *can we delay
```
```
boog900: not when we are in competition with my syncing monerod!
```
```
syntheticbird: Maybe I can review low hanging fruits
```
```
syntheticbird: you said 384 was pretty small
```
```
boog900: /s yeah although I think they can be merged in time 382 and 389 are going to be the only hard ones to review IMO 
```
```
boog900: > <@syntheticbird:monero.social> you said 384 was pretty small

it's waiting on 382 though
```
```
syntheticbird: Ok so 382 top priority, which unlock 385 and 384
```
```
boog900: @hinto are you ok with me merging 385 now?
```
```
boog900: > <@syntheticbird:monero.social> Ok so 382 top priority, which unlock 385 and 384

nah they are in a queue in this order: `382, 384, 386, 389`
```
```
boog900: all building off the last 
```
```
hinto: I will review it today
```
```
boog900: I wouldn't spend too long on it 👍️
```
```
syntheticbird: https://github.com/Cuprate/cuprate/pull/386/files#diff-3a3764a1c30d9d038456bf12e25ec9eef596511a7e0f8b261125540516e68f84L162-R182
https://github.com/Cuprate/cuprate/pull/382/files#diff-3a3764a1c30d9d038456bf12e25ec9eef596511a7e0f8b261125540516e68f84L162-R196

Why is there duplicate changes between 382 and 386 ?
```
```
syntheticbird: is 386 based on 382 ?
```
```
boog900: because they build off each other 
```
```
boog900: yes
```
```
boog900: the git resident wizard: in this order: 382, 384, 386, 389 they will have duplicate changes 
```
```
hinto: FYI the initial planned architectures are `{windows,macos,linux} * {x64,arm64}`
```
```
syntheticbird: I would have found it clearer to make 386 PR `batch-outputs` <- `new-monero-oxide-api` instead of simply `main` <- *
```
```
hinto: I'd like to test them all but I don't think I'll have time if we're releasing soon so I'll be prioritizing  x64 linux
```
```
boog900: I tested x64 linux a lot + I did a sync on a PI
```
```
syntheticbird: Are all the PRs related to musl been pushed ?
```
```
syntheticbird: I remember some issues and some fix proposed but not that they were merged.
```
```
hinto: It would also be good if we eventually made something similar to https://doc.rust-lang.org/rustc/platform-support.html
```
```
boog900: > <@syntheticbird:monero.social> I would have found it clearer to make 386 PR `batch-outputs` <- `new-monero-oxide-api` instead of simply `main` <- *

maybe but they are going to be merged to main not to batch outputs first 
```
```
syntheticbird: yeah i know, it's just a matter of making review easier
```
```
syntheticbird: * yeah i know, it's just a matter of making independent review easier
```
```
boog900: once 382 is merged the diff will update
```
```
syntheticbird: I agree
```
```
boog900: I am active most of the day it'll be merged quick after approval 
```
```
boog900: anything more on this or should we move on?
```
```
hinto: out of all niche arches, this is probably the one to focus on for alpine, correct? 
```
```
syntheticbird: yes
```
```
hinto: I wrote in the roadmap that supporting more niche OSs would be less prioritized but supporting alpine seems like a worthy exception
```
```
hinto: more so than freeBSD
```
```
hinto: ok, we can move on
```
```
boog900: - anti-Kewbit Code of Conduct?

```
```
boog900: the git resident wizard: 
```
```
syntheticbird: Linked issue: https://github.com/Cuprate/cuprate/issues/390
```
```
syntheticbird: With the upcoming release we can expect an influx of new users opening issues and/or contributors
```
```
syntheticbird: I would like to discuss in this meeting consensus about making a short of code of conduct
```
```
syntheticbird: It's just a matter of having some materials against bad actors, hostile people.
```
```
monero.arbo: I will chime in that "tolerant of opposing views" as a blanket value makes me go 'hmmm'
```
```
monero.arbo: as long as the topics are directly related to the project though, should be fine? shrug
```
```
syntheticbird: For context, this is based on Ruby code of conduct
```
```
syntheticbird: https://www.ruby-lang.org/en/conduct/
```
```
syntheticbird: Yes, here opposing views means on a technical or related topic. Opposing views as of a "political sides" is de-facto prohibited by the "no political discussion" rule
```
```
syntheticbird: ie. You will be tolerant of the other contributors explaining in large why your idea sucks.
```
```
monero.arbo: for sure, I get that. though as noted in the draft there may be times when those intersect
```
```
syntheticbird: just to be clear, what intersect, opposing views on technical topic, or technical and political topic?
```
```
monero.arbo: I am referring to the part that says no politics "unless directly concerning Cuprate" i.e. cuprate as a project may have to deal with 'political' issues is how I interpret that
```
```
syntheticbird: yeah you're right, I'm mostly referring here to any geopolitical situation, such as "X maintainer or contributor have been removed from the CODEOWNERS because he has been drafted into the army"
```
```
monero.arbo: I think, for me, as long as it's clear "Everyone is welcome!" implies that basic respect for ethnicity, gender, etc I'm good
```
```
monero.arbo: Not that I think you don't, but we live in a world where "opposing views" sometimes don't incldue those things
```
```
syntheticbird: Yeah I understand. For me these characteristics are implied.
```
```
monero.arbo: fair enough
```
```
syntheticbird: I'll treat everyone equally, and don't give a particular value to any characteristics. Of course I don't want let's say nazi to feel free in the repo/channels. So if they start acting "hostile or repetitively offensive", they are going to get banned
```
```
syntheticbird: ideally i would want zero nazi
```
```
syntheticbird: hope that clears up things
```
```
monero.arbo: for sure, just wanted to share my thoughts from reading it, aprpeciate the clarification
```
```
syntheticbird: boog900: hinto whats your opinion on having a CoC, not particularly my draft.
```
```
boog900: hinto: do you have any thought on this?
```
```
boog900: ah nice delay
```
```
boog900: i don't mind having a CoC I think we are probably small enough where we don't really need one 
```
```
boog900: but then you can retrospectively add one when it is needed 
```
```
boog900: can't*
```
```
boog900: critical typo 
```
```
syntheticbird: yeah I am mostly worried about having to place a code of conduct during a "drama". That's a nice seed for some useless shitstorm from people that wouldn't give 2 f*ck about the project or people.
```
```
syntheticbird: now is a good time imo since new contributors will be aware of this from the start.
```
```
hinto: I don't think I have any meaningful thoughts here although I agree that adding things like this works better when done early.
```
```
boog900: now is choosing which CoC
```
```
syntheticbird: Mine can always be adapted but out of the my very worked Covenant Contributor adaptation for monero, Ruby CoC seems to have a frank success from people that were otherwise unhappy about the idea
```
```
syntheticbird: * Mine can always be adapted but out of the very worked Covenant Contributor adaptation for monero, Ruby CoC seems to have a frank success from people that were otherwise unhappy about the idea
```
```
boog900: it's small and simple which is nice
```
```
boog900: a decision doesn't have to be made right now, people can put their thoughts in the comment of that issue and we can decide in a future meeting 
```
```
syntheticbird: sgtm
```
```
boog900: anything else anyone wants to discuss today?
```
```
monero.arbo: I think cuprate is neat
```
```
rucknium: IMHO, it would be good to have a public FAQ about what is cuprate to release when the alpha goes live
```
```
rucknium: Community members don't understand what cuprate is, why it exists, its relationship to monerod, and whether it is intended to replace monerod in the future
```
```
boog900: yeah I agree, also what we are missing so people don't confused why their wallet isn't working 
```
```
boog900:  * yeah I agree, also what we are missing so people don't get confused why their wallet isn't working 
```
```
hinto: I am planning on creating a (truncated) user book for the first release, I will try covering those points and more
```
```
syntheticbird: i may have seen "will the database be compatible with monerod" at least 10 times now
```
```
hinto: https://user.cuprate.org will likely be a general FAQ landing page for the first couple releases
```
```
boog900: > <@syntheticbird:monero.social> i may have seen "will the database be compatible with monerod" at least 10 times now

yeah I slightly regret making it incompatible now lol 
```
```
syntheticbird: fjall on the way dw
```
```
boog900: true, I am excited to test that when (if) it gets added 
```
```
rucknium: AFAIK, alternative node implementations rarely (if ever) have compatible DB formats
```
```
hinto: it's worth noting `f(MonerodDb) -> CupratedDb` and the inverse function are practically possible and not too difficult to do
```
```
boog900: it is best, gives us maximum flexibility 
```
```
boog900: we could probably build a crate that impls the service interface and just uses monerod's DB format 
```
```
rucknium: You probably also want to say in the FAQ that the DB size is larger than monerod
```
```
syntheticbird: All the point to covers are worth a github issue
```
```
syntheticbird: (to also accept external inputs)
```
```
boog900: anything else for today?
```
```
syntheticbird: i think we're good
```
```
boog900: monerod is currently at `2450773 `
```
```
syntheticbird: end the poll lol
```
```
boog900: Thanks everyone!
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
- Created by: moo900 | 2025-02-25T19:03:04+00:00
- Closed at: 2025-03-04T19:20:18+00:00
