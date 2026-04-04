---
title: 'Monero Tech Meeting #101 - Monday, 2024-12-30, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1132
author: rbrunner7
assignees: []
labels: []
created_at: '2024-12-27T15:38:46+00:00'
updated_at: '2024-12-30T18:20:03+00:00'
type: issue
status: closed
closed_at: '2024-12-30T18:20:03+00:00'
---

# Original Description
Location is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting [here](https://github.com/monero-project/meta/issues/1131).

# Discussion History
## rbrunner7 | 2024-12-30T18:20:03+00:00
````
<r​brunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/1132
<s​needlewoods> Hey
<r​brunner7> We got info from jeffro256 earlier on: "Sorry, I will not be able to make the meeting today. Not too much to report besides continuing to work on what I've been working on"
<j​berman> *waves*
<r​brunner7> Alright, anything to report despite Christmas in between the last meeting and this one?
<s​needlewoods> I've been trying to catch up with all the merges, also rebased my PR and made some progress https://github.com/monero-project/monero/pull/9464
<r​brunner7> Yeah, rebasing for a longer running PR is always much fun :)
<j​berman> I completed the faster torsion check impl in C/C++ (re-implemented kayabanerve 's rust impl). On my machine it's benchmarking ~55% faster than the initial torsion clear, which should speed up tree building by ~30-40% (affects both daemon sync and the current wallet sync impl that builds the tree locally). Working on integrating the faster torsion check into tree building now, then<clipped messag
<j​berman>  moving back over to constructing FCMP++ txs
<j​berman> Source branch: https://github.com/j-berman/monero/commits/torsion-check/
<r​brunner7> Amazing that this torsion thing is such a large percentage of the total processing time there. So good news with that speedup!
<j​berman> yep, it was the slowest part of tree building before this change
<r​brunner7> Is this new way to do this the result of some recent research, a "new invention" so to say?
<j​berman> Checking the date on the paper
<j​berman> Paper from 2 years ago: https://eprint.iacr.org/2022/1164.pdf
<rbrunner7> Interesting, thanks
<j​berman> kayabanerve has mentioned we'd want an academic review on the approach as well, similar to what we've been doing for FCMP++ research tasks
<r​brunner7> Sounds like a good idea, if indeed nobody reviewed the paper yet
<r​brunner7> Do we have anything to discuss today beyond reports? Guess not, given the slow times
<r​brunner7> No MRL meeting either last week ...
<j​berman> nothin from me
<s​needlewoods> Not from me, I still appreciate feedback on the Wallet API, if I don't know how to continue I'll work on tests
<r​brunner7> Noted.
<r​brunner7> So read you again in 2025, (maybe) the year of the history-making hardfork to FCMP++. Thanks for attending!
<sneedlewoods> +1
<jberman> +1
<s​needlewoods> thanks, cu
```


# Action History
- Created by: rbrunner7 | 2024-12-27T15:38:46+00:00
- Closed at: 2024-12-30T18:20:03+00:00
