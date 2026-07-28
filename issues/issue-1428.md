---
title: 'Cuprate Meeting #113 - Tuesday, 2026-07-28, UTC 18:00'
source_url: https://github.com/monero-project/meta/issues/1428
author: moo900
assignees: []
labels: []
created_at: '2026-07-21T18:23:51+00:00'
updated_at: '2026-07-28T18:38:58+00:00'
type: issue
status: closed
closed_at: '2026-07-28T18:38:58+00:00'
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

Previous meeting: #1424

# Discussion History
## Boog900 | 2026-07-28T17:09:49+00:00
I am posting my update here as it's going to be a bit long.

Firstly, I did an AI scan of the tapes database, and it identified a few issues, I have been working through fixing these and am almost ready to push. The issues were around our custom in memory cache, this could go out of sync under rare circumstances. Luckily these were found before they have caused issues.

Secondly, as I have already mentioned, I slopped a performance test for Cuprate RPC vs monerod. This performance test has been updated to now output graphs! The tests uses nodes with no connections, in the real world P2P connections could cause contention on the DB, especially with monerod which uses mutexes. 

You will notice on the graphs there are 2 Cuprates. Cuprate sets the limits on the amount of blocks given out per request  lower than monerod, this is because monerod sets them at the literal boundary of what is allowed by epee. This does have an impact on the amount of blocks we can give out a second but it is worth it for stability. For the sake of the test though I have added a version of cuprated with the limits matched.

The first graph measures how many blocks are given out per second with different number of wallets:

<img width="1100" height="680" alt="Image" src="https://github.com/user-attachments/assets/f41a9073-9883-4cbf-8e5a-f160e8416486" />

For 1 wallet monerod and Cuprate (with increased limits) are tied, this is probably down to the bottleneck being the wallet rather than the node. This means monerod and cuprate can saturate a wallet for recent blocks. For full chain scans Cuprate is faster from personal experience. This is probably due to lower blocks having less txs so the wallet can make more RPC requests per second.

Cuprate can clearly scale better than monerod. It also has much tighter min-max ranges. monerod stays almost flat but in some runs it gives out _less_ blocks for 16 wallets compared to 1.

If you look closely though monerod is actually slightly ahead for 2 wallets and for 4 wallets it is on average just ahead. I thought this could be because LMDB is caching blocks in memory, so only the first wallet is doing disk look-ups for blocks. 

So to make the test more ~~favourable to cuprate~~ realistic, I made a new test that tests the sync of 1 wallet with more wallets syncing at random points in the chain to add DB pressure. In all seriousness, I do think it is something to look at, how we are poorer at caching recent look-ups. However, I do not think 4 syncing wallets from the same point is the thing that should be celebrated, in the real world the DB will be getting lots of different requests for different data, hence this next test.

<img width="1100" height="680" alt="Image" src="https://github.com/user-attachments/assets/af1f0cb3-f4fc-4e98-87e1-6bc6a2f20eb1" />

That test confirms that monerod was benefiting a lot from LMDB caching recent requested blocks.

Here are some more graphs:

<img width="1100" height="680" alt="Image" src="https://github.com/user-attachments/assets/b929bc20-cc1e-467f-a262-e4e8dc0e8ad2" />

<img width="1100" height="680" alt="Image" src="https://github.com/user-attachments/assets/5ba5bf75-a4ea-47a0-a6b8-81c4aa5d00fc" />

<img width="1100" height="680" alt="Image" src="https://github.com/user-attachments/assets/95e11297-59a6-4738-86ee-dff06c0509f5" />

## moo900 | 2026-07-28T18:38:57+00:00
## Meeting logs
```
boog900: 1) greetings 
```
```
redsh4de: hello
```
```
boog900: 2) updates
```
```
boog900: I have already posted my update: https://github.com/monero-project/meta/issues/1428#issuecomment-5107322419
```
```
redsh4de: rebased couple smaller PRs, 605 and 644
```
```
boog900: 3) Project: What is next for Cuprate?
```
```
boog900: I will probably put out the pre-release this week
```
```
boog900: I need to update some docs and get the tapes fixes in
```
```
redsh4de: Ill prob continue maintaining existing PRs, havent found anything new to take up so far
```
```
boog900: fair, I will get to them eventually
```
```
redsh4de: that reminds me, is this issue still relevant after the tapes upgrade? as its append only: https://github.com/Cuprate/cuprate/issues/531
```
```
boog900: less so 
```
```
boog900: I think we could do a lot with a better block downloader
```
```
boog900: but tapes halved sync speeds 
```
```
redsh4de: i reckon 475 can been closed too as we return target height from the syncer now
```
```
syntheticbird: Hi
```
```
redsh4de: Hiya
```
```
syntheticbird: update: Slowly but surely reviewing graceful shutdown part 2 
```
```
syntheticbird: reading more about the supposed deanonymization attack over tor paper
```
```
syntheticbird: tho this is more of a matter for the MRL meeting of tomorrow
```
```
boog900: closed
```
```
syntheticbird: Could you do friday ?
```
```
syntheticbird: so people have the time to play out during week-end
```
```
boog900: Sure
```
```
syntheticbird: I will try to rehabilitate the website tomorrow so we can draft a blog post
```
```
syntheticbird: lag
```
```
boog900: nice thanks
```
```
boog900: does anyone have anything else they want to discuss?
```
```
syntheticbird: Yes
```
```
boog900: go on ....
```
```
syntheticbird: It just come to my mind recently that the RPC timeout mitigation PR was never merged (and abadonned (congrats syntheticbird)). As I've said earlier in the PR discussion this is an attack vector and an exploited vulnerability that needed to be patch on monerod.
However this mitigation only works on Linux (and supposedly BSD), because of Windows driver shenanigans. Resolving windows support was the blocker but I propose that we go on with the PR in this state regardless.
```
```
syntheticbird: I'm not satisfied at letting windows support atm but I am even more unsatisfied at having a Beta release without it
```
```
syntheticbird: support out*
```
```
boog900: Do you have a link?
```
```
syntheticbird: hold on
```
```
syntheticbird: https://github.com/Cuprate/cuprate/pull/466
```
```
boog900: Ah yeah I remember
```
```
syntheticbird: The tests were failing on windows not linux
```
```
syntheticbird: so this would need to be gated
```
```
syntheticbird: and I think you weren't happy with the abstraction of the duration source
```
```
syntheticbird: I argued this could be modified on the fly but you wanted it to be fixed.
```
```
boog900: Yeah I'll have a look 
```
```
boog900: Do we need platform specific code?
```
```
syntheticbird: currently nope
```
```
syntheticbird: its abstracted by tokio
```
```
boog900: anything else for today?
```
```
syntheticbird: I think I saw redsh4de writing at some point
```
```
redsh4de: Ah yea stepped away for a bit - i did recall i had a PR that i closed with the goal of re-structuring it later after some PRs were merged
```
```
redsh4de: for logging sync progress while syncing
```
```
redsh4de: so will get that up to date
```
```
redsh4de: thats it from me
```
```
boog900: I think we can end here
```
```
boog900: thanks everyone!
```

# Action History
- Created by: moo900 | 2026-07-21T18:23:51+00:00
- Closed at: 2026-07-28T18:38:58+00:00
