---
title: 'Monero Tech Meeting #95 - Monday, 2024-11-18, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1110
author: rbrunner7
assignees: []
labels: []
created_at: '2024-11-15T16:22:33+00:00'
updated_at: '2024-11-18T18:37:20+00:00'
type: issue
status: closed
closed_at: '2024-11-18T18:37:20+00:00'
---

# Original Description
Location is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting [here](https://github.com/monero-project/meta/issues/1103).


# Discussion History
## rbrunner7 | 2024-11-18T18:37:20+00:00
````
<r​brunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/1110
<s​needlewoods> Hey
<j​berman> *waves*
<r​brunner7> So today with a bit less attendance, but that was expected, because of Monerotopia ...
<r​brunner7> Anyway, any reports?
<s​needlewoods> Mainly worked on the tests and made some progress after having a chat with jberman.
<s​needlewoods> Also posted an update on the [Wallet API PR](https://github.com/monero-project/monero/pull/9464#issuecomment-2483736771) with the last few things on my TODO list, which I'm currently stuck at.
<s​needlewoods> Not sure how to proceed on it on my own, so I'm thinking about removing the "[WIP]" from the title of the PR and edit the first comment to include something like: "Ready for reviews and feedback" to get more eyes on it. Any opinions?
<r​brunner7> Will try to find time to comment to your "TODOs" this week
<sneedlewoods> +1
<r​brunner7> Maybe others will chime in as well
<r​brunner7> I think it would be nice to open for reviews with something like a "release candidate", IMHO
<j​berman> me: posted a CCS update 2/3 linked above. Reiterating: finished a solid tree sync impl in wallet2, working on restore from arbitrary height next. Also my presentation at Monerotopia was mostly on the tree implementation in the daemon/wallet, and hopefully would help anyone who wants to understand my current WIP PR on the fcmp++ integration in the Monero repo. I got solid feedback <clipped messag
<j​berman> on it from people who found it easier to understand what the whole "tree" thing is about from the presentation
<sneedlewoods> +1
<s​needlewoods> can you explain what you mean by that?
<r​brunner7> Better to get those 3 TODOs out of the before issuing a broad invite to everybody for review
<r​brunner7> *out of the way
<s​needlewoods> excited to see your presentation jberman
<r​brunner7> jberman: People were able to follow? What was your impression / gut feeling?
<s​needlewoods> Alright
<r​brunner7> Ah, you already wrote about it ...
<j​berman> mostly people with dev backgrounds were able to follow, and people came up to me and expressed positive sentiment/appreciated the understanding they got from it (and made it clear to me they understood more components to the curve tree after the presentation versus before)
<j​berman> I tried to make it very approachable for any dev to follow along. even included a slide on the very basics of hash functions and a basic slide on merkle trees
<r​brunner7> Sounds interesting to watch then :)
<r​brunner7> Usually making such presentations also sharpens one's own view on things
<jberman> +1
<r​brunner7> Alright, do we have anything beyond these reports for today?
<s​needlewoods> Just one general question, do I just make a PR if I want my gpg keys to get added [here](https://github.com/monero-project/monero/tree/master/utils/gpg_keys) or are there other requirements?
<s​needlewoods> (btw rbunner your keys there are expired)
<j​berman> TBC, @SNeedlewoods you want feedback on the TODO's so that you can make progress right now, ya?
<r​brunner7> Thanks for the reminder, yes, my key is expired. Will care about that soon. I think making a PR is ok. Somebody may ask for another proof, e.g. you making a statement on your GitHub as confirmation that you is you
<r​brunner7> Or maybe here, maybe GitHub is not "more secure" than the PR already ...
<s​needlewoods> Yes, apart from that list I don't know what else needs to be worked on, other things will get revealed in the full review stage I guess.
<r​brunner7> People do not seem to use their keys often, as it seems, but things like that can probably become important should any kind of emergency happen, like an attack
<s​needlewoods> I thought it might be a good idea to share the keys before I claim my CCS so I can sign the request
<r​brunner7> Certainly not a bad idea, yeah
<s​needlewoods> Nothing else to discuss for me
<j​berman> is there something on the wallet2 callback methods that you need feedback on @SNeedlewoods or is that just on the TODO list
<j​berman> w.r.t. setDaemon... looks like we'd want wallets to go through the API to accomplish what wallet2's init currently accomplishes, and for a distinct way to accomplish wallet2's set_daemon. looks like doInit is pretty close to wallet2::init with some caveats worth double checking/thinking on for the CLI, and a new setDaemon could just call wallet2's set_daemon. WalletManager::setDae<clipped messag
<j​berman> monAddress{Async} seems ok to leave as is
<r​brunner7> Allow me to close the meeting proper, but of course do continue to discuss. Thanks for attending, read you again next week!
````


# Action History
- Created by: rbrunner7 | 2024-11-15T16:22:33+00:00
- Closed at: 2024-11-18T18:37:20+00:00
