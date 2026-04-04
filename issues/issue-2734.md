---
title: Please Help! -- GUI wallet Daemon failed to start and can't find log or monerod
source_url: https://github.com/monero-project/monero-gui/issues/2734
author: afariab
assignees: []
labels: []
created_at: '2020-01-19T02:32:57+00:00'
updated_at: '2020-08-26T23:27:22+00:00'
type: issue
status: closed
closed_at: '2020-08-26T23:27:22+00:00'
---

# Original Description
I'm running the GUI wallet v0.15.0.2 with a Ledger Nano S (the Ledger is updated as of yesterday) on a mac. When I open the wallet I keep getting this message "Daemon failed to start. Please check your wallet and daemon log for errors. You can also try to start monerod manually."

I've scoured the monero guide and the internet and can't seem to solve this. I can't find monerod or monerod.exe on my computer and my firewall is completely turned off, so that's not the issue. I've re-downloaded the GUI app and still no monerod.exe.

How/where can I check the daemon log or run monerod manually? I'm really at a loss. Any help would be greatly appreciated!

# Discussion History
## selsta | 2020-01-19T07:37:04+00:00
Right click on monero-wallet-gui -> Show package contents -> Contents -> MacOS -> monerod

Are you using simple mode?

## imrecsoka | 2020-01-22T06:26:50+00:00
> 
> 
> I'm running the GUI wallet v0.15.0.2 with a Ledger Nano S (the Ledger is updated as of yesterday) on a mac. When I open the wallet I keep getting this message "Daemon failed to start. Please check your wallet and daemon log for errors. You can also try to start monerod manually."
> 
> I've scoured the monero guide and the internet and can't seem to solve this. I can't find monerod or monerod.exe on my computer and my firewall is completely turned off, so that's not the issue. I've re-downloaded the GUI app and still no monerod.exe.
> 
> How/where can I check the daemon log or run monerod manually? I'm really at a loss. Any help would be greatly appreciated!

I honestly dont see why u putting up with this wallet, it has not changed since 2017, its the same nonsense wallet.

## selsta | 2020-01-22T12:38:34+00:00
> I honestly dont see why u putting up with this wallet, it has not changed since 2017, its the same nonsense wallet.

daemon not starting is unrelated to the wallet.

## imrecsoka | 2020-01-23T03:52:36+00:00
I want to install the GUI wallet and the Daemon should just work. 
If i install the Bitcoin Core wallet , it all just works.
Why should a component be broken, its just painful to deal with.

## selsta | 2020-01-23T13:48:23+00:00
> Why should a component be broken, its just painful to deal with.

The majority of people have no problem. It can have multiple reasons why it isn’t working on your side. Do you have enough harddisk space left?

## selsta | 2020-08-26T23:27:22+00:00
Closing due to inactivity. Issue is most likely resolved in v0.16.0.3. Please open a new issue if you still have problems.

# Action History
- Created by: afariab | 2020-01-19T02:32:57+00:00
- Closed at: 2020-08-26T23:27:22+00:00
