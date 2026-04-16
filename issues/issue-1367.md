---
title: 'Cuprate Meeting #98 - Tuesday, 2026-04-14, UTC 18:00'
source_url: https://github.com/monero-project/meta/issues/1367
author: moo900
assignees: []
labels: []
created_at: '2026-04-07T18:45:43+00:00'
updated_at: '2026-04-14T18:38:23+00:00'
type: issue
status: closed
closed_at: '2026-04-14T18:38:22+00:00'
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

Previous meeting: #1364

# Discussion History
## moo900 | 2026-04-14T18:38:23+00:00
## Meeting logs
```
boog900: 1) greetings
```
```
redsh4de: hi!
```
```
hinto: hello
```
```
boog900: 2) updates
```
```
SyntheticBird: Hi
```
```
boog900: I made a lot of progress on the RPC last week, I think all the endpoints needed for wallets are working enough for full wallet support.
```
```
boog900: I have also made a tx fully with cuprated and the CLI wallet
```
```
redsh4de: Submitted three smaller issue closing PRs:
parsing proxy URL: https://github.com/Cuprate/cuprate/pull/596
broadcast block before txpool notif: https://github.com/Cuprate/cuprate/pull/597
support for alt-blocks in txs_in_block: https://github.com/Cuprate/cuprate/pull/599
```
```
hinto: me: reviewed 587, preparing `cuprated v0.0.9`, I think we can release this week
```
```
SyntheticBird: I have continued looking at the tapes PR focusing first and foremost on storage crates but I didn't have the time to go elsewhere. I don't have any comments to submit yet.
```
```
boog900: 3) Project: What is next for Cuprate?
```
```
SyntheticBird: also reviewed a PR from redsh4de
```
```
hinto: or perhaps we wait to release?
```
```
hinto: seems like RPC changes can be included as well
```
```
boog900: We _could_ but I want to test it a lot first
```
```
boog900: So I think I would rather put out just the tapes for now
```
```
Josh Babb: I can help test.  these are old undisclosed crates but what's new is I've been using cuprate-regtest to make cuprate-simnet and monero-simnet as alternatives to shadowformonero/monerosim for playing around with xmr and wownero.  https://github.com/sneurlax/xmr-wow/tree/main/deps/cuprate-simnet and https://github.com/sneurlax/xmr-wow/tree/main/deps/monero-simnet

but still the old db version
and dirty

will need to move to new db and clean just sharing ~things~
```
```
redsh4de: planning to work on resolving a FIXME i stumbled upon in PR 597, regarding using the KI map from the consensus crate instead of recomputing from inputs. rough idea is to add an Arc for spent_key_images in VerifiedBlockInformation, so callers can just clone the list and then pass it onto txpool for notifs
```
```
Josh Babb: basically wanted to make a shadowformonero/monerosim that used cuprate instead of monerod.
```
```
boog900: thanks, I'll let you know when I push the changes
```
```
SyntheticBird: huge undertaking. Wishing you success
```
```
hinto: I forgot to mention in the review but should the connection count default be lower? If not then our minimum memory spec will be higher
```
```
hinto: assuming wallet sync + active RPC connections I think we need some leeway as well
```
```
boog900: Yeah I'll lower it a bit
```
```
boog900: has your node OOMed since?
```
```
hinto: it was stable for a week+, I'm currently re-syncing 0.0.8 to get better comparison numbers
```
```
boog900: nice
```
```
boog900: is there anything anyone else wants to discuss?
```
```
Josh Babb: just more thanks to all cuprate contributors
```
```
boog900: Thank you!
```
```
boog900: I think we can end here
```
```
boog900: Thanks everyone!
```
```
SyntheticBird: thank you all
```

# Action History
- Created by: moo900 | 2026-04-07T18:45:43+00:00
- Closed at: 2026-04-14T18:38:22+00:00
