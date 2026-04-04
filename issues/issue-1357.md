---
title: 'Monero Tech Meeting #162 - Monday, 2026-03-23, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1357
author: rbrunner7
assignees: []
labels: []
created_at: '2026-03-20T12:28:09+00:00'
updated_at: '2026-03-23T18:28:16+00:00'
type: issue
status: closed
closed_at: '2026-03-23T18:28:16+00:00'
---

# Original Description
Location is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting [here](https://github.com/monero-project/meta/issues/1353).


# Discussion History
## rbrunner7 | 2026-03-23T18:28:16+00:00
````
<r​brunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/1357
<UkoeHB> Hi
<v​tnerd> Hi
<s​yntheticbird> Hi
<s​needlewoods> Hey
<j​berman> *waves*
<r​brunner7> Alright. What is there to report from last week? Me: Went carefully through all of https://github.com/seraphis-migration/monero/issues/306
<r​brunner7> Noticed that jeffro256 did not yet comment there
<r​brunner7> Left my own opinion as of now
<s​needlewoods> continue work on wallet-rpc, `grep "\<m_wallet\>" src/wallet/wallet_rpc_server.cpp -c` gives 44 results
<r​brunner7> Love your countdowns :)
<jberman> +1
<s​needlewoods> :) it's an easy way to measure progress, but will have a PR to show soonish
<j​berman> Continuing on an edge case hang-on-shutdown in monerod
<r​brunner7> Such things may be hard to debug, right?
<UkoeHB> Waiting to hear from jeffro256, planning to review carrot_core
<j​berman> yes not the easiest. nice that ofrn identified a way to reproduce it fairly consistently, and I've implemented a fix that is holding up, but I'm working on a test case that 100% demos the issue and that's been a bit of a challenge
<r​brunner7> Is this in the FCMP++ version or the ordinary daemon?
<j​berman> ordinary daemon
<j​berman> it's caused by this PR, which was necessary to fix a distinct issue: https://github.com/monero-project/monero/pull/10278
<r​brunner7> Looks like fairly extensive changes at first sight
<j​berman> it wasn't, a good portion of that PR was de-duplicating logic
<j​berman> and a 70 line test
<r​brunner7> In the soon-to-arrive AI dominated future we will have essentially the same logic in 50 places and nobody cares :)
<r​brunner7> Alright, thanks for the reports. I was thinking to propose to go back to the subject of "hybrid wallets" today, but then I noticed that UkoeHB's post is only 4 days old, so it's probably too early, and as already mentioned at least comments from jeffro256 did not yet arrive.
<r​brunner7> I can only advice to have a look, and maybe give your opinion as well, because IMHO it would be good to reach "loose consensus" soon about which way we go
<s​needlewoods> I tend to agree with your latest comment on the issue
<j​berman> Will try to share my view soon too. Fwiw my opinion is still against the hybrid model in favor of separate
<r​brunner7> Ok, nice
<r​brunner7> I understand the "lure" of the hybrid solution, in a way it's very clever, and has a certain elegance. But when I think how that will look "high up", in the wallet apps, it's probably quite hairy
<UkoeHB> I want to add more jamtis features to carrot, so will withhold commentary until jeffro replies to my arguments.
<j​berman> ack
<r​brunner7> Adding still before the hardfork to FCMP++?
<r​brunner7> Wouldn't that be quite ambitious, if yes?
<UkoeHB> Yes. Not extremely ambitious no, just address parsing, address gen and management, and adjustments to tx construction/scanning. Not trivial but not on the scale of current code changes.
<r​brunner7> Interesting. More minds bring more ideas :)
<r​brunner7> Alright. Do we have something more to discuss today?
<r​brunner7> Doesn't look like it. Thus we can close; thanks for attending everybody, read you again next week!
<j​berman> thank you!
<s​needlewoods> thanks everyone, see ya
````


# Action History
- Created by: rbrunner7 | 2026-03-20T12:28:09+00:00
- Closed at: 2026-03-23T18:28:16+00:00
