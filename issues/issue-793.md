---
title: Wallet file inconsistencies
source_url: https://github.com/monero-project/monero/issues/793
author: arnuschky
assignees: []
labels: []
created_at: '2016-04-03T22:00:19+00:00'
updated_at: '2016-05-10T12:33:21+00:00'
type: issue
status: closed
closed_at: '2016-05-10T12:33:21+00:00'
---

# Original Description
I deleted my `walletname.bin` in order to rescan my wallet when upgrading to 0.9.2.
- After rescanning and terminating simplewallet, I noticed that the wallet wasn't saved. I had to manually enter `save` after rescanning in order to make the change permanent. Seems a bug to me.
- The new db file is called only `walletname` rather than `walletname.bin`. Is that intentional?
- The new file is world-readable. Urgh.


# Discussion History
## moneromooo-monero | 2016-04-04T16:26:30+00:00
Did you kill simplewallet, or exit it with exit ?

The wallet is called whatever you call it. If your keys file is named walletname.bin.keys, the cache should be walletname.bin. If your keys file is named walletname.keys, the cache should be walletname.


## arnuschky | 2016-04-04T16:28:55+00:00
Ok for the naming part then. Didn't understand your other comment. I tried both: `exit` and ctrl-c when running in RPC server mode.


## moneromooo-monero | 2016-04-06T19:02:44+00:00
https://github.com/monero-project/bitmonero/pull/801 fixes the permissions issue (except on windows, which is always the weird one, so will need someone with Windows to fill in the blanks).


## moneromooo-monero | 2016-04-10T15:59:01+00:00
https://github.com/monero-project/bitmonero/pull/803 fixes the saving in RPC mode


## fluffypony | 2016-05-10T12:33:21+00:00
Fixed, per @moneromooo-monero 


# Action History
- Created by: arnuschky | 2016-04-03T22:00:19+00:00
- Closed at: 2016-05-10T12:33:21+00:00
