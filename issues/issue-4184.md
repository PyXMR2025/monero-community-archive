---
title: Ledger Nano S not found, Fedora Linux
source_url: https://github.com/monero-project/monero/issues/4184
author: conclusionmurray
assignees: []
labels: []
created_at: '2018-07-27T18:12:36+00:00'
updated_at: '2018-08-06T18:47:08+00:00'
type: issue
status: closed
closed_at: '2018-07-29T12:06:54+00:00'
---

# Original Description
f77bb740	ERROR	default	src/device/device.cpp:60	device not found in registry: 'Ledger'

when creating wallet, gui and cli

# Discussion History
## moneromooo-monero | 2018-07-27T20:11:23+00:00
You built it yourself, and without building ledger in, didn't you ?
If so, build again, making sure ledger is built in. Check the output by cmake. It needs libpcsc-lite at least.


## conclusionmurray | 2018-07-27T22:14:32+00:00
I downloaded the latest release, should have mentioned that. I tried the x64 version cli and that gave me; Error: failed to generate new wallet: Fail SCard API : (2148532253) Service not available. Device=0, hCard=0, hContext=0

I can try to compile it myself. The ledger is working with ledger live and other applications (tronscan)

## moneromooo-monero | 2018-07-28T00:06:48+00:00
That's odd, this'd mean those binaries were built without ledger support. I'll ask around.

## dEBRUYNE-1 | 2018-07-28T09:04:49+00:00
@conclusionmurray - Have you properly followed all sufficiently prepared steps (i.e. the 5 steps after "We first have to ensure that we're sufficiently prepared. This entails the following:")?

https://monero.stackexchange.com/questions/8503/how-do-i-generate-a-ledger-monero-wallet-with-the-cli-monero-wallet-cli

## sedited | 2018-07-28T09:09:26+00:00
@conclusionmurray what is the output, if you run `pcsc_scan` in the terminal? 

## conclusionmurray | 2018-07-29T06:35:44+00:00
@TheCharlatan
 Reader 0: Ledger Nano S [Nano S] (0001) 00 00
  Card state: Card inserted
@dEBRUYNE-1 you did not derive that from my previous statement that I have the ledger working with other apps? I followed https://monero.stackexchange.com/questions/8695/how-do-i-on-windows-generate-a-ledger-monero-wallet-with-the-cli-and-subsequen (were the only interesting info is the command line options)


## dEBRUYNE-1 | 2018-07-29T09:06:08+00:00
@conclusionmurray - The "sufficiently prepared" steps can differ for other coins. For instance, for Bitcoin on Linux, it's simply plug-and-play as far as I know, whereas for Monero you have to go follow some technical steps first in order to ensure it works properly. 

> I followed https://monero.stackexchange.com/questions/8695/how-do-i-on-windows-generate-a-ledger-monero-wallet-with-the-cli-and-subsequen (were the only interesting info is the command line options)

This is the Windows guide. Have you looked at the Linux guide (which differs)?

https://monero.stackexchange.com/a/8700/44

In addition, please see this SE answer, which is specific to Fedora:

https://monero.stackexchange.com/a/9883/44

## conclusionmurray | 2018-07-29T10:39:25+00:00
@dEBRUYNE-1 thank you for the second link, it complements @TheCharlatan post asking for a pcsc_scan result. pcscd is not installed by default on Fedora so I installed that and started the service.

Looking at your second link I can confirm the settings are there although the 
`<key>ifdFriendlyName</key>` has the value `<string>Ledger Nano S</string>`. Since the error is; `cannot find 'Ledger' in the registry` I changed the value to that and restarted the service. same error, change it to `'Ledger Token'` for good measure, no change.

I am very familiar with the nano and can tell you that there are no suprises when it comes to using monero. The 'sufficiently prepared' steps are equevilent to "have you unboxed your modem", "here is how to connect a power cord". 

https://gist.github.com/ptantiku/e53eaae96e5503a77774636b1f948424
Is required to get the device recognized for fedora, and if you look closely you see that the udev rules that ledgerwallet provides has a nonexistent user under fedora, hence the sed to whoami.
pcscd is not required for other applications (Tronscan and Ledger live (and previously chrome apps) ) to function, reading the information it is not clear to me that it is for the Monero app to interface with the ledger hardware.

edit: formatting. removed simplEOS (does not work with ledger)

## moneromooo-monero | 2018-07-29T11:01:42+00:00
Somthing that seems really odd to me is that the "device not found in registry" and "Fail SCard API : (2148532253) Service not available." logs seem to be impossible to get at the same time. Please post the actual log (level 1,device\*:TRACE). From the log file, not from the console.

## conclusionmurray | 2018-07-29T12:06:54+00:00
@moneromooo-monero I realised that one error came from the x64 and I have continued with the x86.
I tried, realising I have the service installed and running, and it is currently generating my wallet.

This would mean my problem is solved by installing pcsc-tools and starting pcscd and using the x64 version. I did try the command line option to start with so I will be using that wallet with the gui.

## joshpurvis | 2018-08-06T18:44:29+00:00
Just wanted to drop a comment here for future searchers who land on this issue...

I was running into very similar problems on Manjaro Linux, I tried what @conclusionmurray suggested with `pcscd`, but no success. `pcsc_scan` was failing to detect the device, and when I ran `pcscd` in debug mode (using `pcscd -fd`), it said:

```
00000062 hotplug_libudev.c:729:HPRegisterForHotplugEvents() No bundle files in pcsc drivers directory: /usr/lib/pcsc/drivers
00000006 hotplug_libudev.c:730:HPRegisterForHotplugEvents() Disabling USB support for pcscd
```

I finally solved the problem by installing the latest `ccid` package (ccid-1.4.29-3-x86_64)

This is what tipped me off to the `ccid` package might needing updated: https://github.com/LudovicRousseau/pcsc-tools/issues/4

# Action History
- Created by: conclusionmurray | 2018-07-27T18:12:36+00:00
- Closed at: 2018-07-29T12:06:54+00:00
