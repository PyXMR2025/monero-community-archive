---
title: 'Seraphis wallet workgroup meeting #68 - Monday, 2024-04-29, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/997
author: rbrunner7
assignees: []
labels: []
created_at: '2024-04-26T14:46:50+00:00'
updated_at: '2024-04-29T18:41:09+00:00'
type: issue
status: closed
closed_at: '2024-04-29T18:41:09+00:00'
---

# Original Description
On Monday, November 14 2022, we started with regular weekly meetings of the Seraphis wallet workgroup, and all interested parties from the community that want to join. Time is 18:00 UTC on each Monday. "Location" is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting here: https://github.com/monero-project/meta/issues/993

# Discussion History
## rbrunner7 | 2024-04-29T18:41:09+00:00
````
<r​brunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/997
<o​ne-horse-wagon> Hello!
<d​angerousfreedom> Hi
<a​rticmine> Hello
<r​4v3r23> hi
<tobtoht_> Hi
<j​effro256> howdy
<r​brunner7> So what is there to report from last week?
<r​brunner7> I wrote this here yesterday: https://old.reddit.com/r/Monero/comments/1cf8oom/the_monero_core_software_wallet_api_will_probably/
<s​needlewoods> hey
<d​angerousfreedom> After the discussion about deprecating [wallet2](https://github.com/seraphis-migration/wallet3/issues/64) and the willingness of current and new wallets to rely only on the `wallet2_api` (if it has all features needed), I believe it makes sense to me to re-target my next tasks to use an interface for my PoC CLI wallet. The idea will be to use the `wallet2_api.h` and/or create a ne<clipp
<d​angerousfreedom> w interface from which I will base on my CLI. The final goal stays the same. I want to have the most basic CLI wallet capable of sending/receiving txs using a regtest network. After that, hopefully, we will be able to discuss the scalability/compatibility/design and other issues with that approach. I also tried to study FCMP but couldnt find enough time to fully digest kayaba's introduction on it.
<s​needlewoods> looks like only positive feedback there too
<jberman> :waves:
<s​needlewoods> I haven't done much but reading some code regarding the wallet api, but I reviewed https://github.com/UkoeHB/monero/pull/42
<r​brunner7> kayabanerve is fully funded already, right?
<d​angerousfreedom> Yes :)
<r​brunner7> Nice
<o​ne-horse-wagon> rbrunner7: Monero has never wanted funds for legitimate projects that I've ever seen.  It's very strong financially.
<a​rticmine> I am working on the new scaling and fee proposal. This is based upon the latest estimate of 3000 bytes 2/2 transaction for FCMP. 
<a​rticmine> It will incorporate a new sanity median of 1000000 bytes. 
<a​rticmine> Also the use of node relay to control growth, by increasing the minimum node relay fee.
<r​brunner7> I was almost a bit disappointed that I did not manage to flush out a single wallet dev with a reaction of "Whaaaat!" with my post
<jberman> me: implemented a tool to import the Seraphis enote store into wallet2's m_transfers container (+ m_payments + m_confirmed_txs), which is useful to enable using wallet2 to construct txs "in a box" as described here: https://github.com/seraphis-migration/wallet3/issues/48 , and to drop the async scanner into wallets today
<jberman> Putting final touches on that, and will implement koe's review comments in the async scanner next, then open another CCS
<j​effro256> ArticMine:  what do you think of tx-pow?
<a​rticmine> Not a good idea
<r​brunner7> jberman: Nice that you already started to work on that. Progress finally!
<j​effro256> @jberman: nice !
<a​rticmine> It is very discriminatory against the global south
<jberman> the enote store is missing a few things to have complete compatibility, I have a list written up and will share it soon too
<r​ucknium> FWIW I am also skeptical of tx-pow. But I will run some numbers anyway.
<a​rticmine> POW belongs in cold places during the winter. Not in the tropics
<r​ucknium> Probably the set of tx-pow parameters that make spamming very difficult and normal transactions easy, is empty.
<j​effro256> That's about my thoughts as well, just wanted a quick opinion ;)
<j​effro256> Talked to kayabanerve  yesterday. He claims that with a new divisor scheme, the FCMP-RCT proposal is comparable (even for the first layer) with Seraphis in performance
<a​rticmine> Is this tx size, verification or both?
<r​brunner7> Everyday something new out of that corner, it seems :)
<s​yntheticbird> Is this new divisor scheme also compatible for Seraphis ? Or will the performance improvements only meaningfull for FCMP++
<s​yntheticbird> only be meaningful*
<j​effro256> ArticMine: at least for CPU time, I'm not sure about tx size
<j​effro256> verification side, that is
<r​ucknium> Is this the new divisor scheme by Liam Eagen that Cypher Stack decide not to review?
<j​effro256> SyntheticBird: This is where it gets a bit hazy for me, but IIUC, the divisors here are really only applicable to FCMP-RCT since they help keep track of the parallel keys together
<j​effro256> So they don't help *as much* with Seraphis
<j​effro256> Rucknium: I do not know
<rucknium> +1
<r​brunner7> dangerousfreedom, SNeedlewoods , did you actually team up on that wallet API work?
<s​needlewoods> I haven't found the time yet, only looked at the current state of the code for now
<d​angerousfreedom> No. I havent start implementing anything yet. Just thinking how to do
<r​brunner7> Alright. I do think it could be a good idea to build a little team there.
<0xfffc> +1
<dangerousfreedom> +1
<s​needlewoods> if I can close https://github.com/UkoeHB/monero/pull/40 then I have nothing on my table, that would prevent such work
<r​brunner7> That would be most unfortunate, with all the work that we have ahead, in principle :)
<r​brunner7> Really, having that API would open up many work opportunities, as already mentioned last week.
<s​needlewoods> sorry, I think I phrased that poorly, I mean if that PR gets closed, there is nothing 'urgent' that would prevent me to fully concentrate on the API
<r​brunner7> :)
<s​needlewoods> and jeffros #42 does the same as #40 and much more, plus it's way cleaner, so I'm in favor of #42
<jberman> seems like we're good to close #40, I want to review #42 as well
<jberman> I could use help on this idea: https://github.com/seraphis-migration/wallet3/issues/64#issuecomment-2070568200
<jberman> if we agree it's an acceptable route
<r​brunner7> Will have to read it first carefully, and then think about it. Probably it's again a case of almost too many possible ways to go with our move away from wallet2 ...
<jberman> @dangerousfreedom legacy knowledge proofs are an example of something to swap in the wallet API from using wallet2 (m_wallet->) to using the Seraphis lib
<r​brunner7> I guess a first important info will be to see what is actually missing from wallet2_api.h and connected other .h
<d​angerousfreedom> jberman: True
<r​brunner7> Ok. Is there anything else to discuss today?
<r​brunner7> Doesn't look like it. So thanks everybody for attending, read you again next week!
<s​needlewoods> thanks and cu
<d​angerousfreedom> I did an implementation of that a while ago: https://github.com/seraphis-migration/wallet3/issues/55#issuecomment-1696071739. We just have to better structure the work now :)
<d​angerousfreedom> Thanks
````


# Action History
- Created by: rbrunner7 | 2024-04-26T14:46:50+00:00
- Closed at: 2024-04-29T18:41:09+00:00
