---
title: transfers information disappeared from wallet
source_url: https://github.com/monero-project/monero/issues/2706
author: jonahar
assignees: []
labels: []
created_at: '2017-10-22T20:07:50+00:00'
updated_at: '2017-11-14T20:00:32+00:00'
type: issue
status: closed
closed_at: '2017-11-14T20:00:32+00:00'
---

# Original Description
I pulled and compiled after the subaddresses merge so I can try it. Since then I can't see anything when typing the command `show_transfers`.
Machine: Ubuntu 16.04, 64-bit

# Discussion History
## moneromooo-monero | 2017-10-22T21:42:15+00:00
If you've not exited yet, kill the wallet process so it doesn't save the cache over the old one.

## jonahar | 2017-10-23T04:57:43+00:00
Too late for that, I already closed the cli. Do you think there's anything else to do now?

## moneromooo-monero | 2017-10-23T09:01:22+00:00
No, if it's saved the cache, the info is most likely gone, unless this is a display bug only (unlikely).

## moneromooo-monero | 2017-10-23T10:56:43+00:00
It's not gone, but there is some corrupt info. I don't think it's recoverable cleanly, but should be recoverable in most cases.

https://github.com/monero-project/monero/pull/2715 fixes the bug, but does not fix a resaved cache. It should be possible to detect and fix the most egregious (ie, index > 250), but can't be sure if someone's used a lot of subadresses already.

## jonahar | 2017-10-23T13:57:42+00:00
I have the `.unportable` file. Can I use it to restore the information?

## moneromooo-monero | 2017-10-23T14:01:35+00:00
Did you ever receive something on a subaddress to this wallet ? If not, I can make some changes which will recover the info.

## jonahar | 2017-10-23T14:38:36+00:00
No, still haven't used a subaddress.

## moneromooo-monero | 2017-10-23T15:00:00+00:00
https://github.com/moneromooo-monero/bitmonero/tree/zerosub

NOTE: this destroys all subaddress information in historical records. So if a wallet has already used subaddresses, this will corrupt it. So only use once, to restore a wallet with corrupt info.

## jonahar | 2017-10-23T16:16:05+00:00
I was able to recover only part of the transactions - just the outgoings.

## moneromooo-monero | 2017-10-23T21:16:24+00:00
Try again with the new code, one of the fields was missing.

## jonahar | 2017-10-24T06:17:04+00:00
This fixed it!
Would you mind sharing your personal tip address :) ?

## moneromooo-monero | 2017-11-14T19:41:53+00:00
It's on moneroaddress.org, where you can optionally verify it with my GPG key :)

Fix merged.

+resolved


# Action History
- Created by: jonahar | 2017-10-22T20:07:50+00:00
- Closed at: 2017-11-14T20:00:32+00:00
