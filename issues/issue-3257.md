---
title: 'Possible conflict between "Inno Setup: BlockchainDir" setting and main.qml:
  MoneroSettings { property string blockchainDataDir: "" }'
source_url: https://github.com/monero-project/monero-gui/issues/3257
author: mattmill30
assignees: []
labels: []
created_at: '2020-12-05T19:51:57+00:00'
updated_at: '2020-12-18T00:58:16+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
When I originally installed Monero GUI Wallet v0.14.1.0, I specified the BlockchainDir in the Inno Setup as "C:\ProgramData\Cryptocurrencies\Monero", rather than the default "C:\ProgramData\bitmonero", but after upgrading to Monero v0.17.1.5 and following a power failure - #3256 - the [HKCU\SOFTWARE\monero-project\monero-core] registries were re-initialised to the same configuration as MoneroSettings, including blockchainDataDir and wallet_path.

The Monero GUI Wallet should not have the ability to automatically and silently reinitialise the blockchainDataDir registry or any other monerod configurations (daemon{Flags,Password,Username}), especially if settings were configured by the installer and are present under [HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\Monero GUI Wallet_is1].
Monero GUI Wallet should configure monerod via an API - monero-project/monero#7083

Such re-configuration of monerod poses a serious security threat on Multi-user workstations - monero-project/monero#7079.

I noticed that a [change to the PersistantSettings for languages](https://github.com/monero-project/monero-gui/commit/56e611480abcd2e02701961a5a4772ddbad4666d) was implemented between https://github.com/monero-project/monero-gui/compare/v0.17.1.3...v0.17.1.5, which if re-initialisation of MoneroSettings were triggered, I assume would cause all of the existing PersistentSettings to reset, including account_name, blockchainDataDir and wallet_path

Comparison of MoneroSettings and current 'Monero GUI Wallet_is1' and 'monero-core' registries:
MoneroSettings:
```
        property string language: 'English (US)'
        property string language_wallet: 'English'
        property string locale: 'en_US'
        property string account_name
        property string wallet_path
        property bool   allow_background_mining : false
        property bool   miningIgnoreBattery : true
        property var    nettype: NetworkType.MAINNET
        property int    restore_height : 0
        property bool   is_trusted_daemon : false
        property bool   is_recovering : false
        property bool   is_recovering_from_device : false
        property bool   customDecorations : true
        property string daemonFlags
        property int logLevel: 0
        property string logCategories: ""
        property string daemonUsername: ""
        property string daemonPassword: ""
        property bool transferShowAdvanced: false
        property bool receiveShowAdvanced: false
        property bool historyShowAdvanced: false
        property bool historyHumanDates: true
        property string blockchainDataDir: ""
        property bool useRemoteNode: false
        property string remoteNodeAddress: ""
        property string bootstrapNodeAddress: ""
        property bool segregatePreForkOutputs: true
        property bool keyReuseMitigation2: true
        property int segregationHeight: 0
        property int kdfRounds: 1
        property bool hideBalance: false
        property bool askPasswordBeforeSending: true
        property bool lockOnUserInActivity: true
        property int walletMode: 2
        property int lockOnUserInActivityInterval: 10  // minutes
        property bool blackTheme: true
        property bool checkForUpdates: true
        property bool autosave: true
        property int autosaveMinutes: 10

        property bool fiatPriceEnabled: false
        property bool fiatPriceToggle: false
        property string fiatPriceProvider: "kraken"
        property string fiatPriceCurrency: "xmrusd"

        property string proxyAddress: "127.0.0.1:9050"
        property bool proxyEnabled: isTails
```

Monero GUI Wallet_is1 registry:
```
[HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\Monero GUI Wallet_is1]:
"Inno Setup CodeFile: BlockChainDir"="C:\ProgramData\Cryptocurrencies\Monero"
"Inno Setup: User"="Administrator"
"InstallLocation"="C:\Program Files\Cryptocurrencies\Client\Monero\"
```

monero-core registry:
```
[HKEY_CURRENT_USER\SOFTWARE\monero-project\monero-core]
"hideBalance"="false"
"daemonPassword"=""
"remoteNodeAddress"=""
"auto_donations_enabled"="false"
"fiatPriceProvider"="kraken"
"nettype"=dword:00000000
"bootstrapNodeAddress"=""
"historyHumanDates"="true"
"kdfRounds"=dword:00000001
"receiveShowAdvanced"="false"
"is_trusted_daemon"="false"
"transferShowAdvanced"="false"
"blackTheme"="true"
"is_recovering_from_device"="false"
"lockOnUserInActivityInterval"=dword:0000000a
"segregationHeight"=dword:00000000
"logCategories"=""
"lockOnUserInActivity"="true"
"daemonFlags"=""
"is_recovering"="false"
"allow_background_mining"="false"
"walletMode"=dword:00000002
"fiatPriceCurrency"="xmrusd"
"historyShowAdvanced"="false"
"auto_donations_amount"=dword:00000032
"language"="English (US)"
"payment_id"=""
"customDecorations"="true"
"fiatPriceEnabled"="false"
"remoteNodeRegion"=""
"logLevel"=dword:00000000
"daemonUsername"=""
"showPid"="false"
"keyReuseMitigation2"="true"
"useRemoteNode"="false"
"segregatePreForkOutputs"="true"
"miningIgnoreBattery"="true"
"remoteNodeService"=""
"blockchainDataDir"=""
"fiatPriceToggle"="false"
"account_name"=""
"locale"="en_US"
"wallet_path"=""
"restore_height"=dword:00000000
"askPasswordBeforeSending"="true"
"checkForUpdates"="true"
"autosave"="true"
"autosaveMinutes"=dword:0000000a
"proxyAddress"="127.0.0.1:9050"
"proxyEnabled"="false"
"language_wallet"="English"

[HKEY_CURRENT_USER\SOFTWARE\monero-project\monero-core\QQControlsFileDialog]
"sidebarSplit"="111.60000000000001"
"favoriteFolders"=hex(7):00,00
"sidebarWidth"="80"
"width"=dword:00000000
"sidebarVisible"="false"
"height"=dword:00000000
```

# Discussion History
## xiphon | 2020-12-06T02:14:02+00:00
> I noticed that a change to the PersistantSettings for languages was implemented between v0.17.1.3...v0.17.1.5, which if re-initialisation of MoneroSettings were triggered, I assume would cause all of the existing PersistentSettings to reset, including account_name, blockchainDataDir and wallet_path

It shouldn't. If it does, please provide steps to reproduce.

## mattmill30 | 2020-12-18T00:58:16+00:00
I can't necessarily provide steps to reproduce. However, the issue has reoccurred following the update from https://github.com/monero-project/monero-gui/compare/v0.17.1.5...v0.17.1.7

```
[HKEY_CURRENT_USER\SOFTWARE\monero-project\monero-core]
"hideBalance"="false"
"daemonPassword"=""
"remoteNodeAddress"=""
"auto_donations_enabled"="false"
"fiatPriceProvider"="kraken"
"nettype"=dword:00000000
"bootstrapNodeAddress"=""
"historyHumanDates"="true"
"kdfRounds"=dword:00000001
"receiveShowAdvanced"="false"
"is_trusted_daemon"="false"
"transferShowAdvanced"="false"
"blackTheme"="true"
"is_recovering_from_device"="false"
"lockOnUserInActivityInterval"=dword:0000000a
"segregationHeight"=dword:00000000
"logCategories"=""
"lockOnUserInActivity"="true"
"daemonFlags"=""
"is_recovering"="false"
"allow_background_mining"="false"
"walletMode"=dword:00000002
"fiatPriceCurrency"="xmrusd"
"historyShowAdvanced"="false"
"auto_donations_amount"=dword:00000032
"language"="English (US)"
"payment_id"=""
"customDecorations"="true"
"fiatPriceEnabled"="false"
"remoteNodeRegion"=""
"logLevel"=dword:00000000
"daemonUsername"=""
"showPid"="false"
"keyReuseMitigation2"="true"
"useRemoteNode"="false"
"segregatePreForkOutputs"="true"
"miningIgnoreBattery"="true"
"remoteNodeService"=""
"blockchainDataDir"=""
"fiatPriceToggle"="false"
"account_name"=""
"locale"="en_US"
"wallet_path"=""
"restore_height"=dword:00000000
"askPasswordBeforeSending"="true"
"checkForUpdates"="true"
"autosave"="true"
"autosaveMinutes"=dword:0000000a
"proxyAddress"="127.0.0.1:9050"
"proxyEnabled"="false"
"language_wallet"="English"
"askDesktopShortcut"="false"

[HKEY_CURRENT_USER\SOFTWARE\monero-project\monero-core\QQControlsFileDialog]
"sidebarSplit"="111.60000000000001"
"favoriteFolders"=hex(7):00,00
"sidebarWidth"="80"
"width"=dword:00000000
"sidebarVisible"="false"
"height"=dword:00000000
```

I've noticed that changes to the QML cache (which I understand relates to registry settings) were made to both versions:
v1.17.1.5 - portable: use portable storage folder to store QML disk cache - https://github.com/monero-project/monero-gui/commit/ec8cd137cc9592aa910e9829f8e9ce251488c70f
v1.17.1.7 - main: disable QML cache - https://github.com/monero-project/monero-gui/commit/486ba05526e2ece353da21d8a2100f614704856c

Further to the logs for my previous upgrade issue reported in https://github.com/monero-project/monero-gui/issues/3256#issuecomment-739427201 the logs for the upgrade period are:
[C:\ProgramData\Cryptocurrencies\Monero\bitmonero.log](https://github.com/monero-project/monero-gui/files/5712975/bitmonero_blockchainDataDir.log)
[C:\Users\User\AppData\Roaming\monero-wallet-gui\monero-wallet-gui.log](https://github.com/monero-project/monero-gui/files/5712976/monero-wallet-gui.log)

# Action History
- Created by: mattmill30 | 2020-12-05T19:51:57+00:00
