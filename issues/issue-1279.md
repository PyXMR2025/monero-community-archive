---
title: 'Monero Tech Meeting #141 - Monday, 2025-10-13, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1279
author: rbrunner7
assignees: []
labels: []
created_at: '2025-10-10T05:16:17+00:00'
updated_at: '2025-10-13T18:38:29+00:00'
type: issue
status: closed
closed_at: '2025-10-13T18:38:29+00:00'
---

# Original Description
Location is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting [here](https://github.com/monero-project/meta/issues/1277).


# Discussion History
## rbrunner7 | 2025-10-13T18:38:29+00:00
````
<r​brunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/1279
<j​berman> *waves*
<s​needlewoods> Hey
<j​effro256> Howdy
<v​tnerd> hi
<r​brunner7> Alright, I think we can already start with the reports from last week
<r​brunner7> I can soon make a film out of the FCMP++ GitHub repo mails that I receive, starting with 24 pieces per second :)
<s​needlewoods> made a [PR](https://github.com/monero-project/monero/pull/10165) for the issue where estimated block height is above actual block height
<s​needlewoods> also made a little progress on the CLI, `sweep_single` should be done, `m_wallet` count is down to 15
<s​needlewoods> ~30 TODO comments left, an incomplete list of some of the things:
<s​needlewoods> - `cold_sign_tx()`
<s​needlewoods> - `--restore-multisig-wallet`, `--generate-from-json`
<s​needlewoods> - handling of some exceptions and error messages (e.g. [handle_transfer_exception](https://github.com/monero-project/monero/blob/8d4c625713e3419573dfcc7119c8848f47cabbaa/src/simplewallet/simplewallet.cpp#L617))
<jberman> +1
<s​needlewoods> And I want to mention that I received an offer from binarybaron to spend some hours reviewing their wallet code. That could be a good incentive to learn rust. Of course my CCS would have priority, I'd aim to spend 20h/week (12h/week were advertised and the total is already exceeded, though I really want to finish it) on that and only work on eigenwallet if I have time beyond that, but I think I'm relatively close to getting into review phase for the CLI (hopefully not more than a month until a PR is made) and if I don't have enough CCS work by then, I'd spend more time on the eigenwallet review.
<s​needlewoods> Any thoughts/opinions?
<v​tnerd> I got carrot subaddresses working lws, but I had to modify make_carrot_subaddress_v1 (used in unit test), and tweak the relevant carrot spec. Eagerly waiting to get feedback on whether my tweak was valid
<j​berman> me: almost exclusively worked on stressnet issues, made a number of PR's fixing some connectivity issues and wallet slowness, continuing investigating different issues
<s​needlewoods> btw it was jbermans suggestion to use recent hard fork height from `hardforks.cpp`, which I think was a great idea
<j​effro256> Where is the tweak at?
<v​tnerd> I just PR’ed something to your carrot repo
<v​tnerd> ~15 mins ago
<v​tnerd> it was pretty minor as all of the unit tests still pass, but it affected the make_carrot_subaddress_v1 function which I was using in a lws unit test
<j​effro256> Okay responding to that now
<r​brunner7> SNeedlewoods: IMHO such a course of action regarding your work hours, as you described it here, would be ok. How do other people here see this?
<r​brunner7> I think there were times also where jberman distributed time to his Monero CCS and some Rust / Serai work. As long as it's done in good faith, and in the open, I don't see a problem.
<j​berman> IIUC, binarybaron is offering to pay you separately from your CCS to review their wallet code?
<jeffro256> +1
<s​needlewoods> yes
<j​effro256> me: reworked large portions of the Carrot Rust library and opened a PR to hopefully speed input verification in many large-load cases: https://github.com/monero-project/monero/pull/10157
<j​berman> no issue at all with that! pretty cool of binarybaron
<sneedlewoods> +1
<j​effro256> vtnerd: https://github.com/jeffro256/carrot/pull/5#issuecomment-3398566553
<s​needlewoods> thanks for the feedback, appreciate it :)
<j​berman> 1 other related task that I think would be very nice re: that wallet restore stuff SNeedlewoods is finding a way for wallets with an expected daemon connection to set the restore height using the daemon's reported height, rather than the offline estimate
<r​brunner7> jeffro256: Just curious, was that Carrot Rust library rework a result of insights and experience gained in the meantime, since writing the original library version?
<j​berman> offline estimate is a welcome improvement for sure tho
<j​berman> we discussed that connection stuff a bit last week, those logs may be helpful
<j​effro256> kayabanerve: gave a lot of good feedback on how to make it Rustier
<r​brunner7> Rustier, lol
<j​berman> (and this PR sort of mentions it: https://github.com/seraphis-migration/monero/pull/162 , we probably shouldn't need to override the restore height in that step 2, it's only there because the wallet's initial creation isn't using a functional daemon connection)
<s​needlewoods> isn't that already happening here https://github.com/monero-project/monero/blob/d32b5bfe18e2f5b979fa8dc3a8966c76159ca722/src/wallet/wallet2.cpp#L5703-L5729
<s​needlewoods> or am I misunderstanding?
<j​berman> problem is when that's called with the GUI e.g., the wallet doesn't have the connection to the daemon established yet
<s​needlewoods> I also looked in the GUI side, but didn't have enough time to figure out how that works exactly, but it seems it uses `restore_height` from `persistentSettings`, and that is the restore height of the wallet that was opened before
<s​needlewoods> will try to figure that out this week
<j​berman> the context described in that linked PR description may help
<r​brunner7> Regarding that potential Carrot sub-address generation problem: One would really hope that if there was a problem in there, audit(s) should have unearthed it already?
<r​brunner7> A problem of that magnitude that gets through until implementation and only gets stopped by some unit tests failing would worry me ...
<r​brunner7> We will certainly soon see how this plays out :)
<r​brunner7> Alright, seems we are through with reports and coordination. Anything else to discuss today?
<j​effro256> It shouldn't be an issue AFAIK, it looks like a notation mixup
<j​berman> rbrunner7: you might be interested in this PR: https://github.com/seraphis-migration/monero/pull/162
<j​berman> it touches the incremental pool stuff
<j​berman> to make refresh/show_transfers fast on every call
<r​brunner7> ... that my old brain probably already forgot almost completely
<r​brunner7> No, seriously, will try to have a look
<jberman> +1
<s​needlewoods> I'm happy to test it when new release is out
<s​needlewoods> nothing else to discuss for me
<r​brunner7> So we won't prevent busy people working on stressnet any longer! Thanks for attending everybody, read you again next week
<s​needlewoods> thanks everyone
````


# Action History
- Created by: rbrunner7 | 2025-10-10T05:16:17+00:00
- Closed at: 2025-10-13T18:38:29+00:00
