---
title: Failure to Generate Ledger Wallet on Windows 7
source_url: https://github.com/monero-project/monero/issues/4187
author: TheRealDarkhorse702
assignees: []
labels: []
created_at: '2018-07-29T06:18:53+00:00'
updated_at: '2018-10-20T19:24:53+00:00'
type: issue
status: closed
closed_at: '2018-10-20T19:24:53+00:00'
---

# Original Description
Has anyone been able to generate a ledger wallet on Windows 7 . I haven't been able to since 12.2.0 was released.

I am using the command:

monero-wallet-cli.exe --log-level 4 --generate-from-device WalletName --subaddress-lookahead 3:200

2018-07-18 04:02:54.980	10288	ERROR	device.ledger	src/device/device_ledger.cpp:426 Fail SCard API : (-2146435026) 0x8010002E Device=0, hCard=0, hContext=14771806782070194176

2018-07-18 04:02:54.980	10288	ERROR	msgwriter src/common/scoped_message_writer.h:102	Error: failed to generate new wallet: Fail SCard API : (-2146435026) 0x8010002E Device=0, hCard=0, hContext=14771806782070194176

2018-07-18 04:02:54.990	10288	ERROR	wallet.simplewallet src/simplewallet/simplewallet.cpp:2980	account creation failed

2018-07-18 04:02:54.990	10288	ERROR	wallet.simplewallet src/simplewallet/simplewallet.cpp:7566	Failed to initialize wallet

I believe SCardListReaders is returning 0x8010002E, Group contains no readers.

https://github.com/monero-project/monero/blob/master/src/device/device_ledger.cpp

#ifdef SCARD_AUTOALLOCATE

dwReaders = SCARD_AUTOALLOCATE;

rv = SCardListReaders(this->hContext, NULL, (LPSTR)&mszReaders, &dwReaders);

#else

dwReaders = 0;

rv = SCardListReaders(this->hContext, NULL, NULL, &dwReaders);

if (rv != SCARD_S_SUCCESS) return false;

mszReaders = (LPSTR)calloc(dwReaders, sizeof(char));

rv = SCardListReaders(this->hContext, NULL, mszReaders, &dwReaders);

#endif

I could pull the repo and search it to see if the SCARD_AUTOALLOCATE compile option is being used.

From my understanding the device has to be connected/active and be listed under

HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Cryptography\Calais\ Readers

I have no driver errors in the device manager, but I notice when entering the Monero app the device disconnects and reconnects.

But just because the error is visible on the Monero Software side doesn't mean the ledger app is not the root cause.

On (https://github.com/LedgerHQ/blue-app-monero) they have listed

Revision
v 0.12.4 / Beta 5
Targeted Client: Monero 0.12.1

U2F support

Fix Windows detection problem

activate Mainnet 'Beta stage: USE AT YOUR OWN RISK'

I am hoping "Fix Windows detection problem" is the issue I have been experiencing.

# Discussion History
## dEBRUYNE-1 | 2018-07-29T09:03:12+00:00
Paging @cslashm.

## dEBRUYNE-1 | 2018-07-30T10:08:00+00:00
Perhaps this report benefits you? 

https://www.reddit.com/r/Monero/comments/925q5m/gui_v01230_with_direct_ledger_support_released/e39hhfw/?context=3

## cslashm | 2018-07-30T13:05:28+00:00
I work on a PCSC alternative. 

## TheRealDarkhorse702 | 2018-07-31T04:12:34+00:00
Okay, I finally figured it out. I had to update the driver in an unusual way and the device manger never showed an error, so finding this solution wasn't intuitive.

In the device manager, under Universal Serial Bus controllers, one of the drivers the ledger will show up as is a USB Composite Device. Go to update the driver, but when doing so, search for the driver under C:\Windows\winsxs. After doing this the device should show up under Smart card readers as a Microsoft Usbccid Smartcard Reader (WUDF).

## moneromooo-monero | 2018-10-20T19:00:59+00:00
The ledger code now uses blihidapi rather than libpcsc, so this is moot, it should now work.

+resolved

# Action History
- Created by: TheRealDarkhorse702 | 2018-07-29T06:18:53+00:00
- Closed at: 2018-10-20T19:24:53+00:00
