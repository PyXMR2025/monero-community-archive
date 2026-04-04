---
title: 'Seraphis wallet workgroup meeting #73 - Monday, 2024-06-03, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1016
author: rbrunner7
assignees: []
labels: []
created_at: '2024-05-31T18:03:48+00:00'
updated_at: '2024-06-03T18:34:26+00:00'
type: issue
status: closed
closed_at: '2024-06-03T18:34:26+00:00'
---

# Original Description
On Monday, November 14 2022, we started with regular weekly meetings of the Seraphis wallet workgroup, and all interested parties from the community that want to join. Time is 18:00 UTC on each Monday. "Location" is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting here: https://github.com/monero-project/meta/issues/1013

# Discussion History
## rbrunner7 | 2024-06-03T18:34:26+00:00
````
<r​brunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/1016
<jberman> *waves*
<s​needlewoods> hello
<r​brunner7> First a comment about next Monday, today in 1 week: I propose to skip that meeting because not much will probably happen this week because of Konferenco, and next meeting would be in 2 weeks.
<s​needlewoods> alright
<jberman> +1 from me
<r​brunner7> Ok. I won't be there this year, by the way.
<r​brunner7> Maybe next year
<jberman> same for me
<r​brunner7> Alright, any reports from last week?
<jberman> Update: was mostly recovering from being sick last week, nothing to report. Back 100% this week. Working on the trim_tree algo for fcmp's
<s​needlewoods> me: finished the comments for `Wallet` in `wallet2_api.h` https://github.com/SNeedlewoods/seraphis_wallet/blob/afe5049be382e55ca0019764d45b6f03a3b48a3c/src/wallet/api/wallet2_api.h#L428
<r​brunner7> When I reviewed jberman's incremental sync PR for hopefully the last time I couldn't help thinking "My, how much we will have to put into our new wallet to just reach feature-parity again"
<s​needlewoods> and put a little more effort into unit_tests, here is the diff with monero-project/monero https://github.com/monero-project/monero/compare/master...SNeedlewoods:seraphis_wallet:x_api_1_definitions
<r​brunner7> Splendid! I guess that took quite some time to write
<jberman> yep, deprecating and replacing wallet2 is a large task
<r​brunner7> (I refer to the comments)
<s​needlewoods> it's been quite an effort, but also good learning experience
<s​needlewoods> you can have a quick look at the first link I posted, imo it's much cleaner now and will hopefully be more fun to work with in the future
<r​brunner7> Ok, will try to find time. Might become Friday, or even Sunday
<sneedlewoods> +1
<r​brunner7> If you reorder methods, won't that give some quite hard-to-read and confusing PRs?
<r​brunner7> Or are there anyway so many changes that it will be hard to see correspondences?
<s​needlewoods> probably, that's why I didn't reorder everything so far, just some things where I felt it was necessary
<s​needlewoods> and yes, I think there will be enough that need to be added that it comes close to a full rewrite
<r​brunner7> Anyway, I guess if we go for such things better to pull that through now without mercy, so that after this cut things get incremental again
<r​brunner7> jberman, what's your gut feeling here?
<jberman> lean towards not reordering unless there's a really good reason
<r​brunner7> "where I felt it was necessary" Do you have striking examples?
<s​needlewoods> let me see, one sec
<r​brunner7> Maybe some ordering becomes untenable if you add much new things
<r​brunner7> Well, maybe you can go ahead, we look at the result, best case we agree that improved order is nicer than having few differences in the PR, worst thing you have to restore the old order?
<r​brunner7> Sometimes you really have to look at the code to decide such things
<s​needlewoods> that sounds good to me
<r​brunner7> Some turbulences are probably unavoidable :)
<s​needlewoods> sorry I can't find an exact example right now, but a general point for the reordering was that imo `wallet.h`, `wallet.cpp` and `wallet2_api.h` should have the same ordering
<r​brunner7> I think we are lucky that we found somebody who goes through this with motivation and patience. I think a complete API will be a big win.
<r​brunner7> Sounds reasonable .... code probably "degenerated" over time.
<s​needlewoods> and imo we should become more strict in general for future PRs, to not add to much chaos, e.g. his PR alone has both snake case and camel case as params and uses different styles for bracktes https://github.com/monero-project/monero/commit/774a21394ab95bb3303bb99beb236570bafd5731
<r​brunner7> Woah there, that's almost archeology ... pre-biblical Monero times :)
<r​brunner7> Yeah, devs often considerably underestimate how long their code will live, and how many eyes will be forced to read it over the years
<s​needlewoods> maybe it's just OCD, but I think working with clean code is more fun and more producitve
<r​brunner7> I am fully with you there.
<jberman> cool with me
<r​brunner7> Ok. Anything general to discuss today? Probably not, with only the 3 of us :)
<r​brunner7> And some lurkers maybe
<jberman> nothin from me
<s​needlewoods> I have some very specific questions in `TODO` comments, but nothing urgent
<s​needlewoods> will continue with comments for the other structs (16 more to go iirc) in `wallet2_api.h`, which will hopefully be done until next meeting
<r​brunner7> Sounds good.
<r​brunner7> Thanks then for attending, read you again in 2 weeks this time.
<s​needlewoods> thank you both, cu
<j​berman> thanks
````

# Action History
- Created by: rbrunner7 | 2024-05-31T18:03:48+00:00
- Closed at: 2024-06-03T18:34:26+00:00
