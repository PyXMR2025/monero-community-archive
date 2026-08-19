---
title: 'Monero Tech Meeting #182 - Monday, 2026-08-17, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1442
author: rbrunner7
assignees: []
labels: []
created_at: '2026-08-15T09:35:25+00:00'
updated_at: '2026-08-17T18:32:55+00:00'
type: issue
status: closed
closed_at: '2026-08-17T18:32:55+00:00'
---

# Original Description
Location is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting [here](https://github.com/monero-project/meta/issues/1438).


# Discussion History
## rbrunner7 | 2026-08-17T18:32:55+00:00
````
<rbrunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/1442
<sneedlewoods> Hello
<selsta> hi
<tobtoht> Hi
<jberman> waves
<jpk68> Hello
<slowbeardigger> Buenos dias
<rbrunner7> Alright, on to the reports for last week!
<sneedlewoods> Apart from the usual stuff, I failed to figure out why polyseed_static and debug builds don't get along.
<rbrunner7> I had a bit of a setback after @sneedlewoods found a problem with debug builds for my Polyseed PR, but I hope @tobtoht:monero.social will come to the rescue :)
<jberman> various upstream monerod improvements, beginning to prepare for FCMP++/Carrot beta stressnet v3 
<slowbeardigger> +1
<jpk68> Me: reviewed some PRs, investigated a few issues related to hardware wallets, etc.
<slowbeardigger> +1
<tobtoht> I looked at this briefly, but I couldn't a solution. It's on my to-do list.
<rbrunner7> +1
<rbrunner7> Seems we have quite a healthy flow of Monero PRs right now.
<slowbeardigger> +1
<tobtoht> Yes, more than 4x since last year?
<slowbeardigger> @tobtoht: wow
<sneedlewoods> (not complaining, just one drawback: When I started with the Wallet API I could work on it for weekss without needing to rebase or fix conflicts, now there is something new every week)
<tobtoht> And more than 100x since Jan-Mar 2022 when we had a grand total of 4 commits, ow.
<rbrunner7> Then I also remembered (again) that maybe Polyseed will have the same licensing problem as that other package with crypto ops from Tevador ...
<tobtoht> The discussion on whether to allow copyleft code in non-optional parts of the codebase continues on: https://github.com/monero-project/monero/pull/10964
<tobtoht> I guess neither tevador or jeffro are present?
<rbrunner7> Ah, ok, will follow
<tobtoht> In which case, I suggest we continue the discussion asynchronously on the PR.
<rbrunner7> Does this all mean that strictly speaking all current wallet apps with permissive licenses that use Tevador's Polyseed library are in some sort of license breach?
<rbrunner7> Alright, maybe that question also already belongs there
<jpk68> FWIW, Cake Wallet uses their own implementation of Polyseed, as far as I can tell
<tobtoht> Yes, unless they comply with the license terms (which is none of them?)
<rbrunner7> Yes, Cake Wallet uses a rewrite in Dart
<tobtoht> In the of mx25519, I would have been more understanding of restrictive licensing if mx25519 didn't incorporate permissive sources to the extent that it does.
<tobtoht> Still, even if mx25519 had been mostly original work, I don't think we should erode Monero's permissive core or burden downstream projects with license compliance.
<jpk68> +1
<rbrunner7> In a personal relationship you would say now "It's complicated" :)
<tobtoht> +1
<rbrunner7> Difficult trade-offs, as I see it
<jpk68> The mx25519 situationship :P
<rbrunner7> Anyway, seems we are through already with the reports and related things. Do we have something beyond that to discuss today? (Assuming licensing makes sense to discuss further in the frame of the given GitHub PR.)
<rbrunner7> Maybe just a cry out: Stressnet V3 now please!
<slowbeardigger> @rbrunner7: pretty please
<rbrunner7> (About 50% joking of course)
<jberman> +1
<tobtoht> I hope we can get another batch of FCMP++ PRs merged this week :)
<rbrunner7> Does Luigi do any merge work at all nowadays?
<tobtoht> Not really. He only merges things I can't, like changes to the CoC.
<rbrunner7> Ok
<rbrunner7> Looks a bit like we have, how to call this, a bit of a "bus factor" there?
<tobtoht> I think bf also has access to the repo (and maybe more core team?)
<jpk68> Is there a reason the 'members' of the monero-project org are not public?
<tobtoht> I don't know
<tobtoht> I have merge rights on 4 repos, but I don't think I'm a member of monero-project.
<rbrunner7> GitHub's rights management is quite byzantine ...
<tobtoht> @tobtoht: Yeah "You must be a member to see who’s a part of this organization."
<rbrunner7> I saw I little bit of it when I set up my "Seraphis" organization.
<rbrunner7> Maybe it's nothing more than avoiding the headache of managing a list of organization members in the first place?
<jpk68> I mean, it could be good for transparency, even if it's not the most helpful thing ever
<rbrunner7> The fact that almost nobody noticed this, as far as I remember, might want to tell us that it pretty much does not matter ...
<rbrunner7> Looks like the meeting proper ran its course for today. Thanks everybody for attending, read you again next week!
<slowbeardigger> +1
<tobtoht> +1
<jpk68> +1
<sneedlewoods> thanks everybody, cu
````


# Action History
- Created by: rbrunner7 | 2026-08-15T09:35:25+00:00
- Closed at: 2026-08-17T18:32:55+00:00
