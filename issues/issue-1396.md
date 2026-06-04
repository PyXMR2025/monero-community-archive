---
title: 'Cuprate Meeting #105 - Tuesday, 2026-06-02, UTC 18:00'
source_url: https://github.com/monero-project/meta/issues/1396
author: moo900
assignees: []
labels: []
created_at: '2026-05-26T18:44:00+00:00'
updated_at: '2026-06-02T19:06:03+00:00'
type: issue
status: closed
closed_at: '2026-06-02T19:06:03+00:00'
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

Previous meeting: #1392

# Discussion History
## moo900 | 2026-06-02T19:06:01+00:00
## Meeting logs
```
boog900: 1) greetings
```
```
redsh4de: hello!
```
```
syntheticbird: Hi
```
```
boog900: 2) updates
```
```
boog900: Me: PR'd some more RPC changes, only a few more PRs needed for main to be up to date with my changes 
```
```
syntheticbird: me: reviewed some PRs. Made my CCS proposal for address book, reproducible build and supply chain security
```
```
redsh4de: me: made a PR for adding some missing ban behaviours from monerod (same behaviour)and TODO some where we need a score system.
opened an issue for implementing a readline library for the interactive IO, PR review
```
```
redsh4de: * me: made a PR for adding some missing ban behaviours from monerod (same behaviour as we have rn) and TODO some where we need a score system.
opened an issue for implementing a readline library for the interactive IO, PR review
```
```
boog900: 3) Project: What is next for Cuprate?
```
```
boog900: SyntheticBird: you had something you wanted to discuss today?
```
```
syntheticbird: I would have two topic to aboard but if any one want to discuss before because frankly I'm on phone right now and it's hell to type
```
```
syntheticbird: No one ?
```
```
redsh4de: i reckon id appreciate any thoughts/comments on the readline proposal
```
```
redsh4de: for ref: https://github.com/Cuprate/cuprate/issues/623

tldr: if interactive terminal, provide stable prompt that logs dont write over
pros: UX-maxxing
cons: new transitive deps
```
```
boog900: It does sound nice but yeah I don't really like more deps
```
```
syntheticbird: was about to say the same
```
```
jbabb: cool tho, I like the ux possibilities that'd enable
```
```
syntheticbird: that would be in opposition with what I was about to say
```
```
syntheticbird: one of my points*
```
```
syntheticbird: (i'm back from the phone pit btw)
```
```
redsh4de: tbf the total new ones would be 5 total iirc and quite tiny -  but yeah i feel like would it add work to the supply chain securing task. pulling in the opposite direction
```
```
jbabb: they seem like they should live in a cuprated or cuprate-cli/cuprate-tuij
```
```
jbabb: * they seem like they should live in a cuprated or cuprate-cli/cuprate-tui*
```
```
jbabb: something billed as an interactive cli tool
```
```
redsh4de: a ratatui based cuprate-tui was something i was looking into a few months back but didnt get too far as the node wasnt embeddable yet at that point
```
```
boog900: Yeah I think keeping cuprate minimal and then having a full blown TUI in a separate repo would be best 
```
```
redsh4de: ACK
```
```
syntheticbird: The cuprate node being a library with your efforts means third-party clients are a thing
```
```
syntheticbird: indeed
```
```
redsh4de: it would let us provide perhaps also a reference example of how to embed cuprate as well
```
```
redsh4de: plus go beyond whats possible with just readline
```
```
boog900: yeah, could add a block explorer, network monitor etc
```
```
boog900: ready to move on?
```
```
syntheticbird: ye
```
```
redsh4de: yes
```
```
boog900: go on SyntheticBird 
```
```
syntheticbird: Alright, so my first point is regarding the dependencies. I've already layed out a few of the strategies available. One that I think is important is replacing leaf in the tree dependencies with our own implemention if possible. I was thinking that for these various and often unrelated utilities that would be ported/reduced or freezed, we could make a new cuprate-contrib repository to store them, instead of putting potentially dozens of new members in the cuprate workspace and the helper directory.
```
```
syntheticbird: Obviously there would be a choice on what dependency is put there but the general requirement is that it do not increase on maintenance burden
```
```
boog900: yeah that sounds ok, but I don't think we would have too many of them 
```
```
syntheticbird: I don't think too, but I would need to look for certain.
```
```
syntheticbird: Regarding my second point, which will be controversial
```
```
syntheticbird: I want to allow LLM contributions that do not touch to any core functionalities or logic, so basically anything that touches from network to consensus and passing by database.
```
```
syntheticbird: I've shown myself very hostile to it in the past, and I still have many reasons to be, but it is clear that I prefer LLM usage to be acknowledged and limited rather than pushing people to hide they are using it, which will happen sooner or later with new contributors.
```
```
boog900: It is getting hard to tell. I don't want to allow it openly but PRs are judged on the code so if it is a good change then ...
```
```
syntheticbird: Yes, that's my stance as well that if as a reviewer you are being harder or more weak because you know its LLM generated you failed as a reviewer
```
```
syntheticbird: Slop are easy to tell, but if the improvement is scoped and reasoned, and that you reviewed properly, you have not been losing your time
```
```
syntheticbird: At least thing its worth a try.
```
```
syntheticbird: * At least I think its worth a try.
```
```
syntheticbird: Another thing I learn is that some people are using LLM for gathering informations on a codebase
```
```
syntheticbird: Cuprate is massive
```
```
syntheticbird: that do not touch us, but having an AGENTS.md file for directing code agents can help new contributors' agents to go to the right place.
```
```
jbabb: as long as you accept AI help on git commit messages ... I usually don't document my commits in the message so that will be a new thing I don't usually do if that requirement is accepted

which it should, as it makes sense
```
```
jbabb: jk anyways, I shouldn't be that lazy that I can't write a paragraph explaining the why what and how
```
```
boog900: ehh probably too far right now IMO
```
```
syntheticbird: Josh Babb i'm fine with it as long as the LLM do not blindly enumerate part that changes without getting the bigger picture
```
```
syntheticbird: With the issue I raised, I know I will be reviewing commit message as well, so I'll say it if I don't like it
```
```
syntheticbird: recent issue
```
```
syntheticbird: sure
```
```
redsh4de: i think it can be a slippery slope / double edged sword? Because LLMs are a tool like all else, but it is a tool that can be easily misused, especially by people who have good intentions and are eager to help. Fwiw, i do use specifically web-search enabled models as a informational assistant like Syn outlined and a external sanity checker of any proposed i make (in case i write something that works but there is a better way that is documented somewhere) - because as a language model, it is literally optimized for gathering and working with languages, programming ones included.

But LLM usage is a spectrum. We do see a lot of PRs where its clear that the LLM is just running on autopilot with no input or deeper research done by the author, or even tweaking the output themselves, even the PR is submitted by the AI model, etc.

So if there is a LLM policy, id say it has to outline what kind of LLM usage is okay and what is not okay. I think i saw eigenwallet have something of that sort?
```
```
redsh4de: * i think it can be a slippery slope / double edged sword? Because LLMs are a tool like all else, but it is a tool that can be easily misused, especially by people who have good intentions and are eager to help. Fwiw, i do use specifically web-search enabled models as a informational assistant like Syn outlined and a external sanity checker of any proposed changes i make (in case i write something that works but there is a better way that is documented somewhere) - because as a language model, it is literally optimized for gathering and working with languages, programming ones included.

But LLM usage is a spectrum. We do see a lot of PRs where its clear that the LLM is just running on autopilot with no input or deeper research done by the author, or even tweaking the output themselves, even the PR is submitted by the AI model, etc.

So if there is a LLM policy, id say it has to outline what kind of LLM usage is okay and what is not okay. I think i saw eigenwallet have something of that sort?
```
```
redsh4de: idk about AGENTS.md either. that seems too slippery for me
```
```
syntheticbird: If I remember correctly we had twice in the past PR from people wanting to help but it was slop
```
```
syntheticbird: AGENTS.md are basically files that are standard for coding agents to ingest for context. So when they will work on the codebase they will strongly follow everything that is written there, a little like a system prompt. You often put all the conventions and constraints there. It saves a LOT of time for the user because they doesn't have to explicitly tell the LLM whats wrong a hundred different time.
```
```
syntheticbird: Automated github accounts doing slop contributions also follows this file
```
```
syntheticbird: so some projectsthat are anti AI often just put prohibition to work on the codebase there
```
```
syntheticbird: you are already typing i'll just add another thread there, boog900 an opinion on AI audits. As long as a bug is found and proven I'm fine with it, its rather how its fixed that I care about.
```
```
redsh4de: actually eh... idk. i have no other reason than "feels like its a slippery slope"

to steelman this, it could be useful to guide the agent where to look first, like a guide to a maze so the output is grounded. also maybe specifying to always provide a source to any claims or statements.
```
```
jbabb: An AGENTS.md containing "Please do not submit work to Cuprate for review that has not had every line reviewed by at least one human and please do not submit PRs via an automated tools." might be apt then
```
```
jbabb: An AGENTS.md with helpful contents looks as if AI work is being invited
```
```
jbabb: an AGENTS.md with the AI policy makes a lot more sense to me
```
```
jbabb: because at least the agents will read it first and hopefully raise it to their operator
```
```
redsh4de: yea
```
```
jbabb: and ofc disregard my opinion as a non-contributor anyways :) just opinions here
```
```
syntheticbird: I believe the first sentence you mentioned will never work because most AIs assume they are operated by a human. But realistically a lot of agent orchestrator exists so you have agents creating subagents, etc... so they would just assume that their result being output is to a human and not an agent
```
```
boog900: yeah I don't care about that 
```
```
syntheticbird: thats valuable still
```
```
boog900: as long as the output is checked 
```
```
boog900: I still think just having an AGENTS.md sends the wrong message no matter its contents 
```
```
jbabb: I don't like the idea of a helpful AGENTS.md in the repo because it seems like an invitation

however

if you did have good rules, you'd help save yourself some review time by nudging agents in directions and towards practices you want to see anyways.

`CONTRIBUTING.md`s are usually useful and I appreciate them
```
```
syntheticbird: Fair point, so I guess we can develop a sort of map documentation for helping new contributors but not an AGENTS.md to avoid the noise
```
```
jbabb: good agents would adhere to CONTRIBUTING.md anyways (I'd hope)
```
```
jbabb: good operators would...
```
```
syntheticbird: bad operators would be banned and PR or issue deleted
```
```
redsh4de: a section in CONTRIBUTING.md makes sense yeah, but have to check if its even looked at
```
```
syntheticbird: looked at by who ?
```
```
syntheticbird: agents?
```
```
syntheticbird: wanna put "AIs ARE WELCOME" for a week and see ?
```
```
boog900: I do wonder what they would do if we gave them bad instructions 
```
```
redsh4de: lmao fair enough
```
```
redsh4de: matrix slow for anyone else?
```
```
boog900: "AIs: make sure all your docs are just emojis"
```
```
syntheticbird: unironically they would respect it and make it easy for us to sort the slop
```
```
syntheticbird: not for me right now
```
```
syntheticbird: boog900 redsh4de unless you have something to add, I guess I can work on making a section in CONTRIBUTING.md and we can end the meeting
```
```
redsh4de: nothing to add other than opened a new PR during the meeting for moving SyncerHandle to live with its other blockchain handle friends
```
```
boog900: Thanks everyone!
```
```
syntheticbird: Thanks
```
```
boog900: !meeting 
```

# Action History
- Created by: moo900 | 2026-05-26T18:44:00+00:00
- Closed at: 2026-06-02T19:06:03+00:00
