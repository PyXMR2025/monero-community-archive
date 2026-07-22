---
title: 'Monero Tech Meeting #178 - Monday, 2026-07-20, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1427
author: rbrunner7
assignees: []
labels: []
created_at: '2026-07-19T04:45:30+00:00'
updated_at: '2026-07-20T19:31:49+00:00'
type: issue
status: closed
closed_at: '2026-07-20T18:21:52+00:00'
---

# Original Description
Location is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting [here](https://github.com/monero-project/meta/issues/1422).


# Discussion History
## rbrunner7 | 2026-07-20T18:21:52+00:00
````
<rbrunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/1427
<sneedlewoods> hey
<selsta> hi
<rbrunner7> Holiday season meeting :)
<rbrunner7> Anyway, any reports from last week?
<rbrunner7> @jpk68 left this yesterday: "My updates so far include testing the GUI for Qt6 migration, plus minor patches as usual, and pestering the i2pd developer to fix a few bugs/issues"
<sneedlewoods> mainly worked on your review comments on the wallet-rpc PR
<rbrunner7> I could fix a fat bug in the Polyseed PR thanks to selsta
<sneedlewoods> +1
<rbrunner7> And yes, that review
<rbrunner7> The Wallet RPC server is almost a new program now
<selsta> rbrunner7: disclosure, the latest chatgpt model found it and i later validated it, that would have been a bad one if not caught
<rbrunner7> Oh. Interesting.
<rbrunner7> Sure, yeah. We wouldn't want to trash all existing multisig wallets
<rbrunner7> Beside this hit, where there many false alarms in that review?
<selsta> honestly the models are quite good at not hallucinating at this point, it did not find any false alarms
<rbrunner7> If those models will be able to help with reviews, that will be a net win
<rbrunner7> I guess most people here are quite sceptical about incorporating code written by them, but reviews are a whole different story
<selsta> definitely, as long as we don't become complacent in skipping human reviews, but it's useful as an extra layer
<jeffro256> Howdy
<UkoeHB> hi, no updates<rbrunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/1427
<sneedlewoods> hey
<selsta> hi
<rbrunner7> Holiday season meeting :)
<rbrunner7> Anyway, any reports from last week?
<rbrunner7> @jpk68 left this yesterday: "My updates so far include testing the GUI for Qt6 migration, plus minor patches as usual, and pestering the i2pd developer to fix a few bugs/issues"
<sneedlewoods> mainly worked on your review comments on the wallet-rpc PR
<rbrunner7> I could fix a fat bug in the Polyseed PR thanks to selsta
<sneedlewoods> +1
<rbrunner7> And yes, that review
<rbrunner7> The Wallet RPC server is almost a new program now
<selsta> rbrunner7: disclosure, the latest chatgpt model found it and i later validated it, that would have been a bad one if not caught
<rbrunner7> Oh. Interesting.
<rbrunner7> Sure, yeah. We wouldn't want to trash all existing multisig wallets
<rbrunner7> Beside this hit, where there many false alarms in that review?
<selsta> honestly the models are quite good at not hallucinating at this point, it did not find any false alarms
<rbrunner7> If those models will be able to help with reviews, that will be a net win
<rbrunner7> I guess most people here are quite sceptical about incorporating code written by them, but reviews are a whole different story
<selsta> definitely, as long as we don't become complacent in skipping human reviews, but it's useful as an extra layer
<jeffro256> Howdy
<UkoeHB> hi, no updates
<UkoeHB> @jeffro256 what's the paper/section for https://github.com/monero-project/monero/pull/9828 ?
<jeffro256> Hi, working on some speedups and bug fixes recently: https://github.com/monero-project/monero/pull/10605 and https://github.com/monero-project/monero/pull/10924. Beefed up testing infra in preperation for the Carrot/FCMP++ test merges: https://github.com/monero-project/monero/pull/10934.
<ofrnxmr> +1
<ofrnxmr> @rbrunner7: Using them to sanity check your own review, or pre-review before submission is nice as well
<jeffro256> UkoeHB: It's mainly just an algebraic conversion that you can do if you know the equations for both curves 
<rbrunner7> @jeffro256: You think you can slip in somewhere a second review pass of my Polyseed PR? It ripened quite a bit since your initial review, there are also a few questions.
<jeffro256> But I can try to find a more official source 
<jeffro256> @rbrunner7: That PR is on my TODO list. I think I should be able to give it another pass this week 
<rbrunner7> Splendid!
<jeffro256> Thanks for the reminder 
<rbrunner7> Seems we are through with the reports. Anything special to discuss or decide today?
<rbrunner7> Does not seem to be the case. So I think we can close already for today. Thanks for attending, read you again next week!
<jeffro256> UkoeHB: Do you want me to add it into the code as a comment?
<UkoeHB> sure that would be helpful for future readers
<sneedlewoods> Thanks everyone
<jeffro256> How about linking RFC 7748?
<jeffro256> Section 4.1 of https://www.rfc-editor.org/rfc/inline-errata/rfc7748.html
<UkoeHB> looks appropriate
<jberman> Apologies for missing. My udpate is continuing the same: upstream FCMP++ integration PR's and continuing down the rabbit hole to solve the sporadic double spends on stressnet
````

# Action History
- Created by: rbrunner7 | 2026-07-19T04:45:30+00:00
- Closed at: 2026-07-20T18:21:52+00:00
