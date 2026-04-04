---
title: 'Cuprate Meeting #39 - Tuesday, 2025-01-21, UTC 18:00'
source_url: https://github.com/monero-project/meta/issues/1140
author: moo900
assignees: []
labels: []
created_at: '2025-01-14T19:09:02+00:00'
updated_at: '2025-01-21T19:10:50+00:00'
type: issue
status: closed
closed_at: '2025-01-21T19:10:49+00:00'
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
- [Killswitch timestamp](https://github.com/Cuprate/cuprate/pull/365)
- Release cycle length
- Release versioning and naming

- Any other business

Previous meeting: #1137

# Discussion History
## moo900 | 2025-01-21T19:10:48+00:00
## Meeting logs
```
boog900: meeting time https://github.com/monero-project/meta/issues/1140
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
boog900: Me: I finished my work improving the consensus crates API
```
```
hinto: me: working on setting up everything related to releases and filling out the user-book. Still preparing the CCS and reddit post, I said this last time but I'm pretty sure this will be ready by this week.
```
```
boog900: soon™️
```
```
syntheticbird: seems implied but would appreciate a review of the ccs and discuss the reddit post more deeply before posting. I think there is a cooperation to be done here with the website blog.
```
```
boog900: 3. Project: What is next for Cuprate?
```
```
hinto: I am planning to post them here in draft status to gather opinions before publishing
```
```
boog900: - [Killswitch timestamp](https://github.com/Cuprate/cuprate/pull/365)
```
```
boog900: I am ok with the PR in its current form FWIW
```
```
syntheticbird: The testing period have not been discussed iirc
```
```
syntheticbird: how many days/weeks are letting alpha releases run
```
```
boog900: thats next discussion right?
```
```
syntheticbird: ah yeah probably
```
```
hinto: If we're setting the killswitch timestamp to a constant in the binary, it means it is tied in with our release schedule (there should be a new binary ready before the timestamp). I posted an issue with a set of rules and a schedule here: https://github.com/Cuprate/cuprate/issues/374. Under the current impl of the killswitch there are 2 parameters we need to figure out:
- RELEASE_CYCLE_WEEK_LENGTH
- KILLSWITCH_GRACE_PERIOD
```
```
hinto: I think we should discuss those 2 before the other points in that issue
```
```
syntheticbird: Regarding release cycle, I've already said prior that i'm not against 8 weeks
```
```
syntheticbird: 6 weeks is too short imo but 8 weeks is still reasonable
```
```
syntheticbird: As for the killswitch grace period, 1 or 2 weeks would be good
```
```
syntheticbird: we assume alpha users are trying to be up to date with new releases on their free time in the week-end
```
```
hinto: Other project's release cycles for reference:

- [Rust](https://endoflife.date/rust): 6 weeks
- [Linux](https://www.kernel.org/category/releases.html): 9-10 weeks
- [reth](https://github.com/paradigmxyz/reth/releases): ahhoc yet seems to be around every 4 weeks
- [zebra](https://github.com/ZcashFoundation/zebra/releases) adhoc yet seems to be around every 4-8 weeks
```
```
hinto: since the release cycle can be changed it at any time I don't think it matters too much what is selected now, as long as the killswitch timestamp lines up correctly and a cycle is eventually stabilized
```
```
boog900: I'm not sure if we should have the same policy while we are still building compared to when we are stable. IMO I don't think we should have an enforced release cycle for alpha, I can see us wanting to release before the 8 weeks.
```
```
syntheticbird: true
```
```
syntheticbird: so for alpha would a 4 week be good ?
```
```
boog900: and what even is a release going to be? just an announcement? people will build themselves  
```
```
syntheticbird: It's just a checkpoint for people to differentiate when it's just minor fixes to major changes required for alpha stage
```
```
hinto: actually I was thinking since a killswitch exists and the previous concerns were dealt with, that releasing alpha binaries would be okay
```
```
syntheticbird: I personally do not want to have to rebuild main branch at merge commit
```
```
syntheticbird: * I personally do not want to have to rebuild main branch at every merge commit
```
```
hinto: if an adhoc release approach is taken then the killswitch timestamp has to account for it, I think getting into the rhythm of releases early on would be a good idea too
```
```
syntheticbird: that kinda contradict with ^
```
```
syntheticbird: unless i missed something
```
```
syntheticbird: ah no my bad
```
```
syntheticbird: I missed boog's second part of his sentence
```
```
boog900: I just dont want to be in a situation where a good performance improvement is waiting many weeks for the scheduled 
```
```
syntheticbird: Yes, even for alpha following a release cycle would be good
```
```
syntheticbird: IMO, 
- People have to build => 4 week alpha release cycle. 1 week grace period
- Distribute binaries => 6 week alpha release cycle. 2 week grace period.
- Stable => 8 week release cycle
```
```
boog900: I would be fine with a minimum release schedule, with possible more frequent releases
```
```
boog900: not just for security updates
```
```
syntheticbird: This will make packaging and sysadmin life harder for only short-term benefit (excluding security updates).
```
```
hinto: How does this sound?: `RELEASE_CYCLE_WEEK_LENGTH = 8 weeks`, `KILLSWITCH_GRACE_PERIOD = 1 week` + alpha releases whenever where the killswitch is adjusted for that release date
```
```
boog900: > <@syntheticbird:monero.social> This will make packaging and sysadmin life harder for only short-term benefit (excluding security updates).

This is only going to apply during alpha while big changes are still happening 
```
```
syntheticbird: oh I assumed you were talking stable cycle
```
```
syntheticbird: Sorry i don't understand "+ alpha releases whenever where the killswitch is adjusted for that release date"
```
```
hinto: 8 weeks (cycle length) + 1 week (grace period) is the new killswitch timestamp for that adhoc release
```
```
syntheticbird: Yes
```
```
syntheticbird: oh nvm i got it
```
```
hinto: or it could be REMAINING_TIME_UNTIL_NEXT_MINIMUM_RELEASE + grace period
```
```
boog900: nah first is better a release should reset the timer 
```
```
syntheticbird: the first is good, 
```
```
syntheticbird: * the first is good,
```
```
syntheticbird: * the first is good
```
```
hinto: I would say if the release cycle were shorter in the beginning adhoc releases wouldn't need to happen and we could just stick to the document
```
```
hinto: i.e. 2-4 weeks
```
```
syntheticbird: I'm good with 3-4 week alpha, but I want 8 week for stable
```
```
boog900: Yeah I was thinking if we are giving out binaries I would like a very short kill switch 
```
```
syntheticbird: 1 week imo, just so people have the whole week to be aware of a new release
```
```
syntheticbird: and not be surprised when cuprate suddenly stop
```
```
boog900: I think I would be fine with 4 week releases for now.
```
```
syntheticbird: I assume you meant grace period
```
```
syntheticbird: my bad
```
```
boog900: > <@syntheticbird:monero.social> 1 week imo, just so people have the whole week to be aware of a new release

I mean the whole release cycle + grace period 
```
```
syntheticbird: I concur
```
```
syntheticbird: * I concur for alpha
```
```
hinto: Ok, is this consensus for an alpha release cycle?: `RELEASE_CYCLE_WEEK_LENGTH = 4 weeks, `KILLSWITCH_GRACE_PERIOD = 1 week`
```
```
hinto: * Ok, is this consensus for an alpha release cycle?: `RELEASE_CYCLE_WEEK_LENGTH = 4 weeks, KILLSWITCH\_GRACE\_PERIOD = 1 week\`
```
```
boog900: yeah
```
```
syntheticbird: yes
```
```
hinto: * Ok, is this consensus for an alpha release cycle?: `RELEASE_CYCLE_WEEK_LENGTH = 4 weeks, KILLSWITCH_GRACE_PERIOD = 1 week`
```
```
hinto: great, moving on: release codenames
```
```
syntheticbird: Do we know yet if we prefer metal or cake names ?
```
```
hinto: I vote for metal names and am ok with https://github.com/Cuprate/cuprate/issues/371#issuecomment-2600984085 for alpha releases 
```
```
hinto: Also:

> Changed upon semantic version change, ignoring alpha builds (0.0.x -> 0.x.0, 0.x.0 -> x.0.0, x.0.0 -> y.0.0)
```
```
hinto: I think a new name for each `0.0.x` is too much
```
```
syntheticbird: agree
```
```
hinto: perhaps 1 name for {alpha, beta}, then for each stable
```
```
syntheticbird: sgtm
```
```
boog900: > <@hinto:monero.social> I vote for metal names and am ok with https://github.com/Cuprate/cuprate/issues/371#issuecomment-2600984085 for alpha releases

I did think that was a mouthful but I am ok with it
```
```
boog900: > <@hinto:monero.social> Also:
> 
> > Changed upon semantic version change, ignoring alpha builds (0.0.x -> 0.x.0, 0.x.0 -> x.0.0, x.0.0 -> y.0.0)

👍️
```
```
hinto: https://github.com/Cuprate/cuprate/issues/371 also lays out the checklist I think we should go through for each release cycle, any thoughts?
```
```
syntheticbird: do you guys have arm64 hardware?
```
```
syntheticbird: also we have a cuprate mastodon account
```
```
syntheticbird: otherwise looking good
```
```
hinto: I am planning to buy/rent a few machines in the next CCS
```
```
syntheticbird: I presume Ampere Altra ?
```
```
hinto: The tasks in the list that need attention from others are:

1. Decide specific commit
1. Collect binary hashes and PGP signatures
```
```
hinto: I think I can be responsible for the rest, unless someone else wants to
```
```
hinto: not sure yet
```
```
boog900: are we signing builds done by GH CI
```
```
syntheticbird: well I would expect you to no be the only one having to deal with user book and `cuprated` stage
```
```
syntheticbird: it might be annoying in the long-term
```
```
syntheticbird: since we don't have reproducible build I presume yes
```
```
syntheticbird: oops i just ticked a checkbox sorry hinto
```
```
hinto: We could, or we could build ourselves (kind of a pain as the architecture list grows). I think users with GH binaries in their security scope would build anyway.
```
```
hinto: Until reproducible builds I think GH CI for pre-built builds is probably ok, we could also note releases with this info
```
```
boog900: Alright 
```
```
boog900: yeah I agree it should be stated 
```
```
syntheticbird: re: user book, tracking issue and your comment imply that update to it is done before release. Shouldn't this be done responsibly on commit merge/PRs instead ?
```
```
syntheticbird: * re: user book, tracking issue and your comment imply that update to it is done before release. Shouldn't this be done responsibly on individual commit merge/PRs instead ?
```
```
syntheticbird: It might not be ideal to keep track of all the changes and then edit the book.
```
```
boog900: it still needs to be fleshed out but when that is done, yes.
```
```
boog900: I can merge 365 right?
```
```
hinto: yes, I think there will be a follow up PR updating the timestamp and sanity check before release
```
```
boog900: anything else anyone wants to discuss today?
```
```
syntheticbird: i think we're good
```
```
boog900: ok then we can end here, thanks everyone 
```
```
syntheticbird: thanks
```
```
hinto: thanks
```

# Action History
- Created by: moo900 | 2025-01-14T19:09:02+00:00
- Closed at: 2025-01-21T19:10:49+00:00
