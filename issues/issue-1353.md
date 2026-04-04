---
title: 'Monero Tech Meeting #161 - Monday, 2026-03-16, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1353
author: rbrunner7
assignees: []
labels: []
created_at: '2026-03-13T17:00:45+00:00'
updated_at: '2026-03-16T19:47:42+00:00'
type: issue
status: closed
closed_at: '2026-03-16T19:47:42+00:00'
---

# Original Description
Location is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting [here](https://github.com/monero-project/meta/issues/1350).


# Discussion History
## rbrunner7 | 2026-03-16T19:47:42+00:00
````
<s​needlewoods> Meeting time. Hello everyone, unfortunately rbrunner7 can't run the meeting today and I'll try to sub for him.
<k​oe000> Hi
<s​needlewoods> Okay, what are your reports from last week?
<s​needlewoods> Me: mainly rewrote the `std::exception_ptr` system I presented [here](https://github.com/monero-project/monero/issues/10343#issuecomment-4033621058) to use new `enum ExtendedStatus` instead
<s​needlewoods> and `grep "\<m_wallet\>" src/wallet/wallet_rpc_server.cpp -c` now gives 87 results
<s​needlewoods> ping jberman
<k​oe000> Rereading old papers, in the middle of reading the carrot spec. Trying to convince stubborn people about nice things.
<jberman> +1
<j​berman> *waves* sorry for the delay
<s​needlewoods> Do you want to elaborate on these "nice things"?
<j​berman> Combined phases 1 & 2 of the propsoed FCMP++ audit integration plan into phase 1a & 1b, upstreamed PR's for 1b, and reached out to Cypher Stack to get a quote on starting with phase 1a & 1b: https://github.com/seraphis-migration/monero/issues/294
<koe000> +1
<sneedlewoods> +1
<k​oe000> That ‘FCMP++’ is a decidedly not-nice name (6 words, 8 syllables). That FCMP++ should be a distinct tx era instead of shoehorned into RingCT.
<j​berman> Also updated the FCMP++ integration documentation PR to match the latest: https://github.com/seraphis-migration/monero/pull/110
<k​oe000> Also that Carrot should be a new address format with more Jamtis features.
<s​needlewoods> too bad jeffro isn't here today
<k​oe000> I messaged him, he has an essay to read.
<sneedlewoods> +1
<s​needlewoods> Is there anything else you want to bring up?
<s​needlewoods> Or discuss today?
<k​oe000> Not me. Will continue looking at carrot. Also need to write a github issue for discussion about carrot wallet handling.
<s​needlewoods> Alright sounds good, I think we can close the meeting here, thanks everybody for attending, read you again next week.
<koe000> +1
<j​berman> thanks sneedle
<r​brunner7> Thanks a lot, SNeedlewoods , for running the meeting! You were only the second person ever to run one, beside me.
````


# Action History
- Created by: rbrunner7 | 2026-03-13T17:00:45+00:00
- Closed at: 2026-03-16T19:47:42+00:00
