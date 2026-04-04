---
title: Cleanup (startup) logging output
source_url: https://github.com/monero-project/monero-gui/issues/613
author: voidzero
assignees: []
labels:
- resolved
created_at: '2017-03-26T22:23:35+00:00'
updated_at: '2018-11-18T18:00:35+00:00'
type: issue
status: closed
closed_at: '2018-11-18T18:00:35+00:00'
---

# Original Description
As discussed on IRC where I mentioned that in particular the following lines may be a bit too messy and confusing (these come before the user has entered the password):

```
2017-03-26 23:32:10.702     7fab48822700        ERROR   net.http   contrib/epee/include/storages/portable_storage.h:161       portable_storage: wrong binary format - signature missmatch
2017-03-26 23:32:10.702     7fab48822700        ERROR   wallet.wallet2     src/wallet/wallet2.cpp:2081     !r. THROW EXCEPTION: error::invalid_password
2017-03-26 23:32:10.702     7fab48822700        WARN    net.http   src/wallet/wallet_errors.h:697  /mnt/tmp/src/monero-core/monero/src/wallet/wallet2.cpp:2081:N5tools5error16invalid_passwordE: invalid password
2017-03-26 23:32:10.703     7fab48822700        ERROR   WalletAPI  src/wallet/api/wallet.cpp:502   Error opening wallet: invalid password
2017-03-26 23:32:10.719     7fab48822700        ERROR   WalletAPI  src/wallet/api/wallet.cpp:551   Status_Critical - not storing wallet
```

Perhaps move these to a lower log level and/or make it clear that this is expected behaviour. Right now it's a bit ambiguous - if the user didn't enter a password yet, no password was tried that was invalid. "Password unknown - querying user" could be a more suitable alternative.

Additionally, when the password has been correctly entered, perhaps a line like "wallet opened - resuming wallet storage" can be added to re-ensure the user.

# Discussion History
## MaxXor | 2017-04-14T09:25:42+00:00
I searched for this error until I stumbled across this post. Good to know this is expected behavior. I 100% agree this should be made more clear as it's very confusing right now.

## voidzero | 2017-04-21T01:59:08+00:00
One thing to note - I usually run monerod with `tsocks`, and recently discovered that most of the output pertaining to proxies, connections and so on is actually barfed out by that one, and not by monerod. So then I edited the tsocks source, basically just moved a lot of logging from notice (iirc) to debug, and recompiled. I can still see it if I run `tsocks --debug` but otherwise it cleaned up the output by a substantial amount.

*edit:* argh, I was talking about monerod. Didn't realise that this is the monero GUI repository - I was just cleaning up some of my old notifications. Sorry about that. Still a useful tip, though. :grimacing: 

## erciccione | 2018-11-18T13:19:26+00:00
+resolved

# Action History
- Created by: voidzero | 2017-03-26T22:23:35+00:00
- Closed at: 2018-11-18T18:00:35+00:00
