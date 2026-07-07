---
title: 'Monero Tech Meeting #176 - Monday, 2026-07-06, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1416
author: rbrunner7
assignees: []
labels: []
created_at: '2026-07-03T14:27:11+00:00'
updated_at: '2026-07-06T18:34:51+00:00'
type: issue
status: closed
closed_at: '2026-07-06T18:34:51+00:00'
---

# Original Description
Location is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting [here](https://github.com/monero-project/meta/issues/1412).


# Discussion History
## rbrunner7 | 2026-07-06T18:34:51+00:00
````
<rbrunner7> Meeting time. Hello! monero-project/meta #1416
<sneedlewoods> hi
<jpk68> Hello
<jberman> waves
<rbrunner7> On to the reports from last week!
<rbrunner7> @dangerousfreedom left a report a while before this meeting, in this room. Looks like he made great progress. Not 100% what was planned, but still solid.
<sneedlewoods> Mostly reviews, also started to look into this (oxen-io/oxen-core #1466) refresh lock issue that selsta brought up in the last meeting, but with my limited knowledge I didn't spot any issue so far.
<jpk68> Me: worked on baking I2P support into the GUI, plus regular patches as normal; helped with testing Qt6 builds of the GUI
<rbrunner7> I myself did two passes through my Polyseed PR, based on review comments from 3 people (thanks to all!), and I could update with improved code.
<rbrunner7> Maybe @jeffro256 will find time for a re-review, or anybody else for a first review
<jberman> me: continuing handling upstream FCMP++ PR's, beta stressnet v2.1, and continuing finalizing investigation into sporadic observed double spends on stressnet
<rbrunner7> It's this here of course: monero-project/monero #10765
<rbrunner7> @jberman:monero.social: So these double-spends are still with you?
<rbrunner7> Seems to be a tough nut to crack :)
<jberman> @rucknium mentioned one was still observed one with a fix in place, and I haven't yet had a chance to dig into those logs. My initial take is that it's revealing multiple interconnected / related upstream bugs that only trigger on very rare occassion, that's exacerbated by stressnet
<rbrunner7> So this goes into a long row of things that broke when real pressure was applied to a Monero network ...
<rbrunner7> No "battle-tested" without any battle, lol
<jberman> essentially yes
<rbrunner7> Alright, seems that's about it regarding reports.
<rbrunner7> Do we have to discuss something this week beyond those?
<jeffro256> Howdy sorry I'm late
<rbrunner7> Right on time still to drop your report :)
<jeffro256> Not too much to report from me other then I'm still deep in reviewland
<rbrunner7> Ok, I guess that progress if you are not mostly producing more mountains of code anymore
<rbrunner7> Are any bigger programming jobs left at all on the way to FCMP++?
<rbrunner7> With emphasis on "bigger"
<selsta> I opened multiple PRs in regards to our test suite that would need review in case anyone has time
<rbrunner7> On the normal Monero repo? Somehow can't see multiples
<jeffro256> @rbrunner7: Multisig, HW
<rbrunner7> Ah, no, just did not go back far enough, sorry for the false alarm
<jeffro256> hot/cold is mostly done, tx proofs are mostly done
<jeffro256> consensus code is mostly done
<jeffro256> the rest of Carrot is mostly done
<jeffro256> HW support is mostly done on the hot side, the bulk of the work left for HW support is on the HW side
<jeffro256> So for the core repo, mainly Multisig which Koe is working on
<rbrunner7> Sounds good
<jpk68> Does multisig require a separate audit?
<sneedlewoods> @rbrunner7: too slow, but I think selsta is referring to these
<sneedlewoods> 10818 10820 10823 10826 10844 10855
<rbrunner7> @jpk68: Maybe depends on the definition of "require" ... I am pessimistic that we would find the funds to do a proper audit there, but that's only MHO.
<jeffro256> @jpk68: If we were to audit yes
<jeffro256> AKA it's not under the scope of any currently contracted or planned audit
<rbrunner7> It's "experimental", all is good :)
<sneedlewoods> +1
<jpk68> +1
<rbrunner7> Maybe we will end up using the improved Rust implementation of a much more solid multisig approach, one that does not result in 1000 messages passed back and forth if you want 7 signers or so ....
<rbrunner7> Alright, looks like we are through for today. Thanks everybody for attending, read you again next week!
<sneedlewoods> thanks everyone, cu
<jeffro256> Thanks everyone !
<jpk68> Thanks :))
````


# Action History
- Created by: rbrunner7 | 2026-07-03T14:27:11+00:00
- Closed at: 2026-07-06T18:34:51+00:00
