---
title: 'Monero Tech Meeting #121 - Monday, 2025-05-19, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1206
author: rbrunner7
assignees: []
labels: []
created_at: '2025-05-18T09:37:34+00:00'
updated_at: '2025-05-19T18:40:37+00:00'
type: issue
status: closed
closed_at: '2025-05-19T18:40:36+00:00'
---

# Original Description
Location is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting [here](https://github.com/monero-project/meta/issues/1202).

# Discussion History
## rbrunner7 | 2025-05-19T18:40:36+00:00
````
<r​brunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/1206
<s​needlewoods> hey
<j​berman> *waves*
<r​brunner7> So, what is there to report from last week?
<r​brunner7> I am still testing peer selection. Quite some things to investigate still, e.g. bad success rate selecting new white peers
<s​needlewoods> Made good progress on simple_wallet, now you can open or generate a new wallet, let it sit in idle mode and close it without any segfaults using only Wallet API methods.
<s​needlewoods> `grep "\<m_wallet\>" src/simplewallet/simplewallet.cpp` gives 641 results on monero master and 534 on my branch.
<jberman> +1
<s​needlewoods> There were some more things that changed for the Wallet API and there will be more to come. What do you think, should I add the changes to my [Wallet API PR](https://github.com/monero-project/monero/pull/9464) every so often, or should I wait until the work on simplewallet is done and then add everything in one commit? Or other suggestions?
<s​needlewoods> I don't think I should bring the new Wallet API additions in with the simplewallet PR, because there are some breaking changes w.r.t. #9464
<r​brunner7> Yeah, I wouldn't mix either.
<j​berman> me: some solid PR wrangling with jeffro, we got a few PR's into fcmp++-stage (Carrot integration, torsion ban, tree root in PoW hash, updated composition/removed key image migration code). Also did an optimization/cleanup pass. I'm continuing this week on the scan_tx feature/fetching paths via RPC. Also shared a CCS update: https://repo.getmonero.org/monero-project/ccs-proposals/-<clipped messag
<j​berman> /merge_requests/574#note_29985
<r​brunner7> Regarding modifications, I would say do it in the way that is most comfortable for you. I don't think somebody immediately depends on your work already, so seems to me you are pretty free.
<jberman> +1
<s​needlewoods> UnstoppableSwap dev mentioned they use the new wallet2_api.h  https://github.com/monero-project/monero/pull/9918#issuecomment-2854236785
<r​brunner7> Yes, that, but I would assume they are well aware about the preliminary state of the API additions
<sneedlewoods> +1
<r​brunner7> jberman: How is it going for you and jeffro256 in the light of the difficulties to prove the safety of divisors? Some dent in the motivation, or do you have such a speed that nothing can stop you right now?
<r​brunner7> A bit funny, by the way, how nobody outside our close dev circles seemed to pick that up already. E.g. the new "Revuo" Monero weekly has no mention.
<j​effro256> Hi! Sorry I'm late
<j​berman> I feel confident we'll find a reasonable means to move forward on that front. So basically going full steam on the remaining tasks with that assumption
<jeffro256> +1
<sneedlewoods> +1
<r​brunner7> Good to hear.
<r​ucknium> Move forward in which direction?
<r​brunner7> Those difficulties have no direct influence anyway, nothing in your coding is different now, right?
<j​berman> Both directions of an alternate implementation of non divisors FCMP++, and am fairly content that CS is separately still continuing work on divisors
<rucknium> +1
<j​effro256> Still lots to work on today even without knowing the exact FCMP construction and assuming that divisors won't make it into the next HF. For example, rn I'm working on changing the cold/hot wallet flows for Carrot/FCMP++. The separation of membership proofs from SA/L proofs changes the flow for that business logic. There's a lot of fine logic involved in tree building on both the wallet and daemon side.
<j​effro256> There's new consensus rules to consider. There's HW device integration for Carrot/FCMP++. There's multisig updates for Carrot/FCMP++. There's optimizing those aforementioned things. There's regression testing for Carrot scanning and Carrot tx building.
<rucknium> +1
<j​berman> We've paused hardening tx weight and a blinds cache as examples. And I second jeffro's comments there^
<r​brunner7> Is the lack of divisors the direct consequence of your "workflow" changes? That surprises me a bit now
<r​brunner7> Er, not consequence of course, direct reason
<j​effro256> No that flow change was always the case for FCMP++, I just gave it as an example of something we can still work just the same without divisors
<r​brunner7> Ah, ok
<j​effro256> And all the Carrot work is more or less completely unaffected
<j​berman> Also divisors / non-divisors is an internal FCMP++ detail that shouldn't significantly affect the API. So we can continue on tasks that need to get done either way with the current API
<jeffro256> +1
<r​ucknium> Any idea how a non-divisor FCMP implementation could get written?
<r​ucknium> From the MRL meeting, it seemed that the expected verification time is not known exactly.
<j​berman> AFAIK it needs a new circuit implementation. We ideally get the ideal candidate for the job to write the changes. And I will try to have more to update on that front by MRL meeting
<j​berman> Expected verification time is not known exactly, but expected to be slower
<rucknium> +1
<r​ucknium> It would help to know the verification time, to see if block sizes would have to be restricted to limited safe zone in a non-divisor hard fork era
<r​brunner7> I don't now, in the light of these difficulties somehow I wonder a bit how Zcash managed to successfully build something with roughly the same privacy that we will get from FCMP++ years ago already ...
<r​ucknium> Is the ideal candidate kN? Was that implied?
<r​brunner7> Maybe they were lucky, and maybe their network wouldn't work propery with 100% shielded transactions ...
<r​brunner7> *properly
<r​ucknium> Zcash also built a protocol with a counterfeiting flaw. And they still quarantine all their shielded pools.
<r​brunner7> Right :)
<r​brunner7> *That* we don't have to emulate
<r​ucknium> If you don't have that kind of quarantine, you must be extra extra sure that there is no fatal flaw in the cryptography. Different standard.
<r​brunner7> Ok, seems to be a bit of patience is in order. Monero had some good luck several times in the past, maybe things will work out alright.
<j​effro256> I'm obv biased towards Monero's way of doing it, and not to knock how Zcash did it, but Zcash's ZK-SNARK constructions rely on more underlying mathematical assumptions than Curve trees and GBPs. The math is a lot lot hairer, but if you're willing to swallow the complexity and trusted setup requirement and not wait for a more solid base than you can prototype your consensus layer faster. Since XMR is quite a bit bigger and actually used IRL, I honestly wouldn't feel comfortable using trusted setups or the cryptography that Zcash uses. I'm really happy for the competition and it's cool as an experimental product, but they're just different ways of going about it
<r​brunner7> Yes. And for a long time they needed gigabytes of RAM and minutes to create a single transaction. It's not yet *that* long that they got rid of trusted setup and have reasonable tx construction times.
<r​ucknium> Or at least that is the point I made at the Monerotopia 2023. That's where I predicted (wrongly, I hope) that Monero would keep using rings for the foreseeable future, because of just these problems with uncertainty and risk that are unique to Monero.
<r​brunner7> Anyway, we can't just copy anything from them, even if we were bold enough, so we will have to find our way.
<r​brunner7> Ok. Do we have anything special to discuss today, beyond reports?
<r​brunner7> Doesn't look like it. Thanks for attending everybody, read you again next week!
<s​needlewoods> thanks everyone
<syntheticbird> thanks
````


# Action History
- Created by: rbrunner7 | 2025-05-18T09:37:34+00:00
- Closed at: 2025-05-19T18:40:36+00:00
