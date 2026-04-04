---
title: 'Cuprate Meeting #9 - Tuesday, 2024-06-25, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1028
author: moo900
assignees: []
labels: []
created_at: '2024-06-24T15:13:19+00:00'
updated_at: '2024-06-25T20:04:33+00:00'
type: issue
status: closed
closed_at: '2024-06-25T19:25:23+00:00'
---

# Original Description
[Cuprate](https://github.com/Cuprate/cuprate) is an effort to create an alternative Monero node implementation.

Location: [Libera.chat, #cuprate](https://libera.chat/) | [Matrix](https://matrix.to/#/#cuprate:monero.social?via=matrix.org&via=monero.social)

Note that there are currently communication issues with Matrix accounts created on the matrix.org server, consider using a different homeserver to see messages.

[Join the Monero Matrix server if you don't already have a Matrix account](https://www.getmonero.org/resources/user-guides/join-monero-matrix.html)

Time: 18:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html)

Moderator: @boog900

Please comment on GitHub in advance of the meeting if you would like to propose a discussion topic.

Main discussion topics:

- Greetings
- Updates: What is everyone working on?
- Project: What is next for Cuprate?
- Any other business

Previous meeting with logs: #1024

# Discussion History
## moo900 | 2024-06-25T19:25:22+00:00
## Meeting logs

```
boog900: meeting time! https://github.com/monero-project/meta/issues/1028
```

```
boog900: 1) Greetings 
```

```
hinto: hello
```

```
boog900: lets hope the bot works :)
```

```
yamabiiko: Hi
```

```
boog900: lets move onto: 
```

```
boog900: 2) Updates: What is everyone working on?
```

```
boog900: Me: I have mainly been working on changes to our P2P crates API, trying to make them simpler and easier to use 
```

```
hinto: me: working on a proposal for `benches/`, still working on RPC types, and opened the DB split for review (#160)
```

```
hinto: also I made a bot, say hi moo 
```

```
hinto: !status
```

```
moo: moo v0.0.3, 0c8e09ea68787263f6ef799e3683ff2d9190ec09 (release), meeting: true, uptime: 6 minutes, 48 seconds
```

```
yamabiiko: I am ready to start contributing in a consistent manner and I am looking for what would be best to work on
```

```
boog900: Seems like a good point to move onto: 
```

```
boog900: 3) Project: What is next for Cuprate?
```

```
boog900: The next major task that no one is working on would be ZMQ, however IMO it might be best to start with something smaller.
```

```
yamabiiko: Does it make sense to split some work for the RPC interface? 
```

```
yamabiiko: At the very least, I think I can review the related PRs 
```

```
boog900: Probably not possible since hinto has an open CCS to work on it 
```

```
kayabanerve: 👋
```

```
boog900: For my next CCS I am planning to work on the `cuprated` binary. I recently opened a few issues that do need to fixed if you like the look of any of them?
```

```
hinto: > <@hinto:monero.social> boog900 kayabanerve: it would be helpful to open an issue on `monero-serai` usage in Cuprate and maybe spend some meetings on it, I'm not sure #191 would be a good long-term solution

I thought about #191 a bit more, and I think it may actually be good for both Cuprate/Serai (at least in the medium-term). It allows:

1. Serai to have more control over `monero-serai`, so fixes/changes can be made with less bureaucracy
2. Cuprate to choose its own API and expose things from `monero-serai` it needs and/or add things that `monero-serai` doesn't need

boog900: hopefully by now you know I'm debt-adverse (wrappers instead of upstream types), but figuring out proper governance over `monero-serai` may take a while. Since there's a bunch of stuff left that Cuprate has to do and not too many resources, it may be more beneficial in the long run if we go with something like #191. The downsides are the extra maintenance and worse debugging.
```

```
yamabiiko: > <@boog900:monero.social> For my next CCS I am planning to work on the `cuprated` binary. I recently opened a few issues that do need to fixed if you like the look of any of them?

Sounds good, I can def start looking at those
```

```
kayabanerve: If anyone is unaware, the modern monero-serai has no wallet code at all.
```

```
kayabanerve: Eh. monero-clsag has prove and multisig signing under a feature.

If prove algorithms count as wallet code, that doesn't entirely hold true.
```

```
kayabanerve: I point that out as I don't expect Cuprate to not need anything still with monero-serai (barring prove fns and associated structs).
```

```
hinto: yamabiiko: review on any PRs are welcome btw, but yes my current CCS covers all of the RPC interface (not the inner handlers though)
```

```
yamabiiko: I think it'll be easier for me to review the RPC ones as I'm more context aware due to the previous design work
```

```
yamabiiko: But I'll also look to get more involved with the P2P side, with the issues boog opened 
```

```
hinto: Btw I mean #191 + our current fork setup, our wrappers would be using a specific commit rather than upstream and update when needed, ideally while not breaking our wrapper API
```

```
boog900: > <@hinto:monero.social> I thought about #191 a bit more, and I think it may actually be good for both Cuprate/Serai (at least in the medium-term). It allows:

1. Serai to have more control over `monero-serai`, so fixes/changes can be made with less bureaucracy
2. Cuprate to choose its own API and expose things from `monero-serai` it needs and/or add things that `monero-serai` doesn't need

boog900: hopefully by now you know I'm debt-adverse (wrappers instead of upstream types), but figuring out proper governance over `monero-serai` may take a while. Since there's a bunch of stuff left that Cuprate has to do and not too many resources, it may be more beneficial in the long run if we go with something like #191. The downsides are the extra maintenance and worse debugging.

I agree, If I am honest I don't really like some of the new monero-serai API (mainly the new tx enum) 
```

```
boog900: I don't really think it is as helpful to Cuprate which needs to always match monerod  
```

```
boog900: IMHO it makes it harder to check they match
```

```
boog900: so isolating that API would be beneficial  
```

```
hinto: Another thing: I think this approach is a little selfish, I think at least _some_ of the maintenance burden of `monero-serai` should be placed on Cuprate, although figuring this out practically is hard which is why #191 is only a medium-term solution IMO
```

```
kayabanerve: boog900: Suggestions welcome.
```

```
boog900: The thing is trying to change the API post 1.0 isn't going to happen,
```

```
kayabanerve: I wanted to remove panics in RctPrunable/Transaction. The main way to do that is to use errors on attempting to serialize invalid structs. That requires serialize, which returns a Vec u8, return an Option Vec u8 as writing to a Vec u8 can now fa.
```

```
boog900:  * The thing is trying to change the API post 1.0 is probably not going to happen,
```

```
kayabanerve: (It's infallible if solely propagating errors from the Write impl)
```

```
kayabanerve: *can now fail
```

```
kayabanerve: The next option was to remove RctPrunable::Null. That actually keeps most of the integrity of the ringct code. It also forces using Option RctSignatures.
```

```
kayabanerve: For the transaction enum itself... There was one issue it resolved, and it resolved the not yet documented issue of a prefix version of 1 yet RctSignatures being Some.
```

```
kayabanerve: The options truly end up:
1) Unsafe structs (what we have)
2) Increased runtime errors
3) A garbage in, garbage out policy
4) Somewhat annoying structs
```

```
kayabanerve: *1 is what we had. 4 is what we have.
```

```
kayabanerve: There is a getter for the prefix. Getters for the proofs (Option Vec RingSignature, Option RctProofs) should remove the matching.
```

```
kayabanerve: (As yes, I've also been annoyed by that)
```

```
kayabanerve: But I can't abide option 1, tried option 2 and got a worse API, and hate option 3.

It's literally adding a bunch of undefined behavior.
```

```
boog900: I'll have to work on moving us over before I'll give any definite thoughts right now I am just very unsure  
```

```
kayabanerve: *I believe I can link the almost completed option 2, which I made a commit out of for posterity, to show why it's bad in practice.
```

```
boog900: I will prioritize this though 
```

```
kayabanerve: Sure. I'm not trying to defend this death, and sorry if I do sound a bit defensive. Just trying to explain it's a least bad option and I do need a better option to consider when faced with dislike of this one :/
```

```
boog900: not unsure of monero-serai, more so unsure of what option would be best 
```

```
kayabanerve: I'm not convinced those panics we had were unreachable in Cuprate BTW.
```

```
kayabanerve: Especially if y'all are now adding JSON RPC, and with it the ability to really mess with these fields.
```

```
kayabanerve: Sorry. Those two messages are out of order. Brief internet issue.
```

```
boog900: kayabanerve: do you have any more thoughts on moving monero-serai out of 
```

```
boog900:  * kayabanerve: do you have any more thoughts on moving monero-serai out of Serai?
```

```
boog900: to its own repo, personally I would like that. 
```

```
kayabanerve: I'm not inherently against moving to its own repo or its own organization, similar to the prior Rust Monero org (which is now largely dead).

I'd question the benefit of a new repo under Serai. Mind if I ask your elaboration there?
```

```
boog900: Mainly to show that it is its own project, maintained by Serai (if under that org). Pretty minor, I know, but probably better to do this now? 
```

```
boog900: It would also help having the issues, discussions and PRs for just monero-serai in one place  
```

```
kayabanerve: 🤔
```

```
kayabanerve: The README has said that from the start. I'd agree it *further* distinguish.
```

```
kayabanerve: No, that's the funny thing, it wouldn't.
```

```
kayabanerve: It'd break up the Serai monorepo. While the goal is to minimize Serai's influence on monero-serai, that doesn't change Serai reflects a real world use case *and* monero-serai depends on several crypto libs within it.
```

```
kayabanerve: Recently, I optimized the CLSAG algorithm by making a breaking change in FROST. That'd have been two PRs to distinct repos if monero-serai had its own repo.
```

```
kayabanerve: *the change largely made sense anyways. The CLSAG algorithm helped me realize it as the functionality I changed was added to be flexible enough to support algorithms like CLSAG.
```

```
kayabanerve: https://github.com/serai-dex/serai/commit/a25e6330bdd6d2f237d731c9229f971130899ad3 for reference
```

```
kayabanerve: I've also worked to remove dependency on our crypto libs. That doesn't change monero-clsag has the modular-frost dependency, and monero-wallet does too.

Then the question is raised does the monero-wallet tree stay under Serai or also move? I'd say also move, in order to keep it clear it's not solely for Serai, yet nonero-wallet further takes advantage of modular-frost.
```

```
kayabanerve: It's the exact fragmentation the monorepo is meant to prevent. I think I could only justify it if it had an effect on governance, and didn't just exist for promotional reasons.
```

```
kayabanerve: Also, I do tag all Monero items as Monero. That does also scrape in Serai things re: Monero, yet I'd be fine distinguishing the tags. That isn't meant to justify the thoughts above. Solely help you find Monero related items within Serai.
```

```
boog900: Yeah that is all fair, for Cuprate though to be so reliant on it when Serai will seemingly always have the upper hand by having it in Serai's monorepo doesn't put Cuprate in the nicest of positions if we disagree on changes  
```

```
kayabanerve: 1) That's why I'm proposing agreement on the 1.0 APJ at the least.
2) I'm not against a modern Rust Monero infrastructure.
```

```
boog900: I understand that moving it to a separate repo under Serai doesn't really change that, however it does pave the way to completely move it out of Serai and to an independent Org 
```

```
kayabanerve: I don't think the organizational change of splitting the monorepo for purpose clarity is sufficiently worthwhile.

Creation of a new governance structure may make it sufficiently worthwhile.
```

```
kayabanerve: *API, sorry.
```

```
kayabanerve: I'll rethink any organizational issues, as those should be minimized are can likely be eliminated if there's a modular-frost 1.0?

But I'd ask we either propose an independent org or table splitting the monorepo. Creation of a new repo will still require moving the history and issues, if within Serai or a new org, so it does that work now, but it doesn't set up less work overall.
```

```
hinto: FWIW I think an independent org sounds the healthiest long-term
```

```
hinto: medium-term, I think things staying the way they are now is the least work for all
```

```
kayabanerve: Largely agree. It'd need an organization and some policy documents yet shouldn't be infeasible in the long-term.
```

```
boog900: I agree 
```

```
kayabanerve: So would that just be agreement on a 1.0 API _and_ further understanding/minimization of linkages?
```

```
boog900: Yeah
```

```
boog900: Plus added testing which I may prioritize
```

```
boog900: Is there anything else people want to discuss? 
```

```
boog900: Ok I think we can end here
```

```
boog900: Thanks everyone!
```


# Action History
- Created by: moo900 | 2024-06-24T15:13:19+00:00
- Closed at: 2024-06-25T19:25:23+00:00
