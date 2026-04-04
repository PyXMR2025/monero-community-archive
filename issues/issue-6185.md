---
title: Monero Gui Linux x64 v0.15.0.1 no longer works with Trezor T
source_url: https://github.com/monero-project/monero/issues/6185
author: hiviah
assignees: []
labels: []
created_at: '2019-11-25T22:46:18+00:00'
updated_at: '2020-03-06T01:09:33+00:00'
type: issue
status: closed
closed_at: '2019-11-25T23:06:05+00:00'
---

# Original Description
Trezor account that was working with monero-gui-v0.14.1.0, does no longer work with 0.15.0.1.

Can't even create/restore wallet with 0.15. The 0.14 is still working, but displays that wrong package hash as mentioned in #6179.

Nothing specific about the why Trezor connection fails in logs:

    2019-11-25 22:44:22.046	    7f599cae6700	INFO	global	contrib/epee/src/net_ssl.cpp:127	Generating SSL certificate
    2019-11-25 22:44:22.137	    7f5992cfc700	WARNING	wallet.wallet2	src/wallet/wallet2.cpp:4192	Account on device. Initing device...
    2019-11-25 22:44:22.147	    7f5992cfc700	ERROR	WalletAPI	src/wallet/api/wallet.cpp:717	Error opening wallet: device not found: Trezor
    2019-11-25 22:44:22.161	    7f59b37887c0	ERROR	frontend	src/wallet/api/wallet.cpp:414	Error opening wallet with password:  device not found: Trezor
    2019-11-25 22:44:23.747	    7f59b37887c0	INFO	logging	contrib/epee/src/mlog.cpp:273	New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO
    2019-11-25 22:44:23.754	    7f5992cfc700	INFO	global	contrib/epee/src/net_ssl.cpp:127	Generating SSL certificate
    2019-11-25 22:44:23.838	    7f599cae6700	WARNING	wallet.wallet2	src/wallet/wallet2.cpp:4192	Account on device. Initing device...
    2019-11-25 22:44:23.838	    7f599cae6700	ERROR	WalletAPI	src/wallet/api/wallet.cpp:717	Error opening wallet: device not found: Trezor
    2019-11-25 22:44:23.845	    7f59b37887c0	ERROR	frontend	src/wallet/api/wallet.cpp:414	Error opening wallet with password:  device not found: Trezor
    2019-11-25 22:44:24.428	    7f59b37887c0	INFO	logging	contrib/epee/src/mlog.cpp:273	New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO
    2019-11-25 22:44:24.525	    7f5991cfa700	WARNING	wallet.wallet2	src/wallet/wallet2.cpp:4192	Account on device. Initing device...
    2019-11-25 22:44:24.525	    7f5991cfa700	ERROR	WalletAPI	src/wallet/api/wallet.cpp:717	Error opening wallet: device not found: Trezor
    2019-11-25 22:44:24.528	    7f59b37887c0	ERROR	frontend	src/wallet/api/wallet.cpp:414	Error opening wallet with password:  device not found: Trezor
    2019-11-25 22:44:25.107	    7f599cae6700	INFO	global	contrib/epee/src/net_ssl.cpp:127	Generating SSL certificate


# Discussion History
## selsta | 2019-11-25T22:56:15+00:00
See here: https://github.com/monero-project/monero-gui/issues/2479, the Linux GUI was accidentally compiled without Trezor support.

We will release GUI v0.15.0.2 in the next days to fix this. You can use GUI v0.14.1.0 or CLI v0.15.0.1 in the meantime if you need access to your funds.

## hiviah | 2019-11-25T23:06:05+00:00
OK, thanks.

## Engelberg | 2020-03-06T00:26:41+00:00
Did this regress in v0.15.0.4? I'm using v0.15.0.4 GUI and when I try to create a new Trezor-based wallet in 0.15.0.4, I get the error message:
```
failed to generate new wallet: device not found: Trezor
```
The Trezor never prompts for passphrase, as if it hasn't been contacted by the app.

The log doesn't show any Trezor-specific error message, just the QT binding loop error for property "implicitWidth" and no other errors.

Yes, this is a Trezor Model T, and yes it has been initialized, and yes the Trezor Bridge is installed, and yes it works with other apps. This is also on Ubuntu.

## selsta | 2020-03-06T00:27:45+00:00
@Engelberg Which OS are you using?

## Engelberg | 2020-03-06T00:28:02+00:00
Ubuntu

## selsta | 2020-03-06T00:30:10+00:00
It is possible that this regressed. Please continue using v0.15.0.1 or download v0.15.0.2, if this is broken it will get fixed with v0.15.0.5, but this will take 2 weeks or so. Alternatively you can compile v0.15.0.4 with Trezor support yourself.

## Engelberg | 2020-03-06T00:41:00+00:00
Thanks. I'm having trouble finding where to download older versions; can you point me in the right direction?

## selsta | 2020-03-06T00:44:38+00:00
https://www.reddit.com/r/Monero/comments/eaj3u6/gui_v01502_carbon_chamaeleon_released/ has download links.

## Engelberg | 2020-03-06T00:49:08+00:00
I can confirm that v0.15.0.2 works, so I think this is very likely a regression.

## selsta | 2020-03-06T01:09:32+00:00
Opened https://github.com/monero-project/monero-gui/pull/2796 so that this does not happen again in the future.

# Action History
- Created by: hiviah | 2019-11-25T22:46:18+00:00
- Closed at: 2019-11-25T23:06:05+00:00
