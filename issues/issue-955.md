---
title: 'Seraphis wallet workgroup meeting #53 - Monday, 2024-01-15, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/955
author: rbrunner7
assignees: []
labels: []
created_at: '2024-01-12T17:26:47+00:00'
updated_at: '2024-01-15T18:35:55+00:00'
type: issue
status: closed
closed_at: '2024-01-15T18:35:54+00:00'
---

# Original Description
On Monday, November 14 2022, we started with regular weekly meetings of the Seraphis wallet workgroup, and all interested parties from the community that want to join. Time is 18:00 UTC on each Monday. "Location" is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting here: https://github.com/monero-project/meta/issues/953

# Discussion History
## rbrunner7 | 2024-01-15T18:35:54+00:00
````
<r​brunner7> Meeting in 1 hour
<j​berman> I won't be able to make the meeting today either, but update: completed the tasks I set out to complete on monero-serai (aimed at squashing all fingerprints which incidentally led me to identify a couple edge case fingerprints in the Seraphis lib: https://github.com/UkoeHB/monero/issues/27), and collaborated with kayabanerve to progress on full chain membership proofs. I have momentum on fcmp's and am planning to continue there
<k​ayabanerve> The value of alternative implementations :)
<j​berman> On my work on fcmp's: we implemented a clean functioning high level API to call `setup`, `prove`, and `verify`. I also started looking through areas that would need to change in the Seraphis lib for fcmp's using a new curve (to support a curve cycle) and the amount of changes seemed large, when my initial goal is strictly to demonstrate constructing fcmp's using the Seraphis protocol.
<j​berman> After discussing with @kayabaNerve, it seemed the most straightforward path would be to implement a very rough PoC that initially sticks with ed25519 for all Seraphis/Jamtis pub keys, by implementing fcmp's using a tower cycle using Liam Eagen's bulletproof25519 curve in which its scalar field is Ed25519's field element field. Once that's demonstrated and a Seraphis tx with fcmp's
<j​berman> has been constructed using the Seraphis lib, we could then build on top of that higher level API and isolate the sections of code that would need to change for switching curves to support a curve cycle, which imo will make implementation smoother and easier to review. The initial PoC I'm working on with the ed25519 <> bulletproof25519 tower cycle would explicitly be insecure
<j​berman>  and (very) inefficient, but paves a path toward the more efficient curve cycle (a tower cycle would double proof sizes, increase verification time, and limit future scalability enhancements)
<j​berman> Not a tower cycle* just a tower
<r​brunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/955
<r​brunner7> dangerousfreedom excused himself earlier today and will write updates in the next days
<s​needlewoods_xmr> hey
<r​brunner7> jberman also excused himself and left interesting info about his work with FCMPs.
<r​brunner7> But trusty newcomer SNeedlewoods is here, nice :)
<s​needlewoods_xmr> I made several commits to my PR and right now I'm working on `LegacyEnoteOriginContextV2` like jberman suggested here https://github.com/seraphis-migration/monero/pull/16#discussion_r1451698327
<g​hostway> Oo what did he do?
<g​hostway> > <@rbrunner7> jberman also excused himself and left interesting info about his work with FCMPs.
<g​hostway> In reply to @rbrunner7
<g​hostway> jberman also excused himself and left interesting info about his work with FCMPs.
<g​hostway> What did he do?
<r​brunner7> Your PR accumulated an already quite long list of updates already. Does this document your progress in understanding and implementation I guess?
<g​hostway> > <@rbrunner7> jberman also excused himself and left interesting info about his work with FCMPs.
<g​hostway> In reply to rbrunner7
<g​hostway> jberman also excused himself and left interesting info about his work with FCMPs.
<g​hostway> What did he do?
<r​brunner7> ghostway, if you can scroll back, it's just 1 message up from me
<s​needlewoods_xmr> it's a little worrying that for a feature which seemed to be small in the beginning I'm already at ~800 lines of changed code
<g​hostway> That's great
<g​hostway> Oh, it copies the whole message...
<r​brunner7> Not for me, I see only 2 lines
<g​hostway> Hello kayabanerve :)
<s​needlewoods_xmr> I think my understanding improved quite well for the parts I'm focusing on, but I have still huge knowledge gaps
<s​needlewoods_xmr> been bouncing back and forth between duning-kruger effect and imposter syndrom lol
<r​brunner7> Yeah, I remember similar things from the start of my Monero "career" :)
<k​ayabanerve> I worked on implementing GBPs for FCMPs. While initially, I wanted a proper solution to a vector commitment scheme, I'm now of the belief it can fundamentally increase proof times by several factors.
<k​ayabanerve> BP+ uses two inner-product rows per circuit gate. BP uses 1.
<k​ayabanerve> My work with BP+ required several pointless multiplications so the variables were part of the proof, even though I didn't need a ZK multiplication of them. GBP's VC scheme voids that.
<k​ayabanerve> I've moved over the BP+ lib to GBPs and am working on moving FCMPs over. Then I'll re-architecture the circuit for the new considerations and redo the low level optimizations. Then I'll plan the rest of the work and submit a new CCS *for the work from this point on*.
<k​ayabanerve> This point, in my message's timeline, not now. I don't plan to include the GBP effort in any CCS/arguably in my prior CCS.
<r​brunner7> What does GBP stand for?
<k​ayabanerve> Generalized Bulletproofs
<k​ayabanerve> YRNTK AMA
<k​ayabanerve> (You really need to know all my acronyms)
<r​brunner7> Yet some other variant them.
<k​ayabanerve> Right, so there's BP, BP+, BP++. GBPs is an extension of the original BP to support vector commitments. Pedersen commitments with a vector of values instead of one.
<r​brunner7> Sound like quite some adventure, your journey
<g​hostway> That is interesting, so it let's you bring variables with less gates?
<k​ayabanerve> I implemented BP+ with my own horrific shim for a VC scheme, as GBPs was described on a theoretical level yet without the transformation. Aaron believes the theory is sane and provided the transform.
<k​ayabanerve> I'm replacing my shim for free/under the prior CCS out if a belief I should correct my mistakes myself. While it's not really a mistake, as it got us where we did when we did, I still don't wish to further inconvenience the Monero community with it.
<k​ayabanerve> Yes and no?
<k​ayabanerve> Prior, the goal was minimization of IP rows. BPs inherently halves them in comparison to BP+ thanks to a differing alignment of the arithmetic circuit argument.
<k​ayabanerve> I used AC multiplication gates to enter in variables under BP+. Now, vector commitments can.
<k​ayabanerve> The size of the IP argument is *max(multiplication gates, vc[0].len, vc[1].len, ...)*
<g​hostway> I've read the bulletproofs paper, not bp+, no idea how they do stuff
<k​ayabanerve> So using VCs for variables does still grow the IP *if they become the worst case*. Accordingly, we'll likely have multiple VCs for commitments in a time/space trade off.
<r​brunner7> Your next CCS will be "normal" in the sense that you will seek financing before most of the work is done, right?
<k​ayabanerve> I'll start work after submission
<k​ayabanerve> I'm unsure when I'll work on it in relation to the CCS and don't plan to explicitly limit myself to wait until funded/fundraising.
<r​brunner7> Sounds good to me.
<r​brunner7> I except it will move to funding much faster than the last one with all its extra "drama", but you never really know.
<r​brunner7> *expect
<r​brunner7> All very interesting, thanks for the report, kayabanerve . Nice to see the progress.
<s​needlewoods_xmr> ^ yes, I agree
<k​ayabanerve> Thank jberman
<k​ayabanerve> They organized my most recent sprint :p
<r​brunner7> ghostway: Is your key container PR ready for a review already, now with dangerousfreedom 's contributions, what would you say?
<s​needlewoods_xmr> I could try to review it too
<r​brunner7> Good idea
<g​hostway> I would say so!
<r​brunner7> Anything else in the frame of this meeting today?
<s​needlewoods_xmr> not seraphis related, but I'm still trying to figure out how t disable github checks
<s​needlewoods_xmr> they weren't enabled in the beginning
<r​brunner7> @selsta over in /monero-dev may know, they are playing around with such things all the time
<s​needlewoods_xmr> alright thanks, nothing else from my side
<r​brunner7> Alright, thanks everybody for attending, read you next week!
<s​needlewoods_xmr> good meeting, cu
<g​hostway> See you next week!
````


# Action History
- Created by: rbrunner7 | 2024-01-12T17:26:47+00:00
- Closed at: 2024-01-15T18:35:54+00:00
