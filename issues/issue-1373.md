---
title: 'Monero Tech Meeting #166 - Monday, 2026-04-20, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1373
author: rbrunner7
assignees: []
labels: []
created_at: '2026-04-17T06:14:18+00:00'
updated_at: '2026-04-20T18:51:47+00:00'
type: issue
status: closed
closed_at: '2026-04-20T18:51:47+00:00'
---

# Original Description
Location is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting [here](https://github.com/monero-project/meta/issues/1369).


# Discussion History
## rbrunner7 | 2026-04-20T18:51:47+00:00
````
<r​brunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/1373
<j​pk68> Hello
<s​needlewoods> hey
<v​tnerd> Hi
<k​oe000> Hi
<j​berman> *waves*
<r​brunner7> Alright, let's proceed to the reports from last week. Me: Made good progress implementing Polyseed in the CLI wallet
<s​yntheticbird> Hi
<k​oe000> Me: not much done. Started mapping multisig changes required. Reconstructing the signed message will be most painful.
<s​needlewoods> added all new Wallet API changes from the wallet-rpc work to [#9464](https://github.com/monero-project/monero/pull/9464)
<s​needlewoods> rebased [#10232](https://github.com/monero-project/monero/pull/10232) onto that and [#10233](https://github.com/monero-project/monero/pull/10233) and the wallet-rpc onto #10232
<r​brunner7> Quite a number of balls in the air that you juggle there now :)
<j​pk68> I have been researching SAM protocol parameters (encryption type, etc.)
<j​pk68> Sadly, post-quantum support is not ready yet
<r​brunner7> That's for I2P, right?
<j​pk68> Yes
<j​berman> Preparing all code for FCMP++ beta stressnet (aiming to have the code all ready by Wednesday's MRL meeting), PR review, audit followup, drafted a blog post to retroactively deprecate Monero's custom unlock_time (waiting on analysis of blockchain data to finalize)
<jbabb> +1
<r​brunner7> Yeah, I wonder also how many real locks have sneaked in since we don't propagate them anymore
<s​needlewoods> I think I'll mark the PRs to release as draft, until master is somewhat settled, I haven't updated those in a while
<r​brunner7> It seems Wallet API will need a couple of new methods to support Polyseed ...
<sneedlewoods> +1
<j​berman> Also merged some PR's from a new contributor JeetRex 🎉 https://github.com/seraphis-migration/monero/issues?q=is%3Apr%20state%3Aclosed%20author%3Ajeetrex17
<sneedlewoods> +1
<redsh4de> +1
<jpk68> +1
<iamnew117> +1
<kowalabearhugs> +1
<r​brunner7> Oh, nice
<i​amnew117> Thank s
<i​amnew117> A little intro about myself
<i​amnew117> I am an 3rd year college student studying mathematics and computation from india
<r​brunner7> Careful, contributing to Monero can become a veritable addiction :)
<j​berman> Welcome! :)
<iamnew117> +1
<i​amnew117> Very true
<i​amnew117> There is soo much to learn
<s​yntheticbird> Welcome, hope you'll continue to enjoy
<iamnew117> +1
<r​edsh4de> can confirm
<r​brunner7> Alright, if we are through with the reports, I have a question for the room - not terribly important, but I am curious what other people think:
<r​brunner7> I wonder how "aggressive" the Polyseed capable CLI wallet app should promote that when creating a new wallet
<j​effro256> Howdy sorry I'm late
<r​brunner7> Basically, I see 3 possibilities:
<r​brunner7> 1) Ask interactively when creating the wallet whether you want Polyseed instead of "classic" seed
<r​brunner7> 2) Silently default to Polyseed, unless a startup command line parameter lie `--polyseed` is given
<r​brunner7> Oh, no, that would be of course `--classic seed` for 2
<r​brunner7> 3) Silently default to "classic seed", like now, unless `--polyseed` is given
<s​yntheticbird> 1. and you say that Polyseed is *Recommended*
<s​needlewoods> gut feeling says nr 2
<k​oe000> What would be the reason to use the classic seed?
<k​oe000> Why would someone use it instead *
<j​berman> Silently defaulting to polyseed I think is reasonable. Including the birthday height in the seed as default is a major +1 for noobs
<r​brunner7> Principle of "least surprise", for people who already use the CLI wallet for a long time maybe?
<r​brunner7> I wonder how many "noobs" use the CLI wallet app
<s​needlewoods> I do
<j​berman> "new users" probably a better term here
<j​pk68> I feel like defaulting to Polyseed could ostensibly cause some confusion when trying to restore
<r​brunner7> Yeah, you are the role model of a noob, right :)
<s​yntheticbird> i'm sorry to inform you that you aren't a noob SNeedlewoods
<j​effro256> I vote for 2 since it can prevent situations like this: https://gist.github.com/jeffro256/4155401274699e0437ba5b79b93c647f. Future key material may need to depend on being hidden from QAs. I don't see any compelling reason to make classic the default. Maybe some paranoid people want the full 256 bits of entropy, but it probably won't make any difference for the average user
<j​effro256> How so?
<i​amnew117> I vote for 2 has well
<s​needlewoods> was half joking
<syntheticbird> +1
<j​effro256> We already support multiple seed types with automatic detection
<r​brunner7> Yes, right now I don't see any problem with restoring.
<j​pk68> Oh yeah, forgot about the automatic thing
<s​yntheticbird> 2. then
<j​pk68> The intersection of people who use the CLI, yet don't know the difference between seed types is also probably quite limited anyways
<r​brunner7> Internally, I just throw the seed at the Polyseed code. If it says "ok", all is well, and it's of course a Polyseed
<r​brunner7> This approach should even guard against future Polyseed iterations, e.g. with more words for more entropy. Don't have to hard-code 16 for 16 words that way
<r​brunner7> Ok, looks like we have "loose consensus" for 2. That's good, one more question for restoring isn't really good UX anyway, no?
<r​brunner7> Er, no, for creating of course.
<r​brunner7> As I said restoring is ok
<k​oe000> Can label the seed type to reduce confusion
<r​brunner7> Yes, the wallet will clearly show you the type with the `seed` command, and maybe also with `wallet_info`
<sneedlewoods> +1
<r​brunner7> It's understood, you really want anything going wrong with seeds.
<r​brunner7> Especially if you are nervous already anyway, having to restore, and not yet knowing whether you will ever see your beautiful XMR again :)
<r​brunner7> jeffro256: Anything interesting to report from your side?
<r​brunner7> Maybe already back to coding, the good man
<j​effro256> There's some vulnerability work I can't reveal rn
<r​brunner7> Ok, understood.
<r​brunner7> Do we have to discuss something else today?
<j​effro256> Also working on setting up a framework for testing Ledger firmware for the FCMP++ migration
<jpk68> +1
<s​needlewoods> there is [this](https://github.com/monero-project/monero/pull/9464/changes/30d5a24ecb4bc25d33b246b0ce896da6610144ec#diff-21f483ea6b07b32bd1a19340344df0c12077b7a32a1c2ecd60e6ddfc801aa2dfR543-R550) method, which I added to the Wallet API, that returns a `void*` to get access to `tools::wallet2::tx_construction_data`. I assume that has to change, because `void*` are too low level and shouldn't be part of the API, but I also don't like the alternative to add a getter for each member of construction data that we need just for `on_describe_transfer`
<j​effro256> Also just doing review / prep for Beta stressnet
<r​brunner7> Maybe stupid question, but why not a small struct, or class, to give back that data? I think it's done that way with a number of similar things already there
<r​brunner7> Is that data too complex for that?
<s​needlewoods> that's probably the way to go
<r​brunner7> Is that needed somewhere? Which type of client would work with that data?
<j​effro256> You can do what the FCMP++ integration does with FCMP++ proofs: just pass around a variable length byte buffer
<s​needlewoods> it is just very rarely used (0 times in simplewallet, 1 time in wallet-rpc)
<s​needlewoods> https://github.com/monero-project/monero/blob/230de379498039b5ca229ab80d4dd04812bb33cd/src/wallet/wallet_rpc_server.cpp#L1474
<j​effro256> Opaque to the caller, so only implementor decodes it in practice
<s​needlewoods> will look into that, thanks
<j​effro256> `tools::wallet2::tx_construction_data` already has serialization code, so you can reuse that
<r​brunner7> Yeah, that RPC server method linked does exactly that: Looking at many info in there, to "describe" the transfer.
<r​brunner7> Looks like a tough nut to crack
<r​brunner7> Will try to have a closer look in the coming days
<s​needlewoods> I'm also getting the "Error loading page" now, which I think koe reported the other day
<r​brunner7> Tying to load what?
<r​brunner7> *Trying
<s​needlewoods> src folder in here https://github.com/seraphis-migration/monero
<r​brunner7> so GitHub not working reliably there? Strange.
<s​needlewoods> reload works, but need to reload every time you change the page ... whatever, I have nothing else to discuss for this meeting
<j​berman> I get that error sporadically as well now
<r​brunner7> That cries out for some nice conspiracy theory :)
<r​brunner7> Alright, I think we can close for today. Thanks everybody for attending, read you again in 1 week!
<s​needlewoods> thanks everyone, see you
<s​yntheticbird> thanks
<j​pk68> Thanks
````


# Action History
- Created by: rbrunner7 | 2026-04-17T06:14:18+00:00
- Closed at: 2026-04-20T18:51:47+00:00
