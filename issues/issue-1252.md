---
title: 'Monero Tech Meeting #132 - Monday, 2025-08-11, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1252
author: rbrunner7
assignees: []
labels: []
created_at: '2025-08-09T14:14:06+00:00'
updated_at: '2025-08-11T18:22:51+00:00'
type: issue
status: closed
closed_at: '2025-08-11T18:22:51+00:00'
---

# Original Description
Location is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting [here](https://github.com/monero-project/meta/issues/1248).


# Discussion History
## rbrunner7 | 2025-08-11T18:22:51+00:00
````
<j​berman> My update in advance (I don't believe I'll be able to make it today unfortunately): rebased fcmp++-stage back on top of main master, shared a final update on my last CCS and opened a new proposal to continue. Marching ahead to alpha stressnet. Aside from PR review/stressnet/bug fixing, my next significant task will likely be a final organizational/cleanup pass through, then implementing fee/weight changes, and will then start up documentation again.
<j​berman> Multisig is on the radar as well, but thinking that can be postponed for now, and we can aim toward finalizing code ready for review in the main repo before completing multisig
<r​brunner7> Awww, without you waving at the start of the meeting, it's not the same :) Thanks for the report.
<r​brunner7> Meeting in a bit more than 1 hour
<r​brunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/1252
<s​needlewoods> *waves*
<r​brunner7> Oh, thanks :)
<sneedlewoods> +1
<r​brunner7> Will probably be a short meeting today.
<r​brunner7> jberman left already his report before the meeting. Again, a very busy and successful week
<s​needlewoods> yeah, I rebased and solved conflicts and spend most time with the debugger, currently after calling `make_multisig` calls to `verifyPassword()` fail, but you can still close and reopen the wallet with the same password
<r​brunner7> Sounds a bit strange
<s​needlewoods> I have a suspect, but each test to narrow it down takes a while
<r​brunner7> I see. Are you still drawing down from your CCS hours, by the way? It has been quite a while now.
<j​effro256> Howdy
<j​effro256> rbrunner7: Did you see this comment?: https://github.com/monero-project/monero/pull/9939#discussion_r2252960166
<r​brunner7> I myself don't have much to report. Not doing much except watching all things Qubic quite closely. Right now the chain reorgs come in in 15 minutes intervalls. We had a 3 block reorg earlier today. Wouldn't be surprised if these frequent reorgs will bring some bugs to light.
<r​brunner7> jeffro256: No. Arrgh, I don't know why GitHub does not inform me if something new is written there.
<s​needlewoods> I'd guess I'm closer to 2x the estimated hours now, lost track tbh, but I said that I will work on it even if the time was misjudged
<r​brunner7> Will probably answer tomorrow
<r​brunner7> SNeedlewoods: Well, that's up to you certainly ...
<r​brunner7> For the record, and to give it more "exposure", I think this GitHub discussion has quite some importance right now: https://github.com/monero-project/research-lab/issues/136
<s​needlewoods> I've subscribed that issue, very interesting, thanks to kayaba for making this summary
<r​brunner7> What can you do wrong that GitHub does not send you an e-mail if somebody adds a comment to your own PR?
<r​brunner7> I hope that Rucknium will find time to write some comments as well and add to the discussion of that PR
<s​needlewoods> idk, but maybe you can click "Subscribe" on the right hand side
<r​brunner7> Will try, thanks
<s​needlewoods> I usually get email notifications automatically as soon as I drop a comment on an issue/PR
<r​brunner7> Alright, anything else for today?
<s​needlewoods> nothing from me
<r​brunner7> Then thanks everybody for attending, read you again in 1 week!
<s​needlewoods> thank you
<j​effro256> Thank you
````


# Action History
- Created by: rbrunner7 | 2025-08-09T14:14:06+00:00
- Closed at: 2025-08-11T18:22:51+00:00
