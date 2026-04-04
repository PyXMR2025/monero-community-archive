---
title: 'Monero Tech Meeting #109 - Monday, 2025-02-24, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1160
author: rbrunner7
assignees: []
labels: []
created_at: '2025-02-23T06:38:36+00:00'
updated_at: '2025-02-24T18:43:15+00:00'
type: issue
status: closed
closed_at: '2025-02-24T18:43:12+00:00'
---

# Original Description
Location is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting [here](https://github.com/monero-project/meta/issues/1157).

# Discussion History
## rbrunner7 | 2025-02-24T18:43:12+00:00
````
<r​brunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/1160
<j​effro256> Howdy
<j​berman> *waves*
<s​yntheticbird> Hi
<s​needlewoods> Hello
<r​brunner7> Alright, what is there to report from last week?
<j​berman> Just shared my 2nd CCS update: https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/527#note_28861
<j​berman> Highlights: FCMP++ tx construction / verification are set up, FCMP++ optimization competition is set up ready for review, and continuing my re-review on PR 9135
<sneedlewoods> +
<jeffro256> +1
<rottenwheel> +1
<r​brunner7> Nice
<r​brunner7> Progressing smoothly
<j​berman> *thumbs up*
<j​effro256> Really getting into the weeds with Carrot tx construction / HW devices. Trying to set up an API that will last a long time and is reusable across different applications
<jberman> +1
<sneedlewoods> +1
<rottenwheel> +1
<j​effro256> I think I'm a lot happier with where the API is compared to a couple weeks ago, but my development kinda stopped for a while until I got this right
<rottenwheel> +1
<s​needlewoods> I learned that I'm not very good at giving estimates. Still working on the passwords in GUI, I think ([this way](https://stackoverflow.com/questions/44913102/nullify-qstring-data-bytes)) to wipe passwords may work from the tests I've done so far, but want to further confirm that and found some more cached passwords in the wizard for create/restore and I want to investigate the second password field when you enter a new password.
<r​brunner7> Regarding SNeedlewoods 's big Wallet API PR: About 2 or 3 weeks ago there was a discussion, I think over in -dev, that the rule of thumb "two reviews for every important PR before merge" will get followed more strictly. In this regard this here would need a second review, alongside mine: https://github.com/monero-project/monero/pull/9464
<r​brunner7> I myself probably have a small re-review open there, after a force-push
<s​needlewoods> Two reviews for an important PR seems not much, but I guess it depends on who is doing the review
<r​brunner7> jeffro256: "Carrot tx construction / HW devices" Do you own such HW devices, or are you operating from info you get from today's interfaces? And any contacts to the devs of the manufacturers until now?
<j​effro256> SNeedlewoods:  Perhaps you're beginning to realize how slow development moves in Monero sometimes ;)
<r​brunner7> Yeah, reviews can be a bottleneck ...
<j​effro256> That wallet API PR has been on my todo list for a while, I promise I'm not neglecting it
<rbrunner7> +1
<sneedlewoods> +1
<jberman> +1
<rottenwheel> +1
<r​brunner7> Well, it's not yet complete for review for long
<s​needlewoods> I don't blame you, you always have many important things you're working on
<j​berman> thank you jeffro256
<s​needlewoods> I think vthor said it nicely, something like: the development in Monero moves extremely fast and extremely slow at the same time
<r​brunner7> Also how slowly things sometimes diffuse from master to some release branch
<r​brunner7> Ok. Something to discuss today beyond these reports?
<j​effro256> I own both Ledger and Trezor. I started with a free Ledger device, but realized how shady they were and am moving to a Trezor. So I'll be able to test on both eventually, but I'm not actually writing the implementation yet. Because Carrot changes how tx outputs are derived from addressed, and FCMP++ changes the proofs we use to spend, the HW device interface needs a complete overhaul basically. There's also HW device security features for spending Carrot enotes that haven't yet existed with spending legacy enotes, and I want to document those checks and give support to those developers
<rottenwheel> +1
<j​effro256> Until recently, I hadn't yet nailed down an API I was happy with, but now that I have, then plan is to talk to HW developers soon to get feedback on how it can be improved, etc. I have their contact info, but haven't reached out yet.
<rottenwheel> +1
<r​brunner7> Sounds very good, jeffro256 . We really don't want to lose those HW wallets
<j​effro256> There
<j​effro256> 's a few things that bug me about our HW interfaces today, one of them being two different APIs for tx construction:"cold signing" versus "live device signing". They really should be one in the same since they more or less so the same thing cryptographically
<j​effro256> There's also state required against calls when there shouldn't be IMO which makes writing device-side apps harder
<r​brunner7> Single API for both sounds reasonable. Probably "historic" reasons they are separate now, I would guess.
<r​ucknium> Could the integrated address display issue be fixed in this revision?
<j​effro256> Yeah I think it was just the way the code came together: I think "cold" signing came after the `hw::device` interface, and they just tacked on a new API instead of refactoring, which makes sense at the time
<r​brunner7> Good point, Rucknium . If we go for a new API anyway, we can hand the HW wallet the necessary info display correctly!
<r​brunner7> *to display correctly
<rottenwheel> +1
<j​effro256> Yes lmao I had this issue in mind when writing the API for Ledger since that issue pisses me off. It should be easier to write the code for that on the device side with this API
<j​effro256> Technically it's already possible to fix it, since Trezor has done it, the Ledger devs are just lazy on this issue
<j​effro256> Which is incredibly important IMHO
<r​brunner7> Ah, I thought they don't receive the necessary info over the current API to do so
<j​effro256> But yeah this API makes it super simple for them
<rucknium> +1
<r​brunner7> Well, to be fair, those devs have a *lot* of coins to support
<j​effro256> They do, but they would more or less have to rewrite the flow of their application
<r​brunner7> Mostly ERC20 and Bitcoin forks probably, but still
<r​brunner7> Making it "super simple" might indeed go a long way with them :)
<r​brunner7> Ok, I think we can close the meeting proper here. Thanks everybody for attending, read you again next week!
<s​needlewoods> Thanks everyone
<j​effro256> The "live device signing" type of tx construction flow works by making the HW device basically build each component, whereas the "cold signing" tx construction flow works by creating data structures which allow tx to be reproduced meaningfully/verifiably. I think Trezor uses the latter flow for tx construction. The "cold signing" technique is almost always better, but it requires  a bit more planning to get right.
<j​effro256> The "cold signing" type of API also requires fewer round trips, which can make a performance difference in some systems
````


# Action History
- Created by: rbrunner7 | 2025-02-23T06:38:36+00:00
- Closed at: 2025-02-24T18:43:12+00:00
