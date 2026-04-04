---
title: 'Monero Tech Meeting #87 - Monday, 2024-09-16, 18:00'
source_url: https://github.com/monero-project/meta/issues/1075
author: rbrunner7
assignees: []
labels: []
created_at: '2024-09-14T20:15:18+00:00'
updated_at: '2024-09-16T18:34:37+00:00'
type: issue
status: closed
closed_at: '2024-09-16T18:34:36+00:00'
---

# Original Description
Location is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting [here](https://github.com/monero-project/meta/issues/1069).


# Discussion History
## rbrunner7 | 2024-09-16T18:34:36+00:00
````
<r​brunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/1075
<s​needlewoods> hello
<j​berman> *waves*
<rottenwheel> *waves*
<r​brunner7> Well, may quite an exclusive club today :) What are your reports from the past week?
<j​berman> me: implemented + pushed trimming the tree on reorg/pop blocks and the key image migration for fcmp's, working on optimizing some ec math (batching inversions) now, and moving to tx construction this week
<rottenwheel> +1
<s​needlewoods> demystified the transaction object from wallet2 quite a bit with your help, also worked on some other of your comments https://github.com/monero-project/monero/pull/9464
<s​needlewoods> objects*
<j​effro256> howdy
<r​brunner7> Yeah, you are slowly making headway, right? It's all additive
<s​needlewoods> at least it feels like things are coming together
<j​berman> excellent :)
<r​brunner7> jberman: Did you already decide where that new tx construction code will go?
<j​effro256> me: A) Working on implementing an enote store for Carrot and legacy enotes for complete balance recovery. B) Contacted more auditors regarding Carrot C) Closing out CCS and opening new CCS
<rottenwheel> +1
<j​berman> I was thinking `cryptonote::construct_tx_and_get_tx_key` (so the tx construction code I'm referring to is what wallet2 calls, but not touching wallet2 for now)
<r​brunner7> Could be that soon you and jeffro256 will have to coordinate closer than until now, from the sound of your reports
<j​effro256> That will likely also be the function that I touch for tx construction if Carrot is to be implemented
<j​effro256> *integrated
<j​effro256> Tx construction is already implemented
<rottenwheel> +1
<j​berman> I would re-use rct_config and I figure these would be diff sections of the function, so probably won't end up with significant conflicts if any
<r​brunner7> Looks like this will get interesting pretty soon, exciting
<r​ottenwheel> Why did you have to close and reopen? Just curious.
<j​effro256> I'm done with my hours
<r​brunner7> jeffro256: Is your enote store and the scanning code copied and modified from some Seraphis library code?
<j​effro256> rbrunner7: yup!
<r​brunner7> Ok. So at long last some of that stuff will go into service.
<r​ottenwheel> Wouldn't be easier to say open new CCS to continue working on XMR? :) You didn't close it, you finished it. Semantics. Carry on with the meeting, gents.
<r​brunner7> Ah, I see. No, nobody will close out dear jeffro :)
<rottenwheel> +1
<one-horse-wagon> +1
<r​brunner7> Just curious, what larger new code parts are still coming behind these two, Carrot scanning and trees?
<r​brunner7> And tx construction of course
<j​effro256> There will probably need to be a daemon RPC endpoint that allows for selecting FCMP tree paths with decoys, in the case that the wallet does not implement wallet-side tree building
<r​brunner7> Maybe just dozens of things each smaller than these two or three big things?
<j​berman> would like for wallet-side tree building to be included in first release personally, so that
<j​berman> on my end generally for fcmp's there's still tx construction/verification/consensus changes too
<r​brunner7> As it seems we are on a good way time-wise, at least so far, wallet-side trees sound like a reasonable goal, as far as I can judge that
<j​berman> we'll also need to be sure to implement sending to dummy 0-amount outputs when there's no change, so that background scanning (and light wallet scanning) can identify those txs without revealing a user's key images to a daemon (and update scanning flow slightly for this case)
<j​effro256> Yup, that's a requirement specified in the Carrot spec, and it's implemented in the Carrot lib just like how Seraphis does it
<sneedlewoods> +1
<r​brunner7> Maybe more work to figure out properly than implementing later, with a bit of luck
<j​berman> nice
<r​brunner7> Alright. Anything special to discuss beyond things already reported now?
<r​brunner7> Doesn't look like it, so I think we can close already. Thanks everybody for attending, read you again next week!
<s​needlewoods> thanks everyone, until next time
<j​effro256> Thanks everyone!
<j​berman> thanks guys
````


# Action History
- Created by: rbrunner7 | 2024-09-14T20:15:18+00:00
- Closed at: 2024-09-16T18:34:36+00:00
