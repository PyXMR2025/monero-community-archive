---
title: Getting wrong device error with the ledger (0x6a30 expected 0x9000
source_url: https://github.com/monero-project/monero-gui/issues/3154
author: Belfor-IT
assignees: []
labels: []
created_at: '2020-10-13T22:02:50+00:00'
updated_at: '2020-10-16T23:07:24+00:00'
type: issue
status: closed
closed_at: '2020-10-16T23:06:47+00:00'
---

# Original Description
Hi, 

I'm getting the wrong device error when I try to log in on my GUI Monero wallet on windows 10 with my ledger. 
Error message"Wrong device status 0x6a30 (unknown)EXPECTED 0x9000 (SW_OK), MASK 0xffff"



# Discussion History
## selsta | 2020-10-13T22:16:49+00:00
Do you have some Anti Virus on your system?

## xiphon | 2020-10-13T22:33:28+00:00
Ledger Monero app version is not compatible with the Monero GUI version. Check for updates.

## Belfor-IT | 2020-10-13T22:41:35+00:00
> Ledger Monero app version is not compatible with the Monero GUI version. Check for updates.

I already was using ledger nano S with the Monero Wallet.. was working fine 

## selsta | 2020-10-13T22:42:07+00:00
Did you update Monero GUI? If yes, please also update Ledger monero app to v.1.7.x

## Belfor-IT | 2020-10-13T22:42:40+00:00
> Ledger Monero app version is not compatible with the Monero GUI version. Check for updates.



> Do you have some Anti Virus on your system?
Yes, but I white listed monero

## Belfor-IT | 2020-10-13T22:54:30+00:00
> Did you update Monero GUI? If yes, please also update Ledger monero app to v.1.7.x
I have updated my Monero GUI and Ledger app V1.7.3 still getting the wrong Device but now  "SW-CLA_NOT_SUPPORTED" status 0x6e00 EXPECTED 0x9000


## selsta | 2020-10-13T22:56:19+00:00
And you used Monero GUI v0.17.0.1 ?

## Belfor-IT | 2020-10-13T23:13:36+00:00
> And you used Monero GUI v0.17.0.1 ?

Yes! 

## selsta | 2020-10-16T22:49:36+00:00
Please try again with v0.17.1.0 and Ledger app v1.7.4 and make sure that Ledger Live is closed.

## Belfor-IT | 2020-10-16T23:07:24+00:00
It's working again! 


# Action History
- Created by: Belfor-IT | 2020-10-13T22:02:50+00:00
- Closed at: 2020-10-16T23:06:47+00:00
