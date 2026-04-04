---
title: 'Monero Tech Meeting #156 - Monday, 2026-02-02, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1335
author: rbrunner7
assignees: []
labels: []
created_at: '2026-02-01T05:57:50+00:00'
updated_at: '2026-02-02T18:30:47+00:00'
type: issue
status: closed
closed_at: '2026-02-02T18:30:46+00:00'
---

# Original Description
Location is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting [here](https://github.com/monero-project/meta/issues/1331).


# Discussion History
## rbrunner7 | 2026-02-02T18:30:46+00:00
````
<r​brunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/1335
<j​berman> *waves*
<s​needlewoods> Hey
<plowsof> waves
<r​brunner7> Alright, what is there to report from last week? I myself looked at the code of Feather and Cake wallet to see how exactly they handle Polyseeds. Nothing too complicated.
<sneedlewoods> +1
<joshbabb> +1
<s​needlewoods> Left a comment about a bug I haven't been able to fix yet, on [#10233](https://github.com/monero-project/monero/pull/10233#discussion_r2746278037)
<s​needlewoods> short version: when refreshing you either a) have to type a password for every tx found, instead of once per refresh, or b) miss incoming pool txs
<s​needlewoods> but mainly working on wallet-rpc
<s​needlewoods> I try to not add features, but take notes if I notice something missing and will add those later to the PR. For example:
<s​needlewoods> The current wallet-rpc supports `freeze` and `thaw` by `key_image`, the Wallet API also supports to do these by `enote_pub_key`.
<s​needlewoods> And in the wallet-cli you can call `frozen` without arguments to get all frozen enotes, the RPC only works on single enotes with given key image.
<s​needlewoods> `grep "\<m_wallet\>" src/wallet/wallet_rpc_server.cpp -c`
<s​needlewoods> on `master` branch: 354
<s​needlewoods> on `remove_wallet2_from_rpc` branch: 250
<r​brunner7> Something like a deathmarch down to zero :)
<v​tnerd> Hi
<j​effro256> Howdy
<j​berman> me: restructured some of the FCMP++ integration code in prep for audits and in prep for beta, followed up on outstanding PR's
<j​effro256> Me: Mainly prep for Monerotopia , slides are due on the 5th.
<r​brunner7> I forgot to check: Was any issue opened, or comment added, on a dev related place, i.e. mostly GitHub, related to OVKs?
<r​brunner7> The Reddit discussion at least currently stays at almost zero posts and new comments
<j​effro256> Not that I know of
<r​brunner7> It looks like this came, made noise, and then went again ...
<interloper> +1
<jeffro256> +1
<joshbabb> +1
<j​effro256> It will probably be back at some point I think since it has been a recurring concern
<r​brunner7> I think so as well.
<r​brunner7> Ok. Looks like everything is running smoothly. Already time then to ask whether we have to discuss something beyond reports today :)
<j​berman> A note, I'd like to get a v1.6 alpha stressnet release out that includes tx relay v2 + reverted pool complement changes that tx relay v2 should replace + connection patches. Just so that we can get tx relay v2 tested on alpha stressnet before rolling it out with beta
<sneedlewoods> +1
<jeffro256> +1
<redsh4de> +1
<r​brunner7> But the current stressnet blockchain will just grow on with that new 1.6 alpha, right?
<r​brunner7> In the far future, when Monero will have taken over the world, the coins on that blockchain will be very expensive collectors' items :)
<j​berman> haha yes
<r​brunner7> Anything else?
<r​brunner7> Doesn't look like it. Thanks everybody for attending, read you again next week!
<sneedlewoods> thank you
````


# Action History
- Created by: rbrunner7 | 2026-02-01T05:57:50+00:00
- Closed at: 2026-02-02T18:30:46+00:00
