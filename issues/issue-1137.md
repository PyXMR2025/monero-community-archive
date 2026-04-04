---
title: 'Cuprate Meeting #38 - Tuesday, 2025-01-14, UTC 18:00'
source_url: https://github.com/monero-project/meta/issues/1137
author: moo900
assignees: []
labels: []
created_at: '2025-01-07T20:04:40+00:00'
updated_at: '2025-01-14T19:09:03+00:00'
type: issue
status: closed
closed_at: '2025-01-14T19:09:03+00:00'
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

Previous meeting: https://github.com/monero-project/meta/issues/1129

# Discussion History
## moo900 | 2025-01-14T19:09:02+00:00
## Meeting logs
```
boog900: meeting time: https://github.com/monero-project/meta/issues/1137
```
```
boog900: 1) greetings
```
```
syntheticbird: Hello
```
```
hinto: hello
```
```
boog900: 2) updates 
```
```
boog900: me: I left a review on hinto's RPC PR. I have also been working on improving the consensus API, which is going to be needed to add fast-sync and probably relay rules.
```
```
syntheticbird: me: changed my pgp key
```
```
hinto: me: still working on the roadmap 2025 CCS.

The document's scope is getting quite large and is turning into something resembling a company's quarterly/annual statement. I think doing it like this via the CCS is a good opportunity to clearly communicate developments and future plans. I plan on posting a draft this week and will ask for some opinions on it since it also implicitly contains a value hierarchy (via the roadmap/goals) on what is important / what should be focused on in Cuprate, which I think should be decided by multiple people / stakeholders.

I also plan on posting on /r/Monero and using this document to aid in briefing the wider community what Cuprate is, because I don't think it's too well known yet. Perhaps an article on https://getmonero.org would be good too.
```
```
hinto: other than that, I am preparing on getting an alpha `cuprated` ready within the next ~3 months, e.g. release notes, release CI checks, etc. boog900 did you have any thoughts on this? I would be willing to lay out a formal document on what our release cycles will look like, and perhaps you could do the actual releases.
```
```
syntheticbird: > I also plan on posting on /r/Monero and using this document to aid in briefing the wider community what Cuprate is, because I don't think it's too well known yet. Perhaps an article on https://getmonero.org would be good too.

100% Agree. The second we've stopped reddit updates everyone except usual matrix users forgot about us
```
```
syntheticbird: tho there is a cuprate.org blog post update planned. Might be good to wait for it then post on reddit
```
```
hinto: I personally think a 6-week release cycle resembling Rust is a good precedent to follow: https://rust-lang.github.io/rustup/concepts/channels.html. If automation/workflows are created (I willing to do this), this shouldn't be too much of a hassle.
```
```
syntheticbird: I think it's too much. 6 weeks is relatively annoying for rolling distributions so even more for casual users (i don't expect cuprate to be packaged on freezing distros). I would prefer between 8 to 12 weeks
```
```
boog900: sounds good I am excited to see what you have so far, also agree a lot of community members still probably don't know what Cuprate is. 

As something symbolic it would be good to get the alpha binary out in February as that is Cuprate's 2 year birthday.
```
```
syntheticbird: 23 february iirc
```
```
syntheticbird: first commit
```
```
boog900: I did also think about not giving out binaries for the alpha binary, requiring people to build themselves. It provides a nice barrier to entry so only people actually willing to build can run Cuprate.
```
```
ack-j: Hi
```
```
hinto: worth noting zebra also follows a 6-week cadence, one of the advantages is that small incremental PRs / improvements are included on a more regular basis and the general philosophy of continual integration, i.e. releases aren't scary because they happen frequently - I haven't thought too deeply on this though, just bringing it up
```
```
hinto: Cuprate is only ~1 year old in my mind since that's when paid development started happening :)
```
```
ack-j: I’m excited to run the alpha and see how this project has progressed so far
```
```
syntheticbird: we are too buddy
```
```
hinto: zebra also does this, no binaries, only build instructions and a docker image
```
```
syntheticbird: fwiw we can have some delay between alpha to stable to resolve reproducible build maybe
```
```
hinto: I've also considered not releasing binaries in case `cuprated` exposes major network problems, no binaries would a hacky but real limiter to that problem
```
```
hinto: or if `cuprated` itself is the issue
```
```
syntheticbird: The `what is important / what should be focused on in Cuprate` is going to be interesting discuss (to re discuss in an extent).
```
```
boog900: yeah we will need to stress that alpha means don't trust with anything critical 
```
```
rucknium: Zcash has a different release philosophy. At least with the old C++ zcashd, old releases had an intentional killswitch after their "expiration date" even without a hard fork. Just to put it in context.
```
```
boog900: Oh yeah that was another idea, we could put a killswitch in the alpha binary to force people to update.
```
```
boog900: 3) Project: What is next for Cuprate?
```
```
boog900: hinto: do you think the alpha binary will include RPC?
```
```
hinto: I don't think it needs to although if it does, probably a small subset of methods/endpoints that don't panic on trivial input
```
```
hinto: Although I guess it depends on how loose an alpha build can be, an argument could be made to just enable everything from the beginning even if it panics
```
```
syntheticbird: I would prefer the former over the latter
```
```
boog900: yeah ngl I would be fine just including them with it documented somewhere which methods are safe 
```
```
syntheticbird: ah yes disagree
```
```
syntheticbird: well ig im ok with both
```
```
boog900: no one should be exposing this publicly _yet_
```
```
hinto: Ok, I want to have the User Book somewhat available alongside the initial release, there is an RPC section there that could have some information: https://hinto-janai.github.io/cuprate-user-book/rpc/intro.html
```
```
boog900: and if anyone does they risk giving out invalid data to unsuspecting people through potential bugs in Cuprate 
```
```
syntheticbird: I would have preferred the latter because think including all endpoints might just lead to 1. Having difficulty keeping track of which methods are unsafe and what are known needing to be fixed 2. Probably a few are going to make a  bug report about it.

But the User Book seems good to resolve that
```
```
boog900: hinto: actually it should be pretty easy to just not include them with axum right?
```
```
hinto: this can be somewhat enforced by only allowing RPC to bind on `localhost:18081`
```
```
boog900: just don't add them to the server 
```
```
boog900:  * just don't add the methods to the server 
```
```
syntheticbird: sgtm
```
```
syntheticbird: would prefer this
```
```
hinto: `cuprate_rpc_interface` makes it very simple https://doc.cuprate.org/cuprate_rpc_interface/struct.RouterBuilder.html#example
```
```
boog900: ok I would just not include them if it is very easy
```
```
syntheticbird: So alpha with limited RPC ?
```
```
syntheticbird: or just an assumption and we will see what is available at anniversary date?
```
```
hinto: adding the RPC server to `cuprated`'s main will look something like: https://github.com/Cuprate/cuprate/blob/cebb71d7dccb9f7cf66293ea487e20bb29530e8c/rpc/interface/README.md?plain=1#L119-L136
```
```
hinto: it's only a few lines, then a few chained methods to enable/disable method/endpoints
```
```
boog900: the anniversary date is not set in stone FWIW it's juts a nice target, if we can get all RPC methods working by waiting a week I would want to wait.
```
```
syntheticbird: ok
```
```
boog900: anything else anyone wants to discuss today?
```
```
hinto: I've been thinking about learning Guix to help tobtoht with monero-core PRs, specifically to move FCMP++ along
```
```
hinto: could it be argued that getting FCMP++ live on `monerod` is more important than `cuprated` (for the time being)?
```
```
syntheticbird: Yes absolutely, it can be argued. You are free to help monerod.
```
```
syntheticbird: If you learn Guix I suppose it would maybe profit cuprate regarding reproducible build
```
```
boog900: yeah I agree 
```
```
hinto: this does mean development on `cuprated` will slow down most notably RPC integration
```
```
syntheticbird: When would you start helping toboth_ ?
```
```
syntheticbird: before alpha release or just after?
```
```
syntheticbird: * When would you start helping tobtoht\_ ?
```
```
hinto: yeah I'm not sure about the timing although I assume if it is deemed worth it to have another Guix reviewer (not sure if this is the case yet) then it would be beneficial for me to spend some time learning it before FCMP++ integration in `monerod` is done
```
```
hinto: I think I can continue on `cuprated` for the time being, enough for an alpha build + release cycle set in place, user book, and maybe some RPC?
```
```
syntheticbird: sounds good to me
```
```
syntheticbird: would you allow minor PRs to the RPC part while helping monerod? or would you prefer freezing it until you come back
```
```
hinto: it should move on without me if necessary, although I think I can at least review things
```
```
syntheticbird: ok 👍️
```
```
boog900: anything else to discuss today?
```
```
boog900: I think we can end here thanks everyone!
```
```
hinto: thanks
```
```
syntheticbird: thanks
```

# Action History
- Created by: moo900 | 2025-01-07T20:04:40+00:00
- Closed at: 2025-01-14T19:09:03+00:00
