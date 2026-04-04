---
title: 'Seraphis wallet workgroup meeting #40 - Monday, 2023-10-09, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/907
author: rbrunner7
assignees: []
labels: []
created_at: '2023-10-06T14:22:56+00:00'
updated_at: '2023-10-09T18:53:54+00:00'
type: issue
status: closed
closed_at: '2023-10-09T18:53:53+00:00'
---

# Original Description
On Monday, November 14 2022, we started with regular weekly meetings of the Seraphis wallet workgroup, and all interested parties from the community that want to join. Time is 18:00 UTC on each Monday. "Location" is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting here: https://github.com/monero-project/meta/issues/902

# Discussion History
## rbrunner7 | 2023-10-09T18:53:53+00:00
````
<r​brunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/907
<d​angerousfreedom> hello
<j​berman> hello
<r​brunner7> Anything to report? Was a quiet week here in the channel, and for me as well. Did almost nothing Monero wise.
<d​angerousfreedom> This week I cleaned up a bit my tx_history and I would like to invite you to [review](https://github.com/seraphis-migration/monero/pull/1) it. The tests are failing because it depends on the wallet2_basic (but a review could be done before it is merged). Of course I dont expect it to be perfect in the first try but comments about the functionality and the direction are very welcom<clipped 
<d​angerousfreedom> e. I wrote a summary and what each file does in the PR content. I also wrote the weak points and what needs to be addressed/discussed. For the moment I believe I have enough for the basic version of this component. Thank you in advance for any review.
<r​brunner7> Ok, will have a look, maybe Friday!
<d​angerousfreedom> Thanks!
<d​angerousfreedom> I also looked at the [transaction_class](https://github.com/seraphis-migration/wallet3/issues/7) issue and wrote the most basic naked version of a [variant](https://github.com/DangerousFreedom1984/seraphis_lib/commit/feaa255eedb3a9247f588c1595a2c15583c0fd57) so I could start playing with the blockchain files to understand it and to see where/how this generic class could be used/useful.
<r​brunner7> But of course jberman , with his larger knowledge of the Seraphis library than me right now, would also be a welcome reviewer!
<j​berman> Completed my final TODO's on background sync (PR 8619) and about to submit the changes, I appreciate the review :) Intending to move back to Seraphis work this week (fcmp's most likely)
<d​angerousfreedom> I will start doing the tasks described [here](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/409) for the next weeks (as it does not depend on someone's else work) while I wait some review and learn more about the blockchain files and node. I will start with the wallet initialization. I already tried to do something on this direction but now I believe I h<clipped 
<d​angerousfreedom> ave better understanding about how to build it in a modular way.
<d​angerousfreedom> I will try to review it this week too.
<r​brunner7> Splendid.
<j​berman> will take a look, nice progress dangerousfreedom
<r​brunner7> Any ETA for a PR for your scanning code already, jberman?
<d​angerousfreedom> Thanks jberman
<r​brunner7> Even if only for having a good look
<j​berman> hmm, I was going to prioritize fcmp's, but I can try to get a draft PR up for that on a timeline of 2-3 days. a completed PR I think would be 1-2 weeks of work
<r​brunner7> Yeah, maybe prepare a "Do not merge, only look" PR. Might influence how other people implement things and look at it.
<j​berman> Sounds good, sure will do that this week
<r​brunner7> Nice, thank you. I guess once you tunnel into that FCMP proofs you won't resurface any time soon :)
<r​brunner7> Anything specific to discuss? I guess most "action" will happen, if at all, in the MRL meeting in 2 days, regarding the Jamtis extensions
<r​brunner7> I wonder whether our decision process called "loose consensus" is up to the task to agree on a particular solution ...
<r​brunner7> Alright, seems that's it for today. Thanks for attending, until next week!
<j​berman> +1
<d​angerousfreedom> +1
````


# Action History
- Created by: rbrunner7 | 2023-10-06T14:22:56+00:00
- Closed at: 2023-10-09T18:53:53+00:00
