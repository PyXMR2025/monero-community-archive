---
title: 'Monero Tech Meeting #168 - Monday, 2026-05-04, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1382
author: rbrunner7
assignees: []
labels: []
created_at: '2026-05-02T15:44:15+00:00'
updated_at: '2026-05-04T19:04:43+00:00'
type: issue
status: closed
closed_at: '2026-05-04T19:04:43+00:00'
---

# Original Description
Location is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting [here](https://github.com/monero-project/meta/issues/1378).


# Discussion History
## rbrunner7 | 2026-05-04T19:04:43+00:00
````
<rbrunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/1382
<sneedlewoods> hey
<jpk68> Hello
<jberman> waves
<rbrunner7> Alright, on to the reports about last week
<rbrunner7> @dangerousfreedom left a report in this room this morning UTC, about making progress with the curves relevant for FCMP++. Interesting stuff.
<jberman> Beta stressnet launched, kicked off Phase 1 of the integration audit
<jpk68> Made some solid progress on I2P work
<sneedlewoods> testing, small fixes, clean-up, resolve merge conflicts for the rpc and cli and everything downstream
<sneedlewoods> also I was reminded that the "restore height on wallet creation" is still an issue, and I did some research again. IMO this PR (https://github.com/monero-project/monero/pull/10165) would help (if done for release, so it can be used by GUI)
<rbrunner7> I did make some progress regarding Polyseed in the CLI wallet app, but not that much
<koe000> hi, multisig WIP
<rbrunner7> Those 26 days of deviation for mainnet surprise me a bit. I got only about 5 days difference when I compared a Polyseed birthday based height calculcated once without daemon connection, and once with. Maybe not exactly the same thing?
<sneedlewoods> @rbunner7 do you already have a plan how you will get the restore height for the Polyseed?
<rbrunner7> What is done already elsewhere in the code: Ask the daemon if it's possible to reach one, and do some estimate if not. (That's what I claim currently gives about 5 days of difference for mainnet)
<rbrunner7> Maybe I have to check again
<rbrunner7> Your approximation kicks in in the "no daemon" case, right? So Polyseed birthday to blockheight translation will benefit
<jeffro256> howdy, sorry I'm late. Working on beta stressnet, and some potential DoS mitigations 
<rbrunner7> Will take a closer look at your PR this weekend and compare
<sneedlewoods> just checked again, getting 18888 blocks (~26.2 days) deviation > <@rbrunner7> Those 26 days of deviation for mainnet surprise me a bit. I got only about 5 days difference when I compared a Polyseed birthday based height calculcated once without daemon connection, and once with. Maybe not exactly the same thing?
<sneedlewoods> @rbrunner7: yes
<rbrunner7> Ah, I remember, I think I got those 5 days of difference for a Polyseed that was a year old or so
<sneedlewoods> +1
<rbrunner7> Will check again in any case, might be interesting
<sneedlewoods> btw Feather wallet uses a Websocket service to get the restore height from a daemon before the wallet is created, AFAICT
<sneedlewoods> else they use a similar approach to estimate the restore height, based on a known height from last release
<rbrunner7> Don't know, I just saw that the wallet loads a file with correction values if no daemon connection is possible. @tobtoht:monero.social is a bit of a perfectionist :)
<rbrunner7> I remember to wonder whether the code to evaluate and write that file is open sourced or not ...
<ixr3> I saw the Cypherstack audit of the GBPs is discontinued
<ixr3> https://github.com/cypherstack/generalized-bulletproofs-fix/issues/2#issuecomment-4370448089
<rbrunner7> You mean they started, but finally gave up?
<ixr3> Something like that
<rbrunner7> I don't understand much of the things discussed there, so can't judge whether progress was achieved, and if yes how much
<rbrunner7> So hardfork of the beta testnet to FCMP++ is in 2 days?
<rbrunner7> Ah, beta stressnet
<rbrunner7> "testnet" would be a bit misleading
<jberman> @ixr3: Erm, I wouldn't exactly say that's the conclusion from that comment. Have they responded to that comment elsewhere?
<jberman> @rbrunner7: Yep :)
<rbrunner7> Is there a party somewhere? :)
<sneedlewoods> +1
<rbrunner7> No, seriously, quite a milestone I would say
<jberman> Not that I know of heh
<ixr3> @jberman: They didn't respond, but doesn't KayabaNerve gently asked them to end it? That's how I read it. I may be wrong.
<jberman> My read of that comment is just kayaba not wanting to demand continued work on it as it's unpaid. And the general plan with GBP's is to continue with zk security as an additional qualified independent party. Though CS is obviously still free to respond there
<jbabb> +1
<ixr3> +1
<rbrunner7> Could you call this beta stressnet code something like "feature complete"? Except multisig, and hardware wallet support maybe
<jberman> and hot/cold wallets and tx proofs (for now, jeffro mentioned he's aiming to have hot/cold wallets complete before beta is finished)
<rbrunner7> Sounds good
<rbrunner7> Will be interesting to see how this software reacts if the network gets stressed
<rbrunner7> How about that PoW for large transactions? How was that called again?
<jberman> ah yes, PoWER
<jeffro256> @jberman: This is true. Working on it now, I want to have it done by the end of the week (fingers crossed)
<sneedlewoods> +1
<jeffro256> Depends on if I can lock in and stop jumping between different tasks 
<jberman> @hinto:monero.social has implemented PoWER ( https://github.com/seraphis-migration/monero/pull/230 ), will review that fully and we can aim to have that in for beta too
<rbrunner7> I think it would be nice to have that in early. Seems to me it's an important part of the overall system
<jeffro256> +1
<jpk68> @jeffro256: When I'm in a being-locked-in competition and my opponent is Jeffro
<jeffro256> +1
<jberman> @rbrunner7: fwiw it shouldn't have a very noticeable effect on perf (if noticeable at all), it's more of a layered in DoS protection mechanism
<ixr3> Will beta include P2P Encryption+Authentication?
<rbrunner7> I see. But still important to test a brand new and not exactly simple part of the whole system
<jberman> @ixr3: ah right, I mentioned we can get that tested in beta stressnet too. I think it would be good to get in. I can start a list of things we want in for the beta
<rbrunner7> Good that you can hardfork the thing pretty much as often as you like :)
<ixr3> @jberman: I hate that it increases the attack surface
<jeffro256> @ixr3: Interesting, this is a good idea 
<jberman> I hate that nodes default relay data in plaintext :)
<jpk68> +1
<jeffro256> TBC Authentication wouldn't really be present at the beginning AFAIK, just encryption 
<jberman> https://github.com/seraphis-migration/monero/issues/354
<jeffro256> Which changes the failure mode for relay-level confidentiality from passive to active
<vtnerd> +1
<rbrunner7> "wishlist", how cute
<jpk68> And this would just be integrating the existing P2P encryption PR?
<jpk68> Using TLS
<jberman> yep https://github.com/monero-project/monero/pull/8996
<rbrunner7> That's a solid start I guess?
<rbrunner7> Alright. Quite a large undertaking, getting this all in.
<rbrunner7> Do we have something left to discuss today?
<rbrunner7> Does not look like it. So thanks everybody for participation, and read you again next week!
<sneedlewoods> thanks everyone
<jpk68> Thanks :)
````


# Action History
- Created by: rbrunner7 | 2026-05-02T15:44:15+00:00
- Closed at: 2026-05-04T19:04:43+00:00
