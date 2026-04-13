---
title: 'Monero Tech Meeting #165 - Monday, 2026-04-13, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1369
author: rbrunner7
assignees: []
labels: []
created_at: '2026-04-10T18:25:57+00:00'
updated_at: '2026-04-13T18:48:05+00:00'
type: issue
status: closed
closed_at: '2026-04-13T18:48:04+00:00'
---

# Original Description
Location is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting [here](https://github.com/monero-project/meta/issues/1366).


# Discussion History
## rbrunner7 | 2026-04-13T18:48:04+00:00
````
<r​brunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/1369
<s​needlewoods> Heyx
<k​oe000> Hi
<i​amnew117> hello
<j​effro256> Howdy
<j​berman> *waves*
<r​brunner7> Ok, let's start with the reports from last week. Me: Started to work on implementing Polyseed in the core software in earnest.
<s​needlewoods> squashed, rebased and pushed the wallet-rpc ([src](https://github.com/monero-project/monero/compare/master...SNeedlewoods:seraphis_wallet:x_remove_wallet2_from_rpc), commit 1-3 are old PRs, [4th](https://github.com/monero-project/monero/commit/193d6d4cae5563643073203644991adab42d72b8) commit are new changes for the Wallet API and [5th](https://github.com/monero-project/monero/commit/c2d32d974c682f8da74d4cccea9f396917d8562b) commit are the wallet-rpc changes)
<s​needlewoods> but didn't make a PR yet, because I'm still having issues with some functional tests (`k_anonymity` works most of the time if I put a `sleep(10)` in front of `refresh()`)
<s​needlewoods> Other tests that still fail: `multisig`, `transfer`
<plowsof> *waves*
<k​oe000> me: finished carrot_core review, research/discussion on Jamtis-PQ, started looking at multisig for the hf
<j​berman> me: FCMP++ integration audit talks with candidates, working on benchmarking the latest FCMP++ lib with changes to GBP's applied
<j​effro256> ME: H1 reports, worked on carrot_core review with ukoe, reviewing some PRs, talking with audit candidates, taxes
<j​pk68> Hello
<r​brunner7> Quite a lot of discussions going on regarding Carrot, implementing the Carrot key hierarchy or not, and Jamtis-PQ. Not sure it makes sense to discuss something here today, but anyway, a question to the room: Is my impression correct that "sentiment" is shifting away from implementing the Carrot key hierarchy?
<j​effro256> I plan on implementing it, just not necessarily before the first FCMP++ release binary
<ixr3> +1
<j​effro256> It is not a blocker, but I still plan on at least having the option for release available
<j​berman> I don't have too much of an opinion on it at this time except that I would strongly prefer that the Carrot key hierarchy does not take up time that could be spent on tasks for the fork
<r​brunner7> Alright. Maybe you saw it already, Tevador made an update of their Jamtis gist. I marvelled at the proposed key hierarchy here: https://gist.github.com/tevador/639d083c994c1ef9401832c08e2b7832#44-key-hierarchy
<r​brunner7> Have to admit that looking at this makes me a bit uneasy ...
<k​oe000> I don't plan to work on it, would prefer to focus on other things down the line (Jamtis-PQ, fee discretization, scanning optimizations, etc.). Related, I'd rather not do multisig for any new protocols and instead just continue with bare minimum support for existing/new legacy multisig wallets.
<r​brunner7> koe000: Would that mean no multisig for Carrot from you for the time being?
<k​oe000> It means only multisig for Legacy-Carrot.
<r​brunner7> Ah, yes, that.
<k​oe000> Multisig is frankly too difficult and too unused to justify full support and improvements with current talent availability.
<r​brunner7> Multisig for Legacy-Carrot will have a better UX than today because no more need for key data exchange after each transfer, right?
<k​oe000> Should be the same UX, legacy-carrot doesn't have view-received.
<j​effro256> ^^^
<j​effro256> Will it does have view-received, but it doesn't have view-balance
<j​effro256> *well
<j​berman> We're close to the finish line here on FCMP++/Carrot fork, I think focusing our immediate effort on fork blockers will significantly help get this across the line and complete Monero's most significant upgrade by sheer work alone
<k​oe000> Right sorry
<j​effro256> Legacy wallets cannot calculate key images without interaction, regardless of CARROT
<j​effro256> CARROT by itself only allows *new* key hierarchies which have those better UX properties
<r​brunner7> Maybe this will develop into a good dynamic as soon as the first testnet with the candidate FCMP++ / Carrot code is running.
<r​brunner7> I understand the argument about multisig: Somebody built a really nice GUI tool for doing Monero multisig, *finally* you could say, and it got almost zero attention
<r​brunner7> But anyway, I think we have a certain responsibility to at least keep multisig working after the FCMP++ hardfork
<k​oe000> Yes the goal is to keep it working.
<rbrunner7> +1
<jberman> +1
<r​brunner7> Haveno uses it, for one
<j​pk68> What is meant by "full support" for multisig? Support in the core implementation?
<j​pk68> Doesn't monero-oxide maintain one for Serai
<j​pk68> *an implementation of multisig
<s​needlewoods> (for the record, I assume you're talking about [this](https://github.com/freigeist-m/monero-multisig-gui/tree/master/))
<k​oe000> Full support as in: good docs with security attributes described, all addressing protocols supported, best-in-class multisig protocols implemented for best UX, upgrading from 'experimental' status to 'official' status, availability of talent for ongoing support and development.
<jpk68> +1
<r​brunner7> SNeedlewoods: Exactly that one, thanks for the link
<r​brunner7> The latest Jamtis has such an inflation of secrets and keys that it will take quite some effort to just memorize them all to be able to follow discussions :)
<r​brunner7> I really wonder whether some day somebody will come along and present a system with similar properties that is 10 times less complex ...
<r​brunner7> Probably not, but one can dream :)
<r​brunner7> Alright, after these reports, and confirming that we are shooting for keeping multisig working more or less within the current capabilities - do we have to discuss something else today?
<r​brunner7> Doesn't look like it. So thanks everybody for attending, read you again in 1 week!
<k​oe000> Thanks
<s​needlewoods> thanks everyone, see you
<j​pk68> Thanks
<i​xr3> Thanks
<j​effro256> Thanks everyone
<i​xr3> Great
<r​brunner7> Really looking forward to have *z_ur (unlock-received post-quantum key)* in my Monero wallets, chuckle
<tevador> rbrunner7: Each of the keys has a purpose. AFAICS you cannot remove any of the keys without losing features.
<r​brunner7> I don't doubt, and don't get me wrong, I don't want to ridicule anything. I am in awe about the construct, just uneasy about the complexity. I think to achieve any meaningful simplification one would have to find a radically different approach.
````


# Action History
- Created by: rbrunner7 | 2026-04-10T18:25:57+00:00
- Closed at: 2026-04-13T18:48:04+00:00
