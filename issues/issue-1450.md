---
title: 'Cuprate Meeting #119 - Tuesday, 2026-09-08, UTC 18:00'
source_url: https://github.com/monero-project/meta/issues/1450
author: moo900
assignees: []
labels: []
created_at: '2026-09-01T18:40:23+00:00'
updated_at: '2026-09-08T19:15:21+00:00'
type: issue
status: closed
closed_at: '2026-09-08T19:15:21+00:00'
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

Previous meeting: #1447

# Discussion History
## moo900 | 2026-09-08T19:15:20+00:00
## Meeting logs
```
boog900: 1) greetings 
```
```
syntheticbird: Hello
```
```
redsh4de: ello
```
```
boog900: 2) updates 
```
```
syntheticbird: been zzzzzzzzzZZZZZZZZZZzzzzzzzzzzzZZZZZZZZZZZZZZZzzzzzzzzzzzzz during last week
```
```
boog900: I have been working on making the rolling tapes for pruning 
```
```
redsh4de: submitted a PR for ending the block downloader task when shutting down, reviews
```
```
boog900: 3) Project: What is next for Cuprate?
```
```
boog900: le birb: do you want to discuss stagex
```
```
syntheticbird: lets treat stagex in last
```
```
boog900: Is there anything anyone wants to discuss first?
```
```
syntheticbird: looks like i can start
```
```
syntheticbird: kayabanerve: recently shared his negative opinion on the StageX project on an old PR from tobtoht that planned on providing monerod release builds with StageX. 
```
```
syntheticbird: this has been mentioned last CCS meeting since concerning my CCS that is currently funding
```
```
syntheticbird: Discussing whether to stay on StageX or switching to another system is therefore encouraged
```
```
irc_plowsof: 🙏
```
```
boog900: What do you think about stagex le birb?
```
```
syntheticbird: From what I understand from kayabanerve's critics were that StageX doesn't emphasize on quality and that binaries were found in some packages, despite some reasoning behind it. He has contributed to the project before and I'm inclined to believe his general sentiment on the project despite not having a lot more details
```
```
syntheticbird: I think stagex is a thousand time easier to setup than Guix, and also forces us to rely on musl which I think is a good thing
```
```
syntheticbird: Rust package and boostrap is also much more straightforward
```
```
syntheticbird: StageX is more attractive to me
```
```
syntheticbird: But
```
```
irc_selsta: not cuprate related from monero's side I would like for us to move to StageX and tobtoht also had that opinion, Guix is so difficult to use and requires tons of storage space it will make it so that we will barely get people participating in repro builds
```
```
syntheticbird: Guix is of much more quality that is an undeniable fact
```
```
irc_selsta: (not refuting kayaba's concerns here)
```
```
syntheticbird: selsta thx for confirming my comprehension
```
```
boog900: This is quiet an annoying decision
```
```
boog900: Both options don't seem great 
```
```
syntheticbird: Guix is way much harder but much less at risk of reproducibility incident
```
```
irc_plowsof: fork it and remove the binaries :P
```
```
boog900: Its more the llm code I worry about 
```
```
syntheticbird: yeah so kayabanerve cited that opion but ain't no way we are maintaining a fork
```
```
irc_plowsof: 👍
```
```
syntheticbird: boog900 in stagex?
```
```
syntheticbird: * boog900 you mean in stagex?
```
```
boog900: Yeah
```
```
syntheticbird: im too but I'm just assuming Guix is using it too but in secret
```
```
boog900: Isn't it made by the fsf?
```
```
syntheticbird: > The Free Software Foundation (FSF) is a fiscal sponsor through the Working Together for Free Software Fund.
```
```
boog900: Ah 
```
```
boog900: It still makes me think they would be more against llms than the stagex guys 
```
```
boog900: Who are very open to it and use it a lot 
```
```
syntheticbird: If I had to choose I would go with StageX because of all the difficulties you have to deal with with Guix and if it is found to not be appropriate then switch to Guix. Because Guix is much more consequential to learn and maintain.
```
```
syntheticbird: i get the concern yeah, I think too they are more likely to fuck up llm contributions than gnu-lovers
```
```
boog900: What's the worse case with the llm use? 
```
```
syntheticbird: they break a package update or make it not reproducible
```
```
syntheticbird: fucking up the entire bootstrapping process is very unlikely but that is in the worst case scenario
```
```
syntheticbird: I assume these would be detected and fixed rather quickly (2 weeks?)
```
```
syntheticbird: just on the allocator note from kayabanerve
```
```
syntheticbird: I'm more than fine at shipping musl mandatory with hardcoded allocator
```
```
syntheticbird: glibc should die and wanting to use hardened_malloc for cuprate is, while honorable, useless
```
```
syntheticbird: on the "we should update libc", I think that's perfectly appropriate because of how much slower musl vulnerabilities comes out compared to glibc.
```
```
jpk68: >glibc should die
```
```
jpk68: Holy based
```
```
syntheticbird: thats sums up my thought honestly
```
```
syntheticbird: boog900, redsh4de what do you think we should do ?
```
```
boog900: I do feel like we would be sacrificing security by going with stageX
```
```
syntheticbird: That's undeniable, but it's really a matter of whether it fits our reproducibility need. Do we want every versions to be reproducible to the end of time ? then we burn Guile and GNU viruses in your brain. If all we want is "auditability" during a release window, then StageX is fine IMO.
```
```
redsh4de: Im not really excited about the fact they plan to full-slop everything
```
```
redsh4de: It sounds like we’d have to permanently pin a older version
```
```
syntheticbird: sounds like something that might happen yes
```
```
redsh4de: Maintaining a fork isn’t really realistic at our current manpower
```
```
irc_selsta: would be unfortunate if monero and cuprate use a different system for repro builds
```
```
redsh4de: I am however less excited about Guix and its complexity, so i think given we have these two options i’d lean towards the one that’s easier to deal with
```
```
syntheticbird: I am just going to say that since the start of this meeting the guix package website broken and no package can be seen or search
```
```
syntheticbird: just a reminder that Guix too can break
```
```
syntheticbird: (far fetched i know)
```
```
syntheticbird: Guile is just utterly disgusting to learn, and you need the resources, but ig once you overcome these two you transcended into a GNU superbeing that Guix becomes incredible to use
```
```
syntheticbird: hardware resources*
```
```
redsh4de: and yeah this is a good point too
```
```
boog900: Are these the only 2 options even if we drop the bootstrap requirement?
```
```
syntheticbird: no there is a much simpler one
```
```
syntheticbird: i actually proposed it 3 years ago
```
```
syntheticbird: 2 years
```
```
syntheticbird: i don't remember
```
```
syntheticbird: debian repository archives
```
```
syntheticbird: virtual machines with a specific set of resources with a fixed date snapshot of debian repository
```
```
syntheticbird: i know what you are going to say: (imagine Mickey talking) "its very hacky we need something robust, a toolchain made for it HAHA"
```
```
syntheticbird: and then you imagine writing thousands of lines of Guile
```
```
syntheticbird: Gives you perspective
```
```
syntheticbird: actually selsta is right in that monero and cuprate both using stagex is actually a good thing because that means sharing the fate burden if stagex breaks 
```
```
syntheticbird: burden of fate*
```
```
syntheticbird: more manpower to the issue
```
```
boog900: But then why have 2 impls 
```
```
boog900: Redundancy and that 
```
```
syntheticbird: im not following, which 2 impls?
```
```
boog900: Cuprate and monerod 
```
```
syntheticbird: oh
```
```
syntheticbird: yeah thats far fetched, its not because we are a monero network safety net, not a monerod building infra safety net
```
```
syntheticbird: * yeah thats far fetched, its not because we are a monero network safety net that we are also monerod building infra safety net
```
```
syntheticbird: imo
```
```
boog900: I would be OK with stagex in a different repo with it still being recommended to build yourself
```
```
boog900: But the binaries being used instead of the github binaries currently
```
```
kayabanerve: Hi, sorry, I'm here
```
```
kayabanerve: I'm also a failure apparently
```
```
syntheticbird: I would be fine with that
```
```
syntheticbird: * I would be fine with that too
```
```
syntheticbird: what
```
```
syntheticbird: BELIEVE IN YOURSELF
```
```
kayabanerve: StageX cannot be trusted moving forward IMO, but it is fine as-is and can be forked moving forward for builds.
```
```
kayabanerve: We need a minimal subset _and_  Monero would also benefit from a fork with a certain package set.
```
```
syntheticbird: If a fork had to be done I would like it to be shared between monerod and cuprate
```
```
kayabanerve: Their LLM usage is reckless and unsafe. The existing code also lacks QA and has historically continuously had binary blobs found.
```
```
syntheticbird: you said in your last comment in the repo that these were compiled Regexes automaton. Should I understand from your message that other binaries were found without a proper reasoning  behind it ?
```
```
jpk68: So, they're basically using an LLM to modify the human-written source of an intermediate Rust compiler?
```
```
syntheticbird: were was that cited ? I must have missed it
```
```
syntheticbird: where
```
```
jpk68: I'm just asking, not sure I understand correctly
```
```
jpk68: Not sure where I heard it, sorry
```
```
kayabanerve: I don't trust them to perform QA themselves.
```
```
kayabanerve: I can't comment on Guix's QA but the whole point will be about which frontend we prefer for how we want to attempt reproducible builds, bootstrapped.
```
```
kayabanerve: > <@syntheticbird:monero.social> If a fork had to be done I would like it to be shared between monerod and cuprate

That, and Serai, may become a feasible amount of work which is worth it.
```
```
kayabanerve: > <@syntheticbird:monero.social> you said in your last comment in the repo that these were compiled Regexes automaton. Should I understand from your message that other binaries were found without a proper reasoning  behind it ?

No, they also shipped precompiled Zig and Ocaml compilers, and multiple participants knew but didn't raise it.
```
```
syntheticbird: LMAO
```
```
kayabanerve: They don't even have a clear definition on what "bootstrapped" is. The members who didn't raise it said it count as bootstrapped from source because the bin blobs are part of the Zig/Ocaml sources.
```
```
kayabanerve: There's also generated scripts (autoconf and so on) and a lack of investigation in general.
```
```
syntheticbird: well that's pretty convincing to not use StageX
```
```
syntheticbird: boog900: are you fine with Guix ?
```
```
syntheticbird: I can switch to Guix, but I would honestly prefer to fork stagex if I can get confirmation Monero will also participate with Cuprate and Serai
```
```
kayabanerve: mrustc supports Rust 1.94 or so, and the de facto head is using an LLM to upgrade it to compile Rust 1.98 or so, which is reckless IMO
```
```
syntheticbird: tho no idea if such long-term effort can fold into my current CCS
```
```
boog900: I would prefer guix especially as I am not the one doing it :)
```
```
syntheticbird: <Pasted image (2).png>
```
```
kayabanerve: It wouldn't be too hard to maintain a minimal package set just for us IMO. Then we could volunteer QA efforts moving forward.
```
```
irc_selsta: forked stagex sounds a lot nicer than guix
```
```
syntheticbird: I really don't want to maintain something else but my hate for GNU will provide me the energy for one last responsibility
```
```
boog900: > <@boog900:monero.social> I would be OK with stagex in a different repo with it still being recommended to build yourself

I still think what I said here would be fine 
```
```
kayabanerve: I've chimed in my part
```
```
syntheticbird: I would prefer to go this route of implementing Cuprate with current stagex as introductory towards a forked and maintained subset in the long-term
```
```
boog900: Yeah 
```
```
syntheticbird: good part
```
```
syntheticbird: just to be sure, is the other repository only hosting the stagex tooling or is a downstream fork of Cuprate ?
```
```
syntheticbird: probably first since you want to ship its binaries in main cuprate but i ask jic
```
```
boog900: Not just the tooling 
```
```
jpk68: Is there anything actually wrong with the code? Or do people just generally dislike the idea of using LLMs for that
```
```
syntheticbird: in this case its not generally, you don't fuck around with compilers
```
```
syntheticbird: you don't trust your llm, you don't trust your pc, you don't trust yourself
```
```
syntheticbird: what else?
```
```
boog900: Ah I meant to say no, just the tooling 
```
```
syntheticbird: got it
```
```
syntheticbird: allg for me, we can close discussion or opress upcoming criticism, or both
```
```
boog900: Using an llm to do big task like that is almost always a bad idea. Reviewing their code properly takes as long as it would have taken to just write it all yourself. So if they are just slopping and pushing they aren't reviewing. 
```
```
boog900: We can end here 
```
```
boog900: !meeting 
```

# Action History
- Created by: moo900 | 2026-09-01T18:40:23+00:00
- Closed at: 2026-09-08T19:15:21+00:00
