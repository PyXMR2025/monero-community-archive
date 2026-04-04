---
title: Monero GUI wallet first-launch wizard (reinitialised) after power failure
source_url: https://github.com/monero-project/monero-gui/issues/3256
author: mattmill30
assignees: []
labels: []
created_at: '2020-12-05T11:24:54+00:00'
updated_at: '2020-12-06T01:59:05+00:00'
type: issue
status: closed
closed_at: '2020-12-06T01:59:05+00:00'
---

# Original Description
I have been running a Monero GUI Wallet for over a year since v0.14.1.0, now upgraded to v0.17.1.5, and have received several Monero transactions.

Following a power failure, immediately prior to which there was a large amount of hard drive activity - although monerod had completed the blockchain synchronisation, but due to system resources may have been partially suspended in paged memory - relaunching the Monero GUI Wallet presents the "first-launch" configuration interface.

![image](https://user-images.githubusercontent.com/6415621/101229647-31e63a00-3699-11eb-928d-261ba49ee3dc.png)

An additional factor is that on the relaunch of Monero GUI Wallet the Immunet antivirus decided to silently quarantine executables: "monero-blockchain-export.exe" and "monero-wallet-rpc.exe", which after a couple of Wallet relaunches I then realised and restored. Except "monero-wallet-rpc.exe" apparently failed to restore, but it is once again in the Monero folder, so I've no idea what "failed" about the restoration.

I haven't attempted a re-installation of the Monero v0.17.1.5 GUI wallet.

Original configuration:
```
Monero Program Files: %ProgramFilesFolder%\Cryptocurrencies\Client\Monero\
Monero Program Data (bitmonero): %AllUsersProfile%\Cryptocurrencies\Monero\
Monero Daemon log: %AllUsersProfile%\Cryptocurrencies\Monero\bitmonero.log
Monero Wallet File: %LocalAppData%\Wallets\Monero\
Monero Wallet Log: %AppData%\monero-wallet-gui\monero-wallet-gui.log
```

NB: I can't find a location containing monero.conf or bitmonero.conf. I don't know whether these normally exist. Though a Hard Drive Deep Scan hasn't revealed a file with either of those names which has recently been deleted either.

Since the power failure the following configuration appears to be present:
```
Monero Program Files: (unchanged)
Monero Program Data (bitmonero): %AllUsersProfile%\bitmonero\
Monero Daemon log: %AllUsersProfile%\bitmonero\bitmonero.log
Monero Wallet File: ?no idea?
Monero Wallet Log: ?no idea? - on one launch after tweaking the Monero GUI Wallet shortcut "start in" working directory to C:\ProgramData\Cryptocurrencies\Monero\: %AppData%\monero-wallet-gui\monero-wallet-gui.log
```

**Registry files**:
_Computer\HKEY_CURRENT_USER\SOFTWARE\monero-project\monero-core_:
```
REG_SZ: "blockchainDataDir": <blank>
REG_SZ: "wallet_path": <blank>
```

_Computer\HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\Monero GUI Wallet_is1_:
```
REG_SZ: "Inno Setup CodeFile: BlockChainDir": C:\ProgramData\Cryptocurrencies\Monero
REG_SZ: "Inno Setup: User": Administrator
REG_SZ: "InstallLocation": C:\Program Files\Cryptocurrencies\Client\Monero\
```

# Discussion History
## mattmill30 | 2020-12-05T11:25:15+00:00
It would be ideal to be provided with "standalone" and "workstation" solutions, as if the "standalone" solution is to populate the HKEY_CURRENT_USER "blockchainDataDir" and "wallet_path" registries mentioned above, this isn't useful for a multi-user "workstation" environment.

It would also be useful to determine how this happened, and whether a "workstation" configuration would mitigate this issue in future, in the case that this resulted from corrupted config/registries which caused the Monero GUI Wallet "re-initialisation" to a default (seemingly non-existant) LOCAL_MACHINE configuration, such as "LOCAL_MACHINE\SOFTWARE\monero-project\monero-core" registries.

How does the "Inno Setup" work? Does it provide a "first-launch" configuration of the Monero GUI Wallet based upon the "Monero GUI Wallet_is1" "Inno Setup" registries?
In which case, was the cause of the "re-initialisation" a corrupt or missing config/registries, which aren't automatically re-applied, because they are only applied at "first-launch" by the "Inno Setup", and so weren't re-applied because this wasn't a "first-launch" of the Monero GUI Wallet?

## mattmill30 | 2020-12-05T11:39:13+00:00
It would be ideal for a best practice multi-user workstation configuration to be provided in the above bug, after which I'd appreciate assistance in recovering my current users Monero GUI Wallet

## mattmill30 | 2020-12-05T22:56:11+00:00
[C:\ProgramData\Cryptocurrencies\Monero\bitmonero.log](https://github.com/monero-project/monero-gui/files/5647979/bitmonero_blockchainDataDir.log)
[C:\Users\User\AppData\Roaming\monero-wallet-gui\monero-wallet-gui.log](https://github.com/monero-project/monero-gui/files/5647990/monero-wallet-gui.log)


Additional bitmonero log, which was populated by default after 'blockchainDataDir' was reset, but also strangely has been logging trace amounts simultaneously with the bitmonero.log above.
[C:\ProgramData\bitmonero\bitmonero.log](https://github.com/monero-project/monero-gui/files/5647978/bitmonero_default.log)


## mattmill30 | 2020-12-06T01:53:00+00:00
I added the following registry key to ensure monerod was using the custom monero blockchain directory:
```
[HKEY_CURRENT_USER\SOFTWARE\monero-project\monero-core]
"blockchainDataDir"="C:\ProgramData\Cryptocurrencies\Monero"
```

![image](https://user-images.githubusercontent.com/6415621/101269266-252f1800-3765-11eb-9d05-11cbe8dadb9a.png)

Relaunching Monero GUI Wallet and choosing 'Advanced mode' to 'Open a wallet from file', created the wallet_path registry:
```
[HKEY_CURRENT_USER\SOFTWARE\monero-project\monero-core]
"wallet_path"="C:\Users\User\AppData\Local\Wallets\Monero\wallets\User\User.keys"
```

## mattmill30 | 2020-12-06T01:59:05+00:00
The above fix restored the Monero GUI Wallet to full working order, but the cause of this issue needs to be identified and resolved, as it is a major UX issue, which will either inhibit XMR adoption to non-technically savvy users, or result in negative press due to people believing they've lost funds.

# Action History
- Created by: mattmill30 | 2020-12-05T11:24:54+00:00
- Closed at: 2020-12-06T01:59:05+00:00
