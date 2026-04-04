---
title: 'Monero Tech Meeting #91 - Monday, 2024-10-14, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1091
author: rbrunner7
assignees: []
labels: []
created_at: '2024-10-11T16:26:16+00:00'
updated_at: '2024-10-14T18:42:21+00:00'
type: issue
status: closed
closed_at: '2024-10-14T18:42:21+00:00'
---

# Original Description
Location is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting [here](https://github.com/monero-project/meta/issues/1087).


# Discussion History
## rbrunner7 | 2024-10-14T18:42:21+00:00
````
<r​brunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/1091
<s​needlewoods> hey
<o​ne-horse-wagon> Hello.
<j​berman> *waves*
<j​effro256> howdy
<r​brunner7> Alright, what is there to report from last week?
<s​needlewoods> Got a little sidetracked with reviewing this [PR](https://github.com/monero-project/monero/pull/9492) by vthor. It adds some functions to the API that overlap with my PR.
<jeffro256> +1
<s​needlewoods> Not much changed on wallet API PR, mostly trying to figure out some things and taking notes.
<j​berman> me: completed first pass at the TreeSync class wallets can use to sync a local tree, initial unit tests set up and passing. Next planning to integrate the class into wallet2. Source: https://github.com/j-berman/monero/commits/fcmp%2B%2B-tree-sync/
<sneedlewoods> +1
<j​effro256> The MRL decided on an auditor for carrot and I kept writing integration code for it
<j​effro256> jberman: that's super exciting!
<j​berman> @jeffro256 I also created an interface like you suggested, and then implemented a child class that keeps all data in memory (interface is named TreeSync, impl is TreeSyncMemory). So someone could implement the TreeSync interface using a db for multi-wallet sync eg: https://github.com/j-berman/monero/commit/1a3b4e36f786e2b28ea4265b6e816772992de39c
<jeffro256> +1
<r​brunner7> jeffro256: Working on a hard deadline, right? :)
<r​brunner7> jberman: What's the expected amount of changes for that wallet2 integration? Is this a big story?
<k​ayabanerve> *waves*
<vthor> hi, about the review of the PR, I'm expected to change that or not expected to change anything and on a possible merge the person merging it will change it?
<j​berman> wallet2 mostly just needs to parse and pass data to the TreeSyncMemory impl. The bulk of the implementation will all be contained to that class
<r​brunner7> SNeedlewoods: Maybe also worth to mention that your CCS was met favorably in the last community meeting. Seems "Go".
<jeffro256> +1
<k​ayabanerve> I've been working on multi-input proving for FCMPs. monero-serai also has a drafted CCS for its auditing to be discussed at the next MRL. A new paper released today on a more efficient curve trees construction (with trade offs).
<j​berman> probably the most involved wallet2 thing will be implementing restore from arbitrary height: wallet2 would fetch the "right-most" path of tree elems, and then just pass that into the TreeSync class
<plowsof> yes, will be merged at the next opportunity. Jeffros Carrot spec review also
<j​berman> I haven't implemented support for "start sync from arbitrary height" in TreeSync yet. It expects syncing from genesis as currently implemented
<s​needlewoods> vthor you'll have to make the changes yourself, but if you're not sure if you should change something I suggested you can ask for other opinions
<r​brunner7> @vthor: You mean proposed changes by the reviewer? If yes, and if the proposals are ok, normally you are expected to do the changes
<s​needlewoods> ccs was a very smooth experience so far, thanks to everyone who helped out :)
<vthor> oh man, this looks so much more complicated then work. What if the reviews have contradictions?
<j​berman> nice ! @SNeedlewoods
<r​brunner7> Well, then more discussion is needed, usually. And yeah, writing the code is one thing, the review phase and the modifications is something on top.
<j​effro256> vthor: then you just talk it out. Almost every discussion I've had on code review was in good faith, very few times are there actual deep disagreements if there isn't a misunderstanding of the premise
<j​effro256> If there's a deadlock, you could probably discuss it here or in #monero-dev
<s​needlewoods> review is less fun than just coding, but it's part of the process, otherwise your code will sit there unmerged forever, sorry if this gives you additional unexpected work
<jeffro256> +1
<r​brunner7> Yes, after you get around the intial little shock of people taking apart pieces of code, the experience usually is quite interesting
<r​brunner7> *pieces of your code
<r​brunner7> And something I could hardly believe what things I all had simply overlooked
<r​brunner7> *And sometimes
<s​needlewoods> True, you can learn a lot from good reviewers
<syntheticbird> +1
<r​brunner7> So, many things are currently running in parallel, but thankfully with pretty little friction, with the exception of vthor + SNeedlewoods, which I don't doubt will get resolved
<sneedlewoods> +1
<r​brunner7> Do we have to discuss something in particular today, in addition to these reports?
<vthor> "<s​needlewoods> True, you can learn a lot from good reviewers" <- I think that is the iggest benefit. So I will try my best, but communicating is the most draining activity for me, so it takes me always longest.
<jbabb> +1
<r​brunner7> vthor, that's the spirit, and don't worry too much :)
<vthor> "So, many things are currently running in parallel, but thankfully with pretty little friction, with the exception of vthor + SNeedlewoods, which I don't doubt will get resolved" There is no friction on my side, I would be also okay if I can grab the data in another way, I did the changes only because there was no reasonable way to sync the outputs and keyimages otherwise from monero-gui
<r​brunner7> A small, somewhat off-topic question: The "Monero Dev" matrix channel stopped to work for me in Element in the browser. Is that just me, or do other people also have that problem?
<j​babb:cypherstack.com> It works for me on this acct but not my sneurlax matrix acct
<j​babb:cypherstack.com> YMMV…
<vthor> "don't worry too much :)" <- this is the super power of an autistic person. There is nothing you can't worry about :D
<r​brunner7> vthor: I see.
<r​brunner7> I think your modification are in the right place, it's just bad luck that you and SNeedlewoods work in the exact same spot at the same time.
<s​needlewoods> vthor I'm pretty sure your PR could get merged first and I'll base mine on yours, no problem
<j​babb:cypherstack.com> It’s good luck imo that we finally have not just one, but two people taking a serious look at it
<vthor> Honestly I never expected it to get merged at all, my impression was that things almost never move while all moves at once (know sounds odd, but don't know how to express it better)
<r​brunner7> Alright, I think we don't have any more important on-topic questions, so we can close the meeting. Thanks everybody for attending, read you again next week!
<vthor> "vthor I'm pretty sure your PR could get merged first and I'll base mine on yours, no problem" <- so then I should hurry to not block you. I will look in some hours into, try to fix my or better said my daughters life finally. I'm better how I have an idea and pills (again) now :D
<r​brunner7> Josh Babb: Yeah, that Wallet API was suffering from quite some neglect, given its importance
<s​needlewoods> Thanks everyone, good meeting
<r​brunner7> I wonder what new *public* stuff jberman will come up in `wallet2` that then *again* is not yet represented in the Wallet API ...
<j​berman> errrr, can't think of anything that needs to change on the public side right now (except anything to do with specifycing ring size e.g.). these changes should all be internal
<r​brunner7> Good to hear.
<j​berman> the changes to wallet2 should really end up very small, we'll see
<r​brunner7> That's a bit surprising, with Seraphis the changes would have been so massive that we would have been pretty much *forced* to abandon `wallet2`. Now we will live a bit longer with this marvel of software engineering. Ahem.
<j​berman> tx construction changes i think will be a bit more involved, but syncing changes needed should be minimal because I pushed so much logic out into this separate class
````


# Action History
- Created by: rbrunner7 | 2024-10-11T16:26:16+00:00
- Closed at: 2024-10-14T18:42:21+00:00
