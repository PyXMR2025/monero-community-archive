---
title: Testnet v8 sync from scratch got stuck
source_url: https://github.com/monero-project/monero/issues/3383
author: zhang111111111
assignees: []
labels: []
created_at: '2018-03-11T09:25:57+00:00'
updated_at: '2018-06-11T09:17:02+00:00'
type: issue
status: closed
closed_at: '2018-06-11T09:17:02+00:00'
---

# Original Description
Hello, I compiled the master branch last week and synced the testnet chain from scratch. Now it got stuck at block height 1070941/1070941.

Found the following error while examining bitmonero.log:
https://paste.fedoraproject.org/paste/ei5uecAybaBgjYtGBNXL4w/raw

After the error occurred it synced up to 1070941 where it is now.

The current behavior:
https://paste.fedoraproject.org/paste/PzK46DmY8ZWz~7NXv~Qqxw/raw



# Discussion History
## moneromooo-monero | 2018-03-11T10:08:10+00:00
The first error seems you found a peer on a different chain.

The second log looks like you might not have popped blocks till v6 (1057026) before syncing with the new code. You have to pop blocks with the original version.

## zhang111111111 | 2018-03-11T10:32:39+00:00
I synced the whole chain with the new code so what are you referring to with the original version?

## moneromooo-monero | 2018-03-11T12:59:47+00:00
Then my second comment does not apply. What commit hash are you running ?

## zhang111111111 | 2018-03-11T15:10:09+00:00
c7ace5fa

Looks like it synced the wrong chain at some point, right?

## moneromooo-monero | 2018-03-11T17:19:22+00:00
You're missing the PoW and min mixin changes.
Might or might not be the problem, but try current master first, whuch has those.

## zhang111111111 | 2018-03-11T22:11:36+00:00
It's still the same with e9f41e4
Is there anything else that I can try to fix the issue?

## moneromooo-monero | 2018-03-11T22:20:17+00:00
If you've synced past 1057026, then you need to pop blocks back to that height with the *previous* version of monero (monero-blockchain-import --pop-blocks N), then start syncing again with the current version of monero.
If your chain is below 1057026, then it's something else.

## zhang111111111 | 2018-03-11T22:25:24+00:00
Just to be sure, I have to use c7ace5f to pop the blocks and e9f41e4 to resync?

## moneromooo-monero | 2018-03-11T22:33:49+00:00
That is correct.

## zhang111111111 | 2018-03-11T22:54:15+00:00
monero-blockchain-import --testnet --pop-blocks 13915
height: 1057026

Still the same behavior:
https://paste.fedoraproject.org/paste/AG35wM67FxhNCQpQ3vFs0w/raw

## zhang111111111 | 2018-03-12T15:06:26+00:00
Some further experiments and observations:

Popped back to height 1000000, synced and it got stuck somewhere
Popped back to height 1057000 and synced with --block-sync-size 1 and it got stuck at 1057027/1111971.
Restarted monerod and it synced past 1057027.

Popped back to 1057000 multiple times and these are the outcomes:
Sometimes it got stuck at 1057027 without recovery. (a deleted p2pstate.bin makes it worse)
Sometimes it got stuck at 1057027 but recovered after a few minutes.
Sometimes it synced straight past 1057027.

After that, I let it sync further. At the first time it got stuck at 1057365/1101553
Popped back to 1057000 and managed that it synced past 1057365.
Restarted monerod because I wanted to raise the --block-sync-size and it didn't sync anymore.
Popped back (multiple times until it synced past 1057027) and let it sync until 1058177/1058272, restarted monerod on purpose and it didn't sync anymore.

It seems like monerod isn't able to resume the synchronisation of v8 blocks after a disruption. (in my case most likely triggered by connection drops)
That it got stuck at 1057027 so many times might be related or a separate issue. 

## moneromooo-monero | 2018-03-12T15:12:16+00:00
I got a similar thing this morning, it looks like a bug in the sync code.

## moneromooo-monero | 2018-06-11T09:14:17+00:00
Sync bugs are now fixed.

+resolved

# Action History
- Created by: zhang111111111 | 2018-03-11T09:25:57+00:00
- Closed at: 2018-06-11T09:17:02+00:00
