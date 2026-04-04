---
title: 'Feature request: converting view-wallet to full-wallet and vice versa'
source_url: https://github.com/monero-project/monero/issues/1381
author: JollyMort
assignees: []
labels: []
created_at: '2016-11-26T21:00:16+00:00'
updated_at: '2017-08-25T21:20:28+00:00'
type: issue
status: closed
closed_at: '2017-08-25T21:20:28+00:00'
---

# Original Description
Prompted by [this SE question](http://monero.stackexchange.com/questions/2711/can-i-retroactively-add-the-spendkey-to-a-watch-only-wallet), I'd like to propose this, as a convenience.

Idea would be to have 3 commands, working names: view-to-full, view-to-full-temp and full-to-view.

**view-to-full**
- prompt the user for seed or private key
- convert the wallet to full-wallet, update key images and save

**view-to-full-temp**
- same as above, but ...
- keep everything in memory and prevent saving the privkey data. The wallet would save generated key images only. I think this could facilitate easy cold-spending etc as you could move the file back and forth from hot PC to cold PC.

**full-to-view**
- wipe all the privkey data
- of course, keep the already generated key images

Any thoughts?

# Discussion History
## moneromooo-monero | 2016-11-26T21:06:28+00:00
The first one might be useful, though why not copy the full one if you have one.

The second is pointless. If you weren't concerned about being pwned, you would have your spend key in there in the first place.

The third one seems a bit useless There is a save_watch_only already, if you want to spawn a view wallet to copy elsewhere.

If you have arguments as to why the above is wrong, please make them, as there might be cases where they're useful where the above doesn't apply.

## JollyMort | 2016-11-26T22:52:36+00:00
You're right, I didn't think it through. Apart for the first one, which would avoid having to refresh from 0 when you want to permanently convert to a full-wallet, the rest would be duplicating the functionality already there when using the new import/export outputs command.

Idea was to make the process less clunky, but while chasing this thought I realize it woudln't be much of an improvement. So yeah, only the 1st one would be useful, other things could be achieved with existing commands.

Below is just for info on what I had in mind, but now I've realized it's practically the same as what we have [here](https://github.com/monero-project/monero/issues/1236#issuecomment-254751727).

Initial status: watch wallet fully synced.
1. **copy** the watch wallet to cold PC
2. enter seed
3. wallet does: generate key images and save inside itself, flag somehow they're to be checked vs blockchain list when refreshing next time.
4. purge private key
5. **copy** all to online PC, refresh, correct balance now displayed
--- cold spending ---
6. prepare unsigned txes
7.  **copy** wallet & txes to cold PC
8. enter seed
9. wallet signs txes
10. bonus question: could it immediately prepare a signed key image for the change output, to later show the correct balance without having to do 1-5 again?
11. **copy** all back to online PC, push the TX.
12. if 10 not possible, goto 1.

# Action History
- Created by: JollyMort | 2016-11-26T21:00:16+00:00
- Closed at: 2017-08-25T21:20:28+00:00
