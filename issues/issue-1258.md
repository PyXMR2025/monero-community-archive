---
title: 'Monero Tech Meeting #134 - Monday, 2025-08-25, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1258
author: rbrunner7
assignees: []
labels: []
created_at: '2025-08-22T15:49:29+00:00'
updated_at: '2025-08-25T18:33:24+00:00'
type: issue
status: closed
closed_at: '2025-08-25T18:33:23+00:00'
---

# Original Description
Location is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting [here](https://github.com/monero-project/meta/issues/1255).


# Discussion History
## rbrunner7 | 2025-08-25T18:33:23+00:00
````
<r​brunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/1258
<s​needlewoods> hello
<j​effro256> howdy
<s​yntheticbird> hi
<j​berman> *waves*
<r​brunner7> Alright, onwards to the reports from last week
<s​needlewoods> made great improvements on the Wallet APIs `wallet_keys_unlocker` thanks to jeffro
<s​needlewoods> also finally fixed the bug that made `verifyPassword()` fail after make_multisig
<r​brunner7> So the hunt for the last remaining pieces of direct wallet2 use in the CLI wallet can continue :)
<s​needlewoods> yay, way more fun than starring at the debugger :D
<r​brunner7> If the bug is interesting ...
<j​berman> me: fixed a couple bugs testing forking from current testnet (in the migration and in scanning) in prep for alpha stressnet, cleaned up the FFI (removed unwraps/asserts, used int error returns to gracefully handle errors, de-duplicated some code with macros, clippy+fmt), implemented consolidated paths in the RPC for getting paths in the tree by global output id, started on a better organizational structure for curve trees logic in the db code, tested kayaba's latest prove/verify optimizations (good results!!)
<j​berman> Planning to complete organizational structure in the next day, then moving to documentation/Carrot review, in prep for opening PR's to the main Monero repo
<j​berman> Good news: kayabanerve  implemented linear prove() times, dropping 128-input tx construction down from 5m30s to ~1m!! Huge
<jeffro256> +1
<rbrunner7> +1
<rucknium> +1
<sneedlewoods> +1
<j​effro256> me: initiated communication about Carrot follow-up review by Cypherstack, updated FCMP++ benchmark tool for all the latest FCMP++ changes (github.com/jeffro256/clsag_vs_fcmppp_bench/), working on supporting high input counts in benchmark tool, working on patches in Monero core repo, re-reviewing the de-dup PR by rbrunner7, reviewed several PRs in seraphis-migration, did a write-up for an upcoming vuln disclosure, helped prepare v0.18.4.2 release
<sneedlewoods> +1
<r​brunner7> Rucknium answered jeffro256 's questions that came up during his review, and I made the requested (smaller) changes. I think it's ready now for a second review, that certainly seems a good idea because of the importance of the code: https://github.com/monero-project/monero/pull/9939
<r​brunner7> "an upcoming vuln disclosure". Oh, always interesting. Did the fuzzing already turn up something auctionable?
<k​ayabanerve> *waves*
<k​ayabanerve> I deduplicated 25k lines of code and optimized FCMP++ prove. Apologies for being a few minutes late to the meeting.
<r​brunner7> That's the 5 times speedup that jberman mentioned?
<j​effro256> Yes, but this specific one isn't related to the fuzzing group. The report will go up as soon as v0.18.4.2 binaries are out, not sooner so users don't get confused.
<k​ayabanerve> I also raised the topic of migrating the hash to point algorithm with FCMP++s after finally successfully identifying the present algorithm.
<k​ayabanerve> Largely rbrunner7
<j​effro256> But if you're self-compiling for your own wallet, just make sure to be on the latest release-v0.18 or master branch.
<r​brunner7> Just curious, what is there to win if we migrate to another "hash to point" algorithm? A bit faster?
<r​brunner7> jeffro256: Thanks for the hint
<k​ayabanerve> Bits of security currently being lost.
<plowsof> jeffro256 would this be on -site as a blog post also - pushed at the same time binaries are?
<k​ayabanerve> We currently use keccak256. Would you be happy if I set the first byte to 0 after every usage?
<k​ayabanerve> We currently use a hash to point which has an explicit bit of bias and probably has further bias after.
<r​brunner7> Is this a trick question :)
<k​ayabanerve> a new hash to point just tightens everything back up
<k​ayabanerve> It's also only ~10 lines of cryptography. It just invokes the existing hash to curve twice. It isn't a major change re: cryptography
<r​brunner7> And no hairy compatibility issues if we switch that algorithm? Or will it be done in standard version based way?
<r​brunner7> Before like so, afterwards differently
<j​effro256> plowsof: yes that could be done
<k​ayabanerve> New outputs are added to the tree with a key image generator sampled using the new hash to point
<k​ayabanerve> Old outputs are added to the tree with their key image generators sampled using the existing hash to point
<k​ayabanerve> The world keeps spinning
<r​brunner7> Alright :)
<j​effro256> It's a type of vuln that doesn't really benefit much from being hidden from attackers since it's a data leak, it mainly just hurts users the longer they don't update. If it makes sense, perhaps a report PR can be made to the monero-site, but I just don't want it to spread on social media sites before the release binaries are posted, and cause confusion
<j​effro256> @selsta
<j​berman> plowsof: bumping this PR too not sure who else to bump to: https://github.com/monero-project/monero-site/pull/2510
<r​brunner7> Ok. Anything else to discuss today beyond these reports?
<r​brunner7> Doesn't look like it. I think we can close. Thanks everybody for attending, read you again next week!
<selsta> fuzzing found issues but so far none have been exploitable
<s​needlewoods> thanks everyone
<r​brunner7> Good to hear, selsta.
<r​brunner7> By the way, SNeedlewoods , it looks as if eigenwallet really went the API way instead of using wallet2 directly, which is nice: https://libera.monerologs.net/monero/20250712#c540320
<jeffro256> +1
<j​effro256> Yes, sorry, I should have been more clear about the changes made due to the fuzzing group: actionable, but not exploitable.
<j​effro256> Thanks everybody
<r​brunner7> (There must be some more recent statement, but can't find right now)
<s​needlewoods> had a chat with the devs a while ago and gave them a link to the branch I'm currently working on, so they can track the most recent changes to the API
<j​effro256> rbrunner7: about the changes?
<j​effro256> for fuzzing?
<r​brunner7> Er, no, about eigenwallet using the API
<j​effro256> Oh okay nvm
````


# Action History
- Created by: rbrunner7 | 2025-08-22T15:49:29+00:00
- Closed at: 2025-08-25T18:33:23+00:00
