---
title: 'Monero Tech Meeting #84 - Monday, 2024-08-26, 18:00'
source_url: https://github.com/monero-project/meta/issues/1062
author: rbrunner7
assignees: []
labels: []
created_at: '2024-08-23T15:30:09+00:00'
updated_at: '2024-08-26T18:32:25+00:00'
type: issue
status: closed
closed_at: '2024-08-26T18:32:25+00:00'
---

# Original Description
Location is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting [here](https://github.com/monero-project/meta/issues/1058).


# Discussion History
## rbrunner7 | 2024-08-26T18:32:25+00:00
````
<r​brunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/1062
<s​needlewoods> hey
<j​effro256> howdy
<r​brunner7> dangerousfreedom wrote he won't be with us today, and next week neither
<s​needlewoods> I'm short on time today too
<r​brunner7> Ok, then already on to the reports :)
<s​needlewoods> Just pushed https://github.com/monero-project/monero/compare/master...SNeedlewoods:seraphis_wallet:x_api_add_new_functions
<s​needlewoods> If you search for `QUESTION`, those are TODOs for y'all :D
<s​needlewoods> That are things I'm stuck at or would like to get consensus on.
<s​needlewoods> Feedback is very much appreciated.
<s​needlewoods> Also some direct questions:
<s​needlewoods> 1. Should I already change calls to `wallet2` functions in this PR for those that are now available in the API? E.g. like it's done here:
<s​needlewoods> https://github.com/monero-project/monero/compare/master...SNeedlewoods:seraphis_wallet:x_api_add_new_functions#diff-fcae134993cca2b6f1e887a60638f226ab00165e30bd4d326c17f0a58e11871fL749-R753
<s​needlewoods> 2. In the API are a few places where IMO the error handling is funky or completely missing, but that's a TODO for after this PR I would say. I'd still like to get your opinions on the following:
<s​needlewoods>    - In places where we `setStatusError()`, should we also _always_ `LOG_ERROR()`?
<s​needlewoods>    - Should I add detailed error messages like e.g. [this](https://github.com/monero-project/monero/compare/master...SNeedlewoods:seraphis_wallet:x_api_add_new_functions#diff-fcae134993cca2b6f1e887a60638f226ab00165e30bd4d326c17f0a58e11871fR3166) to functions where I just did `setStatusError(e.what());` like e.g. [here](https://github.com/monero-project/monero/compare/master...SNee<clipped m
<s​needlewoods> dlewoods:seraphis_wallet:x_api_add_new_functions#diff-fcae134993cca2b6f1e887a60638f226ab00165e30bd4d326c17f0a58e11871fR3151)? The later one is from my perception more frequently used, unfortunately.
<j​berman> *waves*
<r​brunner7> For point 1), you mean *within* the API code itself?
<s​needlewoods> (I have to press "Load diff" on wallet.cpp for the links to work properly)
<s​needlewoods> yes
<r​brunner7> Hmm, why not. Would give some nice additional testing, I would say.
<sneedlewoods> +1
<r​brunner7> For a good opinion regarding 2) I have to take a look first. Will try to find time this week.
<s​needlewoods> There aren't many such cases like that iirc, I haven't done much private functions yet.
<r​brunner7> I think your "problem" with the links is just GitHub not loading large files as default, perfectly normal and harmless
<s​needlewoods> Just mentioned it in case you think I posted the same link three times lol
<r​brunner7> Ah, I see
<j​berman> +1 to yes for question 1, progress :)
<r​brunner7> By the way, how did it go with some more complicated new stuff, where you wanted to get some hints e.g. from Woodser's library? Did that work out?
<j​berman> on #2a, quick glance it looks like the pattern currently used which makes sense is to just LOG_ERROR when it's not a result of user error (e.g. a daemon response shouldn't fail and is worth a LOG_ERROR, mis-typed seed isn't)
<sneedlewoods> +1
<s​needlewoods> I only "came up" with a solution for `wallet2::multisig_tx_set`, because that's already covered by the APIs `PendingTransaction` the other transfer/transaction/payment objects still causing me a headache tbh.
<r​brunner7> So we will find those as the mentioned "QUESTION" marks? :)
<s​needlewoods> Yes, you should if I didn't mess up
<r​brunner7> Alright, will probably get a headache as well ...
<r​brunner7> Problem, at least for me, often is that you can do something a hundred different ways, and I get blocked and can't decide
<r​brunner7> Alright, any more reports?
<s​needlewoods> None from me
<r​brunner7> Anything to discuss on the technical side?
<r​brunner7> Beyond that wallet API I mean
<j​berman> on #2b, I think use your best judgment depending on the error case. The pattern of `setStatusError("short description of the failure: " + e.what())` seems reasonable to me. the goal is to get a quick solid idea of the error from the message
<s​needlewoods> Agree, thanks for the feedback
<j​effro256> Usually, the approach of a preformatted message is more helpful to the person debugging, but it can sometimes lose information of the inner scope if the `e.what()` is not also dumped.
<s​needlewoods> Alright, gtg now, if anyone has something more to discuss I try to respond ASAP, thanks everyone and cu
<r​brunner7> I have only a little question left: Does anybody have a strong opinion against calling these meetings *Tech meetings* into the future, and also giving this room a second name / title of *Monero Tech*?
<r​brunner7> We have some other proposals in the discussion issue, but as far as I concerned I found nothing really convincingly better ...
<j​effro256> Yeah I'd be fine with that
<j​effro256> "No Wallet Left Behind" sounds so heroic though
<r​brunner7> Maybe, but no wallet is in danger of really being left behind, that's the problem :)
<r​brunner7> At least not yet
<r​brunner7> Alright, room is open for anybody to voice their oposition if there is such
<r​brunner7> I think we can close for today. Thanks for attending, read you next week!
<j​effro256> Thanks, all
````


# Action History
- Created by: rbrunner7 | 2024-08-23T15:30:09+00:00
- Closed at: 2024-08-26T18:32:25+00:00
