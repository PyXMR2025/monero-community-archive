---
title: 'Monero Tech Meeting #107 - Monday, 2025-02-10, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1153
author: rbrunner7
assignees: []
labels: []
created_at: '2025-02-09T13:16:16+00:00'
updated_at: '2025-02-10T19:02:52+00:00'
type: issue
status: closed
closed_at: '2025-02-10T19:02:51+00:00'
---

# Original Description
Location is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting [here](https://github.com/monero-project/meta/issues/1150).

# Discussion History
## rbrunner7 | 2025-02-10T19:02:51+00:00
````
<r​brunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/1153
<s​needlewoods> hey
<s​yntheticbird> hi
<j​effro256> Howdy
<j​berman> *waves*
<r​brunner7> So, what do you have to report from last week?
<r​brunner7> Hmm, do we have a Matrix server problem?
<s​needlewoods> made some progress on password handling in the GUI, removed the cached password where possible and to verify passwordDialog.password we use a Wallet API method that uses `tools::wallet2::verify_password()` instead now
<j​effro256> me: basic wallet2 FCMP++-ready input selection: https://github.com/monero-project/monero/pull/9697/commits/309cf2634101f576b5b799d7b749e02834db1d2b. Earlier I did FCMP++ SA/L transaction signing on Carrot enotes, so the pieces are pretty quickly coming together for FCMP++/Carrot transaction building in wallet2
<s​needlewoods> no problem, I'm just slow
<j​berman> FCMP++ tx verification is nearly done, the last main step is the balance check, and then some finalizing work / integration into jeffro256 's latest. Need a change in the FCMP++ lib to implement the balance check. Consensus changes to validate FCMP++ txs are in place, and clients can construct the FCMP++ txs: https://github.com/j-berman/monero/commits/fcmp%2B%2B-dev/
<j​berman> I also set up tests & benchmarks for the FCMP++ competition. This is a longer summary:
<j​berman> ec-divisors is relatively simple since there is one fn `scalar_mul_divisor` that clearly takes up all the time in that fn
<j​berman> You can navigate the approach for ec-divisors in this README: https://github.com/j-berman/fcmp-plus-plus-optimization-competition/tree/3da4c0f39b80afdc2ab46b1b143e333f63b82d1b/ec-divisors-contest
<j​berman> helioselene is more complicated. My benchmark tests currently test all curve arithmetic implemented in the helioselene crate (Helioselene field add/mul/sub/square/double/invert/sqrt/pow, and Helios / Selene point ops add/mul/mul by G/sub/double).
<j​berman> As expected some ops are significantly faster than others. To account for this, I wrote individual benchmarks for individual ops. I'm thinking it may make sense to have a scoring system that is a combined weighted score of the speed-ups to each individual op, with some ops more heavily weighted like field add
<j​berman> I'm very much so open to ideas on this
<j​berman> Looking at the flamegraph for hash_grow for example, it's dominated by Helioselene Mul and Add. And then since the points' Mul implementation lean on field double and add, field double and add dominate point Mul 
<j​berman> Perhaps I should only be benching the Helioselene field ops
<j​berman> But what if there are ways to implement faster point operations that we may also want implemented. Thoughts there would be welcome
<j​berman> Next I'm working on using @kayabaNerve's wasm-cycles crate, which will test ability to build on wasm and do some cycle counting to help validate constant timedness
<r​brunner7> Much progress on many fronts. Well, the questions "when FCMP++" get somewhat more frequent now :)
<r​brunner7> tobtoht_ over in monero-dev recently had a very nice way to put their estimates:
<r​brunner7> > <t​obtoht_> eoli: Here is my probability distribution for the FCMP++ hard-fork: Q2 2025: 1%. Q3 2025: 9%. Q4 2025: 25%. Q1 2026: 40%. Q2 2026: 20%. Later or never: 5%. I hope that helps.
<s​yntheticbird> I share kayabanerve disgust regarding Q4 2025 and worse Q1 2026. Is there no way the hard fork organization can reasonably be accelerated.
<r​brunner7> Not sure what you mean. Too early, or later than whished for?
<s​yntheticbird> implementation and audits are thing, but then integration shouldn't take more than 6 months.
<j​berman> I think audits/sufficient review will be the bottleneck
<j​berman> Integration is making really solid progress rn, we're in the last third / last quarter I think
<r​brunner7> Well, integration probably won't take 6 months, but you have to release the fork-ready release early
<j​berman> Multisig might be a drag
<jeffro256> +1
<r​brunner7> As well as hardware wallets, maybe
<jeffro256> +1
<r​brunner7> I think we have to catch the point in time when we will be ready to reach out to them and tell them "This is it, people, your hardware wallet has to deal with *this*"
<j​berman> kayaba brought up a good point at one point, hw wallets should be able to reuse the FFI if they want
<j​effro256> I think that point is very soon (under 2 weeks), once we more or less finalize the best flow for how we want to integrate FCMP++/Carrot code, we just have to reach out and update them with hardware interface inplementation requirements
<r​brunner7> So they would put some of the Rust libs into the firmware of their wallets?
<j​effro256> The scanning side for Carrot HW devices is done, all we need is a solidified interface for SA/L proofs
<j​berman> they could, ya
<j​effro256> Perhaps, depends on their toolchain requirements
<j​effro256> Perhaps rust isn't allowed
<j​effro256> Who knows
<r​brunner7> Just making them aware that's a possibility then
<j​effro256> Of course, and we're refactoring the FCMP++ FFI interface to support C as well as C++, so perhaps it is reusable for hardware devices
<j​effro256> which use C code, but can link with Rust
<r​brunner7> Will multisig look any different under Carrot, from a UX / workflow point of view? Which multisig will it be, anyway?
<r​brunner7> The new one from the Rust side? "Frost" based, or how it's called?
<j​effro256> With a new Carrot-derived multisig wallet, you won't have to sync key images which is nice, you only need to coordinate when spending
<r​brunner7> And for building the wallet initially, of course
<j​effro256> Yes
<r​brunner7> And for that, how much of the existing C++ based multisig code must change, or has to be rewritten?
<j​effro256> Basically all of it....
<r​brunner7> Splendid
<r​brunner7> Yeah, do we have any volunteers already for that lol
<r​brunner7> Not many people at hand who can realistically tackle that, seems to me :)
<s​yntheticbird> im volunteer but ill release it under 48 months and will include at least 4 critical vuln
<j​effro256> jberman do you wanna talk about the old-multisig compatible dev flow ?
<j​effro256> If you had any thoughts, that is
<j​effro256> I haven't given it much thought myself at this point
<r​brunner7> So this may shape up as some still weak point in the way up to the hardfork ...
<j​berman> Let me dust off some thoughts on it. IIRC kayaba wrote a legacy multisig compatible FCMP++ rust lib, and had fleshed out thoughts on how we could smoothly port it into wallet2. Let me try and find that link
<r​brunner7> I think back in his time koe put considerable dev time into this in his Seraphis library
<jeffro256> +1
<a​surar0:unredacted.org> Should we expect multisig wallets to not be available at testnet launch?
<r​brunner7> But of course that's all "snow from yesterday", as Germans quip
<j​effro256> I would have to look back and see if any of this is applicable to us with FCMP++ since the composition is different
<r​brunner7> asurar0: Sounds like it, if you ask me
<j​effro256> Yes
<a​surar0:unredacted.org> Okay
<r​brunner7> Ok, thus some research ahead in this regard, hopefully possible soon
<j​effro256> Multisig support doesn't require any consensus or relay rules, so one can update their node/wallet later to add multisig support and still be compatible with everyone
<j​effro256> I think it was for this reason, among others, that Koe argued that multisig code shouldn't be in the core repository at all
<r​brunner7> Yes, as a last resort, probably
<r​brunner7> I remember, yes
<r​brunner7> Alright. If we are through with this for the moment, I have little terminology question to submit to the people here
<j​effro256> Just that at a research level, multisig was known to be supported by the consensus protocol
<s​yntheticbird> ngl I was surprised when i first heard of FROST multisig. I really thought it requires official support somehow. But at least having one "official" multisig implementation make the core wallet job easier (we aren't gonna implement the N different schemes in official wallet)
<r​brunner7> With Carrot, we will support *two* types of wallets: The wallets as they ever were, with the two CryptoNote style spend and view secret key, and the new Carrot wallets with 4 keys and 2 secrets, as the spec puts it
<r​brunner7> The question arises how we call these two types of wallet
<r​brunner7> One difficulty there is that the term "wallet", like people actually use it, is ambiguous
<r​brunner7> Sometimes it's the wallet as container for key material, enotes, options and caches
<r​brunner7> And often it's the wallet app
<r​brunner7> Thus, if we speak about e.g. "legacy wallet" versus "Carrot wallet" people may confuse this with "Carrot enabled wallet app"
<r​brunner7> And if we add "key" or "keys", like with "legacy key wallet" versus "Carrot key wallet", some people will invariably drop the "key", and then we might have confusion again
<r​brunner7> Thus I tried to come up with something that is hard to confuse, and hard to mangle: "two key wallet" versus "six key wallet"
<j​berman> Can't find it atm (maybe tobtoht has that link handy ?). Here is the legacy multisig SAL impl: https://github.com/kayabaNerve/fcmp-plus-plus/blob/78754718faa21f0a5751fbd30c9495d7f7f5c2b1/networks/monero/ringct/fcmp%2B%2B/src/sal/legacy_multisig.rs
<jeffro256> +1
<j​berman> IIRC that link explained what steps to take to integrate that into wallet2
<r​brunner7> Looks pretty wild, that stuff
<j​effro256> I just thought about this. This is a pretty good nomenclature, but there is a third type: hybrid wallets, which will have _7_ keys: keys from both legacy-derived and Carrot-derived (2+6), with the private key view shared (-1) between them
<j​effro256> This is probably what HW wallets will do
<r​brunner7> Good then that they have a different number of keys :)
<r​brunner7> Why do you think that they will prefer this?
<j​effro256> Doesn't require a seed migration
<r​brunner7> Hmmm, yes, but didn't you argue against supporting such mixed wallets?
<j​effro256> For reference wallets, yes
<r​brunner7> Because of a potential of even bigger confusion, and the necessary effort to suppor them on the wallet app side?
<j​effro256> Sorry I should've been clearer about that
<j​effro256> I wonder if the effort to support them would be that much bigger ...
<r​brunner7> Ok, maybe that's a subject that merits further discussion, but anyway, any more comments about the proposed terms?
<r​brunner7> I will make sort of a "Carrot announcement post" on Reddit soon, and want to try to "get it right" from the start, so to say
<r​brunner7> To the native speakers of English: Is "two keys wallet" with plural better than "two key wallet"? Or doesn't it matter too much?
<j​effro256> I would initially use their long names to get people familar with the type of key association instead of the shorted ones at first. So instead of saying just "2 key accounts" and "5 key accounts", say "2 key legacy accounts" and "6 key Carrot accounts". Then they can be shorted to just the number when the type of keys is well associated to the readers
<j​effro256> Personally, it sounds better without the *s*
<r​brunner7> Yeah, that's a variant. You say now "account" instead of "wallet" - any deeper meaning in this, but just synonyms? "accout" threatens to cause confusion with "accounts" as compartments *within* wallets
<sneedlewoods> +1
<j​effro256> Eh true
<j​effro256> Yeah use "wallets"
<r​brunner7> I know, such terminology questions may seem a bit pedantic, and hey, this is a *dev* meeting, but I feel it has a certain importance
<r​brunner7> Alright, at least I see nobody actively opposing to "two keys legacy wallet" and "six keys Carrot wallet"
<s​needlewoods> They sound good to me
<r​brunner7> Oh, well, jeffro256 voted for "without s" - I misread. I also prefer singular, it just rolls easier off the tongue. Just wasn't sure it's correct English
<j​effro256> No I get it, it would be even more discouraging if I started seeing questions like "How do I upgrade account 2 to a Carrot account, but leave Account 1 untouched in Monero GUI?"
<r​brunner7> Lol
<r​brunner7> Thus it's "two key legacy wallet" and "six key Carrot wallet" then
<s​needlewoods> yeah, to me accounts in Monero have something to do with major subaddress indices
<r​brunner7> Right. Not perfect as terminology, but established, have to live with it, probably
<r​brunner7> Until somebody complains that "legacy" is kind of derogatory and votes for more neutral "two key CryptoNote wallet" ...
<j​effro256> I'm fine with "Two key Cryptonote wallet"
<r​brunner7> Well, if a few years in the future Carrot gets superseded we would have legacy wallets and legacy legacy wallets ...
<r​brunner7> Ok, enough of this silliness. Anything else to discuss today?
<j​effro256> wallet_old_backup_real_backup_feb2025_final.bak.zip.bak
<r​brunner7> It's gets better and better
<r​brunner7> Seems to me we can close for now. Thanks for attending, interesting meeting. Read you again in 1 week!
<s​needlewoods> thanks, cu
<j​effro256> Thanks, all
<s​yntheticbird> Thanks
````


# Action History
- Created by: rbrunner7 | 2025-02-09T13:16:16+00:00
- Closed at: 2025-02-10T19:02:51+00:00
