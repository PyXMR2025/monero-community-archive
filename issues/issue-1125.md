---
title: 'Monero Tech Meeting #99 - Monday, 2024-12-16, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1125
author: rbrunner7
assignees: []
labels: []
created_at: '2024-12-13T16:37:53+00:00'
updated_at: '2024-12-16T18:31:54+00:00'
type: issue
status: closed
closed_at: '2024-12-16T18:31:53+00:00'
---

# Original Description
Location is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting [here](https://github.com/monero-project/meta/issues/1121).


# Discussion History
## rbrunner7 | 2024-12-16T18:31:53+00:00
````
<r​brunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/1125
<j​berman> *waves*
<s​needlewoods> hello
<r​brunner7> Alright, maybe more will join later. I think we can start with the reports.
<j​effro256> Howdy
<j​berman> me: opened a new CCS proposal (https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/527), nothing significant to report from last week (spent it mostly fixing my dev env setup unfortunately). This week I'm continuing with the optimized torsion check
<s​needlewoods> I received quite a lot of feedback on some things from multiple persons.
<s​needlewoods> Have a local WIP branch for the changes I proposed [here](https://github.com/monero-project/monero/pull/9464#issuecomment-2539057424), but before I start changing everything, I'd like to hear what you think.
<s​needlewoods> Especially after vthor expressed some concerns in this channel a couple days ago (matrix users see here: https://matrix.to/#/!PAAeACCTzofUENRcqJ/$JW3WPkK2WYP8aukz79cZiyYObg9RDDp6DZszpBiU760?via=monero.social&via=matrix.org&via=tchncs.de )
<s​needlewoods> Also, another note, tobtoht made a good point for adding freeze/thaw methods by pubkey, but not sure if those should be part of this PR or a following one, any opinions?
<j​effro256> me: fixed wownero's decoy selection issue, spent time reading kayaba's FCMP++ code and about switch commitments, planning Carrot integration pathway into `wallet2`, and left a CCS update: https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/504#note_27675
<r​brunner7> That's the "coin control" thing that they have to do now in some complicated way, if I understand correctly, SNeedlewoods ?
<r​brunner7> jeffro256: What was the bug in Wownero, in one or two sentences? Very curious
<s​needlewoods> the thing about freeze/that, yes
<j​effro256> thanks for documenting all these issue, reading the github comment rn
<sneedlewoods> +1
<r​brunner7> We have already so many methods, we can afford two more to take away the need to jump through hoops for that, IMHO
<vthor> Hey everybody. :o Was not aware that I expressed concerns, unfortunately the link does not really work for me, but I will try to find through scrolling back.
<s​needlewoods> that would come with the drawback of another slight modification of wallet2
<j​effro256> The blockchain code set the start height of the RingCT output distribution based on the wrong fork version, way too high, so there wasn't enough outputs in the distribution, making all the decoy picks very old. They also commented out the assertion in the wallet that was catching this bug, assuming it was simply an annoying remnant
<s​needlewoods> vthor sorry if I misrepresented the situation, I mean e.g. you disliked the idea of introducing the term "enote" instead of "output"
<r​brunner7> If it takes away friction moving from wallet2 to Wallet API, so be it (it = modifying wallet2 a bit)
<sneedlewoods> +1
<vthor> ah, now I remember. :D But it's not expressed concerns, it's more my opinion and how I see the things. Things are best black  or white, all other colors and shades better left to quantum computing and other oracles :D (if it was about graduatly changing which leads to a weird state in between)
<r​brunner7> Well, about that enote thing: Yes, we may fail to fully establish that new term, but if you never try to improve with such arguments, where would that leave you :)
<s​needlewoods> for reference, here is a link to the coin control patch https://github.com/MrCyjaneK/monero_c/blob/2a38bf29618a8ce163f9d6f83b7ae86924752e32/patches/monero/0009-coin-control.patch#L161
<vthor> sneedlewoods, don't worry ;) everything fine. Looks to me only like I would complain, what I don't. All this decissions are not easy and not mine to take either...
<r​brunner7> Maybe "enote" will grow on you over time, vthor, who knows ...
<vthor> rbunner, no in my opinion it is all or nothing. When I make changes like that I grep through the whole source and change everywhere....
<r​brunner7> Ah, I see. Well, with large codebases like Monero any such sweeping changes, for whatever, are difficult
<vthor> rbunner, and it is not that I really care about the term, only think it is a bad Idea two have in one source two terms for the same thing...
<r​brunner7> Ok. Seems that right now, in this forum, this is a minority opinion. But yeah, it's not really difficult, getting the two important PRs, yours and SNeedlewood's, ready and merged is of course much more important.
<r​brunner7> *it's not really important
<s​needlewoods> I'd like to get some consensus and not just choose names that I prefer, seems most active people in this room like the term "enote", others who never heard it find it strange
<vthor> and how I said, not complaining, I dislike it, but this is my issue... It is how I said more meant as opinion. Because it makes things harder, and  think a developer should look to makes the things easier, simpler and clearer. But I will for sure not complain how somebody else does it's work ;)
<r​brunner7> Ok, I think you two will find each other somewhere.
<s​yntheticbird> not gonna lie I have no idea what is an enote
<s​yntheticbird> despite having followed these meetings for a little while
<vthor> yah, I think you make it for someone new (I would still consider me new to the source although I read already hours inside) harder if you jump from exportOutput -> export_enotes -> export_outputs or similar. 
<r​brunner7> jberman new CCS proposal is a very interesting read. Looks like we enter a very interesting phase in the way towards FCMP++ very soon.
<s​needlewoods> https://github.com/seraphis-migration/wallet3/issues/1 
<s​needlewoods> you can think of it as electronic banknote
<syntheticbird> +1
<r​brunner7> Yes, the term "does not explain itself". But neither does "output", if you think about it.
<s​yntheticbird> "output" was highly confusing 3 years ago
<s​yntheticbird> definitely not self explanatory
<r​brunner7> Do we have something to discuss today beyond what was already mentioned?
<s​needlewoods> Not from me
<r​brunner7> Alright, does not look like it. Therefore thanks for attending, read you again at the start of Christmas week
<vthor> Have a great time everybody! :)
<s​yntheticbird> delicious meeting as always
<j​effro256> For conflicts 1, 2, I agree with vthor's approach: serializing/deserializing tx sets shouldn't be part of the *wallet* API. For conflicts 3, the functions have some overlap, but they are different: vthor's function actually submits the transaction to the network, whereas the `wallet2` and your proposed function do not AFAICT. For conflict 4, I prefer your version because that optimization is already exposed. As for version 5, the only substantive difference is that a `size_t` versus `bool` is returned. I would prefer `size_t` to keep it inline with `wallet2` and it isn't that much more complicated. As for the naming of "enote" vs "output" here, I prefer enote generally for big sections of new code, but honestly it might get confusing if we're mixing terms on the same API interface
<s​needlewoods> thanks everyone, I'll probably won't be here next meeting, so happy holidays everybody
<r​brunner7> Thanks, likewise to everybody who will join again after the holidays
<s​needlewoods> thanks a lot jeffro
````


# Action History
- Created by: rbrunner7 | 2024-12-13T16:37:53+00:00
- Closed at: 2024-12-16T18:31:53+00:00
