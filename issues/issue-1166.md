---
title: 'Cuprate Meeting #46 - Tuesday, 2025-03-11, UTC 18:00'
source_url: https://github.com/monero-project/meta/issues/1166
author: moo900
assignees: []
labels: []
created_at: '2025-03-04T19:20:18+00:00'
updated_at: '2025-03-11T19:17:56+00:00'
type: issue
status: closed
closed_at: '2025-03-11T19:17:55+00:00'
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

Previous meeting: #1161

# Discussion History
## moo900 | 2025-03-11T19:17:55+00:00
## Meeting logs
```
boog900: 1) greetings 
```
```
m-relay: <p​lowsof> 👋
```
```
m-relay: <u​ncle_rae> salaam
```
```
hinto: hello
```
```
boog900: 2) updates
```
```
boog900: Worked on getting the last PRs ready for release and reviewed 355
```
```
boog900:  * Me: Worked on getting the last PRs ready for release and reviewed 355
```
```
hinto: me: opened https://github.com/Cuprate/cuprate/pull/165 for review, will likely finish the rest of the `v0.0.1` release PRs today
```
```
fluorescent_beige: Working on #209
```
```
boog900: 3. Project: What is next for Cuprate?
```
```
boog900: Well we defiantly missed our very unmovable deadline lol
```
```
boog900: hinto: dose that mean `v0.0.1` today?
```
```
hinto: if 165 + 370 + 391 are merged today / tomorrow morning then high likelihood for releases starting tomorrow
```
```
boog900: nice
```
```
hinto: tagging + verification + signatures + changelog is what is left after the PRs
```
```
boog900: is there anything you want to discuss about those PRs in this meeting?
```
```
syntheticbird: Hello 
```
```
syntheticbird: me: Opened my CCS proposal for working on Cuprate tor/arti integration in the next two months
```
```
syntheticbird: (I'm on phone so might be slow to answer)
```
```
boog900: https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/564
```
```
boog900: I will give that a thumbs up on GitLab soon
```
```
rucknium: Boog900 (Backup): You may want to read Biryukov &Pustogarov (2015) "Bitcoin over Tor isn't a good idea" https://arxiv.org/abs/1410.6079   https://dl.acm.org/doi/10.1109/SP.2015.15
so you know potential issues with the protocol.
```
```
syntheticbird: > <@rucknium:monero.social> Boog900 (Backup): You may want to read Biryukov &Pustogarov (2015) "Bitcoin over Tor isn't a good idea" https://arxiv.org/abs/1410.6079   https://dl.acm.org/doi/10.1109/SP.2015.15
> so you know potential issues with the protocol.

I was aware of issues regarding blockchain downloading over Tor but didn't managed to retrieve the information I saw years ago. Will read attentively thx
```
```
spirobel: this is also why scanning QR codes from you phone while using the tor browser is a bad idea
```
```
spirobel: unsure it relates to backup boogs aka synbirds work
```
```
boog900: the plan currently is just to copy what monerod does over Tor
```
```
boog900: We wont be extending it by allow sync using onion addresses for example 
```
```
rucknium: Boog900 (Backup): Maybe also check the papers that cite that one, since it is over 10 years old and possibly out of date. The acm.org link has its citations.
```
```
spirobel: the article is more concerned with wallet user security and compartmentalization what is the possible relationship to node software? 
```
```
spirobel: why not?
```
```
hinto: maybe the changelog formatting in 370? I am defaulting to something similar to `monero-project` releases
```
```
boog900: because it is easier to sybil than clearnet, monerod doesn't even allow IPv6
```
```
rucknium: > <@spirobel:kernal.eu> the article is more concerned with wallet user security and compartmentalization what is the possible relationship to node software?

It discusses node issues, too. Especially sybil/eclispse
```
```
rucknium: > The man-in-the-middle attack exploits a Bitcoin built-in reputation based DoS protection and the attacker is able to force specific Bitcoin peers to ban Tor Exit nodes of her choice. Combining it with some peculiarities of how Tor handles data streams a stealthy and low-resource attacker with just 1-3% of overall Tor Exit bandwidth capacity and 1000-1500 cheap lightweight Bitcoin peers (for example, a small Botnet) can force all Bitcoin Tor traffic to go either through her Exit nodes or through her peers. This opens numerous attack vector.
```
```
spirobel: ah because the cost to get an IP is higher than getting a tor hidden service address. So we would need to have some kind of system where there is a cost to creating addresses to make it feasible 
```
```
spirobel: roger
```
```
syntheticbird: Yeah sorry if my response to Rucknium were confusing, I weren't planning on implementing block relay over Tor, we're solely replicating monerod behavior.
```
```
hinto: Rucknium: I added an FAQ section to the user book and tried to cover the topics you brought up: https://hinto-janai.github.io/cuprate-user-book/#faq
```
```
syntheticbird: * Yeah sorry if my response to Rucknium were confusing, I weren't planning on implementing block relay over Tor, we're solely replicating monerod behavior. The information I encountered were regarding downloading blocks from clearnet nodes over Tor specifically.
```
```
rucknium: hinto: Thanks!
```
```
syntheticbird: FAQ lgtm
```
```
syntheticbird: nice job
```
```
boog900: > <@hinto:monero.social> maybe the changelog formatting in 370? I am defaulting to something similar to `monero-project` releases

yeah I think it would be good to set up a changelog for every crate, or have a changelog for all crates 
```
```
boog900: not just the binaries 
```
```
boog900: A change per crate is better for devs but is a pain if a change spans many crates 
```
```
boog900:  * A changelog per crate is better for devs but is a pain if a change spans many crates 
```
```
syntheticbird: I agree with hinto I prefer something similar to `monero-project` releases
```
```
hinto: currently the setup is `misc/changelog/$CRATE/$VERSION` which only holds `cuprated/0.0.1.md` right now
```
```
boog900: oh wait it's in `misc`, I though it was in `binaries`
```
```
boog900:  * oh wait it's in `misc`, I thought it was in `binaries`
```
```
boog900: my bad
```
```
boog900: in which case I would rather the changelog be in the crate folder 
```
```
hinto: a combined changelog for all crates would be much easier
```
```
boog900: or that
```
```
spirobel: is there a timeline yet for publishing some of the crates? I import cuprate a subtree currently for the epee parsing and encoding. 
```
```
spirobel: * is there a timeline yet for publishing some of the crates? I import cuprate as a subtree currently for the epee parsing and encoding. 
```
```
boog900: I guess we publish on release so pretty soon
```
```
spirobel: change logs for some of the crates that wallets  / ( maybe monero oxide in the future?) depends on would be good
```
```
boog900: hinto: A combined file might get annoying if the versions get out of sync 
```
```
spirobel: but I see its less work to just do it for many crates at once especially when changes span many crates
```
```
spirobel: * (but I see its less work to just do it for many crates at once especially when changes span many crates)
```
```
boog900: change log per directory?
```
```
boog900: not many changes should span multiple directories anymore 
```
```
boog900: I wouldn't have thought anyway
```
```
spirobel: combined changelogs for the bin + changelogs for crates that are actively used / useful for other projects ( wallets etc)
```
```
syntheticbird: couldn't someone just check out `git` history in between two tags and check out the crate as a keyword ? or something similar based on area of diffs? A changelog per crate sounds... clumsy
```
```
spirobel: its just nice as a consumer of a library to quickly read what changed. similar to how it is nice as a user of the binary to read what changed. 
```
```
spirobel:  / which new features got added
```
```
spirobel: its not a big deal or super urgent, just a nice touch. (asides from breaking changes that require attention lol )
```
```
boog900: We are probably going to split the single file into crate sections anyway
```
```
boog900: otherwise tracking versions is going to be annoying/weird
```
```
boog900: anything else anybody wants to discuss today?
```
```
hinto: The changelog/release scheme can change in the future although for now I think this makes sense:
- 1 release tag "type", `cuprated-$VERSION` over `$VERSION` in-case `cuprate-lib-$VERSION` is needed
- Combined changelog, i.e. `cuprated` changes, `cuprate_library` changes, etc, like: https://github.com/Cuprate/cuprate/blob/7d35f4327f7445f1d4444d20f89cf6b17d17339e/misc/changelogs/cuprated/0.0.1.md

Also some questions that need answers:

- Who is responsible for updating changelogs on libraries (how/can/will it be enforced?)
- What do `Cuprate/cuprate` releases contain, a `cuprated` release? A library release?
```
```
hinto: for now the answer for the last question seems to be: whenever there is a new `cuprated` version, like `reth` or `zebra`
```
```
boog900: > Who is responsible for updating changelogs on libraries (how/can/will it be enforced?)

part of the requirements to merge a PR?
```
```
boog900: > What do Cuprate/cuprate releases contain, a cuprated release? A library release?

`cuprated` I think
```
```
boog900: no need to put crate releases there too IMO
```
```
boog900: anything else to discuss?
```
```
boog900: ok I think we can end here
```
```
boog900: thanks everyone!
```
```
hinto: future discussion on publishing rules for certain libraries would be beneficial
```
```
hinto: there's also crates.io to talk about
```
```
hinto: thanks
```

# Action History
- Created by: moo900 | 2025-03-04T19:20:18+00:00
- Closed at: 2025-03-11T19:17:55+00:00
