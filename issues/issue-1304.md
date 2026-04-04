---
title: 'Monero Tech Meeting #148 - Monday, 2025-12-01, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1304
author: rbrunner7
assignees: []
labels: []
created_at: '2025-11-28T06:54:17+00:00'
updated_at: '2025-12-01T18:25:52+00:00'
type: issue
status: closed
closed_at: '2025-12-01T18:25:52+00:00'
---

# Original Description
Location is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting [here](https://github.com/monero-project/meta/issues/1300).


# Discussion History
## rbrunner7 | 2025-12-01T18:25:52+00:00
````
<rbrunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/1304
<j​berman> *waves*
<s​needlewoods> hey
<r​brunner7> Alright, let's start with the reports
<j​effro256> Howdy
<s​needlewoods> not much, some small local fixes (e.g. review comment from iamamyth), will push when there is more
<s​needlewoods> also noted something related to the issue where the CLI prints `Height x / y` in the case when we create a transaction and wait for confirmation,
<s​needlewoods> we use `pauseRefresh()` [src](https://github.com/monero-project/monero/blob/41ad5238a05dfc1867469eff8336ade312598cbe/src/wallet/api/wallet.cpp#L2472-L2479) in `createTransactionMultDest()` [src](https://github.com/monero-project/monero/blob/41ad5238a05dfc1867469eff8336ade312598cbe/src/wallet/api/wallet.cpp#L1622), but `m_refreshEnabled` gets set to `true` after a while. IIUIC this `LOCK_REFRESH()` [src](https://github.com/monero-project/monero/blob/41ad5238a05dfc1867469eff8336ade312598cbe/src/wallet/api/wallet.cpp#L61-L72) macro from jberman may be a better fit do make sure this doesn't happen, testing at this moment
<s​needlewoods> nah, didn't work lol
<j​effro256> Made a tweak to Carrot account derivation in the spec https://github.com/jeffro256/carrot/pull/6, wrote a concrete PQ turnstile design around it https://gist.github.com/jeffro256/146bfd5306ea3a8a2a0ea4d660cd2243, and implemented it in the C++ lib https://github.com/seraphis-migration/monero/pull/250
<r​brunner7> Sounds like quite some edge case
<j​berman> me: opened a new CCS proposal, continuing investigating sync issues reported in the stressnet channel (a newly reported connection drop issue [244] & slower than expected sync on one of the stressnet participant's machine [246]), then stressnet release v1.5. I didn't have much availability the last week for thanksgiving, back at 100% availability now
<j​effro256> Also sending out quote requests for a carrot_core code audit, so we can get that audit out of the way
<s​needlewoods> I think creating transaction is not the only place where this happens, but it's easy to reproduce for not
<s​needlewoods> for now*
<r​brunner7> I see
<r​brunner7> jeffro256: Those turnstiles will get important if/when somebody comes along with a working quantum computer? If yes, isn't it awfully early to program something already now? Or is this to verify / prove the design?
<j​effro256> This issue is that if you don't prepare for it now, you can't use it later. The tweaks were relatively small and provable that hashes didn't bind to anything less than they were currently binding
<j​effro256> took a couple hours at most
<r​brunner7> Ah, ok, imagined this quite a bit bigger then
<j​effro256> It would be nice to validate that the design can do what it claims it can tho
<r​brunner7> Yes
<r​brunner7> I saw from discussions over last week that there are still quite differing opinions about the future design of fees and related issues like block size growth limits. Does that hold up anything right now? Guess not.
<r​brunner7> That goes on for quite a while now, no? :)
<j​effro256> Right now? Probably holding up an accurate beta stressnet
<j​effro256> some of the fee policy can be deciding in relay fees, but the scaling rules as it relates to block subsidy penalty need to be decided in consensus
<r​brunner7> And if you change such growth parameters later, that will invalidate tests that you do now.
<r​brunner7> I guess sometimes reaching consensus takes time, it's in the nature of complex questions. I hope that the dust will soon settle.
<r​brunner7> Alright, is there something to discuss beyond these reports?
<j​effro256> Yes, if we want an accurate view of how mainnet will scale, we need to know the paramaters before starting a new stressnet IMO
<j​berman> also going to spend some more time focusing on that discussion soonish
<r​brunner7> That would certainly be useful; seems to me not many people have the necessary background knowledge to take part. I certainly don't.
<r​brunner7> I don't know much more than "It's complicated" :)
<r​brunner7> I think we can close the meeting here. Thanks everybody for attending, read you again next week!
<s​needlewoods> thank you
````


# Action History
- Created by: rbrunner7 | 2025-11-28T06:54:17+00:00
- Closed at: 2025-12-01T18:25:52+00:00
