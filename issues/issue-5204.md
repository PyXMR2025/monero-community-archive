---
title: '[Wallet API] createWatchOnly results in error'
source_url: https://github.com/monero-project/monero/issues/5204
author: selsta
assignees: []
labels:
- invalid
created_at: '2019-02-26T22:59:58+00:00'
updated_at: '2019-03-05T14:09:38+00:00'
type: issue
status: closed
closed_at: '2019-03-05T14:09:38+00:00'
---

# Original Description
I’m currently trying to fix the create view only wallet button in the GUI (https://github.com/monero-project/monero-gui/pull/1975), but I get the following error message:

```
2019-02-26 23:06:11.433	     0x1150dc5c0	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:6953	/Users/selsta/Monero/wallets/selsta/selsta_viewonly.keys is already unlocked.
2019-02-26 23:06:11.876	     0x1150dc5c0	ERROR	wallet.wallet2	src/wallet/wallet2.cpp:11520	outputs.first > m_transfers.size(). THROW EXCEPTION: error::wallet_internal_error
2019-02-26 23:06:11.876	     0x1150dc5c0	WARNING	net.http	src/wallet/wallet_errors.h:856	/Users/selsta/dev/sel/monero-gui/monero/src/wallet/wallet2.cpp:11520:N5tools5error21wallet_internal_errorE: Imported outputs omit more outputs that we know of
2019-02-26 23:06:11.876	     0x1150dc5c0	ERROR	WalletAPI	src/wallet/api/wallet.cpp:513	Error creating view only wallet: Imported outputs omit more outputs that we know of
2019-02-26 23:06:11.876	     0x1150dc5c0	DEBUG	net	contrib/epee/include/net/net_helper.h:513	Problems at cancel: Bad file descriptor
2019-02-26 23:06:11.876	     0x1150dc5c0	DEBUG	net	contrib/epee/include/net/net_helper.h:516	Problems at shutdown: Bad file descriptor
2019-02-26 23:06:11.878	     0x1150dc5c0	DEBUG	net	contrib/epee/include/net/net_helper.h:513	Problems at cancel: Bad file descriptor
2019-02-26 23:06:11.878	     0x1150dc5c0	DEBUG	net	contrib/epee/include/net/net_helper.h:516	Problems at shutdown: Bad file descriptor
```
My code: https://github.com/monero-project/monero-gui/pull/1975/files#diff-5cf776c8892be6f28e64b4cad1bef6f6R181

It’s possible that I didn’t use the API correctly.

# Discussion History
## selsta | 2019-02-28T07:25:37+00:00
I think this had something to do with a broken wallet cache or something. I also had problems transferring with this wallet. Using an older backup of the same wallet solved this.

@moneromooo-monero should I close this?

## moneromooo-monero | 2019-03-05T13:40:21+00:00
I guess so. If it happens again with a "good" cache, please reopen.

+invalid

# Action History
- Created by: selsta | 2019-02-26T22:59:58+00:00
- Closed at: 2019-03-05T14:09:38+00:00
