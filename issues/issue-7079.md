---
title: monerod + Monero GUI wallet multi-user workstation configuration
source_url: https://github.com/monero-project/monero/issues/7079
author: mattmill30
assignees: []
labels: []
created_at: '2020-12-05T02:55:16+00:00'
updated_at: '2020-12-05T11:40:02+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I want to run Monero on a multi-user workstation, where a single monerod instance, probably a Windows Service, provides blockchain services for a separate wallet for each user

My current configuration is:
```
Monero Program Files: %ProgramFilesFolder%\Cryptocurrencies\Client\Monero\
Monero Program Data (bitmonero): %AllUsersProfile%\Cryptocurrencies\Monero\
Monero Daemon log: %AllUsersProfile%\Cryptocurrencies\Monero\bitmonero.log
Monero Wallet File: %LocalAppData%\Wallets\
Monero Wallet Log: %AppData%\monero-wallet-gui\monero-wallet-gui.log
```

Please would someone detail a best practice installation + configuration procedure?

# Discussion History
## mattmill30 | 2020-12-05T03:13:01+00:00
My current configuration may not be ideal, so I'm willing to relocate files or use additional services to implement extra layers of security.

For example, my setup is on a home workstation, so currently my user profiles aren't encrypted, which means that whilst Wallet files at %LocalAppData%\Wallets are password protected by the Monero GUI Wallet, there isn't any additional protection which might be desirable for common multi-user workstation environments.

## erciccione | 2020-12-05T09:47:39+00:00
The repository of the GUI wallet is https://github.com/monero-project/monero-gui.

## erciccione | 2020-12-05T11:32:05+00:00
I see you already created https://github.com/monero-project/monero-gui/issues/3256. Thanks :)

# Action History
- Created by: mattmill30 | 2020-12-05T02:55:16+00:00
