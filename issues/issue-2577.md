---
title: NanoX device not working for sending transfers.  In only
source_url: https://github.com/monero-project/monero-gui/issues/2577
author: taylormade2k
assignees: []
labels: []
created_at: '2019-12-08T23:46:34+00:00'
updated_at: '2021-06-29T03:05:58+00:00'
type: issue
status: closed
closed_at: '2021-06-29T03:05:58+00:00'
---

# Original Description
When I tray and send monero from my NanoX I get this spinning wheel that says "Creating transaction please check your hardware wallet your input may be required" This has been going for 15 minutes now. The nano does not appear to see the transaction request to take action.  

Troubleshooting.  Checked to make sure my nano x was updated to the latest version which is 1.2.4-1
Uninstalled all apps on nano and reinstalled BTC first then monero.



# Discussion History
## xiphon | 2019-12-09T10:54:54+00:00
What Monero app version is installed on the device?

## taylormade2k | 2019-12-09T16:23:16+00:00
Hi, Its v0.15.0.1 (Qt 5.9.7)

## xiphon | 2019-12-09T19:55:57+00:00
I mean the Ledeger Monero app version, the one you have installed on the device.

## taylormade2k | 2019-12-09T20:27:39+00:00
Ah Ok, Its App 1.4.2 Spec 1.0

## xiphon | 2019-12-09T23:44:32+00:00
Reproduced the issue once. But then i enabled the debug logs and i can't reproduce it again.

Could you please try to send the tx once again and wait for some minutes (5 mins should be okay) and report back?

## taylormade2k | 2019-12-10T01:01:50+00:00
Sure I will do that shortly. Should I enable debug logs? is that something i can do on my end?  Anyway will try and report back in the meantime. 

## xiphon | 2019-12-10T01:06:37+00:00
Try without the logs first, if the issue reproduces give it another run with log level 4.

## taylormade2k | 2019-12-10T02:13:13+00:00
Ok it worked after rrunning log level 4.  Before that same thing happened.  The infinite spin loop saying check your nano for further instructions.  I was able to transfer a test balance out.  It seemed a bit clunky asking me for my password multiple times but it worked, and I'm thankful for that.

## selsta | 2019-12-10T02:25:26+00:00
ping @cslashm

## cslashm | 2019-12-10T08:44:24+00:00
I never see that and I am not able to reproduce :-/

## selsta | 2021-06-29T03:05:58+00:00
Closing as a lot has changed since this issue was opened, including Ledger firmware updates.

# Action History
- Created by: taylormade2k | 2019-12-08T23:46:34+00:00
- Closed at: 2021-06-29T03:05:58+00:00
