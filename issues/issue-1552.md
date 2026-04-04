---
title: Updating remaining block count during wallet sync isn't continuous
source_url: https://github.com/monero-project/monero-gui/issues/1552
author: akuukka
assignees: []
labels:
- resolved
created_at: '2018-09-02T07:34:49+00:00'
updated_at: '2019-07-15T14:45:50+00:00'
type: issue
status: closed
closed_at: '2019-07-15T14:45:50+00:00'
---

# Original Description
Not sure if daemon sync has the same problem (I always run the daemon), but when I open the GUI and it has to sync my wallet, the remaining block count behaves strangely.

It quickly goes down by several thousand block, then stops completely for a long time. Then again it updates itself later and goes down by several thousands. Rinse and repeat.

It's really frustrating. Isn't it possible to update the remaining block count more "continuously"?

I'm running Monero on external HDD (yeah, initial sync was really painful but I can now easily keep up with the chain) so the wallet sync is quite slow for me. It would be super cool and user friendly to know the progress better.

# Discussion History
## sanderfoobar | 2018-09-02T10:27:03+00:00
GUI version, OS?

## akuukka | 2018-09-02T10:28:57+00:00
0.12.3.0 OS X

Reproducing might require an external HDD and wallet which is behind at least 10000 blocks.

## sanderfoobar | 2018-09-03T16:23:44+00:00
This external HDD is hooked up via USB (2.0?)

## akuukka | 2018-09-03T16:28:54+00:00
USB-C on a brand new MacBook Pro

## sanderfoobar | 2018-09-03T17:50:03+00:00
How long does the total wallet refresh take, do you reckon?

For clarification:
- Blockchain sync
- Wallet refresh <== what we're talking about now

## sanderfoobar | 2018-09-03T18:02:38+00:00
I'm going to assume `monerod` is busy syncing the blockchain whilst the GUI is trying to refresh the wallet.

Try the following:

1. Open GUI->Settings
2. Press 'Stop Local Node' (if it is started)
3. Navigate to 'Blockchain location' -> Show advanced
4. Set input value to `--max-concurrency 2`
5. Press 'Start Local Node'

If you start `monerod` independently, append `--max-concurrency 2` to startup arguments.

Your local node (`monerod`) should now take up less resources (I/O, CPU) and I suspect this would make your wallet refresh faster.

If not, inspect a resource manager like `htop` or `top`.

## akuukka | 2018-09-03T18:11:57+00:00
Yes, we are talking about wallet sync now. My blockhain is always synced because I run monerod 24/7.

But if I haven't opened the wallet GUI in about a week, it takes about 1-2 minutes to sync the wallet and as I mentioned, the progress indicator tends to stop at times.

I don't think this is about concurrency, because my older dual core MacBook Pro behaves almost exactly the same as my newer quad core MacBook Pro. It's clear that the disk I/O is the bottleneck because the newer computer is only slightly faster.

## lacksfish | 2018-11-09T14:07:23+00:00
I see the same UI/UX issue. Unlocked balance doesn't update while syncing a few thousand blocks. This is on 0.13.0.4

Unlocked balance should jump back to full balance after only syncing the next 10 blocks after spending.

## dEBRUYNE-1 | 2019-07-03T17:39:18+00:00
Can you check whether this is still an issue with GUI v0.14.1.0?



## lacksfish | 2019-07-03T18:15:02+00:00
Will do

## dEBRUYNE-1 | 2019-07-03T21:00:51+00:00
Thanks. 

## dEBRUYNE-1 | 2019-07-12T16:07:26+00:00
@lacksfish - ping. 

## lacksfish | 2019-07-12T16:26:26+00:00
Sorry sorry, will get to it.

## dEBRUYNE-1 | 2019-07-13T06:24:56+00:00
Thanks!

## lacksfish | 2019-07-15T11:40:54+00:00
Giving it a spin now.

## lacksfish | 2019-07-15T12:08:26+00:00
Syncing, got my eyes on it

## lacksfish | 2019-07-15T13:35:19+00:00
Regarding balance during sync:

So it seems to refresh while syncing, but I have a bunch of tx's where I churned back into the same wallet, and the sync seems to always *add* the amount I churned, but is not subtracting the amount sent out correctly? Otherwise, I can not explain it, but the balance during sync is too high.

Block count is moving along just fine, no big random jumps, very consistent.

## dEBRUYNE-1 | 2019-07-15T14:42:35+00:00
It shows the balance at that time, which was probably higher than now. 

>Block count is moving along just fine, no big random jumps, very consistent.

All right. Then I will mark this as resolved. 

## dEBRUYNE-1 | 2019-07-15T14:42:39+00:00
+resolved

# Action History
- Created by: akuukka | 2018-09-02T07:34:49+00:00
- Closed at: 2019-07-15T14:45:50+00:00
