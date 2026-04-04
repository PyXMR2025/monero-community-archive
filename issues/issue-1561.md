---
title: Bitdefender Antivirus detection false positiv?
source_url: https://github.com/monero-project/monero-gui/issues/1561
author: awigg
assignees: []
labels:
- resolved
created_at: '2018-09-16T17:00:39+00:00'
updated_at: '2018-12-17T08:18:29+00:00'
type: issue
status: closed
closed_at: '2018-12-17T08:18:29+00:00'
---

# Original Description
I installed monero-wallet with homebrew:

> brew cask info monero-wallet
> monero-wallet: 0.12.3.0
> https://getmonero.org/
> /usr/local/Caskroom/monero-wallet/0.12.3.0 (160B)
> From: https://github.com/Homebrew/homebrew-cask/blob/master/Casks/monero-wallet.rb
> ==> Name
> Monero Wallet
> ==> Artifacts
> monero-gui-v0.12.3.0/monero-wallet-gui.app (App)

And I checked the checksum against https://getmonero.org/downloads/
Everything seems fine, but Bitdefender Antivirus doesn't seem to like the gui:

> 16.09.18, 18:48
>  
> Adware.MAC.Generic.10610 deleted
>  
> /Applications/monero-wallet-gui.app/Contents/MacOS/monero-blockchain-import
>  
> 16.09.18, 18:47
>  
> Adware.MAC.Generic.10610 deleted
>  
> /Applications/monero-wallet-gui.app/Contents/MacOS/monero-blockchain-import
>  
> 16.09.18, 18:46
>  
> Adware.MAC.Generic.10733 deleted
>  
> /Applications/monero-wallet-gui.app/Contents/MacOS/monero-blockchain-export
>  
> 16.09.18, 18:45
>  
> Adware.MAC.Generic.10733 deleted
>  
> /Applications/monero-wallet-gui.app/Contents/MacOS/monero-blockchain-export
>  
> 16.09.18, 18:45
>  
> Application.MAC.Miner.ID deleted
>  
> /Applications/monero-wallet-gui.app/Contents/MacOS/monero-wallet-gui
>  
> 16.09.18, 18:44
>  
> Application.MAC.Miner.ID deleted
>  
> /Applications/monero-wallet-gui.app/Contents/MacOS/monero-wallet-gui
>  
> 16.09.18, 18:43
>  
> Adware.MAC.Generic.10607 deleted
>  
> /Applications/monero-wallet-gui.app/Contents/MacOS/monerod
>  
> 16.09.18, 18:42
>  
> Adware.MAC.Generic.10607 deleted
>  
> /Applications/monero-wallet-gui.app/Contents/MacOS/monerod
>  
> 16.09.18, 18:42
>  
> Application.MAC.Miner.IE deleted
>  
> /Applications/monero-wallet-gui.app/Contents/MacOS/monero-wallet-rpc
>  
> 16.09.18, 18:41
>  
> Application.MAC.Miner.IE deleted
>  
> /Applications/monero-wallet-gui.app/Contents/MacOS/monero-wallet-rpc
>  
> 16.09.18, 18:39
>  
> Adware.MAC.Generic.10590 deleted
>  
> /Applications/monero-wallet-gui.app/Contents/MacOS/monero-blockchain-usage
>  
> 16.09.18, 18:38
>  
> Application.MAC.Miner.ID deleted
>  
> /Applications/monero-wallet-gui.app/Contents/MacOS/monero-wallet-cli
>  
> 16.09.18, 18:37
>  
> Adware.MAC.Generic.10661 deleted
>  
> /Applications/monero-wallet-gui.app/Contents/MacOS/monero-blockchain-blackball
>  
> 16.09.18, 18:35
>  
> Application.MAC.Miner.IE deleted
>  
> /Applications/monero-wallet-gui.app/Contents/MacOS/monero-gen-trusted-multisig
>  
> 16.09.18, 18:09
>  
> Application.MAC.Miner.IE deleted
>  
> /private/var/folders/*/*/*/*/monero-gui-v0.12.3.0/monero-wallet-gui.app/Contents/MacOS/monero-gen-trusted-multisig


Is this all a false positiv? And if so, could you let them fix this?

# Discussion History
## dEBRUYNE-1 | 2018-09-16T17:57:57+00:00
>Is this all a false positiv?

Yes, see my comment here:

https://www.reddit.com/r/Monero/comments/99ofpm/malwarebytes_considers_monero_malware/e4pime5/

>And if so, could you let them fix this?

Unfortunately, I genuinely doubt they would remove the Monero software from their detection list. 

## awigg | 2018-09-16T18:02:07+00:00
Thank you for your quick answer.
I would suggest to try it first, and publish their answer, so that we could start a discussion.

## dEBRUYNE-1 | 2018-12-17T08:05:13+00:00
Going to close this in favor of #1747. 



## dEBRUYNE-1 | 2018-12-17T08:05:18+00:00
+resolved

# Action History
- Created by: awigg | 2018-09-16T17:00:39+00:00
- Closed at: 2018-12-17T08:18:29+00:00
