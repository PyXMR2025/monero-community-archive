---
title: 'Monero Tech Meeting #124 - Monday, 2025-06-09, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1218
author: rbrunner7
assignees: []
labels: []
created_at: '2025-06-06T12:24:16+00:00'
updated_at: '2025-06-09T18:37:32+00:00'
type: issue
status: closed
closed_at: '2025-06-09T18:37:31+00:00'
---

# Original Description
Location is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting [here](https://github.com/monero-project/meta/issues/1214).


# Discussion History
## rbrunner7 | 2025-06-09T18:37:31+00:00
````
<r​brunner7> Meeting in a bit more than 1 hour
<j​berman> In case I can't make today's meeting (looking unlikely), my update in advance: all expected tests now pass in fcmp++-stage (we have green CI), shared a TODO list for launch issue tracker (https://github.com/seraphis-migration/monero/issues/53), made serious headway on destroying FFI types correctly thanks to @jeffro256 (https://github.com/seraphis-migration/monero/pull/39).
<j​berman> Working on finishing that last task, and allowing txs with >8 inputs next
<sneedlewoods> +1
<r​brunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/1218
<s​needlewoods> hey
<r​brunner7> Probably no wave today from jberman , he left his report already about an hour ago
<r​brunner7> His TODO list for launch looks interesting: https://github.com/seraphis-migration/monero/issues/53
<r​brunner7> Do you have something to report?
<s​needlewoods> I think I have found an overlap from that TODO list with my work on wallet-cli, there are two settings `default-ring-size` and `print-ring-members` that I would not add to the Wallet API
<s​yntheticbird> hi
<s​needlewoods> unfortunately GUI and CLI settings differ, CLI settings are stored in the wallet file handled by wallet2 so I think they have to be part of the Wallet API
<r​brunner7> The GUI differs? You mean it offers a different set of settings, or stores them in a different way? The latter would be surprising
<r​brunner7> Maybe it does not offer all of them
<r​brunner7> `default-ring-size` is of course obsolete already for a long time and probably only presereved to avoid all risk something goes astray if a wallet has that set
<s​needlewoods> sorry not well prepared, here is the set of settings for GUI https://github.com/monero-project/monero-gui/blob/4e9b0ae000b702a7fbdc4770869a48480aee2cc3/main.qml#L1378-L1480
<r​brunner7> *preserved
<r​brunner7> I think what you see there is a mix of GUI specific settings, app global i.e. not per wallet, and wallet specific settings that go into the wallet file like they do if you use the CLI wallet
<s​needlewoods> but for example `allow_background_mining` or `restore_height` are also CLI settings
<s​needlewoods> though IIRC that `restore_height` in GUI is only used for restore, else it relies on the `m_restore_height` or however it's called in wallet2
<s​needlewoods> it's a bit tricky, but I think I'm on the right track
<r​brunner7> Anyway, I think both the CLI and the GUI code should be quite simple. It's also quite easy to see in the `wallet2` code itself what settings exactly are stored in the wallet files themselves. Will just take work and patience :)
<r​brunner7> That code is anyway the "ultimate source of truth" for per-wallet options
<r​brunner7> I have added an option or two myself there, in the good old times
<r​brunner7> Looks like the FCMP++ coding competition's end as set so far is less than 1 month away: https://github.com/j-berman/fcmp-plus-plus-optimization-competition
<r​brunner7> I wonder whether somebody got confirmation already that at least *somebody* is working on something
<r​brunner7> jberman or jeffro256 , if you know something, please drop it later, just for curiosity's sake
<s​yntheticbird> sagewilder are you still participating to the tournament ?
<r​brunner7> Alright, anything else for today? With things running so smoothly at the moment, meetings are a piece of cake :)
<r​ucknium> Did you see selsta say next release will be tagged in two weeks? I wonder if subnet deduplication might be reviewed and approved before then.
<r​brunner7> Everything ready to merge to release branch in a mere two weeks looks unlikely IMHO
<s​needlewoods> nothing from me
<s​needlewoods> just thanks to jeffro and jberman for their hard work, got a ton of mails from the seraphis-migration repo recently lol
<r​brunner7> Right, the amount of PRs they do at the moment is amazing
<r​brunner7> It's a bit of a pity that it might miss the next release
<r​brunner7> Critical things often get some time of running them on master, just to be sure. And peer selection better works, right
<rucknium> +1
<s​needlewoods> I don't feel qualified for a review for the subnet PR
<r​brunner7> Yeah, it's a different corner of the codebase than on what you worked so far
<r​brunner7> Ok, I think we can close for today. Thanks everbody for attending, read you again next week, the week just before - hurray! - MoneroKon
<s​needlewoods> thanks and cu
````


# Action History
- Created by: rbrunner7 | 2025-06-06T12:24:16+00:00
- Closed at: 2025-06-09T18:37:31+00:00
