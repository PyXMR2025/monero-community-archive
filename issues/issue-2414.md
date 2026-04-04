---
title: Error writing wallet from hardware device. Check application logs. ?
source_url: https://github.com/monero-project/monero-gui/issues/2414
author: gorenom
assignees: []
labels:
- resolved
created_at: '2019-10-11T00:22:41+00:00'
updated_at: '2019-11-11T23:00:40+00:00'
type: issue
status: closed
closed_at: '2019-11-11T23:00:40+00:00'
---

# Original Description
Hello, I've run into a snag trying to create a monero wallet with trezor.
Their support directed me here.

I followed the instructions here:
https://wiki.trezor.io/Monero_(XMR)#Monero_in_Trezor 

When I tried to create the hardware wallet (from device), I always got the following error message:
_Error writing wallet from hardware device. Check application logs. ?_

Can you help?
Thanks

# Discussion History
## xiphon | 2019-10-11T00:38:15+00:00
What OS do you use?

Edit: also there should be a error message on the GUI bottom, isn't it?

## gorenom | 2019-10-11T01:06:47+00:00
Thanks for the quick response!

1. I'm on Windows 10, 64 bit

2. There's no additional error message on the bottom.
Screenshot of the screen where I get the error message:
https://i.imgur.com/xgxv6dT.png

## xiphon | 2019-10-11T01:14:01+00:00
>     2\. There's no additional error message on the bottom.
>         Screenshot of the screen where I get the error message:
>         https://i.imgur.com/xgxv6dT.png

It should appear for 5 seconds right after you click on `Create wallet` button. Could you please check it?

## xiphon | 2019-10-11T01:16:29+00:00
>     1. I'm on Windows 10, 64 bit

GUI writes the log into `%APPDATA%\monero-wallet-gui\monero-wallet-gui.log`. Does it contain any Trezor-related error messages>



## gorenom | 2019-10-11T01:31:47+00:00
> It should appear for 5 seconds right after you click on Create wallet button. Could you please check it?

Ah, yes, it says:
"failed to generate new wallet: Cannot get a device address"

> GUI writes the log into %APPDATA%\monero-wallet-gui\monero-wallet-gui.log. Does it contain any Trezor-related error messages>

Yes, two lines I can discern:

WARNING	device.trezor.transport	src/device_trezor/trezor/transport.cpp:716	Reading from UDP socket failed: An existing connection was forcibly closed by the remote host
ERROR	device.trezor	src/device_trezor/device_trezor.cpp:174	Get public address exception: Trezor returned failure: code=1, message=Unknown message

## xiphon | 2019-10-11T01:39:32+00:00
Paging @ph4r05 

## selsta | 2019-10-11T11:29:50+00:00
Make sure the latest version of the Trezor firmware and Trezor bridge is installed.

## ph4r05 | 2019-10-11T13:31:30+00:00
It may be the case that your Trezor has not been initialized. Did you setup the Trezor via webwallet?


## rating89us | 2019-10-13T16:18:26+00:00
Must Trezor's first run (seed creating) be done through Trezor webwallet, or could it be done in a third party app (like Monero GUI/CLI)?

If it must be done through Trezor webwallet, then we could inform users on our GUI/CLI wallets.

## ph4r05 | 2019-10-13T16:32:00+00:00
The initialization must be done via webwallet, it is the only one supported mechanism. Trezor should inform on the setup procedure on the first start

## rating89us | 2019-10-14T20:47:20+00:00
> The initialization must be done via webwallet, it is the only one supported mechanism. Trezor should inform on the setup procedure on the first start

Actually no. Exodus desktop wallet can initialize a new Trezor device (https://support.exodus.io/article/1114-getting-started-with-exodus-and-trezor#new). 

Monero GUI should also be able to do it.

## ph4r05 | 2019-10-14T20:54:05+00:00
As far as I am aware the only official initialization is via officia webwallet.

Integration this to Monero codebase is not planned.

## ph4r05 | 2019-10-15T06:20:07+00:00
Also, the Trezor asks user to personalize the device after the first start so user should follow the official device guidelines (including proper backup) before using the device. 

Maintaining another init version is costly and error prone. From the mentioned reasons, we won’t support/recommend the init in Monero apps.

## selsta | 2019-11-11T22:57:39+00:00
Please comment if initializing didn’t resolve your issue.

+resolved

# Action History
- Created by: gorenom | 2019-10-11T00:22:41+00:00
- Closed at: 2019-11-11T23:00:40+00:00
