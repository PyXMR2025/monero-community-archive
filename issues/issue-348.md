---
title: Daemon not compatible with GUI
source_url: https://github.com/monero-project/monero-gui/issues/348
author: jsnfwlr
assignees: []
labels: []
created_at: '2016-12-23T03:21:59+00:00'
updated_at: '2016-12-23T12:09:17+00:00'
type: issue
status: closed
closed_at: '2016-12-23T11:30:25+00:00'
---

# Original Description
![oops](https://cloud.githubusercontent.com/assets/1097895/21446500/d459cae0-c901-11e6-99a5-7a49f0164a51.png)

Freshly downloaded, machine has never had any monero daemon installed on it ... the daemon is the one that was in the same zip as the GUI ...

# Discussion History
## ghost | 2016-12-23T04:15:28+00:00
What versions are listed on the settings page for the GUI and daemon?

## jsnfwlr | 2016-12-23T04:23:33+00:00
Unfortunately I can't get to the settings page because it crashes immediately after showing this error

## medusadigital | 2016-12-23T06:32:47+00:00
what platform is this ?
can you launch it via cmd (assuming its windows) like this:

monero-wallet-gui.exe > log.txt

## jsnfwlr | 2016-12-23T11:08:28+00:00
odd ... when I run it with the > log.txt at the end, it works fine ... 

## jsnfwlr | 2016-12-23T11:12:11+00:00
Actually, no ... it only worked because I got my password wrong ... odd 

2016-Dec-23 19:10:13.344081 ERROR C:/msys64/home/vagrant/slave/monero-core-win64/build/monero/contrib/epee/include/storages/portable_storage.h:161 portable_storage: wrong binary format - signature missmatch
2016-Dec-23 19:10:13.344581 ERROR C:/msys64/home/vagrant/slave/monero-core-win64/build/monero/src/wallet/wallet2.cpp:1959 !r. THROW EXCEPTION: error::invalid_password
2016-Dec-23 19:10:13.344581 C:/msys64/home/vagrant/slave/monero-core-win64/build/monero/src/wallet/wallet2.cpp:1959:N5tools5error16invalid_passwordE: invalid password
2016-Dec-23 19:10:13.345081 ERROR C:/msys64/home/vagrant/slave/monero-core-win64/build/monero/src/wallet/api/wallet.cpp:298 Error opening wallet: invalid password
2016-Dec-23 19:10:13.557108 ~WalletImpl
2016-Dec-23 19:10:13.557108 closing wallet...
2016-Dec-23 19:10:13.557108 wallet::store done
2016-Dec-23 19:10:13.557108 Calling wallet::stop...
2016-Dec-23 19:10:13.557108 wallet::stop done


## BoscoMurray | 2016-12-23T11:27:32+00:00
I saw the same error but only for a second, then the error vanished and the daemon started syncing. I used the downloaded binaries on a fresh install of Ubuntu 16.04, 2 vCPU, 8GB RAM in a VirtualBox VM on an i5 laptop with decent SSD.

## jsnfwlr | 2016-12-23T11:30:16+00:00
Well it's working perfectly now.

## Jaqueeee | 2016-12-23T11:33:12+00:00
@BoscoMurray the error above is nothing to worry about. It's just the wallets way of saying that the password was wrong. If you have a wallet with password that error is always shown because it tries to open the wallet without a password first. 

## BoscoMurray | 2016-12-23T11:45:17+00:00
I didn't get my password wrong. It's like the wallet was too quick to think there was an issue and threw up this error, then cleared the error itself. No biggie, just a UX thing.

## Jaqueeee | 2016-12-23T11:49:28+00:00
Not saying you got it wrong. But the GUI always tries to open the last opened wallet on startup, and if it is password protected it will throw this error. 

## BoscoMurray | 2016-12-23T12:03:18+00:00
Yup. I know it's trivial for a dev, but is it not worth changing its behaviour for a better UX?

## Jaqueeee | 2016-12-23T12:09:17+00:00
ah. I think we're talking about different things here. I was referring to the error in the log. =)
We should definitely fix the issue that causes the GUI to report the daemon isnt compatible. If we can reproduce it somehow. 

# Action History
- Created by: jsnfwlr | 2016-12-23T03:21:59+00:00
- Closed at: 2016-12-23T11:30:25+00:00
