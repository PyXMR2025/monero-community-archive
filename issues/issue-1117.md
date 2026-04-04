---
title: 'Monero Tech Meeting #97 - Monday, 2024-12-02, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1117
author: rbrunner7
assignees: []
labels: []
created_at: '2024-11-29T16:48:23+00:00'
updated_at: '2024-12-02T18:34:56+00:00'
type: issue
status: closed
closed_at: '2024-12-02T18:34:55+00:00'
---

# Original Description
Location is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting [here](https://github.com/monero-project/meta/issues/1114).


# Discussion History
## rbrunner7 | 2024-12-02T18:34:55+00:00
````
<r​brunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/1117
<r​ottenwheel:unredacted.org> Hola a todas y todos.
<a​rticmine> Hi
<s​needlewoods> hey
<r​brunner7> So what is there to report from last week?
<r​brunner7> jberman can't make it today. For the record:
<r​brunner7> "I won't be able to make today's meeting unfortunately, my update in advance: I'm very close to finishing FCMP++ wallet sync from an arbitrary restore height. Less than a day of work remaining. Next I plan to work on FCMP++ tx construction"
<r​brunner7> "My working branch for wallet sync: https://github.com/j-berman/monero/commits/fcmp%2B%2B-tree-sync-dev/"
<s​needlewoods> Tested the callback functions and am relative certain they work as expected, added implementation for `setDaemon()` and while doing a small review on my own I found two more questions and posted those on the PR https://github.com/monero-project/monero/pull/9464
<jeffro256> +1
<s​needlewoods> Also I've been delaying to post an update on my CCS, because I tried to get my PR out of WIP state first, but I feel like a donkey hunting a carrot on a stick, just one step away from reaching that goal. So I'm hoping to get there soon and plan to post this now, if anyone wants to leave feedback: https://paste.debian.net/hidden/1f5880b7/
<r​brunner7> Nice, SNeedlewoods . Where does vthor's wallet PR stand in the meantime, that will need some coordination with yours? Any news there?
<s​needlewoods> vthor updated his PR, I haven't fund the time to review it yet though
<vthor> Hello :) I hope I did it right, if not I will probably need some help with the github web interface side - pretty confusing for me
<a​rticmine> I am working on scaling and fees to support FCMP++ 
<a​rticmine> The main changes are linear scaling for all fee levels as opposed to quadratic scaling for the lower two levels and simplification of the fee calculations at the  wallet level
<r​brunner7> I like the sound of "simplification" :)
<r​brunner7> Looking forward to the complete proposal. I hope that our decision processes will be up to the task to agree on modifications ...
<r​brunner7> By the way, kayabanerve has announced that he will reduce the number of his many engagements and concentrate on Serai.
<r​brunner7> Sounds reasonable, even geniuses need to sleep :)
<s​needlewoods> vthor I just had a quick look, I think the ".gitignore" file should not be part of the commit and I saw you added functions to the wallet_rpc, are they used by your PR or did you add them because of my comment https://github.com/monero-project/monero/pull/9492#discussion_r1794199366 ? I just left that for discussion, sorry if that was confusing.
<s​needlewoods> Will try to have a more detailed look into your PR this week
<r​brunner7> Alright. Anything else to discuss?
<r​brunner7> The MRL meetings seem to get longer and longer while we have somewhat of a lull lately here :)
<j​effro256> Hello, sorry I'm so late
<j​effro256> Just working on improving the Carrot code
<vthor> sneedlewoods: heck, I need to see how to remove the .gitignore modifications will, see how to fix that. I wanted to make a PR for that, but I never did. But it should not be there included in the PR - if so I fucked it up...
<r​brunner7> Did any modifications result from the completed review, jeffro256 ?
<r​brunner7> The scheme seems to hold, right?
<j​effro256> Not any crypto changes, but the spec could use a lot of rewording to make certain parts more precise and clear
<s​needlewoods> vthor I can try to help you solve it, I don't think it's "fucked up"
<r​brunner7> Seems that we can close for today. Thanks everybody, read you again next week!
<s​needlewoods> thanks everyone, cu
<vthor> 8) thank you sneedlewoods, I (try to) work at the moment double the time to make up the lost 2/3 weeks, so I'm almost never look in any irc channel, but my nick mentioned here gives me a notification in center of my screen and every once in a while I will see if there is a message in matrix.
````


# Action History
- Created by: rbrunner7 | 2024-11-29T16:48:23+00:00
- Closed at: 2024-12-02T18:34:55+00:00
