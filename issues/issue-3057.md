---
title: Error writing wallet from hardware device...
source_url: https://github.com/monero-project/monero-gui/issues/3057
author: epimazzo
assignees: []
labels: []
created_at: '2020-08-28T19:40:27+00:00'
updated_at: '2021-09-29T03:06:53+00:00'
type: issue
status: closed
closed_at: '2020-09-02T21:06:54+00:00'
---

# Original Description
Hey there,

I'm under the latest MacOS Catalina version running the latest 2.10.0 Ledger Live app and trying to create a new wallet from the hardware with Monero App client just downloaded. It fails all the time. I have a Nano S device.

ERROR:
 error writing wallet from a hardware device. Check the application logs.

Any idea how to fix it? 

Thanks for it.

# Discussion History
## selsta | 2020-08-28T19:50:04+00:00
What Ledger monero app version?

Also there should be an additional error message on the bottom of the screen, can you post it?

## epimazzo | 2020-08-28T20:28:51+00:00
> What Ledger monero app version?
> 
> Also there should be an additional error message on the bottom of the screen, can you post it?

Hey Selsta,
Thanks for coming by...

I've just downloaded the latest version from the Monero community website for MacOS 64Bits. Version is 0.16.0.3 (qt 5.12.8)
The bottom message is: Failed to generate new wallet. Unable to open device 4:11415

I'm connected to Ledger Live and logged in with my Nano unlocked showing up all crypto. Manager is also opened. 

Thanks.

## selsta | 2020-08-28T20:29:51+00:00
Please make sure that Ledger Live is closed when using Ledger + Monero, it can interfere. Also try to restart your computer.

## epimazzo | 2020-08-28T20:46:32+00:00
Now I got a different error in the bottom:

Failed to generate a new wallet. Wrong channel. MacBook was restarted. No extra app opened. 

Thanks

## selsta | 2020-08-28T21:02:02+00:00
Just to confirm:

- v0.16.0.3 GUI
- Firmware 1.6.1
- Monero Ledger app v1.6.0

? I also run latest MacOS Catalina so not sure what is going on here.

## epimazzo | 2020-08-28T21:12:33+00:00
All versions are equal than yours except my Ledger Live firmware which is 1.2.4-4

Monero is 1.6.0 and GUI is 0.16.0.3 

That was funny. ;-) 

## epimazzo | 2020-08-28T21:13:25+00:00
Which 1.6.1 firmware is this? 

## selsta | 2020-08-28T21:14:11+00:00
- Ledger Live 2.10.0
- Ledger firmware 1.6.1

## epimazzo | 2020-08-28T21:21:27+00:00
Hummmm..... mine is getting a different Firmware version. Do you have a Nano S? Cause that's what I have with this updated firmware on it. Just grab it from the update notification right after I had plugged in. :-) Our Ledger Live is the same. 

## selsta | 2020-08-28T21:22:54+00:00
You sure that you don’t have a Ledger Nano X? :) Though it should also work with Monero.

## epimazzo | 2020-08-28T21:35:59+00:00
Mine is a Nano X ledger. ;-) Sorry LOL! 

but it's using a different firmware version than you. 

## selsta | 2020-08-28T21:37:34+00:00
You have the correct firmware, S and X have different versioning.

Did you accept exporting the view key during wallet creation?

## epimazzo | 2020-08-29T02:32:54+00:00
Nope, not even get into this point. It fails right in the beginning while in the creation window. Sounds weird. It should work as expected. 

## selsta | 2020-08-29T02:35:49+00:00
Did you connect using bluetooth or USB?

## epimazzo | 2020-08-29T16:01:41+00:00
Connected through an USB Hub. My MacBook Pro is a 2019 15' with only usb-c input. 

## epimazzo | 2020-08-31T14:17:47+00:00
Hi Selsta,

No more clues ;-) can't figured out yet...

## selsta | 2020-08-31T14:19:02+00:00
Sorry, forgot to reply. At this point I suspect its the USB hub, maybe the USB library used (hidapi) does not play well together with it.

Do you have a Micro USB to USB-C cable to test this?

## epimazzo | 2020-08-31T14:36:03+00:00
No worries ;-) 
Unfortunately not. I'll try to borrow one USB-C cable. But Nano X has Bluetooth on it. Wouldn't work? I tried but it could be found too. LOL! 

## selsta | 2020-08-31T14:41:32+00:00
I’m not familiar with bluetooth + Ledger :)

## epimazzo | 2020-08-31T16:08:17+00:00
Yep..Bluetooth does not work at all. Meanwhile, I got this new error:

Failed to generate new wallet: Wrong device status. 0x6e00 (SW_CLA_NOT_SUPPORTED), EXPECTED 0x9000 (SW_OK), MASK 0xffff

## epimazzo | 2020-09-02T21:06:27+00:00
Hi Selsta,

I just figured out what was causing this issue and believe me; it was a simple step! 

The Monero App must be up and running in your ledger Nano X before the wallet is created. Otherwise, you get these errors. 

It's all clear now! 

Thanks for your help and support.



## selsta | 2020-09-02T21:15:24+00:00
Good to know for the future to ask this if someone has problems, thanks for the follow up.

## reanimat0r | 2021-09-29T03:06:53+00:00
> Hi Selsta,
> 
> I just figured out what was causing this issue and believe me; it was a simple step!
> 
> The Monero App must be up and running in your ledger Nano X before the wallet is created. Otherwise, you get these errors.
> 
> It's all clear now!
> 
> Thanks for your help and support.


Thank you for the heads up, brother. It helped me to get over the errors as well, so I could complete the Ledger X Setup! 



# Action History
- Created by: epimazzo | 2020-08-28T19:40:27+00:00
- Closed at: 2020-09-02T21:06:54+00:00
