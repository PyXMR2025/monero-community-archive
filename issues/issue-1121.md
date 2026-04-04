---
title: 'Monero Tech Meeting #98 - Monday, 2024-12-09, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1121
author: rbrunner7
assignees: []
labels: []
created_at: '2024-12-06T16:12:52+00:00'
updated_at: '2024-12-09T18:34:09+00:00'
type: issue
status: closed
closed_at: '2024-12-09T18:34:08+00:00'
---

# Original Description
Location is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting [here](https://github.com/monero-project/meta/issues/1117).


# Discussion History
## rbrunner7 | 2024-12-09T18:34:08+00:00
````
<r​brunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/1121
<a​rticmine> Hi
<s​needlewoods> hey
<j​berman> *waves*
<j​effro256> Howdy
<r​brunner7> So, what is there to report from last week?
<s​needlewoods> Comparing the current state of [vthor's PR](https://github.com/monero-project/monero/pull/9492) to my [Wallet API PR](https://github.com/monero-project/monero/pull/9464) to identify any conflicts and taking notes, will post an update soon which probably needs some discussion to choose how to continue.
<j​berman> me: start sync from arbitrary sync is working, did some cleanup, and wrote up this idea from @jeffro256 to drastically simplify trim handling: https://github.com/monero-project/monero/pull/9436#issuecomment-2519858103
<j​berman> Over the weekend kayaba implemented what should be a faster torsion check that I'm going to use to hopefully speed up tree building and benchmark this week
<vthor> oh heck, sneedlewoods, I forgot about that :/ sorry, will try to do it as soon as possible.
<j​effro256> Decided to switch towards a faster Carrot integration for the time being instead of more "thorough" after talking to jberman @jberman. Also , working on a FCMP++ benchmark to compare against CLSAG
<s​needlewoods> no worries, the things I commented on do not delay me right now @vthor
<r​brunner7> What are the tradeoffs here, jeffro256 , "faster" versus "thorough"?
<vthor> thank you sneedlewoods 8)
<j​effro256> The way I was doing it would require a lot of changes to wallet2, which I want to do eventually, but it wouldn't probably take much longer to review
<r​brunner7> You found a way for better separation of your changes then?
<r​brunner7> "a lot of changes to wallet2" does not sound very fortunate, in any case :)
<j​effro256> The separation was already there, but I was being overzealous in trying to replace large portions of wallet2 off the bat IMO
<j​berman> Tbc, jeffro I think you meant "would* probably take much longer to review" haha right?
<j​effro256> Yes oops
<r​brunner7> We could also keep the hope alive that one fine day we will be able to replace wallet2, and as long as we do, avoiding unneccessary changes to that are probably a good idea
<sneedlewoods> +1
<jberman> +1
<j​berman> Continuing the effort to replace wallet2 is my highest priority after FCMP++
<rottenwheel> +1
<j​berman> after FCMP++ fork*
<j​berman> (keeping the hope very much alive)
<r​brunner7> Yeah, "after the fork" is a better point in time than "after FCMP++"
<j​berman> wanted to make that distinction because it would include post-Carrot too. I think large changes to wallet2 before the fork would delay the fork, and I'd vote to prioritize the fork
<rbrunner7> +1
<jeffro256> +1
<rottenwheel> +1
<r​brunner7> And well, if we can fork without them, maybe we will even get away with not making them after all, because we are able to build new code
<j​berman> The technical debt really is pretty massive, I think we really should focus on trying to reduce it ... though fork is higher priority
<j​berman> imo
<r​brunner7> The fork party will make you forget anything about "technical debt" and other nasty stuff :)
<r​brunner7> Alright, do we have something to discuss today beyond reports and coordination?
<s​needlewoods> In regards of the second question [here](https://github.com/monero-project/monero/pull/9464#issuecomment-2511857932):
<s​needlewoods> rbrunner commented "Maybe we can get away with only offering the methods that address by key image in the Wallet API?"
<s​needlewoods> I think that's the right way to do it, if no one disagrees I'll remove the `freeze/thaw/is_frozen()` by index methods.
<r​brunner7> Did you check whether other methods already use that "access through index" in the Wallet API, SNeedlewoods ? That really looks quite brittle to me, as an approach.
<s​needlewoods> I think it's only used internally in wallet2
<joshbabb> +1
<r​brunner7> That's good, then we shouldn't introduce it now IMHO
<r​brunner7> Looks like we are through for today. Thanks everybody for attending, read you again next week!
<rottenwheel> +1
<a​rticmine> Thanks
<j​effro256> Thanks all
<s​needlewoods> thanks and cu
<j​berman> thanks squad
````


# Action History
- Created by: rbrunner7 | 2024-12-06T16:12:52+00:00
- Closed at: 2024-12-09T18:34:08+00:00
