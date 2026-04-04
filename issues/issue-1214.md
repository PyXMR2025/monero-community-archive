---
title: 'Monero Tech Meeting #123 - Monday, 2025-06-02, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1214
author: rbrunner7
assignees: []
labels: []
created_at: '2025-05-30T15:05:19+00:00'
updated_at: '2025-06-02T18:17:18+00:00'
type: issue
status: closed
closed_at: '2025-06-02T18:17:18+00:00'
---

# Original Description
Location is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting [here](https://github.com/monero-project/meta/issues/1210).


# Discussion History
## rbrunner7 | 2025-06-02T18:17:18+00:00
````
<r​brunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/1214
<j​berman> *waves*
<r​brunner7> Alright, maybe fewer participants than usual. What is there to report from last week?
<r​brunner7> For the record: SNeedlewoods reported earlier that they are still making their way through simplewallet, converting to the Wallet API
<r​brunner7> I myself made my first PR since quite a long time: https://github.com/monero-project/monero/pull/9939
<j​berman> Opened this PR to fix tests and am working through some bugs for some failing tests atm: https://github.com/seraphis-migration/monero/pull/50
<r​brunner7> Do you have good coverage with the existing tests?
<r​brunner7> I mean, not too many things really particular to FCMP++ and Carrot
<moneromooo> What is (are? ) the benefit of changing simplewallet to use the wallet API ?
<j​berman> I'd say yes, I'm working through functional tests at the moment
<moneromooo> nvm, I'll ask later
<r​brunner7> moneromooo: The "endgame" that we plan is moving everything away from wallet2.h to the Wallet API to get the freedom to re-implement the wallet
<j​berman> Some more context https://github.com/seraphis-migration/wallet3/issues/64
<moneromooo> So the wallet api will no longer be a layer above wallet2 then ?
<r​brunner7> Thanks, I knew I wrote something deep in the past about that :)
<r​brunner7> Ideally, yes.
<moneromooo> Ah, yes, wallet3. Forgot aout this. Makes sense now.
<r​brunner7> Maybe the wallet implementation itself, or a layer above ... something else, hopefully better structured
<r​brunner7> So nice that the existing functional tests for transactions are still useful and have results, i.e. help you find bugs
<jberman> +1
<r​brunner7> But I guess at some point some more specific tests for the new tech will be added?
<j​berman> The integration brings a lot of major changes internally that these tests are hitting because they are wider in scope
<j​berman> We've also been testing specific functionality as it's been added along the way (e.g. my tree code has extensive unit testing), with more planned too
<j​berman> jeffro256: also has added hefty amount of Carrot specific unit tests too
<j​berman> 8 new "carrot_" unit test files
<r​brunner7> Sounds solid.
<r​brunner7> I guess that's the way with really complex code.
<r​brunner7> Alright, if you don't have something special to bring up, maybe we can already wrap up the meeting.
<r​brunner7> Thanks for attending, read you again next week!
````


# Action History
- Created by: rbrunner7 | 2025-05-30T15:05:19+00:00
- Closed at: 2025-06-02T18:17:18+00:00
