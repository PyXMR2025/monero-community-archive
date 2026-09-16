---
title: 'Monero Tech Meeting #185 - Monday, 2026-09-14, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1456
author: rbrunner7
assignees: []
labels: []
created_at: '2026-09-13T17:33:26+00:00'
updated_at: '2026-09-14T18:45:00+00:00'
type: issue
status: closed
closed_at: '2026-09-14T18:45:00+00:00'
---

# Original Description
Location is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting [here](https://github.com/monero-project/meta/issues/1452).


# Discussion History
## rbrunner7 | 2026-09-14T18:45:00+00:00
````
<rbrunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/1456
<jeffro256> Howdy
<sneedlewoods> Hey
<jpk68> Hello
<selsta> hi
<jberman> waves
<vtnerd> Hi
<rbrunner7> Summer lull seems to be over, many people here :)
<rbrunner7> Alright, what are your reports from last week?
<sneedlewoods> rebased, fixed conflicts and updated #9464 (https://github.com/monero-project/monero/pull/9464), #10232 (https://github.com/monero-project/monero/pull/10232), #10233 (https://github.com/monero-project/monero/pull/10233), #10819 (https://github.com/monero-project/monero/pull/10819) with latest round of LLM review comments
<rbrunner7> Me: Polyseed PR merge ready, or at least almost so
<sneedlewoods> +1
<rbrunner7> @sneedlewoods: Those LLM reviews, were they solid? Any comments?
<jpk68> Me: worked on some patches for the core repo and GUI, more AI 'audits' for I2P SAM, reviewed quite a few PRs
<selsta> Mostly worked on Hackerone reports and tried to make progress on the release. AI makes it so easy to low severity find edge cases that it's kinda becoming unsustainable with our existing bug bounty.
<rbrunner7> You mean, we may start to classify submissions?
<jberman> hot-cold PR review and release PR's
<rbrunner7> To HackerOne
<sneedlewoods> @rbrunner7: Most of the comments I received were valid, some were very helpful
<selsta> I don't know what the solution is. Maybe increase the minimum amount of severity to be eligible for a bounty.
<jberman> bumping minimum severity makes sense imo
<rbrunner7> Yes, that's what I meant with classifying.
<jeffro256> me: working on a version compatibility testing framework. It's something that I've been wanting for months now, but I'm getting around to it now. You will able to put in a list of "control commits" and a "target commit". Then the framework will compile all those commits then run a suite of C++/Python functional tests against (control_commit, target_commit) for each control_commit. Will be useful for checking cross-version serialization compatibility, or compatibility for tx relay v2, etc
<sneedlewoods> +1
<rbrunner7> Although that may lead to conflicts with submitters ...
<jeffro256> First public commit will be in the next couple of days 
<rbrunner7> Sounds interesting, if a bit on the complex side
<selsta> jeffro256: Is this something we can run on CI our better for specific changes manually?
<rbrunner7> Maybe interesting for Cuprate as well, at least the general approach?
<jeffro256> Yeah I don't see why not. It'll be pretty heavy due to all the compiling involved, but I'm making it configurable, so you can filter out only the needed test suites and needed control commits 
<jpk68> What's it written in?
<jeffro256> Python/C++/C
<jpk68> +1
<rbrunner7> Will be interesting to see what you needed C for in there :)
<jeffro256> just for FFI basically
<jpk68> With Python? Boost.Python can always work ;)
<rbrunner7> So this "hold/cold" PR and its review makes steady progress, and we are nearing its merge, right? And then on to a new version of stressnet!
<jeffro256> True, but Boost.Python is probably a bit overkill for what I need
<jpk68> +1
<rbrunner7> Will koe's multisig PR become easily testable only after that merge?
<rbrunner7> And probably on the new stressnet as well
<jeffro256> If koe wants to maintain backwards compatibility for multisig code until the fork, then I imagine that my framework would be very useful 
<jpk68> Speaking of multisig, just throwing this out there: I was wondering about the possibility of using monero-oxide's FROSTLASS scheme over FFI. It's already been audited, and provides better security assumptions than the current scheme.
<jpk68> IIUC, it would not require any new dependencies
<jpk68> It would require more work, of course, hence why I'm just surfacing it for no particular reason
<rbrunner7> That would also start a pretty fundamental discussion whether we want multisig in the core repo at all, or if a separate one is a better place. Not an easy decision at all, if you ask me.
<jpk68> Right, but I meant as more of a drop-in replacement, which happens to use the Rust code, since that's what's being used for FCMP++ anyways
<rbrunner7> And you could even start to dream about a mid-to-far future where we can leave the C++ code itself behind and do pure Rust, of course with that multisig
<rbrunner7> Well, something that would make all existing Monero multisig wallets inoperable could not be a "drop-in replacement", seems to me
<rbrunner7> With "wallets", I mean wallet files
<jpk68> True. This does provide a very good opportunity, IMO, where it could be moved out of 'experimental', due to already having proofs/audits for both the math and implementation code
<jpk68> The fact that multisig in the main codebase is marked as 'experimental' makes for less of a compulsion, if you will, to maintain strict backwards compatibility
<rbrunner7> Oh, personally I don't think that this "exerimental" disclaimer really hinders actual use ...
<rbrunner7> Haveno is running fine
<rbrunner7> Well, it had bumps in the road, but as far as I know more on the protocol side, not with multisig itself
<jeffro256> +1
<jpk68> @rbrunner7: That it's 'experimental' is the reason it can't be in the GUI, or suggested to anyone, or be suggested to anyone without lots of disclaimers
<jpk68> FROSTLASS doesn't have the scaling problems, and provides a two-round DKG independent of the number of signers, IIRC
<rbrunner7> In the meantime you can also claim that if the AIs don't find anything, that is on the reassuring side :)
<jpk68> Reassuring enough to convince people here to remove the 'experimental' label?
<rbrunner7> No, that's asking too much.
<jpk68> +1
<jpk68> The UX improvements provided by FROST cannot be understated
<rbrunner7> Don't know. You just have to wait a bit longer in that standalone multisig GUI - how is it called again? - because more rounds take place. UI impact: Almost zero
<rbrunner7> Something where you have to cut and past your messages manually, even with FROST, is not ready for mass use anyway, IMHO
<jpk68> @rbrunner7: Not really. Large signer thresholds in the current scheme are pretty much infeasible. FROST scales logarithmically
<jpk68> It always has two DKG rounds as well
<rbrunner7> I can also repeat here that this standalone GUI is almost ignored to death. Why? Because multisig itself seems to be such an edge use case right now, if you ask me.
<jpk68> It's also natively designed for signer-subset flexibility, and forgery-attack mitigation is proven to be secure in FROST due to it having blinding factors
<rbrunner7> Certainly not because of "UI problems"
<jpk68> I think it's something many people would find very useful, if it weren't for the prohibitive usability cost of having to find some niche third-party software to use it (which is barely maintained), and first-party support for it is actively discouraged
<jpk68> This also ties into adoption. Some organizations require multisig, and simply cannot use Monero if it's not easy
<rbrunner7> We could probably continue to chat about this for much longer, but anyway, let's go back to this meeting. Is there any other subject somebody would like to bring up for today?
<rbrunner7> Maybe we also lost some members, scared them away with multisig lol
<jpk68> +1
<rbrunner7> Thus I say let's call it a meeting for now. Thanks everybody for attending, read you again next week!
<jpk68> +1
<sneedlewoods> thanks everyone, ciao
````


# Action History
- Created by: rbrunner7 | 2026-09-13T17:33:26+00:00
- Closed at: 2026-09-14T18:45:00+00:00
