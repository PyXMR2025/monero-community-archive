---
title: 'Settings :: unreachable daemon no timeout; no change possible'
source_url: https://github.com/monero-project/monero-gui/issues/172
author: M5M400
assignees: []
labels: []
created_at: '2016-11-16T08:55:18+00:00'
updated_at: '2016-12-20T15:48:11+00:00'
type: issue
status: closed
closed_at: '2016-12-20T15:48:11+00:00'
---

# Original Description
With a properly connected, up2date wallet: When you go to settings page, set the daemon address to something invalid/unreachable (in my case I changed port from 18081 to 18082, where no process is listening) and hit "save", the following happens:

First I get shown a syncing page (notice the odd block counts)
![screenshot from 2016-11-16 09-40-35](https://cloud.githubusercontent.com/assets/22886679/20340366/793b7948-abe1-11e6-99c0-a14825dc5ded.png)

later, the window freezes

![screenshot from 2016-11-16 09-43-13](https://cloud.githubusercontent.com/assets/22886679/20340388/9a3ec226-abe1-11e6-86a0-aa477a20071e.png)

I have no way to change back the settings and am left with an unresponsive GUI. After force close and reopening, the GUI still tries to sync to the faulty node. And I have no way of changing the settings.

![screenshot from 2016-11-16 09-49-35](https://cloud.githubusercontent.com/assets/22886679/20340487/fe94acd6-abe1-11e6-8021-9af1e3ce14f3.png)

TL;DR; there is no way to set valid daemon settings in the GUI once it tries to connect to a node that is not reachable.

# Discussion History
## M5M400 | 2016-11-16T09:37:34+00:00
Additional info: Ubuntu 16.04.1 LTS amd64, Using Qt version 5.5.1 in /usr/lib/x86_64-linux-gnu

monero-core master 24a66c1

_click save_
_syncing dialog appears_

```
qml: saving daemon adress settings
qml: initializing..
setLanguage   "en"
qml: closing currentWallet
~Wallet: Closing wallet
qml: opening wallet at:  /path/to/wallets/Stash/Stash , testnet:  false
Wallet* WalletManager::openWallet(const QString&, const QString&, bool): opening wallet at /path/to/wallets/Stash/Stash, testnet = 0 
2016-Nov-16 10:28:20.731552 Loaded wallet keys file, with public address: 43SomeWallet
2016-Nov-16 10:28:20.750259 Trying to decrypt cache data
Wallet* WalletManager::openWallet(const QString&, const QString&, bool): opened wallet: 43SomeWallet, status: 0
qml: >>> wallet opened: Wallet(0x7f255001ac80)
qml: Displaying processing splash
qml: initializing with daemon address:  node.supportxmr.com:18082
qml: Recovering from seed:  false
qml: restore Height 0
```

_two minutes later_

```
2016-Nov-16 10:30:28.339153 ERROR /path/to/monero-core-new/monero/contrib/epee/include/net/http_client.h:869 failed to connect node.supportxmr.com:18082
2016-Nov-16 10:30:28.339190 Failed to invoke http request to  node.supportxmr.com:18082/getblocks.bin
2016-Nov-16 10:30:28.339208 ERROR /path/to/monero-core-new/monero/src/wallet/wallet2.cpp:1146 !r. THROW EXCEPTION: error::no_connection_to_daemon
2016-Nov-16 10:30:28.339231 /path/to/monero-core-new/monero/src/wallet/wallet2.cpp:1146:N5tools5error23no_connection_to_daemonE: no connection to daemon, request = getblocks.bin
refreshed
qml: >>> wallet refreshed
qml: Hiding processing splash
2016-Nov-16 10:30:33.345613 ERROR /path/to/monero-core-new/monero/contrib/epee/include/net/http_client.h:869 failed to connect node.supportxmr.com:18082
2016-Nov-16 10:30:33.345654 Failed to invoke http request to  node.supportxmr.com:18082/getheight
2016-Nov-16 10:30:33.345676 ERROR /path/to/monero-core-new/monero/src/wallet/api/wallet.cpp:478 daemonBlockChainHeight: possibly lost connection to daemon
2016-Nov-16 10:30:38.346550 ERROR /path/to/monero-core-new/monero/contrib/epee/include/net/http_client.h:869 failed to connect node.supportxmr.com:18082
2016-Nov-16 10:30:38.346585 Failed to invoke http request to  node.supportxmr.com:18082/json_rpc
2016-Nov-16 10:30:38.346606 ERROR /path/to/monero-core-new/monero/src/wallet/api/wallet.cpp:495 daemonBlockChainTargetHeight: possibly lost connection to daemon
```

_syncing splash vanishes_
_window goes dark_
-the end-


## taushet | 2016-11-16T17:38:11+00:00
Confirmed Ubuntu 16.04


## Jaqueeee | 2016-11-16T19:00:26+00:00
Weird. I could reproduce it on OS X with same node. But with different node (node.moneroworld.com) and local daemon this doesn't happen. Anyway, it's partly solved by https://github.com/monero-project/monero-core/pull/163 but I need to investigate this further


## M5M400 | 2016-11-18T10:59:29+00:00
thanks to #163 I can now close the splash and change the node setting back, but upon saving the (correct) settings, the UI freezes for 2+ minutes, then throws a no_connection_to_daemon error and then works again.

Looks like during the "Closing Wallet" sequence it is trying to fetch something from the (wrong) daemon and has to wait for the command to time out:

```
qml: saving daemon adress settings
qml: initializing..
setLanguage   "en"
qml: closing currentWallet
~Wallet: Closing wallet
***two minutes later***
2016-Nov-18 11:54:31.434076 ERROR /path/to/monero-core-new/monero/contrib/epee/include/net/http_client.h:869 failed to connect node.supportxmr.com:18082
2016-Nov-18 11:54:31.434109 Failed to invoke http request to  node.supportxmr.com:18082/getblocks.bin
2016-Nov-18 11:54:31.434118 ERROR /path/to/monero-core-new/monero/src/wallet/wallet2.cpp:1151 !r. THROW EXCEPTION: error::no_connection_to_daemon
2016-Nov-18 11:54:31.434133 /path/to/monero-core-new/monero/src/wallet/wallet2.cpp:1151:N5tools5error23no_connection_to_daemonE: no connection to daemon, request = getblocks.bin
refreshed
qml: opening wallet at:  /path/to/wallets/Stash/Stash , testnet:  false
```


# Action History
- Created by: M5M400 | 2016-11-16T08:55:18+00:00
- Closed at: 2016-12-20T15:48:11+00:00
