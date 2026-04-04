---
title: 'Seraphis wallet workgroup meeting #10 - Monday, 2023-01-23, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/783
author: rbrunner7
assignees: []
labels: []
created_at: '2023-01-19T19:23:45+00:00'
updated_at: '2023-02-13T00:09:43+00:00'
type: issue
status: closed
closed_at: '2023-02-13T00:09:43+00:00'
---

# Original Description
On Monday, November 14, we started with regular weekly meetings of the Seraphis wallet workgroup, and all interested parties from the community that want to join. Time is 18:00 UTC on each Monday. "Location" is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting here: #780

I propose to look at the subject of hardware wallets and Seraphis for a first time. I invited @selsta to join because they are the one keeping contact with hardware wallet devs, and they should know a lot about the subject of such wallets and Monero in general. @UkoeHB also just comes from supporting hardware wallets in his legacy enote scanning support in the Seraphis library.

I have a hunch that hardware wallet support for Seraphis might become a quite difficult issue.

# Discussion History
## rbrunner7 | 2023-01-23T19:13:39+00:00
````
<dangerousfreedom> Hello guys, I cant make it for the next hour again, sorry. I will read your comments later.
The updates of the week from my side are:
1) Wrote a draft for all knowledge proofs like Koe suggested (https://github.com/DangerousFreedom1984/seraphis_lib/commit/22f78913b7dc2c588a88daf9865c358046cf0562). Basically we are exposing the enotes directly instead of creating Schnorr proofs as I suggested initially for the basic proofs. I still need to polish, write more comments and double-check with more unit_tests but I believe it is getting closer to the end, I will wait for Koe's comments and directions and will try to finish this week.
2) I'm looking again at the functions to load/save a wallet and I believe I will have a better prototype to discuss the nomenclature and the general schemes for starting the wallet soon (hopefully by next week).
<rbrunner7[m]1> Meeting time. Hello everybody! https://github.com/monero-project/meta/issues/783
<selsta> hi
<plowsof11> hi
<JoshBabb[m]1> Hello
<jberman[m]> hello
<shalit[m]> hello
<Rucknium[m]> Hi
<ofrnxmr[m]> Gm
<ghostway[m]> hello
<rbrunner7[m]1> dangerousfreedom[m] can't make it, but left some news about 20 minutes ago: He will soon complete the Seraphis proofs, and then it's wallet time.
<xmrack[m]> Hi
<UkoeHB> hi
<rbrunner7[m]1> I invited selsta to the meeting, and saw them writing "hi" on IRC, but not here on Matrix. Can you write something again please, selsta, to check?
<selsta> test
<rbrunner7[m]1> Ah, thanks, that worked :)
<selsta> wonder if the bridge is wrongly setup again
<selsta> not important for now
<rbrunner7[m]1> Anything to report about work done over the last week?
<ghostway[m]> so with that (not) said
<ghostway[m]> if anyone needs help in any related project, I'd like to help if possible
<UkoeHB> I basically finished cleanup/review of the seraphis library (just need to skim the unit tests today).
<shalit[m]> > <@ghostway:matrix.org> so with that (not) said
<shalit[m]> > if anyone needs help in any related project, I'd like to help if possible
<shalit[m]> same here LOL
<rbrunner7[m]1> I think it should be possible to find some pieces for more people to work on independently, at least for the time being.
<jberman[m]> Nothing to report on my end, was focused on current daemon tasks the past week. Moving back over to scanning work this week
<rbrunner7[m]1> Alright. My idea for today is talking about Seraphis and hardware wallets for a first time
<rbrunner7[m]1> That's the reason I invited selsta: They are the one to keep contact with the dev teams of the hardware wallet manufacturers
<rbrunner7[m]1> Maybe we can start with making clear the status-quo, the point where we stand now regarding hardware wallets
<Rucknium[m]> AFAIK, here's the paper that made HW signing possible (I may be wrong): Klinec, D., & Matyas, V. (2020), "Privacy-friendly Monero transaction signing on a hardware wallet." https://moneroresearch.info/index.php?action=resource_RESOURCEVIEW_CORE&id=119
<rbrunner7[m]1> As far as I know, only two hardware wallets are supported: Trezor and Ledger. No idea whether anything else is on the way right now.
<Rucknium[m]> I have not read the paper
<rbrunner7[m]1> I will have look later to be sure I don't understand it :)
<Rucknium[m]> rbrunner7: A Monero fork of SeedSigner has been CCS-funded. plowsof any updates?
<rbrunner7[m]1> There is something like a "driver system" for hardware wallets as part of the Monero core software. It's here: https://github.com/monero-project/monero/tree/master/src/device
<selsta> only Ledger and Trezor have an integration into the monero codebase
<rbrunner7[m]1> With seemingly some more code for Trezor here: https://github.com/monero-project/monero/tree/master/src/device_trezor
<rbrunner7[m]1> I think just very recently UkoeHB started to use that, for supporting hardware wallets while scanning legacy enotes in the Seraphis library, right?
<UkoeHB> The issue with hw wallets is 'how much needs to be supported?' Right now both tx signing and balance recovery are supported, but they both assume the presence of a control device. If a control device is always present, then afaict it will always know your full balance so idk what the point of implementing hw balance recovery is.
<rbrunner7[m]1> That would have been my next question, to be sure: What are these hardware wallets doing today regarding Monero?
<rbrunner7[m]1> Signing of course. But I think they can also scan the blockchain, right?
<selsta> Ledger scanning on device is broken
<rbrunner7[m]1> Ah, it once worked, but now not anymore?
<selsta> I don't know if it ever worked, possibly in the beginning
<selsta> but it's extremely slow anyway
<rbrunner7[m]1> And I think to remember it was terribly slow already in its best times?
<Rucknium[m]> I am surprised that they can scan the blockchain. That's a lot of work for a low-power device.
<jberman[m]> It works but really slowly when I test it
<UkoeHB> with seraphis I believe the only thing really needed is this https://github.com/UkoeHB/monero/blob/2ca55a743a291d0b382e53b7922a8ac1fd837f64/src/seraphis_crypto/sp_composition_proof.cpp#L168 which is a fairly small proof
<rbrunner7[m]1> Do they construct transactions, i.e. full transactions?
<UkoeHB> rbrunner7[m]1: no, wallet2 makes txs then uses the hw device for signing
<rbrunner7[m]1> You mean to construct transactions? Or to sign?
<jberman[m]> I meant to scan
<UkoeHB> rbrunner7[m]1: to sign
<rbrunner7[m]1> So if scanning is broken anyway, we don't have to worry about that, and users probably won't shout to keep that going, I would say.
<plowsof11> Rucknium: seed-signer updates , no releases as of yet, but its 'getting there' (the proposer has been active a few days ago posting on the feather repo.. nothing exciting yet https://github.com/Monero-HackerIndustrial )
<selsta> jberman[m] says it's working but I often get reports about it, it's basically unusably slow that it appears broken
<rbrunner7[m]1> So this has a realistic chance to become a third one?
<UkoeHB> For post-seraphis, hw wallets should only need to support: A) making legacy key images, B) signing CLSAGs for legacy inputs, C) signing seraphis composition proofs for seraphis inputs.
<plowsof11> yes rbrunner7 , it will be 'adding monero' to an existing project (the seedSigner - built from a pi zero.. lcd screen and such DIY)
<UkoeHB> and probably D) exporting legacy view keys and seraphis view-balance keys
<rbrunner7[m]1> Is keeping the scanning functionality working into the future realistic? They would need large parts of the Seraphis library to do it in firmware, I guess?
<selsta> we should drop scanning
<UkoeHB> it would require a lot of code
<rbrunner7[m]1> Do you still need only a single key to sign with Seraphis? What was the spend secret key?
<ghostway[m]> with delegation of scanning possible in seraphis, it could be cached probably etc
<UkoeHB> rbrunner7[m]1: you need multiple keys but the extra key material can be passed in when requesting a signature from the device
<ghostway[m]> (on the host)
<Rucknium[m]> I agree with dropping scanning. Isn't there very little privacy benefit since the desktop computer sees the txs anyway? The only benefit is privacy for future transactions that you don't want the desktop to see (since view key isn't exported if device itself is scanning).
<plowsof11> we can't forget the long awaited SideKick from monerujo (huge delays there but - it would be an offline android device for signing tx's offline)
<rbrunner7[m]1> So the device does not need to know how to derive those additional keys, I suppose
<rbrunner7[m]1> plowsof: Right, but I can imagine that would not go through the same "driver" framework, but some other Monerujo-specific way
<UkoeHB> no, it only needs to know how to get the view-balance key out of the original seed
<UkoeHB> which would probably mean fully supporting polyseed
<plowsof11> +1 for dropping scanning on device - see service outage this caused for trezor users the last hardfork 
<Rucknium[m]> HW wallets cannot really support polyseed since polyseed include restore height, right?
<JoshBabb[m]1> @shalit and @ghostway, I wanted to save this task for myself, but here's information @dangerousfreedom shared with me about work for a new contributor to do:
- Write C++ BLAKE2 unit tests for https://github.com/UkoeHB/monero/tree/seraphis_lib/tests/crypto like those in https://github.com/UkoeHB/monero/tree/seraphis_perf/tests/crypto using https://github.com/BLAKE2/BLAKE2 as a reference
I will work on this as soon as I can, but perhaps either of you would like to take a swing at it.  I'd definitely like to contribute that work but have been swamped
<selsta> why would it need to support polyseed? current hardware wallets also don't support the 25 word monero seed
<UkoeHB> I will revisit the hw support I added to the seraphis lib and remove all the unnecessary parts
<UkoeHB> selsta: oh really, is it just secrets baked into the device?
<selsta> yep
<selsta> you need an external tool to convert to a monero seed
<Rucknium[m]> "Secrets baked into the device" needs clarification
<plowsof11> the seedsigner and i assume sidekick are just scripting around 'cold/offline signing - export/import/sign transactions'
<rbrunner7[m]1> I think they have their own proprietary ways to derive a Monero key from their master key
<rbrunner7[m]1> Because they have to support a lot of coins
<rbrunner7[m]1> plowsof: I would say so, yes. Cold signing, in principle.
<Rucknium[m]> Trezor and Ledger work by generating a secure random BIP39 (right BIP?) Hierarchical Deterministic mnemonic seed.
<selsta> Ledger and Trezor derive them in different ways
<UkoeHB> ok well either way, if polyseed doesn't need to be supported that's a win for implementation work
<selsta> https://github.com/monero-project/monero/issues/5744
<rbrunner7[m]1> So what else is there? I think the devices can interpret transactions, to make sure everything was built on the PC as it should, and e.g. display destination and amount.
<rbrunner7[m]1> I remember seing a Ledger displaying a Monero address in 3 or 4 parts on its tiny display, man, that's fun :)
<rbrunner7[m]1> What do you think, do hardware wallet users consider such checks valuable?
<rbrunner7[m]1> I guess they should, otherwise you won't you what you really sign, right?
<rbrunner7[m]1> *won't know
<rbrunner7[m]1> And if yes, what does that mean for Seraphis support?
<selsta> they also display change
<selsta> could the hardware wallet display the Recipient ID instead of the full address?
<rbrunner7[m]1> If it can derive it, why not.
<jberman[m]> they could display RIDs for Seraphis/Jamtis. but yea it's a critical part of using a hw wallet that it would display destination + amounts
<UkoeHB> looking at device.hpp I don't see an option to load in a tx, maybe that's some other workflow?
<rbrunner7[m]1> So how complicated is it to dissect built Seraphis transactions?
<Rucknium[m]> Trezor and Ledger as companies might not accept just showing the RID. You would have to get their approval. At least for Ledger. I think you can "side load" "unapproved" apps onto Trezor devices.
<UkoeHB> you can save an SpTxProposalV1, which converts into the tx proposal prefix that all txs sign
<UkoeHB> there is a lot of underlying crypto to convert though - i.e. basically all of jamtis
<selsta> Rucknium[m]: it's the other way around
<selsta> Ledger can load apps, Trezor is all in firmware
<rbrunner7[m]1> Uh, that does not sound too good, needing more or less all of Jamtis
<UkoeHB> you'd need to implement most of what's in this file https://github.com/UkoeHB/monero/blob/seraphis_lib/src/seraphis_core/jamtis_payment_proposal.cpp
<Rucknium[m]> Don't Ledger apps need to be signed by Ledger?
<rbrunner7[m]1> This imports a lot of other stuff, as it seems
<rbrunner7[m]1> Is there no other way than dissecting what the hardware wallet signs, by the hardware wallet? I think so, any other info the Monero wallet app would tell it could be a lie
<rbrunner7[m]1> So this could well be the largest part of Seraphis implementation work, for Ledger and Trezor
<UkoeHB> seems that way
<rbrunner7[m]1> Really just brainstorming now: Could we make their life easier by structuring that payment proposal code, so that it's easy to lift it out of the library and into their firmware, so to say? I guess they do use C++?
<UkoeHB> it's all pretty straightforward work, the issue is the volume of work (plus you'd need to support X25519 and blake2b on top of keccak and ed25519)
<rbrunner7[m]1> MIght even bump into firmware space problems for the less powerful models, I guess ...
<UkoeHB> and if you want to validate selfsend addresses, you'd need twofish
<rbrunner7[m]1> Yeah, what wasn't too hard to add to the "toolbox" may turn out to be quite hard work for those hardware wallet devs
<rbrunner7[m]1> (Not too hard for us to add)
<jberman[m]> FWIW I'm fine with implementing everything needed for Ledger, but it would be better if they did it and maintained it and I'd prefer not to announce to them that I'd do it
<UkoeHB> to really do it right you'd want to implement this semantics checker as well (which has quite a big call tree) https://github.com/UkoeHB/monero/blob/2ca55a743a291d0b382e53b7922a8ac1fd837f64/src/seraphis_main/tx_builders_mixed.cpp#L840
<rbrunner7[m]1> jberman: Well, this meeting room is a public place
<rbrunner7[m]1> You mean you are, in theory, able to work on their firmware, directly?
<rbrunner7[m]1> Make PRs to it?
<jberman[m]> ya, I implemented view tags for them
<rbrunner7[m]1> Wasn't Trezor the one with open source firmware?
<jberman[m]> all of Ledger's monero software is open source too
<rbrunner7[m]1> Interesting.
<Rucknium[m]> As of two years ago, the Monero Ledger on-device app was reportedly 44KB in size: https://reddit.com/r/ledgerwallet/comments/m0jbg3/comment/gq8eqy0/
<UkoeHB> at least you could probably chop out all the unused stuff, would save some binary size
<rbrunner7[m]1> UkoeHB: What would be the key advantages of also checking "semantics"?
<rbrunner7[m]1> Rucknium: The good old times :)
<rbrunner7[m]1> I guess those 44 KB could easily tripple in size for supporting Seraphis
<UkoeHB> rbrunner7[m]1: a valid tx made from a semantics-checked proposal *should* not contain any ways for the tx proposer to fool the tx signer (e.g. burn funds)
<rbrunner7[m]1> If I look at the enumeration of things needed that UkoeHB gave
<rbrunner7[m]1> I see
<UkoeHB> yeah and that semantics checker basically does a trial balance recovery on all self-sends, so in the end you pretty much have all of jamtis
<rbrunner7[m]1> Right now I don't see any shortcuts, just lots and lots of work for those hardware wallet firmware devs, so I guess there isn't something to prepare early.
<rbrunner7[m]1> I mean, something we could do or they could start to do already now, well in advance
<UkoeHB> implement blake2b, x25519, and twofish maybe
<rbrunner7[m]1> Would the problems for mere cold-signers be similar? Like that mentioned "Seed Signer"?
<rbrunner7[m]1> Or are they less, just a secure container for the secret key material, but not able to check transactions?
<UkoeHB> depends if your cold signer is just a normal computer without internet access, or special hardware
<Rucknium[m]> SeedSigner isn't really constrained by storage AFAIK
<Rucknium[m]> UkoeHB: I think SeedSigner is the former
<rbrunner7[m]1> I think that Seed Signer is also its own piece of hardware
<Rucknium[m]> If a RPi is a "normal" compurer
<rbrunner7[m]1> Well, if you can compile the Monero codebase for it, e.g. its ARM incarnation, it's problably not that hard. You just run Seraphis and Jamtis inside then.
<rbrunner7[m]1> If they only want to support a quite small number of coins, or no other coin is as complex as Monero
<Rucknium[m]> Unrelated to HW wallets: There is a group that is trying to list every coin's parameters. silverpill knows more. They had a proposal to "cap" the definition of maximum address length at 128. I don't know what's to be gained from talking with this group, but maybe they have some opinions on Jamtis:  https://github.com/ChainAgnostic/namespaces/issues/41
<selsta> I could be wrong but I think Trezor is quite size constrained since they put everything in firmware and unlike Ledger you can't select what apps / coins to install
<rbrunner7[m]1> Hmm, maybe they will have other models on the market in 2 years time, with more room
<Rucknium[m]> Yes, but then Monero users would have to trash the devices that they own now
<rbrunner7[m]1> Alright, we already reached the full hour. Seems to me much learned, but no actions to take immediately regarding hardware wallets.
<rbrunner7[m]1> selsta: Would you agree?
<selsta> yes
<rbrunner7[m]1> Alright, maybe they will learn soon enough what will hit them :)
<rbrunner7[m]1> I just hope they won't surrender and forego Monero support ...
<UkoeHB> you could probably cut out a lot of the robustness of the semantics checker and just check amount commitments (amount and blinding factor) and recipient addresses (with an 'address ownership proof' and maybe 'address index proof' for selfsends)
<UkoeHB> and don't do the tx proposal conversion
<rbrunner7[m]1> But that would probably need quite a good grasp of the whole Seraphis library, before you can start such cutting-out actions?
<UkoeHB> idk probably not, just one method for converting a tx proposal into a 'hw tx proposal' or somesuch
<UkoeHB> and then some methods demoing how to validate it
<rbrunner7[m]1> Much fun ahead :)
<rbrunner7[m]1> Alright, thanks everybody for attending, was quite an interesting meeting for me

````

# Action History
- Created by: rbrunner7 | 2023-01-19T19:23:45+00:00
- Closed at: 2023-02-13T00:09:43+00:00
