---
title: 'Monero Tech Meeting #173 - Monday, 2026-06-15, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1403
author: rbrunner7
assignees: []
labels: []
created_at: '2026-06-13T04:48:38+00:00'
updated_at: '2026-06-15T19:54:07+00:00'
type: issue
status: closed
closed_at: '2026-06-15T19:54:07+00:00'
---

# Original Description
Location is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting [here](https://github.com/monero-project/meta/issues/1397).


# Discussion History
## rbrunner7 | 2026-06-15T19:54:07+00:00
````
<rbrunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/1403
<selsta> hi
<vtnerd> hi
<jpk68> Hello
<jeffro256> Howdy
<tobtoht> hi
<sneedlewoods> Hey
<jberman> waves
<rbrunner7> Ok, with those waves I think we are ready for the reports from the last 2 weeks. (There was no meeting last Monday because of Monerokon.)
<sneedlewoods> worked on tests for the wallet-rpc based on Wallet API and got the only failing test multisig fail at a later stage now
<rbrunner7> @dangerousfreedom left a report in this room a bit less than 1 day ago. He made good progress and has FCMP++ running in Python as it seems.
<jpk68> Wrote some docs on seed encryption and wordlists, made a few different patches, I2P work, etc.
<rbrunner7> I myself could get the Polyseed PR out the door: https://github.com/monero-project/monero/pull/10765
<tobtoht> +1
<jpk68> +1
<jberman> +1
<selsta> v0.18.5.1, release date got moved up because of the p2pool vuln
<tobtoht> How fast do we want to get this out?
<vtnerd> I updated lws fcmp++ pr to newest lws and fcmp code
<selsta> tobtoht: as soon as possible, of course not rushed
<UkoeHB> Hi, worked on multisig, reviewed jberman’s curve trees impl. Sneedlewood there may be overlap in the multisig issues we are facing.
<jberman> we solved the windows GUI binary crash for stressnet (was an upstream issue), submitted the FCMP++ tree builder PR upstream, integration audit phase 1 should be complete soonish (working with Trail of Bits today on finalizing), reviewed jeffro's PR to speed up pool fetching
<jberman> (while testing found a separate issue in incremental pool fetch logic), started reviewing jeffro's hot-cold PR in earnest, continuing investigating sporadic double spend errors observed on stressnet
<sneedlewoods> UkoeHB: I'm not on fcmp++ branch yet
<jeffro256> me: worked on header compression and testing/review upstream PRs 
<rbrunner7> Ok, if we are through with the reports already, I would like to open a first round of discussion regarding Polyseeds in connection with passphrases, as mentioned this morning UTC here and in -community
<UkoeHB> sneedlewoods: got it
<tobtoht> I'm OK with not storing / showing the passphrase, if it is communicated to the user that they are responsible for remembering if it was used.
<rbrunner7> My PR has code and a "UX approach" inherited from a patch originally done by @tobtoht:monero.social : A passphrase that the user gives gets stored in the wallet.keys file, and the CLI wallet app seed command displays the passphrase together with the Polyseed
<jeffro256> @tobtoht: As a one-time thing, right?
<tobtoht> Every time the seed is shown.
<rbrunner7> There is an argument to do that as follows: If you use a (seed offset) passphrase with a legacy seed, and you display a seed using the CLI wallet command seed, you get everything needed to restore that wallet.
<jpk68> Is the same thing done for legacy seed offsets?
<tobtoht> @tobtoht: Or, perhaps only during restore.
<rbrunner7> Why? Because the offsetted secret bits get translated to seed words
<rbrunner7> If you want to do the same, i.e. display everything needed for restore, with Polyseed, you have to display the passphrase
<rbrunner7> You can't turn the offsetted private key bits into a new Polyseed
<rbrunner7> But well, that's probably to discuss. Some people seem to want to hide the use of passphrases as much as possible, maybe even accepting differences between Polyseed UX and legacy seed UX when doing so
<rbrunner7> @jeffro256:monero.social made his position pretty clear already in a review comment, if I understood that correctly: Displaying the passphrase again undermines the very essence of them
<rbrunner7> For me, I have right now the same opinion as @tobtoht:monero.social regarding display: No strong preference, under the condition the user gets informed clearly.
<rbrunner7> Other opinions?
<tobtoht> @rbrunner7: Under what threat model? The one where you're held at gunpoint and forced to open a wallet, you open a fake wallet with passphrase, which might give away that there is a real wallet with more funds.
<tobtoht> Use a fake wallet without passphrase?
<tobtoht> Or: someone could steal your computer, crack one of the wallets (with passphrase), which might reveal that another wallets exists and come back for more.
<tobtoht> Use a stronger password?
<rbrunner7> A bit of info while we wait: Cake Wallet and Feather Wallet currently do show the passphrase when displaying a Polyseed if one was used
<jeffro256> I mean, anything is possible to do. But accorsing to the standard, a bit is present in the Polyseed which determines whether or not the Polyseed is encrypted with a passphrase. So if the attacker is smart enough to know about offsets/passphrases, they could look at the seed and determine if it's an encrypted Polyseed or not
<tobtoht> We're not using Polyseed encryption.
<rbrunner7> A little correction: My PR does not use Polyseed encryption on its own. It can restore, but does not produce. It uses good old seed offsetting, which is "invisible"
<jeffro256> I'm less concerned about trying to mitigate coercion in this case, but trying to mitigate more run-of-the-mill data exfiltration attacks due to the seed not being encrypted at rest. 
<rbrunner7> It's a little side question what you do when encountering an encrypted Polyseed when restoring: Insisting on the passphrase, or silently restore a "wrong" wallet
<jeffro256> If i'm the kind of person to use a passphrase to encrypt my seed at rest, I expect the seed to be encrypted at rest, and to have to enter the passphrase to decrypt 
<rbrunner7> @jeffro256:monero.social: Not sure I understand: Would that be a vote to use Polyseed encryption?
<jpk68> +1
<rbrunner7> And not seed offsetting?
<tobtoht> You'd rather have the encryption bit be present to give away the fact that you likely have a decoy wallet?
<jeffro256> @rbrunner7:monero.social:  Doing both would be a bit complicated for UX, but I don't see why not
<jeffro256> @tobtoht: That's a Polyseed thing, not a Monero thing 
<rbrunner7> You mean give the option at wallet creation?
<tobtoht> @jeffro256: I know. I'm saying that's a bad design decision.
<tobtoht> A seed should never reveal if a passphrase was used.
<rbrunner7> Ok, anyway, with this we have two questions open already: Whether to "encrypt at rest", and whether displaying passphrases again
<jeffro256> I'd rather reject Polyseeds with encrypted passphrases than to siliently do them completely wrong and store them without passphrases 
<jeffro256> @tobtoht: I'm also agree, I think that the passphrase bit was not a great idea. 
<rbrunner7> If we reject encrypted Polyseeds, you can' restore Cake wallet seeds that used a passphrase. A bit unfortunate ...
<rbrunner7> *you can't
<rbrunner7> Seems to me we have some hard facts that we can't fully avoid. Polyseed encryption and feature bits are as they are, and Cake Wallet uses that.
<rbrunner7> So we probably search for the least evil now.
<rbrunner7> Another thing: If we drop that passphrase storage in account now in the core software, we more or less force all third-party wallets that use the monero_c library to give up passphrase display. Which the devs of those apps may or may not like.
<rbrunner7> We could of course to continue to store, but not display with the seed command.
<jeffro256> @rbrunner7: What is the point of displaying the passphrase again? 
<rbrunner7> And swallow the toad of having a wipeable_string serialization :)
<jpk68> It seems as if legacy seeds currently do not show the offset passphrase after being restored. Is this correct?
<tobtoht> @jeffro256: Without it you can't restore the same wallet.
<rbrunner7> To display everything that is needed to restore the wallet, as it's the case with legacy seeds, even if they use a passphrase.
<rbrunner7> Symmetric UX.
<jeffro256> @tobtoht: Yes, but isn't the point of the passphrase not being in Polyseed that you user has to remember it??
<ofrnxmr> +1
<sneedlewoods> @jpk68: AFAIK they show a new legacy seed
<jeffro256> Why encrypt something if you provide the encryption keys right next to the ciphertext ?
<tobtoht> A dummy passphrase field may be useful to prevent (future) .key file incompatibilities with wallets that used the patch.
<sneedlewoods> and no passphrase
<jpk68> But wouldn't the exact same thing happen with Polyseed offsets? It would just restore an 'incorrect' wallet with no passphrase?
<rbrunner7> @sneedlewoods: Exactly. And that "new" legacy restores you the same wallet, without passphrase.
<sneedlewoods> it does restore the correct wallet though
<sneedlewoods> with legacy
<jpk68> Ah, I see. Thanks
<rbrunner7> Yes. And with Polyseed without passphrase, you get the wrong wallet.
<rbrunner7> But well, as I said, with some info on screen you can probably get away with that UX difference. And I think we do expect people to remember passphrases themselves.
<ofrnxmr> +1
<sneedlewoods> and if they forget they can still show their ssk and restore from there, just without Polyseed features!?
<rbrunner7> @tobtoht:monero.social: Not sure whether a "dummy" passphrase would be enough. If the apps cannot query it, they can't display a passphrase if they so want.
<rbrunner7> Yes, there is a new CLI wallet legacy_seed command that gives you exactly that legacy seed.
<jeffro256> Here's how I would see the UX flow going: user w/ encrypted Polyseed asks for seed, wallet SW seeds that Polyseed is encrypted, wallet SW asks user for passphrase, user gives it, wallet validates password and shows original, encrypted Polyseed phrase
<jeffro256> Passphrase stays in the user's head 
<sneedlewoods> @rbrunner7: Then I don't see a problem in not showing the passphrase and inform the user to keep track of it.
<jeffro256> wallet2 uses a password for in-memory encryption, and needs it for ops which require a decrypted spend key. For UX purposes, that password could be the same as the Polyseed password 
<rbrunner7> That's now a confusing amount of possible ways to do it
<rbrunner7> I think an important point is how much weight people give the argument of "encryption at rest" which is not given with the PR right now
<jberman> @jeffro256: this UX makes sense to me as well. I find it strange the legacy seed UX displays a different seed than the one the user has already written down / was supposed to write down
<ofrnxmr> I never liked that my polyseed wallets show the passphrase next to the seed. The argument is that, if they have access to your wallet where they can access the seed, they already have access to the spend and vjew keys anyway
<ofrnxmr> @jberman: This always confused me, and i still dont know which seed im supposed to use when restoring
<rbrunner7> And whether with or without offsest, right? :)
<rbrunner7> But that's legacy. Looking forward, it would be nice to arrive at some loose consensus how to do it properly with Polyseeds.
<rbrunner7> A compromise could be, as I seed it: A) Not using Polyseed encryption, because that gives the passphrase use away, B) continue to store, in the interest of third party devs who have strong opinion to (continue to) display passphrases, but C) NOT displaying passphrases in our UI
<sneedlewoods> +1
<tobtoht> +1
<jeffro256> @ofrnxmr: Except that if it was implemented correctly, they wouldn't because they have the encrypted seed phrase, not the real key material used to derive the spend key
<rbrunner7> But those wallets happily show you the keys, no?
<rbrunner7> The raw keys
<jeffro256> If they have the encrypted seed phrase and you have a weak password, then yeah, you're cooked.
<sneedlewoods> @rbrunner7: yep
<sneedlewoods> at least for legacy seed and if restored by key
<rbrunner7> I don't think you can drop raw key material display altogether
<ofrnxmr> I prefer C, if only because i dont like to see my passwords in plain text unless i am typing them
<rbrunner7> Well, my proposal has 3 parts, all implemented A) and B) and C)
<rbrunner7> Maybe I should also mention D) sadly, no "encryption at rest" is implemented for Polyseeds
<jeffro256> @rbrunner7: wallet2 needs a passphrase though of some sort if your wallet2 file has a password because the keys are encrypted in-memory. So while at rest, even if someone dumped your while memory, they theoretically can't get your raw keys w/o your passphrase
<rbrunner7> because of complicated and interplaying requirements
<jeffro256> So yes, displaying raw key material is an action, but it requires further knowledge from the user. This is how Polyseed passphrases should be handled. 
<rbrunner7> Correct, of course. I was talking about wallet UIs. I don't think you can only ever display seeds there, and hide raw key values completely from users. They may need raw keys.
<tobtoht> You necessarily store the spend keys, so you might as well store the passphrase for better UX. Unless you're concerned about information leaks. Which you can defend against as I pointed out earlier.
<tobtoht> Wallet password != polyseed passphrase
<rbrunner7> Wallet password as Polyseed passphrase would be quite a serious deviation from current legacy seed UX
<rbrunner7> and one where I don't see tangible benefits right now
<jeffro256> @tobtoht: You necessarily store them encrypted, there's a difference
<tobtoht> You would store the passphrase encrypted as well?
<rbrunner7> It's part of the account, which gets encrypted with the wallet password, like everything else
<jeffro256> I wouldn't store the passphrase, period, just like how you don't store the wallet2 passphrase in-memory, because that would defeat the purpose of the in-memory encryption 
<rbrunner7> The wallet2 password, you mean?
<rbrunner7> @jeffro256:monero.social: How do you weight the argument that with this, we force the hand of all third-party devs that use monero_c ?
<jberman> A user probably shouldn't need both their wallet passphrase and seed passphrase to open their wallet / spend, and a user probably shouldn't use the same wallet passphrase and seed passphrase
<tobtoht> +1
<jpk68> +1
<rbrunner7> I don't think that's on the table as proposal?
<tobtoht> (nit: wallet password. seed passphrase.)
<jberman> +1
<jberman> So it makes sense to be able to arrive at a spend key in an already created wallet without needing the seed passphrase
<rbrunner7> Not sure I understand. How would that not be case?
<jeffro256> @jberman: I disagree. Obviously, when it really gets down to it, it is subjective. But if explicitly add a passphrase to my seed, I expect it to be encrypted with that passphrase...
<jeffro256> *But if I
<rbrunner7> @jeffro256:monero.social: If only there wasn't the tradeoff to give passphrase use away that way.
<jberman> @rbrunner7: it means we'd either need to store the seed passphrase, or the actual spend key somewhere that can be arrived at with just wallet password. Aka probably would make sense to store seed passphrase to achieve that UX
<jeffro256> @rbrunner7: to be frank, it shouldn't be the core repo's problem when downstream jumps the gun and implements something incorrectly without trying to upstream it  > <@rbrunner7> @jeffro256:monero.social: How do you weight the argument that with this, we force the hand of all third-party devs that use monero_c ?
<rbrunner7> Which is unfortunate, but as I said, Polyseed is as it is
<rbrunner7> The actual spend key is always at hand after you gave the wallet password?
<tobtoht> +1
<jberman> @jeffro256: my view of the benefit of a seed passphrase is that if someone finds your seed copy somewhere laying around, you have extra protection from the seed passphrase. It's not for in-memory protection / not an expected UX to have to re-input seed passphrase all the time
<tobtoht> +1
<ofrnxmr> +1
<rbrunner7> Yeah, right, was also thinking along that line, but then you can trivially store 2 halves of your seed in two different places ...
<tobtoht> That wouldn't make it a decoy wallet.
<jeffro256> @jberman: I definitely think that that was the primary intended purpose. I'd be willing to accept that the spendkey and original-passphase-encrypted Polyseed only stays encrypted with the wallet2 password while in-memory. But the passphrase absolutely, positively should not be stored in account keys inside the file 
<tobtoht> @tobtoht: It would obviously be "half a seed"
<rbrunner7> Well, as I said, without drastic measures like forking Polyseed to Polyseed++ without encryption feature bit and overruling tevador's design "encyption at rest" will always have the unfortunate "feature" of giving the passphrase use away.
<rbrunner7> Which people may find worse than having encryption at rest - or not having that? You know what I mean.
<rbrunner7> Well, I for one could live with not storing passphrases. Makes the code quite a bit simpler, actually. And yes, the core software probably has the competence to force the hand of third-party devs in some points.
<rbrunner7> Wallets who do want to continue to display passphrases have the option to do it using a wallet "attribute". There just would be no upgrade path for wallets written by monero_c that I can how to implement.
<rbrunner7> *that I can see how to implement
<rbrunner7> Alright, we might get some more votes later this week from people who read this.
<rbrunner7> Any more arguments and votes right now about this?
<rbrunner7> If not, anything else to discuss right now?
<vtnerd> What about the lgpl license?
<vtnerd> I don't know much about how that license works tbh
<rbrunner7> What is LPGL? Polyseed?
<vtnerd> Yes
<tobtoht> https://github.com/tevador/polyseed/blob/master/LICENSE
<tobtoht> Appear so
<rbrunner7> Uff...
<rbrunner7> No idea, really.
<vtnerd> I think it works, but then monerod becomes defacto lgpl when compiled in
<rbrunner7> Taken to the extreme, could this prevent using Polyseed in any other form than dynmic lib / DLL?
<rbrunner7> *dynamic lib
<tobtoht> Not an option.
<rbrunner7> Is that another license, that with the DLL option?
<tobtoht> We must statically link for release binaries.
<rbrunner7> Ah, you mean that's not something we can technically do.
<tobtoht> +1
<jeffro256> This might be helpful: https://licensecheck.io/blog/lgpl-dynamic-linking
<rbrunner7> That's a whole new can of worms. Did everybody using Polyseed so far just ... well ... glance over this?
<jeffro256> According to this website, the core repo already fits the criteria for static linking with Polyseed
<tobtoht> We would need to add a license command to CLI to show the copyright notice though I think?
<rbrunner7> I would be very grateful if somebody in the know here (which currently is not me) could research a bit here and then report back
<jeffro256> I don't know about Cake 
<jeffro256> @tobtoht: I believe so 
<vtnerd> yeah it looks fine because most wallets are providing 100% source anyway
<tobtoht> Or we could ask tevador to consider relicensing?
<vtnerd> so it meets the “relinking” portion since the source is provided
<rbrunner7> How would such a "license" command look? Would it need to provide the whole text of the license?
<vtnerd> but someone attempting a closed source app “on top” of monero wallets would have to disable/remove polyseed or provide re-linking capability
<rbrunner7> Good luck with that :)
<tobtoht> @tobtoht: The only copyrightable contributions are from tevador.
<rbrunner7> It's unfortunately late to stumble over this problem
<rbrunner7> Is everything else that we compile in really MIT license?
<rbrunner7> Did anybody check that already?
<tobtoht> I vaguely remember rapidjson not even being free software because of some weird clause in its license.
<rbrunner7> Splendid
<rbrunner7> Ok, I guess we have to leave this as pending for the moment.
<tobtoht> We have to replace it eventually anyway given it's unmaintained.
<jeffro256> tevador put mx25519 under the same license BTW 
<rbrunner7> Which we also use?
<jeffro256> So we would need to sort that out before FCMP++
<tobtoht> +1
<jeffro256> mx25519 is used in the CARROT code 
<rbrunner7> And that's considerably newer than Polyseed?
<rbrunner7> Which could mean that Tevador really likes it that way?
<jeffro256> Initial commit was August 2022 
<tobtoht> We could just ask them ^^
<rbrunner7> Maybe they will read this here, who knows.
<rbrunner7> Alright, we are well over the hour, and probably won't have any real breakthroughs today, so let me close the meeting proper. Thanks everybody for attending, read you again next week!
<tobtoht> Well good we stumble upon this issue now and not two weeks before the fork
<jeffro256> Thanks everybody 
<tobtoht> Thanks @rbrunner7:monero.social
<rbrunner7> Yeah!
<jeffro256> I can work on a license command PR for the CLI, so that it can easily be updated as we possible ass LGPL dependencies
<tobtoht> +1
<selsta> Regarding LGPL 3, shouldn't it be ok with gitian/guix giving users a way to rebuild the executable?
<sneedlewoods> Thanks everyone, good meeting
````


# Action History
- Created by: rbrunner7 | 2026-06-13T04:48:38+00:00
- Closed at: 2026-06-15T19:54:07+00:00
