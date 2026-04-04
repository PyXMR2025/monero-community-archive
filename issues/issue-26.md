---
title: several issues when opening password protected wallet on mainnet
source_url: https://github.com/monero-project/monero-gui/issues/26
author: medusadigital
assignees: []
labels: []
created_at: '2016-09-20T16:30:08+00:00'
updated_at: '2016-11-05T09:13:56+00:00'
type: issue
status: closed
closed_at: '2016-11-05T09:13:56+00:00'
---

# Original Description
If opening a password protected wallet with monero-core on mainnet, a few different issues appear.

first a screenshot:

![issuesopenijngwalletwithpassword](https://cloud.githubusercontent.com/assets/17108301/18679444/e86c21c2-7f5f-11e6-9ea5-3dde0067eec4.jpg)

on the screenshot it is visible to see that:
- there is some format issue with the wallet
- monero-core tries to open the wallet with a dummy pasword first, which is not part of the config file
- the window to enter the password opens too small

nevertheless, after the password is entered, the wallet opens correctly.

--> Ubuntu 16.04 on mainnet together with pull request #23


# Discussion History
## Jaqueeee | 2016-10-06T21:13:53+00:00
Are you still experiencing this @medusadigital ?


## medusadigital | 2016-10-07T14:59:14+00:00
i still get the errors in the Log when opening a password protected wallet, but the pasword window now has the correct size (which was the main issue)

Wallet\* WalletManager::openWallet(const QString&, const QString&, bool): opening wallet at /home/pppp/Monero Accounts//restoreAgain/restoreAgain, testnet = 0 
**2016-Oct-07 16:49:21.792413 ERROR /home/pppp/monero-core/monero/contrib/epee/include/storages/portable_storage.h:161 portable_storage: wrong binary format - signature missmatch**
**2016-Oct-07 16:49:21.792663 ERROR /home/pppp/monero-core/monero/src/wallet/wallet2.cpp:1557 !r. THROW EXCEPTION: error::invalid_password**
2016-Oct-07 16:49:21.792819 /home/pppp/monero-core/monero/src/wallet/wallet2.cpp:1557:N5tools5error16invalid_passwordE: invalid password
**2016-Oct-07 16:49:21.793111 ERROR /home/pppp/monero-core/monero/src/wallet/api/wallet.cpp:251 Error opening wallet: invalid password**
Wallet\* WalletManager::openWallet(const QString&, const QString&, bool): opened wallet: 41d7FXjswpK1111111111111111111111111111111111111111111111111111111111111111111111111111112KhNi4, status: 1
qml: >>> wallet opened: Wallet(0x7f5a04004260)

nevertheless i dont think those logs do any harm for now, so im tempted to close it. 

opinions?


## Jaqueeee | 2016-10-11T08:45:17+00:00
The GUI tries to open the wallet without password before the user is prompted for password. So this log message is just it's way of saying it didn't work. I suggest you close it or change the title to make it sound less critical if you only wan't the log message changed. ;)


## M5M400 | 2016-10-17T12:03:10+00:00
@Jaqueeee I just built it from current master and I have the same issue with the password window. Ubuntu 16.04.1 LTS amd64

![monero_wallet_password_dialog](https://cloud.githubusercontent.com/assets/22886679/19436749/4756cbb6-9472-11e6-868c-5fe856ed1cd2.png)


## medusadigital | 2016-10-18T13:56:21+00:00
Hi @M5M400 , the password window should be fixed for some time now, are you sure you have the newest master ? 


## M5M400 | 2016-10-19T08:14:54+00:00
@medusadigital pretty sure
![screenshot from 2016-10-19 10-02-25](https://cloud.githubusercontent.com/assets/22886679/19510441/8b76afe2-95e3-11e6-9a6c-edb1b1fa2296.png)

I suspect this was the fix: https://github.com/monero-project/monero-core/commit/6a5095194054b5023e8fb02e5399fd0f0b10512d

My local passwordDialog.qml is correctly missing the fixed height:

![screenshot from 2016-10-19 10-09-22](https://cloud.githubusercontent.com/assets/22886679/19510756/d2a70c1c-95e4-11e6-8959-6367a076d546.png)


## medusadigital | 2016-10-19T17:40:04+00:00
ok, here it looks like this, same OS. had good results with Qt 5.7 and Qt 5.6.2. 

![loginfixed](https://cloud.githubusercontent.com/assets/17108301/19530107/c6cda92a-9632-11e6-8078-f7c9fce85a53.png)

you are right, https://github.com/monero-project/monero-core/commit/6a5095194054b5023e8fb02e5399fd0f0b10512d was the fix and personally i never experienced the issue ever since.

will leave this open for now until we have more clearity, thanks for your report!


## M5M400 | 2016-10-20T12:38:13+00:00
just to make sure, I recompiled. same behavior :/

QMake version 3.0
Using Qt version 5.5.1 in /usr/lib/x86_64-linux-gnu

trying 5.6.2 next


## medusadigital | 2016-10-24T00:00:05+00:00
there also is another report here: https://github.com/monero-project/monero-core/issues/86


## dternyak | 2016-11-02T05:25:29+00:00
I think this can be closed after https://github.com/monero-project/monero-core/pull/95


## medusadigital | 2016-11-05T09:13:56+00:00
https://github.com/monero-project/monero-core/pull/95 is merged.

works ---> closed


# Action History
- Created by: medusadigital | 2016-09-20T16:30:08+00:00
- Closed at: 2016-11-05T09:13:56+00:00
