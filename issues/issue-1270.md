---
title: 'Monero Tech Meeting #138 - Monday, 2025-09-22, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1270
author: rbrunner7
assignees: []
labels: []
created_at: '2025-09-19T14:24:40+00:00'
updated_at: '2025-09-22T18:32:29+00:00'
type: issue
status: closed
closed_at: '2025-09-22T18:32:29+00:00'
---

# Original Description
Location is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting [here](https://github.com/monero-project/meta/issues/1267).


# Discussion History
## rbrunner7 | 2025-09-22T18:32:29+00:00
````
<r​brunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/1270
<s​needlewoods> Hello
<j​berman> *waves*
<p​arasew> helo
<s​pirobel> hi
<r​brunner7> Seems jberman is already typing his report :)
<r​brunner7> Yeah, what about last week?
<s​needlewoods> down to 77 `m_wallet`, also cleaned up a lot and went from ~1200 unstaged changes to ~100, also began to write some notes for the PR that will hopefully be made in foreseeable future
<jberman> +1
<r​brunner7> That sounds splendid
<r​brunner7> Did you continue to try to make a static build?
<j​berman> me: completed FCMP++ refresh refactor PR 81 (jeffro approved) fortunately was able to make the code much cleaner without chaning the async structure as I originally posited, opened PR for daemons to kick invalid txs from pool upon popping blocks (e.g. to handle a reorg) although seems I'm in the minority in favor of that #10085, and for wallets to identify spends in the pool upon <clipped messag
<j​berman> restore/if they're not the sending wallet (#10083). Stressnet launch nearly here (hopefully after a final round of testing from ofrn)
<j​berman> I've also re-started on documentation for the fcmp++ integration, and will harden my plan for upstreaming my side of changes as I work through documentation
<r​brunner7> "This change kicks these invalid txs from the pool" I can see why that could be controversial, especially compared with a much shorter keep-alive time, not those overly long 7 days
<j​effro256> Howdy
<r​brunner7> A reviewing / merging issue was opened somewhere that might be worth mentioning here, right? Don't have a link handy
<j​effro256> The main downside is that it opens the door for other people  o perform double spend attacks when the reorg depth >= 10
<j​effro256> I made a first draft of the Rusty Carrot library: https://github.com/jeffro256/carrot-rs
<spirobel> +1
<jberman> +1
<r​brunner7> Got it in the meantime: https://github.com/seraphis-migration/monero/issues/103
<j​berman> ah, didn't know what you were referring to
<j​berman> ya that issue is a solid tracking issue by jeffro / plan
<r​brunner7> That will need quite some beating of drums to get people outside of our little circle here to read into FCMP++ tech and start to review ...
<parasew> +1
<r​brunner7> I think it's not that often that one has to implement the same bigger thing in two different languages, like jeffro256 did now with Carrot. Allows for first-hand comparisons of programming languages, here between C++ and Rust.
<r​brunner7> Alright, looks like we are through with the reports. Anything else we have to discuss today?
<s​needlewoods> is the rust lib "feature-complete" in comparison to the c++ one, or are there any differences?
<s​needlewoods> nothing else to discuss on my end
<r​brunner7> Hopefully some potential memory leak "features" are missing from the Rust lib :)
<sneedlewoods> +1
<jeffro256> +1
<j​effro256> Yes, it's feature complete to the `carrot_core` part
<sneedlewoods> +1
<r​brunner7> I don't think that there will be noticable *speed* differences?
<j​effro256> Depends on how fast the underlying cryptography primitives are for the Rust dependencies I used
<s​needlewoods> sorry, I completely missed that question, yes I tried and failed for a couple more attempts, then just continued to use the `master` branch
<rbrunner7> +1
<j​effro256> But the part of the code that is mine is more or less the exact same AFAICT
<r​brunner7> Anyway, nice to see how we will most probably able to keep up Rust because there is enough engagement and interest. In theory, it could just wither because of not enough push.
<r​brunner7> Ok, let me close the formal meeting while chat continues. Thanks everybody for attending, read you again next week!
<s​needlewoods> thanks everyone
````


# Action History
- Created by: rbrunner7 | 2025-09-19T14:24:40+00:00
- Closed at: 2025-09-22T18:32:29+00:00
