---
title: Wallet Blocks Syncronizing all blocks each time opening Monero GUI
source_url: https://github.com/monero-project/monero-gui/issues/1713
author: ghost
assignees: []
labels: []
created_at: '2018-10-30T04:43:07+00:00'
updated_at: '2019-02-22T07:46:22+00:00'
type: issue
status: closed
closed_at: '2018-11-02T09:51:09+00:00'
---

# Original Description
Is it recommended to leave Monero GUI always open in the background?

Yesterday I finally got the Daemon and Wallet Blocks to fully sync, when I've gone into it today the Wallet Block sync has started all over again.

Monero GUI v0.13.0.3
Windows 10 64bit

![2018-10-30 1](https://user-images.githubusercontent.com/14051589/47696287-d5122d00-dc51-11e8-8f83-7ffc227c50b5.png)


# Discussion History
## dEBRUYNE-1 | 2018-10-30T07:28:10+00:00
Are you using the GUI in conjunction with a Ledger device? 

## ghost | 2018-10-30T07:43:46+00:00
No ledger device, just my pc. 

## dEBRUYNE-1 | 2018-10-30T14:46:04+00:00
Can you perhaps run the GUI as administrator to check whether it makes a difference? 

## ghost | 2018-10-30T14:57:19+00:00
I am having difficulties logging in to my wallet every time. I always get this error. I know the password is correct because I copy and past it from a document:

<img width="485" alt="2018-10-31" src="https://user-images.githubusercontent.com/14051589/47727252-d110fa00-dca7-11e8-90b6-179f0a66be2e.png">



## dEBRUYNE-1 | 2018-10-31T07:26:57+00:00
That's a bug present in GUI v0.13.0.3 (which will be fixed in GUI v0.13.0.4). You can temporarily use this workaround:

https://monero.stackexchange.com/questions/6611/cant-load-wallet-in-cli-v0-13-0-2-or-gui-v0-13-0-3-error-stdbad-alloc-err

## ghost | 2018-10-31T11:18:42+00:00
Hey I really appreciate all the support. I've decided to remove the software until stable and usable versions are available.

## dEBRUYNE-1 | 2018-10-31T19:27:26+00:00
Note that GUI v0.13.0.4, which will be out soon, should be relatively stable.

## mr-tron | 2019-02-21T12:01:03+00:00
Issue is still actual in monero v0.13.0.4

## selsta | 2019-02-21T12:02:21+00:00
@mr-tron Make sure to properly close your wallet.

## mr-tron | 2019-02-21T13:04:48+00:00
Yes. Via `x` in the windows right corner. Operational system ubuntu 18.04
On exit i see errors in stdout 
```
2019-02-21 11:44:03.314	    7f22d8f96700	ERROR	wallet.wallet2	src/wallet/wallet2.cpp:2020	!r. THROW EXCEPTION: error::no_connection_to_daemon
2019-02-21 11:44:03.315	    7f22db7fe700	ERROR	WalletAPI	src/wallet/api/wallet.cpp:973	daemonBlockChainTargetHeight: Failed to connect to daemon
2019-02-21 11:44:03.315	    7f22db7fe700	ERROR	WalletAPI	src/wallet/api/wallet.cpp:954	daemonBlockChainHeight: Failed to connect to daemon
```
But exit code is 0.

## mr-tron | 2019-02-22T07:46:22+00:00
It reproduces sometimes. Looks like problems when connected with forced wallet disconnecting.

# Action History
- Created by: ghost | 2018-10-30T04:43:07+00:00
- Closed at: 2018-11-02T09:51:09+00:00
