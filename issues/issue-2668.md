---
title: Dissapearing coins on testnet after 'rescan_bc' - v0.11.0.0-15b0ff2c
source_url: https://github.com/monero-project/monero/issues/2668
author: 1337tester
assignees: []
labels: []
created_at: '2017-10-16T11:10:16+00:00'
updated_at: '2017-10-22T09:56:23+00:00'
type: issue
status: closed
closed_at: '2017-10-22T09:56:23+00:00'
---

# Original Description
Playing with build "v0.11.0.0-15b0ff2c", when suddendly my balance disappeared without any apparent reason, could it be that I just misinterpreting something?

![balance_lost](https://user-images.githubusercontent.com/6553766/31608924-74aeb096-b272-11e7-9037-f0856a729b10.jpg)

after this I tried rescanning
![balance_lost2](https://user-images.githubusercontent.com/6553766/31609114-25afb610-b273-11e7-817d-d059686d0fd0.jpg)

[monero-wallet-cli.log](https://github.com/monero-project/monero/files/1387168/monero-wallet-cli.log)

OS - Ubunutu 17.04

# Discussion History
## moneromooo-monero | 2017-10-16T11:45:47+00:00
Are you on your own testnet, mining from zero ?

## 1337tester | 2017-10-16T23:01:42+00:00
I think im on the testnet v6:
![image](https://user-images.githubusercontent.com/6553766/31638971-ad43ed86-b2d6-11e7-9cb9-05695b68201a.png)


## moneromooo-monero | 2017-10-16T23:12:28+00:00
Post a level 2 wallet log to fpaste.org please.

## 1337tester | 2017-10-17T00:12:47+00:00
I simulated something quite similar, because now I wasnt able to get even the balance, the tx dissapeared without a trace
![image](https://user-images.githubusercontent.com/6553766/31640740-5fea5e26-b2e0-11e7-92e3-c77825cc25ed.png)

Logfile
https://paste.fedoraproject.org/paste/JAVsqmkn2QujW~VIuUSdUA

Might be that this is somehow caused by my setup - launching daemon and the CLI from a virtual machine

## moneromooo-monero | 2017-10-17T08:40:36+00:00
I should have been clearer:

Post a level 2 wallet log to fpaste.org *showing a wallet sync* please.

## 1337tester | 2017-10-19T09:47:13+00:00
Should be more diligent about my initial bug reports;)

Fresh scenario now:
1. Refreshed testnet daemon
1. Check balance (is 0/0)
1. Check transfers (none seem to be present in history)
1. Send a tx to this wallet (as you see on the screenshot)
1. rescan_bc (thought it might help speed it up, didn't)
1. Wait ~15 minutes
1. Check balance, transfers (0/0, **no transfers suddenly**)

I'm running Ubunutu 17.04 in a VM VirtualBox inside another type of linux -> maybe this fact matters

![balance_lost4](https://user-images.githubusercontent.com/6553766/31763949-1d586620-b4c0-11e7-88bd-d0c9c75db483.jpg)

monerod.log (I hope you meant this by wallet log)
https://paste.fedoraproject.org/paste/dBFrmZnlBeRiUokv-8-ciw

monero-wallet-cli.log
https://paste.fedoraproject.org/paste/VBcj7P91pNo~EiwUmJqVgw

## moneromooo-monero | 2017-10-19T11:10:47+00:00
Are you really sure this is log level 2 ?

## moneromooo-monero | 2017-10-19T11:13:21+00:00
Anyway, assuming you have a recent master, type "get" in monero-wallet-cli, and check the value of refresh-from-block-height. If this is a crazy high value, set it to 0 and try again. If you don't have a recent master, update to recent master and try again.

## stoffu | 2017-10-19T11:59:02+00:00
@1337tester 
You have `pool` in the beginning of the line printed by `show_transfers` which means that it's an incoming transfer to you but not confirmed yet. It is a correct behavior to show the balance as 0 when the incoming transfer is still unconfirmed. After the tx is confirmed, it should change from `pool` to `in`. Do you still see zero balance?

## moneromooo-monero | 2017-10-21T10:59:40+00:00
Looks like it will be much easier if you give the seed, and I can check here.

## 1337tester | 2017-10-21T11:34:03+00:00
Sorry for long response time, was trying some things.
Firstly, I realized that this situation was done on monero-wallet-cli, but code was from the [monero-core](https://github.com/monero-project/monero-core) (the split is a bit confusing to me because it seems that the GUI project has the whole cli functionality inside of it)

I tried to repeat the problem with several varying parameters, but was not able to create a wallet with this behavior -> all wallets created after and before have not this bug -> I think the wallet file is therefore somehow unintentionally corrupted

wallet files - https://www.dropbox.com/sh/cm02jembaojmda5/AAC4cXvTJvHfDsLScRooQAw2a?dl=0
password is " "





## moneromooo-monero | 2017-10-21T12:21:39+00:00
Your refresh-from-block-height is 1101524, which is in the future. So you need to use commit 4090e8c6, which allows you to change it via set, and then: set refresh-from-block-height 900000 (or from wherever your wallet started).

## 1337tester | 2017-10-21T13:16:38+00:00
changed the height and rescanned, all tx seems to be there, thanks. Still wonder how could I change the block height refresh on the old version..

For me OK - please close issue


## moneromooo-monero | 2017-10-21T13:41:14+00:00
You can't on the old version. That's why I told you to use commit 4090e8c, 

## 1337tester | 2017-10-21T13:53:50+00:00
I meant how could I created that situation in the first place when I didn't had the new version

## moneromooo-monero | 2017-10-21T13:56:53+00:00
Possibly by creating the wallet while the daemin wasn't running, or when it was running and synced to very few blocks and/or not yet aware of other peers with a more current height.

## moneromooo-monero | 2017-10-22T09:55:28+00:00
+resolved

# Action History
- Created by: 1337tester | 2017-10-16T11:10:16+00:00
- Closed at: 2017-10-22T09:56:23+00:00
