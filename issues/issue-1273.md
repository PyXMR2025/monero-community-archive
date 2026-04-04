---
title: 'Monero Tech Meeting #139 - Monday, 2025-09-29, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1273
author: rbrunner7
assignees: []
labels: []
created_at: '2025-09-26T14:37:58+00:00'
updated_at: '2025-09-29T18:29:40+00:00'
type: issue
status: closed
closed_at: '2025-09-29T18:29:40+00:00'
---

# Original Description
Location is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting [here](https://github.com/monero-project/meta/issues/1270).


# Discussion History
## rbrunner7 | 2025-09-29T18:29:40+00:00
````
<r​brunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/1273
<s​needlewoods> Hey
<h​into> hello
<j​berman> *waves*
<v​tnerd> Hi
<r​brunner7> Alright, on to the reports
<s​needlewoods> made the first tx, but rushed through the implementation, now have to fix some areas to make sure it behaves the same as before and all the command options work as expected
<s​yntheticbird> hello
<r​brunner7> SNeedlewoods: You mean with the CLI wallet running on Wallet API?
<s​needlewoods> exactly
<r​brunner7> Nice milestone :)
<r​brunner7> I am content that my improved peer selection PR was merged. Thanks to the reviewers. Must be my first PR for a year or so ...
<rucknium> +1
<sneedlewoods> +1
<jberman> +1
<s​needlewoods> picked almost all the low hanging fruits and now more complex stuff is still left
<h​into> me: thinking about how to implement PoWER with as few diffs as necessary
<sneedlewoods> +1
<v​tnerd> Got lws server _mostly_ integrated with carrot/fcmp. Legacy and view balance keys work and pickup incoming and spends, but view-incoming doesn't fully work with subaddresses yet
<r​brunner7> hinto: Cuprate, yes?
<j​berman> me: announced FCMP++ & Carrot alpha stressnet v1 (https://github.com/seraphis-migration/monero/releases/tag/v0.19.0.0-alpha.1), started opening some smaller PR's from the integration to the main repo
<h​into> for both `monerod` and `cuprated`
<r​brunner7> Somebody should put up a nice countdown to October 3, with carrots or so
<jberman> +1
<jeffro256> +1
<r​brunner7> I think we reach the point where it becomes quite improbable that the hardfork to FCMP++ will never come, like the one to Seraphis :)
<r​brunner7> So first stressnet will still run without PoWER, obviously
<j​berman> Yep
<r​brunner7> Maybe a good chance to see what happens without that as protection
<k​ayabanerve> Hello, y'all! Congrats to everyone on the tagged network release!
<h​into> jberman: is there any notable behavior or logs to look for when running the 0.19 binary?
<j​berman> When you run the migration, log level 1 is fun to watch the tree roots and n leaves in the tree
<hinto> +1
<h​into> also would the official `monerod` release be an opportunity for `v1.0.0`?: https://github.com/monero-project/meta/issues/721
<k​ayabanerve> I have the partially off-topic update of having been working on a new RPC client which has well-defined bounds, and how that's apparently quite difficult. Nothing from me about FCMP++ other than the comment the Helios/Selene curves will be updated.
<r​brunner7> hinto: That's almost a heresy
<k​ayabanerve> (solely their constants)
<r​brunner7> No big deal, implementation-wise, right?
<k​ayabanerve> No, it'll be trivial. Just updating constants in Rust, and the ones duplicated in C++ by jeffro256 if any exist.
<rbrunner7> +1
<r​brunner7> Helios/Selene, now even more curvy
<k​ayabanerve> It will be a hard fork though. So stressnet will use the old curves until a new net is created.
<jberman> +1
<reverseengineer> hey
<r​brunner7> And of course no speed difference, the code being constant-time
<k​ayabanerve> And because the new parameters won't involve changing any of our methodology
<k​ayabanerve> Oh. There may be very slight differences in the exponentiation function, used for point (de)compression, depending on the amount of bits set in the new choices of prime numbers.
<j​berman> Something probably worth mentioning in here: I'm likely going to start working on Serai soon-ish (potentially within the next week or 2), prioritizing FCMP++/Carrot tasks such that any work I do on Serai should not delay any FCMP++/Carrot work / impact the timeline in any way
<r​brunner7> Is that within the CCS framework, or a different "account" to pay for your Serai work?
<j​berman> different account, completely separate from CCS
<r​brunner7> Ok, good so now misunderstandings and complaints will crop up
<r​brunner7> Some people on Reddit are trigger-happy with such stuff :)
<r​brunner7> (Not that this means much)
<r​brunner7> Alright, looks like we are through with the reports. Anything else to discuss today?
<r​brunner7> Does not look like it. So thanks everybody for attending, read you again next week!
<s​needlewoods> Question about fee priority:
<s​needlewoods> (First a little shout-out: thanks to [this PR](https://github.com/monero-project/monero/pull/9838) the fee priority code in wallet2 is less confusing now.)
<s​needlewoods> Below is some common terminology that's used for the 4 different levels + a default value
<s​needlewoods> 0 Default
<s​needlewoods> 1 Unimportant / Low
<s​needlewoods> 2 Normal      / Medium
<s​needlewoods> 3 Elevated    / High
<s​needlewoods> 4 Priority    / Very High
<s​yntheticbird> JIT
<s​needlewoods> Unfortunately the Wallet API uses a differnt term for the fifth element in the enum: `Priority_Last` ([src](https://github.com/monero-project/monero/blob/master/src/wallet/api/wallet2_api.h#L73-L79)) and I'm not sure if it is supposed to be the same as "4 / Priority / Very High". The original PR does not explain it and the GUI only uses "low", "medium" and "high" ([src](https://gi<clipped 
<s​needlewoods> thub.com/monero-project/monero-gui/blob/440012b454a39de860c97226e33af204ced868ec/src/libwalletqt/PendingTransaction.h#L62-L66))
<s​needlewoods> So my question, should I
<s​needlewoods> a) rename `Priority_Last` to `Priority_VeryHigh`?
<s​needlewoods> b) rather add `Priority_VeryHigh` as fifth element and move `Priority_Last` to the sixth? In case `Priority_Last` is used somewhere e.g. to make sure to always get the highest priority even if the enum was updated, with `Priority_Last-1`.
<s​needlewoods> c) do nothing?
<r​brunner7> Will try to have a look to build an informed opinion
<s​needlewoods> alright thanks, nothing else to discuss for me
````


# Action History
- Created by: rbrunner7 | 2025-09-26T14:37:58+00:00
- Closed at: 2025-09-29T18:29:40+00:00
